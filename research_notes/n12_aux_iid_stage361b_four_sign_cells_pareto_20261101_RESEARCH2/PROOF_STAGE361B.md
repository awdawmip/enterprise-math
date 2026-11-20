# Stage361-B — Exact Pareto exclusion of all four open central residual sign cells

**Author-side mathematical result · 2026-11-01 · Enterprise Math Research2 portable continuation / Draft PR #1736.**  This is a continuous-real-domain auxiliary-model theorem with an executable exact-rational coefficient/corner checker. It is not a formal native CLAIM, independent review or P000 theorem.

## 1. Provenance and fixed mathematical object

Highest previous durable Research2 frontier: Stage360-B `cc96acbc2544830e53c71ef164dd7d9292b16cb1`, especially `research_notes/n12_aux_iid_stage360b_central_r0positive_pareto_20261101_RESEARCH2/PROOF_STAGE360B.md` and `NEXT_TASK_PACKET_361B.md` in `awdawmip/enterprise-math`.

Original scientific freezes are **unchanged**: global `main@bf84bd7c61a2444b59b1da96be57df0e9ae47e53`, Enterprise Math `main@2af3fc484eb11060b69e0afc1b562bcaf5ad1419`, P000 V4 (frozen EM blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`, account P000 canonical original blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`). Current behavior/control is separately read at global main `20087dedd51935dd3bdecff5a1f1f8b03d4829a4` and Enterprise Math main `873e646d910b5593b490d09480bb71762c63398d` without modifying science pins.

For `k=0,1,2,3`, let `B_k(z)=z^k(1-z)^(3-k)`, `w=(1,3,3,1)`, `m=(61,21,9,9)`. At every `(x,y)∈[0,1]^2`, define the **four provenance-distinct residuals** and the total-variation error

\[
 r_k(x,y)=\frac{4B_k(x)+B_k(y)}5-\frac{m_k}{160},\quad
 b(x,y)=\frac5{32}\sum_{k=0}^3w_k|r_k(x,y)|.
\]

The four separately retained audit ports use `D_3(a,z)=(1/2)Σ_k w_k|B_k(a)-B_k(z)|` and

\[
 c(x,y)=\frac{63D_3(1/4,x)+D_3(3/4,x)+9D_3(1/4,y)+7D_3(3/4,y)}{256}.
\]

The two-source optimization minimizes the additive audit cost under an additive `b` upper budget, with an irrelevant fixed constant. No provenance labels are merged in these definitions.

## 2. Main theorem (full open-cell classification)

Consider the closed rational rectangle

\[
 R=\left[\frac{229}{1000},\frac{233}{1000}\right]
 \times\left[\frac{27}{50},\frac{14}{25}\right].
\]

**Theorem.** For **every real point** `p=(x,y)∈R` satisfying `r_0(p)r_1(p)≠0`, there is an explicitly constructible rational point `Q∈[0,1]^2` such that

\[
 \boxed{b(Q)<b(p),\qquad c(Q)<c(p).}
\]

All such points also satisfy the single-source budget-relevance bound `b(p)<299/50000 (=0.00598)`. Thus each can be removed from a feasible pair without increasing its error budget and while strictly decreasing the cost. The open sign cells represented by `(+++-)`, `(+-+-)`, `(-++-)`, and `(--+-)` (ordered `r0,r1,r2,r3`) are completely excluded on `R`. The kink sets `r0=0` and `r1=0` are kept as explicitly separate targets; the right `r1=0` candidate curve is preserved.

More precisely, choose an integer `N` and put `δ=1/N` using the case-dependent formulas in §4; let the resulting real improved intermediate point be `p'`. Pick any integer `M>1000/δ` and set

\[
 Q=\left(\frac{\lfloor Mp'_x\rfloor}{M},\frac{\lfloor Mp'_y\rfloor}{M}\right).
\]

The following strict bounds hold in the four cells (their labels refer to the signs of `r0,r1`):

| Cell | `p'` construction | `b(p)-b(Q)` | `c(p)-c(Q)` |
| --- | --- | --- | --- |
| `++` (`+++-`) | `(x+δ,y)` | `> 7δ/200` | `>39δ/100` |
| `+-` (`+-+-`) | `(x+δ,y)` | `>19δ/100` | `>39δ/100` |
| `-+` (`-++-`) | `(x+δ,y+30δ)` | `>39δ/1000` | `>11δ/250` |
| `--` (`--+-`) | `(x,y-δ)` | `>δ/40` | `>δ/200` |

