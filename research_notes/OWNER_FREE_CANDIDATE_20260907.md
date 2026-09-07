# Owner FREE candidate — 三轴边缘观察的七支点可恢复与八支点盲区

Researcher-ID: EM-FREE-20260907-MARGINAL

## Phase A 冻结包（下文审计不回改本节）

- Candidate-ID: `OWNER-FREE-20260907-3MARGINAL-7V8`
- Initial state: `BLIND_CANDIDATE_FROZEN`；候选类型是派生定理/精确负结果，不是替代 P000 的公理。
- Foundation snapshot: `enterprise-math@ef1893382`（owner 提供的当前源快照）。
- Worldview/P000 KB snapshot: `chatgpt-global-knowledge@ccd838a220b00ad44a7f5375fffeee8aa6afaaa0`；复用 owner 已验证的六小时同步租约。
- Freeze date: `2026-09-07`；先写本节，再进入 Phase B。审计时保存本节 SHA256。
- Primitive dependencies: `definitions/00_FREE_AXIOM_DISCOVERY_SUBSTRATE.md`、`p000_reality_foundation.json`、`definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json` 的有限正有理权重类型、`definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json`、当前世界观；不把任意 `N^6` 宣告为 native Cell。
- Blindness-status: `ANCHOR_EXPOSED`。启动时误做根目录名称列举；随后 owner 传来当前 X6 torsor 地址类型消息； mandatory P000 与 weighted substrate 文件本身也含下游名字。首个数学问题由六轴 Cell 与三轴观察及分支关联生成，但不申报 clean independent discovery。
- Semantic layer: 具有单射六轴坐标的**空间 Cell 中心上的有限非负有理质量分布**及其 raw coordinate marginals；路径身份、内部状态、相位和时间历史不由此定理恢复。
- Structural motivation: 单个 Cell 的所有三轴读出覆盖六个分量，但当不同 Cell 分支先按每个观察分别合并、跨观察身份匹配丢失时，联合关系是否仍能恢复？

**冻结候选。** 设合法 Cell 中心集合 `X` 已具单射六坐标读出 `c:X→A1×...×A6`。对其有限非负有理质量 `μ`，记每个三轴选择 `I` 的完整边缘质量表为 `M_I μ`，并保留观察标签 `I`。如果 `μ` 至多支持七个不同 Cell 中心，则所有二十张三轴边缘表唯一确定 `μ`，即使竞争分布不受七支点限制。若存在一个合法四轴二值矩形的十六个 Cell，则八个偶校验 Cell 与八个奇校验 Cell 的单位质量分布具有相同的全部三轴边缘表；并且每个边缘纤维的 `(C,W,M)` 也逐项相同。因此七/八界限在该合法性条件下精确。更一般，非零有限有理数组若全部 k 轴边缘为零，其正支点与负支点各至少 `2^k`。

- Immediate consequences: 原始三轴观察在稀疏空间分布层可能足够；完整正质量与 CWM 并不总能恢复跨观察四轴关联；已丢失的身份不能由重复换轴观察自动补回。
- Candidate falsifiers: 找到全部三轴边缘相同而一方≤7支点的不同非负分布；或上述合法十六 Cell 例子某个三轴边缘/CWM 不同；或本地归纳证明在切片处丢失了零边缘条件。Native existence 的审计失败只限制 sharpness 的内部实现，不反驳 P000。
- Explicit boundaries: P000 的六空间轴、120° 原生正角、signed primitive axis directions 与三力闭合均作为前提；本候选不研究其真伪；三轴坐标观察不等于三轴 slice 成员；支点数不等于路径数；这里的正负数组是两个正分布之差，不是物理 signed/amplitude 质量。

## Phase B 审计与证明

### 1. 审计状态与快照

