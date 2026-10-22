# 数论、P11 与原生卷文献忠实性 QA

日期：2026-10-22（Asia/Shanghai）。来源快照：`awdawmip/enterprise-math@56f5938da3f707c1d9db1b39afde124eac4634e3`。

结论：本轮发现的五项文献修订已由对应整理作者完成，并已逐项回读当前 Markdown/JSON 的对应字段。**本轮检查范围内无剩余阻断项。** 这不是数学重新证明、正式同行评审、Driver 投票或定理准入；原始研究的未审状态和真实来源缺口继续保留。

## 检查范围与证据复用

- 数论卷：57 个条目的 ID、来源连接、来源状态规则与 10 个旧库复用的分离做了结构检查；定点比对 QR 四组付费界、CRT 正式记录、C27/C28 输入域、R1 25–27 层计算辅助链和 Hart 费用/计时历史。57 个 ID 唯一，10 个复用 ID 与之不重叠，57 条均连接来源并声明非本次新增接受。
- P11 卷：39 组数量与来源结构检查；风险抽查 fixed233、core98 零 first form/abstract Sel4/mixed bit、Magma 输入桥与 NO_INVOKE，以及 actual m7 coefficient obstruction。没有声称逐公式重新核查其余全部 39 组。
- 原生卷：14 个载体组的适用边界与来源状态；定点读取 quadratic/minimum、revisit/absorbing、critical63、boxed64/96、全 chart 两种不可能界、精确实数/有限标签读出，以及低 rank、R5、GEO6 的限定域。
- 复用已有合法 connector captures、原作者全文件提取和已有行政来源完整性检查；必要时只读取精确原文段。未新增逐 lemma 证书，未审查自己的 Student 卷，未运行科学程序、导入科学源码、计算或重放既有实验，未远程写入。

## 已修复的五项文献问题

| 条目 | 原问题 | 已回读的修复 |
|---|---|---|
| `NT-QR-SQUAREFREE-TABLE` | 独立条目的 `L=T+1` 缺少 N/c/T 与实际 QR predicate 定义 | JSON `hypotheses`/`applicable_to` 与 MD 补齐 odd primes `N=pq,3≤p≤q`、`c=ceil√N`、`T=(p+q)/2−c`、`L=T+1`，及 `(c+t)²−N` 的每个素模零 inclusive QR 条件 |
| `NT-QR-PRIMEPOWER-TABLE` | L/c 量词与 residual predicate 未明确 | 补齐 `N odd,c∈Z,L∈Z≥1`、完整 prime-power predicate、指数域、无额外 unit 限制，以及 distinct additive 固定正价格 |
| `NT-C28-SHARED-CALIBRATION` | “共同对称 readout bias”没有显式保存原文独立性及非扰动条件 | 明确 `Z′=ZH`，每个 control 内 `H` 与 `(Y,Z)` 独立、Y 不受扰动、两 control 共用同一 `γ>0`，无须样本耦合 |
| `NT-QR-PRIMEPOWER-TABLE.author_credit` | 只列历史 Root 贡献，漏辅助稿作者 UNKNOWN 的实际归属 | 同时保存 `UNKNOWN / DIRECTED_NONBLIND` 辅助作者与 Root FBF223 提供局部构造/Owner/六别名的贡献；未虚构注册身份 |
| `P11-EXECUTION-BOUNDARY.status_note` | 通用模板把 static NO_INVOKE gate report 写成已获数学 paper review | 改为独立静态 NO_INVOKE、无算术执行输出，明确其不是数学 paper PASS且不撤销另项 paper 结论；`p11-r11.review_scope` 同步标注 |

前两项依据原文 quotation41 第15–22行与 quotation42 第10–16、28行；C28 依据 quotation29 第42–50、64–67行；辅助作者依据 quotation42 第4行。上述 quotation 保留实际 source/ref/blob/member 字段，可由卷内注册表回到完整原文。P11 修订依据 `p11_sources/review_11.md` 的明确 NO_INVOKE verdict。

## 重点比对结果与继续保留的限制

**QR 付费界。** 原 periodic 新显表 lemma 的 `W≥λM+μ ceil((T+1)/M)≥2√[λμ(T+1)]` 及 `M≥1` 的 constrained relaxation 边界转录正确。squarefree 的 factorial/K(L) 与 `2^K(K+2)`、prime-power 的 density144 与 cost288 区分正确。CRT 的四项是原 Task 所要求的 exact index、paid ledger、primary comparison 和有限 Φ(L) 付费 obstruction，不是“四项无限制 factoring 结论”。实际 `DR-A1CDCEE97F3295286EE6` 为 ACCEPTED/destination NONE；原 RR 的 pending 文字与后续实际 review 分开，parent 与 S1/S2/S3 仍 OPEN/未证明。真 partial lists、任意不平衡分组、virtual modulus1、完整 prefix 检查和正费用限制都保留；未迁移到 rank-only、compressed/shared/batched、early success 或其他算法。

