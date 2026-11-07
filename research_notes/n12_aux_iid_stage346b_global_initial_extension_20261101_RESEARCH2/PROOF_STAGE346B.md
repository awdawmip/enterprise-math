# Stage346-B — Global initial Pareto allocation through E = 7/5000 with a low-y audit barrier

**Date:** 2026-11-01 (Asia/Shanghai). **Status:** PORTABLE_AUTHOR_THEOREM / EXACT_FRACTION_BERNSTEIN_EXECUTED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. This is a theorem of the *declared auxiliary three-visit, two-source, sixteen-tag Bernoulli/BRC observer*, not a native P000 X6 or physical theorem. This work reuses the predecessor Stage345-B author proof at its original unreviewed evidence level, not as independent admission.

## Sources and immutability

- Normative GLOBAL_KNOWLEDGE_V1 read pin: `awdawmip/chatgpt-global-knowledge main@b33cf2f18b4fbfd428312f384310cb2601c68a79`, with `00_BOOTSTRAP.md`, `OPERATING_MANUAL.md`, Enterprise Math project and task routes, P000 V4 original (blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`, matching its `P000_STARTUP.json` projection), ACTIVE `我眼中的世界.md`, BRC, mathematics, code, activity and journal policies.
- Enterprise Math current canonical code/control read pin: `awdawmip/enterprise-math main@ce7279d4cafc8d7ddb4a65d75c33e8c40849428c`, `AGENTS.md`, `docs/AUTONOMOUS_RESEARCH_OPERATIONS.zh-CN.md` and `docs/PORTABLE_RESEARCH_PROTOCOL.md`.
- Exact author predecessor: Stage345-B `PROOF_STAGE345B.md`, `REPRO_STAGE345B.py` and 424-leaf evidence at immutable commit `72f47be9e58e66699999d51f229c5a7ca8af15da` (Draft PR #1736). Inherited: the observer definitions, uniqueness of the global `b`-minimum at `q*`, the one-source inequality for `0<=s<=3/2500`, and zero-stratum algebra, all at **author/unreviewed** status. Newly constructed here: global 193-leaf cover, **1615-leaf low-y cost barrier**, tighter q* isolator, old-endpoint comparison and enlarged curvature certificate.
- Native control `em_status` was readable, but the owner/tasks inquiry returned `CONTROL_QUOTA` and checkpoint-list returned `ACCESS_DENIED`; `authority_granted=false` from directed-research manifest. No owner, claimant, Source Result, execution/session capability or independent reviewer was inferred.

## The typed auxiliary observer and statement

For `k=0,1,2,3`, `z in [0,1]`, set

\[
 B_k(z)=z^k(1-z)^{3-k},\quad w=(1,3,3,1),\quad m=(61,21,9,9),
\]
\[
 r_k(x,y)=\frac{4B_k(x)+B_k(y)}5-\frac{m_k}{160},\quad
 b(x,y)=\frac5{32}\sum_{k=0}^3w_k|r_k(x,y)|,
\]
\[
 D_3(a,z)=\frac12\sum_{k=0}^3w_k|B_k(a)-B_k(z)|,\quad
 c(x,y)=\frac{63D_3(1/4,x)+D_3(3/4,x)+9D_3(1/4,y)+7D_3(3/4,y)}{256}.
\]

The four reference/coordinate pairs each have four independently signed word comparisons: **16 tagged comparisons** are retained, and all absolute values are resolved before differentiating. The two source groups are independent parameter choices `q1,q2 in [0,1]^2`, with public budget `P=b(q1)+b(q2)` and audit objective `T=33/1024+c(q1)+c(q2)`. This is BRC **REUSE_APPLIED / EXACT_LABELED_OBSERVER_COMPUTED**, not a claim that scalar totals preserve all future provenance-sensitive observations. The advertised result is only for these fixed observers and this fixed two-source optimization problem.

Let `q*=(x*,y*)` be the unique solution `r0=r1=0`, let `beta*=b(q*)`, and let `q_s` be the unique point on the right `r1=0` arc (`r0<0,r3<0`) with `b(q_s)=beta*+s` (so `q_0=q*`).

**Stage346-B author theorem (continuous parameters):** for every real `0<=E<=7/5000=0.0014`,

\[
 \boxed{\min_{q_1,q_2\in[0,1]^2:\ P\le2\beta_*+E}T
 =\frac{33}{1024}+c(q_*)+c(q_E).}
\]

For `E=0`, the only ordered minimizer is `(q*,q*)`. For `0<E<=7/5000`, the only ordered minimizers are `(q*,q_E)` and `(q_E,q*)`. This extends Stage345-B's `3/2500=0.0012` author interval by `1/5000=0.0002`, a **16.67%** increase over the earlier upper endpoint. The first change in the global allocation structure, if it exists, must occur strictly beyond `0.0014` in this auxiliary model. The exact first-switch location is not established.

## I. Exact continuum enclosure: 193 leaves on the full square

Set

\[
 Q=\frac{21}{4000}=0.00525,\qquad
 R=\left[\frac{89}{400},\frac{473}{2000}\right]\times\left[\frac{21}{40},\frac{63}{100}\right].
\]

**Enclosure:** for every real `q in [0,1]^2`, `b(q)<=Q => q in R`.

`sum_k w_k r_k=0`, so `b=(5/16)sum_k w_k (r_k)_+`. For every nonempty tag-mask `S subseteq {0,1,2,3}`, put `F_S(z)=sum_{k in S} w_k B_k(z)`, `M_S=sum_{k in S}w_k m_k`. For a rational interval `[u,v]`, the four degree-three Bernstein controls of the cubic `F_S` are exactly

\[
 F_S(u),\quad F_S(u)+\frac{v-u}{3}F'_S(u),\quad F_S(v)-\frac{v-u}{3}F'_S(v),\quad F_S(v).
\]

Their minimum `L_S[u,v]` bounds `F_S` below over the **entire real interval**. Thus for a rational rectangle `H=[a,b]x[c,d]`,

\[
 b(x,y)\ge\frac5{16}\left[\frac{4L_S[a,b]+L_S[c,d]}5-\frac{M_S}{160}\right].\tag{1}
\]

`CERTIFICATE_STAGE346B_GLOBAL.csv` gives the **complete 193-leaf recursive quadtree** partition of `[0,1]^2`: `130 HIGH_B` leaves each with an exact (1) bound `>Q`, `63 INNER` leaves entirely in `R`, maximum depth `10`, exact area sum `1`, all four descendants for every split ancestor and no overlapping ancestor leaves. `REPRO_STAGE346B.py` independently rebuilds the quadtree by rational arithmetic, verifies the entire leaf table and the stated bound. This is a continuum exclusion via the Bernstein convex-hull theorem, not grid sampling. As `beta*+7/5000<Q` (see part IV), every point in any investigated feasible sublevel is in the **interior** of R by continuity.

On R, `r2>0` follows from `B_2'(z)=z(2-3z)>0` on both coordinate intervals and exact positivity at the lower corner. Importantly, `r3` changes sign in R and cannot be treated as uniformly negative.

## II. New exact low-y audit barrier: 1615 leaves

**This is the structural change versus Stage345-B.** On the enlarged R the old uniform cost-descent ratio *fails* for the `(-,+)` residual chamber near `y=0.525`. Indeed, the naively reused `q Y'_b<p` cannot be certified for this whole rectangle; retaining the old inequality would leave a real proof gap. Instead cut at

\[
 y_c=\frac{531}{1000}=0.531,\qquad C_0=\frac{3149}{100000}=0.03149.
\]

For all real `(x,y) in R` with `y<=y_c`, the exact **dichotomy** is

\[
 \boxed{b(x,y)>Q\quad\text{or}\quad c(x,y)>C_0.}\tag{2}
\]

On the strip `H=[89/400,473/2000]x[21/40,531/1000]`, the sixteen tags have fixed signs. SymPy symbolically checks the exact tagged derivative identities, including

\[
 c_x=-\frac{(1-x)(189-183x)}{256},\quad
 c_y=\frac{3y(1-y)}{64},
\]

and the exact separable cubic form

\[
 c(x,y)=K+\frac{-189x+186x^2-61x^3}{256}+\frac{3y^2-2y^3}{128},\tag{3}
\]

where `K` is fixed by the source-tag formula at `(23/100,53/100)` (and cross-checked at a different exact rational point). For any dyadic rectangle in H, the sum of the minima of the separate **cubic Bernstein controls** for the two nonconstant terms in (3), plus K, gives a rigorous global lower bound on `c` throughout that rectangle. Applying either this `c` bound or (1) produces `CERTIFICATE_STAGE346B_LOW_STRIP.csv`: a complete **1615-leaf** rational recursive partition of H, `833 HIGH_B` leaves with `b>Q` and `782 HIGH_C` leaves with `c>C_0`; maximum depth `11`, exact area sum `(7/500)*(3/500)=21/250000`. All leaves, rational bounds, indices and ancestry are checked by the executable source. Therefore (2) holds on the entire **continuum**, including edges and corners, without assuming a false global gradient sign.

The barrier is quantitative enough to *exclude the strip from optimality for the newly added budgets*. In fact, the old candidate `q_{3/2500}` satisfies

\[
 c(q_{3/2500})<C_0.\tag{4}
\]

For (4), the verifier first tightens the double-zero isolator to

\[
 \frac{2310839408}{10^{10}}<x_*<\frac{2310839409}{10^{10}},\qquad
 \frac{555508855}{10^9}<y_*<\frac{555508860}{10^9},
\]

using exact `r0` brackets at the two x endpoints and strictly opposite `r1` signs along the implicitly defined `r0=0` curve. Because `r2` increases in both coordinates, this yields tight rational `beta_L<beta*<beta_U`; the verifier then brackets the old endpoint `q_{3/2500}` using the exact `r1` signs and `15r2/16` budget at `x=234719/10^6` and `x=234722/10^6`. Its coordinates satisfy

\[
 x_{3/2500}>\frac{234719}{10^6},\qquad
 y_{3/2500}<\frac{566725}{10^6};
\]

`c_x<0`, `c_y>0` below the cusp, and a final exact rational test gives

\[
 c(q_{3/2500})<c\left(\frac{234719}{10^6},\frac{566725}{10^6}\right)<\frac{3149}{100000}.
\]

Since the candidate audit `s -> c(q_s)` decreases strictly, (4) and (2) exclude all low-y points for **every** `3/2500<=s<=7/5000`. For `s<=3/2500`, use the explicitly inherited Stage345-B one-source theorem instead. It would be invalid to use `c(q_E)<C_0` alone for every smaller `s`, and this proof does not do so.

## III. Audit descent for the surviving high-y region

On the region `R_high=R intersect {y>=531/1000}`, the old `(-,+)` constant-public-error direction has its strict sign restored. Tag signs on R remain exactly

- `(a=1/4,x): -+++`, `(a=3/4,x): --++`;
- `(a=1/4,y): ++--`, `(a=3/4,y): --σ+`, switching its third-word sign at `y_dagger=(1+sqrt(13))/8`.

Symbolic differentiation from all 16 tagged comparisons gives

\[
 c_x=-p(x),\quad p(x)=\frac{(1-x)(189-183x)}{256}>\frac{43}{100},
\]
\[
 c_y=q(y)=\begin{cases}\frac{3y(1-y)}{64},&y<y_\dagger,\\[2pt]
 \frac{3y(18-25y)}{256},&y>y_\dagger.\end{cases}
\]

Both one-sided `q` values are positive and bounded by `1/40`; below the cusp, `q<=3/256`. In `r3<0,r2>0`, conservation yields

\[
 b=\frac5{16}\{-r_3+(-r_0)_++3(-r_1)_+\}.
\]

All strict chambers have a `b`-nonincreasing, `c`-decreasing local direction: `(r0,r1)=(+,+)` and `(+,-)` increase x; `(-,-)` decrease y; and `(-,+)` move along the exact constant-b curve

\[
 dx>0,\qquad\frac{dy}{dx}=\frac{4(1-2x)}{2y-1}>0.
\]

This is a strict audit descent even through the cusp, because **exact rational** comparisons for `y>=531/1000` give

\[
 \underbrace{\frac3{256}\frac{4(1-2x_{\min})}{2y_c-1}}_{1665/3968<0.42}
 <0.43<p(x_{\max}),
\]
\[
 \underbrace{\frac1{40}\frac{4(1-2x_{\min})}{2(23/40)-1}}_{37/100=0.37}
 <0.43<p(x_{\max}).
\]

The second inequality applies above the algebraic cusp because `y_dagger>23/40`.

For `r3>=0`, exact endpoint tests at `(x_max,610/1000)` imply `r3>=0 => y>610/1000` and `r1<0`. The **full residual-positive and zero classification** remains valid with the enlarged R: `r3>0,r0>0` increase x, `r3>0,r0<0` decrease y, `r3>0,r0=0` decrease y into the `r0>0` chamber; `r3=0,r0>0` increase x and `r3=0,r0<0` decrease y. The only `r0=r3=0` point is isolated by `1133/5000<x<567/2500` and `616/1000<y<617/1000` using exact signs and monotone `r0` along `r3=0`. There the direction `(dx,dy)=(1,-14)` strictly decreases `r0,r2,r3` while leaving `r1<0`, and decreases both `b` and `c`; the three component inequalities are independently checked in the source.

The residual-zero curves require care:

1. On `r0=0`, let `y=Y0(x)` with `Y0'=-4(1-x)^2/(1-y)^2<0`. Along this curve `r1` increases strictly with x; its only zero is `q*`. Left of `q*`, `r1<0` and `b=15r2/16` decreases with x, because
   \[
   \frac{dr_2(x,Y_0(x))}{dx}=\frac45(1-x)^2[f(x)-f(y)]<0,\quad f(z)=\frac{z(2-3z)}{(1-z)^2}.
   \]
   The new enlarged interval needs a split rather than the old false full-R endpoint inequality: if `y<=3/5`, `f(y)>=f(3/5)>f(x*)>=f(x)`; if `y>=3/5`, the sign `r0(228/1000,3/5)<0` forces `x<228/1000` on `r0=0`, so `f(x)<=f(228/1000)<f(63/100)<=f(y)`. All endpoint comparisons are exact. The audit `c` decreases since `c_x<0,c_y>0,Y0'<0`. Right of `q*`, with `r1>0`, the `(-,+)` constant-b direction goes into `r0<0` and decreases `c` whenever `y>=y_c`; all lower-y competitors are already excluded by (2).
2. On `r1=0` let `y=Y1(x)`, with
   \[
   Y_1'=\frac{4(1-x)(1-3x)}{(1-y)(3y-1)}\in(0,5)
   \]
   on R. Therefore `dc/dx=-p+qY1'<-0.43+5/40<0` throughout, including one-sided at the cusp. Left of `q*`, `r0>0` and `b=-5r3/16` decreases with x; right of `q*`, `r0<0,r3<0` and `b=15r2/16` increases with x. The latter is the *only* possible constrained c-minimum arc not excluded by local descent and the strip barrier.

This classification handles the artificial `y=y_c` boundary: it lies within the strip's strict audit barrier and thus cannot minimize `c` at the relevant budgets. Global enclosure gives a strict R interior for feasible points, so no external R-edge minimizer was lost.

From the tight beta bracket and the monotonicity of the right arc, the new endpoint `q_E` lies strictly between `x=2353/10000` and `x=2355/10000`, with `y_E<5691/10000<0.570`; the checker verifies the exact `r1` crossing and public-budget inequalities. The right arc therefore uniquely realizes all `s in [0,E]`.

For any `s in [3/2500,7/5000]`, a constrained audit minimizer exists by compactness. The strip barrier (2)--(4) excludes low y, the high-y descent classification excludes all other chambers/zero arcs, and the remaining arc has strictly decreasing c as b increases. Hence

\[
 \boxed{b(q)\le\beta_*+s\implies c(q)\ge c(q_s),\quad
 c(q)=c(q_s)\iff q=q_s.}\tag{5}
\]

For `0<=s<=3/2500`, (5) is the explicitly inherited Stage345-B author result. Together, (5) holds for the enlarged full continuum interval at the author-proof level.

## IV. Curvature box and global two-source allocation

The right `r1=0` arc from `q*` to `q_E` lies in

\[
 C=[231/1000,236/1000]\times[555/1000,570/1000],
\]

strictly below the source-tag cusp. Write `Y=Y1(x)`, `g(Y)=(1-Y)(3Y-1)`. Then

\[
 Y'=\frac{4(1-x)(1-3x)}{g(Y)},\qquad
 Y''=\frac{4(6x-4)+(6Y-4)(Y')^2}{g(Y)}.
\]

The exact checker proves an enclosing derivative interval, with lower/upper endpoints printed as fractions:

\[
 \frac{29}{10}<Y'<\frac{33}{10},\qquad
 -\frac{710092}{11837}<Y''<-\frac{152138}{3053},
\]

and from the exact derivative identities

\[
 b'=\frac3{16}(4x(2-3x)+Y(2-3Y)Y'),
\]
\[
 b''=\frac3{16}(4(2-6x)+(2-6Y)(Y')^2+Y(2-3Y)Y''),
\]
\[
 c'=-p(x)+q(Y)Y',\qquad
 c''=\frac{372-366x}{256}+\frac{3(1-2Y)}{64}(Y')^2+q(Y)Y'',
\]

the rational inequalities

\[
 0<b'<\frac{10999203}{32000000},\quad
 b''<-\frac{1553968929}{488480000}<0,
\]
\[
 c'<-\frac{6343773}{16000000}<0,\quad
 c''<\frac{143727}{128000}.
\]

The last two terms in c'' are nonpositive on C; the other interval bounds use the actual monotonic directions of all factors, not floating estimates. Thus

\[
 \boxed{c''b'-c'b''<-
 \frac{54732038484178971}{62525440000000000}<0.}\tag{6}
\]

With `phi(s)=c(q_s)`, `s=b(q_s)-beta*`, the inverse function theorem gives

\[
 \phi'(s)=c'/b'<0,\qquad
 \phi''(s)=\frac{c''b'-c'b''}{(b')^3}<0
\]

throughout `[0,7/5000]` (one-sided at endpoints). The double-zero b minimum `q*` is unique by the inherited global result, so every feasible two-source pair has `s_i=b(q_i)-beta*>=0` with `s1+s2<=E`. Apply the new (5) to each source, use strict decrease of `phi` to exhaust the budget, and use strict concavity to minimize `phi(s1)+phi(E-s1)` only at the endpoints `s1=0,E`. Equality in (5) gives precisely `(q*,q_E)` and its swap (one pair at zero budget).

## Executed evidence, limits, handoff

Reproduction: run `python REPRO_STAGE346B.py` with Python `fractions.Fraction`, `csv` and SymPy. It reconstructs the original 193-leaf global and 1615-leaf low-y CSVs from scratch, verifies CSV equality, exact dyadic ancestry and area, all strict Bernstein bounds, all 16 signed derivative formulas, exact q* and old/new endpoint isolators, residual branch inequalities and curvature. `REPRO_STAGE346B_EXECUTED_STDOUT.txt` records two **actually executed** matching runs. The exact CSVs, code and proof together make the full author argument reproducible. A successful checker is not independent peer review; formal proof assistant verification and adversarial replication have not occurred.

**Next Stage347-B:** attempt `E<=8/5000=0.0016`, where the low-y audit barrier must be recalculated because the right candidate c decreases further while the b-sublevel expands. Explore whether the new zero-boundary candidate on `r0=0` can cross the right `r1=0` frontier, and derive the first global allocation switch or a rational competitor. Do not silently assume Stage346-B's numerical strip threshold beyond its Q. Preserve X6 source path algebra, true three-dimensional slice third component, triadic closure, independent physical time, and final Cell address observer-fidelity as *separate* proof obligations.
