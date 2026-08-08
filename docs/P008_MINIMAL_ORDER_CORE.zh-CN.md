# P008 —— 最小且保持真实相等语义的序结构核心

状态：`PROVED STRUCTURAL RESOLUTION`

## 结论

对当前 v0.1 的根 / 商 / 坍缩结构，进取数论不需要格、完备格、域、拓扑、度量或实数完备化。

设 `A`、`B` 为偏序状态空间，并有

\[
l:A\to B.
\]

对每个 \(b\in B\)，定义主下水平集合

\[
L_b=\{a\in A:l(a)\le b\}.
\]

右伴随 \(u:B\to A\) 存在，当且仅当每个 \(L_b\) 都具有最大元；该最大元正是 \(u(b)\)。等价地，

\[
l(a)\le b\iff a\le u(b).
\]

因此，整数根与整数商中使用的 `max` 定义，本质上就是右伴随结构，而不是某种近似手段。

## 精确恢复

假设 \(l\dashv u\)。那么

\[
u(l(a))=a\quad\text{对所有 }a
\]

成立，当且仅当 \(l\) 反射序。因为任何左伴随本来就单调，所以这恰好等价于 \(l\) 在其像上是 order embedding。

这个统一结构同时解释

\[
R_p(k^p)=k
\]

与

\[
Q_d(dq)=q.
\]

## 诱导坍缩

定义

\[
C=l\circ u:B\to B.
\]

在偏序上，标准 Galois connection 理论给出

\[
C(b)\le b,
\]

单调性，

\[
C(C(b))=C(b),
\]

以及

\[
C(b)=b\iff b\in\operatorname{im}(l).
\]

所以抽象坍缩核心就是成熟的 interior/coreflection 投影。进取数论不把这些一般序论规律作为新数学主张。`SRC-MATHLIB-CLOSURE` 与 `SRC-MATHLIB-FLOORDIV` 已记录相关成熟结构邻域。

## 为什么仅有 preorder 不足以支持显式状态身份

Galois connection 可以定义在 preorder 上，但不同状态可能同时满足 \(x\le y\) 与 \(y\le x\)。此时伴随规律只能把结果确定到 preorder 等价类，而不能保证显式状态本身相等。

具体反例：令 `A={a0,a1}`、`B={b0,b1}` 都带 indiscrete preorder，即所有比较都为真。定义

\[
l(a_0)=b_0,\qquad l(a_1)=b_1,
\]

以及

\[
u(b_0)=a_1,\qquad u(b_1)=a_0.
\]

由于任意伴随比较两侧都为真，所以这是合法的 Galois connection。但

\[
(l\circ u)(b_0)=b_1,
\qquad
(l\circ u)(b_1)=b_0,
\]

于是按真实相等，幂等性失败：

\[
C(C(b_0))=b_0\ne b_1=C(b_0).
\]

因此，最小的 equality-faithful 选择只能是：

1. 直接使用 partial order；或
2. 对 preorder 先按
   \[
   x\sim y\iff x\le y\land y\le x
   \]
   取商。

## 不需要 lattice

取三元素偏序 `0<a`、`0<b`，其中 `a,b` 互不可比，且没有共同上界。该偏序不是格，但

\[
\operatorname{id}\dashv\operatorname{id}
\]

仍然成立，诱导坍缩就是恒等映射。

所以 lattice 运算对抽象 v0.1 adjoint-collapse 模式确实不是必要结构。

## 最小结构包

对当前 v0.1 且要求真实相等语义的运算，干净的最小包是：

1. partial orders `A,B`（或者 preorder 的 posetal reflection）；
2. 一个 order embedding \(l:A\hookrightarrow B\)；
3. 每个相关下水平集合 \(\{a:l(a)\le b\}\) 都有最大元。

由此自动得到右伴随、生成态精确恢复，以及向下收缩且幂等的投影。

未来进取数论的新运算可能需要更丰富结构，但必须逐个运算证明其必要性，而不能反过来把更强结构预先塞进基础层。
