# Stage482-B | 增长 Q POP 预算的 Euler–BRC 后缀支持压缩
科学冻结：Global bf84bd7c61a2444b59b1da96be57df0e9ae47e53、EM 2af3fc484eb11060b69e0afc1b562bcaf5ad1419、P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488。行为规范读取届时 current normative context。

母问题：原生 X6 受限 A/B/C 历史 P=A^(2k+2), Q=A^(2k+2) W A H A，未来追加允许12个原生有符号方向；精确未来等价、Boolean 支持、正整数人口、rank/unrank。

最高作者侧前沿：Stage481-B 证明对任意合法 Q POP 预算 0≤h≤n−1 的修复键是 (W,suffix_min(h,u)(H))。h=3 的九边 Euler–BRC 公式及精确计算：k=12,u=9, Θ=(28,5,1,3,1,4,3,2,1)，q3=366818、总人口1763560。保留证明、复现程序、证据与本阶段独立执行/复现区别于 research_notes/n12_x6_native_brc_stage481b_three_q_pop_suffix_20261106_RESEARCH2。

下一明确问题：h=Θ(u) 时，如何对固定完整初始观察纤维避开 3^min(h,u) 的逐一后缀枚举？构建九向剩余边 DP 与确定性后缀自动机，完成 k=3,u=8,h=4..8 的精确支持计数，比较状态复杂度/总预处理/输入转换和正整数位长。处理 h≥u 时全部 H 字串可见的边界。给出证明、完整测试输入、可重现源码/结果与最小未解问题。

Source 角色、Owner/CLAIM、Result/Review 以实时原生回执为准；可独立推进的数学工作先保存至当前 PR #1736。