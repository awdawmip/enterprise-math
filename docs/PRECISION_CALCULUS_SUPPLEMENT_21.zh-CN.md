# P018 —— 有限精度证明演算：补充 21

状态：`ACTIVE RESEARCH NOTE`  
范围：带标签 operation-context separation depth、最短 distinguishing-context 证书、高阶 split spectrum，以及 precision–time bifiltration 的成立边界  
依赖：P011、P018-T169–T182  
前人工作边界：nested partition hierarchy 与 ultrametric 表示属于成熟结构；term/context distinguishability 与 syntactic congruence 属于成熟 universal algebra / machine algebra。见 `docs/PRIOR_ART_P018_COALESCENCE.zh-CN.md` 与 `docs/PRIOR_ART_P018_PREDICTIVE_CLOSURE.zh-CN.md`。[SRC-MURTAGH-CONTRERAS-2010-HIERARCHY-ULTRAMETRIC] [SRC-CLARK-DAVEY-FREESE-JACKSON-2004-SYNTACTIC]

---

## 1. Fixed point 之外还保留了什么？

Supplement 19 已确定有限 operation signature `Sigma` 与 static observation equivalence `E` 的规范 exact state relation：

\[
R_*=\operatorname{Syn}_\Sigma(E).
\]

但有限 refinement 算法本身还留下了一条严格的证明轨迹：

\[
\boxed{
R_0=E
\supseteq
R_1
\supseteq
\cdots
\supseteq
R_h=R_*.
}
\]

某一对 states 可能一开始就可区分，也可能只有经过一个或多个 nested operation contexts 才被迫分开，也可能永远无法被该 operation language 区分。

因此真正可问的是：

> **为了证明当前 precision 必须区分两个 labelled states，最短需要多深的允许 operation context？**

---

## 2. P018-T183 —— 扩展 labelled context-separation depth

状态：`PROVED / EXECUTABLE`

对 labelled states `x,y` 定义

\[
\boxed{
\sigma_\Sigma(x,y)
=
\min\{n\in\mathbb N:(x,y)\notin R_n\},
}
\]

若该集合为空，即 `(x,y) in R_*`，则规定

\[
\boxed{
\sigma_\Sigma(x,y)=\infty.
}
\]

所以：

- `sigma=0`：raw observation 已区分该 pair；
- `sigma=n>0`：所有更浅 contexts 都区分不了，但深度 `n` 可以；
- `sigma=infinity`：声明 operation language 中没有有限 context 能区分该 pair。

这里的 depth 是**精度 refinement 的 context depth**，不是物理时间。

---

## 3. P018-T184 —— Separation matrix 与完整 refinement filtration 无损等价

状态：`PROVED / EXECUTABLE`

由 relations 的嵌套性：

\[
\boxed{
(x,y)\in R_n
\iff
\sigma_\Sigma(x,y)>n
\text{ 或 }\sigma_\Sigma(x,y)=\infty.
}
\]

因此 labelled extended matrix

\[
\boxed{
(\sigma_\Sigma(x,y))_{x,y\in X}
}
\]

可以精确重建每个 `R_n`；反之，整条 filtration 也唯一决定每对 labelled states 第一次离开 relation 的深度。

所以二者是无损等价表示。

---

## 4. P018-T185 —— Reverse strong triangle 与 quotient ultrametric

状态：`PROVED / EXECUTABLE / PRIOR-ART STRUCTURAL PATTERN`

任意三个 states 满足

\[
\boxed{
\sigma_\Sigma(x,z)
\ge
\min(\sigma_\Sigma(x,y),\sigma_\Sigma(y,z)),
}
\]

其中 `infinity` 大于全部有限 depth。

证明非常直接：在右侧较小 separation depth 之前，

\[
x\,R_n\,y,
\qquad y\,R_n\,z,
\]

同时成立；每个 `R_n` 都是 equivalence relation，由 transitivity 得到 `x R_n z`，所以 `x,z` 不可能更早分开。

令 `h` 为 first stable depth，并定义

\[
d_{\mathrm{ctx}}(x,y)=
\begin{cases}
0,&\sigma(x,y)=\infty,\\
h+1-\sigma(x,y),&\sigma(x,y)<\infty.
\end{cases}
\]

