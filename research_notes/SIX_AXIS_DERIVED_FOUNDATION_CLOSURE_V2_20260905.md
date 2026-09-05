# 六轴派生基础闭合 V2

Date: 2026-09-05
Status: `DERIVED_LAYER_CLOSED / EXACT_PROOFS + PRIMARY_SELF_CHECK + INDEPENDENT_REFERENCE_CHECK / NOT_NATIVE_X6_PROMOTION`

## 闭合对象

在 P000 六空间维前提、当前 FCC/cubic Barlow 六线族载体、四个重叠 120° 三轴切片与现有 Weighted-BRC 类型边界下，本包闭合以下派生共同层：

1. 四切片是 K4 四顶点星形，六轴是 K4 六边；保持该图册的六轴标签自同构群恰为 S4 的边作用。
2. 12 个 `(slice,axis)` incidence flags 有显式 proper FCC carrier 旋转读出；S4 作用严格等变。该读出不是 native 6D 欧氏嵌入。
3. 局部 120° 朝向的共享边符号连接完整分类：每个三角面乘积为 -1 的连接恰有 8 个，构成一个顶点 gauge 轨道；唯一 S4 不变连接是六边全 -1。该标量连接不自动解释成 native 曲率/自旋/物理相位。
4. 三/四切片局部 min-zero 数据的粘合充要条件是共享边差的一维 cochain 在每个已观察三角上的循环和为 0；满足时存在唯一全局 min-zero 六计数重建。全部非负 lift 恰为 `n0 + h·1`，所以四切片共同只遗失一个公共深度。
5. 任意三个切片 + 公共深度足以无损恢复六计数；任意两个切片一般不足。
6. 六计数合成等价搬运为 `min-zero residual + common depth + S4 frame`；公共深度进位是精确非负 2-cocycle。它与旧最优星形提取 `K` 的 compression carry 严格区分。
7. BRC 接口保留 source/target、具名分支 occurrence、正有理权重、重数、六轴 grade、旋转 frame 与原始 length；不匹配端点在类别代数中贡献 0。
8. 形式长度端口消元闭合：对 `T=[[A,X],[Y,D]]`，`W=D+Y(I-A)^(-1)X`，边界 resolvent 与 determinant factorization 精确成立；边界 label、hidden determinant 与原参数 pole guards 保留。
9. 在“六标签实计数上的 S4 不变二次型 + 全部现有同切片两活跃轴勾股律”这个明确候选类中，全部形式恰为 `Q_c(n)=Σ n_e² + 2c(n_AB n_CD+n_AC n_BD+n_AD n_BC)`。写 `J` 为取 K4 对边的对合，则 `Q_c=<n,(I+cJ)n>`，谱为 `1+c`（重数 3）和 `1-c`（重数 3），正定 iff `-1<c<1`。所以当前局部理论不足以唯一选择全局二次度量；缺口恰为一个跨切片对边标量 `c`。选择 `c=0` 是新增正交性公理，不是既有定理。
10. 原生模型接入被压缩为可检查 contract：给出 native 状态/具名分支及 S4 候选作用后，逐分支 action 保 source/target、axis label、weight 即唯一提升到自由路径类别；下降到任何声明 quotient iff 关系合同对 S4 稳定。

## 闭合成 no-go 的越界

- `12 FCC contact rays / 2` 不能推出 native 六维；六维来自 P000。
- carrier opposite ray 不能自动成为 native negative axis。
- 六计数不能自动成为合法 native Cell address。
- `S4` 是六轴 FCC atlas 的完整标签自同构群，但不能自动宣称为完整 native 6D rotation group。
- 三轴局部勾股律不能选择唯一全局 native metric；即使限制到上述二次型类仍差一个且仅一个跨切片标量。
- 负三角 sign product 不能自动解释成 native 物理 holonomy。
- 未具名/无端点/无重数摘要不能替代需要 provenance 的原路径。

## 仍属原生层的最小未决输入

1. `X6_native` 的状态/地址与合法性；
2. native adjacency/path category 与 quotient relations；
3. native axis readout 到 K4 edge/12-flag atlas 的等变映射；
4. candidate native rotations 在 `X6_native` 上的 action，以及是否存在超出 S4 atlas skeleton 的内部旋转自由度；
5. 若要唯一全局长度，提供至少一个真实跨切片 metric datum/axiom，并验证与现有三轴定律兼容。

## 自检与独立参考

主实现重新执行通过：4,096 六计数 roundtrip；16,384 任意三切片重建；98,304 CountAtlas 旋转一致性；2,401 全部二值局部 chart 包中恰 69 个兼容；600 大整数合成/2-cocycle；6,912 branch group checks；1,536 quadratic covariance checks；symbolic Schur、prefix、port/context、pole-guard 与 7 个 targeted mutants 全通过。

另写独立参考检查器，故意不 import 主 `six_axis.py` 或旧 `vendor.atlas_brc.py`，从 K4/S4/tetrahedral 定义重新构造并通过：864 独立 rotation/flag checks；16,384 独立三切片 roundtrips；穷举 64 个 sign connections，恰 8 个属于固定三角乘积 -1 gauge class；独立 SymPy 求得 metric family eigenvalues `1-c`×3、`1+c`×3。

这些仍是同一研究执行内的独立实现自检，不是外部同行审查、Lean 或全仓库 CI。

## Artifact

- readable source: `experiments/six_axis_foundation_v2_20260905/`
- exact packaged snapshot: `artifacts/six_axis_foundation_v2_closed_20260905.zip`
- ZIP SHA-256: `1996482ec63a4f5278c117e8349b807daf99e913ab7fa4a66f04751322c00d9d`

## 收敛判定

在当前可用公理/定义下，派生六轴共同层已经没有未分类的内部缺口；余项全部属于需要新增 native 输入的原生层。后续其他研究若只使用 atlas/count/frame/BRC/formal-port 语义，应直接复用本包；若需要 native Cell identity 或唯一 global metric，必须显式触发上述原生输入门槛，不能从派生层静默补足。