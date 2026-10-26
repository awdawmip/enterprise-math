# 离散世界的反证压力与经验兼容性任务集

日期：2026-10-26。父目标：OBJ-DISCRETE-EMPIRICAL-COMPATIBILITY-20261026。

## 研究结论与本次边界

本次搜集到的是能够排除明确模型族的条件性不可行定理，以及能限制具体传播、相位、物质和引力机制的独立实验。它们尚不构成“所有离散世界都错误”的证明，也不能被一句“只排除特殊模型”从我们的研究中排除。一个模型即使不满足某个定理的前提，仍须解释与该定理相关的实际实验。

本次完成文献核验、现行原生语义对齐、失败条件设计和十五项任务编写/发布。这里不宣称已执行十五项检验，不宣称现行模型已兼容这些现象，也不将任务出版提升为数学或物理接受。

用户最新方向是主动寻找反证：不能兼容时，应报告模型错误或缺失。现行基础文件以固定版本作为检验基线，不在本次直接修改；基线文件的保护不代表其假设组合免于经验反驳。若某冲突在所有明确允许的补全下仍然成立，必须如实上报基础层冲突，不能以既有文件的“固定”措辞掩盖。

## 一、先拆开“离散”到底意味着什么

| 主张 | 需要另外定义的内容 | 不能由它自动推出 |
|---|---|---|
| 空间由离散 Cell 构成 | 物理距离、关系、更新图、观察者读出 | 固定晶格、最近邻传播、光速必然色散 |
| 时间是离散事件/更新序列 | 本地钟、更新间隔与物理时间的桥 | 每次更新同样长、存在已知普适时间量子 |
| 每个位置只有有限状态 | 可组合状态、环境、记忆、状态类型 | 宇宙全部状态有限、概率只能取有限值 |
| 整个世界只有有限状态 | 边界、总容量、闭合性、动力学可逆性 | 任意连续群或无限精度量子关系可精确实现 |
| 某些测量谱离散 | 具体可观测量、系统与边界条件 | 所有频率、能量、位置和相位都离散 |
| 规律可计算/可模拟 | 输入、精度、资源和可计算性的含义 | 本体已被证明是经典数字计算机 |

