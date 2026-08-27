# Driver Review — Prime Coordinate N-only Valuation-Wall GCD Extractor Independent Replay

Status: `DRIVER_FINAL / ACCEPTED / TASK-TERMINAL / EXACT_N_ONLY_GCD_EXTRACTOR / NO_SPEEDUP_CLAIM / FOLLOWUP_PUBLISHED`

Date: `2026-08-27`

Driver-ID: `EM-DVR-PCF827 / CONTROL_PLANE`

Task: `RS-PRIME-COORD-FACTOR-NONLY-VALUATION-WALL-GCD-EXTRACTOR-INDEPENDENT-REPLAY`

Publication: `TP2-DF186CDB4959BEA10875`

Execution: `ER-85F5DF86C52A676ADAD0`

Researcher-ID: `EM-PCF4R-D74517`

Result: `RR-F24971D684C868A325E2`

Integrated result commit: `cc0106285c579998747c3e777c11c35a3304a274`

Source PR: `#732`

## 1. Driver disposition

`DRIVER_DISPOSITION = ACCEPTED`.

`TASK_SCOPE = TERMINAL`.

`RESULT_CLASS = EXACT_N_ONLY_GCD_EXTRACTOR / RESULT_ONLY`.

`N_ONLY_GCD_EXTRACTOR_VERIFIED = ACCEPTED`.

`FACTORIZATION_SPEEDUP_PROVED = FALSE`.

`FOUNDATION_MUTATION = NONE`.

`WORKING_TRUTH_PROMOTION = NONE`.

`TOOLBOX_MUTATION = NONE`.

The result meets every load-bearing obligation of the published hard target. It independently reconstructs and closes the N-dependent valuation-wall splitter on the stated domain, while preserving the previously accepted fixed-public-prefix no-go as a separate restricted theorem.

The accepted theorem is structural and algorithmic correctness, not asymptotic superiority.

## 2. Accepted exact theorem

Let

\[
N=pq,\qquad 3<p<q
\]

with distinct odd primes, and define

\[
A_s
=
\frac{(2s)!(3s)!}{(s!)^5}
=
\binom{2s}{s}^2\binom{3s}{s}.
\]

For every prime `r>3` and `0<=s<r`, the return correctly proves

\[
v_r(A_s)
=
\left\lfloor\frac{2s}r\right\rfloor
+
\left\lfloor\frac{3s}r\right\rfloor,
\]

hence, because `r` is not divisible by `3`,

\[
r\mid A_s
\iff
3s>r.
\]

The first local wall is therefore `ceil(r/3)`.

For the public dyadic sequence `s=1,2,4,...`, let `s_*` be the first seed with `gcd(A_s,N)>1`. The proof that `s_*<p<q` is valid. Therefore the local valuation law applies simultaneously to both hidden factors and yields the exact first-stop alternative

\[
\gcd(A_{s_*},N)\in\{p,N\}.
\]

If the first response is `p`, extraction is complete.

If the first response is `N`, writing `u=s_*/2` gives

\[
3u<p<q<6u,
\]

and therefore

\[
q<2p.
\]

This synchronization implication is accepted exactly.

## 3. Accepted synchronized fallback

In the synchronized branch define the public seed

\[
t=\left\lfloor\frac{\sqrt N}3\right\rfloor.
\]

The return correctly proves `t+1<p`, so the same local valuation law remains valid for both factors at both fallback seeds.

It then proves the exact alternative

\[
\gcd(A_t,N)=p
\]

or

\[
\gcd(A_t,N)=1
\quad\text{and}\quad
\gcd(A_{t+1},N)=p.
\]

The three-integer-block argument excluding two distinct odd primes greater than `3` from the interval immediately above `3t` is valid.

A small implementation detail is also consistent with the theorem path: in the synchronized branch `sqrt(N)<q<3s_*`, hence `t<s_*`; the fallback residues lie within the already reached public streaming range and do not require a hidden-factor jump.

## 4. Constructor admissibility and modular recurrence

The constructor uses only:

- `N`;
- public integer constants;
- public dyadic indices;
- integer square root;
- modular arithmetic;
- gcd.

