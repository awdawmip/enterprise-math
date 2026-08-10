# P023 / A2 —— 条件 Repair 调度核心 v3

状态：`PROVED OWNER DISTILLATION / RESEARCH`  
归属：A2 future-compatible quotient  
依赖：A2 Precision Incidence Core v3  
冻结来源：`research/p023-precision-incidence-scheduling@646530c3acd69332efe0fb937258cec888713688`

本文把精确有限 repair geometry 中与任务顺序、依赖和编码有关的结果压成一个 owner-level 接口。动态规划、闭包系统、mixed-radix 编码和 greedy 反例都属于成熟数学/算法思想；这里不主张这些一般结构的历史原创性。

## 1. 条件任务成本

令 `X` 为有限状态集，有限任务族由 partitions `E_1,...,E_m` 表示。若任务集合 `S` 已经保留，记 `C_S=cap_{i in S} E_i`，空交集取 universal one-block relation。

对新增任务 `j`，定义

\[
\boxed{\rho(j\mid S)=\rho(C_S,E_j).}
\]

它就是在保留 `S` 全部任务的前提下再加入 `j` 所需的最小 alphabet。若 `S subseteq T`，则

\[
\boxed{\rho(j\mid T)\le \rho(j\mid S).}
\]

已知 context 越丰富，同一新增任务所需的额外 repair 不会增加。

## 2. 顺序相关的 acquisition

给定任务顺序 `sigma=(sigma_1,...,sigma_m)`，令

\[
\rho_r=\rho(\sigma_r\mid\{\sigma_1,\ldots,\sigma_{r-1}\}).
\]

最终 joint relation `E_*=cap_iE_i` 与顺序无关，但逐步 worst-case capacity

\[
\boxed{P_\sigma=\prod_r\rho_r}
\]

可以依赖顺序。精确计数给出

\[
\boxed{|X/E_*|\le P_\sigma.}
\]

对整数 alphabet base `B>=2`，定义 `L_B(n)=min{ell:n<=B^ell}`。顺序总 symbol cost 为

\[
\boxed{C_B(\sigma)=\sum_rL_B(\rho_r),}
\]

且任何顺序都满足

\[
\boxed{L_B(|X/E_*|)\le C_B(\sigma).}
\]

因此 final-state depth 与 acquisition depth 是不同对象。

## 3. 精确取等判据

第 `r` 步中，每个当前已实现 context block 会被新增任务切成至多 `rho_r` 个子块。

\[
|X/E_*|=P_\sigma
\]

当且仅当每一步都 **uniform branching**：所有当前已实现 context blocks 恰好都有 `rho_r` 个真实 extensions。branch-dependent split 会产生实际状态从未实现的 product capacity。

## 4. Scheduling slack 精确分成两个 defect

令 `D_*=L_B(|X/E_*|)`。则

\[
\boxed{C_B(\sigma)-D_*=S_{\rm radix}(\sigma)+S_{\rm inc}(\sigma)}
\]

其中

\[
S_{\rm radix}=\sum_rL_B(\rho_r)-L_B(P_\sigma)
\]

以及

\[
S_{\rm inc}=L_B(P_\sigma)-L_B(|X/E_*|).
\]

两者都是非负整数。`S_radix` 是逐步独立 radix digit 的 packing overhead；`S_inc` 是真实 joint states 没填满最坏 product capacity 的 incidence overhead。

## 5. 两个精确正规化

一个调度顺序在每一步产生一个 local repair digit；给当前 context block 的真实 children 编号 `0,...,rho_r-1`。

### Mixed-radix 正规化

把 digit tuple 双射打包进 `[0,P_sigma)`。这一步只消掉 `S_radix`，不改变 stagewise product state。

### Realized-support 正规化

实际状态只实现其中一部分 packed codes。对已实现 codes 排名得到双射 `[0,|X/E_*|)`，再消掉 `S_inc`。

因此全部 scheduling slack 都能拆成两个精确、分别可正规化的表示 defect。

## 6. Greedy 一般不最优

存在一个五状态三任务系统：从空 context 看，`A,B` 各只需一个 binary symbol，而更丰富的 `C` 需要两个。cheapest-next greedy 会先选 `A` 或 `B`，总成本 `3`；先选 `C` 则只付 `2`，随后 `A,B` 都成为 zero-cost consequence。

所以

\[
\boxed{\text{局部最便宜的下一任务不保证全局最优}.}
\]

精确有限调度应使用 subset/closure-state dynamic program，而不是假定统一 greedy law。

## 7. Zero-cost dependency closure

定义

\[
\operatorname{cl}(S)=S\cup\{j:\rho(j\mid S)=1\}
\]

并迭代到 fixed point。这个 closure 是 extensive、monotone、idempotent。它会删除当前 precision 已经自动决定的任务，因此 exact scheduler 可以只在 closure fixed points 间移动。

但这个 closure 一般不是 matroidal；exchange 可以失败。

## 8. 不能用最小 coordinate 个数定义内禀维数

同一个 final partition 可以有不同基数的 inclusion-minimal task generators。binary tasks `A,B` 与 bundled task `C=(A,B)` 可以让 `{C}` 和 `{A,B}` 都成为同一最终精度的 inclusion-minimal generating sets。

因此“最小 basis 中 task coordinate 的数量”不是 final precision 的内禀维数。必须区分：

\[
\boxed{D_B=L_B(|X/E_*|)}
\]

(final-state depth)，

\[
\boxed{g(\mathcal T)=\min\{|S|:\operatorname{cl}(S)=\mathcal T\}}
\]

(task-language generator number)，以及

\[
\boxed{A_B(\mathcal T)=\min_\sigma C_B(\sigma)}
\]

(acquisition depth)。只有第一项完全由 final partition 本身决定。

## 9. 有界单向 repair 给出近似定理

对两个任务 `E,F`，若 `rho(E,F)<=R`，则先取 `E` 的 base-`B` 总成本至多为

\[
L_B(|X/(E\cap F)|)+L_B(R).
\]

所以统一有界的 directed repair factor 会给出相对最终内禀 depth 的统一 additive approximation，即使反向顺序偶尔更便宜。

## 10. 精确算法

`src/enterprise_math/a2_task_scheduling.py` 实现 context-derived repair factor、order profile、精确动态规划、zero-cost dependency closure、minimal generating task sets、greedy baseline/反例、mixed-radix packing 与 realized-support normalization。

`tests/test_a2_task_scheduling.py` 固定顺序依赖、greedy no-go、closure、unequal-basis 边界、slack 分解与 normalization identities。

## 11. 范围边界

本文是有限声明 task/observation interface 的数学定理。它不声称自然界执行最优编码，不把 task 顺序等同物理时间，也不把选定 interface 升格为本体。各 program 可以消费本 calculus 的特化，但不应复制通用 scheduling 母定理。
