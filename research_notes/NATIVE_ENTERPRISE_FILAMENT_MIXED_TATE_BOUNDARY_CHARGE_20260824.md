# 进取原生 filament survivor basin：Mixed-Tate 边界电荷

Status: `FREE_RESEARCH_EXACT_GROTHENDIECK_CLASS / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-24`

Researcher-ID: `EM-FREE-NEPS-239A6D`

## 一、survivor complement 的 Grothendieck 类

固定长度 \(k\)、特征 \(q>k-1\) 和手性 \(\chi\)。令
\[
X_{k,q}^\chi
=
\mathbb A_{\mathbb F_q}^2
\setminus
\bigcup_{j=0}^{k-1}L_j^\chi
\]
为所有 \(k\) 个 Cell 值均不被 \(q\) 整除的参数 basin。

设 \(b_{k,q}^\chi\) 为零线排列的特征常数。每条线的类为
\(\mathbb L\)，而一个 \(m\)-重交点需要从逐线相加造成的重数中修正
\(m-1\) 个点。因此在
\(K_0(\mathrm{Var}_{\mathbb F_q})\) 中：

\[
\boxed{
[X_{k,q}^\chi]
=
\mathbb L^2-k\mathbb L+b_{k,q}^\chi
}.
\]

所以这个 survivor basin 的 Grothendieck 类是一个精确的 Tate 多项式；其全部局部复杂性压缩在零维整数
\(b\) 中。

## 二、点计数、zeta 与 Betti 数据

对任意扩张次数 \(s\ge1\)：
\[
\#X_{k,q}^\chi(\mathbb F_{q^s})
=
q^{2s}-kq^s+b_{k,q}^\chi.
\]

因此：
\[
Z(X_{k,q}^\chi,T)
=
\frac{(1-qT)^k}
{(1-q^2T)(1-T)^{b_{k,q}^\chi}}.
\]

于是从 Grothendieck 类和点计数看：

- 二维 ambient 项 \(\mathbb L^2\) 相同；
- \(k\) 条零线的一维项 \(-k\mathbb L\) 相同；
- 手性差异只能落在零维常数项 \(b\) 中。

这里不把模 \(q\) 的异常 intersection lattice 自动等同于同一整数方程在特征零中的拓扑类型；当前结论严格停留在有限域 special fiber、其 Grothendieck 类与点计数 zeta 上。

## 三、sharp-nine 的零维手性电荷

对 \(k=9\)：

### 特征 13
\[
b_+=32,\qquad b_-=33.
\]

所以
\[
\boxed{
[X_+]-[X_-]=-[\operatorname{Spec}\mathbb F_{13}]
}.
\]

任意 \(s\ge1\)：
\[
\#X_+(\mathbb F_{13^s})
-
\#X_-(\mathbb F_{13^s})
=-1.
\]

### 特征 23
\[
b_+=32,\qquad b_-=31.
\]

所以
\[
\boxed{
[X_+]-[X_-]=+[\operatorname{Spec}\mathbb F_{23}]
}.
\]

任意 \(s\ge1\)：
\[
\#X_+(\mathbb F_{23^s})
-
\#X_-(\mathbb F_{23^s})
=+1.
\]

因此 sharp-nine 的手性不平衡不是二维 bulk density 的改变，也不是 line 数目的改变，而是一个纯零维边界电荷。

## 四、deletion–restriction 的几何形式

从 \(k\) 条零线增加一条新边界线。设新线与旧 union 相交于
\(s\) 个不同点。

新线实际从 survivor basin 中删去的类为
\[
\mathbb L-s.
\]

所以：
\[
\boxed{
[X_{k+1}]
=
[X_k]-\mathbb L+s
}.
\]

对应：
\[
b_{k+1}=b_k+s,
\]
以及
\[
\delta_{k+1}=\delta_k+k-s.
\]

这说明每一次多 Cell 扩张都分成：

1. 一个普适的一维代价 \(-\mathbb L\)；
2. 一个由 boundary collision 决定的零维返还 \(+s\)。

手性 boundary flux 正是这个零维返还量在左右截断之间的差。

## 五、横向扩张与纵向加精的含义

有限域扩张
\[
\mathbb F_q\to\mathbb F_{q^s}
\]
保持零维电荷，因此绝对手性差始终为 \(\pm1\)。

而在
\[
\mathbb Z/q^a\mathbb Z
\]
中提高 \(q\)-进精度时，first-layer concurrence 会分裂；对 sharp-nine 的
\(q=13,23\)，从 \(a=2\) 开始两手性计数完全一致。

因此：

\[
\boxed{
\text{unramified direction preserves the motivic boundary charge}
}
\]

\[
\boxed{
\text{ramified precision resolves the congruence singularity}
}.
\]

这不是新的经典 prime-distribution 定理，而是由进取原生多 Cell 曲率排列自动产生的一条精确算术几何分叉。
