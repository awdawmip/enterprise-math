# P025 补充 129 —— Unary-Generated Closure Boundary

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-nonideal-boundary-stage125`  
依赖：P025 补充 126–128  
硬阻断：`NONE`

## 1. 什么时候 semantic implication poset 已经足够？

补充 126 构造 largest unary implication preorder；补充 127 证明 higher-order conjunction laws 会让 full closure 严格更粗；补充 128 定义 exact generator horizon。

Stage 129 精确刻画 unary regime 与 genuinely higher-order regime 的边界。

## 2. P025-D52 —— mandatory core 与 unary-generated closure

定义 always-active / mandatory core

\[
\boxed{M:=\operatorname{cl}_\Omega(\varnothing)=\bigcap_{X\in\Omega}X.}
\]

对 required set \(S\)，定义只用 unary consequences 生成的 closure：

\[
\boxed{
\operatorname{cl}_1(S)
:=
M
\cup
\bigcup_{s\in S}\operatorname{cl}_\Omega(\{s\}).
}
\]

由 exact closure 的 monotonicity，

\[
\boxed{\operatorname{cl}_1(S)\subseteq\operatorname{cl}_\Omega(S).}
\]

差集

\[
\boxed{
D(S):=
\operatorname{cl}_\Omega(S)
\setminus
\operatorname{cl}_1(S)
}
\]

就是 \(S\) 的 genuinely higher-order consequences：它们不是任何单个 member 的 consequence。

## 3. P025-T282 —— exact unary-generated criterion

以下条件等价：

1. 每个 conjunction closure 都由 mandatory core 与 singleton closures 决定；
2. 对所有 \(S\subseteq P\)，
   \[
   \boxed{
   \operatorname{cl}_\Omega(S)=\operatorname{cl}_1(S);
   }
   \]
3. 每个 higher-order defect 都消失：
   \[
   D(S)=\varnothing\quad\forall S.
   \]

这些条件成立时，full conjunctive future 完全由 semantic implication preorder + mandatory core 描述。

若失败，任意满足

\[
D(S)\ne\varnothing
\]

的 \(S\) 就是 unary relation geometry 不足的 exact certificate。

## 4. Minimal higher-order defect example

对

\[
\Omega=\{\{a\},\{b\},\{a,b,c\}\},
\]

有

\[
M=\varnothing,
\]

\[
\operatorname{cl}(\{a\})=\{a\},
\qquad
\operatorname{cl}(\{b\})=\{b\},
\]

但

\[
\operatorname{cl}(\{a,b\})=\{a,b,c\}.
\]

所以

\[
\boxed{D(\{a,b\})=\{c\}.}
\]

这是 irreducible binary implication：`c` 被 `a AND b` 强迫，但不被任一单独 label 强迫。

## 5. P025-T283 —— unary-generated regime 的 exact horizon

令

\[
P_\Omega=P/{\sim_\Omega}
\]

为补充 126 的 semantic implication quotient poset。全部 mandatory labels 都具有 all-ones membership column，所以若 \(M\ne\varnothing\)，它们形成一个 semantic equivalence class。

删除该 mandatory class，得到 induced poset

\[
P_\Omega^{\rm opt}.
\]

若 closure unary-generated，则每个 closed query state 都形如

\[
\boxed{M\cup\downarrow A}
\]

其中 \(A\) 是 optional semantic classes 的 antichain。

该 closed set 的 minimum generator 恰是其 maximal optional antichain。因此

\[
\boxed{g(\Omega)=\operatorname{width}(P_\Omega^{\rm opt}).}
\]

若不存在 optional semantic classes，则把 width 解释为 0，并有

\[
\boxed{g(\Omega)=0.}
\]

## 6. Recovery of ordinary poset width

对 all-ideal universe

\[
\Omega=J(P),
\]

除了 original poset universe 本身强制的 labels 外不存在 mandatory core，并且

\[
\operatorname{cl}(S)=\downarrow S
\]

是 unary-generated。

所以 Stage 129 精确退化为此前 width theorem：

\[
\boxed{g(J(P))=\operatorname{width}(P).}
\]

因此 P025 width-saturation theorem 并非 arbitrary；它是更一般 unary-generated closure criterion 的 special case。

## 7. Mandatory-core correction

若

\[
\Omega=\{\{m\},\{m,a\},\{m,a,b\}\},
\]

则

\[
M=\{m\}
\]

始终 active，不应为 query generator 付费。optional semantic poset 是 chain

\[
a<b,
\]

所以

\[
\boxed{g(\Omega)=1.}
\]

若唯一 exact state 就是 full universe，则全部 semantic classes 都 mandatory，

\[
\boxed{g(\Omega)=0.}
\]

这就是 exact formula 使用 **optional** semantic width，而不是未修正 preorder width 的原因。

## 8. 架构结论

Stage 125–129 已识别四层不同 relation geometry：

\[
\boxed{
\begin{array}{ccl}
\text{external relation} &:& \text{可能 unsafe};\\
\text{semantic unary preorder} &:& \text{largest safe unary relation};\\
\text{full conjunctive closure} &:& \text{exact operation quotient};\\
\text{minimum closure generators} &:& \text{exact semantic arity cost}.
\end{array}}
\]

unary preorder 精确在 closure 由 singleton consequences + mandatory core 生成时 complete。

这给出何时 poset-width representation 合法、何时必须进入 higher-order relation state 的精确规则。

## 9. 与 A2/A4 的关系

A2 拥有 generic future quotients；A4 拥有 arbitrary correspondence / witness structure。Stage 129 是 Boolean conjunction specialization，给出 unary relation geometry 何时足够的 exact criterion。

应把它作为 foundation pressure test，而不是竞争性的 generic Horn/FCA theory。

## 10. Prior-art 边界

unary implication systems、closure operators、Horn-style higher-order implications 与 formal concept analysis 都是 classical。这里不主张 generic novelty。

项目侧贡献是 P025 中 width-governed unary precision 与 genuinely higher-order closure precision 之间的 exact boundary。历史新颖性仍为 `NOVELTY_UNVERIFIED`。

## 11. 可执行资产

新增：

- `src/enterprise_math/unary_generated_closure.py`；
- `tests/test_unary_generated_closure.py`。

executable layer 检查 all-ideal width recovery、higher-order synergy defect、mandatory-core removal、zero-horizon all-mandatory case，以及 independent optional width-two states。

## 12. Natural generation boundary

Stage 125–129 已形成 coherent hypothesis-repair generation：

\[
\boxed{
\text{external width failure}
\to
\text{ideal-law iff boundary}
\to
\text{endogenous semantic preorder}
\to
\text{full conjunction closure}
\to
\text{exact generator horizon}
\to
\text{unary-generated iff boundary}.
}
\]

下一 generation 不应继续问 width 是否正确，而应研究 genuinely higher-order closure regime：minimal implication bases、closure-circuit size、closure systems composition，或 closure generators 与 A4 multivalued witness correspondences 的关系。
