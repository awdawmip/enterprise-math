<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-FERMAT-RESIDUAL-PRETERMINAL-20261004",
  "title": "费马数残差：终点之前的真因子候选排除证书",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "已有聊天只给出平方余数与进位恒等式及有限样例；尚无超越终点整除等价改写的预测判据。",
  "next_action": "先独立核验分层更新，固定候选生成规则、终点前信息预算与普通模平方基线，再尝试一个可证明的候选族排除式。",
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-FERMAT-RESIDUAL-PRETERMINAL-20261004",
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

# 费马数残差：终点之前的真因子候选排除证书

## Mother question

对 F_n=2^(2^n)+1，能否在尚未完成目标模数 q 的终点平方链时，利用有来源的残差/进位结构，产生可证明正确、成本透明的真因子候选排除证书？若指定信息压缩确实不足，能否给出同保留状态、异终点观察的见证，准确界定失败范围？

## Frozen inputs and scope

从 x_0=2、x_(j+1)=x_j^2 独立建立模型，不把聊天草稿当作已证明前提。固定奇数 q>=3（允许合数）、中心代表元 r_j、整数商 A_j，令 x_j=q*A_j+r_j、r_j^2=q*c_j+r_(j+1)。明确区分 q|F_n、q^2|F_n 以及 q=F_n 的平凡闭合。底数2的该模型是外部整数算术实例，不是空间或物理公理。

冻结 n、候选 q 的生成规则、h<n 的前缀预算、允许读取的 r/c/A 信息及全部预计算成本。已知641样例只能作校准，不可进入判据或隐藏标签表。q 为素数时的阶条件、n>=2 时 q=1+k*2^(n+2) 的经典限制、普通提前到达1的排除，均作为已有基线，不冒充新结果。改变观察模数必须重新声明信息许可。用已有 BRC 仿射作用接口表示 u_(j+1)=2*r_j*u_j+c_j 的有序复合；高精度信息的取得本身计费。

## Hard target and required outputs

给出一份输入/观察/成本契约和一个明确候选族的命题。优先证明终点前证书的可靠性并给出独立验证器；若只能得到终点等价式，则分类为 ENDPOINT_REFORMULATION，不称预测。若主张特征不足，构造该特征同值而目标不同的反例或严格有限模型下界；不得将受限特征的下界扩大为所有算法的不可能性。

固定一个开发区间和至少一个在判据冻结后才读取标签的检验区间。保留生成器、精确整数输入、所有通过/拒绝/未知结果和反例，比较无筛选模平方、经典候选限制以及新方法。记录模乘次数、整数位长、候选生成、预处理、内存和验证成本；有限通过率不是普遍证明，未发现因子不是素性证书。证明必须处理合数 q 的零因子边界，或明确缩限到有素性证书的 p。

## Research value to preserve

把“残差导致失效”的直觉转化为可提前使用的结构判据，或产出阻止循环论证和成本藏匿的精确否定证书。现有加权残差与半素数平方壳任务只作方法比较；本任务的区别是费马平方链的前缀信息预算，不另造通用分解算法。

## Success, kill, and return criteria

成功须有可复核的新增排除命题/证书，或有明示模型的严格不足结论。仅重现641、把 q|F_n 改称闭合、使用未来标签、遗漏预计算成本、仅缩小数据区间以制造优势，均不能构成成功。若无新增信息或总成本无益，保存 NO_GAIN 或 REFORMULATION_ONLY 及证据，不靠扩大扫描续命。返回已证明范围、反例、成本表和最小未解问题；不把有限样本或候选数量增长外推为所有后续费马数合数。
