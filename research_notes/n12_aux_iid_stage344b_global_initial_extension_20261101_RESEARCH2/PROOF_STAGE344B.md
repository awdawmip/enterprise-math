# Stage344-B — Exact global two-source Pareto allocation through E=1/1000

Date: 2026-11-01. Status: **PORTABLE_AUTHOR_THEOREM / EXACT_FRACTION_CERTIFICATE_EXECUTED / UNREVIEWED / NOT_ADMITTED**. This is an auxiliary three-visit source-tagged Bernoulli/BRC observer theorem, not a result about the P000-native X6 world. No formal CLAIM, native Source Result, independent Driver review or P000 observer-preserving bridge is claimed.

## Frozen source/identity boundary

Read from immutable `awdawmip/chatgpt-global-knowledge main@e1e9409728a16a133670c599579b488a6aa5796f`: `00_BOOTSTRAP.md`, `OPERATING_MANUAL.md`, `projects/enterprise-math/00_EM_PROJECT_BOOTSTRAP.md`, `projects/enterprise-math/00_EM_TASK_RESEARCHER_BOOTSTRAP.md`, P000 projection, ACTIVE `我眼中的世界.md`, mathematical/code/BRC/activity rules. The P000 projection's recorded original blob differs from the actual source blob, so the full `awdawmip/enterprise-math main@1fde72896593e8b10c9abb356983a265d2a4600f:p000_reality_foundation.json` was read, with actual Git blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`; also read joint-observer and Heartbeat World contracts, `docs/PORTABLE_RESEARCH_PROTOCOL.md` and `docs/AUTONOMOUS_RESEARCH_OPERATIONS.zh-CN.md`. The previous portable (not admitted) Stage343-B proof/artifact is `cff27b4a90074e48669b1179f782152b360695ed`. Reuse classification: **REUSE_APPLIED** (exact definitions, Bernstein method and tagged observer); the new constants/enclosure/curvature are verified here, not assumed from Stage343.

The native v0.6.11 service status returned `research_authority_granted=false`, `executor_binding_configured=false`, with 5/5 active control jobs, so no live Owner/CLAIM was authenticated. GitHub artifact storage has no mathematical or native task authorization effect.

## Model, exact target and result

For `k=0,1,2,3`, set

\[
 B_k(z)=z^k(1-z)^{3-k},\quad w=(1,3,3,1),\quad m=(61,21,9,9),
\]
\[
 r_k(x,y)=\frac{4B_k(x)+B_k(y)}5-\frac{m_k}{160},\qquad
 b(x,y)=\frac5{32}\sum_{k=0}^3 w_k|r_k(x,y)|,
\]
\[
 D_3(a,z)=\frac12\sum_{k=0}^3 w_k|B_k(a)-B_k(z)|,
\quad c(x,y)=\frac{63D_3(1/4,x)+D_3(3/4,x)+9D_3(1/4,y)+7D_3(3/4,y)}{256}.
\]

The **16 comparisons retain their four reference/source tags and their four word classes**. Only after checking their signs do we simplify derivatives. For two separately source-tagged groups `q_1,q_2∈[0,1]^2` put `P=b(q_1)+b(q_2)` and `T=33/1024+c(q_1)+c(q_2)`. All rates are real variables; numerical grids are not a proof.

Let `q_*=(x_*,y_*)` be the unique `r_0=r_1=0` point, `β_*=b(q_*)`. On the **right-hand** `r_1=0` arc set `q_s` by `b(q_s)=β_*+s` (so `q_0=q_*`). **Theorem (new interval)**: for every real `E∈[0,1/1000]`,

\[
 \boxed{\min_{q_1,q_2\in[0,1]^2\,;\,P\le2\beta_*+E}T
 =\frac{33}{1024}+c(q_*)+c(q_E).}
\]

At `E=0` the sole minimizer is `(q_*,q_*)`; at every `E>0` the sole minimizers are `(q_*,q_E)` and its source-order swap. This extends the Stage343-B author result from `0.0008` to `0.0010` (+25%). It neither locates the eventual first global switch nor transports to P000 native X6.

## Lemma 1 — 223-leaf certified *continuum* enclosure

Take

\[
 Q=\frac{481}{100000}=0.00481,\quad
 R=[449/2000,469/2000]\times[107/200,623/1000].
\]

