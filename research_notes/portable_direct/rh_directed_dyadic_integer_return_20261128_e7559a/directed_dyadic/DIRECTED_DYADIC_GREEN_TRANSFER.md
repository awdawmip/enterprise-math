# 二幂前向亏缺的准确单调锥不等式与真实 Green 转移

2026-11-28（Asia/Hong_Kong）。共同作者 `EM-DIRECT-E7559A / TASK_RESEARCH`，Activity `RA-D2F111EA1C0D4B1DBEFBC1B4`。控制读取由统筹固定于 Enterprise Math `3d3c3da71c7e20c173de7c55b66c82bcf7aff19e`，全球规范读取 `4b0b44a8caa10502c30f1910980b3765e3e195f6`。本稿延续 P000 / Heartbeat X6 固定原生轴的辅助标量观察，保留完整整数及合数背景、实际 1/n、真实端点和网格；作者推导与有限核验不充当 independent Review 或 formal Result。

直接科学前驱：第7轮 `sparse_lengths/DYADIC_LENGTHS_FOR_FIXED_GREEN.md`。较早 `riemann_matching_isotonic_anchors_20261124/deficit/ISOTONIC_LOCALIZATION.md` 已有单调趋势对原帽正亏缺的非正贡献及加权 PAV 池残差；第6轮 `green_arithmetic/INTERVAL_MEAN_SQUARE_TO_GREEN.md` 已有准确 Abel 转移和原细网格 Green 常数。本稿复用这些接口，新增的是**二幂前向正增量控制反单调锥距离的尖锐不等式**，以及由此在第7轮全部真实 Green 常数中用定向亏缺平方取代无符号平方。

## 1. 主定理：只支付上升方向，常数不变

对整数 h≥1，令

\[
\mathcal C_h=\{v\in\mathbb R^h:v_0\ge v_1\ge\cdots\ge v_{h-1}\},
\quad D_h(z)=\min_{v\in\mathcal C_h}\sum_{i=0}^{h-1}(z_i-v_i)^2,
\]

\[
\mathcal D_h=\{2^j:j\ge0,\ 2^j<h\},
\qquad
Q_h^+(z)=\sum_{d\in\mathcal D_h}\sum_{i=0}^{h-1-d}(z_{i+d}-z_i)_+^2.
\]

当 h=1 时，二幂集合为空且 D_1=Q_1^+=0。对全部 h≥1、全部实向量 z，有

\[
\boxed{D_h(z)\le\tfrac12Q_h^+(z).}\tag{1.1}
\]

对每个 h≥2，常数1/2均不能减小。例如取 z=(0,1,−2,−3,…)，唯一正前向二幂差是 z_1−z_0=1，故 Q_h^+=1，而最优反单调拟合只把前两项合并为1/2，D_h=1/2。

这不是把第7轮无符号谱隙中的平方直接替成正部平方。新的零费用空间是整个反单调锥，而非仅常数；以下证明专门处理这项变化。

## 2. 相邻边的合并引理

若一个向量 p 满足

\[
p_{i+2}\le p_i\quad(0\le i<h-2),\tag{2.1}
\]

则其所有相邻上升对 (i,i+1)，即 p_i<p_{i+1}，互不相交。将每个这样的对换成其算术平均，其余坐标保持，所得 c 全局反单调。

证明：若 (i,i+1) 上升，则 p_{i+2}≤p_i<p_{i+1}，下一对不可能上升。考察任意未合并的相邻接缝 i,i+1，已有 p_i≥p_{i+1}。若左点属于前一个上升对，则其新值为 (p_{i-1}+p_i)/2，且 p_{i-1}≥p_{i+1}；若右点属于下一个上升对，则其新值为 (p_{i+1}+p_{i+2})/2，且 p_i≥p_{i+2}。两个相邻合并对之间则分别用 p_{i-1}≥p_{i+1} 和 p_i≥p_{i+2}。四种情况都给 c_i≥c_{i+1}。

置 d=p−c。若上升对的差为 δ_i=p_{i+1}−p_i>0，则 d 在该对上为 (−δ_i/2,δ_i/2)。因此

