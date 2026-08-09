# LEGO Causal Composition Core —— 从一维 Unit Law 生成维度、几何、耦合与未来状态

状态：`ACTIVE CROSS-ROUTE RESEARCH ORIENTATION / STAGE-2 CONSOLIDATION / NOT CANONICAL FOUNDATION`

本文件收束因果吞并第二阶段。它不创建新的 canonical problem 编号，也不修改《我眼中的世界.md》。旧 supplements、P011/P012/P019 文档继续作为证明来源、历史和 specialized results；本文件只给当前最短恢复入口。

## 1. 核心顺序

当前候选 foundation 不再从 vector space、metric、matrix、tensor、semiring 或 precision 出发，而从：

\[
\boxed{
\text{unit possibilities}
\to
\text{LEGO composition}
\to
\text{causal coupling / witness}
\to
\text{continuation type}
\to
\text{observation / grade}
\to
\text{traditional shadow}.
}
\]

`1` 始终是 unit value。升维改变的是 unit 的可摆放关系、可组合 future 和可区分 relation，不改变 `1` 本身。

## 2. 自由 fiber 是第一个母对象

对 `m` 个 slots、总 unit 数 `c`：

\[
\mathcal F_m(c)=\{(a_1,\ldots,a_m)\in\mathbb N^m:\sum_i a_i=c\}.
\]

其计数：

\[
H_m(c)=|\mathcal F_m(c)|=\binom{c+m-1}{m-1}.
\]

但闭式不是基础。真正的 composition law 是：

\[
\boxed{
\mathcal F_{m+n}(c)
\cong
\bigsqcup_{a=0}^{c}
\mathcal F_m(a)\times\mathcal F_n(c-a).
}
\]

它先于任何 convolution/semiring。

## 3. 维度由一维规则反复生成

由于：

\[
H_1(c)=1,
\]

加入一个自由 slot：

\[
\boxed{H_{m+1}(c)=\sum_{a=0}^{c}H_m(a).}
\]

反向删除一个 placement freedom：

\[
\boxed{H_m(c)=H_{m+1}(c)-H_{m+1}(c-1)},
\]

边界取 `H(-1)=0`。

这不是积分/微分近似，而是增加/剥除一个 LEGO slot 的 exact integer law。

## 4. 一般 added-block occupancy law

若新 block 在 occupancy `b` 时有 `k(b)` 个 admissible causal states，并且该规则不读取旧 block 内部身份，则：

\[
\boxed{
G_{m+1}(c)=\sum_{b=0}^{c}k(b)G_m(c-b).
}
\]

若 `G_m(0)=1`，`k` 可无除法唯一恢复：

\[
\boxed{
k(c)=G_{m+1}(c)-\sum_{b=0}^{c-1}k(b)G_m(c-b).}
\]

不同维度 step 恢复出的 `k` 若不一致，则“同一个 context-free 单-slot law 生成整个维度族”被直接证伪。

特例：

- `k(c)=1`：unrestricted occupancy，生成 stars-and-bars family；
- `k(0)=k(1)=1, k(c>=2)=0`：hard single occupancy，生成 binomial family；
- `k(c)>1`：同 occupancy 存在多种内部 relation states。

## 5. Coupling field 改写高维约束

低维 fine pair `(u,v)` 的联合状态 multiplicity：

\[
\boxed{\kappa(u,v)\in\mathbb N_0.}
\]

语义：

- `0`：pairing forbidden / support missing；
- `1`：unique free composition；
- `>1`：同一个 lower-dimensional pair 上存在多个 joint causal states。

固定 coarse total：

\[
\boxed{H_\kappa=H_{free}-M+S},
\]

其中 `M` 是被禁止的 free pairings，`S` 是额外 joint-state multiplicity。`M,S` 必须分开，因为可数值抵消。

因此“挖掉空间”和“增加 relation degeneracy”成为同一 composition law 中方向相反但因果不同的操作。

## 6. Coupling 的最小 future-safe 状态

匿名 `kappa(r)` 对多步 composition 一般不够；完整 witness identity 又太多。

定义当前 witness 在剩余 future language 下的 continuation signature class `tau`，保存：

\[
\boxed{\kappa(r,\tau).}
\]

这就是有限 coupled-fiber 的最小 identity-free counting state 候选。

Composition：

\[
\boxed{N(r,z)=\sum_\tau\kappa(r,\tau)p(\tau,z).}
\]

若每个 `r` 只有一个 `tau`，anonymous `kappa(r)` 才可进一步安全压缩。

有限 deterministic system 中，`tau` 可由 future partition refinement 自动编译。

## 7. Memory 是状态描述不充分的 shadow

当前 coarse label `r` 若包含多个 continuation types：

\[
\#\{\tau:\kappa(r,\tau)>0\}>1,
\]

则过去仍留下会影响未来的差别；若恰有一个 type，则当前 label 已 future-sufficient。

因此最小 memory refinement 是：

\[
\boxed{r\mapsto(r,\tau)},
\]

