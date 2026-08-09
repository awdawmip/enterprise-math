# A3 Guard-Image Lattice 补充 04 —— Reachable-Effect Quotient 与 State-Local Branch Erasure

状态：`RESEARCH WIP / EXACT RANK-ONE/TWO BRANCH-ERASURE CHECKER`

## 1. 从“branch 可达”回到 future-safe precision

A2/P023 的一般原则是：一个 quotient 只有在 future program 无法通过它删除的区别产生不同 coarse future 时才安全。

A3 已把 multi-guard coarse fiber 的 hidden predicate geometry 压成：

\[
L_G=W(K_A).
\]

但仅知道哪些 branch pattern 可达还不够。真正的 retention obligation 来自：

> **实际可达的 fine branch 是否产生不同 coarse effects。**

因此固定 coarse fiber `y`，记其可达 pattern 集：

\[
R_y\subseteq\{\mathrm F,\mathrm T\}^r.
\]

设 branch effect map 为：

\[
E:\{\mathrm F,\mathrm T\}^r\to\mathcal Y,
\]

其中 `E(sigma)` 可以按任务语义表示：

- 当前一步的 coarse output；或
- 一个完整 descended coarse affine map / transition object；或
- 其他调用方声明的可比较 coarse future effect。

## 2. A3-G16 —— Reachable-Effect Erasure Criterion

对固定 coarse fiber：

\[
\boxed{
\text{hidden branch identity 可擦除}
\iff
E|_{R_y}\text{ 为常值。}
}
\]

即：

\[
\boxed{
|\{E(\sigma):\sigma\in R_y\}|=1.
}
\]

### 必要性

若存在两个可达 patterns：

\[
\sigma,\tau\in R_y
\]

且：

\[
E(\sigma)\neq E(\tau),
\]

则同一个 coarse state 的两个 fine lifts 会产生不同 coarse effect，当前 quotient 不 exact。

### 充分性

若所有可达 branch 的 coarse effect 完全相同，则无论 fine lift 落入哪一个实际 branch，coarse future 都一致。不可达 branch 从未在该 fiber 出现，因此其 effect 不构成 precision obligation。

这严格推广 binary hidden-guard erasure：binary 主文中 hidden guard 保证两个 patterns 都可达，所以当时必须比较两个 branch；multi-guard partial rank 下只能比较**实际可达集合**。

## 3. Unreachable branch 不创造 precision obligation

该结论的一个重要纠偏是：

\[
\boxed{
\text{branch 代码存在}
\not\Rightarrow
\text{当前 coarse state 必须能区分该 branch}.
}
\]

若某 pattern：

\[
\sigma\notin R_y,
\]

则即使 `E(sigma)` 与所有可达 effects 都不同，也不影响当前 fiber exactness。

所以 future precision 必须由：

\[
\boxed{
\text{reachable behavior}
}
\]

而不是 program syntax 的全部理论分支数决定。

## 4. A3-G17 —— rank-one reachable patterns 的 switch sweep

rank-one hidden lattice：

\[
g+t h,\qquad t\in\mathbb Z.
\]

每个 nonconstant guard：

\[
g_j+t h_j
\]

随 `t` 单调，并且只翻转一次 Boolean threshold。

### `h_j>0`

从 `False` 翻成 `True` 的第一个整数点是：

\[
\boxed{t_j=-\lfloor g_j/h_j\rfloor.}
\]

### `h_j<0`

最后一个 `True` 点是：

\[
\lfloor g_j/(-h_j)\rfloor,
\]

所以下一个整数点翻成 `False`：

\[
\boxed{t_j=\lfloor g_j/(-h_j)\rfloor+1.}
\]

### `h_j=0`

该 guard 在整个 fiber 上恒定。

因此：

1. 直接写出 `t -> -infinity` 的初始 pattern；
2. 按所有 switch integers 排序；
3. 同一点翻转的 guards 同时更新；
4. 每个 distinct switch 后得到下一个 reachable pattern。

所以若 nonconstant guards 数为 `q`：

\[
\boxed{|R_y|\le q+1.}
\]

这比一般 rank-one face bound `2q+1` 更紧，因为 binary integer threshold 已把 boundary value `0` 归入 `True`，而一维每个 guard 只产生一次状态翻转。

