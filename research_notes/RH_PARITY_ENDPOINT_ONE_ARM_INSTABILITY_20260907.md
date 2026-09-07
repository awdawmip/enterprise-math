# RH parity endpoint, one-rough-arm leakage, and positive-regularization no-go

Status: `RESEARCH FRONTIER / EXACT POSITIVE LAYER DECOMPOSITION + ENDPOINT CONDITION NUMBER + CRITICAL RESOLUTION LOWER BOUND / NOT A PROOF OF RH`
Date: `2026-09-07`
Project: `Enterprise Math / 进取数论`
Scope: `RH / generalized Dickman carrier / rough-depth Factor-BRC / parity endpoint / positive approximation barrier`
Parent frontier:

- `RH_CONTINUUM_DICKMAN_GAMMA_COUNTERTERM_20260907.md`
- `RH_HARMONIC_ROUGH_TRANSFER_DUHAMEL_REPAIR_20260907.md`
- `RH_ROOTED_FACTORIAL_DEPTH_SHARPNESS_20260907.md`
- `RH_ADJOINT_ROOTED_RESOLVENT_EDGE_ENERGY_20260907.md`

Tool-reuse resolution: `EXTEND_EXISTING_TOOL`.

This note extends the existing generalized Dickman/harmonic rough-state carrier by resolving it into positive rough-arity layers around the exact parity endpoint. No new top-level BRC family is introduced.

P000 is unchanged. The layer index counts arithmetic rough-prime arms in a product-budget relation fiber; it is not a new native X6 spatial dimension.

BRC discipline:

`PROVENANCE > MULTIPLICITY > BOOLEAN SUPPORT`.

The key boundary is:

`POSITIVE_REGULARIZATION_NEAR_PARITY_ENDPOINT != SAFE_RH_APPROXIMATION`.

---

## 0. Question

The continuum generalized Dickman carrier is

\[
\widehat R_t(s)
=\int_0^\infty e^{-su}R_t(u)\,du
=\frac{e^{-tE_1(s)}}s,
\]

where

\[
E_1(s)=\int_1^\infty \frac{e^{-sx}}x\,dx.
\]

At `t=1`,

\[
R_1(u)=\rho(u),
\]

the ordinary Dickman function. This is the continuum rough-parity endpoint: all positive rough-arity layers cancel except the zero-rough-arm sector.

A natural idea is to approach this endpoint from the positive side by taking

\[
t=1-\varepsilon,
\qquad 0<\varepsilon\ll1.
\]

The question is whether a merely logarithmically small `epsilon` can approximate the parity endpoint at the RH square-root scale.

The answer is no. The first positive leakage channel is already much larger than `rho(u)`.

---

## 1. Exact positive rough-layer decomposition

Put

\[
k(u)=\frac{\mathbf 1_{u\ge1}}u.
\]

Its Laplace transform is

\[
\widehat k(s)=E_1(s).
\]

Since

\[
\widehat\rho(s)=\frac{e^{-E_1(s)}}s,
\]

we have, exactly,

\[
\frac{e^{-(1-\varepsilon)E_1(s)}}s
=
\widehat\rho(s)
\sum_{h\ge0}\frac{\varepsilon^hE_1(s)^h}{h!}.
\]

Define

\[
\boxed{
P_h(u)=\frac1{h!}(\rho*k^{*h})(u),
\qquad h\ge0,
}
\]

with `k^{*0}` the identity mass. Then

\[
\boxed{
R_{1-\varepsilon}(u)
=\sum_{h=0}^{\lfloor u\rfloor}
\varepsilon^hP_h(u).
}
\]

The sum is finite because every rough-log coordinate carried by `k` is at least `1`.

Every coefficient is nonnegative:

\[
P_h(u)\ge0.
\]

At `epsilon=1`, `t=0` and `R_0(u)=1`, so

\[
\boxed{
\sum_{h=0}^{\lfloor u\rfloor}P_h(u)=1.
}
\]

Thus `(P_h(u))_h` is an exact positive probability distribution on continuum rough-arm number, and

