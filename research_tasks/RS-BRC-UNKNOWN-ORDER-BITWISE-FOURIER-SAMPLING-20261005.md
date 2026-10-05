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
  "task_id": "RS-BRC-UNKNOWN-ORDER-BITWISE-FOURIER-SAMPLING-20261005",
  "title": "未知阶的按位傅里叶条件采样与有用因数事件",
  "frontier": "v03低位字符恒等式及2^40局部查询已验；它不是完整40位采样。S1是有限完整参考，不提供通用加速；P01已正式发布用于固定相关早期证据版本。",
  "next_action": "不输入未知阶r，固定一个有界条件位查询或采样单元；先证明条件归一化和保真，给代数区间与安全回退，再构造不逐个扫描全部奇返回距离的可验证块摘要或阈值早停，并检验有用周期或因数事件及总成本。",
  "dependencies": [
    "RS-BRC-SHOR-EVIDENCE-PROVENANCE-REPAIR-20261004"
  ],
  "source_refs": [
    "private-intake:EM-BRC-SLICE-PRIVATE-INTAKE-20261004-F9ED02",
    "private-intake-sha256:1edf20e5880df29ca865e2249be429361ba6f1e24798cfb1ba6aebf1ec3bdc6d",
    "private-intake-proposal:P12",
    "private-evidence:brc_fourier_residual_v03/PROOF.md",
    "private-evidence:shor_algebraic_brc_v02/PROOF.md",
    "private-evidence:shor_mod7_benchmark/PROOF.md",
    "https://github.com/awdawmip/enterprise-math/blob/a155bb2c856256d1df260eaa72eedb229fca1e23/research_task_records/RS-BRC-SHOR-EVIDENCE-PROVENANCE-REPAIR-20261004/TP2-D471289CD4EBEF06960B.json"
  ],
  "evidence_status": "PRIVATE_SOURCE_PACKET_VERIFIED; FORMAL_DEPENDENCIES_VERIFIED_OR_ATOMIC_BATCHED; PUBLIC_TASK_METADATA_ONLY; SCIENTIFIC_EXECUTION_NOT_PERFORMED_BY_PUBLICATION",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "BRC",
    "SHOR",
    "FOURIER",
    "UNKNOWN_ORDER",
    "BITWISE_CONDITIONAL_SAMPLING",
    "FACTOR_EVENT",
    "ALGEBRAIC_INTERVAL"
  ],
  "registry_key": "RS-BRC-UNKNOWN-ORDER-BITWISE-FOURIER-SAMPLING-20261005",
  "identity_lane": "P12",
  "parent_task_id": "RS-BRC-SHOR-EVIDENCE-PROVENANCE-REPAIR-20261004",
  "successor_gate": {
    "new_information_gap": "现有v03只证明低位字符恒等式和2^40局部查询；不能逐项扫描全部奇返回距离时，如何做可验证块摘要、随机阈值早停，以及稀有前缀的误差和失败概率仍缺。",
    "why_parent_result_does_not_close_it": "P01只修复证据版本归属；已完成v03和S1也不提供未知阶r下的完整联合采样器或有用因数事件成功率与成本证明。",
    "discriminating_outcomes": [
      "在不输入r的有界单元中给出来源明确的工作纤维、条件归一化、代数区间、安全回退和可验证联合观察，并测量有用周期或因数事件的成功率与总成本。",
      "若发现返回关系或前缀认证仍要求指数扫描或更高总成本，则给出明确失败界，不把局部短公式提升为通用加速。"
    ],
    "kill_condition": "若只能通过输入未知r、把少量比特当完整Shor输出，或省略稀有前缀和回退概率才能成立，则停止并返回否定或有界未决。",
    "alternative_route_or_free_exploration_considered": "可以直接做完整大位宽分布或逐个扫描所有返回距离，但前者成本过高，后者正是待避免路线；本项选择最小可验证条件位单元测试是否存在真实算法收益。",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "已完成阶段只给局部字符查询；本项专门检验未知阶条件采样和有用因数事件，需独立成功率、失败概率与成本证书。"
  }
}
-->

# 未知阶的按位傅里叶条件采样与有用因数事件
Status: `READY / PUBLISHED_REGISTERED / CLAIMABLE_AFTER_IMMUTABLE_RECORD`

## Mother question
不输入未知阶 `r`，能否构造一个有界条件位查询或采样单元：先证明保真与条件归一化，再用代数区间和安全回退处理稀有前缀，并最终产生可验证的有用周期或因数事件，而不是只得到几个局部比特？

## Frozen inputs and scope
共同项目语义服从 P000。P01 `RS-BRC-SHOR-EVIDENCE-PROVENANCE-REPAIR-20261004` 只固定证据版本和归属。
已冻结前沿：v03 的低位字符恒等式和 `2^40` 局部查询已经验证，但不是完整 40 位采样；S1 只是有限完整参考，不提供通用加速。不得把已完成结果重新包装成新任务产出。
私有恢复入口为 `EM-BRC-SLICE-PRIVATE-INTAKE-20261004-F9ED02`（SHA256=`1edf20e5880df29ca865e2249be429361ba6f1e24798cfb1ba6aebf1ec3bdc6d`）。

## Hard target and required outputs
在不知道 `r` 的条件下固定一个有界查询或采样单元，明确工作纤维来源、条件概率归一化、输出位语义和完整联合观察。构造不逐个扫描全部奇返回距离的可验证块摘要或阈值早停，并给稀有前缀的代数区间、失败概率和安全回退。
随后检验输出是否真正提高有用周期或因数事件概率，并把冷输入/模板、模乘、代数根比较、位长、稀有前缀处理、验证和成功率折算全部计入总成本。

## Research value to preserve
局部 Fourier/BRC 字符查询只有在不知道阶时仍能组合成保真的条件采样并最终提升有用因数事件，才具有算法意义。该任务把“简短局部式子”与“完整可验证采样或复杂度收益”严格分开。

## Success, kill, and return criteria
成功：工作纤维、条件归一化、失败或回退概率和联合观察全部可验证；有用周期或因数事件及端到端成本有明确证书。
停止/否定：若关系发现仍为指数级或总成本更高则如实报告；不得把少数比特当完整 Shor 输出，也不得由短公式声称复杂度加速。
