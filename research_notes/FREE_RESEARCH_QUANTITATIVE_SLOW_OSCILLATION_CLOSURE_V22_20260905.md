# V22：四阶素数历史能量的定量慢振荡闭合

日期：2026-09-05（Asia/Taipei）
Researcher-ID：`EM-FREE-PI-PRIME-20260905`
状态：`RESEARCH_NOTE_PROOF / REAL_VARIABLE_QUANTITATIVE_CLOSURE / NO_PNT_INPUT / NOT_LEAN_VERIFIED / NOT_WORKING_TRUTH / NOT_FOUNDATION`

固定来源：`awdawmip/enterprise-math@23a7f1f71e27c34c6147c323596b9aae22926ba3`。
接续对象：`FREE_RESEARCH_PI_PRIME_GEOMETRY_FRONTIER_V21_20260905.md`。
方法复用：`COMPOSE_APPLIED`——复用有限 prime-winding 计数、Selberg 二阶恒等式、正权方差和停止端点；把既有定性实变量闭合定量化，不声称新的经典素数定理或更强的经典余项。

## 0. 结论与强度

令
\[
\psi(x)=\sum_{n\le x}\Lambda(n),\quad r(x)=\psi(x)/x-1\ (x\ge1),\quad r(0)=0.
\]
本稿从 Chebyshev 上界、有限卷积及其 Selberg 对称式出发证明
\[
\boxed{|r(x)|\ll[\log(e+\log x)]^{-1/2}.}\tag{0.1}
\]
对于 V21 原定义的四阶停止历史 Dirichlet 能量，
\[
\boxed{\mathfrak D_4(r;N)\ll[\log(e+\log N)]^{-1}\longrightarrow0.}\tag{0.2}
\]
对 product-bounded 正历史平均，整数深度 \(h(N)=O(\log\log N)\) 也满足
\[
\boxed{\operatorname{HistAvg}_{h(N)}\mathfrak D_4(r;\cdot)\ll(\log\log N)^{-1}.}\tag{0.3}
\]
常数固定但没有计算实际可用的数值常数或阈值。

这是初等算术加**实变量完成层**的证明，不把 PNT、Breusch 余项或 zeta 零点信息作为输入。它没有证明更强的表示论主张：真实算术四阶状态恰好服从固定八室 S3 自治收缩递推。抽象混合器的谱隙不被当作真实误差场已经衰减的理由。

## 1. 固定四阶定义

记
\[
u_a=\Lambda(a)/a,\quad A(x)=\sum_{a\le x}u_a,\quad p_N(a)=u_a/A(N),\quad q_a(n)=\lfloor n/a\rfloor.
\]
各动作独立取 \(p_N\)，\(N\ge2\)。令
\[
\Phi_N(a,b)=\begin{cases}q_{ab}(N),&ab\le N,\\q_a(N),&ab>N,\end{cases}
\]
\[
F_c(a,b)=f(\Phi_N(a,b))+f(q_c\Phi_N(a,b)),\qquad f(0)=0.
\]
定义
\[
\mathcal D_N^{(2)}(F_c)=\tfrac16\mathbb E_{a,b,d}\bigl[
|F_c(a,b)-F_c(b,a)|^2+|F_c(a,b)-F_c(d,b)|^2+|F_c(a,b)-F_c(a,d)|^2\bigr],
\]
\[
\mathfrak D_4(f;N)=\mathbb E_c\mathcal D_N^{(2)}(F_c).
\]
空动作集上约定 \(\mathfrak D_4(f;0)=\mathfrak D_4(f;1)=0\)。没有改变 N>=2 时 V21 的权重、取整、停止约定或 1/6 归一化。

## 2. 算术输入：不使用 PNT

### 2.1 Chebyshev 与第一质量

中央二项式系数给出
\[
\psi(2n)-\psi(n)\le\log\binom{2n}{n}\le2n\log2.
\]
沿二进制尺度累加得 \(\psi(x)=O(x)\)，因此 \(|r(x)|\le B\)，取固定 B>=1。

