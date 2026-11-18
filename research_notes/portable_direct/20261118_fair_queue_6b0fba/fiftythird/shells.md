# 单中心平方壳的占用率、距平方的深度与中心同余偏差

在 P017 的开区间 \(((c-1)^2,c^2)\) 内，取奇素数 \(p<c\)，记 \(r=c-p\)。第 1 轮已确定 \(r^2\le2p\) 时，最小素因子为 \(p\) 的壳至多含一个数。以下对这些壳求平均，同时保留左因子 \(p\)、中心 \(c\) 和到上方平方的实际距离。本文是原问题的未编号算术分叉。[原平方盆地](https://github.com/awdawmip/enterprise-math/blob/7b32ae2ad9d1c13a13ff4668d1d218adda99390d/docs/LEGENDRE_PRESSURE_TEST.zh-CN.md) · [原余因子窗口](https://github.com/awdawmip/enterprise-math/blob/7b32ae2ad9d1c13a13ff4668d1d218adda99390d/src/enterprise_math/p017_cofactor_window.py) · [第 1 轮单中心判据](../sieve.md)

## 一、用实际素数对计算壳

任何壳内数都为 \(p\) 乘某奇商，写成 \(p(p+2r+2j)=c^2-r^2+2pj\)。开区间给出
\[
 \left\lfloor\frac{(r-1)^2}{2p}\right\rfloor\le j\le
 \left\lfloor\frac{r^2-1}{2p}\right\rfloor .
\]
在 \(1\le r\le\lfloor\sqrt{2p}\rfloor\) 只有 \(j=0\)，且 \(p<p+2r<p^2\)（\(p=3\) 可直接检查）。因此壳非空恰当 \(q=p+2r\) 也是素数，唯一元素为 \(pq\)，其深度 \(c^2-pq=r^2\)。端点 \(q=p\) 必须排除。用 \(p\le X\) 取样，记
\[
 D(X)=\sum_{3\le p\le X}\lfloor\sqrt{2p}\rfloor,\qquad
 A(X)=\sum_{3\le p\le X}\big[\pi(p+2\lfloor\sqrt{2p}\rfloor)-\pi(p)\big],
\]
两处外和均仅取素数。对每个固定 \(B>0\)，有无条件公式
\[
 A(X)=2\sqrt2\int_2^X\frac{\sqrt t}{\log^2t}\,dt
        +O_B(X^{3/2}/\log^B X).
 \tag{1}
\]
写 \(L=\log X\)。分部积分给出
\[
 A(X)=\frac{4\sqrt2}{3}\frac{X^{3/2}}{L^2}
       \left(1+\frac4{3L}+O(L^{-2})\right),\qquad
 \frac{A(X)}{D(X)}=\frac2L\left(1+\frac2{3L}+O(L^{-2})\right).
 \tag{2}
\]
分母用素数定理部分求和，主积分为 \(\sqrt2\int_2^X\sqrt t\,dt/\log t\)，逐素数的地板误差至多 \(\pi(X)\)。

## 二、平方根长度的变窗与对数误差

在 \(Y\le n<2Y\) 写 \(L_Y=\log Y,\ H_0=\sqrt Y\)。以下引理带有足够的余量，既能将起点限制为素数，又能让窗随起点改变。固定整数 \(M\ge1\)、常数 \(C>0\)。任给 \(b,d>0\)，除去 \(O_{b,d,M,C}(Y/L_Y^d)\) 个整数 \(n\)，对所有 \(0\le h\le CH_0\) 和所有既约 \(a\bmod M\) 同时有
\[
 \#\{n<q\le n+h:q\text{ 为素数},\ q\equiv a\bmod M\}
 =\frac{h}{\varphi(M)\log n}+O_{b,d,M,C}(H_0/L_Y^b).
 \tag{3}
\]
这是对全部窗长的一致**绝对**误差，小窗不要求相对误差趋零。

Koukoulopoulos 定理 1.2 无条件控制
\(\int_Y^{2Y}\sum_{m\le Q} E(y,h;m)\,dy\ll_{B,\epsilon}Yh/L_Y^B\)，
其中 \(E\) 是同一窗、对全部既约类取最大值的素数 \(\log q\) 权与 \(h/\varphi(m)\) 的绝对差。取 \(Q=M\) 固定，\(\epsilon=1/20\)，窗长从 \(H_0/L_Y^{b+2}\) 到 \(CH_0+O(1)\)，则所有充分大的 \(Y\) 均满足定理中的 \(\theta=\log h/\log Y\) 和 \(Q^2\) 范围。先取间距 \(\max(1,\lfloor H_0/L_Y^{b+2}\rfloor)\) 的整数网格，含零且最末点盖住上端。对整数窗长，区间 \([n,n+1)\) 上的素数和就是起点 \(n\) 的同一和。非负性允许留下单模的误差。Markov 不等式与 \(O_{b,C}(L_Y^{b+2})\) 个网格点的并集，在原定理取充分大 \(B=B(b,d)\) 时，给出上述坏整数界。两个相邻窗的素数和单调，线性均值之差至多一个网格步长，故网格之间也成立。最后在 \(n<q\le n+CH_0\) 将 \(\log q\) 换成 \(\log n\) 的总误差是 \(O_C(H_0^2/Y+1)\)，再除以 \(\log n\)。[Koukoulopoulos, *Primes in short arithmetic progressions*, 定理 1.2 及 \(E\) 的定义](https://arxiv.org/abs/1405.6592) · [期刊原文](https://doi.org/10.1142/S1793042115400035)

对普通素数，Zaccagnini 的 Selberg 积分定理在 \(\epsilon(Y)=0\)、\(Y^{1/6}\le h\le Y\) 给出 \(\int_Y^{2Y}|\pi(t)-\pi(t-h)-h/\log t|^2dt\ll Yh^2(\log\log Y)^2/L_Y^4\)。这个量级足够转移单一固定相对精度到几乎所有素起点。式 (1) 的第二项使用 (3) 的任意对数精度。还可按经典零点法独立检查 \(M=1\) 的这一余量。取 \(T\asymp Y^{3/5}\) 的良好截断高度，\(\psi(x)\) 对称显式式在 \(x\asymp Y\) 的余项 \(O(Y\log^2 Y/T+\log^2Y)\) 远小于 \(H_0/L_Y^B\)。对每个零点 \(\rho=\beta+i\gamma\)，将增量写为 \(\int_0^h(x+v)^{\rho-1}dv\)。Cauchy–Schwarz 后在 \(t=\log((x+v)/Y)\) 的有界区间上以高斯放大平方积分。第 \(i,j\) 个纵坐标单位箱的 Gram 权为 \(O(\exp[-c(|i-j|-1)_+^2])\)，因为参与高斯变换的实指数 \(\beta+\beta'-2\) 有界。每箱按重数有 \(O(\log T)\) 个零点，因此零点和的积分均方（以 \(dx/Y\) 计）至多
\[
 C h^2\log T\sum_{|\gamma|\le T}Y^{-2(1-\beta)}.
\]
对 \(\beta\le1/2\) 总贡献为 \(O(T\log T/Y)\)。在余下区间对 Ingham 密度界 \(N(\sigma,T)\ll T^{3(1-\sigma)/(2-\sigma)}\log^{O(1)}T\) 部分求和，\(2\log Y-3\log T=(1/5)\log Y+O(1)\)；Vinogradov–Korobov 无零区给 \(1-\beta\gg (\log T)^{-2/3}(\log\log T)^{-1/3}\)。零点和于是小于任意固定负对数幂。去除真素幂每阶只须 \(O_C(1)\) 项（相邻平方至少有平方根量级间隔），总权 \(O_C(\log^2Y)\)。这给出同一细网格所需的普通素数均方界。[Zaccagnini 原定理，第 225 页](https://doi.org/10.4064/aa-84-3-225-244) · [Ingham 的密度定理](https://doi.org/10.1093/qmath/os-11.1.201) · [Vinogradov–Korobov 无零区的显式形式](https://doi.org/10.1093/qmath/haae010)

在 (3) 令 \(M=1,\ n=p,\ h=2\lfloor\sqrt{2p}\rfloor\)，坏素数的数目至多为坏整数数目，每个至多贡献 \(O(\sqrt Y)\)。将 \(b,d\) 取大，就可逐个二进段求和，将 \(A(X)\) 换为 \(\sum_{3\le p\le X}2\sqrt{2p}/\log p\)，误差在 (1) 内。末段截断同样有效。经典素数定理带任意固定对数节省，部分求和即得 (1)。此论证没有把固定有限网格的定性收敛用于提取第二项。

## 三、真实深度与中心类的分布

对每个非空壳给一票，设 \(U=p/X,\ V=(c^2-pq)/(2p)=r^2/(2p)\)。对固定 \(0\le u,v\le1\) 有
\[
 \Pr(U\le u,\ V\le v)\longrightarrow u^{3/2}\sqrt v.
 \tag{4}
\]
因为 (3) 允许将半径上端改为 \(\sqrt{2pv}\)，地板改变的区间长度至多 2，再把 \(X\) 换为 \(uX\)。对 \(Y\le p<2Y\) 中除去相对密度趋零的素数，非空壳内部的 \(r/\sqrt{2p}\) 的经验分布函数也一致趋向 \([0,1]\) 上的均匀分布；(3) 同时适用于全部分界点和整个壳，且全壳主项 \(\asymp\sqrt Y/\log Y\)。

固定整数 \(m\)，在 (4) 中另按中心 \(c\bmod m\) 分行。令 \(G=(\mathbb Z/2m\mathbb Z)^\times\)。给定互素端类 \(a,d\in G\)，(3) 在 \(M=2m\) 给出右素数 \(q\) 落在 \(d\) 的权 \(1/|G|\)；对左素数 \(p\equiv a\) 用固定模数的素数定理，再给出 \(1/|G|\)。有限个 \(p\mid 2m\) 或 \(q\mid 2m\) 消失于极限。因此端类对在 \(G^2\) 均匀，且与 (4) 的两个实坐标独立。将这对端类按 \((p+q)/2\bmod m\) 推至中心，得到
\[
 \Pr(c\equiv b\bmod m)\ \longrightarrow\
 \frac1m\prod_{\substack{\ell\mid m\\\ell\ {\rm odd\ prime}}}
 \begin{cases}
 \ell/(\ell-1),&\ell\mid b,\\
 \ell(\ell-2)/(\ell-1)^2,&\ell\nmid b .
 \end{cases}
 \tag{5}
\]
在奇素幂 \(\ell^e\) 上，\(q=2b-p\) 可逆所允许的 \(p\bmod\ell\) 有 \(\ell-1\) 或 \(\ell-2\) 种，每种有 \(\ell^{e-1}\) 个提升；在 \(2^e\mid m\) 的二进分量用模 \(2^{e+1}\) 的奇数对，指定中心及首端后唯一确定奇数次端，各中心均匀。由中国剩余定理相乘。举例 \(m=3\) 的三类权依次为 \(1/2,1/4,1/4\)。这描述按非空壳计票后的中心分布；一个中心可贡献多张票。逐个指定中心的对称素数对计数属于另一问题。

## 四、按左素数或中心截止

记 \(A_c(X)\) 按 \(c=p+r\le X\) 截止，沿用同一批非空壳；则差额
\[
 D_*(X)=A(X)-A_c(X)=\#\{(p,r):p\le X<p+r,\ p+2r\ \text{素},\ r^2\le2p\}.
\]
两次 Brun–Titchmarsh 上界，先在 \(X-O(\sqrt X)<p\le X\) 计 \(p\)，再对每个 \(p\) 在长 \(O(\sqrt X)\) 的窗计 \(q\)，给出 \(D_*(X)\ll X/\log^2X\)。故 (1)、(2)、(4)、(5) 也适用于以中心截止的样本，(4) 中的第一坐标亦可改作 \(c/X\)。候选分母在两种截止之间至多相差 \(O(X)\)，对 (2) 足够。

平均差额的首项可以定出。令 \(Y\) 为整数并按整数 \(Y\le x<2Y\) 求和，每个 \((p,r)\) 贡献 \([p,p+r)\cap[Y,2Y)\) 所含整数的个数。除两个宽 \(O(\sqrt Y)\) 的端段，贡献恰为 \(r\,\mathbf1_{Y\le p<2Y}\)；即使全部按候选计，端段总误差也只有 \(O(Y^{3/2})\)。在各素起点对 (3) 的半径计数部分求和，得到
\[
 \sum_{x=Y}^{2Y-1}D_*(x)
  = 2\int_Y^{2Y}\frac{t\,dt}{\log^2t}
        +O_B(Y^2/\log^B Y)
  \sim\frac{3Y^2}{\log^2Y}.
 \tag{6}
\]
具体地，一个好起点的加权主项为 \(\int_0^{\sqrt{2p}}(2r/\log p)\,dr=2p/\log p\)；坏整数集合用 (3) 对任意 \(d\) 的界，每点至多 \(O(Y)\)。这给出真实边界层的均值，对任何指定 \(x\) 的差额仍只使用上述上界。

## 五、有限复算

原平方开区间逐个整数用最小素因子筛检查至 \(c=501\)，共 1,742 个候选壳，594 个非空。独立地直接列出素数对，按两种截止和五个深度阈值，与素数表二分索引进行了 40 次整数计数比较。在 \(X=10^6\) 共 71,769,820 个左端候选，10,944,394 个非空，中心截止数为 10,934,295，相差 10,099。对全部 \(1\le m\le72\) 穷举 \(((\mathbb Z/2m)^\times)^2\)，以有理数核验 (5) 的局部常数；\(p\le10^5\) 去除端点素数 3 后，三个实测中心类的计数为 255,431、125,817、125,895。脚本还按截短长度与差分数组双路求 (6) 左端。运行 §五的程序只用于整数恒等式与有限样本，渐近常数由短窗定理给出。[复算程序](shells_check.py) · [整数结果](shells_checked.json)
