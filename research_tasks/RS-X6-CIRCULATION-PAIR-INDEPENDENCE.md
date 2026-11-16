<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-X6-CIRCULATION-PAIR-INDEPENDENCE",
  "title": "X6 等权最短路径中两个循环读数的独立性",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "已知所有零行和轴对组合的边际极限、联合特征函数与协方差。尚缺可直接由两组边权判定独立性的条件，以及共享一轴时有限库存下的依赖证据。",
  "next_action": "在共享轴的三环 123/345 上比较混合矩与两边际矩的乘积，以 123/456 的分离三环为对照；由所得机制提出一般独立性判据。",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "NEW_DIRECTION",
  "parent_task_id": null,
  "dependencies": [],
  "source_refs": [
    "https://github.com/awdawmip/enterprise-math/blob/2565d7618b5062dbbc49174fc30f7ddae2c2483d/research_notes/public_math_intake_20261116/craig_path_restriction/x6_limit3.md",
    "https://github.com/awdawmip/enterprise-math/blob/2565d7618b5062dbbc49174fc30f7ddae2c2483d/research_notes/public_math_intake_20261116/craig_path_restriction/x6_projection3.md",
    "https://github.com/awdawmip/enterprise-math/blob/2565d7618b5062dbbc49174fc30f7ddae2c2483d/research_notes/public_math_intake_20261116/craig_path_restriction/check_x6_limit3.py",
    "https://github.com/awdawmip/enterprise-math/blob/c4d450536bf71ed87fd74555295ec60485262f0a/experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py"
  ],
  "evidence_status": "PINNED_AUTHOR_SIDE_PROOFS_AND_REPRODUCIBLE_TESTS",
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-X6-CIRCULATION-PAIR-INDEPENDENCE",
  "parent_objective_id": "OBJ-X6-CRAIG-PATH-REFINEMENT",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL"
}
-->

# X6 等权最短路径中两个循环读数的独立性

固定六轴等权最短步词，各轴库存为 m_i=Nw_i（w_i>0，在整库存尺度上取极限）。给两组实反对称、逐行和为零的边权 λ、κ，令 H(λ)=Σ_{i<j} λ_ij(A_ij−1/2)。问缩放后的两个读数 NH(λ)、NH(κ) 何时在极限中独立，有限库存下这种关系又如何表现。原始观察对象是同一条有名来源路径上的两个读数。

源文已确定任意线性组合的极限特征函数，且可由边权矩阵取得至多两个二维块；因此联合特征函数已有，协方差也可直接求出。此次目标是从这些材料导出可计算的独立充要条件，并找出与零协方差的差别。单写“对所有实数，联合特征函数等于乘积”不能给出所求判别。

一个有辨别力的检验是 1→2→3→1 与 3→4→5→3，两组边没有重合而来源中有一条共轴。对比使用互不相交三轴的 123/456。给出一般条件的双向证明，覆盖退化和重复强度情形；交叠及分离两例各交付一项可独立复算的判定，在具体有限 N 用精确路径计数、混合矩或等价证据检验独立性。若一般等价只在附加条件下成立，应给出反例和已证的条件范围。

这些题目承接直接研究提交 2565d7618b5062dbbc49174fc30f7ddae2c2483d。它们在 V2 中首次作为可独立领取的问题发布；三项共享已保存的输入，各自可独立开展。既有证明与算例按原作者侧证据引用。

## 固定输入

- [x6_limit3.md](https://github.com/awdawmip/enterprise-math/blob/2565d7618b5062dbbc49174fc30f7ddae2c2483d/research_notes/public_math_intake_20261116/craig_path_restriction/x6_limit3.md)
- [x6_projection3.md](https://github.com/awdawmip/enterprise-math/blob/2565d7618b5062dbbc49174fc30f7ddae2c2483d/research_notes/public_math_intake_20261116/craig_path_restriction/x6_projection3.md)
- [check_x6_limit3.py](https://github.com/awdawmip/enterprise-math/blob/2565d7618b5062dbbc49174fc30f7ddae2c2483d/research_notes/public_math_intake_20261116/craig_path_restriction/check_x6_limit3.py)
- [signed_brc.py](https://github.com/awdawmip/enterprise-math/blob/c4d450536bf71ed87fd74555295ec60485262f0a/experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py)
