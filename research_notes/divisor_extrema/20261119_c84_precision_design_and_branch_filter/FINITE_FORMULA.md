# C84　F₃ 首个重叠区间的一维准确式与上端点五项展开

本篇继续 C83 的原 H(0,1) 三读数 Haar 函数。余体积 a 对应首两读数坐标；首末坐标的余体积为 A=2a。格坐标始终保留原整数安排的联合关系。本篇准确式适用于 1/4<a<1/2；a≥1/2 沿用 C82 的闭式。

## 1. 结论

令

$$A=2a,\qquad \tfrac12<A<1,\qquad q=\sqrt{z^2-4A},\qquad b=2-z,$$

$$D=\min(q,b),\qquad k=\sqrt{8A-z^2},\qquad 2\sqrt A\le z\le2.$$

下文给出由有限个有理式、log、atanh、atan 组成的显式函数 H_A(z)，无需再计算任何内积分。则

$$\boxed{F_3(a)=1-\frac{161}{80\pi^2a}
+\frac1{\zeta(2)A}\int_{2\sqrt A}^{2}H_A(z)\,dz.} \tag{1}$$

唯一分点为 z=1+A：左侧 D=q，右侧 D=2−z。这将 C83 的准确二维积分进一步降为一维准确积分。本文没有把剩余 z 积分称为已经完成的初等闭式。

第二个结果是上端点展开。令 ε=1−2a↓0，并记

$$\mathcal E(a)=F_3(a)-\left(1-\frac{161}{80\pi^2a}\right).$$

则

$$\boxed{\begin{aligned}
\mathcal E(a)={}&\frac3{4\pi^2}\varepsilon^4\log\frac1\varepsilon
+\frac{25}{16\pi^2}\varepsilon^4
+\frac{64}{105\pi^2}\varepsilon^{9/2}\\
&+\frac9{4\pi^2}\varepsilon^5\log\frac1\varepsilon
+\frac{339}{80\pi^2}\varepsilon^5
+O(\varepsilon^{11/2}).
\end{aligned}} \tag{2}$$

因此重叠修正的首项是四次幂乘对数，而非纯四次幂。

## 2. 首末坐标中的三角形与平行四边形

沿用 C83 的 W₂、W₃，作线性变换 E(u,v)=(u,2v−u)。在端点坐标 p,q 中，三线性读数为 p₁、(p₁+p₂)/2、p₂。记

$$J_i(A)=\int\delta(\det(p,q)-A)\,W_i(E^{-1}p,E^{-1}q)\,dp\,dq,\quad i=2,3.$$

两向量的面积变换给 dp dq=4 dv dw，delta 缩放给 δ(det(v,w)−a)=2δ(det(p,q)−A)，所以 C83 的有限基公式恰为

$$\mathcal E(a)=\frac{J_2(A)-J_3(A)}{\zeta(2)A}. \tag{3}$$

对三角形 {0,p,q}，令其端点坐标包围矩形宽为 R,S。W₂ 的首末因子是 (1−R)(1−S)，中间因子为 1−H/2，其中 H 是三顶点的坐标和之极差。由于 H≤R+S≤2，中间因子的正部无需另分区。

对平行四边形 {0,p,q,p+q}，同样令 R=|p₁|+|q₁|、S=|p₂|+|q₂|。W₃ 的中间因子是 1−(|p₁+p₂|+|q₁+q₂|)/2，也自动非负。

只需 R,S∈(0,1)、RS>A。置

$$z=R+S,\qquad d=|R-S|,\qquad P=RS,\qquad h=1-A/P\in(0,1/2).$$

下面准确积分两种形状在给定 R,S、归一行列式 A/P 下的内部参数。

## 3. 三角形内部形状积分

将顶点按第一坐标排序为 0,tR,R，将第二坐标排序值写成 0,sS,S。第二坐标的六种排列为

$$ (0,s,1),\ (0,1,s),\ (s,0,1),\ (s,1,0),\ (1,0,s),\ (1,s,0).$$

在正向行列式约束下，每个无标记形状有三个源顶点选择；剩余两向量的顺序由正向决定。这给总因子 3，而不是 6。坐标变换的 Jacobian 为 RS，行列式 delta 对内部归一面积积分又给 1/(RS)，两者抵消。

首、末排列的归一面积分别为 |t−s|、|1−t−s|；其条件密度均为 2h。首排列的坐标和极差恒为 R+S。末排列的平均极差为

$$\max(R,S)-\frac h2(R+S).$$