则

\[
\boxed{
d_{\mathrm{ctx}}(x,z)
\le
\max(d_{\mathrm{ctx}}(x,y),d_{\mathrm{ctx}}(y,z)).}
\]

在 `X` 上这是 integer-valued pseudoultrametric，其零类正是 contextual-closure blocks；在 quotient `X/R_*` 上成为 genuine ultrametric。

hierarchy→ultrametric 属于成熟数学，不主张 novelty。

---

## 5. P018-T186 —— First separation depth 就是最短 distinguishing-context 长度

状态：`PROVED / EXECUTABLE`

一个 elementary context 是一个 basic operation 的 one-hole translation。长度 `m` 的 context path 写成

\[
c=\tau_m\circ\cdots\circ\tau_1.
\]

由 refinement recurrence 归纳得到：

\[
\boxed{
(x,y)\in R_n
\iff
O(c(x))=O(c(y))
\text{ 对所有长度不超过 }n\text{ 的 elementary-context path }c.
}
\]

因此，只要 `sigma(x,y)` 有限，

\[
\boxed{
\sigma_\Sigma(x,y)
=
\min\{\operatorname{len}(c):O(c(x))\ne O(c(y))\}.
}
\]

若 `sigma=infinity`，则没有任何有限 context path 能区分该 pair。

所以每一个“为什么这两个 states 必须保留不同 detail”的结论，都有一条长度至多 `h<=N-c0` 的有限最短证明证书。参考实现通过 labelled-state-pair BFS 返回一条最短 witness。

---

## 6. P018-T187 —— 任意有限 subset 的 separation depth 完全由 pairwise depth 决定

状态：`PROVED / EXECUTABLE`

对至少含两个 states 的有限 subset `A`，定义它第一次不再落在同一 `R_n` block 的深度。则

\[
\boxed{
\sigma_\Sigma(A)
=
\min_{\{x,y\}\subseteq A}\sigma_\Sigma(x,y).
}
\]

理由是：`A` 落在一个 equivalence class 中，当且仅当 `A` 的每一对 states 都处于同一个 class。

因此不存在独立的 higher-order context-depth 原语；labelled pair matrix 已经包含全部有限 subset depth 信息。

这与此前“higher coalescence time = pairwise coalescence time 的最大值”在形式上相反，但本文**不宣称 categorical duality**。

---

## 7. P018-T188 —— 每个 context depth 的 collision-spectrum 精确损失

状态：`PROVED / EXECUTABLE`

继续使用 P011 collision polynomial：

\[
K_P(t)=\sum_{B\in P}((1+t)^{|B|}-1).
\]

若一个大小为

\[
m=\sum_i m_i
\]

的 parent block 被细化为 child blocks `m_i`，则 exact collision loss 为

\[
\boxed{
\Delta^-_P(t)
=(1+t)^m-1-
\sum_i((1+t)^{m_i}-1).
}
\]

其 degree-`k` coefficient 是

\[
\boxed{
\binom{m}{k}-\sum_i\binom{m_i}{k}\ge0.
}
\]

它精确计数：refinement 前属于同一个 parent block、refinement 后不再属于同一个 child block 的 labelled `k`-subsets。

因此对 `R_n -> R_(n+1)`：

\[
\boxed{
[t^k](K_{R_n}-K_{R_{n+1}})
=
\#\{A:|A|=k,\ \sigma_\Sigma(A)=n+1\}.
}
\]

P011 polynomial 因而在 operation-context refinement 轴上获得 exact **split-spectrum** 解释。

---

## 8. P018-T189 —— Split increments 有限精确 telescoping

状态：`PROVED / EXECUTABLE`

有限 chain 给出

\[
\boxed{
K_{R_0}(t)-K_{R_*}(t)
=
\sum_{n=0}^{h-1}(K_{R_n}(t)-K_{R_{n+1}}(t)).
}
\]

所有系数均为非负整数。

因此 raw precision 修复成 exact operation state 时被消除的全部 ambiguity，可以按**首次 distinguishing context depth × subset order** 精确分层。

---

## 9. P018-T190 —— Pair separation matrix 重建全部 higher split spectrum

