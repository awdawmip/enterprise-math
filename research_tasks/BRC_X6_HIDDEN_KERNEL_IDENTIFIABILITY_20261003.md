<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-BRC-X6-HIDDEN-KERNEL-IDENTIFIABILITY-20261003",
  "title": "固定六轴路由核库的时间有序可识别性",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "已完成父研究证明同旧读出概率律可有不同隐藏统计；固定有限轴Markov核库的同刻/有序可识别等价类和最小分离集合尚未求出。",
  "next_action": "冻结5核库、固定轴编号和n=1..4的同刻观察，构造lag1/2有序平方增量特征表，先判等价与碰撞，再求该库内最小分离集合。",
  "dependencies": [],
  "source_refs": [
    "https://github.com/awdawmip/enterprise-math/blob/b61af8438886a3c1eb8ff53297447837bd2ee507/experiments/brc_hidden_residual_20261003_fca717/REPORT.md",
    "https://github.com/awdawmip/enterprise-math/blob/b61af8438886a3c1eb8ff53297447837bd2ee507/experiments/brc_hidden_residual_20261003_fca717/summary.json",
    "https://github.com/awdawmip/enterprise-math/blob/b61af8438886a3c1eb8ff53297447837bd2ee507/experiments/brc_hidden_residual_20261003_fca717/CROSS_REVIEW.md",
    "https://github.com/awdawmip/enterprise-math/blob/b61af8438886a3c1eb8ff53297447837bd2ee507/experiments/brc_hidden_residual_20261003_fca717/ROOT_REVIEW.md",
    "https://github.com/awdawmip/enterprise-math/blob/2c56c3618dcbe2d65ad4c34bf1839d350759ac90/research_task_records/RS-BRC-BASELINE-RESIDUAL-20261002/TP2-20E37C57649A74D4E563.json",
    "https://github.com/awdawmip/enterprise-math/blob/2c56c3618dcbe2d65ad4c34bf1839d350759ac90/research_tasks/BRC_BASELINE_RESIDUAL_HIDDEN_RESIDUAL_20261003.md",
    "https://github.com/awdawmip/enterprise-math/blob/2c56c3618dcbe2d65ad4c34bf1839d350759ac90/research_objective_records/OBJ-GEOMETRY-BRC-RESIDUAL-ACCUMULATION-SYSTEMS/OG-7AE66316D7566C519AE0.json",
    "https://github.com/awdawmip/enterprise-math/blob/2c56c3618dcbe2d65ad4c34bf1839d350759ac90/research_objective_heads/OBJ-GEOMETRY-BRC-RESIDUAL-ACCUMULATION-SYSTEMS.json",
    "https://github.com/awdawmip/enterprise-math/blob/2c56c3618dcbe2d65ad4c34bf1839d350759ac90/research_objective_head_events/OBJ-GEOMETRY-BRC-RESIDUAL-ACCUMULATION-SYSTEMS/OG-7AE66316D7566C519AE0.json",
    "https://github.com/awdawmip/enterprise-math/blob/2c56c3618dcbe2d65ad4c34bf1839d350759ac90/p000_reality_foundation.json",
    "https://github.com/awdawmip/enterprise-math/blob/2c56c3618dcbe2d65ad4c34bf1839d350759ac90/definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json",
    "https://github.com/awdawmip/enterprise-math/blob/2c56c3618dcbe2d65ad4c34bf1839d350759ac90/definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json"
  ],
  "evidence_status": "SOURCE_BACKED_CONTINUATION_NOT_EXECUTED",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "BRC",
    "X6",
    "CONTINUATION",
    "direct-user-publication",
    "bounded-scope"
  ],
  "claim_lease_minutes": 120,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-BRC-X6-HIDDEN-KERNEL-IDENTIFIABILITY-20261003",
  "parent_objective_id": "OBJ-GEOMETRY-BRC-RESIDUAL-ACCUMULATION-SYSTEMS",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "BRC",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-BRC-BASELINE-RESIDUAL-20261002",
  "successor_gate": {
    "new_information_gap": "同刻隐藏矩与旧读出仍不足以说明固定轴核的时间方向是否可辨；五核库内的有序最小分离集合未知。",
    "why_parent_result_does_not_close_it": "父研究考察符号相关、iid轴路由及隐藏统计；没有求本五核轴Markov链的同刻等价类与lag1/2最小分离证书。",
    "discriminating_outcomes": [
      "同刻端点律/矩已分离某核对，产生可核验反例。",
      "同刻方向等价但有序观察分离，给出最小特征和删除碰撞证书。",
      "声明观察仍不能分离，返回具体不可识别类。"
    ],
    "kill_condition": "固定观察无法分离时保留精确碰撞，不扩大核库/时间/lag逃避；未证明的有限数值相等不写成全时定理。",
    "alternative_route_or_free_exploration_considered": "已考虑关闭于父研究、追加一般最小记忆任务或自由扩库；均不能替代此次固定五核的有限可识别问题，通用最小压缩已由GBRC-R1覆盖而排除。",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "用户明确要求发布后续任务；该有限核库与独立输出可由新执行者接手，避免重开已完成baseline或混入通用路径组合任务。"
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:d74aad6dd53d0df42d950f7b1207b27d80696f23410bd06f53a038c459577bb2",
    "review_state": "PASS",
    "temporary_overrides": []
  },
  "parent_objective_generation_id": "OG-7AE66316D7566C519AE0"
}
-->

