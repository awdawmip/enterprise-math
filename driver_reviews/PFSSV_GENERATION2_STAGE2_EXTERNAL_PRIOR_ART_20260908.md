# PFSSV generation 2：有限支持统计先前工作咨询

日期：2026-09-08（UTC / Asia–Shanghai）。性质：`BOUNDED_EXTERNAL_PRIOR_ART_CONSULTATION`，供 Driver 评估已完成的 `RESULT_ONLY` 候选；不是正式 Driver review，也不是新的数学执行或统计模型研发。本咨询由先前执行助手整理，不主张作者独立性；以下外部来源与内部产物明确区分。

## 建议

建议接受本次有界容量反例作为 `NEGATIVE_BOUNDARY / RESULT_ONLY` 的依据，并停止使用旧 Null A 的“所有置换结果都可解释为指定因子窗口中的合法占据”这一解释。原科学 hard target 仍开放，不能据此宣判残差不存在，或宣布一切条件随机化无效。

有成熟方法值得参考，因而不必因这次失败而一概关闭有限窗统计研究。不过，下一步只有在能说明**随机对象、可识别的科学问题、条件信息和细窗口之间的耦合**时，才值得单独定义统计合同。当前证据没有给出这样的合同，也没有自动产生合法的替代 null。本咨询不启动新任务、随机化机制、盲测或程序实现。

## 实际审查对象及其边界

本次完整读取的回传是 `research_returns/PRIME_FACTOR_SEMIPRIME_SHELL_RESIDUAL_VALIDATION_REVISION_RETURN_20260908.md`，本地 SHA256 为 `907783453bed7593872901bdaaadffe8c3f91f29e3dd8460a4bd330a72de7fc9`。Owner 已报告该回传和实际产物发布于 `a82ced7bb227471c1b16fecb5a5e3d7ff72a5536`；Result `RR-BDA72F26E3786AD69EA5` 发布于 `24d314560a35cefe14d240deb3b44ed7cc24fa38`，Result SHA256 为 `45b8a21d91df9a87a2e1fc2370f795c2b3bb61526361d2c1508b7341a58b8a26`。这些远端发布事实继承 Owner 的回读，不冒称本咨询再次远端核实。

该回传记录：21 个原定 cell 的精确观测完成；原 Null A 的确定性容量审计在 21 个 cell 均发现违规，其中 18 个在旧 positive-total-row 子集上仍有可达反例，另外 3 个只有新增 zero-total target 的反例。18,090 个 cell/target/residue 表项存在重叠，不是独立试验或 p 值。以上是**内部已冻结证据的转述**，本咨询没有重新计算、解码轨迹或重新执行这些实验。

反例针对粗分层内逐模 30 通道独立标量置换的窗口占据解释：一个来源行的通道计数，以正概率被分给整数窗口中该残基容量不足的目标行。作为数值向量的置换仍可定义；失败的是把它普遍解释成既定几何窗口中的可容许配置。单格容量只是必要条件，满足它也不自动保证共享素数、细窗口或其他联合约束可以同时实现。科学 null screen、corrected/signed 判据没有因此完成；原 holdout 暴露事实仍不可逆。

## 五个最相关的 primary sources

本次最多允许六个来源，实际采用五个。分类含义：`EXACT_DUPLICATE` 需要覆盖同一因子窗口、行×残基置换及对应容量结论；`PARTIAL_ANTECEDENT` 是相同原则或数学障碍的既有论述；`ADJACENT_METHOD` 是不同对象或条件模型中的可借鉴方法；`NO_MATERIAL_MATCH` 只描述本次有界检索结果。

