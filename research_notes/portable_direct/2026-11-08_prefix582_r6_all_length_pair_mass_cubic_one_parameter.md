# PREFIX-582-R6：原生BRC门控残差与三组轴对质量的全长度一参数三阶定理

2026-11-08（Asia/Shanghai）｜AUTHOR_PROVED_WITH_EXACT_INTEGER_CERTIFICATE / UNREVIEWED / NOT_ADMITTED

## 精确范围及输入

冻结科学输入：`awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`；调用原生BRC 96端口、每端口六种带标签原生动作。实际可执行边定义为 `research_notes/portable_direct/PREFIX565_positive_marginal_certificate.py`（Git blob `7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41`），该实现具有原生支路和完整六轴、门控奖励。本定理固定原生允许零根、96端口**均匀初始分布**及每一步六种原生动作等概率。长度 \(n\) 是原生动作数，未等同物理心跳时间。

设 \(R_i(n)\) 为六个原生轴的累计奖励，\(K_n\) 为累计门控次数。定义
\[
P_0(n)=R_1(n)+R_2(n),\quad P_1(n)=R_3(n)+R_4(n),\quad P_2(n)=R_5(n)+R_6(n).
\]
沿用 PREFIX-579–580-R6 的正交门控残差
\[
Y_n=K_n-\frac{5R_1-R_2+5R_3-R_4-4R_5-4R_6}{192}.
\]
定义**有限长度**三阶联合累积量矩阵 \(C^{(n)}_{ij}=\operatorname{cum}(Y_n,P_i(n),P_j(n))\)， \(i,j\in\{0,1,2\}\)。

## 定理：所有长度都只有一个独立三阶耦合参数

对所有整数 \(n\ge0\)，存在精确有理数 \(q_n\) 使得
\[
\boxed{
C^{(n)}=q_n
\begin{pmatrix}
0&1&-1\\
1&-1&0\\
-1&0&1
\end{pmatrix},\qquad
q_n=\operatorname{cum}(Y_n,P_0(n),P_1(n)).
}
\]
特别是
\[
\operatorname{cum}(Y_n,P_0(n),P_0(n))=0,
\quad
\operatorname{cum}(Y_n,P_1(n),P_2(n))=0
\quad(\forall n\ge0).
\]
继承 PREFIX-581-R6 已发布的独立原生整数枚举证据，
\[
\boxed{q_0=0,\quad q_1=\frac1{576},\quad q_2=-\frac1{864}.}
\]
所以全长度一参数形式与有限深度非零/符号翻转兼容。该矩阵在 \(q_n\ne0\) 时秩为2、在 \(q_n=0\) 时秩为0；作为**9个三阶矩阵分量的共同参数空间**，维数为1。

## 全长度证明：768维整数转移的Cayley–Hamilton证书

1. 对每一步原生边， \(P_0+P_1+P_2=1\)。原生有向图每个端口的出度和入度均为6，故96端口均匀分布是一步转移矩阵 \(A/6\) 的平稳分布。完整576边表给出门控边3条及整数增量 \(H=64K-(3R_1+R_2+3R_3+R_4)\) 的总体单步均值为 \(-1\)，各 \(P_i\) 的单步均值为 \(1/3\)。因此，对每个 \(n\)，
\[
P_0(n)+P_1(n)+P_2(n)=n \ \text{逐路径},\quad
E[H_n]=-n,\quad E[P_i(n)]=n/3.
\]
又 \(Y_n=H_n/64+n/48\)，故三级累积量中的 \(Y_n\) 可换为 \(H_n/64\)。

2. 对任何有序对 \(i,j\)，令 \(D_n=96\cdot 6^n\)，并令 \(S_{HPP}(n),S_{HP_i}(n),S_{HP_j}(n),S_{P_iP_j}(n)\) 分别表示**对全部初始96端口及长度n的全部带标签路径**累加的三重或二重未归一矩（重复指标按原始幂计数）。按三级累积量定义直接展开：
\[
\boxed{
Q_{ij}(n)=9S_{HP_iP_j}(n)
-3n\bigl(S_{HP_i}(n)+S_{HP_j}(n)\bigr)
+9n S_{P_iP_j}(n)-2n^3D_n,
}
\]
\[
\boxed{C^{(n)}_{ij}=\frac{Q_{ij}(n)}{576 D_n}.}
\]
于是 \(C_{ij}^{(n)}=0\) 等价于**纯整数** \(Q_{ij}(n)=0\)。

