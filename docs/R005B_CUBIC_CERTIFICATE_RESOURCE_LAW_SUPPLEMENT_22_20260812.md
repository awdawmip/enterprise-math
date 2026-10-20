# R005-B — Cubic Finite-Certificate Resource Law

Status: `PROVED R005 RESOURCE REDUCTION / NOT CANONICAL`  
Date: `2026-08-12`  
Program: `R005 — Enterprise Prime Toolkit`  
Track: `B — Prime–Collapse Field Geometry`  
Depends on: Supplements 18–21

## 1. Result

The current finite cubic full-forcing theorem is produced by several
certificate languages, but after the scale-complement hypotheses are checked,
two scalar resources control how far the theorem can extend:

1. effective relative prime-interval strength `Delta`;
2. exhaustive horizontal cofactor-gap coverage scale `X`.

Their exact cubic basin horizons are

\[
\boxed{K_V(\Delta)=3(\Delta-1)}
\]

and

\[
\boxed{
K_H(X)
=
\max\{k:k^2-k<X\}
=
\left\lfloor\frac{1+\sqrt{4X-3}}2\right\rfloor.
}
\]

Subject to the already-established Oppermann/effective size complement and one
early upper-prefix certificate, the resulting finite classification endpoint is

\[
\boxed{K_{\rm cert}=\min(K_V(\Delta),K_H(X)).}
\]

This turns improvements in two very different external resources into one
common coordinate system.

## 2. B69 — exact vertical resource law

Let an effective theorem guarantee a prime in

\[
\bigl(y(1-\Delta^{-1}),y\bigr]
\]

whenever its size hypothesis is met.

For the cubic cofactor interval \((A/q,U/q]\), Supplement 19 reduced the fit
condition to

\[
3(k+1)(\Delta-1)>k^2.
\]

Write

\[
D=\Delta-1.
\]

At

\[
k=3D
\]

the exact margin is

\[
3(3D+1)D-(3D)^2=3D>0.
\]

At the next integer,

\[
3(3D+2)D-(3D+1)^2=-1.
\]

Therefore

\[
\boxed{K_V(\Delta)=3(\Delta-1)}
\]

exactly.

The inverse resource requirement is also exact.  To cover a specified cubic
coordinate k, the least integer Delta is

\[
\boxed{
\Delta_{\min}(k)
=2+\left\lfloor\frac{k^2}{3(k+1)}\right\rfloor.
}
\]

Thus one extra unit of Delta buys exactly three further cubic k coordinates in
the pure vertical resource model.

## 3. B70 — exact horizontal database resource law

For q>k,

\[
\left\lfloor\frac{k^3}{q}\right\rfloor\le k^2-k.
\]

If a complete consecutive-prime-gap database is available for every gap start
below X, the whole q>k lower-cofactor region is covered whenever

\[
k^2-k<X.
\]

Because both sides are integers this is equivalent to

\[
k^2-k\le X-1.
\]

Solving the quadratic gives

\[
\boxed{
K_H(X)
=
\left\lfloor\frac{1+\sqrt{4X-3}}2\right\rfloor.
}
\]

The exact inverse resource requirement is

\[
\boxed{X_{\min}(k)=k^2-k+1.}
\]

So horizontal coverage has square-root returns: multiplying X by a fixed
factor c increases the reachable k scale only by about \(\sqrt c\).

## 4. B71 — current bottleneck diagnosis

For the corrected Cully--Hugill--Lee `log x0=60` row used in Supplement 20,

\[
\Delta=76{,}918{,}400{,}000.
\]

Therefore

\[
\boxed{
K_V=230{,}755{,}199{,}997.
}
\]

For the current Prime Gap List exhaustive boundary

\[
X=10^{20},
\]

we have

\[
\boxed{K_H=10{,}000{,}000{,}000.}
\]

Hence

\[
\boxed{K_{\rm cert}=10^{10}}
\]

and the current finite theorem is unequivocally **horizontal-data limited**.

The effective interval theorem has a factor

\[
\frac{K_V}{K_H}\approx23.08
\]

of unused k-range headroom.

## 5. B72 — cost of matching the current vertical resource

To exploit the full corrected CHL row without changing the vertical theorem,
the horizontal database would need to cover through

\[
X_{\rm match}
=K_V^2-K_V+1.
\]

Exactly,

\[
\boxed{
X_{\rm match}
=53{,}247{,}962{,}325{,}424{,}713{,}600{,}013.
}
\]

Relative to the current \(10^{20}\) exhaustive boundary this is a factor
approximately

\[
\boxed{532.48.}
\]

This quadratic resource cost explains why a large improvement in Delta may
produce no change at all in the certified k endpoint while horizontal data is
the active bottleneck.

Conversely, to support the current k endpoint \(10^{10}\), the minimum integer
effective parameter is only

\[
\boxed{\Delta_{\min}(10^{10})=3{,}333{,}333{,}335,}
\]

well below the corrected CHL value \(76{,}918{,}400{,}000\).

## 6. Certificate-resource Pareto interpretation

The finite Prime Toolkit now exhibits an exact resource asymmetry:

\[
\boxed{\text{effective theorem strength}\quad K_V\propto\Delta,}
\]

\[
\boxed{\text{exhaustive gap coverage}\quad K_H\asymp\sqrt X.}
\]

These are different currencies.

A stronger effective interval theorem is valuable only while vertical coverage
is the minimum resource.  Once horizontal data becomes active, additional
Delta is dormant until X catches up.

Likewise, extending the gap database beyond the point where K_H exceeds K_V
would stop improving the theorem unless the effective interval resource is also
upgraded.

Thus the correct finite research target is not `maximize every certificate`.
It is:

\[
\boxed{\text{raise the currently minimal coverage coordinate}.}
\]

For the present cubic stack, that coordinate is X.

## 7. Relation to the post-10^10 annulus

The scalar resource law diagnoses the active bottleneck but does not erase the
more refined geometry from Supplement 20.

Immediately beyond \(10^{10}\), only a subrange of q>k actually escapes the
current database.  Its cofactor upper scale begins just above \(10^{20}\).
Effective relative-interval rows recover coverage again at larger y scales.
Hence a finer extension can be obtained by covering the intermediate cofactor
annulus rather than extending the entire exhaustive database to
\(X_{\rm match}\).

That annulus problem is a **placement** problem inside the horizontal resource,
whereas B69--B72 describe total resource amount.  The distinction mirrors the
project-wide separation between precision amount and precision placement.

## 8. Executable surface

`src/enterprise_math/prime_cubic_certificate_resources.py` implements only the
integer resource compilers:

- `vertical_effective_k_max(delta)`;
- `effective_delta_required_for_k(k)`;
- `horizontal_database_k_max(X)`;
- `horizontal_coverage_required_for_k(k)`;
- `combined_resource_k_max(delta,X)`;
- `coverage_required_to_match_delta(delta)`.

The companion unit tests exhaust small exact inverses and freeze the current
corrected-CHL / \(10^{20}\) reference values.

No external theorem or database is revalidated by this module.

## 9. Boundary

This supplement is an exact arithmetic/resource reduction, not a claim that
external computation cost scales linearly with X or that Delta has a universal
physical meaning.

The formulas quantify the coverage supplied by two declared certificate
resources.  Actual computational cost, proof complexity, storage layout, and
future external theorem improvements are separate engineering/research axes.
