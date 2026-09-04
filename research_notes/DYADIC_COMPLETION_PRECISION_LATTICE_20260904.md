# Dyadic completion precision lattice

Status: `FREE_RESEARCH / MONOTONE REFINEMENT STRUCTURE / NOT_FOUNDATION`
Date: `2026-09-04`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Parent: `#1159`, dyadic annihilation hierarchy

## 1. Setup

Let

\[
E_0(q)=T_q=2qS(\tau/(2q)),
\]

and recursively

\[
E_m(q)=\frac{4^mE_{m-1}(2q)-E_{m-1}(q)}{4^m-1}.
\]

For every `m>=0`, write

\[
y=\frac\tau{2q}.
\]

The annihilation analysis gives

\[
\tau-E_m(q)
=
\tau\sum_{s=0}^{\infty}(-1)^s b_{m,s}y^{2m+2+2s},
\]

with all `b_(m,s)>0` and strictly decreasing term magnitudes for `q>=2`.

## 2. Error is strictly increasing in phase step

Differentiate the positive-error series with respect to `y`.  If `n=m+1+s`, the ratio of consecutive derivative-term magnitudes is

\[
\frac{\mu_{m,n+1}}{\mu_{m,n}}
\,y^2\,
\frac{2n+2}{2n}
\frac1{(2n+2)(2n+3)}
=
\frac{\mu_{m,n+1}}{\mu_{m,n}}
\frac{y^2}{2n(2n+3)}.
\]

From the exact response-ratio telescope,

\[
\frac{\mu_{m,n+1}}{\mu_{m,n}}<\frac43.
\]

For `q>=2`, `tau<4` gives `0<y<1`, so the derivative series is again strictly alternating with decreasing magnitudes and positive first term. Therefore

\[
\boxed{
\frac{d}{dy}(\tau-E_m)>0.
}
\tag{DPL-1}
\]

Hence the error increases with phase step `y`.

## 3. Monotonicity under spatial refinement

Replacing `q` by `2q` halves `y`.  By (DPL-1),

\[
\tau-E_m(2q)<\tau-E_m(q).
\]

Thus

\[
\boxed{
E_m(q)<E_m(2q)<\tau
\qquad(m>=0,\ q>=2).
}
\tag{DPL-2}
\]

More generally, `E_m(q)` is strictly increasing with integer `q>=2`.

## 4. Monotonicity under extrapolation-order refinement

The recursive definition gives

\[
E_{m+1}(q)-E_m(q)
=
\frac{4^{m+1}}{4^{m+1}-1}
\bigl(E_m(2q)-E_m(q)\bigr).
\]

By (DPL-2), the bracket is positive. Therefore

\[
\boxed{
E_m(q)<E_{m+1}(q)<\tau.
}
\tag{DPL-3}
\]

So increasing annihilation order is itself a monotone refinement operation.

## 5. Two-dimensional precision lattice

For `m2>=m1` and `q2>=q1>=2`, monotonicity in both coordinates gives

\[
\boxed{
E_{m_1}(q_1)
\le E_{m_2}(q_2)
<\tau,
}
\]

with strict inequality whenever at least one coordinate is strictly refined.

Thus `(m,q)` carries a directed precision order:

```text
increase q  = spatial/dyadic spectral refinement
increase m  = asymptotic-mode annihilation refinement
```

Both operations preserve the same lower-certificate direction.

## 6. Convergence along either axis

For fixed `m`, the general error bound gives

\[
0<\tau-E_m(q)=O(q^{-2m-2}),
\]

so

\[
E_m(q)\uparrow\tau
\qquad(q\to\infty).
\]

For fixed `q>=2`,

\[
0<\tau-E_m(q)
<
\frac{4^{2m+3}}
{2^{(m+1)(m+2)}(2m+3)!q^{2m+2}},
\]

whose right side tends to zero superfast because of the `2^{-m^2}` and factorial factors. Hence

\[
E_m(q)\uparrow\tau
\qquad(m\to\infty).
\]

Therefore every cofinal path through the `(m,q)` refinement lattice converges to the same internal completion phase.

## 7. Dyadic finite-carrier interpretation

When `q` is dyadic, all values needed to construct `E_m(q)` lie on the exact inverse-decimation nested-radical tower.  Thus both monotone directions remain within finite algebraic data:

- `q -> 2q`: append one inverse-decimation square-root refinement;
- `m -> m+1`: form one rational linear combination of already available dyadic scales.

This gives a two-axis finite precision geometry whose common boundary value is `tau`.

Freeze:

`SPATIAL_REFINEMENT_MONOTONE -> TAU`.

`ANNIHILATION_ORDER_MONOTONE -> TAU`.

`(m,q)_DIRECTED_PRECISION_LATTICE -> COMMON_COMPLETION_PHASE`.
