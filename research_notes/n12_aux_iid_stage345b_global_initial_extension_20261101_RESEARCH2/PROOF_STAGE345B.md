# Stage345-B — Full-domain initial global Pareto allocation through E=3/2500

Date: 2026-11-01, Asia/Shanghai. Research class: **PORTABLE_AUTHOR_THEOREM / EXACT_FRACTION_BERNSTEIN_EXECUTED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING**. This is a theorem *inside the declared three-visit, source-tagged Bernoulli/BRC auxiliary model*, not about native P000 X6 dynamics or experimental physics. No formal task CLAIM, Source Result, independent review or mathematical admission is implied by this manuscript or its GitHub persistence.

## Pinned inputs and inheritance

Frozen normative GLOBAL_KNOWLEDGE_V1: `awdawmip/chatgpt-global-knowledge main@9037e30aaa0d5c085d9700f1eb924e29496aecf1` (read `00_BOOTSTRAP.md`, `OPERATING_MANUAL.md`, Enterprise Math project/TASK routes, ACTIVE `我眼中的世界.md`, math/code/BRC/activity policies). Frozen EM canonical main: `awdawmip/enterprise-math main@4d349d63a10612d9e196f49791bd5946c6dd9bba` (P000 V5, source Git blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`, observer-preservation and native time contracts, autonomous and portable research protocols). Exact predecessor author's Stage344-B commit: `50b38a08dfeb2a74064723ed0d5f59c3c2e4048c` (Draft PR #1736; prior E=1/1000). Reuses the typed, labeled observer and its exact Bernstein machinery; the **new** Q/R, entire certificate, descent bounds and curvature box are calculated afresh.

The BRC carrier is the 16 labeled source-reference/three-bit-word total-variation comparisons. Output of the declared public observer is a different quantity; their labels and correlations are not collapsed into a native spatial statement. Later observer/future-operation fidelity and X6/three-axis-slice/independent-time/triadic-closure/Cell-address bridges are entirely open.

## Complete model

For `k=0,1,2,3` and `z∈[0,1]`, write

\[
 B_k(z)=z^k(1-z)^{3-k},\quad w=(1,3,3,1),\quad m=(61,21,9,9),
\]
\[
 r_k(x,y)=\frac{4B_k(x)+B_k(y)}5-\frac{m_k}{160},\quad
 b(x,y)=\frac5{32}\sum_{k=0}^{3}w_k|r_k(x,y)|,
\]
\[
 D_3(a,z)=\frac12\sum_{k=0}^{3}w_k|B_k(a)-B_k(z)|,
\quad c(x,y)=\frac{63D_3(1/4,x)+D_3(3/4,x)+9D_3(1/4,y)+7D_3(3/4,y)}{256}.
\]

The *four* reference/coordinate sources of `D_3` and their four word classes are separately tagged, hence 16 signed comparisons; all absolute values in this formula are evaluated **before** a polynomial branch is differentiated. For two separate source groups `q_1,q_2∈[0,1]^2`, set `P=b(q_1)+b(q_2)`, `T=33/1024+c(q_1)+c(q_2)`. Let `q*=(x*,y*)` be the unique root `r_0=r_1=0`, `β*=b(q*)`. On the **right** `r_1=0` arc, define `q_s` by `b(q_s)=β*+s` and `q_0=q*`.

**Stage345 theorem (all real parameters, not a grid):** for every real `0≤E≤3/2500=0.0012`,

\[
 \boxed{\min_{q_1,q_2\in[0,1]^2:\,P\le2\beta_*+E}T
 =\frac{33}{1024}+c(q_*)+c(q_E).}
\]

At `E=0` the only source-ordered optimizer is `(q*,q*)`; at `E>0` the only two are `(q*,q_E)` and its swap. Thus the initial global allocation pattern of the auxiliary model persists through `0.0012` (20% beyond Stage344-B). The assertion is an author proof under the declared model, not an independent formal or Source-accepted theorem.

## I. New 424-leaf exact continuum enclosure

Use

\[
 Q=\frac{501}{100000}=0.00501,\qquad
 R=\left[\frac{2237}{10000},\frac{47}{200}\right]\times
    \left[\frac{531}{1000},\frac{313}{500}\right].
\]

**Claim:** for every *real* `(x,y)∈[0,1]^2`, `b(x,y)≤Q` implies `(x,y)∈R`.

The identity `Σw_kr_k=0` follows exactly from `Σw_km_k=160`. Consequently `b=(5/16)Σ_k w_k(r_k)_+`. For each nonempty mask `S⊆{0,1,2,3}`, let `F_S(z)=Σ_{k∈S}w_k B_k(z)` and `M_S=Σ_{k∈S}w_km_k`. For a rational interval `[u,v]`, use the four cubic Bernstein controls

\[
 F_S(u),\qquad F_S(u)+\tfrac{v-u}{3}F'_S(u),\qquad
 F_S(v)-\tfrac{v-u}{3}F'_S(v),\qquad F_S(v).
\]

Their minimum `L_S[u,v]` is a rigorous lower bound for **every real** `z∈[u,v]`. For any rational rectangle `[a,b_]×[c,d]`, its full-rectangle public-error lower bound is therefore

\[
 b(x,y)\ge\frac5{16}\left[\frac{4L_S[a,b_]+L_S[c,d]}5-\frac{M_S}{160}\right].\tag{1}
\]

`REPRO_STAGE345B.py` rebuilds the quadtree using all 15 nonempty masks and exact `fractions.Fraction` arithmetic, and checks each row of `CERTIFICATE_STAGE345B.csv`. Each leaf is either `HIGH` with an exact rational lower bound **strictly greater than Q**, or `INNER` wholly inside `R`. **424 leaves** form a complete recursive dyadic partition of `[0,1]^2`: **272 HIGH**, **152 INNER**, maximum depth 12, no overlapping ancestor leaves, exact total area 1; every non-leaf has all four children. Therefore (1) proves the continuum enclosure, independent of sampling. If `b<Q`, continuity makes `(x,y)` interior to R (otherwise a point outside R nearby would violate the enclosure).

On R, `r_2>0`: `B_2'(z)=z(2-3z)>0` for both coordinate intervals, and the exact minimum `r_2(2237/10000,531/1000)` is positive. Unlike a false fixed-sign shortcut, `r_3` **does change sign** in this rectangle; its nonnegative branch is handled explicitly below.

## II. Tagged derivatives and a complete local-descent classification

With all 16 reference/word absolute-value signs retained, the four tag sign strings on R are

`(a=1/4,x): -+++`, `(a=3/4,x): --++`, `(a=1/4,y): ++--`, `(a=3/4,y): --σ+`.

Only the last third-word comparison switches, at

\[
 y_\dagger=\frac{1+\sqrt{13}}8,\quad
 B_2(3/4)-B_2(y)=\frac{(4y-3)(16y^2-4y-3)}{64}.
\]

The checker verifies all fixed signs by exact cubic Bernstein controls and both symbolic gradient identities from the original 16-tag formula. It gives

\[
 c_x=-p(x)=-\frac{(1-x)(189-183x)}{256}< -\frac{43}{100},\qquad
 c_y=q(y)=\begin{cases}\frac{3y(1-y)}{64},&y<y_\dagger,\\[2pt]
 \frac{3y(18-25y)}{256},&y>y_\dagger.\end{cases}
\]

The one-sided `c_y` are strictly positive at the cusp and throughout R, with `0<q<1/40`; for `y<y†`, `q≤3/256`. Thus increasing x or decreasing y always improves the tagged audit cost (the cusp needs only piecewise integration).

**For `r_3<0`**, with `r_2>0`, conservation gives

\[
 b=\frac5{16}\{-r_3+(-r_0)_++3(-r_1)_+\}.
\]

In strict `(sign r0,sign r1)` chambers:

- `(+,+)`: increasing x decreases `b`, because `b_x=-3x²/4<0`, and decreases `c`.
- `(+,-)`: increasing x decreases `b`, because `b_x=-3(1-2x)²/4<0`, and decreases `c`.
- `(-,-)`: decreasing y decreases `b`, because `b_y=3y(2-3y)/16>0`, and decreases `c`.
- `(-,+)`: move along the local **constant-b** direction `dx>0`, `dy/dx=4(1-2x)/(2y-1)>0` since `b_x=3(1-2x)/4>0` and `b_y=-3(2y-1)/16<0`. The exact uniform inequalities on R are

\[
 \frac{3}{256}\frac{4(1-2x_{\min})}{2y_{\min}-1}
 =\frac{8289}{19840}<\frac{42}{100}<\frac{43}{100}<p(x_{\max}),
\]
\[
 \frac1{40}\frac{4(1-2x_{\min})}{2(23/40)-1}
 =\frac{921}{2500}<\frac{37}{100}<p(x_{\max})
\]

below and above `y†` respectively (exact check `y†>23/40`). Hence `dc/dx=-p+q(dy/dx)<0`, even through the cusp. No strict chamber except the candidate zero curve can contain a constrained audit minimum.

**For `r_3≥0`**, monotonicity and the exact endpoint tests `r_3(47/200,612/1000)<0` and `r_1(47/200,612/1000)<0` force `y>612/1000` and `r_1<0`. If `r_3>0,r_0>0`, increasing x decreases both errors (`b=-15r_1/16`). If `r_3>0,r_0<0`, decreasing y decreases both (`b_y=3y(1-y)/8>0`). If `r_3>0,r_0=0`, decrease y into `r_0>0` (`b_y=3(1-y)(3y-1)/16>0` at the boundary). If `r_3=0,r_0>0`, increase x into the preceding `r_3>0` chamber. If `r_3=0,r_0<0`, decrease y into `r_3<0,r_0<0,r_1<0`, where `b=15r_2/16`, `b_y>0`.

At the **unique** `r_0=r_3=0` point, put `Y_3(x)` for `r_3=0`; `Y_3'=-4x²/Y_3²` and `d(r_0(x,Y_3(x)))/dx<0` since `x<Y_3`. Exact rational signs bracket this unique point in

\[
 1133/5000<x<567/2500,\qquad 616/1000<y<617/1000.
\]

The vector `d=(1,-14)` strictly decreases `r_0,r_3,r_2`, by the three checked inequalities `2(1-x)^2>7(1-y)^2`, `2x²<7y²`, `4x(2-3x)<14y(2-3y)` on the isolating box. Here `r_1<0<r_2`, and immediately along d all of `r_0,r_1,r_3` are negative, so `Db=15Dr_2/16<0`, while `Dc=-p-14q<0`. The boundary/corner is strictly dominated.

**For residual zero curves with `r_3<0`:** On `r_0=0` write `y=Y_0(x)` with `Y_0'=-4(1-x)^2/(1-y)^2`. Along this curve `r_1` strictly increases: its derivative equals `8(1-x)(y-x)/(5(1-y))>0`, so its unique zero is `q*` (bracketed below). Left of q*, `r_1<0`, `b=15r_2/16` decreases as x increases, since

\[
 \frac{d r_2(x,Y_0(x))}{dx}=\frac45(1-x)^2[f(x)-f(y)]<0,\qquad
 f(z)=\frac{z(2-3z)}{(1-z)^2},
\]

and `f(x_max)<f(y_max)` holds exactly (f grows for z<1/2 and decreases for z>1/2). The audit cost also decreases. Right of q*, `r_1>0`; moving into the `(-,+)` chamber along its constant-b direction improves c. On the left `r_1=0` arc (`r_0>0`) increasing x increases y and `r_3`, thus strictly decreases `b=-5r_3/16` and c. On the **right** `r_1=0` arc (`r_0<0,r_3<0`), `b=15r_2/16` strictly increases and c strictly decreases with x: this arc and q* are the only possible constrained audit minimizers.

For `r_1=0`, the implicit derivative is

\[
 Y_1'=\frac{4(1-x)(1-3x)}{(1-y)(3y-1)}\in(0,5)
\]

throughout R (the endpoint bound is checked by exact rationals); hence `dc/dx=-p+qY_1'<-43/100+5/40<0`. For both zero curves the full sign-branch argument is local and uses strict inequalities away from q*; it does not assume differentiability at a cusp.

The exact sign isolators

\[
 231083/10^6<x_*<231085/10^6,\qquad
 555496/10^6<y_*<555521/10^6
\]

prove existence/uniqueness of q*: along `r_0=0`, `r_1` changes sign once and is strictly increasing. Every other point with `b≤Q` has a local **b-decreasing** direction (at `(-,+)` choose `y` increasing); by compactness and the enclosure q* is the unique global minimum of b on `[0,1]^2`. The exact upper bound is

\[
 \beta_*<\beta_U:=\frac{60476723775473217}{16000000000000000000},\qquad
 \beta_U+\frac3{2500}<Q.
\]

At `x=47/200`, `r_1(x,567/1000)>0>r_1(x,568/1000)`, and `15r_2(x,567/1000)/16>Q`; moreover `r_0<0,r_3<0`. Therefore the surviving right arc uniquely crosses every `β*+s` with `0≤s≤3/2500`, strictly within R. Fix such an s. A constrained c-minimizer exists by compactness; all other strata have a local competitor decreasing c **without increasing b**, so it must lie on the surviving arc. There c decreases as b increases, hence its unique feasible point is q_s. We conclude the global one-source inequality

\[
 \boxed{b(q)\le\beta_*+s\ \Longrightarrow\ c(q)\ge c(q_s),\qquad
 c(q)=c(q_s)\Longleftrightarrow q=q_s.}\tag{2}
\]

This holds for **every real** q and s in their declared ranges.

## III. New exact curvature box and two-source budget splitting

The right `r_1=0` candidate through s=3/2500 stays in the rational box

\[
 C=[231/1000,235/1000]\times[555/1000,568/1000],
\]

strictly below the sole tagged cusp `y†`. Here set `Y=Y_1(x)`, `g(Y)=(1-Y)(3Y-1)`; differentiation gives

\[
 Y'=\frac{4(1-x)(1-3x)}{g(Y)},\qquad
 Y''=\frac{4(6x-4)+(6Y-4)(Y')^2}{g(Y)}.
\]

The checker establishes the exact rational uniform comparisons

\[
 \frac{59}{20}<Y'<\frac{16}{5},\quad -59<Y''<-51,\quad
 0<b'<\frac7{20},\quad b''<-3,\quad
 c'<-\frac{39}{100},\quad c''<\frac98.
\]

Here primes refer to x derivatives **along the arc**. They come from the identities

\[
 b'=\frac3{16}\{4x(2-3x)+Y(2-3Y)Y'\},
\]
\[
 b''=\frac3{16}\{4(2-6x)+(2-6Y)(Y')^2+Y(2-3Y)Y''\},
\]
\[
 c'=-p(x)+q(Y)Y',\qquad
 c''=\frac{372-366x}{256}+\frac{3(1-2Y)}{64}(Y')^2+q(Y)Y''.
\]

Because `Y>1/2`, the final two terms of c'' are nonpositive. For b'', `Y(2-3Y)` is positive decreasing on C; interval endpoint substitution is valid. Therefore the curvature numerator is rigorously bounded by

\[
 \boxed{c''b'-c'b''<\frac98\cdot\frac7{20}-\frac{39}{100}\cdot3
 =-\frac{621}{800}<0.}\tag{3}
\]

Writing `φ(s)=c(q_s)` with `s=b(q_s)-β*`, the inverse function rule gives

\[
 \phi'(s)=c'/b'<0,\qquad
 \phi''(s)=\frac{c''b'-c'b''}{(b')^3}<0.
\]

For any feasible `(q_1,q_2)` put `s_i=b(q_i)-β*≥0`; then `s_1+s_2≤E`. Apply (2) to each group. Since φ is strictly decreasing, any optimal split must spend the full budget. By strict concavity the sum `φ(s_1)+φ(E-s_1)` is strictly greater than its (equal) endpoint minimum unless `s_1∈{0,E}`. The equality clause in (2) forces the claimed pair and swap; at E=0 they coincide. This completes the real-parameter proof.

## Evidence, trust limits and next scientific question

`REPRO_STAGE345B.py` uses exact `Fraction` for 424-leaf Bernstein certificates, area/quadtree completeness, endpoint inequalities and curvature bounds; SymPy separately verifies the differentiated **16 tagged** comparison formula. `CERTIFICATE_STAGE345B.csv` is the complete reproducible leaf table. `REPRO_STAGE345B_EXECUTED_STDOUT.txt` contains **two actual matching executions**, not hypothetical expected output. Scientific continuum validity follows from the Bernstein convex-hull theorem plus the above algebraic/monotonic argument, not from sampled grids. Code/checker author validation is not independent formal proof verification. Stage344-B and earlier observer definitions are reused at their author/unreviewed evidence level; their original accepted status was not upgraded.

The next unit Stage346-B asks whether the certificate and curve curvature can extend to `E=7/5000=0.0014`, or whether a typed, exact rational competitor / new residual-zero regime invalidates the current allocation. For that target, `β_U+7/5000<Q` requires a higher Q and a new complete R cover; preserve r3 sign changes and all source tags. Global optimized first-switch location remains unresolved. Explicit X6 observer-fidelity, triadic closure, separate native time, three-dimensional slice third component and final Cell-address semantics remain independent open obligations.
