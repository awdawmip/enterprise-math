# 2026-11-24 OpenAI VP/VNP 公开成果吸收与 Driver 交接

状态：SOURCE_OBSERVATION / UNREVIEWED_RESEARCH_PROPOSAL / NOT_ADMITTED。作者：本轮公开数学吸收对话；外部论文作者 OpenAI，保留其原贡献。非 Task、CLAIM、Result 或 Review。

## 已闭合前沿与规范

11-23 记录 a2e0b7e855437dbcbc0e748b5ec08c7a6946e9dd:research_notes/public_math_intake_20261123/OPENAI_NOV23_SOURCE_SCREEN_AND_QFT_ORIGINAL_RECEIPT_CLOSED.md 已读取。原请求 math-intake-20261122-0934-qft-task-read-r1 原生回读 SUCCEEDED/error=null，原 QFT publication TP2-A9BCBF65D1395E75F2F7；原观察 11-22 01:37:51 UTC，不产生现行授权；无需重发。保留既有 ETH pin openai/math@7ef5c0cc5ca4b0e072b7a050fca09ab24bc6fa3a 与各 Task 原科学输入。

账户规范 main@f7c8ca57b1038e712da4ad0445865df8af9d6127，已读两入口、输出、数学研究、EM Activity、标记、ACTIVE 世界观及 P000 router。EM 当前 main@ba34624744fdc7695ffeb0c27960df7cb4297c3e，已读续接、自主研究、研究方法、P000、联合关系、X6 时间、残差保真、P023、Driver 操作与普通 Chat 控制。em_status 0.6.11 实际 Source 同 SHA；Sites identity probe 不授研究权限。此次没有已核实本会话 ACTIVE DA、owner 或 Result review 绑定。

## 外部新增

授权 GitHub 读取 openai/math main@f5702854040e97fa7675c21ba37a9608f5f92dd3；相对 4eaee87548250b2682affda7d05d947c05554bae compare ahead=2, behind=0；内容提交 e07100d36b22bcf8bb759f2f1abc7976ba472e47（2026-11-24 01:14:20 UTC），PR #5 merge 2026-11-24 01:30:37 UTC。compare 返回的文件列表可能受 GitHub 上限，不宣称完整文件数。
history.md blob 2a8ff2e0b61b0fccf4d34bb5ac353c4e7b294dbb：11月23日版新增 VP and VNP are different，成果取得日期 11月6日；10月7日三稿撤回未改变。官方研究出版索引 https://openai.com/research/index/publication/ 本轮最新可见 11-18，尚未见 VP/VNP 专文；官方仓库已经公开。
固定论文 https://github.com/openai/math/blob/f5702854040e97fa7675c21ba37a9608f5f92dd3/preprints/VP-and-VNP-are-different-November-23-2026/build/Paper.tex (blob 7e83dc86fb95faf3bcf8cb0b4f9eefac2e99c181)；README blob d1803d08a4831d63e986cf2a67a84c81cea27714；CONTENTS.md result 379，blob a174602698a23c7f9a95cb8da4658edcee1db47b。作者主张任意域显式 VNP 族 f_n 的 border arithmetic circuit 下界 exp(Omega((log n)^(5/4)))，推及有向 Hamilton 环多项式（任意域）及 permanent（特征非2）。不是 Boolean P vs NP；非均匀二元加减乘、自由域常数、形式多项式、最终多项式次数与变量数多项式受限。原文 f_n=sum_{x in {0,1}^n} c_x product_i Z_{i,x_i}，c_x 为带固定多项式时钟的通用机接受路径数；需保留计数及域中特征语义。

原文 hinge：欧氏单位球 D 条直径各宽 m 的 equality tensor；有限和 A 项网络，每项 wire cost <=w，strict shortening 当 w+2D log_2 A<2Dm。无 shortening 时 expander、varying balanced cuts、rank 与 hub displacement 给下界；若存在 shortening 则迭代节省 wire、批量 replay、parse map、boundary evaluation/eigenvector law（含 Cartier）支持更强条件下界。此为原文策略核读，不是独立审完整证明。欧氏几何和自由局部表代价仅属外部模型，不能直接取代原生 X6、120度正角、三元平衡或真实计算资源。

## Lean 边界