3. 追踪三项累积奖励 \((H,P_i,P_j)\) 的8个子集混合矩，每个子集都由96个终端端口上的整数状态给出，总维数 \(8\cdot96=768\)。取0/1位掩码 \(m\)，递推公式
\[
M_m(n+1,v)=
\sum_{u\to v}\ \sum_{s\subseteq m}
M_s(n,u)\prod_{\ell\in m\setminus s} w_\ell(u\to v).
\]
同一奖励变量重复出现时，采用两个**有区别的形式拷贝**，乘积公式仍准确计算 \(HP_i^2\)。这定义768维固定整数转移矩阵 \(U\)。按照子集包含序排列，\(U\) 为块下三角，每个96维对角块均为相同的原生整数邻接矩阵 \(A^{\mathsf T}\)（重边按标签计数）。令 \(p(x)=\det(xI-A)\)，则
\[
\chi_U(x)=p(x)^8,\quad \deg\chi_U=768.
\]
由Cayley–Hamilton，全部三重矩序列 \(S_{HP_iP_j}\) 被 \(p(E)^8\) 消去（\(E\) 为前移算子）。

4. 任一双变量二重矩只需4个子集/端口，故被 \(p(E)^4\) 消去。对任何 \(p(E)f=0\)，利用 \([p(E),n]=Ep'(E)\) 可得 \(p(E)^2(nf)=0\)。因此三个 \(n\cdot S_{\text{二重矩}}\) 都被 \(p(E)^8\) 消去。由于 \(A\mathbf1=6\mathbf1\)，有 \((E-6)\mid p(E)\)，故 \(n^3D_n\) 被 \((E-6)^4\mid p(E)^8\) 消去。由式(2)，**每个** \(Q_{ij}(n)\) 都满足同一个次数至多768的首一线性递推 \(p(E)^8 Q_{ij}=0\)。

5. 实际执行同目录 `PREFIX582_R6_pair_cubic_ch768_certificate.py`，对原生576边和上式的768维整数递推，**穷举全部 n=0,1,...,767**，同时验证两个指定全整数序列：
\[
\boxed{Q_{00}(n)=0,\qquad Q_{12}(n)=0
\quad(0\le n<768).}
\]
一共 **1536 个完整零式**，全部精确整数通过，打印 `ALL_CHECKS_PASS`。由第4步的首一递推，这两个序列对全部 \(n\ge0\) 恒零。这是一个有有限、完整验证范围的严格无界长度代数证书。

6. \(\sum_iP_i(n)=n\) 是路径恒等式，故对任何 \(j\)，\(\sum_i C^{(n)}_{ij}=\operatorname{cum}(Y_n,n,P_j(n))=0\)。结合矩阵对称性以及 \(C_{00}^{(n)}=C_{12}^{(n)}=0\)，逐项解线性方程得到唯一形式
\[
C^{(n)}=\begin{pmatrix}0&q&-q\\q&-q&0\\-q&0&q\end{pmatrix}.
\]
结合q的定义，定理得证。

## 证据、关系、下一问题

精确整数证书由一个独立Python标准库驱动从冻结BRC原生边函数重建96×6路径，直接迭代768长度层，校验所有1536零式；本轮实际复跑结果为 `ALL_CHECKS_PASS`。结果摘要 `PREFIX582_R6_PAIR_CUBIC_CH768_RESULTS.json`。数值公式 \(q_1,q_2\) 来自 PREFIX-581-R6 的独立原始路径整数矩证书。

本结论对指定**零根+均匀端口初始分布**的**全部有限整数长度**适用，保留精确路径、端口、六轴/门控联合计数。BRC复用 `REUSE_EXECUTED`；这是一项PREFIX-580-R6的进一步精确有限深度结构，同时保留一切原生来源。无任何原生Source任务 CLAIM、Result、Review 或Working Truth接受之声称。

下一最小可执行问题：求 \(q_n\) 的紧凑有理生成函数/低阶整数递推，给出严格二阶奇偶符号或衰减规律；其次研究如何从原生门控来源构造更短的路径配对证书，并测试非均匀起点及其它冻结允许根的确切适用范围。原生控制服务 `STATUS_DATABASE_UNAVAILABLE`，正式活跃Owner及新Source会话未确认。
