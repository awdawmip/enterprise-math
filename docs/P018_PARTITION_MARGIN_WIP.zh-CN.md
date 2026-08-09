# P018 v2 — 精确 Partition-Margin Transport WIP

状态：`ACTIVE PROGRAM RESEARCH / NOT CANONICAL`  
范围：有限 partition refinement 下 coarse/fine proof margin 的精确代数  
来源：从 P017 MC08 finite-radius precision hierarchy 中抽取  
创新性：`NOVELTY_UNVERIFIED`；代数恒等式本身是初等的，P018 的研究点是把它解释成精确的 precision-compensation 账本。

## 1. Block observables

设有限 precision block `B` 上有有符号整数坐标 `x_s,y_s`。定义

\[
X_B=\sum_{s\in B}x_s,
\qquad
Y_B=\sum_{s\in B}y_s,
\qquad
Z_B=\sum_{s\in B}x_sy_s.
\]

定义 capacity margin

\[
\boxed{D_B=X_BY_B-Z_B.}
\]

展开乘积立即得到精确 off-diagonal 形式

\[
\boxed{
D_B=\sum_{s\ne t\in B}x_sy_t.
}
\]

因此 `D_B` 描述的是 diagonal term `Z_B` 看不到的跨 state 交互。

## 2. 精确 partition transport

设

\[
B=\bigsqcup_{i=1}^m B_i
\]

为任意有限 partition。记 `X_i=X_{B_i}`，`Y_i,D_i` 同理，则

\[
\boxed{
D_B
=
\sum_iD_i
+
\sum_{i\ne j}X_iY_j.
}
\]

### 证明

因为

\[
X_B=\sum_iX_i,
\qquad
Y_B=\sum_iY_i,
\]

所以

\[
X_BY_B
=
\sum_iX_iY_i+
\sum_{i\ne j}X_iY_j.
\]

同时 `Z_B=sum_i Z_i`。因此

\[
D_B
=X_BY_B-Z_B
=
\sum_i(X_iY_i-Z_i)
+
\sum_{i\ne j}X_iY_j.
\]

∎

对 binary split `B=L sqcup R`，得到

\[
\boxed{
D_B
=D_L+D_R
+X_LY_R+X_RY_L.
}
\]

最后两项就是 coarse precision 中存在、在进一步 refinement 时被移除的**精确 sibling compensation**。

## 3. Positive-cone persistence

若某个 proof hypothesis 强制每个 child block 都满足

\[
X_i\ge0,
\qquad Y_i\ge0,
\qquad D_i\ge0,
\]

则所有 cross terms `X_iY_j` 也非负，于是

\[
D_B\ge\sum_iD_i\ge0.
\]

所以一旦 parent 违反 nonnegative margin condition，任意 refinement 后至少有一个 child 继续违反。

这不是单独再证明一次 coarse-certificate persistence，而是从更强的精确恒等式直接推出它。

## 4. 精度提升可以移除精确 masking term

离开 hypothesis positive cone 后，有符号 coordinates 可以让 fine block 的 margin 为负，而 coarse parent 的 margin 仍为正。

具体取

- left block：`x=(-1,0)`、`y=(0,1)`，所以 `D_L=-1`；
- right singleton：`x=(3)`、`y=(0)`，所以 `D_R=0`；
- sibling compensation：`3`。

因此

\[
D_B=-1+0+3=2.
\]

低精度下，fine negative margin 被一个精确的正 cross-block compensation 遮住。提高精度并不是“近似更准确”而已，而是**删除一个可以明确写出的整数交互项**。

这是目前最直接体现项目最初设想的一条公式：

\[
\boxed{
\text{低精度证明}
\to
\text{提高精度}
\to
\text{高低精度的精确相消账本}.
}
\]

## 5. 望远镜式 precision shells

持续做 binary refinement，直到 singleton blocks。令

\[
M_m=\sum_{B\in\mathcal P_m}D_B
\]

表示 precision level `m` 的 block margins 总和。

每一次 refinement 定义 shell compensation

\[
C_m
=
\sum_{B\in\mathcal P_m}
\bigl(X_{L(B)}Y_{R(B)}+X_{R(B)}Y_{L(B)}\bigr),
\]

已经是 singleton 的 block 贡献 0。

于是精确有

\[
\boxed{M_m=M_{m+1}+C_m.}
\]

到 singleton precision，每个 block 只有一个 state，所以 `D=0`，即 `M_term=0`。因此

\[
\boxed{
M_0=\sum_{m<\mathrm{term}}C_m.
}
\]

换句话说，coarse margin 可以被完整分解成逐精度的 compensation shells；不需要极限、导数、概率模型或隐藏连续体。

## 6. 与 P017 MC08 的关系

MC08 中取

\[
x_r=a_r-1,
\qquad y_r=b_r-1.
\]

于是

\[
X_B=U_-^{(B)},
\qquad Y_B=U_+^{(B)},
\qquad D_B=U_-^{(B)}U_+^{(B)}-V^{(B)}.
\]

MC08 的 product certificate 正好就是 `D_B<0`；另外几个 certificate channels 则分别检测 `X_B`、`Y_B` 或 `V_B` 的负值。

在假设 prime-free 的情况下，所有 singleton 的 `x_r,y_r` 都非负，因此每个 sibling compensation 也非负。这给出了 MC08 refinement persistence 的结构性解释。

## 7. 边界与下一问题

partition identity 自身不能证明存在 prime；它对任意 signed sequences 都成立。它的价值是精确分离：低精度究竟丢掉了什么、提高精度时究竟移除了什么。

下一项基础问题是：P018 中其他 proof observables 是否也存在同类 exact merge/shell law，从而形成可复用的 finite-precision proof-margin calculus，而不是停留在一个问题的特殊分解。

Executable WIP 资产：

- `src/enterprise_math/precision_partition_margin.py`；
- `tests/test_precision_partition_margin.py`。
