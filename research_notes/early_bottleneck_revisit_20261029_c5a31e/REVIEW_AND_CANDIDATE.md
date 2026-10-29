# 2026-10-29 早期研究瓶颈重访：证据矩阵、有限矩保真下界与候选后继

**状态：AUTHOR_UNREVIEWED / SOURCE-BOUND RESEARCH DRAFT / NOT FORMALLY REGISTERED / NOT CLAIMED / NOT CANONICAL。** 此件只是本轮可复核科研产物，不是 Taskbook、不可变 publication record、研究 Result 或正式状态机回执；不得拿其 Git commit 代替正式发布。发布和工作身份恢复须经原生控制面及其现行完整校验。本轮没有领取任何现有 Task，也没有借用他人 session/CLAIM/DA。

**读取钉针**：GLOBAL_KNOWLEDGE_V1 在本轮开始固定为 awdawmip/chatgpt-global-knowledge@95d63da344ef3922df6a4e3586c36fafde9aa7b1（00_BOOTSTRAP.md；OPERATING_MANUAL.md；projects/enterprise-math/00_EM_PROJECT_BOOTSTRAP.md、P000_STARTUP.json；我眼中的世界.md；BRC 优先级与科研登记协议）。Enterprise Math 科研原件固定为 awdawmip/enterprise-math@5f89b97b08580572f3bbc07f9791e2f38151e5f7；写出此草案前复核 main=919f879a4b29e686117930e148bbd19b722317f5；其间新增文件仅为其他研究活动与 BRC/D25 笔记，未涉及本篇以下被引用的旧原件或本议题任务书。两个快照不混作单一提交；全局知识索引及更新频率均未修改。

## 一、旧瓶颈的有范围结论及查重

| 早期路线/真实旧障碍 | 现已可用的经来源支持的变化 | 本轮判定及禁止的升级 |
|---|---|---|
| P018/R019 精度对象混用“精确态、商标签、集合纤维、后继运行载体”；一步精确不能自动推导合成精确。原件：research_tasks/R019_P018_PRECISION_OBJECT_SEMANTIC_REAUDIT_20260811.md。 | P023 的 composition-safe collapse、future-safe refinement、partial-operation quotient；research_method_inventory.json 有 canonical executable predictive partition / composition-safe repair。 | **表达/语义瓶颈在具体有限操作语言下已实质改善**；不等于所有无穷后继或原生物理观察自动闭合。旧泛化任务不得重发。 |
| R038 对“离散 exact world 的 π/圆是否只是读出”疑问；R059D AM/AN 的源圆弧与目标转步计数不保距。 | 原件 research_tasks/R038_DISCRETE_EXACT_WORLD_CONTINUUM_CONSTANTS_PI_READOUT_SEMANTICS_20260812.md；R059D_STAGE_AM/AN、P000 原生 X6、观测分层和 BRC 粘合已有明确类型。 | **保留反例/作用域**：有限代数运算的代数闭包和无穷离散对象的特殊常数不能混同；source Euclidean metric 不随 BRC 商自动下降为 target native metric。相关离散实验反例已有 RS-DISC-COMPAT-20261026-00..14 共 15 项正式记录，不能重复注册。 |
| 2026-09-07 BRC squarefree kernel 的固定短名单分布漂移失败。原件：research_notes/BRC_SQUAREFREE_KERNEL_COMPRESSION_NEGATIVE_20260907.md。 | 13 kernels / 98 multipliers 在训练 10,153/10,153；迁移验证分别仅 16,513/19,481（84.76%）、14,591/26,399（55.27%）。BRC_OPPORTUNISTIC_SHORTCUT_PORTFOLIO_20260907 已以完整 fallback 保留前缀。BRC_TABLE_FREE_TAIL_20260907 精确免表证书解决存储依赖但 Python 路线约慢 6–24 倍。 | **真否定结果继续有效**：固定小核库不能替代完整长扫描；免表 ≠ CPU 加速。先审查已存在的分布条件触发、完整候选回退和成本遥测，不另发一个“13核自适应”同义任务。 |
| RH squarefree-alpha 正权 Gram、固定正 α 除极点法未得到 Möbius 临界相干。 | RH_SQUAREFREE_ALPHA_GRAM_RANK_ONE_BOTTLENECK_20260908 严格否定普通 α-L2、泛 Gram 对偶及有限固定正 α 消除 ζ 零点奇性的捷径；RH_CRITICAL_ROUGH_ARITY_POSITIVE_HISTOGRAM_GAUGE_20260908 给出有限 Euler gauge、精确正直方图及 N^{o(1)} 的平方根权条件数。 | **局部表达瓶颈已解除，分析障碍没解除**：正直方图与精确保数载体成立，但 parity readout 仍是 RH-strength；禁止称此为 RH 证明或已取得正号估计。下节给出新的有限观察者保真障碍，精确限定在固定低阶线性矩读出。 |
| RH 道路 anchored cross-frequency 和 escaping horizon、以及 count-centered BRC carry。 | 已有正式 RH-ROAD-KERNEL、RH-ROAD-TAIL、RH-BRC-CARRY-CLOSURE；已有精确起点谱核、临界边界与平方函数任务书。 | 属于**既有 owner/任务**，不能将 source phase 丢失、有限壳结果或条件 Schur 估计升级为 RH，也不重复发布。 |
| 2026-10-26 离散物理兼容性（旋转、相位、传播残差及联立）。 | RS-DISC-COMPAT-20261026-00、01、04、11、14 等 publication records 状态 ACTIVE、claimable 字段为 true；2026-10-28 RS-BRC-FUTURE-FAITHFUL-INTEGRATION 已覆盖 ETH/QFT 的有界未来保真、保数与误差控制。 | **已登记而非待发现空白**；publication 的 claimable 不能证明当前无活跃 CLAIM，原生 tasks/session 在本轮故障，故不宣称活跃 owner 已排除。 |

