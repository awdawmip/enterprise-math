<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-COGENTIC-RIESEL-CHANNEL-SELECTION-20261126",
  "title": "Riesel 旧观测保持下的新通道选择：分离收益与实际覆盖成本",
  "identity_lane": "COG-RIESEL",
  "frontier": "CRT 旧观测保持、R4 预算18尖锐观测阶及预算9精确敏感度已有来源；尚未建立合法新增通道的分离/熵增选择准则与实际覆盖成本之间的有效关系。",
  "next_action": "在既有 R4 或另一明确 R_i 中冻结有限候选根类、旧联合观测、允许新通道目录及真实成本，比较分离代理与同一覆盖目标；先复用既有精确字典和敏感度。",
  "source_refs": [
    "b00f6cef0711ccc285106b7fb00d93e8fd808662:research_notes/portable_direct/cogentic_20261125_554ed9/REPORT.md",
    "b00f6cef0711ccc285106b7fb00d93e8fd808662:research_notes/portable_direct/cogentic_20261125_554ed9/source_manifest.json",
    "b8cc35e065391066f098dc1e1de907a4bcdb0a4a:definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json",
    "b8cc35e065391066f098dc1e1de907a4bcdb0a4a:definitions/RESIDUAL_FAITHFUL_DISCRETE_RELATIONAL_SYSTEM.json",
    "b00f6cef0711ccc285106b7fb00d93e8fd808662:research_notes/portable_direct/cogentic_20261125_554ed9/agents/factorization.md",
    "f869b78cc5143b7f73e7d59880917fe9ee024b5e:research_notes/portable_direct/riesel_r4_eighteen_sharp_20261125/REPORT.md",
    "6eecb7159d46b5ae0b1901af5eb468747091dfd4:research_notes/driver/2026-11-26_riesel_r4_budget9_exact_sensitivity.md",
    "b8cc35e065391066f098dc1e1de907a4bcdb0a4a:research_tasks/RS-RIESEL-R4-FIFTEEN-OBSERVER-20261125.md",
    "b8cc35e065391066f098dc1e1de907a4bcdb0a4a:research_tasks/RS-RIESEL-GRH-COMPATIBLE-SUPPLY-20261122.md"
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
  "registry_key": "RS-COGENTIC-RIESEL-CHANNEL-SELECTION-20261126",
  "parent_objective_id": "OBJ-GEOMETRY-BRC-RESIDUAL-ACCUMULATION-SYSTEMS",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL"
}
-->

# Riesel 旧观测保持下的新通道选择

## 研究问题

在已有算术覆盖对象中，从明确的合法新通道目录选择观测或更新通道，能否以可证明或可复算的成本改善真正的覆盖判定、覆盖构造或剩余候选分离？需要辨明分离质量、候选权重下的熵增与实际覆盖收益之间的关系。

这是 Cogentic 固定来源首次进入正式任务的有限算术接口集成，科学前驱是未登记为 Task/Result 的提取包。它在父目标的“相对观察的必要记忆、合法操作与分支来源保持”范围内提供具体算术比较核；不声称产生原生 BRC 几何或替代其他 Riesel 母题。已有正式任务列为复用及去重来源，不把它们未解决的同一范围转移到此任务。

## 固定起点与对象

复用来源中的 \(F_n(a)=a^2 2^n-1\)、实际旧字典及覆盖成本定义。声明具体 \(R_i\)、参数域、候选根类 \(\mathcal C\)、旧联合观察 \(W_0\)、允许通道目录 \(\mathcal Q\) 和目标；执行中比较策略须使用同一输入与同一目标。

