# R66 — Persistent branch-preserving subtree certificates

2026-11-11. Scientific input frozen at `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Independent TASK_RESEARCH author-side exploration, continuing R63/R64/R65 (PR #2069). Model: the exact rational auxiliary S23 circle observer, not a new P000/X6 axiom or native BRC arithmetic.

## State, labels and observer
Let rational `0<theta0<1` lie in rational `I=[L,U] subset (0,1)`. For `m>=2` the distinct historical phases `{v theta}`, `0<=v<m`, divide the circle into *originally labelled* half-open arcs `A_z(theta)`. Every source is the independently erasable pair `(t,b)` with integer `t<j` and branch identity `b`; its nominal index key is `({t theta0},t,b)`. The derived sparse observer returns the maximum qualifying `t` such that `{x+(t-j)theta} in A_z(theta)`, or empty.

**Information preservation.** The event carrier retains both timestamp and branch. Latest-time projection is sufficient for this one current observer, but not for future branch-specific deletion: `{(70,1),(70,2)}` and `{(70,2)}` have identical current maximum 70, yet deleting branch 2 gives different future results. This is a concrete future-operation fiber distinction, consistent with BRC observer/provenance discipline.

## Theorem 1 — Persistent four-extrema invariant
In a treap ordered by the full nominal key, each node stores its live subtree count, `phase_min/phase_max`, `t_min/t_max`, and its own immutable event. On every insert, split, merge, delete or copied path, recompute each aggregate as the respective min/max over own event and nonempty children. By structural induction, the returned root has exactly the new live set, every subtree aggregate is exact, all untouched roots remain immutable and queryable, and same-time same-phase events with distinct branches remain separate. Under independent randomized priorities and an update schedule fixed independently of those priorities, expected unit-cost update path and copied nodes are `O(log(n+1))`. Rational bit complexity remains input-dependent.

## Theorem 2 — Whole-subtree interval exclusion
Let `ell,u,tmin,tmax` be valid aggregate extrema of an immutable subtree at `theta0`. Set `dL=L-theta0`, `dU=U-theta0`, and `D={tmin*dL,tmin*dU,tmax*dL,tmax*dU}`. Each event continuous phase lift belongs to
`S_I=[ell+min(D),u+max(D)]`.
Assume the labelled history order stays constant over I. Let `nxt` be the successor of label z at anchor. Take `a0={(j+z)theta0-x}` and `c0={(j+nxt)theta0-x}`; add 1 to c0 if needed to enforce `a0<c0<a0+1`. For endpoint shifts d define `a(d)=a0+(j+z)d`, `c(d)=c0+(j+nxt)d`, and require `0<c(d)-a(d)<1` at both endpoints. All target translated arcs then have a continuous lift within `Q_I=[min a(d),max c(d)]`.

If
```
ceil(ell+min(D)-max(Q_I)) > floor(u+max(D)-min(Q_I))
```
then **every event in the subtree is outside the target label arc for every real theta in I**, endpoints included. Proof: a source entering the target gives an integer translate intersection of the two real lift intervals; the displayed integer-separation inequality excludes every such translate. It never assumes that sources retain their internal phase order, so phase-order reversals do not invalidate the result.

## Theorem 3 — Latest-source certificate
Compute anchor winner w by nominal BST interval-max query. Certify its phase stays in the labelled arc by the two exact affine source/boundary noncollision checks (when w exists). To exclude every newer competitor, recursively (a) prune any subtree with `tmax<=w`, (b) apply Theorem 2 to exclude entire subtrees, and (c) for remaining individual newer events certify nonmembership via two affine boundary noncollision checks. For an empty anchor winner, exclude all events. If every check passes, the latest source is w throughout I; otherwise report `INCONCLUSIVE`. An exact boundary equality is treated separately according to half-open membership, not silently identified as stable.

Certificates for a parent interval can be reused for contained intervals on the **same immutable event set**. To certify a parameter interval with a different nominal anchor, the conservative prototype rebuilds the nominal-phase index and counts every rebuild. More efficient certificate transport is left to R67.

## Author verification (exact rational arithmetic)
The local full program `check_r66.py` used only Python integer and `fractions.Fraction` operations, deterministic seed 20261111, and an independent direct historical-label assignment oracle. Its executed evidence bundle is `R66_RESEARCH_BUNDLE.zip` in the conversation artifact, and an independent compact regression is in this PR.

* 220 random models, 12,100 branch insert/delete operations, 1,100 immutable-root snapshots, 4,400 interval queries. Of these 4,397 were certified and checked at 5 exact rational points each; 3 returned inconclusive.
* 4,304 subtree exclusion successes covering 11,651 source-event occurrences, 2,345 time prunes, 2,582 individual leaf tests, 8,564 subtree attempts and 14,423 nominal node visits. A per-newer-event baseline would inspect 11,494 newer event occurrences (22,988 boundary tests), but these counts are of **different arithmetic operations** and are not a measured full bit-cost improvement.
* On 100 events with timestamps around `10^18`, 17 of 17 label queries certified exactly (60-bit time inputs and an 87-bit rational parameter endpoint denominator).
* Frozen S23 rational anchor `p=262204504569236716045286`, `q=10^24`, `m=128,H=225`: labels `0,31,63,127` certified and independently checked; no full 78-stage risk recompilation in this run.
* The R64 witness with `theta0=1/30`, `theta1=1003/30000`, timestamps `{9,15,6042}` and label z=12 changes latest time from 6042 to 15. Depth-6 adaptive bisection returned 8 certified cells and 2 inconclusive cells after 57 event reinsertions; it did not certify the changing whole interval.
* A distinct same-time branch deletion retains the other branch and all prior versions. A two-event internal phase-order reversal still passes a whole-subtree exclusion certificate.

**Claim status:** authored constructive proof plus exact finite computational tests. No independent mathematical review, shared CLAIM, theorem admission, or X6 ontology revision is claimed.

## R67 open work
Cache exclusions by immutable subtree identity, original label, observation configuration and parent certified interval; reuse only for subinterval containment and unchanged subtree membership. Compare *complete* cost (input phases, build, allocations, bigint operand widths, certificate, leaf fallback, output, oracle) with R62/R64 linear checks and R63 nominal query on matched query families. Test exact collision-root cells and large-time sparse labels.