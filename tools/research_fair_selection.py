"""Read-only weighted opportunity accounting over reducer-accepted events.

No queue, counter file or admission authority is created here. Availability and
successful CLAIMs are replayed from the same authenticated runtime snapshot.
"""
from __future__ import annotations

from datetime import datetime, timezone
from fractions import Fraction


def trace_availability(state, at, comment_id):
    eligible = state.get("state") in {"READY", "HANDOFF_READY"} and not state.get("claim_id")
    trace = state["scheduling_trace"]
    previous = next((item for item in reversed(trace) if item["event"] == "AVAILABLE"), None)
    if previous is None or previous["eligible"] != eligible:
        trace.append(dict(event="AVAILABLE", at=at, comment_id=comment_id,
                          phase=2, eligible=eligible))


def trace_claim(state, claim_id, at, comment_id):
    trace = state["scheduling_trace"]
    # Retries and duplicate claim IDs cannot buy or consume another opportunity.
    if not any(item.get("claim_id") == claim_id for item in trace):
        trace.append(dict(event="CLAIM", at=at, comment_id=comment_id,
                          phase=1, claim_id=claim_id))


def target_key(state):
    return tuple(str(state.get(key) or "") for key in
                 ("task_id", "execution_cohort_id", "execution_lane_id"))


def _clock(value):
    try:
        at = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
        return at.replace(tzinfo=timezone.utc) if at.tzinfo is None else at
    except (ValueError, TypeError):
        return datetime(1970, 1, 1, tzinfo=timezone.utc)


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


def select(states, candidates, weights):
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
    available = set()
    history = []
    missing = 0
    for key, state in by_key.items():
        trace = state.get("scheduling_trace")
        if trace is None:
            missing += 1
            if state.get("dispatch_state") == "NEEDS_DISPATCH":
                available.add(key)
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
        counts[key] = counts.get(key, 0) + 1
        last[priority] = len(successful)

    active = {s.get("priority") for s in candidates} & weights.keys()
    if not active:
        # Historical metadata outside configured priorities remains selectable.
        winner = min(candidates, key=target_key)
        return {**{k: v for k, v in winner.items() if k != "scheduling_trace"},
                "fair_selection": {"method": "MISSING_PRIORITY_TASK_FALLBACK",
                                   "missing_history_tasks": missing,
                                   "atomic_global_quota": False}}
    total = sum(weights[p] for p in active)
    priority = max(active, key=lambda p: (credits[p] + Fraction(weights[p], total),
                                        -last.get(p, 0), weights[p], p))
    pool = [s for s in candidates if s.get("priority") == priority]
    groups = {family[target_key(s)] for s in pool}
    group = min(groups, key=lambda g: (-direction_credit.get((priority, g), Fraction()),
                min(_clock(s.get("last_progress_at")) for s in pool if family[target_key(s)] == g), g))
    pool = [s for s in pool if family[target_key(s)] == group]
    winner = min(pool, key=lambda s: (counts.get(target_key(s), 0),
                 _clock(s.get("last_progress_at")), target_key(s)))
    # Attach a projection to the returned copy, never to event/state authority.
    return {**{k: v for k, v in winner.items() if k != "scheduling_trace"}, "fair_selection": {
        "method": "AVAILABLE_WEIGHTED_SUCCESSFUL_CLAIMS",
        "weights": dict(weights), "successful_claims": len(successful),
        "priority_credit": {p: str(credits[p]) for p in weights},
        "direction": group, "missing_history_tasks": missing,
        "direction_basis": "EXPLICIT_PARENT_CHAIN" if winner.get("parent_task_id") else "EXACT_TASK_ID",
        "history_scope": "CURRENT_AUTHENTICATED_PUBLICATION_AND_LANE_REPLAY",
        "atomic_global_quota": False,
    }}
