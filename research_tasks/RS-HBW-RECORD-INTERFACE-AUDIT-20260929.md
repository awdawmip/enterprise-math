<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-HBW-RECORD-INTERFACE-AUDIT-20260929",
  "title": "触发记录候选接口的独立核验",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "候选触发记录接口尚未独立核验；需确认全分布、返回项与计价边界。",
  "next_action": "先独立推导有序返回交叉项与TV归一化，核对保存的T6回归。",
  "dependencies": [],
  "source_refs": [
    "research_notes/heartbeat_outward/20260929_9F026E_PUBLICATION/SOURCE_FRONTIER.md",
    "research_notes/heartbeat_outward/20260929_9F026E_PUBLICATION/SOURCE_MANIFEST.json"
  ],
  "evidence_status": "CANDIDATE_SOURCE_REQUIRES_INDEPENDENT_SCOPE_CHECK",
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "registry_key": "RS-HBW-RECORD-INTERFACE-AUDIT-20260929",
  "parent_objective_id": "OBJ-GEOMETRY-BRC-RESIDUAL-ACCUMULATION-SYSTEMS",
  "parent_objective_generation_id": "OG-7AE66316D7566C519AE0",
  "identity_lane": "HBW-RETURN-9F026E",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "REPLAY",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:44b2174111ec85b5dd252d07f474772649a4d36936b2c99acbfa2cfba8af7a73",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# 触发记录候选接口的独立核验

## Mother question

在不把作者自检当成独立认可的前提下，现有触发记录商、低宽度轨迹和返回修正恒等式，能否形成后续Delta研究可使用的精确接口？这是首次正式登记的候选证据核验，不重设或伪造历史正式任务。

## Frozen inputs and scope

模型及全部原始证据按source_refs固定；源包内THEOREMS.md第1至6节给出定义和候选证明。D=2J-3I，Q=9^T，只有端口1执行a^(2^t)模乘。P0是记录分开分布；Delta(b)为工作相同、记录不同的有序交叉项之和，P_N=P0+Delta/Q。P0的64拍低活跃宽度不意味着原P_N普遍可被精确采样。保持完整可见键、工作相等条件以及同记录内0/2相干。运算入口沿已绑定signed-CWM源码；新增能力须声明对应及代价，不用普通算术改名补证。本任务不研究原生本构推导或直接宣称Shor输出等价。
源报告原研究日2026-09-28；本次仅发布核验任务。核验者使用自身执行身份，不借用原作者的实验或审查身份。已有完整账本是供核验的证据，不是新运行的结果。

## Hard target and required outputs

先核查Delta使用有序beta!=gamma求和以及1/(2Q)的TV归一化，给出独立逐步推导或最小反例。随后确认轨迹选择概率望远镜恒等式、2(t+1)活跃宽度与无返回条件的精确未来操作范围。
交付一份逐项结论表：证明成立/需补条件/反例，分别绑定原证据文件和精确范围。检查源包摘要及关键记录；优先复用保存记录，不重跑64拍整批试验。
有限回归：T3同记录64对32；a2,T4的N21/35/77零误差；T6的N21=80576/531441、N35=33280/531441、N77=0，以及其界122112/531441、39296/531441、0。必要时只执行能鉴别错误的最小BRC单元。
区分标量调用数、整数位长、RNG和审计存储；检查一般无碰撞证书成本尚未解决。输出适用接口清单及应暂停的依赖结论。

## Research value to preserve

保留廉价P0采样与原模型返回干涉之间的严格区分，为后续研究提供可验证输入，而不是让未获独立审查的64拍演示自动成为一般算法前提。

## Success, kill, and return criteria

成功：给出可逐项复查的接口判定及有限回归核对；允许结论是带明确边界的反例。若核心恒等式或类型不成立，保留原始证据、返回最小失败见证，停止依赖该错误的后续构造。
不得将频率近似吻合代替全分布证明，不以扩大相同演示作为核验产出。完成范围是本候选接口核验，不宣告母目标或一般求阶完成。