| 来源、日期与核读位置 | 分类 | 可以支持的判断及适用边界 |
|---|---|---|
| Jesse Hemerik、Jelle Goeman，*Exact testing with random permutations*；在线 2017-11-30，TEST 27 (2018)；§2.1、Theorem 1、§3.1。[出版社全文](https://link.springer.com/article/10.1007/s11749-017-0571-1) | `PARTIAL_ANTECEDENT` | 论文的有限群置换定理要求指定零假设下的分布不变性，并把条件轨道采样与一般 Monte Carlo 区分。由此不能仅凭“同一粗分层”就断言本研究行可交换。这是该定理的适用条件，不是声称所有有效条件随机化都必须采用同一个群构造。 |
| Fabio Rapallo、Ruriko Yoshida，*Markov bases and subbases for bounded contingency tables*；作者稿 v3 2010-01-19；§2、Corollary 1、Theorem 3。[作者论文](https://arxiv.org/abs/0905.4841v3) | `PARTIAL_ANTECEDENT` | 给定统计量的非负整数 fiber、格上界及结构零已有明确理论。不能把无约束表的移动规则直接套到任意受限支撑。Theorem 3 的普通 2×2 移动结论针对固定行列边际、严格正的单格上界；不能无条件推广至这里容量为零的格。连通性也不等于有限运行时间内已校准。 |
| Thomas B. Berrett、Yi Wang、Rina Foygel Barber、Richard J. Samworth，*The conditional permutation test for independence while controlling for confounders*；作者稿 v2 2019-05-07；§2.1–2.2、Theorem 1。[作者论文](https://arxiv.org/abs/1807.05405v2) | `PARTIAL_ANTECEDENT` | 粗化条件变量后在箱内置换，不自动保留原条件独立假设。CPT/CRT 的有效性依赖正确的条件机制；CPT 可以使用非均匀置换权重。素数窗口的条件分布、行的独立性与科学可识别目标并未由该论文替本研究建立。 |
| Asohan Amarasingham、Matthew T. Harrison、Nicholas G. Hatsopoulos、Stuart Geman，*Conditional Modeling and the Jitter Method of Spike Re-sampling: Supplement*；2011-11-18；附录开头、§A.1.2、§A.2 Proposition A.3。[作者补充论文](https://arxiv.org/abs/1111.4296) | `ADJACENT_METHOD` | 附录给出有限二元位置集合，固定预先划定窗口中的数量，在满足这些数量的有限 fiber 上按声明的条件均匀模型采样；交换性在该零假设下成立。这证明有限窗条件随机化有成熟实例。神经脉冲的窗口划分不能直接替代重叠因子窗口、素数和残基约束，也不赋予本任务盲性。 |
| SciPy 官方 `scipy.stats.random_table`，访问 2026-09-08；页面显示 v1.18.0 Manual；参数、Notes 与采样方法。[官方文档](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.random_table.html) | `ADJACENT_METHOD` | 提供独立性模型下、给定行列和的随机列联表分布及 Boyett/Patefield 采样。文档接口只有行列边际等参数，没有任意单格容量或结构零 mask；因此它不是当前几何约束的直接修复器。这里也不能将其分布说成所有表的无条件均匀分布。本咨询未运行该软件。 |

综合判断属于**既有原则的具体实例与部分先例**。这五个来源都不是已识别的 PFSSV 精确重复；本次检索没有找到 `EXACT_DUPLICATE`，不构成新颖性证明，也不支持首创统计方法的声明。

## 对 Driver 的可执行判断

1. 本次支持约束的负向边界可以独立于尚未完成的科学检验被评价。是否正式接受、登记或关闭父任务仍由 Driver 的现行流程决定，本文件不授予权限。
2. 如考虑后续合同，先确定到底随机化素数配置、合法占据，还是仅把计数向量作为抽象替代量。必须明确所条件化的信息、联合可容许支撑和目标问题；不能把三者混用。
3. 受限列联表和有限窗条件采样提供了设计基础，但“每格不超容量”不保证细窗联合可实现；“保持边际”也不证明所需交换性。模型和采样正确性需要分别说明，不能靠截断或反复重抽悄悄改变旧分布。
4. 如果无法给出与原 hard target 有联系、可识别的统计问题，则应关闭这一具体统计解释，保留已完成的观测与容量边界。若能给出，先评估该窄合同的价值，再决定是否另立工作；本次不自动继续。
5. 外部统计机制不自动符合进取数论的原生算术、BRC、观察投影或证据要求；也不恢复已暴露 holdout。此处只有先前工作咨询，没有新 family、API、native 认证或 blind gate。

## 检索范围与可复查性

检索于 2026-09-08 使用 OpenAI web search/open/find，确切十条查询及域过滤保存在同目录 `receipt.json`。特定 `semiprime` 与 permutation/structural-zero 查询未产生本次可以使用的实质匹配；这是检索范围内的 `NO_MATERIAL_MATCH`。本咨询没有执行全库文献综述，也没有把无匹配外推为全局新颖性。

核读的是上表列明的实际章节、定义与命题，不宣称对五篇来源做完整独立证明审计。Diaconis–Sturmfels 的 Stanford 技术报告元数据及作者目录可以找到，但原文链接访问失败，未作为第六个实质依据。jitter 主文的 PMC 页面遇到 reCAPTCHA，采用可读的作者补充论文；未绕过访问控制。

所有来源内容均作摘要，不复刻论文。没有运行数学脚本、随机化软件、LP、枚举或新 null；没有修改研究树、Result/Driver 记录、Issue 或 Git。输出仅为本目录的 `REVIEW.md` 和 `receipt.json`。

Global-Knowledge-Sync: main@b0b335f / GLOBAL_KNOWLEDGE_V1
