# signed X6 的静态 raw 三轴观察成本：完整稀疏度分类

- 日期：2026-09-07。
- 辅助工作包：`/root/stability_research`；`ANCHOR_EXPOSED / TASK helper`，不是新正式任务、claim、CLEAN FREE 声明或 live ownership。
- Global Knowledge 已读租约：`main@4fa7d7d0c19a5e80a681b33c8ee2ab643ce97563`。
- 本次文件冻结时本地 HEAD：`ac4fa6368614285ab73c1b0f67eb1292f187389e`。工作树中的本任务文件以末节 SHA256 为准，不把未提交内容冒充该提交树。
- 本文复用已证的有限零边缘正/负支点下界，解决其尚未给出的任意三轴查询子集及最少表数接口。没有声称新的 trade 下界、covering-design 方法或基础工具 family。

## 1. 冻结合同和结论

固定当前 signed X6 Cell torsor 的一个共同 chart。它包括一个整数 Cell anchor、六条 primitive 轴的排列以及各轴的正向/反向选择。用此 chart 将空间 Cell 中心写为 `Z^6`；目标与竞争分布必须使用同一 chart。这里只是既有 primitive 坐标的重标记，不增加一般 `GL6` 混轴或宣称新的原生物理旋转。

令 `μ,ν:Z^6→R_{≥0}` 均有限支持。目标满足调用方声明的 `|supp μ|≤s`，其中 `s∈Z_{≥0}`；竞争分布的支点数没有限制。空间支持先合并同一个 Cell 的质量，和分支标签数不相同。对三轴集合 `I`，一次查询取得全部带 raw 地址的质量表

`(M_I μ)(a) = Σ_{x:x_I=a} μ(x)`。

查询集 `Q⊆binom([6],3)` 是预先确定、每表成本相同、无重复的集合。没有附加的总质量已知条件。保证的准确含义是

`∀ μ≥0 finite, |supp μ|≤s, ∀ ν≥0 finite: [∀I∈Q, M_Iμ=M_Iν] ⇒ μ=ν`。

**定理。** 在上述合同下，保证条件与最小表数如下。表中轴编号为 1 至 6；Python API 使用 0 至 5。

| 目标声明上界 s | 查询集 Q 保证唯一空间质量的充要条件 | 最少表数 | 达到最少数的例子 |
| --- | --- | ---: | --- |
| 0 | Q 非空 | 1 | 123 |
| 1 | Q 覆盖全部六个轴 | 2 | 123,456 |
| 2 或 3 | 每个轴对都包含在 Q 的某张三轴表中 | 6 | 123,124,156,256,345,346 |
| 4,5,6,7 | Q 是全部二十个三轴集合 | 20 | 全部三轴表 |
| ≥8 | 不存在保证集合 | 不存在 | 全二十表仍有 8 对 8 反例 |

这不是根据所读表推断实际稀疏度；`s` 是未由该程序验证的输入前提。`COUNTEREXAMPLE` 表示该查询计划不能对整个目标类作保证，不表示调用方当前实际数据已经有多个实现。数学结论允许非负实质量；可执行 BRC consumer 使用既有精确正有理分支，零分布用空分支族表示。

## 2. 工具覆盖与复用决策

先冻结第 1 节的合同，再执行有界检索：

```text
python tools/enterprise_toolbox.py --json coverage sparse marginal uniqueness query cover parity trade BRC
```

原始结构化覆盖结果保存在 `experiments/owner_query_design_20260907/tool_coverage.json`。随后只读当前工具面、已定位的 observer/恢复文件、下表中的相关数学源，未整库无界漫游。词法结果只是入口，不是“库中绝无别的定理”的证明。

