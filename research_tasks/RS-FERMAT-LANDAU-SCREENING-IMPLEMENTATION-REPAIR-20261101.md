<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-FERMAT-LANDAU-SCREENING-IMPLEMENTATION-REPAIR-20261101",
  "title": "原稿筛选实现修复：Lucas 复合、轮素因子预处理与统一预算",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "原稿 Lucas 二次分支存在跨阶段状态错误，wheel 遗漏 D 的小素因子预处理；两条实现缺少覆盖全部阶段且不被 fallback 重置的统一预算与返回协议。",
  "next_action": "从固定原稿提取 Lucas 二次分支和 wheel_factorial_dichotomy_factor 原实现，先在声明的解释器中重放 N=108391,B1=50,k=2 与 N=1497,D=210；固定一个共享预算/因子验证结果协议，再依次修复两个错误并加入预算终止。",
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-FERMAT-LANDAU-SCREENING-IMPLEMENTATION-REPAIR-20261101",
  "parent_objective_id": "ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION",
  "parent_objective_generation_id": "OG-AA2BAD92F59DC97880C7",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "MAINTENANCE",
  "parent_task_id": null,
  "successor_gate": null,
  "dependencies": [],
  "source_refs": [
    "awdawmip/enterprise-math@a5902327c911630a2c6a387fbbc4822232edaebd:research_inputs/2026-11-01/fermat_landau_wheel_dichotomy_complete_monograph.md",
    "awdawmip/enterprise-math@1e41c0acc37b9347c91c1d4ded6327433d898edb:research_notes/2026-11-01/fermat-landau-monograph-review-6de891.md",
    "awdawmip/enterprise-math@996d6ef33dfbb8a3a8902ea81e9ff09b18053a56:research_tasks/PRIME_COORD_FACTOR_BLIND_BENCHMARK_SUITE_20260827.md"
  ],
  "evidence_status": "AUTHOR_REVIEW_AND_CODE_REPRODUCTIONS_IMPLEMENTATION_REPAIR_PENDING",
  "identity_lane": "SCREEN-REPAIR",
  "claim_lease_minutes": 240,
  "last_progress_ref": "awdawmip/enterprise-math@a5902327c911630a2c6a387fbbc4822232edaebd:research_inputs/2026-11-01/fermat_landau_wheel_dichotomy_complete_monograph.md",
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "Lucas",
    "wheel",
    "factor-screening",
    "implementation-repair",
    "budget"
  ]
}
-->

## Mother question

能否把用户原稿中的 Lucas 二次筛选分支与 Fermat/wheel 组合修复成可重复调用的有预算候选工具，使一次成功可直接验证，预算耗尽与未命中有明确返回，同时保留原有构造而不将未实现的理论复杂度写成运行保证？

## Frozen inputs and scope

固定原稿为 awdawmip/enterprise-math@a5902327c911630a2c6a387fbbc4822232edaebd:research_inputs/2026-11-01/fermat_landau_wheel_dichotomy_complete_monograph.md，原始文件 28957 bytes，SHA-256 af082f3c0485a309346a7e92791b7b75ff62f62e2db549d970900e9a5d4b95ad。消费作者核查说明 awdawmip/enterprise-math@1e41c0acc37b9347c91c1d4ded6327433d898edb:research_notes/2026-11-01/fermat-landau-monograph-review-6de891.md。该说明是作者核查与具体复算来源，非正式独立 Review；任务先重放实际所用代码与失败输入。

本任务限于原稿两条实现：factor_cyclotomic_torus 的 k=2 Lucas 分支，以及 wheel_factorial_dichotomy_factor 的小素因子预处理、已有有限 Fermat 检查和模轮积路径。其他分圆次数、环面投影、不可约性、光滑性全覆盖和模曲线理论不进入本次工程验收。四次分支若保留在原文件中，保持其来源状态，不以本任务通过为其数学认证。

运行时只接收 N、公开参数、独立种子（若所用原实现需要）与预算；已知分解只进入离线测试验证器。真实任务输入不要求能预先识别隐藏有利因子族，允许有预算试探后验证。复用现有 PCF 可用输入、结果及成本格式，不创建另一个 factor-blind benchmark suite。

