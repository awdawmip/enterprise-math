# R280 — Exact edit-word reachability, first-visibility depth and scoped Port-edge deletion

Date: 2026-11-18. Status: **AUTHOR_PROVED / EXACT_FRACTION_CHECK / NOT_REVIEWED**.
Source frontier: R278/R279 at `791d393652f54411d499b742c3def572676887a7`; science freeze `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Typed scope: finite stable nonnegative-rational **labeled visible BRC Port** matrices under WBRC-T30–T32; one fixed visible star observer; only specified nonnegative-rational named edge additions. P000 and ACTIVE worldview remain unchanged. Existing R278/R279 statements are dependencies, not re-proved or superseded.

## 1. Precise model and new result

Let `W in Q_>=0^(n*n)` have row sums strictly below one; `S=(I-W)^(-1)`. Fix a visible port `r`, and `m>=1` named update types `e_i=(u_i,v_i)`. Set `E_i = e_(u_i) e_(v_i)^T`. For rational `x_i>=0` preserving stability, put

`F(x)=[I-W-sum_i x_i E_i]^(-1)_(r,r)`.

Define an **edit-transfer digraph** `H` with one vertex per named edit type (repeated locations remain separate labels). A vertex `i` is an initial vertex when `S_(r,u_i)>0`, terminal when `S_(v_i,r)>0`, and it has an arc `i->j` precisely when `S_(v_i,u_j)>0`. Because `W>=0` and is stable, `S_(a,b)>0` is equivalent to the existence of a baseline directed path `a -> b` (a zero-length path is allowed).

**Theorem R280-A (exact rational edit-word expansion).** In a nonempty neighborhood of the origin, the expansion is

```
F(x) = S_rr + sum_(d>=1) sum_(i_1,...,i_d in {1,...,m})
   [S_(r,u_i1) S_(v_i1,u_i2) ... S_(v_i(d-1),u_id) S_(v_id,r)]
    x_i1 ... x_id .
