# R590｜signed BRC 辅助整函数的显式增长圆盘逼近定理

日期：2026-11-07；状态：AUTHOR_SIDE_ANALYTIC_PROOF / INDEPENDENT_DRIVER_REVIEW_PENDING。

## 对象和来源

研究问题承接 R589（45a5ec929e418eb80ce7ccf44fd19896275a14bd）提出的增长窗口系数控制，科学输入仍冻结于 R462（18783e01e3646c72b7aab3b16d3f565e83e6446f）。以下 F_k 是 R576–R589 的辅助 Toeplitz–Hessenberg 标量观察谱；原生 signed BRC 联合十二支路的符号、相位、复合观察和 provenance 在其冻结载体中保持原义。

令整数 k≥2，d=2k−1，Catalan 数 C_n=binom(2n,n)/(n+1)。沿 R588 的精确辅助定义：
\[
H_k(s)=\binom{2k+1+s}{2s}\sum_{q=0}^{\min(k,\lfloor(s-1)/2\rfloor)}
\binom{s-1}{2q}4^qC_{k-q},
\quad A_{k,0}=1,\quad A_{k,j}=H_k(j+2)/H_k(2)\ (1\le j\le d).
\]
设
\[
F_k(z)=\sum_{j=0}^{d}(-1)^ja_{k,j}z^j,\quad a_{k,j}=A_{k,j}/k^{2j};
\quad F(z)=\sum_{j=0}^\infty(-1)^ja_jz^j,\quad
a_j=24\cdot8^j/(2j+4)!.
\]
R576 已有固定紧盘收敛；R589 已证 F 的全部零点简单。

## 定理 A：精确因式及全阶包络

对每个 k≥2、0≤j≤2k−1，定义空乘积为一：
\[
P_{k,j}=\prod_{h=1}^j\left(1+\frac{h+3}{2k}\right)\left(1-\frac h{2k}\right),
\quad R_{k,q}=4^qC_{k-q}/C_k.
\]
则
\[
\boxed{\frac{a_{k,j}}{a_j}=
P_{k,j}2^{-j}\sum_{q=0}^{\lfloor(j+1)/2\rfloor}\binom{j+1}{2q}R_{k,q}}\tag{1}
\]
以及
\[
\boxed{0<a_{k,j}\le e^3(k+1)(2k+1)a_j
<21(k+1)(2k+1)a_j.}\tag{2}
\]

证明：由 H_k(2)=binom(2k+3,4) C_k，逐项约去阶乘：
\[
\frac{\binom{2k+j+3}{2j+4}}{\binom{2k+3}{4}k^{2j}}
=\frac{24\cdot4^j}{(2j+4)!}P_{k,j},
\]
代回 H_k(j+2) 得 (1)。每一对乘积因子等于
\[
1+\frac{3}{2k}-\frac{h(h+3)}{4k^2}\in(0,1+3/(2k)].
\]
所以 P_{k,j}≤exp(3j/(2k))≤e^3。由 C_{k-q}≤4^{k-q} 和中央二项式下界
C_k≥4^k/[(k+1)(2k+1)]，可知 R_{k,q}≤(k+1)(2k+1)。非负偶数二项式和等于
\(\sum_{q}\binom{j+1}{2q}=2^j\)，因此 (2) 成立。

## 定理 B：可增长圆盘的一致收敛与速率

对每一个固定实数 0<c<1/8，整数 k→∞ 时有
\[
\boxed{\sup_{|z|\le c(\log k)^2}|F_k(z)-F(z)|
=O_c\!\left(k^{-1+\sqrt{8c}}\log k\right)\longrightarrow0.}\tag{3}
\]
log 是自然对数。特别地，若 R(k)≥0 且 R(k)=o((log k)^2)，则
\(\sup_{|z|\le R(k)}|F_k-F|\to0\)。

