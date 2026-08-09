# Enterprise Math 当前研究分支账本

状态：`CANONICAL OWNER-ISOLATION LEDGER / CURRENT WRITE SURFACE`  
路由快照基线：`main@aec7f625e48eb8f93ba701ba57686a9e225efd17`  
此前 canonical 账本刷新：PR #196、PR #215  
日期：2026-08-09

本账本是当前语义写入面的人工可读快照。实时机器权威仍然是：

`branch_governance_overrides.json + research_scheduler.json + Issue #240 runtime events`。

开放 PR 数量、分支年龄与 Git ancestry 都不能决定 theorem ownership。治理生命周期保持：

`owner research -> freeze exact payload -> fresh/latest-main L4 replay -> exact merge-state gates -> canonical main`。

L1/L2/L3 owner 可以有意落后于移动中的 `main`，不得仅为“保持最新”而 whole-tree sync。L4 publication 全局 `NO NEW MATHEMATICS`。

## 1. 本快照下已 canonical 的可复用层

当前 `main` 已包含以下代表性 canonical 资产：

- A2 finite-arity / future-compatible quotient machinery；
- A3 weighted relation-state、relation lattice/scale core；
- A4 admissible correspondence / relational-spectrum core；
- thin A3->A4 generated-support bridge；
- P021 causal-boundary core；
- P022 `A_p` / root-lattice geometry core；
- 经 PR #262 / `fc81a15a` 进入 main 的 P022 geodesic-multiplicity + HCP executable core；
- 经 PR #288 / `aec7f625` 进入 main 的 P022 Barlow stacking executable core；
- 经 PR #270 / `b4801960` 进入 main 的 P018 centered-prime-radius executable layer；
- Owner-Isolation、scope-aware branch auditing、scheduler / handoff control 与 Foundation Steward 规则；
- 已登记在 owner registry 与 shared-surface machinery 中的当前 canonical E001 finite material/world slices。

P022 下一项有界 publication 是 task-relative Barlow precision。源 PR #265 已验证的 two-blob payload 已在 `main@aec7f625` 上重放为 fresh L4 PR #292；在 exact current-head promotion gates 全绿并完成 merge 前，它仍不是 canonical。

## 2. 当前活动语义写入面：13 条路线

机器 owner registry 当前共有十三条 `ACTIVE_OWNER` / `ACTIVE_BRIDGE` 路线。长期紧凑运行面仍优先压在约 8–12 条可写 refs，因此 13 是暂时高沿，不是新的目标值。压缩必须遵守 semantic result conservation，不能靠任意删 branch 实现。

### 2.1 Core owner — 1

1. `core/a3-relation-lattice-v3`
   - sparse integer relation-lattice continuation；
   - 只拥有 spanning-tree integer coordinates、zero-total orbit/lattice reconstruction 及其直接依赖的 A3 invariants。

### 2.2 Program owners — 6

1. `program/p017-legendre`
   - square-basin / Legendre pressure-test frontier。

2. `program/p018-precision-v2`
   - precision-specific quotient/root-channel 与 carry frontier；
   - generic future-compatible quotient theory 仍归 A2/P023。

3. `program/p021-causal-focusing-v3`
   - causal-boundary promotion 后的 focusing、direction、causal-role/witness 与受物理边界约束的 specialization continuation。

4. `program/p022-geometry-v2`
   - intrinsic discrete geometry owner；
   - `A_p` lattice、geodesic/HCP 与 Barlow stacking executable layers 已 canonical；
   - Barlow precision/growth/coordination 以及后续 observation/collision/repair 仍是同一 owner 内研究，除非按 weakest hypotheses 明确重新归属。

5. `program/p024-action-precision`
   - state/action-language precision specialization；
   - generic quotient/adjunction 仍归上游 owner。

6. `program/p025-abc-support-collapse`
   - abc/radical-support pressure test 与 relation-conditioned bounded-witness precision candidates；
   - 不代表已经证明 abc，也不改变 problem closure。