These claims hold for **all real** inputs in their respective sign cells, not just rational test points.

## 3. Exact ambient sign chamber and derivative identities

Enlarge the rectangle only for small perturbations: `I=[229/1000,234/1000]` and `J=[27/50,561/1000]`. Direct differentiation gives

\[
 B'_0=-3(1-z)^2,\quad B'_1=(1-z)(1-3z),\quad
 B'_2=z(2-3z),\quad B'_3=3z^2.
\]

Hence `B2,B3` increase throughout `I` and `J`; exact corner evaluation yields

\[
 r_2(x,y)\ge r_2(229/1000,27/50)=\frac{3653511}{1250000000}>0,
\]

\[
 r_3(x,y)\le r_3(234/1000,561/1000)
 =-\frac{53439903}{5000000000}<0.
\]

The **audit comparison signs** for the four ports, all strict on `I×J`, are

\[
\begin{array}{c|c}
\operatorname{sgn}(B_k(1/4)-B_k(x))&(-,+,+,+)\\
\operatorname{sgn}(B_k(3/4)-B_k(x))&(-,-,+,+)\\
\operatorname{sgn}(B_k(1/4)-B_k(y))&(+,+,-,-)\\
\operatorname{sgn}(B_k(3/4)-B_k(y))&(-,-,+,+)
\end{array}
\]

for `k=0,1,2,3`. Each sign is certified at the two endpoints of a monotonicity interval, with no floating-point comparisons. The full piecewise derivatives therefore satisfy

\[
 c_x=-\frac{3(1-x)(63-61x)}{256},\qquad c_y=\frac{3y(1-y)}{64},
\]

throughout `I×J`, while `b` has four possible signed formulas:

| signs of `(r0,r1,r2,r3)` | `b_x` | `b_y` used below |
| --- | --- | --- |
| `+++-` | `-3x²/4` | — |
| `+-+-` | `-3(1-2x)²/4` | — |
| `-++-` | `3(1-2x)/4` | `3(1-2y)/16` |
| `--+-` | — | `3y(2-3y)/16` |

These identities use the full weight vector and the exact identity `Σ_k w_k r_k=0`; they are verified symbolically over rational polynomial coefficients in the checker. In `I×J`, the quantitative bounds are

\[
 -c_x>\frac25,\quad 0<c_y\le\frac3{256},\quad
 \frac34\Big(\frac{229}{1000}\Big)^2>\frac{39}{1000},\quad
 \frac34(1-2\cdot234/1000)^2>\frac15,
\]

\[
 b_x\big|_{-++-}\le\frac{813}{2000},\quad
 b_y\big|_{-++-}\le-\frac3{200},\quad
 b_y\big|_{--+-}>\frac3{100},\quad c_y>\frac1{100}.
\]

Therefore, the four displayed directions have strict **joint** decreases at every point along their same-sign line segments:

\[
 (b,c)_{\texttt{++}}' < (-39/1000,-2/5),\quad
 (b,c)_{\texttt{+-}}' < (-1/5,-2/5),
\]

\[
 (b,c)_{\texttt{-+}}' < (-87/2000,-31/640),\quad
 (b,c)_{\texttt{--}}' < (-3/100,-1/100),
\]

where the derivative parameter increases from `0` to `δ` along each specified direction (for `--`, the direction is downward in `y`). These are uniform exact bounds.

## 4. How to choose a sufficiently small **rational** step

For every `p∈R` of the indicated type, choose any **integer strictly greater** than the displayed maximum and define `δ=1/N`:

| Type | Condition on `N` |
| --- | --- |
| `++` | `N>max(1000,24/(5r0(p)))` |
| `+-` | `N>max(1000,24/(5r0(p)),8/(5(-r1(p))))` |
| `-+` | `N>max(30000,14/r1(p))` |
| `--` | `N>max(1000,1/(y-27/50),6/(5(-r0(p))),2/(5(-r1(p))))` |

Each denominator is strictly positive on its named cell. For `--`, the condition `y>27/50` follows from `r1(229/1000,27/50)>0` and monotonicity in `x` throughout the original rectangle.