**For all real `(x,y)∈[0,1]^2`, `b(x,y)≤Q` implies `(x,y)∈R`.** For a nonempty subset/mask `S⊆{0,1,2,3}`, write `F_S(z)=Σ_{k∈S}w_kB_k(z)` and `M_S=Σ_{k∈S}w_km_k`. For each rational interval `[u,v]`, define its four exact cubic Bernstein control coefficients

\[
 F_S(u),\quad F_S(u)+(v-u)F'_S(u)/3,\quad
 F_S(v)-(v-u)F'_S(v)/3,\quad F_S(v).
\]

Let `L_S[u,v]` be their minimum; the Bernstein convex-hull property proves `F_S(z)≥L_S[u,v]` for every *real* `z∈[u,v]`. From `Σw_kr_k=0` (verify `Σw_km_k=160`) one obtains `b=(5/16)Σw_k(r_k)_+`, hence for any rectangle `[a,b_]×[c_,d]`

\[
 b(x,y)\ge\frac5{16}\left(\frac{4L_S[a,b_]+L_S[c_,d]}5-\frac{M_S}{160}\right).\tag{1}
\]

The exact quadtree in `CERTIFICATE_STAGE344B.csv` covers the full unit square with **223 leaves**, 159 `HIGH` leaves each certified by a particular mask and rational bound strictly `>Q`, and 64 `INNER` leaves wholly within `R`. Maximum depth is 12; the area sum is exactly 1 and every four-child split is present. The executable checker regenerates and compares every row, checks exact strict inequalities, nonoverlap and full recursive coverage. Thus the enclosure is not extrapolated from samples. A point with `b<Q` lies in the interior of `R` by continuity.

The new enlarged rectangle has `r_2≥r_2(449/2000,107/200)=16372401/10000000000>0`, since `B'_2(z)=z(2-3z)>0` on both coordinate ranges. **Do not assume `r_3<0`**; it changes sign inside `R`.

## Lemma 2 — exact source-tag derivatives and strict descent outside the right r1-zero arc

The 16 signs, grouped only for display, are `B_k(1/4)-B_k(x): -+++`, `B_k(3/4)-B_k(x): --++`, `B_k(1/4)-B_k(y): ++--`, `B_k(3/4)-B_k(y): --σ+` where the sole changing sign is at `k=2` and `y†=(1+sqrt(13))/8`. All fixed signs follow from rational Bernstein coefficients; the varying atom factors exactly as `(4y-3)(16y²-4y-3)/64`. Differentiating the complete 16-term formula, not an untagged quotient, yields

\[
 c_x=-p(x)=-\frac{(1-x)(189-183x)}{256}< -2/5,
\quad c_y=q(y)=\begin{cases}3y(1-y)/64,&y<y†,\\3y(18-25y)/256,&y>y†.\end{cases}
\]

Both one-sided derivatives at `y†` are positive; on all `R`, `0<q(y)<1/40`, and below the cusp `q≤3/256`.

For `r_3<0` and `r_2>0`, exact mass conservation gives

\[
 b=\frac5{16}\{-r_3+(-r_0)_++3(-r_1)_+\}.
\]

Each strict chamber `(sign r0,sign r1)` has an exact Pareto-descent rule:

* `(+,+)`: increase `x` (`b_x=-3x²/4<0`, `c_x<0`).
* `(+,-)`: increase `x` (`b_x=-3(1-2x)^2/4<0`, `c_x<0`).
* `(-,-)`: decrease `y` (`b_y=3y(2-3y)/16>0`, `c_y>0`).
* `(-,+)`: maintain `b` while increasing `x,y`. Here `b_x=3(1-2x)/4>0`, `b_y=-3(2y-1)/16<0`, so `dy/dx=4(1-2x)/(2y-1)`. Throughout `R` the tagged derivative obeys
\[
 q(y)\frac{4(1-2x)}{2y-1}<\frac25<p(x).
\]
  Below `y†` this follows from the exact rational bound `(3/256)·4(1-2·449/2000)/(2·107/200-1)=1653/4480<2/5`; above the cusp, from `q<1/40`, `y†>23/40` and the corresponding rational bound `<2/5`. Thus the constant-public-cost trajectory strictly lowers `c`. Piecewise integration covers the cusp.

