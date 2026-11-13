# R64 — selective interval certificates and branch-faithful source index

2026-11-11 | Researcher-ID `EM-DIRECT-E75625` | Research-Activity-ID `RA-3AE5D6FCA0C04F1999E69F27`. Continuation of R63 author-side Draft PR #2060. Frozen scientific input commit: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Proof mode: exact rational auxiliary circle-rotation model; mathematical acceptance/independent review pending. P000, six-dimensional native space, independent time, and native BRC rules unchanged.

## Setup

Let `I=[L,U] subset (0,1)` be a closed rational interval, `theta0 in I`, `m>=2`, observation `j in Z, x in Q/Z`, and a finite event set `S subset Z x BranchID` with `t<j`. The indexed history points `h_z(theta)={z theta}` for `0<=z<m` are assumed pairwise distinct at `theta0`. Their counterclockwise half-open arcs `A_z(theta)` retain original label `z`. Define
```
tau_z(theta) = min {j-t : (t,b) in S, {x+(t-j)theta} in A_z(theta)}
```
with `EMPTY` if no matching event. `{ }` denotes fractional part in `[0,1)`.

## Theorem A: selective certification of a sparse original-label observer

At `theta0`, order history labels cyclically as `z_0,...,z_{m-1}` and let `z_next` be the immediate successor of selected label `z`. Compute `t_star`, the maximum timestamp contributing to `z` at `theta0`, or `EMPTY`. Suppose:

1. For every initially consecutive cyclic boundary pair `(a,b)`, the affine function `(a-b)theta` avoids all integers on `I`.
2. For `t>=t_star` (if there is a winner), or for all event timestamps (if none), each function `x+(t-j-v)theta`, for both `v=z,z_next`, avoids all integers on `I`.

Then `tau_z(theta)=tau_z(theta0)` for **every real** `theta in I`. In particular an irrational parameter lying in `I` receives the same certified sparse answer, even if phases of unexamined older events change their order.

**Proof.** The cyclic order of continuously moving labelled history points can change only at a collision. The first collision is between an initially adjacent cyclic pair, because the initial order is unchanged until that first collision. Hypothesis 1 forbids such a collision. Therefore the selected arc has the same two labelled endpoints for the entire interval. For a source at time `t`, membership in that arc changes only at a collision with an endpoint; equality with endpoint `h_v` means `x+(t-j-v)theta in Z`. Hypothesis 2 keeps all inspected source memberships unchanged. The nominal winner remains eligible and every newer source remains ineligible. Older events cannot improve the maximum timestamp. If no winner exists, all sources remain ineligible. Thus the latest-age answer is constant. QED.

The sufficient **integer-avoidance test** for an affine rational function `f(theta)=a+b theta` is: evaluate `v=f(L)`, `w=f(U)` exactly, require both nonintegral and `floor(v)=floor(w)`. Its image is an interval containing no integer. A failed test is `INCONCLUSIVE`, not a counterexample. Tests are finite rational integer operations and certify all real parameters in the interval by linearity.

For `n` active events and `c` newer events than the selected winner, a nominal R63 range maximum takes expected `O(log n)` node operations under its fixed independent-priority model; the history cyclic certificate takes `m` affine tests and the local certificate at most `2(c+1)` tests after time-indexed enumeration (deduplicate equal timestamps). If timestamps are stored in a second ordered index, that enumeration costs `O(log n+c)`; a phase index alone might require scanning `n` timestamps. These are **operation counts**, not bit-complexity upper bounds: exact products, denominator sizes, sorting, index construction, certification and output materialization all contribute.

## Theorem B: visited-key comparisons do not certify a rekeyed persistent tree

Set
```
theta0 = 1/30, theta1 = 1003/30000, m = 13,
j = 10000, x = 8/15, z = 12, S={9,15,6042}.
```
The R63 query offset `b={x-j theta}` is `1/5` at both parameters. The translated arc `A_12-b` is `[1/5,4/5)` at `theta0` and `[503/2500,4/5)` at `theta1`. Source phases are:

| timestamp | theta0 phase | theta1 phase |
|---:|---:|---:|
| 9 | 3/10 | 9027/30000 |
| 15 | 1/2 | 15045/30000 |
| 6042 | 2/5 | 126/30000 |

At `theta0` a valid ordered tree can have root `t=15`, left child `t=9`, and the right child of `t=9` equal to `t=6042`. A range-max query visits only root 15 and lower-bound spine node 9 and absorbs the unvisited right child's cached maximum 6042. Both visited nodes stay inside the translated query arc at `theta1`, so their comparisons remain unchanged, but timestamp 6042 moves outside the arc. The correct maximum moves from 6042 to 15; retaining old topology/aggregate after even a naive phase-field rekey would still return 6042. Thus inspecting the query's literal visited comparisons does not suffice to transport a tree across parameters. Theorem A certifies the **candidate value** instead and rejects this interval when the old winner crosses a labelled boundary.

## Frozen split witness

Let `p=262204504569236716045286, q=10^24`, `I=[p/q,(p+1)/q]`, `m=2`, `j=q+2`, `x=0`, sources at `t=j-1,j-q`. For `theta_a=(4p+1)/(4q)`, the full age vector is `(EMPTY,1)`. For `theta_b=(4p+3)/(4q)`, it is `(q,1)`. Nevertheless `tau_1(theta)=1` throughout `I`; Theorem A needs only two historic-neighbor and two winner-to-boundary affine checks. The old event of age `q` is not inspected. This is an exact selective-observer certificate with changing full state.

## Theorem C: branch typing and safe max-time quotient

At fixed parameter/query, the scalar age observer factors through the maximum eligible timestamp. The persistent carrier may contain several events `(t,branch_id)` at identical phase and time. It must retain those branch IDs (or a provably equivalent identity map) for subsequent arbitrary deletion by identity. Example `theta=2/7, j=20` and three events `(1,old),(8,alpha),(8,beta)`, all with equal phase: the common-arc minimum age is 12; deleting `(8,alpha)` leaves 12, deleting `(8,beta)` next gives 19, and deleting `(1,old)` gives `EMPTY`. Therefore the scalar quotient is sound for the stated current readout but is not a complete state for branch-specific deletion.

Implementation: use fixed-parameter ordered key `(phase,t,branch_id)`, subtree timestamp-max aggregate for age-only queries, and full-key deletion; path copy preserves earlier versions. Parameter transport uses Theorem A or a correctly reindexed tree.

## Exact tests, scope and next question

Ran `check_r64.py` with Python 3 `Fraction`, fixed random seed: **399** random small rational interval models; **268** sufficient certificates, **131** inconclusive; **2,412** independent exact endpoint/intermediate observer checks for certified cases. Frozen S23 split, stale-index counterexample, and same-phase branch-deletion assertions all passed. See `R64_CERTIFICATE.json` and separately executed compact `check_r64_min.py`. Finite tests corroborate, while the interval theorem follows from the elementary proof.

The carrier is the source/event provenance relation and persistent version; observer is a selected labelled latest age; future operations can include branch-specific deletes. This applies the project's BRC observer/retention discipline by preserving all branch identities, without asserting new native BRC algebra or X6/heartbeat dynamics.

**Next R65:** add subtree exclusion certificates over parameter intervals, proving when a whole immutable subtree's reachable phase set stays disjoint from the moving selected arc; compare exact bit costs versus enumerating all newer timestamps, and support adaptive interval bisection/version checkpoints.