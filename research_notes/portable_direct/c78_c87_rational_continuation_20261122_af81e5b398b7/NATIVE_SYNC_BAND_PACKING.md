# 原库存同步带：有限计数、幅度界与必要精度

日期：2026-11-23（Asia/Hong_Kong）。作者侧证明，沿用 EM-DVR-2D6C6F / CONTROL_PLANE；不是独立 Review。
本文件直接保留原三态路径、三条完整尾、全部 \(\binom c2\) 个安排与共同舍入格。辅助归一化不改变原碰撞关系。

## 1. 对象及定理

原安排为 \(2\le W\le V\le c\)，加库存 \(n\ge c\) 时只在第一次 23 之前增加 5。
采用前轮 FINITE_KERNEL_PROOF.md 的原准确读数 \(g(n,V,W)\)，以及本轮有理归一化
\[
\Gamma_c(n,V,W)=\frac{5[g(n,V,W)-1]}{27F_1(c)},\qquad
F_k(m)=\prod_{j=1}^{m}\frac{4j+k}{4(j+k)}.
\]
固定有理 \(0<h\le1/16\)、整数 \(c\ge\max(64,144/h)\)。定义同步带
\[
\mathcal B_{c,h}=\left\{(V,W):
\left\lceil c/4\right\rceil\le V\le\left\lfloor c/2\right\rfloor,\
\left\lfloor V/3\right\rfloor\le W\le\left\lfloor3V/4\right\rfloor,\
|\rho_3(V,W)-1|\le h\right\}.
\]
则
\[
\boxed{|\mathcal B_{c,h}|\ge\kappa h c^2,\qquad\kappa=1/1152.}
\tag{1.1}
\]
取完全明确的有理常数
\[
M_0=32\cdot(41/6)\cdot448^2\cdot2^{16},\qquad M=330M_0.
\]
对任意 \(1\le b\le c\)，这些安排的两次准确归一读数满足
\[
0\le\Gamma_c(c)\le Mh,\qquad
|\Gamma_c(c+b)-\Gamma_c(c)|\le Mh\,b/c.
\tag{1.2}
\]
所以对任意两个独立平移、同宽 \(\delta>0\) 的半开轴格，它们占据的二维格数至多
\[
\boxed{(2+Mh/\delta)(3+2Mh(b/c)/\delta).}
\tag{1.3}
\]
所有常数与格原点无关。

## 2. 原有限同步带的逐行计数

由前轮有限乘积包络，令
\[
u=\frac{W+11/8}{V+19/8},\qquad
E_3=\frac{195}{128}
 \left[(W+7/8)^{-2}-(V+15/8)^{-2}\right],
\]
有
\[
(1-E_3)256u^9\le\rho_3(V,W)^4\le256u^9.
\tag{2.1}
\]
在 \(W_\ell=\lfloor V/3\rfloor\)、\(V\ge16\) 时，\(u\le1/2\)，故
\[
\rho_3(V,W_\ell)^4\le1/2<(15/16)^4.
\]
在 \(W_u=\lfloor3V/4\rfloor\) 时，\(u\ge2/3\)；又 \(W_u\ge12\)，所以
\[
E_3<\frac{195}{128(12+7/8)^2}<1/10,\qquad
\rho_3(V,W_u)^4\ge(9/10)256(2/3)^9>(17/16)^4.
\]
两端因此分别严格位于 \(1-h\) 以下和 \(1+h\) 以上。

准确相邻落点公式是
\[
\rho_3(V,W+1)-\rho_3(V,W)
=\frac{9\,\rho_3(V,W)}{4(W+3/4)}.
\]
由 \(0<\rho_3<4\)、\(W\ge\lfloor V/3\rfloor\)：
\[
0<\Delta_W\rho_3
\le\frac9{V/3-1/4}\le\frac{36}{V}.
\tag{2.2}
\]
若带内有 \(K_V\) 个整数点，带两侧紧邻的外点之间跨 \(K_V+1\) 步，数值跨度严格大于 \(2h\)，所以
\[
K_V>hV/18-1.
\]
条件 \(c\ge144/h,\ V\ge c/4\) 给 \(hV\ge36\)，从而
\[
K_V\ge hV/36\ge hc/144.
\]
整数 \(V\) 的行数至少 \(c/8\)，相乘得到 (1.1)。所选 \(W\) 还满足
\[
W\ge V/3-1\ge c/12-1\ge c/16\ge4.
\tag{2.3}
\]
闭带条件包含 \(\rho_3=1\) 及恰等于 \(1\pm h\) 的点；不依赖避免等号的一般位置假设。

## 3. 归一幅度的有理上界

写内层 \(D=\rho_3(V,W),T=\tau_3(V,W)\)，外层
\(A=\rho_5(n,V),S=\tau_5(n,V)\)。
对 \(c\le n\le2c,\ c/4\le V\le c/2\)，外层有限包络使用
\[
u_5=\frac{V+21/8}{n+29/8}.
\]
有 \(u_5\le9/16\)，而 \(256(9/16)^{15}<1/16\)，故 \(A<1/2\)。
又 \(u_5>1/8\)，对应 \(E_5<1/2\)，故
\[
A^4>2^{-38},\qquad 2^{-16}<A<1/2.
\tag{3.1}
\]
这些是有限乘积界，并非连续极限。