精确阶乘恒等式为
\[
\sum_{a\le x}\Lambda(a)\lfloor x/a\rfloor=\log(\lfloor x\rfloor!).
\]
取整误差介于零与 \(\psi(x)\) 之间，普通阶乘和积分比较遂给出
\[
\boxed{A(x)=\log x+O(1).}\tag{2.1}
\]

### 2.2 Selberg 对称式的有限来源

写算术函数 \(\ell(n)=\log n\)。由 \(\ell=\mathbf1*\Lambda\) 及卷积的对数微分，
\[
\boxed{\mu*\ell^2=\Lambda\ell+\Lambda*\Lambda.}\tag{2.2}
\]
令
\[
M_j(x)=\sum_{d\le x}\mu(d)d^{-1}\log^j(x/d).
\]
\(\sum\mu(d)\lfloor x/d\rfloor=1\) 给出 \(M_0=O(1)\)。普通和积分估计给出
\[
H(y)=\sum_{m\le y}m^{-1}=\log y+\gamma+O(y^{-1}),
\]
\[
J(y)=\sum_{m\le y}(\log m)/m=\tfrac12\log^2 y+c_J+O((1+\log y)/y).
\]
有限重排恒等式为
\[
\sum_{d\le x}\mu(d)d^{-1}H(x/d)=1,
\quad\sum_{d\le x}\mu(d)d^{-1}J(x/d)=A(x).
\]
余项加总均为 O(1)，所以 \(M_1=O(1)\)、\(M_2=2\log x+O(1)\)。再代入
\[
\sum_{m\le y}\log^2m=y(\log^2y-2\log y+2)+O(\log^2(2y))
\]
并用 \(\sum_{d\le x}\log^2(2x/d)=O(x)\)，得到
\[
\boxed{\mathcal S(x)=\sum_{n\le x}\Lambda(n)\log n+
\sum_{ab\le x}\Lambda(a)\Lambda(b)=2x\log x+O(x).}\tag{2.3}
\]
这是经典 Selberg 对称式，不声称外部新颖性。

## 3. 三角平均及非光滑 Abel 余项

令 \(R(x)=\psi(x)-x\)。由 (2.1)、(2.3) 及分部求和，
\[
R(x)\log x+\sum_{a\le x}\Lambda(a)R(x/a)=O(x).\tag{3.1}
\]
再乘 log x，分成 log a 与 log(x/a)，对后者再次应用 (3.1)，有限重排得
\[
R(x)\log^2x=\sum_{k\le x}[(\Lambda*\Lambda)(k)-\Lambda(k)\log k]R(x/k)+O(x\log x).
\]
利用 \(\Lambda\log+\Lambda*\Lambda\ge0\)，
\[
|R(x)|\log^2x\le\sum_{k\le x}(\Lambda\log+\Lambda*\Lambda)(k)|R(x/k)|+O(x\log x).\tag{3.2}
\]
不能对这个依赖 x 的非光滑函数直接使用弱收敛。令 \(g_x(t)=|R(x/t)|\)。它的加权全变差满足
\[
\int_1^x t|dg_x(t)|\le x\int_1^x\frac{d\psi(y)+dy}{y}
=xA(x)+x\log x=O(x\log x).
\]
这里 \(|d|R||\le|dR|\le d\psi+dy\)。故 (2.3) 的累计余项 O(t) 在 Stieltjes 分部求和中贡献 O(x log x)，包括跳跃点的左右极限约定。主项额外的 2dt 部分也只有此量级。因此
\[
|R(x)|\log^2x\le2\int_1^x\log t\,|R(x/t)|dt+O(x\log x).\tag{3.3}
\]
设 \(v(T)=r(e^T)\)、\(u(T)=|v(T)|\)。换元得到某个固定 C0，使
\[
\boxed{u(T)\le\mathcal H_2u(T)+C_0/T,
\quad\mathcal H_2u(T)=\frac2{T^2}\int_0^T(T-t)u(t)dt\quad(T\ge1).}\tag{3.4}
\]

