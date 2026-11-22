# C78：原有限读数的全有理离散 jet 与近库存差商

日期：2026-11-22（Asia/Hong_Kong）
来源冻结：awdawmip/enterprise-math@63eec225728612d1df6c178b516b5ecf4687ee06。
贡献：同上下文子研究 c78_rational_bridge；供 root 整合。作者侧推导和精确有限核对，不是独立 Review。

## 1. 原对象与目标

本证明保留原三状态因子路径、完整三条尾、全部合法安排 2≤w≤v≤c，以及在较大库存 n 上把多出的 5 全放在第一个 23 之前的操作。实际读数始终是原 H(0,1)。

直接公式来源是 C78 的 critical_bins.py。定义

\[
F_k(N)=\prod_{j=1}^{N}\frac{4j+k}{4(j+k)},\qquad k\in\{1,3,5\},
\]
\[
\rho_k(n,s)=4\frac{F_k(n)}{F_k(s-1)},
\]
\[
\tau_k(n,s)=\rho_k(n,s)
\frac{28(4s+k-1)(s+k)^{\overline{3k}}}
     {(s+k-1)(n+k+1)^{\overline{3k}}},
\qquad 2\le s\le n,
\]
\[
B_{n,s,k}(z)=\frac{\rho_k(n,s)+\tau_k(n,s)z}
                  {1+\tau_k(n,s)z}.
\]

这里 x 的上升阶乘为 x(x+1)…，下降阶乘为 x(x−1)…；零阶均为 1。

末尾三值为

\[
z_j(w)=\frac{a_w(t_w A_j+B_j)}{1+a_wt_w A_j},\quad
a_w=F_1(w)/F_1(2),\quad t_w=\frac{840}{(w+2)(w+3)(w+4)},
\]
\[
(A_j,B_j)=(3/32,15/32),(3/2,15/8),(6,3).
\]

内层三值是 B_{v,w,3}(z_j(w))，外层三值是再施 B_{n,v,5}；最终 g 为它们的最大值除最小值。以上均为正有理数；不需要 Gamma、log 或根式计算。

本轮具体证明的是：
1. rho、tau 的任意有限阶空间／库存差分恒等式；
2. 全有限 Newton 余项；
3. 直接用于实际 g 的、对极小内层宽度仍一致的近库存比值估计。

## 2. 任意阶库存差分是精确有理公式

设 a=3k/4，beta=15k/4，Delta_n f(n)=f(n+1)−f(n)。直接约去有限乘积有

\[
\frac{\rho_k(n+1,s)}{\rho_k(n,s)}
=1-\frac{a}{n+k+1},
\]
\[
\frac{\tau_k(n+1,s)}{\tau_k(n,s)}
=1-\frac{\beta}{n+4k+1}.
\]

因此对每个整数 r≥0，

\[
\boxed{\Delta_n^r\rho_k(n,s)
=(-1)^r\frac{a^{\overline r}}{(n+k+1)^{\overline r}}\rho_k(n,s),}
\]
\[
\boxed{\Delta_n^r\tau_k(n,s)
=(-1)^r\frac{\beta^{\overline r}}{(n+4k+1)^{\overline r}}\tau_k(n,s).}
\tag{2.1}
\]

证明只需归纳。若 f(n+1)/f(n)=1−d/(n+e)，则

\[
\Delta\left(\frac{f(n)}{(n+e)^{\overline r}}\right)
=-\frac{d+r}{n+e+r}\frac{f(n)}{(n+e)^{\overline r}}.
\]

从 r=0 迭代即得式 (2.1)，没有无限展开或导数交换。

## 3. 落点方向的精确差分

设

\[
u_k(s)=\frac{4s+k-1}{s+k-1},\qquad
\widehat\tau_k(n,s)=\tau_k(n,s)/u_k(s).
\]

有限乘积直接给

\[
\frac{\rho_k(n,s+1)}{\rho_k(n,s)}
=\frac{s+k}{s+k/4}=1+\frac{a}{s+k/4},
\]
\[
\frac{\widehat\tau_k(n,s+1)}{\widehat\tau_k(n,s)}
=\frac{s+4k}{s+k/4}=1+\frac{\beta}{s+k/4}.
\]

