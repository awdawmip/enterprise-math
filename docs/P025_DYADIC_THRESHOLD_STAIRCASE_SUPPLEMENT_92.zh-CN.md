# P025 补充 92 —— Multi-Threshold Dyadic Staircase Normal Form

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-orbit-normal-stage91`  
依赖：P025 补充 91  
硬阻断：`NONE`

## 1. 一个 threshold 对应一个 crossing depth

Stage 91 已证明，对固定 dyadic difference-pressure orbit

\[
\rho_0\le\rho_1\le\cdots\le\rho_h
\]

与单个 threshold `T`，整条 Boolean activation row

\[
\big(\mathbf1_{\{\rho_j\ge T\}}\big)_{0\le j\le h}
\]

可由一个 first-activation depth 精确表示。

有限 precision system 通常不会只有一个 threshold。Stage 92 因而固定严格递增 threshold grid

\[
\boxed{0<T_1<T_2<\cdots<T_s}
\]

并研究整张 activation matrix 的 exact semantic state。

## 2. P025-D36 —— multi-threshold activation matrix

定义

\[
\boxed{
B_{k,j}:=\mathbf1_{\{\rho_j\ge T_k\}},
\qquad
1\le k\le s,
\quad
0\le j\le h.
}
\]

若完全不使用两种 monotonicity，它只是任意 `s x (h+1)` Boolean matrix，因此形式上有

\[
\boxed{2^{s(h+1)}}
\]

种 states。

对每个 threshold 定义 first activation depth

\[
\boxed{j_k:=\min\{j:\rho_j\ge T_k\},}
\]

若该 threshold 在 horizon 内未达到，则记 `j_k=infinity`。

## 3. P025-T211 —— 每一行都是 suffix

Stage 91 可分别作用于每个 threshold，所以

\[
\boxed{B_{k,j}=1\iff j\ge j_k.}
\]

因此每一行都是 upward-closed suffix。

整行可由 `j_k` 完整恢复。

## 4. P025-T212 —— crossing depths 构成 monotone staircase

因为 thresholds 递增，

\[
T_k<T_{k+1}.
\]

若更高 threshold 已在 depth `j` 达到，则更低 threshold 在该 depth 必然已经达到。因此

\[
\boxed{j_k\le j_{k+1},}
\]

其中有限 depths 均排在 `infinity` 之前。

所以

\[
\boxed{
0\le j_1\le j_2\le\cdots\le j_s\le\infty.
}
\]

整张 activation matrix 因而由一个弱递增 crossing vector 精确表示。

不同 thresholds 可以共享 crossing depth，所以 plateau 是真实状态，必须允许。

## 5. P025-T213 —— exact staircase reconstruction

给定弱递增向量

\[
(j_1,\ldots,j_s)
\in
\{0,1,\ldots,h,\infty\}^s,
\]

按

\[
\boxed{B_{k,j}=\mathbf1_{\{j\ge j_k\}}}
\]

重建 matrix。

反过来，每张 dyadic multi-threshold activation matrix 都唯一给出该 crossing vector。

所以

\[
\boxed{
\text{activation matrix}
\longleftrightarrow
\text{weakly increasing crossing-depth staircase}
}
\]

是 bijection。

## 6. P025-T214 —— exact compatible state count

crossing-depth state 一共有

\[
N:=h+2
\]

个有序值

\[
0,1,\ldots,h,\infty.
\]

从 `N` 个 ordered values 中取长度 `s` 的 weakly increasing sequence，其数量是 combinations-with-repetition：

\[
\binom{N+s-1}{s}.
\]

所以 compatible activation matrices 的数量恰为

\[
\boxed{
\binom{h+s+1}{s}.
}
\]

与 unconstrained Boolean space 相比，

\[
\boxed{
2^{s(h+1)}
\quad\longrightarrow\quad
\binom{h+s+1}{s}.
}
\]

固定 threshold count `s` 时，compatible count 对 horizon 是 polynomial 而不是 exponential；固定 horizon 时对 threshold-grid size 亦然。

## 7. Exact four-threshold fixture

采用 Stage 91 orbit

\[
(q,p,m)=(3,41,2)
\]

并观察 depths `0,1,2,3`，其 pressures 为

\[
\frac1{22},
\frac{13}{22},
\frac{221}{22},
\frac{221}{22}.
\]

选择 thresholds

\[
\boxed{
T_1=\frac1{22},
\quad
T_2=\frac12,
\quad
T_3=1,
\quad
T_4=11.
}
\]

crossing staircase 为

\[
\boxed{(0,1,2,\infty).}
\]

完整 activation matrix 为

\[
\boxed{
\begin{pmatrix}
1&1&1&1\\
0&1&1&1\\
0&0&1&1\\
0&0&0&0
\end{pmatrix}.}
\]

只要 staircase 已知，这张 matrix 里的任何 entry 都无需独立存储。

## 8. Plateau fixture

改选

\[
\frac12<1<10<11.
\]

同一 orbit 的 crossing depths 为

\[
\boxed{(1,2,2,\infty).}
\]

thresholds `1` 与 `10` 在同一 orbit node crossing，因为

\[
\frac{221}{22}>10.
\]

所以 staircase 是 weakly increasing，而不是 strictly increasing。

## 9. P025-T215 —— working grid 的 exact state-space reduction

取

\[
h=3,
\qquad s=4,
\]

unconstrained matrix 有 `16` 个 Boolean entries，因此形式 states 数为

\[
2^{16}=65536.
\]

monotone dyadic threshold theorem 只允许

\[
\boxed{\binom84=70}
\]

个 states。

因此 exact reduction factor 超过

\[
\frac{65536}{70}>936.
\]

该 ratio 只是 calibration；真正 theorem 是 exact binomial state count。

## 10. Threshold-grid precision 是 future-relative 的

staircase 取决于 declared threshold grid。更改 grid 会改变：

- rows 数量；
- crossing vector；
- 哪些不同 thresholds collapse 到同一 plateau；
- semantic state count。

因此不能把 continuum of threshold queries 当作已经天然存在的信息。

有限 declared threshold family 会诱导一个有限、精确的 precision state。

这与项目“precision 由 future language 实际请求的 observations 定义”的底层原则一致。

## 11. Semantic 与 exact pressure state

staircase 对 future query

> 对每个 declared threshold 与每个 dyadic depth，pressure 是否越过 threshold？

是 complete 的。

但它无法恢复 exact numerical pressures。

所以

\[
\boxed{
(\rho_0,u_0,\ldots,u_{h-1})
\longrightarrow
(j_1,\ldots,j_s)
\longrightarrow
\text{selected threshold bits}
}
\]

再次构成 future-relative precision ladder。

## 12. 架构含义

Stage 92 把二维 Boolean history 编译成一维 monotone boundary。

可复用 pattern 是

\[
\boxed{
\text{ordered future thresholds}
+
\text{monotone transport orbit}
\Longrightarrow
\text{crossing staircase}.
}
\]

state 应当保存“未达到 / 已达到”future queries 的边界，而不是一张 unconstrained answer table。

## 13. Prior-art / novelty 边界

monotone matrices、combinations with repetition、staircase encoding 都是 elementary / general prior mathematics。

P025 不单独主张这些概念新颖。

项目侧结果只是 dyadic projective-pressure theorem 生成的 exact arithmetic instantiation，以及它作为 finite precision normal form 的使用。历史新颖性仍为 `NOVELTY_UNVERIFIED`。

## 14. 可执行资产

新增：

- `src/enterprise_math/abc_dyadic_threshold_staircase.py`；
- `tests/test_abc_dyadic_threshold_staircase.py`。

executable layer 验证 crossing monotonicity、exact matrix reconstruction、plateau states、binomial state count，以及 `70 versus 65536` 工作样本。

## 15. 下一前沿

不存在硬阻断。继续：

1. 推导同一 staircase 的 dual node-rank representation；
2. 证明 threshold-crossing coordinates 与 per-node precision ranks 精确等价；
3. 识别由此产生的 Ferrers / lattice-path boundary geometry；
4. 用 boundary area 表示 aggregate threshold activation cost；
5. 比较两种 dual coordinates 对不同 future operations 的优劣，再考虑 Foundation feedback。
