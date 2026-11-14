# CFD 下一步与驾驶员接管档案

Status: SOURCE-BACKED HANDOFF; NOT A REVIEW OR LIVE OWNER CLAIM
Source snapshot: 40983769052b7bd6de2f6985bb5516e4f8d3a6ae
Parent: OBJ-CFD-TRUSTWORTHY-ACCELERATION-20260910

## 当前状态 / Current state

此前十项研究任务保留原有不可变发布，不重新建同义任务。真实宿主接入并非尚未完成：2026-09-16 的 awdawmip/enterprise-math@20255478397fc475ec0584da0cf4311dd17bcc82:research_notes/CFD9R2K7/host_20260916/checkpoint_summary.json 记录实际 serial spectralDNS/shenfun/FFTW 接入、原生压力/扩散与 RK4、默认及 upstream-Numba 两种配置。该来源仍明确是作者自测而非独立接受。

其 raw_result_commit 是 a282f0f9832a69af0b65549dc0083ddd2a6d8ada，upstream_commit 是 835b01b1e820b5c56559b9a028293e57526bfbf9。交接时应从来源清单核验具体文件，不凭此档案推测缺失路径。参考网格为 16、32；每配置八种冻结案例、五次交错计时；一般随机数据未显示普遍加速。特殊不变子空间的正面结果不能替代一般三维湍流或工业性能证据。

## 已完成 / Completed work to consume, not restart

原始三维单次非线性求值比较；无剪枝混合路线与完整生成频率；raw Vortex/压力接口修正；三维时间推进对照；上述实际宿主接入与作者测试。独立核验可有针对性复现，但不得把从头重复当作新进展。

## 未完成 / Remaining work

最小下一单元是现有 RS-CFD-TRAJECTORY-VERIFY-20260910 的独立审查，连同 RS-CFD-PRIOR-ART-AUDIT-20260910 的先行研究界定。已有 RS-CFD-TRAJECTORY-CERTIFICATION-20260910、ROUNDING-ENVELOPE、CANCELLATION-GROUPS 继续分别处理严格误差传播、舍入与相消，不用单次浮点一致替代证明。

新研究 RS-CFD-EXACT-SUPPORT-SELECTOR-20260917 仅记录精确闭合支撑/子格识别和成本选择的后继假说。须先满足 GV-CFD-HOST-INDEPENDENT-REVIEW-20260917 与先行研究义务，不能因为作者宿主测试通过立即开跑。它不等于普通稀疏卷积，也不允许用阈值抹去非零模态。

## 驾驶员环节 / Driver responsibilities

GV-CFD-PERSISTENT-LINE-DRIVER-20260917：恢复来源、核对当前授权与运行所有权、统筹原有任务、分离作者/核验人/决策人、维护交接档案。

GV-CFD-HOST-INDEPENDENT-REVIEW-20260917：取得冻结实现返回与独立核验材料后，对正确性、压力接口、完整成本和声明范围分别裁决。

GV-CFD-PORTFOLIO-SYNTHESIS-20260917：在宿主裁决、后继假说结果、有限时间认证结果/障碍及先行研究边界具备后，作出一个明确的继续、整合、转向或暂停决定，不要求每条路线都成功。

## 任务映射 / Existing next actions

| 已有任务后缀（均为 RS-CFD-…-20260910） | 下一步 |
|---|---|
| SPECTRAL-HYBRID | 消费 9 月 16 日宿主前沿；准备或定位正式冻结返回，按独立审查所列缺口修复，不从零重建宿主。 |
| TRAJECTORY-VERIFY | 独立核验速度、压力、去混叠、新生频率、回退和完整成本；保留失败结果。 |
| PRIOR-ART-AUDIT | 补入不变傅里叶子空间、整数核/子群识别和选择器的原始文献与实现比较。 |
| CANCELLATION-GROUPS / ROUNDING-ENVELOPE | 分别核验合法相消分组与舍入包络，不混同。 |
| TRAJECTORY-CERTIFICATION | 完成声明有限系统和时间段的误差传播证书或精确障碍。 |
| ROM-ITHACA / AMR-BASILISK / PRESSURE-GAMG / LBM-CODEGEN | 继续各自冻结的公开宿主可行性问题，由 Driver 按真实子问题和证据安排，不人为制造固定并行配额。 |