有限精度的平滑曲线本身不能判定本体是连续还是离散。另一方面，反对一个具体离散模型并不需要先证明数学连续体是物理实在：Bell 和情境性检验就是有限设置对特定机制的反证压力。[BELL1964](https://journals.aps.org/ppf/abstract/10.1103/PhysicsPhysiqueFizika.1.195)；[HENSEN2015](https://arxiv.org/abs/1508.05949v1)；[MERMIN1990](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.65.3373)

## 二、现行模型真正要接受的压力

冻结的项目输入来自 enterprise-math@64044ada5e3e2b5d7b3c327942ee028da6e2a967，以及 Global-Knowledge main@1f73bff7ce37e663922e3c8dd29411441b0e37a7 的当前原生波路由。具体路径列于机器清单。

现行语义是六个原生空间维度及单独定型的时间，不能改释为三维空间的六个正负方向。三维限制或读出需要显式桥，并保持允许未来操作所需的联合关系；它不预设六维固定拆成三条可见轴和三条隐藏轴。精确保真与有限尺度近似读出分别按其承诺检验。原生120度关系不能直接当作普通欧氏平面角；三元稳定平衡也需要与表观两端平衡建立桥。

原生波模型允许非邻接跃迁和全域自洽更新，尚未提供固定“一格/一拍”的传播公理。因此不能先把它当作局域规则晶格，再直接用 Bell 或标准晶格色散公式判死。反过来，允许非邻接更新并不自动实现量子关联；允许全域关联也不自动保证不能传信。这正是任务02必须同时检查两边的原因。

激活、正分支质量、残差、相位和能量不是可以任意互换的词。当前原生激活并非概率振幅；公共余量也未因命名就成为经过验证的纠缠机制。现有局部阈值余量模型的有限验证，应保留其方向、阈值和无碰撞/回流等范围，不能推广成全世界动力学。

### 可直接复用的现有结构

本任务集实际复用 BRC 的类型区分与联合关系保真条件：若压缩把两个原生状态视为相同，则在声明允许的所有未来操作下，所需观测必须相同或有明确误差界。正权重质量、带符号/相位关系、精确直方图和来源信息分别定型。对相位、隐藏维度、公共余量和第三平衡项，均使用这一条件寻找最小信息损失见证。

这个复用不等于假定 BRC 已产生 Born 统计、手征粒子或引力。若现有类型缺少相位/测量/尺度接口，任务返回准确的 EXTEND_EXISTING_TOOL 缺项；不以新的通用工具名或经典数值模拟掩盖缺失。此次没有新增原生数学数值运行。外部成熟理论用于确定必须恢复的经验关系及条件障碍，不偷偷作为原生前提。

## 三、七类最有判别力的理论压力

### 1. Bell：共享隐藏信息是否仍只是局域正权重模型

如果联合分布可以分解为独立于设置的共享变量分布，乘上两端各自局域的响应，则 CHSH 量满足绝对值不超过2。共享变量可以很复杂、甚至无限多；关键是分解条件，而非隐藏状态数量。Hensen 等的有限设置实验已产生超过这一界的关联。[HENSEN2015](https://arxiv.org/abs/1508.05949v1)

对我们最有价值的分叉是：公共余量若保留此分解，就在已声明前提下失败；若不保留，要写明其具体更新机制，并检验远端可控设置不能改变本地边缘分布。“有非局域性”不是完整答案。设置独立性的改变也必须形成具体可检验模型，不能把确定性与不独立性直接画等号。 无信号检验使用实际可实现的受控设置操作分布；如果放宽设置独立性，须区分被动条件概率与因果干预，不能将共同原因产生的条件相关直接视为可控传讯。

### 2. 情境性：不能给所有测量组合共用一份朴素预存答案

Peres–Mermin 的有限关系展示了非情境赋值的矛盾。现实仪器还有顺序扰动和兼容性误差，故要用适当实验不等式，而非将理想乘法表直接当作带噪实验的全部判据。[MERMIN1990](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.65.3373)；[KIRCHMAIR2009](https://arxiv.org/abs/0904.1655v2)；[MAZUREK2016](https://arxiv.org/abs/1505.06244v1)

原生机制可以包含上下文，但要说明上下文如何进入状态、何时改变状态、怎样保持同一装置的操作等价。每换一种上下文就另放一张概率表，不能作为统一解释。

### 3. 干涉与组合：正权重计数缺少什么

两种准备可能有相同局部计数，却在重合时产生不同结果。如果压缩状态只保留局部强度，就会把未来可区分状态合并。任务04把这个问题化为最小保真见证，而非立刻要求整个量子理论。

三路径实验提供 Born 型统计的额外压力，但“机械开关狭缝得到非零 I3”不自动意味着违反 Born 法则；改变边界条件会改变传播。相关理论已明确讨论这一修正。[SINHA2010](https://arxiv.org/abs/1007.4193v1)；[SAWANT2014](https://arxiv.org/abs/1308.2022v2) PBR 只在准备独立性等前提下约束重叠的本体分布，不是一般反离散定理。[PBR2012](https://arxiv.org/abs/1111.3328v3)

### 4. 连续对称与离散点作用：精确、统计和涌现要分清

连通拓扑群连续作用于离散拓扑点集时，每个点的轨道只能是单点。这一基础事实可排除一种“离散点集上逐点实现非平凡连续对称”的强要求；其他作用方式须重新审计实际作用对象及其拓扑；若配置空间也取离散拓扑，同一引理仍适用。量子态、统计集合或观测读出不因名称不同就自动豁免。

Bombelli–Henson–Sorkin 对闵氏空间 Poisson 撒点证明，不能以相应可测、等变方式从撒点选出优选方向；其有限价图后果也依赖同一框架。这既说明离散性不自动导致优选参考系，又提醒精确洛伦兹兼容与简单有限邻接之间存在结构成本。[BHS2006](https://arxiv.org/abs/gr-qc/0605006v1) 现行六轴模型并非这个随机撒点模型，不能直接继承其结论。

### 5. 手征费米子：恢复波动方程还远远不够

Nielsen–Ninomiya 约束一类平移不变、局域而具有所定手征性质的晶格费米子。任务05必须固定具体版本，不能把若干版本的前提拼成口号。Lüscher 的原始论文明确列出自由Dirac算符的解析周期性、正确低动量形式、非零动量处可逆性和朴素手征反对易不能同时满足，并说明改变手征实现可以避开该版本。[NN1981](https://doi.org/10.1016/0550-3213(81)90361-8)；[LUSCHER1998](https://arxiv.org/abs/hep-lat/9802011v1)

因此不应说“晶格上绝不可能有手征物理”。真正要问：我们的实际机制使用哪一种手征实现？额外模态去了哪里？引入相互作用和规范约束后仍一致吗？

### 6. 微观破缺的低能稳定性：缩小格距未必解决问题

Collins 等指出，在相应带优选参考系的有效场论中，微观洛伦兹破缺可以通过相互作用进入低维算符，而不按直觉的探测能量/微观能标幂次充分压低。[COLLINS2004](https://arxiv.org/abs/gr-qc/0403053v4)

这使“格子足够小就看不见”成为需要证明的结论。若模型有保护对称性，应给出；若依赖精细调参，应公开；若传统有效场论不适用，应建立自己的跨尺度控制。自然性问题本身不等于实验已否定，但实际生成的超限效应会否定相应模型。

### 7. 涌现引力：普适耦合与质量自由度

Weinberg–Witten 在特定洛伦兹协变守恒流/应力张量前提下，限制能携带相应荷或能动量的高自旋无质量粒子。广义相对论并不同时满足其全部相关前提；它也不是“任何离散涌现引力都不可能”的定理。[WW1980](https://collaborate.princeton.edu/en/publications/limits-on-massless-particles/)

更直接的经验要求是：对不同材料，原生作用为什么产生几乎相同的自由落体？若把余量叫作能量或引力，必须建立通用耦合和可测预算。MICROSCOPE 给出很严的组成依赖约束，光钟和多信使传播又从不同方向限制同一机制。[MICROSCOPE2022](https://arxiv.org/abs/2209.15487v1)；[CLOCK2022](https://arxiv.org/abs/2109.12238v1)；[GW1708172017](https://arxiv.org/abs/1710.05834v2)

## 四、如何使用实验数字

文献中的限值以其原始版本、单位、置信度、符号和模型范围为准。本集合覆盖独立压力通道，不声称穷尽截至当日所有论文，也不把一篇论文的“最强”宣传转成对所有模型的最强约束。

- 高能到达时差约束的是给定传播展开及源模型下的系数；不能直接把 E_QG 当作原生格距的倒数。[LHAASO2024](https://arxiv.org/abs/2402.06009v3)；[FERMI2013](https://arxiv.org/abs/1305.3463v1)
- 同一 GRB 数据用不同推断方法会得到不同限值。2025 DisCan 分析作为稳健性对照，不能与2024分析各取最大数值拼成一个新置信区间。[DISCAN2025](https://arxiv.org/abs/2508.00656v1)
- 偏振和反应阈值提供不同的参数组合。光子与电子部门必须联合给出；只改光子色散不足以判断所有过程。[POLARIZATION2013](https://arxiv.org/abs/1303.4186v1)；[LHAASO_THRESHOLD2022](https://arxiv.org/abs/2106.12350v2)
- 光钟的分数频率读数不确定度，不等于同量级的广义相对论偏离相对上限。[CLOCK2022](https://arxiv.org/abs/2109.12238v1)
- MICROSCOPE 的统计和系统不确定度必须分开。其材料对的结论不能直接宣称对所有新相互作用普遍同界。[MICROSCOPE2022](https://arxiv.org/abs/2209.15487v1)
- 短程引力最小测量间距52微米，不等于宇宙格距小于52微米；Yukawa范围界还带耦合强度前提。[LEE2020](https://arxiv.org/abs/2002.11761v1)
- 天文成像与 Holometer 检验特定噪声累积/相关结构，不能将未见噪声推广成未见离散性。[FOAM2015](https://arxiv.org/abs/1411.7262v5)；[HOLOMETER2017](https://arxiv.org/abs/1703.08503v2)

## 五、统一失败分类

| 返回值 | 必须提供的证据 | 意义 |
|---|---|---|
| COMPATIBLE_WITHIN_SCOPE | 已定义模型对声明数据/设置的预测与误差比较 | 这一范围暂时存活，不是普遍正确 |
| EXCLUDED_WITHIN_SCOPE | 精确矛盾或在明确统计/系统误差下被排除的参数域 | 该版本/假设组合需要淘汰或修订 |
| MISSING_COMPONENT | 缺失的状态类型、动力学、物质/仪器耦合或读出接口 | 尚未成为该现象的可检验模型 |
| THEOREM_NOT_APPLICABLE | 明确不满足哪项前提以及放宽代价 | 只结束该定理路线，实验目标仍保留 |
| EVIDENCE_UNRESOLVED | 数据、误差、原文或适用性存在的具体缺口 | 暂停此项判定，继续独立任务 |
| DERIVATION_OR_IMPLEMENTATION_ERROR | 可定位的推导/实现错误和最小复现 | 先修复再比较，不能当作物理反证 |

失败报告必须区分：本体假设、更新机制、粗粒化/观测桥、参数与数据处理。必要时返回最小冲突假设集合，例如“局域分解+设置独立+目标关联”，而不笼统写“离散错误”或“实验不懂我们的模型”。

## 六、执行顺序与最小交付

先完成00形成可检验模型胶囊；它允许把当前缺项明确冻结，而不要求先完成整个世界理论。随后可并行进行01/02/03/04/08/09/12的有限前提和接口审计。建议首先处理02、03、04和09，因为它们可以快速暴露共享随机性、上下文、相位和隐藏维度的实质缺口。

B组任务以相应接口的实际返回为输入。依赖任务返回缺项不意味着等待无限期：后续可完成条件定理、现象目标和最小接口要求，但不能伪造物理预测。14只整合已经完成的结果，最终检验同一版本、同一读出和同一组物理参数。

正式优先级沿 Researcher 默认 P2/MEDIUM；A/B/C 是本任务集内的推荐依赖顺序，不修改全局调度优先级。十五项任务是当前直接用户方向的独立审计单元，14为整合单元；它们不是某项既有研究成功后自动增生的续阶段。

每个执行单元先交付一个最小有价值结果：一个精确的前提判定、一项不可满足证书、一对被错误合并的状态、一个可观测偏差，或一份不能再笼统表述的缺项。只要已得出这一范围的条件排除，就保存结果并回到父目标；无需为“坚持离散”继续无边界补参。

## 七、研究完整性与潜在突破

任务00/14共同冻结允许的余量类型和参数族、观测算子、操作组合以及训练/留出方式。允许正常拟合并保留实验特定干扰参数，但不允许给每份数据任意新增余量函数，或对不同实验使用不同物理时间/能量定义。

可能的推进不是证明“离散”三个字永远正确，而是找到被经验强制要求的结构：

1. Bell 要求公共关系超出普通局域正权重分解，且又不能被操控为信号。
2. 情境性要求保留与测量组合相关的关系，同时保持操作一致性。
3. 干涉要求保留未来可重合读出的相位/符号信息。
4. 六维读出要求给隐藏自由度一个能通过未来操作检验的动力学去向。
5. 相对论兼容要求区分点集对称、配置对称、统计对称和近似有效对称。
6. 跨尺度检验要求固定参考尺度的统一参数与明确演化；应说明保护机制或受控调谐及其代价。运行耦合可以变化，逐实验任意改参则不算统一解释。

这些都是待研究的方向，不是本次已经得到的新物理定理。一个成功的结果可以是更强的统一模型，也可以是明确指出某条现行路线必须放弃。

## 八、来源与检索边界

本次同时使用专业文献数据库渠道与原始论文页面。KQB Issue6536的6项实际查询均已读取完整返回并保存：2项精确检索无命中，1项命中 MICROSCOPE 题录/摘要但仍为部分覆盖，3项存在原目标缺失或语义错配。没有把搜索成功当成全文阅读，也没有把无命中当成论文不存在。原始论文经独立渠道核验后才用于科学结论。

查询档案：[原始批结果](https://github.com/awdawmip/chatgpt-global-knowledge/blob/cf2a4a8048a05ca002963772f7f2f2700bd6b8a5/sources/professional/operations/KQB-20261026-6536-full-result.json)。先前有效的 BHS 专业检索缓存被复用，没有无谓重发。论文读取范围在来源表逐项记录；仅摘要、选读和完整阅读不得互换。

项目既有工作检索按 Bell、Lorentz、Nielsen、MICROSCOPE、redshift 进行了有界索引搜索，返回无命中不能证明没有既有工作。已明确复用现行波/公共余量、BRC类型及先前光学反对意见笔记；本次不主张任务主题或数学工具的全库新颖性。


## 九、可便携任务目录

每项任务书均包含固定输入、首个可执行问题、产物、失败/缺项条件、原生—有效语义审计及逐篇来源。十五份任务书与十五份不可变出版记录以同一源提交保存；这不表示十五项已经运行。

| 编号 | 任务 | 建议组 | 依赖 | 第一项交付 |
|---|---|---|---|---|
| 00 | [冻结可证伪模型与原生状态—观测桥](../research_tasks/RS-DISC-COMPAT-20261026-00.md) | A | 无 | 用一个两端、各两种设置、各两种输出的实验，列出状态、输入、更新、接收端、读出和随机性来源；每个未能填写的接口标为 MISSING_COMPONENT。 |
| 01 | [连续对称性、有限方向与可观测因果结构](../research_tasks/RS-DISC-COMPAT-20261026-01.md) | A | 00 | 声明旋转/boost究竟作用于什么对象，是否连续，以及哪一个操作会使实验装置相对原生轴改变方向。 |
| 02 | [公共余量的 Bell/CHSH 关联与禁止可控超光速信号](../research_tasks/RS-DISC-COMPAT-20261026-02.md) | A | 00 | 先检查拟用公共余量是否仍满足该分解；若满足，以四个±1响应和正权重给出有限设置上界，而后才设计非局域候选。 |
| 03 | [有限量子情境性与测量上下文的最小状态](../research_tasks/RS-DISC-COMPAT-20261026-03.md) | A | 00 | 写出一个明确的九观测量/六上下文关系表；声明同一测量的身份判据及顺序测量更新。 |
| 04 | [相位、干涉、Born 统计与组合测量](../research_tasks/RS-DISC-COMPAT-20261026-04.md) | A | 00 | 选两组局部计数相同、重合后输出不同的准备，寻找当前压缩状态是否将它们误合并；使用有限实验相位标签而不预设原生三角函数。 |
| 05 | [手征费米子、倍增与规范一致性](../research_tasks/RS-DISC-COMPAT-20261026-05.md) | B | 00, 01, 09 | 先从任务09得到有效3+1维与粒子读出的对应，再从实际更新律或候选提取低能描述，逐项判定所选定理的四个前提。缺少桥则先返回缺项。 |
| 06 | [光子群速度、能量依赖与方向依赖](../research_tasks/RS-DISC-COMPAT-20261026-06.md) | B | 00, 01, 08 | 从一个明确波包/事件传播机制推导可观测到达时间，至少给出首个非零能量依赖项，或证明在规定范围为零。 |
| 07 | [偏振双折射、光子衰变与反应阈值](../research_tasks/RS-DISC-COMPAT-20261026-07.md) | B | 00, 04, 05, 06 | 列出两偏振传播与至少一个光子—电子过程的共同自由参数和守恒规则。 |
| 08 | [红移、Doppler、钟速与能量标定](../research_tasks/RS-DISC-COMPAT-20261026-08.md) | A | 00 | 对同一发射—接收过程写出本地计时、探测事件和能量预算；区分运动Doppler、引力红移和宇宙学红移三类机制。 |
| 09 | [原生六维到可观测三维的动力学及引力距离律](../research_tasks/RS-DISC-COMPAT-20261026-09.md) | A | 00 | 定义可实现的物理移动、距离和探测器耦合；列出该读出未分辨的原生自由度或状态等价类及其动力学去向，不预设固定三条隐藏轴，也不直接令其为零。 |
| 10 | [等效原理、通用耦合与涌现引力的条件障碍](../research_tasks/RS-DISC-COMPAT-20261026-10.md) | B | 00, 08, 09 | 对两个不同组成的测试体写出同一引力场中的加速度读出，明确质量/内能/余量的耦合方式。 |
| 11 | [路径涨落、相干性及余量噪声的相关结构](../research_tasks/RS-DISC-COMPAT-20261026-11.md) | B | 00, 04, 06 | 固定一种可测传播残差，写出其均值、两点相关或确定性误差界，并说明接收端如何耦合。 |
| 12 | [原生三元平衡到表观两力平衡的守恒闭合](../research_tasks/RS-DISC-COMPAT-20261026-12.md) | A | 00 | 选择最小两端拉力或反冲实验，构造保留第三项来源、接触与预算的三元 lift，并明确读出。 |
| 13 | [尺度变化、辐射稳定性与参数保护](../research_tasks/RS-DISC-COMPAT-20261026-13.md) | B | 00, 01, 05, 06, 07 | 给实际候选机制列出被允许的低阶有效项，指出保护它们为零/很小的确切对称或结构。 |
| 14 | [同模型同参数的联合兼容域与最小失败核心](../research_tasks/RS-DISC-COMPAT-20261026-14.md) | C | 00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13 | 汇总前面任务的假设、输出和缺项，将同名参数和观测量对齐；先作逻辑/域交集，再决定是否具备联合统计分析条件。 |

## 十、三个有限判别模板

这些是已有外部量子关系的明确检验输入和透明代数障碍，不是对本模型已完成的物理实现。

### Bell 的有限条件界

两方各两个设置、输出±1。在16种确定性局域策略中，每种都有 C=a₀(b₀+b₁)+a₁(b₀−b₁)=±2。因此设置独立的非负归一化局域混合满足 |S|≤2。无限增加共同历史也不改变这个结论，除非实际改变分解或设置独立性。检验任务必须核对这种分解是否真是模型的性质。外部量子对照表 P(a,b|x,y)=[1+ab(−1)^(xy)/√2]/4 则同时给出 S=2√2 和均匀的单方边缘。

### 语境性的奇偶矛盾

九个观测量按三行排列：(X⊗I,I⊗X,X⊗X)、(I⊗Y,Y⊗I,Y⊗Y)、(X⊗Y,Y⊗X,Z⊗Z)。三行和前两列乘积均+I，最后一列−I。为每个观测量赋予上下文无关的±1值，会让六个乘积相乘一方面为−1，另一方面因每个值出现两次而为+1。现实带噪实验仍须核对兼容性和顺序扰动，不能省略这些实验前提。

### 相位信息损失的最小见证

s₊=(1,1)与s₋=(1,−1)的局部强度均为(1,1)。同一未归一化混合H=[[1,1],[1,−1]]之后，强度分别为(4,0)和(0,4)。如果原生压缩把它们合并，又使用同一未来更新，就不可能产生这两个不同输出。这只排除“强度就是全部未来相关状态”的压缩；有标签的正权重关系或额外相位/符号载体仍需具体检验。

完整条件说明见 [量子支持笔记](DISCRETE_COMPATIBILITY_20261026_quantum_support.md)。

## 十一、来源版本与数字冻结

LHAASO时延表使用2402.06009v3（2026-02-13），不是早先v2。其表1 ML(MINOS)方法给线性E_QG超光速/次光速下限1.1/1.0×10²⁰GeV、二次下限7.0/6.9×10¹¹GeV；校准方法给线性1.0/1.1×10²⁰GeV、二次7.0/7.2×10¹¹GeV，均为对应95%口径。任务应保持方法标签，不选拼最大值。2025 DisCan同事件重分析的下限不同，不能当成独立数据重复实验。

2014 Doppler论文勘误已读全文；它补上两个SME系数的GeV单位，不改变主时间膨胀结果。Nielsen–Ninomiya原始I论文的勘误已定位但未读内容；此集合的精确四条件版本改由已读的Lüscher1998正文支持。手征任务先依赖有效3+1维桥，不把四维γ5直接施加到原生六空间维。

所有引用按下表读取层级使用；没有原始实验数据再分析，没有独立第二次全文复核的声明。

| 来源 | 实际读取范围 | 适用边界和数值说明 |
|---|---|---|
| [BELL1964: Bell, On the Einstein Podolsky Rosen paradox (1964)](https://journals.aps.org/ppf/abstract/10.1103/PhysicsPhysiqueFizika.1.195) | publisher metadata/abstract; original PDF not fully read | 局域性与适当设置独立的条件障碍；不能解释为所有决定论或所有离散性的排除。 |
| [HENSEN2015: Hensen et al., Experimental loophole-free violation of a Bell inequality using entangled electron spins separated by 1.3 km](https://arxiv.org/abs/1508.05949v1) | arXiv v1 abstract | 245 trials; S=2.42±0.20; reported local-realist p=0.039. 有限设置目标；具体统计模型与事件选择须在执行时读实验细节。 |
| [SHALM2015: Shalm et al., A strong loophole-free test of local realism](https://arxiv.org/abs/1511.03189v2) | arXiv v2 abstract | p=5.9e-9；计入设置可预测性后的保守结果为2.3e-7。不要混用两个口径。 |
| [MERMIN1990: Mermin, Simple unified form for the major no-hidden-variables theorems](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.65.3373) | publisher abstract; full text not read | 支持有限语境性路线；本文使用的九观测量奇偶关系在任务支持笔记中显式给出，实验需另做兼容性/扰动审计。 |
| [KIRCHMAIR2009: Kirchmair et al., State-independent experimental test of quantum contextuality](https://arxiv.org/abs/0904.1655v2) | arXiv v2 abstract | 离子系统有限上下文实验；不把理想相容算符关系等同于现实无扰动测量。 |
| [MAZUREK2016: Mazurek et al., An experimental test of noncontextuality without unwarranted idealizations](https://arxiv.org/abs/1505.06244v1) | arXiv v1 abstract; journal DOI metadata | 期刊题名使用 without unphysical idealizations；Nature Communications 7,11780, DOI10.1038/ncomms11780。操作等价和噪声处理是额外义务。 |
| [SINHA2010: Sinha et al., Ruling Out Multi-Order Interference in Quantum Mechanics](https://arxiv.org/abs/1007.4193v1) | arXiv v1 abstract | 该装置对归一化三阶干涉约束至预期二路径干涉的1e-2量级；不是无限精度证明。 |
| [SAWANT2014: Sawant et al., Nonclassical paths in quantum interference experiments](https://arxiv.org/abs/1308.2022v2) | arXiv v2 abstract | 开关狭缝改变边界条件，朴素跨实验叠加并不精确；非零三缝差值不自动否定Born律。 |
| [PBR2012: Pusey, Barrett and Rudolph, On the reality of the quantum state](https://arxiv.org/abs/1111.3328v3) | arXiv v3 abstract | 准备独立性等前提下约束重叠的本体概率分布；不是反离散时空定理。 |
| [BHS2006: Bombelli, Henson and Sorkin, Discreteness without symmetry breaking: a theorem](https://arxiv.org/abs/gr-qc/0605006v1) | original abstract and full HTML theorem/proof/corollary read | Minkowski Poisson撒点分布洛伦兹不变；相应可测等变优选方向映射不可能，有限价图后果有同一框架前提。不是任意离散模型协变性证明。 |
| [NN1981: Nielsen and Ninomiya, Absence of neutrinos on a lattice (I): Proof by homotopy theory](https://doi.org/10.1016/0550-3213(81)90361-8) | primary publisher metadata/search result; publisher full text inaccessible | 原始来源；本次具体四条件版本依据Lüscher1998全文，而不伪称已核读本篇完整证明。原文有1982勘误。 |
| [NN_ERRATUM1982: Nielsen and Ninomiya, Erratum to Absence of neutrinos on a lattice](https://doi.org/10.1016/0550-3213(82)90011-6) | primary publisher metadata only | 已定位勘误，执行任务若采用原始I版证明须核读；本次不据未读勘误内容给出额外结论。 |
| [GW1982: Ginsparg and Wilson, A remnant of chiral symmetry on the lattice](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.25.2649) | publisher abstract | 修改手征实现的原始来源；指数局域与有限邻接不可等同。 |
| [LUSCHER1998: Lüscher, Exact chiral symmetry on the lattice and the Ginsparg-Wilson relation](https://arxiv.org/abs/hep-lat/9802011v1) | abstract and full HTML sections 1–4 | §2四条件：解析周期D(p)、低动量iγp+O(ap²)、非零动量可逆、朴素γ5反对易，不能同时满足；§3/4解释GW修改条件。有效3+1维桥须先建立。 |
| [COLLINS2004: Collins et al., Lorentz invariance and quantum gravity: an additional fine-tuning problem?](https://arxiv.org/abs/gr-qc/0403053v4) | abstract and main full HTML argument read | 优选参考系+相应相互作用/有效理论下低维洛伦兹破缺项可不受E/EPlanck直觉抑制。自然性压力不是无条件数学反证。 |
| [WW1980: Weinberg and Witten, Limits on massless particles](https://collaborate.princeton.edu/en/publications/limits-on-massless-particles/) | author institution abstract; original DOI identified, full PDF retrieval timed out | DOI10.1016/0370-2693(80)90212-9。特定洛伦兹协变守恒流/应力张量条件限制高自旋无质量粒子；具体候选须逐项验前提。 |
| [CAVITY2015: Nagel et al., Direct terrestrial test of Lorentz symmetry in electrodynamics to 10^-18](https://arxiv.org/abs/1412.6954v2) | arXiv v2 abstract | 相对取向频差(9.2±10.7)e-19为95%置信口径；器件和物质响应参与读出，不能直接当普适δc/c界。 |
| [DOPPLER2014: Botermann et al., Test of Time Dilation Using Stored Li+ Ions as Clocks at Relativistic Speed](https://arxiv.org/abs/1409.7951v1) | arXiv v1 abstract | β=0.338；目标时间膨胀关系检验至2.3ppb。必须同时读勘误。 |
| [DOPPLER_ERRATUM2015: Botermann et al., Erratum: Test of Time Dilation Using Stored Li+ Ions as Clocks at Relativistic Speed](https://journals.aps.org/prl/pdf/10.1103/PhysRevLett.114.239902) | full one-page erratum PDF read | 补上SME参数单位GeV：|c~p_Q|<2e-11 GeV、|c~e_Q|<2e-8 GeV；未改变主时间膨胀结果。 |
| [CLOCK2022: Bothwell et al., Resolving the gravitational redshift across a millimetre-scale atomic sample](https://arxiv.org/abs/2109.12238v1) | arXiv v1 abstract and journal metadata | Nature602,420–424, DOI10.1038/s41586-021-04349-7；分数频率测量不确定度7.6e-21，不等于对GR偏离的相同比例上限。 |
| [MICROSCOPE2022: MICROSCOPE Mission: Final Results of the Test of the Equivalence Principle](https://arxiv.org/abs/2209.15487v1) | arXiv v1 abstract; professional database partial matching abstract | η(Ti,Pt)=[-1.5±2.3(stat)±1.5(syst)]e-15；保留统计/系统口径，不未经假设转换联合95%界。 |
| [LEE2020: Lee et al., New Test of the Gravitational 1/r^2 Law at Separations down to 52 micrometers](https://arxiv.org/abs/2002.11761v1) | arXiv v1 abstract | 52μm–3mm测量；引力强度Yukawa修正范围95%界λ<38.6μm。最小间距不是原生格距上限。 |
| [GW1708172017: Gravitational Waves and Gamma-rays from a Binary Neutron Star Merger: GW170817 and GRB 170817A](https://arxiv.org/abs/1710.05834v2) | arXiv v2 abstract | 到达差1.74±0.05s；在源发射时差假设下(c_g-c)/c约受限于[-3e-15,7e-16]；执行需核读源假设和完整速度分析。 |
| [HOLOMETER2017: Interferometric Constraints on Quantum Geometrical Shear Noise Correlations](https://arxiv.org/abs/1703.08503v2) | arXiv v2 abstract | CQG34,165005；两台40m Michelson跨相关，25MHz带宽；限制特定几何剪切相关噪声，非全部离散结构。 |
| [POLARIZATION2013: Götz et al., GRB 061122: a high signal-to-noise polarised Gamma-Ray Burst](https://arxiv.org/abs/1303.4186v1) | arXiv v1 abstract | 250–800keV偏振及源红移模型；所报双折射模型ξ<3.4e-16，不能移植为任意能量依赖光速的普适界；未以摘要补造ξ置信水平。 |
| [FOAM2015: Perlman et al., New Constraints on Quantum Gravity from X-ray and Gamma-Ray Observations](https://arxiv.org/abs/1411.7262v5) | arXiv v5 abstract | δℓ≈ℓ^(1-α)ℓP^α的相位累积框架下Xray/GeV/TeV给不同α约束；排除积累模型，不排除全部时空离散性。 |
| [FERMI2013: Vasileiou et al., Constraints on Lorentz Invariance Violation from Fermi-Large Area Telescope Observations of Gamma-Ray Bursts](https://arxiv.org/abs/1305.3463v1) | arXiv v1 abstract re-opened and version frozen in this root turn | GRB090510等跨源对照；摘要的较强界明确不计源本征色散，不能抹去该前提。本次不把它与其他GRB结果拼接为联合置信域。 |
| [LHAASO2024: LHAASO Collaboration, Stringent Tests of Lorentz Invariance Violation from LHAASO Observations of GRB 221009A](https://arxiv.org/abs/2402.06009v3) | current v3 (2026-02-13) abstract and full HTML Table1/method/model passages read | Table1的95% E_QG下限：ML(MINOS)线性super1.1/sub1.0 ×10^20GeV、二次super7.0/sub6.9 ×10^11GeV；ML(calibrated)线性super1.0/sub1.1 ×10^20GeV、二次super7.0/sub7.2 ×10^11GeV。CCF另列。引用须带方法/符号。 |
| [DISCAN2025: Xi and Shu, Constraints on Lorentz Invariance Violation from GRB 221009A Using the DisCan Method](https://arxiv.org/abs/2508.00656v1) | arXiv v1 abstract | 95%线性sub5.4e19/super2.7e19GeV；二次sub1.0e13/super2.4e12GeV。同一GRB数据方法重分析，不是独立重复实验。 |
| [LHAASO_THRESHOLD2022: LHAASO Collaboration, Exploring Lorentz Invariance Violation from Ultrahigh-Energy Gamma Rays Observed by LHAASO](https://arxiv.org/abs/2106.12350v2) | current v2 (2026-01-10) abstract | 约1.4PeV光子；超光速光子衰变/谱截止条件约束依赖电子部门及运动学，不能单独称时空离散尺度界。 |
| [PHOTON_ELECTRON2022: He and Ma, Joint photon-electron Lorentz violation parameter plane from LHAASO data](https://arxiv.org/abs/2210.14817v3) | arXiv v3 abstract | 1.42PeV光子为直接观测；2.3PeV电子依SSC源模型推断。PLB835,137536。需在光子/电子参数平面分析。 |

## 十二、项目源与贡献归属

- https://github.com/awdawmip/enterprise-math/blob/64044ada5e3e2b5d7b3c327942ee028da6e2a967/p000_reality_foundation.json
- https://github.com/awdawmip/enterprise-math/blob/64044ada5e3e2b5d7b3c327942ee028da6e2a967/definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json
- https://github.com/awdawmip/enterprise-math/blob/64044ada5e3e2b5d7b3c327942ee028da6e2a967/definitions/RESIDUAL_FAITHFUL_DISCRETE_RELATIONAL_SYSTEM.json
- https://github.com/awdawmip/enterprise-math/blob/64044ada5e3e2b5d7b3c327942ee028da6e2a967/definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json
- https://github.com/awdawmip/enterprise-math/blob/64044ada5e3e2b5d7b3c327942ee028da6e2a967/definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json
- https://github.com/awdawmip/enterprise-math/blob/64044ada5e3e2b5d7b3c327942ee028da6e2a967/foundational_logic.json
- https://github.com/awdawmip/enterprise-math/blob/64044ada5e3e2b5d7b3c327942ee028da6e2a967/docs/HEARTBEAT_BRC_ONLY_ARITHMETIC.md
- https://github.com/awdawmip/enterprise-math/blob/64044ada5e3e2b5d7b3c327942ee028da6e2a967/research_constraints/heartbeat_brc_only.json
- https://github.com/awdawmip/enterprise-math/blob/64044ada5e3e2b5d7b3c327942ee028da6e2a967/research_notes/BRC_NATIVE_X6_SEMANTIC_ALIGNMENT_20261002_9D72AC.md
- https://github.com/awdawmip/chatgpt-global-knowledge/blob/1f73bff7ce37e663922e3c8dd29411441b0e37a7/projects/enterprise-math/NATIVE_WAVE_COMMON_RESIDUAL_CURRENT.md

先前光学笔记：https://github.com/awdawmip/enterprise-math/blob/18d4a6d12ab7d8ab0897e9336c81ac07238fd30c/research_notes/discrete_light_objections_20261026_9c8ddfc415e7.md


根贡献者 EM-DIRECT-3041B2 完成原始来源核对、模型输入对齐、综合与任务出版。支持贡献者 EM-QF-493032、EM-COMPATSP-45D575、EM-EMP-ECA41D 分别提供量子、时空/手征、经验参数的条件性逻辑审阅；其首次远端注册调用中断，未完成独立新文献读取。支持笔记保留真实贡献范围，不计作独立审查或原始数据复算。经验支持笔记使用的历史v2建议，由本报告已经核读的当前v3及来源表明确取代。

本次目标完成口径是“文献与条件搜集、十五项可便携任务及记录发布”。后续十五项执行和理论成败判定仍然开放。任何任务的未执行状态不得转写为实验通过。
