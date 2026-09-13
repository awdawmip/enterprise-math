# BRC hidden moments: shortcut coverage and observer composition audit

Status: `RESEARCH NOTE / EXACT OBSERVER COUNTEREXAMPLES / BOUNDED KNOWN-FACTOR FIXTURES / NO N-ONLY EXTRACTOR`
Date: `2026-09-08`
Researcher-ID: `EM-HME-0CE4FD / TASK_RESEARCH`
Global snapshot: `c1c3610234637bd1309e29474c306a0db3040ad8`.
Parent result: `998cff8f0404c26495847baffae66adecf4af1fb`, `research_notes/BRC_HIDDEN_MOMENT_EXTRACTION_20260908.md`.
Tool reference snapshot: `c5d6e6ed4aa4c899706e2a895f55733dc2eb3cb8`.
Scope: Continue the mathematical audit, review the existing shortcut inventory, and verify small known-factor witnesses. No real RSA challenge modulus, factor-search solver, autonomous attack pipeline, or external result submission was used.

## 1. Concrete continuation result

The existing BRC shadow uses more than `N mod m`: it reads the integer square root and remainder of the complete input. The previous product-residue involution alone therefore does not establish a limitation for this interface.

Executing the unchanged actual interface nevertheless supplies a direct counterexample at its **default modulus 64**. Even after adding `S^2 mod 64`, exact bit length, and the complete integer square root, that observation vector does not determine `H3=9M3 mod 64`.

This is a statement about a specific observer. It is not a factoring lower bound, a failure of the telemetry function at its intended task, or an impossibility theorem for arbitrary calculations on complete N.

## 2. Pinned source coverage

The following source notes were consumed without repeating their factor searches or historical benchmarks:

- `research_notes/BRC_OPPORTUNISTIC_SHORTCUT_PORTFOLIO_20260907.md`, sections 1 through 5, at the tool reference snapshot;
- `research_notes/BRC_MULTIPLIER_FACTOR_BRIDGE_20260906.md`, sections 0 through 3, at that same snapshot;
- `src/enterprise_math/brc_opportunistic_shortcuts.py`, blob `1214aa09770893fb3de7f85b994d1994ff56bffe`.

The executed local module matched the referenced source after normalizing line endings. Its actual byte SHA256 appears in the certificate. Only `brc_shadow_signature` was called; no candidate-order generator, filter cascade, factor routine, complete fallback, or backend transport was executed.

Reuse resolution: `REUSE_EXECUTED` for the actual N-visible shadow readout, `REUSE_APPLIED` for the documented interface/precondition audit. This work adds a task-specific counterexample certificate, not a new general-purpose tool family.

| Preserved inventory item | Documented role | Relevance to the hidden-moment question |
|---|---|---|
| Same-parity structural priority | Reorders candidates | A better order does not itself output a hidden moment. |
| Learned fixed prefix | Bounded empirical ordering improvement | Held-out rank and actual runtime are separate claims. |
| Ratio-band prefix | Specialist ordering | Its regime signal must be available; the hidden factor ratio cannot be assumed as free input. |
| Materialized-gap sorting | Sorts already computed states | Generation and storage of those states belong in the cost. |
| Small kernel prefix | Incomplete early coverage | Completeness comes from its fallback, not the prefix. |
| Square-gap residue filter | Exact necessary-condition rejection | Passing the filter is not a sufficient witness or branch selection. |
| Table-free tail | Conditional storage/transport option | Representation savings do not prove extraction of a new observable. |
| Quotient/remainder jet | Updates known arithmetic state | Its validity conditions and initialization cost remain part of the computation. |
| Energy difference jet | Reduces arithmetic work during updates | Faster updates do not establish a new information source. |
| Completion-gap residue jet | Transports existing residues | Previously computed state cannot be charged as free hidden-moment access. |
| Pisano/rank metadata route | Uses already available metadata | Acquiring metadata is a separate obligation; availability cannot be assumed. |
| Cheap BRC shadow | Exact telemetry from N, root, remainder and phase | Directly audited below; the source does not claim it is a moment extractor. |
| Fibonacci/delete-code compression | Storage specialization | The documented storage benefit is distinct from factor information. |

The portfolio's documented exactness after a heuristic miss depends on completing a structural fallback. Under the user's instruction against hard computation, declining that fallback leaves an **inconclusive bounded probe**, not a completeness guarantee. No executor implementing such probes or a public-challenge dispatcher is introduced here.

The existing inventory remains useful for its stated tasks. None of these cited contracts claims to output the actual signed cubic moment from N. That is a capability gap in the documented interfaces, not a theorem that all combinations must fail.

## 3. Actual shadow definition and first scope correction

For a positive integer N, define

`J=floor(sqrt(N))`, `R=N-J^2`,

`Q=min(3, floor(4R/(2J+1)))`.

The existing function validates `J^2+R=N` and `0<=R<=2J`, and returns

`O_m(N)=(N mod m, J mod m, R mod m, Q)`.

Its default m is 64. In general O_m is not determined by N mod m. In particular, the preceding note's pair N=39 and N=119 is separated by the actual API at m=5:

- N=39: `M5:N4:J1:R3:Q0`;
- N=119: `M5:N4:J0:R4:Q3`.

Thus that earlier pair must not be reused as a counterexample against this richer observer.

## 4. Counterexample at the actual default modulus

With `S=p+q`, `U=S^2`, and `H3=2S^3-9NS`, the exact certificate is:

| Quantity | First known-factor input | Second known-factor input |
|---|---:|---:|
| p,q | 97,181 | 67,263 |
| N | 17557 | 17621 |
| S | 278 | 330 |
| bit length | 15 | 15 |
| exact J | 132 | 132 |
| exact R | 133 | 197 |
| N mod 64 | 21 | 21 |
| J mod 64 | 4 | 4 |
| R mod 64 | 5 | 5 |
| Q | 2 | 2 |
| U mod 64 | 36 | 36 |
| E3 mod 64 | 10 | 10 |
| H3 mod 64 | 50 | 46 |

Both actual function calls return exactly `M64:N21:J4:R5:Q2`.

Consequently no single-valued function of

`(O_64(N), U mod 64, bit_length(N), exact J)`

equals `H3 mod 64` for every distinct-odd-prime semiprime in the tested domain, and hence not for all such semiprimes. The finite counterexample establishes that exact universal negation; no inference about asymptotic rates is involved.

Even U was supplied as an extra oracle coordinate in this test. It was not extracted by the API. Failure of this stronger observation vector implies failure of any restriction of that same vector.

A smaller auxiliary example at m=5 uses N=679=7*97 and N=689=13*53. Both have exact J=26, bit length 10, U mod 5=1, and the same signature `M5:N4:J1:R3:Q0`, but H3 residues are 4 and 1.

The complete R distinguishes these rows. Using it is outside the stated compressed-observer model. In fact exact J and R reconstruct N, so this result cannot be used to claim a limitation for arbitrary algorithms given complete N.

## 5. Closure under nonlinear or adaptive postprocessing

Let x and y have the same declared observation O. Suppose a procedure obtains every subsequent response from deterministic functions of O and its existing transcript, and chooses subsequent operations only from that transcript.

Induction on steps shows that the transcripts for x and y remain identical: the initial observations agree; the next operation and the response to it consequently agree. Therefore all final outputs agree.

The same statement holds for randomized procedures when the same random tape is coupled to both inputs: their output distributions coincide. Random guessing cannot create a faithful distinction absent from the observation.

Applying this to the default-modulus witness rules out recovering H3 mod 64 by merely taking powers, combinations, nonlinear classifiers, or adaptive choices from the stated compressed vector. It does not cover a fresh arithmetic query on full N, a new modulus containing genuinely additional information, or independently obtained metadata. Those would need their own evidence and cost analysis.

This is the appropriate composition boundary for the tool audit. It would be incorrect to classify every shortcut in the inventory as a function of this one shadow; many consume full arithmetic states.

## 6. CRT preserves existing local ambiguity

For fixed known U and n modulo an odd prime l, simultaneous negation of the formal local pair `(a,b)` preserves `(ab,(a+b)^2)` and changes

`H=(a+b)(2a-b)(a-2b)`

to -H. If H is nonzero modulo l, these are two distinct output residues.

For a product of r distinct odd primes and a local pair with nonzero H in every component, the sign choices in the separate components produce `2^r` distinct H residue vectors with the same product and squared-sum observations. CRT represents those already different local vectors as residues of the product modulus; it does not identify the actual one.

An explicit fixed example with modulus 55 is:

| Local pair a,b | ab mod 55 | (a+b)^2 mod 55 | H mod 5 | H mod 11 | H mod 55 |
|---|---:|---:|---:|---:|---:|
| 3,13 | 39 | 36 | 1 | 2 | 46 |
| 8,53 | 39 | 36 | 1 | 9 | 31 |
| 47,2 | 39 | 36 | 4 | 2 | 24 |
| 52,42 | 39 | 36 | 4 | 9 | 9 |

All rows have H^2 mod 55=26. Their integral-scaled even centered moments of `{0,a,b}` through degree 12 also agree modulo 55, as predicted by the preceding all-order symmetric-polynomial result.

These are formal local residue pairs, not four factorizations of the complete integer 39. No claim is made that arbitrary local assignments arise in an imposed full-N or prime population. Nor is this a proof that CRT applied to genuinely extracted additional data is useless.

## 7. Bounded verification and public-record context

The first fixture uses 276 distinct products of known odd primes below 100. The second predetermined fixture covers 13,861 distinct products of known odd primes below 1,000, with every N below one million. Its purpose is to test the actual default modulus once. All products are generated from their known factors; no factor routine is run on an unknown N. The observed command completed in under one second on this host; this is incidental wall-clock evidence, not a cross-platform benchmark.

Only fixed-size modular and integer-square-root observations are evaluated. Four explicit local residue rows verify the CRT example using independent exact Fraction central moments. The certificate includes the input witnesses, module fingerprint, source pins, counts and scope limits.

Reproduction after placing the companion script under `experiments/`:

`python experiments/brc_hidden_moment_observer_audit_20260908.py --enterprise-root <checkout-containing-the-pinned-module> --output-dir <scratch-directory>`.

Public RSA challenge records were consulted as literature only. The authors' [computation record](https://members.loria.fr/EThome/computations/) and [2020 paper](https://arxiv.org/abs/2006.06197) report the historical RSA-240 and RSA-250 factorizations. Verifying a published factorization is not a new challenge result, and a small-instance rank improvement is not evidence of a shortcut for a large public modulus. No current-unsolved-record claim is made here.

## 8. Preserved frontier

Completed: inventory/precondition audit; actual existing shadow execution; correction of the earlier witness's scope; default-modulus counterexample; exact postprocessing closure proof; local CRT ambiguity witness; bounded certificate.

Unresolved: a proved N-visible operator that supplies an actual hidden cubic residue beyond the declared observation. No such extractor, general speedup, or RSA public-challenge success is established.

The reusable research outcome is an explicit test pair and a typed information boundary. A future proposed observer can be examined against its own inputs and output contract; the existing counterexample must not be promoted into a blanket impossibility statement about N-only computation.

