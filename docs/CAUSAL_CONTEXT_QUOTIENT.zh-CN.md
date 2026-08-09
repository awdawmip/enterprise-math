# Causal Context Quotient —— 任意有限 Composition Future 下的最粗递归状态

状态：`ACTIVE CROSS-ROUTE RESEARCH WIP / ABSTRACT EXACT THEOREM`

归属：一般 quotient / congruence 母理论应由 A2/P023 消费；本文件给出 LEGO binary-composition / arbitrary-dimension specialization。有限可计算版本已由 A3 contextual refinement 实现。

## 1. 动机

`CAUSAL_MINIMAL_RECURSIVE_STATE` 已经在有限 raw witness set 上证明：按所有 left/right partner context 反复细化，可以得到最粗 recursive-safe state。

但“有限 state set 才有最小 recursive state”只是算法条件，不应该成为理论本体限制。

真正的 horizon-independent 定义应直接量化所有 finite composition futures。

## 2. Raw LEGO composition system

给：

- raw state set `X`，可以无限；
- binary causal composition：
  \[
  *:X\times X\to X;
  \]
- declared observation：
  \[
  o:X\to O.
  \]

这里先研究 deterministic total composition。weighted/multivalued join 由 finite A3 specialization 处理。

## 3. Composition context

一个 finite one-hole LEGO context `C[-]` 由以下方式有限生成：

1. 空 context：`[-]`；
2. 若 `C[-]` 是 context，`a in X`，则：
   \[
   a*C[-]
   \]
   是 context；
3. 同理：
   \[
   C[-]*a
   \]
   是 context。

若 raw `*` associative，可把任何 such context 看成有限左右伙伴序列；不必先选择括号作为本体。

## 4. CQ-01 —— causal contextual equivalence

定义：

\[
\boxed{
x\equiv_{ctx}y
\iff
o(C[x])=o(C[y])
\quad\forall\text{ finite contexts }C.}
\]

解释：

> 不论以后把两个 states 放进任何允许的有限 LEGO composition environment，声明的 observation 都永远无法区分它们。

这是 recursive composition language 下的完整 future signature equality。

## 5. CQ-02 —— observation 自动下降

空 context 本身就在量化范围内，因此：

\[
x\equiv_{ctx}y
\Longrightarrow
o(x)=o(y).
\]

故 quotient 上：

\[
\bar o([x])=o(x)
\]

well-defined。

## 6. CQ-03 —— contextual equivalence 自动是 congruence

若：

\[
x\equiv_{ctx}x',
\qquad
y\equiv_{ctx}y',
\]

则：

\[
\boxed{
x*y\equiv_{ctx}x'*y'.}
\]

### 证明

取任意 outer context `C[-]`。

先固定 `y`，把：

\[
D[-]=C[[-]*y]
\]

视为另一个合法 context。由 `x equiv x'`：

\[
o(C[x*y])=o(C[x'*y]).
\]

再固定 `x'`，定义：

\[
E[-]=C[x'*[-]].
\]

由 `y equiv y'`：

\[
o(C[x'*y])=o(C[x'*y']).
\]

合并得结论。∎

因此 binary join 自动下降：

\[
\boxed{
[x]\star[y]=[x*y].
}
\]

传统 algebraic congruence 是 future-context indistinguishability 的 shadow。

## 7. CQ-04 —— 最粗 observation-safe composition quotient

设 `~` 是任意 equivalence relation，并满足：

1. observation-safe：
   \[
   x\sim y\Rightarrow o(x)=o(y);
   \]
2. composition-compatible：
   \[
   x\sim x',y\sim y'\Rightarrow x*y\sim x'*y'.
   \]

则：

\[
\boxed{
x\sim y\Longrightarrow x\equiv_{ctx}y.}
\]

### 证明

对 context 构造深度归纳。

- 空 context：由 observation-safe；
- 左/右加一个 partner：由 congruence 先把 `x~y` 搬运进新的 composition state，再应用归纳。

故任意合法 quotient 都必须细化 contextual quotient。∎

因此：

\[
\boxed{
X/{\equiv_{ctx}}
\text{ 是当前 observation + composition language 下最粗 exact recursive state}.}
\]

这不依赖 `X` 有限。

## 8. Associativity / identity 也自动下降

若 raw `*` associative：

\[
(x*y)*z=x*(y*z),
\]

则 quotient join 同样 associative。

若 raw state 有 identity `e`，则 `[e]` 是 quotient identity。

因此传统 monoid quotient 结构的因果顺序是：

\[
\boxed{
\text{raw LEGO composition law}
+\text{all-context future indistinguishability}
\to
\text{quotient algebra shadow}.}
\]

不是先给 monoid 再问怎样加 precision。

## 9. 与有限 contextual refinement 的关系

若 `X` finite，直接量化无限多个 contexts 不适合执行。

A3 现有：

- `causal_contextual_join.py`；
- `causal_weighted_context_refinement.py`

通过稳定 partition refinement 计算同一母对象的 finite specialization。

有限 weighted raw join 中，signature 还包含：

- output continuation class；
- integer grade shift；
- multiplicity。

稳定 partition 已证明是最粗 recursive-safe refinement，并有小规模全 partition oracle。

## 10. 与 Myhill–Nerode 的关系

若 composition 退化为“prefix + 新 symbol”的 free-word append，且 observation 是 Boolean language membership，则 `equiv_ctx` 退化为经典 residual-language / Myhill–Nerode equivalence。

所以 Myhill–Nerode 是 causal context quotient 的一个重要 `SHADOW_FORMULA / SPECIALIZATION`，不作为本项目原创主张。

本文件的项目性问题是把同一 future-context principle 用于：

- binary LEGO composition；
- coupling witness；
- grade/carry；
- dimension-uniform recursive generation。

## 11. 传统“不可约 n-body”再纠偏

若某高阶 constraint 在当前 exposed state 下不能 factor，不应直接声称绝对 n-body primitive。

正确问题是：

> contextual quotient 是否存在一个复杂度受控的 state，使 binary join 在 quotient 上 well-defined + coherent？

只有在明确 state-capacity / locality / uniformity 限制后仍无法做到，higher primitive claim 才有数学内容。

## 12. 边界

尚未抽象完成：

- weighted/multivalued join 的无限-state contextual quotient；
- quotient 的有效计算复杂度；
- physical locality constraint；
- stochastic/quantum continuation；
- Lean formalization。
