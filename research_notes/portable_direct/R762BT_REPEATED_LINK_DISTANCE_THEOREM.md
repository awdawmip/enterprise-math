# R762BT — Exact arbitrary-noise distance for repeatable BRC named-Link observations

Date: 2026-11-16 (Asia/Shanghai). Status: **AUTHOR-PROVED, EXACT FINITE CHECKS; NOT_REVIEWED**.

Task provenance: RS-X6-TRIADIC-CLOSURE-DYNAMICS / TP2-8B7E13C5904A2D6F1142. Frozen project science: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json`; current behavioral rules are independently loaded. Immediate model predecessor: R762BS, Draft PR #2527, commit `b22458fa507d89e8300b87a54bded0ade3ba9c1b`. Distinct-name (no repetition) R762BS budget is `N(1..6)=(5,6,10,12,15,16)`.

## Definition and exact problem

The carrier consists of the 40 permutations of six named Ports having directed cycle structure (3,3): two *unordered* directed triadic cycles. BRC branch weights are positive rational `1/1`, with branch identity and provenance retained. Conditioning on the previously observed trusted named Link `1→2` leaves precisely eight distinguishable sources `U`. A named atomic query `Q_(a,b)(σ)=1{σ(a)=b}` has an independent Boolean answer **on every call**. The same query name may now be called repeatedly, and a single adversarial error changes at most one recorded answer bit. This relaxes exactly the `each name at most once` resource contract of R762BS; no assumption is made that repeated errors are independent or stochastic.

Among all named Link tests, 20 are nonconstant and realize 16 distinct positive two-source truth sets. Their incidence graph on the eight sources is `K_{4,4}`. Choose a name for each edge, and let `w_{uv}∈ℤ_{≥0}` count how often that edge predicate is queried (including repetitions). Every integer multiplicity is implementable by repeating the chosen named query. The total cost is `m=Σ_{u∈L,v∈R} w_{uv}`. The resulting binary observation code has distance

`d_w(u,v)=deg(u)+deg(v)-2w_{uv}` for `u∈L,v∈R`, and `d_w(u,u')=deg(u)+deg(u')` for two vertices on the same side, with an analogous formula for `R`.

We minimize `m` over **all** nonnegative integer multiplicities with minimum pairwise Hamming distance at least `q≥1`, not merely over fixed-size nonrepeated panels.

## Theorem — Complete unbounded integer resource formula

Write `q=6k+r`, where `k≥0` and `0≤r≤5`. Let `N_*(q)` be the minimum number of repeatable named-Link calls. Then, for all integers `q≥1`,

| Residue | Exact minimum `N_*(q)` |
|---|---:|
| `r=0` | `16k` |
| `r=1,k=0` | `5` |
| `r=1,k≥1` | `16k+4` |
| `r=2` | `16k+6` |
| `r=3` | `16k+10` |
| `r=4` | `16k+12` |
| `r=5` | `16k+15` |

Every value is realized by an explicit labelled integer query panel. Thus `N_*(7)=20`, `N_*(9)=26`, `N_*(11)=31`, `N_*(13)=36`. In particular an arbitrary three-bit error is correctable after **20** Link calls under this repeated-call interface, while R762BS's twenty distinct names (one call each) have maximum distance six.

### Universal lower bound

Let `d_{ij}=deg(L_i)+deg(R_j)-2w_{ij}≥q`. Summing across all 16 cross-part source pairs gives the exact identity

`Σ_(i,j) d_{ij}=6m`, hence `m≥ceil(8q/3)`.

Define nonnegative row/column excesses
`E_i=Σ_j(d_{ij}-q)=2deg(L_i)+m-4q`,
`F_j=Σ_i(d_{ij}-q)=2deg(R_j)+m-4q`.
Their common total is `6m-16q`. These integer identities yield the sharp residue refinements:

* `q=6k`: averaging immediately gives `m≥16k`.
* `q=6k+1`: averaging gives `m≥16k+3`. At equality the total excess would be 2, but each of four nonnegative `E_i` is odd and hence at least 1. Therefore `m≥16k+4`. For `q=1` even four queries fail: each query is true on exactly two states, so the sum of Hamming weights of eight codewords is 8; eight *distinct* words of length four have minimum total weight `0+4·1+3·2=10`. Therefore `N_*(1)≥5`.
* `q=6k+2`: averaging gives `m≥16k+6`.
* `q=6k+3`: averaging gives `m≥16k+8`. If `m=16k+8`, every cross distance equals `q`, forcing all row and column degrees to be `4k+2` and every `w_{ij}=k+1/2`, impossible. If `m=16k+9`, excess totals 6 and all four row and column excesses are positive odd integers: their sorted pattern is `(1,1,1,3)`. Three ordinary rows and three ordinary columns have degree `4k+2`; one exceptional row and column have degree `4k+3`. For any ordinary row, a cross-distance bound permits at most `k` units on each of the three ordinary columns and at most `k+1` on the exceptional column. Its degree would be at most `4k+1`, contradiction. Hence `m≥16k+10`.
* `q=6k+4`: averaging gives `m≥16k+11`. At that value excess total is 2, but all four row excesses are positive odd integers, contradiction. Hence `m≥16k+12`.
* `q=6k+5`: averaging gives `m≥16k+14`. At that value excess total is 4 and row/column excesses are nonnegative even integers; at least two rows and two columns have zero excess. A zero-excess row has degree `4k+3`. Against a zero-excess column, the cross-distance constraint bounds multiplicity by `k`; against each of at most two positive-excess columns it bounds multiplicity by `k+1` (their degrees are at most `4k+5`). The selected row can have degree at most `4k+2`, contradiction. Hence `m≥16k+15`.

These arguments hold for arbitrary nonnegative integer edge multiplicities, including arbitrarily repeated queries.

### Explicit sharp constructions

Index the bipartition of the eight conditioned source branches as `L_0,…,L_3` and `R_0,…,R_3`. An edge `(i,j)` means the predicate true at precisely `L_i,R_j`. All constructions use **actual named predicates**, as reconstructed by the verifier from the six-axis cycle permutations.

For `q=1,2,3,4,5,6` use respectively:

* `q=1`: a three-edge path `L0–R0–L1–R1`, a two-edge path `L2–R2–L3`, and isolated `R3` (5 calls).
* `q=2`: two disjoint three-edge stars with centres `L0` and `R0`; connect each centre to the other side's three noncentral vertices (6).
* `q=3`: two complete `K_{2,2}` off-diagonal blocks (8 edges), and a two-edge matching across the complementary diagonal high-degree block (10). The degrees are `(3,3,2,2)` on each side; every observed cross-edge has distance at least 3.
* `q=4`: all 16 edges except the four edges of a perfect matching (12).
* `q=5`: all edges except `(0,0)` (15).
* `q=6`: all 16 edges (16).

For `q=6k+r` with `k≥1`, first query **every** one of the 16 edge predicates `k` times. This adds exactly `6k` distance to every cross-part state pair and `8k` to every same-part state pair. For residues `r=2,3,4,5`, append the respective base `r)-panel above, attaining `q`. For `r=1`, append just the four edges incident with `L0`: cross-part distances gain at least 1; same-part distances are at least `8k≥6k+1`. For `r=0` the baseline suffices. The constructions achieve the lower bounds in every residue.

