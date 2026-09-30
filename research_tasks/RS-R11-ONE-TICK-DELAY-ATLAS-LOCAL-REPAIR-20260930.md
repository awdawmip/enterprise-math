<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R11-ONE-TICK-DELAY-ATLAS-LOCAL-REPAIR-20260930",
  "title": "R11：一单位一拍延迟的完整图谱、观测残差与准确局部修复",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "R11已有完整状态六周期和一个单延迟案例，尚未给出全部合法槽的一拍延迟分类、严格影响域、累计观测残差及含认证费用的局部修复成本。",
  "next_action": "读取固定R11/R10原文，写出144个候选扰动的无歧义枚举与合法性条件，先证明背景相位约束和一步依赖锥；再核对原始代码/状态清单后运行准确参考与局部修复。",
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-R11-ONE-TICK-DELAY-ATLAS-LOCAL-REPAIR-20260930",
  "parent_objective_id": "PO-X6-UPPER-STRUCTURE-20260906",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-X6-GLOBAL-TRIADIC-FIELD-NETWORK-LAW",
  "successor_gate": {
    "new_information_gap": "R11已有完整状态六周期和一个单延迟案例，尚未给出全部合法槽的一拍延迟分类、严格影响域、累计观测残差及含认证费用的局部修复成本。",
    "why_parent_result_does_not_close_it": "全局更新律与背景周期描述无扰轨道；确定性、守恒和最终周期性不推出扰动回到该轨道，更不推出局部修复便宜。父任务仍开放；这里不声称其已完成或R11已获独立准入。",
    "discriminating_outcomes": [
      "全144案例回原轨道，附允许相位和恢复时间证书",
      "至少一个与原轨道不相交的新周期准确证书",
      "预算内未知，给已验证前缀、影响域和成本；不得称作永久不恢复",
      "局部修复逐拍等价但总成本无收益的负结果"
    ],
    "kill_condition": "任一案例改变原规则、忽略完整pending/b/边界字段、将hash相等当状态相等、重算已知单例充当新增，或把未执行案例标成未知/通过，拒绝相应结论。",
    "alternative_route_or_free_exploration_considered": "已比较有限预算稳定性、返回缺陷、X6全局律、QFT质量加权证书、RP15两个后继及D24第二位提升。既有任务保持原状；本题限定R11时序扰动，不重做通用商或首次周期。外部物理预测尚需固定本构与观察桥梁。",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "闭合八结点、有限144输入和固定256拍使失败可复核；将枚举和局部修复合为一个任务，避免拆出例行重放阶段。其残差/资源结论可直接约束后续动力学和算法主张。"
  },
  "identity_lane": "R11-DELAY-ATLAS",
  "source_refs": [
    "https://github.com/awdawmip/enterprise-math/blob/88e814717bd60144e6a5add07fc4ab596d483b62/research_notes/HEARTBEAT_ACTIVE_CYCLE_CCBF9335_20260930_R11.md",
    "https://github.com/awdawmip/enterprise-math/blob/88e814717bd60144e6a5add07fc4ab596d483b62/research_notes/HEARTBEAT_RELEASE_FEEDBACK_CCBF9335_20260930_R10.md",
    "https://github.com/awdawmip/enterprise-math/blob/88e814717bd60144e6a5add07fc4ab596d483b62/definitions/RESIDUAL_FAITHFUL_DISCRETE_RELATIONAL_SYSTEM.json",
    "https://github.com/awdawmip/enterprise-math/blob/88e814717bd60144e6a5add07fc4ab596d483b62/definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.md",
    "https://github.com/awdawmip/enterprise-math/blob/88e814717bd60144e6a5add07fc4ab596d483b62/docs/P023_COMPOSITION_SAFE_COLLAPSE.zh-CN.md",
    "https://github.com/awdawmip/enterprise-math/blob/88e814717bd60144e6a5add07fc4ab596d483b62/research_tasks/RS_X6_GLOBAL_TRIADIC_FIELD_NETWORK_LAW_20260909.md",
    "https://github.com/awdawmip/enterprise-math/blob/88e814717bd60144e6a5add07fc4ab596d483b62/research_tasks/RTASK-RF-FINITE-BUDGET-STABILITY-20260927.md",
    "https://github.com/awdawmip/enterprise-math/blob/88e814717bd60144e6a5add07fc4ab596d483b62/research_tasks/RS-SLOWSTRUCT-RETURN-DEFECT-NATIVE-20260930.md"
  ],
  "dependencies": [
    {
      "action": "CONSUME",
      "target": "https://github.com/awdawmip/enterprise-math/blob/88e814717bd60144e6a5add07fc4ab596d483b62/research_notes/HEARTBEAT_ACTIVE_CYCLE_CCBF9335_20260930_R11.md",
      "satisfied": true
    },
    {
      "action": "CONSUME",
      "target": "https://github.com/awdawmip/enterprise-math/blob/88e814717bd60144e6a5add07fc4ab596d483b62/research_notes/HEARTBEAT_RELEASE_FEEDBACK_CCBF9335_20260930_R10.md",
      "satisfied": true
    }
  ],
  "evidence_status": "SOURCE_BACKED_CONDITIONAL_DERIVATION_UNREVIEWED_NOT_ADMITTED; ORIGINAL_R11_BUNDLE_NOT_REPLAYED_BY_PUBLISHER",
  "research_value": "把已知活动周期推进到固定规则下的全单延迟扰动分类和有成本的准确局部修复；同时保留状态恢复与累计观测残差的区别。恢复定理、新周期证书和有界未知均有信息价值，但不把未知写成不恢复。",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:44b2174111ec85b5dd252d07f474772649a4d36936b2c99acbfa2cfba8af7a73",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# R11 单拍延迟：恢复、持续残差与修复费用

