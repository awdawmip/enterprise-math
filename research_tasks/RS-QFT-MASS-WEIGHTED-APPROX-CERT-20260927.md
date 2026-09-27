<!-- ENTERPRISE_MATH_TASK_V1
{
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "dependencies": [],
  "source_refs": [
    "https://github.com/awdawmip/enterprise-math/blob/86022c1ee4de09a9c9055f4c6806a5d35459edfc/research_notes/directed_recovery/20260927_C6438C/qft_row_queries/README.md",
    "https://github.com/awdawmip/enterprise-math/blob/86022c1ee4de09a9c9055f4c6806a5d35459edfc/research_notes/directed_recovery/20260927_C6438C/qft_row_queries/point_queries/MASS_WEIGHTED_APPROXIMATION_BOUND.md",
    "https://github.com/awdawmip/enterprise-math/blob/86022c1ee4de09a9c9055f4c6806a5d35459edfc/definitions/RESIDUAL_FAITHFUL_DISCRETE_RELATIONAL_SYSTEM.json"
  ],
  "evidence_status": "SOURCE_BACKED_RESEARCH_CANDIDATES_UNREVIEWED_NOT_ADMITTED",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "QFT",
    "SHOR",
    "BRC",
    "APPROXIMATION",
    "ERROR_CERTIFICATE",
    "RESIDUAL_FAITHFUL"
  ],
  "claim_lease_minutes": 1440,
  "identity_lane": "QFT-APPROX",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "parent_objective_id": "PO-QFT-NATIVE-APPROX-SAMPLING-20260927",
  "historical_contribution_disclosure": [
    "RA-CAAAC604CB513AEA8BBC1DFC / EM-DIRECT-C6438C; source authorship is not independent review"
  ],
  "task_id": "RS-QFT-MASS-WEIGHTED-APPROX-CERT-20260927",
  "title": "原生 QFT 近似行查询的低成本全局误差证书",
  "frontier": "已有单-walker采样的质量加权总变差上界，但尚无把坏历史质量、好历史振幅误差与认证成本一起低成本计算的证书器。",
  "next_action": "固定一个轨迹一致的近似行查询器与公开历史分区，先在含非零反馈的小族上构造 beta_i、epsilon_i 的有向证书，并把生成与验证成本逐项计费。",
  "task_lineage": "NEW_DIRECTION",
  "parent_task_id": null,
  "successor_gate": null,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-QFT-MASS-WEIGHTED-APPROX-CERT-20260927",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:44b2174111ec85b5dd252d07f474772649a4d36936b2c99acbfa2cfba8af7a73",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# 原生 QFT 近似行查询的低成本全局误差证书

Status: published task specification; scientific result not yet produced.

## 0. Mother question

在不预先给出模乘阶或因子的前提下，怎样低成本认证一个既定、轨迹一致的完整行近似器，使只保留对最终采样有用的信息能够转化为最终输出分布的严格误差界，同时不把指数级历史或工作标签遍历藏进证书生成与验证？

## 1. Frozen inputs and scope

固定 enterprise-math@86022c1ee4de09a9c9055f4c6806a5d35459edfc 的三个 source_refs。精确行记为 v_h(w)，近似行记为 u_h(w)；两者使用同一完整原生坐标和残差载体。u 必须由公开的 (h,w) 与独立固定种子确定，不得依赖本次实际抽到的私有 latent 路径；同一查询必须一致。继续使用冻结来源中的单 walker 提议与两臂读出，不换成未经对应证明的传播器。

候选误差合同按来源使用：对深度 i 的坏历史集合 B_i，以 beta_i 上界其精确总质量；对其余历史，以 epsilon_i 上界完整未归一化振幅误差平方和。目标界为

    TV <= min(1, sum_i (beta_i + sqrt(epsilon_i))).

该式目前只是来源中的 AUTHOR_SYMBOLIC / SHARED_CONTEXT / NOT_ADMITTED 候选。任务必须重新核对其假设与适用范围，不把它当作高效证书器已经存在的证明。精确行查询到求阶的归约只说明通用精确接口很强，不是一般近似算法不可能性定理。

保留 P000、实际 BRC、整数位长、残差、操作顺序和来源。原生采样器逼近、理想 Shor 分布逼近以及最终因数恢复成功率分层表述，不相互替代。

## 2. Hard target and required outputs

给出明确的证书格式、构造或合成规则以及验证算法。对给定近似器和公开分区，输出 beta_i、epsilon_i 的精确有理值或有向上界，并证明健全性覆盖全部声明历史，而不是只覆盖本次抽中的一条轨迹。

先在含非零反馈的明确小族上，用冻结来源的完整行与 BRC 接口给出可重算对照；再至少对一个非退化参数族证明证书生成和验证成本。必须得到一个新的可判别结论：要么在某个无限受限族上严格避免完整“历史 × 工作标签”遍历并证明总资源下降，要么对冻结证书载体给出明确反例或成本障碍，并指出缺少的联合信息。

成本账必须包括近似器或分区初建、完整值及标签关联保存、证书生成、验证、整数位数、失败事件、舍入误差与每次查询成本。零历史压缩只能作诊断，不能据此声明一般高质量历史也同样可压缩。不得事后按成功样本选择证书。

## 3. Research value to preserve

把现有全局误差合同变成可付费、可复核、可被原 QFT 低精度路线调用的部件。该任务不接管原查询器实现路线，也不要求一次解决一般 Shor 去量子化；正结果和严格障碍都能缩小下一阶段真正需要保留的残差信息。

## 4. Success, kill, and return criteria

成功：完成证书健全性论证、声明范围内的精确对照和总成本界，并交付至少一个上述新的判别结论。若只能给出经验误差小、单行便宜、免费使用阶或因子、依赖私有轨迹、遗漏认证成本，均不通过。

若当前源中已经存在等价交付物，则停止重复研究并返回准确去重证据；若所提证书在冻结载体上必然要求与完整枚举同阶的工作，则把该障碍作为有效负结果返回。所有结论区分符号证明、实际执行和独立审查。
