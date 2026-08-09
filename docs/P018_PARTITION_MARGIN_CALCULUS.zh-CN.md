# P018 — 精确 Partition-Margin Calculus

状态：`ACTIVE RESEARCH NOTE`  
范围：有限 partition refinement 下 coarse/fine proof observables 的精确运输  
来源：从 canonical P017 MC08 precision hierarchy 中抽取  
创新性：`NOVELTY_UNVERIFIED`；代数恒等式本身属于初等有限代数，项目特有内容是把它作为精确 precision-compensation calculus 使用。

## 1. 四个 block observables

设有限 precision block `B` 上带有有符号整数坐标 `x_s,y_s`。定义

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

展开乘积得到精确 off-diagonal 形式

\[
\boxed{
D_B=\sum_{s\ne t\in B}x_sy_t.
}
\]

因此自然的 block observation 是

\[
\boxed{
\Phi(B)=(X_B,Y_B,Z_B,D_B).
}
\]

前三个坐标是可加的 signed observables；第四个记录 coarse aggregation 产生的 off-diagonal interaction。

## 2. 精确 partition transport

对任意有限 partition

\[
B=\bigsqcup_i B_i,
\]

记 `X_i=X_{B_i}`，其他坐标同理。则

\[
\boxed{
X_B=\sum_iX_i,
\quad
Y_B=\sum_iY_i,
\quad
Z_B=\sum_iZ_i,
}
\]

而

\[
\boxed{
D_B
=
\sum_iD_i
+
\sum_{i\ne j}X_iY_j.
}
\]

这些都是恒等式，不是估计式。

对 binary split `B=L sqcup R`，

\[
\boxed{
D_B
=D_L+D_R
+X_LY_R+X_RY_L.
}
\]

最后两项就是 coarse precision 中存在、在 children 被分别观察时移除的精确 sibling compensation。

## 3. Merge-closed proof cone

定义 admissible cone

\[
\boxed{
\mathcal K
=
\{(X,Y,Z,D)\in\mathbb Z^4:
X\ge0,\ Y\ge0,\ Z\ge0,\ D\ge0\}.
}
\]

若每个 child observation `Phi(B_i)` 都属于 `K`，那么 parent 的三个 additive coordinates 都满足

\[
X_B\ge0,
\qquad Y_B\ge0,
\qquad Z_B\ge0.
\]

同时每个 `X_iY_j` 均非负，所以

\[
D_B
=
\sum_iD_i+\sum_{i\ne j}X_iY_j
\ge0.
\]

因此

\[
\boxed{
\Phi(B_i)\in\mathcal K\ \forall i
\Longrightarrow
\Phi(B)\in\mathcal K.
}
\]

也就是说，admissible proof cone 对 coarse merge **封闭**。

取逆否命题：

\[
\boxed{
\Phi(B)\notin\mathcal K
\Longrightarrow
\text{至少一个 refined child 也不在 }\mathcal K.
}
\]

所以低精度已经获得的 proof certificate 不会在 compatible refinement 后消失。这里的 persistence 是 exact merge law 的结构性结果，而不是额外施加的单调性原则。

## 4. 两种不同的 coarse masking

四坐标形式把低精度隐藏 fine information 的机制分成两类。

### 4.1 Additive sign cancellation

`X,Y,Z` 都严格可加，所以 negative child contribution 可以被 positive siblings 在 coarse level 抵消：

\[
X_B=\sum_iX_i,
\qquad
Y_B=\sum_iY_i,
\qquad
Z_B=\sum_iZ_i.
\]

refinement 不改变总和，而是把 signed contributions 局域化，让 negative block 能够显现。

### 4.2 Bilinear sibling compensation

capacity margin 还额外带有 coarse interaction term。比如取

- left block：`x=(-1,0)`、`y=(0,1)`，得到 `D_L=-1`；
- right singleton：`x=(3)`、`y=(0)`，得到 `D_R=0`。

sibling compensation 为

\[
X_LY_R+X_RY_L=3,
\]

因此

\[
\boxed{D_B=-1+0+3=2.}
\]

parent margin 为正，但一个 child 已经是 negative margin。提高精度是在移除一个精确可写的整数 interaction，而不只是提高数值近似精度。

## 5. Margin channel 的望远镜 precision shells

持续 refinement 到 singleton resolution。令

\[
M_m=\sum_{B\in\mathcal P_m}D_B
\]

为 precision level `m` 的总 margin。

对一次 binary refinement 定义

\[
C_m
=
\sum_{B\in\mathcal P_m}
\bigl(X_{L(B)}Y_{R(B)}+X_{R(B)}Y_{L(B)}\bigr),
\]

已经 singleton 的 block 贡献 0。

则

\[
\boxed{M_m=M_{m+1}+C_m.}
\]

singleton resolution 时 `D=xy-xy=0`，故 `M_term=0`，从而

\[
\boxed{
M_0=\sum_{m<\mathrm{term}}C_m.
}
\]

整个 coarse bilinear margin 被精确分解成逐精度 compensation shells；不需要极限、导数、概率模型或隐藏连续体。

additive coordinates 的 transport 更简单：它们的全局和在 refinement 中保持不变，变化的只是**signed mass 在哪里被看见**。

## 6. P017 MC08 特化

对 canonical P017 mirror precision certificate，取

\[
x_r=a_r-1,
\qquad y_r=b_r-1.
\]

则每个 radius block `B` 上

\[
X_B=U_-^{(B)},
\qquad
Y_B=U_+^{(B)},
\qquad
Z_B=V^{(B)},
\]

以及

\[
D_B
=U_-^{(B)}U_+^{(B)}-V^{(B)}.
\]

因此 MC08 的四种 certificate channel，恰好就是 `Phi(B)` 离开 `K` 的四种方式：

\[
U_-^{(B)}<0,
\quad
U_+^{(B)}<0,
\quad
V^{(B)}<0,
\quad
U_-^{(B)}U_+^{(B)}-V^{(B)}<0.
\]

在假设 prime-free 时，每个 singleton 都有 `x_r,y_r>=0`，所以所有 compatible blocks 都落在 merge-closed cone 中。MC08 refinement persistence 因而成为一般 P018 transport law 的一个实例。

这也精确解释了更高精度为何可能暴露 certificate：它在不改变底层有限 state set 的前提下，逐步移除 additive sign masking 与 bilinear sibling compensation。

## 7. 范围边界

这些 partition identities 对任意 signed integer sequences 都成立，因此自身不能暗中证明 P017 prime target。它们是基础记账律，不是隐藏的数论定理。

其结构价值在于：P018 现在能够精确区分 lowering proof precision 时损失的两种机制——signed aggregation 与 cross-block compensation——并用有限整数 transport 表达 refinement 的作用，而不再依赖模糊的 approximation 语言。

下一项基础问题是：P018 中其他 proof observables 是否也存在类似的 merge-closed cone 或 exact shell law。

## 8. 可执行资产

- `src/enterprise_math/precision_partition_margin.py`
- `tests/test_precision_partition_margin.py`

测试覆盖一般 partition identity、binary transport、off-diagonal form、positive-cone merge behavior、真实 coarse-masking 例子，以及直到 singleton precision 的精确望远镜分解。
