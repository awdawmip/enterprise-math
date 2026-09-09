# \(P_{46}\) 的双素数 Frobenius 场交证书

Status: `FREE_RESEARCH / EXACT_ENDOMORPHISM_CERTIFICATE_PROTOCOL / THEOREM_ONLY_IF_VALIDATOR_PASSES / NOT_AXIOM / NOT_FOUNDATION`

Date: `2026-09-04`

Researcher: `EM-FREE-F6D046 / FREE_AXIOM_DISCOVERY`

Research unit: `EM-FREE-F6D046-R19-P46-ENDOMORPHISM-FIELD-INTERSECTION`

## 1. 目标

在 R18 的显式模型中，已有

\[
\mathbf Q(i)\subseteq\operatorname{End}^0_{\bar{\mathbf Q}}(P_{46}).
\]

本证书协议的目标是判定该包含是否严格。它不依靠浮点 period matrix，而使用两个 split good primes 的完整 Frobenius 场。

## 2. 单个 split prime 给出的约束

设 \(p\equiv1\pmod4\) 是好素数，并满足：

1. \(P_{46,p}\) ordinary；
2. degree-8 Frobenius 多项式 \(f_p\) 在 \(\mathbf Q\) 上不可约；
3. 不同 Frobenius 共轭根之比均不是单位根。

则该约化在 \(\overline{\mathbf F}_p\) 上绝对单纯。ordinary simple 情形下，其几何 endomorphism algebra 是 CM Frobenius 场

\[
F_p=\mathbf Q(\pi_p),\qquad [F_p:\mathbf Q]=8.
\]

因 \(p\equiv1\pmod4\)，order-4 deck endomorphism 已在 \(\mathbf F_p\) 上定义并与 Frobenius 对易，所以

\[
K=\mathbf Q(i)\subset F_p,
\qquad [F_p:K]=4.
\]

好约化 specialization 给出

\[
D:=\operatorname{End}^0_{\bar{\mathbf Q}}(P_{46})\hookrightarrow F_p.
\]

特别地，\(D\) 必为交换数域，且

\[
K\subseteq D\subseteq F_p.
\]

## 3. 排除中间二次域

把 \(f_p\) 在 \(K[T]\) 上分解为一对共轭不可约四次式 \(g_p,\bar g_p\)。

对首一四次式

\[
g=X^4+aX^3+bX^2+cX+d
\]

取 cubic resolvent

\[
R_g(Y)=Y^3-bY^2+(ac-4d)Y+(4bd-a^2d-c^2).
\]

若 \(g\) 与 \(R_g\) 都在 \(K\) 上不可约，则其 Galois 闭包群为 \(S_4\) 或 \(A_4\) 型；根稳定子在相应群中为极大子群，所以四次域 \(K[X]/(g)\) 没有非平凡中间域。

因此任何 \(K\subseteq D\subseteq F_p\) 只有两种可能：

\[
D=K\quad\text{或}\quad D=F_p.
\]

## 4. 两个 prime 排除 \(D=F_p\)

再取另一个满足同样条件的 split good prime \(q\)。对 \(p,q\) 的两个共轭四次因子全部配对。

若两个四次 \(K\)-域同构，则每个未分歧素理想的分裂型必须相同。取一个 \(\ell\equiv1\pmod4\)，固定根

\[
r^2\equiv-1\pmod\ell
\]

以指定 \(K\) 的素理想 \((\ell,i-r)\)，并比较两个四次式模该素理想的不可约因子次数多重集。只要分裂型不同，就得到严格、有限的非同构证书。

必须检查四种 pairing

\[
(g_p,g_q),\ (g_p,\bar g_q),\ (\bar g_p,g_q),\ (\bar g_p,\bar g_q),
\]

以避免把未标记的 \(i/-i\) eigenspace 选择误当作结构。

若四种 pairing 均非同构，且两边四次域均无中间域，则不存在严格大于 \(K\) 的共同 endomorphism field，故

\[
\boxed{
\operatorname{End}^0_{\bar{\mathbf Q}}(P_{46})=\mathbf Q(i).
}
\]

## 5. 防误报边界

只有独立 validator 同时重算并通过以下项目时才允许提升定理：

- 两个 prime 的 good/split/ordinary 条件；
- 两个绝对单纯性单位根比值证书；
- 四个 \(K\)-四次式与 cubic resolvent 的不可约性；
- 四种 \(K\)-结构 pairing 的未分歧分裂型非同构 witness。

单个 prime、单个 quartic factor、一个数值 field-discriminant 近似或仅比较多项式系数均不足。

分类：

`EXACT_ENDOMORPHISM_CERTIFICATE_PROTOCOL / DERIVED_IF_PASSED / NOT_NEW_AXIOM / NOT_FOUNDATION / P000_UNCHANGED`.