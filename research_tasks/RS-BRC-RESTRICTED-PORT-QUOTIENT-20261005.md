<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-BRC-RESTRICTED-PORT-QUOTIENT-20261005",
  "title": "受限操作语言下的安全端口商与最小可观察状态",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "任意有限切换线性集下的公共不变核、至多m-rankP深度稳定和五Cell N2=0已推导；P03/P04已正式发布相邻联合关系与循环/入口状态任务，但状态依赖合法词下的全局安全端口商尚未执行。",
  "next_action": "固定一个有有限控制状态的合法词语言，构造控制状态×差异空间下降；线性条件失效时改用完整有界状态关系，输出全局q、拒绝词、终止证明与含来源/配对读出的最短反例。",
  "dependencies": [
    "RS-BRC-SOURCE-EXIT-PAIRING-20261004",
    "RS-BRC-CYCLE-FLUX-ENTRY-STATE-20261004"
  ],
  "source_refs": [
    "private-intake:EM-BRC-SLICE-PRIVATE-INTAKE-20261004-F9ED02",
    "private-intake-sha256:1edf20e5880df29ca865e2249be429361ba6f1e24798cfb1ba6aebf1ec3bdc6d",
    "private-intake-proposal:P06",
    "private-evidence:CONVERSATION_FRONTIER.md",
    "https://github.com/awdawmip/enterprise-math/blob/06754542f6e552c705958dee9987096066414a84/research_task_records/RS-BRC-SOURCE-EXIT-PAIRING-20261004/TP2-DCA5A080B5E0D5135648.json",
    "https://github.com/awdawmip/enterprise-math/blob/06754542f6e552c705958dee9987096066414a84/research_task_records/RS-BRC-CYCLE-FLUX-ENTRY-STATE-20261004/TP2-B5596854AA32D5099A95.json"
  ],
  "evidence_status": "PRIVATE_SOURCE_PACKET_VERIFIED; FORMAL_DEPENDENCIES_VERIFIED_OR_ATOMIC_BATCHED; PUBLIC_TASK_METADATA_ONLY; SCIENTIFIC_EXECUTION_NOT_PERFORMED_BY_PUBLICATION",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "BRC",
    "RESTRICTED_OPERATOR_LANGUAGE",
    "PORT_QUOTIENT",
    "MINIMAL_OBSERVABLE_STATE",
    "FINITE_CONTROL",
    "SAFE_COMPRESSION"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-BRC-RESTRICTED-PORT-QUOTIENT-20261005",
  "parent_objective_id": "OBJ-GEOMETRY-BRC-RESIDUAL-ACCUMULATION-SYSTEMS",
  "parent_objective_generation_id": "OG-7AE66316D7566C519AE0",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "P06",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-BRC-CYCLE-FLUX-ENTRY-STATE-20261004",
  "successor_gate": {
    "new_information_gap": "P03/P04分别给出联合配对残差与循环通量/入口状态的待验证边界，但实际路由允许的操作词具有控制状态依赖；任意词闭包或只在单个Cell上检验的端口等价不能自动推出全局安全删状态。",
    "why_parent_result_does_not_close_it": "P04研究特定循环通量、入口状态和必要顺序是否闭合；它不构造有限控制状态下的合法操作语言，也不证明一个候选端口商对所有允许词和来源/配对读出都保持未来等价。P03同样只给联合关系前沿。",
    "discriminating_outcomes": [
      "构造控制状态×差异空间的严格下降算法，给出全局商q、每个允许操作的下降条件、拒绝词、终止证明和最短区分见证。",
      "若线性闭包不适用，转为完整有界状态关系，并给出两个被候选商错误合并但被合法未来词或来源/配对读出区分的严格反例。"
    ],
    "kill_condition": "任何未覆盖的隐藏控制状态、合法未来操作或来源/配对读出都使删状态许可失效；若非线性门控破坏线性不变核前提，则不得挪用Cayley-Hamilton或线性深度界。",
    "alternative_route_or_free_exploration_considered": "保存完整状态始终安全但没有压缩收益；把合法语言放宽成任意词闭包会产生伪等价。选择有限控制乘积是最小既保真又可判定的路线。",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "P04解决一个具体动态闭合问题，本项把P03/P04前沿提升为受限操作语言下的通用安全商判据，交付物是下降算法/有限关系证书而非单个循环窗口，因此需要独立任务。"
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:d74aad6dd53d0df42d950f7b1207b27d80696f23410bd06f53a038c459577bb2",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# 受限操作语言下的安全端口商与最小可观察状态

Status: `READY / PUBLISHED_REGISTERED / CLAIMABLE_AFTER_IMMUTABLE_RECORD`

## Mother question

固定一个具有有限控制状态的合法操作词语言后，哪些端口/内部状态可以在保持所有允许未来读出与来源—配对信息的条件下安全取商；最小可观察状态如何构造，何时必须拒绝删状态？

## Frozen inputs and scope

共同项目语义服从 P000。继承 P03 `RS-BRC-SOURCE-EXIT-PAIRING-20261004` 与 P04 `RS-BRC-CYCLE-FLUX-ENTRY-STATE-20261004` 的正式任务边界，不预设它们尚未执行出的科学结论。已完成前沿包括：任意有限切换线性集下公共不变核、至多 `m-rank(P)` 深度稳定和五 Cell `N2=0` 的条件推导。实际路由若存在状态依赖合法性，不得把任意词闭包或单 Cell 端口等价直接提升为全局结论。

私有恢复入口为 `EM-BRC-SLICE-PRIVATE-INTAKE-20261004-F9ED02`（SHA256=`1edf20e5880df29ca865e2249be429361ba6f1e24798cfb1ba6aebf1ec3bdc6d`）。公开任务书只保留必要任务元数据。

## Hard target and required outputs

固定一个有限控制状态集合、合法操作字母表与拒绝规则，明确每个操作对完整状态、来源/配对坐标和读出的作用。在线性段构造“控制状态 × 差异空间”的下降算法；若门控或容量使更新非线性，则转成完整有界状态关系，不借用线性 Cayley-Hamilton 保证。

至少交付：全局商 `q` 的精确定义；所有允许操作的等价保持/下降条件；被拒绝的词及原因；终止证明和深度界；最短区分见证；至少一个包含来源/配对读出的反例。若执行有限枚举或证书，分别列控制乘积、行空间基/有限关系生成、位长、证书检索与输出费用。

## Research value to preserve

公共不变核只在给定操作族和观察族下有意义。真实路由的合法词受控制状态约束时，过宽的词闭包会误删可观察残差，过窄的单点测试又不能证明全局安全。把控制状态显式乘入差异系统，可以给出可验证的最小状态商，并把“可以压缩”和“必须保留”分开。

## Success, kill, and return criteria

成功：明确全局 `q`、全部允许操作、拒绝词和终止证书；每个被合并状态在全部声明未来词与读出下等价，或存在最短反例精确阻断合并。

停止/否定：未经覆盖的隐藏控制状态、未来观察或来源/配对读出一律不授予删状态许可；非线性门控不满足线性前提时必须切换到有界关系证书。任务结束于安全商、严格反例或明确安全未决，不自动进入后续任务。
