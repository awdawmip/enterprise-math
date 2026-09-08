# Recover the frozen semiprime shell task before redispatch

Classification: control recovery of historical research; no new execution claim,
experimental replay, mathematical acceptance, Working Truth, or tool promotion.

At main `154d649a419bf72fac1b2bf5cb6426a878ac9dbe`, canonical
`research_control_dispatch.py` consumed 734 authenticated Issue #240 comments
through comment `5578453645` and selected
`RS-PRIME-FACTOR-SEMIPRIME-SHELL-RESIDUAL-VALIDATION`, publication
`TP2-8EE46AA7741B8867DAF3`, as `CLAIM_NEW_OWNER / NEEDS_DISPATCH`.
Its own durable progress pointer, however, identified PR #749 and frozen Result
`RR-3287C6124F8D8A1F0901` at source
`1cac434cb9ac542a38a8e7bb6defa414fefb2e4d`.

The seven files from that source are restored with their original Git blobs.
This includes the manifest, discovery freeze, summary, checker, execution record,
Result, and return. The old claim, researcher, timestamps, verdict, and return
remain history. The old branch is not merged wholesale. A new claim would repeat
work whose durable result is already available and is therefore not created.

The source Result pins the correct return Git blob
`705667fbae2379f0d68a03ed58fee09d87d1a5e9`, but its secondary return SHA-256 is
stale. Exact raw audit reproduced two digest errors. The current immutable-history
compatibility mechanism now has one exact-record normalization entry, pinned to
Result blob `629a13a97fd598e095fb6c9fe0840a29e43cf49b`; it recomputes only the
secondary digests in memory after verifying the original primary Git-blob pins.
The correct return SHA-256 is
`78963ec2070cc872806fce3e252a4136aa58334f8fe27c86aa363d2a5bb58c05`.
Every pre-existing compatibility entry and every historical source byte is retained.

The affected-record audit then reports no errors. With the canonical control
bootstrap installed, the recovered task's Result state is
`AWAITING_DRIVER_REVIEW`, `terminal=false`, `review=null`.
This restoration prevents ordinary fresh execution from treating the missing
mainline Result as unfinished experimental work. It does not accept the old
`unresolved_residue=NONE` assertion. The checker and required outputs are being
reviewed separately, and any disposition must use a current source-backed Driver
record and a fresh binding to these exact Result bytes.

Two public command entrypoints also failed direct execution because they imported
`control_plane` before making the repository importable. Their minimal root-path
bootstraps are restored without changing existing function bodies. Three fresh
subprocess regressions pass: runtime guard direct and module help, and the Driver
queue import probe outside the repository without `PYTHONPATH`. The latter is
only an import regression; it is not a claim that a full queue traversal passed.

Verification receipts and exact source pins are retained in
`research_artifacts/PFSSV_DRIVER_RECOVERY_20260908/source_adoption.json`.
The post-exposure independent audit and formal review belong to a subsequent
transaction whose parent already contains the immutable Result.
