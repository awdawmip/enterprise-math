# 霍奇主线：四交数判据、非分裂特殊纤维种子与延拓障碍

Researcher-ID: `EM-HODGE-E8C393`
Research-Activity-ID: `RA-D77892286633B21C12B83F98`
Progress-Event-ID: `HODGE-4M-GRAPH-E8C393-20260910`
Date: `2026-09-10`
Mode: `TASK_RESEARCH / DIRECT_USER_RESEARCH`
Task-ID / Claim: `NONE`。这是用户“推进试试”授权的直接研究，不接管或改写 H0O 的正式整改任务。
Session: `chatgpt-local-hodge-cffcaf05801d41548ab6692cce36c898`，本会话本地生成的稳定键，不是平台服务器会话编号。
Status: `DERIVATION_CANDIDATE / EXACT_CHECKS_PASSED / INDEPENDENT_REVIEW_PENDING`
Publication strength: 研究笔记和可恢复工作前沿；不是 Driver 接受、Working Truth、Foundation 或霍奇猜想证明。

## 0. 结论与边界

本轮获得以下可复核结果：

1. 将 H0N 的特殊 Weil 投影器改写为自伴随算子的三次多项式，并导出只用四个交数的精确判据。
2. 在同一 `K=Q(i)`、判别式 `[-3]` 的特殊乘积纤维上，写出具体代数循环 Gamma，算得其 Weil 投影自交为 `-2`。
3. 对该 Gamma 的完整平坦上同调类，算得保持其为 Hodge 类的允许一阶周期方向只有 3 复维，而环境 Weil 周期域为 9 复维。
4. 对 Gamma 与 u 的逆像图像的结构层，横截 Koszul 计算给出 Ext^1=0、Ext^3 维数 4096；普通短正合扩张不能把这两个支撑粘成新的非平凡层。
5. 新的任务局部检查器完成 78 项精确断言，失败 0。它检查多项式、外代数、交数和切空间线性代数；不证明一般纤维循环存在，不认证全部几何变形理论，也不替代独立数学审查。

**没有构造很一般非分裂六维簇上的首个特殊循环。** 特殊纤维有种子，不等于种子可以延拓。本文不声称这些标准工具的应用具有文献首创性。

## 1. 冻结输入与已有结果复用

目标仍是 H0N/H0O 的很一般非分裂 Weil 六维簇，不改成分裂判别式。

源快照：`awdawmip/enterprise-math@b691afe636d3ae12ddd330c621c9c92421221d56`。

- `research_returns/HODGE_H0N_NONSPLIT_WEIL_EXCEPTIONAL_CH3_SEED_OBJECT_RETURN_20260902.md`
- `research_returns/HODGE_H0O_NONSPLIT_WEIL_INTERMEDIATE_SUPPORT_FM_EXCEPTIONAL_CH3_RETURN_20260903.md`
- `research_task_records/RS-HODGE-H0O-NONSPLIT-WEIL-INTERMEDIATE-SUPPORT-FM-EXCEPTIONAL-CH3/TP2-853EE36ED78FF34CC992.json`

已消费 H0N 的七分块和代数投影接口，不重启其已完成研究。H0O 的种子守恒仍按限定核和限定输入族理解；其过强完成标签不作为证明。

本文在经典复代数几何类型下计算，不把 P000 的项目空间公设替换成经典几何，也不把 P000 当作经典霍奇猜想的证明。

设 A 是复六维阿贝尔簇，带 Z[i] 作用及 Rosati 共轭相容极化 theta，Weil 签名 (3,3)。写

\[
H^1(A,\mathbb C)=V_\sigma\oplus V_{\bar\sigma},\qquad
B_p=\Lambda^pV_\sigma\otimes\Lambda^{6-p}V_{\bar\sigma}.
\]

特殊空间是

\[
W_\mathbb C=B_0\oplus B_6.
\]

取 `u=1+2i`，`U=u^*|H^6`，`bar U=bar u^*|H^6`。它们在 B_p 上的特征值依次为

\[
117-44i,\;-35+120i,\;-75-100i,\;125,\;
-75+100i,\;-35-120i,\;117+44i.
\]

这些数据与 H0N 的原投影器完全一致。

## 2. 自伴随三次投影器

对中间交叉配对 `(x,y)=int_A x cup y`，

\[
U^\dagger=u_*=(\deg u)U^{-1}=\bar U.
\]

