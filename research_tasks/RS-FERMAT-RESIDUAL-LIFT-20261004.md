<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-FERMAT-RESIDUAL-LIFT-20261004",
  "title": "费马数残差：高阶进位提升与代表元不变证书",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "聊天给出第一隐藏位 u 的仿射更新与641处 u=44；高阶进位、换代表元及可复用提升证书尚未核验。",
  "next_action": "先用精确整数重建 mod p^3 的完整更新和换代表元公式，保留二次项，再核验641及5/25对照。",
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-FERMAT-RESIDUAL-LIFT-20261004",
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

# 费马数残差：高阶进位提升与代表元不变证书

## Mother question

在已证 p|F_n 的条件下，如何把有序进位残差提升到 p^k，分离坐标依赖的进位数与代表元不变的整除/赋值信息？能否获得可复用的精确证书，而不是把经典提升结果换名？

## Frozen inputs and scope

F_n=2^(2^n)+1，x_(j+1)=x_j^2，固定奇数 q 的余数截面，x_j=q*A_j+r_j。基础恒等式 A_(j+1)=q*A_j^2+2*r_j*A_j+c_j 须独立重证。素数赋值语句另限定奇素数 p；未知模数不预设为素数。任意更换截面 r'_j=r_j+q*t_j 必须同步 A'_j=A_j-t_j，进位与所有高位状态一起转换。

优先复用 T0_BRC_AFFINE_EFFECT_TRANSPORT 的有序作用复合和既有进位/赋值工具。模 p 的第一隐藏位仿射律不是高阶全状态律；到 p^3 及更高层不得丢弃 p*A_j^2。此处残差是精确结构信息，不是舍入误差或正质量的有符号抵消。

## Hard target and required outputs

给出完整 mod p^3 更新、一般有限 k 的递推/证书格式、截面变换交换图或反例；说明最小需要保留的整数位、来源、操作与观察。证明每层读出与直接整数模 p^k 运算一致，并给出独立校验脚本、可复现输入和故意遗漏二次项/错误换截面的失败见证。

先复核 p=641、n=5 的 r_5=-1、u_5=44、p^2不整除；以 x=2 与 x=7 在模5同值但 x^2+1 分别为5和50作为高层观察对照，不把改变底数的玩具例冒充底数2费马数重因子。再冻结至少三个奇素数、k=2,3,4 的完整小域测试，另含合数 q 和非单位输入的边界测试。

对已有 p|F_n 的分支，严证费马商 Q_p(2) 与终点隐藏位的联系，核对 Hensel、提升赋值和 Wieferich 条件的原始文献；分别标识经典重述、重新证明、接口贡献和真正未解项。交付 invariant_certificate、representative_change、precision_cost 三类证据，不能将需要已知 p 的提升器称为盲因子发现器。

## Research value to preserve

得到代表元不变、精度可核验的残差提升接口，说明累积残差究竟控制初次整除还是重因子。一般仿射复合已是已有工具；新增目标限于平方链高阶非线性项及截面兼容证书，不重复发布通用进位理论。

## Success, kill, and return criteria

成功为带证明和独立校验器的提升/变换证书，或精确的最小信息不足反例。若全部还原为已有经典公式，返回 CLASSICAL_REDUCTION 和可复用接口边界，不宣称新定理。检测到遗漏项、代表元依赖伪不变量或有限验证冒充全 k 证明，保留反例并修正范围。返回最高已验证 k、符号证明覆盖、成本及下一最小缺口；不以寻找重因子作为已有结论的必要条件。
