# 同一输出的整数热率如何相消：整谱、最弱方向与真实 Fourier 初场

固定非零输出 $k\in\mathbf Z^3$，从实值无散的正手性初场取原径向交换子 $-u_+\times\Lambda u_+$，在输出 $k$ 投向负手性线。对于窗 $[A,2A)$ 的可用整数热率，记其数目为 $n$。一个相干读数的全部谱分位都有极限：用 $n$ 缩放负对数特征值，四种坐标奇偶型得到同一条显式曲线。最弱方向的热能比按 $\exp[-(5.6015938\ldots)n+o(n)]$ 衰减。按原窗宽 $A$ 缩放时则保留了三平方筛的密度。这个指数描述了用一个输出的热信号反推各率幅相时的真实失稳。

原任务询问同一输出在不同父模和热率间的相干重组、以及是否能对全网耗散分摊。第93轮证明，若 $\sigma=|p|^2+|q|^2,\ p+q=k$，要有非零读数恰须 $|x|^2=2\sigma-|k|^2,\ x\equiv k\bmod2,\ x\cdot k\ne0,\ x\notin\mathbf R k$。还证明任一有限可用幅相表（含零项）均可在同一实值无散初场的该输出上实现，并给出 **最大** 热能比的线性增长。本篇研究 **最小值和整张谱**，直接展示任意有限同窗输入之间会如何严重抵消。能量指以下热延拓的精确时间积分，固定的是单一输出；初场总能量没有额外预置上限。[原题](https://github.com/awdawmip/enterprise-math/blob/29840e4bcf6fc68a07e3be7677913535b57749e7/research_tasks/NS_BRC_JITTER_ACTION_SUMMABILITY_20260917.md) · [原耗散预算](../seventh/jitter.md) · [三平方筛、幅相实现和上谱端](../ninetythird/heat.md)

## 一、每一个有限窗的精确逆问题

将窗内可用率递增记为 $s_0,\ldots,s_{n-1}$。给复振幅 $b_i$，设
$$
 g(b)=\int_0^\infty\Big|\sum_i b_i e^{-s_i t}\Big|^2\,dt,qquad
 d(b)=\sum_i\frac{|b_i|^2}{2s_i},\qquad
 K_{ij}=\frac{2\sqrt{s_i s_j}}{s_i+s_j}.
$$
最小及最大 $g/d$ 是 $K$ 的两端特征值。记 $g_i=\prod_{j\ne i}(s_i+s_j)/|s_i-s_j|$，$D=\operatorname{diag}((-1)^i g_i)$。Cauchy 行列式及其余子式给
$$
             K^{-1}=DKD,\qquad
             \det K=\prod_{i<j}\left(\frac{s_i-s_j}{s_i+s_j}\right)^2.           \tag{1}
$$
具体地，未归一矩阵 $H_{ij}=1/(s_i+s_j)$ 的逆元等于 $(-1)^{i+j}(2s_i g_i)(2s_j g_j)/(s_i+s_j)$。固定 $b_j=1$，使 $g$ 最小的唯一表是 $H^{-1}e_j/(H^{-1})_{jj}$，最小值恰为 $1/(2s_jg_j^2)$。因此读回单率幅值的精确算子范数为 $\sqrt{2s_j}g_j$。在真实 $k=(1,0,0)$ 取三个率 $7,15,27$，固定中间幅值为 1，另外两项取 $-17/55,-306/385$，最小热能为 $32/88935$。复算用具名原 Fourier 接口的两个共轭链构造了这张最优有理表。

令 $T=\sum g_i^2,\ p_i=g_i^2/T$，以 $p_i$ 为概率计算率的方差 $V$。立刻得到一对可用有理数计算的界
$$
              1\le T\lambda_{\min}(K)\le\big(1-V/(4s_0^2)\big)^{-1}             \tag{2}
$$
（上界在括号为正时使用，在倍频窗恒正）。删除符号后 $K^{-1}/T$ 是 $B_{ij}=\sqrt{p_ip_j}K_{ij}$，正半定且迹为 1；用 $\sqrt p$ 的 Rayleigh 商及 $1-K_{ij}\le(s_i-s_j)^2/(8s_0^2)$ 即得。最小特征向量在按率排序的坐标中严格交替变号，这是 $B$ 逐元严格正的直接结果。

## 二、三平方筛上整张谱的分位定理

下文 $A\to\infty$ 且 $k$ 固定。若 $k$ 有 $t=0,1,2,3$ 个奇坐标，第93轮给出的可用率密度依次为 $\delta=5/12,1/2,1/2,1/4$。任意子区间的计数与长度乘 $\delta$ 的差为 $O_k(\log(2A))$，这包括全偶坐标时三平方禁集与可能删去的四幂。故 $n=\delta A+O_k(\log(2A))$，节点 $x_i=s_i/A$ 按等权趋于 $[1,2]$ 上的均匀分布，且相邻间隔至少 $1/A$。

将 $\lambda_1\ge\cdots\ge\lambda_n>0$ 递减排列。设 $x_*=\sqrt{5/2}$、$D(x)=(x^2-1)(4-x^2)$。对于 $0<c<3$，定义
$$
 f_c(x)=\frac2\pi\arcsin\min\left(1,\frac{c}{2\sqrt{D(x)}}\right),\quad
 q(c)=\int_1^2 f_c(x)\,dx,\qquad
 L(c)=2\int_1^2 f_c(x)\log\frac{x+x_*}{|x-x_*|}\,dx.                         \tag{3}
$$
**整谱分位定理。** $q(c)$ 严格递增地从 0 走到 1。任意 $j/n\to q(c)$ 均有
$$
                      -\frac1n\log\lambda_j\longrightarrow L(c).                \tag{4}
$$
故频窗里有正比例个相互独立的方向需付出指数精度才能辨认。另有
$$
 -n^{-2}\log\det K\longrightarrow 9\log(4/3),\qquad
 -n^{-1}\log\lambda_n\longrightarrow 2\Phi(x_*)=5.6015938\ldots,
$$
其中 $\Phi(x)=\int_1^2\log((x+y)/|x-y|)\,dy$。按 $A$ 计的最弱指数须再乘 $\delta$。

**从格点到有上界的平衡问题。** 置 $G(x,y)=\log((x+y)/|x-y|)$，$I(f)=\iint f(x)f(y)G(x,y)\,dxdy$。全部 $m$ 阶主子式之和等于第 $m$ 个特征基本对称式。这个和在前 $m$ 个特征值之积与其 $\binom nm$ 倍之间，又在最大主子式与其 $\binom nm$ 倍之间。式 (1) 亦适用于每个主子式，其负对数是节点对上 $G$ 的有序和。因为 $\log\binom nm=O(n)$，取 $m/n\to q$ 得
$$
 -n^{-2}\sum_{j=1}^m\log\lambda_j\longrightarrow
 E(q)=\min_{0\le f\le1,\ \int f=q} I(f).                                      \tag{5}
$$
确实，任意子集的经验测度（每点权 $1/n$）的弱极限都受 $dx$ 控制。反向，按均匀子格的目标累积质量 $n\int_1^{1+i/n}f$ 逐次取下整差，可从有序节点选择至多一个对应点来逼近 $f\,dx$；若所需 $m$ 与取整末值不同，改动 $o(n)$ 点即可。核的对角奇性两边均一致可积：第 $h$ 个邻点距中心至少 $h/A$，故每行前 $\epsilon n$ 个邻点对归一能量的总误差至多 $O(\epsilon(1+|\log\epsilon|)+\log n/n)$。可先截断核，再去截断。取 $q=1$ 时 $f=1$，直接两次积分给 $I(1)=9\log(4/3)$。

**显式求出最优密度。** 核在有界实密度上严格正定。写成 $2\sum_{j\ge0}e^{-(2j+1)|\log x-\log y|}/(2j+1)$，每项的一维指数核都有严格正 Fourier 变换；用对数坐标推前并利用对角可积即可。故一阶变分条件足以判定唯一极小值。令 $l,u=(5\mp\sqrt{9-c^2})/2$。式 (3) 的 $f_c$ 在 $x^2\notin(l,u)$ 饱和为 1。在内部
$$
 \partial_c f_c(x)=\frac1{\pi\sqrt{(x^2-l)(u-x^2)}};
$$
在已饱和处导数为零。于是 $q'(c)>0$。势 $V_c(x)=\int G(x,y)f_c(y)dy$ 的空间导数，经 $t=y^2$ 换元是 $-\operatorname{PV}\!\int_1^4 f_c(\sqrt t)/(x^2-t)dt$。将 $f_c$ 表成 $\int_0^c\partial_v f_v\,dv$。每个 $v$ 上，弧正弦密度的 Cauchy 变换在 $z$ 平面是 $[(z-l(v))(z-u(v))]^{-1/2}$，取无穷远同 $1/z$ 的支；这可由 $t=(l+u)/2+[(u-l)/2]\cos\theta$ 的积分得到。其实部在区间内为零，左侧为负、右侧为正。可先在上半平面换序，再取实边界值，移动端点的平方根奇性可积。自由带随 $v$ 递减嵌套，故 $V_c$ 在 $l(c)<x^2<u(c)$ 为常数，在左饱和段递增、右饱和段递减。密度已经占满势较低的两段，自由段的势为 $V_c(x_*)$，故任一保持质量的合法变动的一阶能量非负。这给 $E(q(c))=I(f_c)$。对 $c$ 求导时 $\partial_c f_c$ 只在自由带有质量，因此 $E'(q(c))=2V_c(x_*)$。式 (5) 左侧关于 $m$ 的相邻斜率递增，左右割线夹逼给出 (4)。

**端点须另证。** 由计数误差、整数间距及逐层截断对数核，单个节点的离散势满足 $\log g_i=n\Phi(x_i)+O_k(\log^2(2A))$，对 $i$ 一致。可在半径 $1/A$ 截平 $\log|x-y|$ 并扣除自身，截平函数的总变差为 $O(\log A)$；分部求和再乘计数误差即得。$\Phi'(x)=\log[(x+2)(2-x)/((x+1)(x-1))]$，唯一极大点是 $x_*$。式 (2) 遂确定最小谱指数。最大端 $0\le\log\lambda_1\le\log n$。这样两端也与 (3) 的连续极限一致。

## 三、等差率上的最小谱等价式和固定尾部

当 $k$ 有任意奇坐标，略过有限个初始例外，窗内的率正好是一段公差 $h=2$ 或 $4$ 的等差数列。在同一尺度除以 $h$ 后写为 $a+i$，$0\le i<n$，$a=n+\theta$，则 $\theta=O(1)$；以下估计在有界 $\theta$ 上一致。令 $s=x_*-1$，$\varphi(v)=\Phi(1+v)$，$\gamma=-\varphi''(s)>0$，并记
$$
 B_\theta(v)=\frac{1}{4\pi(1+v)}
 \left(\frac{3+v}{2+v}\right)^{2\theta-1/2}\sqrt{\frac{1-v}{v}},\qquad
 d_*=\frac1{8\gamma(1+s)^2}.
$$
**等差窗尾谱定理。** 对最小值有
$$
 \lambda_n\sim
  \frac{\sqrt{\gamma/\pi}}{B_\theta(s)^2}\,n^{3/2}e^{-2n\varphi(s)},\qquad
 T\lambda_n=1+\frac{d_*}{n}+o(n^{-1}).                                           \tag{6}
$$
对每个固定整数 $j\ge0$ 还有
$$
                \frac{\lambda_{n-j}}{\lambda_n}\sim\frac{n^j}{j!\,d_*^j}.          \tag{7}
$$
这些乘法常数使用等差窗结构。全偶输出可能留下稀疏分布的三平方禁率，本篇对它给 (1)–(5) 及最小谱的指数。

式 (1) 中的单率因子在等差窗恰为
$$
 g_i=\frac{\Gamma(2a+i+n)}
 {\Gamma(2a+i)(2a+2i)\Gamma(i+1)\Gamma(n-i)}.
$$
对 $i/n=v$ 在 $(0,1)$ 的紧子集用 Stirling 展开得 $g_i\sim n^{-1}B_\theta(v)\exp[n\varphi(v)]$。唯一鞍点在 $s$，且 $\gamma=1/(2+s)+1/s+1/(1-s)-1/(3+s)$。远离内子区间可用上一节的离散势估计得指数损失；近区凸性和一致 Stirling 界允许将高斯极限乘任意固定次多项式。故 $T\sim n^{-3/2}B_\theta(s)^2\sqrt{\pi/\gamma}\,e^{2n\varphi(s)}$，在 $p_i$ 权下 $(i-ns)/\sqrt n$ 依全阶矩趋于方差 $1/(2\gamma)$ 的中心正态变量。这解释了符号交替的最弱方向为何集中在中间偏高的局部频段：$B$ 的最大特征向量与 $\sqrt p$ 的距离趋零，例如用式 (2) 的 Rayleigh 商趋一及迹为一即可。

为保留次序之间的比例，写 $x=a+i$、$x_0=n(1+s)$、$\xi=(x-x_0)/(x+x_0)$。因 $K_{ij}=\sqrt{1-\xi_i^2}\sqrt{1-\xi_j^2}/(1-\xi_i\xi_j)$，正逆矩阵 $B$ 展为 $\sum_{j\ge0}h_jh_j^*$，其中 $h_j(i)=\sqrt{p_i(1-\xi_i^2)}\xi_i^j$。截到第 $j$ 列后的剩余迹恰为 $\sum_i p_i\xi_i^{2j+2}=O_j(n^{-j-1})$。全阶矩极限给 $\sqrt n\,\xi\Rightarrow N(0,d_*)$。对 $h_j$ 去掉前 $j$ 列的正交投影，其范数平方等于相应两阶矩行列式之商，故渐近 $n^{-j} j!d_*^j$，其中常数是首一 Hermite 多项式在该正态律下的平方范数。前 $j+1$ 列的非零特征值乘积等于这些正交剩余范数平方之积；逐阶用剩余迹的 Weyl 界，得 $B$ 的第 $j+1$ 大特征值渐近 $j!(d_*/n)^j$。反演给出 (7)。$B$ 的第二特征值因而为 $d_*/n+o(1/n)$，其余尾迹 $O(n^{-2})$，结合总迹为 1 给出 (6) 的第二式。

## 四、谱分位的曲率是完全椭圆积分之比

上面的连续平衡问题与固定尾谱有同一个常数。记 $K_{\rm ell}(z)=\int_0^{\pi/2}(1-z^2\sin^2 t)^{-1/2}dt$（模数约定），$k_0=\sqrt{l/u},\ k'_0=\sqrt{1-l/u}$。则
$$
 E''(q(c))=2\pi\frac{K_{\rm ell}(k_0)}{K_{\rm ell}(k'_0)}.                        \tag{8}
$$
具体地， $q'(c)=K_{\rm ell}(k'_0)/(\pi\sqrt u)$，由 $t=x^2$ 后在 $[l,u]$ 上积分得到。扰动势 $\partial_c V_c$ 在自由带恒定，于 $x=0$ 为零。在 $0<x<\sqrt l$，上节的 Cauchy 变换给其空间导数 $[(l-x^2)(u-x^2)]^{-1/2}$，积到 $\sqrt l$ 后有 $\partial_c V_c(x_*)=K_{\rm ell}(k_0)/\sqrt u$。结合 $E'=2V_c(x_*)$ 即得 (8)。

尤其 $\epsilon=1-q\downarrow0$ 时，$3-c\sim\sqrt{10}\,\epsilon$、$(k'_0)^4\sim(24\sqrt{10}/25)\epsilon$。由 $K_{\rm ell}(k_0)=\log(4/k'_0)+o(1)$ 和 $K_{\rm ell}(k'_0)=\pi/2+O((k'_0)^2)$，得到
$$
 E''(1-\epsilon)=\log[1/(d_*\epsilon)]+o(1),\qquad
 E'(1)-E'(1-\epsilon)=\epsilon\log[e/(d_*\epsilon)]+o(\epsilon),
 \quad d_*=\frac{3}{80\sqrt{10}} .
$$
这里 $d_*$ 与式 (7) 的 Hermite 常数严格相同。式 (4) 固定谱分位、式 (7) 固定整数尾位，这两种极限之间的过渡尺度仍可单独研究。

## 计算与适用边界

复算从第93轮已绑定摘要的代码取合法父模和真实 Fourier 源；核对 20 个由父格直接枚举的窗、精确有理逆矩阵和主子式。对六个节点的全部子集，直接将各阶主子式与原矩阵的特征多项式对照。数值诊断独立计算 $n=12,24,48$ 的全矩阵高精度特征值，并对平衡密度核对自由带等势。等差阵的峰值 $\varphi(s)\simeq2.800796910$；大窗倒迹以 Gamma 对数计算。用七列截断的正逆矩阵另核最末四个谱位，$n=1024$ 的剩余迹约为 $4.16\times10^{-30}$；也用三个内部参数的势积分差商独立比对 (8)。真实三率样例的最优性及热能是有理精确值。接源复算用 Python、SymPy 及其 mpmath 依赖，连续势诊断还用 SciPy。

这里用到的有密度上界的对数平衡法已有成熟理论，完全椭圆积分在模数趋一时的对数展开亦为经典公式。本篇由具名热率的 Cauchy 主子式导出具体约束与反射核，并求得式 (3)、(6)–(8) 中的常数。[Dragnev–Saff 的离散约束能量问题](https://doi.org/10.1007/BF02843160) · [DLMF 的完全椭圆积分渐近](https://dlmf.nist.gov/19.12)

这个输出上，同窗各率几乎相消时，热迹仍区分每一个有限输入，但要稳定恢复它们必须付出上面的精度。原方程的不同输出共享父模和耗散，同一时刻的非线性注入还有新的相位；因此单输出逆界不提供全 Navier–Stokes 网络的延拓界。有关带初始数据的热残差充分条件沿用已有项目结果。[复算程序](cancellation_check.py) · [精确值与诊断](cancellation_checked.json) · [热残差与原闭合条件](https://github.com/awdawmip/enterprise-math/blob/246c6de883f0a7ffd8c2fe0f8fc09b663c25e7b6/research_notes/ns-jitter-initial-data-certificate-20260909.md)

~~~sh
python cancellation_check.py --repo /path/to/enterprise-math | cmp - cancellation_checked.json
~~~