对全部有限参数，\(T,S<448\)。由 (2.3) 与 \(k=1\) 包络，
\[
\left[F_1(W)/F_1(c)\right]^4
\le\left[(c+9/8)/(W+9/8)\right]^3\le16^3,
\]
故实际可取 \(F_1(W)/F_1(c)\le8\)；下文用较宽但统一的 32。
终尾准确修正因子
\[
K_W=\frac{1+(7/3-a_W)t_W}
{(1+(3/32)a_Wt_W)(1+6a_Wt_W)}
\]
满足 \(0<K_W\le41/6\)，其中 \(a_W=F_1(W)/(15/32)\le1\)、
\(t_W=840/[(W+2)(W+3)(W+4)]\le5/2\)。

本轮 RATIONAL_NORMALIZATION_AND_DISCRETE_JETS.md 的准确恒等式为
\[
\Gamma_c=
\frac{F_1(W)}{F_1(c)}K_W
\frac{TS|1-D||1-A|}
{(1+Tz_1)(1+Tz_3)(1+Sv)(A+Su)}.
\tag{3.2}
\]
这里 \(u,v\) 为按外层单调方向排列的两个内层极端值，均正。
分母前三因子至少为 1，最后至少为 \(A>2^{-16}\)；
\(|1-D|\le h,\ |1-A|<1\)。于是
\[
0\le\Gamma_c(n,V,W)\le M_0h
\quad(c\le n\le2c).
\tag{3.3}
\]

## 4. 不把大步条件误用于单步求和

若 \(D=1\)，全部内层尾相同，所有 \(n\) 上 \(g=1,\Gamma_c=0\)。
其余情况，内外层非同步且尾宽正。令 \(q=A/(1-A)<1\)。
前轮 DISCRETE_JET_PROOF.md 的相对一阶差商给出，单步时
\[
|\Gamma_c(n+1)-\Gamma_c(n)|
\le\frac{\Gamma_c(n)}{n}
\left(60+\frac{K_1(1)+K_2(1)}n\right),
\]
\[
K_1(1)+K_2(1)=548985/32<17156.
\]
其中相对 Euler 项的绝对值至多
\(3(75/4)+15/4=60\)。\(n\ge64\) 支付原单步小步条件，且
\[
60+17156/64=5249/16<330.
\]
所以
\[
|\Gamma_c(n+1)-\Gamma_c(n)|\le330M_0h/n.
\]
仅对 \(n=c,\ldots,c+b-1\) 求和，保证 \(n+1\le2c\)，得到
\[
|\Gamma_c(c+b)-\Gamma_c(c)|\le330M_0h\,b/c.
\]
这对全部 \(b\le c\) 有效；没有要求大步 \(b\) 自身满足单步引理的小步条件。

## 5. 任意原点的格数上界

第一坐标位于长度 \(Mh\) 的区间，任意平移的 \(\delta\) 格至多给
\(2+Mh/\delta\) 个格列。
固定某格列，第一坐标变化至多 \(\delta\)；
由 (1.2)，第二坐标位于长度至多 \(\delta+2Mh\,b/c\) 的区间，
故至多给 \(3+2Mh(b/c)/\delta\) 个格行。
相乘即 (1.3)，含所有半开边界。

记 \(z=b/c,\ r=c\delta,\ \lambda=r^2/z\)，则归一化占格上界是
\[
\frac{\#\text{占格}}{c^2}
\le\frac6{c^2}+\frac{7Mh}{cr}+\frac{2M^2h^2}{\lambda}.
\tag{5.1}
\]
若沿一子列 \(\lambda\ge\lambda_0>0\)，又 \(b\ge1\)，则
\((cr)^2=c^2z\lambda\ge c\lambda_0\)，故中间项趋零。
取固定有理
\[
0<h\le\min\left(1/16,\frac{\kappa\lambda_0}{8M^2}\right).
\]
由 (1.1)、(5.1)，充分大时同步带中至少
\(\kappa h c^2/2\) 个安排不能独占输出格。
它们在完整目录中仍不唯一，因此完整目录唯一率满足
\[
\boxed{\mathscr V_{c,b,p}\le1-\kappa h.}
\tag{5.2}
\]
这里允许每个库存选择不同的全局格原点，界仍统一。
具体临界精度参数换算见 NEAR_STOCK_SHARP_REPROOF.md。

## 6. 依赖与核对

有限乘积、相对差商与原核引用已保存的前轮研究包：
research_notes/portable_direct/c78_c87_rational_reproof_20261122_af81e5b398b7/
提交 46eec634a39fd202babd05e66b251d90945be948。

本轮另有 C78_SYNCHRONY_NECESSITY_CHECK.md 的同上下文作者侧常数核对。
verify_sync_band.py 仅核验明确有理常数及有限逐行实例；全称量词由上述证明承担。
