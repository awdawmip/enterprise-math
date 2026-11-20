# Stage347-B — Global initial Pareto allocation through E=1/625, with coupled source-tag Bernstein barriers

Date: 2026-11-01 (Asia/Shanghai). Research status: **PORTABLE_AUTHOR_THEOREM / EXACT_RATIONAL_EXECUTED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING**. Role: this scheduled Researcher-2 conversation's own portable author work; no native source CLAIM, Owner or independent Driver authority is asserted.

## Immutable scientific input and type scope

- GLOBAL_KNOWLEDGE_V1 canonical read: `awdawmip/chatgpt-global-knowledge main@a684cab5440e1af439f84e8db4a7869cf447a7f1`, with `00_BOOTSTRAP.md`, `OPERATING_MANUAL.md`, active worldview, math/BRC/code/activity/journal routes.
- Enterprise Math canonical read: `awdawmip/enterprise-math main@81360632e34cdd2dee88aae87c91472e2d8c29b4`, with `AGENTS.md`, `p000_reality_foundation.json` (P000 V5), `docs/AUTONOMOUS_RESEARCH_OPERATIONS.zh-CN.md`, `docs/PORTABLE_RESEARCH_PROTOCOL.md` and the persistent research contract.
- Predecessor **author** results at Stage346-B commit `b55f3feab5f337e282f4744a50eab8726dcfb471` in Draft PR #1736: the unique one-source public-error minimum `q_*`, exact isolators for `q_*`, strict global envelope through `E=7/5000`, and signed-chamber/zero-stratum analysis. Stage336-B and Stage342-B author proofs remove the entire `r3=0` and `r3>0` loci respectively inside `[0.21,0.24]×[0.5,2/3]`. These prior claims retain their **unreviewed** status; independent verification is a separate obligation.
- This is a theorem within a **fixed, labeled, three-visit Bernoulli/BRC auxiliary observer**. It neither identifies those parameters with native P000 X6 cells nor proves an X6/slice/triadic/time/address bridge. All 16 source-word tags remain distinct through the definition of the cost, including the cusp comparison.

## Exact observer

For `k=0,1,2,3`, put `B_k(z)=z^k(1-z)^(3-k)`, `w=(1,3,3,1)`, `m=(61,21,9,9)` and

\[
 r_k(x,y)=(4B_k(x)+B_k(y))/5-m_k/160,\qquad
 b(x,y)=\frac5{32}\sum_{k=0}^3w_k|r_k(x,y)|.
\]

With `D_3(a,z)=(1/2) sum_k w_k |B_k(a)-B_k(z)|`, define

\[
 c(x,y)=\frac{63D_3(1/4,x)+D_3(3/4,x)+9D_3(1/4,y)+7D_3(3/4,y)}{256}.
\]

The two-source problem is `P=b(q1)+b(q2) <= 2 beta_*+E`, `T=33/1024+c(q1)+c(q2)` for `q_i in [0,1]^2`. Let `q_*` be the unique `r0=r1=0` global b-minimizer, `beta_*=b(q_*)`. Let `q_s` be the right-hand `r1=0` arc with `r0,r3<0` and `b(q_s)=beta_*+s`.

**Stage347-B author theorem (continuum)**: for every real `0<=E<=1/625=0.0016`,

\[
 \boxed{\min_{q_1,q_2\in[0,1]^2:\,b(q_1)+b(q_2)\le 2\beta_*+E}T
      =\frac{33}{1024}+c(q_*)+c(q_E).}
\]

For `E=0` the sole ordered minimizer is `(q_*,q_*)`. For every `0<E<=1/625`, the only ordered minimizers are `(q_*,q_E)` and `(q_E,q_*)`. This expands the prior author interval from `7/5000` to `8/5000`, a relative extension of **1/7 ≈ 14.29%**. The location of the first later structural change is undetermined.

## I. 193-leaf all-real-parameter enclosure

Set

\[
 Q=\frac{271}{50000}=0.00542,\quad
 R=[11/50,6/25]\times[261/500,127/200].
\]

**Enclosure:** `b(x,y)<=Q` for any real `(x,y) in [0,1]^2` implies `(x,y) in R`.

Because `sum_k w_k r_k=0`,

