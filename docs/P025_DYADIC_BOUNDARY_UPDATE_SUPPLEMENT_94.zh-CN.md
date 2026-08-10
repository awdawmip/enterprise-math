# P025 补充 94 —— 双轴局部更新与 Representation Tradeoff

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-orbit-normal-stage91`  
依赖：P025 补充 92–93  
硬阻断：`NONE`

## 1. 等价坐标不代表 update cost 等价

Stage 93 给出同一个 finite activation state 的三种 exact representations：

1. threshold-centric crossing depths `(j_k)`；
2. orbit-centric node ranks `(r_j)`；
3. monotone `H/V` Ferrers boundary word。

它们彼此 bijective，因此 semantic information 完全相同。但 precision system 不只读取 state，还会继续扩展 threshold grid 与 orbit horizon。

Stage 94 研究这两个 extension directions 下的 exact mutation cost。

## 2. P025-T220 —— 新增一个 threshold 对 crossing coordinates 是局部的

固定已有 threshold grid，并在有序位置插入一个 new threshold `T`。

它只新增一个 first crossing depth

\[
\boxed{j_T\in\{0,\ldots,h,\infty\}.}
\]

所有旧 thresholds 的 crossing depths 完全不变。因此 crossing representation 只需插入这个新 coordinate。

按 dense-coordinate write count，

\[
\boxed{W_{\rm cross}^{(T)}=1.}
\]

## 3. P025-T221 —— 同一个 threshold 可能重写一整个 rank suffix

对每个已有 orbit node `j`，new threshold 恰在

\[
\rho_j\ge T
\]

时让 `r_j` 增加 1。

若 `j_T` 有限，则受影响的是 suffix

\[
j_T,j_T+1,\ldots,h.
\]

所以 changed old rank coordinates 的 exact 数量为

\[
\boxed{
W_{\rm rank}^{(T)}
=
\begin{cases}h+1-j_T,&j_T<\infty,\\0,&j_T=\infty.
\end{cases}}
\]

因此 threshold extension 在 crossing representation 中 one-coordinate-local，却可能在 rank representation 中全局分布。

## 4. P025-T222 —— 新增一个 orbit node 对 rank coordinates 是局部的

把 dyadic horizon 延长一个新 node `h+1`。

所有旧 node ranks 都不变；rank representation 只需追加

\[
\boxed{r_{h+1}.}
\]

因此任意 one-node orbit extension 都有

\[
\boxed{W_{\rm rank}^{(j)}=1.}
\]

## 5. P025-T223 —— 同一个 orbit node 可能一次解开多个 infinite crossings

此前已经 reached 的 thresholds 保持原 finite crossing depth 不变。

此前记为

\[
j_k=\infty
\]

的 threshold，若新 node 首次达到它，则变成

\[
\boxed{j_k=h+1.}
\]

若旧 final rank 为 `r_h`，新 rank 为 `r_{h+1}`，恰有

\[
\boxed{r_{h+1}-r_h}
\]

个原来的 infinite crossing coordinates 变为 finite。

因此

\[
\boxed{W_{\rm cross}^{(j)}=r_{h+1}-r_h.}
\]

该量可以是 0、1，也可以很多。

## 6. P025-T224 —— Ferrers boundary 在两个 axes 上都只需单符号更新

boundary word 每个 threshold 对应一个 `V` step，每个 orbit node 对应一个 `H` step。

新增一个 threshold，只需在 crossing location 插入一个

\[
\boxed{V}
\]

step；删掉这个新 `V` 就精确恢复旧 boundary word。

新增一个 orbit node，只需在 rank location 插入一个

\[
\boxed{H}
\]

step；删掉这个新 `H` 就精确恢复旧 boundary word。

因此

\[
\boxed{
\text{threshold extension}=\text{one V insertion},
\qquad
\text{orbit extension}=\text{one H insertion}.
}
\]

Ferrers boundary 因而是 biaxially local update representation。

## 7. Exact threshold-extension fixture

从 Stage 93 state 开始：

\[
(j_k)=(0,1,2,\infty),
\qquad
(r_j)=(1,2,3,3),
\]

boundary word 为

\[
\texttt{VHVHVHHV}.
\]

插入 threshold

\[
T=10.
\]

在同一 arithmetic orbit 上它于 depth 2 crossing，所以 new state 为

\[
\boxed{(j_k')=(0,1,2,2,\infty),}
\]

以及

\[
\boxed{(r_j')=(1,2,4,4).}
\]

因此：

- crossing coordinate writes：`1`；
- rank coordinate rewrites：`2`；
- boundary update：
  \[
  \boxed{
  \texttt{VHVHVHHV}\to\texttt{VHVHVVHHV},
  }
  \]
  恰好插入一个 `V`。

## 8. 一个 threshold 可以重写所有旧 ranks

在同一 four-node orbit 上，从 thresholds

\[
\frac12,1,11
\]

开始，再插入

\[
T=\frac1{100}.
\]

new threshold 在 depth 0 已经 reached，所以所有已有 node ranks 都增加。

因此

\[
\boxed{W_{\rm cross}^{(T)}=1,\qquad W_{\rm rank}^{(T)}=4.}
\]

这说明 update-cost gap 可以随 orbit horizon 线性增长。

## 9. Exact orbit-extension fixture

取

\[
(q,p,m)=(7,17,2).
\]

exponent 2 时

\[
\rho_{2,-}=\frac16.
\]

exponent 4 时 Stage 86 给出

\[
\rho_{4,-}=\frac{13}{6}.
\]

在 horizon 0 上选 thresholds

\[
\frac12,1,2.
\]

起初三个都未 reached：

\[
(j_k)=(\infty,\infty,\infty),
\qquad
(r_0)=(0).
\]

追加 exponent-four node 后，三个 thresholds 同时首次达到：

\[
\boxed{(j_k')=(1,1,1),}
\]

以及

\[
\boxed{(r_j')=(0,3).}
\]

因此：

- crossing rewrites：`3`；
- rank writes：`1`；
- boundary word：
  \[
  \boxed{\texttt{HVVV}\to\texttt{HVVVH},}
  \]
  恰好插入一个 `H`。

这与 threshold-extension fixture 完全镜像。

## 10. P025-C32 —— crossing / rank 没有谁 globally dominates updates

threshold extensions 偏向 crossing coordinates：

\[
W_{\rm cross}^{(T)}=1,
\]

而 rank rewrites 可以随 `h` 增长。

orbit extensions 偏向 rank coordinates：

\[
W_{\rm rank}^{(j)}=1,
\]

而 crossing rewrites 可以随 `s` 增长。

所以两种 dual coordinates 都不可能在两个 extension axes 上同时 globally update-optimal。

这是一个明确 negative boundary：semantic completeness 不能推出 operational optimality。

## 11. Boundary word 用 storage 换 symmetric locality

三种 representations 的长度不同：

- crossing vector：`s`；
- rank vector：`h+1`；
- boundary word：`s+h+1` 个 symbols。

所以 Ferrers path 并不自动具有最小 storage。

它的优势是另一条：

\[
\boxed{\text{两个 extension axes 都变成 one-symbol local edit}.}
\]

因此 representation choice 落在 storage / update-locality tradeoff 上，而不是一个单一 total order 中。

## 12. P025-D39 —— axis-relative coordinate policy

若 workload 主要不断加密 threshold grid，crossing coordinates 自然 local。

若 workload 主要不断延长 orbit horizon，node ranks 自然 local。

若 workload 需要两个 axes 都频繁 mutation，boundary word 提供 symmetric one-symbol updates。

于是得到 representation policy：

\[
\boxed{\text{坐标选择应相对于 future extension language，而不是全局固定}.}
\]

## 13. 与 Stage 90 的关系

Stage 90 说明 future query 决定哪些 observables 与 observation order sufficient。

Stage 94 再增加一层：

> 在 sufficient semantic state 已经确定之后，预期的 **future extension direction** 还会决定哪套等价 coordinate chart 更 local。

所以 future-relative precision 至少有两层：

1. 需要哪个 semantic quotient；
2. 哪个 coordinate chart 最适合 future operations 对该 quotient 的继续作用。

## 14. Prior-art / novelty 边界

sparse updates、dual coordinates、lattice-path insertion 与 storage/update tradeoff 都是 broad prior concepts。

P025 不单独主张这些 notions 新颖。

项目侧结果只是 exact arithmetic Ferrers-state update law 以及它作为 coordinate-choice semantics pressure test 的使用。历史新颖性仍为 `NOVELTY_UNVERIFIED`。

## 15. 可执行资产

新增：

- `src/enterprise_math/abc_dyadic_boundary_update.py`；
- `tests/test_abc_dyadic_boundary_update.py`。

executable layer 验证 exact threshold/rank write counts、one-symbol `V/H` insertion、distributed threshold updates、multi-threshold orbit crossings，以及 symmetric path-update law。

## 16. 下一前沿

不存在硬阻断。继续：

1. 证明 threshold / orbit extension diamond commute；
2. 证明 final boundary 与 extension order 无关；
3. 把三种 representations 表述成 Pareto family，而不是一个 preferred state；
4. 在不硬编码任意 costs 的前提下给 mixed workload 推导 cost envelope；
5. 然后把 semantic-state / coordinate-chart distinction Relay 回 P023/A2。
