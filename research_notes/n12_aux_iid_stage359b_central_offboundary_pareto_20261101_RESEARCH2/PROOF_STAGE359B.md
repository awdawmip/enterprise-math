# Stage359-B — Exact central off-boundary Pareto exclusion by a monotone direction

**Date:** 2026-11-01 (Asia/Shanghai). **Scope:** external two-source, 16-source-label Bernoulli/BRC auxiliary observer with four audit channels. **Classification:** `PORTABLE_AUTHOR_THEOREM / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING`.

## 1. Question and fixed scientific model

Stage358-B excluded an outer-x **tube** around `r0=0`. The remaining independent question is whether a positive-area central region with `r0 != 0` can be excluded without importing the unreviewed Stage346/356 global lemmas. This note constructs a direction that strictly decreases *both* original observer error and audit cost, with a rational witness for each real source parameter.

Let `k=0,1,2,3`, weights `w=(1,3,3,1)`, target counts `m=(61,21,9,9)`, and `B_k(z)=z^k(1-z)^(3-k)`. For `(x,y) in [0,1]^2` put

\[
\begin{aligned}
r_k(x,y)&=\frac{4B_k(x)+B_k(y)}5-\frac{m_k}{160},\\
b(x,y)&=\frac5{32}\sum_{k=0}^3 w_k|r_k(x,y)|,\\
D_3(a,z)&=\frac12\sum_{k=0}^3w_k|B_k(a)-B_k(z)|,\\
c(x,y)&=\frac1{256}\left(63D_3(1/4,x)+D_3(3/4,x)
 +9D_3(1/4,y)+7D_3(3/4,y)\right).
\end{aligned}
\]

This is the **original** 16-label multiplicity-weighted observer, not a total-only surrogate. The cost retains all four provenance-distinct audit channels. In a two-source optimization, the additive error is `b(p1)+b(p2)` and the variable audit cost is `c(p1)+c(p2)`; any fixed constant in the objective cancels in a one-source replacement.

Scientific input pins are inherited from the preceding author's frozen Stage358-B packet: global `main@bf84bd7c61a2444b59b1da96be57df0e9ae47e53`, Enterprise Math `main@2af3fc484eb11060b69e0afc1b562bcaf5ad1419`, branch frontier PR #1736 `b094e92e79a62354c7bc3f82b6bd84b99d32e2d2`, P000 original V4. Current behavioral rule snapshot was separately read at global `main@f4b6711658a88b23d0e4bfbac1809813c1715de3`, project control `main@ec59dcda9a146df692e3ed540d89336035eb1322`. This rule refresh changes no mathematical input coefficients.

## 2. Exact theorem

**Theorem (constructive rational strict Pareto direction).** For **every real**

\[
\boxed{\frac{23}{100}\le x\le\frac{119}{500},\qquad
\frac{29}{50}<y\le\frac35,}
\]

there exists an **explicitly constructible rational** pair `Q=(u,v) in [0,1]^2` with

\[\boxed{ b(Q)<b(x,y),\qquad c(Q)<c(x,y). }\]

This domain satisfies `r0(x,y)<0`, so it is a strictly **off-boundary**, positive-area two-dimensional region. In particular, for any two-source additive error cap and any feasible configuration containing a point in this domain, replacing that point by `Q` strictly decreases both additive error and audit cost. Thus no cost-minimal feasible two-source solution contains such a point. The conclusion also holds after intersecting the domain with the Stage355-B relevance cap `b<=299/50000`.

The following quantitative construction holds. Let `delta=y-29/50>0`. Choose **any integer** `N>200/delta`, set `m=floor(N*x)` and `Q=(m/N,29/50)`. Then

\[
\boxed{b(x,y)-b(Q)>\frac{3}{400}\,\delta,\qquad
c(x,y)-c(Q)>\frac{39}{6400}\,\delta.}
\]

Here `m/N` is rational even for irrational `x`. `Q` is a legitimate original-model parameter: `0<=m/N<=1`.

## 3. Complete proof over the continuous real domain

**Step 1: fix the residual sign chamber.** Put `X=[23/100,119/500]`, `Y=[29/50,3/5]`. `B0` decreases; `B1` increases on `X` and decreases on `Y`; `B2` and `B3` increase on both intervals. These assertions follow from

\[
B_0'=-3(1-z)^2,\quad B_1'=(1-z)(1-3z),\quad
B_2'=z(2-3z),\quad B_3'=3z^2,
\]

and `X<1/3<Y<2/3`. Consequently the following four exact corner values bound every residual in the indicated direction:

\[
\begin{array}{c|c|c}
\mathrm{residual}&\mathrm{rigorous\ bound}&\mathrm{exact\ corner\ value}\\\hline
r_0& r_0(x,y)\le r_0(23/100,29/50)&-603/500000<0\\
r_1& r_1(x,y)\le r_1(119/500,29/50)&-72807/312500000<0\\
r_2& r_2(x,y)\ge r_2(23/100,29/50)&2297/500000>0\\
r_3& r_3(x,y)\le r_3(119/500,3/5)&-707807/312500000<0.
\end{array}
\]

Therefore the exact sign pattern on the entire closed rectangle is `(-,-,+,-)`. No absolute-value kink occurs in the interior of this rectangle.

