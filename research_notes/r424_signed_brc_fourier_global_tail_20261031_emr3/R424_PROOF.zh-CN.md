# R424｜带符号 BRC 辅助 Turán：全余阶无界正性尾域

2026-10-31。科研等级：AUTHOR_SIDE_ANALYTIC / EXACT_CHECKED / UNREVIEWED / NOT_ADMITTED。严格对象：R423 的原始十二支路带符号 BRC 辅助组合读出；原生 X6 动力学保真对应未证。项目 P000 与 ACTIVE 世界观未变。

## 精确命题

定义 \(\delta_{r,q}=[t^r](1-t)(1+t)^{2q}(1+t^2)^{r-q}\)，\(H_{r,q}=\binom{r+q}{2q}\delta_{r,q}\)，\(D_{r,s}=H_{r,s}^2-H_{r,s-1}H_{r,s+1}\)。

**定理 A：对所有整数 \(s\ge50,m\ge1,r=s+m\)，严格有 \(D_{r,s}>0\)。** 该无限参数定理对 m 完全无上界，不依赖固定带计算机证书。常数50是充分条件，不声称最佳。

**定理 B：** 若 \(q\to\infty\)、\(0\le n\le q\)、\(n/q\to\alpha\in[0,1]\)，则
\[
\frac{q\delta_{q+n,q}}{2^n\binom{2q}{q}}\to(1+2\alpha)^{-3/2}.
\]
另对 \(q\ge\max(1,2n)\) 有精确界 \(0\le1-q\delta_{q+n,q}/(2^n\binom{2q}{q})\le(11n+8)/(3q)\)。

## A 的完整解析证明：原始符号及傅里叶正/负半弧

用有限多项式的单位圆系数积分（无解析延拓假设）：
\[
\delta_{q+n,q}=4^q2^n J(q,n),\quad
J(q,n)=\frac1{2\pi}\int_{-\pi}^{\pi}
(1-\cos\theta)\cos^{2q}(\theta/2)\cos^n\theta\,d\theta.
\tag{1}
\]
推导：\(t=e^{i\theta}\) 时两个幂因子分别为 \(4^q e^{iq\theta}\cos^{2q}(\theta/2)\) 和 \(2^n e^{in\theta}\cos^n\theta\)，取第 \(q+n\) 项后指数相位抵消，\(1-e^{i\theta}\) 的奇正弦积分为零。特别是 \(\cos\theta<0\) 的有符号部分完整保留。

取 \(r=s+m,L=s+m\)，设 \(A_q=\binom{r+q}{2q}\)，\(J_h=J(s+h,m-h)\)。逐项消去二项式因子，得到
\[
\frac{D_{r,s}}{(A_s4^s2^m)^2}=J_0^2-\Lambda J_{-1}J_{+1},
\quad
\Lambda=\frac m{m+1}\frac{(2s)(2s-1)(2s+m+1)}{(2s+m)(2s+1)(2s+2)}
<\frac m{m+1}<1.
\tag{2}
\]
从而 \(1-\Lambda>1/(m+1)\)。还具有关键的精确配方：
\[
\frac{L^2}{m+1}=4(s-1)+\frac{(m-s+2)^2}{m+1}\ge4(s-1).
\tag{3}
\]

令 \(J_h=J_h^++e_h\)，其中正半弧 \(|\theta|\le\pi/2\)，负半弧仍为原始带符号尾项。以 \(u=1-\cos\theta\)：
\[
I=J_0^+=\frac1\pi\int_0^1
\frac{u^{1/2}}{\sqrt{2-u}}(1-u/2)^s(1-u)^m\,du>0.
\tag{4}
\]
将(4)归一化为概率测度 \(\mu\)，设 \(T=(1-u/2)/(1-u)=1+Y\)、\(Y=u/[2(1-u)]\ge0\)。对 \(m\ge2\)，\(Y^2\) 可积。设 \(\eta=E_\mu[Y^2]\)，则
\[
J_{-1}^+/I=E[T^{-1}]\le1,\quad
J_{+1}^+/I=E[T]\le1+\sqrt\eta,\quad
0\le E[T]E[T^{-1}]-1\le\eta.
\tag{5}
\]
后式用 Cauchy 和恒等式 \(E[T]E[T^{-1}]-1=E[Y^2/(1+Y)]-E[Y]E[Y/(1+Y)]\)。

