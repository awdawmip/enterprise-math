# Stage320-B — exact global B-box cusp bound and 5.5× extension of the eight-rate Pareto germ

**Classification:** portable author-side proof and executed exact-rational certificate; UNREVIEWED / NOT_ADMITTED. No native Source CLAIM, Result, reviewer independence, P000 theorem promotion or native X6 transfer is asserted.

**Frozen read context (2026-10-31):** `GLOBAL_KNOWLEDGE_V1 main@a174d37d5cbf2960b4b346f582f8bfeea9bc0a3d`; Enterprise Math canonical `main@786b78a839e992827b8eb8add212030e5f47eee6`; research predecessor PR #1736 `head@161d4ace8b93b58278079ef9d34bce8eee811943`. Scientific dependency: Stage318-B full-square 274-leaf exterior certificate, R chamber and curvature certificates at immutable commit `e3517f652de0c11bae9cfd39cc1ebd1dc1459a22`, plus Stage319-B budget result at `161d4ace8b93b58278079ef9d34bce8eee811943`. Stage315/316 global inner-rate MAP reduction and exact two-block infimal convolution are reused. The new checker tests the new lemma and extension conditions; inherited 274-leaf certificates have not been rerun in this turn.

## Model and notation

The model is precisely the existing finite **positive-source** auxiliary BRC observer model, not native P000 dynamics. There are two hidden sources S, eight private histories h=(J,W,Y), eight permanently locked Bernoulli rates t_h in [0,1], and three possible F accesses (with H accesses producing independent fair bits). Public observation is G=(W,Y) with future outputs; provenance-tagged observation is (S,J,G) with future outputs. Source masses, internal MAP reset, and symmetry are exactly those of Stages315–319. For one of the two outer groups put (x,y)=(t000,t100). Define

\[
B_k(z)=z^k(1-z)^{3-k},\quad
r_k(x,y)=\frac45B_k(x)+\frac15B_k(y)-p_k,
\quad(p_0,p_1,p_2,p_3)=\frac1{160}(61,21,9,9),
\]
\[
d(x,y)=\frac12\sum_{k=0}^3{3\choose k}|r_k(x,y)|,\qquad b(x,y)=\frac5{16}d(x,y).
\]

Let (x*,y*) be the unique global minimizer from Stage307-B.2 with r0=r1=0, x* in (231083940855521,231083940855522)/10^15 and y* in (555508857277,555508857278)/10^12. Let beta*=b(x*,y*), Pmin=2 beta*. Write C3(s)=min{c(x,y): b(x,y)<=s} and F3(z)=min{T3(t):P3(t)<=z}; c and the tagged constant K=33/1024 are the exact Stage316 definitions.

## NEW Lemma 320B.1 — improved global B-box error bound

Set B=[23/100,24/100]×[55/100,56/100]. For **every real (x,y) in B**, 

\[
\boxed{d(x,y)-d(x_*,y_*)\geq\frac{2109}{50000}(|x-x_*|+|y-y_*|).}
\]

This improves the earlier usable 1/120 sharpness constant to 2109/50000 **throughout the entire exterior-certification box B**, not only at a tangent point. Consequently

\[
b(x,y)-\beta_*\geq\frac{10545}{800000}(|x-x_*|+|y-y_*|).
\]

**Proof.** The exact quadratic-derivative ranges over B give r2>0 and r3<0 throughout: r2>=17807/5000000>0 and r3<=−25169/2500000<0. Because sum_k binom(3,k)r_k=0,

\[
d=3r_2+[r_0]_++3[r_1]_+
=\max_{e_0,e_1\in\{0,1\}}Q_{e_0e_1},\quad Q_{e_0e_1}=3r_2+e_0r_0+3e_1r_1.
\]

At the unique minimizer r0=r1=0 so **all four Q_e(x*,y*) equal d***. Each Q derivative is a univariate quadratic in its respective variable and therefore has a rigorous range from endpoint and (if internal) stationary-point evaluations. The exact results are:

| Q | interval ∂x Q | interval ∂y Q |
|---|---|---|
| Q00 | [9039/12500, 2304/3125] | [336/3125, 231/2000] |
| Q01 | [156/125,162/125] | [−9/125,−3/50] |
| Q10 | [−2187/3125,−2028/3125] | [−27/3125,−3/500] |
| Q11 | [−432/3125,−1587/12500] | [−588/3125,−363/2000] |

