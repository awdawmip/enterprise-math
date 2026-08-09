# P018 —— 任意幂商映射运输，补充 01

状态：`ACTIVE RESEARCH NOTE`  
范围：整个源盆地严格根下降的精确阈值  
依赖：P018 任意幂两盆地商映射运输  
纪律：纯整数；本结论是 floor division 与整数根盆地边界的精确推论。

## 1. 设置

固定

\[
p\ge1,\qquad k\ge1,\qquad d\ge2,
\]

以及源根盆地

\[
B_{p,k}=\{n:k^p\le n<(k+1)^p\}.
\]

此前任意幂运输定理已经证明，对每个 `n in B_(p,k)`，

\[
R_p(n//d)\in\{j,j+1\},
\qquad
j=R_p(k^p//d)<k.
\]

现在问更强的问题：什么时候源盆地里的**每一个实际状态**在 quotient 后，其 `p` 次根都严格小于 `k`？

## 2. P018-APQ-T03 —— 整盆地严格下降充要条件

状态：`PROVED`。

以下两件事等价：

\[
\boxed{
R_p(n//d)<k
\quad\text{对每个 }n\in B_{p,k}
}
\]

与

\[
\boxed{(k+1)^p\le d k^p.}
\]

### 证明

源盆地在 quotient 后能够产生的最大整数状态是

\[
q_{\max}
=
\left\lfloor\frac{(k+1)^p-1}{d}\right\rfloor.
\]

所有 quotient 状态的根都严格小于 `k`，当且仅当

\[
q_{\max}<k^p.
\]

对正整数 `d`，有精确整数等价

\[
\left\lfloor\frac{A}{d}\right\rfloor<B
\iff
A<dB.
\]

代入

\[
A=(k+1)^p-1,
\qquad B=k^p,
\]

得到

\[
q_{\max}<k^p
\iff
(k+1)^p-1<d k^p.
\]

由于两边都是整数，这又等价于

\[
(k+1)^p\le d k^p.
\]

∎

## 3. 与平方 strict-descent 定理的关系

当 `p=2,d=2` 时，条件变成

\[
(k+1)^2\le2k^2.
\]

对所有整数 `k>=3` 都成立，因此当前 P018 的平方根 strict-descent 结果正是本定理的一个特例。

任意幂版本把结构边界说得更清楚：有限根下降机制本身属于完全幂盆地的一般现象；具体何时跨过根阈值，则由 `p,d` 的整数条件决定。

## 4. 对 quotient 路径的推论

若一条有限 quotient 路径的总除数为

\[
D=\prod_i d_i,
\]

最终状态就是 `Q_D(n)`。因此整条路径最终一定把 `p` 次根降到 `k` 以下，当且仅当

\[
\boxed{(k+1)^p\le D k^p.}
\]

这只是对最终扁平化 quotient 的结论，并不声称每个中间阶段都已经跨过同一根阈值。

## 5. 可执行审计

`power_basin_quotient_window` 现在记录精确的 `strict_root_descent` bit，`whole_basin_strict_root_descent` 直接暴露该判据。

`tests/test_p018_power_basin.py` 在有限指数、盆地指标和除数网格上检查上述等价。有限测试用于审计实现；数学依据是上面的精确证明。
