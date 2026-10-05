<!-- ENTERPRISE_MATH_TASK_V1
{
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "parent_objective_id": "OBJ-GEOMETRY-BRC-RESIDUAL-ACCUMULATION-SYSTEMS",
  "parent_objective_generation_id": "OG-7AE66316D7566C519AE0",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:d74aad6dd53d0df42d950f7b1207b27d80696f23410bd06f53a038c459577bb2",
    "review_state": "PASS",
    "temporary_overrides": []
  },
  "task_id": "RS-BRC-SPARSE-RING-PRECOMPILED-COST-QUERY-20261005",
  "title": "稀疏环执行成本的可预编译查询与真实选择价值",
  "frontier": "固定三蝶形全整数FIVE已由源码证明，c∈{-1,0,1}为253否则255；同support不等于同成本；两类三add重写严格更贵。P01已正式发布用于固定相关材料版本。",
  "next_action": "从真实原语选择一个尚未覆盖的有界参数窗口，只扩一个输入参数或一个合法同输出候选；先证明全部计数/控制相关根的完备性，再构造同任务决策区间和预编译查询费预算，判断查询能否支付自身成本。",
  "dependencies": [
    "RS-BRC-SHOR-EVIDENCE-PROVENANCE-REPAIR-20261004"
  ],
  "source_refs": [
    "private-intake:EM-BRC-SLICE-PRIVATE-INTAKE-20261004-F9ED02",
    "private-intake-sha256:1edf20e5880df29ca865e2249be429361ba6f1e24798cfb1ba6aebf1ec3bdc6d",
    "private-intake-proposal:P17",
    "private-evidence:AFFINE_OUTPUT_COORDINATES.json",
    "private-evidence:AFFINE_INTEGER_CLASS_PROOF.json",
    "private-evidence:FIXED_WINDOW_CONTEXT.json",
    "private-evidence:enumerate_one_coefficient.py",
    "private-evidence:check_finite_model_readonly.py",
    "private-evidence:shor_exact.py",
    "private-evidence:test_hierarchy.py",
    "private-evidence:FINITE_COEFFICIENT_EQUIVALENCE.json",
    "https://github.com/awdawmip/enterprise-math/blob/dd9b44fafe3e6a02c5c6c8ba825e1f130a05bfe5/research_task_records/RS-BRC-SHOR-EVIDENCE-PROVENANCE-REPAIR-20261004/TP2-D471289CD4EBEF06960B.json"
  ],
  "evidence_status": "PRIVATE_SOURCE_PACKET_VERIFIED; P01_CURRENT_PUBLICATION_VERIFIED; PRIOR_COMPLETED_UNITS_CONSUMED_WITHOUT_REPLAY; PUBLIC_TASK_METADATA_ONLY; SCIENTIFIC_EXECUTION_NOT_PERFORMED_BY_PUBLICATION",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "BRC",
    "SPARSE_RING",
    "PRECOMPILED_QUERY",
    "COST_MODEL",
    "SELECTION_VALUE",
    "INTEGER_COMPLEXITY",
    "FIVE"
  ],
  "registry_key": "RS-BRC-SPARSE-RING-PRECOMPILED-COST-QUERY-20261005",
  "identity_lane": "P17",
  "parent_task_id": "RS-BRC-SHOR-EVIDENCE-PROVENANCE-REPAIR-20261004",
  "successor_gate": {
    "new_information_gap": "已有固定窗口证明同support不等于同成本，但尚未证明预编译成本查询在真实同输出候选中能否支付自己的判断成本，也没有完整输入和中间零性跳点证书。",
    "why_parent_result_does_not_close_it": "P01只固定证据版本归属；已完成FIVE与两类三add重写只给局部成本事实，不给新参数窗口中的完整根完备性、查询成本和真实选择价值。",
    "discriminating_outcomes": [
      "在只扩一个输入参数或一个合法同输出候选的有界窗口内，证明所有计数或控制相关根完备，并给出决策区间、整数位复杂度、FIVE、时间和查询成本。",
      "若查询费覆盖收益或没有真实同输出竞争候选，则给出无选择价值证书，不虚构竞争者或复杂度下界。"
    ],
    "kill_condition": "已有五态和两个蝶形不重算；若必须把成本查询与生成完整输出直接比速度，或靠虚构候选才显示收益，则停止并返回无选择价值。",
    "alternative_route_or_free_exploration_considered": "可以扩大到更多参数和候选，但会模糊预编译查询是否本身值得。只扩一个参数或一个合法候选是最小可判别窗口。",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "已完成工作证明某些重写更贵；本项判断预编译成本查询是否能产生真实决策价值，是新的工程/算法层交付。"
  }
}
-->

# 稀疏环执行成本的可预编译查询与真实选择价值
Status: `READY / PUBLISHED_REGISTERED / CLAIMABLE_AFTER_IMMUTABLE_RECORD`

## Mother question
在已有固定稀疏环/蝶形成本事实上，只增加一个输入参数或一个合法同输出候选时，能否预编译一个成本查询，使查询自身的代价小于它带来的真实选择收益？

## Frozen inputs and scope
共同项目语义服从 P000。P01 `RS-BRC-SHOR-EVIDENCE-PROVENANCE-REPAIR-20261004` 只固定材料版本和归属。
冻结前沿：固定三蝶形全整数 FIVE 已由源码证明；`c∈{-1,0,1}` 时为 253，否则 255；同 support 不等于同成本；两类三-add 重写严格更贵。已有五态和两个蝶形不重算。
私有恢复入口为 `EM-BRC-SLICE-PRIVATE-INTAKE-20261004-F9ED02`（SHA256=`1edf20e5880df29ca865e2249be429361ba6f1e24798cfb1ba6aebf1ec3bdc6d`）。

## Hard target and required outputs
从真实原语选一个尚未覆盖的有界参数窗口，仅扩一个输入参数或一个合法同输出候选。先证明所有计数/控制相关根完备，再构造同任务决策区间和查询费预算。
必须区分根候选与总成本实际跳点，并分别记录整数位复杂度、FIVE、时间、预编译、查根、系数获取、缓存失效、写出和原始原语事件。不得把“查询一次成本”与“生成完整输出成本”直接当同一速度指标。

## Research value to preserve
预编译只有在合法同输出候选之间能以更低判断费稳定做选择才有价值。该任务把数学零点、真实原语成本和在线选择收益分开。

## Success, kill, and return criteria
成功：根完备性、成本跳点和查询预算可回放，并能证明净选择价值。
停止/否定：没有真实同输出候选，或判断费覆盖收益时，返回无选择价值；不虚构竞争者、下界或加速结论。
