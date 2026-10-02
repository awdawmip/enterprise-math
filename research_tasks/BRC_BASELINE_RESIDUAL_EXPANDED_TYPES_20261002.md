<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-BRC-BASELINE-RESIDUAL-20261002",
  "title": "BRC 残差跨模型类型扩展验证：闭包、记忆、吸收与图结构边界",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "frontier": "本次有限类型扩展已完成并归档，summary PASS：11类机制含保留控制，积分噪声与j权重为同机制，不计为11个独立盲实验。完成1664个生产矩时点、112个显式分布时点、768个条件Markov四阶矩与768个方差核对；动力学640个仿射时点、20个显式时点、48个非线性转换、256个状态依赖转换、12个有限尾；图上6矩阵×3初值及22182个精确断言。计数重叠，不相加为独立实验。负例与未定义指标均保留；没有正式CLAIM、Driver接受、N0或物理力律结论。",
  "next_action": "从commit 46bd4dbe07fa0a7b5b92f612b16b68b70d48e45c的报告与summary恢复已完成前沿，审阅跨类型结论、闭包失败、相关谱和边界归一化。既有首轮、尺度衰减与本轮完成单元不默认重跑；只有实际新模型或观测数据缺口明确时再有界恢复，不自动继续无限验证。",
  "dependencies": [],
  "source_refs": [
    "https://github.com/awdawmip/enterprise-math/blob/4ef1370c5dfa5fa20ade50906e1df1c544515cfc/src/enterprise_math/brc_transport.py",
    "https://github.com/awdawmip/enterprise-math/blob/4ef1370c5dfa5fa20ade50906e1df1c544515cfc/research_notes/BRC_TRANSPORT_RESIDUAL_EXTRACTED_RESULT_20260919.md",
    "https://github.com/awdawmip/enterprise-math/blob/4ef1370c5dfa5fa20ade50906e1df1c544515cfc/native_semantics_admissibility.json",
    "https://github.com/awdawmip/enterprise-math/blob/8946bbba19f1f8589ef8c2d0d69f1b6a84e4e84e/experiments/brc_model_benchmark_20261002_fca717/REPORT.md",
    "https://github.com/awdawmip/enterprise-math/blob/8946bbba19f1f8589ef8c2d0d69f1b6a84e4e84e/experiments/brc_model_benchmark_20261002_fca717/results.json",
    "https://github.com/awdawmip/enterprise-math/blob/8946bbba19f1f8589ef8c2d0d69f1b6a84e4e84e/experiments/brc_model_benchmark_20261002_fca717/METHOD_AUDIT.md",
    "https://github.com/awdawmip/enterprise-math/blob/b7bec0be19987620eb77e7e72122c79e557aeb1a/experiments/brc_residual_spatial_decay_20261002_fca717/REPORT.md",
    "https://github.com/awdawmip/enterprise-math/blob/b7bec0be19987620eb77e7e72122c79e557aeb1a/experiments/brc_residual_spatial_decay_20261002_fca717/results.json",
    "https://github.com/awdawmip/enterprise-math/blob/b7bec0be19987620eb77e7e72122c79e557aeb1a/experiments/brc_residual_spatial_decay_20261002_fca717/METHOD_AUDIT.md",
    "https://github.com/awdawmip/enterprise-math/blob/b7bec0be19987620eb77e7e72122c79e557aeb1a/experiments/brc_residual_spatial_decay_20261002_fca717/run_spatial_decay.py",
    "https://github.com/awdawmip/enterprise-math/blob/46bd4dbe07fa0a7b5b92f612b16b68b70d48e45c/experiments/brc_expanded_types_20261002_fca717/REPORT.md",
    "https://github.com/awdawmip/enterprise-math/blob/46bd4dbe07fa0a7b5b92f612b16b68b70d48e45c/experiments/brc_expanded_types_20261002_fca717/summary.json",
    "https://github.com/awdawmip/enterprise-math/blob/46bd4dbe07fa0a7b5b92f612b16b68b70d48e45c/experiments/brc_expanded_types_20261002_fca717/run_all.py",
    "https://github.com/awdawmip/enterprise-math/blob/46bd4dbe07fa0a7b5b92f612b16b68b70d48e45c/experiments/brc_expanded_types_20261002_fca717/RELATED_BRANCHES.md",
    "https://github.com/awdawmip/enterprise-math/blob/46bd4dbe07fa0a7b5b92f612b16b68b70d48e45c/experiments/brc_expanded_types_20261002_fca717/GRAPH_BOUNDARIES.md",
    "https://github.com/awdawmip/enterprise-math/blob/46bd4dbe07fa0a7b5b92f612b16b68b70d48e45c/experiments/brc_expanded_types_20261002_fca717/DYNAMICS_REVIEW.md"
  ],
  "evidence_status": "EXPANDED_TYPES_COMPLETED_SOURCE_VERIFIED_SUMMARY_PASS_WITH_CONTROLS_AND_NEGATIVE_RESULTS_NO_CLAIM_DRIVER_ACCEPTANCE_OR_N0",
  "last_progress_ref": "https://github.com/awdawmip/enterprise-math/blob/46bd4dbe07fa0a7b5b92f612b16b68b70d48e45c/experiments/brc_expanded_types_20261002_fca717/REPORT.md",
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "BRC",
    "synthetic-benchmark",
    "residual",
    "expanded-model-types",
    "moment-closure-boundary",
    "memory",
    "absorption",
    "finite-graphs",
    "completed-direct-research",
    "scope-revision"
  ],
  "claim_lease_minutes": 120,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-BRC-BASELINE-RESIDUAL-20261002",
  "parent_objective_id": "BRC-BASELINE-RESIDUAL-LAWS",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "BRC",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "NEW_DIRECTION",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:44b2174111ec85b5dd252d07f474772649a4d36936b2c99acbfa2cfba8af7a73",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# BRC 残差跨模型类型扩展验证：闭包、记忆、吸收与图结构边界

