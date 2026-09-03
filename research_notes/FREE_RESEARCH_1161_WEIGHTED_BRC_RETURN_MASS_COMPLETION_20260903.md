# Free Research #1161 — finite Weighted-BRC return mass and the completion constant

Status: `FREE_RESEARCH_RESULT / FINITE POSITIVE-RATIONAL BRANCH BRIDGE / NOT WORKING_TRUTH / NOT FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-FREE-G61R8`
Parent issue: `#1161`
Dependencies:
- #1159 finite Wallis determinant ratio and tail certificate;
- #1161 proof `Pi_* = tau`.

## 1. Finite branch carrier for the power-series coefficients

For each `n in N_0`, take `2n` ordered time slots. At each slot choose a pair of binary labels

\[
(\epsilon_t,\eta_t)\in\{0,1\}^2.
\]

There are exactly

\[
4^{2n}=16^n
\]

paired histories.

Declare a paired history **balanced** when each coordinate separately contains exactly `n` zeros and `n` ones. The number of balanced histories is

\[
\binom{2n}{n}^2.
\]

Give every paired history the same positive rational weight `16^{-n}`. Then the total balanced-return mass is

\[
\boxed{
c_n
=
\frac{\binom{2n}{n}^2}{16^n}.
}
\]

These are exactly the coefficients used in the pi-free power series

\[
F(z)=\sum_{n\ge0}c_nz^n.
\]

Thus every coefficient of the analytic completion is already a finite explicit positive-rational branch mass.

Typing:

- the two binary labels are branch/provenance labels, not native negative geometric axes;
- multiplicity is retained explicitly before the balanced-return projection;
- this is a finite Weighted-BRC-compatible positive branch family at every finite `n`;
- the infinite generating function remains a derived completion/readout, not a finite N0 state.

## 2. Exact finite return-mass recurrence

From the binomial formula,

\[
\frac{\binom{2n+2}{n+1}}{\binom{2n}{n}}
=
\frac{(2n+2)(2n+1)}{(n+1)^2}
=
\frac{2(2n+1)}{n+1}.
\]

After dividing by the additional factor `16`, one obtains

\[
\boxed{
\frac{c_{n+1}}{c_n}
=
\left(\frac{2n+1}{2n+2}\right)^2.
}
\]

This is exactly the coefficient recurrence behind the differential equation used in the #1161 power-series closure.

Hence that ODE is not an arbitrary imported analytic object: it is the generating-function compression of a finite rational branch-count recurrence.

## 3. Exact finite coupling to the #1159 Wallis determinant ratio

The #1159 finite Wallis quantity is

\[
W_n
=
\prod_{r=1}^n
\frac{(2r)^2}{(2r-1)(2r+1)}.
\]

The power-series/Wallis normalization proof established

\[
\boxed{(2n+1)c_nW_n=1.}
\]

Therefore the finite parity-determinant ratio and the finite balanced-return mass are exact reciprocals up to the simple shell factor `2n+1`:

\[
\boxed{
W_n=\frac1{(2n+1)c_n}.
}
\]

Since #1159 proves

\[
W_n\to\tau/2,
\]

we obtain the purely discrete return-density formula

\[
\boxed{
\lim_{n\to\infty}n c_n=\frac1\tau.
}
\]

The #1161 internal normalization closure proves `Pi_*=tau`, so

\[
\boxed{
\Pi_*
=
\tau
=
\left(\lim_{n\to\infty}n c_n\right)^{-1}.
}
\]

Thus the Gauss–Legendre endogenous completion is also the reciprocal asymptotic density coefficient of a finite binary-pair balanced-return system.

## 4. Pure integer finite certificates for `Pi_*`

The #1159 exact tail certificate is

\[
1<\frac{W_\infty}{W_n}
\le
\frac{4n+2}{4n+1}.
\]

Because `tau=2W_inf` and `W_n=1/((2n+1)c_n)`, this becomes

\[
\boxed{
\frac{2}{(2n+1)c_n}
<
\Pi_*
\le
\frac{4}{(4n+1)c_n}.
}
\]

Substituting the exact count

\[
c_n=\binom{2n}{n}^2/16^n
\]

gives the entirely integer formula

\[
\boxed{
\frac{2\,16^n}{(2n+1)\binom{2n}{n}^2}
<
\Pi_*
\le
\frac{4\,16^n}{(4n+1)\binom{2n}{n}^2}.
}
\]

No square root, transcendental function, elliptic integral, or target pi value appears in these finite bounds.

At `n=10000`, exact integer/rational computation gives approximately

\[
3.141514118681922<\Pi_*<3.141592654571492,
\]

so both endpoints lie in the same four-decimal cell

\[
\boxed{3.1415}.
\]

The decimals are only a human-readable projection of exact rational bounds.

## 5. Three independent finite certificate channels for one completion

The current #1161 packet now has three structurally different finite certificate mechanisms for the same internally proved completion constant:

1. **AGM dyadic root interval channel** — finite integer/rational root enclosures propagated through the AGM state;
2. **#1159 parity determinant/Wallis channel** — exact rational spectral determinant ratios with a finite tail bound;
3. **balanced branch-return channel** — pure integer counts `binom(2n,n)^2` among `16^n` explicit paired binary histories.

Their agreement is not used as a substitute for proof; the power-series/Wronskian theorem already proves the shared limit. The multiple channels instead show that the same completion constant is visible through algebraic renormalization, finite rotation spectrum, and finite branch-return statistics.

## 6. Relation to Weighted-BRC typing

This construction naturally belongs to the globally available positive Weighted-BRC type discipline:

- branch representatives are explicit;
- all branch weights are positive rational numbers;
- total mass and return-event mass are different readouts;
- no signed/amplitude cancellation is used;
- multiplicity is never silently collapsed to Boolean support.

The exact coefficient `c_n` is the total positive mass of the balanced-return subset. The generating function `F` is a derived series of these finite masses.

This is a reuse/application of the existing weighted-branch carrier idea, not a claim for a new global tool family.

## 7. Reproducibility

Task-local checker:

`scripts/check_free_research_1161_return_mass_completion.py`

initial commit:

`d61a14268626f9ea311b53c6dd50fd7b77d44ee4`

Independent execution verified:

- the exact return-mass recurrence for `n=0..999`;
- the integer completion bracket at `n=10000`;
- common four-decimal cell `3.1415`.

## 8. Scope

Freeze at free-research-result strength:

`POWER_SERIES_COEFFICIENT = FINITE_POSITIVE_RATIONAL_BALANCED_RETURN_MASS`.

`TAU = PI_STAR = RECIPROCAL_ASYMPTOTIC_RETURN_DENSITY`.

`FINITE_INTEGER_RETURN_COUNT -> EXACT COMPLETION BRACKET = PROVED`.

`INFINITE_RETURN_GENERATING_FUNCTION = DERIVED_COMPLETION`, not N0 primitive.

`CLASSICAL_PI_NAME = SEPARATE IDENTIFICATION OF TAU`.