## Hard target and required outputs

1. 修复 Lucas 跨素数幂阶段的指数复合。对 Q=1，以当前迹参数实现 V_ab(P)=V_a(V_b(P))，或使用同义的模矩阵/相邻 Lucas 状态；每次复合保留正确的当前交叉常数，不能跨阶段仍使用不匹配的初始 P。给出与独立模矩阵或递推参考的有界对照。回归 N=108391=107*1013、P=3、E=lcm(1..50)：V_E mod N=87421，gcd(V_E-2,N)=107。不要通过写入因子或特判该 N 修复。

2. 在 wheel 删除倍数前处理 D 的已知素因子。D=210 的预处理使用公开的 2、3、5、7；一般 D 的因子表要么作为预先声明的公开轮配置，要么将其构造计入预算。gcd(N,D)=N 不视为有效分解，继续在这些已知素因子中寻找非平凡因子或给合法未命中。回归 N=1497、D=210 必须取得因子 3。覆盖 N 与 D 互素、共享一个因子、N 整体整除 D、素数/平方/无效参数等实际接口边界。保留原稿已有 Fermat 范围及必要边界补轮，不用原失效的单点素数差条件跳过候选。

3. 给两个实现一个共享预算与类型化返回协议。至少支持可重放的整数操作/迭代上限：模乘或模矩阵工作、gcd、Fermat 候选与 wheel 项数；预处理、素数幂构造、Lucas 各阶段、边界补轮、候选验证都消费同一个预算，不能进入 fallback 时重置。可另设 wall-time 上限，但它不替代确定的工作计数。执行下一个计费步骤或有界批次前检查预算，避免默认构造长度约 sqrt(N) 的整个轮积。无需在本任务实现 BGS 或子乘积树；实际逐项模乘必须按其真实工作量记账，LCM 指数构造也不能按 O(log B1) 伪计费。

4. 命中返回 d 和可独立重放的验证数据，统一检查 1<d<N 且 N mod d=0。预算耗尽、声明搜索完成但未命中、无效输入分别返回明确状态，例如 FACTOR_FOUND、BUDGET_EXHAUSTED、NO_HIT_IN_DECLARED_SEARCH、INVALID_INPUT；报告已做工作、剩余预算及所用参数。未命中不产生素性或不可分解结论。若 gcd=N 只说明本次提取退化，按剩余预算处理并保留该状态。

5. 交付最小可复用修复代码、输入/结果协议、精确来源 manifest 和针对这三个已发现问题的回归证据。验证包括上述两个具体失败、若干不使用隐藏因子的独立小输入，以及零预算、恰够一步、在 Lucas 阶段/轮积中途耗尽、失败后进入剩余步骤等预算边界。每个声称因子均由独立整除检查器验证。报告实际运行环境、所测范围与每个阶段的计数，不追求大规模性能排名。

## Research value to preserve

这项任务把已有的具体构造修成可以安全消费的局部候选组件：Lucas 指数复合不再因状态错误丢失已满足条件的命中，wheel 预处理覆盖被轮主动删除的小因子，统一预算使昂贵路径可以廉价试探并给出可解释结果。有效因子是可直接验证的算术交付；既不需要先完成全环面理论，也不以修复程序证明全局速度优势。


## Success, kill, and return criteria

成功：两条原始失败在修复后按实际数学条件返回正确非平凡因子，独立小域对照一致，预算边界可重放，所有因子与返回类型符合协议。局部性能可按实际记录描述，不要求优于全部分解器。

如果独立参考与修复实现仍不一致，冻结具体 N、参数、阶段状态和最小失败见证，继续修该有限缺陷；若原稿另一个分圆分支存在理论问题，作为单独剩余问题保留，不把本工程任务扩展为全理论重建。一次失败或预算耗尽不是整个路线的否定。

返回修复源代码和来源 hash、回归输入与计数、类型化协议、已验证范围、未改变理论声明的状态说明，以及下一最小工程问题。仅重新报告原反例或新建泛化 benchmark 不构成本任务完成。
