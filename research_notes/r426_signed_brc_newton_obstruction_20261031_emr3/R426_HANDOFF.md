# R426｜研究交接与下一最小问题

本轮已完成：对原始 signed BRC 组合读出，独立证明全部整数 r≥4 的正系数行多项式 P_r(x)=Σ_(s=2)^r H_(r,s)x^(s−2) 不可能全部实根；精确分类 r=2,3 为实根例外。两个奇偶族各用一次 Newton 必要不等式和显式有理比率完成无界参数证明，r=5 另用 j=2 Newton 不等式。另得到 r=4 的 3×3 Toeplitz 负子式 -1568（PF₃ 阻断）。

研究输入：R425 作者侧、原始有符号因子 (1−t)，保留 Catalan 核的精确身份；不将标量结果当成十二支路全状态、原生 X6 计算或三维切片保真。详细陈述、完整代数证明与运行范围见本目录 R426_PROOF.zh-CN.md、R426_VERIFY.py、R426_EVIDENCE.json。运行命令：python R426_VERIFY.py --rmax 256 --out R426_EVIDENCE.json；独立本地等价程序返回 R426_EXACT_PASS 256 1125 759 253 253 1125 r4_pf3 -1568。

本轮固定主干来源：GLOBAL_KNOWLEDGE_V1 main@4b0f5f945fbaee76de9800c6cabf24eb1812fb3d，Enterprise Math main@220645478485d6379c23fcc51b4ea25b8a319981，上游作者侧研究 PR #1708 head@ca57161eb36c96ece7028145907342155ca9bd8b。

接下来最小科学问题：r≥5 时，对 H_(r,2),...,H_(r,r) 的全部 3×3 Toeplitz minors（含非连续行列选择与边界零填充）寻找最小负例；若找不到，寻找统一 PF₃ 解析证书。Newton 实根性失败不自动推导出 PF₃ 失败。所有结论标记 AUTHOR_SIDE_EXACT / UNREVIEWED / NOT_ADMITTED；正式 Task、Source owner、CLAIM、Result 与独立 Driver Review 分别由原生控制路径决定。

本轮原生控制查询报 CONTROL_QUOTA，DIRECTED_RESEARCH profile 为 authority_granted=false，因此只作为可移植作者侧研究材料保留；P000 与 ACTIVE 世界观未修改。