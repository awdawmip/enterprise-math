<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-BRC-LOCAL-PREFIX-NET-VALUE-20261101",
  "title": "既有 BRC 局部前缀组合：固定预算净收益与适用区域",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "既有 kernel13、learned20、去重与 fallback 工具已保留；在固定后端、位长、M=1000 与独立分布上的完整净成本、失败费用和尾部成本仍待量化。",
  "next_action": "调用现有 kernel13_prefix/kernel13_order、learned_cover_order、multiplier_probe_batches 与 RegimeShortcutLedger；固定一个真实求值后端、一类预先定义结构输入及独立对照分布，先比较结构顺序和固定预算前缀的成对总成本。",
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-BRC-LOCAL-PREFIX-NET-VALUE-20261101",
  "parent_objective_id": "OBJ-SEMIPRIME-SQUARE-SHELL-FACTORIZATION",
  "parent_objective_generation_id": "OG-94F9DC002F795C10ACF9",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-SEMIPRIME-SQUARE-SHELL-MIDPOINT-BOUNDARY-FACTORIZATION",
  "successor_gate": {
    "new_information_gap": "既有 kernel13/learned20/去重 fallback 已有命中秩和保留率证据；在一个明确后端、位长、M=1000、固定预算及独立分布中，前缀试探的端到端净成本和尾部成本尚未在本单元中量化。",
    "why_parent_result_does_not_close_it": "母任务的 Fermat/平方壳精确等价和已测静态特征边界不确定这组后来保留的显式短前缀在具体成本环境中的净收益。现有 Hart streaming 子任务研究 residual 阈值/桶排序，QR/CRT 子任务研究隐式索引，均不闭合本次 kernel13/learned20 组合机制。",
    "discriminating_outcomes": [
      "在预声明区域与独立对照上，前缀加现有 fallback 保持相同候选覆盖并降低完整成对总成本，冻结可复用的局部预算与收益范围。",
      "命中秩改善但完整成本或尾部变差，定位候选生成、预筛、求值、gcd 或失败试探中的具体支出，冻结该环境的 NO_GAIN 边界。",
      "收益仅在一个允许的公开上下文或已物化状态条件成立，保留该局部路由；隐藏因子标签只用于离线解释，不回流运行时。"
    ],
    "kill_condition": "发生隐藏标签用于候选/路由、候选集合不一致、遗漏失败/fallback/预处理费用时，修复该实验再判定。固定单元已足以判明无净增量后停止该配置，不无界扩展样本或调参维持任务。",
    "alternative_route_or_free_exploration_considered": "保留当前结构顺序作为零新增开销替代；可在固定预算下尝试已有 learned20/kernel13 专家。若所选后端的求值太便宜，保存无收益结果，只有声明新的成本机制或输入族才另开试验，不要求先发明普适分类器。",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "这是既有 portfolio 的特定局部成本续研，交付可在一次配对实验内闭合；不重开母任务的广域特征普查，不占用 Hart streaming 现有 owner，不修改已有冻结结果。独立任务能把局部收益、失败预算与复用条件保存为可执行工具证据。"
  },
  "dependencies": [],
  "source_refs": [
    "awdawmip/enterprise-math@24eb5e125a7bf52366cc49f1ed2594c0cd6d5b14:src/enterprise_math/brc_opportunistic_shortcuts.py",
    "awdawmip/enterprise-math@24eb5e125a7bf52366cc49f1ed2594c0cd6d5b14:research_notes/BRC_OPPORTUNISTIC_SHORTCUT_PORTFOLIO_20260907.md",
    "awdawmip/enterprise-math@24eb5e125a7bf52366cc49f1ed2594c0cd6d5b14:research_notes/BRC_SQUAREFREE_KERNEL_COMPRESSION_NEGATIVE_20260907.md",
    "awdawmip/enterprise-math@24eb5e125a7bf52366cc49f1ed2594c0cd6d5b14:research_tasks/SEMIPRIME_RESIDUAL_PRIORITY_HART_STREAMING_COST_AUDIT_CANONICAL_REPUBLICATION_20261013.md",
    "awdawmip/enterprise-math@24eb5e125a7bf52366cc49f1ed2594c0cd6d5b14:research_tasks/FACTOR_BLIND_QR_CRT_PREFIX_INDEX_COST_20261013.md",
    "awdawmip/enterprise-math@212b6f7ee3966535db9376686ee6263271533713:research_notes/2026-11-01/local-solutions-and-parity-windows-6de891.md",
    "awdawmip/enterprise-math@996d6ef33dfbb8a3a8902ea81e9ff09b18053a56:research_tasks/SEMIPRIME_SQUARE_SHELL_MIDPOINT_BOUNDARY_FACTORIZATION_EXPLORATION_20260829.md",
    "awdawmip/enterprise-math@996d6ef33dfbb8a3a8902ea81e9ff09b18053a56:research_task_records/RS-SEMIPRIME-SQUARE-SHELL-MIDPOINT-BOUNDARY-FACTORIZATION/TP2-12778A2D48A1D5A57BA9.json"
  ],
  "evidence_status": "EXISTING_TOOLIZED_SHORT_PREFIX_PORTFOLIO_LOCAL_END_TO_END_COST_OPEN",
  "identity_lane": "BRC-PREFIX",
  "claim_lease_minutes": 240,
  "last_progress_ref": "awdawmip/enterprise-math@24eb5e125a7bf52366cc49f1ed2594c0cd6d5b14:src/enterprise_math/brc_opportunistic_shortcuts.py",
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "BRC",
    "kernel13",
    "learned20",
    "prefix",
    "local-net-value"
  ]
}
-->

