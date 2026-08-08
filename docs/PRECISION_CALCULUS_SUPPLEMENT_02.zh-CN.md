# P018 —— 有限精度证明演算：补充 02

状态：`ACTIVE RESEARCH NOTE`  
范围：粗精度 cell 证明证书、精化持久性、operation-level naturality defect  
依赖：P018 第一阶段与补充 01

## 1. 从算术恒等式走向证明规则

P018 前两阶段已经建立：

- 精确有限精度纤维；
- 嵌套 detail 与 carry；
- degree-aware transport；
- 带符号 precision shell；
- 有界非线性 naturality defect。

下一步是证明论问题：

> 什么情况下，一个命题可以在低精度上完成证明，而且任何后续精化都不能推翻？

关键在于：粗整数状态不是某个隐藏实数的近似值，而是一个有限显式细状态集合的标签。

## 2. P018-T21 —— 相容精化下的 precision cell 嵌套

状态：`PROVED`

设

\[
d\mid e\mid f.
\]

固定精度 `f` 上的显式状态 `x`。

包含 `x` 的 `d`-cell 为

\[
I_d(x)
=
\left[
R\left\lfloor\frac{x}{R}\right\rfloor,
R\left(\left\lfloor\frac{x}{R}\right\rfloor+1\right)-1
\right],
\qquad R=f/d.
\]

`e`-cell 用 `S=f/e` 同样定义。

则

\[
\boxed{I_e(x)\subseteq I_d(x).}
\]

证明：两个 cell 都是相容欧几里得投影的纤维，而且

\[
\pi_{f\to d}
=
\pi_{e\to d}\circ\pi_{f\to e}.
\]

所以细纤维中的任何状态与 `x` 都有相同的 `d` 投影。∎

这个简单的集合包含关系就是证明持久性的基础。

## 3. P018-T22 —— 有限精度 cell 的单调像包围

状态：`PROVED`

设

\[
F:\mathbb N^m\to\mathbb N
\]

在每个坐标上都单调不减。

对 product precision cell

\[
\mathcal C
=
\prod_{i=1}^m[L_i,U_i],
\]

任意 `x in C` 都满足

\[
\boxed{
F(L_1,\ldots,L_m)
\le
F(x_1,\ldots,x_m)
\le
F(U_1,\ldots,U_m).
}
\]

这里不需要连续性、实数区间、导数或无限完成；它只是有限整数状态上的序关系推论。

这与严格 interval arithmetic 在结构上相邻，而 interval arithmetic 已是明确前人工作。P018 的差别在语义上：这里的 cell 就是实际有限投影纤维，而不是某个未表示实数点的包围。

## 4. P018-T23 —— 阈值证明证书

状态：`PROVED`

考虑命题

\[
P_T(x):F(x)<T.
\]

由 T22 得到 cell 像上下界

\[
L_F=F(L),
\qquad
U_F=F(U).
\]

则恰有三种证明状态：

\[
\boxed{
U_F<T
\Longrightarrow
P_T\text{ 在整个 cell 上为 TRUE};
}
\]

\[
\boxed{
L_F\ge T
\Longrightarrow
P_T\text{ 在整个 cell 上为 FALSE};
}
\]

否则粗精度只能给出

\[
\boxed{\text{UNRESOLVED}.}
\]

这是有限证明规则，而不是启发式判断。

对等式命题 `F(x)=T` 也有对应证书：

- `L_F=U_F=T` 时 TRUE；
- `T` 在 `[L_F,U_F]` 外时 FALSE；
- 其余情况 UNRESOLVED。

## 5. P018-T24 —— 证明证书在精化中永久保持

状态：`PROVED`

若某个阈值命题在精度 `d` 的一个 cell 上已经被证明为 TRUE 或 FALSE，那么根据 T21，所有后续相容精化 cell 都只是它的子集。

因此精化中只能有

\[
\boxed{
\text{TRUE}\to\text{TRUE},
\qquad
\text{FALSE}\to\text{FALSE}.
}
\]

只有

\[
\boxed{
\text{UNRESOLVED}
\to
\{\text{UNRESOLVED},\text{TRUE},\text{FALSE}\}
}
\]

是允许的。

这就是 P018 一般形式的“低精度证明，必要时才提高精度”。

一旦粗精度 cell 已经越过判定边界，证明永久完成；精化不能重新打开已经关闭的证明义务。

## 6. P018-T25 —— 第一阶段序稳定性就是 cell certificate

状态：`PROVED`

对两个一维 precision cell `I_x,I_y`，命题

\[
x<y
\]

若满足

\[
\max I_x<\min I_y,
\]

则在整个 cell 对上恒为 TRUE；若

\[
\min I_x\ge\max I_y,
\]

则恒为 FALSE。

当两个状态的粗商不同，统一欧几里得纤维天然不交并且有序，于是正好恢复 P018-T03。

所以 T03 实际上是一般 coarse-cell certificate calculus 的第一个特例。

## 7. operation-level naturality defect

第二阶段先研究了 monomial。现在可以直接提升到更一般的运算类。

设

\[
F:\mathbb N^m\to\mathbb N
\]

满足：

1. 每个坐标单调不减；
2. 整数 `q`-齐次：

\[
F(rx_1,\ldots,rx_m)=r^qF(x_1,\ldots,x_m)
\]

对所有正整数 `r` 成立。

写细输入为

\[
x_i=ra_i+u_i,
\qquad0\le u_i<r.
\]

## 8. P018-T26 —— 一般单调齐次 defect 界

状态：`PROVED`

定义

