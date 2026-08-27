# Driver Review — P022 Composite Franel Equal-Depth First-Jet Reduction

Status: `DRIVER_TERMINAL / ACCEPTED_EXACT_FIRST_JET_REDUCTION / UNIVERSAL_ESCAPE_OPEN / RESULT_ONLY`

Date: `2026-08-27`

Driver-ID: `EM-DRIVER-01 / CONTROL_PLANE`

Task: `RS-P022-COMPOSITE-FRANEL-EQUAL-DEPTH-ESCAPE`

Publication: `TP2-E4537008BB8B0CCFF88F`

Canonical execution: `ER-6B71E34F8C2A991D3F10`

Canonical claim: `chatgpt-p022esc-20260827-2237-a4c91e`

Result: `RR-B8672BDFC2C7814E4EE8`

Source evidence: Draft PR `#756`, research head `5d95eab7697a7fdd45259138f357519a2451f033`, return blob `803098821d267ffd2ce90cf4894e3f340826fe83`.

## 1. Disposition

`DRIVER_DISPOSITION = ACCEPTED`.

`TASK_TERMINAL_BASIS = MINIMAL_EXACT_EXCEPTION_FROZEN`.

`RESULT_CLASS = EXACT_FIRST_P_ADIC_CORRECTION / FIRST_JET_TRICHOTOMY / RESULT_ONLY`.

`UNIVERSAL_COMPOSITE_ESCAPE_CLOSURE = NOT_PROVED`.

`ADMISSIBLE_EQUAL_DEPTH_WITNESS = NOT_FOUND`.

`P022_SIMPLE_SIMPLE_HASSE_JET_EXCEPTION = OPEN`.

`P022_DOUBLE_DEEP_HASSE_JET_EXCEPTION = OPEN_AS_NONEMPTINESS_QUESTION`.

`FOUNDATION_MUTATION = NONE`.

`WORKING_TRUTH_PROMOTION = NONE`.

`TOOLBOX_MUTATION = NONE`.

The result is accepted exactly at the taskbook-authorized stopping strength. It derives the next exact p-adic correction at the forced midpoint and reduces the surviving equal-depth mechanism to explicit first-jet status loci. It does not prove that the equal-depth signature is impossible for every admissible prime.

## 2. Canonical claim authority

Issue `#240` contains two nearly simultaneous CLAIM comments for the same task generation. Server ordering is decisive:

- comment `5440748806`: `chatgpt-p022esc-20260827-2237-a4c91e`, researcher `EM-P022ESC-A4C91E`;
- comment `5440752923`: `chatgpt-p022ce-20260827-2237`, researcher `EM-P022CE-84B7D1`.

The first server-backed CLAIM owns the live lease. A second CLAIM cannot preempt it. Therefore `EM-P022ESC-A4C91E / ER-6B71E34F8C2A991D3F10 / RR-B8672BDFC2C7814E4EE8` is the sole canonical execution lineage for this publication generation. The later claim is non-authoritative overlapping evidence unless explicitly re-routed after lease release.

This review does not synthesize the later claim as parallel co-authority.

## 3. Provenance normalization

The source result record in research head `5d95eab...` contains

`frozen_at = 2026-08-27T14:58:00+00:00`

even though GitHub's server-authenticated commit time for the result-freeze commit is

`2026-08-27T14:50:34+00:00`.

The declared timestamp therefore cannot be literal provenance for that already-written record.

Driver integration corrects only this control-plane metadata field to the server-authenticated result-freeze commit time:

`frozen_at = 2026-08-27T14:50:34+00:00`.

The logical result identity is unchanged because the canonical `result_id` depends on task, execution record, return blob and owner head, not on `frozen_at`. The research return blob, checker blob, execution record blob, taskbook pin, owner head and all mathematical text are preserved exactly.

Original source result-record blob: `492477c03d435f14ee544093389d8f8bb06970e9`.

Normalized mainline result-record blob: `6a7b2f4477d87a6e5f9805257b8fe4b92db53f65`.

## 4. Independent mathematical audit

Let

\[
p=6k-1,\qquad m=\frac{p-1}{2}=3k-1.
\]

For `0 <= j <= m`, the exact identity

\[
\binom mj
=
(-1)^j\frac{\binom{2j}{j}}{4^j}
\prod_{r=0}^{j-1}\left(1-\frac{p}{2r+1}\right)
\]

is correct in the p-local ring. Cubing and truncating modulo `p^2` gives

\[
\binom mj^3
\equiv
a_j\left(
1-3p\left(H_{2j}-\frac12 H_j\right)
\right)\pmod{p^2},
\]

where

\[
a_j=(-1)^j\binom{2j}{j}^3 64^{-j}.
\]

Summation therefore yields the exact correction

\[
F_m\equiv S_p-3pT_p\pmod{p^2},
\]

with

\[
S_p=\sum_{j=0}^m a_j,\qquad
T_p=\sum_{j=0}^m a_j\left(H_{2j}-\frac12H_j\right).
\]

