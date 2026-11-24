# POWER 进展与前景评估：综合判断及 88 号模块核查

Progress-Event-ID: `power-progress-audit-20261124-74b386d`
At: `2026-11-24`（用户时区 Asia/Hong_Kong）
Role: `RESEARCH_DRIVER / EM-DVR-5F0F6F`
Session: `MCP-a4fbce76b4de4144bb1372a11575058b`
Authority provenance: `DA-9939899B5A3A045BEEE5`
Scope: 用户询问 POWER 进展、突破与前景；对已发布材料作来源审阅和短反例复核，不领取四个研究任务，不提交正式 Result/Review 或数学接纳。

## 一、结论

POWER 有值得继续投入的局部数学成果和工程原型。最近的分解模块扩展很快，但在本次核查版本中，尚无可确认的通用大整数分解、有效多候选 Coppersmith 方法或 RSA-280 分解突破。实际问题包括未实现的根恢复、错误的格关系、删除真分支的启发式截断，以及不包含真因子的参数窗口；它们比单纯缺少更多测试更具体。

最有把握的近期研究价值在任务相关精度、未来安全商与增量维护、稀疏抗擦除观测。整数分解方向仍可研究明确数族、双素数截面分离、保持真根的共同表示和完整成本；现有反例只约束本次实现和对应普遍性主张，不排除其他有效构造或有用的有限预算探测。

## 二、版本与证据

- POWER 主干在 2026-11-24 13:27:42 UTC 的已读快照：`74b386de5f1ca8dcc662935f563c438e1cfeee7e`；13:42:55 UTC 再核主干，仍为同一提交。
- 相对建议 PR 所用的 `049bc552ec90820094ecfdb4013d71cb1a668386`，比较结果为 2 个提交、22 个改动文件；主要新增 86–89 的实现、专论、probe 和结果文件。85 作为直接前序一起核查。
- 79/82/83/84 实现 blob 未变；复用前次的具体诊断，但按真实调用图判断是否进入新路径。85 默认用 Cohen 整数 LLL，84 仅被实例化，不能把 84 的问题当成本轮全部现象的原因。
- 中控任务状态以附录各回执实际时间与 Source 为准。读取时规范 Source 为 `7abe4ae0b36be17894c8bb74f7d0710ec5c8c50b`；保存前主干已前进至 `67f2bf68053dbfa78d5ebb51b133fe8a1f5c6098`，该提交另属 Riesel 观察器进展。没有把跨时间读取包装成全仓原子实时快照。
- 本轮实际运行短原生验证或原函数 AST 提取验证；未跑 RSA-280 长分解，未在同硬件复现所有计时，也未声明全仓 pytest 通过。
- 原始输出在 `EVIDENCE.json`，复核脚本和来源映射见 `REPRODUCTION.md`。

## 三、最近工程进展的实际强度

| 模块 | 可以确认的内容 | 决定评价的缺口 |
|---|---|---|
| 85 五阶段管线 | 已有构基、Cohen LLL、resultant、Sturm 调用链与阶段遥测 | 五个成功样本都在普通 Fermat 首个中心直接返回；格链保根与真候选覆盖没有成立 |
| 86 共享多候选格 | 共享一次预处理，循环处理 5,000 个候选并记录速度 | `r_x=0`；无非零商根恢复；canonical 矩阵完全对角，额外维数没有提供联合关系 |
| 87 二进提升 | 奇偶递推正确，节点与剪枝计数可复算 | 每状态仍有两个后继；固定 beam 会删真解；RSA 样例的半差界小于该输入任何真实因子对半差 |
| 88 联合加速 | 位移构基、分阶段计时、候选循环、消元代码存在 | 候选解码输出被丢弃；所谓 slack 仅由维数公式生成；通用早停规则有小反例 |
| 89 查表与字节提升 | QR 表确实保留真平方，有限窗口扫描可复算 | 实际为标量顺序查表；字节初始化遗漏交叉项，扩展只取 16/256，存在真解丢失 |

其中 86 的真候选复例：N=503×509，M=16，残基 (7,13)，商根 (31,31)，界 X=Y=32。16D/24D 都通过距离门限却返回无因子。87 的真分支复例：N=1009×2003，真实半差 497 符合默认界，第 10 位两条真方向均被宽度 128 的 beam 删除。89 的第一字节甚至在 N=7×11 时漏掉两条真方向。完整推导和原源码链接见附录。

这些复核同时保留了阳性对照：86 输入本身已含因子时初始 gcd 可成功；89 QR 表全部正确，字节方法在 257×263 上能返回正确因子。局部实现缺陷与有效子组件分别记录。

## 四、88：5,000 个候选计时与因子恢复之间没有连通

