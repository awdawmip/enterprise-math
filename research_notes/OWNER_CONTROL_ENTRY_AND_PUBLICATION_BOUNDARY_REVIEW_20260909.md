# Owner review: complete control entrypoints and task publication boundaries

Classification: NO_NEW_MATHEMATICS.
Driver-ID: EM-DVR-01E1D9 / CONTROL_PLANE.

The activity-registration repair is already canonical through EM PR #1420 at 078cdd53e5e96514907c041bf78546325fab0768 and global-knowledge PR #53 at bfc1300130dad2d07916ec3d37d4bc67eb9fc9de. This maintenance increment fixes an older public PRE_FINAL compatibility gap and makes the existing task publication transaction explicit for connector-only writers.

## Control PRE_FINAL

The old and new pre-1420 public facades both rejected a control-only Owner/Driver/Steward input with "task must be an object". The existing liveness contract already supports those roles without a research task. The adapter now accepts an explicit control role only when the input contains no formal task/claim/execution binding and no research-activity binding. It delegates the original strict parent-liveness object to the existing evaluator and always grants no execution authority.

The first local candidate overlooked activity bindings. Owner review reproduced twelve mixed inputs that could incorrectly return final permission; this candidate was never published. The revised adapter excludes the three activity-binding keys even when empty. A control session ID by itself remains valid. Existing authorize/adopt/terminal and research activity behavior are unchanged.

The final focused run passed 13 control tests and 3 existing activity regressions. It covers OPEN-parent continuation, missing or malformed liveness, inconsistent completion with remaining work, control labels carrying task/activity bindings, and direct/module CLI exit statuses. A completed standalone control fixture is explicitly a test fixture; it does not mark the ongoing research parent complete.

## Concurrent task publication

RB PR #1414 reference run 34253129875 and quality run 34253129792 used checkout d72911a6b68203f511e5e191bc4c184917e85ed0, which merged fd9b81c9a872a5a5e8d9a06e11c6e124fbad153d into d80fe75d5e7acbacc6d14df9b98a7fac9ed75a7f.

That base contained research_tasks/1162_UNEQUAL_SUBDIVISION_BETA2_FINITE_STATE_CLOSURE_20260909.md declaring publication but not its immutable record. The reference job 102152155003 and failed unit jobs 102152220248 and 102152220516 reported this same orphan. The other writer added the record at 712ad3b0652f769fa7b79ceacbaca49a7d3e46af. The actual canonical audit at a8502632ee2372b532731ad79f8282188034f573 then passed for 284 publication generations.

The protocol now requires the exact taskbook and its matching record to reach main in one complete commit or integration. Git-data transports can construct a whole tree before moving the ref. A single-file transport stages the pair on a branch and integrates it after verification. Direct-main atomic writes and branch/PR workflows remain allowed; no orphan check or task authorization was relaxed. Concurrent research is preserved.

## Observed activity visibility

The three retrospective activity records were revalidated against actual full-file readbacks from EM main 078cdd53. Their eleven source receipts passed and their unknown historical sessions remained unable to authorize live research or final replies. The canonical report is preserved in research_artifacts/RESEARCH_ACTIVITY_REGISTRATION_20260908/canonical_backfill_readback_validation.json.

An actual bounded Owner overview on a8502632 showed those three records plus a new external conversation's RA-URLEG-7C42A1-20260909T0036 record. That overview is metadata, not a theorem audit or an authenticated assertion that the external session is currently live.

No mathematical checker was rerun for this maintenance increment. The RB blind raw freeze, the historical incomplete return, and the later Result are separate scientific evidence. Existing unfinished research remains OPEN.

Driver-ID: EM-DVR-01E1D9 / CONTROL_PLANE
Global-Knowledge-Sync: main@bfc1300 / GLOBAL_KNOWLEDGE_V1
