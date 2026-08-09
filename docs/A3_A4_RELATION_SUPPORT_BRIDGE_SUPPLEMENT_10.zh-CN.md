# A3 ↔ A4 ↔ A2/P023 Bridge — Supplement 10

状态：`ACTIVE RESEARCH NOTE`  
范围：任意深度 witness-count tensor、coefficient convolution，以及到 existence frontier 的精确投影

## 1. 从 two-stage histogram 推广到任意深度

Stage 09 已经确定 two-stage witness-cost histogram 是全部 budgeted common-target counts 的 count-complete state。相同构造可以推广到任意有限 stage depth。

固定 `k>=1`、endpoints `x,z`，以及 A3 zero-relation quotient 上的整数 metric `rho`。

对 represented chain

\[
x=x_0,x_1,\ldots,x_k=z,
\]

定义 exact cost vector

\[
\mathbf a=(\rho(x_0,x_1),\ldots,\rho(x_{k-1},x_k))\in\mathbb N^k.
\]

## 2. B36 — multistage witness-count tensor

定义

\[
\boxed{
H^{(k)}_{xz}(\mathbf a)
=
\#\{\text{从 x 到 z、exact cost 为 }\mathbf a\text{ 的 represented k-stage chains}\}.
}
\]

它是一个从 `N^k` 到 `N` 的 finite-support function。

对 budget vector `r`，定义 admissible represented chains 数量

\[
\boxed{
N^{(k)}_{xz}(\mathbf r)
=
\sum_{\mathbf a\preceq\mathbf r}H^{(k)}_{xz}(\mathbf a).
}
\]

因此完整 multistage count language 就是 exact cost tensor 的 `k` 维 prefix-sum transform。

## 3. B37 — product-poset Möbius inversion

把 `N^(k)` 在 `N^k` 以外扩展为零。反复有限差分即可恢复每个 exact coefficient：

\[
\boxed{
H^{(k)}(\mathbf a)
=
\sum_{\varepsilon\in\{0,1\}^k}
(-1)^{|\varepsilon|}
N^{(k)}(\mathbf a-\varepsilon).
}
\]

所以 all-budget path-count function 与 exact cost tensor 可以只用整数运算彼此恢复。

在有限重新编码意义下，`H^(k)` 是完整 `k`-stage witness-count language 的 P023 task-minimal coordinate。

## 4. B38 — coefficient convolution

令 `H^(p)` 与 `H^(q)` 分别为 prefix/suffix 的 exact count tensors。对 `u in N^p`、`v in N^q`，记 `u||v` 为 concatenation。

则

\[
\boxed{
H^{(p+q)}_{xz}(u\Vert v)
=
\sum_y
H^{(p)}_{xy}(u)
H^{(q)}_{yz}(v).
}
\]

### 证明

任意 `(p+q)`-stage path 在第 `p` stage 处有唯一 split state `y`。固定 `y` 后，每一个 exact cost `u` 的 prefix path 都可和每一个 exact cost `v` 的 suffix path 拼接，数量相乘；再对全部 split states 求和，每一条 represented full path 恰好计数一次。

这是一个以 non-negative integer coefficients 为基础的 associative matrix convolution。

从 one-stage coefficient

\[
H^{(1)}_{xy}(a)=1[a=\rho(x,y)]
\]

出发，即可递归生成任意有限深度 count tensor。

## 5. Generating-function form

引入 stage-labeled commuting variables `t_1,...,t_k`，定义

\[
\boxed{
P^{(k)}_{xz}(t_1,\ldots,t_k)
=
\sum_{\mathbf a}
H^{(k)}_{xz}(\mathbf a)
\prod_{j=1}^k t_j^{a_j}.
}
\]

只要保持 prefix/suffix variable blocks 不混淆，coefficient convolution 就等价于 polynomial-entry matrix multiplication。

这给 count-complete future state 提供一个紧凑 algebraic view，不需要概率或 real-valued weights。

## 6. B39 — existence antichain 是 count tensor 的 idempotent shadow

取 positive support

\[
S^{(k)}_{xz}=\{\mathbf a:H^{(k)}_{xz}(\mathbf a)>0\}.
\]

则 Stage-06 existence frontier 精确等于

\[
\boxed{
F^{(k)}_{xz}
=\operatorname{ParetoMin}(S^{(k)}_{xz}).
}
\]

因此 information projection 为

\[
H^{(k)}
\longrightarrow
1[H^{(k)}>0]
\longrightarrow
F^{(k)}.
\]

第一步删除 coefficient magnitude，第二步继续删除 dominated positive-support costs。

Stage 08 的 antichain convolution 正是更丰富 natural-number coefficient convolution 的 existence/idempotent shadow。

## 7. B40 — geodesic existence collapse 不会自动压缩 witness counts

Stage-06 geodesic theorem 证明，任意有限 depth 的 existence semantics 都可压缩成 endpoint `rho` 与 total budget。但该压缩对 witness-count semantics **不成立**。

取 normalized endpoints `0` 与 `1.5`，所以 direct integer relation distance 为 `rho=2`。

### System A

相同 capacities `20`，totals 为

\[
(0,15,30)
\]

对应 positions `0,0.75,1.5`。exact `(1,1)` split 只有一个 internal witness。

### System B

相同 capacities `20`，totals 为

\[
(0,12,18,30)
\]

对应 positions `0,0.6,0.9,1.5`。exact `(1,1)` split 有两个 internal witnesses。

两个 systems 对该 endpoint pair 都是 geodesic，并且 existence frontier 都是

\[
\{(0,2),(1,1),(2,0)\}.
\]

但 `(1,1)` coefficient 不同。

所以

\[
\boxed{
\text{geodesic future-depth collapse 对 existence 合法，
但不会自动对 multiplicity 合法。}
}
\]

count-sensitive future language 即使在 `Gamma=0` 时也必须保留更丰富 coefficient state。

## 8. 与 P011 和 A4/E001 的连接

### P011

P011 已证明整数 multiplicity structure 可以通过 coefficient spectra/polynomials 表达，并可由整数 inversion 恢复。Stage 10 使用相同的 coefficient-first 方法论，但对象是 path-cost multiplicities，而不是 fiber-size multiplicities。

两条路线应在结构正确的地方共享 algebraic tooling，但保持语义独立。

### A4/E001

A4 relation truth 是 count matrices 的 positive-support shadow；E001 materialized common-target memberships 自然属于 coefficient layer。工程实现可以根据实际输出需要，选择只计算 existence、计算 count，或继续保留 labeled witness identity。

## 9. Future-state ladder

对 staged support，现在得到严格 semantic ladder：

\[
\boxed{
\text{labeled paths}
\Rightarrow
H^{(k)}/P^{(k)}
\Rightarrow
F^{(k)}
\Rightarrow
\text{selected truth bits}
}
\]

每次向下压缩，都只有在 future language 忽略被删除信息时才合法。

这是当前进取数论“状态大小应由已证明的 future distinguishability 决定，而不是默认保留最大细节”原则最清晰的实例之一。

## 10. Prior-art discipline

path-count generating functions、多维 prefix sums、product-poset Möbius inversion 与 polynomial matrix products 都是成熟数学。当前项目特有的研究目标，是把这些工具与 A3-generated support metric、A4 witness semantics 和 P023 task-relative collapse hierarchy 精确整合。

## 11. Executable reference

reference layer 新增：

- 任意深度 exact cost-count histograms；
- budgeted path counts；
- recursive coefficient convolution；
- 从 coefficient support 投影到 Pareto existence frontier；
- geodesic same-existence / different-count regression example。
