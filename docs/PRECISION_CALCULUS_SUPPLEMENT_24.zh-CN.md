# P018 —— 有限精度证明演算：补充 24

状态：`ACTIVE RESEARCH NOTE`  
范围：精确一步 transport branching、最小 deterministic correction-token alphabet、整数 bit cost、operation-tree composition，以及 radix arithmetic 中 remainder/carry 的精确分层  
依赖：P018-T169–T181、T183–T194、T197  
前人工作边界：communication complexity 与 coding for computing 都属于成熟领域。下面的最小 token 结论只是初等有限 deterministic specialization，不主张为新的 communication-complexity 定理。见 `docs/PRIOR_ART_P018_TRANSPORT_COMPLEXITY.*`。[SRC-YAO-1979-DISTRIBUTIVE] [SRC-ORLITSKY-ROCHE-2001-CODING]

---

## 1. State sufficiency 与 transport sufficiency 是不同问题

Supplement 19 已经回答有限 state 问题：

> 为了让所有声明 operations 精确成立，哪些 state distinctions 必须持久保留？

答案是 contextual/syntactic congruence closure。

但一个实际 operation call 可能已经知道 coarse input classes，只需要额外足够的信息来确定**这一次 operation 的 coarse output**。这是另一个信息问题。

对有限 state set `X`、observation equivalence

\[
E=\ker(O),
\]

以及 `k`-ary operation

\[
\mu:X^k\to X,
\]

固定一个 coarse input cell

\[
C=(y_1,\ldots,y_k)\in O(X)^k.
\]

定义其中可实现的 coarse output set：

\[
\operatorname{Out}_E(\mu;C)
=
\{O(\mu(x_1,\ldots,x_k)):O(x_i)=y_i\ \forall i\}.
\]

---

## 2. P018-T198 —— Transport branching capacity

状态：`PROVED / EXECUTABLE`

定义

\[
\boxed{
B_E(\mu)
=
\max_C|\operatorname{Out}_E(\mu;C)|.
}
\]

它表示：**完整 coarse input tuple 已经知道之后**，最坏 coarse input cell 内还可能剩下多少种不同 coarse outputs。

它满足

\[
1\le B_E(\mu)\le |X|.
\]

更细地，如果每个 raw observation fiber 最多包含 `M` 个 fine states，则

\[
B_E(\mu)\le M^k,
\]

因为一个 coarse input cell 最多只有 `M^k` 个 fine tuples。

---

## 3. P018-T199 —— Congruence 恰好等价于零 transport ambiguity

状态：`PROVED / EXECUTABLE`

以下四条等价：

1. `E` 与 `mu` compatible；
2. `mu` 能 exact descent 到 coarse quotient；
3. 每个 coarse input cell 只有一个 realizable coarse output；
4.

\[
\boxed{B_E(\mu)=1.}
\]

所以 transport branching 是 raw precision 一步 operation-congruence failure 的定量版本。

---

## 4. P018-T200 —— 最小 deterministic correction-token alphabet 的精确值

状态：`PROVED / EXECUTABLE / ELEMENTARY COUNTING`

考虑一步 operation call 的 exact one-message protocol。

decoder 已经知道 coarse input tuple `C`；encoder 看到 fine tuple 后发送一个 token

\[
c\in\mathcal C.
\]

decoder 必须从 `(C,c)` 精确恢复

\[
O(\mu(x_1,\ldots,x_k)).
\]

则

\[
\boxed{|\mathcal C|_{\min}=B_E(\mu).}
\]

### 下界

取一个达到 `B_E(mu)` 的 coarse input cell。其中 `B_E(mu)` 个不同 realizable coarse outputs 必须对应可区分的 token；否则同一个 `(C,c)` 会对应两个不同 exact outputs。

故

\[
|\mathcal C|\ge B_E(\mu).
\]

### 上界

在每个 coarse input cell 内，把 realizable coarse outputs 局部编号为

\[
0,\ldots,|\operatorname{Out}_E(\mu;C)|-1.
\]

不同 cells 之间可以复用 token labels，因为 decoder 已知 `C`。没有任何 cell 需要超过 `B_E(mu)` 个 labels，所以大小恰好为该值的 global token alphabet 足够。

参考实现显式构造了这个 codebook。

本定理只讨论 deterministic、zero-error、one-message 的 alphabet cardinality；不涉及概率平均码率、interactive protocol、variable-length coding 或 asymptotic block coding。

---

## 5. P018-T201 —— 精确 fixed-length 整数 bit cost

状态：`PROVED / EXECUTABLE`

对大小为 `B>=1` 的 token alphabet，最小 fixed-length binary word 长度为

