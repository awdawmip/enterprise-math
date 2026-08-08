# P019 —— 因果角色 / 方向桥接补充 09

状态：`ACTIVE RESEARCH NOTE / STRUCTURAL BRIDGE`
依赖：P019 causal boundary、phase/magnitude correction、Directional Focusing Supplement 08
纪律：causal phase-transition roles 不是几何 tangent/normal directions；在进一步推导前，direction orbits 也不是 physical shear modes。

## 1. 目的

Stage 08 已证明：若以保持合理 marked causal structure 的自同构群作用于 outgoing incidences，其 orbit 可以作为内禀方向类。下一步要检验的是：已有 phase/boundary 层究竟能否真正提供有用 mark，而不是只停在“以后也许可用”。

答案是可以，但必须保持一个关键区分：

- causal phase transition 定义的是**粗粒度因果角色**；
- marked automorphism orbit 定义的是**内禀方向类**；
- 同一个 causal role 可以包含多个 direction classes。

因此不能把 role 与 direction 合并成同一个概念。

## 2. 精确 causal phase role

对 directed primitive incidence `e=(u,v)` 与 phase field

`phi:V->{-1,0,+1}`，

定义

`role_phi(e)=(phi(u),phi(v))`。

最多产生九种精确 transition roles。例如：

- `(+,+)`：positive phase-preserving incidence；
- `(-,-)`：negative phase-preserving incidence；
- `(+,-)` 或 `(-,+)`：opposite-phase crossing incidence；
- 含 `0` 的 role：接触 exact zero-phase boundary state。

整个定义不需要 radius、欧氏法向量、坐标图或角度。

## 3. P019-ROLE-T01 —— 保持 phase 的 automorphism orbits 必然细化 causal roles

状态：`PROVED`。

若 direction orbits 是由保持 phase marks 的 graph automorphisms 计算得到，那么同一 orbit 中的两条 incidences，其 source phases 必相同，target phases 也必相同。

因此每一个 marked direction orbit 都完整落在唯一 causal role 内。

换言之：direction-orbit partition 是 phase-role partition 的 refinement。

这证明 causal phase 确实可以作为不引入外部坐标的合法方向 refinement 来源。

## 4. P019-ROLE-N01 —— Causal role 不是完整 direction invariant

状态：`COUNTEREXAMPLE / NECESSITY RESULT`。

取五顶点图：

`a->x, b->y, a->z, b->z`

当前截面为 `{a,b}`，并给所有顶点 phase `0`。此时全部 outgoing incidences 的 causal role 都是 `(0,0)`。

但是 section-preserving graph automorphism 仍把这些 incidences 分成两个 orbit：

- private-future orbit `{a->x,b->y}`；
- common-future orbit `{a->z,b->z}`。

因此：

`same causal role != same intrinsic direction orbit`。

所以 causal role 只能是 coarse mark，不能替代 automorphism-resolved direction。

## 5. P019-ROLE-T02 —— Phase marks 可以打破原本 transitive 的 direction orbit

状态：`PROVED BY FINITE EXAMPLE`。

对无标记图

`a->x, b->y`

以及 section `{a,b}`，由于存在交换 `a<->b, x<->y`，两条 incidences 原本属于同一 orbit。

现在令两个 source phase 都为 `0`，但

`phi(x)=+1`, `phi(y)=-1`。

任何保持 phase 的 automorphism 都不能再交换 `x,y`，于是原来的单一 orbit 被细分成两个 direction orbits，其 causal roles 分别为 `(0,+1)` 与 `(0,-1)`。

因此，已有 causal phase field 可以真实地产生内禀方向分辨率。

## 6. 哪些情况下可以称为 crossing，哪些不能称为 tangent

若 incidence 两端 phase 是 `(+,-)` 或 `(-,+)`，它确实是离散 phase field 中的 opposite-phase transition，可以安全称为 **opposite-phase crossing role**。

但不能把其余所有 role 自动叫成“horizon tangent”。Tangency 需要额外的局部几何或 boundary-incidence 结构。同相 edge 可能离边界很远，`0->0` incidence 也可能只是位于零 phase 子结构内部，并不能自动定义 continuum tangent direction。

因此 Stage 09 有意停在 causal roles，不越界命名。

## 7. Stage 09 后的紧凑层级

现在可以把结构压缩为：

`marked primitive causal graph`

`-> phase/boundary complex`

`-> causal phase-transition roles`

`-> marked automorphism direction orbits`

`-> per-orbit C and J_k + cross-orbit overlap`

`-> anisotropy diagnostics`。

只要 automorphism group 保持 phase marks，role partition 必然不比 direction-orbit partition 更细。

## 8. 对 shear comparison gate 的影响

Stage 09 消除了一个重要歧义，但并没有完成 shear theory。

现在已经有依据的内容：

- phase/boundary data 可以提供 intrinsic marks；
- 这些 marks 可以细化 graph-symmetry direction classes；
- resolved direction classes 可以承载现有 integer focusing spectrum。

仍然缺少：

- 把任何 direction class 识别为 physical transverse/tangent direction 的推导；
- 可与 continuum shear 比较的 directional anisotropy evolution law；
- graph steps / sections 与 spacetime congruence 的物理校准。

所以接下来最值得证明的不是再增加一个 static scalar，而是研究 **marked direction partition 在一步 causal evolution 下是否稳定、如何分裂或合并**。

可执行参考：

- `src/enterprise_math/directional_focusing.py`
- `tests/test_directional_focusing.py`
