# R427 research continuation / 作者侧交接

本轮最高可复算前沿：对任意整数 r≥5，R426 的左端 Toeplitz 3×3 子式 L_r 全部严格为正；r=4 的同一子式等于 −1568。对每一行 5≤r≤24，利用有严格数学论证的支撑归约与精确整数穷举，完整证明 PF₃，包括无穷多 Toeplitz 位置。共有 59,185 个未分裂 2×2、16,616,469 个未分裂 3×3 行列式精确判号。R427_VERIFY.py（标准库）可确定性重建 R427_EVIDENCE.json，原始 JSON SHA256：a5700ce107294edb1fe1625bf6e5a8b8a5dc90d849bf97682e76074829826475。

最小下一问题：对 r≥25 构造统一 PF₃ 证明，或找到某一行全部三阶 Toeplitz 子式中的最小负例。优先解析内部连续三阶子式 j≥2，再处理非连续子式；不要用 j=1 的无限证明代替全体三阶证明。可考虑 Catalan 加权核、binomial 混合和保留 signed 支路的精确路径解释。独立审计需分别检查 (a) 两个奇偶比值表与多项式等式；(b) 支撑约化无遗漏；(c) 代码循环边界；(d) 科学对象是否仍为 R426 辅助模型。

读源：GLOBAL_KNOWLEDGE_V1 main@b1dac7cea151ce52a6ab1c265438f2d53cf99c3a；Enterprise Math main@53a45e72087663916ab1e3e764655a009519f8b4；R426 源提交 7fc9fabf09d997b7ac3496d6ebeafcb29b68728b。状态 AUTHOR_SIDE_EXACT / GITHUB_PERSISTED / UNREVIEWED / NOT_ADMITTED，正式原生 owner/claim/result/driver 判定不能由本稿替代。P000/ACTIVE 均未修改。

验算：运行 python R427_VERIFY.py，将在同目录写 R427_EVIDENCE.json；输出末行应为 R427_EXACT_PASS 59185 16616469 a5700ce107294edb1fe1625bf6e5a8b8a5dc90d849bf97682e76074829826475。
