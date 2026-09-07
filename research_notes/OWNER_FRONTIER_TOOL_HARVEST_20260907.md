# Owner 前沿定理与工具共享入口

状态：`TOOLBOX_INTEGRATION_CANDIDATE / ROUTING_ONLY / INTERNAL_REVIEW`。

本次使用已有 `research_method_inventory_addenda/*.json` 增量机制登记前沿成果，补足实验目录不会被 `src/enterprise_math` AST 扫描发现的检索缺口。具体目录为 [20260907_owner_native_frontier_candidates.json](../research_method_inventory_addenda/20260907_owner_native_frontier_candidates.json)。没有增加顶层工具 family，也没有用内部交叉审查替代正式 Driver/Steward 接受。

每条记录提供稳定 method ID、准确输入输出、定理或结构法则、复用判定、硬边界、实际 API、证明与独立审计来源，以及冻结源文件 SHA256。`status` 是候选状态；`classification` 表示建议归属而非接受程度。通用证书候选保留 `CANDIDATE_NOT_TOOL` 和建议的 subtool 分类；纯定理与纠错使用 `RESULT_ONLY`，不会伪造可执行 API。

## 查找与跨支线消费

在包含本增量目录的完整 source snapshot 中运行：

```text
python -X utf8 tools/enterprise_toolbox.py --json methods "minimum raw three axis query plan"
python -X utf8 tools/enterprise_toolbox.py --json methods "finite completely monotone exchangeable BRC"
python -X utf8 tools/enterprise_toolbox.py --json methods "quadratic shell maximal shortest length"
python -X utf8 tools/enterprise_toolbox.py --json methods "common depth first return two sided tail"
```

使用 `--json`，因为默认 `methods` 文本输出只显示分数、ID、名字，会隐藏状态和前提。现有 tokenizer 只索引 ASCII 词，纯中文查询可能返回空；应使用上面的英文短语、准确 method ID/API，或中英混合查询。需要家族及生产模块比较时用同样的 `--json coverage`；词面匹配只是检索候选，不是语义已覆盖或实际已执行的证明。

本地其他支线可以直接使用这个隔离 source checkout 的入口，不必修改自己的分支。其他环境应从 [研究 PR #1364](https://github.com/awdawmip/enterprise-math/pull/1364) 或全局知识库发布事件取得**完整远端 commit SHA**，读取该 SHA 上的目录、代码、证明和依赖，再核对记录中的文件摘要。不要只复制 JSON 却遗漏其引用的实验实现，也不要用活动分支名称代替消费记录中的冻结 SHA。

loader 只读取当前 checkout。候选目录发布到 GitHub 后，其他支线可以显式消费该冻结快照；旧 checkout 和 main 不会自动载入它。用户已明确要求及时进入 main，因此本轮发布后继续执行现有的有界集成流程，实际合入 commit 另由发布事件记录。本文件自身不声称合入已经发生；共享路由不提升 proof status，不转移定理 ownership，不授予正式 task 或 CLAIM。

## 消费地图

| 需要 | 目录 method ID | 保留的关键边界 |
|---|---|---|
| 原生三轴观察与稀疏恢复 | `candidate.x6.raw_joint_observer_recovery` | raw 联合坐标；空间质量不是 branch history |
| 有理可行或 Farkas 证明 | `candidate.certificate.rational_nonnegative_phase1` | 原方程回验；资源不足不等于不可行 |
| 含噪有限候选拟合 | `candidate.x6.budgeted_noisy_recovery` | 给定 D 与残差预算；真噪声与稀疏性外部声明 |
| 逐权重整数 histogram | `candidate.x6.integer_histogram_realization` | 一般表未分类；有理质量不是整数 branch 数 |
| 原词敏感的有限端口组合 | `candidate.x6.finite_reverse_step_port_monitor` | 有限 horizon；CWM 不替代 histogram |
| signed 最短词数素数赋值谱 | `candidate.x6.shortest_path_valuation_spectrum` | 参数为事件长度；丢失 endpoint 与 coprime unit |
| 最少静态三轴查询计划 | `candidate.x6.minimum_raw_query_plan` | 稀疏前提未由数据验证；不判实际数据歧义 |
| 区间负惯性指数证书 | `candidate.certificate.rational_interval_inertia` | 完整惯性还需严格条件；输入族与积分目标分开审核 |
| N8 reference 惯性 | `result.rh.n8_reference_eta09_inertia` | 仅指定 prime+Cauchy reference，不是 RH |
| 有限可交换词 BRC | `candidate.brc.finite_exchangeable_factorial_observer` | 阶乘观察，不是普通幂矩或任意非交换 prefix |
| PP 旧幂矩 lift 的阻断 | `result.pp.finite_power_moment_lift_obstruction` | m3 反例不否定 all-m HCM0 |
| 任意集合值通道观察商 | `candidate.x6.nonlinear_channel_gate_quotient` | 共同像 gate 等价不是实际动力可达 |
| 七正点稳定性界 | `result.x6.sparse_marginal_stability` | 最优常数仍在 `[1,111/20]` |
| 八正点极小 trade 分类 | `result.x6.weighted_minimum_trade` | 关闭指定删点路线，不解决一般最优常数 |
| 全 N 平方壳词长锐界 | `candidate.x6.quadratic_shell_max_shortest_length` | 参数为平方读出；辅助 b 不是真实 common-depth |
| 相对首返 common-depth 尾律 | `result.x6.common_depth_first_return_tail` | 非条件质量；不是完整原词权 histogram |
| 双侧 Fourier 倒数尾引理 | `result.analysis.two_sided_reciprocal_cusp_tail` | 四阶加权余项与整圆无零是必要输入条件 |
| RH 能量域勘误 | `result.rh.energy_domain_correction` | 全积分、尾积分、绝对交换各有定义域 |

这些记录服务于明确的未来复用或防止误用，没有把一个新定理自动包装成新工具。各证明报告保留外部先例：例如 Phase I/Farkas、PLDL 惯性、Meng–Sun 固定和四平方、Lawler–Limic Green 渐近和经典 Fourier 奇性分析。

## 验证与版本边界

`experiments/owner_tool_harvest_20260907/validate_catalog.py` 检查现有 loader 实际载入增量目录、全库 method ID 无重复、引用路径与冻结摘要匹配、API 在引用模块中真实定义、家族 ID 与复用字段有效，并实际验证各项自然语言查询能命中。它只认证目录与来源绑定，不重新证明数学定理。原实现检查与独立数学审计仍由每项 `validation_refs`、`source_refs` 给出。

目录更新时要先完成实际受影响的研究/消费者审核，再刷新对应摘要；不能自动把漂移的文件重新标成已审版本。本轮 A 的输入/大整数读出修复先完成，再由独立代理复验最终代码，之后才冻结此目录。

本次 GitHub 发布沿已审并发合同：验证远端父树等于上一共同基树，固定 owned 文件差集，在该父上创建 descendant，nonforce 推送并回读 tree。远端若已改变，重新合并实际 delta；不能只换 parent 而上传旧整树。全局知识库使用独立唯一 journal 事件记录确切 source commit 与本共享入口，保持记录库定位。

Driver-ID: EM-DVR-01E1D9 / CONTROL_PLANE
Global-Knowledge-Sync: main@4fa7d7d / GLOBAL_KNOWLEDGE_V1
