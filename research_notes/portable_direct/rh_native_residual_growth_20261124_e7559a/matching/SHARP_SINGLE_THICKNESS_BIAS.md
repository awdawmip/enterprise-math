# 单厚度完整道路的首阶偏差、尖锐加权尺度与算术校正

日期：2026-11-24（Asia/Hong_Kong）。作者统筹 `EM-DIRECT-E7559A / TASK_RESEARCH`，Activity `RA-D2F111EA1C0D4B1DBEFBC1B4`。本稿接续 Source `3aeecbec1c6f9bfa4d8998f4a39689ef5da0a970` 的实际单厚度族；是作者证明与核验，不是独立 Review。

完整道路、P000/Heartbeat X6 中固定原生轴上的辅助标量读出、单位 D_1=0、真实背景和全部前史保持原义。以下解析工具用于该标量观察，不变更原生空间定义。

## 1. 主要结论

记单厚度源

\[
D_a(n)=a^{-1}\prod_{p\mid n}(1-p^{-a})\quad(n\ge2),\qquad D_a(1)=0,
\]

并令 q_a、q* 分别采用 D_a、Λ 的同背景完整道路。定义确定的首阶源

\[
\boxed{b_n=\frac12\bigl[(\Lambda*\Lambda)(n)-\Lambda(n)\log n\bigr]
=\frac12\sum_{d\mid n}\mu_{\rm Mob}(d)(\log d)^2.}\tag{1}
\]

其完整道路增量记作

\[
T_b(y)=\sum_{n\le y}(y/n-1)b_n.
\]

利用无条件有效素数定理，可以证明

\[
\boxed{T_b(y)/y=-\gamma\log y+C_0+O(e^{-c\sqrt{\log y}}),
\quad C_0=\gamma+2\gamma^2+3\gamma_1,}\tag{2}
\]

其中 γ_1 是 ζ 的 Laurent 展开中的第一 Stieltjes 常数，c>0 为某个常数。

对 a_B=1/B，前驱的 O(log²B/√B) 根误差上界因而可加强为**实际渐近式**。若整数窗口 A=A(B) 满足 A→∞、A/B→0，则

\[
\boxed{\|q_{1/B}-q^*\|_{w,[A,B]}
\sim\gamma\frac{\log B}{\sqrt B}.}\tag{3}
\]

同一渐近式对任意包含真实两端点的插值网格 Π **一致成立**。特别适用于固定 λ>1 的 B=A^λ 窗口，整数取整不影响渐近结论。

终点的绝对道路差有不同尺度：

\[
\boxed{q_{1/B}(B)-q^*(B)=-\gamma\log B+C_0+o(1).}\tag{4}
\]

若加入显式算术首阶校正，定义

\[
q_B^{(1)}(y)=q^*(y)+B^{-1}T_b(y),
\]

则本稿还给出不依赖素数定理的显式完整前缀界：B≥16 时

\[
\boxed{\max_{1\le y\le B}|q_{1/B}(y)-q_B^{(1)}(y)|
\le\frac{4(\log B)^3}{B}\longrightarrow0,}\tag{5}
\]

\[
\boxed{\|q_{1/B}-q_B^{(1)}\|_w,\quad
\|I_\Pi(q_{1/B}-q_B^{(1)})\|_w
\le\frac{4(\log B)^3}{B^2}\sqrt{B-A+1}.}\tag{6}
\]

校正 q_B^(1) 是一个明确的观察/计算入口。返回 q* 时首阶项 T_b/B 仍准确存在，不能作为误差丢弃。

## 2. 首阶源的精确支撑与余项

设 n 的不同素因子为 p_1,...,p_r，ℓ_i=log p_i、L=Σℓ_i。直接展开正乘积得到

\[
b_n=\begin{cases}
-\frac12(\log p)^2,& n=p^j,\\
(\log p)(\log q),&n=p^jq^k,\quad p\ne q,\\
0,&\omega(n)\ge3\text{ 或 }n=1.
\end{cases}\tag{7}
\]

式 (1) 的 Möbius 形式由单厚度展开得到；Dirichlet 形式也可在 Re s>1 由绝对收敛级数验证。式 (7) 保留指数任意的素数幂和两个不同素因子的全部整数。

置

\[
R_a(n)=D_a(n)-\Lambda(n)-ab_n.
\]

对于 r=1，指数函数三阶交错余项给

\[
0<R_a(n)\le a^2(\log p)^3/6.
\]

对于 r=2，用 E(u)=(1−e^(−u))/u=∫_0^1e^(−ut)dt，得到

