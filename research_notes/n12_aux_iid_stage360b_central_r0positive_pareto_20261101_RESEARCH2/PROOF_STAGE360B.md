# Stage360-B — Exact strict Pareto exclusion of the central `r0>0` sign chamber

**Date:** 2026-11-01 (Asia/Shanghai). **Project:** Enterprise Math / Research2 portable author line, Draft PR #1736. **Scientific frontier:** Stage359-B, commit `15670d346c00fd0ad5dcb263ce2f97627e6576c3`. **Result class:** author-checked continuous-domain auxiliary-model theorem, exact rational checker executed; unreviewed, not admitted, no native Task CLAIM.

## 1. Frozen scientific model and provenance

Frozen scientific inputs are the previously declared Stage358/359 research pins: account GLOBAL_KNOWLEDGE_V1 `main@bf84bd7c61a2444b59b1da96be57df0e9ae47e53`, Enterprise Math `main@2af3fc484eb11060b69e0afc1b562bcaf5ad1419`, and P000 original V4 (`770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc` account mirror; source P000 at frozen EM commit has blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`). Current behavioral instructions were separately verified from global canonical `main@d9f0b896c3781e291cbecdebe6d9b124f1ea4cd0`, Enterprise Math current `main@24eb5e125a7bf52366cc49f1ed2594c0cd6d5b14`. They do not alter the frozen coefficients.

For `k=0,1,2,3`, use the original 16 provenance-distinct Bernoulli outcomes with multiplicities `w=(1,3,3,1)`, target `m=(61,21,9,9)` and `B_k(z)=z^k(1-z)^(3-k)`. Define, for `(x,y)∈[0,1]^2`,

\[
 r_k(x,y)=\frac{4B_k(x)+B_k(y)}{5}-\frac{m_k}{160},\qquad
 b(x,y)=\frac5{32}\sum_{k=0}^3w_k|r_k(x,y)|.
\]

Set `D_3(a,z)=(1/2)Σ_k w_k|B_k(a)-B_k(z)|` and keep all four separate audit ports:

\[
 c(x,y)=\frac{63D_3(1/4,x)+D_3(3/4,x)+9D_3(1/4,y)+7D_3(3/4,y)}{256}.
\]

The two-source objective uses additive `b(p_1)+b(p_2)` as an upper-cap constraint and minimizes `c(p_1)+c(p_2)` plus a fixed constant. This study retains the full signed-residual provenance before taking absolute values. It does **not** replace the model by a total-only observer.

## 2. Theorem — entire central `r0>0` chamber is dominated

Define

\[
 \mathcal C=\left\{(x,y):\frac{229}{1000}\le x\le\frac{233}{1000},\quad
 \frac{13}{25}\le y\le\frac{27}{50},\quad r_0(x,y)>0\right\}.
\]

**Theorem.** For **every real** `(x,y)∈C`, there is an explicitly constructible **rational** pair `Q∈[0,1]^2` such that

\[
 \boxed{b(Q)<b(x,y),\qquad c(Q)<c(x,y).}
\]

Furthermore, all `(x,y)∈C` satisfy `b(x,y)≤23151511/4000000000<299/50000`. Thus this exclusion is wholly inside the budget-relevant single-source range used in Stages355–359, not just a formal sign-cell statement.

For an explicit witness, put `R=r_0(x,y)>0` and choose any positive integer

\[
 N>\max\left(1000,\frac{24}{5R}\right),\qquad
 x'=\frac{\lfloor Nx\rfloor+1}{N},\quad\delta=x'-x>0.
\]

Choose any positive integer `M>100/δ` and put `y'=floor(My)/M`. Then `Q=(x',y')` is rational, `Q∈[0,1]^2`, and, **quantitatively**, 

\[
 \boxed{b(x,y)-b(Q)>\frac{3}{100}\delta,\qquad
 c(x,y)-c(Q)>\frac{39}{100}\delta.}
\]

The construction uses floor operations on the given real inputs only to establish existence. It does not assume inputs are rational or that an irrational real is exactly machine-representable.

## 3. Complete analytic proof

**A. Certify the full fixed-sign chamber.** Let `I=[229/1000,234/1000]`, `J=[13/25,27/50]`. In `I`, `B_0` decreases and `B_1,B_2,B_3` increase; in `J⊂(1/3,2/3)`, `B_1` decreases and `B_2,B_3` increase. This follows from the exact derivatives

\[
 B'_0=-3(1-z)^2,\quad B'_1=(1-z)(1-3z),\quad
 B'_2=z(2-3z),\quad B'_3=3z^2.
\]

The exact extreme values are

\[
 \begin{array}{ll}
 r_1(x,y)\ge r_1(229/1000,27/50)=630489/1250000000>0,\\
 r_2(x,y)\ge r_2(229/1000,13/25)=2567511/1250000000>0,\\
 r_3(x,y)\le r_3(234/1000,27/50)=-4533399/312500000<0.
 \end{array}
\]

Consequently, **every point of `I×J` with `r_0>0` has residual pattern `(+,+,+,-)`**. The comparison signs `sgn(B_k(1/4)-B_k(x))=(-,+,+,+)` and `sgn(B_k(3/4)-B_k(x))=(-,-,+,+)` hold throughout `I`: compare the monotone `B_k` with the two fixed rational audit parameters; for the second audit, all four strict endpoint comparisons are verified in the checker.

**B. Derivatives inside this chamber.** In the `(+,+,+,-)` chamber, the weighted residual identity `Σ_k w_k r_k=0` gives

\[
 b(x,y)=-\frac{5}{16}r_3(x,y),\qquad
 \frac{\partial b}{\partial x}=-\frac{3x^2}{4}.
\]

The fixed `x` audit signs from A and preservation of the **original** four audit terms give

\[
 \frac{\partial c}{\partial x}=-\frac{3(1-x)(63-61x)}{256}.
\]

These are full derivatives of the piecewise analytic objective within the specified sign chamber. For all `x∈I`, exact lower bounds are

\[
 -b_x\ge \frac34(229/1000)^2=\frac{157323}{4000000}>\frac{39}{1000},
\]

\[
 -c_x\ge\frac{3(1-234/1000)(63-61\cdot234/1000)}{256}
 =\frac{27993087}{64000000}>\frac25.
\]

(The displayed lower bound for `-c_x` is attained at the right endpoint of `I`, because `(1-x)(63-61x)` decreases on `I`.)

**C. Move strictly right without crossing the `r_0=0` boundary.** For `(x,y)∈C`, the stated `N` and the floor construction ensure `0<δ≤1/N<1/1000`, so `x'∈I`. Since

\[
 \left|\frac{\partial r_0}{\partial x}\right|=\frac{12}{5}(1-x)^2\le\frac{12}{5},
\]

we have `r_0(x+t,y)>R-(12/5)δ>R/2>0` for `0≤t≤δ`. Hence the entire horizontal segment from `(x,y)` to `(x',y)` stays in the certified sign chamber. Integrating the strict bounds from B yields

\[
 b(x,y)-b(x',y)>\frac{39}{1000}\delta,\quad
 c(x,y)-c(x',y)>\frac25\delta.
\]

**D. Rationalize the second coordinate.** The elementary bounds `|B'_k(z)|≤3` on `[0,1]` and `Σw_k=8` imply global (across all sign changes) `y`-Lipschitz estimates

\[
 |b(x',y')-b(x',y)|\le\frac34|y'-y|,\qquad
 |c(x',y')-c(x',y)|\le\frac34|y'-y|.
\]

Indeed the entire `y` coefficient in `b` is `(5/32)(1/5)`, and the entire coefficient of `y` audits in `c` is `(9+7)/(256\cdot2)`; both multiply at most `Σ w_k |B'_k|≤24`. For `M>100/δ` and `y'=floor(My)/M`, `0≤y-y'<δ/100`. It follows that

\[
 b(x,y)-b(Q)>\left(\frac{39}{1000}-\frac{3}{400}\right)\delta
 =\frac{63}{2000}\delta>\frac3{100}\delta,
\]

\[
 c(x,y)-c(Q)>\left(\frac25-\frac3{400}\right)\delta
 =\frac{157}{400}\delta>\frac{39}{100}\delta.
\]

Both inequalities are strict for every real input in `C`.

**E. Budget relevance.** Since `b=-5r_3/16` in `C` and `r_3` increases in both coordinates on the ambient rectangle, every point of `C` has

\[
 b(x,y)\le -\frac5{16}r_3(229/1000,13/25)
 =\frac{23151511}{4000000000}<\frac{299}{50000}.
\]

For any two-source feasible pair containing such a point, replacing only that source by `Q` strictly reduces both the additive error and the total audit cost. Thus no globally cost-minimizing feasible configuration contains a source point in `C`. **QED.**

## 4. Concrete exact instance

Take `p=(231/1000,53/100)` and `q=(232/1000,53/100)`; both have `r_0>0`, and

\[
 \begin{aligned}
 b(p)-b(q)&=160777/4000000000>0,\\
 c(p)-c(q)&=112689397/256000000000>0.
 \end{aligned}
\]

Both individual `b` values are below the original `299/50000` cap. This is a transparent rational test point, separate from the universal construction for arbitrary real `(x,y)`.

## 5. Verification, scope, and next question

`REPRO_STAGE360B.py` uses Python standard-library `fractions.Fraction` and exact polynomial coefficient arithmetic. It checks all decisive rational corner extrema, audit-sign endpoint comparisons, `x`-derivative polynomial identities, uniform gradient bounds, the global `y`-Lipschitz constants, floor-construction inequalities, budget cap, and the rational example. Run it as `python REPRO_STAGE360B.py`; compare its stdout with `REPRO_STAGE360B_EXECUTED_STDOUT.txt`. The continuum conclusion uses the analytic monotonicity, integration, and floor-density argument in §3; the script checks their rational hypotheses, not a grid approximation.

This extends Stage359-B's **upper** central off-boundary exclusion to a disjoint **lower** central `r0>0` sign chamber, while preserving the `r1=0` candidate arc: the new region has `r1>0` strictly. The model is an external finite labeled-outcome Bernoulli/BRC auxiliary observer. The P000 native X6, three-dimensional slices, triadic closure, independently typed time, and Cell-address mapping are separate open obligations.

**Next Stage361-B:** Resolve the central residual sign cells below `y=29/50` not covered by this theorem, in particular `r0<0` and near `r1=0`. Compute exact one-sided derivative cones for `b,c` at their kinks; seek a further Pareto dominance theorem or a rational two-source improvement to the known cusp allocation. Preserve frozen scientific pins and present exact author-evidence without claiming canonical admission.