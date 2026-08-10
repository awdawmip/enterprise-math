# P023 —— 条件 repair task 调度，补充 14

状态：`PROVED RESEARCH NOTE`  
归属：A2 / P023，并连接 P018 adaptive precision 算法层  
依赖：P023-S13 conditional repair、S12 integer symbol depth、P018 有限 dynamic-program selection  
纪律：有限 task ordering 与 dynamic programming 都属于成熟算法思想。本补充的关键是：每一步 cost 由精确 precision incidence 内生导出，而不是预先外部赋价。

## 1. 同一个最终 precision，可以有不同 acquisition cost

令有限 task partitions 为

\[
E_1,\ldots,E_m.
\]

最终 joint precision

\[
E_*=\bigcap_iE_i
\]

与 task 顺序无关。

但是加入一个 task 所需的 repair alphabet 取决于之前已经保留了哪些 tasks。因此，**顺序获取**同一个最终 precision 的成本可以依赖顺序。

这是 higher-order incidence effect，而不是 final quotient 本身发生变化。

## 2. 一个顺序的 conditional repair profile

固定顺序

\[
\sigma=(\sigma(1),\ldots,\sigma(m)).
\]

令

\[
C_0=\top_X
\]

为 universal one-block partition，并递归定义

\[
C_j=C_{j-1}\cap E_{\sigma(j)}.
\]

定义精确 conditional repair factor

\[
\boxed{
\rho_j
=
\rho(E_{\sigma(j)}\mid C_{j-1}).
}
\]

对整数 base `B>=2`，定义阶段 symbol depth

\[
\boxed{
c_j=L_B(\rho_j).}
\]

该顺序的总 sequential depth 为

\[
\boxed{
C_B(\sigma)=\sum_{j=1}^m c_j.
}
\]

这里不需要概率、expected value、对数，也不需要外部指定 observation cost。

## 3. P023-S14-T01 —— Product-capacity bound

状态：`PROVED`。

在第 `j` 步，每个当前 context block 最多分裂成 `rho_j` 个 child blocks，因此

\[
|X/C_j|
\le
|X/C_{j-1}|\rho_j.
\]

从 one-block context 迭代得到

\[
\boxed{
|X/E_*|
\le
\prod_{j=1}^m\rho_j.
}
\]

右侧就是该顺序的 stagewise worst-case sequential repair capacity。

定义 product slack

\[
\boxed{
S_\times(\sigma)
=
\prod_j\rho_j-|X/E_*|.
}
\]

它表示逐阶段最坏情况预留、但最终 joint task 从未同时实现的 capacity。

## 4. P023-S14-T02 —— Integer depth lower bound

状态：`PROVED`。

令

\[
D_*=L_B(|X/E_*|)
\]

为仅仅给所有 final joint classes 编号就至少需要的 base-`B` symbol depth。

因为

\[
|X/E_*|\le\prod_j\rho_j
\]

且

\[
L_B\!\left(\prod_j\rho_j\right)
\le
\sum_jL_B(\rho_j),
\]

得到

\[
\boxed{
D_*\le C_B(\sigma).
}
\]

定义 scheduling slack

\[
\boxed{
S_B(\sigma)=C_B(\sigma)-D_*\ge0.
}
\]

它是纯整数度量：当前 task order 相对于 final joint-state cardinality lower bound 多支付了多少 worst-case sequential coding capacity。

## 5. P023-S14-T03 —— 精确等号判据：每一步都必须 uniform branching

状态：`PROVED`。

单步等号

\[
|X/C_j|
=|X/C_{j-1}|\rho_j
\]

成立，当且仅当**每个**当前 context block 都恰好分裂成 `rho_j` 个 realized child blocks。

因此

\[
\boxed{
|X/E_*|=\prod_j\rho_j
}
\]

当且仅当整个 schedule 的每一步都在所有当前 realized context blocks 上 uniform branching。

### 证明

新 class count 等于所有旧 context blocks 的 local split degrees 之和。每个 degree 都不超过 `rho_j`，因此总和达到 `number_of_old_blocks * rho_j` 当且仅当每个 local degree 都达到最大值。

一旦某一步严格小于该上界，后续只会再乘正整数，所以最终 product equality 不可能恢复。∎

因此 branch-dependent local repair 正是 product slack 的精确来源。

## 6. 一个四状态的 order-dependence witness

取四个 states 与三个 binary tasks：

\[
A=(0,0,0,1),
\qquad
B=(0,0,1,1),
\qquad
C=(0,1,0,1).
\]

三个 tasks 联合后分开全部四个 states。

对顺序

\[
B\to C\to A,
\]

repair factors 为

\[
\boxed{(2,2,1)}
\]

binary depth 为

\[
1+1+0=2.
\]

它恰好达到 final lower bound `L_2(4)=2`。

而顺序

\[
C\to A\to B
\]

的 factors 为

\[
\boxed{(2,2,2)}
\]

binary depth 为

\[
1+1+1=3.
\]

最终 precision 完全相同，但第二种顺序凭空多支付一个 binary symbol。

所以 task order 是真实的有限 precision optimization variable。

