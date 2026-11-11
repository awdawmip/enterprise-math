"""Read-only weighted opportunity accounting over reducer-accepted events.

No queue, counter file or admission authority is created here. Availability and
successful CLAIMs are replayed from the same authenticated runtime snapshot.
"""
from __future__ import annotations

from datetime import datetime, timezone
from fractions import Fraction
from contextlib import contextmanager
from contextvars import ContextVar
import hashlib
import json
import math
import secrets


def trace_availability(state, at, comment_id):
    eligible = state.get("state") in {"READY", "HANDOFF_READY"} and not state.get("claim_id")
    owner_present = bool(state.get("claim_id"))
    trace = state["scheduling_trace"]
    previous = next((item for item in reversed(trace) if item["event"] == "AVAILABLE"), None)
    if previous is None or (previous["eligible"], previous.get("owner_present")) != (eligible, owner_present):
        trace.append(dict(event="AVAILABLE", at=at, comment_id=comment_id,
                          phase=2, eligible=eligible, owner_present=owner_present))


def trace_claim(state, claim_id, at, comment_id):
    trace = state["scheduling_trace"]
    # Retries and duplicate claim IDs cannot buy or consume another opportunity.
    if not any(item.get("claim_id") == claim_id for item in trace):
        trace.append(dict(event="CLAIM", at=at, comment_id=comment_id,
                          phase=1, claim_id=claim_id))


def target_key(state):
    return tuple(str(state.get(key) or "") for key in
                 ("task_id", "execution_cohort_id", "execution_lane_id"))


def lifecycle_clock(value):
    try:
        if isinstance(value, datetime):
            return value
        at = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
        return at.replace(tzinfo=timezone.utc) if at.tzinfo is None else at
    except (ValueError, TypeError):
        return None


def _clock(value):
    return lifecycle_clock(value) or datetime(1970, 1, 1, tzinfo=timezone.utc)


def canonical_availability(state, *, source, closed_at=None, reopened_at=None,
                           opened_at=None, now=None):
    """Project canonical lifecycle boundaries without changing runtime authority.

    Unknown overlay time cannot establish any earlier availability: retain the
    accepted service events but suppress that unproved eligibility interval and
    report the degradation. Merely appending false at now would leave ghost debt.
    """
    trace = state.get("scheduling_trace")
    if trace is None:
        state["scheduling_history_degraded"] = source + ":MISSING_TRACE"
        return state
    raw = [dict(item) for item in trace]
    unknown_close = closed_at is None and opened_at is None
    if unknown_close:
        state["scheduling_history_degraded"] = source + ":UNKNOWN_OVERLAY_START"
        state["scheduling_history_known_from"] = (
            reopened_at.isoformat() if reopened_at is not None else
            now.isoformat() if isinstance(now, datetime) else None)
    def underlying(at):
        # Source lifecycle edges precede Issue comments admitted at that same
        # timestamp (CLAIM gates use at >= reviewed_at). Expiry/base markers
        # already use comment_id=0 and therefore belong to the boundary itself.
        entries = [e for e in raw if e["event"] == "AVAILABLE" and
                   (_clock(e["at"]) < at or
                    (_clock(e["at"]) == at and not e.get("comment_id")))]
        return max(entries, key=lambda e: (_clock(e["at"]), e.get("comment_id") or 0, e["phase"])) if entries else {}
    projected = []
    for item in raw:
        if item["event"] == "AVAILABLE":
            at = _clock(item["at"])
            before_open = opened_at is not None and at < opened_at
            after_close = unknown_close or (closed_at is not None and at >= closed_at)
            before_reopen = reopened_at is None or at < reopened_at
            if before_open or (after_close and before_reopen):
                item["eligible"] = False
        projected.append(item)
    if opened_at is not None:
        value = underlying(opened_at)
        projected.append(dict(event="AVAILABLE", eligible=bool(value.get("eligible")),
            owner_present=bool(value.get("owner_present")), at=opened_at.isoformat(), comment_id=0, phase=0))
    if closed_at is not None:
        projected.append(dict(event="AVAILABLE", eligible=False,
            at=closed_at.isoformat(), comment_id=0, phase=0))
    if reopened_at is not None:
        # Review reopens claimless work; it never makes a live lease available.
        value = underlying(reopened_at)
        projected.append(dict(event="AVAILABLE", eligible=not value.get("owner_present", False),
            owner_present=bool(value.get("owner_present")), at=reopened_at.isoformat(), comment_id=0, phase=0))
    elif unknown_close and state.get("dispatch_state") == "NEEDS_DISPATCH" and isinstance(now, datetime):
        # Current eligibility is known, its past start is not. This is an honest
        # current boundary, not a fabricated historical reopening timestamp.
        projected.append(dict(event="AVAILABLE", eligible=True,
            at=now.isoformat(), comment_id=0, phase=0))
    state["scheduling_trace"] = projected
    state["scheduling_availability_source"] = source
    return state


