<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-FERMAT-RESIDUAL-MEMORY-20261004",
  "title": "费马平方动力学：残差长程保持与观察者最小状态",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "奇素数单位邻域的赋值保持已在聊天中提出；全局平方非单射、非单位与观察升级的精确最小状态边界未系统证明。",
  "next_action": "先复用现有部分操作商与安全压缩接口，冻结模 q 和模 q^2 两种观察语言，构造可区分后缀并分类局部保持与全局合并。",
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-FERMAT-RESIDUAL-MEMORY-20261004",
  "parent_objective_id": "OBJ-GEOMETRY-BRC-RESIDUAL-ACCUMULATION-SYSTEMS",
  "parent_objective_generation_id": "OG-7AE66316D7566C519AE0",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "NEW_DIRECTION",
  "parent_task_id": null,
  "successor_gate": null,
  "identity_lane": "FERMAT-RESIDUAL",
  "source_refs": [
    "research_inputs/fermat_residual_20261004/README.md",
    "research_inputs/fermat_residual_20261004/source_archive.zip",
    "awdawmip/enterprise-math@937aea6bbb6a774d7165a9d8e782940f47248fc4:definitions/RESIDUAL_FAITHFUL_DISCRETE_RELATIONAL_SYSTEM.json",
    "awdawmip/enterprise-math@937aea6bbb6a774d7165a9d8e782940f47248fc4:enterprise_toolbox_registry.json"
  ],
  "dependencies": [],
  "evidence_status": "UNREVIEWED_CHAT_SEED_NOT_ADMITTED",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:d74aad6dd53d0df42d950f7b1207b27d80696f23410bd06f53a038c459577bb2",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# 费马平方动力学：残差长程保持与观察者最小状态

## Mother question

对费马平方链的算术载体，哪些隐藏区别会长期保存，哪些被真实动力学合并，哪些仅对指定观察者可安全省略？能否给出保留状态的充分性证明及最小性见证，而不把“暂时看不见”当作“已经消失”？

## Frozen inputs and scope

模型为整数 x、平方 S(x)=x^2 和显式指定的整数加法；分别冻结观察 O_q=x mod q、O_(q^2)、以及有截断高度的素数赋值。逐项给出允许的未来组合、时间界、模数与资源范围。除以 q、改换模数、查询更高位不默认在原许可内。只有声明过的操作和观察参与等价关系。

复用 src/enterprise_math/partial_operation_quotient.py、composition_safe_collapse.py、brc_transport.py 的现行接口和既有 RS-GBRC-R1-OBSERVER-MEMORY 结果，先核对适用域，不重写通用状态细化器。旧任务处理几何/正权/上下文观察；本任务仅承担整数平方、素数幂精度塔和非单位边界的实例化与额外证明。不预设原生空间桥或量子纠缠机制。

## Hard target and required outputs

严格证明或修正：奇素数 p、p不整除x、p整除非零delta 时，v_p((x+delta)^2-x^2)=v_p(delta)。同时显式检查 x与-x 的全局平方合并、delta=0、p=2、非单位与合数模数；局部可逆性不得升级为全局单射。将实际合并、观察商、受控近似三类机制分别命名和提供反例。

对至少两种不同精度/未来语言，给出保留状态的闭合更新、全允许后缀的观察保真证明，以及每次必要增广的区分后缀；小型状态空间可穷举认证，但一般 k 或无限时间需另给符号证明。核验同 mod5 的2与7在平方加一后的 mod25 区别。联合模数与中国剩余分解只能在保真同构和可获得模数条件下使用，不能以独立边缘替代联合来源。

交付 observer_contracts、state_minimality、transport_classification 和测试证据。若在所选语言中存在更小的商，证明它确实充分；若只在全余数观察下得到 q或q^k 个状态的显然下界，标为基线而非研究增量。解释有限 k 状态与无界精度状态成本的差别。

## Research value to preserve

建立可迁移的判别实例：可逆乘子上的残差可以持续存在，但是否必须携带取决于未来观察。将该结论接入已有 BRC 工具，并隔离非单位耗散、截断损失和坐标假象，避免重复一般观察者最小化理论。

## Success, kill, and return criteria

成功要求一个超出已知局部恒等式的精确边界、最小修复证书或反例分类，并与现有接口对照。仅重现局部赋值保持、模数余数类数目或旧几何八状态回归，返回 REPLAY_ONLY；不得由局部保持宣称普遍不衰减或物理纠缠。若指定观察语言无新增信息，保存准确等价类和否定结论。返回模型/语言、已证与有限检查的范围、失效见证及最小未解单元。
