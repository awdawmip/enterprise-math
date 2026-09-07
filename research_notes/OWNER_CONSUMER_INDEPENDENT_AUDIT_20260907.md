# Owner 独立审计：原生路径监测与 signed X6 算术谱

状态：`PASS_WITH_STATED_SCOPE / LOCAL_RESEARCH_AUDIT / NOT_OFFICIAL_REVIEW`。
Owner：`EM-DVR-01E1D9`。本文件记录一般证明的复核及独立程序检查，不创建正式 task、claim、工具族或 Foundation 采纳。

## 路径观察的完整合同

复核 `experiments/owner_path_monitor_20260907/path_monitor.py`、测试及 README。
输入为有限图、节点的 raw 六轴 signed 坐标、逐边校验的十二种原生一步、正有理边权、端口标签与有限长度界。
不同 routing 标签可以位于同一 Cell；不能因此合并状态。路径长度不是额外声明的物理时间。

十四个监测状态的充分性直接来自最近一步与已经命中的状态；必要性可在原始词上证明：
HIT 与其他状态由空后缀区分；last=a 与任何其他非命中状态由后缀 −a 区分。
独立脚本不调用监测器转移，检查全部91对状态都有空或一步的区分后缀。作者另外真实复用现有 T6 得到 `2→14`。

每条非空端口到端口路径按端口访问时刻唯一切分为正长度 excursion；末段切分给出
`K_0=I, K_n=sum_(l=1..n) K_(n-l) E_l`。边界必须同时匹配 port 与 monitor。
正长度保证固定总长度的切分有限。现有 histogram serial/recoalesce 分别计入每个路径组合与替代分支，
没有把 equal-weight branches 误收为单一加和权重。闭路和相同端点并不能消除内部词的观察信息。

曾发现的接口风险已修复：公开 `SeriesResult` 容器可被任意构造，所以 `COMPLETE` 本身不是证书。
当前独立 `verify_port_series` 绑定原图、raw frame、ordered ports、horizon，重新显式枚举路径并直接扫描词。
验证后的 `verified_series` 是本次枚举所得的冻结快照。结果严格区分 VERIFIED、REJECTED、UNVERIFIED；
预算耗尽和未实现独立 first-return 核验的 EXCURSIONS 均不通过。输入中的运行时预算元数据和 witnesses 不在核验范围内。

Owner 运行作者17项测试全部通过，并增加了两种接口检查：

- 将三条权重 `{1,1/2,1/2}` 的路径直方图改为 `{1,3/4,1/4}`，CWM 的 count、total、dominant 全不变，独立 verifier 仍拒绝。
- 对三张图作四种 signed 轴标签变换及 anchor 平移，共12例；逐项变换所有 monitor blocks 与重新计算完全相同，旧 frame 的结果则被拒绝。

这些是有限实现和观测边界检查，不证明无限路径收敛、性能上界、物理旋转律或完整 provenance 重建。

## 算术谱的一般推导

复核 `OWNER_ARITHMETIC_FRONTIER_20260907.md`、实现与作者独立 factorial census 源码。
完整总体是 `N∈N0` 的 signed X6 L1 壳层。端点的路径计数为 `N!/prod |z_i|!`；
输入包含0、1、偶数和合数半径，p 则是需要验证的素数参数。

逐位等式 `sum_i d_(i,j)+c_j=n_j+p*c_(j+1)` 配合 `c_0=c_L=0` 精确等价于壳层和约束。
Legendre 的有限数字恒等式给出赋值等于进位**数值**之和；c 的取值0至5由六个数字的最大和归纳得到。
这排除了把 `(3,1,0)` 误记为“两次进位”的错误。末端零进位也排除了把其他半径的端点计入中心。

对同一带标签数字历史，r 个已活跃轴当前可以取任意数字；从未活跃轴中选 a 个首次非零。
因此转移系数为 `binom(6-r,a)[x^S]U_p(x)^r V_p(x)^a`。
所有相同 `(carry,r)` 的历史的续接计数相同，故可以合并；这并不声称合并后的输出还保留具体轴身份。
每个终态的非零坐标有独立正负选择，符号因子恰为 `2^r`，只乘一次；N=0 只有中心一种选择。

独立复核 signed lifting：把一个支撑大小 s 的非负六元组嵌入所有包含其支撑的轴集，
容斥系数和为 `2^s(2-1)^(6-s)=2^s`。故作者给出的 k=0..6 无符号谱组合成立，N=0 的 k=0 项不可删。
负号仅属于证明账本，生产实现实际使用正 BRC 转移。

原生路径、端点聚合后的 path-count 权重、赋值投影后的 `p^e` 权重是三种对象。
histogram recoalesce 不把两条单位分支自动改成一条权重2；赋值也不与质量相加交换。
实现只输出端点数按 `(r,e)` 的联合谱，明确遗失 endpoint labels、符号关联和 p-coprime unit。
函数结果不是面向外部伪造对象的独立证书容器，不能仅凭 dataclass 字段来验证任意给定谱。

## 独立实现检查与先例

作者的阶乘商、逐 signed endpoint 检查覆盖 N=0..10 与 p=2,3,5,7，共536980次端点/素数检查。
Owner 阅读了该 oracle 的源代码；未重复整批已通过的 census。

Owner 新脚本 `owner_consumer_audit_20260907.py` 采用另一条计算路线：
无符号 k 加数 carry 矩阵的数字系数用有界 stars-and-bars 容斥求得，随后作 k=0..6 的 signed lifting。
该 oracle 不含 active-axis 状态、不调用 BRC 乘法，也不复用生产数字系数卷积。
21个 `(N,p)` 实例的**完整谱**全部相等，包含 N=1000001；另验 N=30,p=31 的全零赋值边界。
大半径的此项证据是两种精确算法交叉校对，不冒充逐端点 census 或一般证明。
实际输出及所有受审源码 hash 在 `owner_consumer_audit_20260907.json`，运行时确认源码前后未变。

Owner 直接核对了 [Rowland, A matrix generalization of a theorem of Fine, Theorem 3](https://ericrowland.github.io/papers/A_matrix_generalization_of_a_theorem_of_Fine.pdf)。
一般 multinomial 素数赋值数字矩阵属于已有方法；本轮交付定位为当前 signed X6 与正 BRC 的明确适配及实现，未认领方法新颖性。

## 本次绑定的源码

| 文件 | SHA256 |
|---|---|
| `path_monitor.py` | `86c7e3e751f1f4817ed836b397b3779dc65bdaf0a10da71c0ee1e434150daccd` |
| `test_path_monitor.py` | `ae7b61e2988a51c9e6e301140bffd4603d4b06b5690dc407b8aa6470dbc9ccab` |
| `owner_arithmetic_20260907.py` | `71f0214cc414c9d1291facd3ec8a727989fafe1bc21e0db5001b7d5e5655a79d` |
| `OWNER_ARITHMETIC_FRONTIER_20260907.md` | `7bc15c47d2505001234f2e630b300f561ca935be5d1076c6d9fb45b839dbae88` |

运行：`python -X utf8 research_notes/owner_consumer_audit_20260907.py`。独立脚本只依赖标准库与本地已有 BRC 实现。

Driver-ID: EM-DVR-01E1D9 / CONTROL_PLANE
Global-Knowledge-Sync: main@4fa7d7d / GLOBAL_KNOWLEDGE_V1
