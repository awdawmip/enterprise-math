# P008 —— 最小序论框架

状态：`VERIFIED-RESEARCH`  
开放问题：`P008`  
范围：仅数学结构

## 1. 问题

P008 要寻找一个尽可能弱、但已经成熟的代数或序理论结构，使它能够容纳 v0.1 的整数根与坍缩规律，同时不额外引入隐藏连续体。

第一阶段结论应当刻意保持小：

> v0.1 的根/坍缩核心不需要格、完备格、剩余格、域或实数完备化。它的本质成熟结构是偏序集之间的 Galois connection（伽罗瓦连接/序伴随）。在整数根情形，这个连接进一步是 Galois coinsertion；由此诱导的坍缩是一个 interior operator（向下的幂等投影）。

这些都是已有序理论，不是进取数论的新发明。进取数论自己的部分，是在有限状态、显式尺度的基础语义中选择并组合这些结构。当前已登记的相关前人来源包括 `SRC-MATHLIB-NTHROOT`、`SRC-MATHLIB-FLOORDIV` 与 `SRC-MATHLIB-CLOSURE`。

## 2. 右伴随记号

设 \(A,B\) 为偏序集，并有

\[
F:A\to B.
\]

当 \(F\) 存在右伴随时，本研究笔记记作

\[
F^\downarrow:B\to A.
\]

其定义条件是

\[
F(a)\le b\iff a\le F^\downarrow(b).
\]

\(F^\downarrow\) 只是本项目笔记中的记号；底层概念就是 Galois connection 中的标准右伴随。

对 \(\mathbb N\) 上的映射，一个常见具体实现为

\[
F^\downarrow(n)=\max\{k\in\mathbb N:F(k)\le n\}.
\]

## 3. 自然数状态上的存在性

### P008-T01 —— 一个充分存在条件

状态：`PROVED`

设 \(F:\mathbb N\to\mathbb N\) 单调，满足 \(F(0)=0\)，且无界。则对每个 \(n\in\mathbb N\)，

\[
F^\downarrow(n)=\max\{k:F(k)\le n\}
\]

都存在，并且是 \(F\) 的右伴随。

证明：该集合非空，因为 \(F(0)=0\le n\)。由无界性可取 \(m\) 使 \(F(m)>n\)。单调性推出所有 \(k\ge m\) 都有 \(F(k)>n\)，所以满足条件的集合有限，从而存在最大元。若最大元为 \(r\)，则由单调性

\[
F(k)\le n\iff k\le r.
\]

因此

\[
F(k)\le n\iff k\le F^\downarrow(n).
\]

证毕。

这个命题只是 \(\mathbb N\) 上便于构造右伴随的充分条件。抽象框架本身应直接假定伴随关系存在，而不必把这些充分条件强加到所有情况。

## 4. 伴随关系的普遍结论

以下假设

\[
F\dashv F^\downarrow.
\]

### P008-T02 —— 单位与余单位不等式

状态：`PROVED`

对所有 \(a\in A\)、\(b\in B\)，

\[
a\le F^\downarrow(F(a)),
\]

以及

\[
F(F^\downarrow(b))\le b.
\]

它们分别由自反不等式 \(F(a)\le F(a)\) 与 \(F^\downarrow(b)\le F^\downarrow(b)\) 代入伴随定义直接得到。

### P008-T03 —— 伴随映射的单调性

状态：`PROVED`

\(F\) 与 \(F^\downarrow\) 都是单调映射。

这是 Galois connection 的标准结论。

## 5. 一般坍缩算子

定义

\[
C_F=F\circ F^\downarrow:B\to B.
\]

### P008-T04 —— 一般坍缩是 interior operator

状态：`PROVED`

\(C_F\) 具有：

1. 单调性；
2. 向下收缩性：\(C_F(b)\le b\)；
3. 幂等性：\(C_F(C_F(b))=C_F(b)\)。

证明：单调性由 P008-T03 得到；向下收缩性就是 P008-T02 的余单位不等式。由向下收缩性，

\[
C_F(C_F(b))\le C_F(b).
\]

另一方面，对 \(F^\downarrow(b)\) 使用单位不等式：

\[
F^\downarrow(b)\le F^\downarrow(F(F^\downarrow(b))).
\]

再作用单调的 \(F\)，得到

\[
C_F(b)\le C_F(C_F(b)).
\]

由反对称性得到相等。证毕。

因此，现有完全幂坍缩 \(C_p\) 并不是孤立构造，而是序伴随诱导 interior operator 的一个特例。

### P008-T05 —— 不动状态恰好等于 \(F\) 的像

状态：`PROVED`

\[
\operatorname{Fix}(C_F)=\operatorname{im}(F).
\]

证明：对任意 \(a\)，P008-T02 给出

\[
F(F^\downarrow(F(a)))\le F(a).
\]

同时由

