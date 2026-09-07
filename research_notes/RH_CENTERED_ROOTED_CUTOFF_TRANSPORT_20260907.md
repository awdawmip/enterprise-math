# RH centered prime-cutoff transport and rooted factor-face hierarchy

Status: `RESEARCH FRONTIER / EXACT SIGNED TRANSPORT IDENTITY + ENDPOINT UNIFICATION + FACTOR-FACE TOWER / NOT A PROOF OF RH`
Date: `2026-09-07`
Project: `Enterprise Math / 进取数论`
Researcher: `EM-RHHR-20260907`
Scope: `RH / prime-rooted Alladi transport / smooth numbers / prime intensity / Factor-BRC / signed measure`
Parents:

- `RH_PRIME_ROOTED_ALLADI_ROUGH_PHASE_TRANSPORT_20260907.md`
- `RH_BOUNDARY_PROFILE_CRITICAL_DEPTH_LAW_20260907.md`
- `RH_HARMONIC_ROUGH_TRANSFER_DUHAMEL_REPAIR_20260907.md`

## 0. Purpose and typing guard

The parent work leaves one RH-relevant object: the discrete-minus-continuum
prime-rooted source. This note packages it as one signed cutoff-transport
measure whose:

- `t=0` endpoint is the prime-incidence/intensity discrepancy;
- `t=1` endpoint is the largest-prime/smooth-number discrepancy;
- `t^r` coefficient is the discrepancy of rooted `r`-factor faces.

Thus primes, semiprimes and composites with more factors are not separate
ad hoc cases. They are consecutive coefficients of one provenance-preserving
transport family.

P000 remains unchanged. Prime roots, ordered factor arms and cutoff position
are arithmetic relation coordinates, not native X6 spatial dimensions.

BRC resolution:

```text
COMPOSE_APPLIED
POSITIVE_ROOTED_MEASURE -> SIGNED_DISCRETE_MINUS_CONTINUUM_MEASURE
PROVENANCE_RETAINED_UNTIL_FINAL_f_OBSERVER
```

No total-variation estimate is substituted for the signed functional.

---

## 1. Discrete and continuum rooted measures

For `0<t<=1`, recall

\[
\Phi_X(y;t)
=\frac1X\sum_{n\le X}(1-t)^{h_y(n)},
\qquad
h_y(n)=\#\{p\mid n:p>y\}.
\]

At a prime `q`, the exact cutoff jump is

\[
\Phi_X(q;t)-\Phi_X(q^-;t)
=t\frac{V_q}{X}\Phi(V_q,q;t),
\qquad
V_q=\left\lfloor\frac Xq\right\rfloor.
\]

Define the positive discrete rooted measure on `[2,Y]` by

\[
\boxed{
\mu_{X,t}
=\sum_{q\le Y}
\frac{V_q}{X}\Phi(V_q,q;t)\,\delta_q.
}
\]

Equivalently,

\[
d\mu_{X,t}=\frac1t\,d_q\Phi_X(y;t),
\]

where `d_q` is the prime-cutoff jump measure.

Let

\[
R_t(u)
\]

be the generalized Dickman carrier and put

\[
u_y=\frac{\log X}{\log y}.
\]

The continuum cutoff derivative is

\[
\frac{d}{dy}R_t(u_y)
=
\frac{t}{y\log y}R_t(u_y-1).
\]

Define the positive continuum rooted measure

\[
\boxed{
d\nu_{X,t}(y)
=\frac{R_t(u_y-1)}{y\log y}\,dy.
}
\]

Both measures use the same root label `y` and the same residual larger-factor
budget `u_y-1`.

---

## 2. Exact source and defect identities

For a prime test function `f` supported on `[2,Y]`, the exact averaged Alladi
source is

\[
\boxed{
F_{X,Y,f}(t)=-\int_{[2,Y]}f(y)\,d\mu_{X,t}(y).
}
\]

Its continuum counterpart is

\[
\boxed{
\mathcal F_{X,Y,f}^{\rm cont}(t)
=-\int_2^Y f(y)\,d\nu_{X,t}(y).
}
\]

Define the signed centered transport measure

\[
\boxed{
\sigma_{X,t}=\mu_{X,t}-\nu_{X,t}.
}
\]

Then the full centered rooted defect is exactly

\[
\boxed{
\mathcal D_{X,Y,f}(t)
:=F_{X,Y,f}(t)-\mathcal F_{X,Y,f}^{\rm cont}(t)
=-\int_{[2,Y]}f(y)\,d\sigma_{X,t}(y).
}
\]

This is the smallest current RH source carrier. No rough arity, root prime or
residual cutoff coordinate has been discarded.

---

## 3. Cumulative cutoff-phase discrepancy