理由是 `deg u=5^6=15625`，而 `bar u o u=[5]` 在 H^6 上作用也是 15625。因此

\[
S=U+\bar U
\]

自伴随。它在七分块上的特征值为

\[
234,\;-70,\;-150,\;250,\;-150,\;-70,\;234.
\]

于是

\[
\boxed{\Pi_W=-\frac{(S+70)(S+150)(S-250)}{1867776}}.
\]

在 W 上分子等于 `-1867776`，在其他分块为零。该式在整个 H^6 上成立，不需要假设“全部 Hodge 类只有 theta^3 和 W”。

这是已有 H0N 投影器的等价改写，不是新造未经验证的投影对象。由于 U、bar U 来自代数同源，Pi_W 仍由有理代数对应实现，且是交叉配对的正交投影。

在只考虑 S 的多项式选择器时，三个不同补空间特征值都须被杀掉，故次数至少为 3；这里实现的是这个限定多项式模型的最小次数，不声称所有判别算法都至少需要四个输入。

## 3. 四交数判据

对实际代数循环 `Z in CH^3(A)_Q`，令 `alpha=cl(Z)`，定义

\[
m_n(Z)=\int_A \alpha\cup(u^n)^*\alpha,\quad n=0,1,2,3.
\]

必须使用真实循环交数，不能把任意整数四元组当成几何样本。由自伴随性，

\[
(\alpha,U^n\alpha)=(\alpha,\bar U^n\alpha).
\]

展开上一节的三次投影器，并使用 `U bar U=15625 I`，得到

\[
\Pi_W=
\frac{
3562500 I-2375(U+\bar U)
+30(U^2+\bar U^2)-(U^3+\bar U^3)
}{1867776}.
\]

设

\[
\boxed{\Delta(Z)=m_3-30m_2+2375m_1-1781250m_0}.
\]

则精确恒等式为

\[
\boxed{\Delta(Z)=-933888\int_A(\Pi_W\alpha)^2.}
\]

注意负号。

Weil 类在签名 (3,3) 下是实的 (3,3) 类；theta 属于两嵌入平衡分量。对极端外幂再乘 theta 会产生第七个同嵌入因子，所以 `theta cup W=0`。因此 W 是原始中间 (3,3) 空间。Hodge–Riemann 双线性关系在这里的符号是 `(-1)^3=-1`，故

\[
w\ne0\Longrightarrow\int_A w^2<0,\qquad w\in W_\mathbb R.
\]

综上，

\[
\boxed{\Delta(Z)\ge0,\qquad
\Delta(Z)>0\iff \Pi_W[Z]\ne0.}
\]

这不仅适用于很一般目标，也适用于具有额外 Hodge 类的特殊纤维。它不是首种子存在定理，而是一个无需先显式重建 W 坐标的精确检验。

若 Z 为整系数循环，四个交数及 Delta 都是整数，因此严格正值不会依赖浮点阈值。

### 与“度数加自交”简化法的区别

只有另行证明所研究类属于 `Q theta^3 + W` 时，才能仅用
`d=int_Z theta^3`、`v=int_A theta^6`、`m_0` 写成 `d^2/v-m_0=-w^2`。
特殊纤维一般有额外分块，不能直接这样压缩。本节的四交数式没有这一缺口。

## 4. 一个明确的非分裂特殊纤维种子

取

\[
E=\mathbb C/(\mathbb Z+i\mathbb Z),\quad A_0=E^3\times E^3.
\]

以 `(x,y)` 表示两组三坐标，让 `a in Z[i]` 作用为

\[
a\cdot(x,y)=(a x,\bar a y).
\]

取各椭圆因子的极化次数 `(1,1,1,1,1,3)`。在相应 K 格上，Hermitian 形式为

\[
h=\operatorname{diag}(1,1,1,-1,-1,-3).
\]

故签名是 (3,3)，判别式类为 [-3]。`3` 不是 Q(i) 的有理范数：若清分母后有互素整数 `x^2+y^2=3z^2`，模 3 迫使 x,y 都被 3 整除，随后 z 也被 3 整除，矛盾。因此它不是分裂 [-1] 类。

A_0 正是这一固定 Hermitian 格的周期域中的一个特殊点；没有把分裂定理搬到非分裂目标。A_0 的高度可分解性也意味着它绝非所要求的很一般成员。

取实际阿贝尔三维子簇

\[
\Gamma=\{(x,x):x\in E^3\}\subset A_0.
\]

其法丛平凡，故 `m_0(Gamma)=0`。

