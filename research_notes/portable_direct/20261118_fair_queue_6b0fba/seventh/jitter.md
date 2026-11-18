# 同一输出的螺旋三模组何时能分摊 jitter

对固定输出频率和手性，逐个热衰减率计算自身耗散再相加，会低估相干的 jitter。本文给出这种对角上界存在的充要条件，并构造一族真实无散 Fourier 初态，使没有权重的上界失效。在含 65 个不同热率的例子里，同一横向螺旋输出的实际热 Gram 是逐包自付之和的 **64.376545 到 64.376546 倍**。反例发生在初始时刻，作用于一项具体的分摊规则。全系统的有限时间可求和问题仍开放。[冻结任务书](https://github.com/awdawmip/enterprise-math/blob/29840e4bcf6fc68a07e3be7677913535b57749e7/research_tasks/NS_BRC_JITTER_ACTION_SUMMABILITY_20260917.md)

## 对角计费的充要条件

取经典归一化三维周期不可压模型，$\Lambda=(-\Delta)^{1/2}$，$u_s$ 为 $s=\pm$ 螺旋分量。冻结的径向交换子为 $C_s=-u_s\times\Lambda u_s$。固定 $s,k\ne0$，先在相同 $\sigma=|p|^2+|q|^2$ 下，按有序来源累加

$$
 b_\sigma=\tfrac12\sum_{p+q=k,\,|p|^2+|q|^2=\sigma}
 (|p|-|q|)\widehat u_s(p)\times\widehat u_s(q).
$$

每个三模组须保留父频率、手性、相位和径向差；下文的计费对象是这个和形成之后的热率。令

$$
 g(b)=\int_0^\infty\Big\|\sum_\sigma e^{-\sigma\tau}b_\sigma\Big\|^2d\tau
 =\sum_{\sigma,\eta}\frac{\operatorname{Re}\langle b_\sigma,b_\eta\rangle}{\sigma+\eta},
 \qquad
 d_w(b)=\sum_\sigma\frac{w_\sigma\|b_\sigma\|^2}{2\sigma}.
$$

**命题。** 给定正热率集和正权 $w_\sigma$。存在与截断无关的 $C$，对所有有限复向量包满足 $g(b)\le C d_w(b)$，当且仅当

$$
 M=\sup_j\sum_{2^j\le\sigma<2^{j+1}}w_\sigma^{-1}<\infty .
$$

最优常数落在 $(2\sqrt2/3)M\le C_*\le[1+4/(1-2^{-1/2})]M$。把变量归一化为 $x_\sigma=b_\sigma\sqrt{w_\sigma/(2\sigma)}$，核变为 $K_{\sigma\eta}/\sqrt{w_\sigma w_\eta}$，其中 $K_{\sigma\eta}=2\sqrt{\sigma\eta}/(\sigma+\eta)$。同一倍频段上的 $K\ge2\sqrt2/3$；取同向 $x_\sigma=e/\sqrt{w_\sigma}$ 得必要下界。频段相距 $m\ge1$ 时，$K\le2\,2^{-(m-1)/2}$。在每段对 $\sum\|x_\sigma\|/\sqrt{w_\sigma}$ 使用 Cauchy–Schwarz，再对段号使用可和卷积核的 $\ell^2$ 界即得上界。有限矩阵的最佳值也可直接读为归一化加权核的最大特征值。相位间的负交叉项在真实 Gram 中完整保留。

于是，若某倍频段含 $n_j$ 个不同热率，对该段每个率支付 $w_\sigma=n_j$ 即有统一常数；若段内使用相同权重，其必要数量级也是 $n_j$。同热率不同来源的数量不能代替不同热率数量。经典 Hilbert 不等式给整数热率的较粗支付 $g\lesssim\sum\|b_\sigma\|^2$，相当于在这里付与 $\sigma$ 成正比的权重。上述判据属于正实轴离散 Laplace 嵌入的情形，项目增量在于它对本行动逐频支付的精确限制和下述能满足实际螺旋约束的实例。[Jacob、Partington、Pott 的 Laplace–Carleson 嵌入研究](https://doi.org/10.1016/j.jfa.2012.11.016)

**可见行动的尖锐常数。** 对一组有限不同热率，令 $G_{ij}=1/(\sigma_i+\sigma_j)$。则

$$
 \Big\|\sum_i b_i\Big\|^2\le2\Big(\sum_i\sigma_i\Big)g(b).
$$

写 $1-\prod_j(z-\sigma_j)/(z+\sigma_j)=\sum_j v_j/(z+\sigma_j)$。在 $z=\sigma_i$ 代入可知 $Gv=\mathbf1$；在无穷远比较一次系数得 $\sum v_j=2\sum\sigma_j$。对正定 Gram 使用 Cauchy–Schwarz 即得，取 $b_j=v_j e$ 达等。这是自由包上的最佳常数；高热率较多时，它本身不能给出统一的可见行动上界。

## 一个能被实际低频横向模式读出的反例

固定 $k=e_1$、$L=2^m\ge8$，取 $j=L/2,\ldots,L$，共 $N=L/2+1$ 组。令

$$
 p_j=(L,j,0),\qquad q_j=(1-L,-j,0),\qquad p_j+q_j=k .
$$

在正手性上，使用 $h(v)=e_3+i(v\times e_3)/|v|$。因此 $v\cdot h(v)=0$，$iv\times h(v)=|v|h(v)$，并补齐共轭负频得到实场。给 $q_j$ 系数 $h(q_j)$，给 $p_j$ 系数 $\alpha_j h(p_j)$。置 $r=|p_j|,s=|q_j|,z=(r+s)^{-1}$，取

$$
 \alpha_j=[(r-s)j(1/r+1/s)(1-z)]^{-1}.
$$

所有分母为正。四类父频的第一坐标为 $L,1-L,-L,L-1$；要使和为 1 只能选前两类，第二坐标再迫使下标相同。因此该输出的全部正手性来源恰为上述无序对和各自交换次序。热率 $\sigma_j=L^2+(L-1)^2+2j^2$ 全不相同，都在 $[2L^2,4L^2)$。

两方向的交换子贡献相加，实际向量为
$$
 b_j=\frac{(-iX_j,-i,z)}{1-z},\qquad
 X_j=\frac{Ls+(L-1)r}{j(r+s)}.
$$
可直接由 $h(p)\times h(q)=i(\widehat q-\widehat p)-(\widehat p\times\widehat q)$ 求得，此处带帽的波矢表示单位方向。Leray 投影先去掉第一坐标，继而选负螺旋输出后，**每个热率的向量全都等于** $t=(0,-i/2,-1/2)$。这消除了仅凭纵向作用构造反例的疑虑。把初场在 $+k$ 的负手性接收系数取为 $-t$，在 $-k$ 取其共轭，便得到所有三角边都在同一真实场中的构造。接收模是单壳，所以其单手性交换子为零；按冻结的临界能量恒等式，$-2\operatorname{Re}\langle\Lambda u_-,C_+\rangle=2N$，互相干涉确实能被临界三线性项读出。每一组的正手性父模还可独立乘一个复系数并补共轭，从而在这一横向输出实现任意包相位。

令 $d_1$ 表示每包只付自己的对角项。该横向读出的比值精确等于

$$
 \frac{g}{d_1}
 =\frac{\sum_{i,j}1/(\sigma_i+\sigma_j)}{\sum_i1/(2\sigma_i)}
 \ in\ [N/2,N].
$$

下界只需全体率在同一倍频段，上界由向量求和不等式。对未投影的原始 $C_+$ 同样失败：上式中的 $X_j\le2,z\le1/15$，故 $\|b_j\|^2<6$，而第二坐标全同相、模长至少 1，给出原始比值 $\ge N/12$。在一个固定输出上，无权逐率支付缺少的因子没有随尺度统一的上界。所有输入为三角多项式；它们可作为平滑 NS 初态，模拟一个孤立封闭的多三元 ODE 无须作为前提。构造没有证明整场其它输出或非线性能量预算也必然失效。

| $L$ | 不同热率数 | 负螺旋读出 $g/d_1$ 的严格区间 |
|---:|---:|---:|
| 8 | 5 | (4.920769, 4.920770) |
| 16 | 9 | (8.888897, 8.888898) |
| 32 | 17 | (16.817470, 16.817471) |
| 64 | 33 | (32.671063, 32.671064) |
| 128 | 65 | (64.376545, 64.376546) |

## 接续到全 PDE 的条件

沿光滑实解令 $A=\sum_{s,k}|k|^{-1}\|\sum_\sigma b_{s,k,\sigma}\|^2$，$J=\sum_{s,k}|k|^{-1}g(b_{s,k})$。$A$ 在通常全空间 NS 缩放下乘以尺度的平方，$J$ 为临界尺度不变量。以 $N_s$ 表示投到手性 $s$ 的全非线性项。定义 $d^N_{s,k,\sigma}$ 为源包中依次将两条父腿之一的 $u_s$ 替换成 $N_s$ 后相加。逐分支保留被替换的腿和内层父频；这一步既含非零的原有模态，也含瞬时为零而由非线性产生的新输入。然后在同一输出、手性和相同热率上相干复合，最后才形成热 Gram。热生成元贡献为 $-\nu\sigma b_\sigma$。有限谱上 $\mathrm{diag}(\sigma)G+G\mathrm{diag}(\sigma)=\mathbf1\mathbf1^T$，给出冻结的 $J'+\nu A=I$，其中 $I=2\sum |k|^{-1}\operatorname{Re}\langle b,G d^N\rangle$。光滑解上可由 Fourier 收敛使用同一恒等式。零包仍可能有非零导数，做条件估计时需包含新输入的热率。

对响应包的可用率集选择正权并计算各自的 $M_{s,k}(t)$。一个足够的延拓条件是
$$
 \int_0^T\!\left(
 \sum_{s,k\ne0}|k|^{-1}M_{s,k}(t)
 \sum_\sigma\frac{w_{s,k,\sigma}(t)\|d^N_{s,k,\sigma}(t)\|^2}{2\sigma}
 \right)^{1/2}dt<\infty .
$$
令根号内为 $B(t)$，上界常数记为 $C_0=1+4/(1-2^{-1/2})$。Gram 对偶给出 $|I|\le2\sqrt{J}\sqrt{C_0 B}$。既有零点安全能量 $F=J+\nu^2\|u\|_{\dot H^{1/2}}^2/4$ 满足 $F'+\nu^3\|u\|_{\dot H^{3/2}}^2/4\le I$。因此 $\sqrt F(t)\le\sqrt F(0)+\int_0^t\sqrt{C_0 B}$。代回得到有界临界范数和可积临界耗散，再由 $L_t^4L_x^6$ 的 Serrin 判据延拓。取 $w=n_j$ 总能使每个非空频率族的 $M=1$，代价是需要实际控制带倍频段计数的响应。该响应含全系统的三次交互，仍缺一个由初始数据控制、不会在不同输出重复花费同一模态耗散的时间积分估计。局部中轴放大与正手性交互的既有结论并没有提供这个估计。[项目交接](https://github.com/awdawmip/enterprise-math/blob/29840e4bcf6fc68a07e3be7677913535b57749e7/research_notes/ns_brc_program_handoff_20260917.md) · [零点安全临界能量与适用范围](https://github.com/awdawmip/enterprise-math/blob/246c6de883f0a7ffd8c2fe0f8fc09b663c25e7b6/research_notes/ns-jitter-initial-data-certificate-20260909.md)

**复算。** `python3 jitter_check.py --repo "$EM_SOURCE_ROOT" --json jitter_checked.json`，环境为 Python 与 SymPy 1.14。$L=8,16,32,64,128$ 各自枚举所有有符号父频对，按完整波矢验证合法来源，对热 Gram 使用有理分数。对 7 个物理三模组实际调用冻结的 `helical_data`，重新从两个有序交换子求和，逐分量核对散度、螺旋符号、共轭及接收投影。另用 4 组不同热率核验正定性、尖锐端点等式、热生成元及含相位源的微分恒等式。证明保留全部 $m\ge3$；有限数据没有代替无界归纳。逐频完整 Gram 对 $n$ 个不同热率需 $O(n^2)$ 次内积，用倍频段权重计算该对角上界需 $O(n)$ 次统计，均在完成父频枚举和相干组和之后。[继承的 Fourier 实现](https://github.com/awdawmip/enterprise-math/blob/29840e4bcf6fc68a07e3be7677913535b57749e7/research_notes/ns-causal-inverse-newton-basin-20260909/inherited_fourier.py)
