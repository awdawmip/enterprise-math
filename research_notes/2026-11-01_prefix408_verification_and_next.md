# PREFIX-408：执行回执、证据边界与未完成问题

日期：2026-11-01。作者身份：当前进取数论研究6便携研究对话，不是 Source 签发的 owner/CLAIM/Result/Review。数学状态：AUTHOR_SIDE_EXACT_VERIFIED / UNREVIEWED / NOT_ADMITTED / NATIVE_REGISTER_PENDING。

冻结来源：GLOBAL_KNOWLEDGE_V1 main@7b33f8066e9993e7c941959a9d738ed405248eb8；Enterprise Math main@71f5e22a2d4de499694c6db4bf7f195df6d63ab0。已读取规范入口、P000、ACTIVE 世界观、docs/AUTONOMOUS_RESEARCH_OPERATIONS.zh-CN.md、docs/PORTABLE_RESEARCH_PROTOCOL.md、PREFIX-407 原文。

研究问题及精确证明见 research_notes/2026-11-01_prefix408_nonzero_i3_sharp_threshold_and_psd_gap.md。两项新增结果：

1. 在 I2=1、Cu=2 准确，I3∈[0,β]，I4∈[41±κ]，Cv∈[0,10]、I5∈[0,100] 时，来源存在当且仅当 κ≥κ*(β)，其中 βc=(43-3√205)/8，κ*(β)=4-8√(45β)+16β （β≤βc），其他 β 时为0。
2. 在 ε=1/10000、β=10^-6、κ=1，且 Cv、I5 各取名义中心±ε 的联合非零宽度盒中，H0=diag(1,1,0) PSD 可行，但所有单源 rank-one 都不可能；全体可行 PSD 有 λ2(H)≥7291831/10000000，det(H左上2×2)≥92666648343439/100000000000000。

可执行验证代码：research_notes/prefix408_exact_checker.py；原始 stdout：research_notes/prefix408_execution.log。程序从原始五 Port 复矩阵算出测量行系数，符号验证所有 Hermitian PSD 的 I4 线性展开，检查无理阈值见证及有理连续盒证书；3项 PASS，实际环境 Python3 / SymPy1.14。连续全称结论的依据为数学证明，而非有限样本测试。没有执行原生 X6、typed BRC、通用 CAD、形式化 Lean 或独立审阅。

外部文献核验：Candès–Strohmer–Voroninski, PhaseLift (arXiv:1109.4499)；Gao Huang & Song Li, PhaseLift for Coded Diffraction Patterns: Optimal Sampling Rate (2026-08-03, arXiv:2608.02450)。其随机/编码测量设定与本固定 Port 并不相同，不能据此宣传文献定理被推翻。

原生 Source 能力读数显示 research_authority_granted=false（只读身份 sites-em-6abdec598ad48191aebece9a8232f041-ro）；本轮活跃 owner 查询返回 CONTROL_QUOTA，没有获得当前 owner 名单。既有本地 EM-R006 署名只为历史归属，本轮不据此宣称真实原生权限。

下一问题 PREFIX-409：把 Cv/I5 从宽容区间收紧为真实窄联合噪声，求 sharp κ*(ε,β,ηv,η5)；将本文可回放 rank-one NO 证书接入 PREFIX-405 的半判定框架并求边界-only YES 来源证书。保持 P000/typed BRC/原生 X6 桥梁独立证明义务。

保存性质：普通 GitHub 科研物料持久化，不等于 Source 原生 checkpoint、正式 CLAIM、Result 或数学接纳。
