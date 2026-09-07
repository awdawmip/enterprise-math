# 进取数论 owner 持续研究纲领

Owner / Driver: `EM-DVR-01E1D9`。当前用户直接授权：制定方向、充分利用子代理多方向同时推进、处理报错、完善研究架构并研发原生工具。

本文件是持续 owner 工作与证据地图，不替代仓库已有权限合同，不是正式任务发布、CLAIM、Working Truth 或 Foundation 采纳记录。用户的持续研究目标保持开放；下文首轮闭合只指有限子单元，不表示整个目标完成。

源快照：`ef1893382eb1dcfcd773e19882569e9ff072a8ee`。
当前 GLOBAL_KNOWLEDGE 读快照：`4fa7d7d0c19a5e80a681b33c8ee2ab643ce97563`。较早报告中的 `ccd838a` 是当时的来源记录，不回写为新租约。
研究分支：`research/em-owner-20260907`。

## 决策

首轮主攻**六轴联合观察的信息保留与可恢复证书**。该主线已有精确恢复、稳定性、含噪拟合和整数 histogram 实现结果。当前 owner 组合已扩展到**算术谱、原生通道几何、路径观察、旧研究纠错**；不把所有代理长期绑定在同一边缘表问题上。

各方向以能证明、能反证、能独立核验的有限单元推进。允许已有方法的原生适配，但明确先例，不靠改名制造新理论。角色随真实缺口轮换；一个方向闭合后先比较新问题价值，避免自动续开同义工作。

现有 Perfect Prime、RH、Hodge 的有界历史证据已整理到 `OWNER_PRIOR_RESEARCH_MAP_20260907.md`，其中明确区分历史可见与当前 native 入边未核实。本轮未读取完整实时协调事件，不重新领取这些线路，也不宣称其 live ownership。旧计算未重跑；阅读触发的 RH 定义域错误另立独立勘误证据。

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

当前实际轮换：`exact_solver` 从证书、加权分类转几何及 RH 分析纠错；`stability_research` 从稳定性转算术谱及三条历史线路的证据地图；`branch_scout` 从整数实现转路径工具，并独立审核加权分类、几何和 RH 勘误。Owner 自行重建关键证明、检查消费接口、实现第二条精确 oracle，并负责索引与源持久化。清洁 FREE 上下文的新增尝试曾遇到运行时 agent thread limit；复用的三名辅助都保留 `ANCHOR_EXPOSED`，不冒充 CLEAN FREE。

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
- SymPy 1.14.0 的等式 LP 返回错误答案：独立审核复现，原表验证拦截。当前恢复已改为精确消元候选加标准有理 Phase I，所有 primal/Farkas 都对原方程独立核验；求解器返回状态不作为数学权威。
- 路径结果的公开 `COMPLETE` 标签可被伪造：新增绑定原始 graph/frame/ports/horizon 的独立显式词枚举 verifier，预算耗尽返回 UNVERIFIED，不能通过便捷读出获得证书。
- 旧 RH 能量积分把 sigma 的范围写得过宽：原 P2 在零处为非零常数，sigma>=2 必发散；另立勘误并补齐无限求和的条件，保留历史源码 hash。

## 持续推进检查点：证书、稳定性、整数直方图

首轮结束后用户的 owner 目标始终开放。以下工作由新的确切缺口触发，未把“前一单元通过”自动当成续题理由：

1. 原非负求解器在已知可行输入上不能恢复，已用标准 exact Phase-I+Bland 补全，并把 primal/dual 绑定全部原方程；旧21支点失败例现在确实恢复。见 `OWNER_RECOVERY_CERTIFICATE_UPGRADE_20260907.md` 与独立 `OWNER_FEASIBILITY_INDEPENDENT_AUDIT_20260907.md`。
2. 原七支点结论只处理零误差。完整切片归纳现给出 `||μ−ν||1 ≤ (111/20) Σ_20 ||M_Iμ−M_Iν||1`，μ≤7空间支点、ν任意有限非负；常数不依赖候选规模或最小质量。两份独立证明审计及精确验证已完成，见 `OWNER_X6_STABILITY_20260907.md`、`OWNER_STABILITY_INDEPENDENT_AUDIT_20260907.md`。后续三活动轴 parity 差把下界提高到1，当前最佳常数只夹在 `[1,111/20]`，未声称最优。
3. 完整 BRC histogram 带有整数分支重数，质量有理解不能替代。二值六轴、全部三轴、每纤维同一 histogram 的逐权重实现谱为 `λ=0 或 λ≥2`；λ1的Rao阻碍与λ2/3的明确构造闭合该族。现有BRC消费者已分层、生成witness、回表并核验Rao证书，见 `OWNER_BRANCH_SCOUT_20260907.md` 及 `histogram_realization.py`。一般整数表尚未分类。
4. 路径顺序 consumer 已完成：十二 signed primitive steps 的“曾出现相邻反向步”观察需要14态，真实复用T6细化 `2→14`。图×监测器先组合，再作正长度 excursion 和匹配监测边界的端口拼接；17项测试及 Owner 独立词/直方图/坐标变换检查通过。见 `experiments/owner_path_monitor_20260907/README.md`。长度/count/histogram 算术沿用旧工具，不另称新 family。
5. 含噪预算拟合接口已接到同一有理可行性求解器：声明有限D和stacked残差预算η，成功返回非负质量及实际BRC残差；失败证书只覆盖该D/预算。可附带 `111(ε+η_actual)/20` 条件界，未知真分布≤7与真实噪声ε的前提不会被程序冒充为已验证事实。9项回归与48个独立预算边界检查通过，见 `noisy_recovery.py`、`OWNER_NOISY_INTERFACE_INDEPENDENT_AUDIT_20260907.md`。