For `r_3≥0`: monotonicity in `x,y` and `r_3(469/2000,612/1000)<0` force `y>612/1000` when `r3≥0`, where `r1≤r1(469/2000,612/1000)<0`. If `r3>0,r0>0`, increase `x` (`b=-15r1/16`, `b_x<0`); if `r3>0,r0<0`, decrease `y` (`b_y=3y(1-y)/8>0`); if `r3>0,r0=0`, decrease `y` into `r0>0` (`b_y=3(1-y)(3y-1)/16>0`). Audit cost strictly decreases in each case. On `r3=0,r0>0`, increase `x` into the first chamber; on `r3=0,r0<0`, decrease `y` into `r3<0,r0<0,r1<0`, where `b=15r2/16` and `b_y>0`.

At the only double intersection `r0=r3=0`, the curve `r3=0` has `y'=-4x²/y²`, and `r0` is strictly decreasing along it since `x<y`. Exact endpoint signs isolate this intersection in

\[
 1133/5000<x<567/2500,\qquad 616/1000<y<618/1000.
\]

The direction `d=(1,-14)` strictly decreases all three `r0,r3,r2`, using the uniform rational inequalities `2(1-x)^2>7(1-y)^2`, `2x²<7y²`, `4x(2-3x)<14y(2-3y)` throughout this box. Immediately along `d`, `r3,r0,r1<0<r2` and hence `Db=15Dr2/16<0`, while `Dc=-p-14q<0`. The signs `r1<0` are ensured by the previous bound. Thus **every `r3≥0` point is strictly Pareto dominated**, including the double zero.

On `r0=0` within `r3<0`, write `y=Y0(x)`; `Y0'=-4(1-x)^2/(1-y)^2`. The restricted `r1` strictly increases, so has one zero at `q*`. On the left of `q*` where `r1<0`, `b=15r2/16`; its derivative is

\[
 \frac{d r_2(x,Y0(x))}{dx}=\frac45(1-x)^2\{f(x)-f(y)\}<0,\quad f(z)=\frac{z(2-3z)}{(1-z)^2}.
\]

Indeed `f` increases below `1/2`, decreases above it, and the exact endpoint inequality is `f(469/2000)<f(623/1000)`. Increasing `x` lowers `b,c`. On the right, `r1>0`, `b=-5r3/16`; as

\[
 \frac{d r_3(x,Y0(x))}{dx}=\frac{12}{5}\frac{(x-y)(x+y-2xy)}{(1-y)^2}<0,
\]

the public budget grows with `x`; but a nearby move into the `(-,+)` chamber at **constant b** strictly reduces audit cost (above). Thus the right `r0=0` arc is not the constrained minimizer.

On `r1=0` write `y=Y1(x)`;

\[
 Y1'=\frac{4(1-x)(1-3x)}{(1-y)(3y-1)}\in(0,5),\qquad (c\circ Y1)'=-p+qY1'<0.
\]

Left of `q*` one has `r0>0` and `b=-5r3/16` strictly decreasing toward `q*`; these points are dominated. Right of `q*`, `r0<0,r3<0`, `b=15r2/16` strictly increases while `c` strictly decreases; this is the **only remaining candidate family**.

For existence and exact bracketing of `q*`, the rational zero-curve bounds from Stage343 remain valid and are rechecked here:

\[
 \frac{231083}{10^6}<x_*<\frac{231085}{10^6},\quad
 \frac{555496}{10^6}<y_*<\frac{555521}{10^6}.
\]

The left and right rational signs of `r1` on `r0=0` are opposite, and `r1` is strictly increasing there, proving uniqueness. The model's only global `b` minimizer is `q*`: a global minimizer exists by compactness; the enclosure applies since `b(q*)<Q`, and every other point in the enclosure has a strict `b`-descent by the preceding chamber and boundary analysis (`(-,+)` can simply increase `y`). Write

\[
 \beta_*<\frac{60476723775473217}{16000000000000000000}
 =:\beta_U,\qquad \beta_U+1/1000<Q.
\]

At the right endpoint of `R`, `r1(469/2000,566/1000)>0>r1(469/2000,567/1000)` and `15r2(469/2000,566/1000)/16>Q`. The right `r1=0` arc therefore crosses every public budget `β*+s` for `s≤1/1000` **uniquely**. For any fixed sublevel `b≤β*+s`, compactness gives an audit-cost minimizer. Every point outside `q*` and the surviving right `r1=0` arc has an arbitrarily nearby move that strictly reduces audit cost without increasing public error, so cannot minimize. The surviving arc has strictly decreasing `c` and strictly increasing `b` with `x`, making the unique feasible minimum its largest allowed `x`, namely `q_s`. This proves the stronger unique constrained audit optimum

