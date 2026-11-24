# C89：三库存移动位置达到单支 Haar 曲线的充要条件

## 1. 原对象与定理

原整数安排仍为 \(2\leq w\leq v\leq c\)，总数 \(N_c=\binom c2\)，
在库存 \(c,c+A,c+B\) 各读取一次原 \(H(0,1)\)，额外的因子 5 全放在第一次
23 更新之前。每次保留同样的 \(p\) 个二进制小数位，三个格原点可独立改变。

设整数序列满足

\[
1\leq A<B=o(c),\qquad B/c^{1/3}\longrightarrow\infty.
\tag{1.1}
\]

定义

\[
D=\sqrt{c/B},\quad \theta=A/B,\quad
p_*(c,B)=\frac74\log_2c+\frac12\log_2(c/B),
\quad L_c=2^{p-p_*(c,B)},
\]

\[
0<L_-\leq L_c\leq L_+<\infty,
\qquad R_c=\frac{A(B-A)}{\sqrt{cB}}.
\tag{1.2}
\]

\(V_c^{\rm full}(\alpha)\) 是允许整个原目录竞争者时的三读数唯一安排比例。
\(\Phi_\theta(L)\) 是 C84–C88 已定义的单源支 Haar 曲线：

\[
\Phi_\theta(L)=2\int_\Delta F_\theta(L^2J(X))\,dX,
\quad \Delta=\{0<y<x<1\},\quad J=|\det d(G,B_1)|,
\tag{1.3}
\]

其中 \(F_\theta(a)\) 对余体积 \(a\) 的 Haar 格和三个独立均匀相位，使用
局部标记 \((u,(1-\theta)u+\theta v,v)\)。这一概率坐标表示保留原整数竞争者，
不改变原生路径状态或观察者。

**定理（锐的移动位置判据）。** 在 (1.1)–(1.2) 下，

\[
\boxed{
\sup_{\alpha\in\mathbb T^3}
\left|V_c^{\rm full}(\alpha)-\Phi_{\theta_c}(L_c)\right|\longrightarrow0
\quad\Longleftrightarrow\quad
\frac{A(B-A)}{\sqrt{cB}}\longrightarrow\infty.
}
\tag{1.4}
\]

等价地，右端可写为

\[
\boxed{\frac{\min(A,B-A)}{\sqrt{c/B}}\longrightarrow\infty.}
\tag{1.5}
\]

必要性更强：若右端不成立，存在一条库存子列及 \(\varepsilon>0\)，使沿该子列

\[
\liminf\ \inf_{\alpha\in\mathbb T^3}
\left[\Phi_{\theta_c}(L_c)-V_c^{\rm full}(\alpha)\right]
\geq\varepsilon.
\tag{1.6}
\]

因此即使逐库存挑选格原点，也不能在这条子列上消去远支造成的真实损失。

本判据的精度范围是固定正的临界倍率紧区间，外间距满足 (1.1)。
它判断何时达到 \(\Phi_\theta\)，不是把临界唯一率改称趋于一。

## 2. 充分性

C88 `bridge/GENERAL_MOVING_POSITION.md` 已证明：对任意移动整数位置，
\(B=o(c)\)、\(R_c\to\infty\) 及 \(L_c\) 位于正紧区间，
都有 (1.4) 左侧。
该定理保留准确二阶有限差商，排除所有宏观远分支，再用移动位置下的局部格
与源相位均匀性求出 \(\Phi_{\theta_c}(L_c)\)。其误差已对原点一致。

此外 \(R_c\leq B^{3/2}/(4\sqrt c)\)，故 \(R_c\to\infty\) 本身蕴含
\(B/c^{1/3}\to\infty\)。本篇把 (1.1) 单列，是为了必要性也在同一个已经建立
局部线性格极限的范围内成立。

## 3. 有界分离只能出现在端点附近

记 \(\ell_c=D^3/c=\sqrt c/B^{3/2}\to0\)。则

\[
R_c=\frac{\theta_c(1-\theta_c)}{\ell_c}.
\tag{3.1}
\]

若 \(R_c\not\to\infty\)，取一条 \(R_c\) 有界的子列。进一步取子列，使

\[
L_c\to L\in[L_-,L_+],\qquad R_c\to r\in[0,\infty).
\tag{3.2}
\]

由 (3.1)，\(\theta_c(1-\theta_c)\to0\)。再取子列后，只有
\(\theta_c\to0\) 或 \(\theta_c\to1\) 两种情形。

若 \(\theta_c\to0\)，

\[
\frac A D=\frac{R_c}{1-\theta_c}\longrightarrow r.
\tag{3.3}
\]

若 \(\theta_c\to1\)，则

