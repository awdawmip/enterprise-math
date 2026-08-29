# Research Return — P022/P012 graph-distance API stale scheduler closure

- Task: `RS-P022-GRAPH-DISTANCE-API`
- Foundation question: `FQ-20260809-005`
- Claim: `chatgpt-p022gd-20260829-0801`
- Researcher: `EM-P022GD-7EEF3E`
- Base: `main@839dcaf57cdcc3a4f2f39efd553fef6f64e844d0`
- Result: `ALREADY_CANONICAL / STALE_SCHEDULER_ENTRY`

## Executive result

The research question is no longer mathematically or programmatically open. The scheduler entry is stale.

The exact API/domain split requested by FQ-20260809-005 was already researched, steward-accepted, source-canonicalized, and merged through PR #436 at canonical merge `3a40fe680e7aad4bc458540483c3c753e15f2cc4` on 2026-08-10. Current main still contains that exact layered contract.

Therefore this claim must **not** create a second implementation or reinterpret the theorem domain. The correct research disposition is to close the stale scheduler task against the already-canonical resolution.

## Exact canonical contract verified on current main

### 1. Stable P012 metric API

`graph_distance(adjacency, start, goal)` is reserved for the P012 theorem domain:

- endpoints are declared vertices;
- adjacency is closed over declared vertices;
- adjacency is loop-free;
- adjacency is symmetric, hence an undirected simple graph;
- within a connected component it returns ordinary shortest-walk length in `N`;
- cross-component queries raise `ValueError` rather than fabricating a finite distance.

This is the weakest domain on which the ordinary P012 natural-number graph metric claims (identity, symmetry, triangle inequality, adjacency iff distance one) apply without qualification.

### 2. Explicit directed operational helper

`directed_graph_distance(adjacency, start, goal)` preserves the old broader operational behavior for outgoing-neighbor maps:

- adjacency need only be closed over declared vertices;
- asymmetric adjacency and asymmetric reachability are allowed;
- the result is shortest directed unweighted walk length when reachable;
- the function is explicitly **not** asserted to be a metric in general.

### 3. Compatibility relation

On the P012 undirected-simple domain, `directed_graph_distance == graph_distance` pointwise. Thus the split does not duplicate two mathematical notions there; it separates theorem-bearing metric semantics from a broader operational shortest-walk helper.

## Minimal counterexample forcing the split

Take

```python
adjacency = {0: {1}, 1: set()}
```

Then the directed helper gives distance `0 -> 1 = 1`, while `1 -> 0` is unreachable. Hence symmetry fails and a total natural-number metric on the declared two-vertex set does not exist under literal directed adjacency. Calling this broader helper `graph_distance` while citing P012 metric theorems would silently enlarge the theorem domain.

Current regressions correctly require `graph_distance` to reject this asymmetric adjacency and permit it only through `directed_graph_distance`.

## Provenance audit

The current repository evidence is internally consistent:

1. `docs/P012_INTRINSIC_DISCRETE_GEOMETRY.en.md` states P012 on connected undirected simple graphs and treats disconnected graphs componentwise or with an extended infinity-valued distance.
2. `src/enterprise_math/geometry.py` implements the layered contract above.
3. `src/enterprise_math/__init__.py` exports both names explicitly.
4. `tests/test_p012_geometry.py` locks:
   - P012 metric axioms;
   - asymmetric directed behavior under the explicit helper;
   - rejection of asymmetric/self-loop/non-closed input by the metric API as appropriate;
   - agreement of the two functions on the P012 domain;
   - componentwise behavior on disconnected undirected graphs.
5. Foundation Issue #164 records the original research return, steward acceptance, and source canonicalization.
6. Merge commit `3a40fe680e7aad4bc458540483c3c753e15f2cc4` explicitly says it canonicalized the steward-accepted FQ-005 layered graph-distance API.

## Backward-compatibility conclusion

The canonical design is the least disruptive sound split:

- old users that truly require directed shortest-walk semantics have an explicit replacement name;
- callers relying on P012 metric semantics keep the stable `graph_distance` name;
- silent asymmetric use through the theorem-bearing name is rejected rather than misclassified as metric geometry.

No further code change is justified by the research question itself.

## Scheduler/control-plane finding

`research_scheduler.json` still presents `RS-P022-GRAPH-DISTANCE-API` as a P0/High `READY` task even though the underlying FQ was resolved and source-canonicalized on 2026-08-10. This is control-plane staleness, not a renewed mathematical frontier.

Recommended disposition:

- mark this scheduler task terminal/superseded by the canonical FQ-005 resolution;
- do not redispatch it after this return;
- if a separate migration is needed to repair the static scheduler baseline, treat that as governance/control-plane maintenance rather than new research.

## Scope boundary

This return does **not** alter P012 mathematics, introduce an extended-distance API, change disconnected-component semantics, or claim novelty for graph metrics. It only verifies the already-canonical API/domain resolution and identifies the stale scheduler entry.

## Final status

`SUCCESS / ALREADY_CANONICAL / STALE_SCHEDULER_ENTRY_CONFIRMED`

Hard block: `NONE`.

Next action: Driver/control-plane review should close or supersede `RS-P022-GRAPH-DISTANCE-API` against the accepted FQ-20260809-005 canonicalization, without reopening the API question.