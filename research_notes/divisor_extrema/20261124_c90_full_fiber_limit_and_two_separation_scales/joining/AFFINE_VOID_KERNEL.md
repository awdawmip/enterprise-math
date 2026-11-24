# C90：仿射方格避空核的准确大参数式与小参数二阶展开

日期：2026-11-24。本篇从本项目已使用的格平均接口推导新的核公式，
用于完整有限分离曲线中的 \(E_2\)。本篇未将这些公式冒称为此前批次已证结果。

## 1. 定义与所用接口

令 \(\Lambda\) 是余体积为 \(s>0\) 的 Haar 随机线性格，条件于
\(\Lambda\)，令 \(z\) 在基本环面 \(\mathbb R^2/\Lambda\) 上均匀。
写 \(\mathcal A=\Lambda+z\)、\(Q=[0,1)^2\)，定义
\[
E_2(s)=\mathbb P\{\mathcal A\cap Q=\varnothing\}.
\tag{1.1}
\]
窗口边界包含格点的事件为零测，所以可在以下几何论证中使用开或闭方格。

沿用的两个平均接口是：

1. 固定底格，对基本环面上的平移展开积分：
   \[
   \mathbb E_z\sum_{p\in\Lambda+z}f(p)
   =\frac1s\int_{\mathbb R^2}f(x)\,dx.
   \tag{1.2}
   \]
2. primitive Siegel 平均：
   \[
   \mathbb E_\Lambda\sum_{v\in\Lambda_{\rm prim}}g(v)
   =\frac1{\zeta(2)s}\int_{\mathbb R^2}g(v)\,dv,
   \qquad \zeta(2)=\frac{\pi^2}{6}.
   \tag{1.3}
   \]

\(\Lambda_{\rm prim}\) 同时包含 \(v\) 和 \(-v\)。本篇每次将无向短方向
转为 (1.3) 时，都显式乘以 \(1/2\)。公式 (1.2) 可直接由 Tonelli 及基本域
平铺证明；(1.3) 复用此前线性 Haar 格分析的 primitive 接口。

