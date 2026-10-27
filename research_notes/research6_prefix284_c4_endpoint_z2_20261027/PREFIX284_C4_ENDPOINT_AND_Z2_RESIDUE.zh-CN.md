# PREFIX-284｜三来源C4-BRC的单端点恢复与等端点Z₂残差

状态：**AUTHOR_SIDE_EXACT_PROOF / FINITE_C4_CHECK_PASS / NATIVE_DETECTOR_NOT_ESTABLISHED / NOT_ADMITTED**。本文接续 PREFIX-283，但并未复用旧核验作为本轮新增调用。模型数学不等于六维心跳世界物理法则。

## 固定规范与科学输入
- GLOBAL_KNOWLEDGE_V1：`awdawmip/chatgpt-global-knowledge@14be18c2c5017e3831777d0a1e05026303527956`，同一快照读取 `00_BOOTSTRAP.md`、`OPERATING_MANUAL.md`、P000启动投影、ACTIVE世界观及数学/代码/EM/BRC规则。
- P000原件 `projects/enterprise-math/P000_REALITY_FOUNDATION.json` Git Blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`，与启动投影字段 `canonical_blob_sha1` 一致。六个原生空间轴不是下面三条来源历史索引。
- 本轮研究输入：`awdawmip/enterprise-math@25cf910c09db04fec70f9de1a24467c06046faf3`；参考 `docs/PORTABLE_RESEARCH_PROTOCOL.md`、`docs/HEARTBEAT_BRC_ONLY_ARITHMETIC.md`、`definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json`、`definitions/HEARTBEAT_SELF_CONSISTENT_INSTANT_V0_1.json` 和 PREFIX-283。真实GitHub登录账号 `awdawmip` 对仓库具有 admin/push 权限。本轮身份 `EM-R006-P284` 仅为作者侧研究标记，另有自己的RA登记；无原生CLAIM。

## 精确问题与载体
是否仅添加**一个来源端点的正BRC质量读数**，便足以修复三来源包的全部自相关失辨？复相位相较严格正实幅值会留下什么不可观测残差？

取三个来源标签 (j=0,1,2)，幅值 (a_j\in\mathbb C)、(a_0\ne0)，保留全部**有序来源路径对**。令
\[
 Z=\sum_{j=0}^2|a_j|^2>0,\qquad
 C_r=\sum_{j=0}^{2-r}a_j\overline{a_{j+r}},\quad c_r=C_r/Z,
 \qquad p_0=|a_0|^2/Z.
\]
这是一种声明的带来源、相位信息的静态BRC观察，不是原生传播器。全局非零复倍率对 (c_1,c_2,p_0) 无影响。所谓「恢复」均指恢复相对幅值 (a_1/a_0,a_2/a_0)，整体比例和公共相位无法由归一化读数确定。

## 定理A：非奇异完整恢复
令 (r=a_1/a_0)、(t=a_2/a_0)、(v=c_1/p_0)。则有精确BRC路径对恒等式：
\[
 \boxed{t=\overline{c_2}/p_0},\qquad
 \boxed{v=\overline r+\overline t\,r}.
\]
若 \(|c_2|\ne p_0\)，等价于 \(|t|\ne1\)，便有**唯一**反演
\[
 \boxed{r=\frac{\overline v-tv}{1-|t|^2}},\qquad
 \boxed{(a_0,a_1,a_2)\sim (1,r,t)}.
\]
**证明：**按来源路径对直接展开 (c_2=p_0\bar t)、(c_1=p_0(\bar r+\bar t r))。取第二式共轭，得 \(\bar v=r+t\bar r\)；以原式消去 \(\bar r\)，得到 \(\bar v-tv=(1-|t|^2)r\)。分母非零时唯一。证毕。

## 定理B：等端点的精确Z₂双值残差
在 \(|c_2|=p_0\)（即 \(|a_2|=|a_0|\)）的奇异层，同样的 (c_1,c_2,p_0) 最多对应两种不同的归一化 (r)。两种若不同，恰好由
\[
 \boxed{r\longmapsto r^\sharp=t\overline r}
\]
相互转换；该变换为一个非平凡Z₂对合，保留 \(v\) 和 \(|r|\)，从而保留全部已声明观测。

**证明：**当 \(|t|=1\) 时 (v=\bar r+\bar t r)，映射 (r\mapsto t\bar r) 保持 (v)。归一化约束另给出
\[
 |r|^2=p_0^{-1}-2.
\]
写 (t=e^{i\theta}) 仅为数学分析的单位圆记号（**不执行三角运算**）；等价地选择任意复平方根 (q^2=t, |q|=1)，令 (u=\bar q r)，得 (qv=u+\bar u=2\operatorname{Re}u\)。一条实仿射直线与固定半径圆最多相交于两点，它们为 (u,\bar u)，即 (r,t\bar r)。当二者相等时仅一解。证毕。这个Z₂是来源**相位失辨**，不是额外空间维度。

## 推论：严格正实幅值三来源的一次端点修复
当全部 (a_j>0\) 为实幅值，(t>0)，上述奇异分支的非平凡伙伴不在正实可行域中。更简单地，直接从同一BRC恒等式得
\[
 \boxed{\frac{a_2}{a_0}=\frac{c_2}{p_0},\qquad
 \frac{a_1}{a_0}=\frac{c_1}{p_0+c_2}.}
\]
分母严格为正。故**全部归一化自相关加一个端点正质量读数 (p_0)，对任意三个严格正实来源的归一化幅值完全充分**；不必逐来源读取全部概率直方图。

复用PREFIX-279/282的同谱包 (f=(1,4,4),g=(2,5,2))，相同 (c_1=20/33,c_2=4/33)，但 (p_0(f)=1/33,p_0(g)=4/33)。公式分别恢复 (f\sim(1,4,4)) 和 (g\sim(1,5/2,1))，无需重复原始Stage50实验。

## 严格C4反例与条件性额外探针
令 (a=(1,i,1))，(b=(1,-i,1))。它们都为三条正幅值、C4相位的来源载荷：
\[
 Z_a=Z_b=3,\qquad c_1(a)=c_1(b)=0,\quad
 c_2(a)=c_2(b)=1/3,\quad p_0(a)=p_0(b)=1/3.
\]
所有历史差的C4自相关观察、加上端点概率 (p_0)，仍不可区分，但 (a_1/a_0=+i) 与 (-i) 不同。

在**候选**来源相干二元效应类中，令
\[
 E_u=\tfrac12 I+\tfrac12(u|0\rangle\langle1|+\bar u|1\rangle\langle0|),\quad |u|=1.
\]
按完整有序路径对BRC，(\mathcal B_{E_u}(a)=1/2+p_0\operatorname{Re}(ur)\)。它满足 (0\le E_u\le I)，因为 ( |\operatorname{Re}(u\bar a_0a_1)|\le |a_0||a_1|\le(|a_0|^2+|a_1|^2)/2\)，对任意输入读数在[0,1]，余效应 (I-E_u) 亦非负。对不等的奇异伙伴，`u=1` 与 `u=i` 至少一个可区分它们（取复差的实部或虚部）；本例取 (u=-i) 得
\[
 \boxed{\mathcal B_{E_{-i}}(a)=5/6,\qquad
 \mathcal B_{E_{-i}}(b)=1/6,\qquad \Delta=2/3.}
\]
此效应是**数学候选**，尚无证据表明一个完整准备后的六维心跳态存在对应来源相干Detector，不能称为现实可实施仪器。

## 实际精确核验与限制
执行随稿 `verify_prefix284.js` 中同一 `verifyPrefix284` 核心，使用BigInt高斯整数、显式C4相位及有序BRC路径对；不调用浮点、π、三角函数或一般传播器。枚举 (m_0,m_1,m_2\in\{1,2,3\})、第一来源相位固定1、其余两相位各C4，共**432包**，归并为358个观察签名，其中288个非奇异签名均唯一，70个奇异签名里42个有恰好两个不同规范化相对幅值，逐一核验 (r^\sharp=t\bar r)。最大2个规范化类。另枚举正实幅值1..8全部**512包**，439种签名，无不同规范化解的碰撞。直接有序路径对计算本例二元效应得5/6与1/6。有限枚举仅核验有声明范围的实现；一般结论来自上面的解析证明。

## Source核查与原生状态
本轮固定Source内的 `definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json` 保持六维Cell + 独立时间；`definitions/HEARTBEAT_SELF_CONSISTENT_INSTANT_V0_1.json` 要求每个H_n指定 `model_law_id`、完整场/动量/边界、来源与数值状态。前序PREFIX-282/283已核实Stage50 `packet_variance` 为可读取完整**输入包**的软件诊断，未证明为单个准备后态的物理测量；原始Stage50的外Port只给自相关型观察。本轮没有取得新的真实原生Detector、后态测量规则、合法局部相干效应、或 (H_n\mapsto H_{n+1}) 的完整 `model_law_id`；没有执行原始Stage50或物理心跳实验。此发现只证明在审阅到的Source及前序实际审查范围尚未取得合法桥接证据，**不证明全项目或现实物理不存在该仪器**。

分类：一般数学定理已手工证明；精确BRC计算在上述有限范围PASS；原生软件对应与物理探测合法性PENDING；原生Result/Driver未接纳。所有形式来源标签仍是带历史的Path-ID，**不是X6空间维度**；来源历史差r不等于心跳时间n。

## 下一问题 PREFIX-285
由当前真实Source取一个单个完整H_n后态的Detector定义、其来源响应 (E)、生效Port和测量后的状态/损耗；若仅外Port Toeplitz效应合法，证明三来源奇异 (r\leftrightarrow t\bar r) 在其允许的后续操作代数下保持不可分辨。若存在可实施的 (E_u)，在相同准备下校核5/6与1/6，并建立 `model_law_id`、原生X6 Cell/Port/场/材料动量/来源/边界/独立时间与本BRC观察之间逐字段可追溯对应。不得以重新输入分解来替代后态Detector。

Research-Activity-ID: RA-R6P284-20261027-T11-0837 (author-side only).
