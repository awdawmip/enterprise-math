# P001 —— 整数根乘法性的精确条件

状态：`PROVED / LEAN-CHECKED`  
开放问题：`P001`  
范围：普通数学

## 1. 问题

对 \(p\ge1\)，精确刻画何时

\[
R_p(ab)=R_p(a)R_p(b).
\]

令

\[
r=R_p(a),\qquad s=R_p(b).
\]

把两个输入按其坍缩盆地写成

\[
a=r^p+u,
\qquad
b=s^p+v,
\]

其中

\[
u=G_p(a)=a-r^p,
\qquad
v=G_p(b)=b-s^p.
\]

由 P002-T01 与 P002-T02，

\[
0\le u<\Delta_p(r),
\qquad
0\le v<\Delta_p(s),
\]

其中整数盆地宽度记为

\[
\Delta_p(k)=(k+1)^p-k^p.
\]

因此，根的乘法性问题可以精确转化成两个整数盆地乘积中的“进位”问题。

## 2. 整数根总是超乘性

### P001-T01 —— 根的超乘性

状态：`PROVED`

对所有 \(a,b\in\mathbb N\)、\(p\ge1\)，

\[
R_p(ab)\ge R_p(a)R_p(b).
\]

### 证明

因为

\[
r^p\le a,
\qquad
s^p\le b,
\]

所以

\[
(rs)^p=r^ps^p\le ab.
\]

因此 \(rs\) 是定义 \(R_p(ab)\) 时的可容许整数，故

\[
R_p(ab)\ge rs.
\]

证毕。

形式化：已由 `EnterpriseMath.RootMultiplicativity.root_supermultiplicative` 通过 Lean 检查，证明直接使用规范的幂映射/整数根 Galois connection。

所以乘法性失败只可能发生**向上的根进位**，绝不会低于 \(rs\)。

## 3. 精确进位负载

展开乘积：

\[
\begin{aligned}
ab
&=(r^p+u)(s^p+v)\\
&=(rs)^p+s^p u+r^p v+uv.
\end{aligned}
\]

定义盆地乘积的进位负载

\[
L_p(a,b)=s^p u+r^p v+uv.
\]

于是

\[
ab=(rs)^p+L_p(a,b).
\]

在根状态 \(rs\) 之后，下一个可能的根状态阈值位于

\[
(rs+1)^p=(rs)^p+\Delta_p(rs).
\]

对应的 Lean 整数坐标为 `EnterpriseMath.Arithmetic.RootMultiplicativity` 中的 `rootGap`、`basinWidth`、`carryLoad` 与 `offsetLoad`。

## 4. 乘法性的完整刻画

### P001-T02 —— 精确无进位条件

状态：`PROVED`

对所有 \(a,b\in\mathbb N\)、\(p\ge1\)，令

\[
r=R_p(a),\quad s=R_p(b),\quad
u=a-r^p,\quad v=b-s^p,
\]

则

\[
\boxed{
R_p(ab)=rs
\iff
s^p u+r^p v+uv<\Delta_p(rs).
}
\]

等价地，

\[
R_p(ab)=R_p(a)R_p(b)
\iff
L_p(a,b)<\Delta_p(R_p(a)R_p(b)).
\]

### 证明

P001-T01 已给出 \(R_p(ab)\ge rs\)。因此等号成立，当且仅当 \(ab\) 尚未到达下一个 \(p\) 次幂阈值：

\[
R_p(ab)=rs
\iff
ab<(rs+1)^p.
\]

代入

\[
ab=(rs)^p+L_p(a,b)
\]

并减去 \((rs)^p\)，得到

\[
L_p(a,b)<(rs+1)^p-(rs)^p=\Delta_p(rs).
\]

证毕。

形式化：规范判据已由 `EnterpriseMath.RootMultiplicativity.root_mul_eq_iff_carryLoad_lt` 通过 Lean 检查；盆地分解层的算术核心为 `root_product_eq_of_basin_decomposition_iff`，精确乘积展开为 `product_eq_base_pow_add_carryLoad`。

这就是只使用整数的必要且充分条件。

## 5. 乘法根进位量

定义

\[
K_p(a,b)=R_p(ab)-R_p(a)R_p(b).
\]

由 P001-T01，

\[
K_p(a,b)\in\mathbb N.
\]

### P001-T03 —— 进位量的精确刻画

状态：`PROVED`

沿用 \(r,s,u,v\) 的记号，有

\[
K_p(a,b)
=
\max\Bigl\{c\in\mathbb N:
(rs+c)^p-(rs)^p\le L_p(a,b)
\Bigr\}.
\]

特别地，

\[
K_p(a,b)=0
\iff
L_p(a,b)<\Delta_p(rs).
\]

### 证明

对 \(c\in\mathbb N\)，

\[
rs+c\le R_p(ab)
\iff
(rs+c)^p\le ab.
\]

使用 \(ab=(rs)^p+L_p(a,b)\)，等价于

\[
(rs+c)^p-(rs)^p\le L_p(a,b).
\]

取最大的可容许 \(c\) 即得。证毕。

形式化：逐点等价已由 `EnterpriseMath.RootMultiplicativity.le_rootCarry_iff_threshold_le` 通过 Lean 检查；最大值陈述以 Lean 原生序论形式由 `rootCarry_isGreatest` 核验；零进位等价由 `rootCarry_eq_zero_iff` 核验。

所以根乘法性的失败不是模糊的“取整误差”，而是一个精确的整数阈值跨越次数。

