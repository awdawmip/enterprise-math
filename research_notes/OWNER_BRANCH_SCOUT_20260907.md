# Owner 数学分支侦察：整数联合实现优先，路径顺序监测其次

状态：`DERIVED_SCOUT / LOCAL_EXACT_EVIDENCE / NOT_FOUNDATION / NO_OFFICIAL_TASK_OR_CLAIM`。
日期：2026-09-07。辅助代理：`/root/branch_scout`。
本地源 HEAD：`b9adbb13adb158901c84bcb678d67a1ec63aafc4`；全局协议复用父 owner 已同步的 canonical `ccd838a220b00ad44a7f5375fffeee8aa6afaaa0`，以 `git show` 读取，未把旧 KB 工作树当 canonical。

## Owner 可直接采用的选择

**第一优先：完整 BRC histogram 的联合整数实现，不能用空间质量有理解代替。** 本轮已构造并完整证明：X6 二值网格上，全部二十张 raw 三轴表每个地址都要求一个权重为 1 的分支时，空间质量有理可行，完整单位权重 histogram 不可实现；把每个地址改为两个或三个单位分支则可实现。通过 BRC 替代相加，这一均匀族的完整整数实现谱为 `{0}∪{2,3,4,…}`。

**第二优先：声明 native path 的顺序观察后，先与有限监测器取乘积，再做 BRC port 消元。** 已用“曾出现相邻原生反向步”的 14 状态监测器给出具体消费问题与精确反例；不再把 length/count/histogram/valuation 作为新 port 工具的卖点。

**park：另立 sheaf/cohomology 顶层工具。** 当前 local-to-global 例子可直接回流 owner 的联合可行性工具和已有 T2/T8；它是负例生成器，暂没有独立工具族的必要性。

这里不重开七/八支点唯一性证明；新问题的输入是各纤维的完整 exact-weight histogram，待实现的是具有整数分支重数的总体。原先质量恢复器本来只承诺空间聚合质量，本轮结果是接口范围分离，不是对旧承诺的反例。

## 1. 原生结构与 BRC 的实际使用

当前基础来自：

- `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md`；
- `definitions/ENTERPRISE_X6_CENTERED_THREE_AXIS_SLICE_REBASE_20260905.md`；
- `definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json`（父 owner 的既定边界）；
- `definitions/ENTERPRISE_BRC_UNIVERSAL_HISTOGRAM_FOUNDATION_20260903.md`；
- `research_notes/X6_SIGNED_PATH_BRC_AND_PRIMITIVE_LINE_V17_20260905.md`；
- 已有 `OWNER_TOOL_FRONTIER_20260907.md` 的去重结论。

空间对象是选定 Cell anchor 后的 signed `Z^6` 坐标；十二个有向 primitive steps 是 `±E_i`。二值集 `{0,1}^6` 是这些合法原生 Cell 中的有限研究总体，不定义新空间维度。三轴观察必须保留 raw address，或 `(can3, common depth)`，不把 min-zero 观察当 raw 投影。本文固定一个时间切片，不增加时间演化公理；P000 的六空间轴加一时间、120° 原生正角与 signed primitives 不进入质疑。

对有限分支总体，每个分支有空间坐标 `x`、正有理权重 `q`，同位置同权重允许多重分支。令 `n_q(x)∈N_0` 是这些分支的重数。观察为

`H_{S,a} = Σ_q c_{S,a,q}[q]`, 其中 `c_{S,a,q}=Σ_{x_S=a} n_q(x)`。

这是实际复用 WBRC-T36 的 `N[Q_{>0}^×]` carrier，而非给普通质量表改名。其 total-mass projection 是

`m_{S,a}=Σ_q q c_{S,a,q}`。

完整 histogram 与这一投影的求逆问题不同。尤其正有理**权重**可以是分数，不意味着某个固定权重的**分支重数**可以是分数。素数赋值坐标编码的是 q，不能把缺失的整数系数恢复出来。

## 2. 分支 A：代数统计与正交阵——真正尚未覆盖的 typed bridge