### 2.3 Cross-owner bridges — 3

1. `bridge/a3-a4-generated-support-v3`
   - 仅保留真正跨 owner 的 thin A3 relation-state -> A4 generated-support bridge。

2. `bridge/p017-p018-hard-core-v2`
   - arithmetic / precision hard-core、root-channel 与 analytic tail-resource bridge。

3. `bridge/a2-e001-material-markov`
   - future-compatible quotient -> material future-state specialization bridge。

### 2.4 E001 engineering owners — 3

1. `engineering/e001-material-impulse-v2`
   - finite impulse/momentum、force activation、retained remainder 与 reversal-certificate frontier。

2. `engineering/e001-material-contact-network`
   - bounded contact-network incidence/Gram、cycle-kernel 与 rank-duality owner。

3. `engineering/e001-measurement-area-refinement`
   - exact measured-polyline area shells、refinement variation 及其 regressions。

此前 pair-impulse 与 multi-action owner generations 已不再是活动写入点；其有界结果已经 promotion，对应分支现在是 provenance。

## 3. 已耗尽、provenance 或 replay-required generations

不要为了“看起来最新”而 fast-forward 以下 generations。

### Provenance / absorbed

- `core/a2-future-quotient-v2`；
- `core/a3-relation-state-v2`；
- `core/a4-admissible-support-v2`；
- `program/p021-causal-focusing-v2`；
- `engineering/e001-material-impulse-world`；
- `engineering/e001-material-pair-impulse`；
- `engineering/e001-material-multiaction-protocol`；
- owner registry 中已机械/语义判定 absorbed 的 E002 v2 generations；
- owner registry 中已 absorbed 的 P023 与 historical P018 all-power quotient generations。

### Replay-required / stacked sources

- `research/core/relation-quotient` — broad historical A3 source；
- `research/core/relation-support-bridge` 与旧 `bridge/a3-a4-v2` — B01-B06 已进入 thin v3 bridge，其余历史 metric/count/future-language 材料必须按真实 owner 重新归属；
- `engineering/e001-material-state-cost` — 携带 upstream future-state dependency 的 stacked benchmark/application source；
- validation/stacked PR 即使 tests 全绿，也不能因此被当作 canonical merge vehicle。

## 4. 选定历史 PR 审计

结果守恒使用语义分类，不按 branch 年龄分类。

### 已按 absorbed / strict-generalization 关闭

- #22 P005 — `ABSORBED / SEMANTIC`；
- #23 P017 mirror support/incidence — `ABSORBED / STRICT_GENERALIZATION`；
- #65 P017 rough/high-band resource route — `ABSORBED / STRICT_GENERALIZATION`。

### 因仍有 unique 资产而保持 open

#### #21 — `STILL-UNIQUE / REPLAY-QUEUE`

仍有以下独有历史数学：

- support product `G>2k` 下通过 centered carry 得到的 large-support hit；
- 通过 smooth half-scale cofactor 得到的 exact-support closure；
- four-prime support-set reindexing / basin contribution formula；
- `basin_aggregate.py` + tests；
- 尽管后续路径被复用，historical Supplement-06 text 本身仍保留 provenance。

但 historical executable 现在不能原样 replay：`basin_aggregate.py` 导入 `.four_support`，而 current `main` 与 #21 head 都不存在 `src/enterprise_math/four_support.py`。因此旧 quality failure 是该历史切片的真实 dependency defect。它**不是** P017 的 HARD_BLOCK。owner 后续可以先单独 replay 不依赖该模块的 large-modulus / exact-support layer；在发布 aggregate tail layer 前，必须定位、重建或明确 supersede four-support tail dependency。

因此不要把 #21 当 absorbed 关闭，也不要 wholesale merge。

#### #54 — `EXECUTABLE PROMOTED / PROSE-PROVENANCE`

