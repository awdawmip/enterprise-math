# RH boundary-profile critical-depth law

Status: `RESEARCH FRONTIER / EXACT ASYMPTOTIC DEPTH LAW + TAYLOR-TOWER NO-GO / NOT A PROOF OF RH`
Date: `2026-09-07`
Project: `Enterprise Math / 进取数论`
Researcher: `EM-RHHR-20260907`
Scope: `RH / prime-rooted Alladi transport / Factor-BRC arity / boundary layer / critical provenance depth`
Parents:

- `RH_PRIME_ROOTED_ALLADI_ROUGH_PHASE_TRANSPORT_20260907.md`
- `RH_HYPERBOLA_COUNTERTERM_TOWER_20260907.md`
- `RH_GREEN_ALLADI_CRITICAL_PRIMITIVE_SOURCE_PORT_20260906.md`

## 0. Purpose and typing guard

The prime-rooted transport note proved that, at the RH specialization

\[
Y=(\log X)^2,\qquad f(q)=\sqrt q,
\]

the exact normalized Alladi source has the real boundary-layer profile

\[
-\frac{F_X(\tau/L_X)}{S_X}
=e^{-\tau}+O_T\!\left(\frac1{\log\log X}\right),
\qquad
L_X=\log\frac{\log X}{\log Y},
\]

uniformly for bounded `tau>=0`.

The present note asks a narrower exact question:

> how many factorial-moment / rooted-factor-arity layers are required merely
> to cancel the universal leading profile `e^{-tau}` down to the
> `X^{-1/2+o(1)}` scale?

The answer reproduces the previously discovered critical provenance depth

\[
K_X\sim\frac12\frac{\log X}{\log\log X}.
\]

This is a theorem about the Taylor/counterterm resolution of the universal
profile. It is not a lower bound on every conceivable proof strategy and is
not an RH proof.

P000 remains unchanged. The order `R` is Factor-BRC provenance depth, not a
new spatial dimension.

BRC resolution:

```text
COMPOSE_APPLIED
PRIME_ROOTED_PGF + FACTORIAL_MOMENT_ARITY + CRITICAL_SOURCE_SCALE
```

---

## 1. Exact rooted-factorial expansion

Under the positive prime-rooted probability carrier from the parent note,
let

\[
H=h_Q(M)
\]

be the number of prime factors of `M` that are larger than the selected root
prime `Q`. Then exactly

\[
-\frac{F_X(t)}{S_X}
=\mathbb E(1-t)^H
=\sum_{r\ge0}(-t)^r\mathbb E\binom Hr.
\]

The sum is finite for every finite `X`.

For one rooted integer Cell, `binom(H,r)` counts the `r`-element subsets of
its larger-prime arms. Hence the coefficient of `t^r` is the positive mass of
all rooted `r`-faces before the final alternating observer is applied.

Geometrically:

- `r=0`: rooted vertex;
- `r=1`: rooted edge, first seen by squarefree semiprimes;
- `r=2`: rooted triangular face, first seen by three-prime composites;
- general `r`: rooted `r`-simplex face;
- truncation at order `R`: all rooted faces of arity above `R` are removed
  from the observer state.

Prime powers remain in the separate exponent-multiplicity fiber because the
rooted Alladi carrier reads the radical.

Freeze:

```text
TAYLOR_ORDER_r = ROOTED_FACTOR_FACE_ARITY_r
FIXED_ORDER_TRUNCATION = PROVENANCE_ARITY_TRUNCATION
```

---

## 2. Exact remainder bounds for the universal profile

For fixed `tau>0`, define the order-`R` Taylor remainder

\[
E_R(\tau)
=e^{-\tau}-\sum_{r=0}^{R}\frac{(-\tau)^r}{r!}.
\]

Once `R+2>tau`, the omitted alternating terms decrease in magnitude. The
alternating-series remainder therefore has sign `(-1)^{R+1}` and satisfies

\[
\boxed{
\frac{\tau^{R+1}}{(R+1)!}
\left(1-\frac{\tau}{R+2}\right)
\le |E_R(\tau)|
\le
\frac{\tau^{R+1}}{(R+1)!}.
}
\]

Consequently, for fixed `tau`,

\[
\boxed{
|E_R(\tau)|
=\frac{\tau^{R+1}}{(R+1)!}
\left(1+O_\tau\!\left(\frac1R\right)\right).
}
\]

No number-theoretic input is used in this step.

---

## 3. Power-scale depth law

Let

\[
R_X
=\alpha\frac{\log X}{\log\log X}+o\!\left(
\frac{\log X}{\log\log X}
\right),
\qquad \alpha>0.
\]

Stirling's formula gives

\[
\log((R_X+1)!)
=R_X\log R_X-R_X+O(\log R_X).
\]

Because

\[
\log R_X
=\log\log X-\log\log\log X+O_\alpha(1),
\]

we have

\[
R_X\log R_X
=\alpha\log X+o(\log X).
\]

The numerator `(R_X+1)log tau` is only
`O(log X/loglog X)=o(log X)`. Therefore Section 2 yields

\[
\boxed{
|E_{R_X}(\tau)|=X^{-\alpha+o(1)}
}
\]

for every fixed `tau>0`.

In particular:

- fixed `R` leaves a nonzero constant profile error;
- `R=o(log X/loglog X)` leaves only `X^{-o(1)}` suppression;
- `R=alpha log X/loglog X` produces exactly the power `X^{-alpha+o(1)}`.

