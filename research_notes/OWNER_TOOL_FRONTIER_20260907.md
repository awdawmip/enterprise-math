# Owner 工具前沿与历史去重，2026-09-07

状态：非 canonical owner 辅助研究报告；不发布任务、不创建 CLAIM、不提升 theorem/Foundation。

来源快照：本地隔离 checkout `ef1893382`；父 owner 已建立的全局 canonical snapshot `ccd838a220b00ad44a7f5375fffeee8aa6afaaa0`。当前研究边界来自 exact native router、weighted substrate、joint-observer preservation contract 与 toolbox reuse policy。普通 Windows Python 的 coverage JSON 输出出现 GBK `UnicodeEncodeError`，通过 `python -X utf8` 恢复；这是输出编码问题，未作为数学能力缺口。

## 本轮最可用成果

已落地并真实执行：

- `experiments/owner_joint_observer_20260907/observer_certificate.py`。
- `experiments/owner_joint_observer_20260907/parity_certificate.json`。

在 native X6 的四轴 0/1 立方体内，将末两轴固定为 0；前四轴偶数奇偶性的 8 个点与奇数奇偶性的 8 个点各赋单位正质量。20 张 raw 三轴边缘表逐纤维的**完整 exact weight histogram**全部相同，因而 CWM、dominant degeneracy、integer moments 和 weight-valuation readouts 也相同。四轴表则在 16 个地址上不同。允许一次未来操作“只保留前四轴全零的 cylinder，再读 total mass”，输出分别为 1、0。

这证明一个有限碰撞与未来操作不安全证书，**不证明**另一路正在独立审查的“任一 ≤7 支点非负分布由全三轴边缘唯一确定”命题。支点数指聚合后的空间支持数，不是任意 labeled branch 记录数。

适配器未把 label 差异混入 histogram equality 判定：原始 branch label、signed X6 coordinate、positive rational weight 完整保存在独立 provenance 字段，纤维记录同时指回各自 source labels。label 不同没有被宣称等价。单位权重的 valuation 为空是精确值；额外执行了 signed translation `(-3,4,-5,2,0,7)` 与共同权重 `2/3` 的检查，保持三轴 histogram 碰撞、四轴分离。

## 可直接复用的函数

| 接口 | 输入与输出 | 本轮状态 |
|---|---|---|
| `WeightHistogram.from_weights(weights)` | 有限正整数/有理权重 → coalesced exact weight histogram | `REUSE_EXECUTED` |
| `.count`, `.total_mass`, `.dominant_mass`, `.dominant_degeneracy` | histogram → CWM 与 dominant ties | `REUSE_EXECUTED` |
| `.prime_valuation_terms()` | histogram → 每个 exact weight 的整数素数赋值向量及重数 | `REUSE_EXECUTED` |
| `operation_descends(domain, operation, partition)` | 封闭有限状态域、全定义确定操作、当前观测分区 → 是否下降 | `REUSE_EXECUTED` |
| `stable_family_partition(domain, operations, initial_partition)` | 同上 → 所给操作族可下降的最粗细化 | `REUSE_EXECUTED` |
| `recurrent_port_signature(matrix, internal_indices)` | 有限非负有理矩阵、稳定内部块 → `(W_eff,Z_int)` | `REUSE_EXECUTED` |
| `recurrent_port_dynamic_equivalent(left,right)` | 同语义标号的端口签名 → total-mass contextual equality | `REUSE_EXECUTED`；端口标签的对齐仍是调用者前提 |

实验适配器给 consumer 提供：

```python
Branch(label, coordinate, weight=Fraction(1))
fiber_histograms(branches, axes)   # dict[raw_address, WeightHistogram]
raw_marginal_table(branches, axes) # dict[raw_address, Fraction]
all_three_axis_tables(branches)   # 20 个 axis-triple -> mass table
parity_branches(parity)           # parity 0 或 1，各 8 branches
cylinder_filter(branches, axes, address)
parity_certificate()
```

所有轴编号为 0 至 5。原始空间地址是 `Z^6`，没有 min-zero normalization、绝对值替换或删除共同深度。

## 三个方向的 owner 比较

### 1. X6 联合关系观察与稀疏恢复：本轮优先 consumer

**问题。** 全部三轴局部观察到底丢失什么联合关系，何种稀疏条件允许恢复？输出不能只是“发现同总量”，必须有 raw fiber histogram 碰撞、明确 joint observer 与未来操作失败证书。