### A1. 精确的逐权重分层化

给定有限支持的二十张完整 histogram，只讨论这些表宣告的 raw 空间总体和无标签分支多重集。取所有表出现的有限权重集合 Q，并以空间边缘零项过滤候选 Cell。对每个 q 单独建立相同的边缘关联矩阵 M：

`M n_q = c_q,  n_q∈N_0^G`。

**命题。** 在不附加跨权重 branch label、配对、路径来源或内部状态约束的前提下，全体 histogram 可联合实现，当且仅当每个 q 的整数系统均可行。

**证明。** 必要性直接取实现总体中每个 q 的分支重数。充分性把所有 q 的整数解合并，每个 `(x,q)` 放入 `n_q(x)` 条分支；直方图逐 q 相等，因此每个观察纤维完全相等。任何未在 Q 出现的权重都不能进入实现：正分支必落入每个三轴观察中的一个纤维，那里会出现未给出的正系数。证毕。

这只恢复可实现的无标签多重集；即使整数解唯一，也不恢复已擦除的原始路径名称或时间历史。输入若只有质量表，就没有获准反推 q 分层。

### A2. 有理解存在而整数 histogram 无解的六轴证书

对每个 `S⊂{1,…,6}, |S|=3` 和每个 `a∈{0,1}^3`，令

`H_{S,a}=[1]`，即 `c_{S,a,1}=1`。

每张表总 count=8、总 mass=8。若完整 histogram 有 joint realization，则全局恰有 8 条权重为 1 的分支。由于所有坐标的非二值纤维都为零，所有分支坐标必在 `{0,1}^6`。把这 8 条分支排成 8 行 6 列二值数组；任取三列，每个二值三元组恰出现一次。这正是经典 `OA(8,6,2,3)` 的定义。

质量表却有精确有理解：64 个 Cell 各放聚合质量 `1/8`。每个三轴纤维含 8 个 Cell，所以总质量是 1。这里实际 histogram 为 `8[1/8]`，与所需 `[1]` 不相等；代码用现有 `WeightHistogram` 验证 total_mass 相同而 histogram 不同。

假设所需 8 行数组存在。把第 i 列变为 `x_i=(-1)^{bit_i}∈{±1}^8`。三列均匀性及向下求和给出：任何非空 `A⊂{1,…,6}, |A|≤3`，都有 `Σ_rows ∏_{i∈A}x_i=0`。

选择以下**恰好十二个**列函数：

`F={1,x_1,x_2,x_3,x_4,x_5,x_6,x_1x_2,x_1x_3,x_1x_4,x_1x_5,x_1x_6}`。

它们不是全部二次单项式。任意两个不同函数相乘并利用 `x_i^2=1` 后，都是非空、阶数至多 3 的字符：

- 常数与另一个函数相乘：阶数 1 或 2；
- 不同一次项相乘：阶数 2；
- `x_j` 与 `x_1x_i` 相乘：j=1 或 j=i 时降为阶数 1，否则阶数 3；
- `x_1x_i` 与 `x_1x_j`（i≠j）相乘：共同 `x_1` 消去，降为 `x_ix_j`，阶数 2。

因此这十二个长度为 8 的非零列函数两两正交、各自平方和为 8，其 Gram 矩阵是 `8 I_12`，秩为 12；但十二列在 `Q^8` 中的 Gram 秩至多 8，矛盾。完整单位 histogram 无 joint realization。

本例中的 ±1 是证明用外部代数字符值，不是正权 BRC 中的负质量，也不是对 P000 原生正交或空间维数的重新定义。计算中的“Q^8”按分支行编号，不是八维原生空间。

