# P025 补充 93 —— Ferrers Precision Boundary 与双重 Orbit 坐标

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-orbit-normal-stage91`  
依赖：P025 补充 92  
硬阻断：`NONE`

## 1. Staircase 还有一套完全对偶的坐标

Stage 92 用 threshold-centric crossing depths

\[
0\le j_1\le\cdots\le j_s\le\infty
\]

表示 multi-threshold activation matrix。

同一张 matrix 还有自然的 node-centric representation。

对每个 dyadic depth `j`，定义

\[
\boxed{r_j:=\#\{k:\rho_j\ge T_k\}.}
\]

即 orbit node `j` 已经达到多少个 declared threshold levels。

## 2. P025-T216 —— node ranks 单调

由于

\[
\rho_j\le\rho_{j+1},
\]

在 node `j` 已达到的所有 thresholds 到 node `j+1` 仍保持达到，所以

\[
\boxed{0\le r_0\le r_1\le\cdots\le r_h\le s.}
\]

node-centric precision state 本身也是 monotone staircase。

## 3. P025-T217 —— crossing / rank duality

threshold `T_k` 在 node `j` 已达到，当且仅当 crossing depth 不超过 `j`。所以

\[
\boxed{r_j=\#\{k:j_k\le j\}.}
\]

反过来，第 `k` 个 threshold 第一次 active，恰是在 node rank 首次达到至少 `k` 的位置：

\[
\boxed{j_k=\min\{j:r_j\ge k\},}
\]

若不存在则 `j_k=infinity`。

所以

\[
\boxed{(j_1,\ldots,j_s)\longleftrightarrow(r_0,\ldots,r_h)}
\]

是 exact bijection。

两种坐标没有谁 intrinsically 更有信息；它们只是同一个 finite semantic quotient 的双重视图。

## 4. P025-T218 —— column-prefix form

因为 thresholds 有序，

\[
T_1<\cdots<T_s,
\]

若 node `j` 达到 `T_k`，则所有更低 thresholds 也都已达到。

因此 activation matrix 的第 `j` 列为

\[
\boxed{
(\underbrace{1,\ldots,1}_{r_j},
\underbrace{0,\ldots,0}_{s-r_j})^\top.
}
\]

所以 Stage 92 的 row-suffix theorem 与 Stage 93 的 column-prefix theorem 是同一 monotone matrix 的 exact dual descriptions。

## 5. P025-D37 —— Ferrers precision region

把 activation matrix 看成 `s x (h+1)` grid，并在

\[
B_{k,j}=1
\]

时标记 cell `(k,j)`。

标记 cells 构成 monotone Ferrers-type region：

- 每一行沿 orbit direction 是 suffix；
- 每一列沿 threshold direction 是 prefix。

因此整个 finite precision state 就是 inactive 与 active cells 之间的边界。

## 6. P025-T219 —— lattice-path encoding

用一条 monotone lattice path 编码边界，其中包含

\[
h+1
\]

个 horizontal steps `H` 与

\[
s
\]

个 vertical steps `V`。

给定 node ranks，从高度 0 开始。在第 `j` 个 horizontal step 前，先补足 vertical steps 直到高度达到 `r_j`；最后一个 orbit node 后，再补足到高度 `s`。

得到长度

\[
\boxed{h+s+1}
\]

的 word，其中恰有 `h+1` 个 `H` 与 `s` 个 `V`。

反过来，每个 horizontal step 之前已经出现的 vertical steps 数量就恢复 `r_j`。

因此

\[
\boxed{
\text{crossing staircase}
\longleftrightarrow
\text{node-rank staircase}
\longleftrightarrow
\text{monotone lattice path}.
}
\]

Stage 92 的 state count

\[
\binom{h+s+1}{s}
\]

正好就是此类 lattice paths 的数量。

## 7. Exact working boundary

对 Stage 92 fixture，

\[
(j_k)=(0,1,2,\infty),
\]

其 dual node ranks 为

\[
\boxed{(r_j)=(1,2,3,3).}
\]

对应 boundary word 为

\[
\boxed{\texttt{VHVHVHHV}.}
\]

这一个 word 就编码了完整 matrix

\[
\begin{pmatrix}
1&1&1&1\\
0&1&1&1\\
0&0&1&1\\
0&0&0&0
\end{pmatrix}.
\]

## 8. P025-D38 —— activation area

定义 activation area

\[
\boxed{A:=\sum_{k=1}^s\sum_{j=0}^hB_{k,j}.}
\]

它就是 declared finite future grid 中已经 reached 的 threshold / node pairs 数量。

按列计数，

\[
\boxed{A=\sum_{j=0}^h r_j.}
\]

按行计数，若 threshold `k` 的 crossing depth 有限，它贡献

\[
h+1-j_k
\]

个 active cells；若 `j_k=infinity` 则贡献 0。因此

\[
\boxed{A=\sum_{k:j_k<\infty}(h+1-j_k).}
\]

所以得到 exact Ferrers area double-count identity：

\[
\boxed{
\sum_jr_j
=
\sum_{k:j_k<\infty}(h+1-j_k).
}
\]

## 9. Working area 校准

对

\[
(j_k)=(0,1,2,\infty),
\]

row count 给出

\[
A=4+3+2=9.
\]

node ranks 给出

\[
A=1+2+3+3=9.
\]

所以 `4 x 4` grid 的 active area 为 `9`，inactive complement area 为 `7`。

对 plateau staircase

\[
(1,2,2,\infty),
\]

ranks 是

\[
(0,1,3,3)
\]

且 active area 为 `7`。

## 10. 两种坐标服务不同 future operations

crossing-depth representation 是 threshold-centric，自然回答：

> threshold `T_k` 第一次在什么时候成为 true？

node-rank representation 是 orbit-centric，自然回答：

> node `j` 已经达到多少 declared precision levels？

它们 semantic 等价，但 operationally 不同。

当 future query 增加 threshold grid 或延长 orbit horizon 时，这种差异会变得关键。

## 11. Precision-boundary 解释

finite state 不再适合被理解成 table，而应理解为两个 ordered finite axes 的 product 中的一条 boundary：

\[
\boxed{\text{threshold precision}\times\text{orbit depth}.}
\]

边界一侧全部 inactive，另一侧全部 active。

所以 semantic information 被几何地局部化在 monotone boundary 上，而不是独立散布在整个 product grid。

这是一个 exact number-theoretic finite precision boundary geometry。

## 12. Prior-art / novelty 边界

Ferrers diagrams、conjugate partitions、monotone lattice paths 与 area double counting 都是 classical / general mathematics。

P025 不单独主张这些概念新颖。

项目侧结果只是由 dyadic projective-pressure theorem 诱导出的 exact dual boundary representation，以及相应 finite precision interpretation。历史新颖性仍为 `NOVELTY_UNVERIFIED`。

## 13. 可执行资产

新增：

- `src/enterprise_math/abc_dyadic_ferrers_boundary.py`；
- `tests/test_abc_dyadic_ferrers_boundary.py`。

executable layer 验证 crossing / rank duality、path encode / decode、exact boundary words、plateau geometry 与 area identity。

## 14. 下一前沿

不存在硬阻断。继续：

1. 比较新增一个 threshold 与新增一个 orbit node 时的 incremental update cost；
2. 证明两种 dual coordinate 分别在哪个 extension direction 上支持 local append-only update；
3. 定义 representation-switch rule，而不是指定一个 globally preferred coordinate；
4. 研究 threshold precision 与 orbit horizon 同时增长的 mixed extension；
5. 把得到的 coordinate-choice law 作为 theorem-backed precision compiler pattern 返回 P023/A2。