```

Every coefficient is nonnegative rational. For any multiindex `nu` with total degree `d`, its exact coefficient is the sum of the displayed bracketed weights over all edit words having label multiplicities `nu`. It is positive iff some such edit word follows an initial-to-terminal walk in `H`. Thus every nonzero mixed coefficient has a literal baseline-path / named-edge witness; no cancellation is possible in this **positive-weight** BRC observer.

**Theorem R280-B (polynomial-time first visibility).** If the transfer digraph has no directed walk from an initial vertex to a terminal vertex, `F(x)=S_rr` for *all* permitted stable update vectors, not only infinitesimally. Otherwise, the shortest initial-to-terminal walk length `d_*` is the exact smallest total degree of a nonconstant monomial in the Taylor expansion of `F`. In particular `1 <= d_* <= m`. The answer is obtained by ordinary breadth-first search in the `m`-vertex transfer digraph, after the exact baseline Green matrix has been computed. This is a structural visibility test, not an all-coefficient / bit-complexity bound.

**Theorem R280-C (which edge labels can be erased for this one observer).** Let `R` be vertices reachable from *some* initial vertex, and `T` vertices that can reach *some* terminal vertex. Exactly the edit labels in `R intersect T` occur in a nonzero coefficient of `F`. For every label outside this intersection, `F` is independent of its coordinate at every admissible stable update. Deleting those labels is an **exact future-observer-safe quotient only for the fixed scalar star and declared update alphabet**; their effects on other Port readouts, original provenance, or loop-zeta are not erased.

Each relevant edit `i` occurs in a positive coefficient of total degree at most `2m-1`. Indeed, concatenate a simple initial-to-`i` path and a simple `i`-to-terminal path, each of length at most `m`, overlapping at `i`. This bound is attained already at `m=2`, as the five-Port witness below shows.

## 2. Proof

Write `A=I-W` and `Delta=sum_i x_i E_i`. Since `A` is invertible, the exact formal Neumann identity around `x=0` is

`(A-Delta)^(-1)=(I-S Delta)^(-1) S=sum_(d>=0) (S Delta)^d S`.

The `(r,r)` entry of the `d`th summand expands into the asserted ordered-word products. These are rational nonnegative products because `S=sum_(k>=0) W^k` has nonnegative entries. A product is positive exactly when each baseline Green entry it uses is positive. This proves A.

Specialize `x_i=q_i t` with *every* `q_i>0`. The coefficient of `t^d` is a positive linear combination of the length-`d` walk weights, so the first nonzero degree is exactly the shortest initial-to-terminal walk length. A shortest walk uses no repeated edit vertex and has length at most `m`. If none exists, all positive-degree Taylor coefficients vanish. `F` is a rational function, analytic on a nonempty neighborhood of zero; being locally constant it is identically constant as a rational function wherever defined. In particular it is constant throughout the admissible stable rational domain. This proves B.

For C, a label occurs in some nonzero word precisely when a walk from an initial to a terminal vertex passes through it; equivalently, it is forward-reachable from initials and reverse-reachable from terminals. An irrelevant coordinate occurs in no Taylor coefficient; the rational identity argument makes independence global on the stable domain. For a relevant label concatenate shortest simple paths on either side to get a word of at most `2m-1` symbols containing that label. This proves the remaining assertions.

## 3. Exact counterexamples / sharpness

**R279 joint-only cycle recovered.** Take `W=0` on Ports `0,1`, observer `r=0`, edit labels `A:0->1`, `B:1->0`. The transfer graph starts at A, ends at B, and has `A->B`; thus `d_*=2`, with

`F(x_A,x_B)=1/(1-x_A x_B)`.

Both singleton edits are observationally invisible; their joint cycle is visible. With `x_A=x_B=t`, the series is `1+t^2+t^4+...`.

**A label first appears at `2m-1=3`.** Use 5 Ports, observer `r=0`, baseline edges `0->1, 2->0, 2->3, 4->1`, all with weight `1/8`; the only editable edges are `A:1->2`, `B:3->4`. The transfer graph has initial/terminal A, arcs `A->B` and `B->A`, and B is neither initial nor terminal. The *earliest* monomial containing B is `x_A^2 x_B`, with strictly positive coefficient `1/4096` (ordered word A,B,A). No term containing B has total degree one or two. Thus the stated per-label `2m-1` bound is sharp for `m=2`.

**First jet is not a safe all-horizon quotient.** On Ports `0,1,2`, fix baseline `0->1=1/4`, `2->0=1/4`, `2->1=gamma` with `gamma in {0,1/4}`; observer is 0 and the only editable edge is `1->2` of weight x. Direct inversion gives

`F_gamma(x)=(1-gamma*x)/(1-(gamma+1/16)*x)`.

Both models have the same initial readout `1` and identical first derivative `1/16`. Their second Taylor coefficients are `1/256` versus `5/256`; at admissible `x=1/4`, their outputs are `64/63` and `60/59`. All-horizon prediction requires the higher recurrent feedback information.

**Exact scoped label deletion.** On 4 Ports, baseline `0->1=2->0=1/4`; editable edges are `A:1->2`, `B:3->3`, `C:2->3`. For readout `S_00`, only A lies on an initial-to-terminal walk; B and C have no return route. At edit values `(1/4,1/3,1/5)`, deleting B,C leaves the readout unchanged at `64/63`. The theorem covers every admissible update vector, not just this witness.

## 4. Computation, reuse, and scope

`R280_port_walk_visibility_checker.py` uses Python stdlib exact `fractions.Fraction`. It independently calculates Taylor coefficients in two ways: by exact matrix-product recurrence `(S E)^d S` and by enumeration of labeled edit words through degree 5. For each tested model it checks graph BFS against the first nonzero coefficient; it checks first appearance by individual label, direct inverses of the rational witnesses, row-sum stability, and the sharp mixed coefficient `1/4096`. Four model families are checked, including the two variants of `gamma`; the saved JSON is the exact run output. This computation checks the stated finite examples. The universally quantified assertions follow from the symbolic proof in sections 1–2.

This is a specialized algorithmic reachability/observer result built upon the prior classical Green-function/Neumann identity and the project-specific typed BRC port language; no claim of novelty for the underlying resolvent expansion. It complements rather than replaces R278's complete rational-function observer signature or R279's finite-edit hierarchy. Positive rational mass matters: signed/phase path cancellation invalidates the positivity implication.

Next: implement a *multi-output* reachability quotient using all declared star outputs; study how prime-adic cancellation can alter the order/valuation of the first nonzero observation even when the positive rational coefficient exists; test whether R269 auxiliary source-label classes admit a typed Port mapping preserving provenance and future operations. Activity/native CLAIM association remains separate from GitHub proof publication.
