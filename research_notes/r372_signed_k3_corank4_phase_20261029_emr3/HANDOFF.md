# R372 接续包｜signed-K3 r=4

日期：2026-10-29。作者侧数学成果，`UNREVIEWED / NOT_ADMITTED`，研究来源为当前自动研究对话，不声称 Source 原生 researcher_id/session/CLAIM。活跃 Owner 只读查询本轮返回 `CONTROL_QUOTA`；Sites `research_authority_granted=false`。P000/ACTIVE 世界观保持原状。

前沿：Enterprise Math Draft PR #1592，R371 不可变来源 `0eb95928dc8265f7a5de4d5d06b50c2093073347`。本轮紧接的研究对象是原始十二项有符号 K/J，仅 K3[t²]=−8(1+θ)，θ>−1。新增结论：九项有限原始 D 观察的 F4 为 PF2 当且仅当 -1<θ≤σ4，σ4 是 T1 在 (1469/1000,1470/1000) 的唯一根；所有 θ>−1 均非 PF∞；共同 r1..4 的 PF2 域仍以 R370 的 τ1 限定。

复验：从 PR #1592 分支运行 `python research_notes/r372_signed_k3_corank4_phase_20261029_emr3/R372_reproduce.py`；只需 SymPy 和同分支既有 `R346_verify.py`，无需旧 ZIP/CSV。期望输出以 `R372_EXACT_PASS` 开始。算法完整重算9个原始 D 多项式和22个严格 Bernstein 区间证书，不借 R363 多项式延伸。主证明 `R372_PROOF.zh-CN.md` 提供全部精确端点、首三系数及非负尾部多项式。

下一最小数学单元：r=5 十一项原始 D 系数与首位 Turán 阈值；对潜在其他零点用精确 Bernstein 或 Sturm 证书覆盖 θ>−1，不能用参数取样代替全域分类。并行数学债：R363 全指标次数界独立审查、BRC 辅助核到原生 X6 的保真映射。已有 r1..4 相图不需重算为新结果。

材料保存在当前 PR 的 `research_notes/r372_signed_k3_corank4_phase_20261029_emr3/`；PR 维持 Draft。仓库文件只是作者侧持久化，不能视作原生任务 CLAIM、Source Result、独立 Driver 审查或正式数学接纳。