\[
\boxed{
L(B)=\operatorname{bitlen}(B-1)=\lceil\log_2B\rceil,
}
\]

其中 `L(1)=0`。

定义

\[
\boxed{L_E(\mu)=L(B_E(\mu)).}
\]

实现只使用 integer `bit_length`，不引入 floating logarithm。

---

## 6. P018-T202 —— Operation-tree transport branching 具有 submultiplicative 上界

状态：`PROVED / EXECUTABLE`

令 outer `k`-ary operation `mu` 接收互不共享 leaf inputs 的 suboperations

\[
\nu_1,\ldots,\nu_k
\]

的输出。复合 operation 为

\[
\Phi=\mu\circ(\nu_1,\ldots,\nu_k).
\]

固定一个 coarse leaf-input cell，每个 `nu_i` 至多产生

\[
B_E(\nu_i)
\]

种 coarse intermediate outputs，因此 intermediate coarse tuples 至多有

\[
\prod_iB_E(\nu_i)
\]

种。

对于每个 intermediate tuple，outer operation 最多再有 `B_E(mu)` 个 coarse outputs，因此

\[
\boxed{
B_E(\Phi)
\le
B_E(\mu)\prod_iB_E(\nu_i).
}
\]

fixed-length bit cost 因而有 generic additive upper bound：

\[
\boxed{
L_E(\Phi)
\le
L_E(\mu)+\sum_iL_E(\nu_i).
}
\]

这是通用 product protocol，不保证最优。严格不等式意味着存在 transport fusion / cancellation，可由更结构化协议利用。

---

## 7. P018-T203 —— Persistent contextual detail 给 transport branching 上界

状态：`PROVED / EXECUTABLE`

令 `R_*` 为包含 `mu` 的 operation language 的 contextual closure。

对每个 raw observation value `y`，定义

\[
m_y
=
\#\{R_*\text{-blocks contained in }O^{-1}(y)\}.
\]

T176 已证明

\[
D=\max_y m_y
\]

是 `(O(x),D(x))` state 表示所需的最小可复用 persistent detail alphabet。

现在固定 coarse input cell

\[
C=(y_1,\ldots,y_k).
\]

第 `i` 个 operand 在 raw fiber 内最多只可能位于 `m_(y_i)` 个 exact contextual-state blocks。因为 `R_*` 是 congruence，contextual blocks 的 input tuple 已唯一确定 output contextual block，从而也唯一确定 raw coarse output。

所以

\[
\boxed{
|\operatorname{Out}_E(\mu;C)|
\le
\prod_i m_{y_i}.
}
\]

全局有

\[
\boxed{B_E(\mu)\le D^k.}
\]

因此：

- `D` = persistent per-operand exact state complexity；
- `B_E(mu)` = 已知 raw coarse inputs 时，operation-specific one-step correction complexity。

两者可以相差很大。

---

## 8. P018-T204 —— Radix quotient addition 的 transport branching 精确等于 2

状态：`PROVED / EXECUTABLE`

令

\[
Q_r(n)=\left\lfloor\frac nr\right\rfloor,
\qquad r\ge2.
\]

写成

\[
x=ra+u,
\qquad y=rb+v,
\qquad0\le u,v<r.
\]

则

\[
Q_r(x+y)=a+b+\left\lfloor\frac{u+v}{r}\right\rfloor.
\]

最后一项始终只能是 `0` 或 `1`。两个值在任一普通 coarse input cell 都能实现：`(u,v)=(0,0)` 给出 `0`，`(r-1,1)` 给出 `1`。

因此

\[
\boxed{B_{Q_r}(+)=2.}
\]

由 T200：

\[
\boxed{|\mathcal C|_{\min}=2,\qquad L_{Q_r}(+)=1.}
\]

规范 token 正是 carry：

\[
\kappa_r(u,v)=\left\lfloor\frac{u+v}{r}\right\rfloor.
\]

再结合 T178：

\[
\boxed{
\text{remainder：}r\text{-state minimum persistent operand detail},
\qquad
\text{carry：}2\text{-symbol minimum one-step transport token}.
}
\]

这是目前 P018 中 state complexity 与 transport complexity 最锋利的分离。

---

## 9. P018-T205 —— Radix quotient multiplication 达到完整 residue-pair branching

状态：`PROVED / EXECUTABLE`

同一个 quotient precision 在 multiplication 下表现完全不同。

写

\[
x=ra+u,
\qquad y=rb+v.
\]

则

\[
Q_r(xy)=rab+av+bu+\left\lfloor\frac{uv}{r}\right\rfloor.
\]

