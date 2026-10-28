"""Read-only weighted opportunity accounting over reducer-accepted events.

No queue, counter file or admission authority is created here. Availability and
successful CLAIMs are replayed from the same authenticated runtime snapshot.
"""
from __future__ import annotations

from datetime import datetime, timezone
from fractions import Fraction


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
