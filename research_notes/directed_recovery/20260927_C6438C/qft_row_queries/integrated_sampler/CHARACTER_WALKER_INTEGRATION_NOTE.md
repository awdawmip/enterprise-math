# A certified final-bit shortcut in the exact checkpoint sampler

Status: AUTHOR_IMPLEMENTATION_AND_BOUNDED_EXECUTION / SHARED_CONTEXT /
NOT_ADMITTED. Activity RA-CAAAC604CB513AEA8BBC1DFC. This is a composition
of the existing actual native instrument, single-label coupling, checkpoint
row oracle and typed Jacobi schedule certificate. It changes no frozen
dependency, native phase word, residual coordinate, or P000 assumption.

## What is proved and implemented

`character_walker.py` constructs a `CheckpointRowOracle` and starts the
inherited `SingleWalker` at its canonical work label 1. It generates a fresh
`certify_program_final_bit` witness. For the last round only, and only when
the full `verify_program_final_bit` replay succeeds, it uses two independent
fair draws: one proposes Z=W or aW, and the second chooses the reported bit.
It preserves Z, appends the bit to the oracle's full history, and never asks
for the two final amplitude rows or applies their feedback word.

The justification is the typed Jacobi witness and reversed-square chain.
For J(a,N)=-1, all pre-final reachable work labels have character +1, while
their final translates have character -1. At every proposed label one of
x=v_h(Z) and y=T_h v_h(a^-1 Z) is zero. Hence the single-walker local norm
ratio is exactly 1/2, including all residuals. Its joint next-bit/label law
is the same native row-norm law, not merely a fair-bit marginal.

The complete history and actual-word oracle recipe remain available after
the shortcut. A later full row query must reconstruct the original coherent
row using that recipe; a single sampled label is not the full state. No
commutation between different feedback words is assumed.

The wrapper accepts no external mid-run state or oracle. It checks its own
history/event/latent chain back to work 1. The character verifier binds the
actual program descriptor, canonical initial state, typed square schedule,
phase/codec/H4 bindings and sources. Existing native word admission remains
a dependency, rather than being falsely attributed to the Jacobi certificate.

An unavailable or invalid character witness falls back to the unchanged
full row-query sampler. UNAVAILABLE does not imply the bit is biased or the
research cannot continue. The contract remains an unchanged admitted program:
fallback does not authorize externally mutating its dynamics and then reusing
stale row caches. Neither Python types nor certificate hashes are advertised
as a security boundary against arbitrary mutation of trusted code.

## Actual bounded joint-law check

The checker imports the same frozen direct-word t4 bank (existing total error
bound 1/2), with its complete source/certificate verifier. It uses N=21,a=2,
t=4 and the already certified six-coordinate encoding of the full 61-mode
native action. These are instrument comparisons, not default-width factoring
success tests and not an ideal-QFT reference run.

For all eight positive three-bit parent histories it examines every occupied
latent label and both auxiliary proposals. Previous actual positive-transition
witnesses are source-hash bound and replayed through the integrated sampler
from work 1; no arbitrary parent state is injected. This yields 46 live
shortcut trials. Each is run with no remaining point-query budget. The last
step makes zero point queries and zero recursive-node visits.

The checker combines each actual parent's row norm, fair proposal mass and
fair bit mass using actual positive-path observers. For all 16 final child
histories, every resulting work-label mass equals that of the actual full
native child. This covers the complete final joint distribution over the
two reported outcomes and work labels. Full 61 versus codec 6 equivalence
is the frozen prerequisite checked in the previous single-walker experiment;
this new integrated run does not claim a second D61 fixture.

## Same-random-tape and cost observations

The original checkpoint walker and integrated walker use the same source
seed and are compared on the complete requested `randrange` tape, every
selected bit, every auxiliary bit and every latent label.

| Actual bounded input | Character result | Original top-level row queries | Integrated queries | Original oracle units | Integrated units |
| --- | --- | ---: | ---: | ---: | ---: |
| N21/a2/t4 | certified one final bit | 8 | 6 | 29 | 15 |
| N15/a2/t4 | unavailable, ordinary fallback | 8 | 8 | 29 | 29 |

The N21 saving is exactly two root queries and fourteen backward-recursion
node visits. An oracle unit here is a recursive visit or checkpoint input
row, not a CPU instruction, bit operation, or native kernel call. Only one
terminal bit is skipped; the preceding row-query complexity remains.

The N21 arithmetic witness costs 1,297 full-adder digit replays to generate
and another 1,297 for its successful runtime replay. N15's unsuccessful but
valid certificate attempt costs 720 digit replays; it yields no saved query.
The source-native full-adder catalog was already warm, so these certificate
stages add zero kernel invocations in the same-tape fixture. That is catalog
reuse, not zero arithmetic cost. The program's typed tables are shared/warm
between the two implementations; no cold-start runtime advantage is claimed.

The whole new checker records 1,219 actual BRC core calls, including native
bank admission, point-row observers, full-state comparisons and controls.
Complete successful traces and sources are retained. Setup, verification, hashing,
allocation, certificate serialization and memory outside the row oracle
remain real costs. These counts do not prove overall speedup.

## Failure and continuation controls

The checker first exhausts an earlier point-query budget after an auxiliary
coin has been drawn. The parent history and latent label remain unchanged;
raising the live budget resumes the same proposal. At the final certified
round it exhausts the random source after the auxiliary proposal but before
the reported bit. The pending plan is retained and a later supplied source
finishes that same proposal. Both earlier returned records stay unchanged.

The final certified round also completes with zero remaining row-query
allowance. Certificate generation/replay has its own explicit arithmetic
cost, so this is not a claim that all computation continued under a zero
total budget. No durable cross-process cursor is implemented by this wrapper.

External replacement of the history or latent label is rejected. A deliberately
altered Jacobi witness fails complete replay and the original sampler still
finishes without taking the shortcut. These controls distinguish a certified
optimization from trusting a status string or discarding a blocked task.
The failed-replay receipt keeps its reason and core-call delta. The inherited
verifier discards its rebuilt certificate when it raises on a mismatch; no
separate full failed-replay digit trace or digit total is claimed here.

## Frozen evidence

- `character_walker.py` SHA256:
  `7753f32de51037f80616a06b619e2a9a70dc4c89619d7ef78bbb7cffef2943ca`.
- `check_character_walker.py` SHA256:
  `5c0157a29e85af250cfddf8d80c5ce69be118bba5170bf119c6f0d7af217d99f`.
- `CHARACTER_WALKER_RESULTS.json.gz` uncompressed payload SHA256:
  `9955f04ca8a82e7d06927063e0500f2c1c3a7b3b976a09206359d1be8f4b0c1f`.
- Gzip SHA256:
  `b68729d52ea77b82876f607e35b284a5cb9b0c3c8ae0267a5d2bc965d080ae0c`.

All relevant new and frozen dependency sources are hashed before and after
execution and are asserted unchanged. `CHARACTER_WALKER_SUMMARY.json` is
an index, not a replacement for the complete evidence archive. The Jacobi
author performed a shared-context read-only integration check; no independent
mathematical admission is claimed.

The general amplitude-query coupling has prior literature, identified by
the parallel source audit. This unit claims only a certified character-based
terminal shortcut within the actual native implementation. It does not close
QFT/Shor dequantization or establish a polynomial full-algorithm bound.

Global-Knowledge-Sync: main@f44ed5959c92e6e088c61c102951d1ab2c5e98d4 / GLOBAL_KNOWLEDGE_V1