## 4. 有界原函数与慢振荡都是已证明的约束

精确地
\[
A(x)=\psi(x)/x+\int_1^x\psi(y)y^{-2}dy.
\]
因此
\[
\int_0^Tv(t)dt=A(e^T)-T-1-v(T)=O(1),
\]
所以某个固定 K0 满足
\[
\boxed{|\int_a^bv(t)dt|\le K_0\quad(0\le a\le b).}\tag{4.1}
\]

令非减双历史计数 \(B_2(x)=\sum_{ab\le x}\Lambda(a)\Lambda(b)\)。由 (2.3) 与 Chebyshev，
\[
\boxed{B_2(e^t)=e^t t(1-v(t))+O(e^t).}\tag{4.2}
\]
比较 t 与 t+h，并用 B2 的单调性，
\[
v(t+h)\le1-e^{-h}\frac{t}{t+h}(1-v(t))+O(1/t),
\]
对 0<=h<=1 一致。另一方面，psi 单调给出
\[
v(t+h)\ge e^{-h}(1+v(t))-1.
\]
由 |v|<=B，可取固定 L,J，增大到 L>=2B,1，使
\[
\boxed{|v(t+h)-v(t)|\le Lh+J/t\quad(t\ge1,\ 0\le h\le1).}\tag{4.3}
\]
没有在此假定素数定理或未知正则性。

## 5. 定量块亏损引理

取 \(K\ge\max\{K_0,1,4B^2\}\)。设 I=[a,a+Delta] 上 |v|<=m<=2B，且
\[
a\ge1,\quad J/a\le m/8,\quad\Delta=8K/m.
\]
则
\[
\boxed{\int_I|v|\le m\Delta-m^2/(32L).}\tag{5.1}
\]
证明：中间半区间必须有 t0 使 |v(t0)|<=m/2。否则 (4.3) 排除任意充分近两点的相反符号：值差至少 m，但局部上界小于 m。通过有限个短步，整个中间半区间同号，于是其有符号积分绝对值超过
\(m\Delta/4=2K>K_0\)，矛盾。

对 \(0\le h\le m/(8L)\)，(4.3) 给出 |v(t0+h)|<=3m/4。这个短区间在 I 内，因为 m/(8L)<=1 且 m^2<=16LK。因此相对于常数上界 m，积分至少亏损
\((m/4)(m/(8L))=m^2/(32L)\)。证毕。

长度约 1/m 的块有约 m^2 的质量亏损，单位长度平均亏损因而为约 m^3。

## 6. 比较函数完成统一衰减

定义
\[
b(T)=M[\log(e+T)]^{-1/2},\qquad d=(2048LK)^{-1}.
\]
M 为待选常数。

### 6.1 比较函数的平均增量

对 T>=e^16，
\[
\boxed{\mathcal H_2b(T)-b(T)\le4M[\log(e+T)]^{-3/2}=4b(T)^3/M^2.}\tag{6.1}
\]
证明：令 s=t/T。s<T^(-1/2) 的部分至多 2M/sqrt(T)。其余部分有
log(e+Ts)>=log(e+T)/2，故中值定理给出
\[
b(Ts)-b(T)\le\sqrt2 M[\log(e+T)]^{-3/2}(-\log s).
\]
而积分 \(\int_0^12(1-s)(-\log s)ds=3/2\)。在所列 T 范围内
\(2\log(e+T)^{3/2}/\sqrt T\le1\)，因此常数 4 足够。

在 [T/4,T/2] 上，令 m=b(T/4)，同样的中值定理给出
\[
\boxed{0\le m-b(t)\le2b(T)^3/M^2.}\tag{6.2}
\]

### 6.2 第一次接触论证，包括算术跳跃

