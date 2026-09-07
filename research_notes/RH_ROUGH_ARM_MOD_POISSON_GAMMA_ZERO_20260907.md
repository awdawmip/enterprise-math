# RH rough-arm mod-Poisson law, Gamma zero, and all-cumulant endpoint barrier

Status: `RESEARCH FRONTIER / EXACT PROBABILITY LAW + MOD-POISSON PROFILE + FIXED-CUMULANT NO-GO / NOT A PROOF OF RH`
Date: `2026-09-07`
Project: `Enterprise Math / 进取数论`
Scope: `RH / generalized Dickman carrier / rough-arm Factor-BRC / factorial cumulants / Gamma zero / endpoint reconstruction`
Parent frontier:

- `RH_PARITY_ENDPOINT_ONE_ARM_INSTABILITY_20260907.md`
- `RH_CONTINUUM_DICKMAN_GAMMA_COUNTERTERM_20260907.md`
- `RH_HYPERBOLA_COUNTERTERM_TOWER_20260907.md`

Tool-reuse resolution: `EXTEND_EXISTING_TOOL`.

The existing generalized Dickman rough-layer carrier is extended by its exact probability, factorial-moment, and Gamma-residue structure. No new top-level BRC family is introduced.

P000 is unchanged. Rough-arm number is arithmetic serial provenance depth, not native spatial dimension.

BRC discipline:

`PROVENANCE > MULTIPLICITY > BOOLEAN SUPPORT`.

---

## 0. Starting point

The parent note proved the exact positive expansion

\[
G_u(\varepsilon)
:=R_{1-\varepsilon}(u)
=\sum_{h=0}^{\lfloor u\rfloor}P_h(u)\varepsilon^h,
\]

where

\[
P_h(u)=\frac1{h!}(\rho*k^{*h})(u),
\qquad
k(x)=\frac{\mathbf1_{x\ge1}}x,
\]

and

\[
P_h(u)\ge0,
\qquad
\sum_hP_h(u)=1.
\]

Hence there is an exact integer-valued random variable `H_u` such that

\[
\mathbb P(H_u=h)=P_h(u),
\qquad
G_u(\varepsilon)=\mathbb E[\varepsilon^{H_u}].
\]

The event `H_u=0` has probability

\[
\mathbb P(H_u=0)=P_0(u)=\rho(u).
\]

The present note identifies the bulk law of `H_u` and explains why this zero-arm event is invisible to every fixed truncation of the limiting cumulant tower.

---

## 1. Exact factorial-moment carrier

For `m>=0`, differentiate the probability generating function at `epsilon=1`:

\[
\mathbb E[(H_u)_m]
=G_u^{(m)}(1),
\]

where `(h)_m=h(h-1)...(h-m+1)`.

The Laplace transform of `G_u` is

\[
\widehat G_\varepsilon(s)
=\frac{e^{-(1-\varepsilon)E_1(s)}}s.
\]

Therefore

\[
\mathcal L_u\{\mathbb E[(H_u)_m]\}(s)
=\frac{E_1(s)^m}s.
\]

Since `E_1` is the Laplace transform of `k`, inversion gives the exact positive simplex volume

\[
\boxed{
\mathbb E[(H_u)_m]
=
\int_{\substack{x_1,\ldots,x_m\ge1\\x_1+\cdots+x_m\le u}}
\frac{dx_1\cdots dx_m}{x_1\cdots x_m}.
}
\]

Equivalently,

\[
\boxed{
\mathbb E\binom{H_u}{m}
=
\frac1{m!}
\int_{\substack{x_i\ge1\\\sum x_i\le u}}
\prod_{i=1}^m\frac{dx_i}{x_i}.
}
\]

This is the exact positive rough-face BRC carrier before the final parity observer. Each factorial moment counts an unordered selection of `m` distinct rough-log arms subject to the product-budget simplex.

---

## 2. Exact mean

For `m=1`,

\[
\mathbb E H_u
=\int_1^u\frac{dx}{x}.
\]

Thus, for every `u>=1`, not merely asymptotically,

\[
\boxed{
\mathbb E H_u=\log u.
}
\]

This identifies the product-budget depth found in the hyperbola-counterterm tower:

\[
L_X=\log u_X
\]

is exactly the mean number of positive continuum rough arms.

At the RH cutoff

\[
u_X=\frac{\log X}{2\log\log X}+O(1),
\]

we have

\[
\mathbb E H_{u_X}
=\log\log X-\log(2\log\log X)+o(1).
\]

Hence the typical positive rough-arm depth is `Theta(loglog X)`, whereas the maximal/critical provenance depth is

\[
K_X\asymp\frac{\log X}{\log\log X}.
\]

These are rigorously different geometric scales:

- bulk positive-arm depth: `log u ~ loglog X`;
- extreme Factor-BRC support depth: `u ~ log X/loglog X`.

---

## 3. Exact second factorial moment and variance

For `u>=2`,

