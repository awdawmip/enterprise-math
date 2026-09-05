# X6 universal completion：内生 S4 与二阶 companion / chart-holonomy 匹配

Status: `DERIVED / EXACT / CARRIER-COMPATIBILITY / NO_PHYSICAL_PHASE_CLAIM`
Date: `2026-09-05`
Depends on:
- `X6_NATIVE_UNIVERSAL_CELL_COMPLETION_V2_20260905.md`
- `SIX_AXIS_DERIVED_FOUNDATION_CLOSURE_V2_20260905.md`

## 1. 六轴 endpoint algebra 自己恢复四个 star

在 universal endpoint group

`G6^cell ~= Z^2 x Z/2`

中，把六个 distinguished positive-axis generators 记为

`E={AB,AC,AD,BC,BD,CD}`，

唯一非零 torsion element 记为 `t`。

直接由 normal form 可得：六轴的 20 个三元素子集中，

- **恰有四个**三元组的 endpoint sum 为 `0`，它们正是四个 K4 vertex stars：
  - `{AB,AC,AD}`;
  - `{AB,BC,BD}`;
  - `{AC,BC,CD}`;
  - `{AD,BD,CD}`。
- **恰有四个**三元组的 endpoint sum 为 `t`，它们正是四个 K4 triangular faces：
  - `{AB,AC,BC}`;
  - `{AB,AD,BD}`;
  - `{AC,AD,CD}`;
  - `{BC,BD,CD}`。

其余 12 个三元组既不和为 0，也不和为 t。

所以 K4 star/face atlas 不再只是一层外加 carrier 标注；在 universal Cell endpoint algebra 内，它可以从六个 axis generators 的三元返回关系中重新识别出来。

## 2. 内生 axis-permutation automorphism group

考虑保持六个 positive-axis generator 集合 `E` 的 endpoint-group automorphism。

任何此类 automorphism 都必须把“和为 0 的三元素子集”送到“和为 0 的三元素子集”，故必须保持上节的四个 star hyperedges。

保持 K4 四个 vertex stars 的六边置换群已精确证明为 K4 edge action 的 `S4`，阶 24。

反过来，每个 `S4` vertex permutation 都通过 K4 edge action 置换六轴，并严格保持 star relations、face class t 与 endpoint group law。

因此

`Aut_axis(G6^cell,E) ~= S4`。

这把原来的结论

`S4 = FCC six-line atlas skeleton`

提升为：

`S4 = intrinsic positive-axis permutation symmetry of the universal Cell endpoint completion`。

Scope guard：这只分类“把六条 distinguished native positive axes 彼此置换”的 origin-fixing endpoint symmetries；不排除未来存在不表现为 axis permutation 的更丰富 native internal rotation dynamics。

## 3. companion `t` 在 S4 下固定

`G6^cell` 的 torsion subgroup 只有 `{0,t}`，所以任意 group automorphism 必须固定唯一非零 torsion element：

`g(t)=t` for every `g in S4`。

同时 S4 在四个 K4 faces 上传递，因此“每个 face triangle endpoint = t”是完全旋转协变的 global statement，而不是某个选定 face 的坐标伪影。

## 4. 与已闭合 chart-sign connection 的精确 C2 匹配

六轴派生基础 V2 已独立证明：可以取唯一 S4-invariant shared-edge sign connection

`sigma_e=-1` for all six K4 edges，

于是每个 triangular face 的 chart holonomy 都是

`Hol(F)=product_{e in boundary F} sigma_e = -1`。

endpoint completion 中每个同一 face 的三轴 endpoint sum 都是 `t`。

因此存在唯一 C2 isomorphism

`phi:<t> -> {+1,-1}`

满足

`phi(0)=+1`, `phi(t)=-1`。

对每个 K4 face F 有

`phi( End(face-triangle F) ) = Hol(F) = -1`，

而对每个 K4 star return triple S 有

`phi( End(star S) ) = +1`。

这说明两个独立推导出的 Z2 结构在 K4 face/star incidence 上完全匹配：

`GLOBAL_CELL_COMPANION_C2 <-> CARRIER_CHART_SIGN_HOLONOMY_C2`。

## 5. 解释边界

该 isomorphism 是一个**有限代数/载体兼容定理**，不是物理解释。

不得自动升级为：

- quantum phase；
- spin；
- gauge field in physical space；
- extra spatial dimension；
- time bit；
- probability/sign amplitude。

尤其 Positive Weighted-BRC 不携带这个 signed C2 phase；若研究 observer 需要 chart sign，必须保留独立 signed/finite-local-system 标签，不能用 positive mass 冒充。

## 6. 结构意义

现在同一个 K4 结构从三条彼此独立的路线重现：

1. FCC six-line/four-slice incidence atlas；
2. universal native Cell endpoint return algebra；
3. local 120-degree chart-orientation sign connection。

而三者的 S4 与 face C2 都严格一致。

这不是证明 carrier 等于 native identity；相反，它提供了一个更严格的 interoperability certificate：carrier atlas 可以作为 native endpoint completion 的 faithful finite symmetry/readout skeleton，而不把经典 3D vector relations导入 native state identity。