源研究 checkpoint 保存到 owner 研究分支，控制修复保存到独立维护分支。控制分支已有26项检查通过，但还有旧 frozen publication 缺少实质章节的基线故障，不能通过改检查器或填空式别名掩盖。源持久化、数学审核、main 集成是不同状态；持续研究不等待无关 CI 故障自动消失。

## 多方向检查点与当前证据

| 方向 | 本轮实质结果 | 独立检查与边界 |
|---|---|---|
| 加权组合结构 | 零三轴边缘数组若恰八正点，必为八负点、等幅四比特 parity 结构；额外物理轴仅是常量、重复或互补类型 | `OWNER_WEIGHTED_TRADE_FRONTIER_20260907.md` 与独立 audit；58种归一化列结构、3360种六轴嵌入。关闭八正点删轻点路线，未求得一般最优稳定常数 |
| 原生数论 | `N∈N0` 全 signed X6 壳层的最短路径计数，按素数赋值 e 与非零轴数 r 精确统计 | `OWNER_ARITHMETIC_FRONTIER_20260907.md`；42个 carry/active 状态实际复用 BRC。作者完整小域 census 与 Owner 无符号矩阵/lifting oracle 交叉通过。Rowland 矩阵方法明确为 prior art；端点标签与单位部分未保留 |
| 通道几何 | 正双边逆、列归一化、全S6协变排除跨通道混合；显式混合例的两序路径通道差8/25、分支数5与21，其可逆线性商最多一维总质量 | `OWNER_GEOMETRY_FRONTIER_20260907.md` 与独立 audit；C6通道与12 signed 操作分型，附加传递不冒充 beta 标架。矩阵恒等不等于微观 BRC 可逆 |
| 路径观察工具 | 反向步监测、有限端口组合、原始词独立 verifier | `OWNER_CONSUMER_INDEPENDENT_AUDIT_20260907.md`；91对状态的区分后缀、12个 signed frame/anchor 变换，CWM相同而histogram不同的篡改被拒绝 |
| 旧研究整理及纠错 | PP系数/HCM0接口、Hodge异常投影器、RH精确尾界均与其未闭合父问题分开；发现并纠正 RH 能量域及交换次序 | `OWNER_PRIOR_RESEARCH_MAP_20260907.md` 与 `OWNER_RH_ENERGY_DOMAIN_AUDIT_20260907.md`。原能量正确域为每个 `.5<sigma<2`；绝对双和仅在 `1<sigma<2`；判据不是 RH 证明 |

后续有界接入找到历史地图未展开的较晚证据：`RH_LOG3_N8_ARB_POSITIVITY_CERTIFICATE_20260906.md`
及 `scripts/rh_log3_n8_arb_certificate.py` 已记录同一四分支 N=8、32维子空间的 cutoff-free 完整 Weil Gram 正定证书。
所以旧笔记的“同一对角块尚需频率区间积分”不能继续当成当前缺口。该已有结果仅覆盖 full cross、eta=1，
不覆盖 prime+Cauchy reference、eta<1；也不覆盖 Galerkin complement、整个 H_log3 或 RH。
准确五文件来源、环境和复用合同见 `OWNER_RH_FINITE_CERTIFICATE_INTAKE_20260907.md`。

当前新的最小执行单元已经冻结为 **N=8、eta=9/10 的 prime+Cauchy reference 严格惯性包**。
旧浮点 q=8 只作待检候选。复用已有 cutoff-free A、D 构建器，补 Cauchy cross 的严格球；
再由独立 Fraction 工具核验有理区间族的惯性。原始32个 basis 标签、两个 pole 通道及 cross 定义保留。
exact_solver负责严格生产者，stability_research负责独立有理区间惯性器，branch_scout审复用/尾界合同，Owner负责环境、原数学审查与集成。
该单元尚未生成新 reference 证书，运行时和精度不能凭旧结果推测；资源不足必须给 UNDETERMINED。

## 研究架构：把证明接到真实消费者