\[
\langle d,c\rangle=0,
\quad
\|d\|_2^2=\frac12\sum_{i:\,p_i<p_{i+1}}\delta_i^2
\le\|p\|_2^2.\tag{2.2}
\]

所有这些公式包括奇数 h 和两端未配对点。

## 3. 一个完整 PAV 池上的递归费用

先设 z 的最优反单调拟合是同一常数。减去这个常数后，拟合为0，并有

\[
\sum_i z_i=0,
\qquad
\sum_{i=0}^{k}z_i\le0\quad(0\le k<h-1).\tag{3.1}
\]

这套有限 KKT 条件已由前驱的单调回归证明覆盖；对反单调方向，前缀符号相应反向。它也直接意味着

\[
\langle z,c\rangle\le0\quad\text{对所有 }c\in\mathcal C_h,
\tag{3.2}
\]

因为有限分部求和将其写成非正前缀乘非负相邻降幅。

令 p 是把 z 的偶位置子列和奇位置子列分别投影到反单调锥后的合并向量。记这个乘积锥为 P。正交投影到闭凸锥的齐次变分恒等式给

\[
\langle z,p\rangle=\|p\|_2^2,
\qquad
\|z\|_2^2=D_{\lceil h/2\rceil}(z_{\rm even})
+D_{\lfloor h/2\rfloor}(z_{\rm odd})+\|p\|_2^2.\tag{3.3}
\]

按定义 p 满足(2.1)。用第2节将 p 的互不交上升对平均，得到 c∈C_h，置 d=p−c。结合(3.2)—(3.3)，

\[
\begin{aligned}
\|p\|_2^2
&=\langle z,p\rangle
\le\langle z,p-c\rangle\\
&=\frac12\sum_{i:\,p_i<p_{i+1}}\delta_i(z_{i+1}-z_i)\\
&\le\frac12\sum_{i:\,p_i<p_{i+1}}\delta_i(z_{i+1}-z_i)_+\\
&\le\|d\|_2
\left(\frac12\sum_{i=0}^{h-2}(z_{i+1}-z_i)_+^2\right)^{1/2}\\
&\le\|p\|_2
\left(\frac12\sum_{i=0}^{h-2}(z_{i+1}-z_i)_+^2\right)^{1/2}.
\end{aligned}\tag{3.4}
\]

若 p=0，结论直接成立；否则约去其范数并平方。代入(3.3)得完整池上的递归式。

## 4. 任意输入的递归与二幂归纳

一般 z 的最优反单调拟合由连续常值池组成。在每个完整池上应用第3节，减去该池均值不影响任何差或锥距离。

所有池的距离相加等于 D_h(z)。在偶位置及奇位置上，各池限制构成相应子列的一个连续分段；局部编号的奇偶如有交换，对两项之和没有影响。任意全局反单调拟合限制到每段都可行，所以**各段最优误差之和不超过整条子列的最优误差**。而池内相邻正差费用不超过全部相邻正差费用。因此

\[
\boxed{
D_h(z)\le
D_{\lceil h/2\rceil}(z_{\rm even})
+D_{\lfloor h/2\rfloor}(z_{\rm odd})
+\frac12\sum_{i=0}^{h-2}(z_{i+1}-z_i)_+^2.
}\tag{4.1}
\]

所有长度至少2的前向二幂边，在压缩偶、奇索引后准确成为两条子列的前向二幂边，且方向保持。因此

\[
Q_h^+(z)=Q_{\lceil h/2\rceil}^+(z_{\rm even})
+Q_{\lfloor h/2\rfloor}^+(z_{\rm odd})
+\sum_{i=0}^{h-2}(z_{i+1}-z_i)_+^2.
\]

以 h=1 为起点，将(4.1)归纳，即得(1.1)。整个证明只使用有限维投影和非负平方费用，h 无需是二幂。

## 5. 准确 Abel 矩阵保留反单调锥

令整数单元 I=[L,R]，h=R−L，L≥1。对包内任意实源 b_m，定义边索引累计

