# Hodge 专项驾驶员 Handoff

Date: `2026-08-17`
Status: `ACTIVE / DRIVER_HANDOFF`
Source Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`
New Driver: `EM-DVR-HODGE-4Q7M2K / HODGE_CONTROL_PLANE`
Dedicated branch: `research/hodge-special-control-plane`

## 0. 专项使命

建立并验证一个严格的“进取数论 → Hodge”研究程序。

核心假说不是“换一套坐标就能证明 Hodge”，而是：

> 同一个代数对象可能具有至少两种几何 realization：经典垂直/解析 realization 与进取 realization。若进取 realization 能把经典侧隐藏的 Hodge 类重新显化为具有额外可代数化约束的离散/组合 cycle，并能严格提升回原代数簇上的代数循环，则可能形成 Hodge 猜想的新桥梁路线。

截至本 handoff，Hodge 猜想仍是 Clay Millennium Prize Problem；已知某些特殊情形，整体一般情形未解。不得把“方向相似”写成“已经触及证明”。

## 1. 当前项目最高几何定义

必须首先继承当前 source `main` 上的项目级定义，不得回退到旧 A2/rank-2 主语义：

- 平面原生结构正式名：**进取坐标系** / `ENTERPRISE_COORDINATE_SYSTEM`；
- 进取平面：`3` 个进取维、`3` 条原生无向轴、`6` 个有向方向；
- 三轴两两 `ENTERPRISE_ORTHOGONAL`；
- 相邻 `60°` 方向正负交错；
- 传统经典直角/正交坐标表示：**垂直坐标系** / `ORTHOGONAL_COORDINATE_SYSTEM`；
- BRC 目前正式定位为：`ORTHOGONAL_COORDINATE_SYSTEM ↔ ENTERPRISE_COORDINATE_SYSTEM` 的 collapse/realization bridge；
- 进取平方已恢复与普通代数自乘兼容；单三角结构称 `ENTERPRISE_HALF_SQUARE`；
- `3n` 旧 AC 读数重新定型为三边 incidence/boundary count，不是二维面积。

优先阅读：

- `PROJECT_DEFINITION.zh-CN.md`
- `PROJECT_DEFINITION.md`
- `project_definition.json`
- `definitions/ENTERPRISE_COORDINATE_SYSTEM_AND_BRC_BRIDGE_20260816.md`
- `definitions/ENTERPRISE_SQUARE_AND_ROOT_20260816.md`
- `definitions/R059D_STAGE_AC_COUNT_RETYPE_20260816.md`

## 2. 与正在运行的 R059D Stage AD 隔离

R059D Stage AD 正在独立运行：

`RS-R059D-STAGE-AD-TRIANGULAR-COVERAGE-BRC-CIRCLE-RESOLVE`

其任务是通过 triangular coverage / frontier / residual / resolve 研究定长线段在进取坐标系中的圆轨道及 BRC bridge。

Hodge Driver：

- 不修改 AD 分支；
- 不抢占 AD Researcher；
- 不重写 AD 的 source/target 语义；
- 可以把 AD 的最终 bridge 结果作为未来 realization comparison 的输入，但在 AD 冻结前不得假设其结论。

## 3. Hodge 靶心

经典 Hodge 猜想的目标必须保持精确：对光滑射影复代数簇 `X`，研究

`H^{2p}(X,Q) ∩ H^{p,p}(X)`

中的有理 Hodge 类是否由余维 `p` 的代数循环的有理线性组合产生。

专项不得把以下较弱命题误称为 Hodge：

- 找到一个拓扑闭链；
- 找到一个网格 cycle；
- 重建 Betti number；
- 得到一个 `(p,p)` 型离散对象；
- 在有限样本上拟合代数循环；
- 仅证明与 tropical/combinatorial Hodge 某些形式相似。

真正缺口始终是：

`Hodge class -> Enterprise cycle -> algebraic cycle on X`。

最后一步必须是严格的 algebraic lifting theorem，不能靠命名完成。

## 4. 专项最高研究图

目标不是直接攻击未知四维实例，而是建立下列链条：

`algebraic variety X`

`-> Enterprise realization E(X)`

`-> Enterprise chain/cochain complex`

`-> H_E^k(X)`

`-> Enterprise Hodge-type grading / filtration (if it exists natively)`

`-> comparison map Ψ_X between Enterprise and classical realizations`

`-> Enterprise cycle theorem`

`-> algebraic lifting theorem`

`-> classical Hodge conclusion`。

任何环节失败都要保留为真实负结果。

## 5. 第一原则：先证明不是普通换坐标

Hodge structure 是坐标不变量。若 `E(X)` 只是经典空间的另一张坐标图，则本专项没有新的 Hodge 内容。

因此 Stage H0/H1 的第一个硬问题是：

`ENTERPRISE_REALIZATION_IS_NOT_MERE_COORDINATE_REPARAMETRIZATION`。

必须给出可检验标准，例如：

- 原生状态空间不同；
- precision/collapse/fiber 是结构的一部分；
- metric/direction/cycle realization 不由可逆平滑坐标变换完全吸收；
- 但代数运算/组合结构仍能通过明确比较映射保持。

如果无法建立这种差异，专项应降级为 classical coordinate reformulation，不得声称 Hodge breakthrough route。

## 6. 推荐阶段

### H0 — Literature + Type Discipline

建立严格概念地图：Hodge decomposition、algebraic cycles、cycle class map、Lefschetz `(1,1)`、Hard Lefschetz、Hodge–Riemann、mixed Hodge、motives、tropical/combinatorial Hodge、non-Archimedean realization。

产物必须区分：经典 theorem / open conjecture / analogy / Enterprise hypothesis。

### H1 — Enterprise Cohomology Toy Model

只在简单可控对象上建立：

- Enterprise chains/cochains；
- boundary/coboundary；
- `d_E^2=0`；
- homology/cohomology；
- orientation；
- cup/wedge analogue（若自然出现）。

禁止先塞入经典 Hodge decomposition。

### H2 — Known Varieties Recovery

至少重建已知对象：

- `P^1`；
- `P^2`；
- elliptic curve；
- product of curves；
- simple toric examples。

必须与已知 Betti/Hodge numbers 对照，但经典答案只作 checker，不作 generator。

### H3 — Native Hodge-Type Structure

尝试从进取三轴/方向/胞元结构原生推出：

- bigrading or filtration；
- conjugation analogue；
- Hard-Lefschetz-like operator；
- Hodge–Riemann-like pairing/signature。

若只能人工定义成经典结构的同构副本，则报告 `NO_NATIVE_HODGE_STRUCTURE_FOUND`。

### H4 — Realization Comparison / BRC Lift

建立 `Ψ_X`，明确：

- source/target；
- kernel/fiber；
- precision；
- functoriality；
- product compatibility；
- cycle compatibility。

BRC 可成为这里的局部几何 bridge，但不得预设其可推广到代数簇。

### H5 — Lefschetz (1,1) Recovery

把已知 theorem 当第一座真正 algebraicity gate：

用进取机制重新证明 `(1,1)` 情形的代数性，而不是调用经典证明后改写符号。

若这一步无法给出独立 lifting mechanism，则不得推进未知 Hodge。

### H6 — Known Low-Dimension Hodge Recovery

系统覆盖已知低维情形，确认新机制不是只对 toy examples 有效。

### H7 — First Unknown Cases

只有 H0–H6 全部闭环后，才允许选择真正未知的 dimension-4+ target。

不得一开始就搜索“能过 Hodge checker 的公式”。

## 7. π 的历史动机与严格语义

用户在进取数论建立初期曾把“π 可能不是超越对象，而应来自更原生代数结构”作为长期动机之一。

必须严格区分：

- **经典 π**：标准实数 `π` 的超越性是 Lindemann 已证明定理；不得以当前项目为由声称经典 `π` 是代数数；
- **Enterprise π / π_E（若未来定义）**：若进取几何从圆/周期/面积关系原生地产生一个不同对象，可以研究其代数性质；
- 若主张 `π_E` 与经典 `π` 表示“同一更底层对象的不同 realization”，必须给出明确 bridge，而不是直接改经典 π 的算术类型。

π 专题可作为 realization philosophy 的长期压力测试，但不属于 Hodge Driver 的近期证明目标。

## 8. 科学红线

禁止：

- 把 Hodge 猜想改写成更容易的离散命题后宣称解决；
- 把 classical coordinates / classical Hodge answer 作为 Enterprise generator；
- 把“网格 cycle”自动叫 algebraic cycle；
- 把 integral Hodge conjecture 当成一般正确目标；
- 以有限枚举替代理论证明；
- 为匹配 Hodge numbers 增加 ad hoc operator；
- 静默改写 project-level Enterprise geometry；
- 干预正在运行的 AD；
- 删除失败路线或负结果。

注意：经典 Hodge 猜想使用有理系数；更强的 integral 版本一般不成立。Enterprise integer-first 不等于所有最终类必须保持整数系数。

## 9. 与外部数学的关系

优先参考但不继承其答案：

- classical Hodge theory；
- Lefschetz theorems；
- algebraic cycles / Chow groups；
- motives；
- tropical Hodge theory；
- combinatorial Hodge theory；
- non-Archimedean/tropicalization；
- nonabelian Hodge / P=W；
- homological mirror symmetry。

这些是 benchmark、conceptual neighbor 和已有 no-go/positive precedent，不是 target leakage 许可证。

## 10. 新驾驶员权限与仓库纪律

New Driver:

`EM-DVR-HODGE-4Q7M2K / HODGE_CONTROL_PLANE`

默认工作域：

- `research/hodge-*`
- `research_tasks/HODGE_*`
- `research_results/HODGE_*`
- `definitions/HODGE_*`（仅专项定义）

未经用户或总 Driver 明确批准，不得修改：

- `PROJECT_DEFINITION*` 的最高进取几何定义；
- AD 分支；
- 冻结的 R059D 历史结果；
- account-wide worldview。

专项任务必须继续遵守：commit checkpoint、clean ownership、exact theorem vs finite computation separation、target leakage prohibition、失败保留。

## 11. 当前完成度与推进目标

Handoff 时：

- Enterprise coordinate foundation: `~95%` for current plane semantics；
- BRC circle bridge: `ACTIVE / AD RUNNING`；
- Hodge-special conceptual route: `~10%`；
- Enterprise cohomology: `0%`；
- native Hodge-type structure: `0%`；
- algebraic lifting theorem: `0%`；
- unknown Hodge attack readiness: `0%`。

专项第一阶段推进向量建议：

`literature/type-discipline +35 / enterprise-cohomology +25 / realization-test +20 / native-hodge +10 / algebraic-lifting +5 / unknown-hodge +0`。

## 12. 第一条驾驶员判断

新驾驶员接手后的第一项工作不应是“证明 Hodge”。

应先回答：

> **进取数论究竟提供了一个真正不同的几何 realization，还是仅提供了经典代数对象的另一种坐标表达？**

只有前者成立，Hodge 专项才继续。

随后第一座硬验证门应当是：

> **能否用进取原生机制重建 Lefschetz `(1,1)` theorem 的 algebraicity，而不是调用经典证明？**

这是进入一般 Hodge 路线之前最重要的资格测试。

## 13. 外部权威状态锚点

截至 `2026-08-17`，Clay Mathematics Institute 仍将 Hodge Conjecture 列为未解决 Millennium Prize Problem，并说明其核心是 Hodge cycles 是否为代数循环的有理线性组合。

新驾驶员每次准备声明“突破/解决/已知边界变化”前必须重新核验最新权威状态。

---

Handoff disposition:

`HODGE_SPECIAL_CONTROL_PLANE_TRANSFERRED`

`AD_REMAINS_INDEPENDENT_AND_RUNNING`

`NO_HODGE_PROOF_CLAIMED`
