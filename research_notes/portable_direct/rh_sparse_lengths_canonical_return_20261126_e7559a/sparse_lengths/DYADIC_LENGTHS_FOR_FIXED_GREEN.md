# 任意整数单元只需二幂长度：统一谱隙与实际 Green 预算

2026-11-26。共同作者 `EM-DIRECT-E7559A / TASK_RESEARCH`，Activity `RA-D2F111EA1C0D4B1DBEFBC1B4`。直接前驱为第6轮 Source `fabd951fd95df87c35353a620b737634a1b2a820` 的 `green_arithmetic/INTERVAL_MEAN_SQUARE_TO_GREEN.md`。规范读取由统筹刷新；P000 / Heartbeat X6、实际辅助标量、全整数及合数背景、真实前史与端点保持。

本稿是作者解析证明与最小有限复算，不是 independent Review 或 formal Result。不重跑旧证书、不进行远端写入。

## 1. 主结果及其新增内容

第6轮已经给出每个实际单元的完整长长度带均方入口。本轮把所需长度压缩为

\[
\mathcal D_h=\{1,2,4,\ldots,2^{m-1}\},
\qquad m=\lceil\log_2h\rceil,
\tag{1.1}
\]

其中 h≥2，最大的二幂严格小于 h；h=1时取空集。长度数恰为 m。

关键不只在 h 为2的幂时成立。对**任意整数 h≥1**，二幂距离边图均有统一谱隙至少2：

\[
\boxed{
\sum_{i=0}^{h-1}(z_i-\bar z)^2
\le\frac12\sum_{d\in\mathcal D_h}
\sum_{i=0}^{h-1-d}(z_{i+d}-z_i)^2.
}
\tag{1.2}
\]

因此任意 h 不需要向下取成2幂、不需要补齐虚构节点、不需要另加 h−2^j 长度，也不需要增加对数损失。

接回第6轮的准确 Abel 权重转移和原细网格谱常数，可得

\[
\boxed{
\|V_+\|_w^2
\le\frac{C_\Pi R}{2L^2(L+1)}
\sum_{d\in\mathcal D_h}J_{b,I}(d).
}
\tag{1.3}
\]

符号、目标和源权与第6轮相同；新结果缩减的是需要取得的**区间长度集合**。

## 2. 任意 h 的谱隙证明

定义

\[
\mathcal V_h(z)=\sum_{i=0}^{h-1}(z_i-\bar z)^2,
\quad
\mathcal Q_h(z)=\sum_{d\in\mathcal D_h}\sum_{i=0}^{h-1-d}(z_{i+d}-z_i)^2.
\]

按偶数位置和奇数位置分开，得到向量 e、o，长度分别为

\[
a=\lceil h/2\rceil,\qquad b=\lfloor h/2\rfloor.
\]

当 h≥2 时，记 δ=mean(e)−mean(o)。完整方差分解为

\[
\mathcal V_h(z)=\mathcal V_a(e)+\mathcal V_b(o)+\frac{ab}{h}\delta^2.
\tag{2.1}
\]

所有长度至少2的二幂边都保持位置奇偶性，压缩索引后恰为两侧的二幂边，所以有准确递归

\[
\mathcal Q_h(z)=\mathcal Q_a(e)+\mathcal Q_b(o)
+\sum_{i=0}^{h-2}(z_{i+1}-z_i)^2.
\tag{2.2}
\]

这里无边被重复或丢掉，h为奇数时也成立。

### 2.1 相邻边控制奇偶均值差

令

\[
c_i=\begin{cases}1/a,&i\text{ 为偶数},\\-1/b,&i\text{ 为奇数},\end{cases}
\quad
s_i=\sum_{j=0}^ic_j\quad(0\le i<h-1).
\]

因 Σc_i=0，有准确望远镜式

\[
\delta=\sum_{i=0}^{h-1}c_iz_i
=\sum_{i=0}^{h-2}s_i(z_i-z_{i+1}).
\tag{2.3}
\]

若 h=2b，则 s_i 在1/b和0之间交替，因此

\[
\sum_i s_i^2=1/b,\qquad
\sum_i(z_{i+1}-z_i)^2\ge b\delta^2
=\frac{2ab}{h}\delta^2.
\tag{2.4}
\]

若 h=2b+1，则 a=b+1，准确有

\[
s_{2j}=\frac{b-j}{b(b+1)},\qquad
s_{2j+1}=-\frac{j+1}{b(b+1)}\quad(0\le j<b),
\]

\[
\sum_i s_i^2
=\frac{2b+1}{3b(b+1)}
=\frac h{3ab}.
\]

Cauchy–Schwarz因此给

\[
\sum_i(z_{i+1}-z_i)^2
\ge\frac{3ab}{h}\delta^2
\ge\frac{2ab}{h}\delta^2.
\tag{2.5}
\]

这个奇数情形的系数是本轮补齐任意 h 的承重点。

### 2.2 归纳完成

h=1时两边为零。假设较短向量均满足 \(\mathcal Q\ge2\mathcal V\)。把(2.4)或(2.5)代入(2.2)，再使用(2.1)，得到