上述“已改进”是各自精确定理/可执行接口之内的证据等级，不是统一 P000 公理接纳。旧负例被保留而非被后来的正面工具冲掉。一般工具的 Lean 记录与部分 executable checks 在来源里分别标识，本文未独立重跑整个工具链。

## 二、本轮新增精确有限结果：临界粗素因子直方图的固定有限矩线性读出下界

### 2.1 明确对象

沿用已发表的首个 cosine observer。对固定 y>=2、T>=1，令 r_y(n) 为 n 的互异素因子中 **严格大于 y** 的个数，μ(n)² 为平方自由指示量。定义非负粗因子直方图：

H_y(T,r) = sum_{1<=n<=T, μ(n)^2=1, r_y(n)=r} cos(π n/(2T)) >=0.

其 parity 观察量为 P_y(T)=sum_r (-1)^r H_y(T,r)。对任意 j>=0，定义阶矩 M_{y,j}(T)=sum_r r^j H_y(T,r)。底层 r 是算术素因子**来源/路径计数**，不是 P000 的原生六个空间方向。

只审计这一类读出：

P_y(T) ?= sum_{j=0}^m a_j(N,y) M_{y,j}(T),

其中系数允许依赖 ambient N 与固定 cutoff y，但 **不可依赖子尺度 T**，且要求在全部 1<=T<=N 上同时成立。本结论不涉及非线性、自适应 T 读出，也不排除保留完整素数 provenance 的其他表示。

### 2.2 定理（精确，数学证明；作者未受独立审查）

设 p_1<p_2<... 是依次严格大于 y 的素数，q_0=1，q_s=prod_{i=1}^s p_i。若整数 s>=1 且 2q_s<=N，则对上述所有 T<=N 的固定系数线性读出，**不可能只用前 s 个矩 M_0,...,M_{s-1} 精确恢复 P_y(T)**。

更强地，取 T_i=2q_i (0<=i<=s)，矩阵 A=(H_y(T_i,r))_{0<=i,r<=s} 为下三角，且每个对角元至少 1/sqrt(2)，所以

det(A)=prod_{i=0}^s H_y(2q_i,i) >= 2^{-(s+1)/2} >0.

