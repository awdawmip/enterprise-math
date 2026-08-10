# A2——安全操作代数补充 01：多项式一元操作谱

状态：`PROVED_WIP / EXECUTABLE_CHECKED / NOT CANONICAL_MAIN`  
母文档：`docs/A2_SAFE_OPERATION_ALGEBRA.zh-CN.md`  
范围：作用在 P008 complete-growth interval quotient 上的普通 integer-valued polynomial 自映射 `N_0->N_0`

## 1. 问题

母文档已经把经典的绝对 safe clone

\[
\operatorname{Pol}(\ker q)
\]

与项目真正关心的 natural operation spectrum

\[
\operatorname{Spec}_{\mathcal A}(q)
=
\mathcal A\cap\operatorname{Pol}(\ker q)
\]

区分开来。

第一个真正非平凡的 ambient family，可以取普通 polynomial self-maps：

\[
f:\mathbb N_0\to\mathbb N_0.
\]

本补充对 polynomial complete-growth law 给出完整分类。

结果比 translation theorem 更刚性：

> fixed-block linear growth 仍然保留一个周期平移族；而任何二次及以上 polynomial complete growth，在普通 polynomial unary dynamics 中只允许 constants 与 identity 存活。

## 2. Setup

设

\[
V(0)=0<V(1)<V(2)<\cdots
\]

是在 `N_0` 上取整数值的 polynomial，并以

\[
q_V(n)=k
\iff
V(k)\le n<V(k+1)
\]

定义 P008 level quotient。

记

\[
w_k=V(k+1)-V(k).
\]

一个 unary map `f:N_0->N_0` 安全，当且仅当每一个 source basin 都被完整送入某一个 target basin：

\[
\boxed{
q_V(x)=q_V(y)
\Longrightarrow
q_V(f(x))=q_V(f(y)).
}
\]

对于 monotone `f`，至少必须保证每个 basin 的 image span 能装进一个 target basin。

## 3. A2-SOA-S1-T01——source-span 与 target-width 的渐近比较律

假设

\[
V(k)=c k^p+O(k^{p-1}),
\qquad
c>0,
\qquad
p\ge2,
\]

并令

\[
f(n)=a n^m+O(n^{m-1}),
\qquad
a>0,
\qquad m\ge1,
\]

是 `N_0` 上一个 nonconstant polynomial self-map。

定义

\[
x_k=V(k),
\qquad
y_k=V(k+1)-1.
\]

则

\[
w_k
=cpk^{p-1}+O(k^{p-2}),
\]

并且 `w_k/x_k -> 0`。

当 `m>=2` 时，在一个 basin width 上展开 polynomial，得到

\[
\boxed{
f(y_k)-f(x_k)
\sim
a m p c^m k^{pm-1}.}
\]

当 `m=1` 且 `f(n)=an+b` 时，

\[
\boxed{
f(y_k)-f(x_k)
\sim
acp k^{p-1}.}
\]

再令

\[
\ell_k=q_V(f(x_k)).
\]

由于

\[
f(x_k)
\sim
ac^m k^{pm},
\]

因此

\[
\boxed{
\ell_k
\sim
A k^m,
\qquad
A=(ac^{m-1})^{1/p}.}
\]

于是包含 `f(x_k)` 的 target basin width 满足

\[
\boxed{
w_{\ell_k}
\sim
cpA^{p-1}k^{m(p-1)}.}
\]

若 `f` 安全，则对所有充分大的 `k` 必须有

\[
f(y_k)-f(x_k)<w_{\ell_k},
\]

因为两个 endpoint images 必须仍然落在同一个 target basin 中。

下面的完整分类都由这个比较推出。

## 4. A2-SOA-S1-T02——所有二次及以上 polynomial maps 都不安全

设 `p>=2` 且 `m>=2`。

source basin 的 image span 的增长次数为

\[
pm-1,
\]

