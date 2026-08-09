# P011 —— Provenance Repair Spectrum 桥

状态：`PROVED RESEARCH NOTE`  
归属：P011 irreversibility spectrum，消费 P023-S9/S10 repair semantics  
范围：有限确定性映射  
纪律：这里讨论的是数学上的 reconstruction cost，不表示 many-to-one 物理过程真的保存、暴露或能够物理恢复已经丢弃的历史。

## 1. 同一个 fiber 的两种读法

令

\[
F:X\to Y
\]

为有限非空状态集 `X` 上的映射，`|X|=N`。

P011 把非空 fiber 大小记为

\[
m_F(y)=|F^{-1}(y)|.
\]

现在改用 P023 风格问一个任务问题：

> 只保留未来状态 `F(x)`，但要求精确恢复原始状态 label `x`。

对一个 reached output `y`，`F^{-1}(y)` 内所有 states 都具有同一个 retained value，因此必须用不同 repair symbols 才能恢复原 label。

所以 P011 的 history merging 与 P023 的 repair complexity 实际上作用于同一个 partition。

## 2. P011-RS-T01 —— 局部 provenance repair 等于 fiber multiplicity

状态：`PROVED`。

令 `r_F(y)` 表示在 output fiber `y` 上恢复原始状态 label 所需的最小 repair symbols 数，则

\[
\boxed{
r_F(y)=m_F(y)=|F^{-1}(y)|.
}
\]

### 证明

必要性：`m_F(y)` 个不同原始 states 都具有相同 retained output `y`，所以精确恢复 provenance 必须为它们分配不同 repair symbols。

充分性：在该 fiber 内局部编号为 `0,...,m_F(y)-1` 即可。不同 output fibers 之间可以复用同一批 symbols，因为 retained output 已经区分了 fiber。∎

因此全局最小共享 alphabet 为

\[
\boxed{
R_{\max}(F)=\max_{y\in\operatorname{im}F}m_F(y).
}
\]

这正是把 P023-S9 local split multiplicity 应用于从 `F`-kernel 返回 identity partition 的 refinement。

## 3. P011-RS-T02 —— 每个 P011 fiber functional 都是 repair-cost functional

状态：`PROVED`。

对任意整数函数

\[
\varphi:\mathbb N_{>0}\to\mathbb Z,
\]

P011 定义

\[
I_\varphi(F)
=
\sum_y\varphi(m_F(y)).
\]

由 T01，恒等地有

\[
\boxed{
I_\varphi(F)
=
\sum_y\varphi(r_F(y)).
}
\]

因此 P011-T01 同时可以读成 repair theorem：

> 若 `phi` 为 superadditive，则任何确定性的未来 postcomposition 都只能增加或保持局部 provenance-repair alphabets 的 aggregate superadditive cost。

无需另做新证明；这只是已有 fiber identity 的精确解释转换。

## 4. P011-RS-T03 —— Collision spectrum 就是 binomial repair spectrum

状态：`PROVED`。

P011 的 canonical collision spectrum 为

\[
J_k(F)
=
\sum_y\binom{m_F(y)}k.
\]

用 T01 改写得到

\[
\boxed{
J_k(F)
=
\sum_y\binom{r_F(y)}k.
}
\]

所以：

- `J_1=N` 数全部 provenance labels；
- `J_2` 数同一 repair fiber 内竞争的 unordered label pairs；
- `J_k` 数 `k`-way 局部 provenance ambiguities；
- 完整 spectrum 是局部最小 repair alphabet sizes 的 binomial moment spectrum。

P011 的数值完全没有变化，只是从 P023 reconstruction 方向看到了同一批整数的另一种精确含义。

## 5. P011-RS-T04 —— Binomial inversion 恢复完整 repair-size distribution

状态：`PROVED`。

令

\[
c_r(F)
=|\{y:r_F(y)=r\}|.
\]

则 P011-T05 变成

\[
\boxed{
c_r(F)
=
\sum_{k=r}^N(-1)^{k-r}\binom kr J_k(F).}
\]

因此 collision spectrum 能精确恢复：有多少 reached outputs 分别需要每一种大小的局部 repair alphabet。

特别地，

\[
\boxed{
R_{\max}(F)
=
\max\{r:c_r(F)>0\}.
}
\]

所以完整 P011 spectrum 不仅决定 fiber-size profile，也决定精确 global minimum provenance-repair alphabet 以及每个局部 repair-size multiplicity。

## 6. P011 中原本已经存在的三种不同 repair summary

### 6.1 Aggregate excess repair capacity

取 `phi(r)=r-1`：

\[
\boxed{
N-|\operatorname{im}F|
=
\sum_y(r_F(y)-1).
}
\]

这是每个 reached output 在“至少一个 symbol”之外还需要多少局部 extra symbols 的总和。

它不等于 global shared alphabet `R_max(F)`，因为 symbols 可以跨 fibers 复用。

### 6.2 Pairwise ambiguity

\[
\boxed{
J_2(F)=\sum_y\binom{r_F(y)}2.
}
\]

它通过 pairwise competition 对大 repair fiber 给出二次权重。

### 6.3 Worst-case alphabet

\[
\boxed{R_{\max}(F)=\max_y r_F(y).}
\]

