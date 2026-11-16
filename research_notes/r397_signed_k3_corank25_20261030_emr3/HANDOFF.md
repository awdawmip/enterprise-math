# R397 作者侧可移植研究交接｜2026-10-30

继承 R396 PR #1708 commit 9463550d225d4d2fa18ee1899ea3503bd3553ccb，原始 signed K/J Git Blob 1579ceb717ab1945227eca4f7a1878bf4ffa73e1。固定来源 Global main@95dfee104cbc38594d597ef00163624844d63c0a、Enterprise Math main@5d5b1d8b07ccc807c71e7d8c11f2a2f65edb8aec。研究仅将 K₃[t²] 设为 -8(1+θ)，θ>-1。

**已完成：** C25(θ)∈PF₂ ⇔ -1<θ≤η25；η25 唯一根在 (1866885/10^6,1866886/10^6)，近似1.8668857241477095；T25 次生唯一简单根在 (1870578/10^6,1870579/10^6)，局部 c25<0。θ=15/8 时全部 s=1..25 的 c_{25+s} 消零阶数2s、s=1..24 的 T_{25+s} 消零阶数4s；c24,c25<0。顶部 c50=4861946401452(30−16θ)^50。

**可执行复现：** Python 3 + sympy，python r397_symbolic.py && python r397_certify.py；已实际得 R397_SYMBOLIC_PASS、R397_EXACT_PASS，700个 Fraction 交叉等式、104证书对象、115有理段、120 Bernstein 检查、7166严格正控制系数。R397_EVIDENCE_INDEX.md 无损恢复原始 JSON，源码重建51个 C 和49个 T 多项式。

**当前角色与状态：** GitHub awdawmip；本 ChatGPT 研究3 上下文的作者侧实际贡献。原生 em_status v0.6.11 报 research_authority_granted=false，em_control_tasks 返回 CONTROL_QUOTA，活跃 owner 未获权威确认。UNREVIEWED / NOT_ADMITTED / ACTIVITY_REGISTER_PENDING；无原生 CLAIM、Result、Review 回执。

**下一问题：** 研究统一余阶的 (2s,4s) 消零阶数定理成立条件或反例，解释奇偶阈值交错，另可计算 r26。BRC 带符号辅助模型尚无 X6 原生动力学映射。P000/ACTIVE 世界观不改。
