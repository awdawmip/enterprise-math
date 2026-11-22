# C87 位置排序的有限有理重证：正部核、严格 Jensen 余量与已有证书的编译

日期：2026-11-22（Asia/Hong_Kong）。
性质：作者侧数学推导和精确有理复算；由本轮 root 统一保存。
原对象：C84–C87 的辅助 Haar 联合读数、三独立源相位及全部相关整数竞争者。
来源固定快照：awdawmip/enterprise-math@63eec225728612d1df6c178b516b5ecf4687ee06。

## 1. 本轮完成的命题

1. 由 C86 的准确位置恒等式和 C87 的完整正性证书，重新证明全部位置的排序及严格凹性。新的论证不对位置求导，不调用支配收敛或微积分基本定理。
2. 构造一个对所有有理位置可用的有限有理公式。它保持对称、严格凹性和端点/中点排序，且有明确的有理误差包络。
3. 仅消费已有核证书，实际计算三个内部位置之间的严格有理差值区间；不重新生成核积分网格。

该结果继承准确位置恒等式与既有 B 的证书。它消除了“位置排序这一步”的微分证明，并把下游运算完全编译成有理算术；原有限库存到 Haar 读数的桥以及该证书本身的既有分析依据，仍按原来源使用。

## 2. 将位置参数放入一个分段仿射正部核

原恒等式对 0<=theta<=1/2 为

\[
 I_{1/2}-I_\theta
 =C\int_0^1 B(x)[(1-\theta)x-\theta]_+\,dx,
\]
\[
 B(x)=A(x)/x^2,\qquad B(x)\ge\beta:=1/200,
 \qquad C=\frac{16000}{16359\zeta(2)}>0.
\]

利用原模型的端点交换对称，统一定义

\[
 f_\theta(x)=
 \max\{(1-\theta)x-\theta,\ \theta x-(1-\theta),\ 0\},
\quad 0\le x,\theta\le1.
\]

那么

\[
 J(\theta):=I_{1/2}-I_\theta
 = C\int_0^1B(x)f_\theta(x)\,dx.                 \tag{2.1}
\]

对固定 x，f 是三个仿射函数的最大值，因此对任意 a,b,lambda，

\[
 f_{\lambda a+(1-\lambda)b}(x)
 \le \lambda f_a(x)+(1-\lambda)f_b(x).          \tag{2.2}
\]

这是有限 max 运算的代数不等式。乘非负权后相加，直接得到 J 凸、I 凹；无需对积分求导。

## 3. 全有理的有限“面积”算子

对有理端点 l<h 和有理位置 theta，f_theta 是有理分段仿射函数，全部断点也是有理数。定义它的面积为：将断点与 l,h 合并排序，每段用

\[
 (v-u)\{f(u)+f(v)\}/2
\]

求梯形面积，再作有限求和。这个定义只使用有理算术，不以积分或极限作定义。公共分割上的面积算子具有线性和正性；分段仿射非负性由有限个端点的非负性承担。

设 m=min(theta,1-theta)，a=1-m，q=m/a。直接计算三角形面积给出

\[
 \boxed{K_{l,h}(\theta)
 =\frac{1-m}{2}\left[(h-q)_+^2-(l-q)_+^2\right]\in\mathbb Q.} \tag{3.1}
\]

它与上述有限梯形求和严格相等。对式 (2.2) 使用公共断点分割和面积正性，得到 K_{l,h} 的凸性，这是纯有限有理证明。

在整个 [0,1] 上的面积为

\[
 \boxed{j_0(\theta)=K_{0,1}(\theta)
 =\frac{(1-2\theta)^2}{2\max(\theta,1-\theta)}.} \tag{3.2}
\]

## 4. 严格 Jensen 余量也可不用微分证明

令 H(theta)=j_0(theta)-theta^2/2。
对同在左半段的 a,b,z=lambda a+(1-lambda)b，利用

\[
 j_0(t)=-2t+\frac1{2(1-t)}
\]

和有理倒数恒等式，直接得到

\[
 \lambda H(a)+(1-\lambda)H(b)-H(z)
 =
 \frac{\lambda(1-\lambda)(b-a)^2}{2}
 \left[\frac1{(1-a)(1-b)(1-z)}-1\right]\ge0. \tag{4.1}
\]

右半段由对称的同一计算得到。两段在 1/2 处相接，并且对于 a<1/2<b：

\[
 \frac{H(1/2)-H(a)}{1/2-a}+\frac12
 =(1/2-a)\left(\frac12-\frac2{1-a}\right)\le0,
\]
\[
 \frac{H(b)-H(1/2)}{b-1/2}+\frac12
 =(b-1/2)\left(\frac2b-\frac12\right)\ge0.
\]

