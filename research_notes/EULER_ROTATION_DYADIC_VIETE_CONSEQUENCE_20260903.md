# Dyadic Euler rotation refinement -> Viète finite precision-pi sequence

Status: `FREE_RESEARCH / EXACT_FINITE_RECURSION + CLASSICAL_COMPLETION / NOT_FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`
Parent candidate: `AC-EM-FREE-F6D046-EULER-ROTATION-CHARACTER-V1`

## 1. Target-free finite recursion

Start from the half-turn square-root tower in the completed rotation character,

\[
U_0=-1,\qquad U_{n+1}^2=U_n.
\]

Let the positive longitudinal readout after the quarter-turn level be generated algebraically by

\[
c_1=0,\qquad c_{n+1}=\sqrt{\frac{1+c_n}{2}}\quad(n\ge1).
\]

No numerical value of pi occurs in this recursion.

The first terms are

\[
c_2=\frac{\sqrt2}{2},\qquad
c_3=\frac{\sqrt{2+\sqrt2}}2,\qquad
c_4=\frac{\sqrt{2+\sqrt{2+\sqrt2}}}2,\ldots
\]

Define the finite rotation-refinement readout

\[
P_m=\prod_{n=2}^{m}c_n,
\qquad
\pi_m^{\mathrm{rot}}=\frac{2}{P_m}.
\]

This gives a target-free algebraic finite-resolution pi sequence.

Numerically:

| m | pi_m^rot |
|---:|---:|
| 2 | 2.828427124746190 |
| 3 | 3.061467458920718 |
| 4 | 3.121445152258052 |
| 5 | 3.136548490545939 |
| 6 | 3.140331156954753 |
| 7 | 3.141277250932773 |
| 8 | 3.141513801144301 |
| 9 | 3.141572940367091 |
| 10 | 3.141587725277159 |

## 2. Classical character identification

Under the classical complex rotation character, choose

\[
U_n=e^{i\pi/2^n}.
\]

Then

\[
c_n=\cos\left(\frac{\pi}{2^n}\right),
\]

and the recursion above is exactly the half-angle law.

Therefore

\[
P_m=\prod_{n=2}^{m}\cos\left(\frac{\pi}{2^n}\right).
\]

Repeated angle doubling gives the exact finite identity

\[
P_m=\frac{1}{2^{m-1}\sin(\pi/2^m)},
\]

hence

\[
\pi_m^{\mathrm{rot}}=2^m\sin\left(\frac{\pi}{2^m}\right).
\]

The equality of the algebraic recursion and this trigonometric expression is a classical analytic/character interpretation; the algebraic recursion itself does not need pi as input.

## 3. Completion

Using the classical small-angle limit `sin x / x -> 1`,

\[
\lim_{m\to\infty}\pi_m^{\mathrm{rot}}=\pi.
\]

Equivalently,

\[
\prod_{n=2}^{\infty}c_n=\frac2\pi,
\]

which is Viète's product.

The completion error satisfies

\[
\pi-\pi_m^{\mathrm{rot}}
=\frac{\pi^3}{6\,4^m}+O(16^{-m}).
\]

Thus one dyadic orientation refinement improves the leading angular-completion error by a factor asymptotic to `1/4`.

## 4. Enterprise interpretation

This gives a much cleaner precision-pi hierarchy than a post-hoc decimal approximation:

```text
half-turn reversal
 -> successive rotation square roots
 -> exact nested-radical longitudinal states c_n
 -> finite algebraic readout pi_m^rot
 -> analytic completion
 -> classical pi
```

The key point is causal direction: the finite nested-radical states can be generated without using the target numerical value of pi. Classical pi enters when the infinite rotation-refinement tower is identified with the continuous phase completion.

This strongly motivates the free-research Viète branch (GitHub issue #1158), but it does not pre-judge whether the half-angle refinement is itself canonical from the native Cell transition law.

## 5. Boundary

`TARGET_FREE_ALGEBRAIC_RECURSION != NATIVE_CELL_DERIVATION`.

The missing theorem is still: derive the square-root-of-rotation refinement from the actual Enterprise Cell/segment transition structure rather than selecting it because the classical half-angle formula is known.