**Step 2: fix the audit-label signs.** For all `y in Y`, the signs of `B_k(1/4)-B_k(y)` are `(+,+,-,-)`, and those of `B_k(3/4)-B_k(y)` are `(-,-,-,+)`. To verify this on **every real** `y in Y`, use the same monotonicity of each `B_k` on `Y` and compare its rational endpoint extrema with the two fixed `a`-values. In the only potentially close comparison, `B2(3/4)=9/64=0.140625 < B2(29/50)=0.141288` (decimals are explanations; the checker uses exact fractions). Again all signs are strict.

**Step 3: calculate exact directional derivatives.** With the signs from Steps 1–2, differentiate the original absolute-value sums; the `x` audit terms are constant in `y`. Elementary polynomial cancellation gives

\[
\boxed{\frac{\partial b}{\partial y} =\frac{3y(2-3y)}{16}},\qquad
\boxed{\frac{\partial c}{\partial y} =\frac{3y(18-25y)}{256}}.
\]

Both expressions are positive and strictly decreasing for `y in Y`. Therefore for every `x in X` and `y>Y0=29/50`, exact integration yields

\[
\begin{aligned}
b(x,y)-b(x,Y_0)&>\frac9{400}(y-Y_0),\\
c(x,y)-c(x,Y_0)&>\frac{27}{1280}(y-Y_0).
\end{aligned}
\]

The endpoint derivative values are `9/400` and `27/1280`; strictness of the integrals follows because each derivative is strictly greater than its final-endpoint minimum on a positive-measure part of `[Y0,y]`.

**Step 4: turn the real domination into a rational witness.** For all `x,x' in [0,1]`, the same original definitions give global one-variable Lipschitz estimates

\[
|b(x',z)-b(x,z)|\le 3|x'-x|,\qquad
|c(x',z)-c(x,z)|\le 3|x'-x|.
\]

Indeed `|B_k'(t)|<=3` on `[0,1]`, `sum w_k=8`, and the total coefficient of the `x` terms in `b` is `(5/32)(4/5)=1/8`, while in `c` it is `(63+1)/(256*2)=1/8`. The absolute-value map is 1-Lipschitz, so these inequalities hold even across sign changes.

For `N>200/delta` and `m=floor(Nx)`, `0<=x-m/N<1/N<delta/200`. Apply Step 3 at `x` and the global bound at `y=Y0` to obtain

\[
\begin{aligned}
b(x,y)-b(m/N,Y_0)&>\left(\frac9{400}-\frac3{200}\right)\delta=\frac3{400}\delta,\\
c(x,y)-c(m/N,Y_0)&>\left(\frac{27}{1280}-\frac3{200}\right)\delta=\frac{39}{6400}\delta.
\end{aligned}
\]

This supplies the required rational `Q` for every real `(x,y)` in the theorem domain. For an additive two-source optimization, replacing one source by `Q` preserves the feasible upper error bound and strictly decreases the total variable cost. **QED.**

## 4. Non-vacuous exact instance

Take `p=(231/1000,3/5)`, which lies in the theorem's central band and obeys `b(p)<299/50000`; the simple rational witness `q=(231/1000,29/50)` gives

\[
\begin{aligned}
b(p)&=20166327/4000000000, & b(q)&=18132327/4000000000,\\
c(p)&=8646736149/256000000000, & c(q)&=8531736149/256000000000,\\
b(p)-b(q)&=1017/2000000>0,&c(p)-c(q)&=23/51200>0,\\
r_0(p)&=-5805891/1250000000<0.
\end{aligned}
\]

## 5. Exact verification and trust scope

`REPRO_STAGE359B.py` is standard-library-only, uses Python `fractions.Fraction` throughout the decisive calculations, and checks all four corner inequalities, eight strict audit-sign comparisons at the endpoints, the full differentiated polynomial coefficient identities, derivative lower bounds, Lipschitz coefficients, quantitative rational-witness margins and the explicit example. It has been executed twice; the second stdout was compared byte-for-byte against `REPRO_STAGE359B_EXECUTED_STDOUT.txt`. No floating-point computation is used in the checker. The continuum theorem relies on the stated elementary monotonicity/differentiation/integration and the printed exact coefficients, not on finite sampling.

Script SHA256: `c99b7df2e513edd6a53d2258921fd7d8e66a624051c9f59620249b015cc0fde0`. Captured stdout SHA256: `e60996be46386eeb7efa4fe244d21918ea3f9e674fc9ddac5fe9d64bd1793cb1`.

This is a mathematically author-checked, **not independently reviewed or canonically admitted**, auxiliary-observer result. Native authority check for this turn returned `authority_granted=false` and current task/owner query `CONTROL_QUOTA`. GitHub repository write permission (`admin`) does not imply a canonical TASK CLAIM. No source-session role, authenticated Result or Driver review is inferred.

BRC interface reuse: exact 16-labeled-outcome positive rational observer, retained provenance/multiplicities, four audit ports, strict Pareto replacement under the same future two-source additive operation. The theorem is in the external `(x,y)` parameter model. A native P000 X6/three-dimensional-slice/triadic-closure/time/Cell-address representation remains a separate typed mapping problem; P000 itself is a locked starting axiom.

## 6. Next unresolved unit

**Stage360-B:** separate the unsolved central region around the cusp (`y<=29/50`), the upper outer-x strips, and `y>3/5`; compute exact sign-cell gradient cones for `b,c` and test whether fixed directions eliminate additional open cells. Pay special attention to points with `r_1=0` on the right candidate arc so that a valid Pareto frontier is not inadvertently removed. If a candidate direction loses strictness at a residual kink, preserve the kink and test one-sided slopes, or construct a rational two-source counterexample. The mother question remains the full auxiliary model's post-cusp globally optimal budget split.