后一断言使用 h max(R,S)<min(R,S)。该不等式等价于 A>m(M−m)，m=min(R,S)、M=max(R,S)；而 m(M−m)≤1/4<A。

其余四种排列由两两中心对称组成。归一面积都可化成 1−ts，因此 ts=h，形状测度为 dt/t，h<t<1，每种密度为 −log h。现在限制 R≥S。第一对的坐标和极差积分是

$$H_2=\int_h^1\max(tR+S,R+hS/t)\,\frac{dt}{t}.$$

两式的交换点

$$t_0=\frac{R-S+\sqrt{(R-S)^2+4RSh}}{2R}$$

位于 [h,1]。分段初等积分给

$$H_2=z-q-\frac z2\log h
+\frac d2\log\frac{q+d}{q-d}
-\frac d2\log\frac RS,\qquad q=\sqrt{z^2-4A}. \tag{4}$$

第二对的极差积分是

$$H_5=\int_h^1\left[\max(S,R+(1-h/t)S)-\min(S,tR)\right]\frac{dt}{t}.$$

这里最大值恒为第二项，最小值在 t=S/R 交换。仍由 A>S(R−S) 保证 h<S/R<1。于是

$$H_5=-z\log h-S\log(R/S)-2S+hz. \tag{5}$$

将六种排列的密度减去其极差积分的一半，得到准确形状核

$$\begin{aligned}
K_2={}&h\left(4-\frac{5z+d}2\right)+\frac z2h^2-d+q
+\left(\frac{3z}2-4\right)\log h\\
&-d\operatorname{atanh}(d/q)
+\frac z2\log\frac{z+d}{z-d}.
\end{aligned} \tag{6}$$

因此

$$J_2(A)=3\int_{\substack{0<R,S<1\\RS>A}}(1-R)(1-S)K_2\,dR\,dS. \tag{7}$$

## 4. 平行四边形内部形状积分

W₃ 对每个向量分别变号不变。先将正向 delta 写成绝对行列式 delta 的一半，再把两个第一坐标均变为正，四种第一坐标符号区域给因子 4，净因子为 2。

写第一坐标为 Rt、R(1−t)，第二坐标的绝对值为 Su、S(1−u)。第二坐标有四种符号模式。

同号两模式的绝对归一面积为 |t−u|。正同号模式的中间半宽恒为 z/2；负同号模式在面积条件下的平均中间半宽为 (1−h)z/2。它们合计的唯一相位权重密度为

$$4h-hz(2-h).$$

异号模式的归一面积为 t+u−2tu。置 e=1−2h=2A/P−1>0。在两个有效象限中，变元 t=(1+x)/2、u=(1−y)/2 或其反向，使 xy=e。每象限测度为 dx/(2x)。中间绝对值的符号固定：需要的判断归结为 z²<8A，而 z≤2、A>1/2 保证它严格成立。两种异号模式合计贡献

$$\left(\frac z2-2\right)\log(1-2h)-hz.$$

合并得

$$\boxed{K_3=4h-3zh+zh^2+\left(\frac z2-2\right)\log(1-2h),} \tag{8}$$

$$J_3(A)=2\int_{\substack{0<R,S<1\\RS>A}}(1-R)(1-S)K_3\,dR\,dS. \tag{9}$$

这一计算同时保留有向基计数与四种符号模式。没有在 C83 基展开系数之外再除以一个 2。

## 5. 归约到一个显式内原函数

对 R,S 的交换对称性允许限制 R≥S 并乘二。变元 R=(z+d)/2、S=(z−d)/2 的 Jacobian 为 1/2，二者抵消。因此

$$J_2-J_3=\int_{2\sqrt A}^{2}\int_0^{D}
\frac{b^2-d^2}{4}\,\mathcal C_A(z,d)\,dd\,dz, \tag{10}$$

其中 D=min(q,b)、b=2−z，并且

$$\begin{aligned}
\mathcal C_A(z,d)={}&4h-\frac32(z+d)h-\frac z2h^2-3d+3q\\
&+\left(\frac{9z}2-12\right)\log h
+(4-z)\log(1-2h)\\
&-3d\operatorname{atanh}(d/q)
+3z\operatorname{atanh}(d/z).
\end{aligned} \tag{11}$$

它正好是 3K₂−2K₃。

为显示内积分已经完成，置 K=4A、c=9z/2−12、e=4−z、C₀=4−2z+3q、P₁=−4+5z/2。对 r>D≥0 定义下列初等量（所有公式的下端点已减去）：