## Mother question

在保持同一个原生转移 F、完整未来状态 X=(q,p,w,b) 和既定观察者的条件下，局部正质量的到达延迟究竟被消化、改变长期轨道，还是在预算内无法分类？准确局部修复何时真正少做工作，而不是把工作转移给缓存、全场输出或证书？本题研究内部动力学，不将其直接解释为自然界的退相干或量子纠缠。

## Frozen inputs and scope

GLOBAL_KNOWLEDGE_V1 固定为 awdawmip/chatgpt-global-knowledge@688f64b4be0b0594f5a3774bbf88171080ea322e；科学输入固定为 awdawmip/enterprise-math@88e814717bd60144e6a5add07fc4ab596d483b62。source_refs 给出原文。R11/R10均保留作者证据、未经独立准入的身份。

固定 R11 的5832结点环境、闭合8材料结点、原地址/邻接、G={0}、反馈0→1→2→0、三端口及1/2/3拍发射延迟；完整状态必须包含所有正remaining pending槽、类型/端口/数量、q、w及全部b。准备态周期为 C_0,...,C_5，对应原文t=1,...,6。不得改门、反馈、边界、更新次序、发射延迟或背景初值以使结果好看。

扰动 I_(a,v,s)：选a∈{0,...,5}、8材料结点v、C_a中数量为正的一个pending槽s=(port,type,r)，只把该槽的一单位移到相同(port,type,r+1)。其余字段、总正质量48不变。A型相位每结点2槽、B型4槽，故候选带标签输入应为3×8×2+3×8×4=144。必须核验每个注入态合法性；若源验证器限制了r的上界，先给精确契约差异，不能默默删案例或把发射延迟也改掉。原R11单延迟案例只算回归。

执行输入边界：发布者已读原文，但没有重放R11原始完整代码包。原文标识 test_cycles.py 的SHA256为49d1c6ed0be596b82fa8bfa963df934fc1702cf91feda1680fb7f8d8e961c6d7，PROOF.md为fb66e03ed74e46d8546b148f55889c760035357ac4f6c6d3cc9c2f4551f25099。领取后先取得并校验原包，或提交从固定规范到实现的逐字段对应证明；仅据摘要仿写不得称为原包独立复现。取得前可完成下述条件证明，不须把可移植推导停掉。

复用已存在的BRC原生精确算术及R10/R11转移核。地址索引、JSON、hash和相等性检查是控制/验证层；普通整数或Fraction模拟不得冒充BRC物理主路径。补丁表示为背景上的完整正状态替换，不能将有符号差分当成可抵消的物质量。

## Hard target and required outputs

A. 输入清单与可检查证明。固定周期、合法性、端口类型、完整状态编码及观察量。给出144条案例清单。证明或纠正：未受扰背景的最小周期3迫使原周期恢复相位s满足s=0或3 mod6；不能只看材料结点而接受任意相位。对真实一步依赖图证明 D_(t+1)⊆D_t∪Out(D_t)，其中D_t是相同真实时刻相对背景的完整字段差异支撑；Out含pending交付的直接依赖。正延迟禁止同拍无限传播。本八结点封闭夹具只能检验有限域内传播，不能据此宣布任意大网络的衰减定律。