Put a=|x−x*| and b0=|y−y*|. On (+,+), use Q00 and infer Q00−d*>=min(9039/12500,336/3125)(a+b0)>2109/50000(a+b0). On (+,−), Q01 gives min(156/125,3/50)>2109/50000. On (−,−), Q11 gives min(1587/12500,363/2000)>2109/50000. In the only competing-sign quadrant (−,+), use the convex combination (7Q00+9Q10)/16. Its derivative lower bounds along the segment from the minimizer are **(2124 a+2109 b0)/50000**. Since the maximum of Q's dominates this combination, the same global inequality follows. Every segment is contained in B. All derivative extrema and rational comparisons are verified by the attached standard-library Fraction checker. QED.

## NEW Theorem 320B.2 — the full eight-real-rate Pareto germ extends 5.5-fold

For the strictly larger interval

\[
\boxed{0\leq\varepsilon\leq\delta=11/10000000=1.1\times10^{-6},}
\]

**the exact Stage318–319 global theorem persists**:

\[
\boxed{F_3(P_{\min}+\varepsilon)=\frac{33}{1024}+c(x_*,y_*)+c(x_\varepsilon,y_\varepsilon),}
\]

where (x_epsilon,y_epsilon) is the unique rightward r1=0 kink with b=beta*+epsilon. For ε>0 there are precisely **two** global eight-rate tagged-optimal vectors, related by swapping which outer source block takes the entire ε budget; at ε=0 the tagged-optimal vector is unique. Throughout the stated interval C3 is strictly decreasing and twice differentiable away from beta*, and its previously certified uniform curvature is **−41<C3''(s)<−38**. For a positive split θ,ε−θ the strict tagged-cost penalty remains

\[
38\theta(\varepsilon-\theta)<\Delta_\varepsilon(\theta)<41\theta(\varepsilon-\theta).
\]

**Proof.** Stage318's immutable 274-leaf full-square exterior certificate gives b−beta*>1/640000 outside B, and δ<1/640000. Thus every single-block feasible competitor for b<=beta*+δ lies in B. Lemma320B.1 yields

\[
|x-x_*|+|y-y_*|\leq\frac{160000}{2109}\delta=\frac{22}{263625}<\frac{83940855521}{10^{15}},
\]

where the final rational is the minimum certified root-to-boundary margin of the **unchanged** Stage318 rectangle R=[231/1000,2312/10000]×[555/1000,556/1000]. Thus *every* feasible block lies in R even at the enlarged δ. We may reuse all of Stage318's uniform-on-R certificates for the four open residual chambers, nonzero gradient determinants, kink orientations, strict branch slope separation, and curvature. For actual existence of all four kink-arm competitors through δ, use outward x extent L=1/100000; the inherited uniform |dy/dx|<12 keeps them inside R, while their b increase is >18L/100=9/5000000>δ. The strictly winning rightward r1=0 branch therefore exists, is unique, and reaches every desired ε in [0,δ]. Interior and other kink candidates are excluded exactly as in Stage318. Finally Stage316's exact infimal convolution and the inherited strict concavity of C3 force all positive public-error budget into a single block. Stage315 sets all four central rates to their MAP values; the symmetry yields exactly two optimizers. The integral curvature bound gives the allocation gap. QED.

## Verification, scope and next frontier

`REPRO_STAGE320B.py` evaluates all quadratic derivative extrema **exactly**, proves the support-sign identity throughout B, checks each of the four quadrant inequalities, the stricter outer-box gap, all rational root-to-R comparisons, the four kink reach inequalities and the factor δ/(1/5,000,000)=11/2. Actual stdout ends in `STAGE320B_GLOBAL_BOX_SHARPNESS_AND_5P5X_PARETO_EXTENSION_EXACT_PASS`. No floats enter assertions. The continuous theorem consists of this exact lemma and the unchanged scope of Stage318's earlier (author-side) global certificate, not a new independent replay of its 274 leaves. Neither mathematical review nor formal checker admission has occurred.

**Next Stage321-B:** close the residual gap between δ=1.1e-6 and the outer B gap 1/640000≈1.5625e-6 by expanding R leftwards and re-certifying its determinant/sign/slope/curvature inequalities with exact rational intervals; alternatively improve the exterior B gap or produce a strict competitor. Beyond the present certificate, seek the *first actual optimizer branch transition* rather than interpreting a certificate boundary as a physical transition. P000-native X6 six-axis paths, correct three-axis slice/third coordinate, triadic force closure, ordered time and registered final Cell address remain a separately typed observer-preservation proof obligation.