## 7. P023-S14-T04 —— 精确 subset dynamic program

状态：`PROVED / EXECUTABLE`。

对已保留 task set `S`，令

\[
C_S=\bigcap_{i\in S}E_i.
\]

定义

\[
\operatorname{OPT}(S)
=
\min_{j\notin S}
\left(
L_B(\rho(E_j\mid C_S))
+
\operatorname{OPT}(S\cup\{j\})
\right),
\]

终端条件为

\[
\operatorname{OPT}(\{1,\ldots,m\})=0.
\]

因为 `C_S` 只依赖已知 task 的集合，不依赖它们之前的顺序，所以这是精确 subset DP，context states 最多为 `2^m` 个。

把加法目标换成乘法，就得到最小 product capacity 的同类 recurrence。

在没有更强结构定理消除 order dependence 时，这就是正确的有限 exact optimizer。

## 8. P023-S14-T05 —— Cheapest-next greedy 一般不最优

状态：`PROVED BY EXPLICIT COUNTEREXAMPLE`。

取五个 states 和 tasks

\[
A=(0,0,0,0,1),
\]

\[
B=(0,0,0,1,0),
\]

\[
C=(0,0,1,2,3).
\]

从 universal context 出发：

- `A` 只需 1 个 binary symbol；
- `B` 只需 1 个 binary symbol；
- `C` 需要 2 个 binary symbols。

因此任何“当前选最便宜 task”的 heuristic 都必然先选 `A` 或 `B`。

若从 `A -> B` 开始，则 depth profile 为

\[
\boxed{(1,1,1)}
\]

总成本为 `3`；对称的 `B -> A` 同样如此。

但若先选 `C`，其 four-way observation 已经同时决定 `A` 与 `B`，于是

\[
\boxed{C\to A\to B:\quad(2,0,0)}
\]

总成本只有 `2`。

因此

\[
\boxed{
\text{局部最便宜 next task}
\not\Rightarrow
\text{全局最便宜 precision schedule}.
}
\]

所以一般有限情形确实需要 exact DP，而不是贪心规则。

## 9. P023-S14-T06 —— 更多 context 可以让昂贵 task 变便宜甚至冗余

这是 S13 context monotonicity 的 scheduling 版本。

对任意 task `F` 与 contexts `C' subseteq C`，

\[
\rho(F\mid C')\le\rho(F\mid C).
\]

因此一个 task 的成本是**由当前 precision state 内生决定的**。

它不是 task 自身固定不变的属性。

这同时解释了 order dependence 与 greedy failure：提前支付一个 richer task，可能把多个原本便宜 task 的后续成本直接降为 0。

## 10. 与 P018 adaptive precision 的关系

P018 已经拥有用于 adaptive observation selection 的有限 dynamic programming，但它的 cost model 是外部给定，目标是 predicate decision。

S14 解决的是另一问题：

- 每一步 cost 由 exact repair geometry 内生导出，
  \[
  c(E_j\mid C)=L_B(\rho(E_j\mid C));
  \]
- 目标是精确获取一个声明好的完整 joint precision。

未来可以把两者组合：外部昂贵 measurement 与内部昂贵 precision repair 可以共同进入一个整数 Bellman recurrence。

但这两个问题不能混为同一个。

## 11. 研究工具规则

若多个 task coordinates 最终都必须保留：

1. 在 context 未知时，不要给每个 task 预先指定固定 precision cost；
2. 从 realized incidence 计算当前 conditional repair factor；
3. 检查 richer context 后哪些 tasks 变成冗余；
4. task 数量适中时使用 exact subset DP；
5. 先用 exact DP 作为 falsification oracle，再寻找结构化 fast path；
6. scheduling slack 与 final joint class count 分开报告。

这样 task order 就成为受控 theorem/proof-compression 问题，而不是 heuristic workflow 选择。

## 12. 可执行规范

- `src/enterprise_math/precision_task_scheduling.py`
- `src/enterprise_math/precision_task_greedy.py`
- `tests/test_precision_task_scheduling.py`
- `tests/test_precision_task_greedy.py`

回归固定四状态 order-dependence witness，验证 uniform-branching equality criterion，用 exhaustive permutations 对照 exact subset DP，并固定五状态 cheapest-next greedy failure。

## 13. 基础后果

Required precision 不仅 task-relative；**即使最终 quotient 固定，获取 multi-task precision 的成本仍然是 context-relative 与 order-relative 的。**

因此更准确的基础图景为

\[
\boxed{
\text{precision state}
+
\text{next requested task}
\longrightarrow
\text{conditional repair cost}.
}
\]

一个独立于当前 context 的 scalar task price 在一般有限理论里并不足够基础。

## 14. 前人工作与新颖性纪律

Dynamic programming、decision-tree ordering 与 conditional coding 都属于成熟思想，Enterprise Math 不主张发明这些工具。

本项目新增的综合接口是从 precision incidence 精确导出的整数 cost law

\[
\boxed{
c(F\mid C)=L_B(\rho(F\mid C)),}
\]

以及 uniform-branching slack theorem，并把它接入现有 future-safe quotient / repair 框架。