- canonical `prime_gap_slack.py` 此前已经 exact-present on main；
- 仍独有的 centered-prime-radius Stage-9 executable layer 已通过 L4 PR #270 replay，并在三门仓库 gate 全绿后以 `b4801960` 合入；
- historical Supplement prose / numbering / lineage 被有意排除在 #270 之外，仍保留为 provenance，直到以后 selectively replay，或明确分类为 superseded/rejected。

不要 wholesale merge #54。

## 5. 当前 P022 publication chain

P022 仍是一个 geometry theorem home，但 publication 必须按依赖与 payload 分切片。

1. **`A_p` / root-lattice geometry** — 在本快照前已经 canonical。
2. **Geodesic multiplicity + HCP executable core** — 经 PR #262 / `fc81a15a` canonical。
3. **Barlow stacking executable core** — 经 fresh two-blob L4 PR #288 / `aec7f625` canonical；validation PR #261 已关闭为 publication provenance。
4. **Barlow task-relative precision** — 源 PR #265 已独立三门全绿；其两个 frozen blobs 正在 L4 PR #292 中进行 current promotion。
5. **Periodic growth 与 coordination observables** — stacked validation PR #267 与 #269 均已独立三门全绿，但在前置层 canonical 前必须保持 non-merge source；以后每层仍须单独 fresh bounded L4 publication。
6. `program/p022-geometry-v2` 上当前 observation-history / collision / repair research 继续作为独立 owner work，由 scheduler Issue #240 协调。

## 6. 相对旧 12-route ledger 的 scope-audit 修正

当前机器路由相对旧账本有四项实质变化：

1. `core/a3-relation-lattice-v3` 已成为活动 A3 owner generation。
2. E001 pair-impulse 与 multi-action generations 已转 provenance，不再是 active owners。
3. `engineering/e001-material-contact-network` 与 `engineering/e001-measurement-area-refinement` 是替代上述耗尽写入点的当前 bounded E001 owner generations。
4. P022 geodesic/HCP 与 Barlow stacking 已 canonical；Barlow precision 是当前有界的下一 publication slice，而不是再做一次 broad-owner merge。

因此，本快照中的 live semantic surface 是十三条路线，即使仓库中还存在更多用于 validation、provenance 或 stacked research 的 Git refs 与 open PRs。

## 7. Canonical promotion protocol

对每条 active owner 或 bridge：

1. 本地研究，不做 whole-main synchronization；
2. 跨路线需要消费时，通过 Relay 发布可复用 proved WIP/counterexamples；
3. freeze exact publication payload；
4. 从当时 current `main` 启动一个 L4 integration；
5. 只 replay owner-owned frozen assets；
6. main 后续移动时检查实际 intervening deltas，不因为 main 自身移动而制造新的 replay generation；
7. 在 final merge state 上运行 `quality`、`bilingual-sync`、`reference-integrity`，并在适用时运行 Lean 与 shared-surface gates；
8. 只 merge 该 L4；
9. asset conservation 明确后，将被替代的 validation/replay PR 标为 provenance；
10. 只有 historical branch 的每一项 unique result 都明确归入 `INTEGRATE`、`SUPERSEDED`、`COMPARATOR-NEGATIVE`、`OWNER_MOVED` 或 `REJECTED` 后，才可关闭该历史 branch。

移动中的 `main`、CI、review、ACK latency 或其他路线的 publication queue 都不是 research stop condition。只有一个完整指定、并且确实消灭了所有 owner-local meaningful work 的 hard dependency 才构成 `HARD_BLOCK`。

## 8. Authority rule

本文件有意保持为快照。如果它与 current owner registry、scheduler 或 live runtime claims 冲突，应使用：

`branch_governance_overrides.json -> research_scheduler.json -> Issue #240`

确定当前 routing；数学真值则以 canonical `main` + `docs/PROBLEM_STATUS.*` / theorem documents 为准。
