# P025 补充 108 —— Quadratic Rank Energy 的 Cubic History Closure

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-nonlinear-observable-stage107`  
依赖：P025 补充 102、107  
硬阻断：`NONE`

## 1. Stage102 的 closure order 不是通则

Stage102 已证明**线性 activation-area observable** 在 second action-interaction order 闭合。

Stage108 保持完全相同的 threshold/node operation algebra 与 incidence geometry，只把 observable 换成

\[
E=\sum_jr_j^2.
\]

response order 随即提高。

## 2. 有限 extension envelope

设 current thresholds 为 `T_k`，current node values 为 `rho_c`，candidate thresholds 为 `U_i`，prospective future nodes 为 `v_j`。

current column ranks 定义为

\[
r_c:=\#\{k:\rho_c\ge T_k\}.
\]

对 candidate threshold `U_i`，定义 old-column incidence

\[
a_{ic}:=\mathbf1_{\{\rho_c\ge U_i\}}.
\]

对 future node `v_j`，定义

\[
R_j:=\#\{k:v_j\ge T_k\},
\qquad
C_{ij}:=\mathbf1_{\{v_j\ge U_i\}}.
\]

令 `x_i,y_j` 分别表示 candidate rows 与 future columns 的 independent Boolean selections。

## 3. P025-T246 —— exact degree-three response polynomial

quadratic-energy response 精确为

\[
E(x,y)
=
\sum_c\left(r_c+\sum_i x_i a_{ic}\right)^2
+
\sum_j y_j\left(R_j+\sum_i x_iC_{ij}\right)^2.
\]

利用 `x_i^2=x_i` 展开得

\[
\boxed{
\begin{aligned}
E(x,y)=E_0
&+\sum_iD_ix_i
+\sum_{i<k}P_{ik}x_ix_k\\
&+\sum_jN_jy_j
+\sum_{i,j}M_{ij}x_iy_j\\
&+\sum_{i<k,j}K_{ikj}x_ix_ky_j,
\end{aligned}}
\]

其中

\[
D_i=2\sum_cr_ca_{ic}+\sum_ca_{ic},
\]

\[
P_{ik}=2\sum_ca_{ic}a_{kc},
\]

\[
N_j=R_j^2,
\]

\[
M_{ij}=C_{ij}(2R_j+1),
\]

以及

\[
\boxed{K_{ikj}=2C_{ij}C_{kj}.}
\]

因此 response polynomial 的 degree 至多为三。

## 4. P025-CE43 —— exact arithmetic 非零 cubic interaction

使用 exact dyadic pressure orbit `(q,p,m)=(3,41,2)` 的一次 doubling：

\[
\rho_0=\frac1{22},
\qquad
\rho_1=\frac{13}{22}.
\]

不设 old thresholds，取两个 candidate thresholds

\[
U_1=\frac1{10},
\qquad
U_2=\frac12.
\]

old node 位于两个 candidates 下方，future node 位于两者上方。

所以

\[
R_1=0,
\qquad
C_{11}=C_{21}=1.
\]

三个 action variables 上的 energy response 精确为

\[
\boxed{
E(x_1,x_2,y)
=y(x_1+x_2)^2
=x_1y+x_2y+2x_1x_2y.
}
\]

因此 irreducible third Boolean difference 为

\[
\boxed{
\Delta_{x_1}\Delta_{x_2}\Delta_yE=2\ne0.
}
\]

真正的 third-order action interaction 确实出现。

## 5. P025-T247 —— exact closure order 为三

P025-CE43 证明 second order 一般不足。

P025-T246 又证明 degree 永远不超过三。

所以

\[
\boxed{
\text{quadratic rank energy 的 worst-case history interaction order 精确为 }3.
}
\]

所有四阶及以上 irreducible Boolean finite differences 恒为零。

## 6. cubic term 为什么出现

future node 的贡献是其**最终** threshold rank 的平方。

若两个 candidate thresholds 都被选择，并且 future node 同时跨过两者，那么它们在

\[
(R_j+x_i+x_k)^2
\]

中发生乘积。

这个 threshold-pair interaction 又被 future-column selection variable `y_j` gated，于是产生 cubic `x_ix_ky_j` term。

线性 area 中每个 active cell 独立贡献，因此没有这一机制。

## 7. observable degree 与 response order 的初步规律

在这个 incidence model 中：

- linear rank observable `r` 在 future-column gating 后至多给 second-order row/column interaction；
- quadratic rank observable `r^2` 至多给 third-order interaction。

Stage108 暂不把它提升成任意 degree 的 theorem，但出现了非常明确的候选规律：

\[
\boxed{
\text{rank polynomial degree }d
\quad\leadsto\quad
\text{history interaction order 至多 }d+1.
}
\]

## 8. 架构后果

所需 response-jet order 不是 operation family 单独决定的。

同一个 `{threshold insertion, node append}` operation algebra：

- activation area 需要 order `2`；
- quadratic rank energy 需要 order `3`。

所以 minimum future precision 的独立决定因素还包括

\[
\boxed{\text{observable algebra}.}
\]

## 9. Prior-art / novelty 边界

Boolean polynomial expansion、finite differences 与 quadratic cross terms 都是 classical mathematics。P025 不单独主张这些概念新颖。

项目侧结果是 exact arithmetic pressure-test：只改变 observable、保持 operation algebra 不变，就能改变 history-closure order。历史新颖性仍为 `NOVELTY_UNVERIFIED`。

## 10. 可执行资产

新增：

- `src/enterprise_math/abc_quadratic_history_closure.py`；
- `tests/test_abc_quadratic_history_closure.py`。

## 11. 下一前沿

Stage109 将再次区分 response order 与 generator-state complexity：虽然 energy response 是 cubic，threshold incidences 仍嵌在同一条 total order 上。要检验能否用 compact generator 生成完整 cubic jet，而不保存所有 cubic coefficients。