而对应 target basin width 的增长次数为

\[
m(p-1)=pm-m.
\]

两者次数差为

\[
(pm-1)-(pm-m)=m-1>0.
\]

所以

\[
\frac{f(y_k)-f(x_k)}{w_{\ell_k}}
\to\infty.
\]

当 `k` 足够大时，一个 source basin 的 image span 已经比其左端 image 所处的整个 target basin 更宽，因此它必然穿过某个 target boundary。

于是

\[
\boxed{
\deg V\ge2,\ \deg f\ge2
\Longrightarrow
f\notin\operatorname{Safe}_1(q_V).}
\]

这比 stage-3 的 fixed-translation no-go 更强：nonlinear polynomial dynamics 的失败，不是某个固定 step 恰好不兼容，而是它在单个 basin 内产生的扩张最终会超过 target basin geometry 自己能够容纳的宽度。

## 5. A2-SOA-S1-T03——斜率至少为二的 affine maps 全部不安全

令

\[
f(n)=an+b,
\qquad a\ge2.
\]

在 `m=1` 时，T01 中

\[
A=a^{1/p}.
\]

所以

\[
\frac{f(y_k)-f(x_k)}{w_{\ell_k}}
\to
\frac{a}{a^{(p-1)/p}}
=a^{1/p}>1.
\]

因此 image span 最终严格大于可用的 target basin width。

故

\[
\boxed{
\deg V\ge2,\ a\ge2
\Longrightarrow
(n\mapsto an+b)\text{ 不安全}.}
\]

## 6. A2-SOA-S1-T04——斜率一精确退化成 translation rigidity

一个从 `N_0` 到自身的 integer-valued affine map，如果正斜率小于二，那么斜率只能是一：

\[
f(n)=n+b,
\qquad b\ge0.
\]

若 `b=0`，它就是 identity，因此安全。

若 `b>0`，二次及以上 polynomial complete growth 的 basin widths 无界。选择一个满足

\[
w_k>b
\]

的 basin。此时 `V(k)` 与 `V(k+1)-b` 仍在同一 basin 中；但加上 `b` 以后，后者恰好到达下一条 boundary，而前者仍留在旧 basin 中。因此 fixed `+b` 不安全。

所以

\[
\boxed{
\deg V\ge2,\ f(n)=n+b
\Longrightarrow
f\text{ safe}\iff b=0.}
\]

## 7. A2-SOA-S1-T05——nonlinear complete growth 的完整 polynomial unary spectrum

任意 polynomial self-map `f:N_0->N_0` 要么是 degree zero，要么具有正 leading coefficient。

- degree zero 就是 constants，永远安全；
- degree 至少二的 maps 被 T02 排除；
- degree one maps 的整数斜率满足 `a>=1`；其中 `a>=2` 被 T03 排除，`a=1` 由 T04 完整分类。

因此，对任意严格增长且取整数值、满足

\[
\deg V\ge2
\]

的 polynomial complete-growth law，普通 polynomial unary spectrum 完整等于

\[
\boxed{
\operatorname{Spec}_{\mathrm{Poly}}(q_V)
=
\{\text{constant maps }\mathbb N_0\to\mathbb N_0\}
\cup
\{\operatorname{id}\}.}
\]

也就是说，所有 `p>=2` 的 polynomial growth degrees 虽然 basin geometries 不同，却具有同一个 polynomial unary safe spectrum。

这又给出一个重要的 reverse-identifiability 边界：

\[
\boxed{
\operatorname{Spec}_{\mathrm{Poly}}(q_V)
\text{ 在 }p\ge2\text{ 后不能反推出 }p.}
\]

若要恢复 growth degree，必须使用更丰富的 operation language 或额外 causal observations。

## 8. A2-SOA-S1-T06——非平凡 fixed block 的完整 polynomial unary spectrum

现在考虑 linear fixed-block law

\[
V_d(k)=dk,
\qquad d>1,
\]

