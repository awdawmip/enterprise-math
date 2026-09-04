# Free Research — Retained Two-Channel Mellin Matrix

Status: `FREE_RESEARCH_FRONTIER / EXACT_LOCAL_CHANNEL_MATRIX / TRIANGULAR_MELLIN_SPECTRUM / CRITICAL_EXPONENT_0_522 / WEIGHTED_CONE_CONTRACTION / GLOBAL_ODD_SIMPLEX_EMBEDDING_OPEN / NOT_WORKING_TRUTH / NOT_FOUNDATION`
Date: `2026-09-04`
Project: `Enterprise Math / 进取数论`
Parents:

- `FREE_RESEARCH_PERSISTENT_ROW_MIXER_INTERTWINER_V16_20260904.md`;
- `FREE_RESEARCH_DISCRETE_PROFILE_TRANSFER_V16_20260904.md`;
- `FREE_RESEARCH_ODD_SIMPLEX_CONSTANT_MODE_ANCHOR_V16_20260904.md`.

Researcher-ID: `EM-FREE-PI-PRIME-20260904`
Reuse-Resolution: `COMPOSE_APPLIED` from the exact stopped/core row ANOVA, `S_3` standard multiplier, and discrete Mellin transfer calculus.

## 1. Executive advance

The scalar V15 profile

\[
k(s)=1-\frac{32}{9}s(1-s)
\]

adds the mean and standard energies before scale transport.  Retaining the two channels instead produces a triangular positive matrix whose spectral radius is strictly smaller.

For continuation fraction `s in [0,1]`, the homogeneous local row transition is

\[
\boxed{
T(s)=
\begin{pmatrix}
(1-2s)^2&0\\[1mm]
\frac49s(1-s)&s
\end{pmatrix}.}
\tag{1.1}
\]

The input coordinates are:

- `R=x^2`, the stopped/root parity amplitude squared;
- `V`, the already mixed child standard variance.

The output coordinates are:

- squared ordinary row mean;
- mixed row standard energy.

The scalar profile is the first-column sum:

\[
(1,1)T(s)(1,0)^T=k(s).
\]

For a logarithmic barrier `T^-beta`, the Mellin transfer matrix is

\[
\boxed{
\mathcal M(\beta)=
\begin{pmatrix}
A(\beta)&0\\
C(\beta)&B(\beta)
\end{pmatrix},}
\tag{1.2}
\]

where

\[
A(\beta)=
\frac1{1-\beta}-
\frac4{2-\beta}+
\frac4{3-\beta},
\tag{1.3}
\]

\[
B(\beta)=\frac1{2-\beta},
\tag{1.4}
\]

and

\[
C(\beta)=
\frac49\left(
\frac1{2-\beta}-
\frac1{3-\beta}
\right).
\tag{1.5}
\]

Its critical exponent is not the scalar-profile root `0.481892...`, but the unique root

\[
\boxed{
\beta_{\rm ch}^3-5\beta_{\rm ch}^2+
10\beta_{\rm ch}-4=0,}
\tag{1.6}
\]

namely

\[
\boxed{\beta_{\rm ch}=0.522033\ldots .}
\tag{1.7}
\]

Thus retaining the standard channel enlarges the admissible energy exponent.

---

## 2. Exact local matrix

In the notation of the persistent row-mixer theorem, let

\[
x=r(m),
\qquad
s=\frac{A(m)}{A(N)},
\]

and first ignore the residual

\[
\eta=x+P_mr.
\]

The row mean is

\[
(1-2s)x,
\]

so its squared energy is

\[
M'=(1-2s)^2x^2.
\tag{2.1}
\]

The exact mixed row variance is

\[
S'=sV+\frac19s(1-s)(2x)^2
=sV+\frac49s(1-s)x^2.
\tag{2.2}
\]

Equations (2.1)--(2.2) are exactly (1.1).

Summing the two output channels when the input standard channel is zero gives

\[
(1-2s)^2+\frac49s(1-s)
=1-\frac{32}{9}s(1-s),
\]

recovering the scalar profile.  The scalar profile therefore mixes a lower-left transfer into the diagonal at every level.  The retained matrix does not.

---

## 3. Mellin transfer

Under the prime-power first-mass law, the normalized child logarithmic scale `s` is asymptotically uniform.  A barrier

\[
E(m)\asymp(sT)^{-\beta}
\]

therefore transforms by integrating `T(s)s^-beta` over `[0,1]`.

The entries are elementary:

\[
\int_0^1(1-2s)^2s^{-\beta}ds
=A(\beta),
\]

\[
\int_0^1s\,s^{-\beta}ds
=B(\beta),
\]

and

\[
\int_0^1\frac49s(1-s)s^{-\beta}ds
=C(\beta).
\]

The same truncation/discrepancy proof used for the scalar profile applies entrywise for every `beta<1`, so the finite prime-power matrix has the asymptotic multiplier (1.2).

---

## 4. Spectral radius and critical polynomial

Since `M(beta)` is triangular,

\[
\rho(\mathcal M(\beta))
=\max\{A(\beta),B(\beta)\}.
\]

For `0<=beta<1`,

\[
B(\beta)=\frac1{2-\beta}<1.
\]

Thus the first loss of contraction occurs at `A(beta)=1`.

Clearing denominators gives

\[
\boxed{
A(\beta)=1
\iff
\beta^3-5\beta^2+10\beta-4=0.}
\tag{4.1}
\]

Let

\[
P(\beta)=\beta^3-5\beta^2+10\beta-4.
\]

Then

\[
P'(\beta)=3\beta^2-10\beta+10.
\]

