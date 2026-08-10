# P023 / A2 —— Full-Incidence Independence，v3 补充

状态：`PROVED OWNER RESEARCH`  
归属：A2 future-compatible quotient  
依赖：A2 Precision Incidence Core v3

## 1. 定义

令 `X` 为有限状态集，并给定有限 task partitions `E_1,...,E_m`，记 `n_i=|X/E_i|`。若 joint block map 满射：

\[
\boxed{X\longrightarrow\prod_{i=1}^m X/E_i\quad\text{满射},}
\]

就称这族任务 **full-incidence independent**。

等价地，

\[
\boxed{|X/(\cap_iE_i)|=\prod_i n_i.}
\]

这是确定性的有限 realizability 性质，不是概率独立。

## 2. 每个子族也实现完整直积

对任意坐标子集 `S`，

\[
\boxed{|X/E_S|=\prod_{i\in S}n_i,\qquad E_S=\bigcap_{i\in S}E_i.}
\]

因为完整 realized tuple set 投影到任意子坐标后仍然满射。

## 3. 精确 directed repair 公式

对任意坐标子集 `S,T`，

\[
\boxed{\rho(E_S,E_T)=\prod_{i\in T\setminus S}n_i.}
\]

固定一个已实现 `S`-tuple 后，full-product surjectivity 保证真正新增的 `T\S` 坐标上每一种 assignment 都仍由真实 state 实现。

## 4. Uniform repair spectrum

每个 `E_S` block 的 split multiplicity 都相同：

\[
r_{S,T}=\prod_{i\in T\setminus S}n_i,
\]

而 `E_S` blocks 数为 `prod_{i in S} n_i`。所以

\[
\boxed{\mathcal R_k(E_S,E_T)=\left(\prod_{i\in S}n_i\right)\binom{r_{S,T}}k.}
\]

整个 local repair-size distribution 完全 uniform。

## 5. Scheduling 变成 order-independent

若 primitive tasks 逐个取得，那么任何尚未保留的 task `i` 都精确需要 `n_i` 个 repair symbols。因此任意顺序 `sigma` 都满足

\[
\boxed{P_\sigma=\prod_i n_i=|X/(\cap_iE_i)|.}
\]

incidence-capacity slack 恒为 0。固定 base 下总 symbol cost `sum_i L_B(n_i)` 也与顺序无关。若每个 `n_i>=2`，zero-cost dependency closure 也是平凡的。

## 6. Binary 情形：精确 Hamming precision geometry

若所有 `n_i=2`，则

\[
\boxed{\rho(E_S,E_T)=2^{|T\setminus S|}.}
\]

在 base two 下，

\[
\boxed{d_2(E_S,E_T)=|T\setminus S|,\qquad D_2(E_S,E_T)=|S\triangle T|.}
\]

因此由 primitive binary task family 的子集生成的 precision states 精确形成 `m` 维 Hamming cube。primitive-distance-one graph 就是标准 `Q_m`；半径 `r` 的 sphere 大小为 `binom(m,r)`，距离 `r` 的两点间有 `r!` 条最短 coordinate-flip geodesics。

这些 hypercube 结论属于成熟数学；A2 只负责把 repair geometry 精确约化到这个 normal form。

## 7. Pairwise complete 仍然不够

当 `m>=3`，pairwise complete incidence 不推出 full-incidence independence。even-parity / full-cube 的 8-state 反例中，两边的 pairwise binary incidence 都完整，但只有 full-cube 系统实现全部三维 tuples。

所以 full-product independence 是真正的 higher-order 条件。

## 8. Program 推论

只要某条 program 证明一族有限 binary tasks 实现全部 binary patterns，该 family 上的全部 A2 repair/scheduling geometry 就立即退化成上述 Hamming normal form。

P017 的固定有限 least-prime split-bit family 在其 finite-pattern realization theorem 成立后，正好提供一个数论特化。

## 9. 可执行规范

- `src/enterprise_math/a2_full_incidence.py`
- `tests/test_a2_full_incidence_independence.py`

测试覆盖 mixed finite alphabets、精确 product repair factor、uniform repair spectrum 与 binary Hamming 公式。
