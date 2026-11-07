# R369 研究接续包｜作者侧 BRC K₃ 负支路

科学对象：原始 R346 全部 12 项有正负号的 K/J 辅助递推，唯一变化 `K_θ=K−8θ x³t²`；对于全部 `θ>-1`，原始 K₃[t²] 负号仍保留。R368 是分子扰动；本轮是另一条真实 K 支路扰动，不互相覆盖。

**已完成、不重做：**证明在 R348/R363 全指标抽取/次数界前提下，所有 `r≥1` 满足 `Δ^(2r)Q_(θ,r)(0)=Catalan(r)*(30−16θ)^(2r)`；`θ=15/8` 导致最高差分对所有 r 为零。直接从原始 D 三个索引的符号行列式独立抽取出 r=1 的三条整数多项式 `512θ²−2400θ+2620`、`768θ²−2880θ+2520`、`(30−16θ)²`。精确见证 `θ=5/4` 产生正 `(420,120,100)` 但 Turán `−27600`，`θ=3` 产生 `(28,792,324)`、判别式 `590976>0`，分别展示非 PF₂ 和 PF∞；`θ=0` 为 PF₂ 非 PF∞。50 条全精确顶差分、20 条原始 D 交叉核验均通过。以上 r=1 是三项有限观察差分的无条件精确结论，全 r 依赖 R363。

**直接运行：**从本 PR 分支调用 `python research_notes/r369_signed_k3_branch_top_catalan_20261029_emr3/R369_check.py`。仅使用 sibling `r346_unbounded_interior_tp2_corank301_20261028_emr3/R346_verify.py`，以及 Python `sympy`；不依赖用户侧 ZIP、历史 CSV、GitHub Actions 或另一个工作区。输出 `R369_EVIDENCE.json` 和 `R369_EXACT_PASS`，文件中保留完整有理样本与证据计数。

**未解除的义务：**独立审查 R348/R363 全指标抽取和 `q<m` 边界；r>1 其余 Newton 系数的全 θ 区间；全余阶 PF₂ 统一证明/反例；BRC 辅助核对 P000 原生六维 X6 的可观测保真映射；独立 Driver 数学准入。活动/本研究提交不是 native CLAIM、Source Result 或正式授权 owner 交接。

**下一确切动作：**选 `K3[t²]` 的精确参数，先对 r=1..10 的全部 Newton 系数求有理根隔离、定位普通 Turán 首次变号区间；在 r 上升时找稳定半径变化或最早非正反例，明确有限证书与全 r 命题差异。并行送独立审阅者核查 R363 依赖。

**固定控制读取**：GLOBAL_KNOWLEDGE_V1 `awdawmip/chatgpt-global-knowledge@c7293af18643f487f574cb014e3835117b28c413`; Enterprise Math `main@4864ced8447b0953b9023fc017d68c142b9901cb`. P000/ACTIVE 不作修改。源 R346 在 PR #1592 当前关联研究分支；本 R369 以不可变最终提交为准。AUTHOR_SIDE_EXACT / UNREVIEWED / NOT_ADMITTED。
