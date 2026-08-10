# P025 补充 130 —— 根闭包回路与单轮关系律精度

状态：`PROVED_WIP + EXECUTABLE_CHECKED / NOVELTY_UNVERIFIED`  
Owner：`program/p025-closure-basis-stage130`  
范围：由有限 exact-state family 诱导的 conjunction closure；作为 A2/A4 relation-law precision 的压力测试。

## 1. 设置

设 `P` 为有限标签集，`Omega` 为非空 exact Boolean states 族 `X subseteq P`。定义精确合取闭包

\[
\operatorname{cl}_\Omega(S)
=
\bigcap\{X\in\Omega:S\subseteq X\},
\]

若 extent 为空，则约定交集为整个 `P`。

Stage 127 已证明：两个 conjunction queries 语义等价，当且仅当它们具有相同 closure。

对 `b notin A`，称 `(A,b)` 为一个 **rooted closure circuit（根闭包回路）**，若

\[
b\in\operatorname{cl}_\Omega(A)
\]

并且没有任何真子集 `A' subsetneq A` 已经强迫 `b`。

允许空 premise；它记录 `cl(empty)` 中的 mandatory labels。

## 2. 单轮回路定理

对任意 seed `S subseteq P`，

\[
\boxed{
\operatorname{cl}_\Omega(S)
=
S\cup
\{b:\exists\text{ rooted circuit }(A,b),\ A\subseteq S\}.
}
\]

### 证明

若 `A subseteq S` 且 `b in cl(A)`，由 closure 单调性立即有 `b in cl(S)`，故右侧不会产生错误标签。

反过来，取 `b in cl(S)\S`。在所有满足 `A subseteq S` 且能强迫 `b` 的集合中，选一个按包含关系极小的 `A`。则 `(A,b)` 正是 rooted closure circuit，且其 premise 已包含于 `S`。因此 `cl(S)` 中所有缺失成员都能在一次并行回路触发中加入。证毕。

所以，**完整 rooted-circuit table** 是完整 conjunction semantics 的直接单轮表示。

## 3. 高阶关系律谱

定义

\[
N_k(\Omega)
=
\#\{(A,b):(A,b)\text{ 为 rooted circuit},\ |A|=k\},
\]

以及

\[
h_{\rm circ}(\Omega)
=
\max\{|A|:(A,b)\text{ 为 rooted circuit}\},
\]

若没有非平凡 consequence，则取零。

Stage 129 的 unary-generated 边界可以精确改写为

\[
\boxed{
\operatorname{cl}_\Omega
\text{ 可由 mandatory core + singleton consequences 生成}
\iff
h_{\rm circ}(\Omega)\le1.
}
\]

因为 premise size 至少为 2 的 rooted circuit 正是不可约高阶 implication 的见证；反过来任一 higher-order closure defect 中都可抽出一个包含极小、大小至少为 2 的 premise。

## 4. 精确样本

取

\[
\Omega=\{\{a\},\{b\},\{a,b,c\}\}.
\]

其 rooted circuits 为

\[
\{c\}\Rightarrow a,
\qquad
\{c\}\Rightarrow b,
\qquad
\{a,b\}\Rightarrow c.
\]

所以

\[
N_1=2,\qquad N_2=1,
\qquad h_{\rm circ}=2.
\]

其中 binary circuit 正是 Stage 129 的高阶 defect `a AND b -> c`。

## 5. 负边界：direct circuits 不必构成全局不可约 Horn basis

rooted-circuit table 对“每个 root 的 premise”而言是 inclusion-minimal，但这并不意味着在允许 iterative forward chaining 后仍全局不可删。

对 unary implication chain

\[
a\Rightarrow c\Rightarrow b,
\]

其 exact closure system 的 rooted circuits 为

\[
a\Rightarrow c,
\qquad
c\Rightarrow b,
\qquad
a\Rightarrow b.
\]

最后一条仍是 rooted circuit，因为 `{a}` 是强迫 `b` 的 inclusion-minimal premise；但若允许经由 `c` 迭代推导，则 `a -> b` 是全局冗余规则。

因此必须分开两个资源：

1. **direct one-round relation-law table**：自然由全部 rooted circuits 表示；
2. **iterative implication basis**：可以减少规则数量，但要支付 derivation depth。

Stage 131 应研究这个 storage/depth tradeoff，而不能把完整 circuit table 直接称作 minimum basis。

## 6. 前人工作与 ownership 边界

closure systems、Horn implications、minimal premises/rooted circuits 与 forward chaining 都是经典数学/计算机科学对象，P025 不主张这些一般理论的原创性。

项目侧可复用的是精确压力测试分层：

`semantic closure -> rooted higher-order circuit spectrum -> one-round relation-law precision -> 后续 storage/depth compression`。

generic mother theorem 应由 A2/A4/Foundation 审核；P025 继续作为 specialization 与 counterexample generator。