每个 coarse input cell 恰好只有 `r^2` 个 fine residue pairs，所以必有

\[
B_{Q_r}(\times)\le r^2.
\]

而这个上界可以达到。

取 coarse inputs

\[
a=1,
\qquad b=2r.
\]

忽略公共常数 `2r^2`，variable coarse output 为

\[
F(u,v)=2ru+v+\left\lfloor\frac{uv}{r}\right\rfloor.
\]

固定 `u` 时，`F(u,v)` 随 `v` 严格增加，其最大值至多为

\[
2ru+2r-3,
\]

而下一块 `u+1` 的最小值为

\[
2r(u+1)=2ru+2r.
\]

因此不同 `u` 的 `r` 个 value ranges 两两不交；每块内又有 `r` 个不同 `v` values。所有 `r^2` 个 residue pairs 因而产生不同 coarse outputs。

所以

\[
\boxed{B_{Q_r}(\times)=r^2.}
\]

最坏 multiplication cell 的 deterministic one-step token alphabet 至少且恰好需要 `r^2` 个 symbols：

\[
\boxed{L_{Q_r}(\times)=\lceil2\log_2r\rceil.}
\]

从 cardinality 看，最坏 multiplication transport 必须保留完整 joint residue-pair distinction。addition 的 one-bit carry 因而是高度 operation-specific 的结构，不是 quotient precision 的一般福利。

---

## 10. P018-C22 —— 小型 carry-like transport 并不普遍

状态：`COUNTERWEIGHT / DESIGN BOUNDARY`

对同一个 radix quotient state：

\[
B_{Q_r}(+)=2,
\qquad
B_{Q_r}(\times)=r^2.
\]

所以不存在一般性定理：

> coarse quotient arithmetic 总能通过一个小型有界 carry token 修复。

carry cocycle 是 addition 的强特殊结构。其他 operations 的 transport branching 可以大到 coarse cell 的全部 fine-input multiplicity。

因此 P018 必须继续分开：

1. congruence/state closure；
2. exact transport cardinality；
3. 能进一步优雅压缩或组合 token 的额外 algebraic structure。

只有第三层在真正满足相应规律时，才应称为 carry/cocycle-like。

---

## 11. P018-T206 —— Q119 在 unstructured one-step cardinality 层精确解决

状态：`PARTIALLY RESOLVED / EXACT CARDINALITY LAYER`

对有限 state set、有限 operation 与 raw precision equivalence，若 coarse inputs 已知，为恢复一步 exact coarse output 所需的 deterministic one-message correction alphabet 已由

\[
\boxed{B_E(\mu)}
\]

完全刻画。

该层现在具有：

- exact minimum alphabet cardinality；
- exact integer fixed-length bit cost；
- generic operation-tree composition bound；
- persistent contextual detail 给出的直接上界；
- addition 与 multiplication 之间的 sharp arithmetic separation。

这**仍不等于完整解决原始 Q119**。

更强的问题仍开放：

> 什么时候 minimal 或 near-minimal transport tokens 能在 operation trees 上形成 structured、representation-stable、composable algebraic law？generic product composition 与 optimal fused transport 之间的差距怎样刻画？

---

## 12. Executable pressure tests

新增：

- `src/enterprise_math/transport_branching.py`
- `tests/test_transport_branching.py`

测试覆盖：

1. exhaustive two-state binary operations / observations，验证 `B=1` 恰好等于 operation congruence；
2. minimum-size cell-local codebooks 与 encode/decode round trip；
3. exact integer fixed-length bit cost；
4. exhaustive two-state outer-binary / inner-unary composition，验证 T202；
5. contextual-detail product bound；
6. exhaustive two-state local detail bound；
7. radix 2–64 的 addition `B=2`；
8. radix 2–39 的 multiplication `B=r^2`；
9. 直接验证 multiplication transport 可以任意大于 binary addition carry。

---

## 13. 当前 foundational feedback

finite precision stack 现在应当明确分成四问：

\[
\boxed{
\begin{aligned}
&\text{static observation}\\
&\downarrow\\
&\text{contextual closure：minimum persistent exact state}\\
&\downarrow\\
&\text{transport branching }B_E(\mu)：minimum one-step token\\
&\downarrow\\
&\text{structured transport law：在真正存在时才进入 carry/cocycle/fusion。}
\end{aligned}
}
\]

这个分层阻止两个常见误区：

- 把每个 missing state distinction 都当成一个小 carry bit；
- 把一个 compact transport correction 误认为可以消除 persistent exact operand detail。

下一研究目标应当是 **transport fusion 与 representation stability**，而不是再创造新的 state quotient。
