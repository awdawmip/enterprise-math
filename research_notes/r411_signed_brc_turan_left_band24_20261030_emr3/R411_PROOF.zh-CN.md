# R411：带符号 BRC 固定左边界 s=24 的无界余阶 Turán 严格正性

2026-10-30，作者侧精确计算机辅助数学证明。状态：**UNREVIEWED / NOT_ADMITTED**；未取得原生 X6 物理对应或正式 Source Result。

## 对象与定理

在 R404—R410 原始十二支路**带符号** BRC K/J→B→D 辅助模型下，对整数 r≥s+1 定义

\[
\delta_{r,s}=[t^r](1-t)(1+t)^{2s}(1+t^2)^{r-s},\quad
H_{r,s}=\binom{r+s}{2s}\delta_{r,s},\quad
D_{r,s}=H_{r,s}^{2}-H_{r,s-1}H_{r,s+1}.
\]

**R411 定理：对每个整数 r≥25，严格有 D_{r,24}>0。**

## 完整精确证书的归约

复用 R404 已得到、仍待独立审阅的 Catalan 核恒等式

\[
\delta_{r,s}=\sum_{\substack{0\le j<s\\r-s+j\equiv0\pmod2}}
\binom{s-1}{j}2^{s-1-j}\operatorname{Cat}_{(r-s+j)/2},\qquad
\operatorname{Cat}_n=\binom{2n}{n}/(n+1).
\]

写 r=2m+ε（ε=0,1），取 C₀(m)=Cat_(m-1)、C₁(m)=Cat_m，并令 Δ_(q,ε)(m)=δ_(2m+ε,q)/C_ε(m)。用有理 Catalan 比值及二项式恒等式得到

\[
\frac{D_{r,s}}{[\binom{r+s}{2s}C_\varepsilon(m)]^2}
=\Delta_{s,\varepsilon}(m)^2-\lambda(r,s)\Delta_{s-1,\varepsilon}(m)\Delta_{s+1,\varepsilon}(m),
\]

其中 λ(r,s)=2s(2s−1)(r+s+1)(r−s)/[(2s+2)(2s+1)(r+s)(r−s+1)]。

r411_verify.py 按精确有理数消元，并在 s=24 分别获得 F_ε(x)=P_ε(x)/Q_ε(x)，全部整数多项式系数按降幂次序列在 **R411_EVIDENCE.json**，不是仅保存结论哈希。偶数 r=26+2x、m=13+x：deg P₀=deg Q₀=23，共24+24个系数严格正，其中 min(P₀)=28629346802397224108032，min(Q₀)=5138022400；奇数 r=25+2x、m=12+x：deg P₁=deg Q₁=24，共25+25个系数严格正，其中 min(P₁)=14314673401198612054016，min(Q₁)=10276044800。x 取每个非负整数，P、Q 的每一项均非负、常数项正，因此 F_ε(x)>0；归一化因子严格正。两种奇偶遍历 r≥25，故定理成立。该无限性来自**精确恒等式与正系数判号**，不是有限点外推。

## 实际独立检查

运行 `python r411_verify.py && python r411_independent_verify.py`（Python3.10+/SymPy）。实际输出：
```
R411_EXACT_PASS 2 49 49 96 288
EVIDENCE_SHA256 28c6e68c88adf262bbe92f5bb394887697acb8e78eacf36c076083c69b109603
R411_INDEPENDENT_INTEGER_PASS 10 points, 30 Catalan-kernel checks
```
96项原始整数 Turán 精确交叉乘法，288项原始/Catalan 核交叉核验，以及独立标准库对10个奇偶整数点的再计算（包含 r>120）；均无浮点判号。边界值 D_(25,24)=6611550104472736273986577680>0，D_(26,24)=9294934488716085135217059463744>0。全原始 JSON SHA256 为上述值，证书分组哈希见 JSON。

## 适用边界及下一问题

若前置 R403 Jet 传递恒等式成立，则对应退化 Turán 首项严格正、消零阶数为 4s=96；这**不**构成原生 X6 或物理定理，R403/R404 仍须独立数学审核。结合已发布作者侧右带 1≤r−s≤128 与左带 3≤s≤24，尚未覆盖的区域为 s≥25、r−s≥129，首个参数点 (154,25)。下一单元固定 s=25，尝试证明所有 r≥26 的正性或找到整数反例，并研究不依赖固定带宽的解析正性定理。

**来源：** GLOBAL_KNOWLEDGE_V1 main@07d09a5ffc60a64ebb38eee2ab1dabc900883d18；Enterprise Math main@bb6e9bc39ce163763e6ad3febc229a44bd53cf84；R410 Draft PR #1708 @ db4e02917c315bfdc15cb656b7a96b497d0af0ae。P000 和 ACTIVE 世界观未改。当前 em_context_manifest authority_granted=false；em_control_tasks 返回 CONTROL_QUOTA，Source owner 未确认。研究状态 AUTHOR_SIDE_EXACT / UNREVIEWED / NOT_ADMITTED。