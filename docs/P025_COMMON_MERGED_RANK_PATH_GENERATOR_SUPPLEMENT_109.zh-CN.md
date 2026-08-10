# P025 补充 109 —— 跨 Observable 的 Common Merged-Rank Path Generator

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-nonlinear-observable-stage107`  
依赖：P025 补充 104、108  
硬阻断：`NONE`

## 1. cubic response 不意味着 cubic state

Stage108 已证明 quadratic rank energy 存在真正的 third-order action interaction。

但不能据此推出 system state 必须保存 cubic response tensor。

Stage109 回到底层 incidence geometry，构造一个同时适用于 linear area 与 quadratic energy 的共同 generator。

## 2. P025-D50 —— full labelled merged-rank path

把 old thresholds 与 candidate thresholds 合并成带标签 total order

\[
H_1<\cdots<H_m.
\]

对每个 current node `rho_c` 定义

\[
P_c:=\#\{\ell:H_\ell\le\rho_c\}.
\]

对每个 future node `v_j` 定义

\[
Q_j:=\#\{\ell:H_\ell\le v_j\}.
\]

因为 node values nondecreasing，

\[
\boxed{P_0\le\cdots\le P_h\le Q_1\le\cdots\le Q_b.}
\]

这条 weakly increasing integer path 就是 full merged-rank generator。

## 3. P025-T248 —— 从 rank path 重建 selected column ranks

固定 candidate-threshold selection set `I`。

一个 merged rank 为 `q` 的 node，其 active merged thresholds 恰好是前 `q` 个 labels。

因此该 node 的**最终 selected threshold rank** 为

\[
\boxed{
\#\{\text{前 }q\text{ 个中的 old labels}\}
+
\#\{\text{前 }q\text{ 个中 family index 属于 }I\text{ 的 candidate labels}\}.
}
\]

所以 merged rank 加静态 labels 就能重建每个 current/future node 的最终 selected rank。

## 4. P025-T249 —— 一条 path 同时生成 area 与 quadratic energy

一旦所有 selected column ranks 都被恢复，两个 observables 立即得到：

\[
A=\sum r_j,
\]

\[
E=\sum r_j^2.
\]

因此同一条 full merged-rank path 可以生成：

- 所有 activation-area endpoint responses；
- 所有 quadratic-rank-energy endpoint responses；
- 对 independent action selections 求值后得到的完整 Stage108 cubic response polynomial。

primitive state 不需要显式存储 second-order 或 third-order response tensor。

## 5. exact arithmetic realization

对 Stage108 `(q,p)=(3,41)` fixture，不设 old thresholds，candidate thresholds 为

\[
\frac1{10},\frac12,
\]

old/future pressures 为

\[
\frac1{22},\frac{13}{22}.
\]

对应 merged-rank path 只是

\[
\boxed{(0,2).}
\]

从这条 path：

- 选择一个 candidate + future node，future rank 为 `1`，energy 为 `1`；
- 选择两个 candidates + future node，future rank 为 `2`，energy 为 `4`；
- 整个 action-response cube 自动产生 Stage108 的 cubic coefficient `2`。

所以 cubic response 由一条只有两个 entries 的 monotone rank path 生成。

## 6. P025-T250 —— Ferrers path state count

若 merged thresholds 数量为 `m`，declared node positions（current + future）总数为 `n`，任意 incidence matrix 有

\[
2^{mn}
\]

种 Boolean states。

monotone threshold/node incidence state 由长度 `n`、取值于 `0,...,m` 的 weakly increasing rank path 决定。

所以 compatible generator states 恰有

\[
\boxed{\binom{m+n}{n}.}
\]

这再次是 Ferrers/lattice-path count。

## 7. Response order 与 generator dimension

Stages108–109 给出一个非常尖锐的分离：

- quadratic energy response jet：exact worst-case order `3`；
- common incidence generator：每个 node 只需一个 weakly increasing scalar rank。

因此

\[
\boxed{
\text{high response interaction order does not imply high-order primitive state tensor}.
}
\]

response tensor 是 observable algebra 作用于低维 incidence generator 后产生的 derived object。

## 8. 与 Stage104 的关系

Stage104 的

\[
\Gamma_A=(A;L_i;Q_j)
\]

是 full rank path 针对 area observable 的更强压缩。

Stage107 已证明这个 collapse 对 quadratic energy 可以过粗。

所以正确 hierarchy 是

\[
\boxed{
\text{full incidence generator}
\longrightarrow
\text{observable-specific response quotient}.
}
\]

不同 observables 可以允许从同一个 common generator 做不同强度的 collapse。

## 9. 架构后果

minimum-precision architecture 不应把以下三者混成一个对象：

- common state generator；
- observable-specific quotient；
- derived response jet。

三者的 dimension 与 algebraic order 可以完全不同。

## 10. Prior-art / novelty 边界

Ferrers paths、labelled total orders 与 rank reconstruction 都是 classical combinatorics。P025 不单独主张这些概念新颖。

项目侧结果是用它们在 arithmetic pressure test 中严格分离 common incidence-state complexity 与 observable-dependent response order。历史新颖性仍为 `NOVELTY_UNVERIFIED`。

## 11. 可执行资产

新增：

- `src/enterprise_math/abc_merged_rank_path_generator.py`；
- `tests/test_abc_merged_rank_path_generator.py`。

## 12. 下一前沿

Stage110 将保持 operation algebra 与 common rank-path generator 不变，只改变 observable degree，研究 rank moments

\[
M_d=\sum_jr_j^d
\]

的 exact history interaction order。