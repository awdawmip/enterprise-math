# 因果吞并 05 —— P011 Collision Spectrum 作为所有对称 Fiber-Local 整数响应的通用 Interaction Basis

状态：`CROSS-ROUTE RESEARCH WIP / EXACT BINOMIAL BASIS THEOREM + EXECUTABLE REFERENCE`

归属建议：一般母理论应归 A1/P011；本文件在 A3 branch 只作为 cross-route 推导来源。

## 1. 动机

上一条 LEGO interaction 使用 labeled unit subsets。

但项目更底层的 unit `1` 是同种单位，不应为了数学方便永久给每个 unit 贴身份标签。

在 collapse fiber 中真正可见的基本量是：

\[
n=m_F(y),
\]

即当前 coarse state 吞掉多少个 indistinguishable fine histories。

因此研究任意只依赖 `n` 的整数 response：

\[
\phi(n).
\]

## 2. CB-01 —— repeated-unit interaction coefficient

给：

\[
\phi(0),\phi(1),\ldots,\phi(N)\in\mathbb Z.
\]

定义：

\[
\boxed{
a_k
=
\sum_{j=0}^k
(-1)^{k-j}
\binom kj
\phi(j).
}
\]

解释：

> `a_k` 是一个不可约 `k`-unit group 的 interaction effect；它是在所有更低 unit-count response 被扣除后剩下的精确整数。

## 3. CB-02 —— exact repeated-unit reconstruction

有限二项反演给出：

\[
\boxed{
\phi(n)
=
\sum_{k=0}^n
 a_k\binom nk.
}
\]

这很符合 LEGO 解释：

- `a_k`：每一个 `k`-unit interaction group 的 effect；
- `C(n,k)`：`n` 个相同 unit 中恰有多少个 `k`-元组合。

无 unit label 持久化需求。

## 4. CB-03 —— 全局 fiber response 自动落到 P011 `J_k`

对有限 collapse：

\[
F:X\to Y,
\qquad |X|=N,
\]

定义任意 symmetric fiber-local response：

\[
R_\phi(F)
=
\sum_{y\in\operatorname{im}(F)}
\phi(m_F(y)).
\]

要求空 fiber 中性：

\[
\phi(0)=0.
\]

代入 CB-02：

\[
R_\phi(F)
=
\sum_y
\sum_k a_k\binom{m_F(y)}k.
\]

交换有限整数求和：

\[
\boxed{
R_\phi(F)
=
\sum_{k=1}^N a_kJ_k(F).
}
\]

其中：

\[
J_k(F)=\sum_y\binom{m_F(y)}k.
\]

所以：

\[
\boxed{
\text{P011 collision spectrum}
\text{ 是所有 bounded symmetric integer fiber-local response 的通用 basis。}
}
\]

这比“`J_k` 能恢复 fiber-size multiset”更直接：给任意整数 response table，都能显式算出读取 `J_k` 的 interaction coefficients。

## 5. CB-04 —— power moments 被吞并

取：

\[
\phi(n)=n^2.
\]

得到：

\[
a_1=1,
\qquad a_2=2,
\qquad a_{k\ge3}=0.
\]

所以：

\[
\boxed{
\sum_y m_y^2
=J_1+2J_2
=N+2J_2.
}
\]

P011 已有该式。

取：

\[
\phi(n)=n^3,
\]

得到：

\[
\boxed{
n^3
=n+6\binom n2+6\binom n3.}
\]

因此：

\[
\boxed{
\sum_y m_y^3
=J_1+6J_2+6J_3.
}
\]

传统 power moments 不再需要作为独立统计 primitive；它们只是 collision-interaction basis 的特定坐标读取。

传统 Stirling-number identity 可以作为 coefficient tool 使用，但不必成为本体。

## 6. CB-05 —— collision probability 是 spectrum 的后渲染

若外部选择“所有 `k` 元 fine-history subsets 等权抽取”的 sampling semantics，传统 collision probability 为：

\[
\frac{J_k(F)}{\binom Nk}.
\]

core 先保留 exact pair：

\[
\boxed{
P_k^\#
=
\left(J_k(F),\binom Nk\right).
}
\]

因此：

- collision count：primitive integer object；
- probability：额外 uniform sampling interpretation + ratio rendering。

## 7. CB-06 —— entropy 的理论地位下降

P011 已证明完整：

\[
(J_1,\ldots,J_N)
\]

唯一决定 fiber-size multiset。

因此任何只依赖 fiber sizes 的 symmetric scalar：

\[
S(m_1,\ldots,m_r)
\]

都不能包含超出完整 collision spectrum 的 fiber-size 信息。

特别地，若传统 entropy 只从 normalized fiber multiplicities：

\[
p_y=m_y/N
\]

计算，则它只是：

\[
\boxed{
\text{collision spectrum}
\to
\text{recover fiber sizes}
\to
\text{normalize/log}
\to
\text{one scalar rendering}.
}
\]

这**不等于**热力学 entropy 已被推导，也不意味着 log 无用。

它只说明：

> 在 finite deterministic collapse 的 fiber-size 信息层，完整整数 spectrum 比单个 entropy scalar 更底层、更完整。

## 8. CB-07 —— “非线性”与 collision 的统一方向

上一条 LEGO interaction 定义具体 unit-group 的 joint effect。

本条 repeated-unit basis 则说明：如果 operation response 只看一个 fiber 中有多少 unit histories，那么所有非线性 count response 都能写成：

\[
\boxed{
\text{k-body interaction coefficient }a_k
\times
\text{k-body collision count }J_k.
}
\]

这给 P011 一个新的解释候选：

> `J_k` 不只是不可逆性指标，也可能是 indistinguishable-unit system 中天然的 `k`-body interaction carrier。

当前仍标记 `NOVELTY_UNVERIFIED`，需要 prior-art 审计。

## 9. 边界

当前 theorem 要求 response 是：

- finite；
- bounded count range `0..N`；
- integer-valued；
- fiber-local；
- symmetric，只依赖 fiber size `n`；
- 空 fiber 中性 `phi(0)=0`。

以下不自动覆盖：

- 依赖具体 history identity 的 response；
- relation/context-sensitive response；
- real/log response 的 integer exact coefficients；
- infinite fibers；
- stochastic weights。

## 10. 可执行参考

新增：

- `src/enterprise_math/collision_interaction_basis.py`；
- `tests/test_collision_interaction_basis.py`。

回归验证：

- 任意有限 integer response table exact reconstruction；
- square/cube power identities；
- 任意 tested fiber partitions 上 direct response 与 `J_k` basis response 完全一致。

## 11. 吞并结果

当前可以把以下传统对象降级：

- power moments → `J_k` interaction coordinates 的 shadow；
- uniform collision probabilities → exact `(J_k,C(N,k))` pair 的 ratio rendering；
- fiber-size entropy scalar → 完整 collision spectrum 的 lossy/postprocessed rendering。

真正 primitive candidate 变成：

\[
\boxed{
\text{unit histories}
\to
\text{collapse fibers}
\to
\text{collision spectrum }J_k.
}
\]

## 12. 下一步

1. Relay 到 P011 owner，判断是否应把本 theorem 作为 P011 的 general corollary/interpretation；
2. 研究 superadditivity of `phi` 如何翻译成 interaction coefficients `a_k` 的符号条件；
3. 判断哪些 monotone irreversibility functionals 在 `J_k` basis 中具有非负 coefficients；
4. 将 P011 与 LEGO nonlinear interaction spectrum 对接；
5. 寻找传统 cumulant/moment theory 是否可以被更底层的 collision-interaction algebra 吞并，避免直接照搬 probability language。