接口 (1.3) 的冻结出处为
[C82 LATTICE_LIMIT](https://github.com/awdawmip/enterprise-math/blob/4628b5b87d2cf41a385228ad04bf163c06aa6586/research_notes/divisor_extrema/20261119_c82_three_stock_critical_limit/LATTICE_LIMIT.md)；
短向量与薄壳的研究方法继承
[C83 HAAR_SMALL §5](https://github.com/awdawmip/enterprise-math/blob/20c3c2a6cb769a816cedf0ec04cf199149bfa86f/research_notes/divisor_extrema/20261119_c83_small_precision_and_cubic_root_transition/HAAR_SMALL.md)。
本轮新增的是仿射空窗概率的准确式 (2.1)、主区平移公式 (4.4)、
相应的二阶系数及明确余项；C83 当时计算的是源点独占函数 \(F_2\)。

## 2. 大余体积的准确式

**定理 1。** 对每个 \(s\ge1\)，
\[
\boxed{E_2(s)=1-\frac1s+\frac{3}{\pi^2s^2}.}
\tag{2.1}
\]

**证明。** 令 \(N=\#(\mathcal A\cap Q)\)。若方格内存在三个非共线格点
\(p_0,p_1,p_2\)，则
\[
|\det(p_1-p_0,p_2-p_0)|\ge s,
\]
因为两个差向量在 \(\Lambda\) 中，非零行列式是余体积的正整数倍。
而单位方格内三点的这一行列式至多为 \(1\)：行列式对每个点分别仿射，
其绝对值最大可取在方格顶点，直接检查得上界 \(1\)。
所以 \(s>1\) 时不可能存在这样的三点。\(s=1\) 的等号要求达到方格最大
三角形面积，至少有格点在窗口边界上；这对均匀仿射平移为零测。

因此几乎处处，若 \(N\ge2\)，窗口中的所有格点共线。该直线上的格点为
某个 primitive 方向的等距序列；凸窗口包含其相邻点之间所有中间格点，
所以恰有 \(N-1\) 个无向相邻点对。于是有准确的样本恒等式
\[
N-\mathbf1_{\{N\ge1\}}
=\frac12\sum_{v\in\Lambda_{\rm prim}}
\sum_{p\in\Lambda+z}
\mathbf1_Q(p)\mathbf1_Q(p+v).
\tag{2.2}
\]
两端在 \(N=0,1\) 时也同时为零。

对右边先按 \(z\) 平均，再按 \(\Lambda\) 平均，由 (1.2)–(1.3) 得
\[
\mathbb E\!\left[N-\mathbf1_{\{N\ge1\}}\right]
=\frac1{2\zeta(2)s^2}
\int_{\mathbb R^2}\operatorname{area}(Q\cap(Q-v))\,dv.
\]
卷积积分等于 \(\operatorname{area}(Q)^2=1\)，而
\(\mathbb EN=1/s\)。因此
\[
\mathbb P(N=0)
=1-\frac1s+\frac1{2\zeta(2)s^2},
\]
即 (2.1)。所有计数项非负，交换求和与积分不需要额外可积性假设；
最终有限积分同时证明期望有限。证毕。

## 3. 小余体积的空窗必有唯一短方向

下面取 \(0<s\le1/64\)。对固定底格，记其平移避空概率为
\[
q(\Lambda)=\mathbb P_z\{(\Lambda+z)\cap Q=\varnothing\}.
\]

若 \(v\) 为最短非零格向量、\(r=|v|\)，则 \(v\) primitive。把它补为
格基 \(v,w\)，并将 \(w\) 减去整数倍 \(v\)，使 \(w\) 沿 \(v\) 的分量
绝对值不超过 \(r/2\)。其垂直分量的大小为
\[
h=\frac sr.
\]
最短性给 \(r^2\le r^2/4+h^2\)，故 \(r/h\le2/\sqrt3\)。
任一点先取最近的格点行，再取该行最近的格点，可得覆盖半径
\[
R_{\rm cov}\le\frac12\sqrt{r^2+h^2}<2h.
\tag{3.1}
\]
如果某个仿射平移使单位方格为空，方格中心距所有点至少 \(1/2\)，
因此 \(R_{\rm cov}\ge1/2\)。由 (3.1) 得
\[
\boxed{q(\Lambda)>0\ \Longrightarrow\ r\le4s.}
\tag{3.2}
\]

若两个 primitive 格向量均长不超过 \(4s\) 且不共线，则其行列式
不超过 \(16s^2<s\)，与格行列式的整数倍性质矛盾。
所以长度不超过 \(4s\) 的 primitive 向量要么不存在，要么恰为唯一一对
\(\pm v\)。这个唯一性使下文可用一次 primitive 平均准确代表无向短方向，
不会重复计算不同短方向。

## 4. 至多一条格点行穿过方格时的准确平移概率

写短方向
\[
v=r(\cos\vartheta,\sin\vartheta),\qquad
S(\vartheta)=|\cos\vartheta|+|\sin\vartheta|,
\quad C(\vartheta)=|\cos\vartheta\sin\vartheta|.
\tag{4.1}
\]
方格在法向上的投影宽度恰为 \(S\)。平行格点行的法向间隔为 \(h=s/r\)，
每行的点距为 \(r\)。基本环面均匀平移使法向行偏移均匀于长度 \(h\)
的周期中；条件于该偏移，沿行的点相位均匀于长度 \(r\) 的周期中。
这一事实与所选补向量的剪切分量无关。

假设
\[
0<r<\frac sS.
\tag{4.2}
\]
则 \(h>S\)，至多一条格点行穿过方格。设法向位置为 \(y\) 时的方格弦长
为 \(a(y)\)，则
\[
q(\Lambda)=1-\frac Sh+
\frac1h\int_{\operatorname{proj}_\perp Q}
\left(1-\frac{a(y)}r\right)_+dy.
\tag{4.3}
\]
第一项计没有格点行穿窗的偏移；积分项计虽有行穿窗、但短弦落在相邻格点
之间的平移。

旋转、反射后可设方向单位向量为 \((a,b)\)，\(a,b\ge0\)，\(a^2+b^2=1\)。
若 \(ab>0\)，从法向投影的每一端量距离 \(z\)，靠角点的弦长为
\(z/(ab)=z/C\)，直到第一个边界转折。由于这里 \(r\le s<1\)，
弦长小于 \(r\) 的区域恰为每端 \(0<z<rC\)，都处于该线性段。
每个角点贡献
\[
\int_0^{rC}\left(1-\frac z{rC}\right)dz=\frac{rC}{2}.
\]
两端合计为 \(rC\)。轴向角 \(C=0\) 时，弦长在投影内部恒为 \(1\)，
该积分恰为零，与同一公式一致。

代入 (4.3)，得到与其余格形状无关的准确概率
\[
\boxed{
q(\Lambda)=1-\frac{Sr}{s}+\frac{r^2C}{s},
\qquad r<s/S.
}
\tag{4.4}
\]

## 5. 主区的两项准确积分

在 (4.2) 中，primitive 短方向已经唯一至符号，故其总贡献为
\[
E_{\rm main}(s)=\frac1{2\zeta(2)s}
\int_0^{2\pi}\int_0^{s/S}
\left(1-\frac{Sr}{s}+\frac{r^2C}{s}\right)r\,dr\,d\vartheta.
\tag{5.1}
\]
径向积分准确等于
\[
\frac{s^2}{6S^2}+\frac{Cs^3}{4S^4}.
\]
两个角积分分别为
\[
\int_0^{2\pi}\frac{d\vartheta}{S^2}=4,
\qquad
\int_0^{2\pi}\frac{C\,d\vartheta}{S^4}=\frac23.
\tag{5.2}
\]
例如在第一象限令 \(t=\tan\vartheta\)，两积分分别化为
\(\int_0^\infty(1+t)^{-2}dt=1\) 和
\(\int_0^\infty t(1+t)^{-4}dt=1/6\)，再乘四。

因此
\[
\boxed{
E_{\rm main}(s)=\frac{2s}{\pi^2}+\frac{s^2}{2\pi^2}.
}
\tag{5.3}
\]
这是主区贡献的准确等式，余区贡献非负。

## 6. 余区只占薄壳，且其避空概率小

现在考虑 \(q(\Lambda)>0\) 且 \(r\ge s/S\) 的余区。
由 (3.2)，仍有 \(r\le4s<1\)。方格法向投影中的中央区间
\[
I_{\rm long}=[rC,S-rC]
\]
长度为 \(S-2rC\)，其中所有弦长均至少为 \(r\)。
如果某条格点行穿过这个中央区间，则其长度至少为一个格点周期的弦段
必含格点（边界相位零测）。故避空必须先避开全部这样的行。

如果 \(h<S-2rC\)，每个法向平移都使一条行进入中央区间，避空概率为零。
所以正避空概率要求
\[
h=\frac sr\ge S-2rC.
\tag{6.1}
\]
由 \(r\ge s/S\) 与 (6.1)，
\[
0\le r-\frac sS
\le\frac{2C}{S}r^2\le16s^2.
\tag{6.2}
\]
这里使用 \(C\le1/2\)、\(S\ge1\) 与 \(r\le4s\)，因而常数对全部角度一致，
包括接近轴向的角度。

此外，法向偏移没有格点行进入长度 \(S-2rC\) 的中央区间的概率为
\[
\left(1-\frac{S-2rC}{h}\right)_+.
\]
余区满足 \(h\le S\)，又有 \(h\ge S-2rC\ge1-r>1/2\)，故
\[
0\le q(\Lambda)\le\frac{h-S+2rC}{h}
\le\frac{2rC}{h}\le8s.
\tag{6.3}
\]
这个上界只要求中央长弦行不存在，没有假定两条短弦行的点相位独立，
所以对所有剪切参数都一致。

向量薄壳
\[
\mathcal S_s=
\{(r,\vartheta):s/S(\vartheta)\le r
\le s/S(\vartheta)+16s^2\}
\]
的面积满足
\[
\operatorname{area}(\mathcal S_s)
\le32\pi s^3+256\pi s^4
\le36\pi s^3,\qquad 0<s\le1/64.
\tag{6.4}
\]
使用唯一的 \(\pm v\)、(6.3) 和 primitive 平均，
\[
0\le E_{\rm shell}(s)
\le \frac{8s}{2\zeta(2)s}\operatorname{area}(\mathcal S_s)
\le\frac{864}{\pi}s^3.
\tag{6.5}
\]
壳层之外的格由 (3.2) 或 (6.1) 没有避空贡献。

## 7. 小参数展开与明确余项

结合 (5.3)、(6.5)，得到：

**定理 2。**
\[
\boxed{
E_2(s)=\frac{2}{\pi^2}s+\frac1{2\pi^2}s^2+O(s^3)
\qquad(s\downarrow0).
}
\tag{7.1}
\]
一个可直接使用的、未作常数优化的显式版本是
\[
\boxed{
0\le
E_2(s)-\frac{2s}{\pi^2}-\frac{s^2}{2\pi^2}
\le\frac{864}{\pi}s^3,
\qquad 0<s\le\frac1{64}.
}
\tag{7.2}
\]

这两项系数来自单短方向主区的准确积分；正的余项只来自多条格点行可能
穿过方格的薄壳。本证明已经处理短方向趋轴向时的统一性。

## 8. 对完整唯一率公式的直接作用

C90 完整有限分离曲线中的远支因子均为
\(E_2(a_j/\ell_j)\)。当 \(a_j/\ell_j\ge1\)，可直接代入 (2.1)；
当 \(a_j/\ell_j\le1/64\)，(7.2) 给带明确误差的两项式。
零窗口对应 \(E_2(\infty)=1\)，与 (2.1) 连续一致。

这使第一低精度过渡中的仿射核两端均可准确或有控计算。中间参数区间
\(1/64<s<1\) 仍由核的原定义承担，本篇没有声称一个未经推导的全区间
初等闭式。

## 9. 积分核 \(\Xi\) 的准确式与对数次项

定义在正规相遇弧的余面积积分中出现的核
\[
\Xi(b)=2\int_0^1[1-E_2(b/\ell)]\,d\ell,\qquad b>0.
\tag{9.1}
\]
当 \(b\ge1\) 时，全部 \(b/\ell\ge1\)，所以由 (2.1) 逐项积分得
\[
\boxed{\Xi(b)=\frac1b-\frac{2}{\pi^2b^2},
\qquad b\ge1.}
\tag{9.2}
\]
这里第一项为 \(2b^{-1}\int_0^1\ell\,d\ell=1/b\)，
第二项为 \(-6(\pi^2b^2)^{-1}\int_0^1\ell^2\,d\ell\)。

另一端令 \(t=b/\ell\)，则
\[
2-\Xi(b)=2b\int_b^\infty E_2(t)t^{-2}\,dt.
\tag{9.3}
\]
固定 \(\varepsilon=1/64\)。在 \(b<t<\varepsilon\)，(7.2) 给
\[
E_2(t)t^{-2}
=\frac{2}{\pi^2t}+\frac1{2\pi^2}+O(t).
\]
从 \(\varepsilon\) 到无穷的积分由 \(E_2\le1\) 有界。
所以 (9.3) 的主积分为
\((2/\pi^2)\log(1/b)+O(1)\)，得到
\[
\boxed{
\Xi(b)=2-\frac4{\pi^2}b\log(1/b)+O(b)
\qquad(b\downarrow0).
}
\tag{9.4}
\]
对 \(b=L^2J\) 且 \(J\) 在固定正紧区间的情形，该展开的余项一致。

## 10. 配套的端点源核

C82 已有的准确式为
\[
F_2(a)=1-\frac{21}{4\pi^2a}\qquad(a\ge1).
\]
代入 C85 的端点恒等式
\[
F_0(a)=2\int_0^1\ell F_2(a/\ell)\,d\ell
\]
立即给
\[
\boxed{F_0(a)=1-\frac7{2\pi^2a}\qquad(a\ge1).}
\tag{10.1}
\]
这项公式是已有两项恒等式的直接推论，本篇不将其作为新的独立 Haar 定理。
低参数端仍使用 C85 已证的
\[
F_0(a)=C_{\rm end}a^2-\frac2{\pi^2}a^3+O(a^4).
\tag{10.2}
\]

(9.2)、(10.1) 给正规弧局部真实缺口系数的准确高 \(L\) 三项式；
(9.4)、(10.2) 给低 \(L\) 的第一个对数修正。具体代入及弧积分系数见
[正规相遇弧与局部真实尾部](../tail/TRANSVERSE_ARC_AND_LOCAL_TAIL.md)，
此处保留其所需的完整核证明。

## 11. 证明与核查状态

本篇为几何计数、基本环面展开和既有 primitive Siegel 接口下的手推证明。
大参数证明中的有向 primitive 对计数及小参数证明中的无向短方向积分
都显式保留 \(1/2\) 因子。覆盖半径、中央长弦带、壳宽和壳概率分别证明，
未用浮点试验代替角度一致性或余项估计。
