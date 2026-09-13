# Three-region nonnegative Cell slice: observed Lean kernel verification

Progress-Event-ID: `cell-slice-lean-formal-20260913-a8d47f21`
Research-Activity-ID: `RA-20260912-gap-origin-a8d47f21`
Researcher-ID: `EM-CHAT-A8D47F21`
Session: `local-chat-gap-origin-a8d47f21` (local identifier, not platform authenticated)
Status: `LEAN_KERNEL_COMPILED_PASS / SCOPED_RESEARCH / NOT_FOUNDATION / NOT_PRODUCTION`
Control snapshot: `awdawmip/enterprise-math@8bfd04268f1d6df8a9bebe91ed402bc9a2b98a86`.

## Exact input and discrepancy

The user asked to formalize the last visible cell-count experiment. Its attachment `verify_lines.py` has SHA256 `b190bf460e87c855c2e4f5b4c61b75473c0422afad70bd2b7deb1663d6ee54e7`; its results hash is `6c55b8dd327e2382151b429b64e5b41f9cf935f71da235e131cffbbf640bf6fe`. Its three-region output has forms `(0,b,c,0,0,0)`, `(a,0,c,0,0,0)`, `(a,b,0,0,0,0)`, with active entries positive. The six displayed lines have 6,10,7,11,14,18 steps.

The existing `RANDOM_CELL_COUNT_LINES_CERTIFICATE_20260913_A8D47F21.json` at the control snapshot describes a DIFFERENT four-region experiment, with steps 8,2,8,6,6,6. Do not merge those statistics or claim they are the same source. This event preserves that older record and explicitly selects the user-visible three-region attachment. All 16 attachment-manifest hashes were checked before formalization. Previous finite experiments were consumed, not rerun as new progress.

## Formal definitions and proved scope

The native audit domain is the whole fixed two-generator integer slice `Point = Int x Int`, not arbitrary X6 states. A constructor `A(b,c)`, `B(a,c)` or `C(a,b)` stores natural offsets; displayed active fields are offset+1. Thus output is six natural fields, with one inactive field among the first three and the last three zero. The complete code includes the region through its zero pattern. This is not a theorem that all six arbitrary nonnegative fields are legal or represent six globally fixed native components.

Decode in displayed values is:
- `(0,b,c)` -> `(1-c,b-c)`;
- `(a,0,c)` -> `(a+1-c,1-c)`;
- `(a,b,0)` -> `(a,b)`.

The integer plane is partitioned by `m<=0 and m<=n`, `n<=0 and n+1<=m`, and `m>=1 and n>=1`. Kernel-checked inverse laws `decode(encode p)=p` and `encode(decode a)=a`, plus digit injectivity, establish unique lossless addresses. The all-zero display marker is not a legal code. The former chart-zero Cell is not deleted.

The direct piecewise update table is specified independently of encode/decode, faithfully translating the attachment's `code_step`. The universal theorem `decode(step d a)=nativeStep d (decode a)` proves its four existing signed-operation labels are exactly the old unit steps; final coordinates remain nonnegative. Reverse actions are proved to cancel.

For every positive k, the corresponding valid boundaries include `(0,1,k)->(1,0,k)` and `(k,0,1)->(k,1,0)`. For every natural k another boundary is `(0,k+2,1)->(1,k+1,0)`. These universal equations, together with update consistency, prove that crossing need not increment a value, but pure unchanged-value field permutation is not valid everywhere in this scheme.

Every finite ordered direction word has the same decoded endpoint and full vertex trace before and after encoding. The endpoint-acceptance predicates agree word by word; exact-length reachability and minimal-length predicates agree. Trace length is word length+1 (vertex occurrences, not necessarily distinct visited Cells). Arbitrary finite candidate-word populations retain multiplicities and the same ordered state-dependent weight products and accepted sums. Weights are parametrized by their actual operations; this is representation invariance, not a new physical cancellation law. The same decoded quadratic distance observer is preserved. The six displayed full traces are additionally checked by kernel reduction.

BRC resolution: `REUSE_APPLIED / FORMALIZED_TRANSPORT`; preserve direction-word identity, order and transported weights. No new origin edge, discarded return history, hidden-coordinate quotient, or extra physical axis is introduced. Closed-form shortest-distance and multinomial formulas are not newly reproved here; their transport obligations are proved.

## Actual compiler result

Proof: `awdawmip/enterprise-math@c88351a4601d319ad1f75bd249cc83f2ec16abba:research_notes/cell_slice_lean_20260913_a8d47f21/SliceCodec.lean`.
Branch: `research/cell-slice-lean-20260913-a8d47f21` (research source, not merged into the canonical Lean library).
Proof SHA256: `2971ea97ba60f0a528a915c06152cb4aec9824fa85fae0bb88c0e76e4e921b02`.
Proof Git blob: `7c1d49677c9714ced0d69286b43c7ec2d7fcc059`.
Compiler: Lean `4.33.0-rc2`, commit `d8b18978322de05a8f3dba51ef03cf5461676c17`, matching the repository toolchain; only `Std` imported.
Execution: GitHub Actions run `34756571162`, job `103721845905`, at the proof commit; completed successfully `2026-09-13T12:15:27Z`.
Observed output: `CELL_SLICE_LEAN_KERNEL_CHECK_PASSED`; compiled `.olean` nonempty.
The complete 40 named theorems/assertions were compiled and their dependencies printed. No `sorryAx`, custom axiom declaration, `native_decide`, or compiler-trust proof dependency. Observed dependency union is only `propext`, `Classical.choice`, `Quot.sound`; do NOT call this entirely axiom-free. Six concrete traces and several boundary equations have no axiom dependencies.

Two earlier runs failed on proof-script unfolding/tactic bookkeeping; neither was certified. The successful revision repairs those scripts without weakening statements or changing the codec/update definitions. This is a remote observed compiler run, not a claim of local Lean execution or an independent server-signed certificate.

## Remaining boundary

Completed: the user-visible three-region slice codec, its direct update table, arbitrary finite path/weight transport, shortest-length equivalence and all six full trace fixtures. Not completed: full X6 atlas, formal imports connecting every existing project Lean definition, Python-runtime refinement for all inputs, closed-form count derivations, full repository build, production caller/storage migration or Foundation admission. Those obligations remain separate and are not filled with placeholders. No P000, worldview, Working Truth or production source changes were made.

The reproducible Chat package contains the exact Lean file, pinned toolchain, checker, normalized observed compiler stdout, theorem list, validation manifest, Chinese report and the selected attachment inputs. Std alone suffices to recompile the proof. The proof's research branch and this main-side result record have distinct publication meanings.
