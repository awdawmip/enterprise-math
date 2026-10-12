<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-CELL-U27F-09-ARITHMETIC-BRIDGE-20261012",
  "title": "回接整数生成与素数假说的可检验接口",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "能否把经验证的整体关系模型连接到一个不读取素合标签的整数生成程序，并明确定义根操作的结构残差？",
  "next_action": "只先写“整数N如何成为材料与操作输入”的统一生成规则；检验它是否偷偷读取因子表、平方壳或已知素数，冻结后才看标签。",
  "dependencies": [
    "RS-CELL-U27F-08-CONTACT-FORMATION-20261012"
  ],
  "source_refs": [
    "https://github.com/awdawmip/enterprise-math/blob/a02ab81dae21c508708e8774be80a8348a9d469a/research_notes/task_packages/20261012_u27_followup_5d76c1/TASK_PACKAGE.md",
    "https://github.com/awdawmip/enterprise-math/blob/68452be67a2bfdd02b6010c116fdc2f022848611/research_inputs/U27F_20261012/INPUT_MANIFEST.json",
    "https://github.com/awdawmip/enterprise-math/blob/1558a5de9af0f6336d2091e7f30627754f3763a5/research_task_records/RS-U2-NATIVE-OCCUPANCY-BRIDGE-20261007/TP2-E49C20B8D0A6569355F6.json",
    "https://github.com/awdawmip/enterprise-math/blob/c92d3f411ec24a09c5606bd29d1bb7dd8b43c7ae/research_result_records/RS-U2-NATIVE-OCCUPANCY-BRIDGE-20261007/RR-A2E93EC78BC5FE034176.json",
    "research_inputs/U27F_20261012/fixtures/base_case.json"
  ],
  "evidence_status": "U27_CONDITIONAL_UNREVIEWED_INPUTS; TASK_DESIGN_APPROVED_BY_CURRENT_USER; NO_NEW_SCIENCE",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "U27-followup",
    "finite-record",
    "group-B",
    "T09"
  ],
  "claim_lease_minutes": 120,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-CELL-U27F-09-ARITHMETIC-BRIDGE-20261012",
  "parent_objective_id": "OBJ-GEOMETRY-BRC-RESIDUAL-ACCUMULATION-SYSTEMS",
  "parent_objective_generation_id": "OG-7AE66316D7566C519AE0",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "U27F-09",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-U2-NATIVE-OCCUPANCY-BRIDGE-20261007",
  "successor_gate": {
    "new_information_gap": "能否把经验证的整体关系模型连接到一个不读取素合标签的整数生成程序，并明确定义根操作的结构残差？",
    "why_parent_result_does_not_close_it": "祖先U2的RR-A2E93EC78BC5FE034176仍是待审的来源接口缺口返回，不提供本项结论。U27提供有条件、尚未独立审查的输入与工作前缀；当前用户明确要求发布本包剩余任务。本项保持旧Result和父目标状态，不以待审结论为已接受前提。",
    "discriminating_outcomes": [
      "至少一个定义良好的算术接口与其适用范围，附显式可检验预测或同摘要异后继反例。",
      "若有限数据支持假说，仅记为条件支持；新素数定理须另外给全参数证明与计算代价。",
      "若物理/构型属性无法降为整数属性，精确定位准备依赖；允许形成“本模型无该算术接口”的结论。"
    ],
    "kill_condition": "若新结论只能靠重置输入、丢弃相关支路、隐藏额外资源或省略所需作用关系取得，返回可达反例或最小缺口，保留已经成立的条件前沿。",
    "alternative_route_or_free_exploration_considered": "比较了在祖先宽任务中继续、只做单轮参数扩张、独立审查及另起自由探索；本包将多轮、资源、生成、算术和独立审查分为可判别任务。当前指令选择发布这些缺口，后续探索的结论仍按真实前提验收。",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "给出整数表示/组合/根操作中的至少一项非空洞接口定理或反例，形成可证伪的素数假说；不以得到素数判据作为默认通过条件。；本项拥有独立输入接口、证据和反例出口，不因单轮进展自动断言父目标完成。"
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:be0a92bae790fc5100f066235a0257c9a75470d152b48cd36909c318d6a61107",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# 回接整数生成与素数假说的可检验接口

原包：EM-U27-FOLLOWUP-20261012-V1 / PKG-U27F-09。本项仅发布研究任务，未执行研究或审查。

## Mother question

能否把经验证的整体关系模型连接到一个不读取素合标签的整数生成程序，并明确定义根操作的结构残差？

第一项动作：只先写“整数N如何成为材料与操作输入”的统一生成规则；检验它是否偷偷读取因子表、平方壳或已知素数，冻结后才看标签。

## Frozen inputs and scope

复用原包 `em_u27_followup_tasks.zip`，SHA256 `a450cc3e235ca3d37211d31b2d4eb41dd2d4ac28b77c73d18d1b6e3ce45cc9a7`，会话文件 `file_00000000c6d8820697f020b88af9448d`。Source取回入口为 `research_inputs/U27F_20261012/INPUT_MANIFEST.json`；其中已发布起步fixture，完整原代码与证明在该清单指向的原包中，不假称全部安装于Source。取得准确原包后先核对清单；可用原生小输入推进理论/证书设计，科学执行保留真实来源版本。

本项包内输入：
- `fixtures/base_case.json`（原交付包内路径）
- `baseline/cell_u27/NOTE.md`（原交付包内路径）
- `provenance/authority_pins.json`（原交付包内路径）

任务依赖：RS-CELL-U27F-08-CONTACT-FORMATION-20261012
原生归因相关依赖：RS-CELL-U27F-02-NATIVE-TRIAD-20261012、RS-CELL-U27F-08-CONTACT-FORMATION-20261012

依赖未形成时可以先研究显式条件命题；依赖关系保留，最终结论须绑定实际产物，数值或原生归因不越过其前提。

U27及其依赖仍标为有条件、未独立审查的研究输入；同作者复跑不提高证据等级。保留四材料、六轴坐标、来源次序和当前记录分割。工作阶段计数不是物理时钟。具体输入准备或模型修改在返回中分列，不修改P000或原来源证据。

## Hard target and required outputs

给出整数表示/组合/根操作中的至少一项非空洞接口定理或反例，形成可证伪的素数假说；不以得到素数判据作为默认通过条件。

工作单元：
1. 先声明是数量不变量还是统一准备过程的性质；同一N的不同准备与历史必须有可比范围。
2. 第一批可用N=2..12作接口检查，冻结模型与观察后用13..32作条件检验；该范围只是本任务候选试验设计，不是已完成数据。
3. 把平方数、非平方合数、素数幂和素数混合检验；根残差从已声明组合/重建操作中定义，不退回N与最近平方数的距离。
4. 比较“旧素数根残差摘要”“全部旧状态”“当前状态”等预测能力；统计关联、充分性证明和生成算法分别报告。

交付文件：
- `INTEGER_PREPARATION_SPEC.json`
- `ROOT_AND_COMPOSITION_INTERFACE.md`
- `BLINDED_TEST_PLAN.json`
- `ARITHMETIC_BRIDGE_RESULT.md`

复用接口：`verified T08 interaction model`；`existing BRC source/branch composition`。
实际科学计算沿当前项目的typed BRC协议；接口不足时返回具体缺口与可检查关系，不把未执行步骤记作已执行。

## Research value to preserve

给出整数表示/组合/根操作中的至少一项非空洞接口定理或反例，形成可证伪的素数假说；不以得到素数判据作为默认通过条件。 研究应区分观察对象、初态分布、适用时钟与资源预算，保存对照反例和不能互换的条件。复用正确前沿，不为取得会话上下文而重做整条U1至U27。

## Success, kill, and return criteria

正面验收：
- 至少一个定义良好的算术接口与其适用范围，附显式可检验预测或同摘要异后继反例。
- 若有限数据支持假说，仅记为条件支持；新素数定理须另外给全参数证明与计算代价。

反例/缺口验收：
- 若物理/构型属性无法降为整数属性，精确定位准备依赖；允许形成“本模型无该算术接口”的结论。

范围说明：
- 本任务现阶段只可预先设计接口；数值试验等待T08模型冻结。
- 不把新增周期、计数底数或人为路由编码产生的素合信息当作规律发现。

每次返回保存准确输入和哈希、模型变更、证明或反例、代码对应、实际执行覆盖、未处理支路和最小下一问题。仅有有限数据时保留有限范围；研究返回不自行宣称整条父目标完成。