在 \(0\le u\le1/L\)，由 Bernoulli 及 \((1-1/L)^L\ge1/4\) 得
\[
I\ge(12\sqrt2\pi)^{-1}L^{-3/2}.
\tag{6}
\]
同时 \((1-u/2)^s(1-u)^{m-2}\le e^{-(L-2)u/2}\)，故
\[
I\eta\le\frac{\Gamma(7/2)}{4\pi}\Bigl(\frac2{L-2}\Bigr)^{7/2},
\quad
\eta\le\frac{90\sqrt\pi}{L^2}\Bigl(\frac L{L-2}\Bigr)^{7/2}
<\frac{190}{L^2} \quad (s\ge50,m\ge2).
\tag{7}
\]
末项仅用 \(90\sqrt\pi<160\)、\(L\ge52\)、\((L/(L-2))^{7/2}\le(26/25)^{7/2}<(26/25)^4<19/16\)。于是 \(\sqrt\eta\le1\)。

**不丢弃负半弧：** 定义 \(\tau=\max_{h=-1,0,1}|e_h|/I\)。由 \(u\in[1,2]\) 和(6)的粗界
\[
|e_h|\le(2\sqrt2/\pi)2^{-(s-1)},\qquad
\tau\le96L^{3/2}2^{-s}.
\tag{8}
\]
证明对**任意 m≥2** 都有 \(\tau\le L^{-2}\)：
若 \(L\le2s^2\)，由(8)，\(\tau L^2\le96\cdot2^{7/2}s^7/2^s<1152s^7/2^s\le1\)；最后一项在 \(s=50\) 用整数 \(2^{50}>1152\cdot50^7\) 检查，\(2^s/s^7\) 此后递增。
若 \(L>2s^2\)，在负半弧作 \(x=2-u\) 并设 \(q=s+h,n=m-h\)，则
\[
|e_h|=\frac{2^{-q}}\pi\int_0^1\sqrt{2-x}\,x^{q-1/2}(1-x)^n\,dx
\le\frac{\sqrt2}\pi\frac{2^{-q}}{q\binom Lq}.
\tag{9}
\]
此处直接用了整数 Beta 积分 \(B(q,n+1)=1/[q\binom Lq]\)。因为 \(s-1\le q\le s+1\) 且 \(\binom Lq\ge(L/q)^q\ge(L/(s+1))^{s-1}\)，故
\[
\tau L^2\le24\,2^{-(s-1)}L^{7/2}\Bigl(\frac{s+1}L\Bigr)^{s-1}
\le24\,2^{9/2-s}s^{8-s}<1,\quad s\ge50.
\tag{10}
\]
中间不等式利用左式随 \(L\ge2s^2\) 严格递减，以及 \((s+1)/(2s^2)\le1/s\)。两种情形均证明 \(\tau\le L^{-2}\)。

从(5)及 \(\sqrt\eta\le1\)，
\[
J_0^2\ge I^2(1-2\tau),\quad
J_{-1}J_{+1}\le I^2(1+\eta+3\tau+\tau^2).
\]
于是(2)、(3)、(7)、(8)–(10)给出
\[
J_0^2-\Lambda J_{-1}J_{+1}
>I^2\Bigl(\frac1{m+1}-\frac{196}{L^2}\Bigr)\ge0,
\quad (s\ge50,m\ge2),
\tag{11}
\]
因为 \(L^2/(m+1)\ge4(s-1)\ge196\)。严格正号由(7)的严格估计保证。

