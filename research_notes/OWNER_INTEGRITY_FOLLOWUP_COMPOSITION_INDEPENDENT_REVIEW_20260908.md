# Independent review of integrity and follow-up cause composition

Status: BOUNDED_INDEPENDENT_REVIEW_PASS / NEW_COMMIT_CI_PENDING
Owner: EM-DVR-01E1D9 / CONTROL_PLANE
Independent reviewer: /root/execution_gate_review (internal code verification)
Global-Knowledge-Sync: main@982a440 / GLOBAL_KNOWLEDGE_V1

This record persists the already-completed independent review. Its creation did
not rerun tests or alter the reviewed source. It grants no mathematical, Result,
Driver-review, claim or publication authority.

## Exact reviewed input

Baseline commit: `5c06037b971edb8d10e59a668f85acf16ed63a1a`.
Baseline tree: `dbb3c9b61e801fd8f4692e00b160bf1ac4936fb3`.
The authoritative comparison used the complete immutable local 5c snapshot,
not a mixture of cached modules and a changing implementation.

The author froze these three files, whose SHA-256 hashes matched before and
after every independent validation command:

| File | Frozen SHA-256 |
| --- | --- |
| `control_plane/research_driver_followup_fault_isolation.py` | `3b08000a4c61bf1df2a46f06bc4e0d8dad50138d3d12dc05b773dd51cc00d2d2` |
| `tests/test_integrity_followup_cause_composition_20260907.py` | `308a68d25fd2bd4fa5ccdc97b4e3c6d26fd575d4b2f52d441225755b30dfa8f7` |
| `research_notes/OWNER_INTEGRITY_FOLLOWUP_CAUSE_COMPOSITION_20260907.md` | `52d51b501d38524974697ae5cb9e0f6c3edb2b006f16b14cc50a495419401f37` |

UTF-8 LF, whitespace and Python syntax checks passed. The reviewer did not edit
these files, any source record, registry, checker or Result implementation.

## Independent findings and actual validation

The repair composes only the intersection of two independently validated
registries whose task ID, publication ID, record path/blob and taskbook path/blob
all agree. The primary integrity label and every original hard-block key remain
intact. The separate `followup_authority_block` retains the complete packet and
review source set, all six pins and each source review basis. A prior label does
not establish authority. Missing, extra, drifted or stale sources still fail
through the original validators; the strict checker enumeration was not relaxed.

The publication layer establishes root selectors rather than wrapping them.
Installing that existing prerequisite before the follow-up wrappers fixes the
real reverse-order overwrite without pre-installing integrity. The author's
initial 28-error reverse-order diagnostic was retained and independently read.
Fresh-process tests exercise both first-install orders and repeated installation.
The shared-intersection fixture uses copied real invalid GEO6 sources and a
second real invalid review with a synthetic registered packet in TEMP; it does
not substitute a singleton fixture for shared-source coverage.

Python 3.12.14 produced these independent results:

| Check | Actual result |
| --- | --- |
| Reference step 21: `python control_plane/check_publication_fault_isolation.py` | exit 0; 15.469 seconds |
| Reference step 30: `python control_plane/check_driver_followup_nonoperational_review_fault_isolated.py` | exit 0; 14.984 seconds |
| Full bootstrap plus six related unittest modules | **53 tests PASS**; 171.177 unittest seconds, 176.250 seconds for the complete process |
| Complete runtime-view comparison | exit 0; 16.282 seconds |

The 53 tests comprise 13 new composition tests, 4 task-integrity tests,
4 Driver-control tests, 2 result-review-binding tests, 16 review/source-set tests
and 14 Result/follow-up tests. Earlier progress anticipated 52; the raw log
establishes 53 because the binding module contains two tests. No test was removed
or rerun to obtain the reported result.

All 193 definitions were compared. Exactly these four intersections changed:

- `RS-GEO6-NATIVE-RELATION-SELECTOR-CORE`
- `RS-GEO6-NATIVE-TRANSLATION-FOLNER-SEMANTICS`
- `RS-GEO6-PHYSICAL-REFINEMENT-SUPPORT-TRANSPORT-CORE`
- `RS-N-COUPLED-PUBLIC-N-DISTRIBUTIONAL-NONEXTERNALIZABILITY`

The other **189 definitions** and all **149 current records** remained exactly
equal. The genuine two-source, non-overlapping task
`RS-P000-PHILOSOPHY-FIRST-NATIVE-6D-ROTATION-TYPING-MINIMALITY` remained unchanged.
The four intersections retain both exact causes, remain BLOCKED, have no selected
publication and are absent from the current view. Runtime projection errors were
empty. All **195 pinned source files** and the protected **Result10 files from
the final LF 5c tree** retained their bytes. This Result10 comparison does not
relabel earlier pre-normalization test inputs as having been rerun.

## Explicit remaining boundary

The extra `python control_plane/check_driver_followup_fault_isolated.py` whole-store
check is **NOT_COMPLETED_TIME_BOUND**, not PASS. It is outside the original
34-command reference chain and traverses the full Result/review authority maps.
The reviewer applied a 300-second review limit and stopped only its verified
owned child process; recorded process duration was 328.875 seconds. Output was
empty and termination exit code was 4294967295. The termination is not reported
as a reproduced assertion failure. Its original log and annotation are retained.
The already-passed step 21 and step 30 were not repeated during continuation.

The full reference workflow and all eight test shards remain pending CI for the
new commit containing this repair. This bounded review is not complete repository
admission and does not declare the entire control plane repaired. No commit,
push, remote action or eight-shard run was performed by this reviewer.

## Retained evidence

Local evidence directory:
`TEMP/owner-integrity-followup-independent-20260907`.
The full command arguments, frozen-input checks and view comparison are recorded
in `independent-review-final.json`; reproduction runners remain in that directory.

| Evidence | SHA-256 |
| --- | --- |
| `independent-review-final.json` | `94f62e9b913e8d9164f629cad808428bac6c5f8422dda827eb478269dace15dc` |
| `INDEPENDENT_REVIEW.md` | `735ef67995757e8b4ce291d041e9dd3947cbd6f9f4dfddaa7c6a4ca101889c04` |
| `baseline-immutable-5c.json` | `7cf1e135aa4fd9470080a39691de3d35a13415a807d1589d3ef79a1f75b1e989` |
| `step21.log` | `d9dc07ad7be31570ebaf714b75c880faf95b2ac42315459c0f5098768293ce2f` |
| `step30.log` | `7f529c72d4b808e8f96932c3ce7767b4e6d289747e13e596e5fdcbf7c0b1c5b1` |
| `related_unittests.log` | `25c1b24c1de3ea90fc815e8e87c7dc5763a027ffbe94df2ec4c369149b243bc4` |
| `postfix-runtime-view.json` | `4da427cbdaa0c0c5be0710be8a6b243b1371838d9ba9234d5981c2755d92ac5f` |
| `runtime_view.log` | `979f49f3cafd10cd29b85cb20fd01b4a60496cfcb19c6dbc2748a654cf3fb149` |

The author note retains its older `ad23151` read marker. This independent review
used the owner-supplied valid canonical `982a440` lease and read that exact
entrypoint snapshot; it did not normalize or rewrite the author's frozen note.
