# OpenAI 公开数学成果｜CM 阿贝尔簇 Hodge Comparator 修复（2026-10-30）

状态：**PUBLIC_SOURCE_DELTA_VERIFIED / SOURCE_INTERFACE_REVIEWED / UNREVIEWED / NOT_ADMITTED**。本文件是当前普通 Chat 的来源核验及中立研究交接，不是 EM Native CLAIM、Result、Review、Driver 正式任务出版、独立 Lean 内核验证或数学定理验收。GitHub 当前验证身份 `awdawmip`；原生连接 `research_authority_granted=false`，未继承旧对话 session、密钥或贡献独立性。

## 1. 公开版本、时间和精确来源

- 基线 `openai/math@7ef5c0cc5ca4b0e072b7a050fca09ab24bc6fa3a`（2026-10-26）；本轮实读 `main@4eaee87548250b2682affda7d05d947c05554bae`，GitHub compare `ahead_by=2 / behind_by=0`。实际内容提交 `204e5f8f8a301d647f4bea76a5834e04fd2399ff`，提交时间 2026-10-29 23:29:22 UTC；合并提交 `4eaee875...` 时间 2026-10-30 00:35:35 UTC。相较基线，Compare 列出 281 个文件条目（`history.md` 1 个、Lean 路径 280 个；其中若干条目显示 0 行增删，不能将其推定为 280 个实质数学修改）。
- `history.md` 当前 blob `ce3d4ca01564fe0e796c441d1caa6489d661117b`，在标题 **October 29, 2026 / Formalization Fix** 下明确记载：*The rational Hodge conjecture for CM abelian varieties* 的 Comparator challenge 与 solution 使用的命名空间分歧已调整。精确链接：https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/history.md 。
- 主要差异：https://github.com/openai/math/commit/204e5f8f8a301d647f4bea76a5834e04fd2399ff ；基线至当前：https://github.com/openai/math/compare/7ef5c0cc5ca4b0e072b7a050fca09ab24bc6fa3a...4eaee87548250b2682affda7d05d947c05554bae 。
- OpenAI 官方公开公告核对：2026-10-26 https://openai.com/index/building-scientific-understanding-with-academic-communities/ 仍为最近相关数学/计算复杂性/物理公告；本轮未发现 10-29/10-30 另发的数学公告。该官网表述为公开研究主张与外部学术研究安排，不产生 EM 的数学接受。2026-10-07 撤回的三篇 Weil/Kuga–Satake/K3 论文，在当前 `history.md` 仍列为撤回；本次 CM Hodge Comparator 修复**不是**撤回论文恢复，也不是新论文。
- 本轮未发现 ETH/Kakeya 对应文件的新改动；已冻结 ETH A/B 任务外部 source pin **继续保持 `7ef5c0...`**，不得将本次 CM Hodge 修复静默替换为 A/B 的来源版本。

## 2. 精确形式命题接口与证明边界

`Challenge.lean` 由 blob `8e99b5004f788c5522ffaa972bdfd46d930135d8` 变为 `8c1726268436ce5e19513234a5b2750085db9777`。旧版使用短名称 `IsProjective`、`HasComplexMultiplication`、`algebraicCycleClassSpan`；新版把它们分别显式指定为：
`_root_.OAI.AlgebraicGeometry.Foundations.ProjectiveSpaceIs.IsProjective`、
`_root_.OAI.AlgebraicGeometry.ComplexMultiplication.Definitions.HasComplexMultiplication`、
`_root_.OAI.AlgebraicGeometry.ComplexPoint.Basic.ComplexSchemePoint.algebraicCycleClassSpan`。
`CM.lean` 同时将定义放进 `OAI.AlgebraicGeometry.ComplexMultiplication.Definitions`，并调整相关 de Rham/Hodge 引用及导入/namespace；改动与公开说明的名称对齐相符。

`Solution.lean` 在前后两个版本 **Git blob 均为 `e9855a415328438d063f5f3f132473bf919595e3`**，由 `OAI.AlgebraicGeometry.HodgeConjecture.MainSolution.hodge_conjecture_for_cm_abelian_varieties X hCM p` 提供证明；`MainSolution.lean` 前后 blob 均为 `abbe7ea5f1ffbdd2a86e561925854ce56e31c2c6`。`main.json` 前后 blob 均为 `7a3ee084f1de09a45618654cd1c11f2f0c8d878a`；声明 challenge/solution 模块、目标 `HodgeCM.hodge_conjecture_for_cm_abelian_varieties`、允许公理 `propext`、`Quot.sound`、`Classical.choice`，并设置 `enable_nanoda=false`。