边界 m=1 可直接用中心二项式 \(C_s=\binom{2s}s\) 得
\[
H_{s+1,s-1}/C_s=\frac{2s(s^2-3s+5)}{(s+1)(s+2)},\
H_{s+1,s}/C_s=\frac{2(s-1)(2s+1)}{(s+1)(s+2)},\
H_{s+1,s+1}/C_s=\frac{2(2s+1)}{(s+1)(s+2)}.
\]
因此
\[
D_{s+1,s}/C_s^2=\frac{4(2s+1)(s^3-5s+1)}{(s+1)^2(s+2)^2}>0\quad(s\ge3).
\tag{12}
\]
(11)与(12)完成 A。精确边界反例：\(D_{3,2}=-5\)，因此全 s 无条件严格正性为假，必须保留这个回归反例。

## B 与核界的证明

沿用 R423 从原始有符号卷积导出的精确偶核：令 \(d=n-2K\)，\(K\sim\mathrm{Binomial}(n,1/2)\)：
\[
F(q,n)=\frac{q\delta_{q+n,q}}{2^n\binom{2q}q}
=E[\rho_q(d)B_q(d)],\quad
\rho_q(d)=\frac{\binom{2q}{q+d}}{\binom{2q}q},\
B_q(d)=\frac{q(q+1-2d^2)}{(q+1)^2-d^2}.
\]
对 \(q\ge2n\)，有 \(0\le\rho\le1,\ 1-\rho\le d^2/q,\ B\le1\) 且分母至少 \(3q^2/4\)，故 \(0\le1-\rho B\le d^2/q+8(1+d^2)/(3q)\)。用 \(E[d^2]=n\) 即得精确核界。

若 \(n/q\to\alpha\)，则 \(E[e^{itd/\sqrt q}]=\cos(t/\sqrt q)^n\to e^{-\alpha t^2/2}\)，故 \(d/\sqrt q\Rightarrow N(0,\alpha)\)。在 \(|d|\le K\sqrt q\)，乘积形式有 \(\rho_q(d)=e^{-d^2/q+O_K(q^{-1/2})}\)、\(B_q(d)=1-2d^2/q+O_K(q^{-1})\)。取 \(|d|\le q^{3/5}\)，由 \(\rho\le e^{-d^2/(2q)}\)、\(|B|\le6(1+d^2/q)\) 控制大 K 尾；\(|d|>q^{3/5}\) 用 \(|B|\le q^2+q+1\)、Hoeffding 界 \(P(|d|>q^{3/5})\le2e^{-q^{1/5}/2}\) 使尾期望趋零。因此 \(F(q,n)\to E[(1-2X^2)e^{-X^2}]=(1+2\alpha)^{-3/2}\)，其中 \(X\sim N(0,\alpha)\)（\(\alpha=0\) 为零常量）。Lévy/CLT 标准背景可参阅 MIT Mathematics 18.175 Lecture 15: https://math.mit.edu/~sheffield/175/Lecture15.pdf 。

## 验证、范围、下一问题

标准库精确复算程序 R424_VERIFY.py 与执行结果 R424_EVIDENCE_SUMMARY.json 同目录，实际输出：R424_EXACT_PASS 3320 1680 3319 1 global_tail_samples 90 negative_edge -5。精确整数/Fraction 核验3320项原始签名系数与偶核、1680项矩上界、90项新的全余阶尾域 Turán/归一化、边界反例；另外20项双尺度有限样本。**无限命题由上述证明支持，不以样本代替。**

冻结来源：GLOBAL_KNOWLEDGE_V1 main@d2d8c2f23743310331d91d020f43bbc30cdb20de；Enterprise Math main@9e5ac99311a1be29a5ac8330a8857e96cb43c033；R423 前沿 Draft PR head 7ae3dfd9cad5b0ca61f6becd107e44a6ba207da4。GitHub 接入身份 awdawmip；原生 DIRECTED_RESEARCH authority_granted=false，活跃 owner 查询 CONTROL_QUOTA，未获得正式 CLAIM、Result、独立 Driver Review、接纳。P000 与 ACTIVE 世界观未改。

最小下一问题：用原始 signed δ 完整分类 1≤s≤49 的正性/反例区域，并审计以前所有固定 s 证书的定义和边界；争取将50降为更小阈值。保留 m/s 双尺度极限与原生 X6 保真对应这两项不同科学义务。