已保存接口为 \(a'=a+tM\) 保持全部旧模 \(M\) 的未来序列读数；若新素数 \(q\nmid M\)，则指定合法根剩余 \(r\) 可用
\[
t\equiv(r-a)M^{-1}\pmod q
\]
实现。保留模数条件与所要求的精确赋值层级：模 \(p\) 相等本身不保持任意 \(p\)-进赋值。通道可实现性、覆盖字典条件及合法根恢复必须在具体对象中核对。

若使用分离代理，可明确采用条件候选权重下的新联合签名分离概率 \(G(q\mid W)\)，或相应熵增及单位成本版本。权重是选择模型的一部分；平均分离不能自行代替所有合法候选上的判定保真。保留相位、根分支及通道联合关系。

## 既有成果与本任务增量

固定 74 通道的 R4 预算 11–18 最大观测阶序列及预算 18 的 \(645120\) 已有作者证明和复算材料；预算 9 的最小逐坐标商、13 坐标精确重采样影响、成功根脆弱性及失败根修复分布也已有来源。后者是有限固定字典上的精确敏感度，不等于增添新通道的净收益。以上直接复用，不重新发布为待证结论。

本任务关注受约束选择：在合法新增通道或明确自适应策略中，分离/熵增准则何时改善实际覆盖目标，何时会选择没有收益或代价过高的通道。真实成本至少说明通道取得与认证、阶与根检查、字典更新、候选生成/恢复、失败尝试及共享预处理；采用简化成本时标明模型，不能据此声称端到端算法优势。

GRH 条件素数供应由已有供应任务承担；本任务可在明确已给或已认证目录上开始，不把供应定理当作新成果。预算 19 以上尖锐分类、全部支持/密度/最小根等不同前沿不因这里登记而关闭或成为必要验收门槛。

## 可验收结果与止损

交付一个有内容的选择结论：具体实例或参数族中的有效收益界、成本—分离/覆盖关系、可复算策略比较，或者真实合法目录中代理失配的明确机制/反例。给出同输入基线、所保持的观察和量词、全部承重假设以及可检查推导或实际运行证据。

仅重述 CRT 公式、重跑预算 9 静态影响、熵值上升或展示更多可分候选，不足以完成本任务。若某策略不改善目标，按其真实限定域记录障碍并结束该候选；无需为证明方法有效而改换问题。有限结论按有限范围验收，统一结论保留其证明义务。方法和工具由执行者选择。

## 不可变来源

- [research_notes/portable_direct/cogentic_20261125_554ed9/REPORT.md](https://github.com/awdawmip/enterprise-math/blob/b00f6cef0711ccc285106b7fb00d93e8fd808662/research_notes/portable_direct/cogentic_20261125_554ed9/REPORT.md)
- [research_notes/portable_direct/cogentic_20261125_554ed9/source_manifest.json](https://github.com/awdawmip/enterprise-math/blob/b00f6cef0711ccc285106b7fb00d93e8fd808662/research_notes/portable_direct/cogentic_20261125_554ed9/source_manifest.json)
- [definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json](https://github.com/awdawmip/enterprise-math/blob/b8cc35e065391066f098dc1e1de907a4bcdb0a4a/definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json)
- [definitions/RESIDUAL_FAITHFUL_DISCRETE_RELATIONAL_SYSTEM.json](https://github.com/awdawmip/enterprise-math/blob/b8cc35e065391066f098dc1e1de907a4bcdb0a4a/definitions/RESIDUAL_FAITHFUL_DISCRETE_RELATIONAL_SYSTEM.json)
- [research_notes/portable_direct/cogentic_20261125_554ed9/agents/factorization.md](https://github.com/awdawmip/enterprise-math/blob/b00f6cef0711ccc285106b7fb00d93e8fd808662/research_notes/portable_direct/cogentic_20261125_554ed9/agents/factorization.md)
- [research_notes/portable_direct/riesel_r4_eighteen_sharp_20261125/REPORT.md](https://github.com/awdawmip/enterprise-math/blob/f869b78cc5143b7f73e7d59880917fe9ee024b5e/research_notes/portable_direct/riesel_r4_eighteen_sharp_20261125/REPORT.md)
- [research_notes/driver/2026-11-26_riesel_r4_budget9_exact_sensitivity.md](https://github.com/awdawmip/enterprise-math/blob/6eecb7159d46b5ae0b1901af5eb468747091dfd4/research_notes/driver/2026-11-26_riesel_r4_budget9_exact_sensitivity.md)
- [research_tasks/RS-RIESEL-R4-FIFTEEN-OBSERVER-20261125.md](https://github.com/awdawmip/enterprise-math/blob/b8cc35e065391066f098dc1e1de907a4bcdb0a4a/research_tasks/RS-RIESEL-R4-FIFTEEN-OBSERVER-20261125.md)
- [research_tasks/RS-RIESEL-GRH-COMPATIBLE-SUPPLY-20261122.md](https://github.com/awdawmip/enterprise-math/blob/b8cc35e065391066f098dc1e1de907a4bcdb0a4a/research_tasks/RS-RIESEL-GRH-COMPATIBLE-SUPPLY-20261122.md)
