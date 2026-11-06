# Stage476-B — 可变 k 的边界 BRC 压缩与语义独立核验

冻结科学输入（继承 Stage474/475，不以本轮 current HEAD 替换）：
GLOBAL \`bf84bd7c61a2444b59b1da96be57df0e9ae47e53\`；EM \`2af3fc484eb11060b69e0afc1b562bcaf5ad1419\`；P000 blob \`bcc2590d3168a28f72e8b9f0f9b1f76faadcd488\`。当前行为规则仍须单独读取。

母目标：原生 X6 有序历史完整标记未来观察的精确等价、布尔支持、正整数原始人口和可逆排名。

最高作者侧前沿：Stage475 独立证明任意有限 k 代数修复键的停滞区间 m-k+1≤t≤min(n,m+k+1)，且 k=3,t≥m-1 使用固定大小头标签的正整数 BRC 递推；Stage474 覆盖 k=3,t≤m-2。执行结果见同目录 PROOF、REPRO、EXECUTION_SUMMARY；大纤维 t=33..39 全为394240类，t=40降至300032类。Stage474.1 的完整未来操作语义仍待独立审核，没有正式 CLAIM/Result/Driver acceptance。

具体可执行问题：当 k 随 m 增长时，能否在不显式枚举3^k边界字串的前提下，构造能够精确计数 support、population 和 rank/unrank 的确定性正整数 BRC 自动机？优先用 m=2k+2 或 m=3k 的可验证构造：一组具有相同边计数/K而不同未来标签的序列，检查任何候选合并的观察后果、输入变换费用和输出排名费用。另一独立研究单元逐字校验 Stage474.1 在 POP 已追加步骤及 P/Q 双侧 APPEND 所有12方向交错中的充分性与必要性；找到最短有效反例则保留并修正键。

交付应包含严格证明或明确范围反例、可重现计算证据、剩余问题及原生 Source 真实权限/owner 回执，按现行协议保存，不通过作者侧 GitHub 提交冒充正式接纳。