\[
\mathcal Q_h(z)
\ge2\mathcal V_a(e)+2\mathcal V_b(o)+\frac{2ab}{h}\delta^2
=2\mathcal V_h(z).
\]

这证明全部整数 h 的(1.2)。统一系数1/2不能进一步减小，因为 h=2时取 z=(1,−1)准确取等。本稿没有据此声称每个固定 h 的最佳谱隙都恰为2；许多 h 的实际谱隙严格更大。

整个证明也可写成准确有理平方和。设 q=Σs_i²、k=2ab/h，则相邻边的剩余费用为

\[
\sum_i d_i^2-k\left(\sum_i s_i d_i\right)^2
=\frac1q\sum_{i<j}(s_i d_j-s_j d_i)^2
+\left(\frac1q-k\right)\left(\sum_i s_i d_i\right)^2,
\tag{2.6}
\]

其中 d_i=z_i−z_(i+1)。偶数时第二系数为零，奇数时为ab/h>0。该式用于伴随的精确有限矩阵核对。

## 3. 接回实际 1/n 和非对称细网格

沿用第6轮的全部定义。I=[L,R]为正整数单元，h=R−L，Π是包含真实两端的任意整数细网格。对任意包内实源 b_m，设

\[
U(n)=\sum_{L<m<R}G_{L,R}(n,m)b_m/m,\qquad V=I_\Pi U.
\]

这准确使用原实际网格核；没有另造一个均匀包。定义边索引累计

\[
A_k=\sum_{L<m\le k}b_m,
\qquad B_k=\sum_{L<m\le k}b_m/m,
\quad k=L,\ldots,R-1.
\]

第6轮已证明

\[
\|V_+\|_w^2\le C_\Pi\operatorname{Var}(B),
\qquad
\operatorname{Var}(B)\le\frac{R}{L^2(L+1)}\operatorname{Var}(A).
\tag{3.1}
\]

第二式来自准确Abel矩阵：各行和1/L、最大列和R/[L(L+1)]，并将常数向量映成常数。这些前驱接口在本轮原样复用。

对A应用新谱隙(1.2)，其每条边差就是区间内完整源的和。令

\[
J_{b,I}(d)=\sum_{u=L}^{R-1-d}
\left(\sum_{u<m\le u+d}b_m\right)^2,
\]

便得(1.3)。它对混合符号源、原细网格的任意间隙比例及固定位置都成立。无需假设细节点对齐二进制：二幂边只作用于完整整数累计向量，不要求修改原细节点。

该式仍是无符号均方对正输出的充分上界，不是与正输出目标等价的改写；正负源先在每条实际区间里相加再平方。

## 4. 多单元只需一套共同的 O(log H) 长度

设所有粗单元内部不交，位于整数块 [X,Y]⊂[X,2X]，X≥2，最大长度H。第6轮已证

\[
C_{\Pi,I}\le\frac{h_I^2}{8L_I^2}.
\]

由R_I≤2L_I，(1.3)中系数不超过 h_I²/(8L_I⁴)。对每个共同二幂长度d，各单元用到的中心集合互不相交，且被块内中心集合覆盖。于是

\[
\boxed{
\sum_I\|V_{I,+}\|_w^2
\le\frac{H^2}{8X^4}
\sum_{d\in\mathcal D_H}J_{b,[X,Y]}(d).
}
\tag{4.1}
\]

这次全块只需共同的 \(\lceil\log_2H\rceil\) 个长度，而不是全部1≤d<H。中心仍是所有真实需要的整数中心；没有把中心数量也偷换成O(log H)。单元和细网格可依数据选择，因为不交覆盖是逐输入的确定性事实。

对H≥2，令m=ceil(log₂H)，则

\[
\sum_{d\in\mathcal D_H}d=2^m-1<2H.
\]

若仅在这些二幂长度上有

\[
J_{b,[X,Y]}(d)\le K(X)Xd,
\qquad d\in\mathcal D_H,
\tag{4.2}
\]

便得到

\[
\boxed{
\left(\sum_I\|V_{I,+}\|_w^2\right)^{1/2}
\le\frac{\sqrt{K(X)}}{2\sqrt2}
\frac{H\sqrt{2^{\lceil\log_2H\rceil}-1}}{X^{3/2}}
\le\frac{\sqrt{K(X)}}2(H/X)^{3/2}.
}
\tag{4.3}
\]

若H恰为2的幂，第一式可把根系数进一步写成
`(√K/(2√2))(H/X)^(3/2)√(1−1/H)`。H=1时所有余项为零。

因此减少长度没有付额外的log H因子。它严格缩减了第6轮简化全中心条件要求提供的长度集合，同时保持相同的粗尺度增长类上界。

### 计算费用的明确范围

若完整整数累计源已经取得，计算这些均方只需要O((Y−X)log H)次区间差与平方，长度存储为O(log H)。第6轮枚举全部长度的直接方式需要O((Y−X)H)项。这里减少的是**已知前缀之后**的区间统计工作；取得素数、认证对数、完整道路节点或原始来源的成本仍另计，不宣称端到端次线性算法。

