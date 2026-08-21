# R005-B — Cubic Horizontal Certificate Placement and Post-Database Cursor

Status: `PROVED R005 RESOURCE-PLACEMENT REDUCTION / NOT CANONICAL`  
Date: `2026-08-12`  
Program: `R005 — Enterprise Prime Toolkit`  
Track: `B — Prime–Collapse Field Geometry`  
Depends on: Supplements 15, 20, 22

## 1. Result

Supplement 22 measured two finite certificate resources by amount.  The current
cubic endpoint is horizontal-data limited at k=10^10.  The next question is not
only how much horizontal coverage exists, but **where** it is placed in cofactor
scale.

For

\[
A=k^3,\qquad U=(k+1)^3-1,\qquad F=F_3(k),
\]

consider lower-band candidate coordinates q>k.

Let an exhaustive cofactor-gap certificate be valid for gap starts below the
integer scale X.  Let an effective relative prime-interval row be valid from an
integer scale x0 with parameter Delta.

Then:

- database coverage acts on the high-q side
  \[
  q>\left\lfloor A/X\right\rfloor;
  \]
- a strong/visible effective row acts on the low-q side
  \[
  q\le\left\lfloor U/x_0\right\rfloor;
  \]
- the exact unresolved lower-band cursor is therefore
  \[
  \boxed{
  \max\left(k+1,\left\lfloor U/x_0\right\rfloor+1\right)
  \le q\le
  \min\left(\left\lfloor A/F\right\rfloor,
             \left\lfloor A/X\right\rfloor\right),
  }
  \]
  when the effective row is visible and its Delta fits the cubic relative
  width.  If no effective row is active, the left endpoint is simply k+1.

This is the exact placement analogue of Supplement 22's resource amount law.

## 2. B73 — exact horizontal scale range

For integer q>k, the cofactor upper endpoint is U/q.  It is maximal at q=k+1,
where

\[
\boxed{
\left\lfloor\frac{U}{k+1}\right\rfloor
=(k+1)^2-1.
}
\]

Hence an effective row whose size threshold x0 exceeds `(k+1)^2-1` is invisible
to the entire q>k horizontal world, no matter how large its Delta is.

This is why the strong corrected Cully--Hugill--Lee rows with x0=e^55 or e^60
help the vertical q<=k region but do not touch the current horizontal frontier
near k=10^10: the horizontal cofactor world is only of order 10^20.

Thus horizontal effective coverage requires **two coordinates at once**:

\[
\boxed{x_0\le (k+1)^2-1}
\]

and

\[
\boxed{3(k+1)(\Delta-1)>k^2.}
\]

A theorem may be strong enough but start too late, or start early enough but be
too weak.

## 3. B74 — database placement on the q-axis

A database valid for every relevant gap start below X covers a q-coordinate
whenever

\[
A/q<X.
\]

For integer q this is exactly

\[
\boxed{q>\left\lfloor A/X\right\rfloor.}
\]

So the possible database-overflow cursor lies to the **left** of
`floor(A/X)`, not throughout the whole candidate set.

After also imposing q>k and the lower-band condition qF<=A, possible overflow is

\[
\boxed{
k<q\le
\min\left(\left\lfloor A/X\right\rfloor,
          \left\lfloor A/F\right\rfloor\right).}
\]

Near the current X=10^20 boundary the first term is overwhelmingly smaller;
the overflow coordinates sit immediately above k.

## 4. B75 — effective-row placement on the q-axis

An effective row valid for y>=x0 can be applied at the cofactor upper endpoint

\[
y=U/q
\]

exactly when

\[
q\le\left\lfloor U/x_0\right\rfloor.
\]

The row also needs the q-independent cubic width condition

\[
3(k+1)(\Delta-1)>k^2.
\]

When both conditions hold, the row covers a **low-q prefix** while the database
covers a **high-q suffix**.

The exact integer cursor between them is therefore the interval stated in
Section 1.

A convenient sufficient real seam condition is

\[
\frac{A}{X}\le\frac{U}{x_0},
\]

equivalently

\[
\boxed{x_0A\le XU.}
\]

If this holds and the row has enough Delta, the two real coverage regions
already overlap.  Integer floors can occasionally close a slightly weaker
real seam, so the exact compiler uses integer endpoints.

## 5. B76 — the post-10^10 cursor has exact initial speed 2

Freeze the current database boundary as

\[
K=10^{10},\qquad X=K^2=10^{20},
\]

and put

\[
k=K+d.
\]

With no effective row touching the horizontal scale, the database-overflow
integer width is

\[
W_X(k)
=
\left\lfloor\frac{k^3}{K^2}\right\rfloor-k.
\]

Expanding exactly,

\[
\boxed{
W_X(K+d)
=2d+
\left\lfloor
\frac{3d^2}{K}+rac{d^3}{K^2}
\right\rfloor.
}
\]

The correction remains below one precisely through

\[
\boxed{0\le d\le57{,}734.}
\]

Therefore for every

\[
1\le d\le57{,}734
\]

we have the exact cursor

\[
\boxed{
K+d<q\le K+3d,
}
\]

or, relative to the current k,

\[
\boxed{k<q\le k+2d.}
\]

At d=57,735 the width becomes `2d+1` for the first time.

So immediately beyond the exhaustive-data endpoint, the uncovered coordinate
set grows at exactly **two integer q positions per one increment of k**.

## 6. Precision-placement interpretation

Supplement 22 showed

\[
K_V\propto\Delta,
\qquad
K_H\asymp\sqrt X.
\]

The present result shows why those scalar amounts are not the whole state.
Two certificate stacks with the same nominal strength may leave different q
holes because their scale thresholds are placed differently.

The correct horizontal state is therefore at least

\[
\boxed{(X;\ x_0,\Delta;\ \text{cursor endpoints})}
\]

rather than a scalar `best finite k`.

This is a concrete R005 instance of the project-wide principle

\[
\boxed{\text{precision amount}\ne\text{precision placement}.}
\]

## 7. Next consequence

The first post-database frontier no longer requires extending the entire Prime
Gap List computation.  For small d it suffices to certify the tiny cursor

\[
k<q\le k+2d
\]

at the actual prime q coordinates.

For each such prime q, one may search only the corresponding cofactor interval

\[
\left(k^3/q,\ ((k+1)^3-1)/q\right]
\]

for one prime r.  This is a sparse local certificate problem rather than an
exhaustive global gap database problem.

Supplement 24 implements a deterministic version of that local certificate on
the first post-10^10 block.

## 8. Boundary

The placement formulas do not assert that any particular effective theorem or
database is available.  `X`, `x0`, and `Delta` are declared certificate
resources.

Likewise, the exact cursor width counts integer coordinates, not prime
coordinates.  A later executable certificate must still prove primality of the
actual q and cofactor witnesses used.
