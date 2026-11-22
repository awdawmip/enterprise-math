# R5 S4 jet repair completed: primitive 31, phase 59

Date: 2026-11-22 (Asia/Shanghai). Status: AUTHOR_EXACT_CORRECTION / CHARACTERISTIC_ZERO_THREE_POINT_CROSSCHECKED / NOT_REVIEWED. This extension resolves the sole remaining open proof dependency in the earlier RESEARCH.md in this directory. That document's 227/228 figure describes the intermediate audit state; the **current corrected result is 228/228 conditional on the existing six-cone pole lemma**. Historical authorship and immutable inputs are unchanged.

## Theorem and exact model

Let R_m(q)=1-(1-A_m(q))(1-B_m(q))(1-C_m(q)) be the original five-event union numerator at the frozen source enterprise-math@75d986aa23b68a7ecf9b29dc1006f0e322b35a15. The three overlapping short events have supports S0={214,...,218}, S1={214,216,217,218,219,220,221}, S2={215,216,217,218,219,220,221}; B uses 223..290, and C uses 296..312. Write dot R=q dR/dq.

Fix a primitive 31st root z and define c2 as coefficient of z² in the unique integral cyclotomic basis 1,z,...,z²⁹. Every individual signed inclusion-exclusion term in A has a factor (1-q²¹⁷), so A_m(z)=0 for every m. The B block contains 248 and 279 (two multiples of 31), so B_m(z)=dot B_m(z)=0. C_m(z)=0 because Z contains 310. Thus R_m(z)=0 and dot R_m(z)=dot A_m(z)+dot C_m(z).

For **all integers h≥0**, conditional on the previously archived exact six-cone pole-degree bound,

\[
\boxed{c_2(\dot R_{59+62h}(z))=-6727(h+1)\ne0.}
\]

This is the missing all-threshold primitive-31 phase-59 certificate. Nonvanishing at one primitive root implies nonvanishing at all primitive conjugates.

## Proof

In every nonempty subset of the three overlapping short events, retain the full vector of event loads in the exact integer DP for Q_mask,m(q). The only 31-divisible price in each corresponding U_mask is 217. Consequently

\[
\dot D_{U_{\mathrm{mask}}}(z)
=-217\prod_{p\in U_{\mathrm{mask}}\setminus\{217\}}(1-z^p)
\]

and

\[
\dot A_m(z)=
\sum_{\mathrm{mask}\ne\emptyset}(-1)^{|\mathrm{mask}|+1}
Q_{\mathrm{mask},m}(z)\dot D_{U_{\mathrm{mask}}}(z).
\]

The included exact C++17 program VERIFY_D31_EXACT_THREE.cpp computes these integrally in Z[q]/(q³¹−1), then reduces to the 30-dimensional cyclotomic basis. For thresholds m=59,121,183, the nonzero coordinates of dot A are at indices 2..6:
- m=59: [-6727,-53816,-47089,-40362,-6727]
- m=121: twice that vector
- m=183: three times that vector.

The **true**, rather than previously substituted, Z block contribution is

\[
C_m(q)=\prod_{p=296}^{312}(1-q^p)
\sum_{j=0}^{m-1}h_j(q^{296},\ldots,q^{312}).
\]

The corrected exact integer complete-homogeneous recurrence from VERIFY_CBLOCK_JETS.py gives dot C at the same three thresholds, in cyclotomic basis, with only coordinate 0 nonzero; values -19220, -38440 and -57660 respectively. Therefore

\[
(c_2(\dot R_{59}),c_2(\dot R_{121}),c_2(\dot R_{183}))
=(-6727,-13454,-20181).
\]

The existing six-cone rational-generating-function statement at enterprise-math@e0176cd68a434192899a5a1de746c2c66b5946dc has maximal t-pole order μ31=3. Because the A numerator has the exact vanishing factor at q=z, the fixed-phase first Euler jet dot A_{59+62h}(z) is polynomial of degree at most 2 in h, for all h≥0, without finite initial exceptions. For the true C numerator, the first derivative along the same residue progression is polynomial of degree at most one, by its exact finite-threshold root-of-unity generating function. Hence c2(dot R) has degree at most 2. Its three exact characteristic-zero values uniquely determine the polynomial as -6727(h+1). This establishes infinite nonvanishing without extrapolating a finite sample.

The C++ program was compiled and executed both in optimized C++17 and with -fsanitize=undefined -fno-sanitize-recover=all; outputs matched byte-for-byte, with no reported UB. The previous 228-row archive has been fully rescored with the corrected C. Exactly 223 original selected coordinate polynomials remain same-sign; four more have linear roots strictly between 0 and 1 (not integer h); the remaining d31/r59 is discharged by the new c2 polynomial. Thus all **228/228** primitive-order phase arguments are recovered, conditional on the degree lemma.

## Scope, dependencies and next

This repairs the incorrect S4 first-jet implementation visible in earlier d23 and six-order helper sources, without rewriting their immutable records. The d23 corrected five-phase witnesses are contained in the accompanying RESEARCH.md and verified by VERIFY_CBLOCK_JETS.py. The prior 91-class and eight-regime global R5 results retain author-side conditional status: their d31/r59 dependency is now repaired, whereas the independent mathematical review of their other denominator/pole and primitive29/32/43 arguments remains outstanding. The present proof is a scalar observer result, not a P000/X6 native theorem.

Next: independently inspect the complete six-cone pole-degree derivation, verify other dependent derivative tables with correct total-multiplicity event numerators, and then pursue a typed lossless BRC/native-X6 observation bridge. Activity bookkeeping and formal CLAIM/RUN/Review remain governed by separate current authority.