**证明。** 若 r>i，平方自由 n 至少有 i+1 个大于 y 的互异素因子，故 n>=q_{i+1}=q_i*p_{i+1}>2q_i=T_i；该直方图项为空。若 r=i，则 n=q_i 是非零项，其权重 cos(π/4)=1/sqrt(2)。所有权重在 n<=T_i 时非负，于是矩阵严格下三角且对角正。

若低阶矩线性表示成立，令 Q(r)=sum_{j=0}^{s-1} a_j r^j。代入 T_i，得到 A 乘列向量 ((-1)^r-Q(r))_{0..s} 等于 0。由 det(A)>0，必须在 r=0,1,...,s 同时满足 Q(r)=(-1)^r。但 s 次有限前差作用于次数<=s-1 的多项式为 0，而 Δ^s (-1)^r|_{r=0}=(-2)^s≠0，矛盾。证毕。

该证明直接用于原 RH 首余弦权重，不需要把 w(1)=0 的端点差分错误用作单点见证，也没有用 floating-point 计算代替证明。

### 2.3 临界深度版本（经典 PNT 作为外部现成引理）

令 y_N=(log N)^2，s_N=max{s:2q_s<=N}。那么

s_N=(1+o(1)) * log N/(2 loglog N).

上界：q_s>y_N^s，故 s<=log(N/2)/log y_N。下界：由素数定理，区间 (y_N,2y_N] 中的素数个数 ~ y_N/log y_N，显著大于 log N/loglog N；任取固定 ε>0，前 s=floor((1-ε)log N/log(2y_N)) 个大于 y_N 的素数最终全落在 (y_N,2y_N]。因此 2q_s<=2(2y_N)^s<=N（充分大 N），上下夹逼即得。

所以，当 N 足够大且 y_N 固定用于全部子尺度 T<=N，任何精确的 **统一线性前缀多项式矩读出** 必须使用至少 s_N+1 = (1+o(1))log N/(2loglog N) 个阶矩（如按 0,...,m 连续储存）。这与已有 source 里的粗因子最大深度 K_N 的渐近阶一致，但绝不说明所有数据结构/算法有这个无条件信息复杂度下界。

### 2.4 小实例、有限验证与成本

以 y=3、s=3 为例，(q_0,q_1,q_2,q_3)=(1,5,35,385)，(T_0,T_1,T_2,T_3)=(2,10,70,770)；H_y(T_i,r) 依次只允许 r<=i，且 H_y(T_i,i)>=sqrt(2)/2。故任意固定的 0、1、2 阶矩线性组合都不能在 T<=770 上精确恢复 parity。

独立验证有限差分正直方图的见证：m=2 时两个非负整数向量 U=(1,3,3,1)、V=(2,0,6,0) 的 0、1、2 阶矩依次完全相同 (8,12,24)，但 Σ(-1)^r U_r=0、Σ(-1)^r V_r=8。m=5 时 U=(1,6,15,20,15,6,1)，V=(2,0,30,0,30,0,2) 的 0..5 阶矩相同，parity 分别 0 和 64。上述是通用非负直方图微型反例；它们 **不自动等于单个算术 T 的 H_y(T,r)**。本节算术定理靠 T_i 下三角阵独立成立。

验证等级：有限差分小实例已用 Python 整数精算复核；下三角与临界渐近给出符号证明，尚未独立同行审查、Lean 证明或当前工具链原生结果接纳。

成本：符号定理只需 s 个递增素数、s+1 个子尺度及 O(s^2) 数学观察表位置；实际无须枚举到 N 的整数。若选全域数值重放以校核 H 的每一格，可用 μ² 与素因子计数筛 O(N loglog N) 级预处理及 O(N) 存储；首余弦权重如要求认证须采用带误差界的实数区间计算，不能把普通 double 当 exact。保存 s+1 个 T_i 需 O(s log N) 位；素数查找成本、精确三角数值认证和 source pin 读取应分别记账，不以小规模 microcheck 推断长尺度的可计算性。

