# P022 Barlow — Dual Hasse adjoint first-jet theorem

Status: **PROVED_WIP / exact structural theorem / nonvanishing still open**  
Task: `RS-P022-OBSERVATION-HISTORY`  
Publication: `TP2-2346F5D3E731ED56DB0A`  
Researcher: `EM-P022OBS-D5D438`

## 1. Starting sign-free boundary kernel

For a prime

\[
p=6M-1,
\]

the already-frozen double-horizon reduction gives

\[
W_M=
\sum_{j=0}^{2M-1}
\binom{2M}{j}\binom{M+j}{j}\binom{2M-1}{j}
\pmod p.
\]

Its coefficient is

\[
w_j=
\frac{(-2M)_j(1-2M)_j(M+1)_j}{(j!)^3}.
\]

Since `6M=1 (mod p)`, put

\[
N=2M-1=\frac{p-2}{3}.
\]

Then termwise modulo `p`,

\[
-2M\equiv-\frac13,
\qquad
1-2M\equiv\frac23,
\qquad
M+1\equiv\frac76,
\]

and therefore

\[
\boxed{
W_M\equiv
\sum_{j=0}^{N}
\frac{(-1/3)_j(2/3)_j(7/6)_j}{(j!)^3}
\pmod p.
}
\]

This is a universal truncation: after the boundary prime relation is imposed,
the hypergeometric parameters no longer depend on `M`; only the canonical
cutoff `N=(p-2)/3` remains.

Modulo integer shifts the numerator signature is

\[
\left(\frac16,\frac23,\frac23\right),
\]

which is exactly the `j=5` Dwork/Galois conjugate of the previously frozen
one-third Hasse datum

\[
\left(\frac56,\frac13,\frac13\right).
\]

Thus the sign-free kernel is not a new unrelated rank-three object: it is a
contiguous realization of the already identified conjugate character block.

## 2. Exact conjugate Gosper reduction

Define the canonical conjugate Hasse coefficients

\[
d_j=
\frac{(1/6)_j(2/3)_j^2}{(j!)^3},
\qquad
D_p(z)=\sum_{j=0}^{N}d_jz^j.
\]

The coefficient ratio is

\[
\frac{d_{j+1}}{d_j}
=
\frac{(6j+1)(3j+2)^2}{54(j+1)^3}.
\]

For the boundary coefficient `c_j` above,

\[
\frac{c_j}{d_j}
=-\frac{6j+1}{3j-1}.
\]

Put

\[
R_j=\frac{81j^3}{3j-1}.
\]

A direct rational identity gives

\[
\boxed{
\frac{c_j}{d_j}
=-2-\frac{27}{2}j
+R_{j+1}\frac{d_{j+1}}{d_j}-R_j.
}
\]

At `j=N`, the next coefficient ratio contains

\[
(3N+2)^2=p^2,
\]

while `R_{N+1}` contains only one denominator factor

\[
3N+2=p.
\]

Hence the terminal Gosper certificate still has positive `p`-adic valuation;
`R_0=0`.  Summing therefore proves

\[
\boxed{
W_M\equiv
-2D_p(1)-\frac{27}{2}\theta D_p(1)
\pmod p.
}
\]

This is the conjugate counterpart of the previously proved original-Hasse
first-jet formula.

## 3. Conjugate Picard--Fuchs gate

The conjugate canonical period satisfies

\[
\left[
\theta^3-z\left(\theta+\frac16\right)
\left(\theta+\frac23\right)^2
\right]D=0.
\]

At `z=1`, the cubic terms cancel and

\[
\left(\theta+\frac16\right)
\left(\theta+\frac23\right)^2-	heta^3
=
\frac{(9\theta+2)^2}{54}.
\]

Thus

\[
\boxed{
81\theta^2D_p(1)+36\theta D_p(1)+4D_p(1)=0.
}
\]

The local exponent set at `z=1` is again

\[
\{0,1,1/2\}.
\]

Since

\[
\deg D_p=N=\frac{p-2}{3}<\frac p2,
\]

an integral root multiplicity cannot equal the half-root modulo `p`.  Hence a
scalar zero `D_p(1)=0`, whenever it occurs, is simple.

Consequently

