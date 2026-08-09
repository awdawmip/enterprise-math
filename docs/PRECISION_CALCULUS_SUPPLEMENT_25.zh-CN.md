# P018 —— 有限精度证明演算：补充 25

状态：`ACTIVE RESEARCH NOTE`  
范围：n-ary addition 的最小 transport、carry/detail associative composition、operation-tree fusion，以及 persistent state 与 composable transport 的边界  
依赖：P018-T178、T198–T206，以及既有 carry coherence 层  
前人工作边界：radix carry arithmetic、Euclidean decomposition 与 carry associativity/cocycle coherence 都属于成熟数学。项目专门内容是 state/transport minimality 的分离及其 finite transport-complexity 解释。

---

## 1. 从 binary carry 到整棵 addition tree

Supplement 24 已证明

\[
B_{Q_r}(+)=2.
\]

对一次 binary addition，只要 decoder 已知两个 coarse quotient inputs，一个 carry bit 就是精确最小 one-step transport token。

但多次 addition 组成 expression tree 后，会出现更强问题：

> 是否每个 binary node 都必须暴露一个独立 carry bit，还是整棵 tree 可以融合成更小的 exact transport object？

对 addition，这个问题可以精确回答。

写

\[
x_i=r a_i+u_i,
\qquad 0\le u_i<r,
\qquad i=1,\ldots,n.
\]

则

\[
Q_r\!\left(\sum_{i=1}^n x_i\right)
=
\sum_{i=1}^n a_i
+
\left\lfloor\frac{\sum_i u_i}{r}\right\rfloor.
\]

全部 transport ambiguity 被压进一个整数。

---

## 2. P018-T207 —— n-ary addition 的精确 transport branching

状态：`PROVED / EXECUTABLE`

定义 total carry：

\[
\boxed{
c_{r,n}(u_1,\ldots,u_n)
=
\left\lfloor\frac{u_1+\cdots+u_n}{r}\right\rfloor.
}
\]

residue sum 可以实现从 `0` 到

\[
n(r-1)
\]

之间的每个整数，因此 total carry 可以实现

\[
0
\quad\text{到}\quad
\left\lfloor\frac{n(r-1)}r\right\rfloor
\]

之间的每个整数。

所以 exact one-shot transport branching 为

\[
\boxed{
B_{Q_r}(+_n)
=
1+\left\lfloor\frac{n(r-1)}r\right\rfloor.
}
\]

特别地，

\[
B_{Q_r}(+_n)\le n.
\]

当 `n=2` 时恢复 T204。

---

## 3. P018-T208 —— Total carry 就是最小 one-shot token

状态：`PROVED / EXECUTABLE`

已知全部 coarse inputs `a_i` 后，exact coarse output 与

\[
\sum_i a_i
\]

之间只差 `c_(r,n)`。

由于 total carry 的所有可能值都能在一个固定 coarse input cell 内实现，T200 精确给出：

\[
\boxed{
|\mathcal C|_{\min}
=
1+\left\lfloor\frac{n(r-1)}r\right\rfloor.
}
\]

所以 total carry 本身就是 minimum-cardinality deterministic one-shot transport token。

其精确 fixed-length binary cost 为

\[
\boxed{
L_{r,n}
=
\operatorname{bitlen}
\left(\left\lfloor\frac{n(r-1)}r\right\rflooright).
}
\]

全程不需要 floating logarithm。

---

## 4. P018-T209 —— Carry/detail composition law

状态：`PROVED / EXECUTABLE / ESTABLISHED ARITHMETIC FORM`

对任一有限 residue block，保留其 Euclidean transport state：

\[
\boxed{
(c,t)
\quad\text{满足}\quad
\sum u_i=rc+t,
\qquad0\le t<r.
}
\]

对两个 blocks

\[
(rc+t),
\qquad(rc'+t'),
\]

合并后的 state 为

\[
\boxed{
(c,t)\star(c',t')
=
\left(
 c+c'+\kappa_r(t,t'),
 (t+t')\bmod r
\right),
}
\]

其中

