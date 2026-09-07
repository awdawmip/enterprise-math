# 进取数论 owner 持续研究纲领

Owner / Driver: `EM-DVR-01E1D9`。当前用户直接授权：制定方向、组织子代理、处理报错、完善研究架构并研发原生工具。

本文件是持续 owner 工作与证据地图，不替代仓库已有权限合同，不是正式任务发布、CLAIM、Working Truth 或 Foundation 采纳记录。用户的持续研究目标保持开放；下文首轮闭合只指有限子单元，不表示整个目标完成。

源快照：`ef1893382eb1dcfcd773e19882569e9ff072a8ee`。
GLOBAL_KNOWLEDGE：`ccd838a220b00ad44a7f5375fffeee8aa6afaaa0`。
研究分支：`research/em-owner-20260907`。

## 决策

首轮主攻**六轴联合观察的信息保留与可恢复证书**。选择理由：它同时真实调用进取坐标与 BRC，直接回答“观察中遗漏了什么、何时可以恢复、什么未来操作会暴露遗漏”，能交付证明、反例和可执行工具。不会因某个旧方向连续成功而默认续开下一阶段。

已经闭合的数学单元是 raw 三轴边缘表的七/八支点界限及其类型审计；首轮工具单元是生成盲区证书、按声明操作修复观察分区、从原始边缘表恢复空间质量的候选实验。状态见各文件的实际检查结果。

现有 Perfect Prime、RH、几何、Hodge 等跨会话研究不因本次接手而重新领取或重跑。本轮未读取完整实时协调事件，因此不宣称这些线路的当前 owner、最新进度或阻塞状态。

## 世界观与工具纪律

- 在进取数论内部按当前 P000 起点研究：六维离散空间、一维时间；六轴两两进取正交，120° 为原生正角；signed axis primitive direction 与 triadic closure 按原定义使用。
- 当前空间 Cell 中心是 `AFFINE_TORSOR(Z^6)`。零坐标是选择的 Cell anchor；三轴切片、三轴观察、三轴 min-zero 载体分别对待。
- raw 三轴坐标可以用 `(can3, common depth)` 无损表示。只留 can3 会连全局对角位移也丢失。共同深度是已有六轴空间信息，不是第七条空间轴。
- BRC 优先实际应用；明确总体、分支身份、串联/替代、观察输出、允许的未来操作及范围。保留联合关系，删除方向前要有精确证书。
- `WeightHistogram`、CWM、T6 operation-safe quotient 均直接复用。正权分布之差只用于代数证明，不把它当成原生 signed/amplitude branch 质量。
- 外部组合设计、半环自动机、线性代数提供可引用的工具；其类型转换写清，不改 P000，不把已有方法换名当原创。

## 角色分工与首轮实际运行

| 角色 | 责任 | 本轮落点 |
|---|---|---|
| Owner | 选择问题、审核证据、处理异常、决定继续或关闭 | 本文件；恢复原型；持久化与最终核验 |
| 驾驶员辅助 / 控制面整改 | 权限与当前入口核对、错误根因、最小修复 | `OWNER_CONTROL_INTAKE_20260907.md`；独立维护分支 |
| 自由研究员 | 自主出题，先冻结候选，再查先例 | `OWNER_FREE_CANDIDATE_20260907.md`；如实记载 ANCHOR_EXPOSED |
| 任务研究与独立审核 | 检查一般证明、竞争分布、程序反例 | `OWNER_INDEPENDENT_AUDIT_20260907.md` |
| 工具/定理提取、既有研究整理 | 复用判定、历史去重、可执行接口 | `OWNER_TOOL_FRONTIER_20260907.md` |
| 数学分支侦察 | 从外部原始文献寻找可迁移结构 | 本轮由 owner 承担；trade、加权自动机、半环路径 |

运行时共四个并发槽位，角色按任务轮换；角色数不冒充同时运行的代理数。以上是当前用户请求内的辅助工作包，不是未经发布的官方调度任务。任何后续正式任务仍走 V2 publication 与实际 authenticated claim 流程。

## 首轮研究结果

