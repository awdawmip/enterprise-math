# P025 补充 18 —— Exact Preperiod 的有限 Apéry Capacity Frontier

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-access-tail-stage18`  
Base checkpoint：P025 Stage 17 `6220a5a`  
依赖：P025 补充 16–17；A3/A4 antichain language；P023 task-relative precision  
Hard block：`NONE`

## 1. Stage 17 还留下什么

补充 17 对每个 defect residue `j mod P` 保存 Apéry value `a_j` 与

\[
q_j(0)=\left\lceil\frac{L_j(0)}2\right\rceil,
\]

其中 `L_j(0)` 是实现 `a_j` 的最小非负 `L_infinity` factorization radius。

这恰好足以判断 **Apéry element 本身**何时已经能够装进 signed-access cube，但还不能直接描述进入 tail 之前的 access：因为后面的 defect

\[
a_j+kP
\]

可能获得比“给 Apéry factorization 的所有坐标统一加 `k`”更好的 bounded factorization。

例如 row `(1,6)` 的 residue `j=5` 有 `a_j=5`、`L_j(0)=5`、`q_j(0)=3`。target `N=2` 的 base radius 只有 `r_0=1`，Apéry element 本身装不进去；但一个 period 以后 defect 变成 `12=6+6`，其 minimum factorization radius 只有 `2`，所以 exact signed access radius 已经是 `2`。

因此 preperiod 需要一个比单一 tail threshold 更有结构、但仍然有限的 refinement。

## 2. P025-D10 —— shifted Apéry factorization radius

对每个 `k>=0` 定义

\[
\boxed{
L_j(k)
=
\min\left\{
\|y\|_\infty:
 y\in\mathbb N^d,
\ b\cdot y=a_j+kP
\right\}.
}
\]

对满足

\[
j\equiv-N\pmod P,
\qquad
r_0=\frac{N+a_j}{P}
\]

的 target `N`，若尝试 access radius `r_0+k`，则 defect 为 `a_j+kP`，坐标容量为 `2(r_0+k)`。

所以该半径可行当且仅当

\[
L_j(k)\le2(r_0+k).
\]

等价地定义 **capacity threshold**

\[
\boxed{
q_j(k)
=
\max\left(
0,
\left\lceil
\frac{L_j(k)-2k}{2}
\right\rceil
\right).
}
\]

则

\[
\boxed{r_0+k\text{ 可行}\iff q_j(k)\le r_0.}
\]

## 3. P025-T53 —— capacity sequence 给出 exact access

对 residue `-j` 中任意 nonnegative target `N`，

\[
\boxed{
\kappa_b(N)
=
r_0+\min\{k\ge0:q_j(k)\le r_0\}.
}
\]

### 证明

在候选半径 `r_0+k`，补充 16 的 signed/nonnegative transform 给出 defect `a_j+kP` 与 cap `2(r_0+k)`。按 `L_j(k)` 定义，可行性恰好等价于 `L_j(k)<=2(r_0+k)`，也就是 `q_j(k)<=r_0`。取第一个可行 `k` 即得到最小半径。∎

所以完整 preperiod 与 tail 被统一为一个有限 threshold-crossing 问题。

## 4. P025-T54 —— capacity sequence 单调且有限到零

取一个达到 `L_j(k)` 的 factorization，并给每个坐标都加 `1`。因为 `P=sum b_i`，得到 `a_j+(k+1)P` 的 factorization，且 `L_infinity` radius 至多增加 `1`。因此

\[
\boxed{L_j(k+1)\le L_j(k)+1.}
\]

于是

\[
L_j(k+1)-2(k+1)
\le
L_j(k)-2k-1,
\]

从而

\[
\boxed{q_j(k+1)\le q_j(k).}
\]

同时归纳有

\[
L_j(k)\le L_j(0)+k,
\]

故

\[
L_j(k)-2k\le L_j(0)-k.
\]

所以最迟在 `k=L_j(0)` 时，`q_j(k)=0`。

每个 residue 的 exact capacity sequence 因而总是有限。

## 5. P025-D11 —— capacity Pareto frontier

如果相邻两个 shift 的 threshold 相同，后一个点没有任何价值：它付出更大的 `k`，却没有降低所需 base radius。

因此删除所有重复 threshold，只保留每次严格下降的第一次：

\[
\boxed{
\mathcal C_j
=
\{(k,q_j(k)):
 k=0\text{ 或 }q_j(k)<q_j(k-1)\}.
}
\]

随着 `k` 增加，保留的 `q` 严格下降，所以这些点在 componentwise order 中两两不可比较，构成有限 Pareto antichain。

给定任意 base radius `r_0`，exact extra shift 就是 frontier 中第一个满足

\[
q\le r_0
\]

的 `k`。

因此 `C_j` 是该 residue exact access 的完整有限语义摘要。

又因为 `q_j(0)=ceil(L_j(0)/2)`，而保留 threshold 是互异非负整数，

\[
\boxed{
|\mathcal C_j|
\le
\left\lceil\frac{L_j(0)}2\right\rceil+1.
}
\]

## 6. 示例

### 6.1 `(1,6)`，target residue `2`

这里 `P=7`，defect residue `j=5`，且

\[
a_5=5.
\]

sequence 开头为

\[
(L_5(0),q_5(0))=(5,3),
\]

而

\[
(L_5(1),q_5(1))=(2,0)
\]

因为 `12=6+6`。

于是

\[
\boxed{\mathcal C_5=\{(0,3),(1,0)\}.}
\]

对 `N=2`，`r_0=1`；第一个 `q<=1` 的点是 `(1,0)`，因此

\[
\kappa(2)=1+1=2.
\]

对 `N=16`，`r_0=3`；`(0,3)` 已经成立，所以 `kappa(16)=3`。

### 6.2 `(5,2)` 的 Stage-16 唯一异常 residue

对 defect residue `6`，

\[
\boxed{
\mathcal C_6
=\{(0,2),(1,1),(2,0)\}.
}
\]

所以 preperiod 不是任意 lookup table，而是一条三层 monotone capacity frontier。

### 6.3 `(2,5,7,8)`

对 defect residue `6`，

\[
\boxed{\mathcal C_6=\{(0,2),(1,0)\}.}
\]

Target `16` 的 base radius 为 `1`，所以需要 extra shift `1`，得到 `kappa(16)=2`；target `38` 的 base radius 为 `2`，shift `0` 已经可行，因此 `kappa(38)=2`。

## 7. P025-T55 —— 不再需要 target-indexed exception table 的 finite exact response

收集所有 residue frontier：

\[
\boxed{
\Sigma_{\rm cap}(b)
=
\left(
P,
(a_j,\mathcal C_j)_{j\bmod P}
\right).
}
\]

给定任意 `N>=0`，恢复 `j=-N mod P`，计算 `r_0=(N+a_j)/P`，在 `C_j` 中找第一个 `q<=r_0` 的 `(k,q)`，返回

\[
\boxed{\kappa_b(N)=r_0+k.}
\]

因此 `Sigma_cap` 是一个有限 exact state，可以重建整个无限 nonnegative access response。

这并不否定补充 17 的 `tail + exception table` 表示；这里只是把同一个 full exact language 改写为更结构化的 residue-space representation。

目前**不主张** `Sigma_cap` 已经是 P023 意义下的 coarsest possible encoding。

## 8. 与 A3/A4 antichain 和 P023 的关系

Frontier `C_j` 再次是项目已有 antichain pattern 的一个工作实例：

- 一个坐标是额外 access shift `k`；
- 一个坐标是要求的 current/base precision `q`；
- 对当前 threshold language，被支配的点可以永久删除。

P025 不创建新的 generic Pareto theory，而是消费 A3/A4 已有 antichain 语言和 P023 拥有的 task-relative sufficiency 原则。

新增的是 signed-access 特化及其有限 defect-capacity reduction。

## 9. Prior-art 边界

Numerical-semigroup Apéry sets、specified-generator factorization statistics、`L_infinity` factorization lengths 及其 eventual behavior 都属于前人工作，补充 16–17 已登记对应文献。

不等式 `L_j(k+1)<=L_j(k)+1` 只是给 factorization 加 all-ones vector 的直接结果，也不作历史优先性主张。

P025 当前继续检验的架构接口是

\[
\boxed{
\text{signed certificate access}
\to
\text{shifted Apéry factorization capacities}
\to
\text{finite Pareto threshold frontier}.
}
\]

历史创新状态仍为 `NOVELTY_UNVERIFIED`。

## 10. 可执行资产

Stage-18 owner generation 新增：

- `src/enterprise_math/abc_apery_capacity_frontier.py`
  - exact shifted `L_j(k)` capacity sequence；
  - monotone finite threshold sequence；
  - nondominated capacity frontier；
  - exact full access reconstruction；
  - frontier cardinality bound。
- `tests/test_abc_apery_capacity_frontier.py`
  - `(1,6)` preperiod collapse；
  - `(5,2)` 三层 frontier；
  - Stage-17 `(2,5,7,8)` exception 重建；
  - 与 independent exact access oracle 的 full-response 对照；
  - small two-variable exhaustive checks。

## 11. 下一前沿

没有 hard block。继续：

1. 判断 `Sigma_cap` 对 full scalar-access language 是否存在更粗的 P023-minimal quotient；
2. 分类哪些 capacity-frontier shapes 真正来自 arithmetic-derivative block rows，而不是任意 positive rows；
3. 研究多个独立 block targets 的 composition/product law；
4. 与 P024 action-boundary frontiers 对照，但不合并两者不同语义；
5. 在非 ABC certificate system 中寻找同样的 shifted-capacity antichain。
