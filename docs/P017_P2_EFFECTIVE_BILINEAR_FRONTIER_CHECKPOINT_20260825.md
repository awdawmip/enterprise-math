# P017 — P2 Effective Bilinear Frontier Checkpoint

Status: `PROVED_WIP PARAMETER PACKAGE + EXACT CHECKER + EFFECTIVITY FRONTIER / NOT CANONICAL / NO ALL-K P2 CLAIM`

Captured: `2026-08-25T18:58+08:00`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Current owner head before this checkpoint: `25dc2e8f1b598e56c67639ce12c6f2556d7672de`

Latest canonical main seen: `d79fbdd0d8f4eaa02f8fb7947caeeb63464f1674`

GLOBAL_KNOWLEDGE sync event: `cc2ab9c8b3190efc54fc8ee54a87d16b1c337983`

## 1. Frozen exact interface

For the square basin

\[
I_K=\{K^2+1,\ldots,K^2+2K\},
\]

write

\[
H_m(K)=\#\{n\in I_K:m\mid n\},
\qquad
r_K(m)=H_m(K)-\frac{2K}{m}.
\]

The odd-quotient P017 channel satisfies the exact identity

\[
\boxed{
(H_m-H_{2m})-\frac{K}{m}=r_K(m)-r_K(2m).
}
\]

Thus the P017 binary-carry remainder is an exact parity projection of the ordinary short-interval floor remainder. This is the interface to Chen/Iwaniec-Laborde bilinear remainder estimates; it is not a separate new distribution object.

## 2. Four-sevenths effectivity package

The current preferred package is

\[
\theta=\frac{4999}{10000},\qquad
D=X^{4/7},\qquad
a=4,\quad b=\frac52,\quad c=\frac72.
\]

Hence

\[
z=X^{1/7},\qquad D^{b/a}=X^{5/14},\qquad D^{c/a}=X^{1/2}.
\]

Exact positive margins:

\[
2\theta-\frac5{14}-\frac47
=\frac{2493}{35000}>0,
\]

and

\[
\frac27-\frac{3\theta-1}{2}
=\frac{5021}{140000}>0.
\]

The exact-rational integral certificate gives

\[
C_1-C_2
>\frac{181923437}{1248500450}
\approx0.145713553.
\]

The executable certificate at

`experiments/p017_p2_effective_four_sevenths_certificate_20260825.py`

hard-asserts these relations and bounds.

## 3. Comparison state

The earlier `D=X^(5/9)` package has a larger raw bilinear exponent gap but a much smaller certified main-term reserve (about `0.04666595`). The four-sevenths package keeps a fixed bilinear power gap of about `0.07123` while increasing the coarse net reserve to about `0.14571`.

Therefore the active comparison is no longer which package has the larger asymptotic exponent. The relevant question is which package yields the lower explicit numerical threshold after the constants in the bilinear lemma are made effective.

## 4. Negative boundaries retained

1. A constant extra high-prime penalty such as `lambda/2=0.415` is not a complete pointwise P2 detector; low-low-large three-factor configurations can survive.
2. Staying entirely below the square-root level permits crude absolute-value remainder bounds but does not cross the weighted-sieve P2 barrier.
3. The P017 carry/Fourier/roughness representations alone do not manufacture new cancellation; the full carry field factors through classical roughness displacement discrepancy unless the special low-height square-basin coupling is used.
4. No all-k consecutive-square P2 theorem is claimed here. Historical sufficiently-large P2 short-interval results are prior art.

## 5. Current hard mathematical frontier

The sole live analytic task is to make the Iwaniec-Laborde Lemma-4-type bilinear saving effective for the present parameter package, with explicit constants sufficient to compare a finite threshold against the existing Campbell finite/computational overlap.

Target schematic form:

\[
\mathcal R(K)
=\sum_{m}\gamma_m\bigl(r_K(m)-r_K(2m)\bigr),
\]

where the sieve coefficients are decomposed into the factorable/bilinear pieces required by the Chen-Iwaniec argument and the modulus support extends beyond the root level.

Required output is not merely `o(K/log K)`. It is an explicit inequality

\[
|\mathcal R(K)|\le C\,K^{1-\eta}(\log K)^A
\]

or an equivalent effective bound with concrete `C,eta,A`, strong enough that the certified main reserve `>0.145713553` dominates for a computable `K_0`.

## 6. Next executable action

Reconstruct the proof of the bilinear lemma at the exact four-sevenths parameters, isolate every ineffective/asymptotic `O`-constant, and derive the weakest explicit constant package actually needed. Compare its threshold with the five-ninth package before attempting any new P017-specific cancellation theorem.
