# R005 q=78553 catalogue and seam research handoff

Status: `PREPARED FOR ONE REAL RESEARCHER / NO ASSIGNMENT OR CLAIM YET`  
Line Driver: `EM-DVR-81273A`  
Current scope authority candidate: `DA-80BDA97466C306DAD3C3` /
actual Owner comment `5605970384`  
Exact research parent: `OBJ-R005-PRIME-ALGORITHM-LAB-RELAY-20260909`

This is a standalone handoff for the existing task. It is neither a task
publication nor an assignment or execution grant. Driver identity, activity,
ASSIGN and research execution remain different authorities.

## Existing task and frozen boundary

- Task: `RS-R005-Q78553-EXACT-916-GAP-CATALOG-SEAM-CLOSURE`.
- Publication: `TP2-09D6ECE7F315F0766FE1`, generation 1.
- Taskbook: `research_tasks/R005_Q78553_EXACT_916_GAP_CATALOG_SEAM_CLOSURE_20260909.md`.
- Frozen book blob: `f93278bb9f3f3492e0399147a1a13dbd50291386`.
- `q=78553`, `Q=6170573809`, `G=916`, `d_max=2`.
- `k_global_fail=2822453183434`, `k_q2_width=2826122804522`.
- Exact gap-start band: `[1291005053866735,1294364244470160]`.
- Certified frontier stays `k<=2822453183433` until actual accepted seam evidence
  permits a change. Do not proceed to the next prime q in this task.

The question is whether the entire frozen seam can be certified, whether an
exact prime-free interval occurs, or whether catalogue completeness remains
unresolved after substantive auditable work. Under the accepted deficit-two
reduction, every relevant exact-916 gap start `a` contributes only floor
shadows `a` and `a+1`.

## Consume completed work

The scanner repair and DSI review are complete. Do not repeat them:

- Corrected scanner: `experiments/r005a_p2_gap_shadow_inversion.py`, blob
  `1d3d19adc13652bf343972c5eb3ac95684bb8c8a`, SHA-256
  `6fe2dc9fe05ac16ef2bbd1919d3d03fc5b36037d010ca95afeafb62f4958d3f5`.
- Focused regression: `experiments/r005a_p2_gap_shadow_inversion_regression.py`,
  blob `ece824a71c884b09033f1666581a71afe86822a0`.
- Accepted correction: `RR-566554389F6F36576DE2`, raw SHA-256
  `5dc2a43840b2878013281cc49f4956c893754b4feab50148dbea2c75d8f5fc62`.
- Driver review: `DR-7605C20CFE02E3900E8D`; follow-up:
  `DFU-192EC00B45DD90358773`.
- Exact accepted source main: `dbf8ee926870f6c8398d6e64fd205e0fc1013ecd`.
- DSI source note:
  `git:awdawmip/enterprise-math@f9e2a611b45631c43effce36b7300c6f9a56b77b:docs/R005A_P2_DEFICIT_SHADOW_INVERSION_20260902.md`.
- Current line recovery source:
  `driver_reviews/R005_LINE_DOSSIER.md` and
  `driver_reviews/R005_LINE_DRIVER_81273A_20260909/seam_release_receipt.json`.

The real release is Issue240 `UNBLOCK5602494875`. Its artifact dependency is
still present. PR1463's `control_plane/research_dependency_release.py` checks
that release against current Task, raw Result, accepted DR and ready DFU
bindings. Do not delete dependencies or invent a GOV DONE event. Its earlier
765-comment proof is historical test evidence, not your live selection.

## Real startup sequence

1. In the actual researcher conversation, load current account/project task
   protocols and mandatory P000, allocate your own Researcher-ID, retain your
   own real session key, and register your own lightweight TASK_RESEARCH
   activity. Persist and fully read back that RA through the current protocol.
2. Report your exact ID, session, RA path and immutable RA readback to the
   Driver. Do not start mathematical execution or manufacture an assignment.
3. The Driver issues an actual `ASSIGN_RESEARCH_TASK` bound to your identity and
   session, the exact task/publication/parent, and its current source-backed DA.
4. You consume that real assignment through
   `research_control_dispatch.py --kind RESEARCH --assigned-research-task` with
   a current raw Issue240 snapshot. Its dependency proof must validate the real
   release. A proof receipt alone is not a task selection.
