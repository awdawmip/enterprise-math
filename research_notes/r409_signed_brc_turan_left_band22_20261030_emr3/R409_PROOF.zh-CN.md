# R409 — 带符号 BRC 固定左边界 s=22 的无界余阶 Turán 严格正性

日期：2026-10-30。研究身份：本轮 ChatGPT 研究者，作者侧精确计算机辅助证明；UNREVIEWED / NOT_ADMITTED。尚未取得原生 Source CLAIM、Result 或独立 Driver Review。

## 定义与新结论

在 R404、R407、R408 相同的原始十二支路带符号 BRC K/J→B→D **辅助组合模型**内，令

\[
\delta_{r,s}=[t^r](1-t)(1+t)^{2s}(1+t^2)^{r-s},\quad
H_{r,s}=\binom{r+s}{2s}\delta_{r,s},\quad
D_{r,s}=H_{r,s}^2-H_{r,s-1}H_{r,s+1}.
\]

**R409：对所有整数 r≥23，严格有 D_{r,22}>0。** 这是固定 s=22 的全无界余阶命题，不是有限格点归纳。

## 证明：精确有理恒等式 + 全系数正性

所用已知依赖为 R404 Catalan 核公式（在其原始模型中）：

\[
\delta_{r,s}=\sum_{\substack{0\le j<s\\r-s+j\equiv0\pmod2}}
\binom{s-1}{j}2^{s-1-j}\operatorname{Cat}_{(r-s+j)/2},
\quad \operatorname{Cat}_n=\frac1{n+1}\binom{2n}{n}.
\]

令 r=2m+ε，ε∈{0,1}，C₀(m)=Cat_{m−1}，C₁(m)=Cat_m，Δ_{q,ε}=δ_{2m+ε,q}/Cε(m)。精确二项式比值推出

\[
D_{r,s}/[\binom{r+s}{2s}C_\epsilon(m)]^2
=\Delta_{s,\epsilon}^2-\lambda(r,s)\Delta_{s-1,\epsilon}\Delta_{s+1,\epsilon},
\]

\[
\lambda(r,s)=\frac{2s(2s-1)(r+s+1)(r-s)}
{(2s+2)(2s+1)(r+s)(r-s+1)}.
\]

以上所有等式在整数/有理函数环中精确运算；乘除归一化仅用于辅助系数符号证明，不能解释为对原始带符号分支数据的无损投影。

取 s=22，按 r 奇偶分类。偶数组 r=24+2x、奇数组 r=23+2x，x≥0。随附 r409_verify.py 从上述恒等式精确求得各自互素整数多项式 Pε(x)、Qε(x)，满足归一化 Turán 缺陷等于 Pε/Qε。偶数组两个多项式均为21次，奇数组均为22次。完整整数系数在 R409_EVIDENCE.json；**45个分子系数和45个分母系数全部严格正**。偶数组最小正分子/分母系数分别为 410440055640037523456 与 1085276160；奇数组分别为 205220027820018761728 与 2170552320。对所有非负 x，Pε(x)>0、Qε(x)>0；归一化分母原有的二项式与 Catalan 因子也严格正，故 D_{r,22}>0，定理证毕。

这是利用**两条完整精确符号恒等式及其所有系数**得到的无限族计算机辅助证明。用 SymPy（Python3）执行而非 Lean 形式核验，独立复审仍待完成。R404 的 Catalan 核原证明及 R403 十二支路至 Turán 首项的传递接口仍为条件性前置结果。

## 原始证据、核验范围及下一问题

运行 python r409_verify.py，实际得到 R409_EXACT_PASS 2 45 45 98 294。含98项整数 Turán/有理函数交叉乘法核对及294项原始二项式/Catalan 核核对（各奇偶组从最小合法 r 至120），这些有限排错核对不承担无限性的证明。确切边界值 D_{23,22}=27562974232842357772729500；D_{24,22}=32353841896625835086290517520。全部无浮点判号。

实际脚本 SHA256：35f8009d834b97eb51fa2722fc97f2551ba866f889e04dc4dcea7f6b2bbff74f；原始机器 JSON SHA256：08a6828ac1f563b6f1ff725e597440ef44d8d0320adb840ca9170d59f5bac470。R409_EVIDENCE.json 是实际运行的完整系数证据；详见 R409_HANDOFF.md。

知识快照：GLOBAL_KNOWLEDGE_V1 main@8a90490344dbf310db7764d8c53cb8274f0cd904；EM main@52149a3929b86948f137d3720e33014a59ab5afd；上游研究 branch@1f0c7508573fc1d02a6eddb3e60bf377cc8a5176。P000 ACTIVE_LOCKED 与 ACTIVE 世界观未修改。GitHub 连接主体 awdawmip；原生 em_status research_authority_granted=false，control_tasks 返回 CONTROL_QUOTA，未能确认活跃 Source owner。GH 作者侧存证不构成正式 Task CLAIM/Result/Review 或数学接纳。

与 R404/R406/R407/R408 的未审阅前沿合并，尚待解决的两侧阈值区域是 s≥23、r-s≥129，首个可能 r=152。下一步固定 s=23 的全部 r≥24 分奇偶精确证书或严格反例。结论不推广到完整 D-阵列 TP₂、无限 Q、心跳世界原生 X6 动力学或物理实证。
