# Stage343-B — exact full-domain extension to E ≤ 1/1250 in the source-tagged Bernoulli/BRC observer

**Date:** 2026-11-01. **Author status:** PORTABLE_AUTHOR_THEOREM / EXACT_FRACTION_BERNSTEIN_EXECUTED / UNREVIEWED / NOT_ADMITTED. No native CLAIM, formal Source Result, independent Driver review, or P000-native transfer is asserted.

## Immutable provenance and scientific object

Frozen account knowledge `awdawmip/chatgpt-global-knowledge main@1d54eb70828d47f48a39f8fe43a011ed18608c96` (both normative entry files, project/TASK_RESEARCH router, ACTIVE worldview, P000 startup projection, BRC/math/code policies). Frozen Enterprise Math canonical `main@ac48238d40c28c9ad139faa5b0e11cb7defdd8f9` (AGENTS, native P000 V5 Git blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`, joint observer preservation, portable/autonomous research protocols). Latest carried portable research frontier Stage342-B: immutable `50db2cf79e5baf1795ce318753b8f796550fa282`, **not a reviewed theorem or native Source Result**. The current main branches contain other project research not used as proof premises here.

All mathematics in this file is for the **auxiliary** two-source, three-visit Bernoulli/BRC observer, with two rate parameters `(x,y)` per source and four rates in total. It is not a reduction of the native X6 six-space-plus-time world, a two-dimensional native slice, a claim about the P000 third slice coordinate, triadic closure, or final Cell addresses. We retain four word classes, weights/multiplicities, sixteen *individually source-tagged* comparisons and separate public/audit observers; we never infer cancellation of positive mass from signed scalar residuals.

For `k=0,1,2,3`, write

\[
B_k(z)=z^k(1-z)^{3-k},\quad w=(1,3,3,1),\quad m=(61,21,9,9),
\]
\[
r_k(x,y)=\frac{4B_k(x)+B_k(y)}5-\frac{m_k}{160},\qquad
b(x,y)=\frac5{32}\sum_{k=0}^3w_k|r_k(x,y)|,
\]
\[
D_3(a,z)=\frac12\sum_{k=0}^3w_k|B_k(a)-B_k(z)|,\quad
c(x,y)=\frac{63D_3(1/4,x)+D_3(3/4,x)+9D_3(1/4,y)+7D_3(3/4,y)}{256}.
\]

For distinct source groups `q1,q2∈[0,1]^2`, use `P=b(q1)+b(q2)` and `T=33/1024+c(q1)+c(q2)`. The exact mass identity is `r0+3r1+3r2+r3=0`.

## Main theorem (new global initial allocation interval)

Let `q*=(x*,y*)` be the **unique global minimizer of `b`**; equivalently the unique point with `r0=r1=0` in the relevant low-error domain. Write `β*=b(q*)`. Along the right arc `r1=0, x≥x*`, let `q_s` be the unique point with `b(q_s)=β*+s` for `0≤s≤1/1250` (with `q_0=q*`). Then, **for every real budget**

\[
\boxed{0\le E\le\frac1{1250}=0.0008,\qquad
\min_{q_1,q_2\in[0,1]^2\atop b(q_1)+b(q_2)\le2\beta_*+E}T
=\frac{33}{1024}+c(q_*)+c(q_E).}
\]

At `E=0`, the unique optimizer is `(q*,q*)`; at `E>0`, the **only** optimizers are `(q*,q_E)` and its source-order swap. This extends the previously author-proved Stage341-B `E≤29/50000=0.00058` to `E≤1/1250=0.0008`, an increase of `11/50000=0.00022` (~37.93%). The proof below gives a **new 304-leaf full-square Bernstein enclosure and an independent exact strict-concavity inequality**, rather than enlarging the inherited Stage329 curvature assumption. These are author computations and analytic arguments, not independent mathematical review.

### Lemma A — global continuum enclosure at `Q=23/5000`

Define the exact rational rectangle

\[
Q=\frac{23}{5000}=0.0046,\qquad R=\left[\frac9{40},\frac{117}{500}\right]\times\left[\frac{539}{1000},\frac{621}{1000}\right].
\]

**For every real `(x,y)∈[0,1]^2`,**

\[
\boxed{b(x,y)\le Q\Longrightarrow (x,y)\in R.}\tag{A}
\]

Proof: for any nonempty mask `S⊆{0,1,2,3}`, let `F_S(z)=∑_{k∈S}w_kB_k(z)` and `M_S=∑_{k∈S}w_km_k`. On `[u,v]`, the cubic's four **exact** Bernstein coefficients are

\[
F_S(u),\quad F_S(u)+(v-u)F'_S(u)/3,\quad F_S(v)-(v-u)F'_S(v)/3,\quad F_S(v).
\]

Their minimum `L_S[u,v]` is a valid lower bound for *all real* `z∈[u,v]`. Since `∑w_kr_k=0`, the public error is `b=(5/16)∑w_k(r_k)_+`. Therefore, on every rectangle `[a,b_]×[c_,d]` and for every mask `S`,

\[
b(x,y)\ge\frac5{16}\left[\frac{4L_S[a,b_]+L_S[c_,d]}5-\frac{M_S}{160}\right].\tag{A1}
\]

`CERTIFICATE_STAGE343B.csv` records a complete **304-leaf** exact dyadic quadtree covering the full unit square: **185 HIGH** leaves have a specific mask `S` and rational (A1) bound strictly `>Q`; **119 INNER** leaves lie wholly in `R`. Maximum depth 11; exact leaf-area sum 1, every quadtree sibling recursively present. No finite sampling or floating-point rounding is used. The accompanying checker **regenerates the entire tree, verifies the CSV row-for-row, every HIGH inequality, INNER inclusion, prefix-free full coverage, and exact area**. Continuity implies each feasible point with `b<Q` actually lies in the *interior* of `R` (it cannot lie on the boundary since then a neighborhood outside `R` would also have `b<Q`).

On `R`, the exact derivatives of `r2` in both variables are positive and

\[
 r_2\ge r_2(9/40,539/1000)=\frac{9617681}{5000000000}>0.\tag{A2}
\]

The public residual `r3` **does** change sign in `R`; the argument does not conceal that zero boundary.

### Lemma B — all 16 source-tagged signs and strict cost directions

Across `R`, the signed comparisons `B_k(a)-B_k(z)` in order `k=0,1,2,3` are

| comparison | signs |
| --- | --- |
| `(x,1/4)` | `-+++` |
| `(x,3/4)` | `--++` |
| `(y,1/4)` | `++--` |
| `(y,3/4)` | `--σ+` |

The only varying sign is `σ` at `k=2`, which changes exactly at `y†=(1+sqrt(13))/8` because

\[
B_2(3/4)-B_2(y)=\frac{(4y-3)(16y^2-4y-3)}{64}.
\]

Every other comparison has strictly same-sign rational Bernstein coefficients over its *entire* input interval, checked symbolically. Differentiating **all 16 retained signed summands** produces

\[
c_x=-p(x)=-\frac{(1-x)(189-183x)}{256}< -\frac25,
\]
\[
c_y=q(y)=\begin{cases}3y(1-y)/64,&y<y†,\\3y(18-25y)/256,&y>y†,\end{cases}
\qquad 0<q(y)<\frac1{40}.\tag{B}
\]

At `y=y†`, both one-sided positive derivatives obey the stated bounds. The exact rational inequality `y†>23/40` follows from `13>(18/5)^2`.

In the `r3<0` region (and throughout `R`, `r2>0`), conservation gives

\[
 b=\frac5{16}\left[-r_3+(-r_0)_++3(-r_1)_+\right].\tag{B1}
\]

All four *strict* `(sign r0,sign r1)` chambers then have the following controlled directions:

* `(+,+)`: increase `x`; `b_x=-3x²/4<0` and `c_x<0`.
* `(+,-)`: increase `x`; `b_x=-3(1-2x)²/4<0` and `c_x<0`.
* `(-,-)`: decrease `y`; `b_y=3y(2-3y)/16>0` and `c_y>0`.
* `(-,+)`: increase `x` and `y` along the smooth `b=constant` arc (`b_x=3(1-2x)/4>0`, `b_y=-3(2y-1)/16<0`). The exact slope is `dy/dx=4(1-2x)/(2y-1)`, and the audit derivative is `-p(x)+q(y)dy/dx<0` because, below the tagged cusp,
  \[
  q\frac{4(1-2x)}{2y-1}\le \frac3{256}\frac{4(1-2\cdot9/40)}{2\cdot539/1000-1}<\frac25,
  \]
  while above it `q<1/40`, `2y-1>3/20` imply the sharper easy bound `q dy/dx<11/30<2/5`. Continuity and one-sided integration cover `y=y†` without pretending differentiability there.

The last chamber is crucial: a same-public-budget competitor **strictly reduces the tagged audit cost** even though it need not reduce public error. All motions are local and stay in the original real parameter square; the strict `b<Q` sublevel cannot exit `R`.

### Lemma C — independently handle the entire `r3≥0` stratum, including its double zero

Because `r3` increases in `x,y`, the exact inequalities `r3(117/500,153/250)<0`, `r3(9/40,309/500)>0` imply `r3=0` in `R` forces `0.612<y<0.618`. Similarly `r3>0` forces `y>0.612` and hence `r1≤r1(117/500,153/250)<0`. Everywhere `r2>0`, and the full tagged sign formulas of Lemma B apply.

When `r3>0`: for `r0>0` increase `x` (only `r1` negative, so `b=-15r1/16` and `b_x<0`); for `r0<0` decrease `y` (negative `r0,r1` give `b_y=3y(1-y)/8>0`); for `r0=0` decrease `y` into `r0>0`, where the one-sided public derivative is `b_y=3(1-y)(3y-1)/16>0`. Each step also strictly lowers `c` by (B).

When `r3=0, r0>0`, increase `x` into the `r3>0, r0>0` chamber; when `r3=0, r0<0`, decrease `y` into the `r3<0,r0<0,r1<0` chamber, with `b=15r2/16` and `b_y>0`. These also lower both objectives. At the remaining **double zero `r0=r3=0`**, parameterize `r3=0` by `4x³+y³=9/32`, whose derivative is `dy/dx=-4x²/y²`. The function `r0` is strictly decreasing along this curve for `x<y`, so there is only one double zero in `R`. Exact rational endpoint signs isolate it in

\[
\frac{1133}{5000}<x<\frac{567}{2500},\qquad\frac{616}{1000}<y<\frac{618}{1000}.\tag{C}
\]

For **every** point of that box satisfying `r0=r3=0`, the direction `d=(1,-14)` has

\[
D_dr_0<0,\quad D_dr_3<0,\quad D_dr_2<0,
\]

as follows exactly from `2(1-x)^2>7(1-y)^2`, `2x²<7y²`, and `4x(2-3x)<14y(2-3y)`, respectively. Small positive steps enter the `r3<0,r0<0,r1<0,r2>0` chamber, where `b=15r2/16`, so **both** `b` and `c` strictly decrease (`D_dc=-p-14q<0`). Therefore **all `r3≥0` points are strictly Pareto dominated**, including the intersection. This is a fresh direct argument in the new rectangle; its conceptual ancestor is Stage336/342, not a claim of independent review.

### Lemma D — exact zero-curve classification and unique public minimum

The zero curve `r0=0` is a graph `y=Y0(x)` with `Y0'=-4(1-x)^2/(1-y)^2<0`. Along it `r1` increases strictly, since `r1_x>0,r1_y<0`. At `x_L=231083/10^6`, rational tests trap `Y0(x_L)∈(555520/10^6,555521/10^6)` and give `r1(x_L,Y0(x_L))<0`; at `x_H=231085/10^6`, tests trap `Y0(x_H)∈(555496/10^6,555497/10^6)` and give `r1(x_H,Y0(x_H))>0`. Hence there is exactly one double zero

\[
q_*=(x_*,y_*),\qquad\frac{231083}{10^6}<x_*<\frac{231085}{10^6},\quad
\frac{555496}{10^6}<y_*<\frac{555521}{10^6}.\tag{D1}
\]

At `r0=0` to the **left** of `q*`, `r1<0`, `b=15r2/16`. Using `f(z)=z(2-3z)/(1-z)^2` and the exact bound

\[
f(x)\le f(117/500)=\frac{75933}{146689}<\frac{85077}{143641}=f(621/1000)\le f(y),
\]

one gets `d r2(x,Y0(x))/dx=(4/5)(1-x)^2(f(x)-f(y))<0`. Also `d c(x,Y0(x))/dx=-p+qY0'<0`. Thus moving right toward `q*` lowers both costs. To the **right** of `q*`, `r1>0`, and `b=-5r3/16` *increases* along the zero curve because

\[
\frac{d r_3(x,Y_0(x))}{dx}
=\frac{12}{5}\frac{(x-y)(x+y-2xy)}{(1-y)^2}<0.
\]

Every such point is nevertheless audit-dominated at unchanged public error by entering the adjacent `(-,+)` chamber along its constant-`b` curve (Lemma B).

The zero curve `r1=0` is `y=Y1(x)`, with

\[
Y_1' = \frac{4(1-x)(1-3x)}{(1-y)(3y-1)} \in(0,5)
\]

on `R`. Hence `d c(x,Y1(x))/dx=-p+qY1'<-2/5+(1/40)5<0`. Its **left** arm has `r0>0`, `b=-5r3/16`, strictly decreasing toward `q*`; it is strictly dominated. Its **right** arm has `r0<0`, `b=15r2/16`, strictly *increasing* with `x` while `c` decreases. This is the only surviving family of constrained audit minimizers, together with `q*` at the minimal budget.

The exact rational checks at `x=117/500` yield

\[
 r_1(117/500,564/1000)>0>r_1(117/500,565/1000),
\]
\[
 b(117/500,Y_1(117/500))>\frac{15}{16}r_2(117/500,564/1000)
 =\frac{945459}{200000000}>Q.
\]

At `q*`, `r2>0,r3<0`, thus `β*=15r2(q*)/16`. Monotonicity of `r2` and (D1) give an *independently checked*, simple rational upper bound

\[
\beta_*<\frac{15}{16}r_2(231085/10^6,555521/10^6)
=\frac{60476723775473217}{16000000000000000000},\qquad
\beta_*+\frac1{1250}<Q.\tag{D2}
\]

The enclosure (A), Lemmas B–C, and the complete one-sided zero-curve arguments exclude every other point as a minimizer of `c` under `b≤B` for any `β*≤B≤β*+1/1250`. To show `q*` is indeed the **unique global `b` minimizer**, apply (A) to a global minimizer (since `b(q*)<Q`), then note that every point other than `q*` in `R` admits a strict `b` descent: all smooth chambers have one (`(-,+)` uses increasing `y`, not the constant-`b` audit path); every zero curve has a direction toward smaller `b`; and `r3≥0` was handled in Lemma C. Finally, along the right `r1=0` arm, `b` is strictly increasing and `c` strictly decreasing. The root `q_s` exists uniquely for every `0≤s≤1/1250`, and

\[
\boxed{\forall q:\ b(q)\le\beta_*+s\quad\Rightarrow\quad c(q)\ge c(q_s),
\text{ equality iff }q=q_s.}\tag{D3}
\]

No use is made of untagged source-collapse or a fictitious differentiable gradient at any zero boundary.

### Lemma E — *new*, independent exact strict concavity of the surviving frontier

For all `0≤s≤1/1250`, the right `r1=0` segment lies within

\[
\frac{231}{1000}\le x\le\frac{234}{1000},\qquad
\frac{555}{1000}\le y\le\frac{566}{1000}<y_\dagger.
\]

Here `Y1` is smooth and `c_y=q=3y(1-y)/64`. Put `g(y)=(1-y)(3y-1)>0`, `Y=Y1(x)`, and primes for derivatives with respect to `x`. Exact implicit differentiation yields

\[
Y'=\frac{4(1-x)(1-3x)}{g(y)},\qquad
Y''=\frac{4(6x-4)+(6y-4)(Y')^2}{g(y)}.
\]

Along the candidate curve,

\[
b' =\frac3{16}\left[4x(2-3x)+y(2-3y)Y'\right],
\]
\[
b''=\frac3{16}\left[4(2-6x)+(2-6y)(Y')^2+y(2-3y)Y''\right],
\]
\[
c'=-p(x)+q(y)Y',\quad
c''=\frac{372-366x}{256}+\frac{3(1-2y)}{64}(Y')^2+q(y)Y''.
\]

Simple *exact rational interval inequalities* valid for **every real point of that full rectangle** give

\[
3<Y'<16/5,\qquad -59<Y''<-52,
\]
\[
0<b'<7/20,\qquad b''<-3,\qquad c'<-39/100,\qquad c''<9/8.
\]

Every bound is independently checked in `REPRO_STAGE343B.py` using Fraction endpoint algebra and monotonicity on the stated interval. For `φ(s)=c(q_s)` and `s=b(q_s)-β*`, the chain rule gives

\[
\phi''(s)=\frac{c''b'-c'b''}{(b')^3},\qquad
c''b'-c'b''<\frac98\cdot\frac7{20}-\frac{39}{100}\cdot3
=\boxed{-\frac{621}{800}<0}.\tag{E}
\]

Thus **strict concavity is proven here directly in a strictly specified new rational box** and does not depend on extrapolating an inherited Stage329 bound. Also `φ'<0` because `c'<0,b'>0`.

### Conclusion — two-source allocation and exact equality

For every feasible pair put `s_i=b(q_i)-β*≥0`. Lemma D gives `s1+s2≤E` and `c(q_i)≥φ(s_i)`, with equality only on the unique right zero curve. Because `φ` is strictly decreasing, an optimum spends all available public-error budget, `s1+s2=E`. By Lemma E, `φ(t)+φ(E-t)` is strictly concave in `t∈[0,E]`, and therefore has precisely the two endpoint minima `t=0,E` (one at `E=0`). Strict equality in (D3) identifies the ordered source assignments. This proves the theorem over the **entire four-real-rate parameter domain** of the declared auxiliary model.

## Evidence, authority, limitations and next research unit

`REPRO_STAGE343B.py` generates the exact 304-leaf certificate, reads and checks the committed CSV row-for-row, validates the full dyadic coverage/areas, all 16 source-tagged comparisons and their piecewise gradient identities using SymPy, exact root bracketing, zero-curve and positive-side inequalities, plus the independent rational second-derivative margins. `REPRO_STAGE343B_EXECUTED_STDOUT.txt` is the **actual executed output**, with exact terminal `STAGE343B_GLOBAL_E_0p0008_EXACT_BERNSTEIN_AND_CURVATURE_PASS`; the execution was repeated and bytes compared. The proof of continuous-real quantifiers consists of the displayed analytic inequalities and full-cover certificate, **not** finite samples. This remains unreviewed author mathematics; no Lean/formal checker admission is asserted.

Native service v0.6.11 was read this round and explicitly reported `research_authority_granted=false`, `executor_binding_configured=false`; owner-list request returned `CONTROL_QUOTA`. No live owner/CLAIM/session/Driver authority is presumed. GitHub artifact storage and optional global journal are not canonical native Source Result/admission or scientific peer review.

**Smallest next question, Stage344-B:** extend the exact full-domain Pareto interval toward `E=0.0010` by constructing a new global Bernstein sublevel enclosure at `Q≈0.00481`, retaining the `r3≥0` exclusion and the *unchanged* four-rate/source-tag model; or produce a rigorous exact two-source counterexample to current one-group-active structure. The right `r1=0` arc remains below `y†` at `E≈0.0010`, but candidate branches and all boundary strata must be verified anew. A separate independent formal/mathematical audit should first check the 304-leaf certificate, root/curvature inequalities and full-domain chamber reduction. Native P000 X6, three-dimensional slice third component, triadic closure, independent time and six-field Cell address remain explicitly **unproved interface/observer-preservation obligations**.
