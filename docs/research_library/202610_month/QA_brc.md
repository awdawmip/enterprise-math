# BRC／residual 卷独立文献忠实性 QA

固定当前 Source：`56f5938da3f707c1d9db1b39afde124eac4634e3`。对象为当前 `brc_residual.json` 的 **68 个文献单元**及相应 Markdown、coverage。此记录只核对文献转录、假设、引用和历史／当前状态；不是数学正确性评审、独立数学票或新准入。

本次发现一处必要工具适用边界遗漏，已由 curator 修正。修后，在本次列明的文献核对范围内没有未处理的阻塞项。没有运行科学程序、重做拟合、构造反例或验证新定理。

## 已修正事项

**BRC-R-059 的 T7 applicability addendum 原先未进入成果包。** 原 whole-review 明确要求同时消费该 addendum。curator 已通过 connector 读取固定 main 完整文件，加入 associated source 与完整 `mandatory_tool_applicability_addendum`，并补充摘要。

精确文件：`research_notes/owner_goal_20261016/reviews/gbrc_typed_section_nonauthor_c89dc6/T7_REUSE_INTERFACE_APPLICABILITY_ADDENDUM.json`，blob `e0f9c439b49ecd03bc6989c196369d239e98d434`；缓存 `s194.json`（本地核对材料：`/workspace/agent_artifacts/curation_all_recent_20261022/brc_sources/s194.json`）。

保留的条件是：实际 T7 调用要求非空 base／total、完整 total-space permutation image 的实际 staging、精确可哈希标签与投影；抽象空图有 singleton section 不授权直接调用当前 validator；有限 group image 本身不足以把无限 carrier 化为有限工具输入，须另有 sound／complete reduction。本成果是 paper-only COMPOSE，execution 为 0。当前 JSON 的 addendum 对象与缓存来源逐字段相等。

## 重点核对结果

| 单元 | 对照来源 | 文献忠实性结论 |
|---|---|---|
| BRC-R-059 | s059 输入／结论段，s061 verdict／边界，s194 全文 | 保留 finite、nonempty fiber、total-bijection、full action image、static equation 的域。原 PAPER_PASS 是 bounded conditional RESULT_ONLY；没有改成 R1-01 或 R1-02 接受。工具附加条件已补。 |
| BRC-R-113 | s109、s111、s113 | authoritative STOP 为准备时间耗尽且科学 imports／compiles／tests／runs 全为 0。carrier_bridge 的旧 “batch supplied” 句已有明确 stale warning，未当作实测结果。 |
| BRC-R-116 | s119、s122 完整接口／状态，对应原 return 与 review 摘录 | `MATHEMATICAL_PASS_PENDING_FORMAL_NATIVE_REVIEW` 与 raw `NO_GO` 分层保存。旧 standalone Lemma 3.3 已撤回；A0／J、全格点精确守恒、GL4(Z) 等假设保留；非可逆 A6 存在性仍未分类，parent 与 Native formal review 未闭。两个结构化接口与源逐字段相等。 |
| BRC-R-124／127 | PR1525 固定 head `6099d979…` 的 Markdown 与原 PR metadata | metadata 实际为 open、merged=false；成果明确为未合并分支文献。Markov 固定参数渐近、临界首项消失、幂权重的两阈值及有限留出限制均保留；历史算验没有写成新盲实验、普遍反平方或物理定律。 |
| BRC-R-128／132／133 | PR1526 固定 head `618def7f…` 的 Markdown 与 open metadata | 保留指定六轴条件通道、固定观察量、宏操作／单位步／reset 的区分。132 的新增 parity 构造属于原 reviewer 自己的研究；其对他人模型的复核没有被当成自己新增构造的独立评审。 |
| BRC-R-170 | s170、s171，关联 s174–176 的摘录／状态；historical_experiments_raw | `46bd4dbe…` 的历史 REPORT 可达与当前 main 同精确 REPORT／summary 路径 404 分开。11 类含 baseline controls，积分噪声不另计第 12 类；overlapping 历史检查计数不相加成独立实验。指标未定义、条件／无条件量与宽度／距离均保留边界。 |
| BRC-R-160／161 | s160 全文、s161 §A | 12 周期正脉冲是指定 preset controller 下的模型。clock sharp deadline 是 sample **index** `N=(L−1)(b+1)`，要求整数 `L≥2,b≥0`、`k0=0`、严格递增与总 skip budget；含初读时 worst-case readings 为 `N+1`。允许 hold 的 skew≤1 反例与严格时钟定理未混合。§B J1 已明确交 misc 单独采收。 |
| BRC-R-162 | s162、s163 | 固定 square contact-only 的 81-state CWM、正 `x=eta*lambda`、n=2 起点与 proposal-count 观察量保留。`E₂τ₃=(1+x)(24x²+8x+1)/(8x³)` 是 all-positive-x 条件模型公式；eventual reconnect 与先于空态概率分开。后续 identity publication 只更新创建时 REGISTER_PENDING，不变成 Task／Result 或数学准入。 |
| BRC-R-190／192 | 新加入固定历史 @8946／@b7bec 的来源、域声明与原文摘录 | 历史 synthetic baseline 与比较图／统计宽度分型明确；外部 d 维比较载体不替换原生 X6。未升级为引力、源探针耦合、物理力律或当前 main 可用实验根。 |

## 转录与来源校验

`QA_brc_quote_checks.json`（本地核对材料：`/workspace/agent_artifacts/curation_all_recent_20261022/QA_brc_quote_checks.json`） 保存静态文档校验结果：