精确外部目标是：对于满足 `IsIntegral X.left`、`Smooth X.hom`、上述 `IsProjective X.hom`、`GrpObj X`、`HasComplexMultiplication X` 的复几何对象 `X`，对所有 `p : ℕ` 有 `Hdg^p(X; ℚ) ≤ algebraicCycleClassSpan X p`（所有对象名称按新版完全限定的 Lean 定义解释）。`Challenge.lean` 的 `by sorry` 是 Comparator 题面占位，**不是解答通过的证书**；`Solution.lean` 连接现有 `MainSolution` 亦不足以代替完整依赖闭包、目标同一性和实际内核/Comparator 检查。配置里允许公理列表是声明，尚非内核 `#print axioms` 的实际输出。无本轮 Lean/Comparator 运行日志、全依赖/公理审计或独立第三方数学验收；不认定新证明已验收，不将公开外部定理当作 EM 既有结果。

可核源码：
- https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/HodgeConjectureCMAbelianVarieties/Challenge.lean
- https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/HodgeConjectureCMAbelianVarieties/CM.lean
- https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/HodgeConjectureCMAbelianVarieties/Solution.lean
- https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/HodgeConjectureCMAbelianVarieties/main.json

## 3. EM 的当前前沿、去重、原生边界

本轮读取 `enterprise-math main@aeba28cc77ccd95884bbe0dec1d0225732559d9d`，P000 blob `bcc2590d3168a28f72e8b9f0f9b1f76faadcd488`，同时按 ACTIVE `HEARTBEAT_WORLD_NATIVE_X6_TIME`、`RESIDUAL_FAITHFUL_DISCRETE_RELATIONAL_SYSTEM` 与联合观察保真约束解释外部类型；本轮无 P000、世界观或原生六轴定理更动。账户 global canonical main 的本轮已核入口为 `c9259906ca93c223475c87c65dd15edd3f3c3a54`，`GLOBAL_KNOWLEDGE_V1`。EM 原生 `em_status` 报 v0.6.11、服务固定 Source EM `aeba28...`、服务独立 global source pin `7b33f8066e9993e7c941959a9d738ed405248eb8`；服务固定 pin 与账户当前 canonical main 需分开保留。

继续消费 2026-10-29 已回读审计 `research_notes/public_math_intake_20261029/OPENAI_OCT29_SOURCE_UNCHANGED_TASK_DEDUP.md`；family129 的已 ACCEPTED 有限证书不因本更新重新开题；三项 2026-10-28 已正式发布的 V2 Task（`RS-OPENAI-ETH-BRC-REPRESENTATION-20261028`、`RS-OPENAI-ETH-CELL-COUNTING-20261028`、`RS-OPENAI-QFT-BRC-RESIDUAL-20261028`）源与任务出版边界不变。公开吸收初轮 Objective 的已读取不可变记录 `OBJ-PUBLIC-MATH-ABSORPTION-20261007@OG-9C0E1497D407F544BF64` 存储状态为 `OPEN`，其 2026-10-07 scope 有界；不从单一不可变记录推断实时运行态。

`em_control_tasks(request_id=public-math-audit-20261030-taskscan)` 本轮返回 `CONTROL_QUOTA`；`em_status` 显示当前连接 `research_authority_granted=false`、`executor_binding_configured=false`、`active_jobs=5/5`。因此本轮无法独立核定最新 CLAIM/Driver/owner 实时授权，也没有原生 Driver 正式发布、Review、Result 或 native publication receipt。此文件是保全新增来源和有限检查方案的中立 GitHub 材料；后续权限获取必须由合法主体按当前 native 合同进行，不以新会话身份规避现有拒绝。

## 4. 有限信息增益与下一精确单元

候选：**CM Hodge Comparator 声明同一性和依赖可信边界的有限复验**，优先作为公开成果验收方法的补充，不重复 ETH × BRC 或 family129 现有数学任务。严格限定新旧 commit、`Challenge.lean`、`CM.lean`、`Solution.lean`、`MainSolution.lean`、`main.json` 与受影响依赖；检验修复后 challenge 与 solution 是否在 Lean elaboration 后具有同一定义域、假设、结论与所需公理。必要动作：在锁定的 Lean/mathlib/toolchain 环境实际编译并运行其 Comparator，检查依赖闭包及每个目标的 `#print axioms`；排除 `sorry/admit` 和自定义假设替换主结果；若失败，提交最小失配反例、失败日志与输入 pin。形式检查必须保留论文语义和实例前提，不凭路径命名或 Comparator 配置断言证明有效。

本次来源接口检查不涉及将 BRC 对象计算消元，故其源级对齐测试的 BRC 判定为 `NOT_APPLICABLE`；若以后尝试把该连续复几何命题映射到 EM 的 X6/BRC，须先定义有类型载体、观察、允许未来操作与保真证明，不能将外部复代数几何陈述直接提升为原生 P000 定理。是否需要为该有限复验正式出版后继 Task，应由有真实 Driver/owner 权限的角色在恢复可用的 canonical 控制读取后，检查有无同范围已发布任务并按当前准入合同作决定；**本文未正式发布该候选任务**。

接续验收：保留本文件本次 GitHub PR 的提交/回读；合法 Driver/owner 首先回读当前 Task/runtime 及原请求是否已有完成，不重复建立后继；若无对应正式任务而研究价值足够，再按现行 V2/source Native 合同决定发布，并回读不可变 taskbook/publication 与 native receipt。发布是独立动作，不能由本文件存在代替。
