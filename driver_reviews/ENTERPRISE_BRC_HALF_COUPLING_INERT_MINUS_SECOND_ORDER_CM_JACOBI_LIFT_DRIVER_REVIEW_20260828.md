# Driver Review — Enterprise BRC Inert-Minus Second-Order CM/Jacobi Lift

Status: `DRIVER_FINAL / ACCEPTED_AT_STRICT_EXACT_REDUCTION_STRENGTH / FULL_PROOF_NOT_CLOSED / FINITE_CLAUSEN_SWISHER_BRIDGE_ROUTED`

Date: `2026-08-28`

Driver-ID: `EM-DVR-C8A7F2 / CONTROL_PLANE`

Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-MINUS-SECOND-ORDER-CM-JACOBI-LIFT`

Publication: `TP2-05DB03EAF4E1DDCDBDF2`

Claim: `chatgpt-ebp5m2-20260828-1411-d74849`

Execution: `ER-69F4296978826B9EBFA6`

Result: `RR-FFAA492DFF8FEBC025B5`

Follow-up publication: `TP2-6649B392FDDD742C0275`

## 1. Final disposition

`DRIVER_DISPOSITION = ACCEPTED`.

`ACCEPTED_SCOPE = STRICT_EXACT_REDUCTION_TO_SINGLE_FINITE_CLAUSEN_SWISHER_BRIDGE`.

`PARENT_FULL_CONGRUENCE_PROOF = NOT_ACCEPTED`.

`SUN_A14II = CONJECTURAL_IDENTIFICATION_ONLY / NOT_IMPORTED_AS_PROVED`.

`WORKING_TRUTH_PROMOTION = NONE`.

`FOUNDATION_MUTATION = NONE`.

`TOOLBOX_PROMOTION = NONE`.

The source result is accepted exactly as a negative-boundary reduction: it closes the parent task's reduction interface but does not prove the inert-minus supercongruence.

## 2. Decisive exact audit

The return gives an exact finite symmetrization of the predecessor triangle. With

\[
B_k=\frac{(1/6)_k(1/3)_k}{(k!)^2}2^{-k},
\]

the product is symmetrized so that

\[
G_pH_p=\sum_{0\le i,j<p}(1+6(i+j))B_iB_j,
\]

and subtracting the finite tail leaves the triangle `i+j<p`. Clausen coefficient extraction is coefficientwise and finite at every degree:

\[
\sum_{i=0}^n B_iB_{n-i}
=
\frac{(1/2)_n(1/3)_n(2/3)_n}{(n!)^3 2^n}
=
\frac{\binom{2n}{n}^2\binom{3n}{n}}{216^n}.
\]

Therefore the accepted exact identity is

\[
S_p=W_p
\]

with

\[
W_p=\sum_{n=0}^{p-1}(6n+1)
\frac{\binom{2n}{n}^2\binom{3n}{n}}{216^n}.
\]

Combined with the predecessor's already-frozen base-\(p\) expansion, this proves the exact equivalence

\[
(R0-)\ \&\ (R1-)
\iff
W_p\equiv-p\pmod{p^3}
\]

for `p ≡ 17,23 (mod 24)`.

## 3. Valuation and finite-truncation audit

The frozen valuation formula

\[
v_p\!\left(\binom{2n}{n}^2\binom{3n}{n}\right)
=
\left\lfloor\frac{2n}{p}\right\rfloor+
\left\lfloor\frac{3n}{p}\right\rfloor
\]

implies that for `p ≡ 2 (mod 3)` and

\[
M=\frac{2p-1}{3},
\]

all terms with `n>M` vanish modulo `p^3`. Thus the open congruence is equivalent to a genuinely finite truncation and not to an uncontrolled infinite-series substitution.

## 4. Classical-source boundary

The weighted congruence is exactly the `a=1` target-class specialization of Zhi-Wei Sun Conjecture A14(ii). That identification is accepted only as prior-conjecture classification. It is not a proof source.

The independently checked Swisher 2015 congruence supplies the proved finite comparison

\[
E_p:=\sum_{k=0}^{M}(-1)^k(6k+1)\frac{(1/3)_k^3}{(k!)^3}
\equiv -2p\pmod{p^3}
\]

for primes `p ≡ 2 (mod 3)`. Therefore the parent target is equivalent to the single finite bridge

\[
C_p:=
2\sum_{k=0}^{M}(6k+1)
\frac{(1/2)_k(1/3)_k(2/3)_k}{(k!)^3 2^k}
-
E_p
\equiv0\pmod{p^3}.
\]

The analytic infinite identity does not close this finite statement because its truncation boundary has the wrong direction unless separately controlled.

## 5. Regression and method audit

The supplied checker verifies finite Clausen coefficients, the valuation formula, bounded instances of the weighted congruence, the Swisher bridge, and a Domb-side diagnostic. These finite scans are retained only as falsification/regression evidence.

`METHOD_HARVEST = RESULT_ONLY`.

`TOOL_COVERAGE = NOT_APPLICABLE_FOR_NEW_GENERAL_PURPOSE_TOOL`.

The return identifies two structurally distinct continuation lanes—terminating hypergeometric/Swisher and Domb/modular—but does not establish a new reusable tool family.

## 6. Successor-gate audit

A follow-up is justified by a new exact information gap, not by the parent reaching a positive stage verdict.

The prior all-inert finite-Clausen task asked for control of the full finite convolution correction and all four inert residue classes. Subsequent accepted reductions separated the minus route, closed the unit-tail mod-`p` cancellation layer, reduced the minus route to `(R0-),(R1-)`, and this result now reduces those two congruences to the single finite certificate `C_p`.

The new gap is therefore strictly smaller than the old Clausen mother question.

Alternatives considered:
- close the minus route at strict-reduction strength and return to another portfolio route;
- keep the work inside the parent task;
- return to unrestricted/free hypergeometric exploration;
- use the independent Domb/modular route instead of a terminating bridge.

A separate continuation is preferred because the parent task's two-scalar CM/Jacobi interface is now terminal as a reduction object, while `C_p` is a new self-contained finite proof obligation with its own kill conditions and prior-art boundary. Portfolio priority is kept below P1 to avoid turning repeated route success into automatic top priority.

## 7. Final control state

`RR-FFAA492DFF8FEBC025B5 = ACCEPTED_AT_STRICT_EXACT_REDUCTION_STRENGTH`.

`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-MINUS-SECOND-ORDER-CM-JACOBI-LIFT = TERMINAL_AT_TASK_SCOPE_AFTER_FOLLOWUP_MATERIALIZATION`.

`FULL_INERT_MINUS_TARGET = OPEN`.

`SMALLEST_EXACT_RESIDUE = FINITE_CLAUSEN_SWISHER_BRIDGE`.

`FOLLOWUP = RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-MINUS-FINITE-CLAUSEN-SWISHER-BRIDGE / TP2-6649B392FDDD742C0275`.