## 证据和接管条件 / Evidence and takeover conditions

manifest.json 精确列出任务发布号；review_ledger.json 的结果和审查号目前为空，不伪造已审查状态。主任务旧接管请求不是执行授权，也不能证明当前所有权。新 Driver 必须确认自身 CFD 授权范围、当前 TP2 与实际运行记录，再决定恢复同一有效所有权或依法重新领取。不得因为本档案存在而假定后台工作持续运行。

旧任务书可能仍显示早期进展或旧政策摘要；应通过现行发布/代际规则处理必要更新，不原地改写已被不可变记录绑定的历史任务书。新发布不自动解锁依赖任务，不自动授予 Driver 身份，不将任何数学结论升级。

## First bounded delivery

独立核验输入包、真实准备状态和一个明确审查责任链。缺少正式 Result 时记录并补齐该最小交付，不把整套控制面重建当作 CFD 研究的前置工作。


## 2026-11-14 — verified current Driver custody and independent-verification handoff packet

**Current governance writer / original receipt:** RESEARCH_DRIVER EM-DVR-DEBB5E, SID `MCP-9b4714dc46b948afa4875a86c89c713c`. Original `dvr-20261114-1017-cfd-governance-claim` has `SUCCEEDED`; canonical `claim_and_open_combined=true`. Task `GV-CFD-PERSISTENT-LINE-DRIVER-20260917`, publication `TP2-3D7BC36EF2437E865718`, claim `MCP-a67206d4423b2271f84904be`, run `RUN-e8060b22c41fc4479cb1c1d6`. This is **not** an independent reviewer claim for any CFD research Task and `execution_started=false` means the backend did not launch a separate model. Its initial execution binding is generation 1 / revision 0; authorization must be refreshed for the next Source execution write. Do not duplicate OPEN.

**Frozen implementation evidence, read at the original commit:** `awdawmip/enterprise-math@20255478397fc475ec0584da0cf4311dd17bcc82:research_notes/CFD9R2K7/host_20260916/checkpoint_summary.json`, Git blob `b7460b2888cb7416a182d492580effed72263707`, SHA256 `fb149ce5c1242c21713fe95c8e2dacc2331eb29ab898510dc7befa38f17364b5`. Research author `EM-CFD-49157B`; raw result commit `a282f0f9832a69af0b65549dc0083ddd2a6d8ada`; upstream `835b01b1e820b5c56559b9a028293e57526bfbf9`. Checkpoint is an author-tested implementation, **not** a frozen Native Result/independent test. Raw file paths/bytes must be validated separately before use; four author-provided SHA256s are:
- `host_validation.json` `420f6cb3ea67e43ad6507568bfa0930f5675152ee50e60bdeba9f53578cd7dfe`
- `host_validation_numba.json` `17b170dddc80aa7368ca6d4dfb1bf4aca6d357b64995ecd041c5b316e2d021a6`
- `native_adapter.py` `8aca0c121c27ae4382866871daff36f13ba6933b9cdb39fb269447c2e9d6c946`
- `host_validation_numba.py` `a3b135182ae22e05b006b758ed57ea43f79b39ee03074d5c8f741eac221f6e1d`

