# Stage479-B — Q POP=1 三方向完整邻接修复

承接本目录 PROOF_STAGE478B.md。冻结科学输入（Stage477-B 原始 pin）：GLOBAL main bf84bd7c61a2444b59b1da96be57df0e9ae47e53；Enterprise Math main 2af3fc484eb11060b69e0afc1b562bcaf5ad1419；P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488。当前规范另用现行 canonical main。

母目标：原生 X6 完整六维位移、有向12×12邻接、位置 K 的未来等价、Boolean 支持、正整数人口和 rank/unrank。已完成但仍作者侧未经 Driver 审核的 Stage478-B：三方向 W,H 连续块在 Q POP=0 下未来精确键为 W；三字母有向 Euler 路树计数公式及 O(k^8) 整数算术支持算法。复现程序及执行结果同目录。

新研究：在 P=A^(2k+2),Q=A^m W A H A、W,H∈{A,B,C}，允许 Q 最多1次 POP、1次 APPEND，其它 P 预算照前，全部12个原生方向仍允许追加且操作交错任意。先对 k,u∈{1,2,3} 的全部 (W,H) 在固定完整初态 Phi 纤维中比较未来观察；检查同 W 是否仍等价，重点看 H 末方向被 POP 揭示时的邻接与终点变化。发现严格反例时记双历史、初始相同 Theta、可执行操作词、逐步 Phi 差异；否则只报告被穷举的有限域。继而用 Stage478-B 的有向 Euler 计数 N_l(s,t,e) 扩展隐藏人口，给出新修复边界和可计算的正整数类别统计。不得将 Q POP=0 结论直接推广。

正式 CLAIM、Result、Review 只按当前活跃 owner、真实 session 和不可变 task publication 取得。研究材料作为作者侧证据继续保存于现有 PR #1736。