# A3 ↔ A4 Relation-Support Bridge — Supplement 02

状态：`ACTIVE RESEARCH NOTE`  
范围：A3-generated support 诱导的整数 metric，以及 A4 split-completeness 的精确测地判据

## 1. 设置

继续在 Stage 01 的 zero-relation quotient `X0=X/~0` 上工作。对 quotient classes 定义

\[
[i]R_r[j]
\iff
|Z_{ij}|\le r m_i m_j,
\qquad r\in\mathbb N.
\]

Stage 01 已证明 `(R_r)` 在 radius zero 时是 identity，随半径单调，对称，并且关系复合满足次可加性。

因此，这个 support family 在任何两个 quotient states 之间都存在一个规范的最小整数半径。

## 2. B07 — 规范整数 relation metric

定义

\[
\boxed{
\rho([i],[j])
=
\min\{r\in\mathbb N:[i]R_r[j]\}.
}
\]

等价地，只用整数运算可写成

\[
\boxed{
\rho([i],[j])
=
\left\lceil\frac{|Z_{ij}|}{m_i m_j}\right\rceil
=
\frac{|Z_{ij}|+m_im_j-1}{m_im_j}
\text{（最后一步使用 floor division）}.
}
\]

不需要保存任何 rational-valued state；最后一个表达式就是精确的整数 ceiling division。

### B07a — metric 公理

`rho` 是 `X0` 上的整数 metric。

1. `rho>=0` 来自定义；
2. `rho([i],[j])=0` 当且仅当 `Z_ij=0`，也即在 zero quotient 上 `[i]=[j]`；
3. 对称性来自 `Z_ij=-Z_ji`；
4. 三角不等式来自 Stage 01 的 support 次可加性。如果 `rho(i,j)=a`、`rho(j,k)=b`，则 `(i,j) in R_a`、`(j,k) in R_b`，所以 `(i,k) in R_(a+b)`，从而
   \[
   \rho(i,k)\le a+b.
   \]

因此

\[
\boxed{R_r=\{(x,y):\rho(x,y)\le r\}.}
\]

A3-generated A4 support 正是这个整数 metric 的 radius filtration。

## 3. Unit-support graph

定义无向图 `G1`：顶点为 `X0`，两个不同状态 `x,y` 在且仅在

\[
\rho(x,y)=1
\]

时相邻。

令 `d_G1(x,y)` 为通常的 shortest-path distance；如果没有 unit-edge path，则记为 `infinity`。

任何长度为 `L` 的 unit-edge path 都由 metric 三角不等式给出

\[
\rho(x,y)\le L.
\]

因此只要 `d_G1` 有限，就有

\[
\boxed{\rho(x,y)\le d_{G1}(x,y).}
\]

这个差不是数值舍入误差。它测量的是：当前被表示的 state set 是否包含足够多中间状态，使“直接整数 relation distance”能够真的由 unit stages 实现。

## 4. B08 — 全局 split-completeness 与测地性的精确等价

以下两件事等价。

### (A) 所有整数预算拆分都 A4 split-complete

对所有 `r,s>=0`，

\[
\boxed{R_r;R_s=R_{r+s}.}
\]

### (B) Unit-geodesic realization

对所有 `x,y in X0`，

\[
\boxed{d_{G1}(x,y)=\rho(x,y).}
\]

等价地，每一对整数 relation distance 为 `n` 的状态，都存在链

\[
x=x_0,x_1,\ldots,x_n=y
\]

并且每一步满足

\[
\rho(x_{t-1},x_t)=1.
\]

### 证明：由 (A) 推 (B)

取 `rho(x,y)=n`。

- `n=0` 平凡；
- `n=1` 本身就是 unit edge；
- `n>=2` 时，对预算 `1` 与 `n-1` 使用 split-completeness，得到 `z`，满足
  \[
  \rho(x,z)\le1,
  \qquad
  \rho(z,y)\le n-1.
  \]
  `z` 不可能等于 `x`，否则第二个不等式与 `rho(x,y)=n` 矛盾，因此 `rho(x,z)=1`。再由三角不等式可知 `rho(z,y)` 必须恰为 `n-1`，否则 `rho(x,y)<n`。递归即可。

因此构造出长度恰为 `n` 的 unit path，故 `d_G1<=n=rho`；反向不等式前面已证。