No hidden `p`, `q`, factor-labelled coordinate, CRT idempotent, prime enumeration or trial-factor query enters constructor control.

The recurrence

\[
A_s
=
A_{s-1}
\frac{6(2s-1)(3s-2)(3s-1)}{s^3}
\]

is exact. The replay additionally proves that every index actually inverted before theorem termination is `<p`. Therefore `gcd(s,N)=1` on the theorem path, and modular inversion of `s^3` is legitimate. The implementation's pre-inversion gcd guard also turns any unexpected nonunit into an immediate valid factor branch.

This closes the principal composite-modulus safety concern.

## 5. Complexity boundary

The replay's streaming implementation uses only `O(log N)` live memory, but still performs `O(p)` modular recurrence updates.

Thus on balanced semiprimes the method remains exponential in the bit length.

Freeze:

`EXACT_N_ONLY_SPLITTER != GENERAL_FACTORING_SPEEDUP`.

No polynomial-time, sub-square-root, exponent-one-fifth-beating, or external-novelty claim is accepted by this review.

## 6. Evidence and independence boundary

The immutable result manifest pins the durable return, Phase-A freeze and independent checker. The reported finite guard

`PASS valuation_checks=76122 recurrence_checks=357 exhaustive_semiprimes=4278 synchronized_cases=928 adversarial_semiprimes=2000`

is accepted as regression evidence only; universal closure rests on the exact proof.

Phase B compares the independent derivation against supplemental Draft PR `#715` and finds agreement on all load-bearing theorem components, with a distinct fallback proof and a stronger low-memory modular implementation.

One provenance wording correction is binding for future summaries:

- PR `#715` itself existed before the Phase-A freeze;
- therefore “opened against PR #715 in Phase B” must be read as **source exposure/comparison after the blind-forward freeze**, not PR creation after the freeze;
- this Driver does not use the PR creation timestamp as evidence of independence.

The accepted independence claim is limited to the task's disclosed blind-forward protocol and frozen Phase-A artifact/checker sequence.

## 7. CI/control-plane boundary

The source PR `#732` had a `reference-integrity` failure at its head, but the failing step was unrelated to PCF4R: it reported a pre-existing publication fork for `RS-P022-OBSERVATION-HISTORY`. The citation/lineage integrity step passed.

Current main separately resolves that P022 publication-authority fork at commit

`82c0b71cf91644e6c18a3d2311bd3d374cf4475d`.

Accordingly, the historical red check is not treated as a mathematical or lineage defect in `RR-F24971D684C868A325E2`. This review does not retroactively claim that every source-PR CI job was green.

## 8. Portfolio routing

The parent hard target has no in-scope residue. Do not keep PCF4R open merely to optimize its runtime.

PCF2 already owns the sealed benchmark suite and remains active in parallel. PCF3 and PCF6 likewise retain their independent program lanes.

The highest-leverage new gap is proof-level **complexity compression of the now-accepted valuation-wall splitter**.

Successor task:

`RS-PRIME-COORD-FACTOR-VALUATION-WALL-COMPLEXITY-COMPRESSION`

Publication:

`TP2-B6DC0E56825472276091`

The successor must determine whether the required sparse public kernel values can be reached without `Theta(p)` sequential streaming, with full composite-modulus safety and end-to-end bit-complexity accounting.

It must compare any claimed gain against classical product-tree/Pollard-Strassen factoring and the current exponent-one-fifth deterministic factoring line. An `N^(1/4+o(1))` implementation is not, by itself, a general deterministic factoring breakthrough.

## 9. Final freeze

`RR-F24971D684C868A325E2 = ACCEPTED`.

`TP2-DF186CDB4959BEA10875 = TASK-TERMINAL`.

`ACCEPTED_SCOPE = EXACT_N_ONLY_GCD_EXTRACTOR / NO_SPEEDUP_CLAIM / RESULT_ONLY`.

`UNRESOLVED_RESIDUE_WITHIN_PARENT_TASK = NONE`.

`DESTINATION = FOLLOWUP_TASK / TP2-B6DC0E56825472276091`.

`NEXT_FRONTIER = VALUATION_WALL_FAST_EVALUATION_AND_COMPLEXITY_COMPRESSION`.
