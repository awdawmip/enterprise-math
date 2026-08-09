# P025 补充 30 —— Matrix-Preimage Access 作为 Derivative Image 上的 Exact Word Norm

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-shared-access-stage30`  
Base：冻结的 Stage-18–29 generation  
依赖：P025 补充 28；intrinsic discrete-geometry language  
Hard block：`NONE`

## 1. Shared-prime access problem

补充 28 把 independent block preimages 替换成一个 joint integer matrix problem。令

\[
B\in\mathbb Z^{m\times s}
\]

为 block-by-prime derivative coefficient matrix。对 block-value target

\[
t\in\operatorname{im}_{\mathbb Z}B,
\]

定义 exact joint access

\[
\boxed{\kappa_B(t)=\min\{\|x\|_\infty:Bx=t\}.}
\]

在直接调用 Smith/Hermite normal form 或 CVP machinery 之前，`L_infinity` cube 本身已经给出更简单的结构。

## 2. P025-D17 —— radius image sets

对每个整数半径 `r>=0` 定义

\[
\boxed{Z_r(B)=B([-r,r]^s\cap\mathbb Z^s).}
\]

则

\[
\boxed{\kappa_B(t)=\min\{r:t\in Z_r(B)\}.}
\]

one-step image

\[
\boxed{S_B=Z_1(B)}
\]

有限、对称、含零，并包含每个 signed matrix column，因此生成整个 image group

\[
\Gamma_B=\operatorname{im}_{\mathbb Z}B.
\]

## 3. P025-T84 —— exact Minkowski radius law

对所有非负整数 `r,s`，

\[
\boxed{Z_{r+s}(B)=Z_r(B)+Z_s(B).}
\]

### 证明

若 `y` coordinate radius 不超过 `r`、`z` 不超过 `s`，则 `y+z` radius 不超过 `r+s`，故

\[
Z_r+Z_s\subseteq Z_{r+s}.
\]

反过来任取

\[
x\in[-r-s,r+s]^s\cap\mathbb Z^s.
\]

逐 coordinate 把 `x_i` 拆成

\[
x_i=y_i+z_i
\]

并令

\[
|y_i|\le r,
\qquad |z_i|\le s.
\]

例如把 `x_i` clamp 到 `[-r,r]` 作为 `y_i`，其余整数 remainder 放入 `z_i`；因为 `|x_i|<=r+s`，remainder 大小不超过 `s`。

于是

\[
Bx=By+Bz,
\]

得到反向包含。∎

## 4. P025-T85 —— access 精确就是 finite-generator word norm

反复取 `s=1` 得

\[
\boxed{Z_r(B)=\underbrace{S_B+\cdots+S_B}_{r\text{ 次}}.}
\]

由于 `0 in S_B`，这也是最多使用 `r` 个 one-step generators 所能得到的集合。

所以

\[
\boxed{\kappa_B(t)=|t|_{S_B},}
\]

即 abelian image-group element `t` 相对于 finite symmetric generating set `S_B` 的 ordinary word length。

因此

\[
\boxed{
\begin{aligned}
\kappa_B(0)&=0,\\
\kappa_B(-t)&=\kappa_B(t),\\
\kappa_B(t+u)&\le\kappa_B(t)+\kappa_B(u).
\end{aligned}}
\]

Matrix-preimage access 不再只是 search cost，而是 derivative image lattice 上的 intrinsic integer metric/word-norm structure。

### Prior-art 边界

Finitely generated abelian groups 上的 word metrics、cube images、zonotopes 与 Minkowski sums 都是标准数学。P025 不对它们作创新主张。项目侧价值是 arithmetic-derivative `L_infinity` preimage precision 与该结构的 exact identification。

## 5. 不枚举 cube 的 dynamic image computation

`Z_r(B)` 可以 column-by-column 构造。若 `b_j` 是 column `j`，其 radius-`r` contribution 是有限 segment

\[
\{-rb_j,\ldots,0,\ldots,rb_j\}.
\]

反复做这些 column segments 的 Minkowski addition，会即时合并 duplicate image states，因此 reference implementation 枚举的是 derivative-image values，而不是全部

\[
(2r+1)^s
\]

fine coordinate vectors。

收益取决于 `B` 的 rank/geometry；不主张 universal polynomial complexity。

## 6. Shared-prime example `(4,8)`

Derivative matrix 为

\[
B=\begin{pmatrix}4\\12\end{pmatrix}.
\]

所以

\[
S_B=\{(-4,-12),(0,0),(4,12)\}.
\]

因此

\[
\kappa_B(4,12)=1,
\qquad\kappa_B(8,24)=2.
\]

尽管报告两个 block values，image group 实际只有一维，与补充 28 一致。

## 7. Shared-prime example `2,4,6`

这里

\[
B=\begin{pmatrix}1&0\\4&0\\3&2\end{pmatrix}.
\]

状态

\[
(1,4,5)=B(1,1)
\]

满足

\[
\kappa_B=1.
\]

补充 28 的 false separate-ideal state

\[
(0,4,4)
\]

根本不在 image group 中，所以不存在任何 finite access radius。word-norm formulation 自动排除该假状态。

## 8. P025-N12 —— Restrict 到 relation subgroup 后，不一定等于 radius-one intrinsic word norm

现在施加有效 block relation

\[
\boxed{4\cdot2+1\cdot4-2\cdot6=0.}
\]

即

\[
L=(4,1,-2).
\]

对上述 derivative matrix，

\[
\boxed{LB=(2,-4).}
\]

fine relation-adapted coordinates 满足

\[
x_2=2x_3.
\]

radius 1 时唯一 relation-compatible fine coordinate 是零，所以

\[
\boxed{Z_1(B)\cap\ker L=\{0\}.}
\]

但 radius 2 时

\[
x=(2,1)
\]

已 relation-adapted，并给出

\[
\boxed{t=(2,8,8),\qquad\kappa_B(t)=2.}
\]

所以 relation subgroup 中存在 nonzero finite-access elements，尽管它与 ambient one-step generator 的交只有零。

因此

\[
\boxed{
\kappa_B|_{\Gamma_B\cap\ker L}
\text{ 一般不等于由 }S_B\cap\ker L\text{ 生成的 intrinsic word norm}.}
\]

原因是 ambient optimal word decomposition 可以经过单步上暂时离开 relation subgroup 的 image elements，最终再通过 cancellation 回到 relation subgroup。

这是精确的 future/composition boundary：把合法 ambient metric 限制到 relation state，与从 relation-compatible primitive steps 重新生成 metric，并不是同一操作。

## 9. 架构后果

Shared-prime access hierarchy 为

\[
\boxed{
\text{fine coordinate cube}
\xrightarrow{B}
\text{finite one-step image }S_B
\to
\text{word norm }\kappa_B
\to
\text{relation subgroup restriction}.
}
\]

必须区分两种 geometry：

1. **ambient derivative-image access：**由 `S_B` 得到的 exact word norm；
2. **intrinsic relation-step geometry：**若定义，则由 relation-compatible primitive generators 得到的 word norm。

二者可以严重不同，P025 不得静默互换。

## 10. 可执行资产

Stage-30 owner 新增：

- `src/enterprise_math/matrix_access_word_norm.py`
  - exact radius image sets；
  - Minkowski addition；
  - one-step/repeated-step image identity；
  - exact matrix access radius；
  - triangle regression；
  - relation-subgroup one-step failure counterexample。
- `tests/test_matrix_access_word_norm.py`
  - `(4,8)` one-dimensional image；
  - exact `Z_(r+s)=Z_r+Z_s` checks；
  - `2,4,6` false-state exclusion；
  - triangle inequality；
  - relation-subgroup failure boundary；
  - pairwise-coprime calibration。

## 11. 下一前沿

没有 hard block。继续：

1. 定义让 `Z_R(B) intersect ker L` 开始生成整个 relation subgroup 的 minimum relation-generator radius；
2. 分类 ambient access restriction 何时等于 intrinsic relation-step word norm；
3. 将该边界连接到 A5/P012 intrinsic graph geometry，但不混淆 metrics；
4. 只在 SNF/HNF 真能缩短 exact generator/access calculation 时使用它们，而不是自动替换 word-norm state；
5. 把 ambient-vs-intrinsic metric distinction Relay 给 P023/A3/A5。
