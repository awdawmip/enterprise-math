# 象限 / 符号 chamber 代数向量运算 — 历史路线

Status: `SUPERSEDED / HISTORICAL_PROVENANCE`
Original date: `2026-08-17`
Reconciled: `2026-08-21`

本文件原先以 signed-origin-one、六方向/符号 chamber 为基础冻结局部向量运算。其原有 theorem-critical dependencies 在 2026-08-20 三正轴中间阶段被替换；现行 P000 V5 进一步确立六维有符号 Cell-anchored X6，因此本文件不能作为当前 foundational authority。

2026-08-20 中间阶段的局部表示（**历史三正轴载体/观察者，不是现行原生平面**）：

- 载体三重交点 `O_E` 及其相对零表示；
- `THREE_POSITIVE_RAYS`（固定正向 chart）；
- `A_E={(a,b,c) in N_0^3:min(a,b,c)=0}`（相对/min-zero 观察截面）；
- 正二轴扇区 chart `S_12,S_23,S_31`。

现行原生基础是 `p000_reality_foundation.json` V5 与 `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md`：以选定的真实 Cell 为坐标锚点、六个 signed 原生轴及其正反单位步为基本空间结构；固定三轴是 X6 的受限 signed 子扭子，不能由三正向扇区充当原生全空间。`ENTERPRISE_RIGHT_ANGLE=120_DEGREES` 仍按 P000 的项目定义使用。局部 chart 的代数与跨 chart gluing 可在明确的受限/载体或观察者类型中重新推导，原 2026-08-17 signed-origin-one chamber 并非当前 signed-X6 结构。

保留原则：**局部 chart 运算可以存在，跨 chart 需要显式 gluing/transition；实现坐标不能自动晋升为 native geometry。**

本历史文件中的具体 signed-coordinate formulas 统一状态为 `REQUIRES_CURRENT_FOUNDATION_REDERIVATION`。原始完整文本保留在 Git 历史中。