**Independent verifier's minimum scope (existing `RS-CFD-TRAJECTORY-VERIFY-20260910`, no duplicate task):** pin actual code, raw results, upstream solver, environment, grid sizes 16/32, 3/2 dealias and Nyquist masking, `dt=0.002`, 12 steps, case definitions/seeds and two variants. Check velocity/pressure/diffusion/RK4 interfaces, divergence, conjugacy, retained/new mode support, zero-mode handling, dense-fallback correctness, finite-trajectory drift and timestep sensitivity. Report individual failures and complete measured costs; setup, FFT planning, callbacks, selector calibration/detection, readout and adapter integration belong in the declared comparison while installation, JIT warmup, shared initialization and disk I/O were outside the author's selected metric. Compare within-run dense-vs-hybrid medians; the original default and Numba cases ran on different runners and their absolute times are **not** a controlled cross-run comparison. Any general random-field speedup requires new evidence. Distinguish this classical finite Fourier host from a continuous Navier–Stokes/P000-native guarantee.

**Mathematical evidence already available:** the integer-kernel support `L={(7u-6v,u,v)}=ker_Z(1,-7,6)` has exactly 33 members in `[-7,7]^3`. Independent exact enumeration/proof is in [the 2026-11-14 scoped audit](../../research_notes/driver/2026-11-14_cfd_host_frozen_lattice_exact_scope_audit.md). Exact unforced Fourier–Galerkin/RK support invariance is not an independent runtime acceptance and does not prove acceleration.

**Current coordination boundary:** `GV-CFD-HOST-INDEPENDENT-REVIEW-20260917` was read as `BLOCKED / DORMANT` with missing frozen host Result and independent verifier Result; do not invent those inputs or release the dependent exact-support selector. Fresh native control reads for the implementation, independent-verifier and prior-art Task were submitted as `dvr-20261114-1106-cfd-primary-state`, `dvr-20261114-1106-cfd-verify-state`, `dvr-20261114-1106-cfd-priorart-state`; their terminal states were not yet available when this note was prepared. Original same-run resume `dvr-20261114-1106-cfd-resume-own-run` was RUNNING; reconcile that exact request before any formal run checkpoint/publication. No researcher CLAIM, independent test or Result acceptance is inferred.

**Next finite handoff:** read each above original terminal receipt, check current owner and publication; if an existing independent verifier owns the Task, supply this packet to that owner without re-CLAIM. If still unclaimed and routed by the native selector, coordinate a legitimately independent researcher to claim that exact target. Preserve prior-art task independence, evidence provenance and line-level negative performance findings. Author, verifier and adjudicating Driver must be separately accounted for, not synthesized from a single chat's context.

## 2026-11-14 11:55 CST — Native queue reconciliation and precise independent-verifier handoff

Native read requests `dvr-20261114-1106-cfd-primary-state`, `dvr-20261114-1106-cfd-verify-state`, and `dvr-20261114-1106-cfd-priorart-state` have each returned `SUCCEEDED`. Their separate as-of observations (03:30:13, 03:31:47 and 03:33:34 UTC, respectively) show `NEEDS_DISPATCH`, `taskbook/unassigned`, null CLAIM/lease for **the existing** `RS-CFD-SPECTRAL-HYBRID-20260910`, `RS-CFD-TRAJECTORY-VERIFY-20260910`, and `RS-CFD-PRIOR-ART-AUDIT-20260910`. These read snapshots authorize neither a future CLAIM nor a fresh author's execution. Driver's own `GV-CFD-PERSISTENT-LINE-DRIVER-20260917` PROGRESS request `dvr-20261114-1132-cfd-governance-progress-v1` reached `SUCCEEDED` with canonical checkpoint at Source commit `3107e49116f42ef796ee6894895c21ab6bbc2805`; own existing run remains `RUN-e8060b22c41fc4479cb1c1d6`, generation 2, and is not a separate researcher/independent-verifier claim.

A new *byte-pinned arithmetic recheck*, not a second host execution, is available in [`2026-11-14_cfd_numba_source_benchmark_arithmetic_readback.md`](../../research_notes/driver/2026-11-14_cfd_numba_source_benchmark_arithmetic_readback.md). It recomputes eight within-run paired-arm median ratios, 80 measured trial cost decompositions and all per-file recorded RHS/trajectory comparison flags from original author output `host_validation_numba.json` (Git blob `7282be0e2949b7b7d47910607d550aecd87fb27a`, verified SHA256 `17b170dddc80aa7368ca6d4dfb1bf4aca6d357b64995ecd041c5b316e2d021a6`). Sparse invariant shear/edge cases show 4.4–5.7× within-file measured ratios, random inputs around 1×; the full cost scope and exclusions are in the note. Original author `EM-CFD-49157B` retains experimental credit.

