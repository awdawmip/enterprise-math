# Free Research — Pi-to-Prime Geometry Frontier V17

Status: `FREE_RESEARCH_CURRENT_FRONTIER / ODD_SIMPLEX_CONSTANT_ANCHOR_CLOSED / TERMINAL_READOUT_CLOSED / LOCAL_TWO_CHANNEL_MELLIN_CLOSED / IDEAL_ALTERNATING_GREEN_CLOSED / GLOBAL_ODD_SIMPLEX_RECURRENCE_OPEN / NOT_WORKING_TRUTH / NOT_FOUNDATION`
Date: `2026-09-04`
Project: `Enterprise Math / 进取数论`
Supersedes as current frontier: `FREE_RESEARCH_PI_PRIME_GEOMETRY_FRONTIER_V16_20260904.md`
Researcher-ID: `EM-FREE-PI-PRIME-20260904`
Research-Mode: `FREE_AXIOM_DISCOVERY`

## 1. Stable pi-to-prime geometry

The stable structural chain is

\[
\boxed{
\begin{aligned}
\tau^2
&=3!\lim_{M\to\infty}\det(I-B_M^{-2})^{-1},\\
\text{prime }p
&=\text{irreducible multiplicative birth direction},\\
p^a
&=\text{winding-layer birth},\\
\det\mathcal W_M
&=\operatorname{lcm}(1,\ldots,M),\\
\psi(M)&=\log\det\mathcal W_M.
\end{aligned}}
\]

For the normalized error

\[
r(N)=\psi(N)/N-1,
\]

parity twist converts signless prime-power transport into an ordinary gradient on the history carrier.

V16 showed:

- all nonconstant radial shell modes have a uniform gap;
- arithmetic history-depth distributions admit uniform Gamma/Wasserstein control;
- scalar recanonicalization destroys the standard-channel gain;
- the standard row channel itself propagates exactly.

V17 closes the formerly open constant-mode anchor and solves the local retained-channel Mellin matrix.

---

## 2. Constant mode is killed by the odd composite chord

For quotient maps

\[
q_a(n)=\lfloor n/a\rfloor
\]

and signless edges

\[
\delta_af(n)=f(n)+f(q_a(n)),
\]

quotient composition gives

\[
q_bq_a=q_{ab}.
\]

Therefore every ordered pair `(a,b)` forms the odd signed triangle

\[
\boxed{
2f(n)=
\delta_af(n)+
\delta_{ab}f(n)-
\delta_bf(q_a(n)).}
\]

The two adjacent edges are Hamming gradients after parity twist.  The direct composite edge joins equal-parity shells with a plus sign, so it kills their common twisted constant.

After summing against arbitrary nonnegative action weights `u_a u_b`,

\[
\boxed{
4U^2|f(n)|^2
\le3\bigl(UE_1+E_{\rm dir}+E_{\rm tr}\bigr).}
\]

For prime-winding weights, the right side is the complete pair-simplex energy `mathfrak E_N`.  Hence

\[
\boxed{
|r(N)|^2
\le\frac34\frac{\mathfrak E_N}{U_N^2}.}
\]

Thus both the parity constant mode and the terminal one-time scalar readout are closed at exact finite strength.

---

## 3. Sparse primitive chords versus macroscopic provenance chords

Taking `(a,b)=(p,p)` gives the fixed-prime square identity

\[
2f(n)=
\delta_pf(n)+
\delta_{p^2}f(n)-
\delta_pf(q_p(n)).
\]

For `p=2`, weighted Cauchy gives

\[
|f(n)|^2
\le\frac2{\log2}
\left(\mathcal Q(f;n)+
\mathcal Q(f;\lfloor n/2\rfloor)\right).
\]

This is a valid local anchor, but all same-prime factorization chords have finite total unnormalized mass

\[
\sum_p\frac{(\log p)^2}{(p-1)^2}<\infty.
\]

Their normalized pair mass is only `O((log N)^-2)`.  They cannot provide a macroscopic one-step gap.

The full pair-simplex avoids this no-go by retaining `ab` as a degree-two provenance label even when `ab` is not a primitive prime power.  All ordered action pairs contribute, giving total mass `U_N^2`.

---

## 4. Retained local two-channel matrix

For continuation fraction

\[
s=A(m)/A(N),
\]

the residual-free stopped/core row transformation on

\[
(R,V)=(x^2,\text{mixed child standard variance})
\]

is

\[
\boxed{
T(s)=
\begin{pmatrix}
(1-2s)^2&0\\[1mm]
\frac49s(1-s)&s
\end{pmatrix}.}
\]

The mean-square output is the first row.  The standard output consists of the damped stopped/core contrast plus the exactly persistent child standard variance.

The scalar V15 profile

\[
k(s)=1-\frac{32}{9}s(1-s)
\]

is the first-column sum of this matrix.  It is therefore a scalarized image, not the native retained transition.

---

## 5. Two-channel Mellin spectrum

For a logarithmic barrier with exponent `beta`, the entrywise Mellin matrix is

\[
\mathcal M(\beta)=
\begin{pmatrix}
A(\beta)&0\\
C(\beta)&B(\beta)
\end{pmatrix},
\]

where

\[
A(\beta)=
\frac1{1-\beta}-
\frac4{2-\beta}+
\frac4{3-\beta},
\]

\[
B(\beta)=\frac1{2-\beta},
\]

and

