# P025 补充 98 —— Activation Area 不是 Extension-Markov State

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-orbit-normal-stage91`  
依赖：P025 补充 96–97  
硬阻断：`NONE`

## 1. Stage 97 已否定 present-state sufficiency

Stage 97 给出两个 exact arithmetic Ferrers states，在相同 threshold grid 与 horizon 上满足

\[
A^{\rm flat}=A^{\rm jump}=2
\]

但 activation matrices 不同。

还剩一个更强的问题：

> 即使 future 只关心 scalar area，本轮 current area 能否自己决定 declared extension 后的 next area？

Stage 98 证明答案仍然是否定的。

## 2. 复用 equal-area fiber

固定 current threshold grid

\[
\boxed{\left(\frac12,1\right)}
\]

与 horizon `h=1`。

两个 exact states 为：

### Flat state

\[
(q,p)=(3,5),
\qquad
(\rho_0,\rho_1)=\left(\frac12,\frac12\right),
\]

且

\[
A=2.
\]

### Jump state

\[
(q,p)=(7,17),
\qquad
(\rho_0,\rho_1)=\left(\frac16,\frac{13}{6}\right),
\]

同样

\[
A=2.
\]

## 3. 对两个 states 施加同一个 future action

插入同一个 new threshold

\[
\boxed{T=\frac34}.
\]

对 flat state，

\[
\rho_0=\rho_1=\frac12<\frac34.
\]

所以 new threshold 在 current horizon 内从未 reached：

\[
\boxed{j_T^{\rm flat}=\infty.}
\]

new row 没有 active cells，因此

\[
\boxed{A_{\rm next}^{\rm flat}=2.}
\]

对 jump state，

\[
\frac16<\frac34<\frac{13}{6},
\]

所以

\[
\boxed{j_T^{\rm jump}=1.}
\]

new row 有一个 active cell，因此

\[
\boxed{A_{\rm next}^{\rm jump}=3.}
\]

## 4. P025-C38 —— equal current area，却有 unequal future area

两个 states 满足

\[
\boxed{A^{\rm flat}=A^{\rm jump}=2,}
\]

但在同一个 declared threshold-insertion action 下，

\[
\boxed{A_{\rm next}^{\rm flat}=2\ne3=A_{\rm next}^{\rm jump}.}
\]

因此不存在函数

\[
G_T
\]

能对这一 exact arithmetic family 普遍满足

\[
A_{\rm next}=G_T(A).
\]

所以

\[
\boxed{\text{current activation area 不是 threshold extension 的 Markov state}.}
\]

## 5. P025-T237 —— area quotient 对该 future 不 composition-safe

定义 scalar area collapse

\[
q_A(B):=A(B).
\]

令 `E_T` 表示“插入 threshold `T=3/4`”，future observation 是 resulting area：

\[
F_T(B):=A(E_T(B)).
\]

Stage 98 pair 满足

\[
q_A(B^{\rm flat})=q_A(B^{\rm jump})
\]

但

\[
F_T(B^{\rm flat})\ne F_T(B^{\rm jump}).
\]

所以 P023 fiber-constancy criterion 失败：

\[
\boxed{F_T\text{ 不能 descend through }q_A.}
\]

这是真正的 composition-safety failure，而不只是 descriptive detail 丢失。

## 6. P025-T238 —— 用 crossing depth 做 exact one-step repair

对一个 declared new threshold `T`，Stage 96 给出

\[
\Delta_TA
=
\begin{cases}h+1-j_T,&j_T<\infty,\\0,&j_T=\infty.
\end{cases}
\]

因此

\[
\boxed{A_{\rm next}=A+\Delta_TA}
\]

由

\[
\boxed{(A,j_T)}
\]

精确决定。

所以只增加一个 crossing coordinate，就能修复 scalar area state 对该 one-step future action 的不安全。

## 7. P025-T239 —— crossing depth 与 area increment 是等价 repairs

固定 horizon `h` 时，

\[
j_T\mapsto\Delta_TA
\]

为

\[
0\mapsto h+1,
\quad
1\mapsto h,
\quad\ldots\quad
h\mapsto1,
\quad
\infty\mapsto0.
\]

这是 bijection。

因此 one-step future 下两种 repaired states 等价：

\[
\boxed{(A,j_T)}
\]

与

\[
\boxed{(A,\Delta_TA).}
\]

P023 generic one-step repair

\[
(A,A_{\rm next})
\]

也等价，因为

\[
A_{\rm next}=A+\Delta_TA.
\]

所以抽象 repair theorem 在这里具体化成了 theorem-native arithmetic response coordinate。

## 8. Collision pair 的 exact repaired states

flat state：

\[
\boxed{(A,j_T)=(2,\infty),}
\]

重建

\[
A_{\rm next}=2.
\]

jump state：

\[
\boxed{(A,j_T)=(2,1),}
\]

重建

\[
A_{\rm next}=3.
\]

新增 coordinate 恰好分离了导致 future incompatibility 的 equal-area fiber。

## 9. Potential 与 dynamic state

Stages 96–98 现在同时建立三件事：

1. `A` 是具有 exact finite-difference laws 的有用 scalar potential；
2. `A` 不能决定 current Ferrers semantic state；
3. `A` 甚至不能决定自己在所有 declared extension actions 下的 next value。

所以

\[
\boxed{\text{potential}\not\Rightarrow\text{dynamic sufficient state}.}
\]

response law 可以很简单，但选择该 response 所需的 state 仍然可能更丰富。

## 10. Action-relative repair

repair coordinate `j_T` 不是 universal metadata，而是被 declared future threshold `T` 索引的。

future action 一变，required repair 也可能变化。

因此正确对象不是

\[
\text{area plus all possible crossing depths},
\]

而应是

\[
\boxed{
\text{current coarse state}
+
\text{minimal response coordinate for the declared action}.
}
\]

这是 exact number-theoretic action-relative precision 实例。

## 11. 与 P023 / P024 的关系

P023 提供 generic logic：

- 检验 fiber constancy；
- 若 unsafe，则增加足够 future information 恢复 factorization。

P024 研究 action-language precision。

Stage 98 在一个 exact arithmetic fixture 中把两者接起来：

- coarse scalar potential 在特定 action 下 fiber constancy 失败；
- action 选择一个 directional coordinate `j_T`；
- 该 coordinate 给出 exact one-step repair。

这里不主张新的 canonical theorem，只是 existing project layers 之间的 research-pressure bridge。

## 12. Prior-art / novelty 边界

Markov sufficiency、state augmentation 与 one-step repairs 都是 broad prior concepts。

P025 不单独主张这些概念新颖。

项目侧结果只是 exact arithmetic future collision，以及 Ferrers precision geometry 给出的 explicit crossing-depth repair。历史新颖性仍为 `NOVELTY_UNVERIFIED`。

## 13. 可执行资产

新增：

- `src/enterprise_math/abc_activation_area_future.py`；
- `tests/test_abc_activation_area_future.py`。

executable layer 验证 equal-area future divergence、exact crossing-depth repair、area-increment equivalence，以及拒绝非 extension thresholds。

## 14. 下一前沿

不存在硬阻断。继续做完全对偶的 statement：

1. 测试 area 在 **orbit-node extension** 下的 future-safety；
2. 把 node-rank response coordinate 识别为 dual one-step repair；
3. 构造统一 action-relative repair compiler：threshold action 选择 crossing depth，orbit action 选择 rank；
4. 验证两个 repairs 正好就是 Stage 96 potential 的两个 directional derivatives；
5. 然后把 Stages 91–99 作为完整 pressure-test packet Relay 回 P023/P024/A2。
