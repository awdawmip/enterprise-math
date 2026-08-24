# P017 — P2/Chen Carry Bridge, Supplement 02

Status: `PROVED_WIP EXACT PARITY FUNCTIONAL + ROUTE NO-GO / NOT CANONICAL / NO ALL-K P2 CLAIM`

Date: `2026-08-24`

Researcher-ID: `EM-PRIMEBRC-7F3A21`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Depends on:

- `docs/P017_P2_CHEN_CARRY_BRIDGE_20260823.md`;
- `docs/P017_P2_CHEN_CARRY_BRIDGE_SUPPLEMENT_01_20260824.md`.

Scope: determine whether the sharp half-visible detector, the root-linear detector, or any affine interpolation between them can close the exact square-root level by ordinary independent one-dimensional linear-sieve lower/upper bounds.

---

## 1. Standard one-dimensional sieve functions

Let `f(s)` and `F(s)` denote the standard dimension-one lower and upper linear-sieve functions, normalized by

\[
f(s)=0\qquad(0<s\le2),
\]

\[
sF(s)=2e^\gamma\qquad(0<s\le3),
\]

and the differential-delay equations

\[
(sf(s))'=F(s-1)\qquad(s>2),
\]

\[
(sF(s))'=f(s-1)\qquad(s>3).
\]

Only the following consequences are needed:

1. `f(s)>=0`;
2. `G(s):=sF(s)` is nondecreasing, since `G'(s)=f(s-1)>=0` for `s>3` and is constant before that;
3. for `s>2`,
   \[
   \boxed{
   sf(s)=\int_1^{s-1}F(v)\,dv.
   }
   \]

The last identity follows by integrating `(sf)'=F(s-1)` from `2` to `s`.

---

## 2. P2-R12 — The half-weight parity functional is nonpositive

At exact root distribution level `D=W`, take

\[
z=W^{1/s},
\qquad s>2.
\]

After fixing a visible prime `p=z^u`, an ordinary one-dimensional upper sieve remains available only through

\[
1\le u\le s-1,
\]

that is, `p<=D/z=W/z`.

For the sharp constant-half detector from Supplement 01, the normalized one-dimensional contribution is

\[
\boxed{
\mathcal P(s)
=
f(s)
-
\frac12
\int_1^{s-1}
F(s-u)\frac{du}{u}.
}
\]

### Theorem

For every `s>2`,

\[
\boxed{
\mathcal P(s)\le0.
}
\]

More precisely,

\[
\boxed{
\mathcal P(s)=0\quad(2<s\le4),
\qquad
\mathcal P(s)<0\quad(s>4).
}
\]

### Proof

Change variables `v=s-u` and use the integral formula for `sf(s)`:

\[
\begin{aligned}
\mathcal P(s)
&=
\frac1s\int_1^{s-1}F(v)\,dv
-
\frac12\int_1^{s-1}\frac{F(v)}{s-v}\,dv\\
&=
\int_1^{s-1}
\frac{(s-2v)F(v)}{2s(s-v)}\,dv.
\end{aligned}
\]

Pair the point `v` with `s-v`. This gives

\[
\boxed{
\mathcal P(s)
=
\frac1{2s}
\int_1^{s/2}
(s-2v)
\left(
\frac{F(v)}{s-v}
-
\frac{F(s-v)}{v}
\right)dv.
}
\]

For `1<=v<=s/2`, one has `v<=s-v`. Since `G(x)=xF(x)` is nondecreasing,

\[
vF(v)
\le
(s-v)F(s-v),
\]

which is equivalent to

\[
\frac{F(v)}{s-v}
\le
\frac{F(s-v)}{v}.
\]

The other factor `s-2v` is nonnegative. Hence the integrand is nonpositive and `mathcal P(s)<=0`.

If `2<s<=4`, both `v` and `s-v` stay in `[1,3]`, where `xF(x)=2e^gamma` is constant. The paired integrand vanishes identically, so `mathcal P(s)=0`.

If `s>4`, the paired interval contains a positive-measure set with `v<3<s-v`. Since

\[
G'(x)=f(x-1)>0
\qquad(x>3),
\]

`G(s-v)>G(v)` there, and the integral is strictly negative. ∎

### Closed form on the equality range

For `2<s<=4`, `F(v)=2e^gamma/v` throughout the integral. Therefore

\[
\frac12\int_1^{s-1}\frac{F(s-u)}u\,du
=
\frac{2e^\gamma}{s}\log(s-1)
=
f(s),
\]