Let

\[
K_{X,t}(y)=\sigma_{X,t}([2,y]).
\]

Using the discrete jump identity and the continuum derivative gives

\[
\boxed{
K_{X,t}(y)
=
\frac1t\left[
\Phi_X(y;t)-\Phi_X(2^-;t)
-R_t(u_y)+R_t(u_2)
\right].
}
\]

Here `2^-` means a cutoff immediately below the first prime. By construction,
`K` has zero left boundary at `2^-`.

For absolutely continuous `f`, Stieltjes integration by parts yields

\[
\boxed{
\mathcal D_{X,Y,f}(t)
=-f(Y)K_{X,t}(Y)
+
\int_2^Y f'(y)K_{X,t}(y)\,dy.
}
\]

Thus the RH source does not require small total variation of
`\sigma_{X,t}`. It requires cancellation in one signed cumulative transport
functional.

For the critical weight `f(y)=sqrt(y)`,

\[
\boxed{
\mathcal D_{X,Y,\sqrt{\cdot}}(t)
=-\sqrt Y\,K_{X,t}(Y)
+
\frac12\int_2^Y\frac{K_{X,t}(y)}{\sqrt y}\,dy.
}
\]

This boundary-minus-bulk structure is the exact negative-order observer to be
estimated. Taking absolute values of the two terms separately destroys their
possible cancellation.

Freeze:

```text
RH_ROOT_SOURCE = BOUNDARY_MINUS_BULK_CUTOFF_TRANSPORT
TOTAL_VARIATION_SMALLNESS_IS_NOT_REQUIRED_AND_IS_TOO_STRONG
```

---

## 4. The `t=0` endpoint: prime-intensity geometry

The measure family has a continuous limit at `t=0`. Since

\[
\Phi(V,q;0)=1,
\qquad
R_0(u)=1,
\]

we get

\[
\boxed{
\mu_{X,0}
=
\sum_{q\le Y}
\frac{\lfloor X/q\rfloor}{X}\,\delta_q,
}
\]

and

\[
\boxed{
d\nu_{X,0}(y)=\frac{dy}{y\log y}.}
\]

Therefore

\[
\boxed{
K_{X,0}(y)
=
\sum_{q\le y}
\frac{\lfloor X/q\rfloor}{X}
-
\log\frac{\log y}{\log2}.
}
\]

For `f(y)=sqrt(y)`, Section 3 recovers exactly the weighted prime-intensity
discrepancy, including the finite-population floor term.

The first geometric layer is therefore the rooted-vertex layer: one retained
prime root, with no larger selected factor arm.

---

## 5. The `t=1` endpoint: largest-prime/smooth geometry

At `t=1`,

\[
(1-t)^{h_y(n)}=\mathbf1_{\{P^+(n)\le y\}},
\]

with the unit counted by the usual empty-support convention. Hence

\[
\boxed{
\Phi_X(y;1)=\frac{\Psi(X,y)}X,
}
\]

where `Psi(X,y)` counts `y`-smooth integers up to `X`.

Also `R_1=\rho`, the Dickman function. Therefore

\[
\boxed{
K_{X,1}(y)
=
\frac{\Psi(X,y)-1}{X}
-
[\rho(u_y)-\rho(u_2)].
}
\]

Equivalently,

\[
\boxed{
\frac{\Psi(X,y)}X-\rho(u_y)
=K_{X,1}(y)+\frac1X-\rho(u_2).
}
\]

The correction on the right is the exact lower-cutoff anchor.

The discrete atom at a prime `q` is

\[
\mu_{X,1}(\{q\})
=
\frac1X\Psi(\lfloor X/q\rfloor,q),
\]

which counts integers whose largest distinct prime factor is exactly `q`.
Thus the same rooted measure that begins at prime incidence ends at the
largest-prime decomposition of smooth numbers.

Freeze:

```text
PRIME_INTENSITY_ENDPOINT_t0
AND
SMOOTH_NUMBER_ENDPOINT_t1
ARE_ONE_ROOTED_TRANSPORT_FAMILY
```

The known RH sensitivity of the smooth-number endpoint at the
`Y=(log X)^2` threshold is therefore attached to the same prime-root
provenance that carries the `t=0` source.

---

## 6. Exact rooted factor-face coefficient tower

For a root prime `q`, expand

\[
\Phi(V_q,q;t)
=
\sum_{r\ge0}(-t)^r
\frac1{V_q}
\sum_{m\le V_q}\binom{h_q(m)}r.
\]

Therefore

\[
\boxed{
[t^r]\,\mu_{X,t}(\{q\})
=
(-1)^r\frac1X
\sum_{m\le V_q}\binom{h_q(m)}r.
}
\]

