<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-U2-NATIVE-OCCUPANCY-BRIDGE-20261007",
  "title": "U2带符号三元关联与两单位占位后继桥",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "U2已保存固定正守恒线性转向核的普遍2/3下界、来源分辨固定构型场及尾界、两两同摘要三元可区分见证与受控准备可达性；均为候选电路内证书，材料位置仍为输入。原生合法带符号三元关联、材料反作用/存储关系与占位后继未建立；原作者重放不等于独立审查。",
  "next_action": "读取固定U2证明、实现、重放和科学checkpoint，逐项建立已证条件电路结论与未证原生接口的来源表；先核对2/3量词、场尾界和受控可达性边界，再为相邻两单位列合法signed triad incidence及反作用/存储到占位后继所缺的最小关系。",
  "dependencies": [],
  "source_refs": [
    "https://github.com/awdawmip/enterprise-math/blob/fe9ce58293ac77b72092512620e8670ca9be2d78/research_notes/chatgpt_direct/20261007_cell_closure_u2_7f21d8/README.md",
    "https://github.com/awdawmip/enterprise-math/blob/fe9ce58293ac77b72092512620e8670ca9be2d78/research_notes/chatgpt_direct/20261007_cell_closure_u2_7f21d8/packet_router.py",
    "https://github.com/awdawmip/enterprise-math/blob/fe9ce58293ac77b72092512620e8670ca9be2d78/research_notes/chatgpt_direct/20261007_cell_closure_u2_7f21d8/replay.py",
    "https://github.com/awdawmip/enterprise-math/blob/ccd05f7e0e68b8c04288985c38f5f0bd15381d4e/research_notes/chatgpt_direct/20261007_cell_closure_u2_7f21d8/CHECKPOINT.json",
    "https://github.com/awdawmip/enterprise-math/blob/a2294c71268e009400e70f28dc0d4df604213c1d/research_notes/chatgpt_direct/20261006_CELL_CLOSURE_U1_PORT_BUDGET_6C4E2A.md",
    "https://github.com/awdawmip/enterprise-math/blob/ff90471f4245464de9d132114e135ca235c5a63b/research_notes/chatgpt_direct/20261006_CELL_CLOSURE_ROADMAP_4D93A7.md",
    "https://github.com/awdawmip/enterprise-math/blob/fe9ce58293ac77b72092512620e8670ca9be2d78/src/enterprise_math/brc_weighted.py"
  ],
  "evidence_status": "PINNED_PUBLIC_U2_CONDITIONAL_SOURCE_AND_CHECKPOINT; SAME_AUTHOR_REPLAY_ONLY; NATIVE_OCCUPANCY_UNSOLVED; DIRECTION_CAPTURE_ONLY_NO_NEW_SCIENTIFIC_EXECUTION",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "BRC",
    "U2",
    "NATIVE_X6",
    "SIGNED_TRIAD_INCIDENCE",
    "OCCUPANCY_SUCCESSOR",
    "JOINT_PACKET_MEMORY",
    "SOURCE_AUDIT"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-U2-NATIVE-OCCUPANCY-BRIDGE-20261007",
  "parent_objective_id": "OBJ-GEOMETRY-BRC-RESIDUAL-ACCUMULATION-SYSTEMS",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "U2-OCCUPANCY-BRIDGE",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "NEW_DIRECTION",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:d74aad6dd53d0df42d950f7b1207b27d80696f23410bd06f53a038c459577bb2",
    "review_state": "PASS",
    "temporary_overrides": []
  },
  "parent_objective_generation_id": "OG-7AE66316D7566C519AE0"
}
-->

# U2带符号三元关联与两单位占位后继桥

Status: `READY / CLAIMABLE_AFTER_IMMUTABLE_V2_PUBLICATION`

## 0. Mother question

在心跳世界的原生六维离散 Cell 空间中，以 U2 已保存的来源分辨联合响应包和固定构型场解为条件工具，能否给出**有来源的合法带符号三元关联，以及材料反作用／存储到占位的后继关系**，使相邻两单位的材料状态与场共同相容；若不能，究竟是哪一项关系欠定或不兼容？

先审清 U2 的适用量词、实现对应与受控可达性，再研究这一条新接口。固定材料位置后求场不是材料位置的解；响应预算可配成三腿也不自动给出三个原始作用。新任务捕获的是这项未决桥接问题，不把历史草案视作已审定前提。

## 1. Frozen inputs and scope

固定来源如下，可按精确提交直接恢复，不需要原对话私有状态：