In the frozen forced-midpoint sector `p = 5 or 7 (mod 8)`, the accepted owner theorem gives `p | F_m`, and `S_p ≡ F_m (mod p)`, so `p | S_p`. Hence

\[
C_p:=S_p/p\pmod p
\]

is well-defined in the p-local ring. Division by `p` is therefore legitimate, not a formal cancellation of a nonzero residue.

Using the accepted harmonic pairing

\[
U_p\equiv2T_p\pmod p
\]

gives

\[
\boxed{
2F_m/p\equiv2C_p-3U_p\pmod p.
}
\]

Consequently,

\[
v_p(F_m)=1
\iff
2C_p-3U_p\ne0,
\]

and

\[
v_p(F_m)\ge2
\iff
2C_p-3U_p=0.
\]

For the third-minus Franel value let

\[
n=2k-1=\frac{p-2}{3}.
\]

The frozen Whipple specialization gives only the needed mod-`p` zero equivalence

\[
F_n\equiv2^nP_p(1)\pmod p.
\]

On the scalar-Hasse locus `P_p(1)=0`, define

\[
W_p:=2^{-n}F_n/p\pmod p.
\]

This is a definition from the Franel quotient on a locus where `p | F_n`; it does **not** assume or infer a mod-`p^2` Whipple transformation. Since `2^n` is a p-unit,

\[
v_p(F_n)=1\iff W_p\ne0,\qquad
v_p(F_n)\ge2\iff W_p=0.
\]

Combining the two exact quotient tests gives the claimed first-jet trichotomy:

1. `W_p != 0` and `2C_p-3U_p != 0`: both depths are exactly one;
2. exactly one vanishes: the depths differ, so the equal-depth escape is killed;
3. both vanish: both depths are at least two and only then is a second-jet comparison relevant.

Under the already-frozen earlier-escape hypotheses, the simple-simple locus therefore is an exact first-order surviving condition, while the double-deep locus is the only branch that can require higher p-adic depth.

## 5. Independent finite regression

The task-local checker was independently replayed rather than trusted as a theorem oracle.

For all target-sector primes

\[
p<5000,\qquad p\equiv5\pmod6,\qquad p\equiv5\text{ or }7\pmod8,
\]

there are `168` cases. Independent exact integer/modular evaluation found:

- `0` failures of the mod-`p^2` midpoint expansion;
- `0` failures of the quotient first-jet identity;
- `0` failures of `U_p=2T_p`;
- `0` scalar-Hasse zero candidates in that finite range.

This remains finite regression only. The zero observed scalar-Hasse candidates do not establish emptiness of either exceptional locus.

## 6. Method harvest

`METHOD_HARVEST = RESULT_ONLY`.

The new content is a task-local p-adic first correction obtained by expanding the exact midpoint binomial product and then composing it with an already-accepted harmonic pairing. It does not justify a new general-purpose project tool family or Foundation primitive.

## 7. Successor gate

A genuine information gap remains after this task:

\[
P_p(1)=0
\]

does not yet determine the joint first-jet status of

\[
W_p
\quad\text{and}\quad
J_p:=2C_p-3U_p.
\]

This gap is narrower than the parent composite Franel problem and has discriminating outcomes:

- an exact incompatibility forcing exactly one of `W_p,J_p` to vanish closes the equal-depth channel at first order;
- an admissible simple-simple witness (`W_p != 0`, `J_p != 0`) freezes a concrete surviving equal-depth exception;
- a proof or exact witness that `W_p=J_p=0` is attainable establishes nonemptiness of the double-deep locus and alone justifies a later second-jet task.

No current open task or open research return was found that already owns this exact first-order compatibility question. The live legacy P022 observation-history execution concerns the separate `q=3r-1` first-reentry boundary and is not a substitute.

Accordingly, one narrow typed continuation is authorized. It must not reopen the broad composite route, replace proof by a larger cutoff, assume generic p-adic independence, or begin second-jet mathematics before nonemptiness of the double-deep locus is established.

## 8. Final control state

`RR-B8672BDFC2C7814E4EE8 = ACCEPTED / TERMINAL_MINIMAL_EXACT_EXCEPTION`.

`TP2-E4537008BB8B0CCFF88F = TERMINAL_BY_TASKBOOK_EXACT_BLOCKER_STOPPING_RULE`.

`FORCED_MIDPOINT_MOD_P2_CORRECTION = ACCEPTED`.

`PAIRED_MIDPOINT_FIRST_JET = ACCEPTED`.

`FIRST_JET_TRICHOTOMY = ACCEPTED`.

`UNIVERSAL_EQUAL_DEPTH_ESCAPE_CLOSURE = OPEN`.

`CANONICAL_EXECUTION = EM-P022ESC-A4C91E / ER-6B71E34F8C2A991D3F10`.

`LATER_DUPLICATE_CLAIM = NON_AUTHORITATIVE`.

`NEXT_CONTROL_PLANE_ACTION = PUBLISH_ONE_NARROW_HASSE_MIDPOINT_FIRST_JET_COMPATIBILITY_SUCCESSOR`.