\[
A_k=\sum_{L<m\le k}b_m,
\qquad B_k=\sum_{L<m\le k}\frac{b_m}{m},
\quad k=L,\ldots,R-1.
\]

前驱准确 Abel 矩阵 T 满足 B=TA，其中

\[
(Tv)_k=\frac{v_k}{k}+\sum_{m=L}^{k-1}\frac{v_m}{m(m+1)},
\quad
\|T\|_{2\to2}^2\le\frac{R}{L^2(L+1)}.\tag{5.1}
\]

本轮所需的附加观察是，对任意 v，

\[
(Tv)_k-(Tv)_{k-1}=\frac{v_k-v_{k-1}}k.
\tag{5.2}
\]

因此 T 将反单调锥映入反单调锥。选取 A 的最优反单调拟合 v，便得

\[
\boxed{
D_h(B)\le\|T(A-v)\|_2^2
\le\frac{R}{L^2(L+1)}D_h(A).
}\tag{5.3}
\]

实际 1/m 先由恒等式精确保留，再支付矩阵范数；没有把它直接替成1/X。

## 6. 同一真实 Green 目标的定向转移

沿用原 Green 核

\[
G_{L,R}(n,m)=\frac{(\min(n,m)-L)(R-\max(n,m))}{R-L},
\]

\[
U(n)=\sum_{L<m<R}G_{L,R}(n,m)\frac{b_m}{m},
\qquad V=I_\Pi U,
\]

其中 Π 包含真实两端，是任意整数细网格。C_Π 为原闭整数质量/刚度常数；没有内部细节点时 C_Π=0。

对任意反单调边向量 v，其源 v_m−v_{m-1} 非正，Green 核及插值重心均非负，故相应 V^v≤0。于是

\[
V_+\le(V-V^v)_+.
\]

用前驱的 Dirichlet 能量与累计方差恒等式，

\[
\|V_+\|_w^2\le C_\Pi\operatorname{Var}(B-v)
\le C_\Pi\|B-v\|_2^2.
\]

对 v 取小，再用(5.3)与(1.1)，得到

\[
\boxed{
\|V_+\|_w^2
\le C_\Pi D_h(B)
\le\frac{C_\Pi R}{L^2(L+1)}D_h(A)
\le\frac{C_\Pi R}{2L^2(L+1)}
\sum_{2^j<h}J_{b,I}^+(2^j),
}\tag{6.1}
\]

其中

\[
\boxed{
J_{b,I}^+(d)=\sum_{u=L}^{R-1-d}
\left(\sum_{u<m\le u+d}b_m\right)_+^2.
}\tag{6.2}
\]

**正化发生在完整同区间源和之后。** 每条区间内的负项、合数背景、相位及抵消都先保留。式(6.1)是对同一正 Green 输出的充分上界，尚未把它说成等价目标。

## 7. 多单元预算不增加对数损失

设内部不交粗单元位于 [X,Y]⊆[X,2X]，X≥2，最大长度 H。用原常数 C_Π≤h²/(8L²)，并对每个共同长度按实际中心集合不交性相加，得

\[
\boxed{
\sum_I\|V_{I,+}\|_w^2
\le\frac{H^2}{8X^4}
\sum_{2^j<H}J_{b,[X,Y]}^+(2^j).
}\tag{7.1}
\]

若只在这些二幂长度上有 J^+(d)≤K_+(X)Xd，则

\[
\boxed{
\left(\sum_I\|V_{I,+}\|_w^2\right)^{1/2}
\le\frac{\sqrt{K_+(X)}}2(H/X)^{3/2}.
}\tag{7.2}
\]

这些常数与第7轮无符号版本相同；没有新增 log H 费用。H 为二幂时仍可保留准确长度和，将根系数改善为

\[
\frac{\sqrt{K_+(X)}}{2\sqrt2}(H/X)^{3/2}\sqrt{1-1/H}.
\]

各单元及网格可依实际源选择；所用集合覆盖是不交性的逐输入确定性事实。

## 8. 普通素数接口、强度及严格改进的范围

取完整整数源 b_m=1−1_{m prime}log m，则