\[
 b=\frac5{16}\sum_kw_k(r_k)_+
   =\max_{S\subseteq\{0,1,2,3\}}\frac5{16}\bigg[\frac{4F_S(x)+F_S(y)}5-\frac{M_S}{160}\bigg],
\]

where `F_S(z)=sum_{k in S}w_k B_k(z)`, `M_S=sum_{k in S}w_km_k`. For every cubic polynomial `f` on a rational interval `[u,v]`, its degree-3 Bernstein controls are exactly

\[
 f(u),\quad f(u)+\tfrac{v-u}{3}f'(u),\quad f(v)-\tfrac{v-u}{3}f'(v),\quad f(v).
\]

Their minimum bounds `f` below over the full **continuum**. On a rectangle `[a,d]×[e,f]`, using the minima `L_S` of the four controls gives

\[
 b(x,y)\ge \frac5{16}\left[\frac{4L_S[a,d]+L_S[e,f]}5-\frac{M_S}{160}\right]. \tag{1}
\]

`CERTIFICATE_STAGE347B_GLOBAL.csv` is a complete 193-leaf recursive partition of `[0,1]^2`: **123 HIGH_B** leaves with a selected exact (1) bound strictly exceeding `Q`, and **70 INNER** leaves wholly contained in `R`. Maximum depth 10, exact leaf area 1, no missing quadtree children. Thus every real `b<=Q` point belongs to `R`; strict `beta_*+1/625<Q` ensures each feasible point is actually interior to `R` by continuity. Also `r2>0` throughout `R`: each `B2` increases for `0<z<2/3` and `r2(11/50,261/500)>0` exactly.

## II. New *coupled* audit barriers: 55 low-strip leaves and 1 high-strip leaf

Let `C0=781/25000=0.03124`, `lambda=6/5`. On

\[
 L=[11/50,6/25]\times[1/2,531/1000],\quad
 H=[11/50,6/25]\times[5/8,127/200],
\]

we prove the strict **global affine separation**

\[
 \boxed{c(x,y)+\lambda b(x,y)>C_0+\lambda Q
   =\frac{2359}{62500}=0.037744.}\tag{2}
\]

Hence **inside either strip**, `b<=Q` forces `c>C0`. The previously used Stage346-B low-y implication was specific to its smaller `Q`, and has not been recycled unchanged here.

All source-tag signs on each strip are fixed, and all sixteen word comparisons are retained. For `x in [11/50,6/25]`, the tag signs against `1/4,3/4` are `-+++` and `--++`. On the low y strip the two y signs are `++--` and `--++`; on the high y strip they are `++--` and `---+` (the third word switches at the algebraic cusp). Thus exact cubic expressions are

\[
 c=K_j+p_x(x)+p_{y,j}(y),\quad
 p_x(x)=\frac{-189x+186x^2-61x^3}{256},
\]

\[
 \begin{array}{lll}
 j=L:&K_L=2673/16384,&p_{y,L}(y)=(3y^2-2y^3)/128,\\
 j=H:&K_H=621/4096,&p_{y,H}(y)=(27y^2-25y^3)/256.
 \end{array}
\]

The key stronger method is to combine `c` and `lambda*b` **before** bounding. For each of the 16 masks `S` we have

\[
 c+\lambda b\ge
  K_j-\frac{\lambda M_S}{512}
  +\underbrace{\left[p_x(x)+\frac\lambda4 F_S(x)\right]}_{G_{S,j}(x)}
  +\underbrace{\left[p_{y,j}(y)+\frac\lambda{16}F_S(y)\right]}_{H_{S,j}(y)}. \tag{3}
\]

Take the exact cubic Bernstein minimum for each bracket on a rectangle, add constants, and maximize the resulting 16 valid lower bounds. This **fused** enclosure avoids the excessive pessimism of separately bounding `b` and `c`. `CERTIFICATE_STAGE347B_LOW_STRIP.csv` provides 55 strict (3) leaves, depth≤6, exact area `31/50000`; `CERTIFICATE_STAGE347B_HIGH_STRIP.csv` needs only a single strict (3) root leaf, exact area `1/5000`. Every row is exact rational; the checker rebuilds and separately validates quadtree coverage and the stated inequalities. This establishes (2) for every real point in each strip, including edges.

## III. Exact old/new endpoint comparisons

Use the inherited Stage346-B strict double-zero isolators