- Source HEAD verified: `ef1893382eb1dcfcd773e19882569e9ff072a8ee`。
- Phase-A 初始文件 SHA256（含当时的 Phase-B 占位句）: `11538533B17998EEFBFEDD3CBAEFD57A4502EFEE57F424539681CD1274E2D8A3`。
- Mathematical status: **PROVED_DERIVATION**；下文给出完整有限归纳证明。Witness component: **EXACT_NEGATIVE_OBSTRUCTION**。
- Discovery disposition: **PRIOR_ART_ANALOGUE / DERIVED_NOT_AXIOM**。七/八极值结构和归纳技术有传统 trade 先例，不申报新原理、独创通用工具、Working Truth 或 Foundation。
- Owner 在收到冻结陈述后也重建了切片归纳论证；这是同一候选的交叉论证检查，不是 clean independent discovery，也不是正式 Driver review。

### 2. 精确对象与观察器

选定同一个 Cell anchor 与同一套有标签 signed 六轴坐标。设 `μ:X→Q_{>=0}` 有限支持。支点是 `μ(x)>0` 的**不同空间 Cell 中心**；同一 Cell 上的多条路径先聚合为空间质量时，其路径身份不属于待恢复对象。

对 `I⊂{1,...,6}`、`|I|=3` 与三坐标值 `a`，定义

`(M_I μ)(a) = Σ_{x∈X : coord_I(x)=a} μ(x)`。

观察器保留全部二十个 `I` 标签、每个 `a` 标签、精确质量与隐含零项。它不保留同一个 branch 在不同 `I` 之间的匹配身份。本文讨论的是这个明确的信息压缩；不是只留二十个总质量数字。

**Raw coordinate guard.** 当前源定义的 `Obs_I=can3(coord_I)` 还会减去三坐标共同最小值。本文 `M_I` 必须由 raw 三坐标，或等价的 `(can3(coord_I), min(coord_I))` 共同深度修复读出产生。只给 can3 的边缘表不满足定理前提。三轴坐标观察本身不证明被观察 Cell 属于以该 anchor 为中心的三轴切片。

**Future-operation lease.** 本结论的观察目标仅为空间质量分布及其函数；负例的下一步观察为四轴乘积 `F(x)=x_1 x_2 x_3 x_4`。未声明路径扩展、force scatter、signed amplitude、未知旋转或隐藏内部状态从此空间压缩中可恢复。精确可识别性也不自动给出有效求解复杂度或含噪稳定性。

### 3. 正负支点下界：完整证明

**引理。** 令 `f:A_1×...×A_n→Q` 为非零有限支持数组，`0≤k≤n`。若每个至多 k 坐标的边缘数组都为零，则

`|{x:f(x)>0}| ≥ 2^k`，`|{x:f(x)<0}| ≥ 2^k`。

**证明。** 对 k 归纳，允许维数 n 随归纳变化。

1. `k=0` 的条件是 `Σ_x f(x)=0`。非零有限数组总和为零，至少有一个正项与一个负项，所以下界是 `1=2^0`。
2. 设结论对 `k-1` 成立。因总和为零且 f 非零，支持至少含两个不同点，因此至少有一个坐标 j 在支持中取两个不同值。对任意取值 b 定义切片 `f_b(x_{-j})=f(x_1,...,b,...,x_n)`；至少两个这样的切片非零。
3. 对任意 `J⊂{1,...,n}\{j}`、`|J|≤k-1`，`f_b` 的 J 边缘就是 f 的 `J∪{j}` 边缘在第 j 坐标为 b 的那一片，故严格为零。每个非零 `f_b` 因而由归纳假设各有至少 `2^(k-1)` 个正支点和同样多的负支点。
4. 不同 b 的切片支持不相交。取两个非零切片相加，得到每种符号至少 `2·2^(k-1)=2^k` 个支点。证毕。

若只给全部恰 k 坐标的零边缘，对其额外坐标求有限和即可得到所有较低阶零边缘，因此同样适用。

这个证明计数**不同非零位置**，不把正整数权重的重数当作不同支点；因此直接涵盖非均匀正有理质量。它也不依赖任何轴间欧氏夹角。

### 4. 七支点唯一恢复

设 μ 非负、支持≤7；ν 是任意有限支持非负竞争分布，全部二十张三轴边缘表与 μ 相同。令 `f=μ-ν`。把合法坐标集以外的位置只作零值数组延拓；这是证明的计算载体，**不宣告这些位置是新合法 Cell**。

