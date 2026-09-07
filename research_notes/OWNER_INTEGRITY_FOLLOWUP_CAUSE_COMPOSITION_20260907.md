# Integrity and follow-up cause composition

Driver-ID: EM-DVR-01E1D9 / CONTROL_PLANE
Global-Knowledge-Sync: main@ad23151 / GLOBAL_KNOWLEDGE_V1

This control-only repair is based on integration commit
`5c06037b971edb8d10e59a668f85acf16ed63a1a`, tree
`dbb3c9b61e801fd8f4692e00b160bf1ac4936fb3`. Its scope is the existing
follow-up isolation module, one new test module, and this note.

## Two reproduced defects

The clean commit's actual reference step 21 and CI both reported
`integrity quarantine registration source drifted` for four tasks:

- `RS-GEO6-NATIVE-RELATION-SELECTOR-CORE`
- `RS-GEO6-NATIVE-TRANSLATION-FOLNER-SEMANTICS`
- `RS-GEO6-PHYSICAL-REFINEMENT-SUPPORT-TRANSPORT-CORE`
- `RS-N-COUPLED-PUBLIC-N-DISTRIBUTIONAL-NONEXTERNALIZABILITY`

The follow-up overlay replaced the primary integrity source and hard block.
Both underlying faults remained exact and active; replacing the diagnostic
source hid one of them. The integrity checker correctly rejected that view.
The original step-21 log is retained in
`TEMP/owner-reference-exact-5c06037b-20260907-ulnig58l/21.stdout.log`, SHA-256
`08f266aba99a2d6d7c9e8fa6be59062e083ab219a2445342aec887546a313008`.

The first new fresh-process test also exposed an installation dependency.
Installing follow-up before integrity let integrity's first publication-layer
installation replace the current/dispatch root functions. The earlier follow-up
wrappers disappeared while their module markers remained set. Its real audit
reported 28 errors: eight other derived tasks leaked current/non-BLOCKED/selected
publication views, and the four intersections lost their secondary cause.
The first 15-test run recorded one failure plus a subsequent test snapshot
indexing error; both that run and the 28-error diagnostic are preserved.

## Resulting control behavior

The follow-up module validates both registries and requires equality of task ID,
publication ID, record path/blob, and taskbook path/blob before composing causes.
It reconstructs the integrity projection from its validated row, preserving
`TASK_INTEGRITY_QUARANTINE` and every original integrity hard-block field.
Incoming source labels and hard-block payloads do not establish an intersection.

An explicit `followup_authority_block` carries the independent follow-up cause:
all six task/publication pins, the complete singular or plural source identity,
and every exact packet's ID, review ID, Result ID, path, blob and review basis.
The existing follow-up audit checks this entire object and every primary
hard-block key, including the required null operational publication pin.
An extra source, missing source, stale review fault or changed pin still fails
through the original validators. No source review or mathematical disposition
is repaired or inferred.

Follow-up installation now establishes the existing publication layer before
wrapping its selectors. It does not install integrity early. Consequently the
actual follow-up-before-integrity sequence remains independently exercised.

## Validation and exact scope

Python 3.12.14 ran full bootstrap followed by five related unittest modules in
one process: 4 existing integrity tests, 13 new composition tests, 4 existing
Driver-control tests, 16 review/source-set tests and 14 Result/follow-up tests.
All 51 passed in 205.814 seconds. The new tests additionally launch fresh Python
processes for each first-install order, then full bootstrap, opposite/repeated
installs and another bootstrap. Both orders produce identical full public views
and pass both isolation audits.

The shared-intersection fixture copies the real GEO6 record/book pins and their
four actual mandatory-section faults into TEMP. A second real invalid review
provides a synthetic explicitly registered second packet source. The live source
validators recompute both review faults; the test preserves both packet/review
identities and plural hard-block source lists. Negative tests cover all six
cross-registry pins, original source bytes, registry pins, missing/extra sources,
repaired or drifted reviews, forged prior labels and damaged audit projections.
Only the latter negative tests inject an incorrect public projection; they still
call the real underlying selectors and do not replace a source validator.

The actual step-21 and step-30 CLI commands both exited 0 on the final module,
with empty stderr. Independent baseline
`TEMP/owner-integrity-followup-independent-20260907/baseline-immutable-5c.json`
(SHA-256 `7cf1e135aa4fd9470080a39691de3d35a13415a807d1589d3ef79a1f75b1e989`)
was compared against all 193 definitions. Exactly the four intersections changed;
the other 189 definitions and all 149 operational current records are identical.
For those four, the changed fields are `evidence_status`, `frontier`, `hard_block`,
`last_progress_ref`, `next_action`, `owner`, `registration_source`, and the new
`followup_authority_block`. The owner field returns to the integrity projection's
original research owner; each task remains BLOCKED with publication ID null.
All 195 pinned source files matched the independent baseline before and after
the run, including the frozen source and registry evidence.

Evidence directory:
`TEMP/owner-integrity-followup-composition-20260907-bb0da8jf`.

| Evidence | SHA-256 |
| --- | --- |
| `tests-first.log` | `eff0b5e36c001cec891b84ba60449b242479a90101140691d4ff74a2264ef7a7` |
| `reverse-first-diagnostic.json` | `f211bb07e1fc42f7323091384704cf0a3a161f086f5f933a1ba82a01b663c69a` |
| `tests-final.log` | `d46c16dcbf371f66532751136089e30231122b9847b9e3a7e85d41234f543d4d` |
| `step21-final.stdout.log` | `d9dc07ad7be31570ebaf714b75c880faf95b2ac42315459c0f5098768293ce2f` |
| `step30-final.stdout.log` | `7f529c72d4b808e8f96932c3ce7767b4e6d289747e13e596e5fdcbf7c0b1c5b1` |
| `final-public-delta.json` | `617f7331a48b9f7ef62f786baa8598926ce8ce3b449d7fb096df6eff2fc2a42d` |

Reproduction scripts `run-final-tests.py` and `run-final-public.py` are retained
in that directory. The latter records each CLI's command, exit code and elapsed
time, checks the 195 sources, and saves the full definition comparison. This is
bounded control-fix evidence, not a new complete 34-command or eight-shard CI run.
No source record, quarantine registry, Result implementation, claim, publication,
Driver disposition, mathematical conclusion or authority flag was changed.
