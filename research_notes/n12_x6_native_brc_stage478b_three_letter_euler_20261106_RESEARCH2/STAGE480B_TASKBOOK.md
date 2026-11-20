# Stage480-B — 两次 Q POP 的精确后缀修复

前沿：本目录 PROOF_STAGE478B.md 和 PROOF_STAGE479B.md。科学冻结 pin：GLOBAL main bf84bd7c61a2444b59b1da96be57df0e9ae47e53；EM main 2af3fc484eb11060b69e0afc1b562bcaf5ad1419；P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488。现行行为规范从当前 canonical main 加载。

已获作者侧证明：在 P=A^(2k+2)、Q=A^m W A H A、W/H 为原生 A/B/C 三方向连续块、P POP/APPEND≤k、Q APPEND≤1、未来追加12方向的完整观察纤维，Q POP=0 时精确未来键 W；Q POP≤1 时键 (W,H末)，存在 k=1,u=3 的一 POP 严格区分证人。所有类别的人口采用三字母 Euler 有向九边统计的精确矩阵树公式，支持计数 O(k^8) 整数运算。k=24,u=18 时 POP1 类别11,077,827,340、来源人口29,751,344,474,760；证据和可运行程序见本目录。数学结论仍待独立 Driver 审核。

下一实质研究单元：Q 最多两次 POP、一次 APPEND，P 最多 k 次 POP/APPEND，允许全部12个原生方向和合法交错。研究 u≥2 时是否仅需新加 H_{u-1}，并特别处理 u=1 时第二次 POP 跨过隐藏 H 到其前的 A 边界。给出必要和充分证明或严格反例（含两历史、同初始 Phi、操作序列、逐步差异），并建立修复后缀边界与九边 Euler 人口的精确公式。对 k,u≤3 的全组合穷举核对，报告完整覆盖和实际代码。

成果保留在 PR #1736 作者侧研究分支。正式 CLAIM、Result、Review 以当前身份、真实 owner 和 V2 publication 控制；发表研究草稿不等于数学接纳。