def directions(states):
    """Use explicit parent links, never lexical similarity or identity ID stems."""
    parents = {s["task_id"]: s.get("parent_task_id") for s in states}
    result = {}
    for state in states:
        current = state["task_id"]
        seen = set()
        while current not in seen and parents.get(current):
            seen.add(current)
            current = parents[current]
        result[target_key(state)] = min(seen) if current in seen else current
    return result


_SELECTION = ContextVar("research_new_unit_selection", default=None)


@contextmanager
def selection_scope(seed=None, at=None):
    """One new-unit draw; callers retain the returned seed for exact replay."""
    token = _SELECTION.set({"seed": str(seed) if seed is not None else secrets.token_hex(16),
                            "at": lifecycle_clock(at) or datetime.now(timezone.utc)})
    try:
        yield
    finally:
        _SELECTION.reset(token)


def _draw(items, seed, domain, weight):
    # Independent hash races are insensitive to input order. A random seed is
    # consumed once at the new-unit boundary, never on receipt polling.
    def score(item):
        key = json.dumps(item, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
        value = int.from_bytes(hashlib.sha256((seed + "\0" + domain + "\0" + key).encode()).digest()[:8], "big")
        unit = min(1 - 2**-53, (value + 1) / (2**64 + 1))
        return (-math.log(unit) / max(float(weight(item)), 1e-12), key)
    return min(items, key=score)


def _waiting_days(state, at):
    if state.get("scheduling_history_degraded"):
        return 0.0  # Unknown lifecycle time cannot manufacture old waiting debt.
    entries = [e for e in state.get("scheduling_trace", []) if e.get("event") == "AVAILABLE"]
    if not entries:
        return 0.0
    edge = max(entries, key=lambda e: (_clock(e["at"]), e.get("comment_id") or 0, e.get("phase", 0)))
    known = lifecycle_clock(edge.get("at"))
    if known is None or not edge.get("eligible"):
        return 0.0
    if known.tzinfo is None:known = known.replace(tzinfo=timezone.utc)
    return max(0.0, (at - known).total_seconds() / 86400)


def _rotate(candidates, by_key, family, weights, credits, direction_credit,
            counts, successful, missing, reasons, config):
    context = _SELECTION.get()
    if context is None:
        with selection_scope() as _:
            return _rotate(candidates, by_key, family, weights, credits, direction_credit,
                           counts, successful, missing, reasons, config)
    seed, at = context["seed"], context["at"]
    scale = max(1.0, float(config.get("wait_scale_days", 7)))
    cap = min(4.0, max(0.0, float(config.get("max_wait_bonus", 3))))
    unclaimed = min(2.0, max(1.0, float(config.get("unclaimed_bonus", 1.5))))
    def age(s):
        return 1.0 + min(cap, _waiting_days(by_key[target_key(s)], at) / scale)
    def service(value):
        return min(4.0, max(0.25, 1.0 + float(value)))
    active = {s.get("priority") for s in candidates} & weights.keys()
    unproved = any(by_key[target_key(s)].get("scheduling_history_degraded") for s in candidates)
    effective = {p: float(weights[p]) * (1 if unproved else service(credits[p])) for p in active}
    if active:
        priority = _draw(sorted(active), seed, "priority", effective.__getitem__)
        pool = [s for s in candidates if s.get("priority") == priority]
    else:
        priority, pool = None, candidates
    groups = {family[target_key(s)] for s in pool}
    def direction_weight(group):
        wait = max(age(s) for s in pool if family[target_key(s)] == group)
        debt = 1 if unproved else service(direction_credit.get((priority, group), Fraction()))
        return debt * (1 + (wait - 1) / max(1.0, cap))
    group = _draw(sorted(groups), seed, "direction:" + str(priority), direction_weight)
    pool = [s for s in pool if family[target_key(s)] == group]
    def task_weight(key):
        state = by_key[key]
        n = counts.get(key, 0)
        return age(state) * (unclaimed if n == 0 else 1.0) / (1 + min(n, 3))
    selected_key = _draw(sorted(target_key(s) for s in pool), seed, "task:" + group, task_weight)
    winner = next(s for s in pool if target_key(s) == selected_key)
    return {**{k: v for k, v in winner.items() if k != "scheduling_trace"}, "fair_selection": {
        "method": "SEEDED_WEIGHTED_WAITING_ROTATION_V1", "weights": dict(weights),
        "effective_priority_weights": effective, "successful_claims": len(successful),
        "priority_credit": {p: str(credits[p]) for p in weights}, "direction": group,
        "direction_basis": "EXPLICIT_PARENT_CHAIN" if winner.get("parent_task_id") else "EXACT_TASK_ID",
        "selection_seed": seed, "selection_at": at.isoformat(),
        "candidate_count": len(candidates), "selected_waiting_days": round(_waiting_days(by_key[selected_key], at), 3),
        "selected_successful_claims": counts.get(selected_key, 0), "selected_task_weight": task_weight(selected_key),
        "candidate_set_sha256": hashlib.sha256(json.dumps(sorted(target_key(s) for s in candidates)).encode()).hexdigest(),
        "missing_history_tasks": missing, "degraded_history_reasons": sorted(reasons),
        "boundary": "NEW_RESEARCH_UNIT_ONLY", "retry_policy": "REUSE_ORIGINAL_REQUEST_RECEIPT_AND_SEED",
        "history_scope": "CURRENT_AUTHENTICATED_PUBLICATION_AND_LANE_REPLAY", "atomic_global_quota": False}}


def select(states, candidates, weights, *, rotation=None):
    """Smooth weighted fair service, accruing only while a candidate is present.

    An absent class accrues no debt. Its existing fractional residual is retained
    across leases/handoffs. Actual successful winners, including stale-snapshot
    winners, are charged; failed attempts and owner renewals never enter this log.
    """
    states = list(states)
    candidates = list(candidates)
    if not candidates:
        return None
    by_key = {target_key(s): s for s in states}
    by_key.update({target_key(s): s for s in candidates})
    family = directions(by_key.values())
    credits = {p: Fraction() for p in weights}
    direction_credit = {}
    counts = {}
    last = {}
    last_direction = {}
    available = set()
    history = []
    missing = 0
    degradation_reasons = set()
    for key, state in by_key.items():
        trace = state.get("scheduling_trace")
        available_entries = [e for e in trace or [] if e["event"] == "AVAILABLE"]
        last_available = max(available_entries, key=lambda e: (_clock(e["at"]), e.get("comment_id") or 0, e["phase"])) if available_entries else None
        if (state.get("dispatch_state") not in {"NEEDS_DISPATCH", "LEASED"}
                and last_available and last_available["eligible"]):
            # Compatibility for callers supplying an older canonical projection
            # without lifecycle timestamps. Never trust its reducer-only tail.
            state = canonical_availability(dict(state), source="UNRECONCILED_CANONICAL_OVERLAY")
            trace = state["scheduling_trace"]
            by_key[key] = state
        if not trace:
            state = {**state, "scheduling_history_degraded": "MISSING_TRACE"}
            by_key[key] = state
        if trace is None or state.get("scheduling_history_degraded"):
            missing += 1
            degradation_reasons.add(state.get("scheduling_history_degraded") or "MISSING_TRACE")
        for index, item in enumerate(trace or []):
            history.append((_clock(item["at"]), item.get("comment_id") or 0,
                            item["phase"], key, index, item))
    successful = set()
    for _, _, _, key, _, item in sorted(history):
        if item["event"] == "AVAILABLE":
            if item["eligible"]:
                available.add(key)
            else:
                available.discard(key)
            continue
        identity = (key, item["claim_id"])
        if identity in successful:
            continue
        successful.add(identity)
        winner = by_key[key]
        priority = winner.get("priority")
        if priority not in weights:
            continue
        counts[key] = counts.get(key, 0) + 1
        last[priority] = len(successful)
        last_direction[(priority, family[key])] = len(successful)
        if winner.get("scheduling_history_degraded"):
            known_from = lifecycle_clock(winner.get("scheduling_history_known_from"))
            if known_from is None or _clock(item["at"]) < known_from:
                # The CLAIM is a fact, but an unknown eligible set cannot prove
                # either a positive entitlement or a negative fairness debt.
                continue
        # A successful successor CAS is a new unit even though the predecessor
        # was leased. Include that winner at its historical service boundary.
        eligible = available | {key}
        active = {by_key[k].get("priority") for k in eligible} & weights.keys()
        total = sum(weights[p] for p in active)
        for p in active:
            credits[p] += Fraction(weights[p], total)
        credits[priority] -= 1
        groups = {family[k] for k in eligible if by_key[k].get("priority") == priority}
        for group in groups:
            pair = (priority, group)
            direction_credit[pair] = direction_credit.get(pair, Fraction()) + Fraction(1, len(groups))
        pair = (priority, family[key])
        direction_credit[pair] -= 1

    if isinstance(rotation, dict) and rotation.get("enabled") is True:
        return _rotate(candidates, by_key, family, weights, credits, direction_credit,
                       counts, successful, missing, degradation_reasons, rotation)
    active = {s.get("priority") for s in candidates} & weights.keys()
    if not active:
        # Historical metadata outside configured priorities remains selectable.
        winner = min(candidates, key=target_key)
        return {**{k: v for k, v in winner.items() if k != "scheduling_trace"},
                "fair_selection": {"method": "MISSING_PRIORITY_TASK_FALLBACK",
                                   "missing_history_tasks": missing,
                                   "atomic_global_quota": False}}
    total = sum(weights[p] for p in active)
    degraded_candidates = any(by_key[target_key(s)].get("scheduling_history_degraded") for s in candidates)
    if degraded_candidates:
        # Unknown eligibility must not pin a runnable low-priority task behind
        # unprovable negative debt forever. Shared successful-service age is an
        # approximate, debt-free fallback; it does not invent historical supply.
        priority = max(active, key=lambda p: (weights[p] * (len(successful) + 1 - last.get(p, 0)), weights[p], p))
    else:
        priority = max(active, key=lambda p: (credits[p] + Fraction(weights[p], total),
                                            -last.get(p, 0), weights[p], p))
    pool = [s for s in candidates if s.get("priority") == priority]
    groups = {family[target_key(s)] for s in pool}
    group = min(groups, key=lambda g: (last_direction.get((priority, g), 0) if degraded_candidates
                                      else -direction_credit.get((priority, g), Fraction()),
                min(_clock(s.get("last_progress_at")) for s in pool if family[target_key(s)] == g), g))
    pool = [s for s in pool if family[target_key(s)] == group]
    winner = min(pool, key=lambda s: (counts.get(target_key(s), 0),
                 _clock(s.get("last_progress_at")), target_key(s)))
    # Attach a projection to the returned copy, never to event/state authority.
    return {**{k: v for k, v in winner.items() if k != "scheduling_trace"}, "fair_selection": {
        "method": "WEIGHTED_SERVICE_AGE_FALLBACK" if degraded_candidates else "AVAILABLE_WEIGHTED_SUCCESSFUL_CLAIMS",
        "weights": dict(weights), "successful_claims": len(successful),
        "priority_credit": {p: str(credits[p]) for p in weights},
        "direction": group, "missing_history_tasks": missing,
        "degraded_history_reasons": sorted(degradation_reasons),
        "direction_basis": "EXPLICIT_PARENT_CHAIN" if winner.get("parent_task_id") else "EXACT_TASK_ID",
        "history_scope": "CURRENT_AUTHENTICATED_PUBLICATION_AND_LANE_REPLAY",
        "atomic_global_quota": False,
    }}