### 证明：由 (B) 推 (A)

取 `(x,y) in R_(r+s)`，令 `n=rho(x,y)<=r+s`。选取长度 `n` 的 unit geodesic。因为 `n<=r+s`，存在整数

\[
k\in[\max(0,n-s),\min(r,n)].
\]

取 geodesic 上第 `k` 个顶点 `z`，则

\[
\rho(x,z)\le k\le r,
\qquad
\rho(z,y)\le n-k\le s.
\]

故 `(x,y) in R_r;R_s`。Stage 01 已证明反向包含。

因此，在 A3-generated subclass 中，A4 的全局 split-completeness **精确等价于**：整数 relation metric 就是其 radius-one support graph 的本征 shortest-path metric。

## 5. B09 — geodesic defect

定义 pairwise geodesic defect

\[
\Gamma(x,y)=
\begin{cases}
 d_{G1}(x,y)-\rho(x,y),&d_{G1}(x,y)<\infty,\\
 \infty,&\text{否则}.
\end{cases}
\]

则 `Gamma>=0`，并且

\[
\boxed{
\Gamma\equiv0
\iff
R_r;R_s=R_{r+s}
\text{ 对所有 }r,s\in\mathbb N.
}
\]

所以 `Gamma` 把无限多组 budget-split 等式压缩成了对有限 quotient state set 的一次 metric audit。

它比某一组 `(r,s)` 上的 `missing_interpolations` 更强：不仅告诉我们哪里缺 witness，还量化了缺失状态造成的额外 unit-path 长度；若完全断开则直接记录为 infinity。

## 6. 例子

### 连续 unit states

对 values `{0,1,2}`，`rho(0,2)=2`，同时存在 unit path `0-1-2`，长度也是 2。因此所有 pair 的 `Gamma=0`，重新得到 B05。

### 缺失 midpoint

对 values `{0,2}`，`rho(0,2)=2`，但 unit graph 没有边，也没有路径。因此

\[
\Gamma(0,2)=\infty,
\]

这重新得到 B06，并把 `1+1` 拆分失败解释为 graph-geodesic hole。

### Weighted / non-unit states

该定理不要求 unit capacities，也不要求 capacity-normalized state 本身是整数。capacities 只通过精确 cross-multiplied integer radius `rho` 进入定义；取完 zero quotient 后，测地检验完全是有限组合问题。

## 7. 跨路线后果

### 对 A4

以后无需逐个检查所有 `(r,s)` composition 才知道是否 split-complete。只要构造 `G1` 并比较其 shortest-path metric 与 `rho` 即可。

### 对 A5 / P012 / P022

桥梁现在直接落到 intrinsic discrete geometry。radius-one A4 support graph 可作为候选 primitive adjacency，而 B08 问的是其 intrinsic graph metric 是否精确恢复 A3 的 direct integer relation metric。具体 geometry 可以研究哪些 lattice/root-lattice states 满足 `Gamma=0`、`Gamma` 有界，或出现 disconnected interpolation sectors。

### 对 A2 / P023

若某 quotient 保留 endpoint `rho`，却改变了 `Gamma`，那么对包含 staged support composition 的 future operation language，它就不是 future-safe。以后必须明确：未来任务只需要 endpoint support，还是还需要 geodesic/intermediate-witness structure。

### 对 A3

`rho` 与 `Gamma` 把两个不同属性分开：

- 直接 coarse relational separation；
- 该 separation 是否能由实际表示的 intermediate states 实现。

这为 relation-state precision 与 support-composition precision 建立了一个有限整数接口。

## 8. Prior-art discipline

整数 metric、graph shortest-path metric、geodesic metric space 与 relation powers 都是已有数学。本项目不主张这些一般概念本身的新颖性。

当前项目特有的研究贡献候选，是从 A3 weighted relation field 精确导出这一 metric/geodesic 接口，并用它连接 A4 split-completeness、A5 intrinsic geometry 与 A2 future-compatible precision。

## 9. Executable reference

`src/enterprise_math/relation_support_bridge.py` 新增：

- 用 ceiling division 得到 integer relation-distance matrix；
- radius-one graph shortest paths；
- geodesic-defect audit；
- 通过 metric equality 检验全局 split-completeness。

测试覆盖 unit、weighted 例子以及 `{0,2}` disconnected defect。
