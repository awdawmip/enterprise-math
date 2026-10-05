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
  "task_id": "RS-BRC-MOD7-HOTPATH-FULL-COST-20261005",
  "title": "MOD7地址因子替换进入真实热路径的全成本比较",
  "frontier": "mod7唯一素数分轴及全域对照已完成；裸换编码未降低物理算术；不同地址不能通分后认作同一目标；P01已正式发布用于固定早期材料的版本与归属。",
  "next_action": "固定已保存传播事件与mod7本构，只替换地址更新组织，保留完整六字段、取向、类内位置与当前因子；用增量成本账比较冷构造、因子维护、DIV、定位、索引、失效、地址解码、完整输出和位长。",
  "dependencies": [
    "RS-BRC-SHOR-EVIDENCE-PROVENANCE-REPAIR-20261004"
  ],
  "source_refs": [
    "private-intake:EM-BRC-SLICE-PRIVATE-INTAKE-20261004-F9ED02",
    "private-intake-sha256:1edf20e5880df29ca865e2249be429361ba6f1e24798cfb1ba6aebf1ec3bdc6d",
    "private-intake-proposal:P11",
    "private-evidence:mod7_complex_M8/PROOF.md",
    "private-evidence:mod7_only_system/PROOF.md",
    "private-evidence:residual_numerator_R4/PROOF.md",
    "private-evidence:wave_benchmark_M5/PROOF.md",
    "https://github.com/awdawmip/enterprise-math/blob/a155bb2c856256d1df260eaa72eedb229fca1e23/research_task_records/RS-BRC-SHOR-EVIDENCE-PROVENANCE-REPAIR-20261004/TP2-D471289CD4EBEF06960B.json"
  ],
  "evidence_status": "PRIVATE_SOURCE_PACKET_VERIFIED; FORMAL_DEPENDENCIES_VERIFIED_OR_ATOMIC_BATCHED; PUBLIC_TASK_METADATA_ONLY; SCIENTIFIC_EXECUTION_NOT_PERFORMED_BY_PUBLICATION",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "BRC",
    "MOD7",
    "HOT_PATH",
    "ADDRESS_FACTOR",
    "FULL_COST",
    "CACHE_INVALIDATION",
    "BIT_LENGTH"
  ],
  "registry_key": "RS-BRC-MOD7-HOTPATH-FULL-COST-20261005",
  "identity_lane": "P11",
  "parent_task_id": "RS-BRC-SHOR-EVIDENCE-PROVENANCE-REPAIR-20261004",
  "successor_gate": {
    "new_information_gap": "已有mod7因子替换只完成接口级证明；尚未把维护、缓存、失效、索引、地址解码和完整输出纳入真实热路径，因此不能判断总成本是否实际下降。",
    "why_parent_result_does_not_close_it": "P01只修复版本、作者、输入输出和证据归属，不评估mod7地址组织进入真实执行路径后的增量费用；已完成的mod7全域对照也只说明语义一致性与裸编码成本，不覆盖缓存、失效和索引。",
    "discriminating_outcomes": [
      "在固定传播事件和本构不变的前提下，替换地址组织后每个目标Cell和完整后继与基线一致，并给出包含冷构造、因子维护、DIV、定位、索引、失效、解码、输出和位长的全成本账。",
      "若新组织总成本不降或被维护、索引、失效费用抵消，则给出可回放的无收益证书并保留原组织。"
    ],
    "kill_condition": "若收益必须依赖改变传播规则、丢弃六字段、取向或类内位置，把不同地址通分后当作同一目标，或恢复已被取代的mod13/mod256混合路线，则停止并返回否定结论。",
    "alternative_route_or_free_exploration_considered": "可以重新设计更有利的传播或换更大素数，但那会改变问题。本项只做同一传播语义下的地址组织替换，以隔离真实工程收益。",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "已完成阶段回答了mod7表示是否正确与裸算术是否减少；本项回答接口进入真实热路径后的全成本是否有净收益，交付物不同且可被明确否定。"
  }
}
-->

# MOD7地址因子替换进入真实热路径的全成本比较
Status: `READY / PUBLISHED_REGISTERED / CLAIMABLE_AFTER_IMMUTABLE_RECORD`

## Mother question
固定已保存传播事件与 mod7 本构，只替换地址更新组织，保留完整六字段、取向、类内位置与当前因子；这种因子化地址真正进入热路径后，总成本是否降低，还是只是把费用转移到维护、索引和解码？

## Frozen inputs and scope
共同项目语义服从 P000。P01 `RS-BRC-SHOR-EVIDENCE-PROVENANCE-REPAIR-20261004` 只作为早期材料版本/归属的正式前置，不把治理修复当作科学结论。
已冻结前沿：mod7 唯一素数分轴及全域对照已完成；裸换编码没有降低物理算术；不同地址不能通分后认作同一目标。不得重跑这些阶段，不恢复已被用户取代的 mod13/mod256 混合坐标路线，也不从素数大小猜动力学。
私有恢复入口为 `EM-BRC-SLICE-PRIVATE-INTAKE-20261004-F9ED02`（SHA256=`1edf20e5880df29ca865e2249be429361ba6f1e24798cfb1ba6aebf1ec3bdc6d`）；公开任务书仅保留必要元数据。

## Hard target and required outputs
固定同一组已保存传播事件与同一 mod7 本构，只替换地址更新的组织方式。必须保留六个地址字段、取向、类内位置、当前因子和目标 Cell 身份，逐事件验证完整后继与基线一致。
费用单列因子持有/构造、DIV、定位、索引、缓存命中与失效、地址解码、完整输出及位长。使用增量成本账；若执行代码或证书，保留完整输入版本和原始回执。

## Research value to preserve
已完成结果只能说明 mod7 表示可用以及裸编码没有自动减少物理算术；真实收益取决于热路径组织成本。把维护、索引、失效、解码和输出全部纳入，才能区分“表示更紧凑”和“端到端更便宜”。

## Success, kill, and return criteria
成功：每个目标 Cell 与完整后继逐项相同，错误拒绝和共同预算语义正确，并给出可回放的全成本比较。
停止/否定：若总成本无收益则明确保留无收益结论；若任何收益依赖改变传播、本构或地址身份，则不计为本任务收益。任务终止于净收益证书、无收益证书或精确未决。
