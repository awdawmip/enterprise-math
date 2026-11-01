<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-BRC-TABLEFREE-TAIL-LOCAL-COST-20261101",
  "title": "免表尾部两校正传输：证书共享、阶数选择与局部资源成本",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "现有免表尾部已有偶阶下界、两校正证书、齐次 Horner 与系数缓存；证书/预测器共享、精确阶数选择或短串复用的一项局部资源增量待完成。",
  "next_action": "固定 source state mN=J²+R 与 h∈{1,2}，读取实际 lower_increment、two_correction_certificate、transport_certified_tail；列出重复幂/分母和阶数选择费用，选择其中一种机制完成一个局部优化。",
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-BRC-TABLEFREE-TAIL-LOCAL-COST-20261101",
  "parent_objective_id": "OBJ-SEMIPRIME-SQUARE-SHELL-FACTORIZATION",
  "parent_objective_generation_id": "OG-94F9DC002F795C10ACF9",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-SEMIPRIME-SQUARE-SHELL-MIDPOINT-BOUNDARY-FACTORIZATION",
  "successor_gate": {
    "new_information_gap": "现有精确免表尾部已给偶阶下界、两校正证书和有限 CPython CPU 负结果；证书与预测器共享幂/分母、单档阶数选择或连续状态复用能否在一个具体资源场景降低费用，仍是未完成的局部实现问题。",
    "why_parent_result_does_not_close_it": "母任务的平方壳/乘子等价没有测定现行免表实现的证书与预测器成本；原免表笔记证明存储性质并报告旧单步 CPU 结果，不能判定新的精确共享机制。Horner 已经实现在源码中，本任务不将该既有技巧当作新交付。",
    "discriminating_outcomes": [
      "选定的一种共享/阶数/短串复用机制保持精确目标状态与至多两次校正证书，并在预声明位长、尾部、内存条件下改善一种实际资源。",
      "共享机制正确但 CPU/空间开销无净改善，冻结完整成本分解、交叉条件和该场景 NO_GAIN 边界。",
      "拟议复用无法保持证书或精确状态，交付最小失败见证，并保存原可用后端与精确条件。"
    ],
    "kill_condition": "若优化破坏来源状态、严格整数下界、两校正判定或完整成本计费，应回退并保留见证；一个选定机制已经给出决定性局部结果后停止，不同时捆绑任意逼近、所有阶数和全部后端。",
    "alternative_route_or_free_exploration_considered": "同环境直接 isqrt、现有 pairwise/mod-8 传输和原免表后端均为替代。首次只选证书/预测器共享、精确阶数选择、短串复用三者之一；存储目标允许有 CPU 代价，不要求所有资源同时胜出。",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "该单元处理每次状态传输成本，与显式前缀命中排序和既有 residual-priority/Hart 流式排序科学增量不同。沿用母路线的精确乘子状态，新增一个可闭合的局部实现机制，不回填或重开已冻结的平方壳广域任务。"
  },
  "dependencies": [],
  "source_refs": [
    "awdawmip/enterprise-math@24eb5e125a7bf52366cc49f1ed2594c0cd6d5b14:src/enterprise_math/brc_table_free_tail.py",
    "awdawmip/enterprise-math@24eb5e125a7bf52366cc49f1ed2594c0cd6d5b14:research_notes/BRC_TABLE_FREE_TAIL_20260907.md",
    "awdawmip/enterprise-math@24eb5e125a7bf52366cc49f1ed2594c0cd6d5b14:research_notes/BRC_OPPORTUNISTIC_SHORTCUT_PORTFOLIO_20260907.md",
    "awdawmip/enterprise-math@212b6f7ee3966535db9376686ee6263271533713:research_notes/2026-11-01/local-solutions-and-parity-windows-6de891.md",
    "awdawmip/enterprise-math@996d6ef33dfbb8a3a8902ea81e9ff09b18053a56:research_tasks/SEMIPRIME_SQUARE_SHELL_MIDPOINT_BOUNDARY_FACTORIZATION_EXPLORATION_20260829.md",
    "awdawmip/enterprise-math@996d6ef33dfbb8a3a8902ea81e9ff09b18053a56:research_task_records/RS-SEMIPRIME-SQUARE-SHELL-MIDPOINT-BOUNDARY-FACTORIZATION/TP2-12778A2D48A1D5A57BA9.json"
  ],
  "evidence_status": "EXACT_CERTIFIED_TABLEFREE_TOOL_AVAILABLE_LOCAL_RESOURCE_OPTIMIZATION_OPEN",
  "identity_lane": "BRC-TAIL",
  "claim_lease_minutes": 240,
  "last_progress_ref": "awdawmip/enterprise-math@24eb5e125a7bf52366cc49f1ed2594c0cd6d5b14:src/enterprise_math/brc_table_free_tail.py",
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "BRC",
    "table-free-tail",
    "exact-certificate",
    "resource-cost"
  ]
}
-->

## 研究问题

现有 brc_table_free_tail 已通过精确偶阶下界与两校正证书消除逐乘子预测表依赖。原 CPython 测量给出存储收益与单步 CPU 成本差异。本任务选择一个结构受限的执行场景，改善证书/预测器之间的共享计算或阶数选择成本，得到可复用局部后端。

## 起点与最小单元

首轮资源评价限定母目标中的奇半素数 N；已有传输恒等式的更广整数有效域作为来源说明保留。源状态满足 mN=J²+R、0<=R<=2J，步长 h∈{1,2}、m>=h。沿用偶阶 K 的已有下界与证书
c_(K+1)J(h/m)^(K+1)+h/(2m)<=1，
以及 G=R+hN−d(2J+d) 和奇宽校正。

实际源码已经使用齐次 Horner，并缓存系数。先审计 two_correction_certificate 与 lower_increment 的 m^K / m^(K+1)、公分母和重复中间量，以及尝试多个 K 的总费用。选择“证书/预测器共享中间量”“以精确界选择一档阶数”或“有证明的连续状态复用”之一作为第一单元；其他方案作为后续，不捆成一次验收。

## 交付

1. 一项明确局部改进及其适用场景、输入条件和与原工具的精确对应。
2. 保留目标 (m+h)N=J'²+R'、0<=R'<=2J'，对证书通过的路径核对校正上界；边界包含 h=1/2、m=h 和证书临界附近。
3. 计入证书判定、阶数选择、冷/热系数、共享缓存、幂运算、整数位长、校正、完整输出和内存；与原免表后端及同环境 isqrt/现有传输进行同工作量比较。
4. 在一个预先定义的资源场景中交付实际收益，或交付可复用的成本边界/无收益原因；存储和 CPU 分别评价，不要求全部维度同时变好。
5. 直接扩展现有模块与测试/基准接口。任何新有理逼近或分块式需给对应下界/余项/校正关系，不替换成没有证书的近似。

## 查重与接续

本任务消费现有免表证明、阶数阈值和原性能记录，不再发布“去掉 O(M) 预测表”的同义问题，也不再发布已实现的 Horner 计算。
局部 prefix 任务关注候选顺序和命中，本任务关注单次或短串状态传输成本；二者可分别交付。
