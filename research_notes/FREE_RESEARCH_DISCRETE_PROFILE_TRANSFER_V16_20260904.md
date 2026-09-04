# Free Research — Discrete Prime-Power Profile Transfer and Scalar Recanonicalization No-Go

Status: `FREE_RESEARCH_FRONTIER / DISCRETE_VOLERRA_PROFILE_TRANSFER / RATIONAL_CRITICAL_POLYNOMIAL / CONDITIONAL_LOG_RATE / SINGLE_CHANNEL_RECLOSURE_REFUTED / TWO_CHANNEL_INTERTWINER_OPEN / NOT_WORKING_TRUTH / NOT_FOUNDATION`
Date: `2026-09-04`
Project: `Enterprise Math / 进取数论`
Parents:

- `FREE_RESEARCH_PI_PRIME_GEOMETRY_FRONTIER_V15_20260904.md`;
- `FREE_RESEARCH_PRIME_PARITY_BLOCK_COUPLING_V16_20260904.md`.

Researcher-ID: `EM-FREE-PI-PRIME-20260904`
Reuse-Resolution: `COMPOSE_APPLIED` from the V15 parity-fold scattering law, the first prime-power mass estimate, the `S_3` relation mixer, and the existing affine cascade calculus.

## 1. Executive result

The V15 ideal profile kernel

\[
\boxed{k(s)=1-\frac{32}{9}s(1-s)}
\tag{1.1}
\]

is not merely a continuum heuristic.  The actual finite prime-power quotient cloud inherits its Mellin multiplier:

\[
\boxed{
M(\beta)
=\frac1{1-\beta}
-\frac{32}{9(2-\beta)}
+\frac{32}{9(3-\beta)},
\qquad0\le\beta<1.
}
\tag{1.2}
\]

The equation `M(beta)=1` is equivalent to

\[
\boxed{9\beta^3-45\beta^2+86\beta-32=0.}
\tag{1.3}
\]

It has a unique root

\[
\boxed{\beta_*=0.481892\ldots}
\tag{1.4}
\]

in `(0,1)`.

Consequently, any genuinely persistent two-channel energy satisfying the finite V15 profile recurrence has decay

\[
E(N)=O\bigl((\log N)^{-\beta}\bigr)
\quad\text{for every }\beta<\beta_*.
\tag{1.5}
\]

A one-time quadratic scalar readout would then give

\[
\left|\frac{\psi(N)}N-1\right|
=O\bigl((\log N)^{-\beta/2}\bigr),
\qquad\beta<\beta_*.
\tag{1.6}
\]

The same analysis proves a no-go: if the mean and standard channels are collapsed back to one scalar norm after every level, the exact scattering conservation restores coefficient `1`.  Thus (1.5) is conditional on a retained two-channel intertwiner; it cannot be obtained by repeatedly converting to a scalar envelope.

---

## 2. V15 scattering profile

For one stopped/core row, let

\[
\alpha\in[0,1]
\]

be the valid-continuation mass fraction.  In the homogeneous residual-free model, the stopped value is `x` and the valid-core mean is `-x`.

The row mean is

\[
\boxed{m=(1-2\alpha)x,}
\tag{2.1}
\]

while the core/stopped contrast energy is

\[
\boxed{c=4\alpha(1-\alpha)x^2.}
\tag{2.2}
\]

They obey the exact orthogonal scattering law

\[
\boxed{m^2+c=x^2.}
\tag{2.3}
\]

The `S_3` mixer leaves the mean line fixed and multiplies the standard amplitude by `1/3`, hence the contrast energy by `1/9`.  The surviving row energy is

\[
\begin{aligned}
m^2+\frac19c
&=\left((1-2\alpha)^2+
\frac49\alpha(1-\alpha)\right)x^2\\
&=\boxed{k(\alpha)x^2},
\end{aligned}
\tag{2.4}
\]

with `k` as in (1.1).

The minimum occurs at `alpha=1/2`:

\[
\boxed{\min_{0\le\alpha\le1}k(\alpha)=\frac19.}
\tag{2.5}
\]

---

## 3. Scalar recanonicalization no-go

