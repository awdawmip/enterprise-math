<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-ROUGH-PARITY-LOCAL-STATE-UPDATE-20261101",
  "title": "粗素因子有界深度奇偶状态：素数插入更新与局部成本",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "已有粗因子深度 K=2/3 的精确奇偶读出窗口及真实 prime-insertion 递推；所选单一深度族上的状态维护、精确子尺度共享与完整维护成本尚未完成。",
  "next_action": "固定 y、K∈{2,3}、一个有限有序粗素数窗口与相应精确子尺度集合，消费已给奇偶读出式；从 F_new(T,z)=F_old(T,z)+zF_old(T/p,z) 推出二项矩/原始矩的更新，并核查一次和两次实际素数插入。",
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-ROUGH-PARITY-LOCAL-STATE-UPDATE-20261101",
  "parent_objective_id": "OBJ-GEOMETRY-BRC-RESIDUAL-ACCUMULATION-SYSTEMS",
  "parent_objective_generation_id": "OG-7AE66316D7566C519AE0",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "INTEGRATION",
  "parent_task_id": null,
  "successor_gate": null,
  "dependencies": [],
  "source_refs": [
    "awdawmip/enterprise-math@212b6f7ee3966535db9376686ee6263271533713:research_notes/2026-11-01/local-solutions-and-parity-windows-6de891.md",
    "awdawmip/enterprise-math@24eb5e125a7bf52366cc49f1ed2594c0cd6d5b14:research_notes/RH_CRITICAL_ROUGH_ARITY_POSITIVE_HISTOGRAM_GAUGE_20260908.md",
    "awdawmip/enterprise-math@9bce0563395c812cf1bb92dff8d991ffba1f51f2:research_notes/early_bottleneck_revisit_20261029_c5a31e/REVIEW_AND_CANDIDATE.md",
    "awdawmip/enterprise-math@24eb5e125a7bf52366cc49f1ed2594c0cd6d5b14:src/enterprise_math/p017_rough_recursion.py"
  ],
  "evidence_status": "AUTHOR_DERIVED_LOCAL_PARITY_WINDOWS_AND_EXISTING_INSERTION_RECURRENCE_STATE_MAINTENANCE_COST_OPEN",
  "identity_lane": "ROUGH-PARITY",
  "claim_lease_minutes": 240,
  "last_progress_ref": "awdawmip/enterprise-math@212b6f7ee3966535db9376686ee6263271533713:research_notes/2026-11-01/local-solutions-and-parity-windows-6de891.md",
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "rough-primes",
    "parity",
    "finite-depth",
    "state-update",
    "local-cost"
  ]
}
-->

## 研究问题

本轮已有的奇偶读出公式直接作为输入。本任务研究这些量怎样在真实素数插入和子尺度变换中维护，使有界粗因子深度区域形成可复用算法。

对固定 y，令 H_y(T,r) 为原首余弦权的平方自由粗因子直方图，P_y(T)=Σ_r(-1)^rH_y(T,r)。取严格大于 y 的前 k 个素数之积 q_k。已取得 T<q_3 上 P=M0−4M1+2M2，以及 T<q_4 上 P=M0−4M1+2M2−8H(T,3) 的作者符号推导。先保留该实际来源等级，消费其证明与输入定义，不将重新证明插值恒等式当作本任务全部交付。

## 起点与最小单元

使用现有精确正递推 F_new(T,z)=F_old(T,z)+zF_old(T/p,z)，其中新加入的 p 尚未出现在旧允许素数集。固定一个有限有序粗素数窗口和 K=2 或 K=3，选择一次及两次插入作为第一单元。

可使用二项矩 B_j(T)=Σ_r binom(r,j)H_y(T,r)。需要具体推导和维护的关系为
B_j,new(T)=B_j,old(T)+B_j,old(T/p)+B_(j−1),old(T/p)，B_(−1)=0。
也可使用等价原始矩更新，但应说明状态变换的成本。

子尺度保留精确 T/d；原余弦权取决于 T/d 本身，不可仅凭 floor(T/d) 相同就合并。允许用有来源的符号权与精确整数系数证明递推，再对需要的数值观察使用实际匹配的接口和误差语义。

## 交付

1. 一组明确输入、合法操作、深度界、状态表示和读出规则，以及一次/两次插入下的精确维护关系。
2. 在所选族上完成原目标 P 的恢复；若扩展 K=2 到 K=3，说明新增状态、更新和读出的变化。
3. 给可重放的小型证据与一个边界见证，核查重复素数、平方自由条件、空支路和子尺度合并。
4. 用实际输入参数计费：素数窗口大小、深度 K、不同子尺度数、平滑基底初始化、缓存、运算次数及所用权重的表示/求值成本。
5. 完成一个新的局部维护算法、共享状态规律、明确修复，或有信息增量的可复用维护成本界。已证明的窗口公式与统一低矩边界继续作为输入。

选择一种实际可执行操作族即可，不要求同时解决任意后继、全部尺度或 RH 的统一估计。若某候选状态在下一插入失效，保存具体见证并尝试最小补充状态，返回已完成部分与下一精确问题。

## 查重与接续

RH-BRC-CARRY-CLOSURE-20260909 的任务是耦合 moving-port 平方函数与全尺度 polylog 闭合；本任务研究粗因子直方图有限深度状态的具体维护。
RS-BRC-FUTURE-FAITHFUL-INTEGRATION-20261028 已覆盖一般未来保真、ETH 编码与原生响应；本任务选择固定算术观察和已给出的精确窗口，不重建一般 BRC 保真体系。
src/enterprise_math/p017_rough_recursion.py 处理最小素因子/区间子窗口；其中 Ω 含重数，而本任务 r_y 为互异粗素因子数。相关工具须按类型适配后复用。
