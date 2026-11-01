# Stage366-B — an exact, four-parameter sharp local optimum at the first audit cusp

Date: **2026-11-02** (Asia/Shanghai). Role: Research2 portable mathematical author (GitHub account `awdawmip`); **not** a formal native CLAIM, Result or independent Driver review. Scientific inputs remain frozen at GLOBAL_KNOWLEDGE_V1 `bf84bd7c61a2444b59b1da96be57df0e9ae47e53` and Enterprise Math `2af3fc484eb11060b69e0afc1b562bcaf5ad1419`; project P000 V5 remains `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`. Current normative reads: global canonical `main@1ea86263e66f7d98af6151da4bcdfd2bbbd15e50` and EM `main@ff2cb418398f05b1b4a865febda17c0fc2aa52d1`. P000 and ACTIVE residual-preserving X6/three-dimensional-slice world assumptions are unchanged. This is an **external auxiliary Bernoulli/BRC observer theorem**.

## Exact question and input

Previous Stage353-B proved that the first audit-cusp pair is the optimal split **restricted** to the right `r1=0` arc for the cusp budget; Stage365-B proved an equal-error projection for off-arc points near the cusp. Neither alone establishes unrestricted four-parameter local optimality, particularly around the other source's simultaneous `r0=r1=0` junction. This stage answers that remaining local question **at the exact cusp budget**.

Keep the **original sixteen separately provenance-labelled comparisons** of four word probabilities at four source/anchor ports. For `k=0,1,2,3`, set

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

Let `q*=(x*,y*)` be the unique central simultaneous root `r0=r1=0`. Let `alpha=(1+sqrt(13))/8` (the first root of `B2(alpha)=9/64` encountered along the increasing right arc) and `qa=(xa,alpha)` the unique nearby `r1=0` point. Put `beta*=b(q*)`, `E_c=b(qa)-beta*`. The full unrestricted two-source objective is `T(p,q)=33/1024+c(p)+c(q)` subject to `b(p)+b(q)<=2 beta*+E_c`. Here `p,q` range over the full ambient `[0,1]^2` **independently**, so this is a four-real-parameter optimization problem.

## Theorem — explicit-radius strict local optimality in the full four-parameter model

Set `rho=1/40000`, `lambda=49/40`, and `||.||inf` for the maximum-coordinate norm. For **all real** `p,q in [0,1]^2` with

\[
\|p-q_*\|_\infty\le\rho,\quad
\|q-q_\alpha\|_\infty\le\rho,\quad
b(p)+b(q)\le b(q_*)+b(q_\alpha),
\]

one has

\[
\boxed{\begin{aligned}
&T(p,q)-T(q_*,q_\alpha)\\
&\quad\ge \frac{\|p-q_*\|_\infty+\|q-q_\alpha\|_\infty}{4000}
+\frac{49}{40}\bigl(b(q_*)+b(q_\alpha)-b(p)-b(q)\bigr).
\end{aligned}}
\]

The inequality is **strict** whenever at least one source differs from the stated candidate (because the local lower estimates are strict). Consequently `(q*,qa)` and its source-swapped counterpart are isolated strict local constrained minima of the **unrestricted** model at this particular budget. The associated cusp budget is algebraic and satisfies the certified coarse bracket `0.002181<E_c<0.002182`; the sharper Stage351 source interval `0.0021814072266<E_c<0.0021814072275` is a previously established independent numerical isolator, not required here.

**Scope:** This establishes a sharp local optimality neighborhood at `E=E_c`; the global unrestricted minimum for any budget, and the unrestricted optimum when `E>E_c`, are still open. Source/word labels, `r0` and `r1` remain independent; no quotient of these observers is asserted.

## Proof 1 — exact algebraic point isolation and sign charts

The standalone checker uses rational brackets

\[
\begin{array}{rcl}
x_*&\in&(2310839,2310840)/10^7,\\
y_*&\in&(5555086,5555091)/10^7,\\
x_\alpha&\in&(2378068,2378070)/10^7,\\
\alpha&\in&(5756939,5756940)/10^7.
\end{array}
\]