对 s+r≤n+1 的每个整数 r≥0，

\[
\boxed{\Delta_s^r\rho_k(n,s)
=\frac{a^{\underline r}}{(s+k/4)^{\overline r}}\rho_k(n,s),}
\]
\[
\boxed{\Delta_s^r\widehat\tau_k(n,s)
=\frac{\beta^{\underline r}}{(s+k/4)^{\overline r}}\widehat\tau_k(n,s).}
\tag{3.1}
\]

证明同样是有限归纳。rho 和 tau-hat 各自分离为 n 的函数乘 s 的函数，故混合 Delta_n^r Delta_s^t 的系数就是上述两种系数相乘。取 r、t≤2 即有实际有限格点上的二阶 jet；不必先构造 Gamma 插值再对连续变量求导。

tau 本身可由 tau=u_k tau-hat 和有限差分乘积恒等式恢复。u_k=4−3(k−1)/(s+k−1) 为显式有理函数。没有遗漏 u_k 的差分。

## 4. 全有限 Newton 公式与有符号余项

设 f 为 rho 或 tau，分别取 (d,e)=(a,k+1) 或 (beta,4k+1)。对整数 b≥R≥1，有限求和恒等式给

\[
f(n+b)=\sum_{r=0}^{R-1}\binom br\Delta^rf(n)
+\sum_{i=0}^{b-R}\binom{b-1-i}{R-1}\Delta^Rf(n+i).
\tag{4.1}
\]

可由反复求和 Delta f，或对 b 归纳证明。代入 (2.1)，并用 f(n+i) 递减、正分母递增，得到

\[
\boxed{
0\le(-1)^R
\left[f(n+b)-\sum_{r=0}^{R-1}\binom br\Delta^rf(n)\right]
\le
\binom bR\frac{d^{\overline R}}{(n+e)^{\overline R}}f(n).
}
\tag{4.2}
\]

更精细的下界同样成立：

\[
(-1)^R{\rm Rem}\ \ge\
\binom bR
\frac{d^{\overline R}}{(n+e+b-R)^{\overline R}}f(n+b-R).
\]

R=2 的重要特例，连同 b=1 时余项为零，给出

\[
0\le\frac{f(n+b)}{f(n)}-1+\frac{bd}{n+e}
\le\frac{b(b-1)d(d+1)}{2(n+e)(n+e+1)}.
\tag{4.3}
\]

因此近库存差商没有由除以 b 导致的失控：

\[
0\le
\frac nb\left[\frac{f(n+b)}{f(n)}-1\right]+d
\le
\frac{de}{n+e}
+\frac{n(b-1)d(d+1)}{2(n+e)(n+e+1)}.
\tag{4.4}
\]

这是对每个有限 n,b 的有理不等式，右侧为明确的 O((b+1)/n)。

## 5. 接入原 g：内层端点差完全保留并约消

固定模板后，内层三值不随外库存 n 改变。设它们的最小与最大值不同。

把两个端点按外层单调性排列为 u,v：
- rho<1 时 u 为小端点、v 为大端点；
- rho>1 时 u 为大端点、v 为小端点。

记 rho=rho_k(n,s)，tau=tau_k(n,s)。则原外层无向读数 g 满足

\[
h:=g-1
=\frac{(v-u)\tau(1-\rho)}
       {(1+\tau v)(\rho+\tau u)}>0.
\tag{5.1}
\]

实际两块模型在这里取 k=5、s=首落点 v_original；公式中的端点 v 与原落点符号是不同对象。

式 (5.1) 是两个分式直接相减。每个极小的内层端点差 v−u 都被完整保留，不将其丢进误差。

设

\[
q=\frac{\rho}{|1-\rho|},\qquad
\eta=b/n,\qquad
\eta\le\frac1{2\max(\beta,aq)}.
\tag{5.2}
\]

