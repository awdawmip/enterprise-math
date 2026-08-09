# Enterprise Math 当前研究分支账本

状态：`CANONICAL OWNER-ISOLATION LEDGER / CURRENT WRITE SURFACE`  
当前路由基线：`main@85919bbb939ac8155a37c70e088b15b15fab795f`  
此前已审计 11 路快照：PR #215 / `main@683d6baaec90f4d59a5c3a64c9d40a6f3a24a337`  
日期：2026-08-09

本账本记录当前语义写入面。PR #215 正确 canonicalize 了当时的 11 路审计快照；该审计完成后，P025 作为新的独立 L2 program owner 创建，因此当前活动面自然增长为 12 路。这是 Owner-Isolation 下的正常增量，并不意味着 #215 的审计错误。

治理主规则保持不变：

`owner research -> freeze exact payload -> fresh latest-main L4 replay -> exact merge-state gates -> canonical main`。

L1/L2/L3 owner 可以合法落后于移动中的 main；不得仅为“保持最新”而 whole-tree sync main。L4 全局 `NO NEW MATHEMATICS`。

## 1. Canonical reusable layers

当前 main 已包含 A2、A3、A4 第一代 canonical cores；thin A3->A4 generated-support B01-B06 bridge；P021 causal-boundary core；P022 `A_p`/root-lattice geometry core；Owner-Isolation 执行规则；scope-aware branch audit；E001 finite impulse-world integration；以及后续 P018 quotient-channel coalescence。

本轮压缩/发布的重要 merges 包括 `87231d29`、`ca923d64`、`e8407882`、`21c1ef66`、`4a4a2fde`、`683d6baa` 与治理 merge `85919bbb`。

## 2. 当前活动写入面：12 条分支

目标区间不是永久配额。12 条目前处于预期紧凑写入面的上沿，而且每条都有不同的 theorem/application home。

### 2.1 Program owners — 6

1. `program/p017-legendre`
   - square-basin / Legendre pressure-test frontier；
   - 当前 branch-side 工作仍属于 P017。

2. `program/p018-precision-v2`
   - precision-specific frontier；
   - generic future quotient 仍归 A2/P023。

3. `program/p021-causal-focusing-v3` — Draft PR #213
   - causal-boundary promotion 后的新 generation；
   - 保留 focusing、direction-orbit/causal-role、causal witness 与受物理边界约束的应用路线。

4. `program/p022-geometry-v2`
   - `A_p` lattice core 已 canonical；
   - geodesic multiplicity、HCP 与 Barlow 继续作为同一 geometry owner 内的研究。

5. `program/p024-action-precision`
   - closed-form action-language / boundary-precision specialization；
   - generic quotient 与 adjunction 继续归上游 owner。

6. `program/p025-abc-support-collapse` — PR #216
   - 在 #215 的 11 路审计完成后创建；
   - 拥有 abc 压力测试：radical-support collapse、multiplicity residual、exact integer rational-exponent defect、relation-conditioned witness-precision candidates、P025 prior-art、lineage 与 regressions；
   - 明确不把 radical 当成 addition congruence；
   - generic correspondence / quotient mother theory 仍归上游 owner；
   - 不声称证明 abc conjecture，也不改变 canonical problem status。

### 2.2 Cross-owner bridges — 3

1. `bridge/a3-a4-generated-support-v3` — thin A3 relation-state -> A4 generated-support bridge。
2. `bridge/p017-p018-hard-core-v2` — arithmetic / precision hard-core、root-channel 与 tail-resource bridge。
3. `bridge/a2-e001-material-markov` — future-compatible quotient -> material future-state specialization bridge。

### 2.3 E001 engineering owners — 3

1. `engineering/e001-material-impulse-v2` — finite impulse/momentum、force activation、remainder 与 reversal-certificate frontier。
2. `engineering/e001-material-pair-impulse` — bounded two-body equal-and-opposite impulse owner，PR #205。
3. `engineering/e001-material-multiaction-protocol` — empirical multi-action protocol -> canonical P023 future partition adapter，PR #185。

