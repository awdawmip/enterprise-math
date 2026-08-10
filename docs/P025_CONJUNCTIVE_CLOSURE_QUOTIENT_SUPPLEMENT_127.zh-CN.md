# P025 补充 127 —— Exact Conjunctive Closure Quotient

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-nonideal-boundary-stage125`  
依赖：P025 补充 125–126；A2/A4 future-signature boundary  
硬阻断：`NONE`

## 1. Unary implication 仍然可能过精

补充 126 已从有限 exact-state family

\[
\Omega\subseteq2^P
\]

构造 largest unary membership-implication preorder。每个 exact state 都成为 semantic quotient poset 的 ideal。但 unary implication 不一定捕获 labels 之间的 higher-order conjunction laws。

Stage 127 推导 exact conjunction quotient。

## 2. P025-D50 —— extent 与 conjunctive closure

对 required label set \(S\subseteq P\)，定义 exact-state extent

\[
\boxed{
E_\Omega(S)
:=
\{X\in\Omega:S\subseteq X\}.
}
\]

定义 closure

\[
\boxed{
\operatorname{cl}_\Omega(S)
:=
\bigcap_{X\in E_\Omega(S)}X,
}
\]

并约定 empty intersection 等于 full label universe \(P\)。

该约定一致：若没有 exact state 包含 \(S\)，也不可能有 exact state 包含 \(P\)，否则该 state 必然也包含 \(S\)。

## 3. P025-T277 —— closure-operator laws

对所有 \(S,T\subseteq P\)：

1. extensivity：
   \[
   S\subseteq\operatorname{cl}_\Omega(S);
   \]
2. monotonicity：
   \[
   S\subseteq T
   \Longrightarrow
   \operatorname{cl}_\Omega(S)
   \subseteq
   \operatorname{cl}_\Omega(T);
   \]
3. idempotence：
   \[
   \operatorname{cl}_\Omega(\operatorname{cl}_\Omega(S))
   =
   \operatorname{cl}_\Omega(S).
   \]

而且每个 exact state \(X\in\Omega\) 本身都是 closed：

\[
\boxed{\operatorname{cl}_\Omega(X)=X.}
\]

所以 exact-state family 嵌入由 exact states 任意 intersection 生成的 closure system。

## 4. P025-T278 —— conjunction future 的 exact operation quotient

核心恒等式是

\[
\boxed{
E_\Omega(S)
=
E_\Omega(\operatorname{cl}_\Omega(S)).
}
\]

任何包含 \(S\) 的 state 都包含这些 states 的 intersection `cl(S)`；而 `S subseteq cl(S)` 给出反向蕴含。

因此

\[
\boxed{
E_\Omega(S)=E_\Omega(T)
\iff
\operatorname{cl}_\Omega(S)
=
\operatorname{cl}_\Omega(T).
}
\]

closure 因而是 conjunction query 在全部 exact states 上 truth vector 的 exact semantic normal form。

这就是 declared exact-state family 诱导的 coarsest query quotient。

## 5. P025-T279 —— semantic implication preorder 是 unary fragment

对 labels \(x,y\in P\)，

\[
\boxed{x\preceq_\Omega y
\iff
x\in\operatorname{cl}_\Omega(\{y\}).}
\]

因此补充 126 可以由 full closure operator 限制到 singleton queries 精确恢复。

unary relation geometry 只是 complete conjunctive theory 的一层，不是全部。

## 6. Strict higher-order compression

取

\[
P=\{a,b,c\}
\]

以及

\[
\Omega
=
\{\{a\},\{b\},\{a,b,c\}\}.
\]

则

\[
\operatorname{cl}(\{a\})=\{a\},
\qquad
\operatorname{cl}(\{b\})=\{b\},
\]

所以 `a,b` 不 unary-equivalent，在 semantic implication poset 中仍 incomparable。

但

\[
\boxed{
\operatorname{cl}(\{a,b\})
=
\{a,b,c\}
=
\operatorname{cl}(\{c\}).}
\]

所以

\[
\boxed{\{a,b\}\sim_{\rm conjunction}\{c\}}
\]

尽管 unary poset 无法把 `{a,b}` 约化成其中一个 member。

semantic implication quotient width 是 2，但 full conjunction language 已把这个 two-label query 与 one-label query 合并。

## 7. Raw query-state collapse

形式上存在

\[
2^{|P|}
\]

个 raw conjunction queries。

exact semantic query-state count 变成

\[
\boxed{|\operatorname{Fix}(\operatorname{cl}_\Omega)|,}
\]

即 closed sets 数量。

上面的 three-label example 中，8 个 raw queries 只剩 4 个 closure classes：

\[
\varnothing,
\{a\},
\{b\},
\{a,b,c\}.
\]

## 8. 对 poset normal form 的 sharpening

补充 119 的 antichain normal form 在**固定 poset 的全部 ideals**上 exact。对 restricted exact-state family，移动到 semantic implication poset 后它仍是 safe normalization，但由于额外 higher-order correlations，未必 coarsest。

因此 Stage 127 把架构精确化为：

\[
\boxed{
\text{unary implication quotient}
\quad\subseteq\quad
\text{full conjunctive closure quotient}.
}
\]

此前 all-ideal scope 下的 theorem 没有失效；只是 task-relative restricted-family quotient 可以更粗。

## 9. 架构结论

真正的 operation/query state 可以直接由 exact-state family 通过 Galois-style closure 内生生成，无需假设 external order。

得到 progression：

\[
\boxed{
\text{external order}
\to
\text{semantic unary implication}
\to
\text{full conjunctive closure}.
}
\]

每一步都继续丢掉没有被实际 future semantics 支持的结构。

## 10. 与 A2/A4 的关系

A2 拥有 generic declared-future signatures；A4 拥有 arbitrary finite correspondences。Stage 127 是 finite Boolean/conjunctive specialization。应把它作为“relation-state geometry 可以从 admissible state family 内生导出”的证据，而不是新的 generic closure theory。

## 11. Prior-art 边界

closure systems、Galois connections、formal concept analysis 与 implication closure 都是标准 prior mathematics。这里不主张 generic novelty。

项目侧贡献是 exact pressure-test placement、unary-poset boundary 的 sharpening 与 executable higher-order collision。历史新颖性仍为 `NOVELTY_UNVERIFIED`。

## 12. 可执行资产

新增：

- `src/enterprise_math/conjunctive_state_closure.py`；
- `tests/test_conjunctive_state_closure.py`。

executable layer 验证 closure laws、extent/closure equivalence、singleton recovery of semantic preorder、exact-state closedness、impossible-query handling，以及 strict higher-order compression example。

## 13. 下一前沿

closure classes 自身仍可能有很小 generators。Stage 128 应定义每个 closure class 的 minimum generator size 以及这些 minima 的 maximum。它给出真正的 worst-case semantic conjunction arity；该值应不超过 semantic implication quotient 的 width，并且在 higher-order dependencies 存在时可以严格更小。