固定源码：[co_optimized_asymptotic_algebraic_synthesizer.py](https://github.com/awdawmip/power/blob/74b386de5f1ca8dcc662935f563c438e1cfeee7e/src/power/weapons/co_optimized_asymptotic_algebraic_synthesizer.py)，Git blob `217aa66a9a4fd255333a9d49241ce89a4e39a121`。

### 4.1 候选循环丢弃解码残差

`benchmark_joint_pipeline` 用首个 p_cand/q_cand 构建并约化一个矩阵。随后逐个构造候选 target，调用解码后仅保留 `aborted`，以 `_, _, aborted` 丢弃残差和距离。消元阶段又只使用最初的 reduced[0:2]；最终恢复用最初 p_cand。候选流没有接入候选对应的根提取。[源码 L288–365](https://github.com/awdawmip/power/blob/74b386de5f1ca8dcc662935f563c438e1cfeee7e/src/power/weapons/co_optimized_asymptotic_algebraic_synthesizer.py#L288-L365)。

因此“处理 5,000 个候选”描述的是 5,000 次数值调用，不是为这些候选完成有效因子恢复。Probe 的 RSA 各档记录也没有保存 `is_success` 或 factors。[probe](https://github.com/awdawmip/power/blob/74b386de5f1ca8dcc662935f563c438e1cfeee7e/scripts/test_co_optimized_joint_synthesis_probe.py)。

### 4.2 构基仍遗漏原关系项

原因子关系是

\[
(p_0+Mx)(q_0+My)-N=M^2xy+Mq_0x+Mp_0y+(p_0q_0-N).
\]

新构基只使用 xy 系数和常数；线性项没有进入对应格行。部分带权系数被分别模 N 压缩，未给出合法的整数行变换和列权重整除保证，之后 `row_to_y` 通过右移丢低位来除权重。这没有修复前序 82 的保根关系。[构基 L165–207、还原 L329–348](https://github.com/awdawmip/power/blob/74b386de5f1ca8dcc662935f563c438e1cfeee7e/src/power/weapons/co_optimized_asymptotic_algebraic_synthesizer.py#L165-L207)。

### 4.3 通用提前拒绝规则有零距离反例

对单位格基 I_5，target=(2,0,0,0,0)，允许平方距离界 1。目标本身就是格向量 2e_1，真实最近距离为 0。

原函数倒序处理 e_5,e_4,e_3,e_2 后，尚未处理能完全消除残差的 e_1，却因当前前四坐标平方和为 4>1 而提前退出。实际返回 `aborted=True`，残差仍为 (2,0,0,0,0)。这说明“当前残差大”不是剩余基向量处理后的误差下界。[原函数 L210–237](https://github.com/awdawmip/power/blob/74b386de5f1ca8dcc662935f563c438e1cfeee7e/src/power/weapons/co_optimized_asymptotic_algebraic_synthesizer.py#L210-L237)。

`check_synth.py` 运行的是原静态方法的未修改函数体，只移除静态绑定装饰并跳过无关 package 初始化；源文件 Git blob 精确匹配。本次 RSA 存档三个维数的 early_aborts 都为 0，故没有把这个反例误报成该存档 RSA 运行的实际删解原因。

### 4.4 slack 随维数改善是公式结果

代码使用

\[
\alpha_d=\tfrac12(1-1/\sqrt d),\quad
\mathrm{slack}=b_N\alpha_d-(b_N/2-b_M).
\]

该数值与实际短向量、候选质量、独立多项式关系或根恢复无关。对 b_N=928、M=2^64（bit_length=65），16/24/32 维分别为 −51、−29.713603、−17.024387；本轮精确按原表达复现。单凭这列趋近零不能推断“接近 RSA 分解阈值”。[源码 L370–372](https://github.com/awdawmip/power/blob/74b386de5f1ca8dcc662935f563c438e1cfeee7e/src/power/weapons/co_optimized_asymptotic_algebraic_synthesizer.py#L370-L372)。

### 4.5 遥测应按其实际执行内容解释

存档 [joint_co_optimization_probe_results.json](https://github.com/awdawmip/power/blob/74b386de5f1ca8dcc662935f563c438e1cfeee7e/docs/joint_co_optimization_probe_results.json) 和 [co_optimized_asymptotic_algebraic_synthesizer_results.json](https://github.com/awdawmip/power/blob/74b386de5f1ca8dcc662935f563c438e1cfeee7e/docs/co_optimized_asymptotic_algebraic_synthesizer_results.json) 表明：

| 维数 | 候选数 | 构基+约化+解码等总时长 | 提前拒绝数 | 所存因子证书 |
|---|---:|---:|---:|---|
| 16 | 5,000 | 约 1.073 秒 | 0 | 未保存 |
| 24 | 5,000 | 约 2.438 秒 | 0 | 未保存 |
| 32 | 5,000 | 约 4.504 秒 | 0 | 未保存 |

“五阶段”中的 F2 消元只做独立小基准，未在这个 pipeline 内调用；没有给出针对所用 RSA 候选、与因子存在性相连的使用证明。文稿“提前淘汰超过80%”与本次存档零 early_aborts 不一致。

直接 Bezout 的 1,000 次计时为 23.1919 ms，对照 Sylvester 为 21.5501 ms；速度比被 probe 以 max(1.0, ratio) 截为 1.0。这个计时没有展示加速。对二次齐次填充的公式还存在全局符号差；在二次对二次且仅判断消元根时，该非零符号不改变根集，不能把符号本身夸大为主要失败原因。

## 五、较扎实的已有成果

### 5.1 任务相关精度：有明确对象与可复算的压缩差异

等奇数宽度 w、同步单位平移、h<w 的 n 坐标模型中，完整坐标观察需要 (h+1)^n 类，坐标和需要 binomial(h+n,n) 类，ANY/ALL 越界观察各需要 h+1 类。前轮已遍历 w=5,h=4,n=6 的全部 15,625 状态，得到 15,625 / 210 / 5 / 5 个类。

来源：[precision_task_observable.py](https://github.com/awdawmip/power/blob/049bc552ec90820094ecfdb4013d71cb1a668386/src/power/precision_task_observable.py)；[已发布方向说明](https://github.com/awdawmip/enterprise-math/blob/5367901ecfd320a880a332772238b89997d44005/driver_routes/POWER_RESEARCH_DIRECTIONS_20261124.md)。这是具体模型下“任务改变所需保留状态”的真实结果，尚不是新近发布的近似编译与动态维护任务的答案，也未直接证明某个生产引擎的收益。

### 5.2 稀疏抗擦除观测：精确跨度与候选构造

对声明的非自适应相等关系观察模型、周期上限 H 和最多 e 个已知位置被删除，已有最小跨度公式 A_min(H,e)=e+max_{1≤r≤H} r ceil((e+1)/r)。0≤e<H 时为 e+max(H,2e)。低擦除范围还有达到最小跨度的稀疏构造，H=4096,e=2 的185点对应完整区间4099点。

来源：[原始候选报告](https://github.com/awdawmip/enterprise-math/blob/6b40284e808edb8bf74ff07ffa9efaf02bcfd021/research_notes/power_span_erasures_20260923_16243626C61A/REPORT.md)。报告有自包含论证和历史有限验证，状态为 `RESEARCH_CANDIDATE_NOT_ADMITTED`。这可作为后续最少点数、高擦除、保护核权衡的底座；跨度最优与采样位置数最优是不同问题。

### 5.3 QR/CRT 前缀：已有实际接纳的限定成果

`RS-FACTOR-BLIND-QR-CRT-PREFIX-INDEX-COST` 有冻结 Result `RR-79DED8D7DF67EEB5FB57` 和 ACCEPTED 审查 `DR-A1CDCEE97F3295286EE6`。实际成果包括精确 rank/select/有序枚举、逐项成本账本及“完整物化所需列表并扫描全部前缀幸存者”模型的近线性总成本下界。具体来源、前提与排除范围见附录。

这给后续研究明确了需要突破的表示/遍历瓶颈，仍允许压缩、共享、摊销、不同查询接口、额外约束或提前成功等路线。

## 六、前景与建议投入方向

以下是结合已核证据作出的研究判断，不是成功概率、既定交付期限或新任务命令。

| 方向 | 当前基础 | 最有价值的增量 |
|---|---|---|
| 任务精度与增量未来安全商 | 对象、精确参照与反例完整，已有跨库相同实现 | 在任务/动作/证据改变时，给出可执行更新、信息补入与误差/成本保证 |
| 稀疏抗擦除观察 | 精确跨度候选定理和稀疏构造可用 | 最少位置数常数差距、高擦除范围、保护核与跨度权衡 |
| QR/CRT 查询与压缩 | 精确接口、已接纳的完整成本边界 | 避免完整列表物化的表示、共享结构或有用的受限查询；按实际成本判断 |
| 认证格与多候选共享 | 工程原型和精确小反例已给出修正目标 | 保持根关系的共同子格/表示、合法转换、真实非零根恢复与等功能总成本优势 |
| Frobenius 双截面分离 | 系数/粗化/gcd 原型已有 | 对明确数族证明一侧为零另一侧非零的可构造条件，并计入环宽、种子和构造成本 |
| 通用大整数分解 / RSA-280 | 本轮未发现有效的全链成功证据 | 需要新的有效数学约束或相同输出条件下的可复算完整计算收益；当前不具备时间表依据 |

分解方向的局部工程优化仍可能有用。例如 QR 预表可作为有限预算探测的一环，即使不保证所有输入成功，只要实际探测成本、漏解代价及后续收益清楚，仍可形成独立工程交付。要称为新的分解能力，最有说服力的证据是对明确输入族输出非平凡因子并验乘，且新机制提供了普通首步 Fermat/直接 gcd 没有的增量。

外部比较可复用成熟工具作基准：CADO-NFS 官方文档将其定义为包含各阶段的完整 NFS 实现；Nguyen–Stehlé 的原始论文区分普通浮点 LLL 的不稳定性与有证明保证的 L2 方法。这些用于选择完整成本与认证比较对象，不据此推断 POWER 的其他新机制不可能。

- https://cado-nfs.gitlabpages.inria.fr/
- https://perso.ens-lyon.fr/damien.stehle/FPLLL.html

## 七、已发布事项的状态

此前中控四项新问题已在 `5367901ecfd320a880a332772238b89997d44005` 发布；本轮的实际任务回执及观察边界见状态附录。出版与待分配状态不计为研究进展。

POWER [PR #1](https://github.com/awdawmip/power/pull/1) 本轮读取仍为 OPEN、merged=false，head `11591d8e6f2a9625ea529333299661e297497595`。本轮没有合并、改写 PR 或冒领这些任务。当前材料为 Driver 来源审阅与证据保存，不是四项任务的 Result，也不改变其科研接纳状态。


---

以下附录保留各只读复核工作包的范围与时间。文中的本地缓存路径是此次复核工作区相对路径，复现映射见 REPRODUCTION.md。保存本报告不构成对其中研究候选的正式接纳。


---

# 附录 A：85/86 源码复核

# POWER 当前进展核查：85 号管线与 86 号多候选格

## 核查范围与判断

本次固定源码为 `awdawmip/power@74b386de5f1ca8dcc662935f563c438e1cfeee7e`。审阅了 85、86 的实现、专论、测试和对应 JSON；对 86 做了小型含真候选复核，对 85 的五个已报告成功样本做了整数算术核验。未重跑 RSA-280 长实验，也未审计 87–89。79、82、83、84 的核心实现与前轮固定版本相同，按 blob 核对后复用此前结论。

**判断：这两项新增内容体现了把组件接起来、尝试共享候选预处理的工程进展；尚不能据此认定产生了新的有效多候选 Coppersmith 方法、格分解突破或 RSA-280 的可行攻击。决定性问题来自实际数学关系和恢复分支，不只是证据数量不足。**

| 内容 | 当前可确认的进展 | 不能由现有证据推出的结论 |
|---|---|---|
| 85 五阶段管线 | 有矩阵组装、Cohen LLL、resultant、Sturm 的调用及阶段计时 | 已打通有效 CRT 筛选到因子恢复；已证明保根；553.92 ms 是 RSA-280 分解时间 |
| 85 小规模成功记录 | 五个 40、51、63、71、79 位样本确实有正确因子 | 格链有效，或相对普通近平方分解有新优势；五例全部第一步 Fermat 即可命中 |
| 86 多候选流 | 复用一次构基/约化，并循环处理候选、记录吞吐 | 能从候选残基恢复非零商根；当前成功分支只会重复输入候选的直接 gcd |
| 86 16D/24D 结构 | 创建这些尺寸的矩阵并计时 | 利用了相应维数的联合代数关系；实际 canonical 矩阵对角化，目标仅前三坐标非零 |
| 86 数千倍 speedup | JSON 报告了每秒约 4,366 / 7,764 个候选的算术处理 | 等成功率、等正确性、含恢复及认证总成本的分解加速 |

## 1. 86：非零商根恢复尚未实现

最关键的控制流在 [86 源码 L136–166](https://github.com/awdawmip/power/blob/74b386de5f1ca8dcc662935f563c438e1cfeee7e/src/power/weapons/simultaneous_coppersmith_multi_candidate_lattice.py#L136-L166)：

1. 每个候选先做 `gcd(p_cand, n)`，有非平凡因子就退出。
2. 解码距离通过门限后，将 `r_x` **写死为 0**。
3. 随后做 `gcd(p_cand + r_x*m_sieve, n)`，与第一步完全相同。

因此，在不抛异常并正常返回的执行中，`is_success=True` 只可能因为输入的某个 `p_cand` 本身已经有非平凡 gcd；格解码不会产生新的成功。导入了 resultant 和 Sturm，并构造 isolator，但扫描方法没有调用它们。专论声称的自动代数根提取尚不存在于这个版本中。[86 源码 L26–29、L60–64](https://github.com/awdawmip/power/blob/74b386de5f1ca8dcc662935f563c438e1cfeee7e/src/power/weapons/simultaneous_coppersmith_multi_candidate_lattice.py#L26-L64)；[专论 L44–57](https://github.com/awdawmip/power/blob/74b386de5f1ca8dcc662935f563c438e1cfeee7e/docs/86_SIMULTANEOUS_COPPERSMITH_MULTI_CANDIDATE_LATTICE_MONOGRAPH.md#L44-L57)。

### 已复算的含真候选例

取：

\[
N=503\cdot509=256027,\quad M=16,\quad (p_0,q_0)=(7,13).
\]

真实商根是：

\[
(x_0,y_0)=(31,31),\qquad
(7+16\cdot31)(13+16\cdot31)=N.
\]

将界限设为 \(X=Y=32\)，真实根严格在界内。

| 输入/配置 | 距离门限 | 实际返回 |
|---|---|---|
| 唯一真候选 (7,13)，16D，商位数 5 | 13 < 14，通过 | `is_success=False, factors=None` |
| 同一真候选，24D，商位数 5 | 13 < 14，通过 | `is_success=False, factors=None` |
| 仓库测试原样的四个候选、默认界限 | 共扫描 4 个 | `is_success=False, factors=None` |
| 直接给 (503,509)，作为阳性对照 | 初始 gcd 已命中 | `is_success=True, factors=(503,509)` |

这比“尚未在大数成功”更具体：**一个已知在界内、通过距离门限的真残基，也没有接入有效根恢复。** 仓库测试确实含真残基，但只要求返回类型、扫描数或成功、吞吐量和非零 slack，不要求找到真因子。[测试 L29–46](https://github.com/awdawmip/power/blob/74b386de5f1ca8dcc662935f563c438e1cfeee7e/tests/test_simultaneous_coppersmith_multi_candidate_lattice.py#L29-L46)。

本地复核文件：

- `progress_review/lattice/probe_85_86.py`
- `progress_review/lattice/probe_85_86_results.json`

复核直接加载固定源码函数/类的未修改 AST；仅略过仓库初始化和未使用的导入，不构造扫描方法从不读取的 Sturm 对象。实际 Mahler 构基、Cohen LLL 和 86 扫描方法均运行原代码，没有替换数值算法或返回值。

## 2. 86：当前并没有构成所称的联合高维根关系

### 2.1 canonical 格退化为对角格

86 预处理调用 82 的构基器时固定 `p_cand=q_cand=0`。[86 L66–86](https://github.com/awdawmip/power/blob/74b386de5f1ca8dcc662935f563c438e1cfeee7e/src/power/weapons/simultaneous_coppersmith_multi_candidate_lattice.py#L66-L86)。

82 的唯一非对角写入是：

\[
(W X^{i-1}Y^{j-1})\bmod N,\qquad W=p_0q_0-N.
\]

此时 \(W=-N\)，所有非对角元都是 0；其余内容都在对角线上。[82 L101–138](https://github.com/awdawmip/power/blob/74b386de5f1ca8dcc662935f563c438e1cfeee7e/src/power/weapons/padic_mahler_measure_hyperbolic_lattice.py#L101-L138)。

所以当前 Cohen 约化只会重排正交的坐标行。候选 target 又仅在前三坐标非零，后续新增的 13/21/29 个坐标全部没有参与候选关系。[86 L144–153](https://github.com/awdawmip/power/blob/74b386de5f1ca8dcc662935f563c438e1cfeee7e/src/power/weapons/simultaneous_coppersmith_multi_candidate_lattice.py#L144-L153)。

上述真候选例中，16D 和 24D 均得到：

\[
(91,6656,3584,0,\ldots,0).
\]

复算同时确认两档构基的非对角非零元数量都是 0，约化后只是原矩阵各行的排列。这里维数增加改变的是循环和计时规模，尚没有表现为更强的候选约束。每个候选还被独立处理，代码没有把不同候选之间的代数约束合并成一个联合系统。

### 2.2 所述 affine translation 定理不成立

专论把多项式分解：

\[
f_{p_0,q_0}=f_{0,0}+q_0Mx+p_0My+p_0q_0
\]

直接提升为格的等式：

\[
\mathcal L(p_0,q_0)=\mathcal L_0+\mathbf w(p_0,q_0).
\]

这一步没有成立。由生成元取整数线性组合得到的格一定含 0；非平凡平移陪集通常不含 0。若 \(\mathbf w\in\mathcal L_0\)，平移又只是原格本身，无法据此表达一般候选格的变化。[专论 L36–45](https://github.com/awdawmip/power/blob/74b386de5f1ca8dcc662935f563c438e1cfeee7e/docs/86_SIMULTANEOUS_COPPERSMITH_MULTI_CANDIDATE_LATTICE_MONOGRAPH.md#L36-L45)。

与当前实现对应的最小证据：取 \(N=77,M=5,X=Y=4,p_0=2,q_0=1\)。canonical 格第一坐标只能是 77 的倍数；文档/代码的 defect 向量第一坐标为 \(-75\)（采用分解中的另一约定则为 2），两者都不属于这一坐标子群。因此平移陪集不含 0，而候选矩阵生成的格含 0，两者不可能相等。

**合理研究方向仍然存在**：不同候选可能共享某个子格、预条件器或可认证的转换。需要明确表示共同部分、候选变化部分及根保持映射，不能由“主要系数相同”直接推成“整个格是一个固定平移”。

### 2.3 Babai 与速度声明的范围

函数直接对原始约化行依次作投影，没有使用 Gram–Schmidt 正交向量；`dp / norm_sq` 还是 Python 浮点除法。它不能作为一般非正交格的认证 nearest-plane 实现。在目前恰好对角的 canonical 格上，这一点不改变上述退化结论。[86 L88–104](https://github.com/awdawmip/power/blob/74b386de5f1ca8dcc662935f563c438e1cfeee7e/src/power/weapons/simultaneous_coppersmith_multi_candidate_lattice.py#L88-L104)。

结果文件记录：

- 16D：5,000 个候选，解码 643.98 ms，预处理 89.70 ms，speedup 4,138.31。
- 24D：5,000 个候选，解码 1,145.31 ms，预处理 566.19 ms，speedup 2,326.89。

JSON 没有记录 `is_success`、因子、真实候选是否存在、命中率或根证书；slack 还分别是 −51 和约 −29.71。[86 结果 L5–27](https://github.com/awdawmip/power/blob/74b386de5f1ca8dcc662935f563c438e1cfeee7e/docs/simultaneous_coppersmith_multi_candidate_lattice_results.json#L5-L27)。

这些数字可以描述当前代码的处理耗时。它们不能表明“同一有效分解任务加速数千倍”，因为比较对象的实际功能不同，86 的非零根恢复缺失、保根关系也未成立。未在本轮相同硬件重跑计时，不对记录本身的墙钟数值真实性另作判断。

## 3. 85：确有调用链，但尚未证明完整管线有效

### 3.1 有效进展与缺失环节

85 的 resultant 和 Sturm 调用确实存在，位于 [L211–242](https://github.com/awdawmip/power/blob/74b386de5f1ca8dcc662935f563c438e1cfeee7e/src/power/weapons/grand_unified_asymptotic_algebraic_pipeline.py#L211-L242)。因此可以称为组件整合原型。

但“完整五阶段分解”的证据有以下具体缺口：

| 环节 | 当前代码实际行为 | 影响 |
|---|---|---|
| CRT 筛选 | 构造 CRT 对象，Stage 1 只选择 M 及候选默认值，没有调用该对象生成/筛选候选 | 阶段时间不含真实候选生成成本，也未展示真残基覆盖 |
| Selmer 剪枝 | 对单个 defect 求一个布尔结果，继续执行后续阶段；记录的百分比直接写成 61.66 或 100 | 该数字不是本次候选集的实测淘汰率 |
| 格构造 | 直接调用 82 Mahler 构基 | 继承遗漏线性项、加权列任意取模等保根问题 |
| 多项式还原 | 用 `row[col] // X^iY^j` | 构基破坏整除性后，整除截断会进一步改变多项式 |
| 根恢复界 | 用维数公式计算 alpha/slack | 未给出该具体矩阵、真实根、独立关系的相应证明/证书 |

对应源码：[Stage 1–2 L104–145](https://github.com/awdawmip/power/blob/74b386de5f1ca8dcc662935f563c438e1cfeee7e/src/power/weapons/grand_unified_asymptotic_algebraic_pipeline.py#L104-L145)、[构基及 reduction L147–186](https://github.com/awdawmip/power/blob/74b386de5f1ca8dcc662935f563c438e1cfeee7e/src/power/weapons/grand_unified_asymptotic_algebraic_pipeline.py#L147-L186)、[除权重 L195–209](https://github.com/awdawmip/power/blob/74b386de5f1ca8dcc662935f563c438e1cfeee7e/src/power/weapons/grand_unified_asymptotic_algebraic_pipeline.py#L195-L209)、[固定剪枝值 L246–269](https://github.com/awdawmip/power/blob/74b386de5f1ca8dcc662935f563c438e1cfeee7e/src/power/weapons/grand_unified_asymptotic_algebraic_pipeline.py#L246-L269)。

### 3.2 五个成功样本全部是第一步近平方恢复

结果 JSON 的五个成功记录均标为 `selmer_2descent_direct_recovery`。[85 结果 L3–63](https://github.com/awdawmip/power/blob/74b386de5f1ca8dcc662935f563c438e1cfeee7e/docs/grand_unified_asymptotic_algebraic_pipeline_results.json#L3-L63)。

精确算术复核令 \(a=\lceil\sqrt N\rceil\)，均有：

| 实际位数 | 因子对 | \(a^2-N\) | 第一步 \(a\pm\sqrt{a^2-N}\) |
|---|---|---|---|
| 40 | 1,000,003；1,000,033 | 225 = 15² | 直接得到报告因子 |
| 51 | 33,554,467；33,554,473 | 9 = 3² | 同上 |
| 63 | 2,147,483,647；2,147,483,659 | 36 = 6² | 同上 |
| 71 | 34,359,738,377；34,359,738,431 | 729 = 27² | 同上 |
| 79 | 549,755,813,911；549,755,813,927 | 64 = 8² | 同上 |

这是真实正确的小例分解，但样本全部是普通 Fermat 第一候选即命中的近平方数。85 的 `solve` 在 horizon 扫描成功后直接返回，不进入格链。[85 L273–293](https://github.com/awdawmip/power/blob/74b386de5f1ca8dcc662935f563c438e1cfeee7e/src/power/weapons/grand_unified_asymptotic_algebraic_pipeline.py#L273-L293)。

测试中两个 `solve` 成功断言也使用近平方例；唯一直接 `run_pipeline` 的测试虽给真残基，却只断言遥测值，不要求成功。[85 测试 L19–60](https://github.com/awdawmip/power/blob/74b386de5f1ca8dcc662935f563c438e1cfeee7e/tests/test_grand_unified_asymptotic_algebraic_pipeline.py#L19-L60)。

### 3.3 RSA-280 记录是阶段计时，不是成功分解证据

Phase 2 选择 \((\lfloor\sqrt N\rfloor\mathbin{|}1)\bmod 2^{64}\) 同时作为 p、q 的残基，并没有展示这是真实因子残基。[probe L63–79](https://github.com/awdawmip/power/blob/74b386de5f1ca8dcc662935f563c438e1cfeee7e/scripts/test_grand_unified_algebraic_pipeline_probe.py#L63-L79)。

生成 JSON 时只写维数、时间、向量范数、slack，**没有把实际的 success/factors 字段写进去**。[probe L91–105](https://github.com/awdawmip/power/blob/74b386de5f1ca8dcc662935f563c438e1cfeee7e/scripts/test_grand_unified_algebraic_pipeline_probe.py#L91-L105)。

结果中 16D/24D/32D slack 均为负，分别约 −51、−29.71、−17.02；所谓“48D_MAHLER”条目实际 `dimension=24`，因为该档名不受 82 支持而回退到 24。[85 结果 L65–125](https://github.com/awdawmip/power/blob/74b386de5f1ca8dcc662935f563c438e1cfeee7e/docs/grand_unified_asymptotic_algebraic_pipeline_results.json#L65-L125)。

所以 553.92 ms 可以表述为该输入下的 24D 阶段调用耗时，不能表述为 RSA-280 分解耗时或有效根恢复耗时。

## 4. 与上一轮 79 / 82 / 83 / 84 问题的关系

| 旧模块 | 当前 blob | 85 / 86 的实际关联 |
|---|---|---|
| 79 projected BKZ | `d56909f3ae504847e59371a0a46f6b8d7934aef5`，未变 | 两个新模块都未直接调用 79；不能把 79 的全部实现问题直接归给新路径 |
| 82 Mahler 构基 | `0a7b67542b4c6fbf0b2f7fb0258d433804b4e5d6`，未变 | 两者直接依赖。遗漏线性项、直接对带权坐标取模的保根缺口进入新路径 |
| 83 deep insertion | `00eea54e85e432e088f4b7f548123223aabf55b9`，未变 | 85 在 `use_deep_insertion=True` 时调用；本次 RSA-280 probe 明确设 False；86 不调用 |
| 84 adaptive float | `a074f16f3890b7596ff983b99b9707dd72a9fea6`，未变 | 85 仅实例化对象，实际 reduction 分支未调用；86 不调用 |

85 实际调用位置见 [L67–73](https://github.com/awdawmip/power/blob/74b386de5f1ca8dcc662935f563c438e1cfeee7e/src/power/weapons/grand_unified_asymptotic_algebraic_pipeline.py#L67-L73) 和 [L169–177](https://github.com/awdawmip/power/blob/74b386de5f1ca8dcc662935f563c438e1cfeee7e/src/power/weapons/grand_unified_asymptotic_algebraic_pipeline.py#L169-L177)。

84 的旧反例 \(\operatorname{diag}(2^{60},2^{59})\) 和由 swaps/fallbacks 拼出的 speedup 字段，在同 blob 下仍适用；但它们**不是本次 85 默认计时或 86 失败的直接原因**。[84 L129–162、L184–223](https://github.com/awdawmip/power/blob/74b386de5f1ca8dcc662935f563c438e1cfeee7e/src/power/weapons/provably_exact_adaptive_float_lll.py#L129-L223)、[84 L267–279](https://github.com/awdawmip/power/blob/74b386de5f1ca8dcc662935f563c438e1cfeee7e/src/power/weapons/provably_exact_adaptive_float_lll.py#L267-L279)。

82 的直接保根问题可由旧小例看出：\(N=77,p_0=q_0=1,M=2,X=4,Y=6\)，真商根是 (3,5)。xy 行的带权系数 96 被改成 19，常数是 1；除权重后为 \(1+(19/24)xy\)，在真根值为 \(103/8\)，不是原整系数根关系。85 再用整数除法把 \(19/24\) 截成 0，并不能修复该关系。[82 L101–138](https://github.com/awdawmip/power/blob/74b386de5f1ca8dcc662935f563c438e1cfeee7e/src/power/weapons/padic_mahler_measure_hyperbolic_lattice.py#L101-L138)。

## 5. 对突破与前景的科学评价

**当前地位：有工程原型积累，有值得研究的共享候选计算想法；在本次核查范围内，没有已经成立的新格分解突破。**

较有价值的下一步，是把“候选间存在共同结构”收窄为一个可证明、可否证的问题：在明确输入族、残基来源、根界和资源模型下，是否存在保持所有目标候选根关系的共同子格/表示，使共享预处理后的认证总成本严格优于逐候选方法。允许结果是有效构造、受限族定理、反例、不可复用边界或完整成本的负结论。

能够实质改变判断的证据包括：

- 给出从原关系 \((p_0+Mx)(q_0+My)-N\) 到每一格行、再到输出多项式的可核查保根映射；列权重、合法行变换、整除性均可验证。
- 对包含真残基且非零商根在声明界内的实例，实际提取根并乘回验证；把普通 Fermat 第一候选、直接 gcd、已知因子作为单独基线记录，避免它们替代格链成果。
- 如果主张摊销优势，比较相同有效功能、相同候选覆盖和成功条件的总成本，计入共同预处理、真实候选生成、错误候选处理、恢复、认证及回退。

这些不是预设必须采用的固定方法步骤，而是判断“新增机制是否确有数学与计算增量”的证据标准。目前没有依据估计攻破 RSA-280 的时间或给出成功概率；也不能从这几个实现反例推出整个共享格研究方向不可能。



---

# 附录 B：87/89 源码复核

# POWER 87 / 89 进展审阅

固定版本：`awdawmip/power@74b386de5f1ca8dcc662935f563c438e1cfeee7e`。仅审 87 / 89、各自结果与测试，以及 probe 中调用它们的部分。没有改源码，没有远端写入，没有运行综合器或长时分解。

## 判断

这轮有可复算的实现进展：正确的逐位乘法同余递推、保留真平方的二次剩余查表、有限扫描与分支耗时统计。**目前证据支持“筛法与搜索原型在做工程优化”，不支持“已发现可泛化的因数分解突破”。**

其中 89 的标量 QR 查表可以保留；87 的固定宽度 beam 以及 89 的字节提升均不能当作保留真解的完备筛法。尤其 87 的 RSA 剪枝样例用了一个可直接证伪的半径上界；89 的 byte 初始化还有明确代数错误和漏解。

## 1. 87：奇偶递推正确，50%筛除不等于新独立信息

```
p' = p_k + b_p 2^k,  q' = q_k + b_q 2^k,
b_p + b_q ≡ (N-p_k q_k)/2^k (mod 2).
```

对 k>=1、p_k/q_k 为奇数、当前乘积同余成立时，该等式正确，代码也正确执行。每个父状态四个扩展中留下两个，但仍是**每层分支数乘2**。对任一奇数 a mod 2^k，都存在唯一 b=N a^{-1} mod 2^k；因此仅此条件仍有 2^(k-1) 个有序残余对。它是乘法同余的逐位展开，不能把它再算作与乘法同余独立的新约束。

证据：
- [实现 94–116](https://github.com/awdawmip/power/blob/74b386de5f1ca8dcc662935f563c438e1cfeee7e/src/power/weapons/dyadic_hensel_branch_rigidity_filter.py#L94)
- [文稿代数展开 34–46](https://github.com/awdawmip/power/blob/74b386de5f1ca8dcc662935f563c438e1cfeee7e/docs/87_DYADIC_HENSEL_BRANCH_RIGIDITY_FILTER_MONOGRAPH.md#L34)

### 实际 bounded beam 会删除真解

宽度不是被上述定理证明有界，而是 [代码 121–125](https://github.com/awdawmip/power/blob/74b386de5f1ca8dcc662935f563c438e1cfeee7e/src/power/weapons/dyadic_hensel_branch_rigidity_filter.py#L121) 排序后只取前 W 条。

原生代码反例：

- N=1009×2003=2,021,027。
- 真实半差 R=497，远小于默认 R_max=65,536；所以并非半径条件不适用。
- 使用默认 W=128、默认目标深度，返回 `is_success=False`。
- 用 Python trace 观察未经修改的原函数：第10位截断前有256条；真残余方向 (979,1009)、(1009,979) 排在零基索引233与248，均被前128条截断。
- 第9位它们还在，第10位丢失，此后无法恢复。该例没有 Archimedean 剪枝，丢解完全来自 beam。

所以“只保留60/64条”的数字是受限搜索工作量，不能解释成在保留真正因子的前提下已把全空间缩到60条。[文稿 95–96](https://github.com/awdawmip/power/blob/74b386de5f1ca8dcc662935f563c438e1cfeee7e/docs/87_DYADIC_HENSEL_BRANCH_RIGIDITY_FILTER_MONOGRAPH.md#L95) 的指数空间对比没有计入这个完备性损失。

## 2. 87：RSA样例的R<=2^24前提实际不成立

[probe 64–66](https://github.com/awdawmip/power/blob/74b386de5f1ca8dcc662935f563c438e1cfeee7e/scripts/test_multi_candidate_hensel_probe.py#L64) 对928位 RSA-280 硬设 `max_fermat_radius=1 << 24`。

用库内 [RSA_280_INT](https://github.com/awdawmip/power/blob/74b386de5f1ca8dcc662935f563c438e1cfeee7e/src/power/rsa280_spec.py#L14) 可直接证明这个半径范围内根本没有整数因子对，无需知道实际因子：

设 c=ceil(sqrt(N))。任何正奇因子对都满足

```
S=(p+q)/2 >= c,
R²=S²-N >= c²-N.
```

原生大整数计算给出的 c²-N 是 **464位整数**，严格大于 (2^24)²=2^48；其平方根下取整已经是 **232位整数**。因此报告中的 Archimedean 排除并不处于一个包含真实因子解的半径条件下。

短复算与存档结果逐项相符：

| 64位提升条件 | 节点 | 奇偶剪枝 | 半径剪枝 | 剩余beam | 因子 |
|---|---:|---:|---:|---:|---|
| probe 的 R_max=2^24 | 14,253 | 7,126 | 2,288 | 60 | 无 |
| 原生默认 R_max（460位） | 14,845 | 7,422 | 0 | 64 | 无 |

存档 [结果 84–90](https://github.com/awdawmip/power/blob/74b386de5f1ca8dcc662935f563c438e1cfeee7e/docs/dyadic_hensel_branch_rigidity_filter_results.json#L84) 的计数能够复现，这是正面的可复算性；但解释必须同时带上参数与解保留条件。

## 3. 89：QR表是正确标量优化，没有实现64素数SIMD

实现为每个素数 p 预制一个 Python 整数 mask，再对每个候选 t 顺序执行：

```python
for p in self.primes:
    rem = t % p
    if not ((self._qr_masks[p] >> rem) & 1):
        return False
```

证据：[建表 54–62；筛法 64–76](https://github.com/awdawmip/power/blob/74b386de5f1ca8dcc662935f563c438e1cfeee7e/src/power/weapons/vectorized_bitmask_dyadic_sieve.py#L54)。

它没有 NumPy、数组批处理或硬件SIMD调用，也没有把64个不同素数条件放在一个64位字操作里同时判断。最大 mask 实际 **313 bits**；“64 primes”是配置数量，因早退出不是每个候选都做满64次模运算。

正面：这种查表避免重复求模幂，适合固定小模数；包含余数0，不会误拒真平方。本地检查64张表全都等于对应二次剩余集合，且 0² 到 4095² 全通过。精确数学理由比样本更强：平方 t 在每个 p 下必属建表集合，mod8也属于0、1、4。

需要收窄 [文稿 15–27](https://github.com/awdawmip/power/blob/74b386de5f1ca8dcc662935f563c438e1cfeee7e/docs/89_VECTORIZED_BITMASK_DYADIC_SIEVE_MONOGRAPH.md#L15) 和源码开头关于 SIMD / O(1) byte extensions 的称谓。真实成果是“标量预计算表筛”，其速度价值需要相同候选与输出口径的基线比较。

## 4. 89：byte提升没有遍历256个扩展，并有首字节错误

### 4.1 实际只试16种，直接省去大多数真分支

[114行](https://github.com/awdawmip/power/blob/74b386de5f1ca8dcc662935f563c438e1cfeee7e/src/power/weapons/vectorized_bitmask_dyadic_sieve.py#L114) 是 `for bp in range(16)`，不是文稿中的0..255。后续每个 p 字节的高4位都被限制成0。这不是把256条等价计算向量化，而是没有搜索其中240条。随后 [136–139行](https://github.com/awdawmip/power/blob/74b386de5f1ca8dcc662935f563c438e1cfeee7e/src/power/weapons/vectorized_bitmask_dyadic_sieve.py#L136) 又进行固定宽度截断。

### 4.2 k=0时被忽略的交叉项不消失

字节公式的乘积展开包含 2^(2k) b_p b_q。要在模2^(k+8)下丢弃它，需要 k>=8。原函数却从 `prev_k=0`、`(p_curr,q_curr)=(1,1)` 开始就用线性式。[85–120行](https://github.com/awdawmip/power/blob/74b386de5f1ca8dcc662935f563c438e1cfeee7e/src/power/weapons/vectorized_bitmask_dyadic_sieve.py#L85)

独立于16种采样限制的最小反例：N=77=7×11，真实第一字节可由 b_p=6、b_q=10 得到：

```
(1+6)(1+10)=1+6+10+6×10=77.
```

算法忽略交叉项60，令 b_q=76-6=70，因此不生成(7,11)，反方向也不生成。原函数第一字节仅留下(1,77)、(13,65)，均满足乘积模256，但不包含真正因子的第一字节。也就是说末尾模乘检查阻止了错误状态混入，却不能补回已经漏掉的真状态。

原生短验证：

| p,q | N | byte lift 4字节结果 | 第一字节保留真方向 |
|---|---:|---|---|
| 7,11 | 77 | None | 否 |
| 17,19 | 323 | None | 否 |
| 503,509 | 256,027 | None | 否 |
| 1,000,003 / 1,000,033 | 1,000,036,000,099 | None | 否 |
| 257,263（对照） | 67,591 | (257,263) | 是 |

另一个小错误：N=15，2字节 native 调用返回 `(1,15)`；N=9 返回 `(1,9)`。因子命中分支只检查 p_curr>1 和 N%p_curr==0，未排除 p_curr=N。[102–104行](https://github.com/awdawmip/power/blob/74b386de5f1ca8dcc662935f563c438e1cfeee7e/src/power/weapons/vectorized_bitmask_dyadic_sieve.py#L102) 这不是有效的非平凡因数分解。

## 5. “101位极快分解”与“100%筛除”的证据口径

### 5.1 六个成功样本均为普通Fermat第一步可解的近因子族

[存档结果 5–89](https://github.com/awdawmip/power/blob/74b386de5f1ca8dcc662935f563c438e1cfeee7e/docs/vectorized_bitmask_dyadic_sieve_results.json#L5) 六个样本全部：

- candidates_tested=1；
- simd_pruned=0；
- 因子差仅为30、6、12、16、16、18；
- 首个奇偶对齐的整数中心恰好就是(p+q)/2。

本地逐个验乘并验证：不使用任何QR表、Hensel或格，普通Fermat一次平方根检验同样直接分解。因此这些成功可证明返回结果正确、近因子入口可用，不能证明对通用40–101位半素数的能力或相对已有方法的加速。

[计时从 scan 内部159行开始](https://github.com/awdawmip/power/blob/74b386de5f1ca8dcc662935f563c438e1cfeee7e/src/power/weapons/vectorized_bitmask_dyadic_sieve.py#L151)，mask预计算在构造器中；[probe34行先建engine，48行才调用scan](https://github.com/awdawmip/power/blob/74b386de5f1ca8dcc662935f563c438e1cfeee7e/scripts/test_co_optimized_joint_synthesis_probe.py#L34)。所以0.01–0.02ms不是含建表的首次调用端到端时间。复用预计算可以有价值，但必须说明摊销。

[190行](https://github.com/awdawmip/power/blob/74b386de5f1ca8dcc662935f563c438e1cfeee7e/src/power/weapons/vectorized_bitmask_dyadic_sieve.py#L189) 吞吐分母下限人为设为0.0001秒，所有单候选小样本显示10,000/s，是统计下限造成的平台，不是精确计时吞吐。

### 5.2 RSA的50,000/50,000拒绝可以复现，但没有因子输出

原生短跑完全复现候选计数与全部拒绝：`is_success=False, factors=None`。这说明这段有限近平方窗口没有通过小模筛的候选，不能外推为已排除RSA全体因子空间或已逼近真正因子。

本地50,000候选约38.6ms，存档约69.98ms；环境不同，仅可用来核验逻辑与计数，不能据此宣称倍数加速。源码没有同环境基础Fermat/已有轮筛/标量查表对照，也没有完整分解的工作量比较。

byte RSA16/32/64位的节点数33/1313/5409、beam16/64/64也全部复现，均无因子。这些小计数同时受到16选256和beam截断影响，不能称为保真解决了指数增长。

## 6. 测试覆盖与可做的下一步

现有87测试只有两组近因子成功与粗略奇偶剪枝比例。[tests87 11–33](https://github.com/awdawmip/power/blob/74b386de5f1ca8dcc662935f563c438e1cfeee7e/tests/test_dyadic_hensel_branch_rigidity_filter.py#L11)

89 byte测试对503×509使用：

```python
if factors is not None:
    assert factors[0] * factors[1] == n
assert nodes > 0
```

因此不返回因子也会通过，并没有检测真分支保留；只验乘还不能排除(1,N)。[tests89 20–27](https://github.com/awdawmip/power/blob/74b386de5f1ca8dcc662935f563c438e1cfeee7e/tests/test_vectorized_bitmask_dyadic_sieve.py#L20)

值得继续的范围：

1. 保留QR预表筛作为可基准化的基础组件；让“初始化+候选产生+筛选+验证”总成本和摊销成本都可复算。
2. 先把字节初始化、完整扩展与非平凡因子条件修正；明确区分完备候选集与限制预算的启发式beam，后者必须报告真解保留率。
3. 要把“rigidity”提升成研究结果，需要额外、可证明且不依赖未知因子的限制：它相对于乘法同余真正减少多少自由度、在哪类输入成立、证明/构造/执行总成本是多少。50%本身没有回答这些问题。
4. 基准加入不同因子差、随机平衡半素数、失效例及相同预算基线；把当前近因子成功当一类样本，不能作通用位数标尺。

这与先前提出的“联合幸存状态表示+全部成本”“明确数族上的非平凡分离条件”是一致的研究缺口；无需因新增名称和局部计时自动另开一条已解决路线。

## 本地复算材料

- `progress_review/factor/audit_checks.py`：导入原样源码的短验证；trace仅观察局部变量，不修改函数。
- `progress_review/factor/audit_checks_results.json`：全部原生输出与RSA半径证明大整数。
- `progress_review/factor/source_manifest.json`：11份源码/文稿/结果/测试的Git blob精确匹配。
- pytest启动因环境未装pytest而未运行；没有把它报告成通过。独立原生检查正常执行，完成上述结论所需验证后停止。



---

# 附录 C：任务状态与既有成果

# POWER 任务实际进展核查

观察记录更新：2026-11-24 13:39:15 UTC。本次仓库固定 Source：`awdawmip/enterprise-math@7abe4ae0b36be17894c8bb74f7d0710ec5c8c50b`。本轮是只读现状核查；未开展新研究、未运行新科学实验，未改动远端。

## 核心判断

新发布的四个任务确实登记成功，但登记与科研执行、结果冻结和审查通过是四件事。先读取原 `power-directions-verify-task-20261124-01` 至 `-04` 的耐久回执：四项均 `SUCCEEDED`，对应任务均为 `READY / NEEDS_DISPATCH`、`taskbook/unassigned`、`NO_RUNTIME_EVENT`、`claim_id=null`。它们的出版时间都是 2026-11-24 11:29:51 UTC，原回执观察时间为 11:57:18、11:58:46、12:21:23、12:22:48 UTC，原回执 Source 为 `de68b2863b6c1839ea59113a5e617b8908f5bd1c`。不能把这些旧回执直接说成报告时刻的实时事实。

固定 Source `7abe4ae0b36be17894c8bb74f7d0710ec5c8c50b` 的八个精确 `research_result_records/<task_id>` 路径（新四项和旧稀疏四项）都返回 `404 / NOT_FOUND`；这是该 Source 缺少规范 Result 目录的有限观察，不证明所有外部草稿不存在，也不替代实时 owner 状态。

与此不同，旧 QR/CRT 前缀任务有实际冻结 Result 和非作者审查记录；它是可以列出的已接受、任务范围内的实质成果。其成果是精确接口、完整成本账本和受限表示的负面边界，不能表述为已经取得一般整数分解提速。

## 有界精确状态读

新四项有界精确状态读取已全部返回；没有新建研究身份、领取任务或改变任何现有 owner。 旧任务的额外实时读不作为本报告完成前置；以下旧成果判断以已读取的固定 Source、Result 和 Review 为据。

| 任务 | 已证实的原生状态 | owner / claim 边界 | 回执观察时间（UTC） |
|---|---|---|---|
| `RS-POWER-TASK-PRECISION-COMPILER-20261124` | READY / NEEDS_DISPATCH | taskbook/unassigned; claim=None | 2026-11-24T13:38:26.422510+00:00 |
| `RS-POWER-INCREMENTAL-FUTURE-QUOTIENT-20261124` | READY / NEEDS_DISPATCH | taskbook/unassigned; claim=None | 2026-11-24T13:35:39.491744+00:00 |
| `RS-POWER-CERTIFIED-RESIDUAL-LATTICE-20261124` | READY / NEEDS_DISPATCH | taskbook/unassigned; claim=None | 2026-11-24T13:34:15.128411+00:00 |
| `RS-POWER-FROBENIUS-SECTION-SEPARATION-20261124` | READY / NEEDS_DISPATCH | taskbook/unassigned; claim=None | 2026-11-24T13:37:03.237625+00:00 |
| `RTASK-POWER-ROBUST-INTAKE-20260927` | 最新读取尚未完成 | 不从出版元数据推断实时 owner | — |
| `RTASK-POWER-ROBUST-MARK-GAP-20260927` | 最新读取尚未完成 | 不从出版元数据推断实时 owner | — |
| `RTASK-POWER-HIGH-ERASURE-SPARSE-20260927` | 最新读取尚未完成 | 不从出版元数据推断实时 owner | — |
| `RTASK-POWER-PROTECTED-CORE-TRADEOFF-20260927` | 最新读取尚未完成 | 不从出版元数据推断实时 owner | — |
| `RS-FACTOR-BLIND-QR-CRT-PREFIX-INDEX-COST` | 最新读取尚未完成 | 不从出版元数据推断实时 owner | — |

原回执与后续读均保留各自 Source 和观察时间。`execution_authorized=false` 只表示该只读回执不授予执行权；判断“当时没有领取”应依据 `NO_RUNTIME_EVENT`、空 claim 和实际状态，而不是单看这个字段。

当前原生读使用 `LATEST_AT_ADMISSION_READ_V1`，不声称全仓原子快照。认证格回执完成时 Source 仍为上述固定提交；任务精度、增量商与 Frobenius 回执完成时 `latest_source_sha` 已为 `67f2bf68053dbfa78d5ebb51b133fe8a1f5c6098`、`source_unchanged_at_completion=false`。三项的事件页均完整重验且 `issue_unchanged_at_completion=true`，但不能据此把所有 Source 文件也称为完成时完全未变。无 Result 目录的结论严格绑定本次固定提交。

新四项出版记录：

- [任务精度编译](https://github.com/awdawmip/enterprise-math/blob/7abe4ae0b36be17894c8bb74f7d0710ec5c8c50b/research_task_records/RS-POWER-TASK-PRECISION-COMPILER-20261124/TP2-D2EFEEFB3E6FCC346366.json)：P1 / HIGH，资源约束近似编译、组合误差及任务改变后的有成本升级。
- [增量未来安全商](https://github.com/awdawmip/enterprise-math/blob/7abe4ae0b36be17894c8bb74f7d0710ec5c8c50b/research_task_records/RS-POWER-INCREMENTAL-FUTURE-QUOTIENT-20261124/TP2-DD8B3B7291FF9E6FD8C0.json)：P1 / HIGH，转移、动作或观察变化后的正确拆分/合并和增量成本。
- [认证残差格](https://github.com/awdawmip/enterprise-math/blob/7abe4ae0b36be17894c8bb74f7d0710ec5c8c50b/research_task_records/RS-POWER-CERTIFIED-RESIDUAL-LATTICE-20261124/TP2-3255B42C5DCC00A62CC7.json)：P2 / HIGH，保根关系、合法压缩与完整精度认证成本。
- [Frobenius 双截面分离](https://github.com/awdawmip/enterprise-math/blob/7abe4ae0b36be17894c8bb74f7d0710ec5c8c50b/research_task_records/RS-POWER-FROBENIUS-SECTION-SEPARATION-20261124/TP2-65B32E1AB172F45CF517.json)：P2 / MEDIUM，双素数截面的非平凡分离、环宽/种子界和总成本。

上述都是待解决问题；出版记录自身明示 `PROSPECTIVE_QUESTION; NO_NEW_MATHEMATICAL_ACCEPTANCE`，不宜在用户进展报告中写成四项“新突破”。

## 稀疏抗丢失：已有候选成果与未完成续接

本轮重新读取固定原始报告：[POWER feedback X](https://github.com/awdawmip/enterprise-math/blob/6b40284e808edb8bf74ff07ffa9efaf02bcfd021/research_notes/power_span_erasures_20260923_16243626C61A/REPORT.md)。该文件 Git blob 为 `78d8456b798855bc48d3df62d07840a78da22c72`，第 7 行明示 `SELF_CONTAINED_SCOPED_PROOFS + EXECUTED_CHECKS / RESEARCH_CANDIDATE_NOT_ADMITTED`。

可报告的实际内容：

- 对非自适应固定位置、只观察精确模幂相等关系、最多删除 e 个已知位置、区分全部 1≤r≤H 并把其他阶输出为超范围的模型，报告给出目标可识别的精确 closure 条件，以及有限 prime-coarsening 失败见证（报告第 31–74 行）。
- 最小跨度公式 `A_min(H,e)=e+max_(1≤r≤H) r ceil((e+1)/r)`；0≤e<H 时化为 `e+max(H,2e)`（第 76–112 行）。这是最小跨度，尚不等于最少采样位置。
- 0≤e≤floor(H/3) 时有跨度 H+e 的无保护位置稀疏构造，其位置数上界为 `b+e+(e+1)ceil(W/b)`，其中 W=H-floor(H/3)。例如 H=4096,e=2，报告列出 185 个位置，相比完整区间 4099 个位置（第 114–154 行）。该比较不等于对优化经典求阶算法的全面优胜。
- 报告保存了 279 项历史测试通过及多个完整枚举范围，并保留反例与预算耗尽语义（第 177–205 行）。这些是旧证据，本轮没有重跑，也不算本轮新增测试或独立审查。

四个旧任务仍分别承接：候选基线纳入；低擦除区间最少位置上下界常数差距；高擦除稀疏构造；保护核和跨度/位置数/失点预算的权衡。固定 Source 未见它们的规范 Result 目录。不能因为旧报告已有自包含证明，就说这四个续接问题已全部完成。

证据边界：[旧 intake 任务书](https://github.com/awdawmip/enterprise-math/blob/7abe4ae0b36be17894c8bb74f7d0710ec5c8c50b/research_tasks/RTASK-POWER-ROBUST-INTAKE-20260927.md) 明示 `LEGACY_RESEARCH_CANDIDATE_PINNED_NOT_INDEPENDENTLY_ADMITTED`；报告也明确没有独立 Driver review、Working Truth/Foundation 或 RSA-270 运行的主张。最小跨度定理可称“有精确证明和有限验证的候选结果”，需要保留它的实际接纳状态。

## QR/CRT：已有审查接受的受限成果

精确任务：`RS-FACTOR-BLIND-QR-CRT-PREFIX-INDEX-COST`。

- [Result RR-79DED8D7DF67EEB5FB57](https://github.com/awdawmip/enterprise-math/blob/7abe4ae0b36be17894c8bb74f7d0710ec5c8c50b/research_result_records/RS-FACTOR-BLIND-QR-CRT-PREFIX-INDEX-COST/RR-79DED8D7DF67EEB5FB57.json)，Git blob `54504b876aba3f5e3112ef0c2908b8027a81c012`。冻结时间为 2026-10-13 03:18:39 UTC，原结论 `NEGATIVE_BOUNDARY`，任务范围内的四项交付齐备。
- [Review DR-A1CDCEE97F3295286EE6](https://github.com/awdawmip/enterprise-math/blob/7abe4ae0b36be17894c8bb74f7d0710ec5c8c50b/research_result_reviews/RR-79DED8D7DF67EEB5FB57/DR-A1CDCEE97F3295286EE6.json)，Git blob `397d810cef11ae645cf9ab909688276fcea9b51f`。2026-10-13 03:59:02 UTC，`ACCEPTED`、`terminal=true`、`destination_class=NONE`。
- [非作者审查全文](https://github.com/awdawmip/enterprise-math/blob/7abe4ae0b36be17894c8bb74f7d0710ec5c8c50b/driver_reviews/mcp/MCP-da1a569335fc4f3b8c01a5f878ca66fc/f061973dbd48e092e37f/CRT_PREFIX_INDEX_COST_GENUINE_NONAUTHOR_DRIVER_REVIEW.md)，Git blob `eee18265019ad3cc15b3d1ac287290777c51e511`；明确披露共享上下文、非盲来源，不把新身份本身当作独立性。

被接受的内容包括：只用公开 N 和声明的公开奇素数集合、在平方自由奇模数且 gcd(N,M)=1 的范围内，给出精确 QR/CRT 前缀 rank、zero-based select 和有序枚举；按实例计入选素数、局部剩余类、CRT、列表、排序、查询、输出和整数平方/因子验证成本；在“完整物化每个所需非平凡组列表，且检查整个前缀的全部幸存者”的表示与遍历模型下，给出统一 `L exp(-O(log L/log log L)) = L^(1-o(1))` 的规范化工作下界。审查全文第 29–45、49–67、79–81 行对应这些结论。

这个结果的价值是明确了一个看似有希望的 CRT/MITM 路线的精确能力与收费边界，防止把幸存列表、排序、预处理和验证当免费资源。它不是一般分解算法的下界，也没有排除 rank-only/select-only、避免完整列表的表示、压缩/共享/摊销/批量结构、额外谓词或提前因子成功；母目标及 S1/S2/S3 均仍开放。原任务已接受的范围应复用，不应当作未完成题再发一遍。

## 给主报告的措辞建议

可以说：“POWER 已经有具体数学对象、精确原型和部分有证明的结果；最明确的已审成果之一是 QR/CRT 前缀接口和成本边界，稀疏抗丢失方向有较完整但尚待正式纳入/独立接纳的候选工作。新发布四项目前的证据属于明确问题和任务登记；科研进度须看实际领取、冻结 Result 与审查记录。”

不能说：“四项新任务都在推进”“新任务已经产生四个突破”“185 对 4099 证明了通用求阶提速”“CRT 负面结论证明所有压缩算法无效”或“某本专论标题说明已突破一般分解”。

## 本地审计材料

`state_progress_snapshot.json` 保存每个精确目录观察、原回执摘要及最新读请求状态。`state_receipts/` 保存四个原 verify-task 回执原始结构；`state_sources/` 保存此次读取的稀疏原报告、CRT Result、Review 和审查正文。该记录是只读报告的证据缓存，不是新增研究成果或接纳动作。