由 (4.3)，|rho(n+b)−rho|≤a rho eta，所以外层不跨过 rho=1；同一端点次序适用于两个库存。

定义完全有理的 Euler 系数

\[
\mathcal E=
-\beta+\frac{a\rho}{1-\rho}
+\frac{\beta\tau v}{1+\tau v}
+\frac{a\rho+\beta\tau u}{\rho+\tau u}.
\tag{5.3}
\]

下面给出全有限界：

\[
\boxed{
\left|
\frac nb\left(\frac{g(n+b)-1}{g(n)-1}-1\right)
-\mathcal E
\right|
\le\frac{K_1(q)+K_2(q)b}{n}.
}
\tag{5.4}
\]

一般 k 的可用常数如下。置

\[
A=\beta+aq,\quad B=a\beta q,\quad
K=a+2\beta,\quad L=a\beta+\beta^2.
\]

则可以取

\[
K_1=a(q+1)(k+1)+3\beta(4k+1),
\]
\[
K_2=\tfrac12[a(a+1)(q+1)+3\beta(\beta+1)]
+4\{B+L+(A+K)[K+L/(2\beta)]\}.
\tag{5.5}
\]

对实际外层 k=5，

\[
\boxed{
K_1(q)=\frac{4815+90q}{4},\qquad
K_2(q)=\frac{475260+34485q}{32}.
}
\tag{5.6}
\]

这些常数意在完整、可验证，不宣称最优。

### 5.1 有限代数余项证明

写 P=(v−u)tau(1−rho)，D=(1+tau v)(rho+tau u)，h=P/D。
令 r=rho(n+b)−rho，t=tau(n+b)−tau，R=a rho eta，T=beta tau eta。
式 (4.3) 给 −R≤r≤0、−T≤t≤0，并给出相对于
r_0=−ba rho/(n+k+1)、t_0=−b beta tau/(n+4k+1)
的非负余项，上界分别为
a(a+1)rho eta²/2、beta(beta+1)tau eta²/2。

分子、分母只有二次项，故准确分解为

\[
P'=P+P_1+P_2,\quad
P_1=(v-u)[(1-\rho)t-\tau r],\quad P_2=-(v-u)rt,
\]
\[
D'=D+D_1+D_2,
\]
\[
D_1=(1+\tau v)r+(u+\rho v+2\tau uv)t,\quad
D_2=vrt+uvt^2.
\]

由正性，

\[
|P_1|/P\le A\eta,\quad |P_2|/P\le B\eta^2,
\]
\[
|D_1|/D\le K\eta,\quad |D_2|/D\le L\eta^2.
\]

且 rho'≥(1−beta eta)rho、tau'≥(1−beta eta)tau，
所以 D'≥(1−beta eta)²D≥D/4。

纯分式恒等式为

