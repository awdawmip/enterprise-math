# D25/R23 原始 S-low 的已发表超同余：Guo–Zudilin 外部成果复用与精确核验

日期：2026-10-27。分类：**EXTERNAL_PUBLISHED_PROOF_REUSE / NONBLIND_FINITE_CHECK / AUTHOR_CONTROL_NOTE / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY**。本记录仅作数学文献识别、可移植证据及复用，不是 Native Result、Driver Review、Reference、Synthesis、Follow-up 或发布研究任务。原有作者/贡献史及 frozen D25 pin 不变。

控制读取：`awdawmip/enterprise-math main@cd1850c9ab7d696aa52c36648ceed0d5adb0fc64`；本研究数学 pin `c47e13e4aba0e006366f989d6334d443f6333ae3`；GLOBAL_KNOWLEDGE_V1 `main@7093d637d9417831dc679e3ad783f27fc24ef739`；P000 原始 blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`。适用 ACTIVE worldview，原生 X6 空间+独立时间、三维切片和 BRC 来源保真不变。

## 1. 与 D25 原输入严格同式的既有定理

设 p>3 为素数，m=(p−1)/2；沿用 R23/R47 的两个不同算术来源：

```
w_k = (6k+1)(2k)!(3k)! / [(k!)^5 216^k]
s_k = (8k+1)(4k)!       / [(k!)^4 2304^k]
L_W = Σ_{k=0}^m w_k,     L_S = Σ_{k=0}^m s_k.
```

Victor J. W. Guo 与 Wadim Zudilin，*A q-microscope for supercongruences*, Advances in Mathematics **346** (2019), 329–358; DOI 10.1016/j.aim.2019.02.008; https://arxiv.org/abs/1803.01830，已证明其 Ramanujan `S((p−1)/2)` 截断在 **所有 p>3** 满足

```
L_S ≡ p·(−3/p) (mod p³),       (−3/p) 为二次特征。
```

这不是本研究新发现或新证明的定理：其项系数确实完全一致，因为 `binom(4k,2k)binom(2k,k)^2=(4k)!/(k!)^4`，且 `2^(8k)·3^(2k)=2304^k`；截断上限和权 `8k+1` 也相同。对于 D25 的素数类 `p≥13,p≡1(mod6)`，`(−3/p)=+1`，于是 **L_S≡p (mod p³)** 严格成立。相对于 R53 仅在共振 E={139,199,277} 逐点算得的 `L_S≡p(mod p²)`，这是全体目标素数的高一位已知数学输入，应准确归功原作者。

## 2. 原始 R23 source-labelled 等价化简

R23 作者已证、待原生独立审核的来源保持分解为

```
W_p−S_p ≡ (L_W−L_S)+p²·U_p (mod p³).
```

将已发表的 Guo–Zudilin 定理用于**完全相同**的原始 S 来源，不动 W、S、U、高阶边界或任何 R23 数学定义，可代数推出

```
W_p−S_p ≡ L_W−p+p²·U_p (mod p³),   p≥13,p≡1(mod6).
```

于是 D25 的原 supercongruence 目标 `W_p−S_p≡0(mod p³)` 当且仅当 `L_W−p+p²·U_p≡0(mod p³)`。此处“当且仅当”相对于 **R23 给定分解与外部已发表定理**；不是已经证明剩余目标。R36/R52 Green 两源、六 Hasse ports、native H0/B0 与 Frobenius、κ 均维持原标签和未完证明义务；只有指定 mod-p³ 低半和 observer 下的 S 值可用已知定理替换。

## 3. 同一轮独立于作者计算器的有限整数核验

另编写 Python 3 标准库直接模 p³ 阶乘、模逆和素数筛；对 `5≤p<5000` 的 **667 个素数**（p≡1mod6 有330个，p≡5mod6 有337个）全部精确计算原始两个低半和，**零失败**满足

```
L_S≡p(−3/p)(mod p³)  [既有 Guo–Zudilin 定理的有限交叉验证]
L_W≡p(−3/p)(mod p²)  [只做有限猜想/观察，没有全称证明]
```

在原始重要点 `p=139,199,277,373`，S 的 p³ 余数依次正好为 `139,199,277,373`；而 `(L_W−p)/p² mod p` 分别为 `126,27,267,107`。第二行 W 的普遍性仍需证明或找到已发表先验成果，不可由 667 例推断为一般定理。详细可复现的 stdlib checker 和 JSON 均保存于本次对话附件 `EM_DRIVER_D25_SOURCE_S_PRIOR_ART_AUDIT_20261027.py`、`.json`；脚本已实际运行且输出本地回读。

## 4. 后续具体证明义务与控制边界

1. 先核查 W 原始半和 mod p² 的真正先验文献/严格证明，而不是把有限共性自动升级。
2. 在 R23、R36 原始高项 `U_p` 和 W 来源之间建立同 rank/source-labelled 的模 p³ 抵消；目标 `L_W−p+p²U_p≡0` 继续 OPEN。
3. #1559 原生 H0/B0、p=373 的 `[X]U mod p²`、Frobenius/κ 仍属独立原始类研究，不以本外部同余替代。
4. 当前 Site 权限实际为 `source:read/control:read` 且不签发当前 Driver DA；此辅助研究不提交 native reviewer/CLAIM/Source checkpoint，不复活旧会话，不建立 V2 tasks，原贡献历史和审阅保持不变。正式消费须通过真实合法 Driver、exact review set 和当前 writer。

BRC 使用决议：`REUSE_APPLIED` 于已知 S-low 位数，保留两个 labelled 来源、有限 p-adic 精度与未闭合的有符号残差；不把正权 BRC 分支误作 signed cancellation，也不据此声称原生六维动力学数学准入。