lean/docs/379.md blob e138903e12a699f43601678a3a5153c607041e7c 声明：exact 非均匀 VP != VNP 任意域；显式齐次多重线性族度 n、2n 变量，任意固定 C>=1 及特征，充分大 n exact size>n^C，阈值对同特征域一致；HC 及特征非2 permanent exact 下界。论文更强的定量 border 下界不在该 Lean 说明所列验证范围。
Comparator challenge lean/ComparatorChallenges/VPVNP.lean blob 617a845fc5b66da1635e73fbcbe6e6ca83fc0b90 中 sorry 是待比较挑战占位；配置 VPVNP.json blob b55ae410b72d0d0f6d1f223cd638cb3dbb2845f5 指向 OAI.Computability.VPVNP.ClassSeparation，theorem OAI.Computability.VPVNP.Standalone.vp_ne_vnp，允许 propext, Quot.sound, Classical.choice，enable_nanoda=false。实际 solution ClassSeparation.lean blob 513ce5b4c02108143cadee0e1e612156349d2202，入口通过 Separation 与 Valiant.Project 的 iff 转换；入口无 sorry/admit，依赖闭包尚未独立检查。combined statuses=[]；未本地执行 Lean、Comparator 或公理审计。不得宣称独立验证通过。复验入口：cd lean; lake update; lake exe cache get; lake env comparator ComparatorChallenges/VPVNP.json（须有 pinned toolchain、comparator、landrun、lean4export）。

## 去重与拟交接的有限方向

当前 Source research_tasks 目录列出886项；文件名匹配 Valiant/VPVNP/tensor/circuit/complexity/openai 等未见专门 VPVNP Task，四个相关 OpenAI/BRC Task 已存在。GitHub 内容检索 VPVNP、Valiant、strict shortening、permanent 返回空；不能证明所有既存研究绝无同类结论。综合任务 RS-BRC-FUTURE-FAITHFUL-INTEGRATION-20261028 已有真实成本、未来保真、计数/路径和联合关系要求，P023 已有纤维与未来闭包，不另发普通压缩任务。

新增候选：在实际 typed BRC 的有限二端口/多端口网络，研究固定 cut 的 joint equality relation 与可选择 cut 的关系网络，分开 (i) 秩/未来观察保真下界 (ii) selector、分支身份、局部表、路径重组、构造恢复与实际 wire/bit cost。外部参考基线（非 BRC 定理）：任意域、m 位两端口 equality 矩阵 I_(2^m)，若固定同一 cut 上 A 项网络之和且每项 cut 至多 b 位二值内部指标，则各项可按 cut 指标写成至多 2^b 个 rank-one 外积；rank(I)=2^m<=A*2^b，所以 b+log_2 A>=m。逐项不同 cuts 不能用此式直接相加；这正是可区分的新资源问题，不重复 P023 的一般商判据。该简短线性代数论证是候选核对基线，非原创一般秩定理、非原生 BRC 实验。

拟由合法 Driver/owner 核实去重后，优先在既有综合任务允许范围绑定，否则建立有限新研究单元；新输入只冻结本次公开 pin，不覆盖原任务。
有限首单元：选择 m=1,2,3，使用 F2/F3 与自然数路径计数分别建联合 equality tensor，明确输入/输出端口及允许未来操作，检查 selector 加和是否保持联合观察（特别区分布尔支持、域中抵消、正重数）；比较直接网、固定 cut、变化 cut，完整记录构造/恢复、边长位宽、局部表大小、选择及验证成本。给一个严格缩短证书或仅就声明枚举类证明无缩短，找出失败后最小修复；不以局部节省推出 VP/VNP 或原生物理结论。P000 保持不变，若研究实际 X6 几何，必须明确六轴嵌入、三维切片与时间语义、合法复合路径及 observer bridge；不把欧氏直径当原生轴。

正式发布状态：PENDING_DRIVER_DECISION / NO_TASK_PUBLICATION。当前 native Sites followup_materialize 要求真实自身 ACTIVE DA、原 Result read、review/synthesis 与 own publication；本次是外部来源新增而非现存已审 Result 后继，尚无该绑定。不得制造 Result、借其他 owner 或使用历史 SID。交接对象为当前合法 Driver/综合任务 owner；下一动作核实际当前任务覆盖与发布合同，正式发布或绑定后回读真实 Task/publication ID。独立 Lean 核验仍待执行。