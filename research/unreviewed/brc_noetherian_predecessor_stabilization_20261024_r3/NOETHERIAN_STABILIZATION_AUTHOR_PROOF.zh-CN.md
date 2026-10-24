# BRC 跨动作谱运输前驱层级的有限稳定定理与两动作模型完全分类

日期：2026-10-24；状态：AUTHOR_ANALYTIC_PROOF / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED。

## 0. 输入、数学对象与权限边界

GLOBAL_KNOWLEDGE_V1 固定快照：awdawmip/chatgpt-global-knowledge main@e3e45513affb9845c315a0ee84f6a4d9d6e1005f。已读取规范入口、P000 原契约（blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc）、ACTIVE 世界观、MATH_RESEARCH_POLICY 与 BRC 使用规范。Enterprise Math Source 固定 main@43b6d1fc7f75e451a84fc1401ebe77b8436c914c；portable 规范 docs/PORTABLE_RESEARCH_PROTOCOL.md，blob ca5de2d680d2439ff4b67c2c55fbd4159813cd5c。

前沿依赖：作者侧未审论文 TWO_STEP_PREDECESSOR_AUTHOR_PROOF.zh-CN.md，commit dc8ca1d8409e99341d0101540f77d455ff42fab6，及其明确列出的跨动作运输定义与两动作核。相关工具/方法解析：REUSE_APPLIED（复用现有非负谱运输与前驱证明方法），不是新建 BRC 载体或声称独立工具实现。

真实连接：GitHub 身份 awdawmip，仓库可写；原生 em_control_tasks 返回 CONTROL_QUOTA，em_session_start 返回 STATIC_READONLY_SCOPE_DENIED、operation_sent=false。本轮无法权威核实活跃 Owner，未取得新 Researcher 活动、Task CLAIM、独立 Driver 审查或 Source Result 接纳。作者侧研究只存于非规范未审研究分支，不声称正式任务运行。

研究范围仅是有限隐藏标签、有限公开动作、全正概率的辅助 BRC 好边占有观察器。未提供 P000 六维 Cell、三维切片第三分量、时间与支路保真映射；P000 不被改动，不推断原生动力学或物理结论。

## 1. 定义

令隐藏标签有限集 V，公开动作有限非空集 A。每种动作 b 对标签 i 的概率 q_b(i)>0，且 \sum_i q_b(i)=1。令指定的无向好边集合 E 为两元标签子集，d_i 为标签 i 在好边图中的度数。对非空公开动作计数 c\in\mathbb N^A 定义

$$
W_i(c)=\prod_{b\in A}q_b(i)^{c_b},\quad
s_{b,e}=\sum_{i\in e}q_b(i),\quad
W_e(c)=\prod_{b\in A}s_{b,e}^{c_b}.
$$

好边两标签恰为最后累计出现标签支持的概率由容斥表示为

$$
\delta(c)=\sum_{e\in E}W_e(c)-\sum_{i\in V}d_i W_i(c)
\quad (|c|\ge 1).
$$

空历史单独定义 \delta(0)=0；不将上式套到空历史。
对下一动作 a，定义

$$
\Delta_a(c)=\delta(c+\mathbf e_a)-\delta(c)
 = \sum_i D_{a,i}(c)-\sum_e C_{a,e}(c),
$$

$$
D_{a,i}(c)=d_i(1-q_a(i))W_i(c),\qquad
C_{a,e}(c)=(1-s_{a,e})W_e(c).
$$

当且仅当对全部公开动作 b 都有 q_b(i)\le s_{b,e}，允许谱运输弧 i\to e（允许非关联弧，但必须经过谱序检查）。K_0 是对每个下一动作 a 都存在非负流 F^{(a)}_{i,e} 的非空计数状态集合，满足

$$
\sum_e F^{(a)}_{i,e}=D_{a,i}(c),\qquad
\sum_i F^{(a)}_{i,e}\le C_{a,e}(c),
$$

其中不允许的运输弧流量为零。递归定义

$$
K_{r+1}=K_r\cup
\{c: |c|\ge 1,\ \Delta_a(c)\le0\ \forall a,\ 
c+\mathbf e_a\in K_r\ \forall a\}.
$$

真实全未来安全集为
$$
S=\{c:|c|\ge1,\ \Delta_a(c+f)\le0\ 
\forall f\in\mathbb N^A,\ \forall a\in A\}.
$$