状态：`PROVED STRUCTURAL CONSEQUENCE / EXECUTABLE`

T184 先从 labelled pair separation matrix 重建每个 `R_n`；T188 再从 partitions 得出各阶 split increments。也可以直接利用 T187，把 `k`-subset 的首次 separation depth 写成其最小 pairwise separation depth。

于是

\[
\boxed{
\text{labelled pair separation matrix}
\Longrightarrow
\text{complete context-resolved P011 split spectrum}.
}
\]

higher polynomial 是 Pair 层的下游计数投影，不能替代 labelled history。

---

## 10. P018-C20 —— Unlabelled split spectrum 不能恢复 labelled distinctions

状态：`COUNTEREXAMPLE / INFORMATION-LOSS BOUNDARY`

取

\[
X=\{0,1,2,3,4\}
\]

与 raw observation blocks

\[
\{0,1,2,3\},\qquad\{4\}.
\]

两个 unary systems：

\[
F_A=(0,0,4,4,4),
\qquad
F_B=(0,4,0,4,4).
\]

它们都有相同 block-size trajectory：

\[
(4,1)\to(2,2,1).
\]

所以完整 collision-polynomial trajectory 与 split spectrum 完全相同。

但 labelled pair history 不同：

- `F_A` 中 `0` 与 `1` 保持同组、与 `2` 分开；
- `F_B` 中 `0` 与 `2` 保持同组、与 `1` 分开。

所以

\[
\boxed{
\text{same context-resolved P011 spectrum}
\not\Rightarrow
\text{same labelled separation geometry}.
}
\]

aggregate observable 仍然不能反向恢复 identity-level structure。

---

## 11. P018-T191 —— 扩大 operation language 只可能更早区分

状态：`PROVED / EXECUTABLE`

若

\[
\Sigma\subseteq\Sigma',
\]

由 refinement recurrence 归纳可得

