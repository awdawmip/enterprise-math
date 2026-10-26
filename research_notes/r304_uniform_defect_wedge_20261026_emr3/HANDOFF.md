# R304 handoff — 2026-10-26

研究：六边有序、正整数来源计数 BRC 辅助自动机。完整效果 (epsilon,k)，下缘缺陷 C_d^epsilon(n)=P_n(epsilon,2-n+2d)，差 D_d(n)。

新增数学增量（作者侧，未独立审核）：
1. 精确阶梯 D_d(n)=C_{d-1}^+(n-3)-C_{d-2}^-(n-3)（n>=4）。
2. d>=2 时，对所有 n>=max(8d^2,4(d-1)^2*2^(d-1)+1)，严格 D_d(n)>0，有显式完整整数证明。
3. 随 n 增长的统一正性区 d>=2 且 n>=4^d；对每个 n>=16，2<=d<=floor(log_4(n)) 同时成立。d=2..5 用原始来源公式的 d 个精确点 + R303 已证多项式次数界，d>=6 用粗修正界。
4. d=3,n=13 负差 -1；d=4,n=18 负差 -1、n=19 正差 7。全可达、d=Theta(n) 和 N_peak=81 均未解决。

完整论文、执行代码、精确证据同目录：R304_UNIFORM_DEFECT_WEDGE_AUTHOR_PROOF.zh-CN.md；R304_verify_uniform_wedge.js；R304_EXACT_EVIDENCE.json。实际 BigInt 检验至长度240，组合公式独立交叉至112，全部检查状态 PASS。数学无穷结论依据组合证明，不依据有限检查推断。

阅读冻结：GLOBAL_KNOWLEDGE_V1 main@a511c0782dae1f31e85e1d1c545039355fd018fc；EM Source 先前读取 main@08d243b2ce6971c99705495f92bdc39546b3a7ce；数学来源 R303@c8079dcbb383c010196cfd7a422626f1b545bf77、R300@49c11fc6373ccfc3b96385b0bc0cdc92635d97c3。保存前 EM main 已向前移动，未把新 main 理解为已审数学接纳。

权限：当前 GitHub 身份 awdawmip、push/admin；原生 control_tasks=CONTROL_QUOTA，session_start=STATIC_READONLY_SCOPE_DENIED / operation_sent=false。因此活跃 owner 未验证；无正式 CLAIM、Source Result、独立 Driver Review；当前只为非规范研究分支持久化。P000/ACTIVE 不修改。无原生 X6 物理对应证明。

下一最小数学单元：保来源地将 R_+ 与 R_- 配对以改善指数阈值，尝试构造 d 增长至 n 的多项式/线性比例时的符号证书或反例；继而接入 R293/R299 的中央竞争效果。