# P023 —— 标签删除与 image separation，补充 08

状态：`PROVED`  
归属：A2 / P023 future-compatible quotient  
来源压力：P017 L054/L052 与 P024 future-safe precision  
纪律：集合像、单射与 decoder 存在性属于初等成熟数学；这里提炼的是可重复的 quotient/repair 判据。

## 1. 问题：辅助标签什么时候真的可以删掉

数论证明中经常把状态写成

\[
(i,x),
\]

其中 `i` 是 shell / factor / residue-class label，而 `x` 是真正继续参与后续运算的坐标。

一个常见但危险的习惯是：

- 一旦引入了 `i`，以后一直携带；或者
- 看到当前 `x` 不冲突，就永久删除 `i`。

P023 的未来安全纪律要求更精确地问：

> 当前删除标签以后，经过声明的后续映射，标签是否仍能从保留坐标中唯一恢复？

答案完全由不同 shell 的**实际像是否相交**决定。

## 2. 设置

令 `I` 为标签集合，`X` 为细状态空间，并给定一族 shell

\[
W_i\subseteq X
\qquad(i\in I).
\]

带标签状态空间为不交并

\[
S=\{(i,x):x\in W_i\}.
\]

当前标签删除映射为

\[
E:S\to X,
\qquad
E(i,x)=x.
\]

再令

\[
G:X\to Y
\]

为某个后续确定性映射。

## 3. P023-S8-T01 —— 当前标签删除判据

状态：`PROVED`。

以下等价：

1. `E(i,x)=x` 在 `S` 上为单射；
2. 对任意 `i!=j`，
   \[
   \boxed{W_i\cap W_j=\varnothing.}
   \]

### 证明

若两个不同 shells 有共同 `x`，则 `(i,x)!=(j,x)` 却被 `E` 送到同一状态，所以不单射。

反之若 shells 两两不交，`E(i,x)=E(j,y)` 给出 `x=y`；这个状态只能属于一个 shell，故 `i=j`，于是 `(i,x)=(j,y)`。∎

### 含义

如果 exact coordinate 本身已经编码 shell identity，那么继续携带 shell label 只是重复状态维度。

## 4. P023-S8-T02 —— 经过后续映射后的标签可恢复判据

状态：`PROVED`。

以下等价：

1. 存在一个只在 reachable image 上需要定义的 decoder
   \[
   D:G\!\left(\bigcup_iW_i\right)\to I
   \]
   使得
   \[
   D(G(x))=i
   \qquad(x\in W_i);
   \]
2. 不同 shell 的实际 images 两两不交：
   \[
   \boxed{
   G(W_i)\cap G(W_j)=\varnothing
   \qquad(i\ne j).
   }
   \]

### 证明

若存在共同 image `y=G(x_i)=G(x_j)`，其中 `x_i in W_i`、`x_j in W_j` 且 `i!=j`，则 decoder 必须同时满足 `D(y)=i` 与 `D(y)=j`，矛盾。

反之若 images 两两不交，则每个 reachable `y` 只来自唯一 shell。把 `D(y)` 定义为该唯一标签即可。∎

因此“标签删除后未来仍安全”不是抽象直觉，而是一个**image separation test**。

## 5. P023-S8-T03 —— 标签恢复与完整状态恢复必须分开

状态：`PROVED`。

映射

\[
H:S\to Y,
\qquad
H(i,x)=G(x)
\]

在 `S` 上单射，当且仅当同时满足：

1. 不同 shell images 两两不交；
2. 每个限制
   \[
   G|_{W_i}:W_i\to Y
   \]
   都是单射。

### 证明

这是单射在“跨 shell”与“shell 内部”两个方向的精确分解。

- 跨 shell image 相交会合并不同标签状态；
- 同一 shell 内 `G` 不单射会合并同标签的不同细状态；
- 两类碰撞都不存在时，`H` 显然单射。∎

所以必须区分：

\[
\boxed{
\text{shell label 可恢复}
\not\Rightarrow
\text{完整原状态可恢复}.
}
\]

这在 coarse root、bucket、basin coordinate 中尤其重要。

## 6. P023-S8-T04 —— 声明 context 下的安全标签删除

