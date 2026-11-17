# H0O 同一 TaskID 的定理保留与终局条件校正（2026-11-18）

**任务**：`RS-HODGE-H0O-NONSPLIT-WEIL-INTERMEDIATE-SUPPORT-FM-EXCEPTIONAL-CH3`；当前公开版本 `TP2-853EE36ED78FF34CC992`。此稿仅执行现有 P2 REVISION；作者角色为 TASK_RESEARCH，不执行独立 Driver 数学审核。

## 冻结范围、原输入与归属

保持原 very-general 极化 nonsplit [-3] Weil 六维阿贝尔簇 `A=A_gen`，`K=Q(i)`，H0N 的 `B_p` 分块和投影 `Pi_W`，实际的 K 相容极化同源 `lambda:A -> Ahat`，归一化 Poincaré 线丛 `P`，`Q=(id_A × lambda)^*P`，以及 `Psi_Q(F)=Rp_{2*}(p_1^*F ⊗^L Q)`。输入族仍为 **全部**在同一 A 上纯余维三的 coherent sheaves F；输出是目标 D^b(A) 对象。不添加 WIT、光滑支持、半齐性输出或预设 `Pi_W([F]_cyc)=0`。

旧 Result `RR-FB3CF77C4F611FDED79B`、旧 return 和全部 46 次历史有限检验均按原字节留存；本稿不修改它们，不将历史 PASS 叙述成新计算。其原作者 `EM-HODGEH0O-D39219`、H0N 原作者和先前 Driver 的贡献、检验与审查范围保留。

## 可复用数学链条

原 frozen H0O return 给出的证明为如下条件定理。在 Abelian 目标的 Todd class 为 1 下，标准 Poincaré cohomological Fourier–Mukai transform 使 `H^n(A) -> H^(12-n)(Ahat)`，因而目标 `ch_3` 仅来自源 `ch_3`。中间次数上 `B_p -> Bhat_{6-p}`，Rosati 共轭使 `lambda^*(Bhat_q)=B_{6-q}`，所以 `T_lambda=lambda^* F_P|H^6` 保持各个 `B_p`，特别保持 `W_K=B_0 ⊕ B_6` 及其补空间。原 H0N projector 是这两端块上的选择算子，故 `Pi_W T_lambda=T_lambda Pi_W`。两个因子为有理上同构，`T_lambda|W_K` 可逆。对纯余维三 sheaf，leading Chern component `ch_3(F)=[F]_cyc`。于是

```
Pi_W(ch_3(Psi_Q(F))) = T_lambda(Pi_W([F]_cyc)),
Pi_W(ch_3(Psi_Q(F))) != 0  iff  Pi_W([F]_cyc) != 0.
```

此式为**原报告已有的、在其载明前提下的种子守恒定理**，不是本稿新证明或独立复核的完整对外数学认可。它保证零 exceptional 源无法由该固定变换直接生成非零 exceptional 输出；未确定 exceptional 源是否存在。

## 六项原要求逐项对账

| 原要求 | 现存证据及边界 | 本次状态 |
|---|---|---|
| 1. 类型化核、源族、支持几何、目标输出 | 原 return §2 给出 Q、全部纯余维三 sheaf、Psi_Q 的 derived 输出 | 在原定范围提供 |
| 2. 精确 GRR 六次/余维三贡献 | 原 return §3 给出 degrees 反转与仅 ch_3 项贡献 | 在原前提下提供 |
| 3. 对 H0N B_p/Pi_W 的分块计算 | 原 return §4 给出两次互补映射、块保持及投影交换 | 在原前提下提供 |
| 4. 三项 terminal theorem 至少一项 | 三项均未由该 return 建立，详见下表 | **UNMET** |
| 5. 半齐性、除子代数、split 迁移、WIT/支持的对抗检查 | 原 return §8 有相应排除说明；真实正例存在性未证明 | 保留既有范围，非新增审计 |
| 6. 有限符号证书不代替无限论证 | 原 return §9 报告历史 46 项；无限链条用 GRR、Rosati、support-cycle theorem | 旧证书仅作为既有有限证据 |

## 三项原 terminal 替代条件（全部保持原定义）

| 条件 | 现存证据 | 是否达到 |
|---|---|---|
| A. 给出同一非分裂目标上的明确代数/导出 E，且 `Pi_W(ch_3(E)) != 0` | 原报告没有构造出正向源 `F` 或其 exceptional support cycle；只有条件等价式 | **NOT ESTABLISHED** |
| B. 证明所声明的整个 `Q` + 全部纯余维三 sheaf 族的所有输出投影均为零 | 由定理仅知该投影与源 support 的投影等价；未证明所有源的 exceptional 投影为零 | **NOT ESTABLISHED** |
| C. 精确证明该族不能在固定非分裂目标上实例化，并命名缺失条件 | 该极化目标上存在普通纯余维三 sheaf；Q、Psi_Q 实际可构造。仅一个 *正向成员* 的 exceptional support seed 尚未知 | **NOT ESTABLISHED** |

**普通成员实证**：选 `A` 上 ample 线丛 L 的充分大正幂，取三条适当一般的平滑横截除子 `D_i ∈ |L^m|`，交成三维 complete intersection `Z`。`O_Z` 是纯余维三 sheaf，`Psi_Q(O_Z)` 在固定目标上有定义。其 `[Z]=m^3 c_1(L)^3` 落在 divisor-cube 线，H0N projector 将其杀掉。这个成员说明**整族可实例化**，但它并非非零 seed。

**确切剩余**：在同一 `A_gen` 上构造并证明某个 `gamma ∈ CH^3(A)_Q` 的 `Pi_W(cl(gamma)) != 0`，或在严格的原始全族条件下证明相反的全域零定理，或找到真实的目标侧族实例化不可行证明。已证明的等价式只把正例转化为待解的 support-cycle 存在性；不能把“尚未找到 gamma”当作“gamma 不存在”。有理 cycle 的有效性问题也不自动产生 no-go：若投影非零，则一个有理 cycle 的某个不可约分量的投影非零，对应结构 sheaf 会给出可用的纯 support 候选。

## 精确纠正及交接

- 保留 `Pi_W(ch_3(Psi_Q(F)))=T_lambda(Pi_W([F]_cyc))` 及可逆性、H0N separator 和非分裂 [-3] 来源的条件证明。
- 将旧 Result 的 `SATISFIED_AT_POINCARE_POLARIZATION_...` 识别为**超过原硬目标授权的完成标签**；本次同 TaskID revision 的正确界定为 `NEGATIVE_BOUNDARY / PARTIAL`，原硬目标仍 `UNRESOLVED`，原第 4 条 `UNMET`。
- 不认定“只差 seed”构成原第三项“整个族不可实例化”的证明；普通 complete intersection 已提供家族实例。
- 撤销由超强标签推导的**自动关闭 H0O 路径**这一建议的证明依据，保留母目标 `HODGE_SPECIAL_OPEN_FRONTIER_ALGEBRAICITY_MECHANISM` 为 OPEN。若将来审查决定归档固定变换路线，应与原硬目标完成分别记录。
- 历史证明、历史 finite checks、H0N 投影证书、审查人贡献全部保留；不声称本次独立 replication、新数值测试、全 Hodge 命题证明、Working Truth/Foundation 晋升或下游新任务授权。

**建议的下一控制动作**：在此 same-Task REVISION 正式 Source 出版后，交由独立 Driver 针对新修订 return 进行现行 review。Driver 的复核是单独动作；本稿只是研究者提出的校正材料。