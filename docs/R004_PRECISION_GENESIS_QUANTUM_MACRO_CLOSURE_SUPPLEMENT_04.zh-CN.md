# R004 精度宇宙生成 —— Supplement 04：ordered scale geometry 与 prime-axis rank

状态：`PROVED_WIP + EXECUTABLE_CHECKED + CANDIDATE_PHYSICAL_INTERPRETATION`  
Parent：`R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_03.zh-CN.md`  
Owner branch：`research/r004-precision-genesis-closure-20260810`

本补充把 geometry 问题进一步具体化：

> 一个 scalar integer precision hierarchy，能否在不预先放入 Euclidean continuum、也不先手工声明 dimension 的情况下生成 connected finite spatial geometry？

答案分成三层。integer order + boundary bridge law 足以精确生成一维 path；多条独立 ordered precision axes 的 Cartesian product 生成 finite grid；最后，unique prime factorization 又给 scalar scale factor 一个规范的 arithmetic axis rank，可以作为 product construction 的候选 seed。前两层属于直接 finite graph construction；把 prime-axis rank 解释成 physical spatial dimension 仍然只是 R004 hypothesis。

## 1. 一般 ordered-boundary path theorem

设

\[
1=d_0\mid d_1\mid\cdots\mid d_t=L
\]

是任意有限 divisibility chain。在 finest carrier

\[
X_L=\{0,1,\ldots,L-1\}
\]

上使用 canonical P005-style projection

\[
\pi_{L\to d}(x)=x//(L/d).
\]

每个 projection fiber 因而都是连续 integer interval。

在每个 parent scale `d_i`，按 integer leaves 的顺序排列 scale `d_{i+1}` 的 immediate child fibers。对每一对相邻 child fibers，只加入一条 **boundary witness edge**：

\[
\max(\text{left child})
\;--\;
\min(\text{right child}).
\]

### Theorem

所有 refinement levels 上的 boundary witness edges 的 union 精确等于

\[
\boxed{
\{\{0,1\},\{1,2\},\ldots,\{L-2,L-1\}\}
}
\]

也就是普通 path graph `P_L`。

### Proof

任取相邻 fine states `k,k+1`。在 root scale `d_0=1` 它们 projection 相同，在 final identity scale `L` 它们必然不同。令 `j` 是第一次 projection 不同的 level。则在前一层它们仍位于同一个 parent fiber，在第 `j` 层进入两个不同 immediate children。由于 projection fibers 都是连续 intervals，而且 `k` 与 `k+1` 之间没有第三个整数，它们必然处于两个相邻 child fibers；`k` 是左 child 的最大 leaf，`k+1` 是右 child 的最小 leaf。因此 boundary rule 精确加入 edge `{k,k+1}`。

更早层级它们尚未分离，所以不会产生该 edge；一旦分离，后续又已位于不同 parent fibers，因此不会在更晚 level 首次产生。于是每条 adjacent fine edge 恰好出现一次，并且不存在 nonadjacent edge。∎

该证明对任意 refinement ratios 都成立，不限于 powers of two。

## 2. Intrinsic path metric

由于 generated graph 就是 `P_L`，其 intrinsic shortest-path distance 为

\[
\boxed{d(i,j)=|i-j|.}
\]

这里复用成熟 path-graph / P012 graph metric 数学。graph 定义本身不使用 real coordinate length；只需要原生 integer order 与 finite quotient-boundary rule。

因此得到一个明确正面结果：

\[
\boxed{
\text{divisibility hierarchy}
+\text{integer order}
+\text{boundary bridge admissibility}
\Longrightarrow
\text{1D finite path geometry}.
}
\]

但新增的两项结构非常重要。hierarchy 单独仍然推不出 path。

## 3. Independent ordered axes 生成 finite grid geometry