- 68 个唯一 entry ID；所有 primary fixed ref 与 URL 一致。
- **483 个公式／结果／域或 review 引文块**，均是该 entry 已绑定 primary／associated／review 缓存来源中的逐字子串，未发现转录缺口。关联多稿的摘录按各自 source blob 匹配，不误当只有 REPORT 一份来源。
- F7 reviewed theorem interface、process status 与 GBRC mandatory addendum 均与固定来源结构逐字段相等。
- 每条 `new_tool_family=false`，本轮 scientific execution／new mathematical vote 均为 0。

来源的有效固定哈希及 connector 观察复用 curator 已完成记录；没有为每个 lemma 重新制造字节证明。实际语义阅读集中于上述关键输入、状态和适用边界；逐字子串匹配只是文档转录检查，不宣称对全部 483 块重新数学审核。

## 范围限制

最后一项 PR1525 changed-file metadata 分页已由 Root 与 curator 实际补齐：page4 为 19 条，合并 79 个唯一路径；PR1526 为 40 个唯一路径，coverage 两项均已标明 pagination_complete=true。这闭合所指 PR 的文件元数据清单，不把所列 68 单元扩张为全部 Git 历史的穷举。current 404 只针对已实际查询的精确路径与固定 ref，不是历史 Source 不存在。此 QA 不覆盖其后新增或改写的文献单元；若仅增加同源导航、去重或归档元数据，不产生新数学审核。

## 后续补充：第 69 组 BRC-R-200

本节仅新增核对 `BRC-R-200`，原 68 组的科学条款不重做。对象为 `brc_residual.json`／`brc_residual_publication.json` 与 Markdown 中的历史隐藏残差组，共 11 项子结果。完整静态阅读了历史固定 ref `b61af8438886a3c1eb8ff53297447837bd2ee507` 下 `experiments/brc_hidden_residual_20261003_fca717/` 的 REPORT、summary、HIDDEN_CORRELATED、HIDDEN_DYNAMICS、HIDDEN_PLANE、ROOT_REVIEW、CROSS_REVIEW 七份来源；本地缓存为 `s200.md`（本地核对材料：`/workspace/agent_artifacts/curation_all_recent_20261022/brc_sources/s200.md`） 至 `s206.md`（本地核对材料：`/workspace/agent_artifacts/curation_all_recent_20261022/brc_sources/s206.md`），精确路径／blob 对应既有 source index 和 actual connector 返回。历史可达不改写为当前 main 实验根可用。

发现的两处摘要边界已修正并同步工作版、发布版和正文：一是恢复轴平均递推的 `E_I[q′]`、`E_I[(q′)²]`、`E_I[A3′]`、`E_I[(q′)³]`，明确给定当前 H 与下一符号，避免写成逐路径恒等式；二是明示含 n 分母的标准化量取 `n≥1`，旧二维读出归零的条件四阶取偶数 `n=2m≥2` 且条件有正概率，零响应／`A2=0`／`S2=0` 时标准化未定义，不填 0。原文字面摘录没有改写。

| 核对对象 | 保留的原文假设、结论与边界 |
|---|---|
| P5 隐藏量 | 独立均匀轴路由且独立于整个符号过程；任意固定符号词的二／四阶与弱极限，同平稳对称 Markov 的六阶／混合四阶分开。纯 H 的“六阶首次识别”只限所列对称链、同一时刻的纯隐藏多项式矩，不排除第 2 步完整分布差异或更早联合信息。Gaussian 弱极限不决定格点点概率。 |
| 窗口、积分、乘性、振荡 | 确定权重的独立创新、旧更新顺序及完整有序队列／联合状态保留；原生位置 X 与响应 Q/Z、窗口及投影读出另型。零平方协方差不提升为独立；高阶闭包不是二阶生产矩模块自动具备的能力。原五组振荡完整套件为复用。 |
| P4 条件分布与路由 | 十二方向各 1/12 的 iid 核、正概率条件及所列三种组内路由明确。`Γ4=0` 的第 2 步反例仍有非 Gaussian 六阶差异；相同旧读出路径律不固定隐藏系数，也不固定 dominant refinement。 |
| 隐藏返回与响应驱动 | `P(H4_n=0)∼3/(π²n²)` 是声明差分格点上的隐藏返回时间概率律，与完整原生返回不同，不是距离／力律。显式响应耦合保留整数单位原生步，三次增长属于响应，不宣称守恒物理通量。rank4/rank5 是六分量读出支撑，不是新原生空间、Cell 地址或晶包层。 |
| 审核与旧计算 | ROOT_REVIEW 复核相关／动态他作者模块；CROSS_REVIEW 复核 root 的 plane 模块，不把作者自己模块的审核算独立票。均为原任务内交叉审查，不是 Driver／Native／Foundation／工具准入。本轮执行与新数学票均为 0。 |

**代码版本差异已显式保存。** CROSS_REVIEW 记载所审 `hidden_plane.py` SHA256 为 `07ae847ea90529378cb6cc05766dddcdc629ac837e8d70324f5e2bb437883c3b`；summary 最终来源哈希为 `3474b32f3d8d366f8248f177c9be9d901b1de3ea9d59645ee953812c31d5670c`。当前条目的 `review_version_boundary.identical_code_version_proved=false` 正确保留两者不同；既有数学推导及额外第 4 步 20,736 词检查按原报告登记，不称为 summary 最终代码的同版 whole 审核。

`QA_brc_hidden_source_checks.json`（本地核对材料：`/workspace/agent_artifacts/curation_all_recent_20261022/QA_brc_hidden_source_checks.json`） 记录新增组的静态核对：7 个来源绑定一致；30 个字面摘录块均属于已绑定来源且在 Markdown 中完整保留；工作版和发布版的该组科学字段一致；历史 summary 与 s201 逐字段相等。44,318／26,250／768／54 等历史计数有重叠，未相加为独立实验，也未复跑。修后本组没有未处理的文献转录／来源／状态阻塞；这不构成新的数学正确性裁定。
