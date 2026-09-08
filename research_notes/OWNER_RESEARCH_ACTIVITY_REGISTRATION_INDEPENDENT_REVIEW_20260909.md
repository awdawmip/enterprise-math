# Research activity registration: bounded independent review

The v2 source passes the bounded independent review of the two previously reproduced activity-gate defects. PR1420 is **not admitted by this report**: its reference check failed because the new tool is missing from the existing Common Surface ownership index, while quality was still running at the single CI snapshot.

This is a control-code review by an owner-assigned peer. It creates no research task, claim, Driver decision, or mathematical acceptance. Reviewed source is [PR1420 head `6029caaa74f5ca64e102202799e10310ae051423`](https://github.com/awdawmip/enterprise-math/commit/6029caaa74f5ca64e102202799e10310ae051423); this note does not refer to an unpublished future commit.

The original v1 counterexamples were: omission of the current session could pass the live activity gate, and retrospective persistence permission could pass public pre-final. V2 requires an explicit current session for a live record and requires both activity and persistence permission for public pre-final. Historical source bookkeeping remains available without granting permission to research or finish a live research activity.

| Independent synthetic case | Actual v2 outcome |
| --- | --- |
| Live session omitted | Activity and persistence refused; `BIND_CURRENT_RESEARCH_ACTIVITY_SESSION` |
| Explicit different session | Rejected as a different or unknown original session |
| Explicit matching current session | Activity and persistence allowed; formal authorization and all five authority flags remain false |
| Retrospective source tracking at public pre-final | Persistence allowed; activity, final, and formal authorization remain false |

The replay ran once at `2026-09-08T15:56:50.165712+00:00` to `2026-09-08T15:56:51.769204+00:00`, exit 0, 1.602442 seconds, empty stderr. Exact invocation, with the recorded Windows paths normalized only for display:

```text
C:/Users/Administrator/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe -B -X utf8 D:/em/TEMP/owner-activity-independent-review-v2-20260908-7df012/reproduce.py
cwd: D:/em/control-research-activity-registration-20260908
```

Executed script SHA256: `a6bc69a8c7dfde7c9cb18a878c90ef53ff065798224a5f1c28e347c9e413292d`. Original execution receipt: `294eda4758095e57deec3ddf7f8d461e73fe94e444871f1491279219ba94a2bb`; outcome JSON: `82f6cfafbe56a71377f69748c9997722b4d93eaf34b94dc425b75339a51a2034`. The original v1 failed outcome `b73ae58cb239c723be91c0380a01344e7528789d127eb3dc0d0430b5c502eb06` is retained. Packaging this report did not repeat the regression. The author's separate nine-test run is not represented as independent execution here.

The four implementation/test inputs stayed byte-identical during the replay. The protocol wording was also read. All five reviewed file bytes now match both the frozen v2 manifest and the published PR Git blobs:

| Exact reviewed source | SHA256 |
| --- | --- |
| [tools/research_activity.py](https://github.com/awdawmip/enterprise-math/blob/6029caaa74f5ca64e102202799e10310ae051423/tools/research_activity.py) | `5c35556af36ac20ab701f71fe11c7d42ce27bcfd2a8c7e58c80d2e482ebd234a` |
| [tools/research_runtime_guard.py](https://github.com/awdawmip/enterprise-math/blob/6029caaa74f5ca64e102202799e10310ae051423/tools/research_runtime_guard.py) | `21bf30f62659bdcf919be6ef92469a564af11564c3d5c8eecf7a626aba7b4e0f` |
| [research_control_dispatch.py](https://github.com/awdawmip/enterprise-math/blob/6029caaa74f5ca64e102202799e10310ae051423/research_control_dispatch.py) | `6a8ca75092c7525831e93861f12c75d23eac6b87538d3f71976221ff3d9069a8` |
| [tests/test_research_activity_registration.py](https://github.com/awdawmip/enterprise-math/blob/6029caaa74f5ca64e102202799e10310ae051423/tests/test_research_activity_registration.py) | `5662b303df6999707951044e7e9048f1c83deb0382f3007e1190a547a0dda6fc` |
| [docs/RESEARCH_ACTIVITY_PROTOCOL.md](https://github.com/awdawmip/enterprise-math/blob/6029caaa74f5ca64e102202799e10310ae051423/docs/RESEARCH_ACTIVITY_PROTOCOL.md) | `e00e20a5f6811ee99ce9511443e34152045f35baabf5f93fdaeb34a400951919` |

The dispatch integration supplies metadata visibility without creating a claim; existing formal task/claim routing remains separate. Source observation envelopes provide structured readback and byte comparisons, not cryptographic authentication. The regression used explicitly synthetic envelopes. It does not independently certify the PR's three real backfill activity records or eleven actual observation sidecars. An earlier connector transport failure was retained as a transport observation, not attributed to source code.

One CI snapshot was read at `2026-09-08T16:01:19.074Z`. No eight-shard rerun or repeated workflow polling was performed.

| Workflow | Status | Conclusion |
| --- | --- | --- |
| [control-plane-surface](https://github.com/awdawmip/enterprise-math/actions/runs/34248260193) | completed | success |
| [reference-integrity](https://github.com/awdawmip/enterprise-math/actions/runs/34248260312) | completed | failure |
| [bilingual-sync](https://github.com/awdawmip/enterprise-math/actions/runs/34248260371) | completed | success |
| [control-plane-pr-focused-validation](https://github.com/awdawmip/enterprise-math/actions/runs/34248260190) | completed | success |
| [quality](https://github.com/awdawmip/enterprise-math/actions/runs/34248260238) | in_progress | not terminal |

[Reference job 102135765323](https://github.com/awdawmip/enterprise-math/actions/runs/34248260312/job/102135765323) actually checked out `e63caf0dfc85992a8d11a9e2aedd5b14695cd650`. Its Git tree is `c38d85bfdd05f451657a616bd6211eb75d755ecb` and ordered parents are `[2e8f4ecb61fdffd123beafce588ad9b9015c0407, 6029caaa74f5ca64e102202799e10310ae051423]`. Fresh main was exactly the first parent, so this snapshot contains no additional main delta. The 22 changed-path metadata entries were read; this is not a claim of an independent full-content audit of all 22 paths.

The failed step was `Check shared theorem and tool routing`, at `tools/check_research_common_surface.py:389`, with `repository tool ownership index drift: missing_from_declared_surface=['tools/research_activity.py']; stale_in_declared_surface=[]`. The saved complete connector-decoded log, encoded as UTF-8 without newline alteration, has SHA256 `563319734dba86d97f3b4832684bd2d23ecd0a2f2c4842f5354680c1473113b3` and 47681 bytes. The required follow-up is to update the existing ownership index for this tool and obtain the applicable checks on the resulting exact input. This report does not treat pending, skipped, or failed checks as PASS.

Global-Knowledge-Sync: main@97fb304 / GLOBAL_KNOWLEDGE_V1