On both boxes, `r1` is strictly increasing in `x` and decreasing in `y`. At the star box the checker establishes `r1(xL,yL)>0>r1(xU,yU)`; there is a unique increasing `r1=0` graph `y=Y(x)`. The inequalities `r0(xL,yU)>0>r0(xU,yL)` and strict decrease of `r0(x,Y(x))` give exactly one simultaneous root. At the cusp, `B2(yL)<9/64<B2(yU)` and `B2'>0`, while `r1(xL,yL)<0<r1(xU,yU)`; hence the unique algebraic cusp intersection falls in its box. At the star and cusp neighborhoods expanded by `rho`, the checker establishes `r2>0`, `r3<0`, and additionally `r0<0` at the cusp. It checks all fifteen unchanging labelled port comparisons in the cusp box and all sixteen in the star box (with the one remaining cusp tag treated explicitly as a positive part). On the `r0=r1=0` and cusp boxes, `b=(15/16)r2` exactly. Since `r2` increases in both coordinates, its bracket values yield the announced `E_c` interval.

For any point in either radius-`rho` box, the identity `sum_k w_k r_k=0` and the proved `r2>0>r3` give the **exact** positive-part representation

\[
b=\frac{15}{16}r_2+\frac5{16}(r_0)_++\frac{15}{16}(r_1)_+.
\]

At the cusp `r0<0`, so its `(r0)_+` term vanishes. Explicit expansion of all four labelled audit ports (each retaining its four word comparisons) gives a common smooth cost polynomial `C_lo` with

\[
\nabla C_{\rm lo}=
\left(-\frac{3(1-x)(63-61x)}{256},\ \frac{3y(1-y)}{64}\right).
\]

At the cusp the **entire** extra nonsmooth audit contribution equals

\[
C_{\rm hi}-C_{\rm lo}=\frac{21}{256}\left(B_2(y)-\frac9{64}\right);
\quad
c=C_{\rm lo}+\frac{21}{256}\left(B_2(y)-\frac9{64}\right)_+.
\]

This is an exact source-labelled identity in these sign neighborhoods, not an erasure of the labels.

## Proof 2 — strict first-order support at both distinct nonsmooth points

Set `L=c+lambda*b` with `lambda=49/40`. At either candidate `z`, write `v` for a perturbation. There are exactly two independent positive-part normals; their coefficients are listed below. In the star case, put

\[
U_*=\lambda\frac5{16}\nabla r_0(q_*),\quad
V_*=\lambda\frac{15}{16}\nabla r_1(q_*),\quad
W_*=\nabla C_{\rm lo}(q_*)+\lambda\frac{15}{16}\nabla r_2(q_*).
\]

At the cusp case put

