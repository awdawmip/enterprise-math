# 第二位 mod p³ 文献有界交接

本次有界检索未找到覆盖 p ≡ 13,19 (mod 24) 的精确第二位证明。精确目标已出现在 2025 primary paper 的数值验证中；这既不构成证明，也不支持全局“未证明”或首次发现声明。

## 本次唯一目标

S_p = Σ_{k=0}^{p−1} (6k+1) binom(2k,k)² binom(3k,k)/216^k
    = Σ_{k=0}^{p−1} (6k+1) (1/2)_k (1/3)_k (2/3)_k/(k!)³ · (1/2)^k。

只问 S_p ≡ +p (mod p³)，p ≡ 13,19 (mod 24)。不把本单元扩大为旧 Sun A14(ii) 归一化后的 mod p³ / 原加权和 mod p⁴ Bernoulli 强式。CDLNS2013 的 mod p² 第一位和已冻结的曲线极性核对保持既有结果。

## 可以直接引用的精确前沿

[Babei–Roy–Swisher–Tobin–Tu, arXiv:2408.08844v3, 2025-03-12](https://arxiv.org/pdf/2408.08844v3) 的 §6、printed p.23、式 (6.8) 恰好是 [F_{6,(1/2,1/3,2/3)}]_{p−1}(1/2) ≡ sgn · ((1−λ)/p) · p (mod p³)，λ=1/2。式前报告的是适用素数 5 ≤ p < 150 的有限数值验证。该文定义 (1.1) 明确 F 的权重是 αk+1，因此这里的 6 确为 6k+1。

沿用已保存的 CM / 符号分类：两类素数均 (-6/p)=−1、(2/p)=−1，sgn=−1；λ=1/2 时 ((1−λ)/p)=(2/p)，所以该式预测 +p。没有重做第一位或 j 不变量校验。

| 位置 | 精度和条件 | 本目标是否获得证明 |
|---|---|---|
| BRSTT Theorem 2.1，p.6 | 模 p²；后文讨论模 p³ 的猜想升级 | 只覆盖已知第一位 |
| BRSTT Theorem 6.1，p.22 | 模 p³；参数 (1/2,1/6,5/6)，ordinary prime | 参数及素数条件均不匹配 |
| BRSTT Proposition 6.3，p.23 | 条件命题：若 Theorem 2.1 升为模 p³，则推出后续猜想 | 不能倒置为第二位证明 |
| BRSTT (6.8)，p.23 | 全参数、权重、λ 和 p−1 截断精确匹配；仅有限数值验证 | 为研究目标提供 primary 先例 |

[Beukers, arXiv:2403.03301v3, 2025-06-16](https://arxiv.org/pdf/2403.03301v3) 的 Theorem 1.22、printed p.9 是模 p³ 加权定理，但要求 p 在 Q(α) 分裂，并保留 Assumption (II)、积分性和单位等条件。Appendix C §9.3、p.29 的 F(1/3,1/2,2/3;1,1|108t)、系数 (3k)!(2k)!/(k!)⁵、α=√−6/3、t(α)=1/216 恰好匹配本目标的生成函数和点；目标两类素数却在 Q(√−6) 惰性，故不能直接使用 Theorem 1.22。所需 δ=−1/6 本单元未另行计算，分裂条件已足以排除直接套用。

不把 BRSTT 对未加权 F_0 的超奇异模 p³ 失败说明，当成本加权式 (6.8) 的反例；两者是不同目标。也未借助尚无证明的参数转换，把 half³、−1/8、q-sum 或其他权重的相邻结果算作本目标证明。

## 下一步及保留范围

Root 可继续 independently fixed OLD-R + 6τ 的消去关系 / LIFT 有限证书，追求本目标的第二位。文献 intake 的结论是“本次有界检索没有拿到现成证明”，数学单元保持开放。有限数值先例可进入背景引用，不能据此登记数学完成、首次证明或全 novelty audit 完成。

本地保存完整两篇原文、文本抽取、参数条件矩阵及读取 receipts。child bundle 为 modular-citation-scout/；根部 TARGET_MATCH_MATRIX.json 是本交接的紧凑总表；FINAL_ARTIFACT_PINS.json 冻结整个本地单元的 bytes/SHA256。既有 first-digit / Root Source bytes 未改。本单元没有 Task、Claim、Source 发布及 provider/API quota 操作。

P000 / Heartbeat 的语义绑定沿用当前合法会话；本次外部超几何模型不构成 Full-X6 传播声明。