# 固定六轴路由核库的时间有序可识别性

Status: `V2 PUBLICATION / READY UPON IMMUTABLE RECORD / NOT EXECUTED`

## 0. Mother question

固定五个轴 Markov 核的同刻观察能否辨认循环方向？lag 1/2 有序观察能否区分，并给出仅此库内的最小分离集合？

## 1. Frozen inputs and scope

P000 固定完整六维立体 X6，无原生平面；三维为晶包层，任意三轴不自动定义完整层。n 显式演化、时间另型；原生步为整数 ±E_i，正支路质量与读出/净流/响应分型。输入为 b61af843… 的 REPORT/summary/CROSS_REVIEW 及所引精确证据（完整链接见元数据）。数学父为 baseline 第8代 TP2-20E37C57649A74D4E563；已完成输入不作未完成依赖。新任务仅组织绑定 OPEN GBRC Objective/OG-7AE66316D7566C519AE0，不改旧 baseline，不冒充 GBRC-R1 后继或 Driver 接受。接手者读取固定来源并取得合法执行绑定后开展本任务；发布本身不授予数学接受。

ΔX_t=ε_t e_{I_t}，ε iid 对称且独立于完整轴链；I_0 平稳均匀。Q=(1−η)J/6+ηC，C 为六轴正向/反向循环，η∈{0,1/2,1}，η=0 去重，共五核。轴编号固定；若讨论重标记等价，另列允许的重标记与观察，不能静默商掉方向。

旧标量 S=ΣXi 全部路径律相同。同刻观察固定为 n=1..4 的完整端点律、H5=(I−J/6)X 二/四/六阶及父研究既有混合量；H5 是有理读出，不是 Cell。有序候选固定为 E[(ΔX_{t,i})²(ΔX_{t+ℓ,j})²]，ℓ=1,2。只在该特征库按“最大lag、特征数”排序求最小性。排除 GBRC-R1 通用最小记忆/压缩和 RTASK-RF-ORDERED-PATH-RESIDUAL 仿射组合。

## 2. Hard target and required outputs

交付五核观察精确表、等价类、同刻不能辨认方向的证明或反例；交付有序分离集合、排序最小性证明，以及删掉每个所选特征后出现的具体核对碰撞证书。附路径/矩阵或等价精确代码、结果、来源与审查所需材料，区分有限核验与范围外命题。

## 3. Research value to preserve

父研究没有处理这五个轴链的时间方向与最小分离证书；此有限问题能独立接续，避免把同刻相同当作未来相同，也不重做泛压缩。

## 4. Success, kill, and return criteria

固定五核及观察完成即返回。若特征不能分离，保留具体不可识别类，不扩大核库、n或lag制造成功；若同刻已分开，返回反例而不维护预设结论。有限点相同不能写成全时定理，重标记必须显式。成果不自动授予 Driver 接受、N0、Working Truth 或新研究范围。
