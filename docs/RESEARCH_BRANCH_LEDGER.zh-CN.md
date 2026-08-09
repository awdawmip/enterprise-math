# Enterprise Math 当前研究分支账本

状态：`CANONICAL OWNER-ISOLATION LEDGER / AUDITED WRITE SURFACE`  
快照：`main@683d6baaec90f4d59a5c3a64c9d40a6f3a24a337`  
日期：2026-08-09

本账本记录 Architecture-v2 / Owner-Isolation 迁移后的当前语义写入面。Git 祖先关系只是证据，不等于所有权：一条分支可以远远落后 main 但仍是有效隔离 owner；一个旧 generation 即使历史提交仍可见，也可能已经在语义上耗尽。

治理主规则是：

`owner research -> freeze exact payload -> fresh latest-main L4 replay -> full merge-state gates -> canonical main`。

L1/L2/L3 owner 不追逐移动中的 main。L4 全局 `NO NEW MATHEMATICS`。

## 1. 本轮迁移已达到的 canonical 状态

以下可复用层已经进入 canonical main：

- A2 k-ary operation-congruence / future-compatible quotient 扩展；
- A3 weighted relation-state / relation-lattice / integer-scale core；
- A4 finite correspondence / admissible-support / relational-spectrum core；
- thin A3->A4 generated-support bridge 的 B01-B06 切片；
- P021 finite causal-boundary core；
- P022 A_p/root-lattice geometry core；
- `AGENTS.md` 中的 Owner-Isolation 执行规则；
- scope-aware branch governance auditor。

按顺序压缩期间的重要 canonical merges 包括：

- branch-ledger refresh：`87231d29`；
- Owner-Isolation AGENTS replay：`ca923d64`；
- thin A3/A4 bridge：`e8407882`；
- P021 causal-boundary core：`21c1ef66`；
- P022 A_p lattice core：`4a4a2fde`；
- 并发 E001 finite impulse-world integration：`683d6baa`。

## 2. 当前活动写入面：11 条分支

目标不是永久固定某个分支数字。当前审计后保留 11 条 theorem/application home 真正不同的写入分支。

### 2.1 Program owners — 5

1. `program/p017-legendre`
   - 当前 square-basin / Legendre frontier；
   - 审计到的 branch-side 工作仅位于 `P017_*` / `p017_*` 资产；
   - 当前 directional 工作仍是 WIP，不占 canonical theorem numbering。

2. `program/p018-precision-v2`
   - 当前 precision-specific owner；
   - branch-side 工作仅位于 P018 / precision partition-margin 资产；
   - generic quotient theory 仍归 A2/P023。

3. `program/p021-causal-focusing-v3` — Draft PR #213
   - v2 causal-boundary promotion 后，从 `main@683d6baa` 新建的 generation；
   - 初始只有 `owner_manifest_p021_v3.json`；
   - 保留 focusing observables、direction-orbit / causal-role structure、causal witness transport、finite causal spectra 以及受物理边界约束的应用路线；
   - generic future quotient -> A2/P023；generic correspondence/witness algebra -> A4；generic precision response -> P018；physical validation policy -> P016。

4. `program/p022-geometry-v2`
   - A_p lattice core 已 canonical；
   - HCP、Barlow stacking/coordination、geodesic multiplicity 及相关 precision 问题继续作为同一 P022 geometry owner 内的活动研究；
   - 因此 `p022_*` source/test families 与 P022 bilingual registration 是合法 owner 资产，不能仅因为文件名不是 `lattice_*` 就判成 `SCOPE_DRIFT`。

5. `program/p024-action-precision`
   - closed-form action-language / boundary-precision specialization owner；
   - generic quotient 与 adjunction mother theory 继续归上游 A2/P023/P008。

### 2.2 Cross-owner bridges — 3

1. `bridge/a3-a4-generated-support-v3`
   - 当前 thin A3/A4 bridge；
   - 第一批三资产 B01-B06 slice 已 canonical；
   - 后续 bridge 工作必须真正同时依赖 A3 relation state 与 A4 correspondence/support。

2. `bridge/p017-p018-hard-core-v2`
   - 活动 arithmetic/precision bridge；
   - 审计到的 branch-side files 仅位于 `p017_p018_*` theorem/test families；
   - 当前包含 hard-core root-channel、tail-resource 与 cubic ambiguity 结构。

3. `bridge/a2-e001-material-markov`
   - 活动 future-material specialization bridge；
   - branch-side files 仅位于 `material_future_*` code/tests；
   - generic quotient/minimization 仍归 A2，material meaning 仍归 E001。

### 2.3 E001 engineering owners — 3

1. `engineering/e001-material-impulse-v2` — PR #190
   - 在已 canonical wall-world slice 之外继续推进 finite impulse/momentum 研究；
   - 保留 force activation、subquantum accumulation、precision re-entry 与 reversal-certificate 问题。

2. `engineering/e001-material-pair-impulse` — PR #205
   - canonical one-body wall impulse world 之后的下一代 bounded two-body generation；
   - equal-and-opposite delivered impulse、total integer momentum invariance 与 relative separation 是明确局部问题。

3. `engineering/e001-material-multiaction-protocol` — PR #185
   - 独立 empirical/P023 adapter owner；
   - explicit measured action graph -> canonical future partition；
   - 不拥有 generic P023 minimization。

## 3. 已耗尽或冻结的 owner generations

以下 refs 不再是当前写入点：

