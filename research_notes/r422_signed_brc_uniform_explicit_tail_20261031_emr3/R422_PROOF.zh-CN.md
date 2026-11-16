# R422｜带符号 BRC 辅助 Turán：全余阶显式正性阈值与定量下界

日期：2026-10-31。研究状态：AUTHOR_SIDE_ANALYTIC / EXACT_CHECKED / UNREVIEWED / NOT_ADMITTED。继承 R421 原始十二支路带符号辅助组合读出；非原生 X6 动力学或物理定理。

## 对象与新定理

对整数 m≥1、s≥3、r=s+m，定义

\[
\delta_{r,q}=[t^r](1-t)(1+t)^{2q}(1+t^2)^{r-q},\quad
H_{r,q}=\binom{r+q}{2q}\delta_{r,q},\quad
D_{r,s}=H_{r,s}^2-H_{r,s-1}H_{r,s+1}.
\]

令 \(W_s=\binom{2s+m}{2s}\binom{2s}{s}>0\)。**统一显式解析定理**：对于所有整数 \(m\ge1,\ s\ge72(m+2)^4\)，有

\[
\boxed{D_{s+m,s}/W_s^2\ \ge\ 4^m/[2(m+1)s^2]\ >0.}\tag{R422}
\]

这是 R421 每个固定 m 最终正性的首次显式统一阈值和正的定量余量。本证明不使用逐带机器证书；常数72不声称最优。

## 完整证明

**1. 原始带符号系数的精确分解。** 固定整数 \(q\ge n\ge0\)，对 \(|d|\le q\)，定义

\[
\rho_q(d)=\binom{2q}{q+d}/\binom{2q}{q}
=\prod_{j=0}^{|d|-1}\frac{q-j}{q+j+1}.
\]

二项式相邻比直接给出
\[
\rho_q(d)-\rho_q(d-1)=\rho_q(d)\frac{1-2d}{q-d+1}.
\]
以 \(d=n-2k\)，展开 \((1-t)(1+t)^{2q}(1+t^2)^n\) 的原始有符号卷积：
\[
a(q,n):=\frac{\delta_{q+n,q}}{\binom{2q}{q}}
=2^n\,\mathbb E\!\left[(1-2d)\frac{\rho_q(d)}{q-d+1}\right],
\quad\Pr(d=n-2k)=2^{-n}\binom nk. \tag{1}
\]
该平均仅作为计算恒等式；被平均项可为负，没有将 BRC 有符号支路改写为正质量。

**2. 有理误差界。** 对 \(|d|\le n\le q\)，各因子位于 \([0,1]\)，利用 \(1-\prod(1-u_j)\le\sum u_j\) 得
\[
0\le1-\rho_q(d)\le\sum_{j=0}^{|d|-1}\frac{2j+1}{q+j+1}
\le d^2/q\le n^2/q.
\]
因 \(q-d+1\ge q-n+1>0\)，
\[
\left|\frac{q\rho_q(d)}{q-d+1}-1\right|
=\frac{|q(\rho_q(d)-1)+d-1|}{q-d+1}
\le\frac{n^2+n+1}{q-n+1}.
\]
又因 \(\mathbb E[d]=0\)、\(\mathbb E[1-2d]=1\)、\(|1-2d|\le2n+1\)，式(1)推出
\[
\boxed{\left|\frac{q\,a(q,n)}{2^n}-1\right|
\le\frac{(2n+1)(n^2+n+1)}{q-n+1}.}\tag{2}
\]

**3. 三个相邻读出的统一控制。** 对 \(h=-1,0,1\)，置 \(q=s+h,n=m-h\)，\(b_h=s\,a(s+h,m-h)/2^{m-h}\)。在 \(s\ge72(m+2)^4\) 下，\(s\ge2m+2\)，所以 \(q\ge s-1\)、\(n\le m+1\)、\(q-n+1\ge s-m-1\ge s/2\)、\(s/q\le s/(s-1)\le2\)。且
\[
(2n+1)(n^2+n+1)\le2(m+2)^3,\quad
|s/q-1|\le1/(s-1)\le2/s.
\]
由式(2)及三角不等式，
\[
|b_h-1|\le\frac{8(m+2)^3+2}{s}
\le\frac{9(m+2)^3}{s}
\le\varepsilon:=\frac1{8(m+2)}<1. \tag{3}
\]
于是 \(1-\varepsilon\le b_h\le1+\varepsilon\)，每项严格正。

**4. Turán 差归一化与余量。** 用 \(W_q=\binom{r+q}{2q}\binom{2q}{q}=(r+q)!/[q!^2(r-q)!]\)，精确消去得
\[
\lambda=\frac{W_{s-1}W_{s+1}}{W_s^2}
=\frac{m s^2(2s+m+1)}{(m+1)(s+1)^2(2s+m)}
<\frac m{m+1}, \tag{4}
\]
因为 \((2s+m+1)s^2<(2s+m)(s+1)^2\)。从式(1)定义直接代换，
\[
\frac{s^2D_{s+m,s}}{4^mW_s^2}
=b_0^2-\lambda b_{-1}b_{+1}
\ge(1-\varepsilon)^2-\frac m{m+1}(1+\varepsilon)^2
=\frac{1-(4m+2)\varepsilon+\varepsilon^2}{m+1}.
\]
由于 \(\varepsilon=1/[8(m+2)]\)，分子严格大于
\[
1-\frac{4m+2}{8(m+2)}=\frac{4m+14}{8(m+2)}>\frac12.
\]
故成立 R422，证毕。全程为精确代数和有限乘积不等式，不依赖有限数值外推或浮点符号。

## 执行核验与后继

附加 R422_VERIFY.py 使用标准库精确 Fraction 与组合数：72组小规模输入中，直接原始带符号系数对照216项 δ 与72项 D；32组 m=1,…,32 在 s=72(m+2)^4 的阈值点验证三个 b_h 和结论。实际运行返回 R422_EXACT_PASS；参见 R422_CHECK.txt。测试是代码/公式交叉检查，无限量词由以上解析推导给出。

范围：任意 m≥1，s≥72(m+2)^4；对 s 较小的区域尚无新结论。下一步证明更低阶（如 O(m^3)）统一阈值，或研究 m≥257 且 257≤s<72(m+2)^4 的空白区，寻找不丢失符号与来源的全参数 TP₂ 机制。

来源：R421 原始精确表达与渐近研究，作者侧提交 719225d40906c948cc7f1f5f0d4929ed025a3463。本轮读 pin 为 GLOBAL_KNOWLEDGE_V1 main@7ac05e2ee9971c21e36189b61c3de301f5fe0dab、Enterprise Math main@f4112d8e365f1afba239d4ef242c94d3e049b80d。GitHub 用户 awdawmip；原生 Site 0.6.11 状态 research_authority_granted=false，control CODE_REVIEW_REQUIRED，活跃 Owner 未取得原生确证。P000、ACTIVE 世界观未修改。未经独立 Driver 审阅或正式数学接纳。