Suppose a proof retains only the total damped scalar energy

\[
E'=m^2+c/9=k(\alpha)x^2
\]

and then attempts to recover the original scalar channel `x^2` through a uniform inequality

\[
x^2\le C E'.
\]

Taking `alpha=1/2` forces

\[
\boxed{C\ge9.}
\tag{3.1}
\]

At that point

\[
CE'\ge x^2,
\]

with equality for the most strongly mixed row.  Hence no strict uniform contraction survives a scalar forgetful projection followed by scalar reconstruction.

Equivalently, before damping, (2.3) shows that mean and contrast are complementary channels carrying exactly the original energy.  Damping only one channel creates a gain if the two channels remain typed separately.  Forgetting that typing makes the missing contrast recoverable only at the reciprocal cost of the damping.

Therefore:

\[
\boxed{
\text{MIX STANDARD BY }1/9
+\text{FORGET CHANNEL TYPE}
+\text{RECONSTRUCT SCALAR}
\Longrightarrow\text{NO STRICT GAP}.}
\tag{3.2}
\]

This is the finite version of the normalization obstruction previously seen for per-level clipped-profile conversion.

---

## 4. Actual arithmetic profile coordinate

For a parent cutoff `N`, write

\[
T:=\log N,
\qquad
m_{N,q}:=\left\lfloor\frac Nq\right\rfloor,
\]

and define the normalized child logarithmic scale

\[
\boxed{s_{N,q}:=rac{\log m_{N,q}}T\in[0,1].}
\tag{4.1}
\]

The action probability is

\[
\boxed{p_N(q):=\frac{\omega(q)}{A(N)},
\qquad
\omega(q)=\Lambda(q)/q.}
\tag{4.2}
\]

The first-mass theorem

\[
A(X)=\log X+O(1)
\tag{4.3}
\]

implies that the distribution of `s_(N,q)` converges to Lebesgue measure on `[0,1]`.

For fixed `z in (0,1]`,

\[
\boxed{
\sum_{s_{N,q}\le z}p_N(q)
=z+O_z(1/T).}
\tag{4.4}
\]

The floor displacement is controlled by

\[
0\le\log(N/q)-\log\lfloor N/q\rfloor
\le\frac{2q}{N}
\qquad(q\le N/2),
\]

so its mean is `O(1/T)` by `psi(N)=O(N)`.  The boundary `m=1` has probability `O(1/T)`.

---

## 5. Discrete Mellin transfer theorem

For `0<=beta<1`, define the regularized barrier

\[
B_\beta(t):=(1+t)^{-\beta}.
\]

Then

\[
\boxed{
\lim_{N\to\infty}
T^\beta
\sum_{q\le N}p_N(q)
 k(s_{N,q})B_\beta(\log m_{N,q})
=M(\beta),
}
\tag{5.1}
\]

with `M` given by (1.2).

### Proof scheme

Fix `delta in (0,1)` and split the child scale into `s<=delta` and `s>delta`.

On `[delta,1]`, the test function

\[
s\longmapsto k(s)s^{-\beta}
\]

has bounded variation.  The discrepancy estimate (4.4), Stieltjes summation, and the floor bound give convergence to its Lebesgue integral.

On `[0,delta]`, positivity and `beta<1` give the uniform bound

\[
\limsup_N
T^\beta\sum_{s_{N,q}\le\delta}
 p_N(q)k(s_{N,q})B_\beta(Ts_{N,q})
\ll\delta^{1-\beta}.
\]

Letting `delta` tend to zero proves (5.1).

The integral is

\[
\begin{aligned}
\int_0^1 k(s)s^{-\beta}\,ds
&=\int_0^1
\left(1-\frac{32}{9}s+\frac{32}{9}s^2\right)s^{-\beta}\,ds\\
&=\frac1{1-\beta}
-\frac{32}{9(2-\beta)}
+\frac{32}{9(3-\beta)}.
\end{aligned}
\]

Thus the finite prime-power cloud and the ideal Volterra model have the same asymptotic Mellin multiplier.

---

## 6. Critical polynomial and uniqueness

Clearing denominators in `M(beta)=1` gives