\[
 \boxed{\forall q\in[0,1]^2:\ b(q)\le\beta_*+s\Longrightarrow c(q)\ge c(q_s),\quad
 c(q)=c(q_s)\iff q=q_s.}\tag{2}
\]

All statements have the exact scope `0≤s≤1/1000`, with no assumption of a differentiable objective at residual-zero or tag-zero cusps.

## Lemma 3 — *new* strict curvature box and two-source allocation

The right arc through the entire new `E` interval is inside the **new exact box**

\[
 C=[231/1000,293/1250]\times[555/1000,566/1000],
\]

strictly below `y†`. Indeed at `x_C=293/1250=0.2344`, `r1(x_C,565/1000)>0>r1(x_C,566/1000)` and

\[
 \frac{15}{16}r_2(x_C,565/1000)>\beta_U+\frac1{1000};
\]

`r2` is increasing in `y`, so the candidate has exhausted more than the allowed budget before reaching `x_C`. The lower bounds follow from the `q*` isolating interval and increasing `Y1`.

Let `Y=Y1(x)`, `g(y)=(1-y)(3y-1)`. Exact differentiation gives

\[
 Y'=\frac{4(1-x)(1-3x)}{g(Y)},\quad
 Y''=\frac{4(6x-4)+(6Y-4)(Y')^2}{g(Y)}.
\]

On `C`, exact endpoint rational bounds (verified by the checker) are

\[
 3<Y'<16/5,\quad -59<Y''<-52,
\]
\[
 0<b'<7/20,\qquad b''<-3,
\qquad c'<-39/100,\qquad c''<9/8,
\]

where primes now denote **derivatives along the curve with respect to `x`**. These follow from the exact identities

\[
 b'=\frac3{16}[4x(2-3x)+Y(2-3Y)Y'],\quad
 b''=\frac3{16}[4(2-6x)+(2-6Y)(Y')^2+Y(2-3Y)Y''],
\]
\[
 c'=-p(x)+q(Y)Y',\quad
 c''=\frac{372-366x}{256}+\frac{3(1-2Y)}{64}(Y')^2+q(Y)Y''.
\]

Since the last two terms of `c''` are nonpositive on `C` and `b''` is strictly negative, the *exact global* upper bound for the curvature numerator is

\[
 c''b'-c'b''<\frac98\cdot\frac7{20}-\frac{39}{100}\cdot3=-\frac{621}{800}<0.
\]

Writing `φ(s)=c(q_s)` with `s=b(q_s)-β*`, the chain rule yields

\[
 \phi'(s)=\frac{c'}{b'}<0,\qquad
 \phi''(s)=\frac{c''b'-c'b''}{(b')^3}<0.
\]

For any feasible `(q1,q2)`, put `s_i=b(q_i)-β*≥0`. Then `s1+s2≤E`, and (2) gives `c(q_i)≥φ(s_i)` with equality only at `q_i=q_{s_i}`. The strict decrease of `φ` forces `s1+s2=E` at an optimum. The map `t↦φ(t)+φ(E-t)` is strictly concave on `[0,E]`; its only minima are the two endpoints `0,E` (coincident if `E=0`). The equality conditions in (2) identify the unique source-ordered optimizers. QED.

## Execution, limitations and next question

`REPRO_STAGE344B.py` is the exact `Fraction`/SymPy checker using the Stage343 method but revised numeric bounds; it regenerates the 223-leaf certificate, checks every row and the complete dyadic cover, all 16 source-tag signs and differentiated gradients, rational bracket inequalities and strict curvature intervals. `REPRO_STAGE344B_EXECUTED_STDOUT.txt` records two real consistent executions. SHA256 of the committed CSV is given by the actual checker log. The checked full-cover certificate and displayed analytic derivative/sign proof imply the continuous-real quantifiers. Independent review and formal proof checking are not claimed.

Smallest next Stage345-B question: extend to `E=0.0012` with a fresh certified `Q>β_U+0.0012`, or exhibit a *rigorous exact* two-source counterexample; classify new entry of the right curve/cusp and any failure of the pointwise audit-descent certificate. P000-native six-axis/three-dimensional-slice/time/triadic closure/final Cell address observer fidelity remains a completely separate proof obligation.