若 `(1+2i)^n=a_n+b_ni`，Gamma 与 `(u^n)^{-1}Gamma` 相交时，每一坐标满足
`(u^n-bar u^n)x=0`。对 n=1,2,3，该同源的次数是 `4b_n^2`，故

\[
m_n(\Gamma)=(4b_n^2)^3=64b_n^6.
\]

使用

\[
u=1+2i,\quad u^2=-3+4i,\quad u^3=-11-2i
\]

得

\[
(m_0,m_1,m_2,m_3)=(0,4096,262144,4096),
\]

\[
\boxed{\Delta(\Gamma)=1867776,\quad
\int_{A_0}(\Pi_W[\Gamma])^2=-2.}
\]

这给出的是**同一非分裂分支的特殊纤维上的非零代数种子**，不是很一般纤维种子。

### 独立的外代数复核

在六个椭圆因子的实一形式 `dx_j,dy_j` 下，

\[
[\Gamma]=\prod_{j=1}^3
(dx_{j+3}-dx_j)\wedge(dy_{j+3}-dy_j).
\]

令

\[
\eta=\bigwedge_{j=1}^3(dx_j+i\,dy_j)\wedge
\bigwedge_{j=4}^6(dx_j-i\,dy_j).
\]

按椭圆因子的复定向，

\[
\Pi_W[\Gamma]=\frac14\operatorname{Im}\eta,\quad
\int(\operatorname{Im}\eta)^2=-32.
\]

这再次给出自交 -2。检查器既用有限同源核计数，也用 12 维实外代数展开计算四交数，不是重复代入同一个数字公式。

这里 `int theta^6=2160`，`int_Gamma theta^3=96`。
因此 `96^2/2160=64/15` 不等于 2，明确展示了上一节“两数字简化”在特殊纤维上的适用边界。

## 5. 实际尝试延拓 Gamma：六个一阶方向被阻挡

现在检查它能否直接随完整 9 复维 Weil 家族变形。

在固定 K 格的实化上写

\[
J_0=\operatorname{diag}(iI_3,-iI_3),\quad
h=\operatorname{diag}(I_3,-D),\quad D=\operatorname{diag}(1,1,3).
\]

满足 K 线性、`J^2=-1` 和极化相容的一阶变分具有形式

\[
\dot J=
\begin{pmatrix}0&B\\D^{-1}B^\dagger&0\end{pmatrix},
\qquad B\in M_3(\mathbb C).
\]

推导：反交换关系排除对角块；对 `J^\dagger hJ=h` 求导得到下左块为 `D^{-1}B^\dagger`。B 提供 9 个复周期方向。

将 A_0 的物理复坐标转换到固定 K 格后，Gamma 的实切空间是

\[
L=\{(v,\bar v):v\in\mathbb C^3\}.
\]

保留这个有理子空间为复子空间要求 `dot J L subset L`，即

\[
D^{-1}B^\dagger=\bar B
\iff B^T=DB.
\]

直接求解：

\[
\boxed{
B=\begin{pmatrix}
a&b&0\\
b&c&0\\
0&0&0
\end{pmatrix}.}
\]

因此允许一阶方向为 3 复维；线性方程秩为 6。

这不只是“选了一种参数化不方便”：Gamma 的完整平坦类是非零可分解实 6-形式。一条可分解实 6-形式是 (3,3) 当且仅当其确定的实余法空间保持在 Hodge 圆作用下，从而相应实子空间 L 为复子空间。故保留这个完整平坦类为 Hodge 类同样要求上述条件。改变同一类的循环代表不能绕过其 Hodge 型的一阶变化。

边界：这是 Gamma 的完整类的限制；不能推出纯 Weil 类 `Pi_W[Gamma]` 的代数性不存在。纯 Weil 类沿整个 Weil 家族仍是 (3,3)，但本文没有证明其代数代表能够延拓。

## 6. 第二个具体尝试：用普通层扩张粘合两个图像

令

\[
F_0=\mathcal O_\Gamma,\qquad
F_1=u^*\mathcal O_\Gamma=\mathcal O_{u^{-1}\Gamma}.
\]

u 是有限平坦同源。两个支撑都是光滑余维三阿贝尔子簇，交集有 4096 个横截点。

在每个交点，Gamma 的三条局部正规方程限制到另一支撑后仍是正则参数。对其 Koszul 分解施加 Hom，局部 Ext 只在次数 3 非零。局部 Ext 的支撑是有限点集，所以局部到整体谱序列不给出额外次数。因此