\[
R_n^{\Sigma'}\subseteq R_n^{\Sigma}
\quad\forall n.
\]

所以对任意 labelled pair，若右侧有限：

\[
\boxed{
\sigma_{\Sigma'}(x,y)
\le
\sigma_\Sigma(x,y).
}
\]

原本在较小语言中永不分开的 pair，也可能在较大语言中变为有限深度可区分。

所以增加 exact operational obligations 只能让缺失 detail 在同样或更浅的 context depth 暴露。

---

## 12. P018-T192 —— Contextual fixed point 是规范 time-monotone row

状态：`PROVED / EXECUTABLE`

令 unary operation

\[
F:X\to X
\]

属于生成 `R_*` 的 declared operation language。

因为 `R_*` 是 congruence：

\[
x\,R_*\,y\implies F(x)\,R_*\,F(y).
\]

定义 time `t` 的 labelled-history kernel：

\[
K_{*,t}=\{(x,y):F^{[t]}x\,R_*\,F^{[t]}y\}.
\]

则

\[
\boxed{K_{*,t}\subseteq K_{*,t+1}.}
\]

因此最小 contextual repair 完成之后，deterministic time 恢复 P010/P011 的 irreversible merge 方向。time monotonicity 直接来自 operation congruence，不需要新增时间公理。

---

## 13. P018-C21 —— Closure 之前的 naive precision–time grid 不一定是 bifiltration

状态：`COUNTEREXAMPLE / FOUNDATIONAL BOUNDARY`

取

\[
X=\{0,1,2\},
\qquad
E=\{\{0,1\},\{2\}\},
\]

以及 unary operation

\[
F=(0,2,2).
\]

raw precision 下 `0~1`；一步之后

\[
F(0)=0,
\qquad F(1)=2,
\]

所以原来相等的 pair 裂开；与此同时原本不同的 `1,2` 又相遇。

raw history partition 从

\[
\{\{0,1\},\{2\}\}
\]

变成

\[
\{\{0\},\{1,2\}\},
\]

二者互不 refine。

因此 raw time axis 并不 monotone。

对语言 `{F}` 做 contextual closure 后，`E` 被修复为 equality；equality 与 `F` compatible，于是 stable row 上 time kernel 重新 monotone。

所以：

\[
\boxed{
\text{仅有 nested precision refinement 并不能保证 precision–time bifiltration。}
}
\]

每一个被当作 time row 的 precision relation 必须满足相应 operation-congruence 条件，否则 grid 会发生 tearing。

---

## 14. P018-T193 —— Closure 后的 exact saddle monotonicity

状态：`PROVED / EXECUTABLE`

选定 unary time operation `F`，定义

\[
B_{n,t}=\{(x,y):F^{[t]}x\,R_n\,F^{[t]}y\}.
\]

固定任意 `t`，因为 `R_(n+1) subseteq R_n`：

\[
\boxed{B_{n+1,t}\subseteq B_{n,t}.}
\]

所以 P011 collision polynomial 沿 context/refinement depth coefficientwise **nonincreasing**。

在 stable row `n=h`，T192 给出

\[
\boxed{B_{h,t}\subseteq B_{h,t+1},}
\]

所以同一 polynomial 沿 deterministic time coefficientwise **nondecreasing**。

得到 finite saddle-shaped monotonicity：

\[
\boxed{
\text{context depth 消除 apparent collisions；}
\qquad
\text{closed deterministic time 产生 genuine history collisions。}
}
\]

二者作用在同一个 Pair/partition substrate 上，但不能把它们视作同一种关系。

---

## 15. P018-T194 —— Q118 的边界分类

状态：`RESOLVED AS A FINITE STRUCTURAL BOUNDARY`

precision/context 轴现在有 canonical labelled invariant：

\[
\boxed{
\sigma_\Sigma(x,y)
=
\text{shortest distinguishing-context depth}.
}
\]

它无损重建 contextual refinement filtration 与全部 higher split spectra。

deterministic closed-time 轴则继续使用此前的 merger-time invariant

\[
\tau_F(x,y).
\]

C21 表明：naive full two-dimensional precision–time grid **并不自动**成为 bifiltration，因为 pre-closure observation relations 可能在时间推进时 tearing。

正确的规范结论是：

1. contextual refinement 单调收敛到 greatest operation congruence；
2. stable contextual row 是所有 declared unary operations 都获得 monotone time kernels 的 coarsest exact row；
3. 若一整族 precision relations 本来就已经 operation-congruent，则 T155 的 stronger bifiltration 可以逐层成立；
4. `sigma` 与 `tau` 是 refinement 与 irreversible merge 的两个不同 labelled Pair coordinates。

因此 Q118 被解决为一个**有限 closure/bifiltration boundary classification**，而不是“普遍 time–precision duality”的声明。

---

## 16. 仍开放的问题

Supplement 19 的 Q119 仍是主要 transport 问题：

> 已知最小 exact contextual state 后，什么时候其 operation interactions 可以通过更小的 structured、composable transport data 实现？其 minimum transport complexity 是多少？

另一个派生方向是：

> T186 的 shortest distinguishing-context certificates 能否被编译成 P017/P018 可重用的 proof certificates，而无需 materialize 整个 contextual quotient？

这属于 proof-engineering 问题，不是新的 foundational primitive。

---

## 17. Executable pressure tests

新增：

- `src/enterprise_math/context_separation.py`
- `tests/test_context_separation.py`

测试覆盖：

1. 从 labelled separation matrix 重建每一级 contextual filtration；
2. shortest distinguishing-context length = first separation depth；
3. two-state binary-operation 的穷举 certificate 检查；
4. reverse strong triangle / ultrametric inequality；
5. higher subset depth = minimum pairwise depth；
6. exact degree-`k` split-spectrum counts；
7. split increments 的有限 telescoping；
8. C20：相同 unlabelled spectra、不同 labelled separation histories；
9. operation-language enlargement 下 separation depth 单调；
10. C21：raw time monotonicity 失败、stable contextual row 恢复；
11. context depth 与 closed deterministic time 的相反 coefficientwise monotonicity。

独立额外穷举还覆盖了三 labelled states 上全部 19,683 个 binary operations 与全部五种 equivalence partitions，共 98,415 个 algebra/observation cases；对 295,245 个 unordered pair checks 未发现 separation-depth strong triangle、shortest-context equality 或 split-spectrum interpretation 的反例。
