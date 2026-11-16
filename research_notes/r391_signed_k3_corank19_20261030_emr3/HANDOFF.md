# R391 portable research handoff

来源：GLOBAL_KNOWLEDGE_V1 main@6dd6d2d00b5bad517b119e48aa7c9b8426b45be0；Enterprise Math main@84b725104b07628241b4a12be4d77b423ebf6c0f；先前 R390 不可变源码 commit f6fc39da42ba9d11029076cf7642f2b5178a958c（PR #1708）。唯一参数变形 K3[t²]=−8(1+θ)，其他保号十二支路不变。

本轮 r=19 的39项 Newton 和37项 Turán 全参数有限分类，PF₂ iff −1<θ≤η19，η19 为 T19 在 (1862144/10⁶,1862145/10⁶) 的唯一根。另证明 T19 在 (1868088/10⁶,1868089/10⁶) 发生第二次局部转正，但 c19 仍严格负，不能误判 PF₂ 再入。证明见 R391_PROOF.zh-CN.md。

源程序：r391_exact.py、r391_symbolic.py、r391_certify.py。运行 python r391_symbolic.py && python r391_certify.py，复原 R391_POLYNOMIALS.json 和 R391_EVIDENCE.json；须保留与本 PR 同级的 R390 目录代码。预期 R391_SYMBOLIC_PASS / R391_EXACT_PASS、532精确交叉核验、80证书、91有理子区间、93次 Bernstein 检查、4348个严格正控制系数。完整摘要和不可变输出的 SHA256 见 R391_EVIDENCE_SUMMARY.json，所有数学符号及证明见 R391_PROOF.zh-CN.md。

实际控制：GitHub awdawmip 可写；原生 research_authority_granted=false，Owner 查询 CONTROL_QUOTA；不冒用别人的 session/CLAIM，原生 REGISTER_PENDING、DRIVER_UNREVIEWED、NOT_ADMITTED。P000/ACTIVE 世界观没有改变。研究范围只是保号 BRC 辅助有限 Q/D 观察；不覆盖全指标、整个 D 阵列或原生 X6 物理。

完成不重做：R390/r18 完整相图、本轮 r19 完整相图及第二局部根。下一科学问题：r20 的41项有限分类，或 T-center 二次变号与系数负性顺序的可证明阶增长规律；将 R386—R387 留数证明交给真实独立审阅者。
