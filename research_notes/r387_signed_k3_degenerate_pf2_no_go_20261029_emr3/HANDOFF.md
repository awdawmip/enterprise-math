# R387 研究接续 · 2026-10-29

本轮按原 R386 Sheffer 生成函数和原始带符号十二支路 K/J→B→D，证明 θ=15/8 时 **所有 r≥1 有限 Newton 系数序列均非 PF₂**。完整证明在 R387_PROOF.zh-CN.md；复现程序在 R387_verify.py；原始回归证据摘要 R387_SUMMARY.json。通过原始 R384 源码再生完整 R387_EVIDENCE.json。

原前沿：R386 作者侧形式留数证明，GitHub 不可变提交 00cab03254615ca4372f27aefa6b1b984849aa79；不重做已证明的奇数余阶 c_r 负项。R387 的新部分为全部偶数余阶：r≥10 的顶端 T_(r−1) 严格负性多项式恒等式，r=2,4,6,8 的精确原始 BRC 反例。

复现：在同一仓库研究注释目录中运行 python research_notes/r387_signed_k3_degenerate_pf2_no_go_20261029_emr3/R387_verify.py，依赖 R384 同目录兄弟源码和 SymPy。实际作者本地原始版本运行 R387_EXACT_PASS，含8偶数余阶共32项顶端恒等式、8奇数最高系数恒等式，核验 r=1..16。远端脚本是整理版，必须独立运行后才能称远端版本实测 PASS；本地结果及其 SHA 见 R387_SUMMARY.json。

下一步：独立 Driver 审核 R386 形式留数的全余阶换序/唯一多项式延拓和本轮顶端 jet 整理；然后考察 θ=15/8+ε 的统一 r→∞ 边界缩放。作者侧材料不等于原生 CLAIM、Source Result、Driver 审阅或接纳；R386 依赖、带符号支路来源和 X6 边界均须保留。GLOBAL_KNOWLEDGE_V1 固定读取 main@a9247ccc955548ff91fb15d319a0b8ab2fef480a；Enterprise Math 控制 main@55d5a6f9ed278a01b36f89952b76e3fe7641a9c3。