\[
U_\alpha=\left(0,\frac{21}{256}B_2'(\alpha)\right),\quad
V_\alpha=\lambda\frac{15}{16}\nabla r_1(q_\alpha),\quad
W_\alpha=\nabla C_{\rm lo}(q_\alpha)+\lambda\frac{15}{16}\nabla r_2(q_\alpha).
\]

The exact rational interval checker isolates the unique coefficients `theta_U,theta_V` solving `W+theta_U U+theta_V V=0`:

| Point | `theta_U` certified | `theta_V` certified | determinant and max-entry certificate |
|---|---|---|---|
| star | `1/100 < theta_U < 1/50` | `3/4 < theta_V < 4/5` | `det(U,V)>1/22`, `max |U_i|,|V_i|<4/5` |
| cusp | `2/5 < theta_U < 3/5` | `3/4 < theta_V < 4/5` | `det(U,V)<-1/400`, `max |U_i|,|V_i|<1/4` |

Every enclosure is obtained by outward rational interval operations on the **whole root boxes**, using Cramer's rule, not by evaluating a decimal approximation of the algebraic roots. Crucially all coefficients are strictly between 0 and 1 and the two normals are independent. Because the actual local nonsmooth functions are **positive parts** (not arbitrary absolute-value sign flips), their one-sided directional derivative is

\[
L'(z;v)=(U\cdot v)_+-\theta_U U\cdot v
+(V\cdot v)_+-\theta_V V\cdot v.
\]

Each summand is at least `min(theta,1-theta)*|normal·v|`. By Cramer's inverse formula,

\[
|U\cdot v|+|V\cdot v|\ge\frac{|\det(U,V)|}{M}\|v\|_\infty,
\]

where `M` is any strict upper bound on the four absolute entries of `U,V`. The exact intervals therefore yield

\[
\boxed{L'(q_*;v)>\|v\|_\infty/2000,\quad
L'(q_\alpha;v)>\|v\|_\infty/500}\quad(v\ne0).
\]

This is a **positive sharpness** certificate in all two-dimensional directions, including those departing from `r1=0`, `r0=0` or the audit-cusp manifold. Its conclusion depends on the positive-part structure; merely containing zero in a general nonconvex Clarke subdifferential would not have sufficed.

## Proof 3 — finite radius and two-source composition

For each polynomial `B_k`, `|B_k''|<=6` on `[0,1]`; thus the Taylor remainder of `r_k` is bounded by `3||v||inf^2`. The positive-part map is 1-Lipschitz. On the same neighborhoods, `C_lo` has `|C_xx|<3/2`, `|C_yy|<1/20`; its Taylor remainder is `<||v||inf^2`. The audit-cusp positive-part remainder is `<||v||inf^2/4`. With the exact coefficients at `lambda=49/40`, the complete remainder of `L` after subtracting its directional derivative is **less than `10||v||inf^2`** at either center. The checker verifies the full radius-`rho` sign stability and each rational remainder bound.

Since `10 rho=1/4000`, the directional bounds imply for every nonzero perturbation with `||v||inf<=rho`

\[
L(q_*+v)-L(q_*)>\|v\|_\infty/4000,
\qquad
L(q_\alpha+v)-L(q_\alpha)>\|v\|_\infty/4000.
\]

For any feasible pair, expand `c(p)+c(q)=[L(p)+L(q)]-lambda[b(p)+b(q)]` and subtract the value at `(q*,qa)`. The budget condition makes the last correction nonnegative. This yields the theorem, its explicit error/cost margin and uniqueness within the two product neighborhoods. Exchanging the two sources gives the symmetric alternative.

## Actual reproducibility and next discrimination

`REPRO_STAGE366B.py` independently expands all sixteen signed port comparisons using SymPy, checks the original weighted-residual identity, roots, radii, signs, analytic gradients and positive-part coefficients using **exact Python Fraction interval arithmetic**, and verifies the uniform finite-radius remainder. It ran twice with byte-identical stdout saved in `REPRO_STAGE366B_EXECUTED_STDOUT.txt`, finishing `STAGE366B_UNRESTRICTED_FOUR_PARAMETER_CUSP_STRICT_LOCAL_OPTIMUM_EXACT_PASS`. The analytic bridge from interval certificates to all real points is supplied in Proofs 1–3; the checker is not an independent Driver or formal proof assistant.

**BRC**: `REUSE_EXECUTED` for the original sixteen provenance-labelled Bernoulli comparisons; `COMPOSE_APPLIED` for the two independent residual and audit-cusp positive-part normals, exact four-parameter local sharpness and budget composition. The source labels survive, and no native quotient, Cell-address or time-evolution claim is made.

**Next Stage367-B:** analyze `E_c<E<=11/5000` where the restricted optimum is `(q_{E-E_c},q_alpha)` rather than `(q*,q_alpha)`. Establish a budget-dependent strict unrestricted local theorem through a transversality/kink condition at the near-star source and the audit cusp, or construct an exact rational four-parameter competitor violating such a claim. This may require a two-source constrained second-order argument because the smooth right arc is strictly concave. Separately seek an exact global exclusion/counterexample certificate for remaining off-arc regions; no unrestricted **global** optimality follows from this local result. Native P000 X6/three-dimensional slice/triadic closure/independent time/six-field Cell bridge remain separately typed.