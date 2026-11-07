# Enterprise Math — Stage348-B: exact global initial allocation extension to E=9/5000

**Date:** 2026-11-01 (Asia/Shanghai). **Status:** PORTABLE_AUTHOR_THEOREM / EXACT_RATIONAL_BERNSTEIN_EXECUTED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. This is an author proof with explicitly inherited, unreviewed analytic lemmas; it is not a native Source Result or Foundation promotion.

## Frozen input, provenance and type boundary

- Verified GLOBAL_KNOWLEDGE_V1 `main@eefc162283b2f27ce1333bde7e9ff7cc81e6b1d1`: canonical `00_BOOTSTRAP.md`, `OPERATING_MANUAL.md`, project role router, P000 V4 original and matching `P000_STARTUP.json` projection blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`, ACTIVE worldview, mathematical/code/BRC and activity policies. This pin is fixed for this unit.
- Enterprise Math canonical `main@ca3a36728e8452c131b82a03bd7988c4a492ce3c`: `AGENTS.md`, `docs/AUTONOMOUS_RESEARCH_OPERATIONS.zh-CN.md`, `docs/PORTABLE_RESEARCH_PROTOCOL.md`.
- Immediate exact predecessor Stage347-B: Draft PR #1736 head `8f365417c123464ee50ab8d9a2415556a6e22f6a`, file `research_notes/n12_aux_iid_stage347b_global_initial_extension_20261101_RESEARCH2/PROOF_STAGE347B.md`, verifier and immutable CSV certificates. Stage336/342 r3>=0 dominance, Stage346 base interval and unique b-minimum are **author-level premises**, not independently admitted propositions.
- Scientific carrier: sixteen separately labeled Bernoulli output words, branch/source identities intact. The observer is an **external auxiliary two-parameter rational probability model**, not a native six-axis/three-dimensional-slice construction. In particular the missing third slice coordinate is not set to zero. The native P000 X6, triadic balance, time, and lossless Cell address map are unproved transfer obligations.
- Own present work has no confirmed active task Owner or service-issued Researcher claim; control listing returned `CONTROL_QUOTA`, source manifest reports `authority_granted=false`. No new identity or authority is inferred from the previous assistant/PR author history.

## Model, inherited inputs and statement

For k=0,1,2,3 define `B_k(z)=z^k(1-z)^(3-k)`, binomial multiplicities `w=(1,3,3,1)` and target unnormalized word data `m=(61,21,9,9)`. Put

\[
 r_k(x,y)=\frac{4B_k(x)+B_k(y)}5-\frac{m_k}{160},\qquad
 b(x,y)=\frac5{32}\sum_{k=0}^3w_k|r_k(x,y)|,
\]

\[
 D_3(a,z)=\frac12\sum_{k=0}^3w_k|B_k(a)-B_k(z)|,\qquad
 c(x,y)=\frac{63D_3(1/4,x)+D_3(3/4,x)+9D_3(1/4,y)+7D_3(3/4,y)}{256}.
\]

The sixteen comparison coordinates **remain labeled** and are not collapsed to only a total variation mass. Assume the inherited unique global b-minimizer `q_*=(x_*,y_*)` with `r0(q_*)=r1(q_*)=0`, `beta_*=b(q_*)`, and the right `r1=0` arc `q_s=(x_s,Y_1(x_s))` with `b(q_s)=beta_*+s` and `r0,r3<0`. Its known b-minimizer isolation is

\[
 2310839408/10^{10}<x_*<2310839409/10^{10},\quad
 555508855/10^9<y_*<555508860/10^9.
\]

**Theorem (author level, with inherited prior lemmas).** For every real `0<=E<=9/5000=0.0018`, over **all** ordered pairs `q1,q2 in [0,1]^2` with `b(q1)+b(q2)<=2 beta_*+E`, the minimum of `T=33/1024+c(q1)+c(q2)` equals

\[
 \boxed{\min T=\frac{33}{1024}+c(q_*)+c(q_E).}
\]

The unique minimizer at E=0 is `(q_*,q_*)`. At every E>0, the only ordered minimizers are `(q_*,q_E)` and `(q_E,q_*)`. Compared with inherited Stage347-B this expands the proved-author initial interval from `1/625=0.0016` to `9/5000=0.0018` (+12.5%), **without locating the first later switch**.

## 1. New 226-leaf exact global enclosure

Set

\[
 Q=281/50000=0.00562,\qquad R=[11/50,6/25]\times[103/200,127/200].
\]

We prove the continuum statement

\[
 \boxed{b(x,y)\le Q\implies (x,y)\in R}\qquad ((x,y)\in[0,1]^2).
\tag{1}
\]

Let `F_S(z)=sum_{k in S}w_k B_k(z)` and `M_S=sum_{k in S}w_k m_k` for the 16 word masks. Since `sum_k w_k r_k=0` exactly,

\[
 b=\frac5{16}\sum_kw_k(r_k)_+
  =\max_{S\subseteq\{0,1,2,3\}}\frac5{16}\left[\frac{4F_S(x)+F_S(y)}5-\frac{M_S}{160}\right].
\tag{2}
\]

For any cubic polynomial h on a rational interval `[u,v]` its exact degree-3 Bernstein coefficients are `h(u)`, `h(u)+(v-u)h'(u)/3`, `h(v)-(v-u)h'(v)/3`, `h(v)`. Their minimum is an all-real lower bound. We take these independent x and y lower bounds in (2), maximize over masks and subdivide the unit square into four equal rational subrectangles only where needed. `CERTIFICATE_STAGE348B_GLOBAL.csv` has **226 leaves: 133 HIGH_B** leaves where a rational lower bound is strictly above Q, and **93 INNER** leaves wholly contained in R. The quadtree max depth is 10 and exact total area is 1. It certifies (1) across the entire continuum, including boundary points. The checker reconstructs every tree split and every bound from the source rational polynomials.

The inherited b-isolators imply `beta_*+9/5000<Q` by exact Fraction arithmetic. Therefore every feasible source point has `b<Q` and is strictly inside R; otherwise continuity would give a boundary point `b<=Q` outside/intersecting the exterior, contradicting (1) and strictness.

## 2. New 58+1-leaf fused source-tag audit barrier

The inherited middle band `[531/1000,5/8]` does not change; the enlarged outer low-y region must be excluded without presupposing the old barrier. Put

\[
 L=[11/50,6/25]\times[1/2,531/1000],\quad
 H=[11/50,6/25]\times[5/8,127/200],
\]

`C0=31/1000`, `lambda=121/100`. The new strict all-real barriers are

\[
 \boxed{c(x,y)+\lambda b(x,y)>C_0+\lambda Q=\frac{189001}{5000000}}\quad\text{for }(x,y)\in L\cup H.
\tag{3}
\]

The exact threshold is

\[
 C_0+\lambda Q=\frac{31}{1000}+\frac{121}{100}\frac{281}{50000}
 =\frac{189001}{5000000}=0.0378002.
\]

The comparison word signs are fixed over each closed strip: for x against anchors 1/4,3/4, signs `-+++` and `--++`; for low-y `++--`, `--++`; for high-y `++--`, `---+`. All eight signed word differences per coordinate are checked by strict cubic Bernstein controls. The resulting exact polynomial expressions on each strip are

\[
 c=K_j+p_x(x)+p_{y,j}(y),\qquad p_x(x)=\frac{-189x+186x^2-61x^3}{256},
\]

\[
 K_L=\frac{2673}{16384},\quad p_{y,L}(y)=\frac{3y^2-2y^3}{128};\qquad
 K_H=\frac{621}{4096},\quad p_{y,H}(y)=\frac{27y^2-25y^3}{256}.
\]

The code proves these polynomial identities by four-by-four rational interpolation grids plus the strict comparison signs. By (2), for any mask S,

\[
 c+\lambda b\ge K_j-\frac{\lambda M_S}{512}+
 \left[p_x(x)+\frac\lambda4F_S(x)\right]
 +\left[p_{y,j}(y)+\frac\lambda{16}F_S(y)\right].
\tag{4}
\]

Each bracket is cubic, so the sum of its exact degree-3 Bernstein lower bounds on a rectangle is valid everywhere on the rectangle. Select the strongest of 16 lower bounds in (4), and split as needed. `CERTIFICATE_STAGE348B_LOW_STRIP.csv`: **58 FUSED leaves**, max depth 6, exact area `31/50000`. `CERTIFICATE_STAGE348B_HIGH_STRIP.csv`: **1 FUSED root leaf**, depth 0, area `1/5000`. Every lower bound strictly exceeds `189001/5000000`; masks remain explicit in the CSV. Consequently, on either strip,

\[
 b\le Q\implies c>C_0.
\tag{5}
\]

The smaller R-y portion below 1/2 is absent because R begins at `103/200 > 1/2`. The new R bottom also contains some points with `r2<=0`, but these lie in L and are **eliminated by (5)**; no argument assumes r2>0 throughout the enlarged R.

## 3. Exact old/new frontier cost comparison

The isolators for qstar and monotonicity of B2 imply exact rational `beta_L<beta_*<beta_U` obtained by `beta_{L/U}=15*r2(x_{L/U},y_{L/U})/16`. To bound the inherited `s0=1/625` frontier cost, use the rational point

\[
 (x_o,y_o)=(23596/100000,5704/10000).
\]

The exact checks `r1(x_o,y_o)<0`, `15r2(x_o,y_o)/16<beta_L+s0`, and monotonicity of r1 in y and r2 in both variables yield `x_{s0}>x_o`, `Y1(x_{s0})<y_o`, hence

\[
 c(q_{s0})<c(x_o,y_o)=\frac{123961593321361}{4000000000000000}
 \approx0.03099039833<C_0.
\tag{6}
\]

At new `s1=9/5000`, use `(x_l,x_u)=(2365,2367)/10000`, `(y_l,y_u)=(572,573)/1000`. The checker proves

\[
 r_1(x_l,y_l)<0,\quad 15r_2(x_l,y_l)/16<\beta_L+s_1,
\]

\[
 r_1(x_u,y_l)>0>r_1(x_u,y_u),\quad 15r_2(x_u,y_l)/16>\beta_U+s_1.
\]

Since Y1 and b along the relevant right arc are strictly increasing, `x_l<x_{s1}<x_u`, `Y1(x_{s1})<y_u`; exact source-tag signs give `c_x<0,c_y>0` below the cusp, so

\[
 c(q_{s1})<c(x_l,y_u)=\frac{63048486619}{2048000000000}
 \approx0.03078539386<C_0.
\tag{7}
\]

The function `s -> c(q_s)` decreases, so (6)-(7) imply `c(q_s)<C0` throughout `[s0,s1]`. By (5), every b-feasible point in either outer y-strip has strictly greater audit cost than the right-arc candidate.

## 4. Reuse of the unchanged middle-y chamber lemma

After outer-strip exclusion the remaining domain is precisely

\[
 R_{mid}=[11/50,6/25]\times[531/1000,5/8].
\]

This **is identical** to Stage347-B's middle band: `r2>0` holds throughout because B2 is increasing for z<2/3 and `r2(11/50,531/1000)>0` exactly. The imported Stage336/342 author results eliminate `r3=0` and `r3>0` by strict local Pareto domination in their declared rectangle `[.21,.24]×[.5,2/3]`; the current `R_mid` lies inside it.

In `r3<0`, using `sum w_k r_k=0` gives

\[
 b=\frac5{16}\big[-r_3+(-r_0)_++3(-r_1)_+\big].
\tag{8}
\]

Stage347-B's exact residual chamber classification for the unchanged `R_mid` excludes all open `(sign r0,sign r1)` chambers by simultaneous or constant-b descent except the right `r1=0` arc. Its `r0=0` analysis also excludes that zero stratum, including the algebraic tag cusp; left `r1=0` descends toward qstar. The necessary inequalities (constant-b slope bound, r0-curve f-comparisons, and `Y1'<5`) are reevaluated in `REPRO_STAGE348B.py` and remain strict. No new middle-band hypotheses or 2-D native-plane interpretation are introduced.