5. You perform canonical execution prepare, actual server CLAIM and runtime
   authorize yourself. Preserve any current legitimate claim; if a competing
   owner exists, use the current recovery rules instead of a duplicate claim.
   Capture actual argv, outputs and raw server envelopes. Begin mathematics only
   after your real execution authorization succeeds.

Use a complete verified current checkout for execution. A complete e5 snapshot
was prepared at `e5c9cc27e82d65bfd7a2b518ff76a1cb64572e35`, full tree
`a43af681e98375ffb14ca7911d85c079f8f0129b`. That is a recoverable base, not a
promise that later main has not advanced. Refresh and apply the complete later
delta; never call an old partial overlay a current complete execution tree.
GitHub I/O uses the connected GitHub tools; native Git stays local with
`GIT_NO_LAZY_FETCH=1`. Preserve other worktrees and unrelated dirty files.

## Research work and completeness

First recover any task-specific source, catalogue, claim, checkpoint or Result
that appeared before your actual start. Consume verified completed work. Then
try the substantive routes permitted by the task:

- Locate a primary complete gap dataset whose coverage, threshold, generation
  procedure and completeness claim actually cover the entire exact band.
  Verify its provenance, immutable bytes and schema; compare independent
  sources or available certificates where applicable.
- If existing data is insufficient, investigate a reproducible construction
  or certificate. An exact segmented computation or equivalent verified
  coverage method must account for boundaries, all intervals and every
  possible qualifying gap. A pilot or sample is not full-band completeness.
- Reuse the accepted DSI/scanner and current adequate tools. Before constructing
  a new general mechanism, apply current BRC/tool-coverage and reuse rules.
  Preserve integer endpoints, gap identity, ordering and coverage provenance;
  a count, record list or compressed aggregate cannot silently replace them.

Record-gap and first-occurrence tables do not enumerate every repeated 916-gap.
A source may support a certified maximum-gap bound while still failing to
provide the complete required catalogue. Keep those evidence roles separate.
A missing filename, unsuccessful single query, missing remote UI affordance or
an absent catalogue in one checkout does not prove no data is available.
An unresolved outcome needs a concrete source/coverage ledger and documented
constructive attempts or a verified remaining completeness obstruction. State
what was checked and what remains unknown; never claim universal unavailability
from an unsuccessful search.

## Scanner and required delivery

Use the accepted scanner's catalogue schema
`R005A_CONSECUTIVE_PRIME_GAP_CATALOG_V1`. Its sorted unique rows and
`rows_sha256` must match the exact catalogue. Coverage, complete-gap threshold,
maximum-gap bound and its coverage endpoints must all satisfy the frozen seam.
Set `completeness_attestation=true` only after the actual evidence supports it;
the flag itself is not a completeness proof.

Execute the accepted scanner on the final catalogue with the recorded actual
interpreter and argv, including `--q 78553 --catalog <exact-file> --output
<exact-file>`. Final certification may not rely on skipping required row
verification. Independently verify every dangerous row/candidate's prime
endpoints and prime-free interior. Preserve the full completeness argument,
checked paths, exit codes, output bytes, digests, and exact source commit.

Return the catalogue/certificate when available, source-and-coverage ledger,
actual code/run evidence, outcome reasoning, failed approaches and remaining
scope, plus a complete manifest and new immutable Result for this existing
task under your own actual execution binding. Persist all material needed for
later Driver review before ending. Put the mathematical outcome in the return;
use current Result schema fields honestly. Do not copy a historical success
spelling into a control field merely by habit or mark incomplete startup as a
satisfied research target.

Only these taskbook outcomes close this research unit:

1. `Q78553_SEAM_CERTIFIED_CLOSED`: complete justified catalogue and accepted
   scanner evidence certify the entire seam through `k=2826122804521`.
2. `Q78553_EXACT_COUNTEREXAMPLE_FROZEN`: an exact verified failure with full
   witness data and evidence for any claimed first/minimal failing k.
3. `Q78553_CATALOGUE_COMPLETENESS_UNRESOLVED`: substantive auditable work leaves
   a precisely stated completeness boundary and no frontier extension.

None of these bypasses Driver review or authorizes the next q. Parent closure,
Working Truth, Foundation and promotion remain separate gates.