选择 T0>=e^16，满足
\[
BT_0\ge64K,\quad BT_0\ge32J,\quad B^3T_0\ge4C_0/d.
\]
再取
\[
\boxed{M\ge2B\sqrt{\log(e+T_0)},\qquad M^2\ge24/d.}\tag{6.3}
\]
u<b 在 [0,T0] 成立。假设存在第一次接触 u(T)>=b(T)。v 右连续且有左极限，故此论证包括向上的跳跃，不假设 v 连续。接触前有 u(t)<=b(t)。在接触点 b(T)<=B，故
\(m=b(T/4)\le\sqrt2 b(T)\le2B\)。

在 [T/4,T/2] 放入长度 Delta=8K/m 的完整块。函数 Tb(T) 与 Tb(T)^3 在所用范围非减。T0 与 M 的选择保证
\[
\Delta\le T/8,\quad4J/T\le m/8,\quad C_0/T\le(d/4)b(T)^3.
\]
完整块数至少 T/(8Delta)。三角平均核在该带至少 1/T，故 (5.1) 的总亏损至少
\[
\frac1T\frac{T}{8\Delta}\frac{m^2}{32L}=\frac{m^3}{2048LK}\ge d b(T)^3.
\]
把块内上界 m 改回 b(t) 的成本，由 (6.2) 至多 2b(T)^3/M^2。其余部分用接触前上界。因此
\[
\mathcal H_2u(T)\le\mathcal H_2b(T)+2b(T)^3/M^2-d b(T)^3.
\]
结合 (3.4)、(6.1)、(6.3)，
\[
u(T)\le b(T)+(6/M^2-d)b(T)^3+C_0/T
\le b(T)-(d/2)b(T)^3<b(T),
\]
矛盾。所以
\[
\boxed{|v(T)|\le M[\log(e+T)]^{-1/2}.}\tag{6.4}
\]
这证明 (0.1)，过程中没有使用 v(T)->0。

## 7. 原四阶能量的定量传递

令 X=Phi_N(a,b)，Y=q_c(X)。X>=1；Y 可以为零，但 r(0)=0，不是坏的正端点。由第一质量及 Abel 求和，
\[
C_2(x):=\sum_{ab\le x}u_au_b=\tfrac12\log^2x+O(1+\log x).
\]
对整数 2<=Z<=N，一致地
\[
\boxed{\Pr(1\le X<Z)\ll(1+\log Z)/\log N.}\tag{7.1}
\]
有效部分为 [C2(N)-C2(N/Z)]/A(N)^2；停止部分不超过 [A(N)-A(N/Z)]/A(N)。二者均满足该界。

对固定 X，精确地
\[
\boxed{\Pr(1\le q_cX<Z\mid X)=
\frac{A(X)-A(\lfloor X/Z\rfloor)}{A(N)}
\ll\frac{1+\log Z}{\log N}.}\tag{7.2}
\]
X<Z 时分子为 A(X)<=log Z+O(1)，所以仍然一致。

令 epsilon_Z=sup_{m>=Z}|r(m)|。没有坏正端点时 |Fc|<=2epsilon_Z；总是 |Fc|<=2B。因此
\[
\mathbb E|F_c|^2\le4\epsilon_Z^2+O(B^2(1+\log Z)/\log N).
\]
三个换位差各以两端二次矩的两倍控制，产品测度使其边缘相同，故
\[
\boxed{\mathfrak D_4(r;N)\le8\epsilon_Z^2+O(B^2(1+\log Z)/\log N).}\tag{7.3}
\]
取 Z=ceil(exp(sqrt(log N)))。由 (6.4)，epsilon_Z^2=O(1/log log N)，坏端点质量为 O((log N)^(-1/2))。从而
\[
\boxed{\mathfrak D_4(r;N)=O(1/\log\log N).}\tag{7.4}
\]
不要求 D4 随 N 单调；小规模数值不被用于推出此极限。

