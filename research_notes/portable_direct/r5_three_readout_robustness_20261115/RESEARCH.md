# R5: Exact noise tolerance of the three-count optimizer decoder

Date: 2026-11-15. Status: AUTHOR-PROVED / EXACT-FINITE-CHECKED / NOT_REVIEWED.

## Frozen scope and source

The mathematical object is the *derived indexed-center one-dimensional radius-two observer* on 954 events, with the 28 switchable length-three gaps of frozen input commit 435e77af0d180eac32bd1f9c4c464bc4010b7551. It is an observer of Enterprise Math's preserved native X6 foundation, not a proposed lossless replacement of that native state.

Use the exact previously published optimizer-family tomography in research_notes/portable_direct/r5_global_optimizer_tomography_20261114/VERIFY_R5_GLOBAL_OPTIMIZER_TOMOGRAPHY.py at PR #2427. Its full standard-output JSON (28,337 bytes) has SHA-256 261b3945e9efdcf1a3f4be215a42b19bccac3fee9e06e2ef3bd3eba4dc279f41. Its coefficient table is the source of all numerical computations below.

The eight effective zero-based cut variables are (3,8,9,10,15,17,25,27). A closure mask b belongs to {0,1}^8. Define the exact three-integer readout

\[
F(b)=(N_b(214),N_b(223),N_b(294)),
\]

where N_b(K) is the number of *all* optimum indexed-center subsets of size K, not a selected solution or a runtime approximation. For each budget, write the previously proven Möbius coefficient representation

\[
N_b(K)=\sum_{A\subseteq b} a_A(K).
\]

The coefficients for all three budgets are taken from the frozen 954-event computation. The established three-readout theorem proves that F has 256 distinct values.

## Exact robustness theorem

Define the minimum maximum-coordinate separation over distinct closure states:

\[
D_\infty=\min_{b\ne c}\max_{j=1,2,3}|F_j(b)-F_j(c)|.
\]

An exhaustive exact-integer evaluation of all 32,640 unordered pairs yields

\[
\boxed{D_\infty=76289178155959966960189440.}
\]

Consequently, given three *integer-valued measurements* whose absolute error in **every** coordinate is at most

\[
\boxed{\delta_{\max}=38144589077979983480094719,}
\]

the original eight closure bits are uniquely decodable. This uniform integer threshold is sharp. There are 64 pairs attaining D-infinity; one pair differs only by whether cut 15 or cut 17 is closed (the state bitmasks are 16 and 32).

For independent coordinatewise *relative* errors, suppose each reported value y_j satisfies

\[
|y_j-F_j(b)|\le \varepsilon F_j(b).
\]

Define

\[
\varepsilon_*=\min_{b\ne c}
\max_{j=1,2,3}\frac{|F_j(b)-F_j(c)|}{F_j(b)+F_j(c)}.
\]

The exact rational answer is

\[
\boxed{\varepsilon_*=\frac{4022840}{4361603107999}
\approx 9.22330597349\cdot10^{-7}.}
\]

Every \(\varepsilon<\varepsilon_*\) guarantees unique recovery among all 256 states; the strict inequality is necessary for a universal guarantee when measurements may be real. Equality allows overlapping admissible error intervals. There are exactly 64 critical relative-error pairs, including the empty mask versus singleton cut 25 (bitmasks 0 and 64).

**Proof of decoding bounds.** Two distinct codewords can both explain one coordinatewise observation with errors bounded by \(\delta\) precisely when their absolute-error boxes intersect. For three independent coordinates, this first happens when \(\delta\ge\frac12\max_j|F_j(b)-F_j(c)|\). Integer measured values require \(2\delta<D_\infty\), giving the stated greatest safe integer \(\delta\). For relative-error boxes, in coordinate j the two positive count intervals first intersect at \(|F_j(b)-F_j(c)|/(F_j(b)+F_j(c))\); the three-coordinate boxes first intersect at the maximum of these thresholds. Minimizing over all pairs proves the sharp relative bound. The supplied exact integer/Fraction checker establishes the finite numerical extrema and critical-pair multiplicities by examining every pair, with no sampling.

## Information-erasure limitation

If one budget's scalar is missing, the number of distinct retained two-coordinate signatures is:

| Missing budget | Remaining distinct signatures |
|---|---:|
| 214 | 16 |
| 223 | 128 |
| 294 | 64 |

Therefore each one-coordinate deletion aliases distinct closure states. The full three-readout channel corrects bounded numeric noise but has no single-readout erasure correction.

## Reproducibility

In the original tomography source directory, run:

    python VERIFY_R5_GLOBAL_OPTIMIZER_TOMOGRAPHY.py > tomography.json

Then run the new standalone checker copied there, or invoke it by path:

    python VERIFY_R5_THREE_READOUT_ROBUSTNESS.py tomography.json > robustness.json

Expected pass status: PASS_EXACT_R5_THREE_READOUT_ROBUSTNESS. All state signatures and pair separations use Python unbounded integers; relative comparisons use exact fractions. Computation domain is **all 256 closure masks and all 32,640 unordered pairs** under the published 954-event count coefficients. This result is conditional on that source coefficient derivation, whose author-side verifier and witness input pin are stated above. Independent mathematical review is pending.

## Next scientific problems

Compute exact worst directed nearest-optimizer recourse for cut indices 3, 8, 9 and 10 over K=214..221, keeping max over all new optimizers outside min over all old optimizers. The decoder noise theorem is also useful for studying adaptive or fewer noisy count probes and observer-preserving compression; an operational realization would require a separately defined readout/noise mechanism.