\[
C(\beta)=
\frac49\left(
\frac1{2-\beta}-
\frac1{3-\beta}
\right).
\]

It is triangular, so its spectral radius is the larger diagonal entry.  Since `B(beta)<1` for every `beta<1`, the critical point is the unique root of

\[
\boxed{
\beta^3-5\beta^2+10\beta-4=0,}
\]

namely

\[
\boxed{\beta_{\rm ch}=0.522033\ldots .}
\]

For every `beta<beta_ch`, the positive cone functional

\[
R+\lambda_\beta V,
\qquad
\lambda_\beta=
\frac{1-A(\beta)}{2C(\beta)},
\]

contracts with coefficient

\[
q_\beta=
\max\left\{
\frac{1+A(\beta)}2,
B(\beta)
\right\}<1.
\]

This improves the scalarized critical exponent `0.481892...` and makes the representation-theoretic cost of scalarization quantitative.

---

## 6. Exact persistent standard intertwiner

For a parent first action `a`, put

\[
m=\lfloor N/a\rfloor.
\]

The mixed parent second-action row, restricted to the valid core, is exactly

\[
\boxed{
K_mg_m+\text{constant}.}
\]

Hence its standard variance is the same child mixed standard variance; no inverse factor appears.

The exact row second moment is

\[
\begin{aligned}
&((1-2s)x+s\eta)^2+sV(m)\\
&\qquad+
\frac19s(1-s)(2x-\eta)^2,
\end{aligned}
\]

where

\[
\eta=x+P_mr.
\]

The averaged residual forcing is

\[
O\left(\frac{\log\log N}{(\log N)^2}\right).
\]

Thus the local matrix and its forcing are both closed.  No state-propagation ambiguity remains in the standard channel.

---

## 7. Exact alternating Green model

The finite adaptive descent satisfies

\[
r+Pr=e.
\]

If `tau` is the first hitting time of state `1`, finite iteration gives

\[
\boxed{
 r(n)=r(1)\mathbb E_n[(-1)^\tau]
+
\mathbb E_n\sum_{j<\tau}(-1)^je(X_j).}
\]

In the ideal logarithmic Hardy chain, `-log` scale decrements are exponential.  For lower threshold `T_0`,

\[
\tau-1\sim
\operatorname{Poisson}(\log(T/T_0)),
\]

so

\[
\boxed{
\mathbb E[(-1)^\tau]
=-(T_0/T)^2.}
\]

The signed occupation density is

\[
\boxed{
\delta_0-e^{-2y}dy.}
\]

Accordingly, every forcing bounded by `C/(1+T)` remains `O(1/T)` under the ideal alternating resolvent.

The finite arithmetic stopping formula is exact.  What remains is stability of this signed kernel in the odd-simplex Dirichlet topology, not its ideal computation.

---

## 8. Correct unique remaining bridge

The preceding V16 frontier listed two possible final anchor routes.  V17 removes that ambiguity.

The anchor and scalar readout are already supplied by the macroscopic odd simplex.  The only unresolved theorem is an end-to-end same-type recurrence for its normalized energy.

Define

\[
\overline{\mathfrak E}(N)
:=\frac{\mathfrak E_N}{U_N^2}.
\]

The target is a positive embedding into a retained channel state

\[
\mathfrak I_N
\overline{\mathfrak E}(N)
=(R(N),V(N))
\]

such that

\[
\boxed{
(R(N),V(N))
\preccurlyeq
\sum_{q\le N}p_N(q)
T(s_{N,q})
(R(m_q),V(m_q))
+\mathbf F(N),}
\]

with:

1. all three pair-simplex channels `UE_1`, `E_dir`, `E_tr` represented positively;
2. the direct composite chord retained, not collapsed to a primitive action;
3. the persistent standard-core intertwiner used exactly;
4. moving-cutoff errors assigned to the already controlled lower-scale/residual channels;
5. `N_lambda(F(N))=O(1/log N)` or better;
6. no per-level inverse standard projection.

If this theorem holds, then for every `beta<0.522033...`,

\[
\overline{\mathfrak E}(N)
=O((\log N)^{-\beta}),
\]

and the terminal odd-simplex readout gives

\[
|r(N)|=O((\log N)^{-\beta/2}).
\]

This implication is conditional; the recurrence itself is not yet proved.

---

## 9. Updated closure table

Closed:

1. prime birth and winding determinant geometry;
2. qualitative PNT by the already recorded real-smoothing route;
3. complete deepest provenance carrier and V14 density bridge;
4. V15 parity fold and scalar profile;
5. discrete profile transfer;
6. scalar-recanonicalization no-go;
7. persistent standard row intertwiner;
8. fixed- and growing-depth Gamma overlap;
9. radial nonconstant shell gap;
10. odd-simplex constant-mode anchor;
11. terminal one-time scalar readout;
12. local retained two-channel Mellin matrix and exponent;
13. ideal alternating Green resolvent.

Open:

1. global normalized odd-simplex-to-channel recurrence;
2. complete forcing audit for `UE_1`, `E_dir`, and `E_tr` together;
3. a promoted native logarithmic remainder for `psi(N)-N`;
4. any RH-scale conclusion;
5. Working Truth or Foundation promotion.

V17 compresses the program to

\[
\boxed{
\text{local geometry, spectrum, anchor, and terminal readout: closed};
\qquad
\text{one global positive intertwining recurrence: open}.}
\]