所以左侧各条接缝割线斜率不超过 -1/2，右侧不小于 -1/2。将跨接缝割线按长度分成两段，斜率是两段斜率的凸组合；结合每段的凸性，得到 H 在整个 [0,1] 上凸。这是有限割线不等式，没有导数或微分极限。

于是对任意 0<=a<b<=1、0<lambda<1、z=lambda a+(1-lambda)b，

\[
 \boxed{\lambda j_0(a)+(1-\lambda)j_0(b)-j_0(z)
 \ge\frac{\lambda(1-\lambda)}2(b-a)^2.}        \tag{4.2}
\]

分解 B=beta+(B-beta)，其中 B-beta>=0。残余部分仍由式 (2.2) 给出凸性，故原辅助曲线满足

\[
 \boxed{
 I_z-\lambda I_a-(1-\lambda)I_b
 \ge \frac C{400}\lambda(1-\lambda)(b-a)^2.} \tag{4.3}
\]

这给出了严格凹性的定量余量。对有理参数，除原共同常数 C 外右端全部有理；下节将 C 包在有理区间内。

同样，对 0<=a<b<=1/2，f_a-f_b 非负，且

\[
 j_0(a)-j_0(b)
 =(b-a)\left(2-\frac1{2(1-a)(1-b)}\right)>0.
\]

故

\[
 \boxed{I_b-I_a\ge\frac C{200}
 (b-a)\left(2-\frac1{2(1-a)(1-b)}\right)>0.}  \tag{4.4}
\]

对称性给出右半轴的反向排序，1/2 为唯一最大点，两个辅助端点是等值最小点。式 (4.3) 同时覆盖跨中点的三点关系，无需拼接二阶导数。

## 5. 将 C 及 B 的现有证书转为有限有理输入

### 5.1 C 的有理包围

令 S_N=sum_{k=1}^N 1/k^2。有限的

\[
 \frac1{k(k+1)}<\frac1{k^2}<\frac1{k(k-1)}
\]

在尾部直接望远镜求和，给出熟知的有理尾界。因此

\[
 S_N+\frac1{N+1}<\zeta(2)<S_N+\frac1N.
\]

令

\[
 C_-=\frac{16000}{16359(S_N+1/N)},\qquad
 C_+=\frac{16000}{16359(S_N+1/(N+1))}.         \tag{5.1}
\]

本次 N=64，得到

\[
0.59454218<C<0.59462908
\]

（有理外扩端点；更紧的完整分数在 JSON）。仅取 N=2 就有 zeta(2)<7/4，故 C>64000/114513>1/2，因而式 (4.3) 还有简单的纯有理下界

\[
 I_z-\lambda I_a-(1-\lambda)I_b
 >\frac1{800}\lambda(1-\lambda)(b-a)^2.       \tag{5.2}
\]

### 5.2 B 的 61 个有理区间界

原证书在 [1/8,1] 给出 60 个连续闭区间 [l_i,h_i]，以及 A 的有理端点 A_i^-,A_i^+。直接取

\[
 L_i=A_i^-/h_i^2,\qquad U_i=A_i^+/l_i^2
\]

就有 L_i<=B(x)<=U_i，且每个 L_i>1/200。

在 [0,1/8]，复用原轴证书 B>1/40 及

\[
 |B(x)-a_2-b_2x^{1/20}|\le Ex,\quad
 b_2<0,\quad E=9318931/47520000,
\]

其中 a_2=211*2^(-1/20)/244-101*4^(-1/20)/122+23/61。
两个整数比较

\[
 2\cdot97^{20}>100^{20},\qquad
 4\cdot93^{20}<100^{20}
\]

给出

\[
 B(x)
 \le\frac{211}{244}\frac{97}{100}
 -\frac{101}{122}\frac{93}{100}
 +\frac{23}{61}+\frac E8
 =\frac{10909757191}{23189760000}<\frac12.
\]

所以轴段可用 [1/40,1/2]。完整区间数为 61，端点全部有理。

## 6. 一个保持严格形状的有限有理公式

取 b_i=(L_i+U_i)/2、C_0=(C_-+C_+)/2，定义中心化代理

\[
 \boxed{
 \widehat I_\theta=-C_0\sum_i b_iK_{l_i,h_i}(\theta),
 \qquad \widehat I_{1/2}=0.}                 \tag{6.1}
\]