| 已定位工具/结论 | 实际处理 |
| --- | --- |
| `OWNER_FREE_CANDIDATE_20260907.md` 第 3–5 节 | `REUSE_APPLIED`：全部 k 轴零边缘的每种符号至少 `2^k` 支点；≤7 唯一性；四轴 parity 盲区。本文不重开这些已闭合结论。 |
| `OWNER_X6_STABILITY_20260907.md` 第 3 节 | 现有更强定量切片工具覆盖零残差特例；本任务不改常数、不建立另一份 noisy solver。 |
| `observer_certificate.py` 的 `Branch`, `fiber_histograms`, `raw_marginal_table` | `REUSE_APPLIED`：查询、空间支点核算、反例重验直接调用现有 consumer。底层继续使用 `WeightHistogram`。 |
| `recovery.py` | 接受全二十张 raw 表的有限候选恢复；没有本合同的任意 Q 最少表分类接口。保留原工具，不把此查询规划器称为求解器替换。 |
| `histogram_realization.py` | 全二十表、均匀二值六轴、逐权重层的实现判定；合同不同，不套用于本任务任意目标空间质量。 |
| T0 BRC / 精确权重直方图 | 保存正权纤维的真实质量与诊断数据；不能从 mass 表恢复已删路径身份。 |
| 三轴 directional-defect / native-hex tomography | 其支持域及 X-ray/directional-difference 观察合同不同；不作为本定理的替代证明。 |
| T2 finite certificate / typed incidence | 只识别证书/关联结构可用的思路；此次不调用不适用的独立块 max-law，不宣称新 family。 |

具体新增缺口是：将已存在的支点下界与有限 covering 条件组合，分类所有 `Q` 并为失败计划生成可直接交给既有 BRC 的正分布反例。新代码仅是任务内 consumer 和计划器。

## 3. 充分性的自足证明

先明确复用引理也对有限**实**数组成立。设非零有限数组 `f` 的全部至多 k 轴边缘为零，则正支点、负支点各至少 `2^k`。

证明对 k 归纳。`k=0` 时总和为零，非零数组必须各有一个正、负值。`k≥1` 时，若 `k=n`，全坐标边缘就是 f，自相矛盾；以下取 `k<n`。总和零的非零数组有两个不同支持点，所以某轴 j 在支持上至少取两个值。按 j 的值切片，至少两个切片非零。每个切片在任意至多 `k−1` 个其他轴上的边缘，等于原数组相应轴连同 j 的边缘中的该片，故为零。归纳给每个非零切片各至少 `2^(k−1)` 正支点与负支点；两个切片的支持不相交，合计得到 `2^k`。只使用有限求和与实数正负性，没有有理化或有限拟合步骤。

若 Q 覆盖全部 k 轴集合，任何 k 轴边缘可由包含它的一张完整三轴表对额外坐标求和得到。其他更低阶边缘也可继续求和。因此，对 `f=μ−ν`，查询表相等推出全部至多 k 轴边缘为零。若 `f≠0`，正支点至少 `2^k`，但 `f(x)>0` 必须有 `μ(x)>0`，故正支点数至多 s。当 `s<2^k` 时矛盾。

分别用 `k=1,2,3`，得到 s=1、s=2/3、s=4..7 各行的充分性。竞争 ν 无须稀疏，也无须落在预先猜出的有限 candidate carrier；只是与 μ 同样有限支持。

`s=0` 单独处理：μ=0。任意一张全表都读出总质量零；ν 非负，因此 ν=0。此处不能省略非负性，也不能将“目标是零”误当“无需观察就能排除任何竞争分布”。

## 4. 必要性与真实正 BRC 反例

设非空轴集 `U⊆[6]`，`|U|=t`。在 U 上让坐标取 0 或 1，其他轴坐标固定 0。所有这些 Cell 由共同 anchor 上有限 primitive signed 步合法到达。定义

`μ_U = Σ_{b∈{0,1}^U, Σb even} δ_b`，

`ν_U = Σ_{b∈{0,1}^U, Σb odd} δ_b`。