| 对象 | 精确来源 | 可使用强度 |
| --- | --- | --- |
| U2 证明与适用边界 | [README.md](https://github.com/awdawmip/enterprise-math/blob/fe9ce58293ac77b72092512620e8670ca9be2d78/research_notes/chatgpt_direct/20261007_cell_closure_u2_7f21d8/README.md) | 条件电路命题，尚未正式准入 |
| 联合包与场实现 | [packet_router.py](https://github.com/awdawmip/enterprise-math/blob/fe9ce58293ac77b72092512620e8670ca9be2d78/research_notes/chatgpt_direct/20261007_cell_closure_u2_7f21d8/packet_router.py) | 待核对的原始执行对象 |
| 自包含复验入口 | [replay.py](https://github.com/awdawmip/enterprise-math/blob/fe9ce58293ac77b72092512620e8670ca9be2d78/research_notes/chatgpt_direct/20261007_cell_closure_u2_7f21d8/replay.py) | 原作者保存的 3329 项检查；不是独立审查 |
| 科学前沿 | [CHECKPOINT.json](https://github.com/awdawmip/enterprise-math/blob/ccd05f7e0e68b8c04288985c38f5f0bd15381d4e/research_notes/chatgpt_direct/20261007_cell_closure_u2_7f21d8/CHECKPOINT.json) | 明确 native_material_position_solved=false |
| U1 障碍与自适应预算 | [U1 proof](https://github.com/awdawmip/enterprise-math/blob/a2294c71268e009400e70f28dc0d4df604213c1d/research_notes/chatgpt_direct/20261006_CELL_CLOSURE_U1_PORT_BUDGET_6C4E2A.md) | 特定输入、自适应分配范围；不替代 U2 固定核 |
| 问题来源路线 | [Cell-closure roadmap](https://github.com/awdawmip/enterprise-math/blob/ff90471f4245464de9d132114e135ca235c5a63b/research_notes/chatgpt_direct/20261006_CELL_CLOSURE_ROADMAP_4D93A7.md) | 规划来源，不是正式父任务或科学准入 |
| 复用内核 | [brc_weighted.py](https://github.com/awdawmip/enterprise-math/blob/fe9ce58293ac77b72092512620e8670ca9be2d78/src/enterprise_math/brc_weighted.py) | U2 记录的内核 blob 为 3f205696709e847909958a153f8fe10d3f6b70f0 |

来源关系属于直接研究笔记到新正式方向的捕获，`parent_task_id=null`；保留 U1/U2/路线图来源，不虚构曾存在的正式父任务。方向发布本身不构成新的科学执行。

**已完成、消费而不重复计功的单元。** U2 固定正守恒线性核，在每个输入均有等量三异轴包覆盖的条件下，给出逐输入至少 `2/3` 变轴的下界及达到例。来源分辨状态 `(source, Cell, incoming)` 的固定构型场在 `rho=12*lambda<1` 下有正 BRC 路径级数与全域尾界。相邻两单位、四方、四链和三轴星的两边自身回传是固定准备的诊断结果。三元集合 `P={123,145,246,356}` 与 `Q={124,135,236,456}` 在全部有向边际、两两 CWM 和单端口阻断读出上相同，却在共同阻断 `+1,+2` 后可区分；同转向器受控提取所产生的缓冲各占预算 `1/40`，不同剩余储库各占 `39/40`，储库是披露的边界状态。来源盲的任意整包阻断／释放及正标量串联读出已有有向三元直方图的必要充分性论证。上述都保留原证明和作者归属，不宣称已独立验证。

**尚未完成的单元。** 默认 40 组三异轴组合未证明均满足 `TRIADIC_CLOSURE_E`；分数响应包不是已准入不可分原始作用。没有材料反作用／存储本构，也没有位置／占位后继。受控提取见证没有证明在相同外部边界下由两材料无外部操控地产生；新鲜无记忆核输出可由完整输入重建，不等于自动生成隐藏历史。

硬研究窗口为两个有身份的材料单位，初始占位 `c` 与 `c+E_1`，保留完整六轴空间、十二有向端口、来源／入射／包成员／目标 Cell／必要储存状态及边界条件。原生空间没有平面；限制表示必须给出 X6 嵌入或读出桥，且联合关系在允许的未来操作下保持。时间在研究占位后继、先后或存储时显式单独定型；路径深度、求解迭代和物理时间不混同。零源／单单位只作为同一接口的必要校准，不扩展为独立研究线。

数学输入先沿原证书审计：固定核 `K(q,p)`、`0<lambda<1/12`、`rho=12*lambda`、保守路径传播、按来源的注入与回传。只要新增散射或材料行为改变这些条件，就必须重新列出受影响接口，不能套用旧标量场或把旧尾界转移到未证的新系统。反作用、时间或离散占位规则只能作为有来源前提，或明确标记的新候选；无来源时保留未知。

去重边界：P07 `RS-BRC-MULTISOURCE-TRIAD-MATCHING-BUDGET-20261005` 处理旧 M2/M3/N1 的有限多源接触匹配与共享预算；P08 `RS-BRC-THRESHOLD-RELEASE-FEEDBACK-CONSTRAINT-20261005` 处理旧单材料节点反馈表族。本项固定 10 月 7 日 U2 的来源分辨场与联合包，研究**两单位材料占位与场的相容后继**，不重新发布旧匹配或表族问题，也不假定它们已有科学结果。四单位 `2x2x1`、无操控残差生成、素合判别及物理标定不属于本任务硬目标。

## 2. Hard target and required outputs

交付可以是合法桥接证书，也可以是严格欠定／不兼容证书，均必须从同一固定源前沿开始。

1. **来源和审计表。** 对 `2/3` 下界的固定／线性／正守恒／每输入覆盖量词，固定位置场的状态键、收敛／尾界，三元见证的观察范围与受控准备／储库边界，逐项列“原声明—证明依赖—实现对应—可保留强度—未决点”。有限检查与普遍证明分列。原作者运行及同作者重跑不是独立审查；声称独立审查须附真实不同审查者对决定性步骤的检查依据，不能只换身份或以原作者摘要自证。尚无独立审查时写为待审，不把源中的完成计数当成准入。
2. **最小原生接口表。** 明确有身份两材料、合法占位、入射有向端口、真实三元关联、第三作用来源、预算单位、反作用／整包存储及释放、边界回流、时间更新顺序。每个字段标注直接前提、来源定理、候选关系或 `UNKNOWN`。核中三条替代支路不直接当成三个同时作用；三条空间单轴腿也不要求在 `Z^6` 位移求和为零来冒充作用闭合。原生作用个数与材料个数保持不同类型。
3. **精确两单位问题。** 有合法接口时，写出完整联合状态、允许作用和观察集合，以及材料占位／内态／场共同满足的后继关系；位置必须是未知输出或相容关系变量，不能先固定最终位置再称为解。保留自源和交叉源反应，任何删除都需作用／观察保真证书。给一项可核验相容实例及适用域，或给不相容条件与精确反例。若只能得到多个合法后继，交付全体候选或明确覆盖域、分支选择尚缺条件，不能挑一个作为唯一物理态。
4. **欠定出口。** 若当前来源无法提供原生 signed triad incidence 或反作用／占位规则，给最小缺失字段及依赖图；若可证明存在两个符合全部已知约束却后续不同的完成，给出该对见证；若连这样的完成也无足够前提，准确保留 `UNKNOWN`，不伪造不可识别性定理。可辨别结果为：来源条件下相容、来源条件下不相容、已证非唯一、或精确前提缺失。不要把它们合并为“模型已闭合”。
5. **可接续证据。** 保存精确输入、公式、来源版本、证明／反例、实际检查及未执行项；说明既有前沿与本次新增信息各是什么。计算支持可从源目录的 `python replay.py` 进入，但不把特定软件或环境当成理论工作的准入条件；若未实际运行，明确保持待执行。科学执行沿既有带类型 BRC 操作，新增载体先证明与路径／CWM／观察的对应。不能用普通分数程序、经典三角或未证替代传播器补出科学结果。需要详版 25074 检查的原始附件而尚未取得时，仅声明该部分证据未取得；仓库自包含复验的已存范围独立列示。

只为审查发现的明确缺口或新桥接输入运行必要检查。重复已有两边回传、U1 正性、普遍 `2/3` 下界或 P/Q 见证不能充当新数学；核对它们的输出也必须标为复验。资源账分别记录支路／包类数、来源存储、整数／有理位长、场深度和尾界、检查费用。

## 3. Research value to preserve

U2 把“可配齐的正响应预算”和“真实材料占位由作用决定”之间的差距变成了可定位接口。其场解、来源标签和三元关联已经可恢复，最有价值的下一步是查清合法作用和材料后继究竟能由哪些来源条件支撑，而不是继续增加固定构型的路径深度或把普遍配齐当成素数信号。

新信息缺口是**从条件响应电路到两单位占位—场联合后继**；已有结果不关闭它，因为材料位置始终由准备给定，反作用和存储本构尚缺。可考虑停留在条件电路并独立审查，或复用 P07/P08 将来形成的合法接口；这些路线保留为有效替代。本项只有在审计确认可用强度后才尝试桥接，失败也应产出准确缺口或不兼容证书。闭合原任务的局部结论与选择四单位、无操控可达性或整数算术等下一方向分开决定。

## 4. Success, kill, and return criteria

成功：源审计明确每一声明的实际强度，且两单位窗口交付下列之一：有来源原生接口下的联合相容后继；精确不相容证书；具有完整前提的非唯一见证；或最小本构缺失／欠定接口清单及可执行下一问题。每项保留原作者、实际审查者和未核验范围，计算通过不等于定理证明或原生准入。

停止／否定：若三元合法性或反作用／占位规则没有来源，则在缺口证书处结束本任务，不凭相位、正响应、等概率、目标图案或力的负和补造本构；若桥接改变 U2 假设，则仅返回受影响接口和最小待证条件，不借旧尾界宣告全域正确；若同一外部准备／储库条件下的无操控可达性未证，保留该状态，不把受控 P/Q 见证移作证明。原始不可分作用不能由分数预算直接继承。也不把预设两体势、欧氏弹簧、平方壳或素合标签加入原生前提。

返回包应给：当前合法强度、精确源路径／提交、已完成且不再重做的单元、剩余一个最小问题、实际证据与欠项、候选／未知字段、决定性反例或证书、接续条件。若合法两单位接口已成立，另记录能否在同一规则与外部边界下研究 `2x2x1` 的理由和所需新增关口；本任务不自动执行四单位、证明自发记忆生成或建立素数规律。任务结论的终止范围为本项，不把母研究目标记作完成。
