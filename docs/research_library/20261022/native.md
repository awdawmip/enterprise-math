# 原生 X6 成果、公式与复用工具整理

整理日期：2026-10-22（Asia/Shanghai）。来源快照：`63f87045b456cf573a9eaa7bbc8d4a4673a3e6ea`。这是既有文献抽取；保留来源的作者、审核与状态，不产生新证明、新审核票、正式化或数学晋升。

统一定型：心跳世界的完整六维 signed `Z^6` Cell torsor。锚点是选定的 Cell，没有全局特权原点；本文 signed 坐标是内部 raw chart，不能直接作为最终公开 Cell 地址。原生空间不存在平面。静态条目不强制引入时间；闭迹的次序索引另行定型。观察标签、有限群和图关系均不自动成为物理运动或力学定律。

| 条目 | 来源所载状态 | 工具整理 |
|---|---|---|
| X6-SENSOR-FIBERS | 有界非作者 whole-review PASS；result only | T4、T6 精确复用 |
| X6-PHASE-MIN64 | 有界非作者 whole-review PASS；result only | T4 局部容量、T6、T7 精确复用 |
| X6-ADJACENCY-AUT | 有界非作者 whole-review PASS；result only | 标准无限网格图论组合；不硬套有限 T7 |
| X6-TRACE24-REUSE | 旧 V10/C24 exact REUSE；已关闭 | 合并回旧构造，不新增工具或新定理票 |
| X6-SEPARATOR-DRAFT | 本地作者待审稿；固定主快照精确路径 404 | 仅登记缺口，未入已审核集合 |

## X6-SENSOR-FIBERS — 六个正向邻居的联合二次读出：完整纤维分类与锚点修复

**状态。** 作者与同行报告已在固定主快照可读；同行报告明确有界整体验证通过。本次只抽取其原有结论，不增加数学接受票、正式化、Working Truth或Foundation地位。 作者：EM-FREE-185026；审核：EM-FREE-CF1677。

**定型与条件。** Heartbeat X6的完整signed Z^6 Cell torsor内，固定锚点a的有限盒B；signed chart不是最终Cell地址。

- B={a+z:z∈{-1,0,1}^6}，全部729个Cell保留。
- p_i=a+e_i；O为保留轴标签和联合关联的六元组，使用既有component-quadratic读出。
- 静态Cell-center观察，不声明路径、packet或动力学未来语言。

**可复用公式。**

- `Q(z)=Σ_{i=1}^6 z_i²; O_i(z)=d6(a+z,a+e_i)²=Q(z)+1−2z_i`
- `O(z)=O(w) ⇒ w=z+t(1,…,1), t(Σ_i z_i+3t−1)=0`
- `u_A=−1_A; v_A=1_{A^c}, |A|=2; O(u_A)=O(v_A), Q(u_A)=2,Q(v_A)=4`
- `15 doubletons + 699 singletons; |O(B)|=714; (O,Q) is injective on B`

**结论。** O(z)=O(w)当且仅当z=w，或无序对{z,w}恰为某唯一二元轴集A对应的{u_A,v_A}。其余Cell均为单点纤维；附加锚点二次距离Q恰好拆开全部碰撞。

**边界。**

- 不证明任意传感器设计中七个读出的最小性。
- 不适用于无标签读出、多重集、独立边缘、任意盒或完整packet身份。
- O纤维不等于整个global-diagonal轨道；不授权其他未来操作的商。
- 不推出物理传感、传播、Euclidean角度或力学定律。

**工具与去重。** T4_FINITE_FIBER_CAPACITY_COLLISION_MINIMA：REUSE_APPLIED（nu=729,kappa=714,collision defect=15）；T6_OPERATION_SAFE_QUOTIENT：REUSE_APPLIED（Q非O纤维常值；(O,Q)为此静态有限盒的精确修复）。

这是具体有限读出结果，非新Tool族。与二十个positive-min-zero观察的diagonal商区分；未声称全库无先例或全球首创。

**出处。**

