# P008 最小性收口 —— v0.1 核心真正需要的最弱序结构

状态：`PROVED STRUCTURAL RESOLUTION`  
父问题：`P008`

## 1. 问题

P008 要求寻找：在不引入连续体假设的前提下，支撑 v0.1 根/坍缩核心所需的最小代数/序结构是什么。

此前 P008 已经确认 Galois connection 是正确的成熟语言。本文把这个答案进一步收紧为必要—充分条件，并明确区分三个不能混淆的层次：

1. 不等式层面的伴随；
2. 对不同显式状态保持真实相等语义的坍缩；
3. 对左侧生成状态的精确恢复。

不需要格、完备格、域、拓扑或实数完备化。

## 2. 主下水平集合

设 \(A,B\) 为偏序集，并有

\[
l:A\to B.
\]

对 \(b\in B\)，定义主下水平集合

\[
L_b=\{a\in A:l(a)\le b\}.
\]

\(l\) 的右伴随是映射

\[
u:B\to A
\]

满足

\[
\boxed{l(a)\le b\iff a\le u(b).}
\]

## 3. P008-M01 —— 右伴随恰好就是“取最大下水平元素”

状态：`PROVED`

映射 \(u:B\to A\) 是 \(l\) 的右伴随，当且仅当对每个 \(b\in B\)，\(u(b)\) 都是 \(L_b\) 的最大元。

### 必要性

假设

\[
l(a)\le b\iff a\le u(b).
\]

取 \(a=u(b)\)，得

\[
l(u(b))\le b,
\]

所以 \(u(b)\in L_b\)。

若 \(a\in L_b\)，则 \(l(a)\le b\)，从而

\[
a\le u(b).
\]

所以 \(u(b)\) 是 \(L_b\) 最大元。

### 充分性

反过来，若每个 \(L_b\) 都有最大元 \(u(b)\)，那么

\[
l(a)\le b
\]

恰好等价于 \(a\in L_b\)，而这又恰好等价于

\[
a\le u(b).
\]

所以 \(l\dashv u\)。∎

### 后果

进取数论里使用的 `max` 不是实现技巧，而正是右伴随的序论内容。

我们不需要任意集合都有 supremum；只需要这些特定下水平集合拥有最大元。

## 4. 根与商都是这一结构的实例

### 整数根

取

\[
l(k)=k^p
\qquad(p\ge1).
\]

对每个 \(n\in\mathbb N\)，

\[
L_n=\{k:k^p\le n\}
\]

的最大元就是 \(R_p(n)\)。因此

\[
k^p\le n
\iff
k\le R_p(n).
\]

### 整数商

取

\[
l(q)=dq
\qquad(d\ge1).
\]

对每个 \(n\)，

\[
L_n=\{q:dq\le n\}
\]