若 `f≠0`，引理 `k=3` 给出至少八个正支点。但 `f(x)>0` 蕴含 `μ(x)>0`，故 f 的正支点不可能超过七个，矛盾。因此 `μ=ν`。

结论是一方≤7即够，不需要预先限制竞争分布的支持大小。对应一般公式：全部 k 轴 raw 边缘唯一确定任意支持严格小于 `2^k` 的非负有限分布。

### 5. 合法八对八盲区及精确 BRC 计算

Phase B 已读当前源 `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md` §§2–3。它正式定义 `X6_NATIVE_SPATIAL=AFFINE_TORSOR(Z^6)`，signed unit axis translations 是合法原生邻接。故选 anchor `c_*` 后

`x_B = c_* + Σ_{i∈B} e_i`，`B⊂{1,2,3,4}`

是十六个不同且合法的空间 Cell 中心。可依轴标签顺序经原生单位步到达每个中心；多轴位移仍是 composite path，未引入新的原生方向。这里不要求十六点位于单个三轴 slice，也未增加第七条空间轴。

令 μ_even 在 `|B|` 偶数的八点各放单位质量；μ_odd 在奇数的八点各放单位质量。两分布支持不交。固定三轴 I，令 `r=|I∩{1,2,3,4}|≤3`。每个可出现的读出值恰固定 r 个活动位，剩余 `4-r≥1` 位里偶校验与奇校验各占一半，故两分布对应纤维均有

`C = 2^(3-r)`，`W = 2^(3-r)`，`M = 1`。

因此全部二十张完整 raw 边缘表逐项相等，每一纤维的 CWM 也逐项相等。由于这些路径权重全为1，连**未标签的精确权重直方图**也相同。两边全局都有 `(C,W,M)=(8,8,1)`；若归一化为概率，则两边为 `(8,1,1/8)`。两种约定均有 `E=W/M=8` 与形式读出 `Delta=LN(8)`，不需要数值计算对数。

这实际复用 `t0.weighted_brc_cwm` 的有限正权分支接口：单支权重1输入 `(1,1,1)`；替代分支合并用 `(+,+,max)`。脚本直接调用现有 `cwm_from_positive_weights`，没有重写 CWM 运算。

**可显露的联合方向。** 对 `F(x)=x_1x_2x_3x_4`，

`Σ F(x) μ_even(x)=1`，`Σ F(x) μ_odd(x)=0`。

所以四轴联合方向不能由这些三轴边缘表合成。对于此一对见证，增加 F 即可区分；这不声称 F 是全体空间分布的完整修复坐标。原生平方长度的**整张分布**也能区分：偶侧 `L_E^2` 直方图是 `{0:1,2:6,4:1}`，奇侧是 `{1:4,3:4}`；平均平方长度相同不足以代替其分布。

### 6. can3 单支点反例与旋转范围

取 `z=(0,0,0,0,0,0)` 与 `z'=(1,1,1,1,1,1)`。两个合法 Cell 不同，位移原生平方长度是6，但全部 can3 三轴读出均为 `(0,0,0)`。在其上各置一个单位支点，全部 can3 观察和 CWM 都相同。因此 **can3-only 连单支点唯一恢复都不成立**；七支点保证绝不能省去共同深度条件。

相对于 raw 三轴边缘表，已知的 `S6` 轴置换仅重新排列二十种选择和坐标标签，不能把上面的四轴相关盲区变成可见。此句只覆盖在各次观察间丢弃分支匹配、最终仅保留各张边缘表的统计协议。若持续跟踪每条分支身份，或允许引入别的已证明原生旋转操作，则观察器变强，本文没有否定其恢复能力。

### 7. 去重与工具复用判定

按 `tool_invocation_policy.json` 与 account BRC first-line contract，冻结后运行现有 toolbox coverage。保存完整结果：`owner_free_20260907_coverage.json`、`owner_free_20260907_coverage_marginal.json`。首次控制台输出受 Windows GBK 编码限制，改以 `python -X utf8` 成功完成；未把环境编码问题归为数学能力缺口。