- [author_complete_bundle](https://github.com/awdawmip/enterprise-math/blob/8ec23a3f152a176f506ee52281d2767b772685d4/research_notes/free_native_discovery/20261017_EM_FREE_185026_X6_POSITIVE_NEIGHBOR_FIBERS_WHOLE.json)；当前固定快照 blob：`b0526239c068a905138e03c40dff6a89d611fd50`。
- [nonauthor_whole_review](https://github.com/awdawmip/enterprise-math/blob/a31536aa76c972c408505856a7af8e9476680d6c/research_notes/owner_goal_20261017/reviews/native_x6_sensor_fibers_nonauthor_cf1677/NATIVE_X6_SIX_POSITIVE_NEIGHBOR_FIBERS_NONBLIND_COMPLETE_TECHNICAL_WHOLE_REVIEW_AND_CONTEXT.md)；当前固定快照 blob：`ef7802a72ddd5f0d7b172b8989084c0499d8e2d7`。

## X6-PHASE-MIN64 — 具全部S6轴置换和十三个局部分离标签的有限Abelian平移观察器：最小阶64

**状态。** 固定主快照含完整作者bundle和BFF的有界整体验证报告；其原始创建时PENDING字段保留为历史。 作者：EM-FREE-185026；审核：EM-DVR-BFF6DC。

**定型与条件。** 原生完整Z^6 torsor上的明确声明有限Abelian观察/更新carrier；不是完整Cell身份。

- A为有限Abelian群，由六个标号元素x_i生成。
- 每个σ∈S6都诱导A的automorphism，x_i↦x_{σ(i)}。
- 0及全部±x_i共十三个元素两两不同。
- 观察器q(a+z)=Σ_i z_i x_i；允许未来语言仅有限平移词和该S6重新标号作用。

**可复用公式。**

- `r=ord(x_i−x_j)≥2; K=ker(Z^6→A)⊆D_r={v:v_i≡v_j (mod r)}; |A|=r^5[D_r:K]`
- `L={v∈Z^6: all v_i have the same parity, Σ_i v_i≡0 (mod 4)}; A=Z^6/L`
- `[Z^6:D_2]=32, [D_2:L]=2, |A|=64`
- `q(z) ≅ ((z_1−z_6,…,z_5−z_6) mod 2, Σ_i z_i mod 4), with joint parity constraint`
- `q(z+v)=q(z)+q(v); q(σz)=φ_σ(q(z))`

**结论。** 在此明确类别中，最小阶为64。若|A|≤64，r≥3被r^5≥243排除；r=2时32阶会导致x_i=−x_i，违背分离；上述L达到64，并支付全部十三标签分离与规定操作的精确下降。

**边界。**

- 不分类全部64阶carrier。
- 不证明非Abelian、非线性编码、任意有限自动机或完整独立sign-flip对称下的最小性。
- 4e_i∈L，故标签会合并不同Cell；不保norm、path或packet身份。
- 64仅为群状态数，不是物理内存、能量、相位、时间或传播定律。

**工具与去重。** T4_FINITE_FIBER_CAPACITY_COLLISION_MINIMA：REUSE_APPLIED（仅十三标签局部容量下界13≤|A|，不提供64下界）；T6_OPERATION_SAFE_QUOTIENT：REUSE_APPLIED（已明示q/平移/S6语言下的kernel下降准则）；T7_FINITE_SYMMETRY_EQUIVARIANCE：REUSE_APPLIED（构造出的64元素群的明确有限S6作用）。

r^5整除与L的匹配构造是来源中自付的具体standard COMPOSE结果；不建立新Tool族或全库缺失证明。bundle内闭迹24项为exact REUSE，不能增加第二项新结果或新审核票。

**出处。**

- [author_complete_bundle](https://github.com/awdawmip/enterprise-math/blob/f0cef5c863e059ae40f8ded281bfc531424db0eb/research_notes/free_native_discovery/20261017_EM_FREE_185026_TRANSLATION_PHASE_MIN64_AND_CLOSED_TRACE_WHOLE.json)；当前固定快照 blob：`c59fbc3e6b774da8c5ff7b3eb310d40d28e11e20`。
- [nonauthor_whole_review](https://github.com/awdawmip/enterprise-math/blob/41007df6361348bde7f574ff56fb969566e9af41/research_notes/owner_goal_20261017/reviews/native_translation_phase_min64_nonauthor_bff6dc/NATIVE_X6_FINITE_TRANSLATION_PHASE_MIN64_NONBLIND_COMPLETE_TECHNICAL_WHOLE_REVIEW_AND_CONTEXT.md)；当前固定快照 blob：`576de501c6ea3770ad2dd62e441879de74cc9fdc`。

## X6-ADJACENCY-AUT — 完整Cell无向十二邻接图的任意自同构恰为锚点变换加signed轴置换

**状态。** 作者原文创建时未审；后续完整非作者报告已在固定主快照公开，载有精确关系范围PASS。 作者：EM-FREE-CF1677；审核：EM-FREE-185026。

**定型与条件。** 完整X6 signed Z^6 Cell torsor；关系为十二个signed-unit邻接的无标签无向并集。

- E={±e_1,…,±e_6}，x∼y iff y−x∈E；保留全部Cell。
- f是全部Cell上的双射，并满足x∼y iff f(x)∼f(y)。
- 假设中不预设affine、坐标逐点形式或每条有向边标签固定。

**可复用公式。**

- `N(x+s)∩N(x+t)={x} if t=−s, else {x,x+s+t}, for distinct s,t∈E`
- `d_s(x)=f(x+s)−f(x); d_{−s}(x)=−d_s(x); d_s(x+t)=d_s(x) for all s,t∈E`
- `f(a+z)=b+Σ_{i=1}^6 z_i ε_i e_{π(i)}, b=f(a), π∈S6, ε_i∈{±1}`

**结论。** 每个这样的全图自同构必有显示的signed affine形式，反之每个显示形式都是自同构，且存在实际逆。指定a及其像b后，六个正邻居的像唯一确定π与ε_i。

**边界。**

- 只保存指定的无向并邻接关系，不证明全部原生关系或PERP_E的自同构。
- 不分类单向homomorphism、非满射、partial map、local embedding或endomorphism。
- 不推出signed permutation在物理上可实现为旋转/反射、力学或时间演化。
- 使用signed chart内部坐标，不构造最终公开Cell地址codec。

**工具与去重。** 具体来源方法：COMPOSE_APPLIED（standard grid-graph rigidity：common-neighbor识别opposite配对，四边word传播局部增量，有限signed路径积分到全图；不假称T7有限算法覆盖无限图）。

与有限Abelian carrier的预设S6作用不同；后者不提供任意全图映射的必要性。来源称standard COMPOSE且novelty UNKNOWN，无新Tool提议。

**出处。**

- [author_complete_note](https://github.com/awdawmip/enterprise-math/blob/9cb5d2d4aad2bba3c54a2211966a340529b5e91b/research_notes/owner_goal_20261017/native_x6_adjacency_automorphism_cf1677/NATIVE_X6_FULL_CELL_ADJACENCY_AUTOMORPHISMS_ARE_SIGNED_AFFINE_DERIVED_NOTE_V1.md)；当前固定快照 blob：`45a01f07e9a7b7ebc599029c3e4f62b26b38c9be`。
- [nonauthor_whole_review](https://github.com/awdawmip/enterprise-math/blob/0390463494c7c5c0f61244cf2ba35f3cc9fa1ae1/research_notes/owner_goal_20261017/reviews/native_full_cell_adjacency_nonauthor_185026/NATIVE_X6_FULL_CELL_ADJACENCY_SIGNED_AFFINE_NONBLIND_COMPLETE_TECHNICAL_WHOLE_REVIEW_AND_CONTEXT.md)；当前固定快照 blob：`348d8d7b997cd288fa3ff4ed353aaa20e9f088eb`。

## X6-TRACE24-REUSE — 绕开锚点并遍历十二个signed邻居的简单闭迹：旧C24构造复用

**状态。** 作者bundle与同行min64报告均明确将此项作为旧V10 exact REUSE关闭；不是第二个新定理或额外审核票。 作者：EM-FREE-185026 (2026-10-17 rediscovery/closure only; old construction provenance retained)；审核：EM-DVR-BFF6DC (checked closed companion within min64 whole; no new trace vote)。

**定型与条件。** 完整X6空间Cell的有序邻接闭迹；次序索引另型，不是物理时钟。

- 锚点a及全部十二邻居a±e_i。
- 闭迹含全部十二邻居、避免a、除最终回到初始Cell外不重复空间Cell。
- 每步都是原signed unit邻接。

**可复用公式。**

- `12 cyclic gaps × at least 2 primitive moves = 24 moves`
- `v=(e_1,…,e_6,−e_1,…,−e_6), v_12=v_0, w_j=v_j+v_{j+1}; a+v_0,a+w_0,a+v_1,…,a+v_11,a+w_11,a+v_0`

**结论。** 在字面条件下最短为24步，显示构造有24个不重复空间Cell。该signed顺序与全部OUTER两步lift已见旧V10第7–9节；2026-10-17项按重复复用关闭。

**边界。**

- 不保证存在canonical S6-equivariant闭迹选择。
- 不推断物理最短时间、native旋转动力学、完整事件回归或通用branch selector。
- 同行实际旧证据为bundle嵌入的原142–254行，不冒充旧V10整篇managed Source阅读。

**工具与去重。** 具体来源方法：REUSE_APPLIED（旧signed-direction C12的all-OUTER C24完整vertex/edge构造；无新Tool payload）。

合并回旧V10/C24来源，保留新探索的归档与下界说明；不建立平行新编号定理、论文或自动后继。原生C24与divisor-extrema有界漂移C24是不同型对象。

**出处。**

- [complete_bundle_documents_3_to_6](https://github.com/awdawmip/enterprise-math/blob/f0cef5c863e059ae40f8ded281bfc531424db0eb/research_notes/free_native_discovery/20261017_EM_FREE_185026_TRANSLATION_PHASE_MIN64_AND_CLOSED_TRACE_WHOLE.json)；当前固定快照 blob：`c59fbc3e6b774da8c5ff7b3eb310d40d28e11e20`。
- [closed_companion_check](https://github.com/awdawmip/enterprise-math/blob/41007df6361348bde7f574ff56fb969566e9af41/research_notes/owner_goal_20261017/reviews/native_translation_phase_min64_nonauthor_bff6dc/NATIVE_X6_FINITE_TRANSLATION_PHASE_MIN64_NONBLIND_COMPLETE_TECHNICAL_WHOLE_REVIEW_AND_CONTEXT.md)；当前固定快照 blob：`576de501c6ea3770ad2dd62e441879de74cc9fdc`。
- 旧文件 `research_notes/X6_GLOBAL_SIGNED_DIRECTION_C12_AND_C24_LIFT_V10_20260906.md`，实际复用证据为上述公开 bundle 内嵌的原 142–254 行；旧 whole-file SHA-256：`e03cf388c6b418f2c906bfc7804c155ec73bafc1379c5f9e40e4c6ebdc0b0d7d`。不冒充旧整篇 managed Source 阅读。

## X6-SEPARATOR-DRAFT — 有限标记Cell补图：唯一无限分支及首个分离集的作者草稿

**状态。** 2026-10-22固定主快照的精确whole-bundle路径返回GitHub 404；本地完整作者稿及oncefrozen上下文存在，未发现该稿独立同行报告。这里只登记作者主张与待审边界，不放入已审核定理集合。 作者：EM-FREE-CF1677；审核：尚无独立报告。

**定型与条件。** 完整X6 signed-unit邻接图，有限标记集S下的静态S-avoiding word关系；标记Cell仍存在。

- S是实际Cell的有限集合。
- 补图连通仅指所有顶点避开S的有限原邻接word。
- 不把静态avoidance定义解释为物理阻挡/运动许可。

**可复用公式。**

- `For every finite S, X\S has exactly one infinite component`
- `|S|≤11 ⇒ X\S is connected`
- `|S|=12: X\S disconnected ⇔ S=N(x)={x+s:s∈{±e_i}}; components={x} and one infinite component`

**结论。** 作者草稿主张最小有限分离集大小为12，且所有达到者恰为某唯一中心的完整十二邻居集。本次未新增证明审核或接受该结论。

**边界。**

- 独立同行whole-review及公开Source缺失。
- 不分类大于12的分离集或无限S，不给出最短绕行。
- 不推出物理堵塞阈值、可通行性、force或time law。
- 旧adjacency automorphism定理不是其数学前提。

**工具与去重。** 具体来源方法：NOT_APPLICABLE（仅保留作者standard grid connectivity COMPOSE自述；未识别/未新建generic Tool，不以目录匹配代替实际工具复用）。

来源仅有两个已知primitive的有界文字比较及他人occupation-only回复；全库覆盖与novelty UNKNOWN。草稿不自动恢复研究分支。

**出处。**

- [local_oncefrozen_primary](/workspace/enterprise-math/research_notes/owner_goal_20261017/native_x6_finite_vertex_separators_cf1677/NATIVE_X6_FINITE_FORBIDDEN_CELL_REACHABILITY_AND_MINIMUM_SEPARATOR_DERIVED_NOTE_V1.md)（LOCAL_FROZEN_AUTHOR_BYTES_ONLY）；SHA-256：`8c6188284e5dfbbc30e1bf5e31d585f4a6c543f72aaff2ad09d3fe1679ab9cc3`。
- [local_complete_whole_bundle](/workspace/enterprise-math/research_notes/owner_goal_20261017/native_x6_finite_vertex_separators_cf1677/NATIVE_X6_FINITE_FORBIDDEN_CELL_SEPARATOR_COMPLETE_WHOLE_BUNDLE.json)（LOCAL_ONLY_NOT_SOURCE_PUBLICATION）；SHA-256：`5dd8b85cdfc9097ea2889965949622723e379460302c0728030acec53b8f632b`。
- 固定主快照对精确 whole-bundle 路径实际返回 `404 NOT_FOUND`；没有可引用的已发布作者 Source。

## 工具库调用边界

本次没有创建新的顶层工具族或科学实现。T4/T6/T7 的映射沿用来源已经明确支付的数学接口，状态为 `REUSE_APPLIED`，并不表示执行过对应程序。六传感器条目是静态纤维修复；64 状态条目只对其声明的平移与 S6 操作语言安全。后续用途若增加 Q、路径、packet、时间或物理观察，必须重新核对保持范围。

无限图的自同构分类、有限删除集草稿与有限 T7 群作用程序具有不同输入域。工具的同名或词汇命中不提供无限图定理，也不构成能力缺口或新 Tool 理由。草稿与 exact REUSE 项不增加已审核新成果数量。

