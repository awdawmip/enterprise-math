<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-COGENTIC-OBSERVATION-COMPLETION-COST-20261126",
  "title": "允许观测目录的补全成本：熵增选择与最坏未来保真",
  "identity_lane": "COG-OBS",
  "frontier": "已有未来观察闭包/预测商接口及低阶矩失真回归；尚未解决固定允许目录和实际成本下的补全选择，以及熵增/加权分离是否保证最坏未来误差。",
  "next_action": "选定明确有限对象类、旧联合摘要、合法未来语言和允许观测目录，复用闭包或完整状态基线，建立预算—真实未来误差的同输入比较。",
  "source_refs": [
    "b00f6cef0711ccc285106b7fb00d93e8fd808662:research_notes/portable_direct/cogentic_20261125_554ed9/REPORT.md",
    "b00f6cef0711ccc285106b7fb00d93e8fd808662:research_notes/portable_direct/cogentic_20261125_554ed9/source_manifest.json",
    "b8cc35e065391066f098dc1e1de907a4bcdb0a4a:definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json",
    "b8cc35e065391066f098dc1e1de907a4bcdb0a4a:definitions/RESIDUAL_FAITHFUL_DISCRETE_RELATIONAL_SYSTEM.json",
    "b00f6cef0711ccc285106b7fb00d93e8fd808662:research_notes/portable_direct/cogentic_20261125_554ed9/agents/learning_games.md",
    "b00f6cef0711ccc285106b7fb00d93e8fd808662:research_notes/portable_direct/cogentic_20261125_554ed9/agents/algebra_checks.py",
    "b00f6cef0711ccc285106b7fb00d93e8fd808662:research_notes/portable_direct/cogentic_20261125_554ed9/agents/algebra_checks.json",
    "b8cc35e065391066f098dc1e1de907a4bcdb0a4a:research_tasks/RS-BRC-X6-OBSERVER-CLOSURE-20261003.md",
    "b8cc35e065391066f098dc1e1de907a4bcdb0a4a:research_tasks/RTASK-RF-ORDERED-PATH-RESIDUAL-20260927.md",
    "b8cc35e065391066f098dc1e1de907a4bcdb0a4a:lineage_e002_predictive_quotient.json"
  ],
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "dependencies": [],
  "evidence_status": "SOURCE_BOUND_OPEN_RESEARCH",
  "last_progress_ref": "b00f6cef0711ccc285106b7fb00d93e8fd808662:research_notes/portable_direct/cogentic_20261125_554ed9/REPORT.md",
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "COGENTIC_TRANSFER",
    "USER_FOLLOWUP_PUBLICATION"
  ],
  "claim_lease_minutes": 120,
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "INTEGRATION",
  "parent_task_id": null,
  "successor_gate": null,
  "parent_objective_generation_id": "OG-7AE66316D7566C519AE0",
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-COGENTIC-OBSERVATION-COMPLETION-COST-20261126",
  "parent_objective_id": "OBJ-GEOMETRY-BRC-RESIDUAL-ACCUMULATION-SYSTEMS",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL"
}
-->

# 允许观测目录的补全成本与最坏未来保真

## 科学问题

在已声明对象、合法未来操作和目标读出的模型中，从允许观测目录补入哪些观测、支付多少真实成本，才能达到指定最坏未来误差或精确保真？熵增、候选对分离概率或单位成本版本，何时能服务于这个目标，何时会失配？

这是 Cogentic 未登记提取包的首次正式集成，属于父目标的相对观察记忆与合法操作保持问题。增量是有目录约束和成本的选择，不是重建未来闭包本身。原生 X6 单点、其上的联合分布、以及选择时赋给候选对象的先验权重分别定型；保留操作合法性与分支来源。

## 范围与可选精确接口

声明候选对象类 \(\mathcal C\)、已有联合观察 \(W_0\)、允许新增目录 \(\mathcal H\)、未来目标集合 \(\mathcal G_{\mathcal L}\) 与实际成本 \(C(W)\)。目录各项给出实现方式、可用条件和测量/保存/更新/恢复成本；若只计观测个数，限定在该模型。区分有限时域与全部合法未来词。

对实值无噪声读出，可以用完整签名定义
\[
E_{\mathcal L}(W)=
\sup_{\substack{c,d\in\mathcal C\\
S_{W_0\cup W}(c)=S_{W_0\cup W}(d)}}
\ \sup_{g\in\mathcal G_{\mathcal L}}|g(c)-g(d)|.
\]
目标为在预算内减少 \(E_{\mathcal L}\)，或以尽量低的成本达到 \(E_{\mathcal L}\le\varepsilon\)。\(\varepsilon=0\) 仅表示声明范围的精确保真。给出单位/归一化、无残留候选对时的约定、合法未来语言是否依状态而变；合法性差异本身不能因仅比较共同可用读出而被抹去。带噪声/非实值情形另行声明误差语义。

这是研究问题的语义接口，不是已有算法或近似比结论。若采用候选权重 \(\pi\)，它与候选联合分布自身的 \(\mu\) 不同；支持、最小质量和目标幅度必须显式。

