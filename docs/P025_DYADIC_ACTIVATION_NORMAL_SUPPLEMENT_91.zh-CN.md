# P025 补充 91 —— Dyadic First-Activation Normal Form

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-orbit-normal-stage91`  
依赖：P025 补充 86、90  
硬阻断：`NONE`

## 1. Stage 86 的冻结输入

固定不同奇素数

\[
3\le q<p
\]

以及 base exponent

\[
m\ge2.
\]

对 dyadic difference orbit 定义

\[
e_j:=2^jm,
\qquad
\rho_j:=\rho_{e_j,-}.
\]

Stage 86 已证明精确递推

\[
\boxed{
\rho_{j+1}
=ho_j u_j,
\qquad
u_j:=m(p^{e_j}+q^{e_j})\in\mathbf N_{\ge1}.
}
\]

因此

\[
\boxed{\rho_0\le\rho_1\le\rho_2\le\cdots.}
\]

Stage 91 研究这条单调性对 finite precision 的含义。

## 2. P025-D34 —— threshold activation profile

固定 future threshold

\[
T>0
\]

与有限 dyadic horizon

\[
0\le j\le h.
\]

定义 Boolean activation profile

\[
\boxed{a_j(T):=\mathbf1_{\{\rho_j\ge T\}}.}
\]

如果不利用 transport theorem，它形式上会是一条长度 `h+1` 的任意 Boolean word。

## 3. P025-T206 —— 每条 dyadic activation profile 都是 suffix

因为 pressure sequence 单调不降，

\[
\rho_j\ge T
\Longrightarrow
\rho_{j+1}\ge T.
\]

所以

\[
\boxed{a_j(T)\le a_{j+1}(T).}
\]

每个有限 activation profile 必为

\[
\boxed{00\cdots0011\cdots11.}
\]

最多只会发生一次 threshold-crossing transition。

## 4. P025-D35 —— first activation depth

定义

\[
\boxed{
j_T:=\min\{j\in\{0,\ldots,h\}:\rho_j\ge T\},}
\]

若集合为空，则记

\[
\boxed{j_T=\infty.}
\]

于是 P025-T206 给出 exact reconstruction rule

\[
\boxed{a_j(T)=1\iff j\ge j_T,}
\]

并约定任何有限 `j` 都不大于无穷。

因此 `j_T` 是整个 threshold activation profile 的 complete normal form。

## 5. P025-T207 —— 精确 finite state-space collapse

长度 `h+1` 的 unconstrained Boolean profile 有

\[
2^{h+1}
\]

种可能。

而 upward-closed suffix 只由

\[
0,1,\ldots,h,\infty
\]

中的一个状态决定，所以 compatible dyadic profiles 恰只有

\[
\boxed{h+2}
\]

种。

因此 transport theorem 把 semantic threshold-profile state space 从

\[
\boxed{2^{h+1}}
\]

精确压缩到

\[
\boxed{h+2.}
\]

这不是 asymptotic heuristic，而是 exact combinatorial reduction。

## 6. P025-T208 —— cumulative multiplier formula

迭代 Stage 86 recurrence 得

\[
\boxed{
\rho_j
=ho_0
\prod_{i=0}^{j-1}u_i.
}
\]

所以

\[
\boxed{
j_T
=
\min\left\{
0\le j\le h:
\rho_0\prod_{i<j}u_i\ge T
\right\}.}
\]

first-activation depth 因而是正整数 residual multipliers 累积乘积的 first-passage index。

取对数后，它变成一个 monotone additive resource accumulation problem。

## 7. 精确非平凡 crossing fixture

取

\[
(q,p)=(3,41),
\qquad m=2.
\]

对应 exponents

\[
2,4,8,16
\]

的 exact difference pressures 是

\[
\boxed{
\frac1{22},
\frac{13}{22},
\frac{221}{22},
\frac{221}{22}.
}
\]

在 threshold

\[
T=1
\]

下 activation profile 为

\[
\boxed{(0,0,1,1),}
\]

所以

\[
\boxed{j_1=2.}
\]

这说明 normal form 并不只覆盖 `j_T=0` 或 `infinity` 两个 trivial boundary cases。

## 8. 边界 fixtures

### 起点已激活

对

\[
(q,p,m)=(23,41,2),
\]

Stage 82 给出

\[
\rho_{2,-}=\frac32>1.
\]

因此所有有限 dyadic descendants 都 active，

\[
\boxed{j_1=0.}
\]

### 测试 horizon 内未激活

对

\[
(q,p,m)=(3,5,2),
\]

exponents `2,4,8,16` 上的有限 pressures 在 tests 中都保持 `1/2`，所以在这个 horizon 内

\[
\boxed{j_1=\infty.}
\]

这里只是 finite-horizon statement；Stage 91 不从有限计算推断无限 tower。

## 9. P025-T209 —— active signed seed 控制 crossing depth

Stage 86 还证明

\[
\rho_{2m,-}
\ge
\max\{\rho_{m,-},\rho_{m,+}\}.
\]

因此对任意 threshold `T`：

- 若 `rho_{m,-}>=T`，则
  \[
  \boxed{j_T=0;}
  \]
- 若 `rho_{m,+}>=T` 且 `rho_{m,-}<T`，则
  \[
  \boxed{j_T\le1.}
  \]

所以一个 active sum state 是 immediate one-step certificate：相应 difference dyadic orbit 最迟在下一节点进入 active basin。

例如 `(q,p,m)=(5,59,3)` 的 cube-sum pressure active、cube-difference pressure subunit，但 doubled difference state 已 active。

## 10. P025-T210 —— first activation depth 是 future-relative 的

orbit 固定不变，但 `j_T` 取决于 declared threshold。

对 `(3,41,2)` fixture：

- `T=1`：`j_T=2`；
- `T=10`：`j_T=2`；
- `T=11`：直到 exponent `16` 都没有达到 threshold。

所以 normal form 不是 orbit 自身的 intrinsic label，而是 future query 的函数。

这正是 Stage 90 edge-level future-relative precision 在 orbit level 的对应形式。

## 11. Semantic 与 exact orbit state

对 future query

> 在 `h` 以内哪些 depths 满足 `rho_j>=T`？

`j_T` exact sufficient。

对更强 future query

> 每个 exact pressure `rho_j` 是多少？

`j_T` 不够；必须保留 base pressure 与足够的 cumulative multiplier information。

所以同一个 dyadic orbit 又出现 natural precision ladder：

\[
\boxed{
(\rho_0,u_0,\ldots,u_{h-1})
\longrightarrow
j_T
\longrightarrow
\text{one selected activation bit}.
}
\]

正确 collapse 取决于 future language。

## 12. 架构含义

Stage 91 把 deterministic monotone transport 编译成 finite orbit normal form。

可复用机制是

\[
\boxed{
\text{monotone refinement orbit}
+
\text{threshold future}
\Longrightarrow
\text{first-passage precision}.
}
\]

如果 transition theorem 已强迫 threshold bits 构成 upward-closed suffix，系统就不应保存一整段冗余 history。

这比简单 deduplicate dyadic descendants 更强：它识别了 threshold future 真正需要的 exact semantic coordinate。

## 13. Prior-art / novelty 边界

monotone Boolean sequences、first-passage indices 与 threshold-crossing compression 都是 elementary / general prior concepts。

P025 不单独主张这些概念新颖。

项目侧结果只是：由 Stage 86 signed arithmetic pressure law 得到的 exact instantiation、number-theoretic executable fixtures，以及 future-relative precision interpretation。历史新颖性仍为 `NOVELTY_UNVERIFIED`。

## 14. 可执行资产

新增：

- `src/enterprise_math/abc_dyadic_activation_normal.py`；
- `tests/test_abc_dyadic_activation_normal.py`。

executable layer 验证 suffix reconstruction、exact first crossings、boundary normal forms、finite state-space reduction、threshold dependence，以及 active-sum one-step bound。

## 15. 下一前沿

不存在硬阻断。继续：

1. 用 ordered finite threshold family 替代单一 threshold，把整张 activation matrix 压成 monotone crossing-depth staircase；
2. 精确计算 multi-threshold state-space reduction；
3. 判断 mixed future query（既要 threshold activation 又要 selected nodes exact pressure）的 minimal state；
4. 把 dyadic normal form 与 Stage 89 odd-prime Hasse cover labels 合并；
5. 最终定义 exponent-transport orbit normal form，而不是 descendant-state table。