\[
R_{1-\varepsilon}(u)
=\mathbb E_u[\varepsilon^{H_u}]
\]

is its probability generating function.

The exact parity endpoint `epsilon=0` selects only

\[
P_0(u)=\rho(u).
\]

Any positive displacement from the endpoint admits the one-arm layer immediately.

Freeze:

`PARITY_ENDPOINT = ZERO_ROUGH_ARM_FACE_OF_POSITIVE_LAYER_SIMPLEX`.

---

## 2. Exact delay system for the layers

The generalized Dickman equation is

\[
uR_t'(u)=-tR_t(u-1),
\qquad u>1,
\]

with `R_t(u)=1` on `0<=u<=1`.

Substituting the positive layer expansion and comparing powers of `epsilon` gives

\[
\boxed{
uP_0'(u)=-P_0(u-1),}
\]

and, for `h>=1`,

\[
\boxed{
uP_h'(u)
=-P_h(u-1)+P_{h-1}(u-1).}
\]

The initial data are

\[
P_0(u)=1,
\qquad
P_h(u)=0\quad(h\ge1),
\qquad 0\le u\le1.
\]

On the first nontrivial interval `1<=u<=2`, this gives exactly

\[
\boxed{
P_0(u)=1-\log u,
\qquad
P_1(u)=\log u,
\qquad
P_h(u)=0\ (h\ge2).
}
\]

The delay system is a positive BRC transport law: mass leaves the `h` layer and is injected from the preceding layer when one additional rough arm becomes available.

---

## 3. The one-rough-arm layer

The first leakage coefficient has the explicit convolution form

\[
\boxed{
P_1(u)
=\int_1^u\frac{\rho(u-v)}v\,dv
=\int_0^{u-1}\frac{\rho(w)}{u-w}\,dw.
}
\]

The Dickman mass follows directly from its Laplace transform. Since

\[
E_1(s)=-\gamma-\log s+s+O(s^2),
\]

we have

\[
\int_0^\infty\rho(w)\,dw
=\lim_{s\downarrow0}\frac{e^{-E_1(s)}}s
=e^\gamma.
\]

The same expansion gives a finite first moment. Splitting the integral at `w=u/2`, expanding `(u-w)^{-1}` on the first part, and using the super-polynomial Dickman tail on the second part yields

\[
\boxed{
P_1(u)=\frac{e^\gamma}{u}+O\left(\frac1{u^2}\right).
}
\]

Geometric meaning:

- `P_0`: a completely `Y`-smooth core, with no rough prime arm;
- `P_1`: one rough prime label attached to an arbitrary smooth core;
- `P_h`: `h` distinct rough prime arms attached to the smooth core, after symmetric ordering is quotiented only at the final continuum observer.

The one-arm layer is semiprime-like relative to the cutoff, but it is not literally the set of semiprimes: the smooth core may itself contain many small prime factors.

---

## 4. Positive leakage inequality

For every real `0<=epsilon<=1`, positivity gives the exact lower bound

\[
\boxed{
R_{1-\varepsilon}(u)-\rho(u)
=\sum_{h\ge1}\varepsilon^hP_h(u)
\ge\varepsilon P_1(u).
}
\]

Therefore

\[
\boxed{
R_{1-\varepsilon}(u)-\rho(u)
\ge
\left(e^\gamma+o(1)\right)
\frac\varepsilon u.
}
\]

This is a one-layer obstruction. It does not use the high-arity tail, prime discrepancy, or any cancellation estimate.

Suppose, for some fixed `C>1`, one wants a positive regularization satisfying

\[
R_{1-\varepsilon}(u)\le C\rho(u).
\]

Then necessarily

\[
\boxed{
\varepsilon
\le
(C-1)\frac{\rho(u)}{P_1(u)}
=
\left(\frac{C-1}{e^\gamma}+o(1)\right)
u\rho(u).
}
\]

Thus the true endpoint resolution scale is not `1/log u`; it is at most

\[
\boxed{\varepsilon_{\rm parity}(u)\asymp u\rho(u).}
\]

---

## 5. Parity endpoint condition number

Define the relative endpoint condition number

\[
\boxed{
\kappa_{\rm par}(u)
=
\left.
\frac{\partial}{\partial\varepsilon}
\log R_{1-\varepsilon}(u)
\right|_{\varepsilon=0}
=
\frac{P_1(u)}{\rho(u)}.
}
\]

Using the one-arm asymptotic,

\[
\boxed{
\kappa_{\rm par}(u)
\sim
\frac{e^\gamma}{u\rho(u)}.
}
\]

Hence the parity endpoint is exponentially ill-conditioned in the Dickman depth variable: an extremely small positive admixture changes the value by a large relative factor.

This is a precise BRC observer statement. The positive layer carrier is stable, but the final observer selecting `h=0` is not stable under positive endpoint displacement.

Freeze:

`POSITIVE_LAYER_STABILITY != PARITY_ENDPOINT_STABILITY`.

---

## 6. RH-critical consequence

Use the critical depth

\[
Y=(\log X)^2,
\qquad
u_X=\frac{\log X}{\log Y}
=\frac{\log X}{2\log\log X}+O(1).
\]

The classical Dickman asymptotic gives

\[
\rho(u_X)=X^{-1/2+o(1)}.
\]

Since `u_X=X^{o(1)}`,

\[
\boxed{
u_X\rho(u_X)=X^{-1/2+o(1)}.}
\]

Therefore any positive regularization that remains comparable with the parity endpoint at the RH scale must satisfy

\[
\boxed{
\varepsilon
\le X^{-1/2+o(1)}.
}
\]

In particular,

\[
\varepsilon\asymp\frac1{\log u_X}
\]

is enormously too large. Its one-arm leakage alone is

\[
\asymp\frac1{u_X\log u_X},
\]

which is only logarithmically small and dominates `rho(u_X)=X^{-1/2+o(1)}` by a power-scale factor.

This rules out a broad class of proposed positive approximations:

> one cannot prove the RH-scale parity statement by evaluating the positive generalized Dickman carrier at a polylogarithmic distance from `t=1` and then passing continuously to the endpoint.

The exact signed endpoint must remain in the state, or the endpoint displacement must already be controlled at essentially the desired square-root precision.

---

## 7. Fixed-layer asymptotics

For each fixed `h>=1`, the `h`-fold rough kernel satisfies

\[
k^{*h}(u)
\sim
\frac{h(\log u)^{h-1}}u.
\]

The geometric reason is the same hyperbola-shell mechanism found in the counterterm tower: one logarithmic coordinate carries the macroscopic remainder, while the other `h-1` coordinates supply independent logarithmic volume; there are `h` choices for the macroscopic coordinate.

Convolution with the integrable Dickman core of mass `e^gamma` gives

\[
\boxed{
P_h(u)
\sim
\frac{e^\gamma}{(h-1)!}
\frac{(\log u)^{h-1}}u
\qquad(h\text{ fixed}).
}
\]

Thus the one-arm theorem is the first member of an entire positive leakage hierarchy.

---

## 8. The natural positive boundary layer

Let

\[
\varepsilon=\frac\tau{\log u},
\qquad 0\le\tau\le T,
\]

with `T` fixed. The fixed-layer asymptotics suggest a nontrivial positive boundary profile rather than convergence to the parity endpoint.

A uniform convolution majorant follows inductively from

\[
k^{*h}(v)
\ll
\frac{h2^{h-1}(1+\log v)^{h-1}}v,
\]

combined with the integrability and super-polynomial tail of `rho`. It permits dominated summation of the positive layer series on compact `tau`-intervals. Consequently

\[
\boxed{
\nu\log u\,
\bigl(R_{1-\tau/\log u}(u)-\rho(u)\bigr)
\longrightarrow
 e^\gamma\tau e^\tau
}
\]

uniformly for `tau` in compact subsets of `[0,infinity)`.

Equivalently,

\[
R_{1-\tau/\log u}(u)
=
\rho(u)
+
\frac{e^\gamma\tau e^\tau}{u\log u}
+o_T\left(\frac1{u\log u}\right).
\]

This is the positive `t->1` boundary layer. It is distinct from the `t->0` hyperbola-counterterm boundary layer found in the parent note.

The profile also agrees with the Gamma-Dickman amplitude:

\[
\frac{e^{\gamma t}}{\Gamma(1-t)}u^{-t},
\qquad
t=1-\frac\tau{\log u},
\]

because

\[
\Gamma\left(\frac\tau{\log u}\right)^{-1}
\sim\frac\tau{\log u}
\]

and

\[
u^{\tau/\log u}=e^\tau.
\]

The layer proof supplies the endpoint-uniform interpretation that a fixed-`t` asymptotic alone would not justify.

---

## 9. Relation to primes, semiprimes, and higher-factor composites

The positive layer decomposition gives a cutoff-relative geometric hierarchy:

\[
\boxed{
\text{smooth core}
\to
\text{one rough arm}
\to
\text{two rough arms}
\to\cdots
}
\]

- A prime above `Y` with trivial core lies in the one-arm layer.
- A product of one rough prime and one smooth prime is a literal semiprime within the one-arm layer.
- A product of two rough primes with trivial core lies in the two-arm layer.
- A composite with many smooth factors but one rough prime still has one rough arm: total factor depth and rough-arm depth are different coordinates.

This sharpens the original Factor-BRC geometry. The decisive RH endpoint does not suppress composites by total `Omega` alone; it selects the zero-rough-arm face relative to a moving cutoff. The first instability is caused by a single new labeled rough direction, not by a high-dimensional cloud.

X6 can display each local arm, while the serial path retains prime labels and the growing provenance depth. The layer index is not a seventh axis.

---

## 10. Exact checker

Task-local checker:

`experiments/rh_parity_endpoint_rough_layer_check.py`.

It numerically integrates the exact layer delay system and verifies:

- the closed formulas on `1<=u<=2`;
- nonnegativity of the computed layers;
- the exact positive leakage inequality;
- numerical approach of `uP_1(u)` to `e^gamma`;
- the `tau/log u` boundary-layer profile.

The checker is diagnostic only. The exact decomposition and one-arm lower bound are analytic identities; the asymptotic statements are established by the convolution arguments above, not by the finite computation.

---

## 11. Prior-art boundary

Generalized Dickman functions, their convolution powers, and their fixed-parameter asymptotics are classical. The project claim is narrower:

1. the exact positive rough-arm BRC resolution around the parity endpoint;
2. the identification of `P_1` as the first cutoff-relative prime/composite geometry leaking through a positive observer;
3. the endpoint condition number `P_1/rho`;
4. the resulting RH-critical positive-regularization lower bound;
5. the separation of the natural `1/log u` positive boundary layer from the much thinner `u rho(u)` parity-resolution window.

No generic novelty claim is made for generalized Dickman theory itself.

---

## 12. New smallest research unit

This result closes the proposed route

`NEARBY_POSITIVE_t<1_CARRIER -> CONTINUITY_TO_EXACT_PARITY_ENDPOINT`.

At RH depth the endpoint condition number is `X^(1/2-o(1))`, so the required positive-parameter accuracy is already square-root scale.

The remaining admissible route is exact and signed:

\[
\mathcal R_{<K}(X,t)
=t\sum_{r=0}^{K-2}(-t)^r
\mathcal L_{X,Y,\sqrt\cdot}(\mathcal K^rQ),
\]

with the actual quadrature source `Q` retained. The next theorem must exploit cancellation in the root/edge/quotient provenance itself; neither positive endpoint regularization nor absolute path capacity can provide it.

A useful next test is the exact derivative of the adjoint Green field with respect to the root-prime coordinate. If its terminal boundary term reproduces `J_(1/2)`, the edge transform is only a reformulation. If the cumulative prime discrepancy pairs only with a genuinely smaller edge variation after summing rooted depths, that would be the first source-specific gain beyond the current no-go results.

No RH proof is claimed.