的最大元就是 \(Q_d(n)=n//d\)。因此

\[
dq\le n
\iff
q\le Q_d(n).
\]

所以根和商真正需要的是同一个最小“下水平最大元”结构。

## 5. P008-M02 —— 诱导的同空间投影就是 interior operator

状态：`PROVED`

设

\[
l\dashv u
\]

位于偏序之间，并定义

\[
C=l\circ u:B\to B.
\]

则：

### 向下收缩

\[
C(b)\le b.
\]

### 单调

\[
b_1\le b_2
\implies
C(b_1)\le C(b_2).
\]

### 幂等

\[
\boxed{C(C(b))=C(b).}
\]

### 不动点

\[
\boxed{C(b)=b\iff b\in\operatorname{im}(l).}
\]

这些都是偏序 Galois connection 的成熟标准结论，mathlib 已有相应 API。

所以项目不需要自己创造一套抽象“坍缩代数”。

## 6. P008-M03 —— 精确恢复左侧状态等价于 order embedding

状态：`PROVED`

设 \(A,B\) 为偏序，并有

\[
l\dashv u.
\]

以下条件等价：

1. 对所有 \(a\in A\)，\(u(l(a))=a\)；
2. \(l\) 反射序：

\[
l(a)\le l(a')\implies a\le a';
\]

3. 因为所有左伴随本来都单调，所以 \(l\) 是其像上的 order embedding。

### embedding 推出恢复

伴随总是给出

\[
a\le u(l(a)).
\]

同时有

\[
l(u(l(a)))\le l(a).
\]

若 \(l\) 反射序，则

\[
u(l(a))\le a.
\]

因此相等。

### 恢复推出序反射

若

\[
l(a)\le l(a'),
\]

伴随给出

\[
a\le u(l(a'))=a'.
\]

所以 \(l\) 反射序。∎

### 对进取数论的后果

\[
R_p(k^p)=k
\]

和

\[
Q_d(dq)=q
\]

不是两个孤立巧合。它们来自同一个事实：正整数幂构造与正整数乘法构造都是 order embedding。

## 7. 为什么仅有 preorder 不足以支持“真实状态相等”

Galois connection 完全可以定义在 preorder 上；只做不等式推理时，这已经足够。

但 preorder 允许不同状态满足

\[
x\le y
\quad\text{且}\quad
y\le x
\]

却仍然 \(x\ne y\)。

因此，标准伴随规律可能只能确定到 preorder 等价类，而不能确定到显式状态相等。

若进取数论把不同显式状态真的当作不同状态，那么 equality-level 的坍缩语义需要 antisymmetry；或者必须先把 preorder 按等价关系商掉。

## 8. P008-C01 —— 一个合法 preorder Galois connection，其诱导坍缩并不按真实相等幂等

状态：`COUNTEREXAMPLE`

取

\[
A=\{a_0,a_1\},
\qquad
B=\{b_0,b_1\},
\]

并在两个集合上都使用 indiscrete preorder：任意元素都 \(\le\) 任意元素。

定义

\[
l(a_0)=b_0,
\qquad
l(a_1)=b_1,
\]

以及

\[
u(b_0)=a_1,
\qquad
u(b_1)=a_0.
\]

因为两个 preorder 中所有比较都为真，所以

\[
l(a)\le b\iff a\le u(b)
\]

对所有 \(a,b\) 都成立，因此 \(l\dashv u\) 是完全合法的 Galois connection。

但诱导映射

\[
C=l\circ u
\]

满足

\[
C(b_0)=b_1,
\qquad
C(b_1)=b_0.
\]

于是

\[
C(C(b_0))=b_0\ne b_1=C(b_0).
\]

所以按真实状态相等，幂等性失败；尽管所有这些状态在 preorder 中彼此等价。

这正好说明：如果显式状态身份本身具有语义意义，偏序的 antisymmetry 为什么重要。

### 商集修复

如果对每个 preorder 按

\[
x\sim y\iff x\le y\land y\le x
\]

取商，那么上述两个元素的 indiscrete preorder 会变成只有一个状态的偏序，真实相等歧义消失。

因此最小选择是：

- 直接使用 partial order；或
- 使用 preorder，但先显式取 posetal reflection。

## 9. 不需要 lattice 结构

### P008-C02 —— 非格偏序也已经可以支撑伴随/坍缩核心

状态：`COUNTEREXAMPLE TO OVER-STRONG ASSUMPTIONS`

取

\[
P=\{0,a,b\}
\]

并规定

\[
0<a,
\qquad 0<b,
\]

而 \(a,b\) 互不可比，并且在 \(P\) 中没有共同上界。

则 \(P\) 是偏序，但不是格，因为 \(a\vee b\) 不存在。

然而

\[
\operatorname{id}_P\dashv\operatorname{id}_P,
\]

诱导投影就是恒等映射，并满足所有向下收缩、单调与幂等规律。

所以 abstract adjoint-collapse core 不需要格运算。

更不需要 complete lattice。

## 10. v0.1 equality 语义真正需要的最小包

在 order-adjoint 路线内，最小而干净、能忠实保留状态相等的结构是：

1. partial orders \(A,B\)；
2. 一个 order embedding

\[
l:A\hookrightarrow B;
\]

3. 对每个 \(b\in B\)，下水平集合

\[
\{a:l(a)\le b\}
\]

都拥有最大元。

把该最大元定义为 \(u(b)\)。于是自动得到

\[
l\dashv u,
\]

\[
u\circ l=\operatorname{id}_A,
\]

并且

\[
C=l\circ u
\]

是单调、向下收缩、幂等的投影，不动点集合恰好是 \(\operatorname{im}(l)\)。

在这一抽象层面，不需要 join、meet、任意 supremum、任意 infimum、加法、乘法、域结构、拓扑、度量或连续体完备化。

## 11. 为什么这不构成新数学主张

上述每一部分都是成熟序论：

- Galois connection；
- order embedding；
- 主下水平集合的最大元；
- interior operator / coreflection；
- preorder 的 posetal reflection。

P008 的作用是**结构降维**：确认 v0.1 运算究竟需要哪些成熟结构，并明确拒绝那些没有参与任何证明的更强假设。

## 12. P008 解决状态

对当前 v0.1 根/商/坍缩族，P008 的字面“最弱结构”问题现在可以结构性解决：

- preorder 足以支撑只到等价类层面的伴随；
- 若不同显式状态的真实相等具有意义，则 partial order 是最小直接选择；
- 生成态精确恢复要求左映射为 order embedding；
- 右伴随存在恰好要求相关下水平集合具有最大元；
- lattice 与 completeness 都不是必要条件。

未来新增运算可能需要更丰富结构，但应逐个运算证明其必要性，而不是反过来把更强结构一次性塞回 v0.1 基础。
