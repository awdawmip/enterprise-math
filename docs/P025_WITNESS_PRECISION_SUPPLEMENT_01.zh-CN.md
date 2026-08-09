# P025 补充 01 —— Relation-Conditioned Witness Precision

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner：`program/p025-abc-support-collapse`  
依赖：P023 future-safe quotient；Pasten arithmetic derivatives 前人工作  
创新状态：`ARCHITECTURE NOVELTY_UNVERIFIED`

## 1. 从 arithmetic derivative 转成有限坐标

固定 primitive abc 三元组

\[
a+b=c,\qquad \gcd(a,b)=1,
\]

并令

\[
S=\operatorname{supp}(abc).
\]

Pasten 的 universal Leibniz map 以每个 `p in S` 的 `xi_p` 为坐标；一个 derivation `psi` 在当前有限 support 上可写成整数向量

\[
x=(x_p)_{p\in S},\qquad x_p=\psi(\xi_p).
\]

对整数 `n`，

\[
d^\psi(n)=n\sum_{p\mid n}\frac{v_p(n)}p x_p.
\]

这些公式和以下格结构均来自 Pasten 的前人工作 [SRC-PASTEN-2021-ARITHMETIC-DERIVATIVES]。P025 的新增候选只是把它重新解释成有限精度对象。

## 2. P025-T05 —— 加法 witness 格是一个整数超平面核

条件

\[
d^\psi(a)+d^\psi(b)=d^\psi(c)
\]

等价于

\[
\sum_{p\in S}\alpha_p x_p=0,
\]

其中，由于 `a,b,c` 两两互素，

\[
\alpha_p=
\begin{cases}
 a\,v_p(a)/p,&p\mid a,\\
 b\,v_p(b)/p,&p\mid b,\\
 -c\,v_p(c)/p,&p\mid c.
\end{cases}
\]

每个系数都是整数。令

\[
\alpha=(\alpha_p)_{p\in S}
\]

并除去全部坐标的 gcd、固定整体符号，得到 primitive normal

\[
\widehat\alpha(a,b,c).
\]

于是 Pasten 的加法 witness 模块可写成

\[
\boxed{
T(a,b)=\ker_{\mathbb Z}\widehat\alpha
=\{x\in\mathbb Z^S:\widehat\alpha\cdot x=0\}.
}
\]

Pasten 已证明在 `c>2` 的相应范围内它是 saturated free abelian subgroup，秩为

\[
|S|-1=\omega(abc)-1.
\]

### 架构解释

当前 relation 不需要把所有 valuation 数据都直接保存在 coarse state 中；它首先把细状态压成一个**带 prime 标签的 primitive normal**，然后由该 normal 生成允许的 witness 格。

因此可暂记 relation signature

\[
\boxed{\Sigma_{\rm add}(a,b,c)=(S,\widehat\alpha).}
\]

这里的格论本身是初等/既有数学；`relation signature` 是 P025 的架构命名。

## 3. P025-T06 —— primitive normal 是 additive witness lattice 的完备签名

设 `S` 为固定有限标签集，`alpha,beta in Z^S` 都是 primitive nonzero vectors，并定义

\[
L_\alpha=\ker_{\mathbb Z}\alpha,
\qquad
L_\beta=\ker_{\mathbb Z}\beta.
\]

则

\[
\boxed{
L_\alpha=L_\beta
\iff
\beta=\pm\alpha.
}
\]

### 证明

`<=` 方向显然。

反向若两个整数核相同，则它们张成的有理超平面也相同：任意 `ker_Q(alpha)` 中的有理向量乘清分母后都落入 `ker_Z(alpha)`，反之亦然。因此

\[
\ker_{\mathbb Q}\alpha
=
\ker_{\mathbb Q}\beta.
\]

两个非零线性泛函具有相同 codimension-one 核，故 `beta=lambda alpha` 对某个非零 `lambda in Q` 成立。由于二者均 primitive integer vectors，只可能

\[
\lambda=\pm1.
\]

证毕。

### P023 最小修复解释

如果未来观察量不是单个数值，而是

\[
h(a,b,c)=T(a,b),
\]

那么规范化后的 `Sigma_add` 是 `h` 的完备编码。