## 5. 普通素数及完整相关匹配的接续

取

\[
b_m=1-\mathbf1_{m\ {\rm prime}}\log m.
\]

则J的第一项是区间内全部整数的准确数量；合数背景不删。r5准确正Green对偶说明(4.1)左侧平方根恰为普通素数预算 \(\mathfrak P_\Pi\)。因此只须对共同二幂长度证明(4.2)，就可得到所需正输出充分上界。

第6轮已核对的整数长度离散/连续恒等式仍然适用。已读取的Languasco–Zaccagnini式(22)在RH下给固定加法长度Ψ均方 `J(T,d)≪dT log²T`；将它限制到二幂长度后当然成立，所以第6轮的**条件**结论

\[
\mathcal E^{1-\Lambda}_\Pi\ll(H/X)^{3/2}\log X
\quad\text{在RH下}
\]

保持。普通素数的高次幂支付、κ背景支付及固定ε>0时H≤X^(1−ε)的条件趋零结论均沿用第6轮。新谱隙定理是无条件有限代数事实；它没有无条件证明普通素数的均方输入。

真实匹配道路的返回也不变。若完整相关半径满足
`||IΠ(q_D−q*)||w, ||IΠ0(q_D−q*)||w≤R_B`，则

\[
|\mathcal E_\Pi(D)-\mathcal E_\Pi(\Lambda)|\le2R_B.
\]

真实粗端点仍包含在第二个完整插值项，完整前史不由本轮区间图删除；粗骨架本身的统一控制仍开放。

## 6. 固定数量长度不能统一保持这条方差谱隙

这一节的必要性只针对**本稿用到的任意实累计向量方差谱隙**，不是对所有可能的素数方法作不可能性声明。

设选取k个长度d_1,…,d_k∈{1,…,h−1}，其全部固定位置边图的谱隙为λ。令

\[
Q=\lfloor(h-1)^{1/k}\rfloor.
\]

对Q^k+1个点
`(j d_1/h,…,j d_k/h) mod1`，j=0,…,Q^k，按Q^k个等立方体分箱。两点落入同一箱，给某个1≤q≤Q^k≤h−1，使全部 \(\|qd_i/h\|\le1/Q\)。

取均值为零的复向量 `z_n=exp(2πiqn/h)`。每种长度只有h−d_i条实际边，故

\[
\sum_i\sum_{n=0}^{h-1-d_i}|z_{n+d_i}-z_n|^2
\le\frac{4\pi^2kh}{Q^2}.
\]

实部或虚部至少有一个的Rayleigh比不超过这个复比，所以

\[
\boxed{\lambda\le\frac{4\pi^2k}{\lfloor(h-1)^{1/k}\rfloor^2}.}
\tag{6.1}
\]

因此任何固定k，不论长度怎样依h选择，都不能在h→∞时保持统一正谱隙。还能得到所需长度数的定量下界。由floor u≥u/2（u≥1），若要求某个固定λ_0>0满足λ≥λ_0，则

\[
\lambda_0\le16\pi^2k\,(h-1)^{-2/k},
\qquad
\boxed{k\log\frac{16\pi^2k}{\lambda_0}\ge2\log(h-1).}
\tag{6.2}
\]

这里log为自然对数。若k≥log(h−1)，下面结论显然成立；否则log(Ck)≤loglog(h−1)+O(1)，代入(6.2)即得

\[
\boxed{k\ge(2-o(1))\frac{\log h}{\log\log h}.}
\tag{6.3}
\]

本轮O(log h)长度给出了一个明确可行的增长长度数；(6.3)与它之间仍有loglog h因子，因此没有证明O(log h)在数量上最优。该必要条件只属于任意实累计向量的统一方差谱隙路线，不能自动转成实际素数Green目标的必要条件。

第6轮已有的单一/相邻宏观长度周期源反例仍有效；本轮二幂集合跨越多个尺度，避免了该例的零空间。

## 7. 最小有限核验与范围

伴随 `verify_sparse_lengths.py` 使用准确分数验证奇偶递归的完整二次型矩阵恒等式、相邻边均值差系数、平方和非负余量，以及少量带实际1/n和非对称整数细网格的源转移。没有采用浮点特征值作正确性依据。

本轮实际通过20个代表长度的完整矩阵恒等式，共65,537个矩阵项；长度包括1、奇数、2的幂及其相邻值，最大为129。此外检查39个新有理源/非对称细网格组合，以及最大粗间隙分别为16和17的两个非均匀多单元覆盖例。所有输入都由脚本中的固定整数与准确分数定义，没有调用真实道路，也没有新增素数筛。

复算只需标准库：

```sh
python research_round7/sparse_lengths/verify_sparse_lengths.py
```

无穷全参数结论由第2节归纳承担，有限矩阵不被外推为证明。原1,270点、原55个子窗以及第6轮全部证书均不重跑。结果文件为 `sparse_length_results.json`。

本轮尚未证明二幂长度上的无条件强普通素数均方；已经证明的是只需这组O(log h)明确长度即可合法接回实际Green预算，且任意整数h不增加额外对数支付。