\[
\mathbb E[(H_u)_2]
=\int_1^{u-1}\frac{\log(u-x)}x\,dx.
\]

With the dilogarithm `Li_2`, this is exactly

\[
\boxed{
\mathbb E[(H_u)_2]
=
\log u\log(u-1)
-\operatorname{Li}_2(1-1/u)
+\operatorname{Li}_2(1/u).
}
\]

Consequently

\[
\mathbb E[(H_u)_2]
=(\log u)^2-\frac{\pi^2}{6}
+O\left(\frac{\log u}{u}\right),
\]

and, using the exact mean,

\[
\boxed{
\operatorname{Var}(H_u)
=
\log u-\frac{\pi^2}{6}
+O\left(\frac{\log u}{u}\right).
}
\]

Thus the rough-arm count is Poisson-like at leading order but has a definite negative variance correction. This correction is not a numerical artifact; it is the second member of the Gamma/zeta cumulant tower below.

---

## 4. Mod-Poisson profile

For fixed real `epsilon>0`, the small-`s` expansion

\[
E_1(s)=-\gamma-\log s+O(s)
\]

gives

\[
\widehat G_\varepsilon(s)
=e^{\gamma(1-\varepsilon)}s^{-\varepsilon}
(1+O_\varepsilon(s)).
\]

Laplace inversion yields, locally uniformly for `epsilon` in compact subsets of `(0,infinity)`,

\[
\boxed{
G_u(\varepsilon)
\sim
u^{\varepsilon-1}
\Psi(\varepsilon),
\qquad
\Psi(\varepsilon)
=
\frac{e^{\gamma(1-\varepsilon)}}{\Gamma(\varepsilon)}.
}
\]

Since

\[
u^{\varepsilon-1}
=\exp((\varepsilon-1)\log u)
\]

is the probability generating function of a Poisson variable of mean `log u`, the family `H_u` has a mod-Poisson profile with limiting residue `Psi`.

This recovers the exact mean and the leading variance. More importantly, it isolates the non-Poisson information in one Gamma residue.

Freeze:

`ROUGH_ARM_BULK = POISSON(log u) x GAMMA_RESIDUE`.

This is a continuum probability statement, not a discrete Mertens estimate.

---

## 5. Limiting factorial cumulants

Put

\[
\varepsilon=1+s.
\]

For `|s|<1`, the classical expansion

\[
\log\Gamma(1+s)
=-\gamma s
+\sum_{m\ge2}\frac{(-1)^m\zeta(m)}m s^m
\]

gives

\[
\boxed{
\log G_u(1+s)
=s\log u
-\sum_{m\ge2}
\frac{(-1)^m\zeta(m)}m s^m
+o(1).
}
\]

Hence the limiting factorial cumulants are

\[
\boxed{
\kappa^{(F)}_1(H_u)=\log u
}
\]

exactly, and for every fixed `m>=2`,

\[
\boxed{
\kappa^{(F)}_m(H_u)
\longrightarrow
(-1)^{m+1}(m-1)!\zeta(m).
}
\]

For `m=2`,

\[
\kappa^{(F)}_2\to-\zeta(2),
\]

so

\[
\operatorname{Var}(H_u)
=\mathbb EH_u+\kappa^{(F)}_2
=\log u-\pi^2/6+o(1),
\]

in agreement with the direct dilogarithm calculation.

---

## 6. The Gamma zero is an all-cumulant effect

The exact parity endpoint corresponds to

\[
\varepsilon=0,
\qquad s=-1.
\]

The limiting residue satisfies

\[
\Psi(0)=\frac{e^\gamma}{\Gamma(0)}=0.
\]

In the cumulant expansion this zero is produced by

\[
\log\Psi(0)
=-\sum_{m=2}^{\infty}\frac{\zeta(m)}m
=-\infty.
\]

Thus no finite set of limiting factorial cumulants creates the zero. Every finite truncation leaves a positive residue.

Let

\[
S_M=\sum_{m=2}^{M}\frac{\zeta(m)}m.
\]

Split `zeta(m)=1+(zeta(m)-1)`. Then

\[
S_M
=H_M-1
+\sum_{m=2}^{M}\frac{\zeta(m)-1}{m}.
\]

Moreover,

\[
\sum_{m=2}^{\infty}\frac{\zeta(m)-1}{m}
=\sum_{n=2}^{\infty}
\left[-\log(1-1/n)-1/n\right]
=1-\gamma.
\]

Since

\[
H_M=\log M+\gamma+o(1),
\]

we obtain

\[
\boxed{
S_M=\log M+o(1),
\qquad
e^{-S_M}\sim\frac1M.
}
\]

Therefore the order-`M` truncation of the limiting Gamma-log cumulant series, evaluated at the parity endpoint, predicts an algebraic residue of size

\[
\boxed{
G_{u,M}^{\rm cumulant}(0)
\asymp\frac1{Mu},
}
\]

whereas the true endpoint mass is

\[
G_u(0)=\rho(u),
\]