状态：`PROVED`，是 T02 的逐 context 应用。

给定一族声明的后续 context maps

\[
\mathcal G=\{G_c:X\to Y_c\}_{c\in C},
\]

如果任务要求在每个 context 输出后仍能恢复 shell label，则当前标签可以安全删除，当且仅当对每个 `c` 与每对 `i!=j`，

\[
\boxed{
G_c(W_i)\cap G_c(W_j)=\varnothing.
}
\]

一旦某个 context 出现 image overlap，该 overlap 就是需要 repair 的**精确见证**。

这与 P023 operation-word future quotient 完全一致：这里把“未来可区分”专门压成 shell-label query 的 image language。

## 7. P017 L054 的 A2 重解释

在 P017 的 open square basin 中，令 label 为 least prime `p`，保留坐标为 stripped cofactor

\[
q=n/p.
\]

对应 shells 正是

\[
W_p(k)=
\left[
\left\lfloor\frac{k^2}{p}\right\rfloor+1,
\left\lfloor\frac{k(k+2)}{p}\right\rfloor
\right].
\]

L054 证明 `k>=4` 后所有这些 raw windows 两两不交。

由 T01：

\[
\boxed{
\text{从 }k\ge4\text{ 起，least-prime label }p
\text{ 已经是 exact cofactor }q\text{ 的函数。}
}
\]

而且同一 `p` shell 内 `n=pq`，所以此时 `q` 不仅恢复 label，也恢复完整 composite state。

因此 L054 可以解释为：**factor label 在 exact stripped coordinate 中已经成为冗余维度。**

## 8. Root projection 说明“当前可删”不等于“未来永远可删”

后续若只保留

\[
G(q)=R_2(q),
\]

则 T02 要求检查的不是原窗口是否不交，而是

\[
R_2(W_p(k))
\]

这些**实际 images**是否不交。

这一点立即解释 P017 两种看似相近、实际不同的结论：

- L054：exact quotient shells 从 `k>=4` 起不交；
- L052：把每个 actual image 先扩大为候选 pair `{j_p,j_p+1}` 后，要到 `k>=15` 才能保证这些粗候选对不交；
- 新的 L055：保留真实窗口再取 actual root image，只需要 `k>=9` 即可保证 lower-band shell label 可恢复。

所以 `15 -> 9` 不是“同一个不等式算得更紧”这么简单，而是一个 precision lesson：

> **扩大候选集会制造真实状态从未实现的假 collision。**

## 9. Repair 的正确含义

如果 `G(W_i)` 与 `G(W_j)` 相交，不能马上得出“必须保留整个原标签”。真正需要保留的信息只是足以拆开这些实际 overlaps 的最小 repair partition。

一般最小 repair 仍由 P023 的 future-compatible quotient 负责。本补充只提供一个快速 zero-repair 判据：

\[
\boxed{
\text{所有相关 shell images 两两不交}
\Longrightarrow
\text{shell label repair cost}=0.
}
\]

## 10. 研究工具化

面对 factor shell、residue shell、geometric sector、collision mode 等显式标签，统一流程应为：

1. 写出 label 对应的真实细状态集合 `W_i`；
2. 先检查 `W_i` 是否已经在保留坐标上两两不交；
3. 对每个声明 future map `G_c` 计算 actual image `G_c(W_i)`；
4. image 仍不交，则删除标签；
5. image 开始相交时，只对相交区域编译 minimal repair；
6. 不使用人为放大的 candidate superset 替代 actual image，除非明确接受它带来的假 collision 成本。

## 11. 可执行审计

- `src/enterprise_math/label_erasure.py`
- `tests/test_p023_label_erasure.py`
- P017 特化：`src/enterprise_math/p017_actual_root_separation.py`

测试分别固定：当前 shell disjointness、变换后 label decoder、label recovery 与 full-state injectivity 的严格区别，以及 P017 actual root image 的 sharp threshold。

## 12. 前人工作与新颖性纪律

“disjoint images iff a label decoder exists”本身是初等集合论，不是新数学。

Enterprise Math 的研究价值在于把它提升为 future-safe precision 的一个**零 repair 编译器**，并系统性要求数论/工程路线在携带辅助标签之前先做 actual-image separation audit。