| 匹配 | Resolution | 实际用途与边界 |
|---|---|---|
| `t0.weighted_brc_cwm` | `REUSE_APPLIED + REUSE_EXECUTED` | 逐纤维应用 `(+,+,max)`，直接运行既有正有理 CWM 实现。CWM/权重直方图均不能恢复已丢弃的跨观察标签关联。|
| `t1.triaxial_directional_defect` | `NOT_APPLICABLE` | 其 native-hex X-ray/宽度证书的域与本次六坐标产品边缘不同；接口还明确排除 binary/nonlinear tomography。不能挪用其唯一性结论。|
| 当前 X6 torsor 与 common-depth 修复 | `REUSE_APPLIED` | 提供合法四轴矩形、固定 chart、raw 与 can3 的类型区分及 S6 观察重标记边界。|
| 其他宽查询返回的 recurrence/Newton/holonomy/算术方法 | `NOT_APPLICABLE` | 此处是有限静态坐标质量与边缘求和，未声明它们所需的 recurrence、Newton 或算术任务结构。|

精确 `marginal` coverage 无词法命中不等于确认全库能力缺口。另做有界源码/定义/笔记检索，读取到 `X6_TRIADIC_ATOMIC_SCATTER_AND_BRC_CORRELATION_V1_20260906.md` §6 及其 frontier 汇总：既有结果已指出单 token Boolean marginal supports 不恢复三 token atomic closure。本结果与它同属 joint-correlation 保留原则，但对象不同：这里保留全部三坐标**质量表与 CWM**，证明空间分布的七/八 sharp threshold；不把既有 triadic closure 结论改名为本轮新发现。有限检索范围内未找到完全相同的内部陈述；这不是全库无重复或方法创新证明。

**外部先例。** Ghorbani、Kamali、Khosrovshahi、Krotov 的 [On the volumes and affine types of trades](https://arxiv.org/abs/1810.02296)（最终版2020；[期刊全文](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v27i1p29/pdf/)）明确记载非空 `[t]`-trade 的已知最小体积为 `2^t`，并把 binary array 差与该结构联系起来。把二值坐标向量识别为其1位置子集，本文单位权重偶/奇构造正是 `[3]`-trade 型：三轴完整边缘相同与所有至多三坐标交互计数相同可由有限容斥互换。因此本轮不以该极值或归纳方法的新颖性立项；记录的是其在 current signed X6、合法 Cell、raw/common-depth 观察和精确 BRC 分支语义中的可审计应用。非均匀有理权重的**支点数**下界由本文直接归纳证明承担，不仅靠引用“volume”一词替代。

### 8. 精确有限检查及交付边界

运行 `python -X utf8 research_notes/owner_free_20260907_check.py` 得到 `PASS`，输出 `owner_free_20260907_check.json`：

- 完整声明总体为全部 `2^6=64` 个二值 chart Cell，无奇偶/合数类预先删除；四活动轴的15种选择、其余两位4种背景，共60个十六 Cell 矩形全部核对。
- 比较了1200张成对三轴边缘表、5280个成对 CWM 纤维；全部相等。
- 核对四轴乘积 `1 versus 0`、两张平方长度直方图，以及 can3-only 单支点对角碰撞。
- 一般七支点唯一恢复依靠 §§3–4 的数学证明，**不是**有限枚举证明。此脚本属于已选候选的精确见证回归，不冒充独立随机验证。

Script SHA256: `9337AE66ABFDCB732240AB26B992DBFD3578B5CFE740744AFC5FA465B6C67946`。

Result SHA256: `E1B960E565939EC50C4808D5B8B4FC918B08BEFF5E214ECAF71700A818DA2F04`。

本有界单元已完成：冻结、完整证明、合法性审计、工具实际复用、现有/外部去重、精确见证均落盘。没有修改共享基础，没有创建任务/claim/review，没有外部发布或提交。后续若 owner 选择集成，只需将本 observer 条件与已有 joint-correlation 条目相接；无需重新证明 P000 或把已知 trade 技术包装为新公理。

Researcher-ID: EM-FREE-20260907-MARGINAL / FREE_AXIOM_DISCOVERY

Global-Knowledge-Sync: main@ccd838a / GLOBAL_KNOWLEDGE_V1