\[
 2310839408/10^{10}<x_*<2310839409/10^{10},\qquad
 555508855/10^9<y_*<555508860/10^9.
\]

Since `B2` is increasing in both relevant coordinates, evaluating `15r2/16` at these four rational endpoints bounds `beta_*` strictly. The exact checker prints the rational lower/upper values and checks `beta_*+1/625<Q`.

For the **old** `E_0=7/5000` candidate, at `x0=235341/10^6`, `y0=568564/10^6`, exact signs give

\[
 r_1(x_0,y_0)<0,\qquad \frac{15}{16}r_2(x_0,y_0)<\beta_L+7/5000.
\]

`r1` decreases strictly with y above 1/3; therefore `Y1(x0)<y0`. As `b` increases along the right r1-zero arc, `x_{E0}>x0`, `y_{E0}<y0`. The signed derivative formulas `c_x<0,c_y>0` (below the cusp) yield

\[
 c(q_{E0})<c(x_0,y_0)
 =\frac{7997158980991873343}{256000000000000000000}<C_0.\tag{4}
\]

For `E_1=1/625`, the checker uses exact signs of `r1` and `r2` at `xL=2359/10000, xU=59/250, yL=5703/10000, yU=571/1000`. They establish

\[
 0.2359<x_{E1}<0.236,\quad y_{E1}<0.571,
\]

and `c(q_E1)<c(0.2359,0.571)<C0`. Because `s -> c(q_s)` strictly decreases, (4) proves `c(q_s)<C0` for **all** `E0<=s<=E1`. Combining this with (2), no low-y (`y<=0.531`) or high-y (`y>=0.625`) point can minimize `c` under `b<=beta_*+s` in the newly added budget range.

## IV. Middle-y residual chambers and zero curves

It remains to analyze `R_mid = R intersect {531/1000<=y<=5/8}`, with `r2>0` throughout. The previously established author results Stage336-B/Stage342-B strictly dominate each point with `r3=0` or `r3>0` in this region; their exact reference domain `[0.21,0.24]×[0.5,2/3]` contains `R_mid`. Thus consider `r3<0`.

Conservation gives

\[
 b=\frac5{16}\left[-r_3+(-r_0)_+ +3(-r_1)_+\right].\tag{5}
\]

The 16 tagged comparisons yield `c_x=-p(x)<-43/100`, `c_y=q(y)>0`, where

\[
 p(x)=\frac{(1-x)(189-183x)}{256},\quad
 q(y)=\begin{cases}3y(1-y)/64,&y<y_\dagger,\\3y(18-25y)/256,&y>y_\dagger,\end{cases}
 \quad y_\dagger=(1+\sqrt{13})/8.
\]

Both one-sided derivative formulas are used at the cusp. The signs `(r0,r1)=(+,+),(+,-)` admit increasing x that strictly lowers `b,c`; `(-,-)` admits decreasing y. For `(-,+)`, moving on a **constant-b curve** with

\[
 dx>0,\qquad dy/dx=4(1-2x)/(2y-1)>0
\]

strictly lowers c: for `y<=y_dagger` use `q<=3/256`, `y>=531/1000`, `x>=11/50`, which gives `q*dy/dx<43/100<p(x)`; above the cusp, `y_dagger>23/40` and `q<=1/40`, giving the same strict conclusion. These are exact rational endpoint comparisons in the verifier, including the cusp's one-sided signs.

On `r0=0` write `y=Y0(x)` with `Y0'<0`. Along its part left of `q_*`, `r1<0`; the derivative of `r2` has sign `f(x)-f(y)`, where `f(z)=z(2-3z)/(1-z)^2`. For `y<=3/5`, `f(y)>=f(3/5)>f(x_*)>=f(x)`; for `3/5<=y<=5/8`, exact `r0(228/1000,3/5)<0` implies `x<228/1000`, and `f(y)>=f(5/8)>f(228/1000)>=f(x)`. Hence increasing x along `r0=0` strictly lowers both b and c. Right of `q_*`, `r1>0`; the constant-b descent immediately enters the `r0<0` chamber and lowers c.

On `r1=0` the implicit derivative

\[
 Y1'=\frac{4(1-x)(1-3x)}{(1-y)(3y-1)}\in(0,5)
\]