\[
J_\theta^+(X,d)
=\sum_{u=X}^{2X-1-d}
\big[d-\theta(u+d)+\theta(u)\big]_+^2.
\]

全部整数背景仍准确为 d。第5轮的正 Green 对偶说明(7.1)左侧仍为同一个普通素数测试预算平方；本轮把输入缩到了普通素数的亏缺一侧。高次素数幂在控制实际参考正预算的方向继续只减小输出，背景 κ−1 和完整匹配差仍按原费用承担。

因为 J_θ^+≤J_θ，旧无符号输入自动蕴含新输入。一般源类中这种缩减可以严格：令 b_m≡−1（质量源1−b_m≡2非负），则所有 J_b^+=0、全部 Green 正输出为0，而旧无符号 J_b 为正。这个例子说明新的输入不再支付纯过剩源；它不是普通素数的渐近估计。

由第7轮真实宏观三节点帽及其全部整数尺度的 Mellin 指数，可以立刻将其全整数 X 的 RH 判据中的 K_θ 替换为

\[
K_\theta^+(X)=\max_{2^j<X}J_\theta^+(X,2^j)/(X2^j).
\]

具体地，(7.2)在 X=2m,H=X 时给原宏观正帽根预算≤sqrt(K_θ^+(2m))/2，加原 κ 费用即可。故全整数 X 的统一次多项式 K_θ^+ 上界推出 RH；RH 下原 Selberg 无符号估计又给 K_θ^+=O(log²X)。这一接续复用前驱已证指数，不重复宣称固定帽乘子定理为新。

本轮统筹已经进一步证明仅需窗口 X=2^k：见相邻分支 [DYADIC_WINDOWS_AND_INTEGER_BRIDGES.md](../arithmetic_sampling/DYADIC_WINDOWS_AND_INTEGER_BRIDGES.md) 的定理4.1。其机制是单向平移平均链和跨二幂接缝的真实整数跳跃1，再通过非负 Mellin 实轴奇点得到

\[
\mathrm{RH}\iff K_\theta^+(2^k)=2^{o(k)}
\iff K_\theta^+(2^k)=O(k^2).
\]

该算术锚点论证不依赖本稿的锥距离定理；本稿的用途是把同一个方向性统计以原常数接回任意实际网格的 Green 正预算。两条新证明互相补充，不能仅靠第7轮无符号谱隙自动推得。

本稿未证明真实无界普通素数族的 K_θ^+ 估计。已经证明的是保持方向和完整区间抵消的确定性入口，且在原 Green 预算上不额外损失对数或形状常数。

## 9. 实现和核验

`verify_directed_dyadic.py` 使用标准库准确分数检查：有限字母表下全部输入的 PAV KKT、相邻上升对合并、递归式与主不等式；另检查实际1/n的 Abel 锥保持、任意细网格 Green 能量链及多单元定向覆盖。全部固定输入在脚本内，不调用新素数筛、真实道路点或指数。

本轮脚本实际通过9,840个 `{-2,0,3}` 输入（h=1,…,8）、23,509个完整 PAV 池、32个尖锐等号例、64个实际1/n源、180个细网格及4个不交覆盖例。另可直接看出，一个先前尝试的捷径不足：z=(0,3,1,2)的正二幂边构成四节点路径，普通无向谱隙仅为2−sqrt2，并非2；因此不能把所有当前正边图都视为有谱隙2。本稿的池投影证明不要求这项错误前提。

这些有限检查用于发现实现及端点错误；全部 h 和全部实源的结论由第2—7节的解析证明承担。没有重跑旧证书。运行方式：

```bash
python research_round8/directed_dyadic/verify_directed_dyadic.py
```

相关外部研究存在 directed Poincaré / monotonicity testing 体系，例如 Renato Ferreira Pinto Jr., *Directed Isoperimetry and Monotonicity Testing: A Dynamical Approach*, ECCC TR24-087 Rev.1 (2024)，以及其 Waterloo 博士论文第6章。检索用于核对术语和背景；本稿全部具体不等式均在上文直接证明，不声称该大类方法由本轮首创，也未从那些不同域的定理直接套用本稿常数。