Therefore using inherited Stage347-B at `s<=s0` and the newly certified exclusions for `s in [s0,s1]`, we obtain the author-level **unique sourcewise frontier**

\[
 b(q)\le\beta_*+s\Longrightarrow c(q)\ge c(q_s),\quad
 [c(q)=c(q_s)\iff q=q_s],\quad 0\le s\le9/5000.
\tag{9}
\]

## 5. Fresh exact curvature box and two-source allocation

The extended right arc from qstar to `q_{s1}` lies within

\[
 C=[231/1000,237/1000]\times[555/1000,573/1000].
\]

This box is strictly below the tag cusp `y_dagger=(1+sqrt(13))/8`, so the c derivatives keep the lower formula. Write `Y=Y1(x)`, `g(Y)=(1-Y)(3Y-1)`. Differentiation of `r1(x,Y(x))=0` gives

\[
 Y'=\frac{4(1-x)(1-3x)}{g(Y)},\qquad
 Y''=\frac{4(6x-4)+(6Y-4)(Y')^2}{g(Y)}.
\]

With interval arithmetic over the entire rational C (no sampling), the checker proves

\[
 \frac{14}5<Y'<\frac{17}5,\quad Y''<-47,\quad
 0<b'<\frac25,\quad b''<-\frac{29}{10},\quad
 c'<-\frac{39}{100},\quad c''<\frac98.
\tag{10}
\]

Here derivatives are along `r1=0`. Using exact formulas

\[
 b'=(3/16)[4x(2-3x)+Y(2-3Y)Y'],
\]
\[
 b''=(3/16)[4(2-6x)+(2-6Y)(Y')^2+Y(2-3Y)Y''],
\]
\[
 c'=-\frac{(1-x)(189-183x)}{256}+\frac{3Y(1-Y)}{64}Y',
\]
\[
 c''=\frac{372-366x}{256}+\frac{3(1-2Y)}{64}(Y')^2+\frac{3Y(1-Y)}{64}Y'',
\]

obtain the new **strict** bound

\[
 \boxed{c''b'-c'b''<\frac98\frac25-\frac{39}{100}\frac{29}{10}
 =-\frac{681}{1000}<0.}
\tag{11}
\]

Since `b'>0`, the budget-parameter cost `phi(s)=c(q_s)` satisfies `phi'(s)<0` and `phi''(s)=(c''b'-c'b'')/(b')^3<0` throughout `[0,9/5000]`. Sourcewise penalties `s_i=b(q_i)-beta_*` are nonnegative (inherited global uniqueness of qstar). Equation (9) gives `c(q_i)>=phi(s_i)`. Because phi decreases, the optimum exhausts the total budget; because phi is strictly concave, `phi(s1)+phi(E-s1)` has as its only minimizers `s1=0` and `s1=E`. Equality in (9) gives exactly `(q_*,q_E)` and its permutation. This proves the stated **conditional author theorem**.

## Exact verification, interpretation, and outstanding obligations

`REPRO_STAGE348B.py` runs without third-party packages under ordinary Python (assertions enabled). It deterministically regenerates and checks the 226, 58 and 1 leaf partitions; verifies every leaf predicate via `Fraction`; checks quadtree coverage; uses exact 4×4 rational polynomial interpolation plus Bernstein sign controls for each tagged strip; and checks all endpoint/curvature and reused middle-band rational inequalities. `REPRO_STAGE348B_EXECUTED_STDOUT.txt` is the output of two actual byte-identical runs. Certificates have SHA256 (hex):

- Global 226 leaves: `39275467b1a180c2ec94f99709a1dd06b8061bc03914ecbbab72e1d4c7dddaf2`;
- Low 58 leaves: `456d8c1d0196e48c7d6fe1d7d4044362f08e10761552cd7171cd4ef1f88255f9`;
- High 1 leaf: `9621fa07e4ab69b610236a52cef0647b9c29ecbf389774c17e2b88b29a4a2ab5`.

These are **exact finite certificates of specified polynomial inequalities on continuous rectangles**, not external prior-art novelty, a formal proof kernel, physical experiment, independent mathematical review, or a Source admission. The analytical derivations and completeness of imported Stage336/342/346/347 lemmas remain review obligations. BRC reuse resolution: `REUSE_APPLIED` for branch-label-preserving positive-rational observer weights and exact source provenance; not a claim of signed-amplitude cancellation or of native-X6 equivalence.

**Next discriminating question (Stage349-B):** Seek the first genuine allocation switch rather than extending by arbitrary increments. Check `E=1/500=0.0020`, exact low-y tag competitor near `y=0.531`, and the cusp budget `~0.0021814`; first attempt rational competition with exact b,c values, then certify a larger interval only if no competitor exists. Independently review prior r3>=0 dominance and the zero-stratum sign topology; separately construct a real P000 X6/three-dimensional-slice/observer-fidelity bridge or an exact information-loss witness.