## 复用接口与独立范围

`RS-BRC-X6-OBSERVER-CLOSURE-20261003` 已承担 13 状态条件模型的回拉观测空间、最小统计和受控词闭包；`RTASK-RF-ORDERED-PATH-RESIDUAL-20260927` 已承担有序路径的端点条件矩、联合闭包和传播。这里复用其对象与真实可用结果。任务已经发布并不证明其结论已解决；若无可用闭包结果，可在明确有限对象上用完整状态/完整路径枚举作基线，不接管原任务。

E002 预测商用于真实未来可区分性的已有检查接口。自动机最小化与有限域 Moore 行列式分别有自己的类型，不能混同。本任务新增的是给定允许目录与成本之后的选择结论，不将重跑最小化作为新成果。

已保存 Vandermonde 分布对、低阶矩相同而三阶分离、AB/BA 顺序差异、模 6 消元与稀疏余核小例仅作必要回归和工具；不重新设为验收目标。Cogentic 的熵增—条件候选对分离引理及低误差不保证常数进展的反例直接复用。仅复述零权重对象得不到平均保证，不足以完成本任务。

## 可验收结果与止损

在一个与既有范围可区分、明确有意义的对象/目录上，交付预算—最坏误差边界、有效成本上下界、代理有效条件、满支持等非平凡条件下的失配证据，或针对失配的修正及其实际效果。可选择适合的一项或组合，不要求通用算法，也不预设新颖性。

比较始终固定目录、成本和未来目标，以完整状态或可靠闭包接口验证。熵/矩阵秩增加和摘要变短分别保留自身含义，不能替代未来保真。若计算承重，保存固定输入、确切算术或误差界、运行方法与真实输出；书面结论给出可检查推导。

若候选只能重现已有闭包、小例，或优势依靠免费目录外观测/遗漏恢复成本，则停止该候选并记录原因。发现已有工作已覆盖同一目录—成本—目标时，保留精确来源并回到已有任务范围，不制造重复研究。有限结果按有限范围交付。

## 不可变来源

- [research_notes/portable_direct/cogentic_20261125_554ed9/REPORT.md](https://github.com/awdawmip/enterprise-math/blob/b00f6cef0711ccc285106b7fb00d93e8fd808662/research_notes/portable_direct/cogentic_20261125_554ed9/REPORT.md)
- [research_notes/portable_direct/cogentic_20261125_554ed9/source_manifest.json](https://github.com/awdawmip/enterprise-math/blob/b00f6cef0711ccc285106b7fb00d93e8fd808662/research_notes/portable_direct/cogentic_20261125_554ed9/source_manifest.json)
- [definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json](https://github.com/awdawmip/enterprise-math/blob/b8cc35e065391066f098dc1e1de907a4bcdb0a4a/definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json)
- [definitions/RESIDUAL_FAITHFUL_DISCRETE_RELATIONAL_SYSTEM.json](https://github.com/awdawmip/enterprise-math/blob/b8cc35e065391066f098dc1e1de907a4bcdb0a4a/definitions/RESIDUAL_FAITHFUL_DISCRETE_RELATIONAL_SYSTEM.json)
- [research_notes/portable_direct/cogentic_20261125_554ed9/agents/learning_games.md](https://github.com/awdawmip/enterprise-math/blob/b00f6cef0711ccc285106b7fb00d93e8fd808662/research_notes/portable_direct/cogentic_20261125_554ed9/agents/learning_games.md)
- [research_notes/portable_direct/cogentic_20261125_554ed9/agents/algebra_checks.py](https://github.com/awdawmip/enterprise-math/blob/b00f6cef0711ccc285106b7fb00d93e8fd808662/research_notes/portable_direct/cogentic_20261125_554ed9/agents/algebra_checks.py)
- [research_notes/portable_direct/cogentic_20261125_554ed9/agents/algebra_checks.json](https://github.com/awdawmip/enterprise-math/blob/b00f6cef0711ccc285106b7fb00d93e8fd808662/research_notes/portable_direct/cogentic_20261125_554ed9/agents/algebra_checks.json)
- [research_tasks/RS-BRC-X6-OBSERVER-CLOSURE-20261003.md](https://github.com/awdawmip/enterprise-math/blob/b8cc35e065391066f098dc1e1de907a4bcdb0a4a/research_tasks/RS-BRC-X6-OBSERVER-CLOSURE-20261003.md)
- [research_tasks/RTASK-RF-ORDERED-PATH-RESIDUAL-20260927.md](https://github.com/awdawmip/enterprise-math/blob/b8cc35e065391066f098dc1e1de907a4bcdb0a4a/research_tasks/RTASK-RF-ORDERED-PATH-RESIDUAL-20260927.md)
- [lineage_e002_predictive_quotient.json](https://github.com/awdawmip/enterprise-math/blob/b8cc35e065391066f098dc1e1de907a4bcdb0a4a/lineage_e002_predictive_quotient.json)
