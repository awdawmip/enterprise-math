# R376｜带符号 BRC K₃ 第八余阶接续

2026-10-29 作者侧精确数学研究，未取得原生 Source CLAIM、Result 或独立 Driver 审阅。GitHub 登录 awdawmip；Site 实时报告 research_authority_granted=false，当前活跃 owner 查询返回 CONTROL_QUOTA。发布的 Research-Activity/日志若存在均属来源与进度保全，不代表数学接纳。

**数学前沿**：R376 严格分类原始带符号十二项核、K₃[t²]=−8(1+θ)、θ>−1 的第八余阶 17 项有限原始 D 观察：PF₂ 当且仅当 −1<θ≤η₈。η₈ 是 T₉=c₉²−c₈c₁₀ 在 (183/100,1831/1000) 中唯一实根，约 1.830976487806697。证明用32个多项式的精确 Sturm 根数与4个连续覆盖区间的负性证书，附 51 条独立精确有理点交叉等式。θ=15/8 时 c₉,…,c₁₆ 全为零、次数退化为8，但 T₃ 严格负。无需 R348/R363 全指标抽取假设，不涉及原生 X6 映射。

**复现入口**：从 PR #1592 的本目录运行 python R376_CHECK.py；依赖同 PR 目录中的原始 R346_verify.py（定义全部带符号 K/J）和 R369_check.py（仅作第二精确算路），及 SymPy。脚本生成非空 R376_EVIDENCE.json，输出 R376_EXACT_PASS，并复验 C/T 多项式联合 SHA256 1641424c4da68106c12a5b49c8d81faac5742a4d8c7f8eb8bc13a5532ed7a54a。原始有限闭包 B_s≤44、t 次数≤26。完整证明见本目录 R376_PROOF.zh-CN.md。

**冻结规范**：GLOBAL_KNOWLEDGE_V1 main@5e17647d9e43d87639963b49c8d1a032d1c64472；项目 main@243cdc6ce8e061ec371426bfb650fff0eae8d629；所用原始 R346 K/J Git Blob 1579ceb717ab1945227eca4f7a1878bf4ffa73e1。P000 与 ACTIVE 世界观保持原样。

**下一问题**：构造 r=9 的 19 项有限原始 D 观察，在 σ₆∈(901/1000,902/1000) 的当前共同稳定区间上求首个失效阈值，若仍保持则给出精确充分区间；独立审查 R348/R363 无限抽取及次数界。原生 Owner/CLAIM 状态由合法 Source 会话另行取得，不以本 PR 的证据替代。