\[
W_M=0\quad\Longrightarrow\quad D_p(1)\ne0,
\]

and the boundary zero condition is exactly

\[
\boxed{
W_M=0
\iff
\frac{\theta D_p(1)}{D_p(1)}=-\frac4{27}
\pmod p.
}
\]

## 4. Exact formal-adjoint pairing

Write the original canonical operator in ordinary `d/dz` form as

\[
L_P=a_3\partial^3+a_2\partial^2+a_1\partial+a_0,
\]

with

\[
a_3=z^2(1-z),
\qquad
a_2=3z-\frac92z^2,
\qquad
a_1=1-\frac{19}{6}z,
\qquad
a_0=-\frac5{54}.
\]

For the negative formal adjoint `-L_P^*`, the coefficients are

\[
\begin{aligned}
b_3&=a_3,\\
b_2&=3a_3'-a_2,\\
b_1&=3a_3''-2a_2'+a_1,\\
b_0&=a_3'''-a_2''+a_1'-a_0.
\end{aligned}
\]

Direct substitution yields

\[
b_3=a_3,\qquad b_2=a_2,\qquad b_1=a_1,\qquad
b_0=-\frac2{27}.
\]

But `-2/27=-(1/6)(2/3)^2`, so this is exactly the conjugate canonical
hypergeometric operator.  Therefore

\[
\boxed{L_D=-L_P^*.}
\]

The Lagrange concomitant for a solution `P` of `L_P P=0` and a solution `D`
of `L_D D=0` is

\[
\begin{aligned}
\mathcal B(P,D)=
&\ a_3(DP''-D'P'+D''P)\\
&+(a_2-a_3')DP' +(2a_3'-a_2)D'P\\
&+(a_3''-a_2'+a_1)DP.
\end{aligned}
\]

Its derivative vanishes.  At `z=0`,

\[
a_3=a_2=a_3'=0,
\qquad
a_3''-a_2'+a_1=2-3+1=0,
\]

so

\[
\mathcal B(P,D)=0
\]

identically.

At `z=1`,

\[
a_3=0,
\quad a_2-a_3'=-\frac12,
\quad 2a_3'-a_2=-\frac12,
\quad a_3''-a_2'+a_1=-\frac16.
\]

Since `theta=d/dz` at `z=1`, the zero concomitant becomes

\[
\boxed{
3\left(D\,\theta P+P\,\theta D\right)+PD=0.
}
\]

Therefore, on the joint scalar-ordinary locus,

\[
\boxed{
\frac{\theta P}{P}+\frac{\theta D}{D}=-\frac13.
}
\]

## 5. The two first-jet targets are one adjoint condition

The previously frozen original-Hasse theorem says that a one-third Franel zero
lies in the original scalar-ordinary locus and satisfies

\[
\frac{\theta P}{P}=-\frac5{27}.
\]

The new conjugate reduction gives

\[
\frac{\theta D}{D}=-\frac4{27}.
\]

But

\[
-\frac5{27}-\frac4{27}=-\frac13,
\]

exactly the formal-adjoint Lagrange relation.

Hence these are **not two independent first-order obstructions**.  They are the
two sides of one dual Hasse condition.  In particular, trying to prove boundary
nonvanishing by adding the conjugate scalar first jet cannot succeed without a
new invariant.

The route boundary is now sharper:

\[
\boxed{
\text{next independent object must be matrix/second-order: a transfer minor,
Casoratian, Cartier block determinant, or equivalent.}
}
\]

This explains why the conductor-18 three-section construction remains useful:
it introduces information not already forced by the rank-three adjoint pair.

## 6. Regression controls

The executable theorem checks the exact rational Gosper identity, the conjugate
Picard--Fuchs relation, the formal-adjoint coefficient identity, and the
Lagrange relation.

Two useful controls are retained:

- `p=107`: both scalar Hasse values vanish, but the boundary/Franel obstruction
  does not; the conjugate scalar zero is certified simple.
- `p=149`: the known non-target control `149 | F_50` satisfies both paired
  logarithmic-derivative conditions `-5/27` and `-4/27` exactly.

These controls are theorem diagnostics, not evidence for the admissible
all-parameter nonvanishing statement.
