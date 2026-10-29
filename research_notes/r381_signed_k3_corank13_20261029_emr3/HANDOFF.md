# R381 可移植研究接续包（2026-10-29）

入口：Enterprise Math Draft PR #1592。原始十二支路带符号 R346 BRC K/J 核，只改动负支路 K3[t²]=-8(1+theta)，theta>-1。对第十三余阶27项有限原始 D/Newton 观察，完成 PF2 当且仅当 -1<theta<=eta13 的全域分类。eta13 为 T13 在 (1850889/1e6,1850890/1e6) 的唯一零点，约 1.8508899056188908。

材料：R381_PROOF.zh-CN.md 载有定义、根的唯一性和从阈值至无穷的严格负性闭区间覆盖；R381_compute.py 从原始符号支路生成全量27个系数、25个 Turán 多项式与 R381_COEFFICIENTS.json；R381_verify.py 验证66次精确有理 Bernstein、2041个严格正系数、81个分离算路精确有理点等式，并生成 R381_EVIDENCE.json。R381_EVIDENCE_SUMMARY.json 给出精确输入/摘要/哈希。依赖同一 PR 上 R346_verify.py 和 R369_check.py；在仓库根依序运行上述 compute、verify。开发环境 Python 3.13.5 + SymPy 1.14.0，本地执行状态 SYMBOLIC_PASS / EXACT_PASS。

控制边界：本轮 GitHub 身份 awdawmip；原生 Site gateway 仅静态只读且 research_authority_granted=false，Owner 查询 CONTROL_QUOTA。作者侧研究，不认领 canonical CLAIM/Result/Review、独立审查或 Working Truth；P000/ACTIVE 世界观不变，模型与 X6 仍待证明正式桥接。历史 R370—R380 综合共同阈值 sigma6 (约0.9018959) 仅按旧作者侧结论条件复用。

接续问题：r=14 29项有限原始 D 观察的 PF2 全参数相图，先在 (-1,sigma6] 内找严格反例；独立验证 R348/R363 全指标抽取及 theta=15/8 次数退化边界，不重复本轮已验证的确定性证书。