## 三、拟议后继（候选，非正式 Task；不与现存 RH 任务合并前先查重）

候选名称：**RH 临界粗素因子奇偶的非线性/尺度适配 future-safe 观察者与素数窗口误差**。

- **原问题与根源**：2026-09-08 squarefree-alpha Gram 的泛范数/固定 α 消元 no-go；同日 positive rough histogram gauge 已得到精确正直方图与临界 K_N 深度、RH 等价 parity 观察，但尚缺 parity 跨尺度**算术相干**。本轮定理又否定了一整类统一低矩线性读出，不等于推翻已有正直方图表示。
- **现在新增的工具、证据等级**：P023/T6 的有限 future-safe quotient/refinement（来源称 canonical executable）、当前有类型 BRC provenance、正直方图 prime insertion exact recursion 和有限 Euler gauge（原有精确推导）；本轮定理作者符号证明/未独立审查。无可转移的 RH-strength 均匀相干估计。
- **实质不同的目标**：在明示的“增加一组粗素数”“T -> T/p”“先汇合后继续”的有限未来语言下，求 parity 所需的 **非多项式或 T-适配的最小保真状态**，或证明明确的有限语言内低维压缩不可能；对每个源素数窗口分离 exact insertion 与连续 Buchstab–Dickman 近似的带来源残差。先给可证、可被反例杀死的有限结果，**不直接申请 RH 证明**。
- **最小实验**：先以 y=3、T<=770 执行原首余弦 H 与四个 T_i 的严格正下三角证书；再使用一对有限素数窗口和两步插入操作比较原计数、M_0..M_2、future-safe 完整 H 与候选紧缩状态，在相同现在读数、不同未来 parity 时输出最小反例；最后扩到固定 ambient N 的若干完整子尺度，给每个窗口的有符号误差与区间认证，而非只汇总绝对误差。
- **验收**：定义输入/操作/读出/保真等价与状态位长；至少一个非同义精确降维定理 **或** 对真实算术族的最小未来-失真见证；提供 N、y、素数窗口、完整字节证书、重放工具以及包括初始化/质数筛/有理或区间运算/峰值空间的完整成本；明确与 P023 普遍最小商和既有 RH road/carry任务的差异。
- **失败/撤回**：候选保数只适用于单时刻、未来一插入即破坏；把原正权 histogram 当作天然 parity contraction；只靠 generic low moments 保证所有尺度读出（本轮下界排除）；将有限采样/固定 PNT 界外推 RH；将素数标签误作 P000 六空间轴；声称经典矩下界是新基础公理。任何这些出现时保存反例并停止推广。
- **成本边界**：符号基础 O(s^2) 表述位；有限全量筛 O(N loglog N) 时间、O(N) 整数单元，直接全 T 的余弦加权求和最坏 O(N^2) 观察工作，不可混作 O(N)；更快算法必须写完整构造与额外缓存成本。若精确实数式或间接临界统一界需要不可控超多项式位/资源，归类资源障碍而非成功。禁止无上限数值扫描。

**查重风险**：RS-BRC-FUTURE-FAITHFUL-INTEGRATION-20261028 已研究一般未来保真和误差，RH-ROAD-KERNEL/TAIL 与 RH-BRC-CARRY-CLOSURE 已研究另两条相干路线。该候选只有在其“粗素因子直方图 + 固定首余弦 + 临界深度算术约束”未被现有 owner 当前 CLAIM 覆盖，且当时的 Objective、真实身份及 publication gate 全部满足时才可提交正式 task。本文不为其自发配一个旧 parent/claim，也不推定当前 owner 空闲。可先作为有明确边界的研究建议交 Driver 评估。

## 四、正式状态机阻断及原生回执

