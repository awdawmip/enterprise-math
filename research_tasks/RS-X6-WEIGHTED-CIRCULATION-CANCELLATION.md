<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-X6-WEIGHTED-CIRCULATION-CANCELLATION",
  "title": "六轴正权具名排序中一阶方差的消去条件",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "等权 X6 的逐轴净权为零判据已证，两轴正权排序的偏置与方差也已知；六轴步权相异时，哪些轴对线性组合还能消去 1/N 项尚未分类。",
  "next_action": "从已保存的具名按剩余总权选步规则出发，给一个含重复步权和一个含不同步权的算例，判别普通等权三环的方差主项。",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "NEW_DIRECTION",
  "parent_task_id": null,
  "dependencies": [],
  "source_refs": [
    "https://github.com/awdawmip/enterprise-math/blob/2565d7618b5062dbbc49174fc30f7ddae2c2483d/research_notes/public_math_intake_20261116/craig_path_restriction/weighted.md",
    "https://github.com/awdawmip/enterprise-math/blob/2565d7618b5062dbbc49174fc30f7ddae2c2483d/research_notes/public_math_intake_20261116/craig_path_restriction/x6_projection3.md",
    "https://github.com/awdawmip/enterprise-math/blob/2565d7618b5062dbbc49174fc30f7ddae2c2483d/research_notes/public_math_intake_20261116/craig_path_restriction/check_weighted.py",
    "https://github.com/awdawmip/enterprise-math/blob/2565d7618b5062dbbc49174fc30f7ddae2c2483d/research_notes/public_math_intake_20261116/craig_path_restriction/x6_limit3.md",
    "https://github.com/awdawmip/enterprise-math/blob/c4d450536bf71ed87fd74555295ec60485262f0a/experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py"
  ],
  "evidence_status": "PINNED_AUTHOR_SIDE_PROOFS_AND_REPRODUCIBLE_TESTS",
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-X6-WEIGHTED-CIRCULATION-CANCELLATION",
  "parent_objective_id": "OBJ-X6-CRAIG-PATH-REFINEMENT",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL"
}
-->

# 六轴正权具名排序中一阶方差的消去条件

六条使用中的轴各有 m_i=Nw_i 个具名最短步，每个 i 轴名字的固定权为 a_i>0。每次按剩余名字的权重比例选择下一步。令 A_ij 为 i 轴在 j 轴之前的步对比例，p_ij=a_i/(a_i+a_j)，以 H=Σ_{i<j} λ_ij(A_ij−p_ij) 定义读数。λ 反对称，且与 N 无关。a_i 描述选步偏置，w_i 描述库存比例。

问题是哪些 (a,w,λ) 使 Var(H) 的 1/N 项精确消失。要求把判据写成能对任给六轴数据计算的形式，说明剩余方差的阶数及退化为零的条件，并给出能与小尺度精确计算比对的系数或公式。考察步权全同、部分重合以及全部不同的情形，允许某类里没有非零消去量。全同的极限须与既有逐轴净权判据一致。

从不同权值的有理小库存实例核对拟出的条件，至少有一个保留或破坏普通三环抵消的具体见证。可用具名排序、概率核或其他方法，保留来源和权重语义。这里研究的是项目中已明确的有偏取样规则在六轴上的推广。

这些题目承接直接研究提交 2565d7618b5062dbbc49174fc30f7ddae2c2483d。它们在 V2 中首次作为可独立领取的问题发布；三项共享已保存的输入，各自可独立开展。既有证明与算例按原作者侧证据引用。

## 固定输入

- [weighted.md](https://github.com/awdawmip/enterprise-math/blob/2565d7618b5062dbbc49174fc30f7ddae2c2483d/research_notes/public_math_intake_20261116/craig_path_restriction/weighted.md)
- [x6_projection3.md](https://github.com/awdawmip/enterprise-math/blob/2565d7618b5062dbbc49174fc30f7ddae2c2483d/research_notes/public_math_intake_20261116/craig_path_restriction/x6_projection3.md)
- [check_weighted.py](https://github.com/awdawmip/enterprise-math/blob/2565d7618b5062dbbc49174fc30f7ddae2c2483d/research_notes/public_math_intake_20261116/craig_path_restriction/check_weighted.py)
- [x6_limit3.md](https://github.com/awdawmip/enterprise-math/blob/2565d7618b5062dbbc49174fc30f7ddae2c2483d/research_notes/public_math_intake_20261116/craig_path_restriction/x6_limit3.md)
- [signed_brc.py](https://github.com/awdawmip/enterprise-math/blob/c4d450536bf71ed87fd74555295ec60485262f0a/experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py)
