# Stage294-B｜适应性动作、弱可合并与受限共享端口的误差

状态 PORTABLE_RESEARCH_INPUT / UNREVIEWED / NOT_ADMITTED，作者侧 Draft PR #1571；不授原生 Task/CLAIM/Result。输入 Stage293-B PROOF_STAGE293B.md、REPRO_STAGE293B.py、实际 stdout，及 Stage292-B 完整前沿。固定科研输入 GLOBAL_KNOWLEDGE_V1 main@e3f641701916719b0833085e3e246769d1214787、Enterprise Math main@1be949decd7509ac2094726b38e9fc292928cbe1。

已证不重做：在有限有理状态、全状态逐步 Markov 商类型下，输出下降与每动作标签块到达质量常值是充要条件；按可见输出起步、逐步签名细分得到最粗安全商。四状态 a→c→d、b→a，观测 o(d)=1、其余0，静态一步 a/b 图无边，但两步结果不同；全状态最少4标签。一个初始标签下的来源加权条件 TV 精确最优 1/3，池化可为0。固定任意未来输出核 Q 的 k 标签问题可经枚举标签及有理 LP 求解；不等于共享 Bernoulli 受限端口优化。

具体任务：研究只要求一个初始混合律的 finite-horizon/weak lumpability 与逐状态 strong lumpability 的严格差别；构造至少两个可选动作、下游可按已观察历史选择动作的全有理最小反例或证明新的完整未来语言闭合条件。进一步将 Q 限制为同一 Bernoulli 参数经重复端口得到的可实现核，证明 k=2 的准确最优或 strict LP gap。列出全部到达历史、来源、零质量分支、路径概率、完整观察语言；完成自足证明和 Python Fraction / 精确符号验证，保存实际执行日志。

未来有原生权限时单独核对活跃 owner、正式 CLAIM/Result、独立 Driver 复核和 P000 原生 X6/BRC 对应。保留 Stage278-A N12 Bellman 独立支线。