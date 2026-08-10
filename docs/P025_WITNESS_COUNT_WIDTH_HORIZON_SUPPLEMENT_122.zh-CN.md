# P025 补充 122 —— Sharp Witness-Count Width Horizon

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-witness-count-stage121`  
依赖：P025 补充 119–121  
硬阻断：`NONE`

## 1. 问题

补充 121 已证明：如果知道每个 ideal 的 count，就可以通过 zeta inversion 精确恢复 witness multiplicity function。补充 119 又证明 raw query 会先规范成 antichain。剩下的问题因此是：

> antichain query arity 必须增长到多大，才能保证 exact witness-count recovery？

## 2. P025-T269 —— width 是充分的 count-recovery horizon

令

\[
w:=\operatorname{width}(P).
\]

每个 ideal \(K\in J(P)\) 都由其 maximal boundary

\[
\partial K=\operatorname{Max}(K)
\]

生成，而且

\[
|\partial K|\le w.
\]

因此，只要 declared count future 包含所有 arity 不超过 \(k\) 的 antichain queries，且

\[
k\ge w,
\]

那么每个 ideal 的 count

\[
c(K)=c(\partial K)
\]

都已被观察到。

Stage 121 的 zeta inversion 随即恢复 exact multiplicity vector。

所以

\[
\boxed{k\ge\operatorname{width}(P)\Longrightarrow\text{exact witness multiplicity recovery}.}
\]

## 3. P025-T270 —— width horizon 在 worst case 下 sharp

对任意整数 \(w\ge1\)，取 \(P\) 为 \(w\)-元素 antichain。此时每个 subset 都是 ideal。

定义两个 Boolean witness families：

\[
\mathcal F_{\rm even}=\{I\subseteq P:|I|\text{ even}\},
\]

\[
\mathcal F_{\rm odd}=\{I\subseteq P:|I|\text{ odd}\}.
\]

固定任意 proper required set

\[
S\subsetneq P.
\]

\(S\) 外至少还有一个 free element。所有 supersets 都可写成

\[
I=S\cup T,
\qquad T\subseteq P\setminus S.
\]

其中恰有一半为偶基数、一半为奇基数。所以

\[
\boxed{c_{\rm even}(S)=c_{\rm odd}(S)=2^{w-|S|-1}.}
\]

因此两个 exact families 在所有 arity

\[
|S|\le w-1
\]

的 queries 上完全一致。

但 full set \(P\) 只有唯一 superset，即 \(P\) 自身，所以

\[
\{c_{\rm even}(P),c_{\rm odd}(P)\}=\{0,1\}.
\]

因此每个 \(k<w\) 都可能无法区分两个不同 exact witness families。

所以

\[
\boxed{\operatorname{width}(P)\text{ 是 exact worst-case witness-count recovery horizon}.}
\]

## 4. Chain consequence

若 \(P\) 是 chain，则 \(w(P)=1\)。empty query 的 total count 加上所有 singleton antichain normal forms 的 counts，已经覆盖 \(J(P)\) 上整个 zeta table，因此能恢复每个 witness multiplicity。

所以 width-one geometry 比 Stage 120 的 existential result 更强：pointwise **counts**，而不仅是 support，就能恢复 exact family identity 与 multiplicity。

## 5. Existential saturation 与 counting saturation

补充 120 已证明 existential joint-membership semantics 在 width 处饱和。Stage 122 进一步证明：

\[
\boxed{\text{同一个 width horizon 也足以恢复 exact multiplicity}.}
\]

但两种 saturation 的语义不同：

- existential future：超过 width 后不会再出现新的 joint truth values；
- counting future：达到 width 时，整个 witness multiplicity state 变成可逆。

共同 horizon 来自 antichain-boundary operation normalization，而不是 observable 强度本身。

## 6. 架构结论

该结果把三件事严格拆开：

1. **query geometry** 决定 maximum essential arity；
2. **observable strength** 决定在完整查询该 geometry 后可以恢复什么；
3. **exact family identity** 可以在相同 essential query coordinates 上要求更丰富的 values。

因此 arity precision 与 value precision 是不同资源。

## 7. Prior-art 边界

Boolean lattice parity split、zeta/Möbius inversion 与 width/antichain facts 都是经典数学。这里不主张 generic novelty。

项目侧结果是把 sharp horizon 精确放入 P025/A2/A4 future-precision hierarchy。历史新颖性仍为 `NOVELTY_UNVERIFIED`。

## 8. 可执行资产

新增：

- `src/enterprise_math/poset_witness_count_horizon.py`；
- `tests/test_poset_witness_count_horizon.py`。

executable layer 验证 width sufficiency、所有低于 width 的 even/odd family collision、full-width separation，以及 proper query 的精确公式 `2^(w-|S|-1)`。

## 9. 下一前沿

如果 declared future 只在一个 queried subposet `Q` 上观察 witness counts，应该只能恢复 ambient exact states 在 `J(Q)` 上的 projected multiplicity distribution，而不能恢复完整 ambient witness identity。Stage 123 应推导这个 task-relative count pushforward，并证明 recovery horizon 变成 `width(Q)`。