不是恢复完整 history。

## 8. Identity-free future state 是 type inventory

定义：

\[
n_\tau=\#\{\text{current witnesses of type }\tau\}.
\]

同 type 内 witness rename 不产生新的 causal state。

若 operation 对 disjoint witness families 可加，一个 type-`tau` witness 的 output profile 为 `P_tau(upsilon)`，则：

\[
\boxed{n'_\upsilon=\sum_\tau n_\tau P_\tau(\upsilon).}
\]

传统 nonnegative integer matrix evolution 是这个 inventory propagation 的 coordinate shadow。

## 9. 多 witness interaction 不用 Taylor

若 operation 不对 witness union 可加，对 type-count vector `n` 的任意有限 integer response 可 exact 展开：

\[
\boxed{
\phi(\mathbf n)=
\sum_{\mathbf k\le\mathbf n}
a_{\mathbf k}
\prod_i\binom{n_i}{k_i}.
}
\]

`a_k` 是不可约 LEGO co-presence effect。

- `|k|=1` only：additive / matrix regime；
- 最大 nonzero `|k|=q`：exact q-body regime；
- `min(n,m)` 有任意高阶 nonzero coefficients，因此 traditional piecewise-linear simplicity 不意味着低 causal interaction order。

## 10. Type collapse 的 interaction 判据

若 fine continuation types 合并成 coarse types，fine multi-index `k` 只留下每个 coarse block 内 selected units 总量 `K`。

Response 能 exact descend 当且仅当：

\[
\boxed{a_{\mathbf k}\text{ 只依赖 }\mathbf K.}
\]

所以 future-safe quotient 可以直接从不可约 interaction 是否仍分辨被合并 types 判断。

## 11. Graded LEGO fiber 统一 graph/radial/minimum

给一个 slot 一个 integer grade：

\[
g(x)\in\mathbb N_0.
\]

多 slot 只做：

\[
c=\sum_i x_i,
\qquad
E=\sum_i g(x_i).
\]

定义：

\[
\boxed{
K_{N,g}(c,E)
=\#\{(x_1,\ldots,x_N):\sum x_i=c,\ \sum g(x_i)=E\}.
}
\]

升维：

\[
\boxed{
K_{N+1,g}(c,E)=\sum_x K_{N,g}(c-x,E-g(x)).
}
\]

于是：

- shell = `K(c,E)`；
- ball = `sum_{E<=T}K(c,E)`；
- minimum cost = `min{E:K(c,E)>0}`；
- minimizer multiplicity = minimum occupied shell count。

对 `N=p+1`、`c=0`：

\[
g(x)=|x|
\]

精确重建 P012 `A_p` graph balls（grade budget `2r`）；

\[
g(x)=x^2
\]

精确重建 P019 quadratic shells（grade `2q`）。

而 P019：

\[
\Psi_{m,s}(c)
\]

只是 `g(x)=|x|^s` graded fiber 的最低 occupied grade。

因此 graph/radial/min-plus/minimizer 不再是四套 primitive。

## 12. Coupled graded fiber

joint pair 还可以有 cross-grade shift：

\[
\gamma(u,v)\in\mathbb Z.
\]

于是：

\[
\boxed{
K_{AB}(c,E)
=
\sum_{u,v}
\kappa(u,v)
\mathbf1[c=c_u+c_v,\ E=E_u+E_v+\gamma(u,v)].
}
\]

这里：

- `kappa` = admissibility / multiplicity；
- `gamma` = cross interaction 对 observation grade 的作用。

不能把 support disappearance 与 grade change 混成一个 energy scalar。

## 13. 传统工具的当前地位

已经有 causal derivation / shadow route：

- convolution / semiring；
- matrix multiplication；
- finite tensor/bilinear pair table；
- graph / radial integer balls；
- min-plus minima；
- finite Markov-like state；
- finite interaction order；
- counting measure / collision spectrum。

仍不得自动升级为 core ontology：

- arbitrary real tensor spaces；
- Hilbert tensor products；
- continuous manifolds；
- calculus foundation；
- arbitrary probability measure；
- quantum amplitudes。

## 14. Close-packed geometry 的当前入口

FCC/HCP 尚未被本文件证明或重建。当前只有一个 combinatorial stacking pressure test：相同 local registry/support 的 states 可以因 future stacking continuation 不同而属于不同 `tau`。

因此候选路线是：

\[
\boxed{
\text{free LEGO fiber}
+\text{local packing coupling }\kappa
+\text{continuation type }\tau
}
\]

生成密堆高维结构，而不是预先赋予 `1` 一个 cubic/FCC/HCP coordinate ontology。

## 15. 当前唯一主攻

研究 coupled graded fiber 的 continuation closure：

> 在 `kappa + gamma + continuation type` 下，什么条件允许高维 future 递归只由低维 typed inventories 生成；什么时候必须出现新的 higher-order compatibility witness？

这个问题将决定 pairwise/local LEGO law 能否真正生成任意维，还是必须引入不可约 n-body coupling rules。
