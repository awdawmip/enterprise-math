# Causal Composition Shadows —— 从 LEGO 拼接与 Witness Matching 导出传统代数复合

状态：`ACTIVE CROSS-ROUTE RESEARCH WIP / EXACT FINITE DERIVATIONS`

## 1. 目的

本文件收束一个统一纠偏：不能因为 `convolution / semiring / matrix multiplication` 是成熟数学，就把它们直接放进进取数论 foundation。

当前因果顺序是：

\[
\boxed{
\text{fine possibilities / witnesses}
\to
\text{实际 composition law}
\to
\text{observation / counting}
\to
\text{传统 algebra shadow}.
}
\]

## 2. 两种最基本的 finite LEGO composition

### Alternative

两个互斥可能性族：

\[
A\sqcup B.
\]

### Joint product

两个独立 choice 同时发生：

\[
A\times B.
\]

它们在 fine-state 层已经有：

\[
A\times(B\sqcup C)
\cong
(A\times B)\sqcup(A\times C).
\]

这是 finite-state bijection，不是先验代数公理。

## 3. CS-01 —— observation 决定 algebra shadow

若某个 observation `Phi` 尊重 structural composition：

\[
\Phi(A\sqcup B)=\Phi(A)\oplus\Phi(B),
\]

\[
\Phi(A\times B)=\Phi(A)\otimes\Phi(B),
\]

则 fine-state 层的结合/分配/单位同构会迫使 `oplus/otimes` 在可达 observation image 上满足相应 semiring-like laws。

已严格出现：

- counting: `(+ , ×)`；
- minimum additive cost: `(min , +)`；
- existence: `(OR , AND)`。

因此：

\[
\boxed{
\text{semiring-like law}
=
\text{LEGO alternative/product 经 compositional observation 的 shadow}.
}
\]

generic semiring 仍可作为成熟计算语言，但不需要先作为 ontology。

## 4. CS-02 —— 底层 singleton 与 algebraic identity 不能混同

底层 joint-product neutral object 是一个 singleton possibility。

counting observation 读取它为：

\[
1.
\]

但 minimum-additive-cost observation 若该 singleton cost 为零，则读取：

\[
0.
\]

所以传统 algebra 中的 `0/1` 是 observation-dependent identity values；不能倒过来解释底层 LEGO unit `1`。

这进一步保护：

> `1` 本身仍是 `1`，传统代数的单位元符号只是某种 shadow 中的角色。

## 5. CS-03 —— matrix multiplication 来自 exact witness matching

一个有限 causal correspondence：

\[
X\xleftarrow{}R\xrightarrow{}Y
\]

的 witness multiplicity：

\[
\kappa_R(x,y)=\#\{r\in R:r\text{ connects }x,y\}.
\]

再有：

\[
Y\xleftarrow{}S\xrightarrow{}Z.
\]

两步 composite witness 是一对 `(r,s)`，要求中间 **exact signature class** 相同。

因此 counting 自动给：

\[
\boxed{
\kappa_{S\circ R}(x,z)
=
\sum_{y\in Y}
\kappa_R(x,y)\kappa_S(y,z).
}
\]

传统 nonnegative-integer matrix multiplication 是 exact witness fiber-product 的 counting shadow。

## 6. CS-C01 —— 形状能乘不代表因果上能乘

若把两个 future-distinct middle states：

\[
y_0,y_1
\]

提前坍缩成同一个 coarse label `Y`，而：

- incoming witness 只到 `y0`；
- outgoing witness 只从 `y1` 出发；

fine world 根本没有可拼的 two-step witness。

但若只把 multiplicity 都推到 `Y`，传统矩阵乘法会制造一个虚假的 cross pairing。

因此：

\[
\boxed{
\text{matrix shape compatibility}
\not\Rightarrow
\text{causal composability}.
}
\]

中间 quotient 必须先证明 future-safe。

## 7. CS-04 —— future-safe quotient 后也不能盲目“两边都求和”

即使 `y0,y1` 对未来拥有完全相同 continuation profile，把它们合并以后：

- incoming multiplicity 应求和，因为 coarse state 确实吞掉多个 incoming witnesses；
- outgoing transition 不应再把两个相同 continuation profiles 求和，而应保存一个**共同诱导 future profile**。

否则 fiber multiplicity 会被重复乘一次。

所以 exact coarse composition 是：

\[
\boxed{
\text{coarse incoming multiplicity}
\times
\text{induced common continuation profile}.
}
\]

这与 P023 的 operation descent / P021 witness necessity 是同一规则。

## 8. CS-05 —— coupling kernel 与 weighted convolution

对两个 LEGO fibers 的 joint→marginal forgetting，定义 local integer coupling multiplicity：

\[
\kappa(u,v)
=
\#\{\text{joint causal states over child pair }(u,v)\}.
\]

则：

- `kappa=0`: child pair 不可达；
- `kappa=1`: independent pairing；
- `kappa>1`: 同一 child pair 上存在 extra cross-future distinctions。

联合 counting：

\[
H_{AB}(c)
=
\sum_a\sum_{u\in F_m(a)}\sum_{v\in F_n(c-a)}\kappa(u,v).
\]

若 `kappa` 只依赖 child totals：

\[
\boxed{
H_{AB}(c)
=
\sum_a
\kappa(a,c-a)H_m(a)H_n(c-a).
}
\]

于是传统 weighted convolution kernel 被重新解释为 causal multiplicity shadow：

- kernel 恒 `1`: independent convolution；
- `0/1`: support-constrained convolution；
- 一般非负整数：multiple joint signature multiplicity。

## 9. CS-C02 —— 单层 kernel 不保证多层可组合

若某个 marginal pair 上有两个 joint witnesses `j1,j2`，仅记录：

\[
\kappa=2
\]

会丢掉它们各自连接哪些后续 states。

如果 continuation profiles 不同，多步 composition 必须保留 witness incidence 或更细 signature quotient。

只有当同一 coarse fiber 内所有 witnesses 的 continuation profiles 完全一致时，匿名 identity 才可安全删除，并有：

\[
\boxed{
\kappa_{next}(r,c)
=
\kappa(r)n(r,c).
}
\]

因此 coupling kernel 本身也服从 P021/P023 future-safe gate。

## 10. 统一解释

目前传统工具的地位开始统一：

- convolution：fiber split 的 counting shadow；
- weighted convolution：coupled fiber multiplicity shadow；
- semiring-like laws：alternative/product 在 observation 下的 shadow；
- matrix multiplication：exact witness matching 的 counting shadow；
- coarse matrix operation：只有 quotient-induced future operation 存在时才合法。

共同母结构不是某个代数，而是：

\[
\boxed{
\text{finite causal possibilities}
+
\text{actual composition/witness relation}
+
\text{declared observation}.
}
\]

## 11. 可执行资产

- `causal_fiber_composition.py`
- `lego_partition_fiber.py`
- `causal_signature_coupling.py`
- `causal_coupling_composition.py`
- `causal_correspondence.py`
- 对应 tests。

## 12. 下一步

1. 判断一般 dynamic-programming algebra 是否都能解释为某种 fiber question，而非 foundation；
2. 将 P021 的 witness transport 写成 causal correspondence composition 的一般 safety contract；
3. 研究 graph/radial/material collision 中真正的 composition primitive 是 relation、fiber 还是 correspondence；
4. 对 coupled dimension contraction 建立 `support kernel + split multiplicity + induced future profile` 的最小充分状态；
5. 暂不把 category/semiring/tensor 等成熟抽象提升为 ontology，除非 causal composition 本身强迫它们出现。