每个工作包至少固定四件事：原生总体与类型、允许观察/未来操作、准确成功或反例目标、可重放证据。
Observer 丢失的标签、质量、联合关系必须逐项声明。不能因一个量可重构就删除其关系身份，也不能因为数值或有限检查吻合就升级一般定理。

| 当前实验入口 | 可接续用途 | 不应越过的返回边界 |
|---|---|---|
| `observer_certificate.py` / `recovery.py` | labeled X6 正分支 → raw表、fiber histograms、空间聚合质量恢复 | 原标签/历史不由空间恢复结果逆推出；唯一性依赖≤7支点定理 |
| `exact_feasibility.py` / `noisy_recovery.py` | 有理线性约束、有限候选D及噪声预算 → 原方程可核验证书 | 资源不足不是不可行，真噪声/稀疏性是外部前提 |
| `histogram_realization.py` | 逐权重整数分支实现、二值统一纤维谱及Rao证书 | 有理解不能替代整数实现；一般表仍未分类 |
| `path_monitor.py` | 真实原生步图 → 有限监测端口系数及独立验证 | 有限 horizon、指定操作语言；验证不扩展到未知隐藏访问 |
| `owner_arithmetic_20260907.py` | 全 signed 壳层 → `(r,e)` 端点谱及 `p^e` BRC histogram | path-count 聚合是明确观察步骤；赋值谱丢失 coprime unit 与端点标签 |

这些是非 canonical consumer 入口；正式工具登记仍要遵循现有 reuse/coverage 与发布协议。理论笔记、候选发现脚本、独立审计和真实输出分开保存，hash 绑定实际受审版本。既有审核文件的来源不会因为新的 checkpoint 而被改写。

## 后续方向与退出条件（持续组合）

| 方向 | 真实信息缺口 | 继续条件 | 退出 / 回流 |
|---|---|---|---|
| 联合观察稳定性 | 一般 `p(f)<=7` 的最优常数仍在 `[1,111/20]` | 新上界证明或不属于已关闭删点路线的下界见证 | 八正点、至少九负点已被排除，不重跑该搜索 |
| 观察方式设计 | 哪些受限分布需要哪一组高阶联合观察 | 明确总体、成本和 future-operation family | 单个四轴标量区分一对例子，不冒充全局最小修复 |
| X6 路径工具组合 | 空间位移、非交换分支词和后续操作同时保留的具体消费接口 | 先有具体问题并复查已存在的 T33–T37 等接口 | 只新增长度/count/histogram 的方向已被既有工具覆盖，关闭重复立项 |
| 算术观察 | 赋值e不能区分C=4与12的p-coprime unit | 真正需要联合单位谱的consumer先查 factorial-unit 先例 | 当前完整赋值谱已闭合，不自动扩为同一数字算法续篇 |
| 几何观察 | 具体混合例已区分空间相同、通道不同、微观分支不同 | 需要新声明的通道操作或观察合同才扩展 | 不从几何邻接推断物理动力学，不重复置换中心化子分类 |
| 旧研究消费 | 同一N8 full-cross eta1已有Arb证书；reference eta9/10的Cauchy条目与负惯性包尚在构建；PP/Hodge父命题尚未闭合 | 按 `OWNER_RH_FINITE_CERTIFICATE_INTAKE_20260907.md` 复用已有A/D，核验准确reference输入 | 不重造已有对角积分器，不把有限惯性当无限空间或父猜想结论 |
| 自由发现 | 由独立研究员另起 primitive 问题 | 干净上下文才宣称 CLEAN | 不能从已暴露目录的会话重新声称 clean blind |

上述是研究组合中的候选方向，不构成 READY/CLAIMABLE 任务。把方向转成正式任务前，写出 exact gap、成功/反例、kill condition、替代路线和 V2 publication；不能靠“上阶段通过”自动续开。

## 分支侦察来源

- [Ghorbani et al., On the volumes and affine types of trades](https://arxiv.org/abs/1810.02296)：最小 trade 体积与本轮二值奇偶结构相关；有理权重的支点数结论由本地完整归纳证明承担。
- [Mohri, Semiring Frameworks and Algorithms for Shortest-Distance Problems](https://cs.nyu.edu/~mohri/pub/jalc.pdf)：路径替代/串联的半环框架是已有工具背景。
- [Bonchi et al., A coalgebraic perspective on linear weighted automata](https://ir.cwi.nl/pub/18069)：weighted bisimulation 与 weighted language equivalence 的区别可用于后续观察契约设计，尚未导入本轮结论。
- [Stanley, Algebraic Combinatorics](https://math.mit.edu/~rstan/algcomb/index.html)：路径与转移矩阵的后续学习入口，未用作本轮定理的证据。

Driver-ID: EM-DVR-01E1D9 / CONTROL_PLANE
Global-Knowledge-Sync: main@4fa7d7d / GLOBAL_KNOWLEDGE_V1