## 研究问题

13 核/98 乘子在 M=1000 的既有有限验证中保留了完整 625 代表扫描的部分命中。现有 portfolio 已实现前缀、去重和完整剩余候选。本任务测量这种局部试探在什么运行场景具有实际净收益，并把结果用于同一工具的预算/顺序选择。

## 起点与最小单元

直接复用 src/enterprise_math/brc_opportunistic_shortcuts.py 的 kernel13_prefix/kernel13_order、learned_cover_order、multiplier_probe_batches、RegimeShortcutLedger 和现有 BRC 求值后端，不重建同义候选库、调度器或账本。

第一单元固定一种候选求值后端、一个明确位长区间和 M=1000；预先选择一种有依据的结构输入族及独立对照分布，使用相同廉价预筛。比较结构基线、kernel13 前缀、learned20 前缀及其已有去重 fallback。适用性可以通过有预算试探加事后因子验证处理；候选生成、路由和预算只使用公开输入与允许上下文。

## 交付

1. 每个输入的完整成对成本：预处理、候选生成、求值、过滤、gcd、前缀未命中、fallback、重复工作避免、峰值空间与总时间；保留超时和失败记录。
2. 命中率、总成本及尾部成本，区分全体样本、廉价预筛后的样本、完整扫描可命中样本。历史保留率直接引用，不作为新增实验。
3. 至少一个局部结果：可复现的正净收益区域及适用预算，或该预设区域的明确无收益原因和可复用成本模型。
4. 用实际公开上下文记录或路由，如位长、扫描长度、既有状态是否已物化、内存压力；已知因子及 q/p 只用于离线标注和解释。
5. 将新结果接回既有 trial plan/ledger，保持候选去重和完整回退的原有正确性。选择一个有信息增量的策略改动即可，不要求所有后端和位长都获益。

成功标准是本次声明区域内的可核验能力/成本增量；允许局部正收益，即使其他区域表现不同。若一个候选不划算，保存原因并明确是否存在可改变的成本条件，不以此扩大否定整个平方自由核结构。

## 查重与接续

RS-SEMIPRIME-RESIDUAL-PRIORITY-HART-STREAMING-COST-AUDIT 已专门研究 upper-square residual 阈值/桶排序及 32–96 位 Hart/Fermat 匹配成本。本任务不重复该主实验、不重新调同一 residual-priority 候选。
RS-FACTOR-BLIND-QR-CRT-PREFIX-INDEX-COST 研究隐式 CRT/MITM rank/select 的精确算法和付费成本，本任务使用已有显式短前缀。
RS-VALLEY-BAND-FACTORING-REPRODUCIBLE-BENCHMARK-ABLATION 的 CFRAC/QS 关系收集与矩阵秩消融保持独立。
已有 PCF benchmark 的可用输入和成本工具可直接消费，不再建一个泛化 benchmark suite。