## 2. 定理一：静态跨动作谱运输集合向上闭合

**定理 1。** 如果 c\in K_0，且 g\in\mathbb N^A，则 c+g\in K_0。

**证明。** 只需追加一个动作 b；对每个被验证的下一动作 a，用原有流构造

$$
F'^{(a)}_{i,e}=q_b(i)F^{(a)}_{i,e}.
$$

顶点供给精确满足
$$
\sum_e F'^{(a)}_{i,e}=q_b(i)D_{a,i}(c)=D_{a,i}(c+\mathbf e_b).
$$

每条边的允许谱序 q_b(i)\le s_{b,e} 保证

$$
\sum_i F'^{(a)}_{i,e}
\le s_{b,e}\sum_i F^{(a)}_{i,e}
\le s_{b,e}C_{a,e}(c)
=C_{a,e}(c+\mathbf e_b).
$$

因此新流仍可行。对任意 g 反复追加即可。证毕。

相同按未来计数逐坐标缩放的流也证明 K_0\subseteq S：对未来 f，取
F^{(a,f)}_{i,e}=F^{(a)}_{i,e}W_i(f)，谱序使边使用量不超过 C_{a,e}(c+f)；因而每个未来增量均非正。

## 3. 定理二：所有前驱层级向上闭合、健全，且有限稳定

**定理 2。** 对每一个 r\ge0：
(i) K_r\subseteq S；(ii) K_r 是 \mathbb N^A 中的向上闭合集。
此外，存在依赖固定 BRC 模型的有限整数 R，使得

$$
\boxed{K_R=K_{R+1}=K_{R+2}=\cdots
=\bigcup_{r\ge0}K_r.}
$$

**健全性归纳。** r=0 由定理1后的流缩放证明。若 c 新增于 K_{r+1}，对 f=0 的所有下一动作增量由新增条件非正；对 f\ne0，任选 b 使 f_b\ge1，写 f=\mathbf e_b+g，因 c+\mathbf e_b\in K_r\subseteq S，即有 \Delta_a(c+f)\le0。旧成员继承，故 K_{r+1}\subseteq S。

**向上闭合归纳。** K_0 由定理1成立。若 K_r 已向上闭合，取新增 c\in K_{r+1}\setminus K_r 和任意 g\ge0。健全性已知 \Delta_a(c+g)\le0；又因 c+\mathbf e_a\in K_r，向上闭合推出
(c+g)+\mathbf e_a=(c+\mathbf e_a)+g\in K_r。
故 c+g\in K_{r+1}。旧成员也向上闭合。

**有限稳定。** U=\bigcup_{r\ge0}K_r 也是向上闭合集。Dickson 引理说有限维 \mathbb N^A 中任意向上闭合集具有有限个坐标极小生成元 m_1,\ldots,m_t。各 m_j 因属于 U，必已属于某个有限层级 K_{r_j}。令 R=\max_j r_j（U 为空则令 R=0）；K_R 向上闭合且包含全部 m_j，故 U\subseteq K_R。反向包含显然，所以 U=K_R 并永远稳定。证毕。

说明：这是逐个固定有限动作模型的**存在性有限终止结论**。并未给出仅由标签数/动作数决定的统一数值上界，也未证明递归并集 U 等于真实 S。Dickson 引理属经典良拟序事实，不据此声称首创。

## 4. 定理三：此前四标签双动作模型的全部层级可以精确分类

仍取 V=\{0,1,2,3\}，E=\{01,02,03,12\}，

$$
q_\alpha=(1,1,1,7)/10,\qquad
q_\beta=(1,1,1,8)/11.
$$

令 c=(x,y)，n=x+y。非空历史的精确占有概率为

$$
\delta(x,y)=
\frac{8^x9^y+3\cdot2^{x+y}-7^x8^y-7}
{10^x11^y}.
$$

对于 a\in\{\alpha,\beta\} 取 m_\alpha=7,m_\beta=8，增量与以下整数同号：

$$
N_a(x,y)=7(m_a+2)+3\cdot7^x8^y
-3(m_a+1)2^{x+y}-2\cdot8^x9^y.
$$

**完全分类：**

$$
\boxed{
K_0=\{(x,y):x+y\ge4\},\qquad
K_1=\{(x,y):x+y\ge3\},\qquad
K_2=K_3=\cdots=S=\{(x,y):x+y\ge2\}.
}
$$