\[
R_a(n)=a\ell_1\ell_2[E(a\ell_1)E(a\ell_2)-1]<0,
\]

\[
|R_a(n)|\le\frac{a^2}2\ell_1\ell_2(\ell_1+\ell_2).
\]

对于 r≥3，R_a(n)=D_a(n)>0，且 D_a(n)≤a^(r−1)Πℓ_i。因此当 a log n≤1 时

\[
\boxed{|R_a(n)|\le a^2(\log n)^3/6.}\tag{8}
\]

r≥3 的验证使用
`a^(r−1)Πℓ_i≤a²L³(aL)^(r−3)/r^r≤a²L³/27`；r=2 的系数≤1/8；r=1 的系数为1/6。

### 2.1 完整算术平均余项

令 S(y)=Σ_{n≤y}Λ(n)/n。按三种支撑分别扩大非负求和，得到

\[
\sum_{\omega(n)=1,n\le y}\frac{|R_a(n)|}n
\le\frac{a^2}6(\log y)^2S(y),
\]

\[
\sum_{\omega(n)=2,n\le y}\frac{|R_a(n)|}n
\le\frac{a^2}4(\log y)S(y)^2,
\]

\[
\sum_{\omega(n)\ge3,n\le y}\frac{R_a(n)}n
\le\sum_{r\ge3}\frac{a^{r-1}}{r!}S(y)^r
\le\frac{a^2}6S(y)^3e^{aS(y)}.
\]

中间式使用当 ω(n)=2 时 `(Λ*Λ)(n)=2logp logq`；最后使用 ω(n)=r 时 `Λ^{*r}(n)=r!Πlogp`。所以对任意 a>0，

\[
\boxed{\sum_{n\le y}\frac{|R_a(n)|}n
\le a^2\left[
\frac{(\log y)^2S(y)}6+
\frac{(\log y)S(y)^2}4+
\frac{S(y)^3e^{aS(y)}}6\right].}\tag{9}
\]

完整道路余项是 Σ(y/n−1)R_a(n)，故其绝对值不超过式 (9) 右侧乘以 y。此处没有删掉 y 之前的历史源。

取 a=1/B，使用前驱初等 `S(y)≤log y+4log2`。B≥16 时，令 L_B=log B，有 S(y)≤2L_B，且 exp(S(y)/B)≤√2<3/2。于是式 (9) 右侧≤`(10/3)L_B³/B²<4L_B³/B²`。这给出 (5)—(6)，插值转移再次使用共同线性半径。

## 3. 首阶累计源的主项

本节使用无条件有效素数定理

\[
\psi(x)=x+O(xe^{-c\sqrt{\log x}}),
\]

以及前驱已经从完整归一化证明的

\[
S(x)=\log x-\gamma+O(e^{-c_1\sqrt{\log x}}).
\]

后一个误差由前驱恒等式 q*(x)/x=−∫_x^∞(ψ(t)−t)t^(−2)dt 和部分求和得到；吸收有限次 log 因子可缩小正常数 c_1。

定义 B_1(x)=Σ_{n≤x}b_n。Dirichlet 双曲线恒等式精确给出

\[
\sum_{n\le x}(\Lambda*\Lambda)(n)
=2\sum_{m\le\sqrt x}\Lambda(m)\psi(x/m)-\psi(\sqrt x)^2.
\]

对 m≤√x，x/m≥√x，有效素数定理误差一致可用。于是

\[
\sum_{n\le x}(\Lambda*\Lambda)(n)
=2xS(\sqrt x)-x+O(xe^{-c_2\sqrt{\log x}})
=x\log x-(1+2\gamma)x+O(xe^{-c_3\sqrt{\log x}}).
\]

另一方面，部分求和给

\[
\sum_{n\le x}\Lambda(n)\log n
=\psi(x)\log x-\int_1^x\frac{\psi(t)}t\,dt
=x\log x-x+O(xe^{-c_4\sqrt{\log x}}).
\]

相减除以2，得到

\[
\boxed{B_1(x)=-\gamma x+O(xe^{-c_5\sqrt{\log x}}).}\tag{10}
\]

这个主项来自素数幂的负首阶误差与两个不同素因子的正首阶误差相消；逐项绝对值支付会丢掉该相消。

## 4. 道路主项常数

令 R(t)=B_1(t)+γt。由 (10)，积分 C_0=∫_1^∞R(t)t^(−2)dt 绝对收敛。有限部分求和给

