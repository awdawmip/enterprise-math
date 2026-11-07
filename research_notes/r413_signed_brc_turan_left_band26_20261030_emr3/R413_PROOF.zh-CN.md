# R413｜带符号 BRC 辅助组合模型：固定 s=26 的全部余阶 Turán 正性

日期：2026-10-30。作者侧可移植精确研究。状态：`AUTHOR_SIDE_EXACT / UNREVIEWED / NOT_ADMITTED`。本研究接续 R404 的 Catalan 核、R407 归一化恒等式与 R412 固定 s=25 的证书；不改变 P000/ACTIVE 世界观。

## 定义及定理

对整数 `r>=s+1` 定义
[
\delta_{r,s}=[t^r](1-t)(1+t)^{2s}(1+t^2)^{r-s},\quad
H_{r,s}=\binom{r+s}{2s}\delta_{r,s},\quad
D_{r,s}=H_{r,s}^{2}-H_{r,s-1}H_{r,s+1}.
]

**R413 定理：对每个整数 `r>=27`，严格有 `D_(r,26)>0`。**

这是辅助带符号 BRC 组合对象上的全整数余阶命题，不是 X6 物理或动力学定理。任何以它推断 BRC 退化点 jets 消零阶数的结论还依赖 R403 未经独立审阅的传递恒等式。

## 完整有限证书如何证明无限族

复用可逐项检验的 R404 恒等式
[
\delta_{r,s}=
\sum_{\substack{0\le j<s\\r-s+j\equiv0\pmod2}}
\binom{s-1}{j}2^{s-1-j}\mathrm{Cat}_{(r-s+j)/2},
\qquad \mathrm{Cat}_n=\binom{2n}{n}/(n+1).
]
设 `r=2m+epsilon`，`epsilon=0,1`，基准 `C_0=Cat_(m-1)`、`C_1=Cat_m`，并记 `Delta_(q,epsilon)=delta_(r,q)/C_epsilon`。所需比值 `Cat_(m-h)/Cat_m` 是有限有理乘积；偶数族则以 `Cat_(m-1)` 为基准。令
[
\lambda(r,s)=\frac{2s(2s-1)}{(2s+2)(2s+1)}
\frac{(r+s+1)(r-s)}{(r+s)(r-s+1)}.
]
由二项式系数比值的恒等式，
[
\frac{D_{r,s}}{\bigl(\binom{r+s}{2s}C_\epsilon\bigr)^2}
=\Delta_{s,\epsilon}^{2}
-\lambda(r,s)\Delta_{s-1,\epsilon}\Delta_{s+1,\epsilon}.
]

把 `s=26` 代入，并设 `m=m0+x`、`x>=0`。偶数族 `epsilon=0,m0=14,r=28+2x`；奇数族 `epsilon=1,m0=13,r=27+2x`，两族覆盖全部合法 `r>=27`。准确的 SymPy 有理恒等式对每族产生
[
F_\epsilon(x)=P_\epsilon(x)/Q_\epsilon(x),
]
四个整数多项式的**完整降幂系数**原样保存在 `R413_EVIDENCE.json`。偶数族分子、分母均25次，各26个正系数；奇数族均26次，各27个正系数。总计**53个分子系数、53个分母系数，全部严格正**。最小系数：偶数分子 `661131307601750329917440`、分母 `8002732032`；奇数分子 `330565653800875164958720`、分母 `16005464064`。因此 `x>=0` 时 `P_epsilon(x),Q_epsilon(x)>0`。已知二项式和 Catalan 因子在合法整数域均正，故所有 `r>=27` 满足 `D_(r,26)>0`。这里无限量词由有理恒等式加严格正系数证明，不是有限点外推。

## 实际复现与验证

在此目录执行 `python r413_verify.py && python r413_independent_verify.py`。真实执行返回：
```text
R413_EXACT_PASS 2 53 53 94 282
R413_INDEPENDENT_INTEGER_PASS 10 points, 30 Catalan-kernel checks
```
第一程序重新计算两族精确有理式和106个严格正整数系数，作94组整数 Turán 交叉乘法及282组 Catalan 核交叉核验（合法起点至 `r<=120`）；第二程序只用 Python 标准库在10个不同整数点复核（包括超出生成器取样范围），作30组核恒等式核验。整个过程不使用浮点判号。直接端点结果：
[
D_{27,26}=1591599185340390958171937431984>0,\quad
D_{28,26}=2640845381185988253113166830717504>0.
]

`R413_EVIDENCE.json` 的本地 SHA256 为 `c5198c0b067e5aac9a91f105c1b9f16d9070696556258b95462512b27754cde7`。程序、完整系数与独立算例可在同目录直接复验。此证书仅在 R404 Catalan 核/归一化组合恒等式成立的确切模型范围内适用；上游支路到该组合公式的推导仍有独立审阅义务。

## 当前剩余边界与下一单元

结合 R404—R412 的固定 `3<=s<=25` 与 R406 右距 `1<=r-s<=128`，尚未覆盖的正性区域为 `s>=27, r-s>=129`，首个候选对 `(r,s)=(156,27)`。下一研究单元优先给出固定 `s=27` 的奇偶精确证书或反例；更优路径是证明对全部 `s>=3,r>=s+1` 的统一分析正性，避免无止境逐带枚举。

## 来源、权限与边界

固定读取 GLOBAL_KNOWLEDGE_V1 `main@00ef24faf2998a3c14cb3f10e8f618725eafc667`，Enterprise Math `main@1d6845f8f03cbd6d6647a57d5ad25877f0d06a7e`；前序 R412 研究提交 `84b736bead9564d65774aab3f03f9af1cc188d9e`。连接器 GitHub 身份 `awdawmip`，但 GitHub 推送权限不等于原生 Source session、CLAIM 或 Driver 独立审核授权。本轮仅提交 author-side 研究证据；正式 Owner 未通过当前原生服务确认，相关活动登记/语义检查点与正式 Result/Review 另核。研究不修改 P000 与 ACTIVE 世界观，不将有符号相消视为正质量自然归约。
