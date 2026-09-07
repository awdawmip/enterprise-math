"""Opportunistic BRC shortcuts: cheap probes, exact fallback, local telemetry.

Heuristics in this module only change trial order/prefix.  Complete multiplier
orders always append the exact mod-8 structural fallback, so a miss cannot
change final mathematical coverage.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from functools import lru_cache
from typing import Iterable, Mapping, Sequence

from .brc_multiplier_priority_jump import (
    odd_n_multiplier_is_scan_irredundant,
    prioritized_odd_multiplier_order,
)


class ShortcutSafety(str, Enum):
    EXACT = "EXACT"
    HEURISTIC_FALLBACK = "HEURISTIC_FALLBACK"
    CONDITIONAL_EXACT = "CONDITIONAL_EXACT"


class ShortcutCost(str, Enum):
    TINY = "TINY"
    CHEAP = "CHEAP"
    MODERATE = "MODERATE"
    EXPENSIVE = "EXPENSIVE"


@dataclass(frozen=True, slots=True)
class ShortcutSpec:
    shortcut_id: str
    name: str
    family: str
    safety: ShortcutSafety
    probe_cost: ShortcutCost
    default_enabled: bool
    trigger: str
    fallback: str
    evidence: str
    source_refs: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class ShortcutContext:
    n_bits: int
    max_multiplier: int = 100
    expected_transitions: int = 0
    states_materialized: bool = False
    memory_constrained: bool = False
    pisano_period_available: bool = False
    likely_moderate_factor_imbalance: bool = False
    gap_filter_dominates: bool = False
    shadow_tag: str = ""

    def __post_init__(self) -> None:
        if self.n_bits <= 0 or self.max_multiplier <= 0:
            raise ValueError("n_bits/max_multiplier must be positive")
        if self.expected_transitions < 0:
            raise ValueError("expected_transitions must be non-negative")


@dataclass(frozen=True, slots=True)
class ShortcutTrial:
    shortcut_id: str
    reason: str
    max_probe_candidates: int | None = None


@dataclass(slots=True)
class ShortcutStats:
    attempts: int = 0
    hits: int = 0
    total_probe_cost: float = 0.0
    total_saved_cost: float = 0.0

    @property
    def empirical_hit_rate(self) -> float:
        return self.hits / self.attempts if self.attempts else 0.0

    @property
    def expected_net_saving(self) -> float:
        return (
            (self.total_saved_cost - self.total_probe_cost) / self.attempts
            if self.attempts else 0.0
        )


@dataclass(slots=True)
class ShortcutLedger:
    stats: dict[str, ShortcutStats] = field(default_factory=dict)

    def record(
        self, shortcut_id: str, *, hit: bool, probe_cost: float, saved_cost: float
    ) -> None:
        if probe_cost < 0 or saved_cost < 0:
            raise ValueError("costs must be non-negative")
        item = self.stats.setdefault(shortcut_id, ShortcutStats())
        item.attempts += 1
        item.hits += int(hit)
        item.total_probe_cost += probe_cost
        item.total_saved_cost += saved_cost

    def ranking(self) -> tuple[tuple[str, float, int], ...]:
        return tuple(sorted(
            ((k, v.expected_net_saving, v.attempts) for k, v in self.stats.items()),
            key=lambda x: (-x[1], -x[2], x[0]),
        ))

    def to_dict(self) -> dict[str, dict[str, float | int]]:
        return {k: {
            "attempts": v.attempts, "hits": v.hits,
            "total_probe_cost": v.total_probe_cost,
            "total_saved_cost": v.total_saved_cost,
        } for k, v in sorted(self.stats.items())}

    @classmethod
    def from_dict(cls, payload: Mapping[str, Mapping[str, float | int]]) -> "ShortcutLedger":
        out = cls()
        for k, v in payload.items():
            out.stats[k] = ShortcutStats(
                int(v.get("attempts", 0)), int(v.get("hits", 0)),
                float(v.get("total_probe_cost", 0.0)),
                float(v.get("total_saved_cost", 0.0)),
            )
        return out


LEARNED_COVER_PREFIX = (
    1,48,96,8,15,80,21,16,56,45,35,3,72,7,99,88,40,55,9,24,
)
RATIO_COVER_PREFIX = (
    1,96,75,45,56,99,72,33,63,55,87,39,21,29,64,48,51,69,15,81,
)
SQUAREFREE_KERNEL13 = (1,13,14,3,15,2,5,6,30,22,105,33,7)
LOW12_COMPACT_MODULI = (4096, 3465, 221, 12673)


def squarefree_kernel(value: int) -> int:
    if value <= 0:
        raise ValueError("value must be positive")
    remaining, kernel, p = value, 1, 2
    while p * p <= remaining:
        e = 0
        while remaining % p == 0:
            remaining //= p
            e += 1
        if e & 1:
            kernel *= p
        p = 3 if p == 2 else p + 2
    return kernel * remaining if remaining > 1 else kernel


def _dedup_complete(prefix: Iterable[int], *, max_multiplier: int) -> tuple[int, ...]:
    fallback = prioritized_odd_multiplier_order(max_multiplier)
    seen: set[int] = set()
    out: list[int] = []
    for m in prefix:
        if (1 <= m <= max_multiplier and
            odd_n_multiplier_is_scan_irredundant(m) and m not in seen):
            out.append(m); seen.add(m)
    for m in fallback:
        if m not in seen:
            out.append(m); seen.add(m)
    if set(out) != set(fallback):
        raise AssertionError("specialist order changed scan coverage")
    return tuple(out)


def structural_order(max_multiplier: int = 100) -> tuple[int, ...]:
    return prioritized_odd_multiplier_order(max_multiplier)


def learned_cover_order(max_multiplier: int = 100) -> tuple[int, ...]:
    return _dedup_complete(LEARNED_COVER_PREFIX, max_multiplier=max_multiplier)


def ratio_cover_order(max_multiplier: int = 100) -> tuple[int, ...]:
    return _dedup_complete(RATIO_COVER_PREFIX, max_multiplier=max_multiplier)


def kernel13_prefix(max_multiplier: int = 1000) -> tuple[int, ...]:
    selected = set(SQUAREFREE_KERNEL13)
    return tuple(
        m for m in range(1, max_multiplier + 1)
        if odd_n_multiplier_is_scan_irredundant(m)
        and squarefree_kernel(m) in selected
    )


def kernel13_order(max_multiplier: int = 1000) -> tuple[int, ...]:
    return _dedup_complete(kernel13_prefix(max_multiplier), max_multiplier=max_multiplier)


def gap_sorted_order_from_materialized_states(
    completion_gap_by_multiplier: Mapping[int, int], *, max_multiplier: int = 100
) -> tuple[int, ...]:
    fallback = prioritized_odd_multiplier_order(max_multiplier)
    missing = set(fallback) - set(completion_gap_by_multiplier)
    if missing:
        raise ValueError(f"missing materialized gaps: {sorted(missing)[:8]}")
    rank = {m: i for i, m in enumerate(fallback)}
    return tuple(sorted(
        fallback,
        key=lambda m: (completion_gap_by_multiplier[m], rank[m]),
    ))


def brc_shadow_signature(
    n: int, root: int, remainder: int, *, modulus: int = 64
) -> str:
    if n <= 0 or root < 0 or remainder < 0 or modulus <= 1:
        raise ValueError("invalid BRC shadow input")
    if root * root + remainder != n or remainder > 2 * root:
        raise ValueError("root/remainder must reconstruct a valid BRC state")
    phase = min(3, (4 * remainder) // (2 * root + 1))
    return f"M{modulus}:N{n%modulus}:J{root%modulus}:R{remainder%modulus}:Q{phase}"


@lru_cache(maxsize=None)
def _square_residue_bitset(modulus: int) -> bytes:
    table = bytearray((modulus + 7) // 8)
    for x in range(modulus // 2 + 1):
        r = (x * x) % modulus
        table[r >> 3] |= 1 << (r & 7)
    return bytes(table)


def _table_has(table: bytes, r: int) -> bool:
    return bool(table[r >> 3] & (1 << (r & 7)))


def passes_low12_compact_square_filter(value: int) -> bool:
    if value < 0:
        raise ValueError("value must be non-negative")
    if not _table_has(_square_residue_bitset(4096), value & 4095):
        return False
    for m in LOW12_COMPACT_MODULI[1:]:
        r = value % m
        if not _table_has(_square_residue_bitset(m), r):
            return False
    return True


def low12_compact_raw_table_bytes() -> int:
    return sum(len(_square_residue_bitset(m)) for m in LOW12_COMPACT_MODULI)


def regime_key(context: ShortcutContext) -> str:
    b = context.n_bits
    bb = "<256" if b < 256 else "256-1023" if b < 1024 else \
         "1024-4095" if b < 4096 else "4096-8191" if b < 8192 else \
         "8192-32767" if b < 32768 else ">=32768"
    h = context.expected_transitions
    hb = "<64" if h < 64 else "64-255" if h < 256 else \
         "256-4095" if h < 4096 else ">=4096"
    parts = [bb, hb,
        f"mat{int(context.states_materialized)}",
        f"mem{int(context.memory_constrained)}",
        f"imb{int(context.likely_moderate_factor_imbalance)}",
        f"gap{int(context.gap_filter_dominates)}",
        f"pis{int(context.pisano_period_available)}",
    ]
    if context.shadow_tag:
        parts.append(f"shadow={context.shadow_tag}")
    return "|".join(parts)


@dataclass(slots=True)
class RegimeShortcutLedger:
    regimes: dict[str, ShortcutLedger] = field(default_factory=dict)

    def record(self, context: ShortcutContext, shortcut_id: str, *,
               hit: bool, probe_cost: float, saved_cost: float) -> None:
        self.regimes.setdefault(regime_key(context), ShortcutLedger()).record(
            shortcut_id, hit=hit, probe_cost=probe_cost, saved_cost=saved_cost
        )

    def ranking(self, context: ShortcutContext) -> tuple[tuple[str, float, int], ...]:
        ledger = self.regimes.get(regime_key(context))
        return ledger.ranking() if ledger else ()

    def to_dict(self) -> dict[str, dict[str, dict[str, float | int]]]:
        return {k: v.to_dict() for k, v in sorted(self.regimes.items())}


def multiplier_probe_batches(
    *, max_multiplier: int = 100, include_ratio_specialist: bool = False,
    include_kernel_specialist: bool = False, quantum: int = 4
) -> tuple[tuple[str, tuple[int, ...]], ...]:
    if max_multiplier <= 0 or quantum <= 0:
        raise ValueError("max_multiplier/quantum must be positive")
    streams: list[tuple[str, tuple[int, ...]]] = [
        ("structural_priority", structural_order(max_multiplier)),
        ("learned_cover_prefix", tuple(
            m for m in LEARNED_COVER_PREFIX
            if m <= max_multiplier and odd_n_multiplier_is_scan_irredundant(m)
        )),
    ]
    if include_ratio_specialist:
        streams.append(("ratio_cover_prefix", tuple(
            m for m in RATIO_COVER_PREFIX
            if m <= max_multiplier and odd_n_multiplier_is_scan_irredundant(m)
        )))
    if include_kernel_specialist and max_multiplier >= 128:
        streams.append(("kernel13_prefix", kernel13_prefix(max_multiplier)))

    cursors = [0] * len(streams)
    seen: set[int] = set()
    batches: list[tuple[str, tuple[int, ...]]] = []
    while True:
        advanced = False
        for i, (name, stream) in enumerate(streams):
            picked: list[int] = []
            while cursors[i] < len(stream) and len(picked) < quantum:
                m = stream[cursors[i]]; cursors[i] += 1
                if m in seen:
                    continue
                seen.add(m); picked.append(m)
            if picked:
                batches.append((name, tuple(picked))); advanced = True
        if all(cursors[i] >= len(streams[i][1]) for i in range(1, len(streams))):
            break
        if not advanced:
            break
    fallback = tuple(m for m in structural_order(max_multiplier) if m not in seen)
    if fallback:
        batches.append(("structural_fallback", fallback)); seen.update(fallback)
    if seen != set(structural_order(max_multiplier)):
        raise AssertionError("round-robin portfolio is not scan complete")
    return tuple(batches)


def flatten_probe_batches(
    batches: Sequence[tuple[str, Sequence[int]]],
) -> tuple[int, ...]:
    seen: set[int] = set(); out: list[int] = []
    for _, batch in batches:
        for m in batch:
            if m in seen:
                raise ValueError(f"duplicate multiplier: {m}")
            seen.add(m); out.append(m)
    return tuple(out)


SHORTCUT_SPECS = (
    ShortcutSpec("structural_priority","same-parity structural priority","multiplier_order",
        ShortcutSafety.HEURISTIC_FALLBACK,ShortcutCost.TINY,True,
        "odd-N multiplier scan","exact mod-8 candidate set retained",
        "Repeated finite rank/runtime benefit",("research_notes/BRC_MULTIPLIER_PRIORITY_JUMP_20260906.md",)),
    ShortcutSpec("learned_cover_prefix","learned 20-multiplier prefix","multiplier_order",
        ShortcutSafety.HEURISTIC_FALLBACK,ShortcutCost.TINY,True,
        "expensive candidate evaluation","append structural fallback",
        "Held-out rank improved; original CPython runtime slightly worse",("conversation 2026-09-06",)),
    ShortcutSpec("ratio_cover_prefix","log-ratio specialist prefix","multiplier_order",
        ShortcutSafety.HEURISTIC_FALLBACK,ShortcutCost.TINY,False,
        "moderate factor-imbalance signal","append structural fallback",
        "Overall worse; q/p in [2,4] diagnostic band improved",("conversation 2026-09-06",)),
    ShortcutSpec("kernel13_prefix","13-kernel early probe","multiplier_prefix",
        ShortcutSafety.HEURISTIC_FALLBACK,ShortcutCost.CHEAP,True,
        "long multiplier horizon","scan remaining exact representatives",
        "98 multipliers: training 100%, shifted full-hit recall 84.76% / 55.27%",
        ("research_artifacts/brc_squarefree_kernel_compression_probe_20260907.csv",)),
    ShortcutSpec("gap_sort_if_materialized","gap sort on existing states","multiplier_order",
        ShortcutSafety.HEURISTIC_FALLBACK,ShortcutCost.CHEAP,False,
        "states already materialized","same complete set",
        "Strong rank gain; lost runtime only when materialization was done for sorting",()),
    ShortcutSpec("low12_compact_gap_filter","LOW12 compact square filter","filter_backend",
        ShortcutSafety.EXACT,ShortcutCost.CHEAP,False,
        "gap filtering dominates","BALANCED cascade",
        "Zero false negatives; filter-level large-bit win in Round-14 prototype",()),
    ShortcutSpec("table_free_tail","certified table-free tail","transport_backend",
        ShortcutSafety.CONDITIONAL_EXACT,ShortcutCost.MODERATE,False,
        "memory constrained","ordinary predictor/direct root",
        "Storage win, not CPython CPU win",("research_notes/BRC_TABLE_FREE_TAIL_20260907.md",)),
    ShortcutSpec("quotient_jet_large_bits","quotient/remainder jet","transport_backend",
        ShortcutSafety.CONDITIONAL_EXACT,ShortcutCost.MODERATE,True,
        "large long tail","native division on smaller inputs",
        "Finite crossover around 4096 bits",("research_notes/BRC_QUOTIENT_JET_TAIL_20260907.md",)),
    ShortcutSpec("energy_jet_very_large_bits","energy difference jet","transport_backend",
        ShortcutSafety.CONDITIONAL_EXACT,ShortcutCost.MODERATE,True,
        "very large long tail","fresh product below crossover",
        "Finite gain at 8192/16384 bits",("research_notes/BRC_ENERGY_DIFFERENCE_JET_TAIL_20260907.md",)),
    ShortcutSpec("gap_residue_jet_ultralarge","completion-gap residue jet","filter_backend",
        ShortcutSafety.CONDITIONAL_EXACT,ShortcutCost.MODERATE,False,
        "ultra-large long filter-dominated stream","native staged modulo",
        "Prototype crossover only in tens-of-thousands-bit regime",()),
    ShortcutSpec("brc_shadow_telemetry","N/J/R/phase shadow tag","telemetry",
        ShortcutSafety.EXACT,ShortcutCost.TINY,False,
        "outcome logging","no routing unless evidence emerges",
        "Old classifier failed; exact observables retained for hidden-regime discovery",()),
    ShortcutSpec("fibonacci_delete_storage_probe","Fibonacci/delete storage compression","cross_family_storage",
        ShortcutSafety.HEURISTIC_FALLBACK,ShortcutCost.CHEAP,False,
        "representation/table compression","binary/BRC representation",
        ">90% bounded storage compression; little semiprime leakage",()),
    ShortcutSpec("pisano_metadata_probe","Pisano/rank metadata probe","cross_family_metadata",
        ShortcutSafety.CONDITIONAL_EXACT,ShortcutCost.TINY,False,
        "Pisano/rank metadata already available","ordinary exact factor pipeline",
        "Strong local reduction when metadata setup cost is already sunk",()),
)
SHORTCUT_BY_ID = {s.shortcut_id: s for s in SHORTCUT_SPECS}


def opportunistic_trial_plan(context: ShortcutContext) -> tuple[ShortcutTrial, ...]:
    trials = [
        ShortcutTrial("structural_priority","cheap robust baseline"),
        ShortcutTrial("learned_cover_prefix","cheap held-out-rank specialist",
                      min(20, context.max_multiplier)),
    ]
    if context.max_multiplier >= 128:
        trials.append(ShortcutTrial("kernel13_prefix","bounded long-horizon prefix",
                                    len(kernel13_prefix(context.max_multiplier))))
    if context.states_materialized:
        trials.append(ShortcutTrial("gap_sort_if_materialized","materialization cost already sunk"))
    if context.likely_moderate_factor_imbalance:
        trials.append(ShortcutTrial("ratio_cover_prefix","[2,4]-band specialist",
                                    min(20, context.max_multiplier)))
    if context.memory_constrained:
        trials.append(ShortcutTrial("table_free_tail","storage pressure"))
    if context.expected_transitions >= 256 and context.n_bits >= 4096:
        trials.append(ShortcutTrial("quotient_jet_large_bits","past finite crossover"))
    if context.expected_transitions >= 256 and context.n_bits >= 8192:
        trials.append(ShortcutTrial("energy_jet_very_large_bits","past finite crossover"))
    if context.gap_filter_dominates:
        trials.append(ShortcutTrial("low12_compact_gap_filter","filter is hot"))
    if (context.expected_transitions >= 4000 and context.n_bits >= 32768
        and context.gap_filter_dominates):
        trials.append(ShortcutTrial("gap_residue_jet_ultralarge","amortizable ultra-large route"))
    if context.pisano_period_available:
        trials.insert(0, ShortcutTrial("pisano_metadata_probe","metadata setup already sunk"))
    return tuple(trials)


def adaptive_trial_plan(
    context: ShortcutContext, ledger: RegimeShortcutLedger | None = None,
    *, min_attempts: int = 5
) -> tuple[ShortcutTrial, ...]:
    if min_attempts <= 0:
        raise ValueError("min_attempts must be positive")
    base = list(opportunistic_trial_plan(context))
    if ledger is None:
        return tuple(base)
    observed = {k: (v, n) for k, v, n in ledger.ranking(context)}
    def key(item: tuple[int, ShortcutTrial]) -> tuple[int, float, int]:
        i, trial = item
        net, n = observed.get(trial.shortcut_id, (0.0, 0))
        if n < min_attempts: return (1, 0.0, i)
        if net > 0: return (0, -net, i)
        return (2, -net, i)
    return tuple(t for _, t in sorted(enumerate(base), key=key))


__all__ = [
    "ShortcutSafety","ShortcutCost","ShortcutSpec","ShortcutContext","ShortcutTrial",
    "ShortcutStats","ShortcutLedger","RegimeShortcutLedger","LEARNED_COVER_PREFIX",
    "RATIO_COVER_PREFIX","SQUAREFREE_KERNEL13","LOW12_COMPACT_MODULI",
    "SHORTCUT_SPECS","SHORTCUT_BY_ID","squarefree_kernel","structural_order",
    "learned_cover_order","ratio_cover_order","kernel13_prefix","kernel13_order",
    "gap_sorted_order_from_materialized_states","brc_shadow_signature",
    "passes_low12_compact_square_filter","low12_compact_raw_table_bytes",
    "regime_key","multiplier_probe_batches","flatten_probe_batches",
    "opportunistic_trial_plan","adaptive_trial_plan",
]