本轮在真实当前对话标识 em-20261029-bottleneck-review-c5a31e 下通过既有 private control bridge 读取：
- 原生 status：<https://github.com/awdawmip/kimi-query-bridge/issues/6629#issuecomment-6484091953>；外层 COMPLETE、内层 SUCCEEDED、enabled 包含 session_registration/claim/driver_activation 等 true。**这是控制面状态查询成功，不代表任何 Task/Result 注册或数学接纳。**
- 原生 tasks：<https://github.com/awdawmip/kimi-query-bridge/issues/6630#issuecomment-6484150522>；外层 COMPLETE、内层 FAILED，错误如下。
- 本对话自己的 session_start(RESEARCHER/TASK_RESEARCH)：<https://github.com/awdawmip/kimi-query-bridge/issues/6631#issuecomment-6484155322>；外层 COMPLETE、内层 FAILED，错误相同。

原样错误：

~~~text
UPSTREAM_CODE_REVIEW_REQUIRED: control_plane/check_current_control_authority.py, control_plane/check_post_cutover_publication_envelope.py, control_plane/check_remote_manual_publication_preflight.py, control_plane/research_startup_transport.py, control_plane/research_task_integrity_fault_isolation.py
~~~

因此本轮没有有效原生 researcher session/claim/active-owner readback，也不能走等价当前校验通过的发布流程。**没有**创建研究_taskbook / immutable publication record / READY 或可领取 Task，任何保存的 GitHub 草案、GitHub Issue、commit 或此文件都不是正式 Task 录入。远程人工绕过上述五个待审 source 文件的发布校验同样不可接受。保留现有历史真否定、任务状态和 owner 权限，不伪造成功。

建议原生修复后先重读同一 Objective 的任务及活跃 owner，必要时由当前 Driver 评估后继门，再对候选使用完整当前出版校验；若已由其他任务覆盖，只把本篇新定理消费进现有范围，**不增加重复 Task**。

## 五、来源钉针（研究范围）

下列相对路径均指 enterprise-math@5f89b97b08580572f3bbc07f9791e2f38151e5f7，除非另有注明：

- research_notes/RH_SQUAREFREE_ALPHA_GRAM_RANK_ONE_BOTTLENECK_20260908.md
- research_notes/RH_CRITICAL_ROUGH_ARITY_POSITIVE_HISTOGRAM_GAUGE_20260908.md
- research_notes/RH_PROVENANCE_HILBERT_GREEN_SUBPOWER_BOUND_20260908.md
- research_notes/RH_MOBIUS_PATH_GAUGE_AND_BOUNDARY_OBSERVER_20260908.md
- research_notes/BRC_SQUAREFREE_KERNEL_COMPRESSION_NEGATIVE_20260907.md
- research_notes/BRC_OPPORTUNISTIC_SHORTCUT_PORTFOLIO_20260907.md
- research_notes/BRC_TABLE_FREE_TAIL_20260907.md
- research_tasks/R019_P018_PRECISION_OBJECT_SEMANTIC_REAUDIT_20260811.md
- research_tasks/R038_DISCRETE_EXACT_WORLD_CONTINUUM_CONSTANTS_PI_READOUT_SEMANTICS_20260812.md
- research_tasks/R059D_STAGE_AM_CANONICAL_BRC_CIRCLE_COLLAPSE_NONISOMETRY_20260817.md
- research_tasks/R059D_STAGE_AN_BRC_PUSHFORWARD_MEASURE_PERSISTENT_DISTORTION_20260817.md
- research_task_records/RS-DISC-COMPAT-20261026-00/TP2-20EC0ABD05545665A8D3.json
- research_tasks/RS-BRC-FUTURE-FAITHFUL-INTEGRATION-20261028.md
- research_task_records/RS-P017-GLOBAL-CAPACITY/TP2-2DD714C3A1DF150154B0.json（SUPERSEDED）
- research_task_records/RS-P024-HIGHER-ACTION-PRECISION/TP2-BFC9EADB566435BB8415.json（SUPERSEDED）
- docs/RESEARCH_TASK_PUBLICATION_PROTOCOL.md、research_task_publication_contract_v2.json、research_taskbook_contract.json

**结论**：已获得新的、严格限定的首余弦正直方图线性有限矩读出下界；并确认部分旧表达问题已被后来的工具化研究推进，部分真负结果仍保持。候选学科方向只进入草案，不在原生控制面阻断时制造假“正式任务”。
