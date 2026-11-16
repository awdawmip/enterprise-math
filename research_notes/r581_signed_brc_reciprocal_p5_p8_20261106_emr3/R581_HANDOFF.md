# R581｜Portable research handoff

冻结科学输入：R462@18783e01e3646c72b7aab3b16d3f565e83e6446f (signed 12-branch BRC)，仅研究该输入派生的 Q_k Toeplitz–Hessenberg 辅助标量观察。可复用前沿：R580@58a6b4e8ef4325896238b770e621d1483af5bb08。

**本轮实际完成**：对固定 k，精确推导全部合法域内 T_5,T_6,T_7,T_8 四个有理函数闭式；其 normalized large-k limits 分别为 63/8、231/16、429/16、6435/128；据 T_8 得 limsup min|λ_{k,i}| ≤ (128/6435)^(1/8)≈0.6128196427。完整定义、证明、公式和域见 R581_PROOF.zh-CN.md。

**复现**：Python 3.13.5 / SymPy 1.14.0，运行 `python R581_VERIFY.py`；stdout 见 R581_EVIDENCE.txt；终止标记 `R581_RECIPROCAL_P5_P8_EXACT_PASS`。符号核对覆盖所有 k≥各自域下界；独立标准库整数/Fraction 核对 k=2..90 中348个有效组合。代码文件 Git Blob 期望值 `3a7d381dc4169406b8866f94c2784f373db8e769`。

**剩余问题**：任意固定 m≥1 的极限是否均为 binom(2m,m)/2^m；需要统一的生成函数/渐近证明或最小反例。之后进一步研究微观极限谱及原生 BRC→辅助读出的保真关系。作者侧全参数数学证明和局部证书已保存，独立 Driver 审查待办。

**本轮原生状态**：原生研究 session_start 回执为 FAILED/OSError，没有新 Researcher-ID、Research-Activity-ID；X6 Owner exact query 遇 EVENT_COLLECTION_IO，reconcile 后为 QUEUED，当前 Owner 未核实；没有 CLAIM，不发布正式 Result/Review。此目录属研究持久化，不是 P000/Working Truth/Foundation 变更。
