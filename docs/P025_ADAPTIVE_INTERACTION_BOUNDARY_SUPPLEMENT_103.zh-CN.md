# P025 补充 103 —— Mixed History Interaction 的自适应 Ferrers Boundary

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-history-closure-stage101`  
依赖：P025 补充 102  
硬阻断：`NONE`

## 1. raw second-order storage 仍然过精

Stage 102 已用 mixed corner block

\[
C_{ij}=\mathbf1_{\{v_j\ge U_i\}}
\]

证明 exact finite-history closure。

若直接保存，看上去 `a` 个 candidate thresholds 与 `b` 个 future nodes 需要 `a*b` 个 Boolean coordinates。

Stage103 证明其中大量 bits 要么被强制，要么是 Ferrers-redundant。

## 2. P025-T234 —— resolved threshold rows 强制全部 mixed corners

记 old orbit maximum 为

\[
M:=\rho_h.
\]

candidate threshold `U_i` 的 old-block span 满足

\[
L_i>0
\iff
U_i\le M.
\]

所有 future nodes 又满足

\[
v_j\ge M.
\]

因此

\[
\boxed{
L_i>0
\Longrightarrow
C_{ij}=1\quad\forall j.
}
\]

所以已经被 old horizon resolved 的 candidate threshold 不产生任何新的 mixed uncertainty。

只有

\[
\boxed{U_i>M}
\]

的 thresholds 才可能携带非平凡 second-order information。

由于 candidate thresholds 有序，这些 unresolved thresholds 自动形成一个 suffix。

## 3. P025-D46 —— unresolved interaction block

令

\[
u:=\#\{i:U_i>M\}
\]

为 unresolved candidate thresholds 数量。

删去 forced all-one 的 resolved rows，只保留 `u x b` unresolved block。

对每个 unresolved threshold 定义 future crossing depth

\[
\kappa_i:=\min\{j:v_j\ge U_i\},
\]

若整个 future prefix 都未达到，则记为 `infinity`。

因为 unresolved thresholds 单调增加，

\[
\boxed{
\kappa_1\le\kappa_2\le\cdots\le\kappa_u.
}
\]

因此整个 unresolved interaction block 可由一条 monotone crossing vector 精确重建。

## 4. 对偶 future-rank coordinates

对每个 future node 定义它在 unresolved candidate thresholds 中的 rank：

\[
q_j:=\#\{i:U_i>M,\ v_j\ge U_i\}.
\]

由于 future values nondecreasing，

\[
\boxed{q_1\le q_2\le\cdots\le q_b.}
\]

两套坐标精确对偶：

\[
q_j=\#\{i:\kappa_i\le j\},
\]

\[
\kappa_i=\min\{j:q_j\ge i\}.
\]

所以 mixed second-order response 再次出现 Stages92–94 的 Ferrers geometry，只不过这次被局部化到**尚未 resolved 的 prospective block**。

## 5. P025-T235 —— 精确 interaction-state count

任意 `u x b` Boolean block 有

\[
2^{ub}
\]

种状态。

Ferrers block 由长度 `u` 的 weakly increasing crossing vector 决定，每项取

\[
0,1,\ldots,b-1,\infty.
\]

因此 compatible mixed interaction states 恰为

\[
\boxed{
\binom{u+b}{u}.
}
\]

当 `u=b=4` 时，

\[
\boxed{70}
\]

替代

\[
\boxed{65536}.
\]

## 6. 退化回 first order

若

\[
u=0,
\]

则所有 candidate thresholds 都已被 old orbit maximum 跨过，整个 mixed block 被强制为全 1，因此

\[
\boxed{\#\text{compatible mixed states}=1.}
\]

此时不需要任何真正新的 second-order precision。

因此“history closure 为二阶”只是 worst-case structural statement；某个具体 state 上实际生成的 precision 仍可退化回 first order。

## 7. Stage101 是最小特例

当只有一个 unresolved threshold 与一个 future node（`u=b=1`）时，compatible interaction states 就是

\[
\boxed{C_{U,v}\in\{0,1\}.}
\]

这正是 Stage101 分离出来的 mixed corner bit。

所以 Stage101 不是孤立 counterexample，而是 Stage103 Ferrers interaction geometry 的最小 cell。

## 8. Arithmetic fixture

对 `(q,p)=(3,41)` dyadic pressure orbit，取到 exponent `4` 的 old prefix：

\[
M=\rho_{4,-}=\frac{13}{22}.
\]

candidate thresholds 取

\[
\frac1{20},\frac12,1,5,11.
\]

只有前两个已被 old horizon resolved，unresolved suffix 为

\[
1,5,11.
\]

后两个 exact dyadic pressures 都是

\[
\frac{221}{22}.
\]

因此 unresolved crossing depths 为

\[
\boxed{(0,0,\infty)},
\]

future unresolved ranks 为

\[
\boxed{(2,2).}
\]

full mixed block 可由任一表示精确重建。

## 9. 架构后果

Stage103 给出 adaptive precision-genesis rule：

\[
\boxed{
\text{second-order state is born only on unresolved future distinctions.}
}
\]

response order 由 operation algebra 决定，但实际需要多少 second-order information，则由 current state 相对于 declared future horizon 的位置决定。

必须区分：

- future language 所需的最大 interaction order；
- current state 上实际生成的 precision dimension。

## 10. Prior-art / novelty 边界

Ferrers matrices、lattice paths 与 monotone rank/crossing duality 都是 classical combinatorics。P025 不单独主张这些概念新颖。

项目侧结果是把 Stage102 exact history interaction block 自适应局部化到 unresolved arithmetic precision，并给出 executable pressure fixtures。历史新颖性仍为 `NOVELTY_UNVERIFIED`。

## 11. 可执行资产

新增：

- `src/enterprise_math/abc_history_interaction_boundary.py`；
- `tests/test_abc_history_interaction_boundary.py`。

## 12. 下一前沿

剩余 first-order node data `(R_j)` 也构成 monotone staircase。Stage104 将尝试把：

1. candidate-threshold old spans；
2. future-node old ranks；
3. unresolved mixed Ferrers boundary；

压成一个更小的 history-response atlas，并检查哪些坐标实际上由共同的 total-order generator 强制生成。