\[
\kappa_r(t,t')
=
\left\lfloor\frac{t+t'}r\right\rfloor.
\]

这只是 `(carry,remainder)` 坐标中的精确 Euclidean addition。carry cocycle/coherence 属于成熟算术，也已经在早期 P018 carry 层登记。

这里真正重要的项目解释是：

- `t` 是 persistent exact state detail；
- `c` 是 accumulated transport information；
- 下一步 transport correction 依赖 persistent detail coordinate。

---

## 5. P018-T210 —— Associativity 与 tree independence

状态：`PROVED / EXECUTABLE`

因为 `(c,t)` 无损表示自然数 `rc+t`，所以 `star` associative：

\[
\boxed{
((c,t)\star(c',t'))\star(c'',t'')
=
(c,t)\star((c',t')\star(c'',t'')).
}
\]

因此同一 residue list 的任意 binary parenthesization 都得到同一个 final pair：

\[
\boxed{
\left(
\left\lfloor\frac{\sum_i u_i}{r}\right\rfloor,
\left(\sum_i u_i\right)\bmod r
\right).
}
\]

所以只要 persistent remainder state 与 accumulated transport token 一起传递，additive structured transport 与 operation-tree shape 无关。

---

## 6. P018-T211 —— Fusion 优于独立 binary carry fields

状态：`PROVED / EXECUTABLE`

含 `n` 个 leaves 的 binary tree 有 `n-1` 个 internal addition nodes。若每个 node 都暴露一个独立 fixed one-bit carry field，则 modular transport budget 为

\[
\boxed{n-1\text{ bits}.}
\]

全局 fused minimum one-shot token 只需要

\[
L_{r,n}
=
\operatorname{bitlen}
\left(\left\lfloor\frac{n(r-1)}r\right\rflooright)
\]

bits。

因为

\[
B_{Q_r}(+_n)\le n,
\]

所以对 `n>=2`：

\[
\boxed{
L_{r,n}\le\lceil\log_2 n\rceil\le n-1.
}
\]

因此当整个 expression 可做 fusion 时，generic node-by-node carry transport 可以非常不经济。

这并不表示 sequential implementation 可以删除 intermediate state；比较的是 separate carry fields 的 fixed-width information budget 与“已知全部 coarse leaf inputs”时的 exact one-shot token。

---

## 7. P018-C23 —— Minimum carry token 单独并不能递归组合

状态：`COUNTEREXAMPLE / STRUCTURED-TRANSPORT BOUNDARY`

一个 minimum one-shot token 不一定包含足够信息作为 reusable subtree interface 继续组合。

对任意 `r>=2`，取两个 left subtree transport states：

\[
(0,0),
\qquad(0,r-1).
\]

它们具有**相同 carry token** `0`，但 persistent remainder detail 不同。

再分别与 right subtree state

\[
(0,1)
\]

组合：

\[
(0,0)\star(0,1)=(0,1),
\]

而

\[
(0,r-1)\star(0,1)=(1,0).
\]

下一 carry 不同。

所以

\[
\boxed{
\text{carry token alone is not a closed recursive transport state.}
}
\]

不能因为存在一个很小的 transport token，就把 persistent remainder 当作实现噪声删掉。

---

## 8. P018-T212 —— Radix addition 的 structured transport 完整解

状态：`RESOLVED FOR THIS OPERATION FAMILY`

对通过 `Q_r` 观察的 n-ary natural-number addition，structured transport problem 已有一个完整 finite solution：

1. T178：minimum persistent operand detail 是 residue `u in {0,...,r-1}`；
2. T207/T208：minimum one-shot operation token 是 total carry；
3. T209：recursive composition 由 associative `(carry,remainder)` law 完成；
4. T210：任意 binary tree grouping 结果一致；
5. 全局 fused fixed-width carry cost 至多按 arity 的 logarithm 增长，而 separate node carry fields 要 `n-1` bits；
6. C23 解释了为什么 transport token 与 persistent state 必须继续作为不同概念。

因此 radix addition 给 Q119 提供了一个**正的 structured-composability exemplar**。

这并没有分类其他 operations。T205 已表明 multiplication 的一步 branching 完全不同，可能需要另一种 transport structure。

---

## 9. P018-C24 —— Cardinality 不决定 compositional structure

状态：`FOUNDATIONAL BOUNDARY`

只知道

\[
B_E(\mu)
\]

可以回答 minimum one-shot token alphabet，但无法决定：

- token 是否存在自然 algebraic operation；
- local tokens 能否不依赖额外 state 直接组合；
- 是否存在 associative fusion law；
- representation change 是否保持 token law；
- generic operation-tree product bound 能否 sharp fusion。

addition 能成功，是因为 Euclidean remainder state 与 carry 有精确 composition law。不能仅凭 `B` 很小就推出同样结论。

因此 Q119 必须保持两层分离：

\[
\boxed{
\text{transport cardinality}
\quad\neq\quad
\text{transport algebra}.
}
\]

---

## 10. Supplement 25 之后的 Q119 状态

现在可以严格分成：

### 已解决

- 每个 finite operation 的 exact one-step deterministic token cardinality：T198–T206；
- generic operation-tree product upper bound；
- persistent-state / transport-token inequality；
- radix addition 的 complete structured minimal transport：T207–T212。

### 仍开放

一般 finite operation 何时具有 minimal 或 near-minimal 的 **representation-stable composable transport algebra**。

下一压力测试目标应该比较 `B_E(mu)` 相同或接近、但 composability 不同的 operation families，而不是继续创造 state quotient。

---

## 11. Executable validation

新增：

- `src/enterprise_math/transport_fusion.py`
- `tests/test_transport_fusion.py`

测试验证：

1. 在有限 radix/arity 范围穷举 residue，核验 exact n-ary branching formula；
2. total carry 与 Euclidean reconstruction；
3. `(carry,remainder)` composition associativity；
4. binary tree grouping independence；
5. fused bit cost 从不劣于 `n-1` 个 separate one-bit carry fields；
6. 对所有测试 radix 验证 C23；
7. n-ary transport capacity 至多线性增长，而不是 naive binary-tree token-product 的指数增长。
