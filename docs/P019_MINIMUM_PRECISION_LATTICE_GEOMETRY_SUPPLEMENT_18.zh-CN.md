# P019 补充 18 —— Quotient-Compatible Dynamics 与 Hidden-to-Coarse Feedback 边界

状态：`RESEARCH WIP / FINITE QUOTIENT CRITERION PROVED`

## 1. 对 Supplement 17 的必要收紧

Supplement 17 证明：如果未来 programs 只有 partition coarsening，则 deleted internal `Z` 永远不可观测，可以安全删除。

但“永远不 refinement”仍然不是一般 dynamics 下的充分条件。

若未来某个 fine operation 先读取 hidden internal relation，再让 coarse totals / relations 发生不同变化，则 hidden detail 可以重新反馈到 coarse 世界，即使 partition 从未变细。

因此真正的安全条件必须写成 operation 对 quotient 的相容性。

## 2. 定义 quotient-compatible transition

设 fine finite state space `X`，current quotient：

\[
Q:X\to Y.
\]

一个确定性 operation

\[
T:X\to X
\]

称为 **Q-compatible**，若：

\[
\boxed{
Q(x)=Q(y)
\Longrightarrow
Q(Tx)=Q(Ty).
}
\]

等价地，存在唯一 coarse transition

\[
\bar T:Q(X)\to Q(X)
\]

满足：

\[
\boxed{
Q\circ T
=
\bar T\circ Q.
}
\]

这只是有限集合上的精确函数因子化，不需要连续结构。

## 3. P019-X58 —— 生成操作全部 descend 即保证任意长 future-safe

设允许的 operation family 为：

\[
\mathcal T=\{T_a\}_{a\in A}.
\]

若每个 `T_a` 都 Q-compatible，且 observation 也只通过 coarse state：

\[
O=\bar O\circ Q,
\]

则对任意有限 operation word：

\[
w=a_1\cdots a_L,
\]

有：

\[
\boxed{
Q(T_wx)
=
\bar T_w(Q(x)).
}
\]

因此：

\[
Q(x)=Q(y)
\Longrightarrow
O(T_wx)=O(T_wy)
\]

对所有有限 `w` 成立。

所以：

\[
\boxed{
Q\text{ 是该 operation/observation language 的 future-safe quotient。}
}
\]

### 证明

由

\[
Q\circ T_a=\bar T_a\circ Q
\]

对 word length 做有限归纳即可。∎

## 4. P019-X59 —— hidden-to-coarse feedback 是不安全性的最小机制

若存在：

\[
Q(x)=Q(y)
\]

但：

\[
Q(Tx)\ne Q(Ty),
\]

则 operation `T` 读取了被 quotient 擦掉的某个 distinction，并把它反馈到了 coarse 可见层。

此时仅一个 future step 就区分 `x,y`。

所以 deleted detail 不安全的最小机制可以写成：

\[
\boxed{
\text{hidden distinction}
\to
\text{operation-dependent branch}
\to
\text{different coarse successor}.
}
\]

这比笼统说“以后可能用到历史”更精确。

## 5. weighted relation quotient 的三个例子

### A. block 内部 redistribution

若 operation 只在一个 current coarse block 内重新分配 fine units，但不改变该 block total/capacity，则：

\[
Q(Tx)=Q(x).
\]

它在 coarse quotient 上 descend 为 identity。

只要未来 observation/operations 始终保持 quotient-compatible，这些 internal moves 永远不可见。

### B. coarse-block dynamics

若一个 operation 的 coarse effect 完全由当前：

- capacities；
- coarse totals；
- weighted relation field

决定，则它直接定义一个 `bar T`，因此安全 descend。

fine 层具体选择 block 内哪个 unit 执行，只要最终 coarse effect 相同，都不影响 quotient dynamics。

### C. hidden-relation feedback

若规则是：

> “若某 coarse block 内 deleted `Z_ij>0`，则向外部 block 转移 1；否则不转移。”

则两个 current weighted quotient 完全相同、但 hidden `Z_ij` 不同的 fine states 可以得到不同 coarse successors。

此 operation 不 Q-compatible。

即使永远没有 refinement，`Z_ij` 仍不能安全删除。

## 6. 与 coarsening-only theorem 的关系

partition coarsening operation 本身天然满足：

\[
Q_\Sigma
=Q_{\Sigma/\Pi}\circ Q_\Pi.
\]

所以 Supplement 17 是 X58 的一个特殊但重要实例：所有 generators 都已经显式 factor through current quotient。

## 7. P019-X60 —— “forward-only”应改称“quotient-closed future language”

更精确的研究术语应是：

\[
\boxed{\text{quotient-closed future language}}
\]

即：

1. observation 只看 current quotient；
2. 每个 future operation 都 descend 到 quotient；
3. operation composition 在 coarse state 上闭合。

对于这种 language：

\[
\boxed{
\text{所有 quotient-erased distinctions 都可永久删除。}
}
\]

“时间只向前”本身不是数学保证；关键是 future dynamics 是否闭合在 coarse quotient 上。

## 8. 与 P021 的进一步统一

P021 发现：witness cardinality matrix 不能自动复合，因为 exact middle witness identity 可能影响后续 chain join。

用 X58 语言可重写：

- 若 witness-cardinality quotient 对下一步 join operation 不 compatible，则不能删 witness identity；
- 若在某结构区间证明 join descend 到 cardinality quotient，则可以安全压缩。

因此 P019/P021 的共同底层工具不应局限于某一种 relation：

\[
\boxed{
\text{先定义 quotient，
再检查所有 future generators 是否 descend。}
}
\]

## 9. 与 P018 的接口

P018 的 precision projection 也可以使用同一标准。

一个 coarse precision state 能否在后续计算中被当作完整 state，不应只由“精度够不够”凭经验判断，而应问：

> 当前允许的 operation family 是否都 factor through 这个 precision quotient？

若是，则 coarse precision 对该任务是 exact；若否，就必须 refinement 或保存 bounded detail/carry。

这可能成为 P018 future-aware precision selection 的通用安全判据。

## 10. 实现与验证

`src/enterprise_math/future_quotient.py` 新增：

- `descended_transition`；
- `transition_descends_to_partition`；
- `operation_family_descends`。

`tests/test_future_quotient.py` 新增最小模型：

- hidden detail 保留在 class 内，但 coarse class swap 相同：transition 可 descend；
- hidden sign 决定是否改变 coarse class：transition 不 descend；
- operation family 只有全部 generators descend 时才被判为安全。

## 11. 前人工作边界

quotient congruence、bisimulation、lumpability、automata minimization 等成熟理论都包含相近的“operation respects equivalence classes”思想。

P019 不把 X58 的一般 quotient factorization 原理作为原创数学。

当前项目价值在于把它作为统一安全门应用到：

- deleted weighted internal relations；
- precision detail；
- contraction history；
- P021 witness transport。

正式合并前需完成对应 prior-art lineage。

## 12. 下一步

1. 对实际 P019 weighted relation operations 建立 operation registry，并自动检查 descend；
2. 对 refinement-capable language，运行 Supplement 08 partition refinement 自动找最小 future-safe relation state；
3. 研究是否可把 `z,rho` detail 只在某些 operation dependencies 激活时懒加载；
4. 把 quotient-compatible criterion 形式化到 Lean；
5. 用同一安全门审计 P018/P021 已有 coarse observables，找出哪些可真正成为 exact compressed states。
