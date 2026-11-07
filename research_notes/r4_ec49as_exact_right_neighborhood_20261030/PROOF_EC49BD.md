# EC49BD — exact all-real causal BRC optimum for 11/25 ≤ η ≤ 99/200

**2026-10-30 | AUTHOR_ANALYTIC_PROOF / EXACT_FRACTION_SYMPY_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED.** All claims concern the strictly-positive **auxiliary probability BRC observer**, not native signed/phase BRC, X6, three-dimensional slice, Heartbeat World, or empirical quantum physics. This work independently audits and strengthens the EC49AV sparse-to-edge reduction under its exact noninteger first-cost premise; formal/independent mathematical review is pending.

## 1. Frozen model and exact theorem

Hidden `w=0,1,2` is uniform. First action `c∈{0,1,2,3,STOP=4}` has costs `(1,1,2,2,0)`. A row-stochastic `x[w,c]` has expected first cost `C1=43/48`, i.e. `sum(w,c) cost[c]*x[w,c]=43/16`. The first observation `u∈{0,1}` occurs with `Pr(u|w)=1/2+(2u-1)(1-w)η`. Sensor mass and support on paid action `c<4` are

`q_z(c,u)=x[z,c]Pr(u|z)/3`, `T(c,u)=sum_z q_z(c,u)`, `V(c,u)=sum_z [43q_z(c,u)-16T(c,u)]_+/172`.

The independent purchasing coin `p(c,u)∈[0,1]` and final acceptance can depend only on **observed** `(c,u)` and, when purchased, `(c,u,z)`; hidden `w` cannot be used at either decision. The exact paid mass is `sum_(c<4,u) p(c,u)T(c,u)=C2=13/16`; after optimally accepting positive-score bought events the target is `H=α-(177/172)β=sum pV`.

**Theorem (all real policies, all real η in this interval):**

```
Hmax(η)=[2752η²+42η+1397−172(1−2η)√(19−26η)]/[8256(1+2η)],
                                    11/25 ≤ η ≤ 99/200.
```

The attaining first-action rows, with `t=(27−10η−4√(19−26η))/(8(1+2η))`, are

```
x[0,:]=((11−8t)/16,0,t/4,0,(5+4t)/16),
x[1,:]=(0,1,0,0,0), x[2,:]=(1,0,0,0,0).
```

Buy every positive-mass paid observable fiber except `(c,u)=(0,1)`, where `p(0,1)=(8η+√(19−26η))/(4(1+2η))`. On purchase accept exactly `(c,u,z)∈{(0,0,2),(0,1,0),(1,0,1),(1,1,1),(2,0,0),(2,1,0)}`. The displayed formulas and constraints imply `3/4<t<4/5`, `0<p(0,1)<1`, both exact costs, and lawful observation-only decisions. At η=11/25 this agrees with EC49BC.

## 2. Sparse-to-edge representative theorem — new explicit rank audit

The strategy space is compact; `H` is continuous and hence has a maximizer. Fix one maximizing `p`. In `x` the three row sums, first cost, and paid-purchase mass are linear equality constraints and `H(x,p)` is convex, being the sum of positive parts of affine scores with fixed `p`. A maximizing vertex of this polytope has **at most five positive** entries. Fix such an `x`; `p` is a box-constrained linear one-resource knapsack so can be replaced by an optimal vertex with at most one fractional positive-mass fiber, preserving `x` and the value.

**Key missing-face argument.** Consider the support `S` of this at-most-five-supported `x`, and the *original* first-stage polytope `P` with three row sums and the single first-cost equation. On the support, the three row-sum rows are linearly independent. If the cost row belonged to their span, every supported action within any row would have the same integer action cost (one of 0,1,2). All three rows sum to one, so total first cost would then be an **integer**, contradicting `43/16`. Consequently the four constraint rows are independent on `S`; the smallest supporting face of `P` has dimension `|S|−4 ≤ 1`. Thus this `x` lies on a **vertex or an edge of P**. This is the needed justification for searching original edges, and it relies essentially on the noninteger cost `43/16` (it is not a universal rank claim at integer first-cost targets).

## 3. Exhaustive finite geometric domain

`P` is the intersection of the product of three 4-simplices with a hyperplane whose level `43/16` is noninteger and misses all 125 pure-action vertices. A slice vertex is therefore exactly the intersection with an original 1-face. A slice edge is exactly the intersection with an original 2-face: a row triangle or a two-row square. Exhaustively enumerate the 2250 original 2-faces, generate exact rational crossings, deduplicate. Output is **168 distinct vertices, 924 edges**. Since STOP removes paid mass and maximal possible sensor mass along an edge is affine, **720** edges have mass <13/16 everywhere, while **204** are potentially feasible. Clip those 204 edges at paid mass =13/16; exactly **8** have exceptional five-supports and **196** are ordinary. All enumeration, equality, support and clipping checks use `fractions.Fraction`.

## 4. Certified ordinary-edge bound on an entire η interval

For any `λ≥0` and first-stage `x`, the one-resource purchase knapsack has valid upper bound

`Dλ(x,η)=λ(13/16)+sum_(c<4,u)[Vη(c,u)-λTη(c,u)]_+ ≥ H(x,p,η)`.

Fix `η_i≤η≤η_(i+1)` and one clipped ordinary edge `x=θx0+(1−θ)x1`. The author-side verifier constructs an **exact nonnegative rational λ**, separately for each of 196 edges and 11 parameter slabs, satisfying all four exact inequalities

`Dλ(xj,ηk) ≤ Bk := H_exceptional(t_k,η_k)` for `j∈{0,1}, k∈{i,i+1}`.

