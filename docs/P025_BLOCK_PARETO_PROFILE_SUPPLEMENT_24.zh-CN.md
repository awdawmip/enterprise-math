# P025 补充 24 —— 由 Radius-Level Absorption 严格下降得到 Arbitrary-Support Exact Pareto Profile

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-access-tail-stage18`  
依赖：P025 补充 20–23；Stage-04 two-cost witness language  
Hard block：`NONE`

## 1. 闭合 Stage 04 的循环

补充 04 定义 fine witness cost

\[
C(x)=(\|x\|_\infty,\eta(x))
\]

及其 Pareto frontier。补充 20–23 已经对当前语言需要的每个 additive state 给出 exact compressed access。

对每个半径 `r`，令 `R_r` 为补充 23 的 compressed additive reachable set，并在存在 nondegenerate state 时定义

\[
\boxed{
E(r)=
\min\left\{
\frac{|av-bu|}{M}:
(u,v,u+v)\in\mathcal R_r,\ av-bu\ne0
\right\},
}
\]

其中

\[
M=m(a)m(b)m(c).
\]

`E(r)` 就是在 geometric precision `r` 下能够获得的最佳 absorption redundancy。

## 2. P025-T70 —— 单调性与端点

由构造

\[
\mathcal R_r\subseteq\mathcal R_{r+1}.
\]

所以一旦 `E` 有定义，

\[
\boxed{E(r+1)\le E(r).}
\]

补充 23 给出第一个有定义的半径

\[
\boxed{r=\mu,}
\]

补充 22 给出第一次达到 arithmetic floor 的半径

\[
\boxed{E(\nu)=\eta_{\min}.}
\]

因为 `eta_min` 是全局正最小值，对所有 `r>=nu` 都有

\[
E(r)=\eta_{\min}.
\]

因此全部 Pareto-relevant 信息都落在有限整数区间

\[
\boxed{[\mu,\nu]}
\]

内。

## 3. P025-T71 —— 严格下降点恰好是完整 Pareto frontier

定义

\[
\boxed{
\mathcal P_{\rm drop}
=
\{(r,E(r)):
 r=\mu
\text{ 或 }
E(r)<E(r-1),
\ \mu\le r\le\nu\}.
}
\]

则

\[
\boxed{
\mathcal P_{\rm drop}
=
\operatorname{Min}_{\preceq}
\{(\|x\|_\infty,\eta(x)):
 x\text{ 为 nondegenerate additive witness}\}.
}
\]

### 证明

固定半径 `r`。任何 norm 不超过 `r` 的 witness 都有 absorption 至少 `E(r)`；按定义又存在 compressed state 达到 `E(r)`，补充 20 为其提供 exact minimum-block-cost fine representative。

若 `E(r)=E(r-1)`，则半径 `r` 第一次出现的任何 absorption 不低于此值的 cost pair，都被更早半径已经拥有的同样 absorption value 支配，因此 `r` 不产生新 Pareto point。

若 `E(r)<E(r-1)`，则半径 `r-1` 以内不可能存在 absorption `E(r)` 的 witness。因此任何达到 `E(r)` 的 representative 的 exact global norm 必须为 `r`，故 `(r,E(r))` 不受支配。

`mu` 之前没有 nondegenerate witness；`nu` 以后 `eta_min` 已经首次取得，后续点都被第一次 floor point 支配。因此 strict-drop graph 就是完整 Pareto frontier。∎

## 4. P025-T72 —— finite frontier cardinality bounds

令

\[
E_0=E(\mu).
\]

每个 frontier point 使用 `[mu,nu]` 中不同 radius，所以

\[
|\mathcal P|
\le
\nu-\mu+1.
\]

它的 absorption coordinates 又是从 `E_0` 严格下降到 `eta_min` 的正整数，因此

\[
|\mathcal P|
\le
E_0-\eta_{\min}+1.
\]

所以

\[
\boxed{
|\mathcal P|
\le
\min\left(
\nu-\mu+1,
E(\mu)-\eta_{\min}+1
\right).
}
\]

这个有限界来自 task coordinates 自身，不依赖 fine witness lattice 的大小。

## 5. 示例

### `2+3=5`

\[
E(1)=2,
\qquad E(2)=1,
\]

故

\[
\boxed{\mathcal P=\{(1,2),(2,1)\}.}
\]

### `2+7=9`

精确 profile 为

\[
\boxed{E(1),\ldots,E(5)=(3,3,3,2,1).}
\]

严格下降出现在 radius `1,4,5`，恢复

\[
\boxed{\mathcal P=\{(1,3),(4,2),(5,1)\}.}
\]

### `1+22=23`

\[
\boxed{E(2),E(3),E(4),E(5)=(2,2,2,1).}
\]

所以

\[
\boxed{\mathcal P=\{(2,2),(5,1)\}.}
\]

这正是 Stage 14 squarefree access-delay tradeoff 的 compressed 形式。

### `25+704=729`

这里

\[
\mu=\nu=6,
\qquad\eta_{\min}=6,
\]

故

\[
\boxed{\mathcal P=\{(6,6)\}.}
\]

### `1+512=513`

同样

\[
\mu=\nu=13,
\qquad\eta_{\min}=3,
\]

所以

\[
\boxed{\mathcal P=\{(13,3)\}.}
\]

## 6. 架构后果

最初的 infinite fine-lattice two-cost problem 现在压成一条有限 monotone integer response：

\[
\boxed{
\text{fine witness lattice}
\to
\mathcal R_r
\to
E(r)\text{ on }[\mu,\nu]
\to
\text{strict-drop frontier}.
}
\]

对全部 rectangle queries

\[
\exists x:
\|x\|_\infty\le K,
\ \eta(x)\le H,
\]

一旦保留这条有限 frontier，就不再需要 fine witness identity。

这只是 P023 task-relative exact compression 与 A3/A4 antichain semantics 的具体实例；P025 不主张新的 generic Pareto theorem。

## 7. 可执行资产

新增：

- `src/enterprise_math/abc_block_pareto_profile.py`
  - 由 compressed reachable states 精确计算 `E(r)`；
  - arbitrary-support `[mu,nu]` radius profile；
  - strict-drop exact Pareto frontier；
  - finite cardinality bound；
  - 与早期 fine exact oracle 交叉验证。
- `tests/test_abc_block_pareto_profile.py`
  - Stage-04 exact frontiers；
  - squarefree access-delay profile；
  - singleton arbitrary-support examples；
  - fine/compressed agreement 与 cardinality bounds。

## 8. 下一前沿

没有 hard block。继续：

1. 为 structured relation classes 寻找 low-radius / `mu=1` criteria；
2. 在可能时把 full reachable sets `V_n(r)` 压成 task-minimal summaries；
3. 从一个 absorption scalar 推广到多个 simultaneous certificate costs；
4. 比较 compressed exact frontier bounds 与 Pasten Geometry-of-Numbers sufficient witness bounds；
5. 判定 Stage 18–24 哪些只是 P025 specialization，哪些值得形成 reusable P023 tooling。
