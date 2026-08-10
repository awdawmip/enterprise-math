# P025 补充 99 —— Activation Potential 的 Action-Relative 双重 Repair

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-orbit-normal-stage91`  
依赖：P025 补充 96–98  
硬阻断：`NONE`

## 1. Threshold action 修复了一个 directional failure

Stage 98 已证明 scalar activation area

\[
A
\]

在 declared threshold insertion 下并不 future-safe。

对该 action，exact one-step repair 是 new threshold crossing depth

\[
j_T,
\]

或等价的 directional increment

\[
\Delta_TA.
\]

Stage 99 研究 Stage 94 另一个 primitive extension —— 追加一个 dyadic orbit node —— 的完全对偶 statement。

## 2. 复用同一个 equal-area fiber

继续使用 Stages 97–98 的 current grid

\[
\left(\frac12,1\right)
\]

与 horizon `h=1`。

两个 exact states 仍满足

\[
\boxed{A^{\rm flat}=A^{\rm jump}=2.}
\]

### Flat state

\[
(q,p)=(3,5),
\qquad
(\rho_0,\rho_1)=\left(\frac12,\frac12\right).
\]

### Jump state

\[
(q,p)=(7,17),
\qquad
(\rho_0,\rho_1)=\left(\frac16,\frac{13}{6}\right).
\]

## 3. 对两者施加同一个 orbit-extension action

分别追加一个 new dyadic difference node。

对 flat orbit，next tested pressure 仍停在 low-threshold level，因此 new node 只达到两个 old thresholds 中的一个。它的 rank 是

\[
\boxed{r_{\rm new}^{\rm flat}=1.}
\]

由 Stage 96，

\[
\boxed{A_{\rm next}^{\rm flat}=2+1=3.}
\]

对 jump orbit，Stage 86 monotonicity 已给出

\[
\rho_{\rm new}\ge\frac{13}{6}>1.
\]

所以两个 old thresholds 都 reached：

\[
\boxed{r_{\rm new}^{\rm jump}=2,}
\]

并有

\[
\boxed{A_{\rm next}^{\rm jump}=2+2=4.}
\]

## 4. P025-C39 —— area 在 orbit extension 下同样不 future-safe

两个 current states 位于同一 area fiber

\[
A=2,
\]

但同一个 orbit-node extension 产生

\[
\boxed{3\ne4.}
\]

因此 scalar quotient

\[
q_A(B)=A(B)
\]

对 future map

\[
F_J(B):=A(E_J(B))
\]

同样违反 P023 fiber constancy，其中 `E_J` 表示追加一个 dyadic orbit node。

所以

\[
\boxed{\text{activation area 在两个 primitive extension axes 上都不是 Markov state}.}
\]

## 5. P025-T240 —— 用 new node rank 做 exact orbit-action repair

Stage 96 给出 exact orbit-axis derivative

\[
\Delta_JA=r_{\rm new}.
\]

因此

\[
\boxed{A_{\rm next}=A+r_{\rm new}.}
\]

所以 exact one-step natural repair 是

\[
\boxed{(A,r_{\rm new}).}
\]

这正是 Stage 98

\[
(A,j_T)
\]

的 orbit-axis dual。

## 6. P025-T241 —— threshold 与 orbit repairs 就是 directional derivatives

对 threshold insertion，

\[
\boxed{\text{repair coordinate}=j_T\leftrightarrow\Delta_TA.}
\]

对 orbit-node append，

\[
\boxed{\text{repair coordinate}=r_{\rm new}=\Delta_JA.}
\]

所以两个 one-step repairs 恰好是 Stage 96 scalar potential 的两条 directional first derivatives。

得到 dictionary：

\[
\boxed{
\begin{array}{c|c|c}
\text{declared action}&\text{natural response coordinate}&\text{area increment}\\ \hline
+T&j_T&h+1-j_T\text{ or }0\\
+J&r_{\rm new}&r_{\rm new}
\end{array}}
\]

## 7. P025-D42 —— action-relative repair compiler

定义 one-step repair compiler，其 input 为：

1. current coarse scalar area；
2. declared future action；
3. action 需要时的 parameter。

然后：

- action 为 threshold insertion `+T`：揭示 crossing depth `j_T`；
- action 为 orbit append `+J`：揭示 new node rank `r_new`。

repaired future area 可由所选 directional coordinate 精确重建。

因此 compiler 为

\[
\boxed{\text{action}\longmapsto\text{directional response coordinate}.}
\]

只声明一个 action 时，它不会无条件索取两个 coordinates。

## 8. P025-T242 —— repair vocabulary 本身就是 action-relative

两种 repairs 并不只是 numerical value 不同，而是属于不同 coordinate vocabularies：

- `j_T` 是 threshold-centric，并由 future threshold 索引；
- `r_new` 是 orbit-centric，并由 future node 索引。

因此 action 改变时，required additional precision 的**类型**本身都可能改变。

这比“一个 action 需要更多 precision，另一个更少”更强。

正确 statement 是

\[
\boxed{\text{future action 可以改变 repair coordinate family 本身}.}
\]

## 9. 一个 coarse state，两种 exact repairs

对 current area 为 `2` 的 jump state：

### Threshold action

插入

\[
T=\frac34.
\]

则

\[
j_T=1,
\qquad
\Delta_TA=1,
\]

所以

\[
A_{\rm next}=3.
\]

### Orbit action

追加一个 new node，则

\[
r_{\rm new}=2,
\qquad
\Delta_JA=2,
\]

所以

\[
A_{\rm next}=4.
\]

同一个 current scalar state 在不同 action languages 下会要求不同 repair coordinates。

## 10. P025-C40 —— 这里没有依据声称存在 action-independent one-coordinate repair

Stages 98–99 只证明了**在 action 已声明之后**的 exact one-coordinate repairs。

它们没有证明存在一个 universal scalar repair coordinate 能同时对两个 primitive action families 都 optimal。

任何更强 compression 都需要单独 factorization theorem。

因此安全的架构结论是 action-relative selection，而不是创造一个 universal coordinate。

## 11. 与 P023 operation families 的关系

P023 研究 future-compatible operation families，而不只是一个 map。

Stages 98–99 给出最小的非平凡 arithmetic example：

- 一个 coarse state 对两个不同 actions 都 unsafe；
- 每个 action 都有简单 one-step repair；
- 两种 repairs 是一个 potential 的不同 directional coordinates。

若 declared operation family 同时包含两个 actions，下一问题就是：需要 repair pair，还是应回到更丰富 boundary chart？

这个问题留给下一 stage，而不静默假定答案。

## 12. 与 P024 action-language precision 的关系

P024 的核心关切是 precision requirement 依赖 action language。

Stage 99 给出 exact number-theoretic witness：

\[
\boxed{
\text{same coarse state}
+
\text{different action}
\Longrightarrow
\text{different repair coordinate type}.
}
\]

这是一个直接 Relay candidate。

## 13. Prior-art / novelty 边界

directional derivatives、action-dependent state augmentation 与 response coordinates 都是 broad prior concepts。

P025 不单独主张这些概念新颖。

项目侧结果只是 Ferrers activation potential 诱导出的 exact arithmetic dual-repair compiler。历史新颖性仍为 `NOVELTY_UNVERIFIED`。

## 14. 可执行资产

新增：

- `src/enterprise_math/abc_activation_area_action_repair.py`；
- `tests/test_abc_activation_area_action_repair.py`。

executable layer 验证 orbit-side future collision、new-rank repair、threshold/orbit action compiler、directional increments 与 action contract errors。

## 15. 下一前沿

不存在硬阻断。继续从单 action 提升到有限 **operation family**：

1. 声明有限 candidate threshold insertions 与一个 orbit append；
2. 推导能预测 family 中每个 action next area 的 natural response signature；
3. 利用 threshold ordering 把 threshold-response vector 再压成 staircase；
4. 比较 family-safe state 与 full Ferrers boundary；
5. 据此确定最适合 Relay 到 P023/P024/A2 的 common abstraction。