这是最坏情形下精确恢复 provenance 所需的可全局复用 repair symbols 数。

这三者是同一个局部 repair profile 上不同的 observable。

## 7. P011-RS-T05 —— 精确 repair composition law

状态：`PROVED`。

令

\[
X\xrightarrow{F}Y\xrightarrow{G}Z.
\]

对每个 reached `z`，定义 reached predecessor set

\[
A_z
=
\{y\in\operatorname{im}F:G(y)=z\}.
\]

则 composition 后的局部 repair alphabet 精确满足

\[
\boxed{
r_{G\circ F}(z)
=
\sum_{y\in A_z}r_F(y).
}
\]

### 证明

final fiber 是旧 fibers 的不交并：

\[
(G\circ F)^{-1}(z)
=
\bigsqcup_{y\in A_z}F^{-1}(y).
\]

取基数并应用 T01 即得。∎

这就是 P011 的 exact fiber-sum law 改写成 repair transport。

## 8. P011-RS-T06 —— 分阶段 repair 的 sharp product bound

状态：`PROVED`。

令

\[
R_F=\max_y r_F(y)
\]

并令

\[
R_G^{\rm reach}
=
\max_z|A_z|
\]

表示从 final `G` output 恢复 reached `F`-output label 所需的最小 alphabet。

则

\[
\boxed{
R_{G\circ F}
\le
R_F R_G^{\rm reach}.
}
\]

### 证明

对任意 `z`，由 T05：

\[
r_{G\circ F}(z)
=
\sum_{y\in A_z}r_F(y)
\le
|A_z|R_F
\le
R_G^{\rm reach}R_F.
\]

对 `z` 取最大值得证。∎

这正是 P023-S9 repair-chain submultiplicativity 在 partition chain

\[
\Delta_X
\subseteq
\ker F
\subseteq
\ker(G\circ F)
\]

上的特化。

### Equality criterion

等号成立，当且仅当存在某个 reached final output `z` 同时满足：

1. `|A_z|=R_G^reach`；
2. 对所有 `y in A_z` 都有 `r_F(y)=R_F`。

所以只有当两个阶段的 worst branches 在同一个 final fiber 上对齐时，stagewise worst costs 才精确相乘；否则 direct repair 可以严格小于两个阶段 worst-case 的乘积。

## 9. P011-RS-T07 —— 新 collision increment 就是新的 cross-repair ambiguity

状态：`PROVED`。

若一个 final output 合并了 predecessor repair fibers，其大小为

\[
a_1,\ldots,a_s,
\]

则 P011 的 exact collision increment

\[
\Delta J_k
=
\binom{a_1+\cdots+a_s}{k}
-
\sum_i\binom{a_i}{k}
\]

恰好数：以前属于不同 repair fibers、现在必须在同一个 final repair fiber 内竞争的新增 provenance `k`-subsets。

对 pairs：

\[
\boxed{
\Delta J_2
=
\sum_{i<j}a_i a_j.
}
\]

因此 P011 的 forward irreversibility growth 与 P023 的 reverse repair growth，是同一次 fiber-coarsening event 的两个方向。

## 10. 与 incidence repair calculus 的关系

取 identity provenance relation

\[
R_{id}
=
\{(x,x):x\in X\}
\subseteq X\times X.
\]

再通过 `F` 观察第二坐标。P023-S10 给出

\[
M(R_{id},F)
=
\max_y|F^{-1}(y)|
=
R_{\max}(F).
\]

所以本 P011 bridge 正是一般 incidence-repair theorem 的 identity-label 特化。

对一般 label relation，predecessor label sets 可能互相重叠，此时 deterministic fiber-sum equality 会退成 union inequality。identity provenance 的特殊之处在于不同 predecessor fibers 的 labels 天然不交。

## 11. Foundation-level 解释

同一个有限 partition 有两种完全精确的读法：

### Forward reading —— irreversibility

多少原本不同的 histories 已经合并到每一个当前状态？

### Reverse task reading —— repair

如果某个 proof/task 现在要求原始 identity，至少需要多少额外离散 symbols 才能重新区分这些 histories？

因此在数学层面：

\[
\boxed{
\text{history multiplicity}
=
\text{minimum exact provenance-repair multiplicity}.
}
\]

这个等式不能被误读成物理可逆性。即使项目的 no-hidden-remainder 假说认为 post-transition ontology 中没有这些历史 labels，研究者仍可以从外部 preimage 比较定义一个数学 decoder alphabet。

## 12. 可执行规格

- `src/enterprise_math/p011_repair_spectrum.py`
- `tests/test_p011_repair_spectrum.py`

回归通过 binomial inversion 重建完整 repair-size distribution，验证 exact composition sum，在三状态 maps 上穷举 sharp product bound，固定 strict submultiplicativity，并与已有 P011 collision formulas 交叉一致。

## 13. 前人工作纪律

Function fibers、binomial moments、finite partition refinement，以及在 fiber 内编码 labels 都是标准数学。这里不主张一般等价关系的历史创新性。项目价值是把独立发展的 integer-first irreversibility layer 与 future-safe precision/minimal-repair layer 精确接成同一个 fiber calculus。