For `++` and `+-`, increasing `x` decreases `r0`, with `|r0_x|≤12/5`; the chosen `N` keeps `r0>0`. Increasing `x` increases `r1` in `I`. The `+-` condition additionally keeps `r1<0` since `0<r1_x≤4/5`. For `-+`, increasing both `x` and `y` decreases `r0`, preserving its negative sign. Along direction `(1,30)`, `|d r1/dt|≤4/5+30/5<7`; thus `N>14/r1` preserves `r1>0`. The bound `N>30000` keeps the path inside `I×J`. For `--`, reducing `y` increases both `r0` and `r1`; the bounds `|r0_y|≤3/5` and `|r1_y|≤1/5` guarantee both stay negative, while the first bound keeps `y>27/50`.

Integrating §3's strict inequalities gives the listed decreases before rationalization. Globally on the entire unit square, both `b` and `c` are coordinate-wise Lipschitz with constants `L_x≤3` and `L_y≤3/4`: use `|B'_k|≤3`, `Σw_k=8`, and each objective's exact port weights. The rounding from `p'` to `Q` therefore changes either objective by **less** than

\[
 \frac3M+\frac3{4M}<\frac{3\delta}{800}.
\]

Subtracting this error from the exact derivative margins yields the four strict quantitative inequalities in §2. Every constructed `Q` lies in `[0,1]^2`; its rounded values need not retain the same sign pattern because the Lipschitz argument already covers any crossed boundary.

## 5. Budget relevance, rational witnesses, and verification semantics

Within each sign cell `b` reduces to a sum of the positive residuals. Monotonicity in each rectangle coordinate gives the following exact **single-source** upper bounds:

| Cell | Upper bound for `b` | Numerical cap |
| --- | --- | --- |
| `+++-` | `18937511/4000000000` | `<299/50000` |
| `+-+-` | `4711/800000` | `<299/50000` |
| `-++-` | `4827/1000000` | `<299/50000` |
| `--+-` | `17469489/4000000000` | `<299/50000` |

For example, the `+-+-` bound is `(5/16)[r0(x_min,y_min)+3r2(x_max,y_max)]`; the mixed extrema are used for a valid upper bound, rather than assuming the rectangle corner belongs to that sign cell. The four rational examples below demonstrate each nonempty sign cell:

1. `+++-`: `(231/1000,27/50) → (23101/100000,27/50)`.
2. `+-+-`: `(229/1000,11/20) → (22901/100000,11/20)`.
3. `-++-`: `(233/1000,11/20) → (23301/100000,5503/10000)`.
4. `--+-`: `(231/1000,14/25) → (231/1000,5599/10000)`.

The accompanying standard-library Python `Fraction` program proves the rational identities for the sign and derivative coefficients, checks the exact corner/cost inequalities, and computes the four strict rational gains. It was executed **twice** with byte-identical stdout, archived in `REPRO_STAGE361B_EXECUTED_STDOUT.txt`.

The **continuum proof** is the analytic sign, derivative integration and rationalization argument above. The script checks its exact algebraic assumptions and finite symbolic certificates; it is not a grid-exhaustion substitute. This theorem is scoped to the finite 16-label Bernoulli/BRC auxiliary observer. Connecting this effective real-parametric model to P000 native X6, the named 3-dimensional slice, provenance-preserving paths, triadic closure, independent time and the registered Cell-address codec remains a separate typed research construction.

## 6. New frontier

**Proved here:** every point of `R` with `r0*r1≠0` admits a strict rational Pareto improvement, so the interior sign chambers are eliminated. **Next discriminating problem (Stage362-B):** calculate exact **one-sided** Pareto tangent cones on `r0=0` and `r1=0` inside `R`; independently recheck the Stage356-B central boundary dominance argument and classify the potentially surviving `r1=0,r0<0` cusp curve. Then test whether all remaining feasible two-source competitors are excluded or find a strict rational counterexample to the Stage353-B right-arc split. Preserve `q*` and the proven restricted-arc theorem unless contradicted by an exact construction.

**Evidence class:** `PORTABLE_AUTHOR_THEOREM / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED`. Native Task owner and Driver roles were not granted in this run; publication as repository research notes creates no Result/Review/CLAIM authority.