1. **一般证明**：非零有限数组的全部 k 轴边缘若为零，正、负支点各至少 `2^k`。于是非负空间质量分布若支持少于 `2^k`，全部 k 轴 raw 边缘唯一确定它；六轴、k=3 给出至多七支点。竞争分布可以具有任意有限支持。
2. **sharp 反例**：四轴二值矩形的八个偶校验与八个奇校验 Cell，所有二十张三轴边缘、每纤维 CWM 和完整无标签权重直方图均相同。四轴 cylinder 操作后质量为 1 与 0。
3. **操作安全**：适配器直接运行既有 T6，确认上述压缩不能承受声明的四轴 filter；在有限声明总体中，安全分区从三类细化为四类。结论只覆盖已声明操作及其组合。
4. **恢复原型**：先把两个互补三轴表连接，再以全部二十张表筛选。若源有 s 个支点，连接前至多 `s^2` 个候选，s≤7 时至多49个。精确消元、必要的自由变量非负求解后，必须通过原始 BRC 边缘重算。输出≤7支点才应用支点界限发出唯一证书。
5. **创新定位**：支点/奇偶思想与已知 trade 理论有关。本轮贡献是当前 signed X6 / common-depth / BRC 联合观察下的明确应用、可运行适配器与完整性检查，未宣称新公理或已进入 Foundation。

恢复原型只恢复空间位置及聚合质量，不恢复原标签、路径顺序、内部状态或时间历史。八支点及以上的可行输出默认不判定唯一或不唯一。通用 LP 失败可能是工具问题；仅返回失败或经验证的证书，不能推出数学无解。源码和 README 给出精确依赖与命令。

## 已处理的错误

- 全局旧工作树缺少 sync script：从已有 canonical Git 引用取出原样脚本执行，再按返回 SHA 读取协议，保留 dirty 工作树。
- Windows GBK 打印 Unicode 失败：统一本轮 Python 调用为 `-X utf8`，不归为数学 blocker。
- Driver allocation 误带 researcher dispatch 参数：改用正确角色入口，实际取得 `EM-DVR-01E1D9`，登记非阻塞。
- runtime guard 脚本入口的导入错误：实测 `python -m tools.research_runtime_guard` 可用。
- 控制 checker 仍要求旧函数调用字面量：验证新共享状态/reducer链等价后做最小修复；测试仍保证 stale owner 优先于 fresh task。
- frozen Branch 接受可变列表坐标：转为不可变 tuple，增加外部修改不影响分支的回归。
- SymPy 1.14.0 的等式 LP 返回错误答案：独立审核复现。原表验证拦截；满秩直接精确解，欠定只把自由变量不等式交给求解器并完整复核。求解器并非数学权威。

## 持续推进检查点：证书、稳定性、整数直方图

首轮结束后用户的 owner 目标始终开放。以下工作由新的确切缺口触发，未把“前一单元通过”自动当成续题理由：

1. 原非负求解器在已知可行输入上不能恢复，已用标准 exact Phase-I+Bland 补全，并把 primal/dual 绑定全部原方程；旧21支点失败例现在确实恢复。见 `OWNER_RECOVERY_CERTIFICATE_UPGRADE_20260907.md` 与独立 `OWNER_FEASIBILITY_INDEPENDENT_AUDIT_20260907.md`。
2. 原七支点结论只处理零误差。完整切片归纳现给出 `||μ−ν||1 ≤ (111/20) Σ_20 ||M_Iμ−M_Iν||1`，μ≤7空间支点、ν任意有限非负；常数不依赖候选规模或最小质量。两份独立证明审计及精确验证已完成，见 `OWNER_X6_STABILITY_20260907.md`、`OWNER_STABILITY_INDEPENDENT_AUDIT_20260907.md`。最佳常数仍只夹在 `[3/4,111/20]`。
3. 完整 BRC histogram 带有整数分支重数，质量有理解不能替代。二值六轴、全部三轴、每纤维同一 histogram 的逐权重实现谱为 `λ=0 或 λ≥2`；λ1的Rao阻碍与λ2/3的明确构造闭合该族。现有BRC消费者已分层、生成witness、回表并核验Rao证书，见 `OWNER_BRANCH_SCOUT_20260907.md` 及 `histogram_realization.py`。一般整数表尚未分类。
4. 侦察把路径顺序监测保留为下一候选：十二 signed primitive steps 的“曾出现相邻反向步”观察需要14态，已通过T6细化 `2→14`。拟组合路径图×监测器后再端口消元；单纯新增长度/count/histogram仍属重复。独立 sheaf 顶层工具路线暂 park，反例回流现有联合可行性工具。

