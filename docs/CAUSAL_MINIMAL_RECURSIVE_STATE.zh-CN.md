# Causal Minimal Recursive State —— 有限 Weighted LEGO Join 的最粗安全 Contextual Quotient

状态：`ACTIVE CROSS-ROUTE RESEARCH WIP / EXACT FINITE THEOREM + EXECUTABLE REFERENCE`

归属：A3 finite weighted specialization。一般 future-safe quotient 母理论仍归 A2/P023。

## 1. 问题

已有 `kappa(r,tau)` 说明：raw witness identity 一般不必永久保存，真正需要的是剩余未来还能区分的 continuation type。

但当“继续和新的 LEGO block 拼接”本身就是 future operation 时，`tau` 不能只根据普通单体 future 定义。它还必须保证 binary coupled composition 在 quotient 后仍然 well-defined。

本文给出有限 weighted join 的精确答案。

## 2. Raw weighted join

令有限 raw witness set 为 `X`，当前 observation：

\[
o:X\to O.
\]

binary raw join kernel：

\[
\boxed{
J(x,y;z,\delta)\in\mathbb N_0,
}
\]

其中 `delta` 是 integer grade shift。

`J=0` 表示该 raw output 不存在；正整数表示对应 raw joint witnesses 的 multiplicity。

## 3. Recursive-safe partition

partition `P` 被称为 recursive-safe，当：

### 当前 observation 不丢

\[
x\sim_Px'\Longrightarrow o(x)=o(x').
\]

### binary composition 可下降

若：

\[
x\sim_Px',\qquad y\sim_Py',
\]

则对任意 output block `C in P` 和任意 integer shift `delta`：

\[
\boxed{
\sum_{z\in C}J(x,y;z,\delta)
=
\sum_{z\in C}J(x',y';z,\delta).
}
\]

这正是“同 continuation types 的任意 raw representatives 拼接后，得到同一个 typed multiplicity/grade profile”。

## 4. Contextual refinement algorithm

从 observation partition `P_0` 开始。

给当前 partition `P_t`，对每个 raw state `x` 记录：

1. `o(x)`；
2. 对每个 raw partner `p`，`J(x,p)` 聚合到 `P_t` output classes 后的 `(class,delta,multiplicity)` profile；
3. 对每个 raw partner `p`，`J(p,x)` 的同类 profile。

相同 signature 留在一起，不同 signature 分裂，得到 `P_(t+1)`。

有限 state set 上，该过程只能有限次严格细化，因此必稳定。

## 5. MR-01 —— 最粗 recursive-safe theorem

令稳定 partition 为：

\[
P_*.
\]

则：

\[
\boxed{
P_*\text{ 是所有 refinement of }P_0
\text{ 中最粗的 recursive-safe partition}.}
\]

### 证明骨架

设 `S` 是任意 recursive-safe partition，且 `S` 细化 `P_0`。

对 refinement round 归纳证明：

\[
S\preceq P_t.
\]

若在 `S` 中 `x~x'`，则对任意 raw partner `p`：

- `p` 本身落在某个 `S` block；
- recursive-safe 保证 `J(x,p)` 与 `J(x',p)` 在每个 `S` output block/grade 上相同；
- 归纳假设下，每个 `P_t` block 是若干 `S` blocks 的并，因此聚合到 `P_t` 后仍相同；
- 左 context 同理。

故 `x,x'` 在下一轮 signature 仍相同，`S` 继续细化 `P_(t+1)`。

稳定后任何 safe `S` 都细化 `P_*`；而 `P_*` 自身由稳定条件满足 recursive-safe，故结论成立。

因此 `P_*` 不是 heuristic summary，而是**当前 observation + binary join language 下的最小 exact identity-free recursive state**。

## 6. MR-02 —— induced typed kernel

在 `P_*` classes 上定义：

\[
\boxed{
K(A,B;C,\delta)
=
\sum_{z\in C}J(x,y;z,\delta),
\qquad x\in A,\ y\in B.
}
\]

MR-01 保证右边与 representatives 无关，所以 `K` well-defined。

这就是 `kappa(r,tau)` 思路在 binary composition language 下的闭合形式：最终 runtime state 不保存 raw identity，只保存 contextual type inventory。

## 7. MR-03 —— raw associativity 自动下降

若 raw weighted join 满足 exact typed witness associativity：

\[
\sum_{u,d_1+d_2=d}
J(a,b;u,d_1)J(u,c;v,d_2)
=
\sum_{u,d_1+d_2=d}
J(b,c;u,d_1)J(a,u;v,d_2)
\]

对所有 raw typed outcomes成立，则 induced `K` 满足同样 associativity。

因此：

\[
\boxed{
\text{associative raw coupled world}
\to
\text{minimal contextual quotient }P_*
\to
\text{associative typed kernel }K.
}
\]

任意维 inventory 随后可由同一个 `K` binary recursion 生成，而不恢复 raw witness identity。

## 8. Observation language 会改变最小 state

同一个 raw dynamics 并不存在唯一“数学上正确 state”。最小 state 取决于未来真的读取什么。

例：mod-4 residue addition。

若只观察 parity，并且 pair grade shift 一律不读：

\[
0\sim2,
\qquad
1\sim3
\]

可保持为 2 个 contextual types。

若 future 还读取 base-4 carry：

\[
\gamma(a,b)=\lfloor(a+b)/4\rfloor,
\]

则：

`0+3` 与 `2+3` 的 carry 不同，故 `0,2` 必须分开；同理最终需要 4 个 types。

所以：

\[
\boxed{
\text{state granularity}
=
\text{future causal language 的结果，非先验 precision 声明}.
}
\]

## 9. 与 coupling order 的关系

若 current marginal state 过粗，minimal nonface 可能表现成高 coupling order。

先求 `P_*` 后再看 induced `K`：

- 若 `K` associative，原高阶 failure 已被 continuation state 局部化；
- 若仍失败，则当前 raw binary law 本身不 coherent，或输入模型缺少必要 higher compatibility data。

因此“高阶 coupling”分析顺序必须是：

\[
\boxed{
\text{exposed failure}
\to
\text{minimal contextual refinement}
\to
\text{typed coherence test}
\to
\text{higher primitive claim (if still needed)}.
}
\]

## 10. 可执行资产

- `src/enterprise_math/causal_weighted_context_refinement.py`
- `src/enterprise_math/causal_recursive_join.py`
- `tests/test_causal_weighted_context_refinement.py`
- `tests/test_causal_recursive_join.py`

## 11. 边界

这是 finite weighted deterministic-description / multiplicity-kernel 层的 exact theorem。

尚未解决：

- infinite raw witness spaces 的最粗 contextual quotient；
- fixed integer-schema complexity 的一般最小化；
- stochastic/quantum amplitudes；
- physical FCC/HCP grade law；
- Lean formalization 与 clean integration CI。