两边各有 `2^(t−1)` 个不同 Cell，全部为单位正质量。若查询 I 不包含 U，选一个 `u∈U\I`。翻转该位给出每个 I 纤维内偶点与奇点之间的双射；因而完整 raw 边缘表相同。这不是相减后的负质量模型，而是两个独立的正质量 BRC 分支族；相减只用于数学证明。

更强地，每个非空纤维的单位权重条数也相同，故既有 `WeightHistogram`、C、W、M 读出逐项相同。加强为未带原分支身份的纤维权重直方图，仍不能区分这些反例。

- 未覆盖某单轴时取 t=1，得到 1 对 1，否定 s≥1 的保证。
- 未覆盖某轴对时取 t=2，得到 2 对 2，否定 s≥2 的保证。
- 遗漏任一三轴表时取其轴集 t=3，得到 4 对 4，否定 s≥4 的保证。任何其他三轴表都不能包含这三个轴。
- s≥8 时任选 t=4，每个三轴查询都遗漏 U 的某位，全二十张表同时出现 8 对 8 碰撞；其任意子集当然也失败。
- s=0 且 Q 为空时，取 μ=0、ν=δ_anchor。两者没有被查询的区别，但空间质量不同。

前三项与第 3 节合起来给出所有查询子集的精确分类；没有仅检验少量集合后外推。第五项也是不假定总质量已知的合同边界。

## 5. 最少表数的证明及六表构造

s=1 时每表最多覆盖三个轴，覆盖六轴至少需两表；123、456 达到下界。

s=2/3 时固定某轴 i。它与五个其他轴的五个轴对都必须覆盖。一张含 i 的三轴表最多贡献两个不同邻轴，所以 i 至少在三张表中出现。六轴总出现次数至少 18，每表贡献三个出现次数，因此 `|Q|≥18/3=6`。这是解析下界，不依赖枚举所有查询集。

显式上界可以结构化构造。把轴分成三个二元组 `A={1,2}`、`B={3,4}`、`C={5,6}`，沿循环 `A→B→C→A`：对每条箭头，取源组的两个轴，再分别添加目标组的一个轴。得到

`123,124 ; 345,346 ; 156,256`。

每组的内部轴对重复出现两次。每两个组之间的四个跨组轴对恰由相应箭头的两张表全部覆盖。因而全部 15 个轴对被覆盖，达到六表下界。每轴恰出现三次。

检验中遇到的另一个六组候选 `123,124,356,456,145,236` 不成立：遗漏轴对 `16,25,34`。程序为其生成 2 对 2 的正 BRC 反例，不把提供的候选当成证据。

s=4..7 时每个三轴选择都有独立的四对四 parity 必要性，因此至少二十表，全部二十表达到。s=0 至少一表、s≥8 无法保证，已在前节证明。

## 6. native 坐标与观察遗忘边界

raw 三轴地址 a 与联合编码 `(can3(a), depth(a))` 一一对应，其中 `depth(a)=min(a)`、`can3(a)=a−depth(a)(1,1,1)`，逆变换逐项加回 depth。故若两者**在同一纤维联合保留**，本定理与成本完全相同。不能改成只保留 can3，或把 can3 与 depth 分别聚合后假定配对仍在。

具体地，单位质量 `δ_(0,0,0,0,0,0)` 与 `δ_(1,1,1,1,1,1)` 在全二十张 can3-only 表中都只有可见地址 `(0,0,0)`，但 raw 表与联合 can3/depth 表不同。因此去掉 depth 后，连 s=1 的充分性都失效。

所有证明允许任意共同整数 anchor、primitive 轴排列与反向，因为这是整个空间及每个相关 raw 地址上的双射。不同目标/竞争者使用不同 chart，或每张表另行实施未声明的混轴观测，不满足本合同。

三坐标是所选观察器的地址长度，不把 X6 或进取空间定义成三维。空间 Cell 质量唯一性也不恢复在同一 Cell 已汇合的路径身份、分支标签、内部状态、相位或时间历史。unit parity 反例可由既有正 BRC carrier 实现，不引入新基础公理。