**C27/C28。** C27 universal direct conditioning 的 `rank H=E` 与局部特定参数的 `e_e0∈row(H)` 分开；neutral/disabled-source 局部 bridge 没有扩大为全13参数严格族。C28 known readout 的 `ker R⊂ker B`、left inverse、三视图的条件独立/正 bias 限制，以及共享 γ 的五参数公式与 `a_A=a_B` 分支保留。未把校准模型的可识别性当作实际仪器模型已成立。

**R1 25–27。** 条目保留 `COMPUTATION_ASSISTED / UNREVIEWED / NOT_ADMITTED`、后续继承先前未审 premise 和有限完整枚举前提。W24/W25、边界 D25/D26 数值与原 note 对应；未添加 W26 或任意 k 定理。来源明言本地 ZIP/program/log 不因 note 发布自动出现在 Source，整理卷保留该源码同步债；没有把两个作者级实现改写为独立正式同行接受或手证。

**Hart。** 定点比对 NEAR48、FAR48、NEAR56 原报告与 mandatory emission erratum：费用 amount2 不冒充 consumer 数；Fermat emission fee0 不冒充 consumer0；416/129、576/580等保存记录与完成返回数分开。CENSOR/缺失 paired comparisons 继续为 UNKNOWN，不补造 completed return 或失败时间；单个 TRAIN、先前 untouched 后已 opened fixture、named fee、wall/CPU、bit cost 与 RSS 均未混同。单输入已付 prefix 支配只在相同非负累积 fee contract 下成立。未来 producer、latch、Pocklington 计划均没有变成既有执行成果。

**P11。** fixed233 的 bounded paper rank1/Sha 结论不表示其被停止的 certificate Task 已执行；core98 仍 `rank∈{0,1,2}`、实际 mixed bit UNKNOWN。abstract Sel4 结构不冒充显式 cover；norm-square CRT 输入不替代 all-place Selmer 证明，Magma handbook/API 描述不等于 binary/runtime/export 已认证。actual m7 的负整数与 source `formal_17.txt` 对应，正式 `DR-053D71583987C94FEE06` 的 ACCEPTED 仅为 unshifted coefficient obstruction：`a=0` 是 polynomial extension，不是 `a>0` 或整数 gap `a≥1` 的 trace 反例；未称 HCM0 被反驳或 m7 最早失败。

**原生14组。** `X6-ABSORBING-FRONTIER` 实际用自己的 peer blob `26b75668c8241edaf43e57368ab974fd34105a30`，对应作者 blob `4ca67855107b8dd3276fd78a1e5629c93033d9df`；新 contact-free probe 与过去允许重访、未来 checkpoint 后吸收的语义明确，未借旧 nonabsorbing 票。`Θ(H^6)` 为共同 Cell/clock/固定容量 convention 的最坏容量，不是物理存储律。七 probe 最少仅对 odd m>1 的固定非自适应 scalar 类；critical63、single-box64、two-axis sharp96、早期93下界、124非 conformal 例和全 chart 量词互不冒充。实数 gap 的 worst-fiber 上界没有写成每纤维上界，精确 irrational output 不冒充普通浮点或物理 sensor。低 rank n=1/2/3 未审、n≥4 原附件 gap，R5 辅助标签模型与 GEO6 typed application 的无物理推广限制均保留。

## 非阻断的库结构建议

数论 JSON 当前含 86 个不同 `(ref,path,capsule_member)` 的完整引文，共707,924个文本字符；未发现将同一 quotation 重复计为多个结果。1.49 MB 文件同时保存摘要、来源注册表和长引文，后续维护宜把完整引文移入**同快照证据附录**，主体条目引用稳定 source ID/member locator/hash，保留必要短引文。既有 raw captures 已存在，不必为精简重新抓取或重建证明；不要删除 member 路径、blob、字节数及 hash，也不要把附录数计成成果数。这只是文献组织建议，不阻止当前打包。

当前真实 Source locator 缺口没有被本 QA 填造或宣布闭合。若最终打包后文档字节变化，文档文件 hash 清单须按最终字节做行政更新；已有科学来源 OID/数学状态不因该更新变化。