\[
\frac{T_b(y)}y=\int_1^y\frac{B_1(t)}{t^2}dt
=-\gamma\log y+C_0-\int_y^\infty\frac{R(t)}{t^2}dt.
\]

余尾为 O(exp(−c√log y))，缩小 c 后吸收 √log y 因子。

为识别 C_0，令 F(s)=−ζ'(s)/ζ(s)。在 Re s>1，

\[
\mathcal B(s):=\sum_n b_n n^{-s}=\tfrac12(F(s)^2+F'(s)).
\]

由 ζ(1+z)=1/z+γ−γ_1 z+O(z²)，

\[
F(1+z)=1/z-\gamma+(\gamma^2+2\gamma_1)z+O(z^2),
\]

\[
\mathcal B(1+z)=-\gamma/z+(2\gamma^2+3\gamma_1)+O(z).
\]

另一方面，绝对收敛与 (10) 给

\[
\mathcal B(1+z)
=(1+z)\int_1^\infty B_1(t)t^{-2-z}dt
=-\gamma/z+(C_0-\gamma)+o(1).
\]

比较常数，即得 (2) 中 `C_0=γ+2γ²+3γ_1`。

## 5. 尖锐加权渐近、插值与实际偏差符号

由 (9) 与 (2)，当 a=1/B 时，对于 2≤y≤B 一致有

\[
\frac{q_{1/B}(y)-q^*(y)}y
=\frac{-\gamma\log y+C_0+O(e^{-c\sqrt{\log y}})}B
+O\!\left(\frac{(\log B)^3}{B^2}\right).\tag{11}
\]

若 A→∞，式 (11) 的第一项在整个 [A,B] 最终为负，第二项不足以改变符号。因此

\[
\boxed{q_{1/B}(y)<q^*(y)\quad(A\le y\le B)}\tag{12}
\]

对所有充分大的 B 成立。源误差本身仍有两种符号；(12) 是完整累计道路在该窗口族上的结论。

若进一步 A/B→0，则

\[
\sum_{n=A}^B(\log n)^2\sim B(\log B)^2,
\]

而常数项及 (11) 的余项在相应根范数中都是低阶，得到 (3)。取 y=B 还得到 (4)。

任意网格 Π 的首阶主形状是 I_Π(y log y)。由于 y log y 凸，且各节点的 log 值≤log B，

\[
\log n\le\frac{I_\Pi(y\log y)(n)}n\le\log B.
\]

平方求和的两端均渐近于 B(log B)²。共同线性半径控制插值后的余项，故 (3) 对全部 Π 一致成立。这一论证包括只有两个端点的网格。

### 5.1 单厚度尺度的精确门槛

同一论证适用于一般 a=a_B>0，只要 `a_B(log B)²→0`。在 A→∞、A/B→0 下，

\[
\boxed{\|q_{a_B}-q^*\|_w
\sim\gamma a_B\sqrt B\log B,}\tag{13}
\]

且任意真实端点插值具有同一一致渐近式。因此，在这个声明的单厚度参数制度内，根误差趋零恰要求 `a_B√B log B→0`。

例如 a_B=B^(−r)、固定 r>0 时，门槛为 r>1/2；r=1/2 的根误差渐近 γlog B。允许精确有理构造时，可取整数 `Q_B=ceil(√B)·ceil(log₂B)²`、a_B=1/Q_B：只需整数平方根及整数位长比较，即有根误差 O(1/log B)→0。公式 (13) 是此单厚度族的尖锐分类，不是全部厚度匹配方案的最小成本定理。

## 6. 有限核验与来源

伴随脚本固定 B=256,1024,4096,16384，对对应精确 a=1/B 的实际正乘积源、首阶 b、余项符号、逐源半径、完整前缀及 (9) 平均支付作 80 位向外区间检查。有限结果只用于核对实现与边界；(2)—(4)、(13) 由上述解析论证承担。

外部标准输入于2026-11-24读取：

- K. S. Kedlaya, *Notes on analytic number theory*, Chapter7, Theorem7.7，有效素数定理：<https://kskedlaya.org/ant/part-2-4.html>。其 prime-power 点半权与完整闭前缀的差至多 logx/2，包含于本稿使用的误差。
- NIST DLMF §25.2.4–25.2.5，ζ 在1的 Laurent 展开和 Stieltjes 常数约定：<https://dlmf.nist.gov/25.2#E4>。

前驱只用初等上界的 O(log²B/√B) 结果仍可独立使用；本稿尖锐主项另使用上述无条件有效素数定理。