throughout R, so `dc/dx=-p+qY1'<-0.43+5/40<0`. Left of `q_*`, public b also decreases when x increases (`r3<0`); right of `q_*`, b increases, and this is the **sole surviving frontier**. There are no relevant artificial R-edge minimizers: all feasible `b<=beta_*+s<Q` points are interior to R, and both y-strip interfaces are eliminated by strict (2).

Compactness and these local exclusion directions therefore establish the **new single-source inequality**

\[
 b(q)\le\beta_*+s \implies c(q)\ge c(q_s),\qquad
 c(q)=c(q_s)\iff q=q_s,
 \quad E_0\le s\le E_1. \tag{6}
\]

For smaller s the exact same statement is inherited from Stage346-B's author theorem (not silently strengthened), so (6) holds at the author-proof level for `0<=s<=1/625`.

## V. New strict curvature box; complete two-source allocation

The right frontier from `q_*` to `q_E1` lies in

\[
 C=[231/1000,59/250]\times[555/1000,571/1000],
\]

strictly below `y_dagger`. Write `Y=Y1(x)`, `g(Y)=(1-Y)(3Y-1)`. Differentiating `r1=0` twice gives

\[
 Y'=4(1-x)(1-3x)/g(Y),\quad
 Y''=\frac{4(6x-4)+(6Y-4)(Y')^2}{g(Y)}.
\]

Exact interval endpoints prove `29/10<Y'<33/10`, `Y''<-48`. Combining these with the exact derivatives

\[
 b'=(3/16)[4x(2-3x)+Y(2-3Y)Y'],
\]

\[
 b''=(3/16)[4(2-6x)+(2-6Y)(Y')^2+Y(2-3Y)Y''],
\]

\[
 c'=-p(x)+3Y(1-Y)Y'/64,
\quad c''=(372-366x)/256+[3(1-2Y)/64](Y')^2+[3Y(1-Y)/64]Y'',
\]

establishes **uniform rational strict bounds** throughout C:

\[
 0<b'<2/5,\quad b''<-3,\quad c'<-39/100,\quad c''<9/8.
\]

Therefore

\[
 \boxed{c''b'-c'b''<-18/25<0.}\tag{7}
\]

For `phi(s)=c(q_s)` with `s=b(q_s)-beta_*`, `phi'<0` and `phi''=(c''b'-c'b'')/(b')^3<0` for all `0<=s<=1/625`, with one-sided endpoint interpretation. The sourcewise budget penalties `s_i=b(q_i)-beta_*` are nonnegative by the inherited unique global `b`-minimum. Apply (6) to each, exhaust total budget because phi decreases, and minimize strictly concave `phi(s1)+phi(E-s1)` on `[0,E]`: the only minimizers are its endpoints `s1=0,E` and `s1=E,0`. Equality in (6) gives exactly the two configurations in the theorem.

## Reproduction and pending review

Run `python REPRO_STAGE347B.py`. It uses only Python standard-library `Fraction`, exact polynomial Bernstein controls, CSV parsing and `hashlib`. It deterministically generates/validates the **193 + 55 + 1** leaf certificates and checks all fixed-strip tag signs, cubic tag polynomials, endpoint isolators, the enlarged symbolic curvature inequalities and residual-chamber constant-b comparisons. All strict comparisons use integer/rational arithmetic. `REPRO_STAGE347B_EXECUTED_STDOUT.txt` records two matching actual runs; the output and each CSV SHA256 are printed. These machine checks discharge the specified rational finite verification obligations; the analytic Bernstein convex-hull lemma, real-valued compactness, implicit-function reasoning, and chamber completeness remain the accompanying mathematical proof obligations articulated above.

The proof imports earlier **author** conclusions (uniqueness at q_*, Stage336/342 nonnegative r3 domination, Stage346 base interval); the new extended bound is an author-level result until independent review. No native service CLAIM, Source Result, independent review, current Owner transfer, P000 physics inference, or foundation promotion follows from file publication.

**Next Stage348-B:** increase budget toward `E=9/5000` and the proposed algebraic cusp `E≈0.0021814`; test whether a new low-y source-tag boundary can beat the right r1 arc, with a rational competitor or a new all-real enclosure. Independently reproduce the Stage336/342 domination and full Stage347 chamber semantics before canonical admission, and separately develop P000 X6-to-auxiliary observer-fidelity bridge.