This is the boundary-profile critical-depth law.

---

## 4. RH source normalization selects `alpha=1/2`

For the RH root weight and cutoff,

\[
f(q)=\sqrt q,\qquad Y=(\log X)^2,
\]

the exact positive source mass is

\[
S_X
=\sum_{q\le Y}\sqrt q\frac{\lfloor X/q\rfloor}{X}.
\]

Prime partial summation gives

\[
S_X
\sim\sum_{q\le Y}\frac1{\sqrt q}
\sim\frac{2\sqrt Y}{\log Y}
=\frac{\log X}{\log\log X}
=X^{o(1)}.
\]

Hence the absolute uncancelled universal source after order `R_X` has scale

\[
S_X|E_{R_X}(\tau)|
=X^{-\alpha+o(1)}.
\]

To reach the critical residual scale

\[
X^{-1/2+o(1)},
\]

one must have

\[
\boxed{\alpha\ge\frac12.}
\]

Equivalently, a Taylor/counterterm scheme based on the universal rooted
boundary profile requires

\[
\boxed{
R_X\ge
\left(\frac12-o(1)\right)
\frac{\log X}{\log\log X}.
}
\]

The threshold is exactly the Alladi/Hildebrand critical depth already found
from the lossless high-arity repair:

\[
\boxed{
K_X
\sim
\frac12\frac{\log X}{\log\log X}.
}
\]

Thus the same depth appears independently from two requirements:

1. **state completeness:** retain the rare high-arity Factor-BRC tail down to
   square-root population size;
2. **observer precision:** cancel the universal boundary profile down to
   square-root amplitude.

This coincidence is structural rather than a choice of notation.

---

## 5. Typical depth and precision depth are different

The parent rooted law gives

\[
H\asymp L_X\asymp\log\log X
\]

for a typical root-selected Cell.

But Section 4 gives the much larger precision depth

\[
K_X\asymp\frac{\log X}{\log\log X}.
\]

Therefore:

\[
\boxed{
\text{typical geometric depth}
\ll
\text{depth needed for RH-scale observer precision}.
}
\]

There is no contradiction. The positive population profile is determined by
typical cells, while a residual of size `X^{-1/2}` is sensitive to factorial
Taylor tails far below ordinary probability resolution.

In BRC terms:

```text
TYPICAL_BRANCH_DEPTH controls macroscopic profile;
RARE_PROVENANCE_DEPTH controls microscopic signed residual.
```

This is another reason a fixed six-port X6 state cannot be the whole RH
carrier. X6 remains the local width; the composite provenance path must grow
to depth `K_X`.

---

## 6. Fixed-order and `o(K_X)` no-go

For every fixed `tau>0` and every

\[
R_X=o\!\left(\frac{\log X}{\log\log X}\right),
\]

Section 3 gives

\[
S_X|E_{R_X}(\tau)|=X^{-o(1)}.
\]

Hence no fixed-order, logarithmic-order, or generally `o(K_X)` subtraction of
the universal Taylor tower can by itself reach the square-root residual
scale.

Freeze:

```text
FINITE_COUNTERTERM_TOWER -> NO_RH_SCALE
SUBCRITICAL_ARITY_o(logX/loglogX) -> NO_FIXED_POWER_PROFILE_SUPPRESSION
```

This no-go applies to schemes whose cancellation mechanism is order-by-order
Taylor removal of the universal rooted profile. It does not rule out a
nonlocal transform that cancels the profile in closed form while preserving
all repair coordinates.

---

## 7. Why this still does not prove RH

The exact discrete boundary profile is currently known here only as

\[
-\frac{F_X(\tau/L_X)}{S_X}
=e^{-\tau}+O\!\left(\frac1{\log\log X}\right).
\]

That error is enormously larger than `X^{-1/2}`. The present theorem analyzes
the resolution needed to cancel the **universal leading profile**; it does
not control the centered arithmetic defect.

The following components remain outside the theorem:

- the signed discrete-minus-continuum cutoff-phase measure;
- the one-point prime-intensity discrepancy;
- the exact floor/population sawtooth source;
- reciprocal-Gamma lower-order corrections;
- growing-order uniformity of actual factorial moments;
- the rare high-arity repair itself.

Therefore:

```text
CRITICAL_DEPTH_MATCH != RH_PROOF
UNIVERSAL_PROFILE_CANCELLATION != ARITHMETIC_DEFECT_CANCELLATION
```

---

## 8. New smallest unresolved unit

The result eliminates the strategy of handling only finitely many Alladi or
rough-arity layers. The next admissible object is the centered prime-cutoff
transport measure

\[
\mathfrak d_{X,t}(dy)
=
\frac1t\,d\left[
\Phi_X(y;t)
-R_t\!\left(\frac{\log X}{\log y}\right)
\right].
\]

The RH source reads this measure against

\[
f(y)=\sqrt y.
\]

A genuine gain must either:

1. estimate this signed measure in a negative/Sobolev-type norm adapted to
   `sqrt(y)`; or
2. construct a closed-form provenance-preserving renormalization of the full
   depth-`K_X` tower before taking the final signed observer.

Taking total variation, fixing the arity, or replacing prime labels by an
arity histogram cannot reach the required scale.

No RH proof is claimed.
