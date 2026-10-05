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
  "task_id": "RS-BRC-ANISOTROPIC-ENVIRONMENT-GRAM-20261005",
  "title": "各向异性私有记录与环境回流的路径Gram证书",
  "frontier": "局部散射、对齐输运、相干/经典路径和部分Gram压缩已验；两种v08原件独立保留；P01已正式发布用于固定早期材料版本与归属。",
  "next_action": "只选两段固定路径加一次环境再访问，推导完整联合Gram与回流项；比较保留二维代码矩阵与扩展当前环境载体的充分性，并给合法通道近似误差、罕见出口边界和来源守恒证书。",
  "dependencies": [
    "RS-BRC-SHOR-EVIDENCE-PROVENANCE-REPAIR-20261004"
  ],
  "source_refs": [
    "private-intake:EM-BRC-SLICE-PRIVATE-INTAKE-20261004-F9ED02",
    "private-intake-sha256:1edf20e5880df29ca865e2249be429361ba6f1e24798cfb1ba6aebf1ec3bdc6d",
    "private-intake-proposal:P14",
    "private-evidence:brc_cell_scattering_v05/PROOF.md",
    "private-evidence:brc_cell_transport_v06/PROOF.md",
    "private-evidence:brc_path_recombination_v07/PROOF.md",
    "private-evidence:brc_noncommuting_closure_v08/PROOF.md",
    "private-evidence:brc_coupled_observer_v09/PROOF.md",
    "https://github.com/awdawmip/enterprise-math/blob/a155bb2c856256d1df260eaa72eedb229fca1e23/research_task_records/RS-BRC-SHOR-EVIDENCE-PROVENANCE-REPAIR-20261004/TP2-D471289CD4EBEF06960B.json"
  ],
  "evidence_status": "PRIVATE_SOURCE_PACKET_VERIFIED; FORMAL_DEPENDENCIES_VERIFIED_OR_ATOMIC_BATCHED; PUBLIC_TASK_METADATA_ONLY; SCIENTIFIC_EXECUTION_NOT_PERFORMED_BY_PUBLICATION",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "BRC",
    "ANISOTROPY",
    "ENVIRONMENT_MEMORY",
    "GRAM",
    "PATH_RECOMBINATION",
    "BACKFLOW",
    "RARE_EXIT"
  ],
  "registry_key": "RS-BRC-ANISOTROPIC-ENVIRONMENT-GRAM-20261005",
  "identity_lane": "P14",
  "parent_task_id": "RS-BRC-SHOR-EVIDENCE-PROVENANCE-REPAIR-20261004",
  "successor_gate": {
    "new_information_gap": "当法线或保护方向缓变、存在微弱各向异性私有记录且环境会返回时，旧标量衰减或直接迹掉环境的商可能失效；此前只验证局部散射、输运和部分Gram压缩。",
    "why_parent_result_does_not_close_it": "P01只修复证据版本归属；既有v05-v09结果也没有覆盖一次真实环境再访问所产生的回拉Gram和记忆项。",
    "discriminating_outcomes": [
      "对两段固定路径和一次环境再访问，推导全部出口、交叉块和来源守恒的联合Gram或回流证书，并证明二维代码矩阵足够或给出需要扩展环境载体的最小维度。",
      "若无记忆商失效，则给最小严格反例与近似误差或罕见出口边界，区分保护项和耗散项。"
    ],
    "kill_condition": "若必须保留额外环境载体，则精确报告而非强行迹掉；不得因损耗小删除保护项，也不得把该有界证书宣称为物理纠缠机理。",
    "alternative_route_or_free_exploration_considered": "可以继续用标量衰减或直接忽略返回环境，但那正是待检验假设；也可建立庞大通用环境模型，但会掩盖最小记忆维度。两路径一次返回是最小判别域。",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "早期结果覆盖局部散射、输运和部分Gram压缩；本项新增环境回流和各向异性私有记录，是不同的记忆闭合问题。"
  }
}
-->

# 各向异性私有记录与环境回流的路径Gram证书
Status: `READY / PUBLISHED_REGISTERED / CLAIMABLE_AFTER_IMMUTABLE_RECORD`

## Mother question
当两条固定路径留下微弱各向异性私有记录，且环境随后再次返回作用于系统时，旧的标量衰减或“先迹掉环境”的压缩是否仍未来充分；二维代码矩阵够不够，还是必须显式扩展环境载体？

## Frozen inputs and scope
共同项目语义服从 P000。P01 `RS-BRC-SHOR-EVIDENCE-PROVENANCE-REPAIR-20261004` 只固定材料版本和归属。
已冻结前沿：局部散射、对齐输运、相干或经典路径和部分 Gram 压缩已验证；两种 v08 原件继续独立保留。不得把同一来源的相干路径与未知经典路径混同，也不得把旧无记忆公式直接外推到环境再访问。
私有恢复入口为 `EM-BRC-SLICE-PRIVATE-INTAKE-20261004-F9ED02`（SHA256=`1edf20e5880df29ca865e2249be429361ba6f1e24798cfb1ba6aebf1ec3bdc6d`）。

## Hard target and required outputs
只选两段固定路径和一次环境再访问。推导完整联合 Gram、回拉或回流项、全部出口与交叉块，逐来源保持守恒。比较保留二维代码矩阵与扩展当前环境载体，证明哪一种对未来输出充分。
必须给合法通道近似误差、罕见出口边界以及保护或耗散分型。若需要额外环境维度，报告最小必要载体；若执行代码或证书，单列环境记录获取、回拉 Gram、构建、位长、输出和因子截断认证成本。

## Research value to preserve
环境返回会把先前看似可丢弃的私有记录重新带回可观察路径。精确联合 Gram 证书能判定哪些残差真正可压缩，哪些必须作为记忆保留。

## Success, kill, and return criteria
成功：所有出口、交叉块和来源守恒可回放；保护与耗散分型明确；环境再访问后的充分状态与误差界清楚。
停止/否定：若必须保留额外环境载体则如实返回；不以小损耗删除保护项，不把有界代数结果称为物理纠缠机理已经证明。
