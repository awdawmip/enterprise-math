# P018 — 精确 Partition-Margin Calculus

状态：`ACTIVE RESEARCH NOTE`  
范围：有限 partition refinement 下 coarse/fine proof margin 的精确运输  
来源：从 P017 MC08 precision hierarchy 中抽取  
创新性：`NOVELTY_UNVERIFIED`；恒等式本身属于初等有限代数，项目特有内容是把它作为精确 precision-compensation calculus 使用。

## 1. Block margin

设有限 precision block `B` 上带有有符号整数坐标 `x_s,y_s`。定义

\[
X_B=\sum_{s\in B}x_s,
\qquad
Y_B=\sum_{s\in B}y_s,
\qquad
Z_B=\sum_{s\in B}x_sy_s.
\]

定义 block capacity margin

\[
\boxed{D_B=X_BY_B-Z_B.}
\]

展开乘积得到

\[
\boxed{
D_B=\sum_{s\ne t\in B}x_sy_t.
}
\]

因此 margin 精确记录了只保留 diagonal observable `Z_B` 时被压掉的 off-diagonal interaction。

## 2. 精确 partition transport

对任意有限 partition

\[
B=\bigsqcup_i B_i,
\]

记 `X_i=X_{B_i}`，`Y_i,D_i` 同理，则

\[
\boxed{
D_B
=
\sum_iD_i
+
\sum_{i\ne j}X_iY_j.
}
\]

这是一条恒等式，不是估计式。

对 binary split `B=L sqcup R`，

\[
\boxed{
D_B
=D_L+D_R
+X_LY_R+X_RY_L.
}
\]

最后两项就是 coarse precision 中存在、在把 `L` 和 `R` 分别观察时被移除的精确 sibling compensation。

## 3. Positive-cone persistence

若某个 hypothesis 强制每个 child block 满足

\[
X_i\ge0,
\qquad Y_i\ge0,
\qquad D_i\ge0,
\]

则每个 cross term `X_iY_j` 也非负，因此

\[
D_B\ge\sum_iD_i\ge0.
\]

取逆否命题：

\[
\boxed{
D_B<0
\Longrightarrow
\text{至少有一个 refined child 也离开 admissible cone。}
}
\]

所以 compatible refinement 不会让 coarse certificate 消失。这里的 persistence 直接来自精确 transport law，而不是额外假设一个单调性规则。

## 4. 精确 masking 与 unmasking

离开 positive cone 后，fine negative margin 可以被 positive coarse compensation 精确遮住。

取

- left block：`x=(-1,0)`、`y=(0,1)`，得到 `D_L=-1`；
- right singleton：`x=(3)`、`y=(0)`，得到 `D_R=0`。

sibling compensation 为

\[
X_LY_R+X_RY_L=3.
\]

所以

\[
\boxed{D_B=-1+0+3=2.}
\]

coarse observation 的 margin 为正，但 left child 已经带有 negative certificate。提高精度并不只是让数值近似更好，而是移除一个能够明确写出的整数 interaction term。

## 5. 望远镜式 precision shells

持续 refinement 直到 singleton resolution。令

\[
M_m=\sum_{B\in\mathcal P_m}D_B
\]

表示 precision level `m` 的 block margins 总和。

对一次 binary refinement 定义 shell compensation

\[
C_m
=
\sum_{B\in\mathcal P_m}
\bigl(X_{L(B)}Y_{R(B)}+X_{R(B)}Y_{L(B)}\bigr),
\]

已经是 singleton 的 block 贡献 0。

binary transport identity 给出

\[
\boxed{M_m=M_{m+1}+C_m.}
\]

到了 singleton resolution，每个 block 只有一个 state，因此 `D=xy-xy=0`，也就是 `M_term=0`。于是

\[
\boxed{
M_0=\sum_{m<\mathrm{term}}C_m.
}
\]

整个 coarse margin 被精确分解为逐精度 compensation shells；不需要极限、导数、概率模型或隐藏连续体。

## 6. P017 MC08 特化

canonical P017 mirror precision certificate 中取

\[
x_r=a_r-1,
\qquad y_r=b_r-1.
\]

则每个 radius block `B` 上

\[
X_B=U_-^{(B)},
\qquad
Y_B=U_+^{(B)},
\]

并且

\[
D_B=U_-^{(B)}U_+^{(B)}-V^{(B)}.
\]

MC08 的 product certificate 恰好就是 `D_B<0`。在假设 prime-free 时，每个 singleton 的 `x_r,y_r` 都非负，所以所有 compatible merge compensations 都落在 nonnegative cone 内，certificate persistence 随即成立。

这精确说明了 precision hierarchy 在代数上做什么：coarse blocks 含有 cross-radius compensation；refinement 逐层移除这些项，直到有符号局部结构显现出来。

## 7. 范围边界

partition identity 对任意 signed integer sequences 都成立，因此它自身不可能暗中证明 P017 的 prime target。它是一条基础记账律，不是隐藏的数论定理。

其结构价值在于：对于一类非平凡的 bilinear proof margins，P018 终于可以精确回答“降低证明精度时究竟移除了什么信息”。

下一项基础问题是：P018 中其他 proof observables 是否也存在同类 exact merge law，从而把低/高精度相消写成有限 shell terms，而不再停留在模糊的 approximation 语言。

## 8. 可执行资产

- `src/enterprise_math/precision_partition_margin.py`
- `tests/test_precision_partition_margin.py`

测试覆盖一般 partition identity、binary transport、positive-cone persistence、真实 coarse-masking 例子，以及直到 singleton precision 的精确望远镜分解。
