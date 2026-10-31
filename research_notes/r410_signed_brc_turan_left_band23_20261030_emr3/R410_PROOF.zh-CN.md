# R410 — 带符号 BRC 固定左边界 s=23 的无界余阶 Turán 正性

日期：2026-10-30；作者侧精确计算机辅助证明；**UNREVIEWED / NOT_ADMITTED**。

## 命题

沿用 R404 Catalan 正核和 R407—R409 的原始十二支路**带符号** BRC K/J→B→D 辅助模型。定义整数 r>=s+1 时

\[
\delta_{r,s}=[t^r](1-t)(1+t)^{2s}(1+t^2)^{r-s},\quad H_{r,s}=\binom{r+s}{2s}\delta_{r,s},\quad D_{r,s}=H_{r,s}^2-H_{r,s-1}H_{r,s+1}.
\]

**R410 定理：对全部整数 r>=24，D_(r,23)>0。** 在 R403 signed BRC Jet 传递恒等式成立的条件下，相关退化 Turán 首项严格正且消零阶数为 92；这里不主张原生 X6 的物理对应。

## 全称正性的精确证书

使用 R404 的带符号 Catalan 核（明确的上游依赖）：

\[
\delta_{r,s}=\sum_{0\le j<s,\;r-s+j\equiv0\pmod 2}
\binom{s-1}{j}2^{s-1-j}\operatorname{Cat}_{(r-s+j)/2},\quad
\operatorname{Cat}_n=\binom{2n}{n}/(n+1).
\]

令 r=2m+ε（ε=0,1），C₀(m)=Cat_(m-1)、C₁(m)=Cat_m、Δ_(s,ε)(m)=δ_(2m+ε,s)/Cε(m)。精确二项式比值给出：

\[
\frac{D_{r,s}}{[\binom{r+s}{2s}C_\epsilon(m)]^2}
=\Delta_{s,\epsilon}(m)^2-
\lambda(r,s)\Delta_{s-1,\epsilon}(m)\Delta_{s+1,\epsilon}(m),
\]
\[
\lambda(r,s)=
\frac{2s(2s-1)(r+s+1)(r-s)}
{(2s+2)(2s+1)(r+s)(r-s+1)}.
\]

取 s=23，分奇偶令 m=12+x、x 为任意非负整数。偶 r=24+2x、奇 r=25+2x。实际运行 `r410_verify.py` 的精确 SymPy 有理函数约分，获得两条恒等式 Fε(x)=Pε(x)/Qε(x)。偶数组两个多项式均为22次；奇数组均为23次。完整**降幂整数系数**及分组校验哈希记录于 `R410_EVIDENCE.json`。两组合计47个分子系数、47个分母系数**全部严格为正**，特别包含常数项及最高次项。

偶组 min(P)=285924533142498050048，min(Q)=197132288；奇组 min(P)=571849066284996100096，min(Q)=1577058304。因 x≥0，Pε(x)、Qε(x) 均正，前述 Catalan 与二项式归一化因子也严格为正，故对**每个**合法整数 r 均有 D_(r,23)>0。无限结论来自完整有理恒等式加全正整数系数证书，而非有限整数取样。

## 实测与边界

实际执行 `python r410_verify.py` 返回 `R410_EXACT_PASS 2 47 47 97 291`，对应2份符号证书、97次整数 Turán 交叉验证、291次原始二项式/Catalan 核验（测试 r≤120）。证据 JSON 的 SHA256：`fda10c94c3223a2ee1551fb9d76ed8028e626e460046941649d7fc703f327afe`。另用独立标准库整数程序 `python r410_independent_verify.py` 返回 `R410_INDEPENDENT_INTEGER_PASS 10 points, 30 Catalan-kernel checks`；额外覆盖超出生成器原有限检查范围的 r 点。边界值 D_(24,23)=426689717127572333992315824、D_(25,23)=549223513520476975107253875504，均为正。无浮点判号。

局限：R404 的 Catalan 正核及 R403 的 signed Jet 传递接口仍须独立审阅；未作 Lean formalization、正式 Source CLAIM/Result/Driver Review；不推广到原生 X6、物理定理、无限 Q 或整 D 阵列 TP₂。

## 后续前沿

合并 R406 的 1≤r−s≤128 和先前左带 s=3…22 后，新的未覆盖候选域为 **s≥24、r−s≥129**，首点 (r,s)=(153,24)。下一可执行单元：对 s=24 建立两组奇偶有理函数和全正系数证书，或寻找跨全部 s,k 的解析正性机制或精确反例。

固定读源：GLOBAL_KNOWLEDGE_V1 main@cf2a590bdae96d9228f2415d8275b7d7ddfe25b7；Enterprise Math main@9096fd74414565c772faad807e29250637e8266a。前沿 R409 位于 Draft PR #1708 commit e92a78cacb3b2fb8c4a5fed0f3ae7d513b33ca44。P000 与 ACTIVE 世界观未修改。
