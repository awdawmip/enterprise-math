<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id":"RS-ADDMUL-FORMAL-GROUP-INTERPOLATION",
  "title":"加乘桥 A3：形式群中间律与有限截断一致性",
  "kind":"RESEARCH",
  "owner":"research/addmul-formal-group-interpolation",
  "base_state":"READY",
  "priority":"P1",
  "leverage":"HIGH",
  "frontier":"Classify the exact family F_c(x,y)=x+y+cxy and its shifted multiplicative coordinate, then determine which parts of one-dimensional formal-group linearization survive as finite/integer operation-safe structure under finite truncation.",
  "next_action":"Prove the exact F_c transport and domain/inverse classification over Z and selected rings, then analyze finite power-series truncations and quantify associativity/coherence defects before comparing against the binomial and delta routes.",
  "dependencies":[],
  "source_refs":["classical: additive and multiplicative one-dimensional formal group laws","research_method_inventory.json@main","src/enterprise_math/precision.py@main"],
  "evidence_status":"DRIVER_ROADMAP_FROM_ADD_MUL_EXTERNAL_THEORY_SCOUT / FIRST_WAVE_UNEXECUTED",
  "last_progress_ref":null,"last_progress_at":null,"hard_block":null,
  "tags":["addmul","formal-group","interpolation","truncation","finite-resolution","coordinate-transport"],
  "claim_lease_minutes":240,
  "created_by_role":"RESEARCH_DRIVER",
  "task_authority":"PUBLISHED_REGISTERED",
  "publication_contract":"RESEARCH_TASK_PUBLICATION_V1",
  "publication_template":"RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key":"RS-ADDMUL-FORMAL-GROUP-INTERPOLATION",
  "parent_objective_id":"OBJ-ADDMUL-BRIDGE-STRUCTURE",
  "parent_objective_generation_id":"OG-9D6617146723B8E72C6F",
  "identity_policy":"AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy":"INHERIT_GLOBAL",
  "identity_lane":"AMFGRP",
  "origin_kind":"DRIVER_ROADMAP",
  "task_lineage":"NEW_DIRECTION",
  "parent_task_id":null,"successor_gate":null,
  "policy_review":{"policy_set":"research_taskbook_policy.json","policy_digest":"sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c","review_state":"PASS","temporary_overrides":[]}
}
-->

# 加乘桥 A3：形式群中间律与有限截断一致性

Status: `READY / P1 / FORMAL-TO-FINITE`

## Mother question

\[F_c(x,y)=x+y+cxy,\qquad 1+cF_c(x,y)=(1+cx)(1+cy).\]
`c=0` 是加法，`c=1` 经 shifted coordinate 连接乘法。这个中间律及一般一维形式群在有限分辨率下能保留什么 exact structure？

## Frozen inputs and scope

先研究 `c,x,y in Z` 或明确交换环。形式幂级数仅作外部模型；进入项目的对象必须有有限/离散语义。必须区分 monoid/group/localization；formal logarithm 的分母、系数环和纯形式语义必须显式记录。有限截断须量化高阶丢失。

## Hard target and required outputs

Hard target: `FORMAL_GROUP_ADD_MUL_INTERPOLATION_ENTERPRISE_TRANSLATION_CLASSIFIED_OR_OBSTRUCTED`

1. 证明 `F_c` 的交换、结合、单位及 `T_c(x)=1+cx` 的乘法 transport，分类像与信息保持。
2. 分类逆元 `-x/(1+cx)` 何时仍在整数/给定环，何时仅在 localization/formal neighborhood。
3. 分类参数 `c` 的真正不同结构与纯坐标重写。
4. 对一般一维形式群做有限阶 truncation，定义并计算最低阶 associativity defect。
5. 给出有限 coefficient/cell 接口及与 A1/A2 的去重结论。
6. exact symbolic checker 覆盖参数、逆元域和截断反例。

## Research value to preserve

保留“加法 + 可调交叉项 → shifted multiplication”的 exact prototype，并决定其有限版本是否比普通坐标变化多出可操作结构。

## Success, kill, and return criteria

有效终态：`FINITE_INTERPOLATING_LAW_INTERFACE_CLASSIFIED` / `POLYNOMIAL_BRIDGE_EXACT_FORMAL_EXTENSION_NOT_INTEGER_SAFE` / `COORDINATE_REWRITE_ONLY`。不得把 formal log 当连续实数本体，不得隐藏分母，不得把 monoid 误称 group。