\[
a\le F^\downarrow(F(a))
\]

再作用单调的 \(F\)，得到反向不等式。因此

\[
C_F(F(a))=F(a).
\]

反之，若 \(C_F(b)=b\)，则

\[
b=F(F^\downarrow(b)),
\]

所以 \(b\in\operatorname{im}(F)\)。证毕。

因此，坍缩可以理解为向一组被指定的固定/可达状态子偏序进行投影。

## 6. Coinsertion 情形

如果还满足

\[
F^\downarrow\circ F=\operatorname{id}_A,
\]

那么按照标准术语，\(F\dashv F^\downarrow\) 是 Galois coinsertion。

### P008-T06 —— 严格递增的自然数映射给出 coinsertion

状态：`PROVED`

若 \(F:\mathbb N\to\mathbb N\) 严格递增，右伴随按“最大满足条件状态”定义，则

\[
F^\downarrow(F(k))=k.
\]

因此 \(F\dashv F^\downarrow\) 是 Galois coinsertion。

对幂映射

\[
P_p(k)=k^p,
\]

得到

\[
P_p\dashv R_p,
\qquad
R_p(P_p(k))=k,
\qquad
C_p=P_p\circ R_p.
\]

所以 v0.1 的整数根/坍缩对，精确地就是一个 coinsertion 以及它所诱导的、投影到完全 \(p\) 次幂子集上的 interior operator。

### P008-T07 —— 严格递增情形的盆地刻画

状态：`PROVED`

对严格递增的 \(F:\mathbb N\to\mathbb N\)，

\[
F^\downarrow(n)=k
\iff
F(k)\le n<F(k+1).
\]

从而

\[
C_F(n)=F(k)
\iff
F(k)\le n<F(k+1).
\]

现有完全幂盆地定理 T007 正是取 \(F(k)=k^p\) 的特例。

## 7. Floor division 与整数根属于同一结构

固定整数 \(a\ge1\)，定义

\[
M_a(k)=ak.
\]

它的右伴随就是普通向下整除