## 8. 增长深度历史平均

写 T=log N。累计质量 t+O(C) 的正测度，在累计序下夹于从 C 开始的 Lebesgue 测度和 Lebesgue+C delta_0 之间。累计序在正卷积下保持，因此
\[
\frac{(T-hC)_+^h}{h!}\le\mathcal C_h(N)
\le\sum_{j=0}^h\binom hj C^{h-j}T^j/j!
\le T^h e^{Ch^2/T}/h!.\tag{8.1}
\]
末式使用 binom(h,l)h!/(h-l)!<=h^(2l)/l!。
对 h=O(log T)，比较 T 与 T-sqrt(T)，有
\[
\Pr_{\mathrm{Hist}_h}(m<e^{\sqrt T})\ll h/\sqrt T+h^2/T.\tag{8.2}
\]
补集上 (7.4) 为 O(1/log T)，全局 D4<=8B^2。因此
\[
\operatorname{HistAvg}_h\mathfrak D_4(r;\cdot)
\ll1/\log T+h/\sqrt T+h^2/T\ll1/\log T.
\]
h=0 直接由 (7.4)；有界深度同理。这不依赖旧反向 frame 中未展开的隐含常数。

## 9. 素数计数与 winding 体积

高次素数幂贡献为 psi(x)-theta(x)=O(sqrt(x)log x)。分部求和得到
\[
\boxed{\pi_{\mathbb P}(x)=\operatorname{Li}(x)+
O\bigl(x/(\log x\sqrt{\log\log x})\bigr),}\tag{9.1}
\]
其中 Li(x)=integral_2^x dt/log t。

原有限算术载体满足
\[
\psi(N)=\log\det\mathcal W_N=\log\operatorname{lcm}(1,\ldots,N).
\]
所以
\[
\log\det\mathcal W_N=N+O(N/\sqrt{\log\log N}).
\]
prime-valuation 方向仍是算术纤维方向，不是新增空间轴；P000 未修改。

## 10. 完成边界与复核

本稿完成 (0.1)、(0.2)、(0.3)、(9.1) 的初等实变量证明。其经典余项很弱，远弱于已有定量 PNT；这里的结果是对 V21 所选能量门槛的非循环闭合，不是刷新数论估计纪录。

实变量积分作用于有限算术跳跃轨道，例如
\[
\int_{\log m}^{\log(m+1)}v(t)dt=
\psi(m)/(m(m+1))-\log(1+1/m).
\]
绝对积分也可在每个胞段按至多一个零点分割后精确计算。这提供有限跳跃几何解释，但不等同于仅凭六维原始旋转公理的证明。

没有声称：八室 S3 自治耗散等式、Riemann 假设尺度、方法外部新颖性、Lean 全证明、CI-green、Working Truth 或 Foundation 晋升。

配套 `scripts/check_v22_slow_oscillation.py` 已在当前计算环境执行：492 项精确 Fraction 断言通过，覆盖 pair Dirichlet 公式、Poincare 上界、四阶二次矩支配、坏端点质量及块亏损常数。可选 NumPy/SciPy 压力测试也通过；数值不是解析证明。完整解析证明是本文第 2—8 节，尚未由证明助手或独立同行核验。

## 参考

- A. Selberg, An elementary proof of the prime-number theorem, Annals of Mathematics 50 (1949), 305–313。
- T. Tao, A Banach algebra proof of the prime number theorem (2014)：公开的 Selberg 对称式说明；不使用其 Banach 代数结论作为输入。
- D. R. Johnston and A. Yang, Some explicit estimates for the error term in the prime number theorem, arXiv:2204.01980：仅比较已有经典余项强度，不作为证明输入。
- 固定项目源：V21 总前沿与 FREE_RESEARCH_CENTERED_FOURTH_ORDER_TRANSPOSITION_GATE_V20_20260905.md；保留原能量定义，不依赖其未证明的自治递推。
