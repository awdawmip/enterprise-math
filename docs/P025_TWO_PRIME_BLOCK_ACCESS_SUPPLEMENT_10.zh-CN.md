# P025 补充 10 —— `1+qr=p^m` 的 Exact Access Formula

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner：`program/p025-abc-support-collapse`  
依赖：P025 补充 05、09  
Hard block：`NONE`

## 1. 结构化 family

假设存在实际 primitive relation

\[
\boxed{1+qr=p^m}
\]

其中 `p,q,r` 两两不同且均为素数，`m>=1`。

`qr` squarefree，所以补充 05 已经给出

\[
\boxed{\eta_{\min}=m.}
\]

本补充进一步把对应的 floor-access radius `nu` 精确求出：三坐标系统可以化成一个二变量 Diophantine minimization。

## 2. P025-T28 —— Floor slice 退化成一个 Bezout 方程

采用 coordinate order `(q,r,p)`。raw additive row 为

\[
\alpha=(r,q,-m p^{m-1}),
\]

而 `W(1,qr)` 的 raw Wronskian row 为

\[
\beta=(r,q,0).
\]

令

\[
H=m p^{m-1}.
\]

两个非零 cross minors 为

\[
Hr,
\qquad
Hq,
\]

由于 `gcd(q,r)=1`，它们的 gcd 恰好是

\[
d=H.
\]

一个 positive-generator floor witness 必须满足

\[
\alpha\cdot x=0,
\qquad
\beta\cdot x=H.
\]

两式相减得到

\[
-Hx_p=-H,
\]

所以

\[
\boxed{x_p=1.}
\]

剩余方程就是

\[
\boxed{r x_q+q x_r=H.}
\]

因此

\[
\boxed{
\nu
=
\max\left(
1,
\min_{ru+qv=H}
\max(|u|,|v|)
\right).
}
\]

这是一个完全精确、无需 witness-lattice enumeration 的公式。

## 3. P025-T29 —— Universal triangle lower bound

若

\[
ru+qv=H
\]

且

\[
B=\max(|u|,|v|),
\]

则

\[
H
\le r|u|+q|v|
\le(r+q)B.
\]

所以

\[
\boxed{
\nu
\ge
L(q,r,p,m)
:=
\max\left(
1,
\left\lceil\frac{m p^{m-1}}{q+r}\right\rceil
\right).
}
\]

这个 lower bound 取等，当且仅当正方形

\[
[-L,L]^2
\]

内存在整数点落在直线

\[
ru+qv=H
\]

上。

因为全部整数解构成 one-dimensional affine lattice，所以是否取等可以用补充 09 同样的 integer interval-intersection calculus 精确判定。

## 4. P025-T30 —— Exact finite solver

由于 `gcd(q,r)=1`，先取一个 Bezout solution `(u_0,v_0)` 满足

\[
ru+qv=H.
\]

全部解为

\[
\boxed{
(u,v)
=(u_0,v_0)+k(q,-r),
\qquad k\in\mathbb Z.
}
\]

对候选 radius `B`，条件

\[
|u_0+kq|\le B,
\qquad
|v_0-kr|\le B
\]

分别给出参数 `k` 的两个整数区间；二者有公共整数点，当且仅当 `B` 可行。

从 triangle lower bound 开始，再用任意 particular solution 给出的有限 upper bound，通过整数二分即可得到 exact optimum。

因此整个 family 只需要：

- extended gcd；
- integer floor/ceiling division；
- interval intersection；
- 对初始 upper radius 做对数数量级的 feasibility checks。

## 5. 取等例子 —— `1+15=16`

这里

\[
q=3,
\qquad
r=5,
\qquad
p=2,
\qquad
m=4,
\]

所以

\[
H=4\cdot2^3=32.
\]

lower bound 为

\[
L=\left\lceil\frac{32}{3+5}\right\rceil=4.
\]

balanced solution

\[
5\cdot4+3\cdot4=32
\]

恰好达到它。因此

\[
\boxed{
\eta_{\min}=4,
\qquad
\nu=4.
}
\]

在 `(q,r,p)` coordinates 中，一个 floor witness 为

\[
\boxed{(4,4,1)}.
\]

## 6. Strict-gap 例子 —— `1+511=512`

这里

\[
511=7\cdot73,
\qquad
512=2^9,
\]

所以

\[
H=9\cdot2^8=2304.
\]

triangle bound 为

\[
L
=
\left\lceil\frac{2304}{7+73}\right\rceil
=29.
\]

但 `[-29,29]^2` 中不存在整数解。exact interval solver 得到

\[
\boxed{\nu=33.}
\]

例如

\[
73\cdot33+7\cdot(-15)=2304.
\]

因此

\[
\boxed{
\eta_{\min}=9,
\qquad
L=29<\nu=33.
}
\]

所以即使在高度结构化 family 中，continuous triangle lower bound 与真正整数 optimum 之间仍可能存在不可消除的**integrality access gap**。

## 7. 一个 family 内部的三种独立 obstruction

对 `1+qr=p^m`，certificate problem 可以拆成：

1. **arithmetic absorption obstruction**
   \[
   \eta_{\min}=m;
   \]
2. **continuous balancing lower bound**
   \[
   L=\lceil H/(q+r)\rceil;
   \]
3. **integrality access defect**
   \[
   \boxed{\Gamma_{\rm int}=\nu-L\ge0.}
   \]

两个样例分别体现：

- `1+15=16`：`Gamma_int=0`；
- `1+511=512`：`Gamma_int=4`。

这比把全部 certificate difficulty 压成一个 norm 更精确。

## 8. 与 P025 更广 precision chain 的关系

现在可写成：

\[
\boxed{
\text{support/valuation data}
\to
\eta_{\min}
\to
\text{continuous access lower bound}
\to
\text{integer access defect}
\to
\nu
\to
\text{full Pareto frontier}.
}
\]

对这个 special family，前四级都已经有显式有限算术公式或 exact one-dimensional solver。

## 9. 成熟数学边界

本阶段使用的都是标准工具：

- linear Diophantine equations；
- Bezout parameterization；
- affine integer line 上的 `L_infinity` minimization；
- triangle inequalities；
- interval intersection。

P025 不对这些工具本身提出 priority claim。这个 family 的价值在于，它让项目中的 arithmetic obstruction、continuous bound 和 integer access defect 三者完全显式分离。

## 10. 可执行资产

新增：

- `src/enterprise_math/abc_absorption_two_variable.py`
  - generic exact `A*u+B*v=N` minimum-`L_infinity` solver；
  - triangle lower bound；
  - `1+qr=p^m` structured specialization。
- `tests/test_abc_absorption_two_variable.py`
  - generic sharp example；
  - `1+15=16` equality case；
  - `1+511=512` strict integrality-gap case；
  - invalid/unsolvable input boundaries。

## 11. 下一前沿

不存在 hard block，继续：

1. 用 modular interval criterion 精确刻画 `Gamma_int=0`；
2. 寻找只依赖 `q,r` 的 `Gamma_int` closed bounds；
3. 搜索 concrete prime-power families 中 `Gamma_int` 或 `delta_abs` 是否可以无界增长；
4. 把同样 decomposition 推广到 `1+b=p^m` 且 `b` 有两个以上 prime factors 的情况；
5. 在得出任何 abc-quality 结论前，把这些 exact access defects 与 Pasten Geometry-of-Numbers norm bounds 做严格比较。