## Corollary — Sharp unbounded signed-source fault budgets

Extend the eight labelled triad branches by four independent hidden signs (Ports 3,4,5,6), exactly as in R762BS. Each sign has its own Boolean atomic query, now repeatable. For a fixed nonadaptive schedule and adversarial budget of `t` corrupted answers and `e` known erasures, put `q=2t+e+1`. The complete block observation distance is

`d_total = min(d_Link, n_3,n_4,n_5,n_6)`,

where `n_i` is the number of queries of sign `i`. Consequently the exact minimum number of atomic calls for all 128 signed source states is

`M_*(t,e)=N_*(2t+e+1)+4(2t+e+1)`.

For arbitrary flips only: `M_*(0,0)=9`, `M_*(1,0)=22`, `M_*(2,0)=35`, **`M_*(3,0)=48`**, `M_*(4,0)=62`, `M_*(5,0)=75`, `M_*(6,0)=88`. No independence or averaging of adversarial errors is used; each repeated call counts individually.

## Verification and future frontier

The self-contained JS program reconstructs all 40 triadic branch permutations, eight conditioned states, 20 informative named tests and their 16 distinct `K_{4,4}` edge predicates. It checks all `2^16=65,536` simple edge panels for the six base distances, validates the explicit formulas on 120 positive integer values of `q`, provides exact named witnesses at `q=7`, and checks signed budgets. All combinatorial operations use exact integer and Boolean arithmetic; the infinite-range optimality is proved by the lower-bound argument and the constructions above, not inferred from the 120 tested cases.

The source/verification boundary remains the conditional directed-Link oracle family, with a trusted fixed arrow, repeatable Boolean readings and arbitrary *per-reading* corruption. Native `TRIADIC_CLOSURE_E` Cell/Port/Link event permission and V17/V29/V39 transport must still determine whether this oracle and its repeated-call interface are genuinely available. Future BRC compression requires preservation of labelled source, query-frame and any future-relevant signed or ordered residue. The next discriminating research step is to intersect this exact integer distance design with the actual native event and permitted observation semigroup, retaining the original Task's frozen science and ownership contracts.