Status: V2 task registration; execution authority is separate; the completed direct-research extension is tracked by its activity and verified report.

本代沿用 `RS-BRC-BASELINE-RESIDUAL-20261002` 与 `DIRECT_USER_DIRECTION`，响应用户“扩大验证的类型范围”的明确指令，supersede `TP2-3DE3CA9E9F75E8F5D084`。所有旧 record 与 taskbook 字节保留。本轮已完成 direct `TASK_RESEARCH` 的有限扩展；任务登记不追溯授予 CLAIM、Driver 接受、N0 或物理规律。

## 0. Mother question

把已完成的线性基准和特定尺度/图壳例子扩展到不同模型类型，检验 BRC 残差的表示、矩闭包和衰减结论何时保留，何时因非线性、乘性分支、记忆、吸收或图结构失效。本轮结果已归档：出现幂律、指数衰减、非零平台、周期保持、最终增长和指标未定义，反平方不是本集合中残差的统一规律。有效独立项数、响应权重、相关时间、图谱、边界和观测归一化是报告中提出的有界解释；不将合成模型解释提升为普遍物理机制。

## 1. Frozen inputs and scope

### 继承前沿与本轮不可变证据

前两轮线性衰减、扩散、振荡基准，以及标准化累积量/RMS、壳平均和局部 outward Moore 端点 CWM 的结果，继续按 frontmatter 的 immutable `source_refs` 恢复。上一轮立方/树图与已有等幅、中性、独立控制不重复计算为新类型。既有 `brc_transport.py` 和 `native_semantics_admissibility.json` 的来源保持不变。

本轮研究源为 commit `46bd4dbe07fa0a7b5b92f612b16b68b70d48e45c`，目录 `experiments/brc_expanded_types_20261002_fca717/`。父执行报告 13 个源文件已通过真实 `github_fetch_file` 全文件读回并逐字匹配本地；本修订直接读取最终 `REPORT.md` 与 `summary.json`。报告和 summary 是恢复入口，`run_all.py` 是重跑入口，`RELATED_BRANCHES.md`、`GRAPH_BOUNDARIES.md` 和 `DYNAMICS_REVIEW.md` 分别保留相关机制推导、图边界与研究内交叉检查。

研究活动为 `RA-BRC-BENCHMARK-20261002-FCA717`，publisher 为 `EM-BRC-FCA717`。研究内交叉检查不是正式 Driver 接受。计数和源码 SHA-256 以该 commit 的 `summary.json` 为准。