## 7. 可调用接口与证书核验

实现：`experiments/owner_query_design_20260907/query_design.py`。不复制或修改底层 BRC/恢复器。

```python
from query_design import (
    SignedAxisChart, classify_query_set, minimum_query_plan,
    observe, verify_counterexample,
)

# API 轴编号为 0..5。
plan = minimum_query_plan(3)
assert plan["status"] == "GUARANTEED"
assert plan["global_minimum_table_count"] == 6

bad = classify_query_set(2, [(0, 1, 2), (3, 4, 5)])
assert bad["status"] == "COUNTEREXAMPLE"
assert verify_counterexample(
    2, [(0, 1, 2), (3, 4, 5)], bad["counterexample"]
)["valid"]
```

- `SignedAxisChart(anchor, permutation, signs)` 校验六个整数、轴排列及 ±1；提供相互逆的 world/chart 变换。
- `classify_query_set(s,Q,chart=...)` 校验 s、查询集合及 chart；返回所需 cover 阶数、逐子集覆盖见证或缺失集合、全局最少数、结论及前提标签。
- `minimum_query_plan(s,chart=...)` 给达到解析下界的计划。s≥8 返回全二十表的失败证书及 `global_minimum_table_count=None`，不把失败集合称为“最少”。
- `observe(branches,Q,chart=...,encoding="raw" 或 "can3_depth")` 通过现有 `raw_marginal_table` 读完整质量表。输入分支是既有正有理 `Branch`；零质量用空列表，不接受浮点质量。
- `verify_counterexample(s,Q,witness,chart=...)` 从原有 Branch/WeightHistogram 重算两个正分布的原始表、实际合并后的空间支持和空间差异。反例以规范 `p/q` 存储质量，SHA256 只绑定原始查询/s/chart 合同，不绑定 witness 的逐字节内容。修改权重或坐标后仍须通过完整数学核验；双侧等比例缩放、合法共同平移等若仍是真反例，应当接受。更改 s、查询或 chart 后不能直接沿用旧合同 hash。

`GUARANTEED` 的逻辑来源是上述定理及显式 cover witness；程序并不读取未知目标以验证稀疏性。输出恒含 `USER_DECLARED_NOT_VERIFIED_FROM_OBSERVATIONS`。失败证书核验不相信自报的支点数或相等标志；即使两个族分支标签不同，只要实际空间质量相同，也拒绝称为反例。

规划规模天然有界：至多二十张不同三轴表、十五个轴对和最多十六个 witness 分支（s=0 例外只有一条）。不运行无界支点枚举或 LP，不声明已提供稀疏恢复算法。具体目标恢复可继续调用适用合同下的既有工具；少表恢复的构造算法不在本次实现内。

## 8. 精确验证与可复查输出

运行：

```text
python -m unittest discover -s experiments/owner_query_design_20260907 -p test_query_design.py -v
```

结果：11 tests PASS（本次 0.247 秒）。验证包括：

- s=0..11 的分段最少数、空目标/空查询、返回值 JSON 可序列化。
- 6 个遗漏单轴、15 个遗漏轴对、20 个遗漏三轴的全部 41 种最大失败计划，逐个以现有 raw BRC 读表重验，并检查补入一张包含所缺轴集的表可区分构造反例。
- 六表构造的逐轴出现次数与逐对覆盖；错误六组例的三个真实遗漏轴对。
- s=8 的全二十表碰撞和四轴 raw 读出可区分。
- 非平凡共同 anchor、轴排列/反向，raw 与联合 can3/depth 的等价及 can3-only 碰撞。
- 两个有理正分支在同一 Cell 的质量汇合仍只算一个空间支点；声明 s=1 不等于从相同查询计划证明真实目标只有一个支点。
- 非法 s/轴/重复表/chart，以及篡改质量、位置、varying_axes、s、查询和 chart 的拒绝。

有限测试核验实现与具体 BRC consumer，解析证明承担所有有限支撑分布及所有查询集合的量词。测试没有拟合无限结果。

