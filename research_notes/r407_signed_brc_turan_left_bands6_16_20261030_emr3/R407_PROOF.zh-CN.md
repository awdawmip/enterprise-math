# R407 — 带符号 BRC：11条新的固定左边界 Turán 全余阶正性定理

2026-10-30。原始十二支路有符号 BRC K/J→B→D **辅助组合模型**，仅 K₃[t²]=−8(1+θ)、θ>−1；a=30−16θ。本文件是作者侧可移植精确计算机辅助数学证明；UNREVIEWED / NOT_ADMITTED，P000 与 ACTIVE 世界观保持不变。

## 全称定理

对整数 r≥2、0≤s≤r，定义

\[
\delta_{r,s}=[t^r](1-t)(1+t)^{2s}(1+t^2)^{r-s},\quad
B_{r,s}=\binom{r+s}{2s},\quad H_{r,s}=B_{r,s}\delta_{r,s},\quad
D_{r,s}=H_{r,s}^2-H_{r,s-1}H_{r,s+1}.
\]

**R407-A：** \(\boxed{\forall\,r,s\in\mathbb{Z}:6\le s\le16,\ r\ge s+1\implies D_{r,s}>0}\)。

由 R404 的 s=3,4,5 结论合并，得到全体 r>s≥3 且 s≤16 的严格正性；再与 R406 的 k=r−s≤128 定理合并，尚待证明区域收缩至 s≥17、k≥129、r≥146。每条固定 s 定理覆盖无限多个 r，不是对有限 r 的采样归纳。

## 推导、分子分母全系数证书

取 r=2m+ε，ε∈{0,1}，令 C₀(m)=Cat_{m−1}、C₁(m)=Cat_m，Cat_j=binom(2j,j)/(j+1)，Δ_{s,ε}(m)=δ_{2m+ε,s}/Cε(m)。由 R404.1 的精确 Catalan 正核恒等式，

\[
\delta_{r,s}=\sum_{\substack{0\le j<s\\r-s+j\ {\rm even}}}
\binom{s-1}{j}2^{s-1-j}\mathrm{Cat}_{(r-s+j)/2}.
\]

利用 Cat_{u−1}/Cat_u=(u+1)/(2(2u−1))（u≥1），逐项除以 Cε，得到 Δ 的确切有理函数。令

\[
\lambda(r,s)=\frac{2s(2s-1)(r+s+1)(r-s)}
{(2s+2)(2s+1)(r+s)(r-s+1)}.
\]

从 B_{r,s±1}/B_{r,s} 的二项式比值，严格得到

\[
\frac{D_{2m+\epsilon,s}}{(B_{2m+\epsilon,s}C_\epsilon(m))^2}
=\Delta_{s,\epsilon}(m)^2-\lambda(2m+\epsilon,s)
\Delta_{s-1,\epsilon}(m)\Delta_{s+1,\epsilon}(m).
\tag{1}
\]

对每组 s=6,…,16 与 ε=0,1，取 m₀=ceil((s+1−ε)/2)、x=m−m₀≥0，使用整数/有理符号消元将 (1) 化为互素整数多项式比 P_{s,ε}(x)/Q_{s,ε}(x)。**22对 P、Q 的全部非零整数幂系数严格为正**：253个正分子系数，253个正分母系数。ε=0 的 P、Q 次数均为 s−1；ε=1 均为 s。正系数多项式对所有 x≥0 恒正；B 与 C 恒正，故全部有效无界余阶的 D>0。具体的全部整数列由实际执行的 r407_verify.py 生成，原始机器证据 SHA256 为 855d13ebc40442e750942ecb0113d07719c046ef9716a73b0416b0acc6ee3aa0；任何非正整数或交叉验证失败均使程序中止而不打印 PASS。

供人工核查 s=6、ε=0、x=m−4 的第一份完整恒等式：

\[
\frac{D_{2m,6}}{(B_{2m,6}\mathrm{Cat}_{m-1})^2}=
\frac{409600x^5+7065600x^4+47936256x^3+158764480x^2+255146892x+159068052}
{1456x^5+21840x^4+115752x^3+283192x^2+326235x+143325}.
\]

## 实际运行与有效边界

实际执行 Python 3 + SymPy，命令：
python r407_verify.py --min-s 6 --max-s 16 --max-r 96 --out R407_EVIDENCE.json

返回 R407_EXACT_PASS；22份有理多项式证书，253+253个严格正系数，935项独立原始二项式卷积验证（7≤r≤96，6≤s≤min(16,r−1)）。程序把原始 H,D 的整数结果与 P/Q 通过交叉相乘逐项检验；无浮点判号。实际执行源码 SHA256：ae808d769dc7a7b5bbd9e191a075191830faafbccf7aebbf2f30a5d1c7f76e55；机器证据11,577字节，SHA256：855d13ebc40442e750942ecb0113d07719c046ef9716a73b0416b0acc6ee3aa0。

若采用 R403.1 作者侧的形式首项传递式 [a^(4s)]T_{r+s}^{(r)}=180^(2r−2s) D_{r,s} 和 a^(4s)|T，可推出本定理范围内 Turán 阶数恰等于4s。该传递式仍依赖 R402 原始 BRC 模型，正式独立审查与原生 Result/Driver 准入待授权工作流完成。本定理本身是组合系数的代数陈述，不断言原生 X6 或物理真理。

来源冻结：GLOBAL_KNOWLEDGE_V1 main@78f6e3adeafa9ba289243bc44594ba502f512f6f，Enterprise Math main@ed9e44843ff386caea4371cb3990323cbf219457；R404@89cba1614fe75643ffb61e3e715169e2de103528、R406@061fe73812cc1f5e1fd3fa060c860a4758288c22。原生 em_status 0.6.11 返回 research_authority_granted=false，em_control_tasks 返回 CONTROL_QUOTA，未获得正式 Source owner、CLAIM、Result/Review 权限确认。

**下一问题：**针对 s≥17、r−s≥129 给出统一的 Catalan 比值不等式，或先增补固定 s=17 之后的严格符号代数证书（需避免大 s 的表达式膨胀）。