**既有工具与复用。** T0 `t0.weighted_brc_histogram` 已完整解决每个有限权重族的 exact histogram、CWM、valuation；T6 已解决明确有限操作族上的分区细化；T8 relation-observable 模块主要输入离散 relation/source/observer，不能从“函数名相似”推定其已提供 X6 六轴分布的 20 表导出与空间恢复。通过 toolbox 对 `joint observer fiber projection X6 marginal histogram` 的覆盖查找，匹配到 T0/T4/T5/T6/T8/T9 与 histogram、Newton fiber/observer、operation-family 等 methods；随后对所需接口精读，采用 T0+T6 现有实现。T4 的 observation 必须先声明、T5 的整数精度并非本问题变粗机制、T9 无运输环，因此均不额外套用；Newton 工具是特定 residual-jet lease，不可直接移植其定理为 X6 marginal theorem。

**精确缺口。** 在已审查接口中缺少“输入 labeled X6 positive branch population，输出全部 20 raw 三轴 fiber histograms、源标签映射与 joint/future obstruction”的批量适配入口。这个缺口已由非 canonical 实验适配器填充，归类为 **T0/T6/T8 consumer composition，非新 top-level family**。这里没有把有限覆盖检索夸大为全库不存在任何相关程序的证明。

**最小目标与当前证据。** 已生成 8-vs-8 四轴 parity 碰撞、16 个四轴不同地址、cylinder 质量 1-vs-0。最小未完成数学单元是 ≤7 的精确唯一性证明及其适用竞争分布范围，由父 owner 独立审核。父 owner 的 `recovery.py` 计划用两个互补三轴表的笛卡尔积构造有限候选，过滤全 20 表，再作 exact rational 非负可行性求解。即使线性求解器成功，也必须复核全部原表；只有获得所需支点界并引用已审核的精确定理时才能输出全竞争分布唯一性。不能用 finite successful recovery 代替普遍证明。

**kill/closure。** 若 ≤7 命题的前提不足，保留 finite counterexample 与 consumer 工具，撤去唯一性模式；不撤去原生坐标和完整 provenance。若现有 X6 adapter 经 exact 证据已覆盖同接口，则合并入口而不是推广新家族。

### 2. 保留 native displacement 和 labeled words 的 port 工具：第二优先、先证范围

**已有部分远多于 total-mass port。** `WBRC-T30..T32` 已完成 positive-rational Schur collapse、合法 port contexts、最小 `(W_eff,Z_int)`；`WBRC-T33..T37` 进一步完成 fixed-length moments、length-aware port transfer、exact histogram 与 prime-valuation universal transfer。尤其已有

\[
\mathcal E(z)=z\mathcal B+z^2\mathcal Y(I-z\mathcal A)^{-1}\mathcal X,
\qquad
(I-z\mathcal W)^{-1}[B,B]=(I-\mathcal E(z))^{-1}.
\]

因此“给 port 加路径长度、count、exact rational weights、equal-weight multiplicity、valuation”不是本轮新定理。Semiring lifting、transfer matrix 与形式幂级数本身也是已明示的通用先例。不得重新发布这些工作。

**真实执行的边界例。** 一个内部 excursion 权重 `1/2` 与两条内部 excursion 权重各 `1/4`，调用既有 port 工具都得 `W_eff=((1/2,),)`，`recurrent_port_dynamic_equivalent=True`。调用既有 histogram 工具分别得到 `[(1/2,1)]`、`[(1/4,2)]`，CWM 分别 `(1,1/2,1/2)` 与 `(2,1/2,1/4)`。这只是 `WBRC-N12` 的现成类型边界再应用，不能被称为新反例。

**尚需精确定义的残余接口。** 输入显式 finite multigraph：边有语义 label、source/target port、正有理权重，以及声明的 native X6 signed step；给定有限路径长度 H 与允许 future port contexts。输出按 `(ports,length,raw X6 displacement)` 索引的 exact histograms，并为需要来源顺序的 observer 保留 noncommuting label words 或声明的 word equivalence certificate。仅把 label 计数当成非交换 word 不够；总位移也不等于路径历史。同一固定端点的所有路径若位移由端点差决定，displacement marker 是已知可重构量，不能人工声称新自由度；非平凡 residual 必须来自已声明 channel/cover/winding 或上下文读取。

**最小证明/反例目标。** 先在 H 有限范围证明串接时长度和 signed displacement 相加、权重 histogram 卷积、来源 word 连接，并证明端口上下文拼接的截断系数相同。给出同 histogram/length/displacement、不同 word 且被声明 future observer 区分的最小实例。若 observer 只读既有 `mathcal E(z)`，立即归为 `REUSE_APPLIED` 并关闭新方向。若确实需要 word-sensitive future readout，归为 T0 扩展/适配；没有先验理由成立新的顶层工具。