因此任何能让完整 additive witness lattice 精确下沉的 quotient 都必须至少区分不同的 `Sigma_add`。若从 radical coarse state `q_rad` 出发，则

\[
\boxed{
q_1=(q_{\rm rad},\Sigma_{\rm add})
}
\]

正是对“保留完整 additive witness lattice”这一指定未来观察的 P023 型最粗一步修复。

注意：这不说明 `Sigma_add` 是 ABC 所需的最小信息，也不说明它对全部未来运算安全；它只精确回答当前 witness-lattice observation。

## 4. Wronskian 退化给出第二个超平面

Pasten 定义

\[
W^\psi(a,b)=a\,d^\psi(b)-b\,d^\psi(a).
\]

它仍是 `x_p` 的整数线性形式：

\[
W^\psi(a,b)=\sum_{p\in S}\beta_p x_p.
\]

定义退化子格

\[
T^\circ(a,b)
=
T(a,b)\cap\ker_{\mathbb Z}\beta.
\]

Pasten 在相应 primitive 非平凡范围内证明

\[
\operatorname{rk}T^\circ
=\operatorname{rk}T-1.
\]

所以得到一个严格格旗标

\[
\boxed{
T^\circ(a,b)\subsetneq T(a,b)\subset\mathbb Z^S.
}
\]

真正可用于 Mason 型论证的 witness 是

\[
x\in T(a,b)\setminus T^\circ(a,b).
\]

## 5. P025-D01 —— witness precision

给环境格 `Z^S` 使用 Pasten 的 sup norm

\[
\|x\|_\infty=\max_{p\in S}|x_p|.
\]

对每个整数半径 `k>=0` 定义

\[
\mathcal W_k(a,b)
=
\{x\in T(a,b)\setminus T^\circ(a,b):
\|x\|_\infty\le k\}.
\]

则显然

\[
\mathcal W_0\subseteq
\mathcal W_1\subseteq
\mathcal W_2\subseteq\cdots.
\]

定义第一可用 witness 半径

\[
\boxed{
\mu(a,b,c)
=\min\{k\in\mathbb N:\mathcal W_k(a,b)\neq\varnothing\}.
}
\]

由于 `T^circ` 是 `T` 的真子格，存在非退化整数 witness，所以 `mu` 有限。

### 精度解释

`mu` 不是测量误差，也不是浮点容差。它表示：

> **为了让当前 relation 在被 radical 等 coarse collapse 遗忘细节以后仍获得一个非退化跨语言证书，至少需要打开多大的离散 witness 坐标半径。**

这给出了一个 task-relative、relation-conditioned 的有限整数精度坐标。

## 6. P025-N02 —— witness precision 不通过 radical state 下沉

比较两个 primitive abc 三元组：

\[
1+2=3,
\qquad
1+8=9.
\]

它们的完整 radical 三元状态完全相同：

\[
\boxed{
(\operatorname{rad}a,\operatorname{rad}b,\operatorname{rad}c)
=(1,2,3).
}
\]

而两者的 witness 坐标都只需要 prime labels `(2,3)`。

### 状态 A：`1+2=3`

加法条件为

\[
x_2-x_3=0,
\]

所以

\[
T_A=\{(t,t):t\in\mathbb Z\}.
\]

Wronskian 对 `t neq 0` 非退化，因此

\[
\boxed{\mu_A=1.}
\]

### 状态 B：`1+8=9`

原始加法系数为

\[
12x_2-6x_3=0,
\]

primitive 化后为

\[
2x_2-x_3=0.
\]

因此

\[
T_B=\{(t,2t):t\in\mathbb Z\},
\]

最小非退化向量 sup norm 为 `2`：

\[
\boxed{\mu_B=2.}
\]

所以

\[
q_{\rm rad}(A)=q_{\rm rad}(B)
\quad\text{但}\quad
T_A\ne T_B,
\qquad
\mu_A\ne\mu_B.
\]

即

\[
\boxed{
\text{witness family 与 witness precision 都不能由 radical coarse state 单独决定。}
}
\]

这是比“radical 不与加法 congruent”更强的架构边界：即使把未来目标放宽为“存在一个小证书”，其最小证书成本仍然感知被 radical 忘掉的 multiplicity。

