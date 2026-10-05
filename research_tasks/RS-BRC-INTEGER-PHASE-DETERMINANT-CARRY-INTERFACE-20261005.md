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
  "task_id": "RS-BRC-INTEGER-PHASE-DETERMINANT-CARRY-INTERFACE-20261005",
  "title": "整数相位、行列式误差与赋值进位的类型化BRC接口",
  "frontier": "G(a,b)=(2a-b,a+2b)、Pi有理读出、误差平方4(ad-bc)^2/((a²+b²)(c²+d²))及高斯赋值进位为对话符号结果，尚未实际BRC接入；P19已正式发布集合更新/近似合并与半开边界任务，P01固定早期证据版本与归属。",
  "next_action": "复用既有实际BRC载体，仅实现非零整数对、精确Pi读出、行列式证书和一个有理误差比较；显式区分正质量、signed/complex观察量、幅值、来源和相位合同，并把半开胞界进位与有限字长近似裁减接入同一类型化接口。",
  "dependencies": [
    "RS-BRC-SHOR-EVIDENCE-PROVENANCE-REPAIR-20261004",
    "RS-BRC-RATIONAL-CELL-SET-MERGE-CERTIFICATE-20261005"
  ],
  "source_refs": [
    "private-intake:EM-BRC-SLICE-PRIVATE-INTAKE-20261004-F9ED02",
    "private-intake-sha256:1edf20e5880df29ca865e2249be429361ba6f1e24798cfb1ba6aebf1ec3bdc6d",
    "private-intake-proposal:P21",
    "private-evidence:CONVERSATION_FRONTIER.md",
    "private-evidence:brc_phase_kernel/PROOF.md",
    "private-evidence:EM_S15SUPPORT_RATIONAL_CELL_CERTIFICATE_20261001.json",
    "https://github.com/awdawmip/enterprise-math/blob/00a66a7e5d4c9aab07769e2dd9043b2fc449a6d0/research_task_records/RS-BRC-SHOR-EVIDENCE-PROVENANCE-REPAIR-20261004/TP2-D471289CD4EBEF06960B.json",
    "https://github.com/awdawmip/enterprise-math/blob/00a66a7e5d4c9aab07769e2dd9043b2fc449a6d0/research_task_records/RS-BRC-RATIONAL-CELL-SET-MERGE-CERTIFICATE-20261005/TP2-36D8698E134A633B1D38.json"
  ],
  "evidence_status": "PRIVATE_SOURCE_PACKET_VERIFIED; P01_P19_CURRENT_PUBLICATIONS_VERIFIED; SYMBOLIC_PHASE_AND_CARRY_RESULTS_CONSUMED_AT_DECLARED_STRENGTH; PUBLIC_TASK_METADATA_ONLY; SCIENTIFIC_EXECUTION_NOT_PERFORMED_BY_PUBLICATION",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "BRC",
    "INTEGER_PHASE",
    "DETERMINANT_ERROR",
    "VALUATION_CARRY",
    "TYPED_INTERFACE",
    "PROJECTIVE_QUOTIENT",
    "HALF_OPEN_CELL",
    "PROVENANCE"
  ],
  "registry_key": "RS-BRC-INTEGER-PHASE-DETERMINANT-CARRY-INTERFACE-20261005",
  "identity_lane": "P21",
  "parent_task_id": "RS-BRC-RATIONAL-CELL-SET-MERGE-CERTIFICATE-20261005",
  "successor_gate": {
    "new_information_gap": "现有G(a,b)、精确Pi读出、行列式误差公式和高斯赋值进位只停留在符号层；尚未形成一个在实际BRC载体上同时保持方向、整数来源、全局尺度、有限字长近似裁减和半开胞界进位的类型化运行合同。",
    "why_parent_result_does_not_close_it": "P19处理有理晶胞集合更新、近似合并和半开边界的一致性，但不定义非零整数相位对、精确Pi读出、行列式误差与赋值进位如何作为BRC类型接口组合；P01也只负责证据版本和归属。",
    "discriminating_outcomes": [
      "在复用既有实际BRC载体的前提下，实现非零整数对、G更新、精确Pi读出、行列式误差证书和一个有理误差比较，并给出零/单位/有向负系数、半开进位、来源、幅值与相位观察合同的类型检查及真实调用账。",
      "若共同尺度商会抹掉幅值或来源，或有限字长裁减/进位不能在声明合同下安全组合，则给出最小类型错误或反例；只有输入合同明确为纯相位时才允许射影商。"
    ],
    "kill_condition": "若缺少与既有BRC载体匹配的类型接口，则先给精确扩展义务；不得绕行普通数值传播，不得把signed/complex系数解释为正质量，不得把有限变量数冒充有限比特状态，也不得声称原生六轴映射已完成。",
    "alternative_route_or_free_exploration_considered": "可以直接用浮点复数、统一除以gcd或把相位对当普通坐标传播，但会丢失精确误差、幅值或来源。复用现有BRC并显式类型化是保留整数/赋值/来源残差的最小路线。",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "P19解决集合与半开边界证书，本项进一步把相位整数对、行列式误差和赋值进位接入实际BRC接口；交付物是类型合同、真实调用账和可组合证书，而非重复P19集合证明。"
  }
}
-->

