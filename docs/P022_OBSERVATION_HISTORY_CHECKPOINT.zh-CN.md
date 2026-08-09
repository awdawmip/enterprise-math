# P022 — Observation、History、Collision 与 Repair Checkpoint

状态：`ACTIVE RESEARCH CHECKPOINT / PROVED WIP ROUTER`  
归属：`program/p022-geometry-v2`  
任务分支：`research/p022-observation-history-20260809`

本文件是当前 P022 research generation 的紧凑路由，不修改 canonical `PROBLEM_STATUS`，也不把 WIP 结果晋升为 `main` 定理。

## 1. 当前 theorem groups

### Observation geometry and history

- `P022_BARLOW_LOCAL_OBSERVABILITY.*`：两个连续 coordination shells 恢复当前无序 absolute-drift pair；统一 state-observation depth 恰好为 2。
- `P022_BARLOW_COORDINATION_HISTORY_SUPPLEMENT_01.*`：完整 coordination history 恢复 global shortest-path multiplicity spectrum，而不只是总数。
- `P022_BARLOW_HISTORY_STRATIFICATION.*`：一个 terminal height-stratified shell profile 与完整 coordination history 信息等价，仅丢 side exchange。

### Checkpoint fibers and collision statistics

- `P022_BARLOW_HIGHER_COLLISION_PRECISION.*`：generalized binomial power-sum 因子化与 exact higher-collision Pareto 冲突。
- `P022_BARLOW_WORST_FIBER_SCHEDULING.*`：odd-balanced/pair-balanced schedule 精确最小化最大 observation fiber。
- `P022_BARLOW_FIBER_CONVOLUTION.*`：完整 selected-layer fiber profile 构成乘法卷积代数，并可反演回无序 checkpoint segment geometry 与 hidden tail。
- `P022_BARLOW_PAIR_COLLISION_ALIAS.*`：固定 `N,m` 的 exact 例子证明 `J_2` 单独不能识别 checkpoint geometry。

### Event-driven repair

- `P022_BARLOW_EXCURSION_ORIENTATION_REPAIR.*`：one-sided signed recovery 每个 zero-departure excursion 恰需一个 orientation bit。
- `P022_BARLOW_TWO_SIDED_REPAIR.*`：two-sided exact repair 为每个 zero excursion 一个 bit，加每个 diagonal side split 一个 bit；fiber size 为 `2^(E+B)`。
- `P022_BARLOW_REPAIR_POLYNOMIAL.*`：weighted chamber polynomial 统一 repair dimension、quotient image、microscopic domain、aggregate repair load 与 P011 collision data。

## 2. 高价值 exact conclusions

1. Precision optimization 是多目标问题：普通 balanced checkpoints 最大化 image size 并最小化 `J_2`；odd-balanced pair packets 则最小化最大 fiber / 最高可能非零 collision order。
2. 完整 P011 collision polynomial 精确编码 selected-layer checkpoint geometry **到 segment order 为止**，并恢复 unobserved tail；`J_2` 单独存在 exact aliases。
3. 当前 hidden Barlow drift 的 sharp observation depth 为 2，但更丰富的 shell-wide future query 仍可能需要任意长 height horizon。
4. Coordination history 可重新编码进一个 terminal shell stratification；保留 history 会改变 observables 之间的信息序。
5. Hidden state 在特定 boundary events 上产生：zero departure 产生 orientation freedom，diagonal split 产生 side-label freedom。

## 3. Negative boundaries

- 不得把普通 balanced spacing 提升为完整 collision spectrum 的 universal optimum。
- 不得从完整 fiber profile 或 collision polynomial 推回 checkpoint segment order。
- 不得从 coordination history 或 global multiplicity spectrum 推回 coordinate-labelled geometry。
- 不得把 two-channel quadratic-history reconstruction 推广到三通道以上；已有 explicit successor-energy collisions。
- 不得用 average fiber、maximum fiber、`J_2` 或 path total 替代 complete ambiguity state。

## 4. Prior-art-sensitive ingredients

中央二项式与 binomial power sums、Franel-type sequences、Stirling/binomial inversion、有限 Dirichlet convolution、Catalan/ballot decomposition、Weyl-chamber walks 与 sum-of-two-squares arithmetic 都属于经典数学。Enterprise Math 当前只主张已证明的 P022 specialization 及其在 finite-resolution observation/repair 框架中的组合；未单独审计部分的历史新颖性保持 `NOVELTY_UNVERIFIED`。

## 5. Verification boundary

分支已包含 ordinary proofs、exact formulas、executable reference modules 与多组 bounded exhaustive reconstructions。仍需 repository-level CI checkpoint，才能称该 generation 在实现层 clean。Executable checks 支持 proof audit，但不自动把 branch WIP 晋升成 canonical-main theorem。

## 6. Next frontier

CI/consistency cleanup 后继续最强开放问题，不等待 integration：

- 刻画多个 collision orders 的 Pareto frontier；
- 研究保留 labelled observations 时能恢复多少有序 checkpoint placement；
- 继续分析 repair polynomial 的内部 coefficient structure，而不只其 endpoint coefficients 与经典 `z=1` chamber count；
- 只有在 weakest hypotheses 真正超出 Barlow geometry specialization 时，才向上抽象 observation/history 母结构。