**硬边界。** 隐状态可被未来操作直接访问会破坏 port lease；有限 H 不升级为无界 horizon；positive weights 不编码 signed/phase cancellation；形式符号表示不构成低 bit complexity 证明。当前报告没有实现该 port 扩展，也没有宣称生产库全局缺失。

### 3. 声明未来操作后的最小 joint repair：已有 T6 的原生 consumer

**问题。** 只补一个能区分当前例子的标量，和对全部声明未来操作安全的修复是否一致？

**本轮实际执行。** 取四个 population 状态 `even, odd, origin, empty`，初始分区由全 20 张三轴 histogram 定义，得到 3 类（even 与 odd 同类）。声明确定的四轴 cylinder filter：even→origin、odd→empty，origin/empty 各自固定。调用 `operation_descends` 得 False；调用 `stable_family_partition` 得 4 类。这对该有限四状态域以及 filter 的任意重复，是现成 T6 给出的最粗安全细化。

**最小修复。** 对已知二元 pair，一个四轴 cylinder mass 读数或四轴 parity 读数足以分离；至少需要两个可观察取值，因为当前二者同类且一次 filter 后可分。它不是全 X6 分布的全局最小修复坐标。Parity 读数 `sum mass(x)*(-1)^(x0+x1+x2+x3)` 是外部 signed observer，输出 8 与 -8；并未把它当作 positive BRC signed branch mass。

**是否另立项目。** 默认不另立；此方向是候选 1 的可重用 consumer 组成。若 owner 声明多个 native 操作（如已定义有限域上的 filters/rotations/channel relabels），可复用 T6 编译最粗安全分区；只有操作语言、horizon 与 finite carrier 变化产生实际未闭合问题，才考虑推进。对无限状态/非封闭操作不能直接用有限 T6 的终止定理。

## 不应重新研究的精确历史证据

| 已完成能力 | 当前 exact 来源与历史定位 |
|---|---|
| signed X6 Cell origin、最短路径 multinomial、native 三轴切片与 min-zero observer 的区分 | `definitions/00_CURRENT_NATIVE_FOUNDATION.md`；`ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md`；`ENTERPRISE_X6_CENTERED_THREE_AXIS_SLICE_REBASE_20260905.md` |
| mass port collapse、context lease、最小 signature | `definitions/ENTERPRISE_BRC_RECURRENT_PORT_FOUNDATION_20260903.md`；`WBRC-T30..T32`；PR #1152/#1153；`src/enterprise_math/brc_recurrent_ports.py` |
| port collapse 不保 count/dominant/provenance，hidden future access 失效 | 同上 `WBRC-N12/N13` |
| primitive moment characters、有限 moment 完备性、length-aware port | `definitions/ENTERPRISE_BRC_UNIVERSAL_HISTOGRAM_FOUNDATION_20260903.md`；`WBRC-T33..T35`；PR #1155–#1157；`src/enterprise_math/brc_moment_transfer.py` |
| exact histogram 与 prime-valuation universal transfer | 同上 `WBRC-T36/T37`；`src/enterprise_math/brc_histogram.py` |
| 确定操作族的 descent、coarsest future-safe refinement | `T6_OPERATION_SAFE_QUOTIENT`；`src/enterprise_math/operation_quotient.py`；`quotient.operation_family_closure` |
| Newton full residual fiber、observer/horizon lease | `ENTERPRISE_BRC_NEWTON_FIBER_QUOTIENT_FOUNDATION_20260904.md` 与 `ENTERPRISE_BRC_NEWTON_OBSERVER_LATTICE_FOUNDATION_20260904.md`；只用于其 exact residual-jet 语义，不能偷换为任意 X6 投影最小性 |

## 验证与下一最小动作

运行 `python -X utf8 experiments/owner_joint_observer_20260907/observer_certificate.py` 成功，输出有限证书。另以 signed translation、权重 `2/3` 检查 exact histogram 碰撞不依赖于原点或单位质量；既有 ports/histogram 边界例也执行成功。没有跑全库测试，因为未修改 canonical library/registry；父 owner 可独立复核证书和完成 recovery consumer。

父 owner 的独立审核发现 list 型 coordinate 可在外部变化，已将 `Branch.__post_init__` 输入固化为 tuple，并执行 `test_observer_certificate.py` 中的精确回归：修改输入 list 后原始 branch 与边缘表都保持不变；随后重新生成有限证书。

建议 owner 本轮以“有限盲区证书 + 已有 T6 最粗修复 + 稀疏唯一性证明审核 + exact recovery consumer”闭合实际研究单元。下一代 native port word 工具仅在声明了确实读取顺序/渠道的 future operation 后启动，避免对已完成 WBRC-T33..T37 重复研发。