### 实际完成的 11 类机制（包括控制）

| 类别 | 冻结模型与参考 | 本轮有界结果或边界 |
|---|---|---|
| 1. 非均匀独立响应 | 等幅、`j`、`(3/4)^(j-1)`、`(4/3)^(j-1)`；仿射矩递推、早期枚举 | 响应权重改变有效独立项数、平台或宽度指数；不同变量下的率不混同 |
| 2. 真正有限窗口 | `L=2,4,8`；移位删除旧状态并跨窗口填满时刻枚举 | `gamma4=-2/min(n,L)`，长期平台，不把加权累积当作有限窗口 |
| 3. 相关创新 | 二状态符号 Markov 核，`rho=-1,-1/2,0,1/2,3/4,1`；条件矩与枚举 | 混合、持续与交替分别给出衰减、平台和退化时点；保留隐藏状态 |
| 4. 乘性随机系数 | 独立乘子 `3/4,5/4` 各半，`X0=1`；原始矩闭式与枚举 | 均值恒为 1，标准化四阶量最终增长；不把随机系数替换为均值系数 |
| 5. 旋转线性模态 | 二维 `cR`，`c=3/4,1,4/3` 与正坐标方向噪声；径向递推/枚举 | 中性径向量 `-1/n`，阻尼和放大均有非零平台而宽度不同 |
| 6. 二次非线性 logistic | `r=2,3,4`，两种同均值方差初态；完整端点 CWM | 所选二次映射证明只保留前两阶不足；不声称一般非线性或混沌已验证 |
| 7. 状态依赖 lazy Ehrenfest | 容量 `N=4,8`；条件矩与完整二项平稳式 | 此特例前两阶仍精确闭合，不将状态依赖等同于必然不闭合 |
| 8. 有限四环 | 有/无停留；矩阵、全谱和正路径枚举 | 周期保持与指数混合不同，有限图不套用无限壳空间率 |
| 9. 缺陷/瓶颈图 | 两组四点图，强弱割 `epsilon=1/4,1/64`，固定初始组间模态 | 相同节点数的混合速率不同，参数与初始模态必须保留 |
| 10. 吸收边界 | 3 个内部点的区间及加停留版本；次概率 CWM | 生存质量与条件形状分开；质量衰减不保证条件形状收敛 |
| 11. 矩存在性边界 | 对称幂尾 `p=2,4`；有限截断 `L=8,...,256` 与无限尾判据分开 | 截断可计算不代表无限分布的所需矩存在；未执行无限 BRC |

另完成二维积分噪声 `v'=v+epsilon, x'=x+v` 的临界剪切实现。它与第 1 类 `j` 权重同属一个响应机制，不作为额外独立机制或重复证据。11 类包括等幅、`rho=0`、中性模态等保留控制，不能写成 11 个独立盲实验。logistic 是本轮选定的二次映射，不声称额外完整覆盖任意二次系统。

### 同指标登记与关键负例

原始均值/协方差误差、标量 `gamma4=kappa4/Var^2`、二维径向 `K/S2^2`、TV、生存质量和带符号二次缺陷分别登记参考、观测、归一化、变量与证据级别。统一的是登记方式，不是可以跨所有面板直接比较的数值。时间 `t`、中心 RMS 宽度 `ell`、漂移位移与图距离 `r` 不能互换；只有在明确模型中核验了关系才能转写率。

本轮必须作为完成证据保留的负例：

- `rho=-1/2` 在 `n=1..16` 拟合 `C/n` 得负系数约 `-0.8890`，长期已推导系数为 `+2`；`17..128` 留出未重拟合，短期拟合会错符号。
- logistic 两初态的前两阶相同但下一步方差不同；前两阶高斯闭包对两者都错。`r=4` 两步均值差 `3/4`，不据此声称一般混沌验证。
- 随机乘子的均值恒为 1，而标准化四阶量最终按 `(353/289)^n` 增长；短期为负、`n=3` 变正，不冒称全程单调增长。
- 无停留吸收区间的生存质量衰减，条件形状仍两周期；条件化与质量损失不同，不能每步重归一化后把损失隐去。
- `rho=-1` 的 64 个偶数正时点方差为零，`gamma4` 记 `null` 和原因，不替换为 0。
- 无限尾 `p=2` 普通均值不可积、二阶发散；对称截断均值 0 不能代表其普通均值。`p=4` 均值/方差存在而四阶发散，标准化四阶量不可用；有限截断属于另一个分布。

