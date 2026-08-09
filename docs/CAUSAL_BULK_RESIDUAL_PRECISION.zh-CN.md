# Causal Bulk Residual Precision —— 从实际 Composition Fiber 生成可消去性与精度

状态：`ACTIVE CROSS-ROUTE RESEARCH WIP / EXACT FINITE THEOREMS + EXECUTABLE REFERENCE`

归属：A3 causal-composition specialization。P018 仍拥有显式 divisibility precision calculus；本文件提供另一条由 causal operation 自身生成的 **derived precision**，两者不得未经 bridge theorem 直接等同。

## 1. 纠偏：normalized residual 不应以减法为本体

此前整数 observation 使用：

\[
\widehat\Sigma_p(s)=O(ps)-O(p).
\]

这对 additive integer bulk 很自然，但仍把“减法能消去当前 bulk”当成特殊结构。

更一般地，给一个实际 causal bulk composition：

\[
\boxed{
b\odot r=t.}
\]

`b` 是已经 settled 的 current bulk，`r` 是未来增量/响应，`t` 是组合后的 observation。

真正 primitive 的问题不是“有没有逆元”，而是固定 `b,t` 时有哪些 reachable `r` 会产生同一 `t`。

## 2. BR-01 —— residual fiber

定义：

\[
\boxed{
\mathcal R_b(t)
=
\{r:b\odot r=t\}.
}
\]

这是 left translation：

\[
L_b:r\mapsto b\odot r
\]

的 fiber。

### singleton 特例

若所有 reachable fibers 都是 singleton，则 future residual 可以唯一恢复。

传统 left-cancellation / exact division 只是在这个 regime 下成立的 shadow。

### non-singleton 不自动是缺陷

若：

\[
b\odot r=b\odot r',
\]

而未来继续只通过同一个 associative law 在右侧追加 `u`，则：

\[
(b\odot r)\odot u
=
(b\odot r')\odot u.
\]

所以 `r,r'` 一旦已被当前 bulk 合并，在该 future language 中永远不会重新分裂。

因此：

\[
\boxed{
\text{non-cancellativity can be a legitimate causal collapse, not an algebraic defect.}
}
\]

## 3. BR-02 —— bulk-relative residual precision

在有限 reachable increment set `R` 上，定义：

\[
\boxed{
r\sim_b r'
\iff
b\odot r=b\odot r'.}
\]

得到 residual partition：

\[
P_b=R/{\sim_b}.
\]

解释：

> `P_b` 正是 current bulk `b` 以后，未来增量仍能被当前 state 区分到什么程度。

所以这里的 precision 不是外加数值标签，而是一个实际 causal operation fiber structure。

## 4. BR-03 —— P011 collision spectrum 直接测 residual distinction loss

对：

\[
L_b:R\to b\odot R,
\]

定义：

\[
\boxed{
J_k(L_b)
=
\sum_t\binom{|\mathcal R_b(t)|}{k}.
}
\]

它精确统计有多少 `k` 元不同 reachable future increments 已经被 current bulk 合成同一个 observation。

因此 P011 `J_k` 再获得一个角色：

\[
\boxed{
\text{bulk-induced residual precision-loss spectrum}.
}
\]

## 5. BR-04 —— commutative accumulation 导出 precision 单调粗化

假设 `odot` associative + commutative，并且新 bulk 是旧 bulk 继续吸收某个 state：

\[
\boxed{
b'=b\odot u.}
\]

若：

\[
b\odot r=b\odot r',
\]

则：

\[
(b\odot u)\odot r
=u\odot(b\odot r)
=u\odot(b\odot r')
=(b\odot u)\odot r'.
\]

故：

\[
\boxed{P_b\preceq P_{b'}.}
\]

也就是 current bulk 增长时，residual distinctions 只能保持或继续合并，不能凭空重新出现。

于是对所有 `k`：

\[
\boxed{J_k(L_{b'})\ge J_k(L_b).}
\]

这给出一个 derived precision law：

> 不是先宣布“bulk 越大精度越低”，而是 accumulation operation 实际让更多 future residuals 落到同一个 fiber，所以 precision 作为结果变粗。

## 6. bulk absorption preorder

若 operation 有 identity，定义：

\[
\boxed{
b\preceq_\odot b'
\iff
\exists u:\ b'=b\odot u.}
\]

associativity 给 transitivity，identity 给 reflexivity。

在 commutative regime 下：

\[
b\preceq_\odot b'
\Longrightarrow
P_b\preceq P_{b'}.
\]

若 `odot` 进一步 idempotent，则：

\[
b\preceq_\odot b'
\iff
b\odot b'=b'.
\]

因此传统 join-semilattice order 在此只是“能否通过继续 causal absorption 到达”的 shadow；不需要提前作为 ontology 放进系统。

## 7. 三个最小例子

### 7.1 Integer addition

\[
b\odot r=b+r.
\]

所有 reachable residual fibers singleton：

\[
J_{k\ge2}=0.
\]

accumulating bulk 不降低 residual distinction。

### 7.2 max

\[
b\odot r=\max(b,r).
\]

bulk=5 时，所有 `r<=5` 都落到同一个 current total 5。

current state 已经合法忘掉它们之间的差异；未来继续做 max 也无法恢复。

随着 bulk 从 2 增到 5，residual partition strictly coarsens，`J_2` 等 collision coordinates 增长。

### 7.3 Boolean OR

一旦 bulk=True：

\[
\text{True OR False}
=
\text{True OR True}
=
\text{True}.
\]

两个 future increments 立即成为同一 residual fiber。若 future 仍只做 OR，它们不需要再保存。

## 8. P018 的位置

P018 当前使用显式 precision scale：

\[
d\preceq e\iff d\mid e,
\]

并研究：

\[
x=r\pi(x)+\delta(x).
\]

这仍是严格而有价值的 **declared resolution calculus**。

本文件补充的 causal residual precision 则是：

\[
\boxed{
\text{actual operation fibers}
\to
\text{future indistinguishability}
\to
\text{derived precision order}.
}
\]

后续研究应分别标记：

- `DECLARED_RESOLUTION`：为了证明/工程/表示主动选择的 scale；
- `CAUSAL_DERIVED_PRECISION`：实际 operation/future language 自动产生的 distinguishability partition。

只有证明两者通过某个 quotient/scale bridge 对应时，才允许把 P018 scale 当作该系统自然产生的 precision。

## 9. normalized residual 的一般版本

若 observation 满足 concatenation law：

\[
O(ps)=O(p)\odot O(s),
\]

则：

- 若 left translation singleton：structural residual 可直接取 `O(s)`；
- 若不是 singleton：structural residual 应取 `O(s)` 在 `P_(O(p))` 中的 causal fiber class；
- 绝不能因为传统上习惯“消去 prefix”就额外发明一个 inverse。

这把 bulk/structure separation 从 integer subtraction 推广到一般 finite/discrete causal composition law。

## 10. 可执行资产

- `src/enterprise_math/causal_bulk_residual.py`
- `tests/test_causal_bulk_residual.py`

回归覆盖 additive singleton fibers、`max`/OR non-cancellative causal collapse、P011 collision spectrum、以及 commutative bulk accumulation 下 residual precision coarsening。

## 11. 边界

尚未研究：

- noncommutative bulk evolution 下 residual precision 的方向性；
- infinite reachable increment sets；
- stochastic/quantum output composition；
- causal residual partition 与具体物理 measurement saturation 的实验 bridge。
