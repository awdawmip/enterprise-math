# A3 ↔ A4 Relation-Support Bridge — Supplement 01

状态：`ACTIVE RESEARCH NOTE`  
范围：A3 生成 support 子类中的 A4 common-target composition 与 split-completeness

## 1. 设置

使用 Stage 01 在 zero-relation classes 上得到的 A3-generated symmetric support family：

\[
[i]R_r[j]\iff |Z_{ij}|\le r m_i m_j.
\]

因为该条件对称，

\[
R_r^{-1}=R_r.
\]

所以 A4 common-target composition 在这里直接变成

\[
\boxed{C_{r,s}=R_r;R_s.}
\]

Stage 01 已经证明

\[
R_r;R_s\subseteq R_{r+s}.
\]

## 2. B04 — split-completeness 等价于预算插值

对固定 `r,s`，等式

\[
\boxed{R_r;R_s=R_{r+s}}
\]

成立，当且仅当每一对满足

\[
|Z_{ik}|\le(r+s)m_im_k
\]

的 endpoint classes `[i],[k]`，都存在至少一个 quotient class `[j]`，使

\[
|Z_{ij}|\le r m_i m_j,
\qquad
|Z_{jk}|\le s m_jm_k.
\]

因此 A4 的 split-completeness 在这一子类中精确变成**A3 表示状态空间的 interpolation property**。

左到右的包含由 weighted triangle theorem 给出；反向包含恰好就是中间 witness 的存在性。

## 3. “离散空间有洞”的解释

split-completeness 失败，并不表示 endpoint 的总半径判断错了，而表示当前被表示出来的 quotient state set 中，没有一个状态能够按照要求把总预算拆成两段。

所以

\[
R_{r+s}\setminus(R_r;R_s)
\]

就是一组有限的 **missing interpolation witnesses**。

这给 A4 split-completeness 一个具体的 A3/A5 含义：它在检查离散表示状态沿 relation coordinate 是否“填得足够密”，从而允许所要求的分段实现。

## 4. B05 — unit-capacity integer-convex 的充分条件

假设所有 capacities 都等于 1，并且在 zero-relation quotient 后，被表示的整数值恰好形成一个连续整数区间

\[
\{a,a+1,\ldots,b\}.
\]

则对所有非负整数 `r,s`，生成 family 都 split-complete：

\[
R_r;R_s=R_{r+s}.
\]

### 证明

unit-capacity 时 `Z_ij=c_i-c_j`，所以 support 就是普通整数差：

\[
|c_i-c_k|\le r+s.
\]

从 `c_i` 朝 `c_k` 的方向最多走 `r` 个整数单位，得到 `c_j`。由于整数区间没有洞，`c_j` 必定存在。于是

\[
|c_i-c_j|\le r,
\qquad
|c_j-c_k|\le s.
\]

所以任何 total-budget pair 都有中间 witness。

这只是充分条件，不主张它在 weighted/general finite 情形下是必要条件。

## 5. B06 — 最小 hole counterexample

取 unit capacities，表示值只有

\[
\{0,2\}.
\]

则

\[
(0,2)\in R_2,
\]

但因为中间值 `1` 不存在，`R_1` 只有 identity，因此

\[
(0,2)\notin R_1;R_1,
\]

从而

\[
\boxed{R_1;R_1\subsetneq R_2.}
\]

缺失的整数状态 `1` 就是缺失的 interpolation witness。

## 6. 后果

### 对 A4

split-completeness 必须继续作为更强性质，而不能升级为 universal admissible-support axiom。即使 support 是由 closed A3 state 规范生成，也可能因为状态集合稀疏而失败。

### 对 A3

`R_(r+s) \ (R_r;R_s)` 成为一个新的 finite observable：它测量“endpoint 看起来足够接近，但 staged transport 无法实现”的 representation holes。

### 对 A5/P022

几何研究可以进一步问：具体 lattice/root-lattice state set 是否满足相应 interpolation property，以及从什么 radius 开始满足。这给 abstract A4 split-completeness 与 discrete-geometric geodesic filling 之间建立了明确接口。

### 对 A2/P023

如果未来 operation 假设的是 two-stage support composition，而不仅仅是 endpoint support，那么在存在 missing interpolation witness 时，单独保存 `R_(r+s)` 就不够。额外 witness 需求再次成为 future-compatibility/refinement obligation。

## 7. Executable reference

`relation_support_bridge.py` 新增：

- `common_target_support`；
- `split_complete_at`；
- `missing_interpolations`。

测试加入：

- unit values `{0,1,2}`：`R_1;R_1=R_2`；
- unit values `{0,2}`：因为缺少 midpoint 而严格失败。