$$\begin{aligned}
R_0(r,D)&=\operatorname{atanh}(D/r)/r,\\
R_1(r,D)&=-\tfrac12\log(1-D^2/r^2),\\
R_2(r,D)&=r^2R_0-D,\qquad R_3(r,D)=r^2R_1-D^2/2,\\
S_0(r,D)&=\frac{D}{2r^2(r^2-D^2)}+\frac{\operatorname{atanh}(D/r)}{2r^3},\\
S_2(r,D)&=r^2S_0-R_0.
\end{aligned}$$

它们分别是 xⁿ/(r²−x²) 及 xⁿ/(r²−x²)² 的 0 到 D 积分；此处所有 R、S 量仅在 r=z>D 使用。

对数原函数为

$$\begin{aligned}
L^-_0(r,D)&=D\log(r^2-D^2)+2r\operatorname{atanh}(D/r)-2D,\\
L^-_2(r,D)&=\frac{D^3}{3}\log(r^2-D^2)+\frac{2r^3}{3}\operatorname{atanh}(D/r)
-\frac{2r^2D}{3}-\frac{2D^3}{9},\\
L^+_0(r,D)&=D\log(r^2+D^2)-2D+2r\arctan(D/r),\\
L^+_2(r,D)&=\frac{D^3}{3}\log(r^2+D^2)-\frac{2D^3}{9}
+\frac{2r^2D}{3}-\frac{2r^3}{3}\arctan(D/r).
\end{aligned}$$

atanh 原函数为

$$\begin{aligned}
A_0(r,D)&=D\operatorname{atanh}(D/r)-rR_1(r,D),\\
A_1(r,D)&=\frac{D^2-r^2}{2}\operatorname{atanh}(D/r)+\frac{rD}{2},\\
A_2(r,D)&=\frac{D^3}{3}\operatorname{atanh}(D/r)
-\frac r3\left(r^2R_1(r,D)-\frac{D^2}{2}\right),\\
A_3(r,D)&=\frac{D^4-r^4}{4}\operatorname{atanh}(D/r)+\frac{r^3D}{4}+\frac{rD^3}{12}.
\end{aligned}$$

在 D=r 时，所需的有限端点值准确为

$$L^-_0(r,r)=2r\log(2r)-2r,\quad
L^-_2(r,r)=\frac{2r^3}{3}\log(2r)-\frac{8r^3}{9},$$

$$A_1(r,r)=r^2/2,\qquad A_3(r,r)=r^4/3.$$

令 \(\mathcal L^\pm(r)=b^2L^\pm_0(r,D)-L^\pm_2(r,D)\)。全部 R_j、S_j 若省略参数均取 (z,D)。则式 (1) 的显式核为

$$\begin{aligned}
H_A(z)={}&\frac14\left[C_0\left(b^2D-\frac{D^3}3\right)
-\frac92\left(\frac{b^2D^2}2-\frac{D^4}4\right)\right]\\
&+\frac K4\left[P_1(b^2R_0-R_2)+\frac32(b^2R_1-R_3)\right]
-\frac{zK^2}{8}(b^2S_0-S_2)\\
&+\frac14\left[c\mathcal L^-(q)+e\mathcal L^+(k)-(c+e)\mathcal L^-(z)\right]\\
&-\frac34\left[b^2A_1(q,D)-A_3(q,D)\right]
+\frac{3z}{4}\left[b^2A_0(z,D)-A_2(z,D)\right].
\end{aligned} \tag{12}$$

端点 D=0 时取 H_A(z)=0。故全部显示量均有准确的有限解释。直接求导每个原函数并代入 h=(q²−d²)/(z²−d²)、1−2h=(k²+d²)/(z²−d²)，即验证 (12) 是 (10) 的内积分。`finite/verify_one_dimensional.py` 对这些原函数和组合恒等式作符号准确核验。

## 6. 上端点展开及统一余项

令 ε=1−A。取 R=1−εx、S=1−εy。RS>A 的域为 0<x<1、0<y<(1−x)/(1−εx)。再作固定域变换

$$y=\frac{(1-x)t}{1-\varepsilon x},\quad 0<x,t<1,\quad
r=(1-x)(1-t),\quad U=x+(1-x)t=1-r.$$

准确关系为

$$P=RS=1-\varepsilon U,\qquad h=\frac{\varepsilon r}{1-\varepsilon U},\qquad
q^2=d^2+4\varepsilon r,$$

$$ (1-R)(1-S)dR\,dS
=\varepsilon^4\frac{x(1-x)^2t}{(1-\varepsilon x)^2}\,dx\,dt.$$

记 w=x(1−x)²t。对 0<ε≤1/4，有 d≤Cε、z=2−εU+O(ε²)，所有 O 项对固定域一致。对数只通过 log r 留下可积边界项。由 (11) 得