**证明 K_0 的精确阈值。** 大标签3的谱概率分别为7/10和8/11，而除03以外所有好边的谱在这两个动作下都是2/10和2/11，因此标签3只能运输到03。将流量分子乘去正的公共分母 10^x11^y(m_a+3) 后，大标签需求为 3\cdot7^x8^y，唯一边容量为 2\cdot8^x9^y，且

$$
\frac{\mathrm{capacity}}{\mathrm{demand}}
=\frac23(8/7)^x(9/8)^y.
$$

若1\le n\le3，该比值不超过 (2/3)(8/7)^3=1024/1029<1，所以 K_0 中不可能有任何长度小于4的非空状态。

若 n=4，该比值至少 (2/3)(9/8)^4=13122/12288>1。对每一个下一动作 a，显式路由

$$
0\to01:\ 3(m_a+2),\quad
1\to12:\ 2(m_a+2),\quad
2\to02:\ 2(m_a+2),\quad
3\to03:\ 3\cdot7^x8^y.
$$

四条弧都是关联边，满足两种动作的谱序。三个小边容量分别都是 (m_a+1)2^4，对动作 alpha 至少128，对动作 beta 至少144，分别严格超过需要的27/18/18及30/20/20。大边容量亦严格超过需求。故全部五个长度4状态对两种下一动作都有严格正运输余量，属于 K_0；应用定理1则所有 n\ge4 都属于 K_0。精确阈值成立。

**证明 K_1、K_2 与真实安全集。** 对 n=2 的全部三种计数和 n=3 的全部四种计数，将上述整数 N_a 逐一求值得到：

| (x,y) | N_alpha | N_beta |
|---|---:|---:|
| (0,2) | −3 | −8 |
| (1,1) | −9 | −14 |
| (2,0) | −14 | −19 |
| (0,3) | −51 | −68 |
| (1,2) | −81 | −98 |
| (2,1) | −105 | −122 |
| (3,0) | −124 | −141 |

因此所有 n=3 状态的两种即时增量均严格负且后继均在 K_0，故进入 K_1；所有 n=2 状态不能进入 K_1（其后继 n=3 不在 K_0），但即时增量严格负且后继都在 K_1，故进入 K_2。

长度为1的历史尚不可能有恰好两种不同隐藏标签，因此 \delta=0；再追加任一全正动作，都有严格正概率得到指定好边，故全部 n=1 状态的下一步增量严格正，永远不进入任何 K_r，也不属于 S。由健全性 K_2\subseteq S，再由 n=1 的排除得 S=\{n\ge2\}。证毕。

n=0 单独以 \delta(0)=0 处理：追加一个动作仍为零，但再追加第二个动作出现严格正增量，因此空状态不在 S，也不会被本定理列入 K_r。以上不依赖非法的空历史容斥扩展。

## 5. 验证界限与可接续问题

精确 JavaScript BigInt 检查脚本 verify_noetherian_stabilization.js 附全部长度1—6的126条双动作历史的独立16掩码支持递推、252条下一动作增量一致性、长度1—3的9个严格大标签割缺口、长度4的10组显式运输正余量，以及81条有限网格前驱分类检查。相关具体整数记录在 EXACT_EVIDENCE.json。无浮点符号判定。

无限模型数目的有限稳定由定理1、2及 Dickson 引理的解析证明承担；有限检查不构成从网格外推。定理3对全部计数的归纳来自 K_0 的遗传性与长度4的完备边界证书，并非只检查到第6轮。

**本轮新科学增量**：
1. 任意固定有限动作正概率辅助 BRC 模型的前驱层级必在某个有限深度稳定（存在性，不给出统一上界）。
2. 已有双动作两层证书示例的整个 K_0/K_1/K_2/... 和真实永久安全集 S 全部完成精确分类，其证书深度上界恰为2。
3. 该固定示例不可能出现 K_3\setminus K_2，因此寻找严格三层见证必须更换模型或结构；这不排除其他 BRC 模型具有严格三层及更深层级。

**下一可判别问题**：寻找另一组严格正概率公开核/好边图，使某状态在 K_3\setminus K_2；或者找出能给具体正概率模型显式计算 R 的有效界（一般存在性不等于可计算的统一边界）。保留 Owner/活动登记、独立 Driver 审查及 P000 保真桥梁三个独立未完成事项。