该 sweep 不需要枚举 `2^r` patterns，也不需要逐 pattern 调 solver。

## 5. rank-two exact erasure

rank-two 情形直接复用 Supplement 02：

\[
R_y
=
\{\sigma:\text{rank-two integer halfplane system for }\sigma\text{ feasible}\}.
\]

若 branch table 本身已经显式列出全部 `2^r` effects，那么逐条调用 exact rank-two reachability 不增加超过 program 输入表示本身的指数展开。

对每一个可达 `sigma` 收集：

\[
E(\sigma).
\]

只要 distinct effect 数超过 1，立即得到 non-exact certificate；若全部相同，则 branch identity 在该 fiber 可安全擦除。

后续如果 branch map 是隐式生成的，则应结合 Supplement 03 的 arrangement faces 避免枚举全部 syntactic branches；这属于下一层编译/算法问题。

## 6. A3-G18 —— State-Local Effect Ambiguity

定义：

\[
\boxed{
a_E(y)=|\{E(\sigma):\sigma\in R_y\}|.}
\]

则：

- `a_E(y)=1`：当前 coarse fiber 对该 effect language exact；
- `a_E(y)>1`：至少存在两个 fine lifts 产生不同 declared coarse effects，当前 quotient 不 exact。

该量不是新的信息熵；它只是一个 finite cardinality witness，可与 P011/P023 的 fiber/ambiguity 工具后续组合。

重要的是：

\[
\boxed{
a_E(y)\le |R_y|\ll 2^r}
\]

在低 hidden rank 情形可以非常显著。

## 7. 实现

新增：

- `src/enterprise_math/guard_branch_erasure.py`；
- `tests/test_guard_branch_erasure.py`。

主要接口：

- `rank_one_reachable_patterns`；
- `rank_one_branch_erasure_report`；
- `rank_two_branch_erasure_report`；
- `BranchErasureReport`。

report 返回：

- exact reachable pattern set；
- reachable distinct effects；
- `safe_to_erase` Boolean。

测试保存两个关键案例：

1. rank-one diagonal guard：mixed patterns 不可达；即使这些 branch effects 任意不同，只要 `(F,F)` 与 `(T,T)` effect 相同，仍可安全擦除；
2. rank-two `scores=(s,t,s+t)`：`(F,F,T)` 不可达，因此该 pattern 的独有效果不应制造 precision obligation；但任一实际可达 pattern 的不同 effect 会使 erasure 失败。

## 8. 精度含义

这一步把 future precision 从：

`必须知道 branch identity`

进一步压成：

\[
\boxed{
\text{只需要区分实际可达且 coarse effect 不等价的 branch classes。}
}
\]

因此，对一个 task：

- 若 `a_E(y)=1`，当前 partition 在该 state 不需要额外 relation refinement；
- 若 `a_E(y)>1`，必须 refinement 或增加某种能区分这些 effect classes 的 retained relation/witness detail。

当前还不能从 `a_E(y)>1` 直接推出最小 refinement rank，因为 piecewise exactness 已知不对任意 refinement 单调；最小 partition 仍需结构 solver。

## 9. 与 A2/P023 的归属

`E|R_y` 常值 iff branch identity 可删，本质上是一般 future-compatible quotient 的 state-local specialization，母定理属于 A2/P023。

A3 的独有部分是可计算 reachable set：

- rank one：整数 switch sweep；
- rank two：exact lattice halfplane solver；
- fixed higher rank：可调用 Supplement 03 的 lattice-basis + fixed-dimension ILP reduction。

不在 A3 复制 behavioral-equivalence 母理论。

## 10. 下一步

1. 把 `a_E(y)>1` 的 effect classes 反推成最小 guard/relation refinement obligation；
2. 研究多个 coarse states 上是否可以把 state-local erasure 合成为一个有限 coarse program，而不重新暴露全部 guards；
3. 对 rank-two implicit branch rules 用 arrangement face traversal 代替 explicit `2^r` branch table；
4. 将 branch-erasure checker 接入 relation rank/quantum precision profile；
5. 选择 P021 或 A3→A4 staged-support 中一组真实 predicates 做跨路线验证。