该论证是经典 Rao bound 的一个特例，不申报新的通用正交阵定理。正交阵和 Rao bound 的现代原始研究出处可查 [Carlet、Kiss、Nagy，Simplicity conditions for binary orthogonal arrays](https://arxiv.org/abs/2204.00835)；本报告提供自足的有限证明承担具体结论。

### A3. 最小正整数倍数恰为 2：已闭合的正例

令六个列标记为

`a_i∈{(1,0,0,0),(1,0,0,1),(1,0,1,0),(1,0,1,1),(1,1,0,0),(1,1,0,1)}⊂F_2^4`。

对每个 `u∈F_2^4` 构造一个原生 Cell 地址

`x(u)=(u·a_1,…,u·a_6)∈{0,1}^6`。

任意三列标记线性独立：没有零标记；两标记不同；三个标记的第一坐标之和为 1，故三者和不为零。因此三坐标映射 `F_2^4→F_2^3` 为满射，核大小 2。给每个 u 一个权重 1 的分支，所有三轴地址恰出现两次，即 `H_{S,a}=2[1]`。列标记整体张成 `F_2^4`，所以 16 个地址也互异；代码直接验证两件事。

λ=1 不存在，λ=2 存在，因此对于全三轴均匀 family `H_{S,a}=λ[1]`，最小正整数 λ 恰为 2。F2 的四个参数是有限生成索引，不是添加四条空间轴。

### A3b. 父 owner 提出的 Paley 补充：闭合完整均匀实现谱

父 owner 在审核上述 λ=2 后提出以 12 阶 Hadamard 阵构造 λ=3；本代理独立执行以下精确构造和验证。此段保留该协作来源，不称为独立盲发现。

在 `F_11` 上令 χ 为 Legendre character，χ(0)=0；`Q_{ij}=χ(j-i)`，i,j=0,…,10。构造

`H=[[1,1^T],[1,Q-I_11]]`。

这是经典 Paley 构造的 q=11 特例；原始来源是 [Paley，On Orthogonal Matrices，1933](https://onlinelibrary.wiley.com/doi/10.1002/sapm1933121311)。本轮没有把引文替代实例验证：代码在整数上逐项确认 H 的 144 个元素均为 ±1，且 `HH^T=H^TH=12I_12`。

从 H 选前六列，每行 r 同时放入 r 与 -r，并转换为 raw 二值地址 `(1-r_i)/2`。得到 24 个单位分支。任何奇数阶字符和为零，因为每行与其负行成对；不同两列的二阶字符和为零，因为 H 的列两两正交，配对只把原和乘 2。

对于任意选中的三列和任意期望符号 `(ε_1,ε_2,ε_3)∈{±1}^3`，对应地址指示函数为

`(1+ε_1 r_1)(1+ε_2 r_2)(1+ε_3 r_3)/8`。

在 24 行上求和，非空项全为零，常数项为 24，所以该地址恰出现 3 次。因此 `H_{S,a}=3[1]`；代码也直接确认全部 20×8 个表项等于 3，并确认本次 24 个地址互异。

现在任意整数 λ≥2 都能写作 `λ=2a+3b`，其中偶数 λ 取 `a=λ/2,b=0`，奇数 λ≥3 取 `a=(λ-3)/2,b=1`。复制 a 份 λ=2 总体和 b 份 λ=3 总体，再做 BRC alternative union，所有直方图变为 `λ[1]`。λ=0 对应空分支总体；λ=1 已被 Rao 证书排除。

故已证明该**六轴二值、所有 raw 三轴、均匀单位 histogram、允许同 Cell 分支重数**问题的完整谱：

`{λ∈N_0 : H_{S,a}=λ[1] 有 joint realization} = {0}∪{2,3,4,…}`。

这使用经典 Rao/Paley 构造和已有 BRC 替代加法，不提出新正交阵通用定理。也不宣称非均匀表、任意 alphabet、原始 branch labels 或 path histories 的分类。复合后的总体可在同一 Cell 出现多条分支，因此不能把结论改写为“所有 λ 都有 simple OA”。

### A4. 优先母问题与下一最小研究单元

**母问题。** 输入带 raw fiber 地址的有限正有理 BRC histogram，如何输出可独立核验的整数 joint realization，或一个确切的不可实现证书，同时将“有理质量可行”“每权重系数有理可行”“整数 histogram 可行”三个状态分开？

首个子单元 A2/A3/A3b 已有完整证明和可执行证据，均匀单位 family 的谱已经闭合，不因成功再重复开题。下一步应给现有恢复工具增设单独的 histogram realization consumer：先逐 q 编译 `M n_q=c_q`，再接上整数 witness 检验和可声明范围的 obstruction 检验。不得把现有质量恢复 API 的成功字段改成暗含 histogram 成功。

代数统计提供整数核、toric ideal/Markov basis 的外部工具背景。Markov basis 连接一个已非空的非负整数 fiber，与任意整数核基不等价；它也不自动证明 fiber 非空。参见 [Diaconis、Sturmfels，Algebraic algorithms for sampling from conditional distributions](https://www.math.ucdavis.edu/~deloera/MISC/LA-BIBLIO/trunk/Diaconis/Diaconis8.pdf)。本轮未编写 Markov basis 求解器，也没有将抽样或随机性加为原生语义。

**可区分产出。** 返回完整整数 n_q 并重算全部 histogram；或返回 q、具体约束、Rao/rank/同余/已核验穷举树等足以独立证明无解的证书；其余返回 `UNRESOLVED`，有理解只标为 relaxation。

**kill / close / park。**

1. 若实际 consumer 只提供质量表，就关闭其 histogram 推断入口；不能凭空指定分支权重。
2. 若生产库已经有同一输入、整数系数和精确验证语义，改为复用，不新建工具族。
3. 若下一拟议子类经证明整数 lifting 自动成立，只保留派生桥梁，关闭在该子类继续寻找“整数障碍”的任务。
4. 若提出的障碍不能拒绝 A2 的明确有理解，或不能接受 A3 的整数正例，拒绝推广该接口。
5. 求解器超时或搜索未找到解不是无解证书；停止把该算法当完备 decision procedure，保留可验证 witness 模式。

## 3. 分支 B：加权自动机——有限顺序观察的 native consumer

### B1. 一对完全具体的路径

取两个四步 native words：

`u=(+E_1,-E_1,+E_2,-E_2)`；

`v=(+E_1,+E_2,-E_1,-E_2)`。

它们都从同一 Cell anchor 回到该 anchor，length=4，每个 signed direction 的计数相同。依次给四种 signed primitive steps 权重 `2/3,3/5,5/7,7/11`；两词权重都为 `2/11`，从而单路径 histogram、CWM、每个整数矩与 prime valuations 完全相同。可是在 u 中发生相邻反向步，在 v 中没有。

这不是新 count/endpoint kernel；这些能力已在 X6 signed path 文档和 WBRC-T33–T37。新 consumer 声明要读取的是“到当前时刻是否曾出现相邻原生反向步”。本文不把这一观测强行定义为能量、物理散射或时间定律。

### B2. 最小有限监测器的现有 T6 复用

alphabet 是十二个 signed primitive steps。状态为初始状态 N、最近一步 a（12 种）、已命中 H（吸收态），共 14 态。N 读 a 后成为 a；last=a 再读 -a 后成为 H；其他步更新 last；H 永远保持 H。

初始观察只分 hit/nonhit 两类。现有 `family_future_partition_sequence` 在十二个原生步操作下给出 `2→14`，此后稳定。直接最小性也清楚：H 与其他态由空词区分；last=a 与 N、或 last=b（b≠a），由后缀 -a 区分。因此对于允许所有后缀的这一观察语言，14 个确定状态不能再合并。

### B3. 要做的工具是乘积适配，不是重复基础定理

给有限 BRC 图的每条边标注一个 primitive symbol、正有理权重，并明确 spatial endpoint/坐标位移。把图状态 i 与监测状态 r 配对。每条边 `(i→j,a,q)` 诱导

`(i,r)→(j,δ(r,a))`，权重 q。

对一族路径 P，定义 histogram 矩阵

`K(P)_{r,s}=Σ_{p∈P : δ*(r,word(p))=s} [weight(p)]`。

替代路径相加、serial paths 的 histogram 矩阵相乘；这是既有 histogram semiring 的组合应用。由此先形成 product graph，再用既有 length-aware port 公式消去内部 `(i,r)`，可以保留外部 port context 所需监测状态。若先只计算标量/histogram port，再擦除顺序，B1 已证明无法从结果补回该 observer。

输出还必须保留 port 标签、length、source provenance 的类型边界。固定实际空间端点时 displacement 本来由端点差恢复，不能假造“新增位移自由度”。监测状态属于装饰/历史观察，不是额外空间轴。有限 horizon 可提供逐系数 exact histogram；无界形式幂级数的存在不等于有限运行时或收敛结论。

加权自动机、行为等价与语言等价是现成数学，参见 [Bonchi 等，A coalgebraic perspective on linear weighted automata](https://ir.cwi.nl/pub/18069)。本轮保留其作为 T0+T6+现有 port 的 consumer；不用 field 上带负系数的最小线性表示替换正权 BRC carrier。

**第二母问题。** 给定一组明确有限 native path monitors，怎样编译最小可组合的 BRC port observation，并输出“先乘积后消元”与逐词枚举相符的证书？若 consumer 只读旧 histogram，就关闭扩展；若允许 future 直接访问被消去的 hidden state，撤销原 port lease；若声称压缩却没有可分词例或状态节省证据，则仅保留标准适配，不申报新数学机制。

## 4. 分支 C：局部到整体与 sheaf 语言——应回流而非另立

另一个精确例子说明：连所有 overlap 的完整单位 histogram 都一致，仍不能保证 global realization。

只让前四个原生坐标取 0/1，后两坐标固定 0。对于全选自前四轴的三轴表，在偶校验四个地址各放一个单位分支。对于含两个活动坐标的表，在四个二值地址各放一个单位分支；对于只含一个活动坐标的表，在两个地址各放两个单位分支。每张表总 count 都为 4。

任意两张表的 overlap 都一致：在两个活动坐标上都是均匀四表，在一个活动坐标上两值各 count=2，空活动 overlap 总 count=4。代码精确完成 `C(20,2)=190` 个 overlap 检查。

但一个 global branch 必须同时满足前四轴的四条“任意三个坐标 xor=0”约束。相减得四坐标相等，再代回得到它们全为 0。因此允许 global support 只有原点；这不可能满足例如三轴 `(1,2,3)` 地址 `(0,1,1)` 要有一个分支的要求。此例甚至没有非负**质量**实现，和 A2 的“质量可行而整数 histogram 不可行”形成真正不同的两层障碍。

这种 local family 是否存在 global section 的观点有现成 sheaf/measurement-cover 语言；[Abramsky、Brandenburger，The Sheaf-Theoretic Structure Of Non-Locality and Contextuality](https://arxiv.org/abs/1102.0264) 提供一般形式。本例只用有限坐标表和正分支，不声称测量实验、量子非局域或 P000 物理机制。

**处置：`COMPOSE_APPLIED / PARK_NEW_FAMILY`。** 将该例作为 owner 当前可行性恢复的输入检查/反例，不另造 cohomology 工具。若未来出现一个明确巨大观测 cover，且局部证书能证明比完整求解更有用，再提出真实复杂度问题；仅换成 sheaf 术语不构成能力增量。

## 5. 已做的去重与可复用接口

先读取具体 X6 / BRC / 既有 owner 范围，再运行当前 `tools/enterprise_toolbox.py coverage` 的三个 query：

1. `noncommutative ordered path word weighted automata Hankel signature`；
2. `marginal fiber integer Markov toric contingency`；
3. `sheaf compatibility marginal local global cohomology gluing`。

coverage 有候选不等于已执行。进一步读取对应 exact APIs 和 hard boundaries；关键词排序会混入无关 BRC factoring 方法，未把这些匹配算成有覆盖。另在 method addenda 和 production source 中有限检索 `orthogonal array / Rao bound / histogram realizability / integer marginal`，未找到所需整数 joint histogram consumer。这是本轮经检索接口的能力缺口判断，不是全历史仓库的“不存在”证明。

| 现有能力 | 准确接口/来源 | 本轮复用状态及边界 |
|---|---|---|
| exact histogram、serial product | `WeightHistogram.from_weights`, `histogram_serial`, `.total_mass`; `src/enterprise_math/brc_histogram.py` | `REUSE_EXECUTED`；q 的整数重数不可降为 rational |
| count、moment、valuation、length port | WBRC-T33–T37；`brc_moment_transfer.py` 的 `moment_transition_matrix`, `moment_walk_series_coefficients`, `moment_port_kernel_at_z` | `REUSE_APPLIED` 于范围判定；不是新缺口，未再次运行 port benchmark |
| 有限未来操作安全最粗细化 | `family_future_partition_sequence`, `apply_word`, `class_count`; `src/enterprise_math/operation_quotient.py` | `REUSE_EXECUTED`，14 态监测器；不推为无限状态终止 theorem |
| E001 finite operator-word equivalence | `material_word_signature`, `material_words_equivalent`; `material_word_quotient.py` | `NOT_APPLICABLE` 于具体 signed X6 word histogram；它针对有限幅度确定算子表，不能只凭 word 名称当覆盖 |
| relation observer signatures | `relation_observation_signature_map`, `quotient_is_relation_observation_safe`; `relation_observable_signature.py` | `NOT_APPLICABLE` 于整数 completion：实现可执行，但其 powerset/source 语义不做整数 histogram completion |
| local/global obstruction、typed circuit | T2/T3/T8；当前 owner raw-table adapter 与 mass recovery | `COMPOSE_APPLIED` 于 C 的回流定位；没有另开 sheaf family |
| holonomy / weighted rational gauge | T9 与 `brc_rational_holonomy.py` | `NOT_APPLICABLE` 于 A 的整数实现障碍；q=1 的所有 valuation 已零，仍有联合障碍 |

A 的建议分类是现有 T0/T8 的 consumer extension；B 的建议分类是 T0/T6 + port composition。两者都不自动建立新顶层工具族，更不自动取得 Foundation status。

## 6. 精确计算与可恢复状态

验证文件：`experiments/owner_branch_scout_20260907.py`。

命令：

```powershell
python -X utf8 experiments/owner_branch_scout_20260907.py
```

已成功执行。验证内容：

- 64 个 `1/8` 质量的全部 20×8 三轴 mass entries 恰为 1；实际 `8[1/8]` 与所需 `[1]` 的 histogram 不同。
- Rao 字符集的 66 对积支持大小：16 对为 1、30 对为 2、20 对为 3；没有错误引用一般 degree-4 消失。
- 明确的 16 个整数单位分支使全部 20×8 三轴 entries 恰为 2。
- Paley H 的 row/column Gram 都严格为 `12I`；24 行构造使全部 20×8 entries 恰为 3；额外对 λ=2,…,20 真实组合总体并重算所有边缘。完整无限 λ 谱由 `2a+3b` 的一般证明承担，不由有限 spot checks 承担。
- 两 native words 的 histogram 都为 `[2/11]`；反向相邻观察分别 true/false；T6 细化阶段为 `[2,14]`。
- 第三分支全部 190 对 overlap 均一致，但 global support join 只含原点且不能满足指定非零项。

计算验证 witness 和有限逐对条件；A2 的普遍不可实现由上文 rank 矛盾证明承担，不能写成“穷举软件证明不存在 OA”。未修改 production library/registry，未提交或 remote 操作，未发布正式任务、CLAIM、review。

父 owner 下一动作应先独立审核 A2/A3 和输入类型，再决定是否把整数 histogram consumer 作为优先工作包。上述研究成果可供 owner 合并到既有研究分支；global durable writeback 由父 owner 统一处理，当前记为 `GLOBAL_KNOWLEDGE_WRITEBACK_PENDING`。

Global-Knowledge-Sync: main@ccd838a / GLOBAL_KNOWLEDGE_V1