\[
\boxed{P(\beta)=9\beta^3-45\beta^2+86\beta-32=0.}
\]

Its derivative is

\[
P'(\beta)=27\beta^2-90\beta+86.
\]

The discriminant is

\[
(-90)^2-4\cdot27\cdot86=-1188<0,
\]

and the leading coefficient is positive.  Hence

\[
P'(\beta)>0
\]

for every real `beta`.  Since

\[
P(0)=-32,
\qquad
P(1)=18,
\]

there is exactly one root in `(0,1)`.  Rational interval evaluation gives, for example,

\[
P(0.4818)<0<P(0.4820),
\]

which certifies (1.4) without treating a floating root finder as proof.

For every `beta<beta_*`,

\[
\boxed{M(\beta)<1.}
\tag{6.1}
\]

---

## 7. Conditional finite barrier theorem

Let `E(N)>=0` be a bounded initial finite energy and assume that, for all sufficiently large `N`,

\[
\boxed{
E(N)
\le
\sum_{q\le N}p_N(q)
 k(s_{N,q})E(m_{N,q})
+\frac{C}{\log N}.
}
\tag{7.1}
\]

Assume crucially that `E` is the same retained two-channel state at every child scale; no per-level scalar recanonicalization is inserted.

Fix `beta<beta_*`.  By (5.1), there are `eta>0` and `N_0` such that

\[
T^\beta
\sum_qp_N(q)k(s_{N,q})
(1+\log m_{N,q})^{-\beta}
\le1-\eta
\]

for `N>=N_0`.

Choose `B` large enough to dominate the finite initial range and satisfy

\[
C T^{-1}\le\eta B T^{-\beta}
\]

for `T>=log N_0`; this is possible because `beta<1`.  Strong induction then gives

\[
\boxed{E(N)\le B(1+\log N)^{-\beta}.}
\tag{7.2}
\]

Thus

\[
\boxed{
E(N)=O((\log N)^{-\beta})
\quad(\beta<\beta_*).
}
\tag{7.3}
\]

---

## 8. One-time scalar readout

Suppose the retained energy has a final, noniterated coercive readout

\[
\boxed{
|r(N)|^2
\le C_0E(N)+O((\log N)^{-2}).
}
\tag{8.1}
\]

Then (7.3) gives

\[
\boxed{
|r(N)|
=O((\log N)^{-\beta/2})
\qquad(\beta<\beta_*).
}
\tag{8.2}
\]

The maximal exponent suggested by this mechanism is

\[
\boxed{\beta_*/2=0.240946\ldots .}
\tag{8.3}
\]

This number is not yet a theorem about primes.  It is the sharp barrier exponent of the ideal profile kernel under the exact finite transfer (5.1), conditional on recurrence (7.1) and readout (8.1).

---

## 9. Relation to the parity-block route

The parity-block coupling provides a complementary constant-overlap mechanism.  Its matched block variance is precisely the kind of retained standard channel that cannot be scalarized by Section 3.

The two routes now agree on the structural requirement:

1. preserve a mean/parity channel;
2. preserve a standard relation channel;
3. apply `S_3` damping only to the standard channel;
4. transport both channels to lower scales before any scalar readout;
5. read `r(N)` only once, at the end.

The profile route predicts a Mellin exponent.  The parity-block route predicts a constant macrostep coefficient if its maximal coupling can be made `S_3`-equivariant.  Either route fails under per-level scalar reconstruction.

---

## 10. Current boundary

Closed at research-note theorem strength:

1. exact scattering profile `k(s)`;
2. scalar recanonicalization no-go;
3. discrete prime-power convergence to the profile integral;
4. exact Mellin multiplier;
5. rational critical polynomial and unique root;
6. conditional barrier theorem for every `beta<beta_*`;
7. conditional one-time scalar exponent `beta/2`.

Still open:

1. prove the actual V15 two-channel state satisfies (7.1) without hidden norm conversion;
2. construct the parity-block / `S_3` equivariant matched subkernel;
3. identify the final coercive readout (8.1) with the retained state using only one terminal comparison;
4. promote any explicit prime remainder;
5. any RH-scale claim, Working Truth, or Foundation promotion.
