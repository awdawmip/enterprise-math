<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-OPENAI-ETH-BRC-REPRESENTATION-20261028",
  "title": "ETH 算法的 BRC 保真表示与位复杂度接口",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "已定位固定 ETH 稿与形式化范围；待完成一个具体表示的保真证明或反例及实际位成本推导。",
  "next_action": "从固定稿共享线性摘要与分组求和中选定一个完整步骤，写清输入、上下文、载体与恢复关系。",
  "dependencies": [],
  "source_refs": [
    "awdawmip/enterprise-math@55d7023906e9a82198047820bfb5cd29efcaf566:research_notes/OPENAI_ETH_QFT_PROJECT_RELEVANCE_20261027_0809.md",
    "awdawmip/enterprise-math@382e6d3005559d808b8ed49cded36d2b01b299b2:p000_reality_foundation.json",
    "awdawmip/enterprise-math@382e6d3005559d808b8ed49cded36d2b01b299b2:definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json",
    "awdawmip/enterprise-math@382e6d3005559d808b8ed49cded36d2b01b299b2:definitions/RESIDUAL_FAITHFUL_DISCRETE_RELATIONAL_SYSTEM.json",
    "awdawmip/enterprise-math@382e6d3005559d808b8ed49cded36d2b01b299b2:definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json",
    "awdawmip/enterprise-math@382e6d3005559d808b8ed49cded36d2b01b299b2:docs/P023_COMPOSITION_SAFE_COLLAPSE.en.md",
    "awdawmip/enterprise-math@382e6d3005559d808b8ed49cded36d2b01b299b2:definitions/ENTERPRISE_BRC_MULTIPATH_ENRICHMENT_BRIDGE_20260821.md",
    "awdawmip/enterprise-math@382e6d3005559d808b8ed49cded36d2b01b299b2:definitions/ENTERPRISE_BRC_WEIGHTED_LOG_FOUNDATION_20260902.md",
    "openai/math@7ef5c0cc5ca4b0e072b7a050fca09ab24bc6fa3a:preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/build/main_full_version.tex",
    "openai/math@7ef5c0cc5ca4b0e072b7a050fca09ab24bc6fa3a:lean/docs/378.md"
  ],
  "evidence_status": "SOURCE_BOUND_TASK_SPECIFICATION",
  "last_progress_ref": "awdawmip/enterprise-math@55d7023906e9a82198047820bfb5cd29efcaf566:research_notes/OPENAI_ETH_QFT_PROJECT_RELEVANCE_20261027_0809.md",
  "last_progress_at": "2026-10-27",
  "hard_block": null,
  "tags": [
    "BRC",
    "ETH",
    "representation",
    "bit-complexity"
  ],
  "claim_lease_minutes": 120,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-OPENAI-ETH-BRC-REPRESENTATION-20261028",
  "parent_objective_id": "OBJ-GEOMETRY-BRC-RESIDUAL-ACCUMULATION-SYSTEMS",
  "parent_objective_generation_id": "OG-7AE66316D7566C519AE0",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "ETHQFT",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "NEW_DIRECTION",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:be0a92bae790fc5100f066235a0257c9a75470d152b48cd36909c318d6a61107",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# ETH 算法的 BRC 保真表示与位复杂度接口

## 0. Mother question

母目标：`OBJ-GEOMETRY-BRC-RESIDUAL-ACCUMULATION-SYSTEMS@OG-7AE66316D7566C519AE0`。

本任务承接用户直接指定的新研究方向：把 OpenAI 的 ETH 研究转为 BRC 残差与有限几何接口中的一个可证明、可核算的结果。
母问题是：外部算法的一个中间表示，究竟保留了哪些分支、联合关系和未来输出；能否在明确上下文中应用 P023 的保真判据，并以原始输入位长证明表示构造与恢复的真实成本？
首轮产出以一个具体表示为界，不扩展为完整移植 SAT 算法。

## 1. Frozen inputs and scope

外部来源固定为 `openai/math@7ef5c0cc5ca4b0e072b7a050fca09ab24bc6fa3a`：

- `preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/build/main_full_version.tex`；
- `lean/docs/378.md` 及其中真实指向的命题和证明入口。

项目接口起点为 `enterprise-math@86e005efc8990e631f3b28fd090357f5e47f6a95`：

- `docs/P023_COMPOSITION_SAFE_COLLAPSE.en.md`；
- `definitions/ENTERPRISE_BRC_MULTIPATH_ENRICHMENT_BRIDGE_20260821.md`；
- `definitions/ENTERPRISE_BRC_WEIGHTED_LOG_FOUNDATION_20260902.md`。

