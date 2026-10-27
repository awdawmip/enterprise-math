# 下一研究单元：N=3 两律共同策略的真实最优压缩常数

冻结输入：GLOBAL_KNOWLEDGE_V1 main@95662c56b4492b094365ee4e7a001939b2671e9e；Enterprise Math 原研究输入 main@d66a463c3c156840d4023b57e6a84e98eac8dfc8。本文及同目录 PROOF.md、DUAL_LOWER_BOUND.md、VERIFY.py、RESULT.json 为本轮作者侧 portable 研究，UNREVIEWED / NOT_ADMITTED。

本轮完成两步且无需重做：真实非对角树 Q 占用质量 Markov 化，将双律 (T,D) 联合 TV 统一上界从 |sa−sb|/2 降为 |sa−sb|/6，并在同一策略下精确保留双律完整停止时间边际；复用已发表的独立有理 facet 见证，将真实 minimax 压缩常数从无已证正下界提高为

\[
\boxed{15/2527\le K_*\le1/6}.
\]

K_* 的量词顺序是 sup_{0<sa,sb<1/2,sa≠sb} sup_{π full} inf_{σ compressed} max_{R=P,Q} TV(L_R^π(T,D),L_R^σ(T,D)) / |sa−sb|。直接占用平均算法在 (2/5,1/3) 同时达到 1/90，证明该算法的 1/6 统一系数不可改进，但此同一 π 存在另一全局无损压缩策略；不能因此宣称 K_*=1/6。

**最小未决**：构造针对所有压缩策略的更大精确有理下界，或改善压缩器上界；优先求 |sa−sb|→0 的双律线性化最优系数，明确保存策略、叶标号、双律质量、约束与证书语义。可按需使用已有有限 Bellman/支撑面工具，勿将有限抽样充当全域证书。

另一个独立问题是覆盖全部非对角参数的有限支撑法向证书。保持 BRC 有序来源与无跨时隐含种子；不得将外部概率辅助模型的结果当成 P000 原生六维 Cell 结论。上轮 23,328 张策略表已经有持久证书，勿重复计算。native owner/CLAIM 读取本轮返回 CONTROL_QUOTA，未获得正式 Result 或独立 Driver 审查。