持续安排：root负责选择及交叉审查；exact_solver补全求解后转审稳定性；stability_research证明稳定性后转审求解接入；branch_scout发现整数障碍后提取消费接口；control_driver在独立维护树处理checker与旧测试入口故障。控制修复尚不等于main已集成，也没有把其他CI故障当数学主线的阻塞条件。

5. 含噪预算拟合接口已接到同一有理可行性求解器：声明有限D和stacked残差预算η，成功返回非负质量及实际BRC残差；失败证书只覆盖该D/预算。可附带 `111(ε+η_actual)/20` 条件界，未知真分布≤7与真实噪声ε的前提不会被程序冒充为已验证事实。9项回归与48个独立预算边界检查通过，见 `noisy_recovery.py`、`OWNER_NOISY_INTERFACE_INDEPENDENT_AUDIT_20260907.md`。

源研究checkpoint保存到owner研究分支，控制修复保存到独立维护分支。它们仍为研究/维护候选，不改变Foundation状态。接下来尝试缩小稳定常数区间，并按母问题价值选择一般整数联合实现或原生路径监测的下一可判别单元。

## 后续方向与退出条件（持续组合）

| 方向 | 真实信息缺口 | 继续条件 | 退出 / 回流 |
|---|---|---|---|
| 联合观察恢复工具 | 已验证输出到更可靠通用非负可行性证书、含噪稳定性之间仍有差距 | 必须声明精确/含噪范围与可独立验证证书 | 仅数值拟合不作证明；第三方求解失败不判无解 |
| 观察方式设计 | 哪些受限分布需要哪一组高阶联合观察 | 明确总体、成本和 future-operation family | 单个四轴标量区分一对例子，不冒充全局最小修复 |
| X6 路径工具组合 | 空间位移、非交换分支词和后续操作同时保留的具体消费接口 | 先有具体问题并复查已存在的 T33–T37 等接口 | 只新增长度/count/histogram 的方向已被既有工具覆盖，关闭重复立项 |
| 自由发现 | 由独立研究员另起 primitive 问题 | 干净上下文才宣称 CLEAN | 不能从已暴露目录的会话重新声称 clean blind |

上述是研究组合中的候选方向，不构成 READY/CLAIMABLE 任务。把方向转成正式任务前，写出 exact gap、成功/反例、kill condition、替代路线和 V2 publication；不能靠“上阶段通过”自动续开。

## 分支侦察来源

- [Ghorbani et al., On the volumes and affine types of trades](https://arxiv.org/abs/1810.02296)：最小 trade 体积与本轮二值奇偶结构相关；有理权重的支点数结论由本地完整归纳证明承担。
- [Mohri, Semiring Frameworks and Algorithms for Shortest-Distance Problems](https://cs.nyu.edu/~mohri/pub/jalc.pdf)：路径替代/串联的半环框架是已有工具背景。
- [Bonchi et al., A coalgebraic perspective on linear weighted automata](https://ir.cwi.nl/pub/18069)：weighted bisimulation 与 weighted language equivalence 的区别可用于后续观察契约设计，尚未导入本轮结论。
- [Stanley, Algebraic Combinatorics](https://math.mit.edu/~rstan/algcomb/index.html)：路径与转移矩阵的后续学习入口，未用作本轮定理的证据。

Driver-ID: EM-DVR-01E1D9 / CONTROL_PLANE
Global-Knowledge-Sync: main@ccd838a / GLOBAL_KNOWLEDGE_V1
