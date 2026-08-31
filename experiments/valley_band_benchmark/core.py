"""Independent valley/CFRAC relation engine and rank-aware linear algebra.

Derived only from the frozen packet and elementary continued-fraction algebra.
No source prototype or source conversation was used.
"""

from __future__ import annotations

import hashlib
import json
import math
import time
import tracemalloc
from collections import defaultdict, deque
from dataclasses import dataclass, field
from typing import Callable, Iterable

from corpus import is_prime


MAX_SAFE_BAND_WIDTH = 100_000


def primes_up_to(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        sieve[0] = 0
    if limit >= 1:
        sieve[1] = 0
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            sieve[p * p : limit + 1 : p] = b"\x00" * (((limit - p * p) // p) + 1)
    return [i for i, flag in enumerate(sieve) if flag]


def legendre(a: int, p: int) -> int:
    if p == 2:
        return a & 1
    value = pow(a % p, (p - 1) // 2, p)
    return -1 if value == p - 1 else value


def tonelli_shanks(n: int, p: int) -> int | None:
    n %= p
    if p == 2:
        return n
    if n == 0:
        return 0
    if legendre(n, p) != 1:
        return None
    if p % 4 == 3:
        return pow(n, (p + 1) // 4, p)
    q, s = p - 1, 0
    while q % 2 == 0:
        s += 1
        q //= 2
    z = 2
    while legendre(z, p) != -1:
        z += 1
    m = s
    c = pow(z, q, p)
    t = pow(n, q, p)
    r = pow(n, (q + 1) // 2, p)
    while t != 1:
        i, t2 = 1, t * t % p
        while i < m and t2 != 1:
            t2 = t2 * t2 % p
            i += 1
        if i == m:
            return None
        b = pow(c, 1 << (m - i - 1), p)
        r = r * b % p
        t = t * b * b % p
        c = b * b % p
        m = i
    return r


def factor_base_for(target_n: int, multiplier: int, bound: int) -> tuple[list[int], int | None]:
    total = target_n * multiplier
    base: list[int] = []
    for p in primes_up_to(bound):
        g = math.gcd(target_n, p)
        if 1 < g < target_n:
            return base, g
        if p == 2 or total % p == 0 or legendre(total, p) == 1:
            base.append(p)
    return base, None


def polynomial_roots_mod_prime(A: int, B: int, C: int, total: int, p: int) -> tuple[int, ...]:
    if p == 2:
        return tuple(t for t in range(2) if (A * t * t + 2 * C * t + B) % 2 == 0)
    aa, bb, cc = A % p, (2 * C) % p, B % p
    if aa:
        root_total = tonelli_shanks(total, p)
        if root_total is None:
            return ()
        inv_a = pow(aa, -1, p)
        return tuple(sorted({((-C + root_total) * inv_a) % p, ((-C - root_total) * inv_a) % p}))
    if bb:
        return ((-cc * pow(bb, -1, p)) % p,)
    if cc == 0:
        return tuple(range(p))
    return ()


def add_factor_dicts(items: Iterable[dict[int, int]]) -> dict[int, int]:
    out: dict[int, int] = defaultdict(int)
    for item in items:
        for p, exponent in item.items():
            out[p] += exponent
    return dict(out)


def factor_product_mod(factors: dict[int, int], modulus: int) -> int:
    out = 1
    for p, exponent in factors.items():
        out = out * pow(p % modulus, exponent, modulus) % modulus
    return out


@dataclass(frozen=True)
class Relation:
    root_mod_n: int
    factors: dict[int, int]
    source: str
    state_step: int
    t: int


@dataclass
class StageTimes:
    state_update: float = 0.0
    root_setup: float = 0.0
    sieve: float = 0.0
    trial_division: float = 0.0
    recombination: float = 0.0
    linear_algebra: float = 0.0
    gcd_extraction: float = 0.0

    def as_dict(self) -> dict[str, float]:
        return {key: round(value, 9) for key, value in vars(self).items()}


class GF2RelationMatrix:
    def __init__(self, target_n: int, factor_base: list[int]):
        self.target_n = target_n
        self.factor_base = factor_base
        self.columns = {-1: 0, **{p: i + 1 for i, p in enumerate(factor_base)}}
        self.basis: dict[int, tuple[int, int]] = {}
        self.relations: list[Relation] = []
        self.rank = 0
        self.dependencies = 0
        self.dependencies_tested = 0
        self.rank_trajectory: list[tuple[int, int]] = []
        self.factor: int | None = None

    def parity(self, relation: Relation) -> int:
        row = 0
        for p, exponent in relation.factors.items():
            if exponent % 2 and p in self.columns:
                row ^= 1 << self.columns[p]
            elif exponent % 2 and p not in self.columns:
                raise AssertionError(f"odd non-factor-base exponent: {p}^{exponent}")
        return row

    def verify_relation(self, relation: Relation) -> bool:
        return pow(relation.root_mod_n, 2, self.target_n) == factor_product_mod(
            relation.factors, self.target_n
        )

    def add(self, relation: Relation, stages: StageTimes) -> None:
        if not self.verify_relation(relation):
            raise ValueError("relation verification failed before matrix insertion")
        index = len(self.relations)
        self.relations.append(relation)
        row = self.parity(relation)
        combination = 1 << index
        start = time.perf_counter()
        while row:
            pivot = row.bit_length() - 1
            if pivot in self.basis:
                basis_row, basis_combination = self.basis[pivot]
                row ^= basis_row
                combination ^= basis_combination
            else:
                self.basis[pivot] = (row, combination)
                self.rank += 1
                self.rank_trajectory.append((len(self.relations), self.rank))
                stages.linear_algebra += time.perf_counter() - start
                return
        self.dependencies += 1
        stages.linear_algebra += time.perf_counter() - start
        self._test_dependency(combination, stages)

    def _test_dependency(self, combination: int, stages: StageTimes) -> None:
        self.dependencies_tested += 1
        chosen: list[Relation] = []
        index = 0
        bits = combination
        while bits:
            if bits & 1:
                chosen.append(self.relations[index])
            bits >>= 1
            index += 1
        factors = add_factor_dicts(rel.factors for rel in chosen)
        if any(exponent % 2 for exponent in factors.values()):
            raise AssertionError("dependency has odd exponent")
        x = 1
        for relation in chosen:
            x = x * relation.root_mod_n % self.target_n
        y = 1
        for p, exponent in factors.items():
            if p == -1:
                continue
            y = y * pow(p, exponent // 2, self.target_n) % self.target_n
        start = time.perf_counter()
        for candidate in (math.gcd(x - y, self.target_n), math.gcd(x + y, self.target_n)):
            if 1 < candidate < self.target_n:
                self.factor = candidate
                break
        stages.gcd_extraction += time.perf_counter() - start

    def trajectory_digest(self) -> str:
        raw = json.dumps(self.rank_trajectory, separators=(",", ":")).encode("utf-8")
        return hashlib.sha256(raw).hexdigest()


class PartialRecombiner:
    def __init__(self, mode: str, large_prime_bound: int):
        self.mode = mode
        self.large_prime_bound = large_prime_bound
        self.singles: dict[int, Relation] = {}
        self.graph: dict[int, list[tuple[int, Relation]]] = defaultdict(list)
        self.partial_relations = 0
        self.dlp_edges = 0
        self.completed_cycles = 0

    def _split_two_primes(self, remainder: int, trial_primes: list[int]) -> tuple[int, int] | None:
        if remainder <= 1:
            return None
        root = math.isqrt(remainder)
        for p in trial_primes:
            if p > root:
                break
            if remainder % p == 0:
                q = remainder // p
                if p <= self.large_prime_bound and q <= self.large_prime_bound and is_prime(q):
                    return (p, q)
                return None
        return None

    def classify(
        self,
        root_mod_n: int,
        factors: dict[int, int],
        remainder: int,
        source: str,
        state_step: int,
        t: int,
        trial_primes: list[int],
        stages: StageTimes,
    ) -> list[Relation]:
        if remainder == 1:
            return [Relation(root_mod_n, factors, source, state_step, t)]
        if self.mode == "none":
            return []
        if is_prime(remainder) and remainder <= self.large_prime_bound:
            partial_factors = dict(factors)
            partial_factors[remainder] = partial_factors.get(remainder, 0) + 1
            partial = Relation(root_mod_n, partial_factors, source, state_step, t)
            self.partial_relations += 1
            previous = self.singles.pop(remainder, None)
            if previous is None:
                self.singles[remainder] = partial
                return []
            start = time.perf_counter()
            combined = Relation(
                previous.root_mod_n * partial.root_mod_n,
                add_factor_dicts((previous.factors, partial.factors)),
                f"slp:{previous.source}+{partial.source}",
                state_step,
                t,
            )
            stages.recombination += time.perf_counter() - start
            return [combined]
        square = math.isqrt(remainder)
        if square * square == remainder and square <= self.large_prime_bound and is_prime(square):
            full_factors = dict(factors)
            full_factors[square] = full_factors.get(square, 0) + 2
            return [Relation(root_mod_n, full_factors, source, state_step, t)]
        if self.mode != "dlp" or remainder > self.large_prime_bound**2:
            return []
        pair = self._split_two_primes(remainder, trial_primes)
        if pair is None:
            return []
        p, q = pair
        partial_factors = dict(factors)
        partial_factors[p] = partial_factors.get(p, 0) + 1
        partial_factors[q] = partial_factors.get(q, 0) + 1
        edge = Relation(root_mod_n, partial_factors, source, state_step, t)
        self.partial_relations += 1
        self.dlp_edges += 1
        start = time.perf_counter()
        path = self._path(p, q)
        self.graph[p].append((q, edge))
        self.graph[q].append((p, edge))
        if path is None:
            stages.recombination += time.perf_counter() - start
            return []
        cycle = [edge, *path]
        self.completed_cycles += 1
        combined = Relation(
            math.prod(rel.root_mod_n for rel in cycle),
            add_factor_dicts(rel.factors for rel in cycle),
            "dlp-cycle:" + "+".join(rel.source for rel in cycle),
            state_step,
            t,
        )
        stages.recombination += time.perf_counter() - start
        return [combined]

    def _path(self, start_node: int, end_node: int) -> list[Relation] | None:
        queue = deque([start_node])
        previous: dict[int, tuple[int, Relation] | None] = {start_node: None}
        while queue:
            node = queue.popleft()
            if node == end_node:
                break
            for neighbor, relation in self.graph.get(node, []):
                if neighbor not in previous:
                    previous[neighbor] = (node, relation)
                    queue.append(neighbor)
        if end_node not in previous:
            return None
        path: list[Relation] = []
        node = end_node
        while node != start_node:
            parent, relation = previous[node]  # type: ignore[misc]
            path.append(relation)
            node = parent
        return path


@dataclass
class RunMetrics:
    status: str
    factor: int | None
    orbit_steps: int
    bands_considered: int
    bands_opened: int
    bands_skipped_resource: int
    total_band_width: int
    point_candidates: int
    band_candidates: int
    full_relations: int
    partial_relations: int
    dlp_edges: int
    completed_cycles: int
    rank: int
    dependencies: int
    dependencies_tested: int
    wall_seconds: float
    peak_memory_bytes: int
    stages: dict[str, float]
    rank_trajectory_digest: str
    relation_stream_digest: str
    mathematical_relation_digest: str
    error: str = ""


class RelationEngine:
    def __init__(
        self,
        target_n: int,
        multiplier: int,
        factor_base_bound: int,
        large_prime_mode: str,
    ):
        self.n = target_n
        self.multiplier = multiplier
        self.total = target_n * multiplier
        self.sqrt_total = math.isqrt(self.total)
        self.factor_base, immediate = factor_base_for(target_n, multiplier, factor_base_bound)
        self.immediate_factor = immediate
        self.large_prime_bound = max(self.factor_base[-1] if self.factor_base else 2, factor_base_bound) * 64
        self.trial_primes = primes_up_to(self.large_prime_bound)
        self.matrix = GF2RelationMatrix(target_n, self.factor_base)
        self.recombiner = PartialRecombiner(large_prime_mode, self.large_prime_bound)
        self.stages = StageTimes()
        self.relation_digest = hashlib.sha256()
        self.math_relation_digest = hashlib.sha256()
        self.full_relations = 0

    def _record_full(self, relation: Relation) -> None:
        relation = Relation(relation.root_mod_n % self.n, relation.factors, relation.source, relation.state_step, relation.t)
        if not self.matrix.verify_relation(relation):
            raise ValueError(f"invalid relation from {relation.source}")
        payload = {
            "root": relation.root_mod_n,
            "factors": sorted(relation.factors.items()),
            "source": relation.source,
            "step": relation.state_step,
            "t": relation.t,
        }
        self.relation_digest.update(json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8"))
        math_payload = {
            "root": relation.root_mod_n,
            "factors": sorted(relation.factors.items()),
            "step": relation.state_step,
            "t": relation.t,
        }
        self.math_relation_digest.update(
            json.dumps(math_payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
        )
        self.matrix.add(relation, self.stages)
        self.full_relations += 1

    def _classify_exact(
        self,
        value: int,
        root_mod_n: int,
        source: str,
        state_step: int,
        t: int,
        prefactored: tuple[dict[int, int], int] | None = None,
    ) -> None:
        start = time.perf_counter()
        if prefactored is None:
            remainder = abs(value)
            factors: dict[int, int] = {-1: 1} if value < 0 else {}
            for p in self.factor_base:
                exponent = 0
                while remainder % p == 0:
                    remainder //= p
                    exponent += 1
                if exponent:
                    factors[p] = exponent
        else:
            factors, remainder = prefactored
        self.stages.trial_division += time.perf_counter() - start
        relations = self.recombiner.classify(
            root_mod_n % self.n,
            factors,
            remainder,
            source,
            state_step,
            t,
            self.trial_primes,
            self.stages,
        )
        for relation in relations:
            self._record_full(relation)

    def open_band(self, A: int, B: int, C: int, root_a: int, step: int, a: int) -> tuple[int, int]:
        width = max(0, a - 1)
        if width == 0:
            return 0, 0
        if width > MAX_SAFE_BAND_WIDTH:
            return width, -1
        start = time.perf_counter()
        roots_by_prime = [
            (p, polynomial_roots_mod_prime(A, B, C, self.total, p)) for p in self.factor_base
        ]
        self.stages.root_setup += time.perf_counter() - start

        values = [A * t * t + 2 * C * t + B for t in range(1, a)]
        residuals = [abs(value) for value in values]
        factors: list[dict[int, int]] = [({-1: 1} if value < 0 else {}) for value in values]
        start = time.perf_counter()
        for p, roots in roots_by_prime:
            for root in roots:
                first = root
                if first == 0:
                    first = p
                if first < 1:
                    first += ((1 - first + p - 1) // p) * p
                for t in range(first, a, p):
                    index = t - 1
                    exponent = 0
                    while residuals[index] % p == 0:
                        residuals[index] //= p
                        exponent += 1
                    if exponent:
                        factors[index][p] = factors[index].get(p, 0) + exponent
        self.stages.sieve += time.perf_counter() - start

        inverse_root = pow(root_a, -1, self.n)
        for index, t in enumerate(range(1, a)):
            root_d = (A * t + C) * inverse_root % self.n
            self._classify_exact(
                values[index],
                root_d,
                f"band:{step}:{t}",
                step,
                t,
                (factors[index], residuals[index]),
            )
            if self.matrix.factor is not None:
                break
        return width, width


def closed_state_step(
    total: int, sqrt_total: int, state: tuple[int, int, int], root_mod_n: int, target_n: int
) -> tuple[int, tuple[int, int, int], int, int | None]:
    A, B, C = state
    if A == 0 or A * B >= 0 or abs(C) >= math.isqrt(total) + (0 if math.isqrt(total) ** 2 == total else 1):
        raise ValueError("state outside reduced nonsquare orbit")
    a = (sqrt_total + abs(C)) // abs(A)
    next_A = A * a * a + 2 * C * a + B
    next_B = A
    next_C = A * a + C
    if next_C * next_C - next_A * next_B != total:
        raise AssertionError("closed-state invariant failure")
    g = math.gcd(root_mod_n, target_n)
    if 1 < g < target_n:
        return a, (next_A, next_B, next_C), 0, g
    next_root = next_C * pow(root_mod_n, -1, target_n) % target_n
    if pow(next_root, 2, target_n) != next_A % target_n:
        raise AssertionError("closed modular-root propagation failure")
    return a, (next_A, next_B, next_C), next_root, None


def cfrac_reference_stream(total: int, target_n: int, steps: int) -> list[tuple[int, int, int, int, int]]:
    sqrt_total = math.isqrt(total)
    m, d, a = 0, 1, sqrt_total
    p_minus_two, p_minus_one = 0, 1
    out: list[tuple[int, int, int, int, int]] = []
    for i in range(steps):
        p = (a * p_minus_one + p_minus_two) % target_n
        next_m = d * a - m
        numerator = total - next_m * next_m
        if numerator % d:
            raise AssertionError("continued-fraction exact division failure")
        next_d = numerator // d
        next_a = (sqrt_total + next_m) // next_d
        signed_d = -next_d if i % 2 == 0 else next_d
        out.append((a, signed_d, next_m, p, next_d))
        m, d, a = next_m, next_d, next_a
        p_minus_two, p_minus_one = p_minus_one, p
    return out


def verify_paired_equivalence(target_n: int, multiplier: int, steps: int) -> str:
    total = target_n * multiplier
    if math.isqrt(total) ** 2 == total:
        raise ValueError("square multiplier target")
    reference = cfrac_reference_stream(total, target_n, steps)
    state = (1, -total, 0)
    root_minus_one, root = 0, 1
    digest = hashlib.sha256()
    for i, (ref_a, ref_A, ref_m, ref_root, _) in enumerate(reference):
        A, B, C = state
        a = (math.isqrt(total) + abs(C)) // abs(A)
        next_A = A * a * a + 2 * C * a + B
        next_state = (next_A, A, A * a + C)
        next_root = (a * root + root_minus_one) % target_n
        if next_state[2] * next_state[2] - next_state[0] * next_state[1] != total:
            raise AssertionError("closed invariant failure")
        if pow(next_root, 2, target_n) != next_A % target_n:
            raise AssertionError("bounded convergent-root failure")
        if i < 32 and math.gcd(root, target_n) == 1:
            inverse_root = next_state[2] * pow(root, -1, target_n) % target_n
            if inverse_root != next_root:
                raise AssertionError("inverse band-root semantics disagrees")
        A, _, C = next_state
        expected_C = ref_m if i % 2 == 0 else -ref_m
        if (a, A, C, next_root) != (ref_a, ref_A, expected_C, ref_root):
            raise AssertionError(
                {"step": i, "closed": (a, A, C, next_root), "reference": (ref_a, ref_A, expected_C, ref_root)}
            )
        digest.update(f"{i}|{a}|{A}|{C}|{next_root}\n".encode("ascii"))
        state = next_state
        root_minus_one, root = root, next_root
    return digest.hexdigest()


def run_collector(
    target_n: int,
    multiplier: int,
    factor_base_bound: int,
    algorithm: str,
    large_prime_mode: str,
    max_steps: int,
    timeout_seconds: float,
    band_threshold: int | None = None,
    adaptive_open: Callable[[int, int, int, int], bool] | None = None,
) -> RunMetrics:
    tracemalloc.start()
    wall_start = time.perf_counter()
    engine = RelationEngine(target_n, multiplier, factor_base_bound, large_prime_mode)
    bands_considered = bands_opened = bands_skipped = total_width = 0
    point_candidates = band_candidates = orbit_steps = 0
    status = "MAX_STEPS"
    error = ""
    if engine.immediate_factor is not None:
        engine.matrix.factor = engine.immediate_factor
        status = "FACTOR_BASE_GCD"
    else:
        try:
            if algorithm == "cfrac_point":
                sqrt_total = math.isqrt(engine.total)
                m, d, a = 0, 1, sqrt_total
                p_minus_two, p_minus_one = 0, 1
                for step in range(max_steps):
                    if time.perf_counter() - wall_start >= timeout_seconds:
                        status = "TIMEOUT"
                        break
                    start = time.perf_counter()
                    p = (a * p_minus_one + p_minus_two) % target_n
                    next_m = d * a - m
                    next_d = (engine.total - next_m * next_m) // d
                    next_a = (sqrt_total + next_m) // next_d
                    value = -next_d if step % 2 == 0 else next_d
                    engine.stages.state_update += time.perf_counter() - start
                    engine._classify_exact(value, p, f"cfrac-point:{step}", step, a)
                    point_candidates += 1
                    orbit_steps = step + 1
                    if engine.matrix.factor is not None:
                        status = "FACTOR_FOUND"
                        break
                    m, d, a = next_m, next_d, next_a
                    p_minus_two, p_minus_one = p_minus_one, p
            elif algorithm in ("closed_point", "closed_band"):
                state = (1, -engine.total, 0)
                previous_root, root = 0, 1
                for step in range(max_steps):
                    if time.perf_counter() - wall_start >= timeout_seconds:
                        status = "TIMEOUT"
                        break
                    A, B, C = state
                    a = (engine.sqrt_total + abs(C)) // abs(A)
                    if algorithm == "closed_band" and step > 0:
                        bands_considered += 1
                        should_open = False
                        if adaptive_open is not None:
                            should_open = adaptive_open(a, A, len(engine.factor_base), max(0, a - 1))
                        elif band_threshold is not None:
                            should_open = a >= band_threshold
                        if should_open:
                            width, processed = engine.open_band(A, B, C, root, step, a)
                            total_width += width
                            if processed < 0:
                                bands_skipped += 1
                            else:
                                bands_opened += 1
                                band_candidates += processed
                            if engine.matrix.factor is not None:
                                status = "FACTOR_FOUND"
                                orbit_steps = step
                                break
                    start = time.perf_counter()
                    next_A = A * a * a + 2 * C * a + B
                    next_state = (next_A, A, A * a + C)
                    next_root = (a * root + previous_root) % target_n
                    engine.stages.state_update += time.perf_counter() - start
                    engine._classify_exact(
                        next_state[0], next_root, f"closed-point:{step}", step, a
                    )
                    point_candidates += 1
                    orbit_steps = step + 1
                    if engine.matrix.factor is not None:
                        status = "FACTOR_FOUND"
                        break
                    state = next_state
                    previous_root, root = root, next_root
            else:
                raise ValueError(f"unknown algorithm {algorithm}")
        except Exception as exc:  # retained as diagnosed failed run
            status = "ERROR"
            error = f"{type(exc).__name__}: {exc}"
    wall = time.perf_counter() - wall_start
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return RunMetrics(
        status=status,
        factor=engine.matrix.factor,
        orbit_steps=orbit_steps,
        bands_considered=bands_considered,
        bands_opened=bands_opened,
        bands_skipped_resource=bands_skipped,
        total_band_width=total_width,
        point_candidates=point_candidates,
        band_candidates=band_candidates,
        full_relations=engine.full_relations,
        partial_relations=engine.recombiner.partial_relations,
        dlp_edges=engine.recombiner.dlp_edges,
        completed_cycles=engine.recombiner.completed_cycles,
        rank=engine.matrix.rank,
        dependencies=engine.matrix.dependencies,
        dependencies_tested=engine.matrix.dependencies_tested,
        wall_seconds=wall,
        peak_memory_bytes=peak,
        stages=engine.stages.as_dict(),
        rank_trajectory_digest=engine.matrix.trajectory_digest(),
        relation_stream_digest=engine.relation_digest.hexdigest(),
        mathematical_relation_digest=engine.math_relation_digest.hexdigest(),
        error=error,
    )


def static_multiplier_score(target_n: int, multiplier: int, prime_limit: int = 97) -> float:
    if math.gcd(target_n, multiplier) != 1:
        return float("inf")
    total = target_n * multiplier
    score = -0.05 * math.log(multiplier)
    for p in primes_up_to(prime_limit):
        if p == 2:
            continue
        symbol = legendre(total, p)
        if symbol == 1:
            score += math.log(p) / (p - 1)
        elif symbol == 0:
            score += math.log(p) / p
    return score


def perturb_recurrence_sign(total: int) -> bool:
    A, B, C = 1, -total, 0
    a = math.isqrt(total)
    next_A = A * a * a - 2 * C * a + B
    next_B = A
    next_C = A * a - C
    # First C=0 step is insensitive; perturb the second step.
    A, B, C = next_A, next_B, next_C
    a = (math.isqrt(total) + abs(C)) // abs(A)
    bad_A = A * a * a - 2 * C * a + B
    bad_B = A
    bad_C = A * a + C
    return bad_C * bad_C - bad_A * bad_B != total


def invalid_band_root_rejected(target_n: int, multiplier: int) -> bool:
    total = target_n * multiplier
    A, B, C = 1, -total, 0
    root_a = 1
    t = 1
    value = A * t * t + 2 * C * t + B
    fake_root = ((A * t + C) * pow(root_a, -1, target_n) + 1) % target_n
    factors: dict[int, int] = {-1: 1} if value < 0 else {}
    remainder = abs(value)
    for p in primes_up_to(1000):
        exponent = 0
        while remainder % p == 0:
            remainder //= p
            exponent += 1
        if exponent:
            factors[p] = exponent
    if remainder > 1:
        factors[remainder] = factors.get(remainder, 0) + 1
    return pow(fake_root, 2, target_n) != factor_product_mod(factors, target_n)