$$\mathcal C_A(z,d)=
-3(\log\varepsilon+\log r)+6\sqrt{\varepsilon r}
+\varepsilon\left[-\frac92U(\log\varepsilon+\log r)-3\right]
+\mathcal R_\varepsilon(x,t), \tag{13}$$

其中存在绝对常数使

$$|\mathcal R_\varepsilon|
\le C\left[\varepsilon^{3/2}r^{-1/2}
+\varepsilon^2(1+|\log\varepsilon|+|\log r|)\right]. \tag{14}$$

这里没有忽略 r=0 附近的曲率项。具体地，

$$0\le q-2\sqrt{\varepsilon r}
=\frac{d^2}{q+2\sqrt{\varepsilon r}}
\le C\varepsilon^{3/2}r^{-1/2},$$

$$0\le d\operatorname{atanh}(d/q)
=d\operatorname{asinh}\!\left(\frac d{2\sqrt{\varepsilon r}}\right)
\le C\varepsilon^{3/2}r^{-1/2}.$$

又 3z atanh(d/z)−3d=O(ε³)，其余有理式与 log(1−2h) 的展开一致。权重满足

$$\int_0^1\!\int_0^1w\,r^{-1/2}\,dx\,dt<\infty,\qquad
\int_0^1\!\int_0^1w\,|\log r|\,dx\,dt<\infty.$$

因此 (14) 积分后为 O(ε^{3/2})；ε²|log ε| 被它吸收。

最后同时展开外面的 1/A 与变换 Jacobian：

$$\frac1{(1-\varepsilon)(1-\varepsilon x)^2}
=1+\varepsilon(1+2x)+O(\varepsilon^2).$$

令 B=(9/2)U+6x+3，则 (3)、(13) 给

$$\frac{\zeta(2)\mathcal E(a)}{\varepsilon^4}
=\int_0^1\!\int_0^1w\left[
-3\log\varepsilon-3\log r+6\sqrt{\varepsilon r}
+\varepsilon\{-B(\log\varepsilon+\log r)-3\}\right]dx\,dt
+O(\varepsilon^{3/2}).$$

将 y₀=(1−x)t 换回单位三角形，以下都是准确 Beta 积分：

$$\int w=\frac1{24},\quad
\int w\log r=-\frac{25}{288},\quad
\int w\sqrt r=\frac{16}{945},$$

$$\int wB=\frac38,\qquad
-\int wB\log r-3\int w=\frac{113}{160}.$$

于是先得到

$$\frac{\zeta(2)\mathcal E(a)}{\varepsilon^4}
=\frac18\log\frac1\varepsilon+\frac{25}{96}
+\frac{32}{315}\sqrt\varepsilon
+\varepsilon\left(\frac38\log\frac1\varepsilon+\frac{113}{160}\right)
+O(\varepsilon^{3/2}),$$

再代入 ζ(2)=π²/6 即为 (2)。单有这个函数值展开不自动证明各阶导数的边界连续性，本文不从中额外断言光滑阶数。

## 7. 复算与数值状态

- `finite/one_dimensional.py` 实现显式核 (12) 和一维积分；没有嵌套数值积分。
- `finite/verify_one_dimensional.py` 准确核验原函数、组合核及端点系数；另外用 45 位数值对 16 个内部参数点的准确核与直接内积分作交叉比较。
- `FINITE_CERTIFICATE.md` 及 `finite/certify_one_third.py` 进一步给出严格外包 0.397047162<F₃(1/3)<0.397047924；这一条有独立整数区间误差证书。
- `finite/one_dimensional_values.json` 保存 40 位工作精度的探索值；例如 F₃(1/3)≈0.3970475447220514、F₃(0.4)≈0.4910917729422501。这些没有区间认证。
- `finite/endpoint_exploration.py` 与 `endpoint_values.json` 检查端点展开的数值趋势；证明依据是第六节的统一余项及准确系数积分。
- C83 两种 96 阶求积彼此接近并不等于严格误差控制。以 a=1/3 为例，C83 的同一公式在 192、384 阶分别约为 0.39704703034、0.39704741553，向本轮一维值靠近。本轮保留“探索值”标签，不将此前近似末位作为严格常数。

直接前件为 C83 `HAAR_FINITE_INTERVAL.md`，不可变源 enterprise-math@20c3c2a6cb769a816cedf0ec04cf199149bfa86f。本篇新增几何形状积分、全部内原函数和端点展开；没有引入新的外部数学定理。