## 7. 这反哺 P023 什么

P023 的 exact repair 路径是：

\[
\text{coarse quotient}
\to
\text{补回区分未来所需的信息}
\to
\text{future operation descends exactly}.
\]

P025 现在出现第二种路径：

\[
\text{coarse quotient}
\to
\text{relation signature}
\to
\text{multivalued witness lattice/flag}
\to
\text{first usable witness radius }\mu.
\]

二者不是同一个概念：

- `q_1=(q_rad,Sigma_add)` 可以让**完整 witness lattice** 精确下沉；
- 但 ABC 真正需要的可能只是“存在足够小的非退化 witness”，未必需要恢复整个 lattice；
- 因而还存在一个新的最小化问题：为了只决定 `mu<=K` 或存在某类 certificate，是否能使用比 `Sigma_add` 更粗的修复？

这成为 P025 下一步与 P023 的精确交叉点。

## 8. 这反哺 A4 什么

A4 已经把 admissible support 视为多值关系而不是强行单值化。P025 的

\[
\mathcal W_k(a,b)
\]

天然也是一个随半径单调增长的有限 admissible witness family。

但不能直接断言它继承 A4 的全部 composition law。当前只获得：

1. 每个固定 `k` 下 witness family 有限；
2. 随 `k` 单调增长；
3. `mu` 是第一次非空的 critical radius；
4. relation 改变会改变格本身，而不是只改变半径。

是否存在可复用的 witness composition / transport law，保持开放并必须通过反例优先测试。

## 9. 更精确的基础架构候选

第一阶段曾写成

`coarse state -> witness family -> witness cost`。

P025-N02 说明这还不够严密，因为 witness family 并不由 coarse radical state 决定。更准确的候选是

\[
\boxed{
\text{fine relation-state}
\xrightarrow{q}
\text{coarse state}
\quad+\quad
\text{relation signature}
\longrightarrow
\text{normed witness flag}
\longrightarrow
\mu.
}
\]

也就是说，“证书层”不是粗状态的普通属性，而是一个由**任务关系 + 尚未完全消失的细结构**共同生成的附着对象。

这与 Foundation `FQ-20260809-004` 的边界直觉一致：functional state、relation-state、multivalued support 不应被过早合成一个类型。

## 10. 当前可执行资产

新增：

- `src/enterprise_math/abc_witness_precision.py`
  - Pasten additive relation 的 primitive integer normal；
  - Wronskian degeneracy normal；
  - normed witness flag；
  - bounded exact witness enumeration；
  - minimal witness cost；
  - same-radical / different-witness-precision 反例；
  - primitive kernel signature normalization。
- `tests/test_abc_witness_precision.py`
  - `1+2=3`：`mu=1`；
  - `1+8=9`：`mu=2`；
  - 相同 radical state 的强反例；
  - witness balls 的单调性；
  - `5+27=32` 的三坐标格样本；
  - primitive normal scaling invariance；
  - exact enumeration state-cap guard。

这些工具只用于小 support 的 exact oracle，不替代 Pasten 的 Geometry-of-Numbers 渐近工具。

## 11. 下一问题

目前最值得攻的不是继续枚举 ABC triples，而是两个一般问题：

### Q1 —— certificate-decision 的最粗修复

若未来只问

\[
\mu(x)\le K?
\]

而不是恢复完整 `T(x)`，那么 `Sigma_add` 很可能过细。

需要求出对该二值/分级未来观测的真正 P023-minimal repair，并比较其信息量随 `K` 的变化。

### Q2 —— normed flag 的规范签名

完整非退化 witness 结构由

\[
T^\circ\subset T\subset\mathbb Z^S
\]

和 norm 决定。`T` 单独由 primitive `alpha` 完全刻画；但 `T^circ` 只取决于第二泛函在 `T` 上的限制，因此 `beta` 在加上 `alpha` 的倍数后可能表示同一个退化子格。

所以完整 flag 的最小规范签名不是简单 pair `(alpha,beta)`，而应研究一个 quotient / row-module / exterior invariant。这个问题正好是 P023 quotient 与 A4 relation-support 的交叉点。

当前状态：`OPEN / HIGH VALUE / HARD_BLOCK=NONE`。