- `core/a2-future-quotient-v2` — 已完全吸收，2026-08-09 审计观察为 `ahead=0`；若新的 A2 mother-theorem work 恢复，应从当时 current main 新建 generation。
- `core/a3-relation-state-v2` — 已完全吸收，观察为 `ahead=0`；仅在真正出现新 owner work 时再建 A3 generation。
- `core/a4-admissible-support-v2` — 已完全吸收，观察为 `ahead=0`；需要时再建新 A4 generation。
- `program/p021-causal-focusing-v2` — causal-boundary slice 已 promotion；PR #182 已关闭为 `PROMOTED / PROVENANCE`；v3 为当前 owner。
- `engineering/e001-material-impulse-world` — 冻结 source PR #194；八文件 wall-world slice 已 canonical 于 `main@683d6baa`。

不要为了“看起来最新”而 fast-forward 这些旧 generations。它们的历史形状属于 provenance。

## 4. 需要 replay 或仍为 stacked 的来源

这些分支包含有价值的历史，但不是当前 theorem home：

- `research/core/relation-quotient` — broad historical A3 source；只能按 owner 选择性 replay。
- `research/core/relation-support-bridge` — broad historical A3/A4 source；B01-B06 已通过 thin bridge promotion，B07-B58 必须按实际内容分别重归 A4/A5/A2/P021。
- `bridge/a3-a4-v2` — 旧 broad bridge generation；不再 active。
- `engineering/e001-material-state-cost` — stacked benchmark/application；携带来自 A2/E001 bridge 的 `material_future_precision`，必须等 upstream bridge canonical 后只 replay 自己独有的 benchmark/test 资产，不能当 mother-theorem owner。

## 5. 选定历史 PR 的语义审计

### 5.1 已按 absorbed 关闭

- PR #22 P005 multi-base scale algebra — `ABSORBED / SEMANTIC`。
  - canonical P005 覆盖 scale-factor compatibility、projection composition、multi-base order、gcd/lcm diamond 与 explicit nonunique refinement witness；
  - 历史 state-only refinement criterion 是 canonical P023 fiber constancy/descent 的 specialization。

- PR #23 P017 transverse mirror support — `ABSORBED / STRICT_GENERALIZATION`。
  - canonical `p017_mirror.py`、`p017_mirror_incidence.py` 与 tests 保留历史 support/incidence 结果，并增加更强的 resource/coprimality 结构。

- PR #65 P017 rough-window/high-band route — `ABSORBED / STRICT_GENERALIZATION`。
  - 核心 cofactor/rough 资产与 Supplements 06-08 保留在 main；
  - 当前 high-band implementation/test/provenance 层严格扩展了历史 resource 结果。

### 5.2 必须继续保持 open 的 research/provenance

- PR #21 — `PARTIAL ABSORPTION / CORRECTED / DEPENDENCY-BLOCKED WIP`，Draft。
  - old L023 已被 canonical L039 包含；
  - old L024 被 L041 修正，后者要求 anchor survival 并给出未加限定版本的反例；
  - 仅 L025 four-support graph-tail aggregate 仍未 canonical；
  - 历史 CI 因 `basin_aggregate.py` 引入不存在的 `enterprise_math.four_support` 而失败，因此 L025 是未验证 WIP，不是 replay-ready result。

- PR #54 — `SPECIALIZATION / STILL-UNIQUE REPRESENTATION / UNVALIDATED DRAFT`。
  - centered-prime radius 是后续 general cofactor-window calculus 的 near-diagonal two-candidate specialization；
  - `centered_prime_radius.py`、其 tests、条件恒等式 `rho(k+1)=sigma(k)+1` 与 `k=10` boundary counterexample 尚未以独立 coordinate layer 进入 canonical；
  - current-head validation、numbering reconciliation 与 prior-art audit 完成前不 replay。

## 6. 本快照中的 scope-audit 修正

scope-aware audit 暴露了两个 metadata 错误和一个 lifecycle 改进：

1. 旧 override 对 P022 过窄。`p022_hcp_*`、`p022_barlow_*`、`p022_geodesic_*`、对应 tests 与 P022 bilingual registration 都是合法同 owner 资产。
2. 新 `bridge/a3-a4-generated-support-v3` 必须取代旧 v2 bridge 成为 active A3/A4 bridge。
3. A2/A3/A4 v2 refs 是已经耗尽的 generations，而不是永久写入点。Canonical theorem homes 位于 main；只有真的出现新 owner mathematics 时才新建 generation。

在本快照中，P017、P018、P021-v3、P022、P024 与三条 active bridge families 按声明路径均未发现跨 home scope 污染。E001 活动 owner 通过 impulse、pair-impulse 与 empirical-protocol 三种角色分离；state-cost 分支明确标为 stacked/replay-required。

## 7. Canonical promotion protocol

对每条 active owner 或 bridge：

1. 在 owner generation 本地研究，不 whole-main synchronization；
2. 将可复用结果 relay 到受影响路线；
3. 冻结选定发布的 exact payload；
4. 从当时 current main 创建 fresh L4；
5. 只 replay 冻结的 owner-owned payload；
6. 在 exact merge state 上运行 quality、bilingual-sync、reference-integrity，并在适用时运行 Lean；
7. 只 merge 该 L4；
8. 当 source generation 剩余 branch-side payload 全部完成归属后，关闭或冻结该 generation。

移动中的 main 不是 research stop condition，只在最终 L4 combination gate 有意义。

## 8. 如何使用本账本

开始新工作前：

- 用 `AGENTS.md` 读取执行规则；
- 用 `RESEARCH_COMMON_SURFACE` 查可复用 theorem/tool；
- 用本账本做 owner/ref routing；
- 用 `branch_governance_overrides.json` 配合 `tools/audit_branch_lifecycle.py` 做机器 scope classification；
- 用 PR/commit provenance 查看历史细节。

不要仅凭 branch age、ahead/behind counts 或历史文件名推断 theorem ownership。
