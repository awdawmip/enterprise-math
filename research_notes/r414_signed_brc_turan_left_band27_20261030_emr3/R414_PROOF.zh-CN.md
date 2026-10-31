# R414｜固定 s=27 的全余阶 Turán 正性与三角 Catalan 递推

日期 2026-10-30。科学对象：原始带符号十二支路 BRC 的**辅助组合模型**；状态 AUTHOR_SIDE_EXACT / UNREVIEWED / NOT_ADMITTED。不会由该组合结论自动推出 X6 动力学、物理校准、正式 Result 或数学接纳。

## 定义及无限族定理

对整数 r≥s+1 定义

$$
\delta_{r,s}=[t^r](1-t)(1+t)^{2s}(1+t^2)^{r-s},\quad
H_{r,s}=\binom{r+s}{2s}\delta_{r,s},\quad
D_{r,s}=H_{r,s}^2-H_{r,s-1}H_{r,s+1}.
$$

**R414-A：所有整数 r≥28 均有 D_{r,27}>0。**

严格复用 R404 的 Catalan 正核恒等式：

$$
\delta_{r,s}=\sum_{\substack{0\le j<s\\r-s+j\equiv0\pmod2}}\binom{s-1}{j}2^{s-1-j}\mathrm{Cat}_{(r-s+j)/2},
\qquad \mathrm{Cat}_n=\binom{2n}{n}/(n+1).
$$

写 r=2m+ε，ε∈{0,1}；偶族取 C_0=Cat_{m-1}、奇族 C_1=Cat_m，令 Δ_q=δ_{r,q}/C_ε。二项式因子之比严格为

$$
\lambda(r,s)=\frac{2s(2s-1)}{(2s+2)(2s+1)}\frac{(r+s+1)(r-s)}{(r+s)(r-s+1)}.
$$

代数恒等式给出

$$
\frac{D_{r,s}}{(\binom{r+s}{2s}C_\varepsilon)^2}
=\Delta_s^2-\lambda(r,s)\Delta_{s-1}\Delta_{s+1}.
$$

取 s=27，m=14+x，x≥0：偶族 r=28+2x，奇族 r=29+2x。使用完全精确的 Catalan 相邻比有理乘积消元，每族得到 F_ε(x)=P_ε(x)/Q_ε(x)。完整的四个整数多项式降幂系数均保存在同目录 R414_EVIDENCE.json，由 r414_verify.py 可复算；并由独立标准库程序复核原始二项式定义。

偶族 P、Q 各 27 个正系数（次数26），奇族各28个正系数（次数27）；共55个严格正的分子系数和55个严格正的分母系数。最小 P 系数依次为4117903573062330626342912和8235807146124661252685824；最小 Q 系数为12918456320和103347650560。因此对所有 x≥0，P_ε,Q_ε 严格正，原归一化因子亦正，从而 R414-A 对所有合法整数 r 成立。此为**计算机辅助的精确有理代数证明**，不是有限网格外推，仍待独立数学审阅。

直接整数端点：
D_{28,27}=24725213384445862173893141337280>0；
D_{29,27}=44355235557195938248473728156459200>0。

## R414-B：完全独立的二参数 Catalan 三角递推

对 r≥1、0≤s<r，

$$
\boxed{\delta_{r,s+1}=\delta_{r,s}+2\delta_{r-1,s}},\qquad
\delta_{r,r}=\mathrm{Cat}_r,\quad \delta_{0,0}=1.
$$

**证明：**直接在 δ_{r,s+1} 的形式多项式中使用 (1+t)^2=(1+t^2)+2t，取 [t^r]，右边分别得到 δ_{r,s} 和 2δ_{r-1,s}；边界系数为
[t^r](1-t)(1+t)^{2r}=binom(2r,r)-binom(2r,r-1)=Cat_r。
无需 R404 正核假设和符号库即可计算三角整数表，并保留带符号的原始组合信息。

由此揭示一个统一证明的障碍：δ 自身并非必然 PF₂。精确反例为 δ_{4,2}=2、δ_{4,3}=4、δ_{4,4}=14，故其 Turán 差为 16-28=-12<0；但 H_{4,2}=30、H_{4,3}=28、H_{4,4}=14，使 D_{4,3}=784-420=364>0。二项式权重的补偿不能忽略。

## 复算、证据与明确范围

实际运行得到：

    python r414_verify.py
    R414_EXACT_PASS 2 55 55 93 279
    EVIDENCE_SHA256 151a47fd23e16a18ec78878a010cc5d2ed8b6e3659968427260d0380d53809a4
    python r414_independent_verify.py
    R414_INDEPENDENT_INTEGER_PASS 10 points, 30 Catalan-kernel checks
    python r414_recurrence_check.py
    R414_RECURRENCE_PASS direct_coefficients= 1347 s27_cert_crosschecks= 293 uncovered_region_positive_grid= 13530 first_uncovered= (157, 28) s28_unknown_grid= 164

第一程序生成奇偶两族精确证书，并作93次 Turán 与279次 Catalan 核交叉检查；第二程序使用标准库独立检查10个整数点及30个核对应；第三程序用独立证明的递推核对1347个原始系数、全部28≤r≤320的293个 s=27 证书实例，以及仍未由无限族证明覆盖的区域 157≤r≤320、28≤s≤r-129 共13530个点全部严格正。**后者是有边界的有限穷举，不证明 r>320 的无限区。** 所有判号均为精确整数/有理运算，没有浮点近似。

前序 R404/R407 提供辅助组合公式的来源；R403 的十二支路到 jets 传递仍需独立审阅。因此本轮只证明清晰定义的辅助组合对象，保留带符号相消与原生 X6 的界限。

结合作者侧 R404—R413 左带和 R406 的 r-s≤128 右带，未覆盖全域为 s≥28、r-s≥129；首个 (r,s)=(157,28)。下一步优先固定 s=28 的无界余阶证书或反例，进一步从递推与 binom 权重推导无固定带上界的解析论证。

来源固定：GLOBAL_KNOWLEDGE_V1 main@b6c619c8fe019e2f827c5975248d7c535a14cbd4；Enterprise Math main@ab9514aa4e200b0033da23ea4b3e895516c63dd2；R413 前沿 a3d85247f065a0f27ff7923f1e329820deec2153。当前 GitHub 登录 awdawmip；原生 gateway research_authority_granted=false、control_tasks 返回 CONTROL_QUOTA，不能权威确认活跃 Source owner。本报告不声称有 CLAIM、Result 或独立 Driver 审核。