这个公式对任意有理 theta 都是有限有理数，且只需要 max、加减乘除。

因为所有 b_i>=beta，完整面积可分成 beta*j_0 与非负系数的剩余面积。第 3–4 节的有限证明直接给出

\[
 \widehat I_z-\lambda\widehat I_a-(1-\lambda)\widehat I_b
 \ge\frac{C_0}{400}\lambda(1-\lambda)(b-a)^2. \tag{6.2}
\]

因此该有限公式在全部有理位置上严格凹、对称，具有原位置曲线的严格排序。这里保留正基线十分关键：仅用若干带权点值形成的分段线性代理，在两个相邻节点之间通常只有非严格凹性。

原中心化曲线与代理的误差有明确有理上界。令 delta_i=(U_i-L_i)/2、delta_C=(C_+-C_-)/2，则

\[
 |(I_\theta-I_{1/2})-\widehat I_\theta|
 \le C_+\sum_i\delta_iK_i(\theta)
     +\delta_C\sum_i b_iK_i(\theta).          \tag{6.3}
\]

因为 K_i(theta)<=K_i(0)=(h_i^2-l_i^2)/2，可得到独立于 theta 的统一有理界。本次粗编译的全位置界为约 0.003922306486278024；确切分数已保存。它是与现成证书配套的可验证误差，而非新的全库存误差。

## 7. 两位置比较可直接用更紧的有理差值包围

对 0<=a<b<=1/2，置 d_i=K_i(a)-K_i(b)>=0。无需分别包围两个 I 再相减，直接有

\[
 \boxed{
 C_-\sum_iL_i d_i
 \le I_b-I_a
 \le C_+\sum_iU_i d_i.}                     \tag{7.1}
\]

本次精确 Fraction 运算给出下列外扩显示区间：

| 比较量 | 有理外扩区间 |
| --- | --- |
| I_(1/2)-I_(1/10) | (0.0024153, 0.0061936) |
| I_(1/2)-I_(1/4) | (0.0010553, 0.0024626) |
| I_(1/4)-I_(1/10) | (0.0013600, 0.0037310) |
| I_(1/2)-I_0 | (0.0035657, 0.0114098) |

每个小数端点均是有限十进有理数；JSON 保存更紧的完整分数端点。新包围有意采用简单的常值段，不主张比原 affine 模型积分所得区间更窄。它的用途是证明下游不需要根、对数、微分或浮点积分，也能严格比较指定有理位置。

## 8. 实际验证与科学范围

脚本 rational_position.py 已实际运行：

- 读取原 60 段证书，准确检查相邻端点与完整覆盖，形成 61 段；
- 10 个含端点、左右半轴及中点的位置，每个 61 段，共 610 次面积公式与独立断点梯形法逐分数相等；
- 10 项数值包围与反射对称检查；
- 4 项同侧和跨中点 Jensen 余量的精确核对。

普遍结论由第 2–6 节的代数证明承担。有限核对验证编译实现，未替代全参数证明。
原 293,423 次根检查与完整径向求积均未重跑，沿用其固定输入证书。

本轮尚未给出原库存比例 V_c 与 Phi_theta(L) 的显式统一误差 E(c,b,p,theta)。因此，把式 (7.1) 的辅助主常数差距转成某个有限 c 上的原读数排序，还需要原库存误差及高精度尾误差小于这段差距。尤其 theta 随 c 接近端点、候选网格随 c 增长、L 与 c 联动时，保留原桥的具体未决范围。

## 9. 来源与复算

- positions/GLOBAL_POSITION_THEOREM.md，blob ace988b74f301e6937570dbab8b4deb727e49924：准确位置恒等式、旧微分证明、原库存量词。
- INTEGRATED_KERNEL_PROOF.md，blob 40b327ba8a5ec56544d1166c605af78ea960cabe：完整 B 正性及轴展开界。
- integrated_kernel_certificate.json，blob 4269238343a4eb5815fb048ffd0dd59b9e4fc280：60 段完整有理包围。
- 统一目录：research_notes/divisor_extrema/20261121_c87_global_position_ordering_and_complete_triangle_integral/。
- 本轮推导及实现：同上下文 c87_rational_position 子任务，root 整合。作者核对，不构成独立项目 Review。

在本项目仓库的标准目录下运行 python rational_position.py，默认读取 research_notes/divisor_extrema/20261121_c87_global_position_ordering_and_complete_triangle_integral/integrated_kernel_certificate.json；也可将固定版本证书路径作为第一个命令行参数。输入应与本节固定 blob 一致。结果写入脚本同目录 rational_position_results.json。