Selecting the `r` larger prime arms explicitly gives the equivalent exact
formula

\[
\boxed{
\frac1X
\sum_{m\le V_q}\binom{h_q(m)}r
=
\frac1X
\sum_{q<p_1<\cdots<p_r}
\left\lfloor
\frac{X}{q p_1\cdots p_r}
\right\rfloor.
}
\]

On the continuum side, define

\[
I_r(v)
=
\int_{\substack{x_i\ge1\\x_1+\cdots+x_r\le v}}
\frac{dx_1\cdots dx_r}{x_1\cdots x_r},
\qquad I_0(v)=1.
\]

Then

\[
R_t(v)=\sum_{r\ge0}\frac{(-t)^r}{r!}I_r(v)
\]

and

\[
\boxed{
[t^r]\,d\nu_{X,t}(y)
=
\frac{(-1)^r}{r!}
\frac{I_r(u_y-1)}{y\log y}\,dy.
}
\]

Consequently the coefficient of `t^r` in `\sigma_{X,t}` is exactly:

> discrete rooted `r`-face mass minus its continuum logarithmic simplex
> carrier.

The first layers have the direct arithmetic geometry:

- `r=0`: prime/rooted vertices;
- `r=1`: squarefree semiprime rooted edges;
- `r=2`: three-prime rooted triangular faces;
- `r>=3`: higher-factor rooted simplices.

Repeated powers of any prime do not open a new face direction; they remain in
the exponent-multiplicity fiber.

This gives the requested unified geometric distinction between primes,
semiprimes and multifactor composites inside one exact transport object.

---

## 7. Why fixed face order cannot close the endpoint bridge

The boundary-profile critical-depth law proves that canceling only rooted
faces up to order

\[
R=o\left(\frac{\log X}{\log\log X}\right)
\]

cannot suppress even the universal profile to a fixed power of `X`.

Thus the signed measure `\sigma_{X,t}` cannot be replaced by any fixed list of
prime, semiprime and low-factor statistics. At RH precision it needs either:

- the complete growing face tower through critical depth; or
- a closed-form transform retaining the same information.

This is the measure-side form of the BRC observer rule:

```text
LOW_FACTOR_MARGINALS != OPERATION_SAFE_FOR_RH_ENDPOINT_TRANSPORT
```

---

## 8. An exact endpoint bridge, not a proof shortcut

The new carrier establishes a precise path

\[
\boxed{
\text{prime intensity}
\xrightarrow{\ t\in[0,1]\ }
\text{rooted factor-face transport}
\xrightarrow{\ t=1\ }
\text{smooth-number discrepancy}.
}
\]

However, neither endpoint is automatically controlled by positivity of the
interpolating measure. The difficult object is the signed difference
`\sigma_{X,t}`.

A uniform positive law for `\mu_{X,t}` gives only the macroscopic profile.
RH requires a microscopic estimate for the discrete-minus-continuum
boundary-minus-bulk functional.

No conclusion may be drawn from:

- positivity of `\mu` and `\nu` separately;
- total mass agreement alone;
- fixed-order coefficient agreement;
- endpoint smallness at only one value of `t`;
- finite computation.

---

## 9. Exact checker

Task-local checker:

`experiments/rh_centered_rooted_transport_measure_check.py`

It verifies with exact rational arithmetic:

- cutoff jump divided by `t` equals rooted factor-cone mass;
- `t=0` gives prime-incidence mass;
- `t=1` gives largest-prime/smooth mass;
- the `t^r` coefficient equals the direct rooted `r`-face count;
- finite signed Stieltjes summation by parts recovers the weighted source.

A rational reference measure is used for the last algebraic regression. The
continuum Dickman measure is an analytic carrier, not an exact rational test
object.

---

## 10. New smallest unresolved unit

For the RH specialization

\[
Y=(\log X)^2,
\qquad f(y)=\sqrt y,
\]

the remaining target is the signed functional

\[
\boxed{
-\sqrt Y\,K_{X,t}(Y)
+
\frac12\int_2^Y\frac{K_{X,t}(y)}{\sqrt y}\,dy.
}
\]

The first admissible advance would be any fixed power saving over the
unsigned estimate, uniformly on a nontrivial `t` range, obtained without
assuming an RH-strength bound at `t=0` or `t=1`.

Two concrete routes survive the current no-go audit:

1. derive a differential/Volterra equation in `t` for `K_{X,t}` whose source
   has zero projection onto the square-root observer;
2. place `K_{X,t}` in a negative-order Hilbert norm where the
   boundary-minus-bulk observer is continuous and prove contraction for the
   centered factor-face transfer.

Any route must retain root labels and the growing critical-depth repair.

No RH proof is claimed.
