# P025 补充 102 —— Finite Action History 的精确二阶闭合

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-history-closure-stage101`  
依赖：P025 补充 101  
硬阻断：`NONE`

## 1. 从 failure 到 closure

Stage 101 已证明 one-step response signature 不会自动对 two-step history 闭合。缺失信息具有明确结构：mixed threshold/node history 缺一个 corner bit，repeated node history 缺后续 node ranks。

Stage 102 继续问：这条 repair hierarchy 会不会随 history 长度无限增长？

对于有限 threshold/node extension envelope，答案是 **不会**。scalar activation-area future 精确地在 interaction order two 闭合。

## 2. 有限 extension envelope

当前 state 有 ordered thresholds

\[
T_1<\cdots<T_s
\]

与 nondecreasing orbit prefix

\[
\rho_0\le\cdots\le\rho_h.
\]

candidate new threshold rows 为

\[
U_1<\cdots<U_a,
\]

预先给定 future node prefix

\[
v_1\le\cdots\le v_b,
\qquad v_1\ge\rho_h.
\]

一个 executable history 可以按任意顺序插入 candidate thresholds 的任意子集，并依次追加 future nodes 的某个 prefix `v_1,...,v_t`。

定义 current area

\[
A:=\#\{(k,j):\rho_j\ge T_k\}.
\]

每个 candidate threshold 的 old-block span 为

\[
L_i:=\#\{0\le j\le h:\rho_j\ge U_i\}.
\]

每个 future node 对 old thresholds 的 rank 为

\[
R_j:=\#\{1\le k\le s:v_j\ge T_k\}.
\]

最后定义 prospective mixed corner block

\[
\boxed{C_{ij}:=\mathbf1_{\{v_j\ge U_i\}}.}
\]

## 3. P025-T231 —— 精确 finite-history area formula

对任意 selected threshold subset `I subset {1,...,a}` 与任意 future prefix length `0<=t<=b`，最终 activation area 都满足

\[
\boxed{
A(I,t)
=
A
+\sum_{i\in I}L_i
+\sum_{j=1}^{t}R_j
+\sum_{i\in I}\sum_{j=1}^{t}C_{ij}.
}
\]

### 证明

最终 active cells 精确分成四个互不相交的 blocks：

1. old thresholds × old nodes —— 贡献 `A`；
2. selected new thresholds × old nodes —— 贡献 `sum L_i`；
3. old thresholds × new node prefix —— 贡献 `sum R_j`；
4. selected new thresholds × new node prefix —— 贡献 `sum C_ij`。

四块不相交并覆盖最终 matrix，因此不存在任何剩余 correction term。

所以公式对所有允许的 histories 都精确成立，并且与这些 row/node actions 的 interleaving order 无关。

## 4. P025-D45 —— second-order history signature

定义

\[
\boxed{
\Sigma^{(2)}
=
\left(
A;
(L_i)_{i=1}^{a};
(R_j)_{j=1}^{b};
(C_{ij})_{1\le i\le a,1\le j\le b}
\right).
}
\]

P025-T231 表明 `Sigma^(2)` 对 declared extension envelope 内**所有 finite area histories** 都 sufficient。

因此 Stage101 的 pairwise repairs 不会继续膨胀成无界 tower。

## 5. P025-T232 —— response coordinates 可以从 histories 反向恢复

这个 signature 不只是方便的 sufficient cache。它的每个坐标都能从 future response language 中读回。

对 threshold row `U_i`，

\[
\boxed{L_i=A(\{i\},0)-A.}
\]

对第 `j` 个 future node increment，

\[
\boxed{R_j=A(\varnothing,j)-A(\varnothing,j-1).}
\]

mixed corner 为

\[
\boxed{
C_{ij}
=
\big(A(\{i\},j)-A(\{i\},j-1)\big)
-
\big(A(\varnothing,j)-A(\varnothing,j-1)\big).
}
\]

因此 declared history-area responses 能确定 `Sigma^(2)` 的每一个坐标。

相对于这个 future language，`Sigma^(2)` 是 exact response coordinate system，而不是隐藏 surplus structure。

## 6. P025-T233 —— degree-two multilinear envelope

引入独立 Boolean row/column selection variables

\[
x_i,y_j\in\{0,1\}.
\]

area response 的 algebraic extension 为

\[
\boxed{
A(x,y)
=
A
+\sum_iL_ix_i
+\sum_jR_jy_j
+\sum_{i,j}C_{ij}x_iy_j.
}
\]

这个 polynomial 的 degree 至多为二。

所以所有三阶及以上 irreducible Boolean interaction coefficient 恒等于零。

物理可执行的 node histories 只是这个 algebraic envelope 中受 prefix constraint 的子族，因此同一组 second-order data 也足以预测它们。

## 7. Stage102 的严格边界

它**确实**证明：

\[
\boxed{
\text{finite row/column area history}
\Longrightarrow
\text{exact second-order closure}.
}
\]

但它**没有**宣称所有 dynamical systems 都具有 second-order history closure。这里依赖的关键事实是 incidence-area observable 是 row/column extension 新增 cells 的 additive count。

它也没有宣称 raw `a x b` corner matrix 已经是最小 storage representation。monotonicity 还会对这块 matrix 加上额外结构；Stage103 将继续压缩。

## 8. Arithmetic realization

executable tests 使用 `(q,p)=(3,41)` 的 dyadic pressure orbit 作为 arithmetic instantiation：取前部 orbit 作为 current state、后续 exact dyadic nodes 作为 future prefix。对所有 candidate-threshold subsets 与所有合法 future-node prefixes 做 exhaust 后，都与 second-order formula 完全一致。

这样 architecture theorem 保持 generic，同时仍有 exact P025 arithmetic pressure test。

## 9. 架构后果

Stage102 给出一条清晰 hierarchy：

- one-step language -> first-order response coordinates；
- two-step counterexample -> mixed interaction 确实必要；
- full finite extension-history language -> first + second order 已 sufficient；
- 对这个 observable 不需要 third-order repair。

这比保存整个 action history 强得多。正确 state 是一个 finite response jet，而所需 jet order 由 observable 的 extension algebra 决定。

## 10. Prior-art / novelty 边界

bilinear incidence counts、Boolean multilinear polynomials、finite differences 与 interaction decompositions 都是 classical/general ideas。P025 不单独主张这些概念新颖。

项目侧贡献是从 one-step quotient failure 到 proved finite-history closure order 的 exact pressure-test route，并提供 arithmetic counterexamples 与 executable recovery formulas。历史新颖性仍为 `NOVELTY_UNVERIFIED`。

## 11. 可执行资产

新增：

- `src/enterprise_math/abc_finite_history_closure.py`；
- `tests/test_abc_finite_history_closure.py`。

## 12. 下一前沿

mixed corner block `C` 不是任意 Boolean matrix。candidate thresholds 单调增加、future node values 单调增加，因此 `C` 自身也是 Ferrers matrix。Stage103 将把 raw `a*b` bits 压成 monotone boundary，并精确计算 interaction-state count。