Its discriminant is

\[
100-120=-20<0,
\]

and its leading coefficient is positive, so `P` is strictly increasing on the real line.  Since

\[
P(0)=-4,
\qquad
P(1)=2,
\]

there is one and only one root in `(0,1)`.  Rational evaluation at nearby decimals certifies (1.7).

For every

\[
0\le\beta<\beta_{\rm ch},
\]

both diagonal entries are strictly below one.

---

## 5. Explicit weighted cone contraction

Fix `beta<beta_ch` and abbreviate

\[
a=A(\beta),
\qquad b=B(\beta),
\qquad c=C(\beta).
\]

Then

\[
0\le a,b<1,
\qquad c>0.
\]

For a positive row weight `lambda`, use the cone functional

\[
\mathcal N_\lambda(R,V)=R+\lambda V.
\]

Under the Mellin matrix,

\[
\mathcal N_\lambda(\mathcal M(R,V))
=(a+\lambda c)R+\lambda bV.
\]

Choose

\[
\boxed{
\lambda_\beta=\frac{1-a}{2c}.}
\tag{5.1}
\]

Then

\[
a+\lambda_\beta c=\frac{1+a}{2}<1.
\]

Consequently

\[
\boxed{
\mathcal N_{\lambda_\beta}(\mathcal M(R,V))
\le q_\beta\mathcal N_{\lambda_\beta}(R,V),}
\tag{5.2}
\]

where

\[
\boxed{
q_\beta=
\max\left\{\frac{1+A(\beta)}2,
B(\beta)\right\}<1.}
\tag{5.3}
\]

This is an explicit Perron cone certificate; no matrix norm search is required.

---

## 6. Residual forcing

The exact local row formula with residual `eta` is

\[
\begin{aligned}
M'+S'
={}&((1-2s)x+s\eta)^2+sV\\
&+\frac19s(1-s)(2x-\eta)^2.
\end{aligned}
\]

Keeping the two output squares separate gives a vector perturbation whose squared residual norm is bounded by

\[
s\eta^2.
\]

The persistent row theorem already proves

\[
\mathbb E[s\eta^2]
=O\left(\frac{\log\log N}{(\log N)^2}\right).
\]

For every `beta<1`, this forcing is lower order than `T^-beta`, so it does not change the critical exponent once the global same-type recurrence is established.

---

## 7. Comparison with scalarization

The scalar multiplier is

\[
M_{\rm sc}(\beta)
=A(\beta)+C(\beta).
\]

Its critical equation is

\[
9\beta^3-45\beta^2+86\beta-32=0,
\]

with root `0.481892...`.

The inequality

\[
\beta_{\rm sc}<\beta_{\rm ch}
\]

has a structural explanation: scalarization adds the standard energy produced from the mean channel directly back into the same coordinate at every scale.  The retained matrix lets that energy remain in the second channel, whose own diagonal multiplier `B(beta)` is still below one.

Thus the exponent improvement is not a numerical accident.  It is the spectral benefit of preserving representation type.

---

## 8. Conditional two-channel barrier theorem

Suppose a nonnegative state

\[
\mathbf E(N)=
\begin{pmatrix}R(N)\\V(N)\end{pmatrix}
\]

satisfies the finite prime-power counterpart of

\[
\mathbf E(N)
\preccurlyeq
\sum_{q\le N}p_N(q)
T(s_{N,q})
\mathbf E(\lfloor N/q\rfloor)
+\mathbf F(N),
\tag{8.1}
\]

with

\[
\mathcal N_{\lambda_\beta}(\mathbf F(N))
=O((\log N)^{-1}).
\]

Then entrywise discrete Mellin transfer and (5.2) give, for every `beta<beta_ch`,

\[
\boxed{
\mathcal N_{\lambda_\beta}(\mathbf E(N))
=O((\log N)^{-\beta}).}
\tag{8.2}
\]

If the macroscopic odd-simplex terminal readout embeds as

\[
|r(N)|^2\le C\mathcal N_{\lambda_\beta}(\mathbf E(N)),
\]

then

\[
|r(N)|
=O((\log N)^{-\beta/2}).
\]

The terminal scalar anchor itself is now closed by the odd-simplex theorem.  What remains is to identify its complete normalized energy with a state satisfying (8.1).

---

## 9. Unique remaining integration theorem

Construct a finite positive embedding

\[
\boxed{
\mathfrak I_N:
\frac{\mathfrak E_N}{U_N^2}
\longrightarrow
(R(N),V(N))}
\tag{9.1}
\]

such that:

1. `R` is the retained row mean/parity square;
2. `V` is the persistent mixed standard variance;
3. the three pair-simplex channels `UE_1`, `E_dir`, and `E_tr` are all represented without negative cancellation;
4. quotient descent intertwines `mathfrak I_N` with the local matrix `T(s)`;
5. moving-cutoff and endpoint terms enter the already summable residual vector;
6. no inverse standard projection is applied before the terminal scale.

This is now the sole gap between the exact V16 local matrix and a native quantitative remainder.

---

## 10. Current classification

Closed:

- exact local two-channel matrix;
- entrywise discrete Mellin transfer;
- triangular spectrum;
- unique critical exponent `0.522033...`;
- explicit positive cone contraction;
- residual forcing compatibility;
- explanation of the scalar exponent loss.

Open:

- the global odd-simplex-to-channel embedding (9.1);
- a complete finite recurrence with the same state type at parent and child;
- a promoted logarithmic remainder for `psi(N)-N`;
- any RH-scale conclusion, Working Truth, or Foundation promotion.