# 整数相位、行列式误差与赋值进位的类型化BRC接口

Status: `READY / PUBLISHED_REGISTERED / CLAIMABLE_AFTER_IMMUTABLE_RECORD`

## Mother question

复用既有实际 BRC 载体，仅实现非零整数对、精确 `Pi` 读出、行列式证书和一个有理误差比较时，怎样建立一个不会抹掉方向、整数来源、幅值和全局尺度的类型化接口；有限字长裁减与半开胞界进位又应怎样进入同一合同？

## Frozen inputs and scope

共同项目语义服从 P000。整数对、相位对和有理误差表达首先是代数/观察接口，**不是原生 X6 空间坐标，也不自动构成完整三维切片**；任何原生转移仍需另行声明切片选择、第三坐标语义、读出及关系保持。

P01 `RS-BRC-SHOR-EVIDENCE-PROVENANCE-REPAIR-20261004` 只作为早期材料版本/归属的正式前置。P19 `RS-BRC-RATIONAL-CELL-SET-MERGE-CERTIFICATE-20261005` 已正式发布，用于提供有理晶胞集合、半开边界和近似合并的任务边界；本任务只消费其已正式允许的强度，不预设尚未执行出的科学结论。

已冻结的符号前沿为：
- `G(a,b)=(2a-b,a+2b)`；
- 精确 `Pi` 有理读出；
- 误差平方 `4(ad-bc)^2 / ((a²+b²)(c²+d²))`；
- 高斯赋值进位与半开胞界的既有符号推导。

这些结果尚未实际接入 BRC，因此本任务不得把符号恒等式当成已经完成的运行接口。私有恢复入口为 `EM-BRC-SLICE-PRIVATE-INTAKE-20261004-F9ED02`（SHA256=`1edf20e5880df29ca865e2249be429361ba6f1e24798cfb1ba6aebf1ec3bdc6d`）；公开任务书仅保留必要元数据。

## Hard target and required outputs

复用既有实际 BRC 载体，不另造普通数值传播器。只实现：
- 非零整数对及其零/单位/有向负系数类型；
- `G(a,b)` 的精确更新；
- 精确 `Pi` 读出；
- 基于 `ad-bc` 的行列式误差证书；
- 一个有理误差比较；
- 与 P19 半开边界一致的赋值进位和有限字长近似裁减。

必须显式区分正质量、signed/complex 观察量、幅值、来源和相位。共同尺度不得在一般输入上被无条件商掉；只有输入合同明确“只关心相位且幅值/来源另有保持”时才许可射影商，并需证明读出不依赖被商掉的尺度。

应交付符号恒等式核对、类型表、半开进位规则、不同观察合同、至少一个保持幅值/来源的正例和一个错误射影商反例。若实际执行代码或证书，记录 BRC 乘加/DIV、bit 增长、gcd/规范化、缓存、读出、来源账和原始回执；未执行项单列。

## Research value to preserve

整数相位接口的价值不在于把连续相位粗暴压成少量变量，而在于同时保留方向、整数/赋值结构、来源、尺度和精确误差证书。把 P19 的半开晶胞边界与行列式误差接到实际 BRC 类型系统，可以明确何时允许安全规范化、何时必须保留幅值或来源残差。

## Success, kill, and return criteria

成功：符号恒等式、零/单位/有向负系数类型、真实 BRC 调用账、半开进位以及不同观察合同均明确；射影商的适用条件有证明，有限个变量不被冒充为有限比特状态。

停止/否定：若缺少与现有 BRC 匹配的类型接口，先返回精确扩展义务；不得绕行普通数值传播，不得用 gcd/共同尺度消掉幅值或来源，不得把 signed/complex 系数当正质量，也不得声称原生六轴映射已经完成。任务终止于可组合类型接口、最小反例或明确安全未决。
