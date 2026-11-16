# EC49FRD — Three new exact BRC seams, 86-node certificate, and global joint optimal price-grid theorem

Date: 2026-11-17. Evidence: **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED**. Predecessor [EC49FRC PR #2601](https://github.com/awdawmip/enterprise-math/pull/2601) at immutable commit `1a06ad839737be59cf170725f94fed9046ac8d37`. Frozen science `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Portable independent research, without a formal Task CLAIM or Result.

## Exact task model
BRC native class 16943 has 310 original configurations, 141 complete named root profiles (multiplicity `m_i>0`, `Σm_i=310`), 228 physical labeled sensing actions (144 terminal + 84 root), 209 distinct partitions. Prior on profile i: `p_i(λ)=(1−λ)/141+λm_i/310`, real `λ∈[0,1]`. Root query cost `r=xt`, terminal `t>0`, `x≥1`. `V(x,λ)` minimizes cost over all finite legal separating adaptive decision trees without a depth cap. Feasible normalized costs:

```
A(x,λ)=(1−λ)(6x+290)/141 + λ(6x+751)/310
B(x,λ)=(1−λ)(5x+293)/141 + λ(5x+704)/310
C(x,λ)=(1−λ)(5x+295)/141 + λ(5x+685)/310
K(x)=7557−169x ; G(x)=310(3−x)/K(x) ; β=620/3299
```

## Theorem 1: Three new all-real-prior exact slices

Conditioned on the inherited 83-node exact endpoint collection and single-seam named-label exclusion lemma, for each of the following exact x and **every real** `λ∈[0,1]`, `V(x,λ)=t min(A,B,C)`. All optimal physical first-query labels are `{32,34}` for `λ<G(x)`, `{140,142}` for `G(x)<λ<β`, and `{16,23}` for `λ>β`. At the two seams, take the unions of adjacent labels.

| x | G(x) | Exact unscaled weighted-Bellman optimum at seam | Independent visited subsets | Native certificate SHA256 |
|---|---|---:|---:|---|
| 49/48 | 5890/70891 | 316598173920 | 6916 | `187b4ce31dd31fb84bc749cfa545fc6115334cd25070fe6d4123336b06427563` |
| 17/16 | 9610/118039 | 175812809760 | 6635 | `72a83171d89b0f3e1d61eaecfebd1f2c4e3639c952b9efc4e5da0e8fe63865ae` |
| 53/48 | 28210/353779 | 1581639706080 | 6428 | `128eeefb4c645d8c8c2c2176a31104f55bb7833cbaf947c91343dba6c3902239` |

**Proof.** Prices are respectively strictly interior to certified old intervals `[1,25/24]`, `[25/24,13/12]`, and `[13/12,9/8]`. At each new price, unrestricted weighted subset Bellman recursion over 141 complete named profiles and all 228 physical actions verifies the sole inner first-transition seam `λ=G(x)`, with all optimal first physical labels exactly `[32,34,140,142]`. A separately structured integer DP reproduces each optimum, and reconstructs and replays all four tied complete decision trees. For fixed price, the unrestricted optimum is the infimum of cost functions affine in λ, hence concave. Combine certified original interval endpoints and feasible A/B/C costs to close both sides of the new seam; the inherited second seam β and named-label exclusion lemma classify all labels. All assumptions inherited from PR #2601 are kept explicit. QED.

## Theorem 2: 86-node continuous enclosure

Let `P83` be the inherited 83 exact price nodes, `P86=P83∪{49/48,17/16,53/48}`. Put `D=2185500`. The uncertified-strip **upper enclosure area** of `[1,3]×[0,1]` is

```
S(P)=Σ_[a,b]adjacent (b−a)(G(a)−G(b))
    =D Σ_[a,b]adjacent (b−a)^2/(K(a)K(b)).
S83=44429865301826323916995/20209109482201273759125792
S86=10770320075410254305/5143575841741225186848
S83−S86=36425/348329424 >0
Certified fraction ≥ 1−S86/2
=10276381363407040119391/10287151683482450373696
=99.8953031858886303530159399645696709966...%.
```

The rigorous interval-regret envelope is `R(a,b)=50(b−a)/(sqrt(K(a))+sqrt(K(b)))²`. Independent rational sqrt brackets at `10^(−32)` resolution compare all 85 intervals strictly and identify the unique largest as `[19/8,77/32]`; the prior leader `[13/12,9/8]` was removed by the new insert. Hence for all real `x≥1`, `λ∈[0,1]`, `t>0`, with the inherited certified `x≥3` region:

```
0 ≤ t min(A,B,C)−V(x,λ)
  ≤ 0.0000546100750162483805137704802... * t.
```

The previous bound was `0.0000706655890435253982773667348... t`; the new bound is 22.72041349...% smaller. The exact enclosure area and radical comparisons are mechanically checked.

## Theorem 3: Globally jointly optimal m-interval price grid (new structure)

For any real `1≤a<b≤3` and integer `m≥1`, among **all** strictly increasing real price grids `a=x_0<...<x_m=b`, the same **unique** grid simultaneously (i) minimizes total uncertified-strip area `S=Σ(x_(i+1)−x_i)(G(x_i)−G(x_(i+1)))` and (ii) minimizes the maximum individual regret envelope `max_i R(x_i,x_(i+1))`. Let `ρ=(K(a)/K(b))^(1/m)>1`. The minimizing knots and optimum values are:

```
K(x_i)=K(a)^((m-i)/m) K(b)^(i/m), 0≤i≤m
S_min=(D/169²)*m*(ρ+1/ρ−2)
R_minimax=(50/169)*(sqrt(ρ)−1)/(sqrt(ρ)+1).
```

**Proof.** Write `k_i=K(x_i)`, `r_i=k_i/k_(i+1)>1`, and `y_i=log r_i>0`. Then `Σ_i y_i=L=log(K(a)/K(b))` is fixed. Each area contribution is exactly `(D/169²)(r_i+r_i^(−1)−2)=(2D/169²)(cosh y_i−1)`. Strict convexity of cosh for positive y and Jensen's inequality uniquely minimize the sum at every `y_i=L/m`. Also `R(x_i,x_(i+1))=(50/169)tanh(y_i/4)`, strictly increasing with `y_i`; the maximum is uniquely minimized at the same equal allocation of `Σy_i=L`. Substitution establishes both closed forms. For m=1 the endpoints fix the sole grid. QED.

Asymptotically, with L fixed as m grows, `S_min=(D/169²)(L²/m+L⁴/(12m³)+O(m^(−5)))`, and `R_minimax=(50/169)(L/(4m)−L³/(192m³)+O(m^(−5)))`. This analytically generalizes the previous single-insertion lemma. The result optimizes the **certificate geometry**; a new BRC optimality certificate at a generally irrational suggested knot requires a native exact Bellman proof or a valid rational approximation with its own seam certificate.

## Provenance and next unfinished unit

Source master SHA256: `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`; original profile CSV SHA256: `a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f`. All original profile multiplicities, 228 physical action labels and candidate tree vectors are preserved. New native full Bellman certificates and the independent verifier result are included in the accompanying downloadable complete evidence archive; this PR preserves their SHA256, values, scopes, mathematical proof and regeneration routes. The 83-node predecessor is reused from its actual immutable evidence.

No modification to P000's six native axes, independent time axis, three-dimensional slice, triadic balance or residual fidelity: this BRC instance is a typed **finite observer/readout problem**, not a full X6 dynamical statement.

**Next unit:** leader interval `[19/8,77/32]`, rational price near the geometric-mean K split, exact native Bellman seam verification, and a parameterized lower bound across the still-unclosed 85 strips or a rigorous counterexample tree. Formal `RS-EC49AS` task publication remains unresolved under the current native read; portable science is saved independently and has not acquired CLAIM, Result or independent Review.