Here rational knots are

`11/25,9/20,23/50,47/100,19/40,12/25,97/200,39/80,49/100,197/400,79/160,99/200`,

and rational comparison strategies `t_k=77/100` on the first five knots and `t_k=19/25` on the last seven. The checker exhaustively constructs the price from the exact piecewise-affine breakpoints `V/T` and verifies 2156 multipliers × four corners = **8624 exact inequalities**, with minimum slack `9062167/8412406320000>0`. The complete 227,222-byte verbose rational price list is generated by `VERIFY_EC49BD.py --prices` (SHA256 `1dc3bdf9981c8533967886492c6bf0d9a884fa10ae608611eb38e30b06557162`). The **entire ordered list of 2,156 rational dual prices** is also independently stored losslessly as `EXACT_ONLY_PRICES_EC49BD.json.gz.b64` (decoded JSON SHA256 `20de2796efa75964b6e18481f3222c271fe966f0e42d605769dc066f5fe49741`), and the separately executed `VERIFY_STORED_PRICES_EC49BD.py` checks all 8,624 four-corner inequalities *without searching for prices*, reproducing the exact minimum slack. The separate stored ledger omits redundant edge labels/slacks, which are reconstructed from the deterministic ordering in the verifier.

At fixed λ, `Dλ` is convex in `x` with η fixed, and convex in η with x fixed (separate convexity; **not** joint convexity). Twice applying Jensen yields `H ≤ chord(B_i,B_(i+1))`. By construction each `B_i≤F(η_i)`, where `F` is the theorem radical formula.

**Exact concavity of `F`.** Let `s=√(19−26η)`, `Q=1352η³+6084η²−14898η+7583`, `R=2496η−1824`. Symbolic differentiation gives

`F''(η)=−[Q(η)+R(η)s]/[48s³(1+2η)³]`.

For 11/25≤η≤1/2, `R<0` and `0<s<3`, so `Q+Rs > Q+3R = 1352η³+6084η²−7410η+2111`. This last cubic has negative derivative on the entire interval and equals **96** at η=1/2, so `F''<0`. Hence the chord of endpoint `F` is ≤ actual F at every intermediate real η. **All 196 ordinary edges lie strictly below F**, including every continuous η between knots, with no grid extrapolation.

## 5. Eight exceptional edges and attainment

The exact symbolic checker reconstructs `(T,V)` as rational-bilinear functions in `(t,η)` on all eight special edges and checks they have identical full multiset signatures (up to relabeling) for every real parameter, not just sampled values. For all atomic scores it checks exact rectangle corners `t∈{0,1}`, `η∈{11/25,99/200}` and proves the sign pattern by bilinearity. Structural zero scores are explicitly asserted to vanish identically. It checks five exact algebraic pairwise density identities, proving the `(0,1)` positive fiber has the smallest score-per-mass throughout the rectangle; other zero-score fibers are not purchased.

Thus for any special edge parameter `t∈[0,1]`, the optimal purchase with required mass 13/16 buys all other paid fibers and buys `(0,1)` at probability `p1=1−(1−t)/(12T1)`, with `T1=[27−10η−(8+16η)t]/96`. This is feasible on the entire parameter rectangle. Its best score is

`Hexceptional(t,η)=h(η)−[at²+bt+c]/[2064(d−ft)]`,

with `h=77/688+(674η−175)/16512`, `a=344(1−4η²)`, `b=2436η²+1568η−1201`, `c=2060η²−5096η+1769`, `d=27−10η`, `f=8+16η`. The derivative numerator is `N(t)=−aft²+2adt+bd+fc`, with `N'(t)=2a(d−ft)>0`. Exact identities at t=3/4,4/5 and their signs for η∈[11/25,99/200] ensure a unique interior global maximum. SymPy checks that the displayed `t*(η)` is stationary and substitution gives the exact `F(η)` for every real η in the interval. The explicit lawful policy reaches `F`; the ordinary edges cannot beat it; exhaustive edge and sparse-to-edge reduction finish the all-real result.

## 6. Reproduction, provenance and limitations

Run Python 3 with `fractions.Fraction` and SymPy 1.14.0:

```
python VERIFY_EC49BD.py > EXACT_REPORT_EC49BD.json
python VERIFY_EC49BD.py --prices > EXACT_PRICES_EC49BD.json
sha256sum EXACT_PRICES_EC49BD.json
```

Both modes were actually executed with exact algebra and outputs checked on 2026-10-30. Published raw-file SHA256 are documented separately; the GitHub `.py.gz.b64` and `.json.gz.b64` files are lossless base64(gzip(raw)); decode with `gzip.decompress(base64.b64decode(...))` before running. This is an author-side reproducible exact finite + symbolic proof; not an independently reviewed, native Source admitted, Lean-certified, signed/phase BRC, X6 or external-physics theorem.

GLOBAL_KNOWLEDGE_V1 pinned main `878381f97f807128125effc8aba26d32b7129768`, EM main `2fdba2f4e10aea0c41c4178535edcdf69bc92fbf`, predecessor PR #1730 HEAD `f72c321f97c5bdad7abbe026737d9fb10a7cef89`. P000 and ACTIVE worldview read-only. Native MCP v0.6.11 `authority_granted=false` and owner query `CONTROL_QUOTA`; no Source-native CLAIM, Result or independent Driver approval. Proposed next EC49BE: examine η∈(99/200,1/2] for a second strategy transition or extend the dual proof; do not equate failure of a particular dual certificate with a real strategy change.