\[
D_a(n)=n\operatorname{//}a.
\]

于是

\[
M_a\dashv D_a,
\qquad
D_a(M_a(k))=k,
\]

并诱导坍缩

\[
C_{M_a}(n)=a(n\operatorname{//}a),
\]

即不超过 \(n\) 的最大 \(a\) 的倍数。

所以整数根与向下整除不只是“很像”。它们是同一个序伴随模式在不同左伴随映射下的实例。

## 8. 复合定理

### P008-T08 —— 右伴随按反序复合

状态：`PROVED`

设

\[
F:A\to B,\qquad G:B\to C,
\]

右伴随分别为 \(F^\downarrow\)、\(G^\downarrow\)。则

\[
G\circ F\dashv F^\downarrow\circ G^\downarrow.
\]

证明：

\[
G(F(a))\le c
\iff
F(a)\le G^\downarrow(c)
\iff
a\le F^\downarrow(G^\downarrow(c)).
\]

证毕。

这已经是 mathlib 的标准 Galois connection 机制；P008 不把它作为新结果主张。

### 推论 P008-C01 —— 整数根按指数乘法复合

状态：`PROVED`

对 \(p,q\ge1\)，

\[
R_{pq}=R_p\circ R_q=R_q\circ R_p.
\]

因为幂映射满足

\[
P_p\circ P_q=P_q\circ P_p=P_{pq},
\]

而右伴随唯一。

该结果已提升为 T013/T014，并分别由 `EnterpriseMath.Arithmetic.IntegerRoot.root_mul` 与 `root_mul_comm` 通过 Lean 检查。底层复合原则属于成熟序理论；`Nat.nthRoot` 的这个专门复合陈述是否值得 upstream，仍处于审计状态。

## 9. 尺度相容其实是一个伴随恒等式

记 \(M_b(k)=bk\)，\(D_b(n)=n\operatorname{//}b\)。对 \(b\ge1\)，有

\[
P_p\circ M_b=M_{b^p}\circ P_p.
\]

两边都存在右伴随。Mathlib 已有的伴随交换方块机制把这个等式传递为

\[
D_b\circ R_p=R_p\circ D_{b^p}.
\]

### P008-T09 —— 根与整除的交换恒等式

状态：`PROVED`

对所有 \(n\in\mathbb N\)、\(p\ge1\)、\(b\ge1\)，

\[
R_p(n)\operatorname{//}b
=
R_p\left(n\operatorname{//}b^p\right).
\]

更准确地，算子恒等式为

\[
D_bR_p=R_pD_{b^p}.
\]

该结果现已成为 T015，并由 `EnterpriseMath.Scale.root_div_scale` 通过 Lean 检查。

### 推论 P008-C02 —— 现有 T010 是结构性结论

状态：`PROVED`

现有定义

\[
R_{p,b,s}(n)=R_p(nb^{ps}).
\]

对 \(nb^{p(s+1)}\) 应用 P008-T09：

\[
D_bR_p(nb^{p(s+1)})
=
R_p(nb^{ps}).
\]

这正是现有尺度相容定理 T010。

因此，T010 不是一个只针对幂运算的孤立技巧，而是交换方块

\[
P_pM_b=M_{b^p}P_p
\]

在右伴随一侧留下的结构恒等式。

该结果已由 `EnterpriseMath.Scale.scaledRoot_succ_div` 通过 Lean 检查，并解决 P014。

## 10. 用固定状态反向表示

### P008-T10 —— 每个 interior operator 都可表示为 coinsertion 投影

状态：`PROVED`

设 \(I:B\to B\) 是偏序集上的单调、向下收缩、幂等映射。令

\[
K=\operatorname{Fix}(I),
\]

取继承序；令 \(J:K\hookrightarrow B\) 为包含映射；令 \(\widehat I:B\to K\) 为把 \(I\) 的陪域限制到固定点集后的映射。则

\[
J\dashv\widehat I,
\qquad
\widehat I\circ J=\operatorname{id}_K,
\qquad
J\circ\widehat I=I.
\]

因此在这一层级上，以下两种描述是等价的：

- 指向一个子偏序的 Galois coinsertion / coreflection；
- 单调、向下收缩、幂等的 interior operator。

这个等价仍然是成熟序理论。进取数论直接复用，而不是再造一套平行术语。

## 11. 为什么当前不应继续加重结构

目前以下更强结构都不是 v0.1 上述规律所必需的：

- 格；
- 完备格；
- 剩余格；
- 环或域；
- 拓扑；
- 实数完备化。

未来可能需要其中一些，但现在引入会让 P008 的答案比现有数学真正需要的更强。

为了直接得到“幂等”等字面相等式，偏序是一个干净的最小工作环境。在预序中，同样的论证首先得到双向不等式，只能在预序诱导的等价关系意义下得到相等。

## 12. 边界反例

### P008-CE01 —— 单调性本身不足以构造全局最大状态右伴随

令所有 \(k\) 都满足 \(F(k)=0\)。该映射单调，但对任意 \(n\ge0\)，

\[
\{k:F(k)\le n\}=\mathbb N
\]

不存在最大元。因此，仅有单调性不能保证“取最大值”的具体公式在 \(\mathbb N\) 上定义右伴随。

该反例已提升为 C011。

### P008-CE02 —— 无界但不单调不能推出伴随律

定义

\[
F(0)=0,\quad F(1)=2,\quad F(2)=1,
\]

并对 \(k\ge3\) 令 \(F(k)=k\)。该映射无界。取 \(n=1\)，满足 \(F(k)\le1\) 的最大 \(k\) 是 \(2\)。但 \(1\le2\)，而 \(F(1)=2\not\le1\)。所以

\[
F(k)\le n\iff k\le F^\downarrow(n)
\]

失败。单调性对“最大状态”构造具有结构性必要性。

该反例已提升为 C012。

## 13. P008 第一阶段答案

当前经过验证的第一阶段答案是：

> **偏序集之间的 Galois connection 足以容纳 v0.1 的根/坍缩核心；整数根映射构成 Galois coinsertion，其坍缩是相应的 interior/coreflection 投影。**

对自然数实现而言，满足 \(F(0)=0\) 的单调无界映射给出一大类可用“最大可容许状态”构造右伴随的例子。

序论层的母结果经审计后均属于 mathlib 已有数学。因此 P008 的成果是减少所需基础结构，而不是创造一套平行代数词汇。P008 继续标记 `PARTIAL-RESOLUTION`，仅因为“对未来所有扩展而言是否绝对最弱”这一字面最小性尚未证明。

## 14. 形式化验证状态

当前 mathlib-native Lean 层已经由内核检查：

- T001 根刻画；
- T002 完全幂精确恢复；
- T004 坍缩向下收缩；
- T005 坍缩幂等；
- T006 完全幂不动点；
- T010 尺度相容；
- T012 历史合流单调；
- T013 整数根指数复合；
- T014 迭代根交换；
- T015 根/整数除法交换；
- 通用伴随坍缩的项目薄包装。

构建固定到明确版本，并把 warning 视为失败。P013 与 P014 因此均已解决。

## 15. 下一步攻击

1. `root_mul` / `root_mul_comm` 只作为暂定 mathlib upstream 候选，直到面向 mathlib 的 API 审查进一步确认不存在等价定理且确有复用价值。
2. 使用整除关系和 P008 的投影结构攻击 P003（坍缩交换性），但不在概念上把 P003 并入 P008。
3. 使用“交换方块 → 右伴随”的方法继续建立 P005 多底数尺度代数。
4. P008 以后只在新结构确实提出更弱/更强基础需求时继续推进，不预先引入更重代数。