## 9. 外部先例、停止重复边界与剩余范围

Ghorbani、Kamali、Khosrovshahi、Krotov 的 [On the volumes and affine types of trades](https://arxiv.org/abs/1810.02296)（[作者期刊全文](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v27i1p29/pdf/)）记录 `[t]`-trade 最小非零体积 `2^t` 及相关二值数组框架。这里的单位 parity 是已有 trade 型结构；一般实权的正/负**支点数**结论由第 3 节直接证明，不能只把体积术语移用过来。

Gordon、Kuperberg、Patashnik 的 [New constructions for covering designs](https://arxiv.org/abs/math/9502238)（[作者大学托管全文](https://www.math.ucdavis.edu/~deloera/MISC/LA-BIBLIO/trunk/Kuperberg/Kuperberg5.pdf)）使用标准覆盖设计 `C(v,k,t)` 框架及 Schönheim 下界。本任务六表问题是 `C(6,3,2)=6` 的小参数情形；第 5 节给完整次数下界与构造，不依赖网络表格或枚举证明。

因此，若问题仅要求重证 trade 最低支点、经典覆盖数或已存在全二十表 ≤7 唯一性，应停止重复。本次结果的价值限于既有原生 BRC/共同 chart 合同下的完整查询计划分类与可核验 consumer。没有声称全局数学新颖性或新基础工具 family。

此合同现已闭合。加权表成本、适应性选表、按具体已观测数据缩减查询、少表的构造恢复算法、有限噪声下最优表组、带标签联合跟踪均未纳入；本笔记没有证明这些推广，也不据此创造新的正式 claim。

## 10. 来源与实现冻结

以下为实际读取文件的内容 SHA256；行号用于定位，不宣称仓库其他当前任务状态。

| 来源 | 定位 | SHA256 |
| --- | --- | --- |
| `research_notes/OWNER_FREE_CANDIDATE_20260907.md` | L43 raw guard；L49–70 引理/唯一性；L76–98 parity/框架边界 | `2fc21dfb799a5183b57e50e44f99d268530b63c8d4b87a965bb8ebfc12e0b7c6` |
| `research_notes/OWNER_X6_STABILITY_20260907.md` | 第 3 节有限定量切片 | `2915e70210dce5bc136c915e45e96a7c8a1f6dd414fae1590a4687f41bff3127` |
| `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md` | L23–41 signed torsor/anchor；L119–136 can3；L244–251 轴骨架 | `519a16725156be5461c6e28a0dcef664e267cff4e85120cfb257d5d540ec459e` |
| `experiments/owner_joint_observer_20260907/observer_certificate.py` | L26 Branch；L63 fiber_histograms；L75 raw_marginal_table | `93a2f2775ec919bc747fb339c52730f0eba7de99bed5dffba89a0fd1b1459d4d` |
| `src/enterprise_math/brc_histogram.py` | L53 WeightHistogram；L84 from_weights；L100 total_mass | `256ef167e2aee651c042195522a0013ba619f265f9e4d8fa24f07d3399695a67` |
| `experiments/owner_joint_observer_20260907/recovery.py` | L45 全二十表输入 guard；L79 recover | `503282c2b6c07f2a9fece03a16f242d3ae5442ed333990a073ce9d0daa5d3b24` |
| `experiments/owner_query_design_20260907/query_design.py` | L106 observe；L160 verify_counterexample；L209 classify_query_set；L252 minimum_query_plan | `b264d96f31dbe47f5c0b5411f6183ed4a484aa10e293fec42ccf0a15a6b1af97` |
| `experiments/owner_query_design_20260907/test_query_design.py` | 11 个测试方法 | `109ae7557e64b737239b9aa8e5a4f2d3fb8213e05e7e7371ce9362713410f990` |

本任务仅新写笔记与独占实验目录；未修改 canonical BRC、Foundation、旧审计定理或 taskbooks/claims，未提交或推送。
