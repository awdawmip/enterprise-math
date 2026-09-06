# X6 上层结构自由研究任务集（2026-09-06）

Status: `DIRECT_USER_FREE_RESEARCH_SET / UPPER_STRUCTURE / X6-SPATIAL-FOUNDATION-CONSUMED`
Parent-Objective-ID: `PO-X6-UPPER-STRUCTURE-20260906`
Publisher: `EM-FREE-PI-PRIME-20260904 / FREE_AXIOM_DISCOVERY`
Base: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`

## 已冻结底座

本任务集不重新研究已经闭合的空间底座。直接消费：

- P000 V5：6D 空间 + 1D 时间、六轴两两进取正交、120° 原生正角；
- `X6_NATIVE_SPATIAL = AFFINE_TORSOR(Z^6)`；
- 十二个 signed primitive coordinate steps；
- `L_E^2=sum_i z_i^2`；
- `S6` 正轴标签置换骨架与 FCC/K4 `S4` 子图册；
- off-native apparent segment = composite native path / BRC multipath；
- primitive stable force arity = 3 with `TRIADIC_CLOSURE_E`；
- centered signed three-axis slice；
- 当前 FCC STAR 的 C6/C12 native microtrace、phase/refinement clock separation、half-turn principal root bundle。

禁止把 carrier 固定半径轨迹、经典 90° 正交、min-zero observer、路径总数、或 precision pro-state 静默当作 full native state/time/rotation identity。

## 任务依赖图

`ROTATION` 与 `TRIADIC` 为双主线；`TIME` 与它们交叉；`NONFCC-SLICE` 消费 `ROTATION`；`INTERNAL-STATE` 消费 `TRIADIC + TIME`；最终 `INTEGRATION` 汇总前五条。

| Priority | Task | 核心目标 |
|---|---|---|
| P0 | `RS-X6-NATIVE-ROTATION-DYNAMICS` | 从 Cell 微路径构造 rotation dynamics，区分静态 frame symmetry 与真实旋转路径 |
| P0 | `RS-X6-TRIADIC-CLOSURE-DYNAMICS` | 把三力平衡从 arity 定义推进到 Cell/路径/旋转上的闭合动力学 |
| P0 | `RS-X6-NATIVE-TIME-DYNAMICS` | 构造时间作为关系变化次序的最小状态，严格分离 physical phase 与 precision refinement |
| P1 | `RS-X6-NONFCC-SLICE-REALIZATION` | 为其余 16 个三轴 coordinate selections 构造 native rotation/path realization，并判定哪些可获得 carrier realization |
| P1 | `RS-X6-CELL-CHANNEL-INTERNAL-STATE` | 在空间 Cell torsor 之上构造 channel/internal state，不制造额外空间轴 |
| P1 | `RS-X6-UPPER-STRUCTURE-INTEGRATION` | 形成 `spatial × rotation × triadic × internal × time × BRC provenance` 的统一 typed dynamics |

## 第一轮攻击顺序

1. 先闭合任意三轴选择上的 signed C6 rotation generator；
2. 求所有 triadic generators 在六轴 frame 上生成的精确群；
3. 把每个 rotation macrostep 提升为 BRC Cell-path fiber，并检查 composition 是否要求保留路径 provenance；
4. 将该结果反馈给三力闭合和 16 个非 FCC 切片任务；
5. 再进入时间与内部态耦合。

## 成功标准

每条任务至少返回一种：精确定理、可执行有限证书、严格 no-go、最小缺失原生关系、或可供其他研究直接复用的 typed operator/tool。有限实验不得冒充无限或 Foundation 结论；任何信息压缩前必须通过 Joint Relation Observer Preservation 与 BRC provenance audit。