已有对照记录：`research_notes/OPENAI_ETH_QFT_PROJECT_RELEVANCE_20261027_0809.md`，发布提交 `55d7023906e9a82198047820bfb5cd29efcaf566`。
执行时核对所用项目接口的现行版本；若有变化，逐项说明，不把两个版本的前提拼接使用。

起步选择原文“共享线性摘要与分组求和”中的一个可完整跟踪的步骤；先摘出真实符号、输入、边界和恢复关系，再定义项目映射。
细对象可以是带边界的子问题或完整中间代数状态，不能未经证明就设成一个布尔赋值。
外部代数方法作为有类型的算法对象；本任务保留 P000，不能从算法表达推出原生六轴空间、时间或物理动力学的新结论。

## 2. Hard target and required outputs

### A1：外部定理与选定表示的调用合同

交付一份精确范围表，记录来源位置、真实定理编号或符号路径、输入编码、固定参数、输出、时间模型、空间界和必要前提。

- 分开记录修订稿的 `(n+m)^{O_k(1)} 2^{O_k(n log log n / sqrt(log n))}` 与公开形式化范围的 `(L+1)^{O_k(1)} 2^{O_k(n (log log n)^2 / sqrt(log n))}`。
- 说明 `n` 是变量数，`m` 是子句数，`L` 是规范编码位长，`k` 固定；固定密度的更强界另外保留 `m <= Dn` 及固定 `D` 的前提。
- 选定步骤必须给出输入、上下文、代数载体、输出、恢复关系和依赖。多个采样值联合插值时，合同对象是完整采样向量。
- 分别记录原文主张、公开证明入口可定位、本地实际重跑通过三种证据。未执行就不声称独立形式检查通过；挑战模板与实际证明入口分开。

### A2：一个表示的保真结论及完整位成本

明确对象空间 `X`、表示空间 `Q`、映射 `q`、目标输出 `h`，以及边界、剩余约束、允许未来操作和时域。
至少交付以下一项具有完整证明的数学结论：

- `q(x)=q(y) => h(x)=h(y)`，并给出恢复映射；
- 同一表示导致不同目标输出的具体反例，并标明缺失的联合关系或上下文；
- 单一摘要不足、完整联合表示足够的精确范围结论。

实际应用 P023 的纤维常值或下降判据，说明被消去和被保留的信息。
对自然数计数、Boolean 支持、正质量 CWM、有限域和有符号系数分别定型；有限域零值或正负相消不能解释成 Boolean 不可达。
涉及联合分支、路径顺序、来源或重数时，证明所选观察及所有声明未来操作可经表示恢复；未证明者保留。

资源账至少包含：表示个数与位长、生成成本、运算次数及每次位成本、比较和去重、恢复、峰值空间。
若细状态数为 `N=2^n`，明确 `N-c0` 轮精化与关于短输入 `n` 的算法界不同。
存在一个小表示不等于可高效找到该表示；恢复成本也计入总界。
若需要运行项目算子，使用实际有类型 BRC 入口并记录版本、载体、分支来源、操作、观察和输出；精确算术代码不能仅凭命名充当 BRC 复用。

## 3. Research value to preserve

价值在于给 BRC 残差与几何有限接口留下一个真正可复用的表示引理、一个带范围的失败见证或一份资源障碍证明。
外部算法的次指数定理、项目中新增的条件化推论和有限运行记录分别保留。
精确输出保真可以成立而高效构造失败；局部观察保真可以成立而扩展未来操作后失败。这些区分本身就是有用结果。
残差非零不构成放弃研究对象的理由；应识别它承载的分支关联、允许传播和后续可观测影响。
若现有载体不能表达所需相消，保留符号问题并写出缺失接口，不用正质量替代相位或符号。
涉及原生残差归因时沿实际有类型 BRC 路线推进；本任务不以外部算法运算替代原生物理桥接。

## 4. Success, kill, and return criteria

成功要求 A1 与 A2 共同完成：来源范围可唯一定位；一个具体步骤已有完整保真证明或反例；成本账可沿实际构造得到总界。
只做文献摘要、只指出“都在压缩”、只列若干小样例或只给存在性表示，均不满足本任务。
有限实例可以核对具体等式和反例，不能替代全称证明或渐近复杂度证明。

若候选步骤依赖未公开内容，转到同一公开材料中更小而完整的步骤，并保留原缺口。
若共同摘要缺少必要上下文，交付可核验反例和最小修复义务；不能把外部方法的局部摘要升格为任意未来安全商。
若修复需要新增 BRC 载体，交付明确类型和必要运算的后续提案，本任务不悄悄修改基础定义。
若最终只有结构类比或成本无改进，仍可按证据结项；不能报告获得项目算法加速。
返回材料须含完整数学对象、来源版本、证明或反例、成本推导、实际执行状态以及最小未决问题。