\[
\boxed{\operatorname{Ext}^k(F_0,F_1)=0\ (k\ne3),\quad
\dim\operatorname{Ext}^3(F_0,F_1)=4096.}
\]

特别地 `Ext^1(F_0,F_1)=0`，普通短正合扩张必分裂，不能提供这里设想的非平凡粘合层。这是对这一对支撑的精确边界，不是对所有层或所有导出构造的否定。

### 明确留下的下一单位

现成的非零通道在次数 3，而不是次数 1。例如可写三角

\[
F_1[2]\longrightarrow E_\xi\longrightarrow F_0
\xrightarrow{\xi}F_1[3],
\quad \xi\in\operatorname{Ext}^3(F_0,F_1).
\]

这只定义特殊纤维上的候选导出对象。其 K 类为 `[F_0]+[F_1]`；
它尚未消去全部非通用的中间分块，不能直接宣布可以随 Weil 家族变形。

真正的下一研究单位是：在保留非零 Weil 分量的同时，构造具有适当完整 Chern 特征的对象，并实际计算其 Atiyah/Kodaira–Spencer 障碍映射，验证是否能覆盖全部 9 个周期方向。Hodge 型保持、某个迹为零或虚拟 K 类存在，都不能代替这个验证。本文未完成此单位。

## 7. 结构方法与来源损失审计

- 复用状态：`REUSE_APPLIED`。直接应用 H0N 的七分块、代数投影和单种子放大接口；新式是该投影的自伴随化与交叉配对特化，不开设新的通用工具家族。
- BRC 适用边界：有符号的有理上同调/外代数不是非负分支质量模型；不能把“质量为正”冒充符号抵消或代数性证明。
- 载体保留：实际循环、u/bar u 的作用、七个嵌入计数分块、外代数符号、固定极化、格和判别式均保留。
- 压缩观察者：四个交数只用于检验 `Pi_W[Z]` 是否为零；不能从 Delta 重建完整循环、Weil 方向、变形障碍或实际支撑。后续变形计算必须回到保留的完整对象。
- 明确的有损错误：把特殊纤维压成 `Q theta^3+W` 会丢掉额外 Hodge 分量；本文的 Gamma 给出数值反例。
- 工具范围：任务局部精确检查，`RESULT_ONLY / CANDIDATE_NOT_TOOL`；无通用工具新增，无独立审查或正式接受。

## 8. 检查与文献

检查器：`research_checks/HODGE_FOUR_INTERSECTION_GRAPH_CHECK_EM_HODGE_E8C393_20260910.py`

运行：
`python research_checks/HODGE_FOUR_INTERSECTION_GRAPH_CHECK_EM_HODGE_E8C393_20260910.py`

本轮本地运行：`PASS_EXACT_IDENTITIES_ONLY`，78 项断言，失败 0。
没有执行 Lean 形式化或外部独立证明审查。脚本中的 Ext 信息来自第 6 节的 Koszul 论证，不把有限断言数当作 Ext 理论的独立认证。

文献只作标准数学工具和外部范围核对，不将未证论文声明当作已证明输入：

1. P. Deligne, *The Hodge Conjecture*, Clay Mathematics Institute:
   https://www.claymath.org/wp-content/uploads/2022/06/hodge.pdf
   用于有理代数循环与 Hodge 类的基本目标区分。
2. J. Xiao, *Mixed Hodge–Riemann bilinear relations and m-positivity*, arXiv:1811.05865, Section 1.1:
   https://arxiv.org/pdf/1811.05865
   其中经典 HRR 的符号为 i^(q-p)(-1)^((p+q)(p+q+1)/2)。取 p=q=3、n=6 得负定号；本文不需要混合推广。
3. E. Markman, *Cycles on abelian 2n-folds of Weil type from secant sheaves on abelian n-folds*, arXiv:2502.03415v2:
   https://arxiv.org/abs/2502.03415
4. E. Markman, *Secant sheaves and Weil classes on abelian varieties*, arXiv:2509.23403v2:
   https://arxiv.org/html/2509.23403v2
   第 1.2 定理和第 11 节用于核对六维结论的分裂范围，以及半正则性不是自动延拓。未将其分裂结论用于 [-3]。

最终前沿：**可计算的特殊纤维种子 + 通用四交数检测 + 明确的一阶/Ext 障碍；很一般非分裂目标上的首种子仍未给出。**