\[
\mathcal R_F
=
\left\lfloor\frac{F(x)}{r^q}\right\rfloor
\]

以及

\[
D_F=\mathcal R_F-F(a).
\]

则

\[
\boxed{D_F\ge0}
\]

并且

\[
\boxed{
D_F
\le
F(a+\mathbf1)-F(a).
}
\]

证明：因为

\[
r a_i\le x_i\le r(a_i+1),
\]

由单调性和齐次性得到

\[
r^qF(a)
\le
F(x)
\le
r^qF(a+\mathbf1).
\]

再按 `r^q` 做整数投影。∎

对 Stage 2 的正单项式这类 cell 内严格增长的映射，上边界在半开输入 cell 内不能取到，于是恢复 P018-T16 更紧的 `-1` 上界。

所以 precision defect 已经定义在一个一般运算类上，而不只属于乘法和幂。

## 9. P018-T27 —— 精确 zero-defect certificate

状态：`PROVED`

naturality defect 为零，当且仅当细输出还没有穿过第一个新的粗输出边界：

\[
\boxed{
D_F=0
\iff
F(x)<r^q\bigl(F(a)+1\bigr).
}
\]

这是 operation-level 的**无 carry 证书**。

它统一了：

- 加法 no-carry；
- 乘法 no-cell-crossing；
- root/collapse 的 zero precision defect。

真正重要的不是某个外部“误差估计”，而是细输出是否穿过了一个离散粗边界。

## 10. P018-T28 —— 一般齐次运算恢复单调性

状态：`PROVED`

设

\[
d\mid e\mid f
\]

相容的 degree-1 输入满足

\[
x_f=sx_e+u,
\qquad s=f/e,
\qquad u_i\ge0.
\]

若 `F` 坐标单调不减且 degree `q` 齐次，则

\[
F(x_f)
\ge
F(sx_e)
=
s^qF(x_e).
\]

所以恢复到基础精度 `d` 的结果单调：

\[
\boxed{
\mathcal R_{F;e\to d}
\le
\mathcal R_{F;f\to d}.
}
\]

P018-T19 是 monomial 情形；P018-T12 是 root/power-collapse 情形。

## 11. 证明流程现在成为有限且单向的过程

对单调谓词问题，P018 现在支持如下严格流程：

1. 选择一个粗有限精度；
2. 找到有限 projection cell；
3. 用整数序计算被证明的像区间；
4. 若命题在整个 cell 上恒定，停止；
5. 否则只精化这个 unresolved cell；
6. 已经在粗精度上完成的证书永不重新打开。

这不是“算一个近似答案然后期待收敛”。

它是一串单调缩小的有限证明义务：

\[
\boxed{
\text{大有限纤维}
\supseteq
\text{小有限纤维}
\supseteq\cdots
}
\]

直到判定边界被排除，或者耗尽当前选择的有限精度。

## 12. 精度证明与精度动力学

P018 现在出现两个单调方向。

### 证明不确定性下降

精化时 unresolved cell 缩小；一旦命题被决定，证书永久保持。

### 可恢复非线性结构上升

对单调齐次运算，从更高精度计算后投回粗层，可恢复的粗结构由 T28 单调增加。

这两个单调性并不相同，但同时受 refinement 驱动：

\[
\text{refinement}
\Longrightarrow
\begin{cases}
\text{proof cell 缩小},\\
\text{recoverable nonlinear coarse structure 增长}.
\end{cases}
\]

这比“精度只是参数”更强地表达了：**精度变化本身就是数学动力学。**

## 13. 反例/边界：不是每个运算都有 scale degree

例如

\[
F(x)=x^2+1
\]

虽然单调，但它不是 degree 2 齐次：

\[
F(rx)=r^2x^2+1
\ne
r^2(x^2+1).
\]

它可能在某个具体 cell 上偶然满足一个数值 defect 界，所以可靠的 graded operation theorem 必须显式要求 homogeneity contract；不能因为几个数值样本“看起来像”就把 degree 偷渡进去。

P018 的可执行实现会在使用一般 defect 定理前，检查该 coarse cell 两个缩放角点上的齐次恒等式。

## 14. 与 interval arithmetic 的关系

严格 interval arithmetic 早已能通过传播有限包围来证明数值命题，这一点已经登记为前人工作。

P018 的项目特有之处不在“上下界可以证明命题”这个一般思想，而在以下组合：

- 有限整数 projection fiber 本身就是 precision state；
- 规范整除 refinement；
- 永久 coarse proof certificate；
- graded exact transport；
- 离散 carry / naturality defect；
- 跨尺度带符号 shell cancellation；
- 不要求隐藏实数完成。

这套整体是否能产生标准框架中没有、或显著更短的证明，仍是开放研究问题。

## 15. 第三阶段状态

- P018-T21 precision-cell nesting：`PROVED`
- P018-T22 monotone finite-cell image enclosure：`PROVED`
- P018-T23 threshold proof certificate：`PROVED`
- P018-T24 proof-certificate persistence：`PROVED`
- P018-T25 order stability as cell certificate：`PROVED`
- P018-T26 general monotone homogeneous defect bound：`PROVED`
- P018-T27 exact zero-defect/no-carry certificate：`PROVED`
- P018-T28 homogeneous operation recovery monotonicity：`PROVED`
- 非单调 predicate calculus：`OPEN`
- 自适应 precision selection 最优性：`OPEN`
- 多运算 compositional certificate：`OPEN`
- 用该 certificate calculus 重写 P017：`OPEN`

可执行检查位于 `src/enterprise_math/precision_proof.py` 与 `tests/test_precision_proof.py`。