现在取 `r>=1` 条彼此独立的 ordered precision axes。第 `i` 条 axis 有自己的 divisibility chain，final size 为 `L_i`。由上一节，每条 axis 都精确生成 path `P_{L_i}`。

取这些 paths 的 Cartesian graph product。fine states 为 tuples

\[
(x_1,\ldots,x_r),
\qquad
0\le x_i<L_i,
\]

primitive edge 每次只改变一个 coordinate 一个 path step。

vertex 数量为

\[
\boxed{|X|=\prod_{i=1}^r L_i.}
\]

primitive edges 数量为

\[
\boxed{
|E|
=\sum_{i=1}^r
(L_i-1)\prod_{j\ne i}L_j.
}
\]

复用 P012 的成熟 lattice/path-product argument，intrinsic distance 精确为

\[
\boxed{
d(x,y)=\sum_{i=1}^r|x_i-y_i|.
}
\]

因此 independent ordered precision axes 可以在没有 hidden Euclidean distance 的情况下生成 finite integer grid。

## 4. Scalar capacity 不能决定 dimension

Product construction 立即给出一个 negative boundary。

完全相同的 16 个 fine states，可以分别组成：

- 一条 length `16` axis：dimension `1`，diameter `15`；
- 两条 length `4,4` axes：dimension `2`，diameter `6`；
- 四条 binary axes：dimension `4`，diameter `4`。

state capacity 全部都是 `16`。

所以

\[
\boxed{
|X|\text{ 或 scalar precision capacity alone}
\not\Rightarrow
\text{spatial dimension or geometry}.
}
\]

若要物理上推出三维，必须找到额外的 independent-axis / rank 结构。

## 5. Scale lattice 内部的 canonical arithmetic rank

positive integer scale 本身通过 unique prime factorization 带有一个规范的有限 rank：

\[
\lambda=\prod_{p\mid\lambda}p^{a_p}.
\]

`lambda` 的每个 divisor 精确对应一个 exponent vector

\[
(e_p)_{p\mid\lambda},
\qquad
0\le e_p\le a_p.
\]

因此 `lambda` 以下的 divisor interval 就是 prime-exponent chains 的 product。定义 **scale-axis rank**：

\[
\boxed{
D_{\mathrm{scale}}(\lambda)
=\omega(\lambda)
=\#\{p:p\mid\lambda\}.
}
\]

这是成熟 arithmetic structure。特别地

\[
D_{\mathrm{scale}}(1)=0.
\]

若 `lambda|mu`，每个整除 `lambda` 的 prime 也必整除 `mu`，所以

\[
\boxed{
D_{\mathrm{scale}}(\lambda)
\le
D_{\mathrm{scale}}(\mu).
}
\]

因此 scale-axis rank 沿 compatible refinement 自动不下降。

## 6. Rank opening 与后续 precision growth

有限链

\[
1\mid2\mid6\mid30\mid60\mid180\mid900
\]

的 exact ranks 为

\[
\boxed{0,1,2,3,3,3,3.}
\]

前三个 nontrivial steps 依次打开 prime support `2`、`2,3`、`2,3,5`。之后的 refinements 只提高已有 prime exponents。

于是得到一个数学上自洽的 pattern：

- precision one：零条 prime axes；
- early refinement 可以提高 arithmetic rank；
- prime support 一旦 stabilizes，precision 仍可通过 exponent growth 继续增长，而 rank 保持固定。

这个 pattern 与 R004 希望的“早期 geometry/rank 打开，后来继续提高 precision”非常相似，但相似性不是 physical identity 的证明。

## 7. Prime-product geometry candidate

若

\[
\lambda=\prod_{i=1}^r p_i^{a_i},
\]

令第 `i` 条 candidate ordered axis 的 side length 为

\[
L_i=p_i^{a_i}
\]

并使用 scale chain

\[
1,p_i,p_i^2,\ldots,p_i^{a_i}.
\]

这些 side lengths 两两 coprime，而且

\[
\prod_i L_i=\lambda.
\]