因此每个 basin width 都等于 `d`。

令 `f:N_0->N_0` 为 polynomial。

若 `deg f>=2`，则在 block

\[
[dq,dq+d-1]
\]

上，endpoint span

\[
f(dq+d-1)-f(dq)
\]

随着 `q->infinity` 无界增长，而任何 target block width 始终只有 `d`。所以 `f` 不安全。

若

\[
f(n)=an+b,
\qquad a\ge1,
\]

则安全性强迫

\[
a(d-1)\le d-1,
\]

因此只能有 `a=1`。剩下的 translation

\[
f(n)=n+b
\]

能够精确保持每一个 fixed block，当且仅当

\[
d\mid b.
\]

constants 始终安全。

于是

\[
\boxed{
\operatorname{Spec}_{\mathrm{Poly}}(q_d)
=
\{\text{constant maps}\}
\cup
\{n\mapsto n+jd:j\in\mathbb N_0\},
\qquad d>1.}
\]

当 `d=1` 时 quotient 就是 equality，因此所有 polynomial self-maps 都安全。

## 9. A2-SOA-S1-C01——polynomial-operation phase transition

把 T05 与 T06 合起来，就得到一个很尖锐的 operation-spectrum 跃迁：

\[
\boxed{
\begin{array}{ll}
V(k)=dk,\ d>1:
&\text{constants 加周期 translations }n\mapsto n+jd,\\[4pt]
\deg V\ge2:
&\text{constants 加 identity，除此以外全部消失。}
\end{array}}
\]

因此 stage-3 的 translation rigidity 不是一个孤立的 additive 事实。它恰好是更一般 polynomial-operation collapse 的 degree-one 边界。

它的解释仍然是 causal，而不是 metric：

> nonlinear complete-growth basins 不只是让某个固定 step “不方便”；它们使所有非平凡普通 polynomial unary dynamics 都无法在 level-only state 上精确运行。

若这个 regime 还要存在更丰富的 exact dynamics，就至少必须引入以下某一种结构：

- 保留 basin/detail state；
- 使用适配 quotient geometry 的 non-polynomial operation；
- 使用 domain 不再只是匿名 coarse level 的 typed operation；
- 按实际 action language 自动生成 future-safe refinement。

## 10. 与母文档 no-go 定理的关系

母文档已经证明：普通内部 binary addition 与 multiplication 都会强迫 P008 quotient 退化成 identity。本补充与它互补：

- 母文档约束的是 **multi-input ordinary arithmetic**；
- T05 约束的是 nonlinear complete growth 下整个 **unary ordinary polynomial self-map** 家族；
- T06 则把 linear fixed-block exception 中到底还剩什么完整分类出来。

三者背后的共同原因完全相同：safe operation 必须把一个已经 collapse 的 fiber 整体运输到另一个 collapse fiber；operation 在 fiber 内产生的 image variation 不能超过 target fiber geometry 实际允许的宽度。

## 11. Prior-art discipline

证明只使用 elementary polynomial asymptotics 与经典 quotient-congruence criterion。generic universal algebra 或 transformation semigroup 的一般理论不作为新数学主张。

当前接受 pressure test 的 Enterprise Math 内容，是这个具体的 P008 complete-growth classification，以及把它解释成 natural-operation-spectrum phase transition 的 causal bridge。

## 12. Executable evidence

`src/enterprise_math/safe_operation_algebra.py` 现新增：

- `finite_growth_unary_witness(...)`：一个 exact finite-prefix descent oracle。

`tests/test_safe_operation_algebra.py` 现对以下结构进行 pressure test：

- square complete growth；
- cubic complete growth；
- width five fixed blocks；
- identity 与 constants 作为 surviving controls；
- positive translation、dilation、squaring 作为定理预测应失败的 controls。

bounded oracle 只提供 executable evidence；T02–T06 的数学证明不依赖有限枚举。
