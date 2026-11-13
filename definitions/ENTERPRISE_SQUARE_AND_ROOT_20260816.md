# 进取平方与开方 — 历史路线索引

Status: `SUPERSEDED / HISTORICAL_PROVENANCE`
Original date: `2026-08-16`
Reconciled: `2026-08-21`

本文件最初从旧零原点/A2 型几何讨论平方与开方，后续又曾被 origin-one / signed-origin-one 路线接管。上述坐标 ontology 曾由 2026-08-20 三正向扇区/原点零模型取代；现行 P000 V5 进一步确立了以实际 Cell 为锚点的六轴有符号原生空间。

## 当前可安全保留的代数事实

在**历史固定正向双轴 chart** 内，分量平方读出可写为 `a^2+b^2`；这一正向 chart 不是现行完整原生 Cell 身份。当前 signed 六轴 X6 对声明的原生位移 `d∈Z^6` 使用 `G(d)=Σ_{i=1}^6 d_i^2`，选定 signed 三轴则取相应三项。

标量平方/开方关系在 `r>=0` 时为 `sqrt(r^2)=r`，作为代数读出保留；它不依赖 signed-origin-one、unit-origin circle 或旧三角面积证明。

历史固定正向 chart 的 path-valued square-root 对象见：

`definitions/ENTERPRISE_PATH_VALUED_SQUARE_ROOT_OPERATOR_20260821.md`。

该定义把 `sqrt(r^2)=r`（`r>=0`）作为标量读出，同时保留满足 `a^2+b^2=r^2` 的 ordered nonnegative component-root branches 及其**chart-local** 多路径纤维。迁移到当前 signed-X6 路径时需保留实际 Cell 起点、所选轴、符号和路径次序。

## 不再使用的历史证明链

不得从本文件或后续 origin-one/signed-origin-one 文件恢复：

- native origin = 1 或 `±1`；
- native zero 不存在；
- 旧 signed-origin-one/chamber ontology（不同于现行 X6 的六轴 signed primitive directions）；
- 旧 unit quadrilateral / initial circle 作为当前 square law 的 foundational proof。

这些只保留在 Git 历史中作为 provenance。
