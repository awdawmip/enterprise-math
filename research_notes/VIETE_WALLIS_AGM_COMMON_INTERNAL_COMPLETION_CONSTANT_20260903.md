# Viète–Wallis–AGM common internal completion constant before classical pi

Status: `FREE_RESEARCH / CROSS-FAMILY SYNTHESIS COROLLARY / NOT_FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-FREE-7D3C9A / FREE_AXIOM_DISCOVERY`
Parent issue: `#1158`
Cross-family sources:
- #1159 free-research Wallis/rotation result;
- #1161 commit `f2d92abea0fe634208d200e706be30820b08117b`;
- `research_notes/VIETE_WALLIS_INTERNAL_COMPLETION_EQUALITY_20260903.md`.

## 1. Independently constructed constants

Three free-research routes now construct internal completion objects without using classical circumference `pi` as the defining normalization.

### Viète / #1158

Binary finite orientation refinement and nested radical readouts define

\[
\Pi_{\rm rot}
=
\lim\Pi_n.
\]

#1158 proves internally

\[
\boxed{\Pi_{\rm rot}=\tau.}
\]

### Wallis / #1159

Finite rational determinant/parity spectra define the Wallis limit

\[
W_\infty
\]

and the first boundary-completion phase

\[
\tau,
\]

with

\[
\boxed{2W_\infty=\tau.}
\]

### Gauss–Legendre AGM / #1161

The AGM route defines its endogenous completion

\[
\Pi_*
\]

and normalized Böttcher rotation phase

\[
\Theta_{\rm AGM}.
\]

At the standard self-dual seed, #1161 now proves internally

\[
\boxed{\Pi_*=\Theta_{\rm AGM}=\tau.}
\]

## 2. Common internal constant

By transitivity,

\[
\boxed{
\Pi_{\rm rot}
=
2W_\infty
=
\Pi_*
=
\Theta_{\rm AGM}
=
\tau.
}
\]

This equality is established before any step that names `tau` as classical `pi`.

Therefore the three formula families do not merely converge numerically to the same familiar target. They reconstruct one common project-internal rotation-completion constant by genuinely different finite mechanisms.

## 3. Finite mechanisms are not duplicates

The equality of the global completion object does not collapse the finite constructions.

### Viète

Finite mechanism:

\[
C_3\leftarrow C_6\leftarrow C_{12}\leftarrow\cdots
\]

with connected binary orientation covers, exact normalized Cayley-distance halving, shortest-root/tie-retaining refinement, and nested radical character traces.

Finite precision:

\[
\text{error}\asymp M^{-2}
\]

in orientation-state count `M`.

### Wallis

Finite mechanism:

- rational Dirichlet determinant rotation modes;
- Hamming-shell parity spectrum;
- exact even/odd determinant ratios.

Finite precision:

certified Wallis tail of order

\[
O(N^{-1})
\]

in the parity-mode cutoff.

### AGM

Finite mechanism:

- normalized equal-resultant/Vïète root;
- componentwise square/complementary quadratic channels;
- Pythagorean cone completion;
- Böttcher phase doubling / AGM renormalization.

Finite precision:

quadratic/double-exponential AGM contraction in iteration depth under the #1161 certificates.

Thus the common constant is a cross-family invariant while the finite resolution dynamics remain distinct.

## 4. Local Viète–AGM relation is stronger than common-target equality

#1161 already proves that one normalized AGM step factors through the exact #1158 finite root state:

```text
Viète normalized equal-resultant root
    -> componentwise square
    -> complementary quadratic channels
    -> AGM/Pythagorean cone completion
```

Therefore the Viète–AGM connection has two layers:

1. **local mechanism relation:** AGM contains the #1158 half-root operation as an exact factor;
2. **global completion relation:** both endogenous constants equal `tau`.

Wallis supplies a different global spectral realization of the same `tau` rather than the same local update.

## 5. A common internal target for other pi-formula families

For later cross-family tests, the preferred internal target can now be stated as

\[
\boxed{\tau}
\]

or equivalently any of

\[
\Pi_{\rm rot},\quad 2W_\infty,\quad\Pi_*,\quad\Theta_{\rm AGM}.
\]

A new formula family should first be tested against this already unified internal completion object, rather than using classical `pi` as an input calibration.

This avoids a logically weaker pattern in which each route separately imports the same classical target and then is declared consistent because the outputs agree.

## 6. Classical compatibility remains a separate naming theorem

Only after the internal equality above is established does the classical compatibility layer identify

\[
\tau=\pi.
\]

Then the familiar equalities follow automatically:

\[
\Pi_{\rm rot}=\pi,
\qquad
W_\infty=\pi/2,
\qquad
\Pi_*=\pi,
\qquad
\Theta_{\rm AGM}=\pi.
\]

But the common-completion theorem itself does not depend on that naming.

## 7. G0/native boundary remains common too

All three routes currently retain a similar strength boundary:

- their finite/algebraic/analytic completion mechanisms are exact at derived G1/G2 strength;
- current P000/Cell foundation does not yet supply one uniquely selected native finite 6D rotation law or canonical Cell-to-orientation quotient;
- therefore the common global constant is **not** evidence that one specific G1 finite mechanism has been promoted to primitive G0 geometry.

The common native frontier is to explain why actual Cell rotation selects the finite orientation/transport structures whose different completions all reconstruct `tau`.

## 8. Current synthesis

At free-research theorem strength:

```text
Viète binary gate refinement -----------\
                                        \
Wallis parity/determinant spectrum ------> tau
                                        /
AGM bisector-square/Böttcher RG --------/
```

and only afterward

```text
tau -> classical compatibility name pi.
```

This is the strongest current cross-family completion synthesis available from #1158/#1159/#1161 without promoting any of the three mechanisms to native Foundation.