positive BRC mass/概率保持非负；有符号坐标、特征值和残差属于外部读出，不能等同于 signed wave amplitude 的干涉传播。本轮未验证一般波动 PDE。所有模型是合成例子；既无真实观测数据，也无由正质量指数推导的吸引力、引力或 N0。

## 2. Hard target and required outputs

以下是已完成的有限类型协议与验收证据。当前下一步是从归档评审，不默认重新执行。

| 模块 | `summary.json` 的实际检查计数 |
|---|---|
| 不等幅/窗口/相关 | 1664 个生产矩时点，112 个显式分布时点，768 个条件 Markov 四阶矩核对，768 个精确方差核对，64 个零方差时点 |
| 动力学 | 640 个仿射时点，20 个早期显式分布时点，48 个非线性转换，256 个状态依赖转换，12 个有限尾截断 |
| 图与边界 | 6 个矩阵、每个 3 个初值、22182 个精确断言；18 条轨迹均至 `t=64` |
| 跨模块一致性 | 8 组积分噪声/加权抽样配对，128 组互为倒数的几何响应标准化四阶配对 |

`summary.status=PASS`。这些计数重叠，不相加为独立实验数。128 步递推、图上 64 步和早期完整路径枚举实际执行；JSON 为控制大小保留抽样及训练/留出汇总，相关模型另保留全部变号/未定义时点。有限检查是实现一致性证据，报告中的全时间结论依赖对应代数或谱推导。

交付包括最终 `REPORT.md`、`summary.json`、`run_all.py`、相关/动力学/图模块代码及各自结果 JSON、相关与图边界证明文档、动力学研究内交叉审查和展示图。核心实验依赖标准库和现有生产模块，未修改生产代码；绘图可用 `python experiments/brc_expanded_types_20261002_fca717/run_all.py --no-plot` 跳过。展示图不是精确核验来源。

父执行已将 13 个文件保存于上述不可变 commit 并验证；源码及结果的 SHA-256 在 summary 中。既有两轮证据与本轮新单元均保留；此代任务书绑定完整报告入口与精确计数，不自行制造正式 Result/Driver 接受。

## 3. Research value to preserve

不同机制揭示只观察低阶状态或一条衰减曲线时丢失的信息。独立对称加权和的精确关系 `gamma4=-2/N_eff`、条件状态与闭包阶数、相关谱和边界归一化是可带入后续具体模型检验的候选结构；它们各自有明确输入与适用范围。非线性闭包失效、最终增长、条件周期和不存在的矩同样是应保留的成果，不以正例数量替代解释。

## 4. Success, kill, and return criteria

本次有限扩展已经完成并归档。完成条件包括：各类型参考与近似对象清楚；实际有限运行和必要代数/谱推导分层；统一记录指标但不混同它们；负例、变号、未定义项与截断边界完整保留；计数遵从 summary 且不把控制和同机制实现伪装成独立实验。研究内检查与审查不等于正式 Driver 接受。

Kill/no-go 条件仍保留：将闭包假设当精确真值、把均值系数代替随机系数而不注明、把加权累积当有限窗口、把相关创新当 iid、把条件存活分布当无条件质量、把有限尺寸混合当无限域空间幂律、把 signed amplitude 当 positive mass、以截断矩替代不存在的原矩，均不能支持对应强结论。不能删去失败或重跑已有类型来提高成功数。

返回与接续：从本轮不可变报告和 summary 恢复最强已验证前沿，可审阅适用范围和研究内证据；不自动继续无限验证，也不默认重跑前两轮或本轮已完成单元。只有实际新模型、观测数据、一般非线性/波动 PDE、无限图或真实空间机制等具体信息缺口明确后，才据用户范围另行开展有界研究。登记与有限验证均不授予 N0、物理规律、正式 CLAIM、Driver 裁定或数学接受。
