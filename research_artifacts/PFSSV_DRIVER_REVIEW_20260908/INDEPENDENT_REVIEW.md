# PFSSV 冻结回传的有界独立审查

结论：**不批准原回传所称的硬目标完整完成。** 已有源可作为历史实验和粗 null 失配的诊断记录保留；不给新 residual candidate 的决定有根据。但 `REFUTED_AT_TESTED_SCALES_AS_A_NEW_RESIDUAL` 与 `Unresolved residue: NONE` 超过当前设计和持久化输出能支持的强度。建议 Driver 按既有合同要求有界补证／修订；本记录不是正式 Review、Result 或状态变更。

审查输入为 main `154d649a419bf72fac1b2bf5cb6426a878ac9dbe` 的任务书，以及从 source `1cac434cb9ac542a38a8e7bb6defa414fefb2e4d` 原样恢复的七个文件。限定阅读任务书、return、manifest、discovery freeze、summary、checker。ER/RR 仅纳入原字节 pin 比较，没有审查或更改其权限。七个恢复文件与该 source 的 Git 对象完全一致，执行前后不变。

## 1. 主要缺口：观测命中条件进入了两个基线

[checker 第 64–85 行](https://github.com/awdawmip/enterprise-math/blob/1cac434cb9ac542a38a8e7bb6defa414fefb2e4d/scripts/check_prime_factor_semiprime_shell_residual_validation.py#L64) 先精确生成候选 prime p 的整数 q 窗口和素数计数，然后在第 71–72 行执行 `keep = counts > 0`。后续 `p`、`qlo`、`qhi`、分层组、Null A、rank、`smooth_profile` 和 `smooth_null_artifact` 都继承这个筛选。

对观察直方图，删除零权行不改变已观察总数。对 null 和平滑基线，它却改变了可被赋值的位置集合：这里保留的是“实际 q 窗口已经命中素数”的 p，而非只由 p、X、壳宽和整数几何决定的候选 p。

实际小核验固定 X=100000，独立 trial division 构造至 50500 的完整素数表；原 `shell_cell` 在两个已公开 discovery 壳上执行。全整数直接对乘另核 raw 与两 trim 计数，与历史记录一致：

| 宽度 | raw pairs | 有非空整数 q 窗口的 scale-trim p | 原函数保留 p | 被删零素数窗口 | 被删位置的正平滑期望总量 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 1/100 | 237 | 59 | 44 | 15 | 11.840328204718341 |
| 1/1000 | 25 | 41 | 12 | 29 | 5.867714049252224 |

这里已排除 `qlo>qhi` 的几何空窗口，因此表中的删除确实取决于实际素数命中。宽壳的平滑质量从全部几何候选上的 85.61094960451904，变为保留位置上的 73.77062139980069；窄壳从 9.00842329041607 变为 3.1407092411638455。随后原第 245 行还将这个受选择的基线重新归一化到观测总量。

一个精确 stratum 例子：宽壳 p=109 和 p=139 都在 band 5、p mod 30=19，分别位于 z-bin 15、17。其 q 窗口为 [918,926]、[720,726]，实际素数计数为 1、0；原函数仅保留 109。139 的平滑期望仍为 1.0632802727717179。窄壳另有同 band 6 / p mod 30=17 的 p=167、197，窗口 [599,599]、[508,508]，计数 1、0。删去零位置会把原可包含正／零两个位置的分层组变成只剩一个位置，改变置换分布和可出现的方差。

**精确限定：条件于非零支持的随机化本身不自动是错误的统计问题。** 但必须明确给出这一条件化目标及相应的 null；现有任务书要求检验完整壳占据、控制局部密度，现有报告又称 surrogate 只含第一阶 q 密度和 shell 几何。该 surrogate 的位置掩码事实上还使用了实际 q 素数命中。它不是不含观测 q 结构的纯第一阶基线。相关 0.799…、选中分数和事后符号反转只能支持这个条件性诊断，不能单独证明真实 residual 已由密度／几何完全解释。

原报告指出粗带置换破坏 p 到 q 窗口的细尺度耦合，这一设计担忧成立。Null B 在已形成的 Z 上打乱相位，不能修复 Null A 的均值／支持选择问题。两个旧 holdout 数值通过同一筛选器，也不使这个筛选器自动满足正确基线的科学条件。

## 2. prime_rank 不是任务书要求的素数秩坐标

任务书第 114 行要求 `(pi(p), pi(q))`。manifest 将它缩为 eligible-p 的归一化 rank；[checker 第 128–129 行](https://github.com/awdawmip/enterprise-math/blob/1cac434cb9ac542a38a8e7bb6defa414fefb2e4d/scripts/check_prime_factor_semiprime_shell_residual_validation.py#L128) 又具体使用 `arange(len(p))/(len(p)-1)`。这是零行删除后的幸存 p 行序号；未计算 `pi(q)`。

实际同一 X、同一个 p=23，其真实 `pi(23)=9`。原坐标在宽壳为 1/43，在窄壳为 0。p=29 的真实秩为 10，原坐标分别为 2/43、1/11。更直接地，以同一 retained p 集合上的真实 pi(p) 做首尾归一化，所得 profile 与原 `prime_rank` profile 在两个小壳都不同。因此这也不是简单省略一个共同偏移／尺度的正确素数秩图。

该问题不证明 density-flat 分支的数值必然错误；它说明任务书明确要求的一种 primary view 未被实现。不能用 metadata 改名把它补成已完成的 `(pi(p), pi(q))` 实验。

## 3. 必需 profiles 生成后被丢弃

`shell_cell` 返回五类各 24-bin profiles，以及完整 `zobs`、`znull` 和逐 p 窗口。然而 [serial_row 第 178–187 行](https://github.com/awdawmip/enterprise-math/blob/1cac434cb9ac542a38a8e7bb6defa414fefb2e4d/scripts/check_prime_factor_semiprime_shell_residual_validation.py#L178) 只输出总数、trim 总数、square 数、一个选定 bin 的 Z 和最大绝对 Z。

本次实际调用证实五类合计 120 个 profile 数值及完整 24-bin residual 均不在序列化行中；冻结 `result_summary.json` 的 21 行也均无这些向量。平滑校正只保存 discovery 聚合一个数和两 holdout 聚合数，没有逐 `(X,eta)` 的完整 corrected profile。

因此任务书第 139 行要求的逐 cell raw/corrected occupancy summaries，以及第 143 行要求的固定坐标跨尺度 residual profile 和 signed phase/correlation 输出未完整持久化。一个 `max_abs_Z`、选中 bin 和全局 surrogate correlation 不能重建这些输出。原代码可以作为后续可重复计算的来源，但这不等于原执行的必需数据已经交付。

## 4. 其余范围核查

- 精确枚举主干的整数 shell 上下界、p<=q、`p**4>X` 判定正确。两个小 cell 的 raw、两 trim、diagonal 计数与独立 trial-prime 对乘及历史表均相同。本次没有据此声称已重验原 21 个大 cell。
- 原报告的 21/21 spotcheck 和两次 blind holdout PASS 是旧来源中的历史声称；本次未重跑、未重新认证其盲性或当时 chronology。
- 冻结 manifest 有完整 X/eta/bin/seed/置换与选择参数；原源码也确实计算 max statistic 和两 null threshold。其含义仍限于所实现的模型。不同模型下事后校正值的符号反转，不是新盲测或校准后的排除定理。
- checker 第 277、285 行硬编码 `preregistered_screen='PASS'` 与 `terminal_class='RESIDUE_OR_DENSITY_ARTIFACT'`，不是根据全部 gate 动态判定；spotcheck 布尔结果也仅被写入。今后程序 exit 0 不能被用作科学 gate 自动通过的证明。此事实不改变原已写数值是否满足其旧规则这一独立问题。
- 边界还有一个明确的描述差异：manifest density-flat 声明 `u<=1/2`，代码却收至 `p<=sqrt(U)` 后把超出 z=1 的值 clip 到末 bin。宽壳内 `317^2=100489` 是合法 pair，且 317>sqrt(100000)，故在宣称区间之外被折进末 bin。此处不直接反驳选中 bin 10，但 diagonal 仅计数，未体现为独立移除／对照分析。
- 原 `is_prime_mr` 的七个 bases 并非一般 64-bit 确定性合同。本次实际核得合数 `10670053*32010157=341550071728321` 被原函数返回 True。该反例超出原最大 q=50500000，不能据它推翻原有限区间的 spotcheck；它仅要求收窄通用“64-bit”标签，或另有充分实现／范围证明。

## 5. 任务硬目标与可接受的收尾范围

| 必需输出 | 本次审查判断 |
| --- | --- |
| 1. 精确 generator + 独立 spotcheck 路径 | 主干存在；两小 cell 独立复核通过；原全量／21 spotcheck 未重验 |
| 2. 冻结设计 manifest | 参数与 discovery freeze 存在；保留原历史代次 |
| 3. 每个 cell raw/corrected summaries | 总数存在，完整 profiles 与逐 cell corrected 向量未交付 |
| 4. 两 null 家族 | 两种机制存在；完整占据与纯密度解释受观测支持掩码问题限制 |
| 5. 固定坐标 residual profile / signed cross-scale 输出 | 选中 bin 的 composites 存在，完整 profile 未持久化；prime-rank 实现不符 |
| 6. family-wise max threshold | 原定义下的阈值、ranks 已记录；不能转作正确科学 null 的保证 |
| 7. 冻结 holdout | 旧数值与规则已记录；本次非 blind 重算，未重放 holdout |
| 8. 分类型 return | 已有；完整反驳及“无剩余”的强断言需要修订 |

可以保留的最强稳妥结论是：raw 小因子通道很强；注册的粗带条件性筛选器出现了同相位 survivor；该筛选器具有可具体定位的密度／窗口与支持选择敏感性，因此其旧 PASS **不足以支持新的算术 residual candidate**。现有材料没有完成完整任务书规定的正确坐标、完整输出和密度控制，也没有证明所有 registered residual 已被排除。

所以不建议将原 `RESIDUE_OR_DENSITY_ARTIFACT` 加 `NONE` 原样作为硬目标已验收完成。该标签目前可保留为原作者对选定筛选器的历史解释；正式 Driver 可按既有合法状态要求修订／补证。也不能直接改成 `NO_STABLE_RESIDUAL_STRUCTURE_AT_TESTED_SCALES` 以绕过尚未完成的完整 gate；小因子 raw 图的诊断不足以覆盖 p>31 后的那个选定 feature。

最小未完成单元清楚且仍属于原任务：明确完整几何候选／条件性支持的 null 合同，给出所要求的真实 `(pi(p),pi(q))` view，持久化逐 cell profiles 和校正／相位输出，并让科学 gate 由实际数据计算。若今后在已打开的 holdout 上重分析，应如实称为事后重分析；真正新增盲检需要另行预注册，不能把旧 holdout 重新标为 blind。本次没有启动这些实验、修改原论文、要求新 claim 或自动建立 successor。

## 6. 实际证据与可重放边界

本次脚本：`small_boundary_review.py`，SHA256 `463a082b919283220892373f40d05a0f27bfe91ef2b8d3be13bc7c8998ff60f7`。

实际回执：`small_boundary_receipt.json`，SHA256 `d4f1f3c976c4fd9ed391e673c890eea0d5c8b5bc9c2222889687adcbde005f66`。进程 exit 0；脚本记录执行约 8.01796 秒。其 PASS 表示审查反例及保留边界被确认，不是原研究硬目标 PASS。

```powershell
& 'C:/Users/Administrator/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe' -B -X utf8 'D:/em/TEMP/pfssv-independent-review-20260908/small_boundary_review.py'
```

该命令只写相邻 TEMP 回执；导入原 checker 的定义但不调用其 `main()`，只执行两个已公开 discovery 小 cell。原 50.5-million sieve、注册 holdout 和全量统计没有重跑。不是新 blind test、native arithmetic 认证、正式 Review 或权限修复。

当前任务书 SHA256：`b4e6011b736026ab2a5fc247f8a3750163cd33909fe25cf04bec6391078157d3`。七个冻结源的完整逐路径 SHA 在回执中，其中 checker 为 `8772484435d77abf74e87a6f053a0edaf4fa9395bdbade93ede2413083f22140`，return 为 `78963ec2070cc872806fce3e252a4136aa58334f8fe27c86aa363d2a5bb58c05`。不把这些字节一致性检查当作 Result authority 验证；后者由 root 负责。

Global-Knowledge-Sync: main@114964c / GLOBAL_KNOWLEDGE_V1