## 6. 两个盆地乘积中的结构

固定根状态 \(r,s\) 后，偏移量位于有限矩形

\[
0\le u<\Delta_p(r),
\qquad
0\le v<\Delta_p(s).
\]

在这个矩形中，乘法性成立的条件就是

\[
s^p u+r^p v+uv<\Delta_p(rs).
\]

由于左侧关于 \(u,v\) 都单调，因此无进位区域是一个向下闭合集合。

### P001-T04 —— 乘法区域的向下闭合性

状态：`PROVED`

固定 \(p,r,s\)。若偏移 \((u,v)\) 满足无进位条件，则任意

\[
0\le u'\le u,
\qquad
0\le v'\le v
\]

也满足无进位条件。

### 证明

所有系数与偏移均非负，所以

\[
s^p u'+r^p v'+u'v'
\le
s^p u+r^p v+uv
<\Delta_p(rs).
\]

证毕。

形式化：已由 `EnterpriseMath.RootMultiplicativity.offsetLoad_mono` 与 `noCarry_downward` 以稍强的纯整数形式通过 Lean 检查；向下阈值蕴含本身不需要额外的盆地矩形假设。

因此，每一个盆地矩形中的乘法性区域不是任意散乱分布，而具有单调阶梯边界。

## 7. 用整数除法写出单侧精确边界

设 \(a>0\)，所以 \(r^p+u=a>0\)。把进位负载改写为

\[
L_p(a,b)=s^p u+(r^p+u)v=s^p u+av.
\]

### P001-T05 —— 第二偏移量的最大可容许值

状态：`PROVED`

固定 \(p,r,s,u\)，且 \(a=r^p+u>0\)。若

\[
s^p u\ge\Delta_p(rs),
\]

则不存在任何 \(v\ge0\) 能使乘法性成立。

若

\[
s^p u<\Delta_p(rs),
\]

则无进位条件等价于

\[
v\le
\left(\Delta_p(rs)-1-s^p u\right)\operatorname{//}a.
\]

在实际的 \(s\) 盆地中，最大的可容许偏移因此是

\[
\min\!\left(
\Delta_p(s)-1,
\left(\Delta_p(rs)-1-s^p u\right)\operatorname{//}(r^p+u)
\right).
\]

### 证明

严格整数不等式

\[
s^p u+av<\Delta_p(rs)
\]

等价于

\[
av\le\Delta_p(rs)-1-s^p u.
\]

当 \(a>0\) 时，向下整数除法给出最大的整数 \(v\)；同时盆地本身还要求 \(v\le\Delta_p(s)-1\)。证毕。

形式化：固定成本已越界时的“不存在第二偏移”由 `EnterpriseMath.RootMultiplicativity.no_second_offset_of_width_le_fixed` 核验；精确 floor-division 等价由 `second_offset_noCarry_iff_le_div` 核验，并直接使用 `Nat.galoisConnection_mul_div`；实际盆地上带 `min` 截断的最大值由定义 `maxSecondOffset` 和定理 `maxSecondOffset_isGreatest` 核验。

这把 P001 再次直接连接到 P008 的序伴随/向下整数除法框架。

## 8. 若干重要特例

### 两个因子都是完全幂

若 \(u=v=0\)，则 \(L_p(a,b)=0\)，乘法性总成立：

\[
R_p(r^p s^p)=rs.
\]

### 只有一个完全幂因子并不够

如果只有 \(u=0\)，精确条件变成

\[
r^p v<\Delta_p(rs).
\]

所以，第一个因子是完全 \(p\) 次幂，并**不能**保证乘法性。

平方根下取

\[
a=4,\qquad b=3.
\]

则

\[
R_2(a)=2,\qquad R_2(b)=1,
\]

但

\[
R_2(12)=3>2.
\]

### 最小的平方根进位

取 \(p=2\)、\(a=b=2\)：

\[
R_2(2)R_2(2)=1,
\qquad
R_2(4)=2.
\]

此时 \(r=s=1\)、\(u=v=1\)，并且

\[
L_2(2,2)=1+1+1=3
=\Delta_2(1).
\]

也就是说，进位恰好从负载达到下一个阈值的那一刻开始。

## 9. P001 解决结论

P001 可以由以下精确整数条件完整解决：

\[
\boxed{
R_p(ab)=R_p(a)R_p(b)
\iff
R_p(b)^pG_p(a)
+R_p(a)^pG_p(b)
+G_p(a)G_p(b)
<
\Delta_p(R_p(a)R_p(b)).
}
\]

同时，我们得到非负进位量 \(K_p(a,b)\)，证明每个盆地矩形中的乘法区域向下闭合，并给出固定一侧偏移后的精确 floor-division 边界。

P001-T01 至 P001-T05 现已全部由导入 root surface 的 warnings-fatal Lean build 覆盖，对应模块为 `EnterpriseMath.Arithmetic.RootMultiplicativity`。

整个结论不需要实值归一化，也不需要隐藏分数余量。

## 10. 前人工作纪律

整数 nth root、floor/root 不等式、整数阈值刻画以及向下整数除法都是成熟数学。本轮对当前 mathlib API 与整数根文献的定向检索，没有发现这一精确“盆地偏移—乘法进位阈值”形式的标准命名结果；检索未发现不构成历史优先权证据。

因此 P001-T01–T05 都是从当前定义推出的普通数学 `PROVED / LEAN-CHECKED` 结论；这一精确包装及其历史创新状态继续保持 `NOVELTY_UNVERIFIED`。