which is super-polynomially smaller in `u`.

Freeze:

`GAMMA_ZERO = COLLECTIVE_ALL_CUMULANT_DIVERGENCE`.

---

## 7. Fixed-cumulant endpoint no-go

The preceding statement has a precise scope. It concerns the route that:

1. takes the limiting mod-Poisson/Gamma log residue;
2. retains only cumulants through order `M`;
3. evaluates that truncated log series at `s=-1`.

Within this route, matching the true zero-arm probability requires at least

\[
\frac1{Mu}\lesssim\rho(u),
\]

hence

\[
\boxed{
M\gtrsim\frac1{u\rho(u)}.
}
\]

At the RH critical depth,

\[
u=u_X=\frac{\log X}{2\log\log X}+O(1),
\qquad
u\rho(u)=X^{-1/2+o(1)},
\]

so the cumulant truncation order would have to satisfy

\[
\boxed{
M\ge X^{1/2-o(1)}.
}
\]

This is not asserted as a lower bound for every conceivable analytic continuation, interpolation, or exact finite polynomial method. It is a no-go for the declared **fixed-order limiting cumulant/Gamma-log truncation**.

In particular, the fixed-order counterterm tower cannot be extrapolated to the exact parity endpoint by merely taking more but boundedly many derivatives. The endpoint zero is generated collectively by all orders.

---

## 8. BRC interpretation

The probability law separates three information scales.

### Positive bulk

`H_u` typically has about `log u` rough arms. Its fixed factorial moments and cumulants are stable, positive-carrier observables.

### Exact zero-arm face

`H_u=0` is the Dickman event with probability `rho(u)`. At RH depth this is `X^(-1/2+o(1))`, far smaller than bulk probabilities.

### Observer singularity

The passage from the positive PGF near `epsilon=1` to the exact coefficient at `epsilon=0` is not controlled by any fixed cumulant order. The Gamma zero is a collective endpoint observer effect.

This is a direct instance of the project rule:

`FINITE_MOMENT_OR_JET_DATA != EXACT_RARE_FACE_COEFFICIENT`.

X6 may display a bounded number of local rough arms. The typical arm count already grows like `loglog X`, and the exact zero-arm event depends on the whole serial provenance distribution. No increase of spatial dimension is implied.

---

## 9. Relation to earlier depth scales

The present law unifies but does not conflate the earlier depths:

1. `log u ~ loglog X`: mean positive rough-arm depth and hyperbola-counterterm tower depth;
2. `u ~ log X/loglog X`: maximal/critical product-budget provenance depth;
3. `1/(u rho(u))=X^(1/2-o(1))`: condition/cumulant order required by the naive limiting-log truncation at the exact parity endpoint.

The third quantity is not a physical path depth. It is an observer-reconstruction complexity for one specific truncated-cumulant method.

Freeze:

`BULK_DEPTH != MAXIMAL_PROVENANCE_DEPTH != ENDPOINT_CUMULANT_RECONSTRUCTION_ORDER`.

---

## 10. Exact checker

Task-local checker:

`experiments/rh_rough_arm_mod_poisson_check.py`.

It integrates the exact rough-layer delay system and checks/prints:

- probability normalization;
- the exact mean `log u`;
- the exact second-factorial-moment dilogarithm formula;
- the variance correction `-pi^2/6`;
- fixed-`epsilon` mod-Poisson diagnostics;
- `M exp(-sum_(m=2)^M zeta(m)/m) -> 1`.

The checker is diagnostic only. The probability, moment, and cumulant identities are analytic derivations, not numerical claims.

---

## 11. Prior-art boundary

Generalized Dickman convolution powers, Gamma asymptotics, and mod-Poisson language belong to classical probability/analytic number theory. The project-specific contribution claimed here is limited to the typed composition with the current rough-arm Factor-BRC route, the exact identification of the three depth/observer scales, and the fixed-cumulant parity-endpoint no-go.

No generic novelty claim is made before a dedicated literature audit.

---

## 12. New smallest research unit

The positive continuum layer is now structurally understood:

- typical depth is `log u`;
- the parity endpoint is a rare zero-arm face;
- the Gamma zero is all-cumulant;
- fixed-order limiting jets cannot recover it.

Accordingly, the remaining RH route must not infer the endpoint from a fixed positive-moment hierarchy. It must retain the exact signed finite discrete carrier and estimate its final coefficient/observer directly.

The current smallest object remains the signed prime-rooted front block

\[
\mathcal R_{<K}(X,t)
=t\sum_{r=0}^{K-2}(-t)^r
\mathcal L_{X,Y,\sqrt\cdot}(\mathcal K^rQ),
\]

but the present result adds a guard: any attempt to replace this finite signed object by a fixed-order continuum cumulant closure is non-operation-safe at the parity endpoint.

The next admissible step is an exact prime-scale adjoint summation-by-parts formula with the cumulative quadrature discrepancy and all boundary terms retained.

No RH proof is claimed.