B. 准确参考与局部修复。每案例从同一注入态开始，参考法完整逐拍调用F；修复法只对差异支撑及其一步依赖闭包重算同一个非线性F，并删除已与背景相同的补丁。门和反馈重新计算，不作线性叠加假定。每一已执行拍比较全部X字段及增量观察量；hash仅定位，证书必须验证精确tuple相等。另给任意图/有限时间的局部重算等价归纳证明，准确列出适用假设。

C. 三分分类及观测账本。每案例只可报告 RECOVERED、NEW_CYCLE、UNKNOWN_BUDGET，并另标 NOT_RUN/INPUT_UNAVAILABLE（不可并入未知或通过）。RECOVERED须给首次完整状态等于原周期状态的时刻和允许相位；NEW_CYCLE须给完整重现状态、周期边序列和与原轨道不相交证书，周期长度改变不是必要条件；UNKNOWN_BUDGET给实际执行拍数及已核验前缀，不等于永久不恢复。每案例另报告原文逐拍释放组数、提交数、到达数、端口通量的累计差：状态恢复不自动等于累计观察恢复。相位对齐后的常量偏置以及相对原时钟的周期偏置须明确保留。

D. 资源和界。预先统一B=256拍/案例，进程CPU预算1800秒、RSS上限1GiB，顺序处理案例。触顶立即保存已完成证书和实际中断位置；不得只挑恢复案例。给max|D_t|、传播图距离、恢复时间或发现周期时间、BRC操作分项、系数最大位长、pending槽数、缓存字节、峰值RSS、建周期/建索引/修复/逐拍全场比较/证书生成与检查/输出各项和总成本。相同输出合同下比较参考与修复；只报修复核提速而省略全场验证不算端到端收益。用结构证明延伸资源界，不能由8结点样本外推规模律。

可复核的条件计数界：在确认w=0、三端口输出类型固定、注入一拍后remaining≤1/2/3后，24个q质量槽与48个pending质量槽共72槽，总质量48；加材料b及统一背景相位，状态数至多3^9·binom(119,71)。这是粗上界而非恢复时间界；须核验假设并可给更紧界。每个质量计数≤48不代表累计通量或实际对象存储为常数。证书生成器和验证器也应计费。

交付：PROOF.md；INPUT_MANIFEST.json（原包及BRC核的完整hash和版本）；144条CASES.jsonl；恢复/新周期完整证书；参考与修复实现；COST.json；反向破坏测试。观察量、注入、预算在出结果前固定。

下列路径是本任务必须产出的验收入口，发布时尚未实现，不是已通过测试：

```text
python research_checks/r11_delay_atlas/verify.py --manifest research_checks/r11_delay_atlas/INPUT_MANIFEST.json --require-cases 144 --max-ticks 256 --strict
python research_checks/r11_delay_atlas/test_mutations.py
python research_checks/r11_delay_atlas/cost.py --include-certification --include-output
```

verify必须核对全部144标签、每个实际前缀、分类证书、完整字段相等及失败/中断计数，零案例不得成功。破坏测试至少覆盖删除一个pending槽、篡改remaining、漏一个背景b、改门、伪造相位、丢累计通量、hash碰撞替身、把未执行标通过。验收可接受严格负结果或明确预算未知，不要求144例全部恢复。

## Research value to preserve

已有安全商回答哪些信息可以忘，却未给这个受扰非线性系统的低成本恢复算法。R11周期快进、P023商兼容性、有限预算稳定性和返回缺陷均不是本图谱的替代。新增信息是完整输入族上的恢复/新周期边界、不能消掉的观察残差，以及有付费证书的局部工作量。三者在同一任务验证，避免把重复演示拆成多个新阶段。

先行对照：Bond–Levine, Abelian Networks I, arXiv:1309.3445v3, Definition 2.1及Lemma 4.7，依赖输入交换公理且后者有停机条件，不能自动用于活动周期中的一拍延迟。Acar, Self-Adjusting Computation (2005), Chapter 7及Theorem 20/34，以计算迹差和维护费用解释增量成本；借用分析思路须证明本转移的依赖语义，不能将小输入支撑直接等同小工作量。本题不主张一般局部性或增量计算为项目原创。

## Success, kill, and return criteria

成功是条件清晰的恢复命题、一个准确新周期/不等价反例、准确局部修复及明确资源边界，或完整预算图谱中的严格未知边界。原代码不可得属于输入证据缺口，不属于物理/数学反证；必须交回已经成立的条件证明和精确缺失项。

一旦规则改变、位长/全局认证成本被隐藏、未执行被记为通过或旧单例被冒充新增，停止相应主张并保全最小失败证据。无需继续扩大样本来掩盖失败。全部144有限验收完成后，不自动扩成无限晶格或量子物理任务；保留可复用结果与仍未闭合的母问题边界。
