# P025 补充 97 —— Activation-Area Collision 与 `Potential != State` 边界

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-orbit-normal-stage91`  
依赖：P025 补充 96  
硬阻断：`NONE`

## 1. Stage 96 留下了一个明确的 injectivity 问题

activation area

\[
A=\sum_{k,j}B_{k,j}
\]

是 biaxial update accounting 的有用 scalar potential。

但 scalar potential 并不会自动成为 sufficient semantic state。

Stage 97 直接测试最强 failure mode：

> 能否存在两个 exact arithmetic dyadic states，使用相同 threshold grid 与 horizon，拥有相同 activation area，却对某个 declared threshold/node future query 给出不同答案？

答案是 yes。

## 2. 固定共同 future grid

取 base exponent

\[
m=2,
\]

horizon

\[
h=1
\]

对应 exponents `2,4`，并固定同一 threshold grid

\[
\boxed{T_1=\frac12,\qquad T_2=1.}
\]

两个 states 之间不允许修改 threshold metadata 或 horizon。

## 3. P025-C35 —— exact equal-area collision

### Flat orbit

对

\[
(q,p)=(3,5),
\]

exponents `2,4` 的 exact difference pressures 为

\[
\boxed{\rho_0=\frac12,\qquad\rho_1=\frac12.}
\]

因此

\[
B^{\rm flat}
=
\boxed{\begin{pmatrix}1&1\\0&0\end{pmatrix}},
\]

crossing depths 为

\[
\boxed{(0,\infty),}
\]

node ranks 为

\[
\boxed{(1,1),}
\]

activation area 为

\[
\boxed{A^{\rm flat}=2.}
\]

### Jump orbit

对

\[
(q,p)=(7,17),
\]

exact difference pressures 为

\[
\boxed{\rho_0=\frac16,\qquad\rho_1=\frac{13}{6}.}
\]

因此

\[
B^{\rm jump}
=
\boxed{\begin{pmatrix}0&1\\0&1\end{pmatrix}},
\]

crossing depths 为

\[
\boxed{(1,1),}
\]

node ranks 为

\[
\boxed{(0,2),}
\]

activation area 仍为

\[
\boxed{A^{\rm jump}=2.}
\]

于是

\[
\boxed{A^{\rm flat}=A^{\rm jump}}
\]

但所有 richer Ferrers representations 都不同。

## 4. P025-T234 —— area 不能决定 activation matrix

两个 exact states 位于同一个 scalar-area fiber

\[
A=2.
\]

但第一个 declared cell 已经不同：

\[
\boxed{B^{\rm flat}_{1,0}=1,\qquad B^{\rm jump}_{1,0}=0.}
\]

因此不存在函数

\[
f
\]

能在这一 fine-state family 上满足

\[
B=f(A).
\]

等价地，

\[
\boxed{\text{activation area 不能 factor full threshold matrix}.}
\]

## 5. P025-T235 —— area 也不能决定任何一套 dual boundary chart

两个 equal-area states 在 crossing coordinates 中分别是

\[
(0,\infty)\ne(1,1),
\]

在 rank coordinates 中分别是

\[
(1,1)\ne(0,2).
\]

Ferrers boundary words 同样不同。

因此

\[
\boxed{
A\not\Rightarrow(j_k),
\qquad
A\not\Rightarrow(r_j),
\qquad
A\not\Rightarrow\text{boundary path}.
}
\]

scalar potential 保留 total active mass，但丢掉 positional information。

## 6. P025-C36 —— exact same-area semantics 可以具有相反几何

两个 `2 x 2` matrices 都包含两个 active cells，但 geometry 不同：

- flat orbit 从一开始就激活 low threshold，并始终达不到 high threshold；
- jump orbit 起初低于两个 thresholds，随后在同一 node 同时跨过两者。

所以 area 无法区分

\[
\boxed{\text{persistent low-level activation}}
\]

与

\[
\boxed{\text{late multi-level activation}.}
\]

这正是 Ferrers boundary 所保留的 temporal / precision geometry。

## 7. P025-T236 —— area 只对 aggregate-area future 安全

对 declared future map

\[
F_A(B):=\sum_{k,j}B_{k,j},
\]

scalar quotient 当然 exact：

\[
F_A(B)=A.
\]

但对保留 distinguishing cell 的 future map

\[
F_{1,0}(B):=B_{1,0},
\]

equal-area collision 给出

\[
F_{1,0}(B^{\rm flat})\ne F_{1,0}(B^{\rm jump}).
\]

所以 area collapse 对 aggregate area query future-safe，但对 richer threshold semantics 不安全。

这就是 P023 与 Stage 90 所强调的 future-relative distinction 的 exact arithmetic 实例。

## 8. P025-C37 —— useful potential 不推出 sufficient state

Stage 96 证明 `A` 在 threshold/orbit extensions 下具有 exact first- 与 mixed-difference laws。

Stage 97 则证明这些漂亮 response laws 并不会让 `A` 在 semantic state 上 injective。

因此

\[
\boxed{\text{scalar potential}\not\Rightarrow\text{sufficient state}.}
\]

这个 negative boundary 很重要，因为 potentials 往往正因 dynamics 看起来更简单而具有强吸引力。

## 9. State / chart / potential / response layering

Stages 93–97 现在严格区分四层：

1. **semantic boundary state** —— exact finite threshold future；
2. **coordinate chart** —— crossings、ranks、path；
3. **scalar potential** —— activation area；
4. **local response law** —— area 的 first 与 mixed finite differences。

没有任何 implication 允许 lower layer 在缺少 declared future query 与 factorization proof 时静默替代 upper layer。

## 10. P023 解释

令

\[
q_A(B):=A.
\]

P023 fiber-constancy criterion 表明：future map 恰在每个 equal-area fiber 上 constant 时才能 descend through `q_A`。

Stage 97 collision 给出了一个 cell future 非 constant 的 exact fiber。

所以这不是对 scalar collapse 的哲学反对，而是 literal future-compatibility counterexample。

不需要新的 P023 theorem；P025 只是为已有 theorem 提供一个非平凡 number-theoretic pressure test。

## 11. Prior-art / novelty 边界

noninjective scalar invariants 与 equal-area Ferrers collisions 都是 elementary / general phenomena。

P025 不主张 generic novelty。

项目侧结果只是 dyadic projective-pressure state 内的 exact arithmetic collision，以及由此得到的 Stage-96 potential interpretation negative boundary。历史新颖性仍为 `NOVELTY_UNVERIFIED`。

## 12. 可执行资产

新增：

- `src/enterprise_math/abc_activation_area_collision.py`；
- `tests/test_abc_activation_area_collision.py`。

executable layer 验证 common grid/horizon、equal scalar area、different matrices/crossings/ranks/path，以及一个 explicit distinguishing future cell。

## 13. 下一前沿

不存在硬阻断。继续：

1. 测试 scalar area 是否连“extension 后的 future area”都 future-compatible；
2. 搜索两个 equal-area states 在插入同一个 new threshold 后 area 分叉的 exact pair；
3. 若找到，记录更强的 `potential is not Markov under extension` 边界；
4. 识别某个 declared extension 所需的 one-step repair data；
5. 然后把 Stages 91–98 作为完整 state/chart/potential/response pressure-test packet Relay 回 P023/A2。
