# P025 补充 125 —— Exact Ideal-Law Boundary for Query Normalization

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-nonideal-boundary-stage125`  
依赖：P025 补充 119–124  
硬阻断：`NONE`

## 1. 问题

Stage 119–124 对 exact state 为 order ideal 的情形使用 poset law：

\[
S\subseteq I
\iff
\operatorname{Max}_P(S)\subseteq I.
\]

Stage 125 保留同样 ambient poset labels，但移除 ideal assumption，直接判断 poset width 本身是否足以产生 query-arity saturation。

## 2. P025-T274 —— exact iff boundary

令 `X subseteq P` 为任意 Boolean exact state。以下条件等价：

1. `X` 是 `P` 的 order ideal；
2. 对每个 required set `S subseteq P`，
   \[
   \boxed{
   S\subseteq X
   \iff
   \operatorname{Max}_P(S)\subseteq X;
   }
   \]
3. 只要 `x<=y` 且 `y in X`，就有 `x in X`。

(1) 与 (3) 就是 downward closure 的定义；`(1)->(2)` 是 Stage 119 normalization theorem。

对 `(2)->(3)`，取 comparable pair `x<y` 与 raw query

\[
S=\{x,y\}.
\]

其 maximal antichain 是

\[
\operatorname{Max}(S)=\{y\}.
\]

若 `y in X`，条件 (2) 强迫 `{x,y} subseteq X`，所以 `x in X`。

因此

\[
\boxed{
\text{maximal-antichain query normalization universally safe}
\iff
\text{exact state obeys the ideal law}.
}
\]

## 3. 最小 width-one failure

取二元素 chain

\[
a<b,
\qquad
\operatorname{width}(P)=1,
\]

但允许 non-ideal exact state

\[
X=\{b\}.
\]

则

\[
\{a,b\}\nsubseteq X
\]

而

\[
\operatorname{Max}(\{a,b\})=\{b\}\subseteq X.
\]

所以一旦移除 downward closure，width-one saturation 立刻失败。

因此

\[
\boxed{\text{poset width alone 不是 Stage-120 saturation 的来源}.}
\]

真正来源是 **order relation + exact-state closure under that relation**。

## 4. Pairwise defect certificate

若 `X` 不是 ideal，则存在

\[
x<y,
\qquad y\in X,
\qquad x\notin X.
\]

这一对 labels 已经是 antichain query normalization 失败的 exact certificate：

\[
\{x,y\}\not\subseteq X,
\qquad
\{y\}\subseteq X.
\]

所以 ideal law 的 failure 永远不需要 high-arity counterexample；arity two 就能见证。

## 5. 架构结论

Stage 120 的 width horizon 包含一个隐藏 legality condition。正确形式应读成：

\[
\boxed{
\text{relation geometry}
+
\text{state closure under that relation}
\Longrightarrow
\text{arity collapse bounded by width}.
}
\]

仅仅在 metadata 中存在一张 label order，并不能自动许可 operation-language collapse。

这与 FQ-006 partial-operation legality 的边界同型：structural compression 只有在相关 legality / closure condition 被保存时才 safe。

## 6. 与 A2/A4 的关系

A2 拥有 safe declared-future quotients；A4 拥有 arbitrary finite correspondences。Stage 125 是 negative-boundary specialization：A4 correspondence 不能只因为 labels 带一张外部 partial order，就继承 Stage-120 的 poset-width conclusions。

exact-state fibers 本身必须尊重该 order。

## 7. Prior-art 边界

order ideals 与 downward closure 都是 elementary poset theory。这里不主张 generic novelty。

项目侧结果是此前 P025 precision compiler 的 exact hypothesis boundary 与 executable minimal counterexample。历史新颖性仍为 `NOVELTY_UNVERIFIED`。

## 8. 可执行资产

新增：

- `src/enterprise_math/nonideal_query_boundary.py`；
- `tests/test_nonideal_query_boundary.py`。

executable layer 验证 iff boundary、width-one chain counterexample、pairwise defect certificate，以及 valid ideal boundary cases。

## 9. 下一前沿

若 externally supplied order 不安全，一个 exact-state family 仍会内生出自己的 implication relation：当每个包含 `y` 的 exact state 也包含 `x` 时，定义 `x` semantically below `y`。Stage 126 推导这张 maximal safe preorder 及其 quotient poset。
