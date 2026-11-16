# R762CE — Exact budgeted BRC law-fiber repair under restricted Boolean interrogation

**Task:** RS-X6-TRIADIC-CLOSURE-DYNAMICS; continuation of R762CD (PR #2561).
**Scientific input:** frozen P000/Task pin `a72226e2430ffa4786321ac86e7f0c599d5f0389`; R762CD policy model at `24721420807392cf3e18a9dec3a83bd0f2627ac9`.
**Evidence:** exact finite combinatorial census and fully reproducible independent Python 3 validator; author-checked, independent review NOT_REVIEWED.
**Scope:** the explicitly conditional sign-only, `S6 × C3`-covariant three-Port law space; Boolean oracle tests are model questions, not an assertion of native executable Cell events.

## Model and question

For four cyclic sign-orbits indexed 0,1,2,3, let rooted permission counts be `r=(1,1,3,3)` and sign-word weights `w=(1,1,3,3)`. Each orbit has state `-1` (EXCLUDED, all gates zero) or a CLOSED root-gate mask `0..2^r_i-1`. There are `(1+2)^2(1+8)^2=729` coherent laws.

The aggregate all-length return observer `A` is equivalent (by R762CB) to `n=(n_0,n_1,n_2,n_3)`, where each CLOSED orbit contributes weight `w_i` to `n_{popcount(mask)}`. Exactly 90 observer fibers occur. Let `Q` be the 12 single-atom tests ordered
`C0,C1,C2,C3,g00,g10,g20,g21,g22,g30,g31,g32`.
Fix a known `A` class and a query budget `q`. An observer-conditioned nonadaptive protocol may select at most `q` distinct atoms and read their Boolean answers simultaneously. The residual indistinguishability is the maximum number of laws in one answer fiber. A protocol may depend on `A`, but not on the unknown law. Define `M_q` to be the maximum, over all possible A classes, of the minimum residual indistinguishability under such protocols.

## Theorem — sharp finite-budget rate curve

For every integer `0 <= q <= 6`,
```
M_q = ceil(36 / 2^q).
```

| q (atom queries) | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| optimal worst residual laws | 36 | 18 | 9 | 5 | 3 | 2 | 1 |
| guaranteed remaining fixed-width repair bits | 6 | 5 | 4 | 3 | 2 | 1 | 0 |

In particular, three selected Boolean probes narrow every law fiber to at most five coherent candidates, even when the initial A observation has 36 candidates. Exactly six probes are necessary and sufficient for worst-case zero-ambiguity law restoration, recovering the q=6 endpoint of R762CD. The values for 1..5 are new budgeted precision points.

The same sharp global curve holds if queries are allowed to be adaptive, since the information-theoretic lower bound applies to *all* binary decision trees and a nonadaptive construction attains it.

### Proof of lower bound

The class `n=(1,3,3,0)` contains 36 coherent laws. Indeed, choose which of the two homogeneous sign-orbits is CLOSED(0) (two choices), assign the mixed sign-orbit closure types `k=1,k=2` to the two mixed orbits (two choices), and select one of three masks of the prescribed type in each mixed orbit (3×3 choices). These choices are disjoint and exhaustive by sign-word weights and total closure contribution. Thus `|A^{-1}(1,3,3,0)|=2·2·3·3=36`. After q binary answers, at most `2^q` outcomes exist, so some answer fiber has at least `ceil(36/2^q)` laws. This applies equally to adaptive protocols.

### Constructive finite upper certificate

The attached JSON lists, for each of the 90 exact A fibers and each `q=0..6`, a 12-bit selected-query mask `m` and its exact maximum answer-fiber cardinality `b`. Enumerate all 729 state tuples, compute A and the 12-atom answer word for each law. For each fiber `F`, all `binom(12,q)` distinct q-atom subsets are inspected; the verifier computes
```
b(F,m)=max_v |{x in F : (atom_bits(x) & m)=v}|.
```
It validates the supplied certificate mask, independently rederives the minimum over all subsets, and checks that the maximum over the 90 fiberwise minima is exactly `ceil(36/2^q)` for every q. This is a complete finite proof: there are no continuous, probabilistic or floating-point assumptions.

For the 36-law fiber `(1,3,3,0)`, one sequence of sharp query sets at q=0..6 is:
```
[]; [C0]; [C0,g21]; [C0,g21,g30];
[C0,g21,g22,g23]; [C0,g21,g22,g23,g30];
[C0,g21,g22,g23,g30,g31].
```
The labels here are interpreted in the machine ordering above: `g21,g22,g23` correspond to positions 6,7,8 (zero-based 3-gate orbit 2); `g30,g31` correspond to positions 9,10 (orbit 3). The full certificate uses exact numerical bit positions, to avoid any naming ambiguity.

The exhaustive verifier also records the per-class residual-size histograms at each budget. All calculations use exact integers and sets.

## Interpretation and next science

This theorem measures a *source-law* BRC repair tradeoff, not full Cell/Port/Link state reconstruction. A class-dependent optimal interrogation strategy can steadily decrease the maximum possible law-state residual; it does not erase the actual sign, geometry, path order, branch provenance, time or holonomy. Its atom oracle is an abstract logical interface.

The task's hard target now requires a native `TRIADIC_CLOSURE_E` event-licensing rule on signed Cells and Links, a certified mapping of native transitions into V17/V29/V39, and a test whether the licensed rule family factors through these 12 sign-only atoms. If not, enlarge the source-state/observer alphabet and recompute this rate curve under the actual event language.

**Source provenance:** frozen P000 V5; `definitions/P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md`; `definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json`; V17 conditional shared-axis holonomy; R762CA–R762CD. Review: NOT_REVIEWED; no Task Result or Foundation promotion.
