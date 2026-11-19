# 普通素数截点的临界方差与素幂细层

固定整数 \(k\ge4\)。在原计数中心进位的二倍窗 \([N,2N)\) 上，先扣除计数中心和第 \(2,\ldots,k-1\) 层的实际读数，再以 \(K_k n^{1/k}\) 校正第 \(k\) 层的确定主项。若普通素数截点 \(2\le y=o(\sqrt N)\)，且
\[
                 \frac{y\log y}{N^{2/k}}\longrightarrow\lambda<\infty ,
\]
则校正后的归一化平方能量趋于 **\(\lambda/8\)**。因此要让这份原权误差趋零，截点的尖锐条件是 \(y\log y=o(N^{2/k})\)。特别在 \(y\sim cN^{2/k}/\log N\) 处，残量趋于 \(c/(4k)\)。以下结论均无条件。第七轮已给出该窗小素数项的大筛上界，本轮由原周期的对角质量得到匹配的下界及临界常数。[第七轮真窗与进位分解](../seventh/carry.md) · [本轮素幂层的常数](ladder.md)

## 相同的算术观察

记 \(c_q(n)=\lfloor 2n/q\rfloor-2\lfloor n/q\rfloor\)，\(\gamma=2\log2-1\)，\(\alpha_n=n^{-1}\sum_{q\le n}c_q(n)\)。全进位为 \(J(n)=\sum_{q\le n}(c_q(n)-\alpha_n)\Lambda(q)\)，截断为 \(H_y(n)=\sum_{y<p\le n}(c_p(n)-\gamma)\log p\)。置
\[
\begin{aligned}
 a_p&=\lfloor p/2\rfloor/p, & B_y&=\sum_{p\le y}(a_p-\gamma)\log p, &
 D(n)&=(\gamma-\alpha_n)\psi(n),\\
 L_y(n)&=\sum_{p\le y}(c_p(n)-a_p)\log p, &&
 A_j(n)=\sum_{p^j\le n}(c_{p^j}(n)-\gamma)\log p.
\end{aligned}
\]
以下使用的细层校正需要读取 \(D,A_2,\ldots,A_{k-1}\) 的实际值。对 \(N\le n<2N\) 且 \(y\le N\)，按普通素数逐个取系数恰得
\[
 S_{k,y}(n):=J(n)-H_y(n)-B_y-D(n)-\sum_{2\le j<k}A_j(n)
           =L_y(n)+\sum_{j\ge k}A_j(n).
\]
对固定 \(k\)，素数定理、按 \(\lfloor n/p^k\rfloor\) 分段及 Chebyshev 界给出，后一和在整窗一致为 \(K_k n^{1/k}+o_k(N^{1/k})\)。其中 \(K_k=(2^{1/k}-2)\zeta(1/k)+1-2^{1/k}-\gamma\)。记 \(Z_{k,y}=S_{k,y}-K_k n^{1/k}\)。

**定理。** 令 \(\tau_N=y\log y/N^{2/k}\)。对 \(y=o(\sqrt N)\)，任一固定实数 \(1\le u<v\le2\)，令 \(I_N=[uN,vN)\cap\mathbf Z\)，有
\[
\begin{aligned}
 N^{1-2/k}\sum_{n\in I_N}\frac{Z_{k,y}(n)^2}{n^2}
   &=\frac{\tau_N}{4}\int_u^v t^{-2}\,dt+o_k(1+\tau_N),\\
 N^{1-2/k}\sum_{n\in I_N}\frac{S_{k,y}(n)^2}{n^2}
   &=K_k^2\int_u^v t^{2/k-2}\,dt
     +\frac{\tau_N}{4}\int_u^v t^{-2}\,dt+o_k(1+\tau_N).
\end{aligned}                                                    \tag{1}
\]
取 \(u=1,v=2\)，若 \(\tau_N\to\infty\)，校正前、后的能量除以 \(\tau_N\) 都趋于 \(1/8\)。每个有正长度的固定子窗都检出相同的非零噪声密度。充要条件也适用于振荡截点序列，从任何远离零的子列再取 \(\tau_N\) 趋于正的有限值或正无穷的子列即可。

## 系数间距及均值消去

在 \(p\) 周期上对 \(c_p-a_p\) 取归一化 Fourier 变换。零频系数为零；Parseval 给出该周期的系数平方和 \(a_p(1-a_p)\)。不同普通素数给出的非零约分频率 \(h/p\) 互异，圆周距离至少 \(y^{-2}\)。因此任意连续整数区间 \(I\) 上有
\[
 \left|\sum_{n\in I}L_y(n)^2-|I|V_y\right|\le 3y^2V_y,\qquad
 V_y=\sum_{p\le y}(\log p)^2 a_p(1-a_p).
\]
此处可用间隔频率的双侧大筛。上界由区间外扩及均匀卷积得到；取共同周期 \(\prod_{p\le y}p\) 的充分大整数倍，完整周期上各频率严格正交。将同一上界用于整周期中给定连续区间的补，得到下界。[第十九轮的双侧区间估计与证明](../nineteenth/road.md)

对奇素数 \(a_p(1-a_p)=(1-p^{-2})/4\)，\(p=2\) 的值为 \(1/4\)。故 \(y\to\infty\) 时分部求和与素数定理给出 \(V_y\sim y\log y/4\)。将区间估计按 \((n/N)^{-2}\) 作离散分部求和，由 \(y^2/N=o(1)\) 得
\[
 \frac1N\sum_{n\in I_N}(n/N)^{-2}L_y(n)^2
   =V_y\left(\int_u^v t^{-2}dt+O((1+y^2)/N)\right).
\]
若 \(y\) 有界，\(V_y\) 和 \(y\log y\) 均为 \(O(1)\)，除以 \(N^{2/k}\) 后都趋零。

另一方面，一个完整 \(p\) 周期的中心进位和为零。故对任意连续区间，\(\left|\sum L_y(n)\right|\le\sum_{p\le y}p\log p\ll y^2\)。对 \((n/N)^{1/k-2}\) 分部求和，主项 \(K_k n^{1/k}\) 与 \(L_y(n)\) 的归一化交叉项为 \(O_k(y^2/N^{1+1/k})=o(1)\)。剩下的素幂误差在整窗为 \(o_k(N^{1/k})\)；Cauchy–Schwarz 将其全部归一化交叉项限制在 \(o_k(1+\sqrt{\tau_N})\)。这就证明 (1)。\(k\ge4\) 使临界尺度 \(N^{2/k}/\log N\) 确实落入这里可作双侧渐近的 \(o(\sqrt N)\) 窗口。

## 整数核验

运行 `python cutoff_check.py --out cutoff_checked.json`。程序以有理数和一个形式符号 \(\gamma\) 按每个实际 \(\log p\) 的系数复核原分解，在完整 \(2\cdot3\cdot5\cdot7\) 周期检验混合项为零。四个整块分别按每个 \(n\) 的原始两个取整和每个 \(p\) 的剩余区间独立生成。\(N=131072,y=61\) 时，
\(N\sum_{N\le n<2N}L_y(n)^2/n^2\) 除以 \(V_y\) 为 \(0.5003601264\)，全块无权平方均值除以 \(V_y\) 为 \(1.0002794034\)。有限样本核对系数与权重；极限及充要性来自 (1)。[复算程序](cutoff_check.py) · [数值回执](cutoff_checked.json)
