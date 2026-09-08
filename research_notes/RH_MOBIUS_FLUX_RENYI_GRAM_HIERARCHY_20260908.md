# RH Möbius cut-flux Lp / positive Gram hierarchy — Mellin-corrected

Status: `RESEARCH FRONTIER / EXACT RH-EQUIVALENT FAMILY + PRIOR-ART-ADJACENT / NOT A PROOF OF RH`
Date: `2026-09-08`
Project: `Enterprise Math / 进取数论`
Scope: `Mertens / transport flux / Lp moments / positive Gram replicas / Mellin continuation`

## 0. Correction

An earlier version of this note stated that a fixed flux moment at its natural square-root average scale was strictly weaker than RH and that the moment order had to tend to infinity to recover RH. That statement used only the generic 1-Lipschitz moment-to-sup inequality and omitted the Möbius Mellin identity.

Correct statement:

**for every fixed `p>=1`, the all-scale bound at the natural square-root Lp scale with arbitrary epsilon slack is already RH-equivalent.**

The fixed-p exponent ladder remains a correct generic metric consequence, but it is not the strongest arithmetic consequence for the Mertens function.

Freeze:

`GENERIC_MOMENT_TO_SUP_STRENGTH != MOBIUS_MELLIN_STRENGTH`.

---

## 1. Normalized cumulative-flux moments

Let

`M(t)=sum_{n<=t}mu(n)`

and for fixed `p>=1` define

`F_p(X)=[(1/X)sum_{t<=X}|M(t)|^p]^(1/p)`.

RH implies, for every epsilon,

`F_p(X)<<_eps X^(1/2+eps)`.

Equivalently after epsilon renaming,

`sum_{t<=X}|M(t)|^p <<_eps X^(1+p/2+eps)`.

---

## 2. Fixed-p natural moment bound implies RH

Assume for one fixed `p>=1` that for every `eps>0`,

`S_p(X):=sum_{t<=X}|M(t)|^p <<_eps X^(1+p/2+eps)`.

Fix `sigma>1/2`.

### p=1

On a dyadic interval `[Y,2Y]`,

`int_Y^(2Y)|M(t)|t^(-sigma-1)dt`
`<=Y^(-sigma-1) S_1(2Y)`
`<<Y^(1/2-sigma+eps)`.

Choose `eps<sigma-1/2` and sum dyadically.

### p>1

Let `p'=p/(p-1)`. By Hölder,

`int_Y^(2Y)|M(t)|t^(-sigma-1)dt`
`<= [int_Y^(2Y)|M(t)|^p dt]^(1/p)`
`   [int_Y^(2Y)t^(-(sigma+1)p')dt]^(1/p')`.

The first factor is

`<<Y^(1/p+1/2+eps/p)`

and the second is

`asymp Y^(1/p'-sigma-1)`.

Since `1/p+1/p'=1`, the product is

`<<Y^(1/2-sigma+eps/p)`.

Choose `eps<p(sigma-1/2)` and sum over dyadic Y.

Thus for every `sigma>1/2`,

`int_1^infinity |M(t)|t^(-sigma-1)dt < infinity`.

The convergence is locally uniform on compact subsets of the half-plane. Therefore

`F(s)=s int_1^infinity M(t)t^(-s-1)dt`

is holomorphic for `Re(s)>1/2` and agrees with `1/zeta(s)` for `Re(s)>1`.

Hence zeta has no zeros in `Re(s)>1/2`; by the functional equation, RH follows.

Therefore, for **any one fixed p>=1**,

`RH <=> S_p(X)<<_eps X^(1+p/2+eps) for every eps>0`.

Equivalently,

`RH <=> F_p(X)<=X^(1/2+o(1))`.

Freeze:

`ANY_FIXED_FLUX_LP_NATURAL_SCALE_EPSILON_FAMILY = RH_EQUIVALENT`.

---

## 3. Generic metric pointwise ladder remains valid but is weaker

Because

`M(t)-M(t-1)=mu(t) in {-1,0,1}`,

M is 1-Lipschitz. If

`H_X=max_{t<=X}|M(t)|`,

then a peak of height H persists for `asymp H` sites at height `asymp H`, giving

`H_X <= C X^(1/(p+1))F_p(X)^(p/(p+1))`.

Thus the same natural Lp bound gives, **without using any arithmetic transform**,

`H_X<=X^[1/2+1/(2(p+1))+o(1)]`.

Examples:

- p=1 -> 3/4;
- p=2 -> 2/3;
- p=4 -> 3/5;
- p=6 -> 4/7.