证明：取 L=ceil(10 log k)，以后 k 充分大以使 L≤k/4。Catalan 递推给出
\[
4C_{n-1}/C_n=1+3/(2n-1).
\]
若 q≤(L+1)/2，则
\[
1\le R_{k,q}=
\prod_{h=0}^{q-1}(1+3/[2(k-h)-1])
\le\exp\{3(L+1)/[2(k-1)]\}.\tag{4}
\]
记成对因子 p_h=1+x_h，
\(x_h=3/(2k)-h(h+3)/(4k^2)\)。利用乘积差的标准望远镜界得
\[
|P_{k,j}-1|\le e^{S_{k,L}}-1,\qquad
S_{k,L}=\frac{3L}{2k}+\frac{L(L+1)(L+5)}{12k^2},\quad j\le L.\tag{5}
\]
结合 (1)、(4) 中的正权平均，得到
\[
\left|a_{k,j}/a_j-1\right|\le e^{E_{k,L}}-1,\qquad
E_{k,L}=S_{k,L}+\frac{3(L+1)}{2(k-1)}
=O(\log k/k).\tag{6}
\]
写 R=c(log k)^2。因为 (2j+4)!≥(2j)!，
\[
\sum_{j=0}^\infty a_jR^j\le
24\sum_{j=0}^\infty(8R)^j/(2j)!
=24\cosh\sqrt{8R}\le24k^{\sqrt{8c}}.\tag{7}
\]
低阶 j≤L 的差因此不超过
\(24k^{\sqrt{8c}}(e^{E_{k,L}}-1)
=O_c(k^{-1+\sqrt{8c}}\log k)\)。

高阶由 (2) 控制。令 b_j=(8R)^j/(2j)!，
\[
\sum_{j>L}a_jR^j+\sum_{L<j\le d}a_{k,j}R^j
\le24[1+21(k+1)(2k+1)]\sum_{j>L}b_j.\tag{8}
\]
当 j≥L≥10 log k 且 c<1/8，
\(b_{j+1}/b_j=8R/[(2j+2)(2j+1)]\le1/400\)。
由 n!≥(n/e)^n，
\[
b_{L+1}\le(2e^2c/100)^{L+1}
<(e^2/400)^{10\log k}=k^{-10\log(400/e^2)}.
\]
末指数大于 39，故 (8) 为 O(k^{-37})。结合低段得 (3)，且 sqrt(8c)<1 保证趋零。若 R(k)=o(log²k)，充分大时 R(k)≤c log²k，结论随之成立。

## 推论 C：增长圆周的零点计数充分证书

对固定 0<c<1/8 和任意 0<r_k≤c(log k)^2，令
\[
\varepsilon_k=\sup_{|z|\le c(\log k)^2}|F_k(z)-F(z)|,\quad
m_k=\min_{|z|=r_k}|F(z)|.
\]
若充分大 k 有 m_k>ε_k，则由 Rouché 定理，F_k 与 F 在 |z|<r_k 中具有相同个数零点（计重数）。本轮的 (3) 给出可控制的 ε_k；仍需研究移动圆周的 m_k 严格下界，才能对选定 r_k 给出无条件计数结论。

## 验证和下一个科学单元

实际 Python 3 标准库脚本 R590_VERIFY.py 从原始 H_k Catalan 求和独立核对 (1)，在 k=2..46 的全部 j=0..2k−1 上完成 2160 对整数/Fraction 精确相等及 2160 对 (2) 的有理放宽包络核查。对 k=256,512,1024,2048 及 j=0..ceil(10 log k) 完成 270 对纯有理上界 (6) 检查；R590_EVIDENCE.txt 含原始执行输出。无限 k 的主张以本证明为依据，计算只是有限交叉核对。

下一步：为 r_k≈c(log k)^2 寻找 F 的圆周最小模 m_k 可核验下界；与 (3) 联用形成移动零点计数，继而结合 R588 的正型谱能量研究窗口内外的分配与 V_k=O(k^{-1/2}) 候选。原生十二支路保真映射另行保留。

来源：R462 frozen input @18783e01e3646c72b7aab3b16d3f565e83e6446f；R588_PROOF.zh-CN.md @0395d0169a57594054a40a893ca0345ee8fd2f2f；R589_PROOF.zh-CN.md @45a5ec929e418eb80ce7ccf44fd19896275a14bd。独立 Driver 审阅待完成。
