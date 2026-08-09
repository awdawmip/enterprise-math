# P018 — Precision State Core

状态：`SEMANTIC REPLAY / PROVED CORE`  
来源：历史 PR #68 的 State Pair / critical-grid 路线  
当前 owner：`program/p018-precision-v2`  
纪律：本文件只重组已证明结构，不新增数学主张。

## 1. 为什么从 Pair 开始

P018 过去大量 defect 公式使用整数差

\[
h=b-a.
\]

但“两个状态是否相同、是否被某个 observation 合并、两条路径是否得到同一端点”本身并不需要减法。

因此更弱的底层比较对象是

\[
\boxed{(a,b)\in X\times X.}
\]

对任意确定性映射

\[
F:X\to Y,
\]

定义 pair transport

\[
\boxed{F_\times(a,b)=(F(a),F(b)).}
\]

它不要求 `X` 有加法、序、距离或拓扑。

这是成熟的 product-map / kernel-relation 结构。P018 的专门用途，是把它作为**精度路径比较在 numeric defect 之前的最弱层**。

---

## 2. Diagonal 与 kernel

定义 diagonal

\[
\Delta_X=\{(x,x):x\in X\}.
\]

确定性立即给出

\[
F_\times(\Delta_X)\subseteq\Delta_Y.
\]

也就是：一旦一对状态已经真正相同，任何公共确定性后缀都不能把它们重新分开。

映射的 kernel relation 为

\[
\boxed{
\ker F
=
\{(x,y):F(x)=F(y)\}
=
F_\times^{-1}(\Delta_Y).
}
\]

因此 P010 的 strict history merge 可以先在 Pair/kernel 层理解，再在需要时加入整数 multiplicity 或 spectrum 坐标。

---

## 3. Difference 是 Pair 的坐标，不是更底层的对象

当状态空间是 `N` 时，Pair 可以无损写成

\[
(a,b)
\longleftrightarrow
(a,h),
\qquad h=b-a\in\mathbb Z,
\]

只需满足

\[
a+h\ge0.
\]

这里出现 `Z` 并不要求把自然状态本体扩成带符号状态；它只是**有向 state difference 的坐标层**。

因此 P006 的 signed physical state 与 P018 的 signed defect 必须继续区分。

---

## 4. Precision critical square

设一个 fine operation、一个 coarse operation 与 projection 组成方块。对同一输入状态 `x`，两条路径的端点记为

\[
a=\pi(F_e(x)),
\qquad
b=F_d(\pi(x)).
\]

P018 首先保留 endpoint pair

\[
\boxed{(a,b).}
\]

方块在该状态严格交换，当且仅当

\[
(a,b)\in\Delta.
\]

若状态有整数坐标，再后置定义 signed holonomy

\[
\boxed{b-a.}
\]

所以数值 defect 是 endpoint-pair failure 的坐标化，不应反过来成为“路径差异”的定义前提。

---

## 5. 2×2 rectangle interchange

考虑两组第一阶段映射 `F_0,F_1` 与第二阶段映射 `G_0,G_1`。令

\[
\begin{aligned}
a&=G_0(F_0(x)),\\
b&=G_0(F_1(x)),\\
c&=G_1(F_0(x)),\\
d&=G_1(F_1(x)).
\end{aligned}
\]

相邻 pair 的拼接仅删除共享中间端点：

\[
(a,b);(b,d)=(a,d),
\]

以及

\[
(a,c);(c,d)=(a,d).
\]

因此：

\[
\boxed{
(a,b);(b,d)
=
(a,c);(c,d)
=
(a,d).
}
\]

这一结果只使用端点相等，不需要任何加法、metric 或 continuum。

Lean 对应模块：

`EnterpriseMath.State.CriticalGrid`。

---

## 6. 整数坐标下的精确 rectangle identity

若四个端点位于 `Z`，则同一个 outer difference 有两种有限 telescoping 分解：

\[
\boxed{
d-a=(b-a)+(d-b)
}
\]

以及

\[
\boxed{
d-a=(c-a)+(d-c).
}
\]

相减得到 rectangle variation identity：

\[
\boxed{
(d-b)-(c-a)
=
(d-c)-(b-a).
}
\]

这只是有限整数恒等式，不是微分、极限或连续曲率。

---

## 7. 关键负边界：outer flatness 不推出 local flatness

必须长期保留以下区分：

\[
\boxed{
\text{outer endpoints equal}
\not\Rightarrow
\text{every local edge defect is zero}.
}
\]

局部非零 defect 可以精确抵消，使最终 outer pair 落回 diagonal。

因此：

- **confluence / same final endpoint** 与
- **every local square commutes**

是不同命题。

这也是 P009 mixed scheduling 与 P010 eventual merge 不能混成一个“全局交换性”概念的原因之一。

---

## 8. 与其它 owner 的边界

### A1 / P010 / P011 / P020

一般 deterministic kernel、coalescence、stabilization 属于 A1。P018 只消费这些一般结果，并研究 precision observation 对它们的影响。

### A2 / P023

“什么 observation quotient 对一组 operations/future language 是 congruence”属于 A2/P023 的一般母问题，不在本文件重复。

### P018

P018 长期拥有：

- precision endpoint-pair interpretation；
- critical-square / holonomy 坐标；
- precision projection 下的 defect/transport；
- 与 carry、detail、context separation 的具体接口。

---

## 9. 可执行与形式化资产

Python：

- `src/enterprise_math/state_pair.py`
- `src/enterprise_math/critical_grid.py`

Tests：

- `tests/test_state_pair.py`
- `tests/test_critical_grid.py`

Lean：

- `EnterpriseMath/State/CriticalGrid.lean`

这些资产从历史 PR #68 semantic replay 到 current-main P018 v2；旧 Supplement 编号继续作为 provenance，不再决定长期模块结构。

---

## 10. P018 v2 底层顺序

当前建议的 precision-specific 顺序是

\[
\boxed{
\text{Typed State}
\to
\text{State Pair / Kernel}
\to
\text{optional Difference coordinates}
\to
\text{critical-grid defect / holonomy}
\to
\text{context sufficiency}
\to
\text{operation-specific transport}.
}
\]

这不是新的 Foundation 宣告；它是 P018 v2 当前最小依赖顺序，等待后续 A2/P023 去重与更广 prior-art 审计后再决定哪些部分有资格向更底层提升。