These exponents describe only what follows for a generic 1-Lipschitz cumulative path. For the special Möbius path, the Mellin identity upgrades the same all-scale moment bound all the way to RH.

---

## 4. Even moments are positive final observables

For integer `q>=1`, take `p=2q` and define

`E_q(X)=(1/X)sum_{t<=X}M(t)^(2q)>=0`.

For every fixed q,

`RH <=> E_q(X)^(1/(2q))<=X^(1/2+o(1))`.

Thus **q=1 already suffices** in the arithmetic/Mellin sense:

`RH <=> sum_{t<=X}M(t)^2 <= X^(2+o(1))`.

Here `X^(2+o(1))` means the full epsilon family `O_eps(X^(2+eps))`.

A stronger uniform estimate `sum_{t<=X}M(t)^2=O(X^2)` implies the classical Weak Mertens Conjecture after dyadic decomposition:

`int_1^X (M(t)/t)^2dt=O(log X)`,

which is known to imply RH and additional zero-simplicity/negative-moment information. The `X^(2+o(1))` criterion is weaker and is used here only for RH.

---

## 5. Exact q-copy positive Gram representation

For a q-tuple

`nvec=(n_1,...,n_q) in {1,...,X}^q`,

define

`a(nvec)=prod_i mu(n_i)`,

`r(nvec)=max_i n_i`,

`phi_nvec(t)=1[r(nvec)<=t]`.

Then exactly

`M(t)^q=sum_nvec a(nvec)phi_nvec(t)`.

Therefore

`sum_{t<=X}M(t)^(2q)`
`=sum_{nvec,mvec}a(nvec)a(mvec)K_X(nvec,mvec)`,

where

`K_X(nvec,mvec)=X-max(r(nvec),r(mvec))+1`.

This is PSD because it is the Gram kernel of the activation features `phi_nvec`. Under the reverse coordinate `u=X-r+1`, it is the classical kernel `min(u,v)`.

Project interface:

`MOBIUS_CUT_FLUX_Q_REPLICA_GRAM`.

The q copies are replica/observer provenance, not X6 axes and not factor depth.

---

## 6. Observer-specific activation collapse

Collapsing q-tuples by activation time for this declared future operation gives

`c_q(r)=sum_{max(nvec)=r}prod_i mu(n_i)`
`=M(r)^q-M(r-1)^q`.

Hence

`sum_tM(t)^(2q)=c_q^T K_X c_q`.

This quotient is operation-safe only for the cumulative-flux Gram observer. It is not a universal arithmetic identity quotient.

---

## 7. Replica depth is not a required growing RH depth

The previous version incorrectly froze `q(X)->infinity` as necessary for RH. It is not.

Correct typing:

- X6 width: fixed at 6;
- factor/ordered-prime provenance depth: can grow like `log N/loglog N` for the previously declared primitive-source/collision observers;
- flux replica order q: **any fixed q>=1 is already RH-equivalent at its natural all-scale moment bound via Mellin continuation**.

One may still study growing q as a concentration hierarchy, but it is optional, not an RH-complexity requirement.

Freeze:

`REPLICA_ORDER != REQUIRED_RH_PROVENANCE_DEPTH`.

---

## 8. Zero-frequency meaning

The q=1 energy

`sum_{t<=X}M(t)^2`

is the squared L2 norm of the Möbius sequence after discrete integration. The inverse difference multiplier is singular at additive frequency zero. Hence ordinary Parseval/local short-interval uniformity does not automatically give the natural `X^(2+o(1))` bound.

The Mellin equivalence shows why this first positive Gram energy is already a hard target: proving its natural scale uniformly across all X would force a zero-free half-plane for zeta.

Thus q=1 is not a weaker fixed-power milestone once the full all-scale epsilon statement is requested; it is already RH-strength.

---

## 9. Prior-art boundary

- The Weak Mertens Conjecture and its consequences are classical; it is stronger than the present RH-only subpolynomial mean-square criterion.
- Verjovsky 2026 (arXiv:2607.25002) proves related local Fourier and Laplace Lp RH criteria and emphasizes moment-to-point-value mechanisms.
- The present note packages cumulative integer-line flux moments as finite PSD replica Gram energies and separates generic metric consequences from Möbius-specific Mellin consequences.

No novelty claim is made for the underlying analytic continuation principle.

---

## 10. Active target

The smallest positive Gram target can be taken at q=1:

`sum_{t<=X}M(t)^2 <= X^(2+o(1))`.

This is already RH-equivalent. Therefore future attempts to prove it must be audited as RH-strength and cannot be advertised as merely a `2/3` Mertens milestone.
