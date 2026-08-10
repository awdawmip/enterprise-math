# P025 补充 110 —— 任意 Rank Moment 的 Exact Interaction Order

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-nonlinear-observable-stage107`  
依赖：P025 补充 108–109  
硬阻断：`NONE`

## 1. 固定 operation algebra

primitive actions 完全不变：

- 选择 candidate threshold rows；
- 选择/追加 future node columns。

Stage109 的 common labelled merged-rank path 也保持不变。

唯一变化的是 observable。

对整数

\[
d\ge1,
\]

定义 rank moment

\[
\boxed{M_d:=\sum_jr_j^d.}
\]

Stage110 决定它的 exact worst-case action-interaction order。

## 2. P025-T251 —— 上界 `d+1`

对 old node `c`，selected rank 形如

\[
r_c+\sum_i x_i a_{ic},
\]

所以贡献

\[
\left(r_c+\sum_i x_i a_{ic}\right)^d
\]

作为 candidate-threshold variables 的 Boolean polynomial，degree 至多为 `d`。

对 future node `j`，贡献还被 future-column selection bit gated：

\[
y_j\left(R_j+\sum_i x_iC_{ij}\right)^d.
\]

内部 rank polynomial degree 至多 `d`，再乘 `y_j` 最多提高一阶。

因此总和满足

\[
\boxed{\deg M_d(x,y)\le d+1.}
\]

所有 `d+2` 阶及以上 irreducible Boolean finite differences 恒为零。

## 3. P025-CE44 —— 同一条 arithmetic edge 实现所有有限 degree

使用 `(q,p,m)=(3,41,2)` 的 exact P025 dyadic edge

\[
\rho_0=\frac1{22},
\qquad
\rho_1=\frac{13}{22}.
\]

对任意固定 `d>=1`，在两者之间选 `d` 个不同 rational thresholds

\[
\rho_0<U_1<\cdots<U_d<\rho_1.
\]

不需要 old thresholds。

old node 位于所有 candidates 下方，future node 位于所有 candidates 上方，所以在 `x_1,...,x_d,y` 上完整非零 moment response 就是

\[
\boxed{M_d(x_1,\ldots,x_d,y)=y(x_1+\cdots+x_d)^d.}
\]

## 4. P025-T252 —— top coefficient 为 `d!`

对全部 `d` threshold variables 与 future selector `y` 做 mixed Boolean finite difference。

`y` difference 去掉外层 gate，留下

\[
(x_1+\cdots+x_d)^d
\]

的 `d` 重 difference。

squarefree monomial

\[
x_1x_2\cdots x_d
\]

的 coefficient 正是把 `d` 个 factors 排列到 `d` 个不同 variables 的排列数：

\[
\boxed{d!}.
\]

所以

\[
\boxed{\Delta_{x_1}\cdots\Delta_{x_d}\Delta_yM_d=d!\ne0.}
\]

interaction order `d+1` 确实被达到。

## 5. P025-T253 —— exact worst-case order

合并 P025-T251 与 P025-T252：

\[
\boxed{\operatorname{ord}(M_d)=d+1}
\]

在 worst case 精确成立。

前两个 degree 恰好恢复此前 stages：

- `d=1`：activation area，exact order `2`；
- `d=2`：quadratic rank energy，exact order `3`。

executable layer 验证 `d=1,...,5` 的 top coefficient，并验证再高一阶的 difference 为零。

## 6. 固定 operation algebra 下 response order 无界

operation language 与 common incidence generator 都固定，只让 `d` 变化。

由于

\[
\operatorname{ord}(M_d)=d+1,
\]

得到

\[
\boxed{\sup_d\operatorname{ord}(M_d)=\infty.}
\]

因此不存在仅由这套 operation algebra 决定的统一 finite response-jet order。

任何与 declared observable family 无关、硬编码固定 interaction order 的架构，最终都会丢失 future distinctions。

## 7. generator complexity 的类型保持不变

尽管 response order 可以任意高，Stage109 primitive incidence state 始终只是一条 monotone merged-rank path。

同一条 path 先恢复每个 selected rank `r_j`，再局部计算任意 declared moment `r_j^d` 即可。

所以

\[
\boxed{
\text{unbounded derived response order}
\not\Rightarrow
\text{unbounded primitive generator order}.
}
\]

generator 只随 declared threshold/node geometry 增长，而不随 observable algebraic degree 改变类型。

## 8. 架构后果

Stage110 识别出三条独立 precision axes：

1. **generator geometry** —— common merged-rank path；
2. **observable algebra** —— 此处为 moment degree `d`；
3. **operation/trace semantics** —— 声明哪些 action words 与 observations。

required response jet 是三者共同作用后的 derived consequence，不应被当成 primitive state type。

## 9. Prior-art / novelty 边界

powers 的 finite differences、coefficient `d!` 与 polynomial-degree bounds 都是 classical algebra/combinatorics。P025 不单独主张这些结论新颖。

项目侧结果是 exact arithmetic pressure-test family：同一 operation algebra、同一种 incidence generator 下，response-jet order 可以无界增长。历史新颖性仍为 `NOVELTY_UNVERIFIED`。

## 10. 可执行资产

新增：

- `src/enterprise_math/abc_rank_moment_closure.py`；
- `tests/test_abc_rank_moment_closure.py`。

## 11. 下一前沿

Stage111 将把 monomial `r^d` 替换成任意 polynomial observable `P(r)`，检验 leading coefficient 非零且 geometry 提供足够 unresolved candidates 时，exact interaction order 是否为 `deg(P)+1`。