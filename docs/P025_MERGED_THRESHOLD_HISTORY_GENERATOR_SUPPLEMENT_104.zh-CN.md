# P025 补充 104 —— Finite History Precision 的 Merged-Threshold Generator

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-history-closure-stage101`  
依赖：P025 补充 102–103  
硬阻断：`NONE`

## 1. second-order tensor 仍可能有更小 generator

Stage102 用

\[
(A;L_i;R_j;C_{ij})
\]

表示 finite-history area responses。

Stage103 又用 Ferrers geometry 压缩 mixed block `C`。

Stage104 发现更强事实：`R_j` 与整列 `C_{*,j}` 本来就由**同一条 scalar threshold order**生成，所以不应视为独立 response coordinates。

## 2. P025-D47 —— labelled merged threshold order

把 existing thresholds

\[
T_1<\cdots<T_s
\]

与 candidate thresholds

\[
U_1<\cdots<U_a
\]

合并成一条 strictly ordered labelled sequence

\[
\boxed{H_1<\cdots<H_{s+a}.}
\]

每个 `H_l` 记录自己来自 old-threshold family 还是 candidate-threshold family，并保留 family index。

对 future node value `v_j` 定义 merged rank

\[
\boxed{Q_j:=\#\{\ell:H_\ell\le v_j\}.}
\]

## 3. P025-T236 —— 一个 merged rank 生成整列 Stage102 future response

在 `v_j` 上 active 的 merged thresholds 恰好就是前 `Q_j` 个 labels。

因此：

- 前 `Q_j` 个中的 **old** labels 数量恰是 `R_j`；
- 其中 **candidate** labels 的集合恰是被 `v_j` 跨过的 candidate thresholds；
- 所以 candidate membership vector 就是完整 corner column `C_{*,j}`。

因此当 labelled merged threshold order 属于 declared schema 时，

\[
\boxed{Q_j\Longleftrightarrow(R_j,C_{*,j})}
\]

精确成立，没有信息损失。

## 4. P025-D48 —— merged history generator signature

保留 Stage100 的 candidate old-block spans

\[
L_i=\#\{r:\rho_r\ge U_i\},
\]

但把 Stage102 的 future tuple `(R_j,C_{*,j})` 替换成 merged ranks `(Q_j)`。

定义

\[
\boxed{
\Gamma
=
\left(
A;
(L_i)_{i=1}^{a};
(Q_j)_{j=1}^{b}
\mid
\text{labelled merged threshold order}
\right).
}
\]

它是 full second-order history response 的 generator representation。

## 5. P025-T237 —— 直接从 generator 计算 history area

设 `I` 是 selected candidate-threshold subset，已经追加 `t` 个 future nodes。

先从

\[
A+\sum_{i\in I}L_i
\]

开始。

对每个 future node `v_j`，查看 merged order 的前 `Q_j` 个 labels：

- old-threshold label 无条件贡献一个 active cell；
- candidate label 仅当其 family index 属于 `I` 时贡献一个 active cell。

对 `j<=t` 求和即得到 exact final area。

所以 `Gamma` 能预测 Stage102 所有 histories，而不需要显式保存 mixed corner matrix。

## 6. 与 expanded second-order signature 精确等价

executable compiler 验证两个方向：

\[
\boxed{
\Gamma
\Longrightarrow
(A;L_i;R_j;C_{ij})
}
\]

通过 labelled-prefix decoding；反向则由

\[
\boxed{
Q_j=R_j+\sum_iC_{ij}
}
\]

恢复。

所以 merged-rank representation 与同一个 finite-history area future language 的 expanded response coordinates 精确等价，但 state 更紧凑。

## 7. P025-T238 —— 自适应 future generator state count

记 old orbit maximum

\[
M:=\rho_h.
\]

假设已有 `q_0` 个 merged thresholds 满足

\[
H_\ell\le M.
\]

它们在所有 future nodes 上都被强制 active。

令

\[
w:=(s+a)-q_0
\]

为 unresolved merged thresholds 数量。

残差 ranks

\[
Q_j-q_0
\]

构成长度 `b` 的 weakly increasing sequence，每项取

\[
0,1,\ldots,w.
\]

因此 compatible future merged-rank states 恰有

\[
\boxed{\binom{w+b}{b}.}
\]

若不利用 monotonicity，则 tuple count 是

\[
(w+1)^b.
\]

若 `w=0`，future generator 完全被强制，state count 为 1。

## 8. 为什么这没有消除 Stage102 的二阶结论

Stage102 说明：若把 endpoint area 看成 independent row/column action selections 的函数，就确实存在 mixed products `x_i y_j`。

Stage104 并没有消掉这些 action interactions。它只是证明：这些 interaction coefficients 全都来自同一条 total-order incidence relation，因此生成这些 responses 的 state 可以更小。

所以必须区分：

- **interaction order**：action-response algebra 的阶数；
- **generator dimension**：产生这些 responses 所需 structured state 的维数。

它们不是一回事。

## 9. Arithmetic realization

executable tests 使用 exact `(q,p)=(3,41)` dyadic pressure tower。对 declared old/candidate threshold 混合集，merged-rank generator 能恢复每个 old-threshold future rank、每个 candidate corner column，以及 expanded Stage102 signature 预测的所有 finite-history areas。

## 10. 架构后果

Stage104 增加一条 minimum-precision principle：

\[
\boxed{
\text{如果 expanded interaction tensor 有低维 ordered generator，就不要保存 tensor 本身。}
}
\]

一个 response 在 action language 中可以是 second-order，但生成它的 state 在更合适 coordinate system 中仍然可能只是 compact first-order rank boundary。

这正是 minimum-precision architecture 必须保留的 response complexity / state complexity 区分。

## 11. Prior-art / novelty 边界

ordered-set merge、labelled ranks 与 Ferrers prefix decoding 都是 elementary/classical constructions。P025 不单独主张这些概念新颖。

项目侧结果是把它们精确用于压缩 arithmetic pressure transport 产生的 Stage102 history-response tensor。历史新颖性仍为 `NOVELTY_UNVERIFIED`。

## 12. 可执行资产

新增：

- `src/enterprise_math/abc_merged_threshold_history.py`；
- `tests/test_abc_merged_threshold_history.py`。

## 13. 下一前沿

Stage105 将把整个 finite-history future 压成 normal form。candidate old-block responses `(L_i)` 本身已经是 monotone crossing staircase，`(Q_j)` 也是 monotone merged-rank staircase。剩余问题是

\[
(A;L_i;Q_j)
\]

是否就是所有 endpoint histories 的 exact compact response normal form，以及 raw action words 如何坍缩为 endpoint classes。