## 3. 已耗尽或冻结的 generations

以下是 provenance，不再是当前写入点：

- `core/a2-future-quotient-v2`、`core/a3-relation-state-v2`、`core/a4-admissible-support-v2` — 审计时均观察到 `ahead=0`；只有真正恢复新 mother-theorem work 时才从当时 current main 开新 generation。
- `program/p021-causal-focusing-v2` — causal-boundary payload 已 promotion；PR #182 已关闭为 `PROMOTED / PROVENANCE`；v3 active。
- `engineering/e001-material-impulse-world` — validated one-body wall-world payload 已 canonical；PR #194 是冻结 provenance，#205 是声明的下一代 pair-impulse generation。

不要为了“看起来最新”而 fast-forward 旧 generations。

## 4. Replay-required / stacked sources

以下保留有价值历史，但不是 active mother-theorem home：

- `research/core/relation-quotient` — broad historical A3 source。
- `research/core/relation-support-bridge` 与旧 `bridge/a3-a4-v2` — B01-B06 已通过 thin bridge；其余 B07-B58 必须按实际 owner 重新归属。
- `engineering/e001-material-state-cost` — stacked benchmark/application，携带 upstream `material_future_precision` dependency；以后只 replay 独有 benchmark/test 资产。

## 5. 选定历史 PR 审计

### 5.1 已按 absorbed 关闭

- #22 P005 — `ABSORBED / SEMANTIC`。
- #23 P017 mirror support/incidence — `ABSORBED / STRICT_GENERALIZATION`。
- #65 P017 rough/high-band — `ABSORBED / STRICT_GENERALIZATION`。

### 5.2 继续保持 open

- #21 — `PARTIAL ABSORPTION / CORRECTED / DEPENDENCY-BLOCKED WIP`，Draft。Old L023 已被包含；old L024 后来需要 anchor-survival 修正；L025 因历史 branch 缺少导入的 `four_support` dependency 而尚未验证。
- #54 — `SPECIALIZATION / STILL-UNIQUE REPRESENTATION / UNVALIDATED DRAFT`。Centered-prime-radius 仍可能是有价值的 near-diagonal coordinate，但 replay 前必须重新验证、协调编号并完成 prior-art audit。

## 6. Scope-audit 修正

当前机器路由记录：

1. P022 `p022_hcp_*`、`p022_barlow_*`、`p022_geodesic_*`、P022 tests 与 bilingual registration 属于合法同 owner 资产。
2. `bridge/a3-a4-generated-support-v3` 取代 broad v2 成为 active A3/A4 bridge。
3. A2/A3/A4 v2 为已耗尽 generations。
4. P021 v3 取代 v2 成为 active causal/focusing owner。
5. P025 是 #215 快照后新建的 clean L2 owner，只允许 `P025_*`、`abc_*`、prior-art/lineage 与 registration 路径。
6. E001 impulse-world 为 provenance；impulse-v2 / pair-impulse / multi-action active；state-cost 继续 replay-required。

## 7. 当前 P022 发布顺序

禁止 wholesale 发布大型 P022 owner。下一步审定的切片顺序是：

1. **Geodesic Multiplicity core** — `A_p` + simple-cubic distance/interval/path multiplicity，并由 recursive/direct-enumeration oracle 独立核验；
2. **HCP extension** — exact integer HCP contact graph 与 geodesic-growth 层，明确依赖 GM core；
3. **Barlow family** — 仅在 GM/HCP 分别验证后继续。

## 8. Canonical promotion protocol

对每条 active owner 或 bridge：

1. 本地研究，不 whole-main synchronization；
2. relay 可复用结果；
3. 冻结 exact publication payload；
4. 从当时 current main 创建 fresh L4；
5. 只 replay owner-owned frozen assets；
6. 在 exact merge state 上运行 quality、bilingual-sync、reference-integrity，并在适用时运行 Lean；
7. 只 merge 该 L4；
8. branch-side 资产全部归属后冻结/关闭耗尽 source generation。

移动中的 main 不是 research stop condition，只在最终 L4 combination gate 有意义。
