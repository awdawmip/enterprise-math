<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-N-COUPLED-ASYMMETRIC-SINGULARIZATION-PRIMITIVE",
  "title": "N 耦合非对称奇异化原语",
  "kind": "RESEARCH",
  "owner": "research/n-coupled-asymmetric-singularization-primitive",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Construct or obstruct a genuinely public N-coupled primitive that creates a proper nonempty hidden-CRT singularity pattern without naming hidden factor support and without reducing the singularization layer to the classical mechanism families already bounded by the multiplicative-bridge review.",
  "next_action": "Freeze a small exact N-coupled operator grammar and one initially CRT-invertible typed state family; classify the mod-p/mod-q channel action symbolically, then search for the first exact asymmetric rank/nonunit transition or prove the grammar cannot create one without an additional selector/state datum.",
  "dependencies": [
    "driver_reviews/MULTIPLICATIVE_BRIDGE_GEOMETRY_TASKSET_DRIVER_REVIEW_20260829.md@main",
    "research_driver/R059D_STAGE_N_DRIVER_FREEZE_20260816.md@main"
  ],
  "source_refs": [
    "research_result_records/RS-BRC-COPRIME-FIBER-BRIDGE-CLASSIFICATION/RR-B64E535B63DAEA5879FE.json@main",
    "research_result_records/RS-BRC-FACTOR-BLIND-BRIDGE-ENDPOINT-RECOVERY/RR-4C9E1B7A62F305D8A114.json@main"
  ],
  "evidence_status": "EXPLICIT_OPEN_RESIDUE_FROM_CLOSED_MECHANISM_CLASS / R059D_PURE_ALGEBRA_COLLAPSE_AVAILABLE / N_COUPLED_CRT_ASYMMETRY_UNRESOLVED",
  "last_progress_ref": "driver_reviews/MULTIPLICATIVE_BRIDGE_GEOMETRY_TASKSET_DRIVER_REVIEW_20260829.md",
  "last_progress_at": "2026-08-29T11:36:00+00:00",
  "hard_block": null,
  "tags": ["BRC","multiplicative-geometry","N-coupling","CRT","singularization","asymmetry","collapse","factor-blind","prior-art-guard"],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-N-COUPLED-ASYMMETRIC-SINGULARIZATION-PRIMITIVE",
  "parent_objective_id": "OBJ-N-COUPLED-ASYMMETRIC-SINGULARIZATION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "NCAS1",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "NEW_DIRECTION",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# N 耦合非对称奇异化原语

## Mother question

对未知不同奇素数半素数 `N=pq`，能否只使用公开的 `N`、公开初始状态与固定的因子盲算子规则，产生一个在隐藏 CRT 分解下**恰有一侧奇异、另一侧仍非奇异**的状态或算子，而执行过程中完全不输入 `p,q`、不枚举候选因子，也不把已有的 support/gcd/order/collision 方法改名为“坍塌”？

允许最后使用标准的 public nonunit/gcd readout；真正需要判新的，是**奇异化如何被产生**，而不是最后如何读出已经存在的非平凡因子。

## Frozen inputs and scope

1. 继承 Multiplicative Bridge Geometry 已接受边界：carrier/fiber 分离、bridge morphism、selective-collapse 三层必须区分。
2. 当前 F3R2 的 public coefficient-support bridge 只证明 support bridge existence；`GL_2(Z)` 平衡线性算子本身模任意 `N` 可逆，不能自行产生单侧 CRT rank collapse。
3. `gcd(N,g)` / `gcd(N,h)` 一旦直接返回 proper divisor，说明 endpoint 已由普通 gcd 暴露；不得把该层重新包装成新 singularization primitive。
4. 继承 R059D 的纯代数 coupled-collapse normal form 作为可复用局部原语，但人工注入一个预先选择的 selector bit/state 不算本任务成功。关键问题是 `N`-coupling 能否**产生或强迫**所需的 asymmetry/selector。
5. 不以 additive number-line distance 为 primitive；允许 subtraction 作为 algebraic collision/equality expression。
6. 允许的第一轮 candidate grammar 应显式冻结且保持低复杂度，例如固定小维矩阵/张量状态、整数多项式或有理整除安全的 `N`-dependent coefficients、有限次 composition、determinant/minor/rank/nonunit observables。研究员可以缩窄 grammar，但不得在看到目标因子后再改 grammar。
7. 允许 exact finite census 作为反例搜索和回归，不得把 bounded census 当成 all-N proof。

## Hard target and required outputs

Hard target:

`N_COUPLED_ASYMMETRIC_SINGULARIZATION_PRIMITIVE_CONSTRUCTED_OR_DECLARED_GRAMMAR_OBSTRUCTED`.

Terminal return 必须完成以下之一：

### A. Positive primitive

给出一个完全公开、factor-blind 的 `S_N` 与初始 typed state family，并证明在声明的无限或精确参数族上：

- pre-state 在每个隐藏 CRT channel 上满足声明的非奇异条件；
- `S_N` 执行不读取 `p,q`；
- post-state 的某个 exact determinant/minor/rank/nonunit pattern 在 `mod p` 与 `mod q` 间产生 proper nonempty asymmetry；
- asymmetry 不是通过显式 support naming 或先验候选因子 schedule 注入；
- public observability 与 endpoint extraction 单独陈述；
- 若最后使用 gcd，只把 gcd 视为 readout，而证明 singularization layer 本身不等价于已有 skeleton。

### B. Exact obstruction

对冻结 candidate grammar 证明 factor-blind `N`-coupling 无法生成 proper nonempty CRT asymmetry，并精确指出最小缺失项，例如：

- selector/history/context state；
- 非线性跨通道 coupling；
- 非可逆 completion event；
- 比当前 grammar 更强的 observable/action。

No-go 必须限定 grammar，不得外推成“所有 BRC/CBRC 都不可能”。

### Required evidence

1. exact symbolic channel analysis；
2. 至少一个 adversarial family 或最小反例族；
3. deterministic exact-integer checker/certificate 用于有限回归；
4. 对每个 surviving positive candidate 做 mechanism classification；
5. 明确列出哪些候选落回既有机制，哪些仍无法归约。

## Research value to preserve

Multiplicative Bridge Geometry 已经把旧问题从“整数之间多远”改写成“什么操作真正改变 carrier/channel singularity”。旧 support-witness route 的价值已经冻结，继续扩大 prime schedule 没有意义；真正没有被做掉的是：

`PUBLIC N-COUPLING -> HIDDEN CRT ASYMMETRY`

这一层若能构造，会提供一个与现有 support naming 不同的结构性机制；若被精确 no-go，也会明确说明必须引入什么额外状态，直接连接 R059D 尚未解决的 selector 问题。

## Success, kill, and return criteria

成功必须跨过至少一个 accepted prior-art guard，而不是只换表述。

以下任一情况直接归类为 prior-art-equivalent / failed candidate，而不是 positive primitive：

- 预先枚举 candidate prime 并测试 `r | N`；
- 通过 `gcd(N,f(public))` 直接命名已经公开的 coefficient support，而 singularity 没有独立生成层；
- Pollard `p-1` / Williams `p+1` 型 order annihilation；
- generic rho/collision；
- congruence-of-squares / Fermat-style collision 被简单重命名；
- factor-aware oracle 决定 selector；
- 人工注入一个恰好选择 hidden channel 的 selector bit；
- 只展示有限 semiprime 成功率而没有 exact mechanism theorem。

若所有低复杂度 grammar 都失败，返回最强 exact obstruction 和下一层最小扩展，不要无界扩大参数搜索。