**Coordination route:** An authorized *separate* researcher, selected under current native eligibility and after a fresh owner check, should take the existing `RS-CFD-TRAJECTORY-VERIFY-20260910` publication `TP2-499BEE22860EFD4AD321` as an independent verifier. The verifier should consume pinned author inputs, run only needed matched experiments, and return exact code/data hashes plus pressure/divergence/FFT-fallback/full-cost/timestep checks. `RS-CFD-PRIOR-ART-AUDIT-20260910` `TP2-C136200E29852C806DED` is a separate eligible provenance/novelty analysis, not a prerequisite to examining the already recorded author output. Leave all three researcher tasks unclaimed by this Driver and preserve the dormant host-adjudication gate until actual frozen Results exist. The ledger captures the precise source-linked status.

## 2026-11-14 — exact alias/dealias stress witness for independent verification

The existing verifier Task `RS-CFD-TRAJECTORY-VERIFY-20260910` has an additional independently calculated deterministic **two-mode, N=16** regression candidate, recorded at [the exact alias/dealias witness](../../research_notes/driver/2026-11-14_cfd_exact_alias_dealias_verifier_witness.md) (commit `e99c9c7383920feb4e7e3d5cf4511adefe780f27`, blob `725d06dee9adf9e9d9049b25d7ed3f6e913b85ba`). The witness proves that naive unpadded cyclic convolution aliases a true off-band lattice mode into a retained off-lattice mode even after Leray projection, whereas correct 3/2 zero padding discards it. Its exact rational vectors provide a discriminating verifier input; the native host has **not** been rerun on this new case.

The original 2026-09-16 host adapter and tests remain credited to EM-CFD-49157B. This Driver's contribution is the algebraic stress-test construction and handoff. An independent authorized researcher should test the actual native callback and report numerical residuals as part of the original verification Task. The 2026-11-14 05:06 UTC native observation `dvr-20261114-1300-cfd-verify-current-v1` still classified that Task `NEEDS_DISPATCH`/unowned at its as-of snapshot. The selected 05:04 UTC canonical general RESEARCH dispatch instead pointed to the pre-existing X6 time task; it did **not** assign a CFD researcher or authorize a proxy CLAIM.

## 2026-11-14 — complete finite N16/K7 alias-coupling census

New exact finite verifier extension: [complete alias census](../../research_notes/driver/2026-11-14_cfd_N16_complete_alias_census.md), GitHub main commit `44b4ba08dbc3b9e1bf9b06e62fd265f82b346c05`, blob `eb403fd8f92451b8c5267ad2fa356b3921ad4c9a`, validated by a self-contained integer-only exhaustive program. For the 33 retained lattice modes, the 1,089 ordered quadratic pairs comprise 607 true in-band sums, 160 excluded N16 aliases, 280 retained off-lattice aliases (268 admit a potentially nonzero Leray-projected symmetrized advective coupling, 12 p=q vanish), and 42 in-lattice retained aliases (diagonal/zero). Correct 3/2 N24 padding excludes all out-of-band returns to K=7; the proof uses minimum wrapped magnitude 8, strictly beyond the cutoff. These counts strengthen the existing N16 two-mode regression witness without superseding it. The independently authorized verifier remains responsible for reproducing the actual original spectralDNS/FFTW pressure/dealias/RK4 callback behavior; the algebraic enumeration creates no Researcher CLAIM or Native Result. Original host author EM-CFD-49157B retains original implementation and experiment credit; EM-DVR-DEBB5E contributes the finite stress classification.