\[
\frac{B-A}D=\frac{R_c}{\theta_c}\longrightarrow r.
\tag{3.4}
\]

因此必要性的全部剩余情形都归结为端点附近的有限分离。

## 4. 每个有限端点分离都留下真实正损失

C89 `joint/PAIR_LATTICE_LIMIT.md` 在原谱的一对正规远支上证明了完整联合格
极限。双斜率横截性经准确有理证书验证，并通过连通解析配对域延拓到几乎处处。
该极限把源支线性 Haar 格、远支仿射 Haar 格和三个真实源相位的联合分布求出。

由此得到：若 \(\theta\to0\)、\(A/D\to\tau<\infty\)、\(L_c\to L>0\)，
则存在 \(\varepsilon(L,\tau)>0\)，使

\[
\limsup_c\sup_\alpha V_c^{\rm full}(\alpha)
\leq\Phi_0(L)-\varepsilon(L,\tau).
\tag{4.1}
\]

正损失来自一条实际远分支的仿射格命中概率，不是从相位允许条件直接推测。
这里仅需源支与一条远支的联合极限：额外分支只会增加碰撞。

### 首末交换的有限分离版本

原目录不必改写。C88 的准确标记恒等式为

\[
a_1=(1-\theta)a_0+\theta a_2
-\kappa_c\Delta Q_c,
\qquad
\kappa_c=\frac{L_c}{2}\frac{A(B-A)}{BD}.
\tag{4.2}
\]

若 \(\theta\to1\)、\((B-A)/D\to\tau<\infty\)，则
\(\kappa_c\to L\tau/2\)。选定宏观远支后，三标记趋于

\[
(u,v-h,v),\qquad h=\frac{L\tau}{2}\Delta B_2.
\]

交换首末读数坐标及对应源相位，得到 \((v,v-h,u)\)，即与首端相同的模型。
坐标交换保持线性和仿射 Haar 概率；圆周相位使用
\(\sigma_1-\sigma_2\pmod1\)，其微流漂移只改变一个符号。
双斜率横截性、整数平移核及环面非共振证明均保持。
因为 \(B/c\to0\)，所需有限谱极限仍是同一 \(G,B_1\)。

故 (4.1) 对末端有限分离同样成立。结合 (3.3) 或 (3.4)，每条有界 \(R_c\)
子列都出现严格损失。

C85 的端点连续性和 \(\Phi_1=\Phi_0\)，连同 \(L_c\to L\)，给
\(\Phi_{\theta_c}(L_c)\to\Phi_0(L)\)。因此 (4.1) 推出 (1.6)，证明必要性。

## 5. 等价尺度及一个同精度对比

置 \(m_c=\min(A,B-A)\)。因 \(0<m_c/B\leq1/2\)，

\[
R_c=\frac{m_c}{D}\left(1-\frac{m_c}{B}\right),
\qquad \frac{m_c}{2D}\leq R_c\leq\frac{m_c}{D}.
\]

这证明 (1.4) 与 (1.5) 的等价性。

例如取 \(B=\lceil c^{1/2}\rceil\)，则 \(D\sim c^{1/4}\)，
\(p_*(c,B)=2\log_2c+o(1)\)。两种中间库存使用相同的原安排、外端库存与位数：

| 中间增量 \(A\) | 分离尺度 | 在临界倍率范围内的结论 |
|---|---|---|
| \(\lceil\kappa c^{1/4}\rceil\)，固定 \(\kappa>0\) | \(A/D\to\kappa\) | 全库存唯一率与端点曲线保持正距离 |
| \(\lceil c^{1/4}\log\log c\rceil\) | \(A/D\to\infty\) | 全库存唯一率原点一致追踪 \(\Phi_0(L_c)\) |
| \(1\) | \(A/D\to0\) | 仍有严格正的远支损失 |

当机械取整使 \(L_c\) 不收敛时，结论按 (1.4) 直接追踪 \(L_c\)；
有限分离的正距离可对子列取极限。固定分离值与倍率紧区间的统一正距离，
也可由联合格损失积分的连续正性及紧性取得。

## 6. 证明状态

本篇把 C88 已证的全移动位置充分性，与 C89 双分支联合格的有限分离严格损失
合成充要判据。新的逻辑步骤是 (3.1)–(3.4) 的端点子列归约、首末对称有限
分离论证及必要性结论。双分支联合格、两处准确算术核验、谱例外弧的证明与
项目内交叉核查分别保存在本轮对应文件中。

一般有限 \(\tau\) 下全库存唯一率的单一极限公式，仍需同时处理更多宏观支。
本定理的必要性不依赖那个全纤维公式。
