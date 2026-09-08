# RH Möbius cut-flux Renyi / growing-moment Gram hierarchy

Status: `RESEARCH FRONTIER / EXACT REFORMULATION + PRIOR-ART-ADJACENT / NOT A PROOF OF RH`
Date: `2026-09-08`
Project: `Enterprise Math / 进取数论`
Scope: `Mertens / transport flux / Renyi moments / positive Gram replicas / RH`

## 0. Motivation and correction context

The dyadic W1/earthmover cost is an exact L1 norm of the cumulative Mertens cut flux, but the natural `X^(3/2)` W1 bound is only an RH consequence, not an equivalence. A fixed Lp moment similarly loses a definite power when converted back to a pointwise Mertens bound.

The correct positive transport hierarchy is obtained by allowing the flux moment order to grow.

This note is prior-art-adjacent. Verjovsky (2026, arXiv:2607.25002) proves an RH-equivalent local high-moment criterion for normalized Möbius Fourier polynomials on arcs of scale `1/N`, and explicitly notes that one fixed moment gives an exponent above `1/2` while arbitrarily high moments recover the critical exponent. The present note concerns cumulative integer-line cut flux instead of local Fourier moments and packages its even moments as exact finite Gram energies. No novelty claim is made for the general high-moment-to-point-value philosophy.

---

## 1. Normalized cumulative-flux moments

Let

`M(t)=sum_{n<=t}mu(n)`

and for `p>=1` define

`F_p(X)=[ (1/X) sum_{1<=t<=X}|M(t)|^p ]^(1/p)`.

Because

`M(t)-M(t-1)=mu(t) in {-1,0,1}`,

M is 1-Lipschitz on the integer line.

Let

`H_X=max_{0<=t<=X}|M(t)|`

and choose `t_0` attaining this maximum. Since `M(0)=0` and increments have magnitude at most one, `H_X<=t_0`. For every integer

`t_0-floor(H_X/2)<=t<=t_0`,

we have

`|M(t)|>=H_X/2`.

Therefore, up to an absolute harmless rounding constant,

`(1/X)sum_{t<=X}|M(t)|^p >= H_X^(p+1)/(2^(p+1)X)`.

Hence the exact-scale moment-to-sup inequality

`H_X <= 2 X^(1/(p+1)) F_p(X)^(p/(p+1))`

(up to an absolute rounding adjustment that is irrelevant asymptotically).

Freeze:

`MOBIUS_FLUX_LP_TO_LINFINITY_LOSS = X^(1/[2(p+1)]) AT SQRT-MEAN SCALE`.

---

## 2. Fixed-p exponent ladder

Suppose for one fixed p that the natural square-root average bound holds:

`F_p(X) <= X^(1/2+o(1))`.

Then

`H_X <= X^[1/2+1/(2(p+1))+o(1)]`.

Examples:

- `p=1` gives exponent `3/4`;
- `p=2` gives `2/3`;
- `p=4` gives `3/5`;
- `p=6` gives `4/7`.

Thus every fixed moment remains strictly weaker than RH at its natural average scale.

This corrects any temptation to treat W1 as special: it is simply the first rung of an Lp ladder.

---

## 3. Growing-p positive-moment RH criterion

Let `p(X)>=1` be any real/integer function with

`p(X)->infinity`.

Then the following are equivalent in exponent form:

1. RH;
2. there exists such an unbounded `p(X)` for which

`F_{p(X)}(X) <= X^(1/2+o(1))`.

Proof:

- RH gives `H_X<=X^(1/2+o(1))`, hence every normalized Lp moment is at most that same supremum.
- Conversely the moment-to-sup inequality gives

`H_X <= X^[1/2+1/(2(p(X)+1))+o(1)] = X^(1/2+o(1))`

because `p(X)->infinity`. This is the Mertens RH criterion.

Thus one may choose `p(X)` to tend to infinity arbitrarily slowly.

Freeze:

`RH = GROWING_ORDER_SQRT_SCALE_CUMULATIVE_FLUX_MOMENTS`.

This is a reformulation, not a proof.

---

## 4. Even moments are strictly positive observables

Take `p=2q`, `q>=1` integer, and define

`E_q(X)=(1/X)sum_{t<=X} M(t)^(2q) >=0`.

Then

`F_{2q}(X)=E_q(X)^(1/(2q))`.

The fixed-q pointwise consequence is

`H_X <= X^[(q+1)/(2q+1)+o(1)]`

whenever `E_q(X)^(1/(2q))<=X^(1/2+o(1))`.

For `q->infinity`, `(q+1)/(2q+1)->1/2`.

Thus RH admits a fully positive final observer:

`RH <=> exists q(X)->infinity with E_q(X)^(1/(2q))<=X^(1/2+o(1))`.

The Möbius signs remain inside the cumulative flux, but the final readout is a nonnegative even moment.

---

## 5. Exact q-copy Gram representation

For a q-tuple

`nvec=(n_1,...,n_q) in {1,...,X}^q`,

define

`a(nvec)=prod_i mu(n_i)`,

`r(nvec)=max_i n_i`,

and the activation feature on cut position t

`phi_nvec(t)=1[r(nvec)<=t]`.

Then exactly

`M(t)^q=sum_nvec a(nvec) phi_nvec(t)`.

Therefore

`sum_{t<=X}M(t)^(2q)`
`=sum_{nvec,mvec} a(nvec)a(mvec) K_X(nvec,mvec)`,

where

`K_X(nvec,mvec)`
`=sum_{t<=X}phi_nvec(t)phi_mvec(t)`
`=X-max(r(nvec),r(mvec))+1`.

This kernel is positive semidefinite because it is explicitly a Gram kernel of the activation vectors `phi_nvec`.

After reversing the coordinate

`u=X-r+1`,

it is the classical Brownian covariance kernel

`min(u,v)`.

Freeze project interface:

`MOBIUS_CUT_FLUX_Q_REPLICA_GRAM`.

No new physical dimension is introduced. The q copies are replica/observer provenance, not X6 spatial axes and not factor-provenance depth.

---

## 6. Exact collapse by activation time

If q-tuples are collapsed only for this declared future operation by their activation time r, their signed coefficient is

`c_q(r)=sum_{max(nvec)=r}prod_i mu(n_i)`
`=M(r)^q-M(r-1)^q`.

Hence

`sum_t M(t)^(2q)=c_q^T K_X c_q`.

This collapse is operation-safe for the stated cumulative-flux Gram observer, but not a universal replacement for prime/integer provenance in other arithmetic operations.

BRC typing:

`ACTIVATION-TIME QUOTIENT = OBSERVER-SPECIFIC`,

not

`GLOBAL ARITHMETIC IDENTITY QUOTIENT`.

---

## 7. Three distinct notions of growing depth

The current RH branch now contains three asymptotically different depth parameters:

1. **X6 width**: fixed at 6 by P000.
2. **factor/ordered-prime provenance depth**: for single Riesz primitive-source resolution, critical scale is roughly `(1/2)log N/loglog N`; factor-only pair-collision resolution can require roughly `log N/loglog N`.
3. **Renyi/replica moment order**: for the cumulative-flux RH reformulation, only `q(X)->infinity` is required, arbitrarily slowly.

Freeze:

`REPLICA_DEPTH != FACTOR_PROVENANCE_DEPTH != X6_DIMENSION`.

Conflating these scales creates false complexity conclusions.

---

## 8. Zero-frequency obstruction

The q=1 energy is

`sum_{t<=X}M(t)^2`.

As a quadratic form it is the image of the Möbius sequence under the inverse discrete-difference/integration operator. In additive Fourier language, inversion of a first difference has multiplier comparable to

`1/(1-e^{-i theta})`,

which is singular at `theta=0`.

Thus global Parseval control of the Möbius Fourier polynomial does not automatically control cumulative-flux energy; the low/zero-frequency mode is amplified.

This is consistent with the current frontier:

- strong short-interval/local uniformity controls increments of M;
- it does not by itself control the global DC level of M;
- any route to a fixed-p square-root flux moment must supply new low-frequency arithmetic information.

Do not identify local Möbius uniformity with the natural bound for `E_q(X)` without a quantitative integration theorem.

---

## 9. Prior-art boundary

Verjovsky, `Local Moments of Möbius Fourier Polynomials and the Riemann Hypothesis`, arXiv:2607.25002 (2026), proves an RH-equivalent high-local-moment criterion for normalized Möbius Fourier polynomials and a moment-to-point-value inequality. The present cumulative-flux moment ladder is a discrete integer-line analogue with a different positive Gram kernel. It should be presented as a project organization/reformulation unless a distinct literature audit supports a stronger novelty claim.

---

## 10. Next concrete target

The first nontrivial rung is q=1:

`E_1(X)=(1/X)sum_{t<=X}M(t)^2`.

A bound

`E_1(X)^(1/2)<=X^(1/2+o(1))`

would imply

`M(X)<=X^(2/3+o(1))`,

a genuine fixed-power improvement far beyond current unconditional Mertens bounds.

Therefore q=1 is already a serious arithmetic target. Any claimed proof must be audited for hidden use of RH-strength low-frequency control.
