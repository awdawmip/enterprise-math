# R305 — 可接续研究前沿（2026-10-26）

对象：有序六边、正整数来源的 BRC 辅助自动机；完整效果 (epsilon,k)；下缘缺陷 D_d(n)=P_n(+,2-n+2d)-P_n(-,2-n+2d)。

本轮确切新结论（作者侧，未经独立 Driver 审查）：
1. 对所有整数 d>=2 且 n>=8d²，D_d(n)>=binom(n,d-2)[n/(4(d-1))-7(d-1)/6]>0。已从 R303 精确首返分解独立推导 r=d-b+1、尾负号 t 位置计数 binom(d-r,t)，借 Vandermonde 得到 R_- 的多项式规模统一上界；显著强于 R304 的指数增长阈值。
2. 缺陷差双变量生成函数 F(x,z) 及其四阶缺陷递推在完整证明第三节，可作为后续正性和高阶有限差分的解析接口。
3. 实际执行 BigInt：n=0..240、d=0..44 的10,845次独立原始DP/有理系数相等；532次已证明窗口有限检查；6,235次更强 n>=4d+4 的有限正性观察（**不是**无限证明）。

冻结知识入口 Global main@7c86b60d4cfc7286c4ef16458f1ce22e29da10ba；项目协议源 main@c3cb394e7f8ffa3d21fa594bd0bd1b1c5e0c6bd1；依赖 R303@c8079dcbb383c010196cfd7a422626f1b545bf77 和 R304@36ba768da6c7df9f657e33b89cf6410c8d01350f。P000、ACTIVE 不修改。未证明原生 X6/心跳物理映射。

未完成：活跃 owner 原生只读查询 CONTROL_QUOTA，原生 session_start 因 static_machine_readonly 返回 STATIC_READONLY_SCOPE_DENIED / operation_sent=false；未取得 CLAIM、Source Result、独立 Driver Review。本分支是作者侧证据存储，不是状态机接纳。请在恢复正规权限后走原生 owner/claim/admission，避免把账户 GitHub 权限解释成研究角色。

最小下一科研单元：证明或证伪每个 d>=2 对全部 n>=4d+4 有 D_d(n)>0。优先从本轮双变量有理函数推导 n=4d+4 的 Newton 正差分或来源级匹配。若建立线性统一正性证书，再连接中央竞争者和 N_peak=81，不重做已通过的 R303/R304 检验。