which displays the equality directly.

---

## 3. P2-R13 — Entire affine detector family collapses to the same obstruction

Let

\[
0\le t\le1
\]

and define the per-visible-prime multiplicity penalty

\[
\boxed{
\rho_t(x)
=
\frac{1+t}{2}-tx,
\qquad 0<x<1.
}
\]

For `n in I_K`, put

\[
\mathfrak w_{K,t}(n)
=
1-
\sum_{\substack{p<W\\p\text{ prime}}}
\nu_p(n)
\rho_t\!\left(\frac{\log p}{\log W}\right).
\]

This is the convex interpolation

\[
\boxed{
\mathfrak w_{K,t}
=
(1-t)\mathfrak w_{K,\mathrm{half-mult}}
+t\mathfrak w_{K,\mathrm{root}},
}
\]

where

\[
\mathfrak w_{K,\mathrm{half-mult}}
=1-\frac12\sum_{p<W}\nu_p(n)
\]

and `mathfrak w_(K,root)` is P2-R01 from the parent note.

Both endpoint detectors are positive on primes and semiprimes in `I_K` and nonpositive on every state with `Omega>=3`. Hence every `t in [0,1]` is also a valid pointwise P2 detector.

At root level `D=W`, with `z=W^(1/s)` and `p=z^u`, its normalized one-dimensional coefficient is

\[
\mathcal P_t(s)
=
f(s)
-
\int_1^{s-1}
\left(
\frac{1+t}{2}-\frac{tu}{s}
\right)
F(s-u)\frac{du}{u}.
\]

### Theorem

For every `s>2` and every `t in [0,1]`,

\[
\boxed{
\mathcal P_t(s)
=
(1+t)\mathcal P(s)
\le0.
}
\]

### Proof

Write

\[
J(s)=\int_1^{s-1}F(s-u)\frac{du}{u}.
\]

Also,

\[
\int_1^{s-1}F(s-u)\,du
=
\int_1^{s-1}F(v)\,dv
=
sf(s).
\]

Therefore

\[
\begin{aligned}
\mathcal P_t(s)
&=
f(s)-\frac{1+t}{2}J(s)
+\frac ts\cdot sf(s)\\
&=
(1+t)\left(f(s)-\frac12J(s)\right)\\
&=
(1+t)\mathcal P(s).
\end{aligned}
\]

P2-R12 supplies the sign. ∎

---

## 4. Interpretation

The half detector has a better naive random-divisibility main coefficient than the root-linear detector. Nevertheless, once the exact lower/upper linear-sieve functions are inserted at `D=W`, the entire apparent advantage disappears into a scalar multiple of the same nonpositive functional.

Thus the obstruction is not poor tuning of the prime penalty. It is the extremal relation between the one-dimensional lower and upper sieve functions at the square-root level.

The conclusion is exact:

\[
\boxed{
\text{no detector in this affine half-to-root family can prove positivity using only independent 1D linear-sieve bounds at }D=W.
}
\]

This is a project-local derivation of the classical sieve parity boundary. It makes no historical novelty claim.

---

## 5. Consequence for the carry program

The original high-prime term

\[
\sum_p\sum_d\lambda_d\bigl(H_{pd}(K)-H_{2pd}(K)\bigr)
\]

cannot be removed by replacing the root-linear detector with the sharp half detector or any affine interpolation. At exact root level, all such choices remain on the same nonpositive one-dimensional boundary.

Therefore a positive route must use at least one ingredient not represented by independent one-dimensional upper bounds, such as:

1. Chen switching and a two-dimensional Selberg/Buchstab estimate;
2. a genuine super-root bilinear remainder theorem;
3. square-specific correlation that improves the high-prime roughness average beyond generic linear-sieve extremals.

The exact P017 binary-carry identity remains a useful coordinate for such an ingredient, but the identity alone does not break parity.

---

## 6. Updated route verdict

`HALF_VISIBLE_DETECTOR = POINTWISE_CLOSED`.

`AFFINE_HALF_TO_ROOT_WEIGHT_OPTIMIZATION_AT_D_EQ_W = CLOSED_NEGATIVE`.

`ONE_DIMENSIONAL_LINEAR_SIEVE_AT_EXACT_ROOT = NONPOSITIVE_BY_EXACT_PAIRING`.

`TWO_DIMENSIONAL_SWITCHING_OR_SUPER_ROOT_CORRELATION = GENUINELY_NECESSARY`.

No Legendre theorem and no all-`K` P2 theorem is claimed.