套用 ordered-axis product construction，就得到一个 finite grid candidate，满足

\[
\boxed{
\text{candidate dimension}=\omega(\lambda),
\qquad
|X|=\lambda.
}
\]

例如：

- `lambda=1`：rank `0`，one-state pregeometry；
- `lambda=2`：rank `1`，axis size `(2)`；
- `lambda=6`：rank `2`，axis sizes `(2,3)`；
- `lambda=30`：rank `3`，axis sizes `(2,3,5)`，`30` vertices，diameter `7`；
- `lambda=60`：rank `3`，axis sizes `(4,3,5)`，`60` vertices，diameter `9`；
- `lambda=180`：rank `3`，axis sizes `(4,9,5)`，`180` vertices，diameter `15`。

prime support stabilizes 后，geometry 仍能继续 refinement，而 candidate dimension 维持三维。

## 8. Critical no-go：为什么恰好只有三个 primes？

Prime-axis construction 消掉了一个手工输入——axis 数量现在可以从 arithmetic scale factor 规范读取——但它同时制造了一个更尖锐的 physical problem。

P005 与 unique factorization 都没有要求 prime support 必须在三个 distinct primes 后停止。未来 refinement 完全可能引入第四个 prime，使

\[
\omega(\lambda)
\]

增加到 4。

因此若要物理上识别

\[
\text{spatial dimension}=\omega(\lambda),
\]

必须额外加入一个 **prime-support stabilization law**。在假设的 three-axis genesis epoch 之后，所有 later refinement factors 都只能使用已经 active 的 prime support。

这是实质 model commitment，也因此是一个有用 kill point。理论必须解释为什么 support stabilizes、为什么 stable rank 正好是 3；仅仅指出 `30=2*3*5` 很方便不构成解释。

## 9. Geometry-to-P016 bridge

Supplement 02 的 threshold-record submodel 使用独立整数 alternative separation `delta`。现在 ordered 与 product geometries 可以内生提供这个 separation：

- 单 ordered axis：`delta=d_path(x,y)=|x-y|`；
- 多 axes：`delta=d_grid(x,y)=sum_i|x_i-y_i|`。

于是 record-overlap law 变成

\[
\boxed{
\eta(x,y;d)
=
\frac{\max(d-d_G(x,y),0)}d.
}
\]

所以在这个 bridge 里，`delta` 不再是独立 fit parameter；它由 geometry 决定。

这马上给出一个 combined negative boundary。同样都是 16-state capacity、record resolution `d=10`，但取 antipodal states 时：

- `P_16`，diameter `15`：`eta=0`；
- `P_4 square P_4`，diameter `6`：`eta=2/5`；
- four-dimensional binary cube，diameter `4`：`eta=3/5`。

所以连 P016 toy prediction 也依赖 internal geometry，而不只是 state count。

剩余自由 physical quantity 是 record resolution `d`，更根本的问题则是 threshold-record law 本身是否真对应实际 apparatus interaction。

## 10. 修正后的 dimensional frontier

R004 现在有一条 finite constructive ladder：

\[
\text{scale divisibility}
\to
\text{ordered quotient fibers}
\to
\text{path geometry}
\to
\text{independent-axis product grid}
\to
\text{candidate axis rank}.
\]

Unique factorization 提供了一个 canonical arithmetic rank candidate。但要闭合成 physical program，同一条 primitive causal law 仍必须同时解释：

1. 为什么 integer order / boundary bridges 是 admissible local relations；
2. 为什么 independent scale directions 对应 spatial directions；
3. 为什么 prime support 恰好 stabilizes 在 3；
4. 为什么同一 geometry 控制 environment-record overlap；
5. 这些 local/causal rules 如何与 Supplements 02-03 的 Bell-locality 与 measurement-independence pressure tests 共存。

这已经比“precision somehow becomes three-dimensional space”窄得多，也更容易被证伪。