\[
h'-h-\frac{P_1D-PD_1}{D^2}
=\frac{P_2D-PD_2}{DD'}
-\frac{(P_1D-PD_1)(D_1+D_2)}{D^2D'}.
\]

除以 h 后，右侧绝对值不超过

\[
4\{B+L+(A+K)[K+L/(2\beta)]\}\eta^2.
\]

把 r,t 的线性部分改成 r_0,t_0 时，由形式有理导数

\[
|\rho h_\rho|/h\le q+1,\qquad
|\tau h_\tau|/h\le3
\]

得到 (5.5) 中剩余的二阶余项。这里只用有理函数的形式系数，未调用微积分。

最后将 n/(n+k+1)、n/(n+4k+1) 换成 1，线性系数的误差至多 K_1/n；形式 Euler 系数就是 (5.3)。乘 n/b 即得 (5.4)。

关键点是所有 P 的界都保留端点差 |v−u|，相对余项中它准确约消。K_1、K_2 不依赖内层端点差大小、tau 大小或内层有多少可见位。只需 rho/(|1−rho|) 的实际有理界。

### 5.2 在 C78 中支付了什么

给定远离外同步的有理上界 q≤Q，公式对所有实际内层非盲安排、所有满足 (5.2) 的整数 b 一致。b=1 包含在内，右侧为 O_Q(1/n)。即使内层极接近同步，它也不产生倒端点差的误差。

内层端点相同的情形有 g=1，直接按精确零处理。rho=1 的那个库存也可直接计算 g=1；比值式因基准 h=0 不适用，应另用原分式或同步区计数。

本引理无需 Gamma 插值，就给出原真实读数的库存方向导数型信息及其显式有限误差。它不完成所有落点方向的 C² 连续模型桥，也不单独证明不同逆分支的全库存稀疏碰撞；这些是后续具体义务。

## 6. 与 root 的四次幂乘积证书结合

root 同轮另证了 F_k(n)/F_k(m) 的四次幂二阶包络：
eta_k=(5k+4)/8，
C_k=|k(16−9k²)|/64，
E=C_k[(m+5k/8)^(-2)−(n+5k/8)^(-2)]/2。
对归一化第四次幂 Q，k=1 有 1≤Q≤1/(1−E)，k=3,5 有 1−E≤Q≤1；
E<1 全域成立，近库存还满足 E≤C_k b/(m+5k/8)^3。

该结果及其原整数多项式证书由 root 保存；本子任务未重复运行。
它承担函数值的有限乘积包络，本稿承担离散 jet 与近库存差商，二者可以直接组合。

## 7. 原谱的真实同步多项式

C77 TWO_STOCK_PRECISION.md 给

\[
x=v/c,\quad y=w/c,\quad A=4x^{15/4},\quad D_0=4(y/x)^{9/4}.
\]

因此外、内同步分别等价于

\[
P_{\rm out}(x,y)=1-256x^{15}=0,
\qquad
P_{\rm in}(x,y)=x^9-256y^9=0,
\]

作用域 x,y>0。这两个 Q 多项式直接作用于原均匀库存格 (v/c,w/c)，可接 root 的有理小值格点计数引理；无需把四次根坐标当作均匀格。

对 t=1，原极限谱可在 r=x^(1/4),s=y^(1/4) 中写成有符号有理函数

\[
G/L_0=
\frac{50176 r^6s^{42}(r^9-4s^9)(1-4r^{15})}
     {(1+448r^{51}s^9)(1+1792r^{66}s^9)}.
\]

无向谱取相应正值。若对 Hessian 或跨分支退化多项式使用原 (x,y) 格点界，须实际消去四次根或使用其有限范数；不能直接把 (r,s) 当原库存坐标。

## 8. 精确有限核验

check_discrete_jets.py 已实际执行，全部使用 fractions.Fraction：
- 库存方向 jet：5,130 项；
- 落点方向 jet：4,506 项；
- Newton 余项：10,260 项；
- 原模型近库存 Euler 比值：60 项；
- 辅助正有理端点 Euler 比值：90 项。
总计 20,046 项，全部通过。

全称结果由上述有限代数证明承担。核验用于发现符号、下标、端点次序与常数的实现错误，不扩大其有限样本覆盖。

## 来源

1. C78 精确有限公式：
https://github.com/awdawmip/enterprise-math/blob/63eec225728612d1df6c178b516b5ecf4687ee06/research_notes/divisor_extrema/20261116_c78_nearby_stock_precision/critical_bins.py
blob b6a44aa43e9db28332be6a7b6deb3a6aac4877ca。
2. C78 局部计数与原 Gamma/C² 桥：
https://github.com/awdawmip/enterprise-math/blob/63eec225728612d1df6c178b516b5ecf4687ee06/research_notes/divisor_extrema/20261116_c78_nearby_stock_precision/LOCAL_ADJACENT.md
blob a2259ca801cccf447083fb4449537d354fba393e。
3. C77 真实极限谱：
https://github.com/awdawmip/enterprise-math/blob/63eec225728612d1df6c178b516b5ecf4687ee06/research_notes/divisor_extrema/20261116_c77_arbitrary_stock_pairs/TWO_STOCK_PRECISION.md
blob dd67713b07026321ffc706f2c510ced697b2ba67。

