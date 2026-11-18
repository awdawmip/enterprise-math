# Eisenstein 三次 Gauss 和：可增长的角频率与定量误差

任务 RS-OAI7-023-D-20261007-6F2A81。令 \(\omega=e^{2\pi i/3}\)，取 \(\mathbb Z[\omega]\) 中模 3 为 1 的主生成元；分裂有理素数上方的两个素理想都计入。令 \(\Theta_\ell(z)=(z/|z|)^\ell\)，\(G(\pi)\) 为冻结手稿按 \(\sum_v\chi_\pi(v)e(\operatorname{Tr}(v/\pi))/\sqrt{N\pi}\) 归一化的三次 Gauss 和，\(c_*=(2\pi)^{2/3}/(3\Gamma(2/3))\)。角频率是 \(\ell\)，幂矩次数另记为 \(k\)。本文承接外部手稿的径向分解、三次筛、径向色散和 Perron 引理，重新估计插入角模后每个依赖频率的接口。结论的证据等级随这些外部输入；有限域复算只核对代数部分。[任务书](https://github.com/awdawmip/enterprise-math/blob/7f434ff87c2dec1801435a55d2a77714f93605c0/research_tasks/RS-OAI7-023-D-20261007-6F2A81.md) · [冻结稿的归一化与径向定理](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/build/paper.tex) · [原固定角模定理](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/build/sections/angular.tex#L19)

**增长窗口。** 写 \(L=\log X\)。固定正函数 \(H(X)\ge1\)，若
\[
 \log(3+H(X))=o\!\left(\frac{L\log\log L}{(\log L)^2}\right),
 \tag{1}
\]
则依照上述冻结输入，有一个固定 \(C\) 使
\[
\sup_{|\ell|\le H(X)}
\left|\sum_{N\pi\le X}\Theta_\ell(\pi)
       \bigl(G(\pi)-c_*(N\pi)^{-1/6}\bigr)\right|
\ll X^{5/6} L^{-3/2}(1+\log L)^C. \tag{2}
\]
素数均取主生成元。对 \(1\le|\ell|\le H(X)\)，删去模型项后同一上界成立。例 \(H(X)=\exp\{L/(\log L)^2\}\) 满足 (1)。原稿的逐模 \(o_\ell\) 单独不能推出这样的窗口：对任意趋于无穷的整数 \(f(X)\)，数组 \(\mathbf1_{|\ell|=f(X)}\) 的每个固定频率最终为零，而区间 \(|\ell|\le f(X)\) 上的上确界始终为一。以下给出所需的统一估计。

## 1. 最大素因子的截断决定可用频率

令 \(\Psi\) 是有限三次特征乘 \(\Theta_\ell\) 的本原 Hecke 特征。有限导子范数 \(D\le9N\mathfrak f_\chi\)，无穷型的两参数为 \(j,j+1\)，\(j=|\ell|/2\)，所以 \(\mathfrak C=3D(j+3)(j+4)\)。非零无穷型或非平凡有限三次特征均排除二次例外零点。二次域的绝对零区常数、固定次数 2 与有界局部参数给出素理想加权和的界
\[
\ll x\{\log(x\mathfrak C)\}^4
 \exp\{-c\log x/(\log\mathfrak C+\sqrt{\log x})\}
 +O(\sqrt x\log^2 x).
\tag{3}
\]
这是对非主特征的估计。Kaneko–Thorner 定理 1.2 的 \(\ell^2\) 假设在本族由 \(|a(p^j)|\le2\) 满足，去掉素数幂仅产生显示的次项。对数范数扭曲和光滑权以部分求和计入，所需范数高度只为 \(L^{O(1)}\)。删去范数为 \(X^{O(1)}\) 的指定元素的素因子，仅删 \(O(L)\) 项。[零区与例外条件，Chen–Park–Swaminathan 引理 2.1](https://arxiv.org/abs/1506.09170v3) · [Kaneko–Thorner，定理 1.2](https://doi.org/10.5802/aif.3698) · [原稿式 (3) 的导子、参数与证明](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/build/sections/angular.tex#L99)

原序列条件 (SW) 要求对长度 \(B\ge X^{b_0}\) 的分解块及任意固定 \(D_1\)，有 \(O(BL^{-D_1})\) 的余量。这里 \(b_0>0\) 由原分解固定。原证明以 \(\exp(\sqrt L)\) 为大素因子下限。现在对所要求的 \(D_1\)、固定除数权和固定分解复杂度选常数 \(K\)，并置
\[
 u=K\frac{\log L}{\log\log L},\quad
 w=L/u,\quad y=e^w,\quad \sigma=\frac{\log u}{2w}.
\]
绝对值控制下，所有素因子范数 \(\le y\) 的部分由 Rankin 估计至多为
\[
 \ll B L^{O(1)}
 \exp\{-b_0 L\sigma+O(\log w+\sqrt u)\}.
\tag{4}
\]
确实，理想素数的 Chebyshev 上界经分部求和给出
\(\sum_{N\pi\le y}(N\pi)^{-1+\sigma}\ll\int_{1}^{w}e^{\sigma v}dv/v+O(e^{\sigma w})\ll \log(2w)+\sqrt u\)。固定次除数权的欧拉积取对数后仍受该量控制，因 \(\sigma<1/4\) 时高次素数幂绝对可和。式 (4) 的负项为 \(-b_0u\log u/2\)，故增大固定 \(K\) 可付清任意预定的对数损失。

其余项固定最大素因子之外的所有变量；原分解的范数分箱、平局规则及区间截断仍可沿用，第一段从 \(y\) 切开即可。剩余素数的长度 \(P\) 满足 \(\log P\ge w-O(1)\)。给定 \(D\le L^{O(1)}\)，由 (1)
\[
 \frac{w}{\log \mathfrak C+\sqrt w}\big/\log L\longrightarrow\infty
\]
一致成立。式 (3) 因而提供任意对数节省，足以支付部分求和、区间与固定补因子的损失。这一改动只替换 (SW) 证明中的分析截断；原分解中由停止条件决定的乘积分箱和粗糙度门槛照用。[原最大素因子分解及区间条件](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/build/sections/decomposition.tex#L430)

## 2. 导数、对偶长度与极端矩的全部频率代价

以下 \(H=H(X)\)，由 (1) 有 \(H=X^{o(1)}\)。本节把这种因子吸收到**固定正幂余量**。仅有对数余量的步骤在第 3 节单独处理。

1. **角 Voronoi 变换。** 精确公式中外相位 \(\Theta_{3\ell}(r)\)、内相位 \(\Theta_{-\ell}(d^3\nu)\) 的模都是 1，只有 \(\ell=0\) 有留数。写 \(Q_\ell(z)=\Gamma(5/6+j-z)\Gamma(7/6+j-z)/[\Gamma(z+j-1/6)\Gamma(z+j+1/6)]\)。在 \(\Re z=-A\) 上，成对取同虚部的 Gamma 模，统一比值界给 \(|Q_\ell(-A+iv)|\ll_A(1+j+|v|)^{2+4A}\)。这来自右半平面的均匀 Stirling 公式；对有限个使实部不够大的 \(j\) 用递推与紧集有界性，分母 Gamma 的极点仅给零。临界线则精确有 \(|Q_\ell(1/2+iv)|=1\)。低高度完成和的误差至多比原式多 \(O_\sigma((1+H)^{2+4\sigma})\)，在 \(X^\epsilon R^{1/2}\) 中先缩小 \(\epsilon\) 即可。DR 的精确系数公式中随角模出现的其余因子均为单位相位。[原式与低高度估计](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/build/sections/angular.tex#L141) · [Dunn–Radziwiłł 式 (5.79)–(5.80)](https://arxiv.org/abs/2109.07463v3)
2. **大高度完成和。** 对 \(T\ge2,\ |t|\asymp T\)，令 \(S=1+T+|\ell|\)。统一对偶截止为 \(I_{\max}=X^\delta R^2 S^4/V\)，按 \(t\) 的整段取共同上界。移到 \(-A\) 后尾部为 \(O(R^{1/2+\eta} S^2 (R^2 S^4/V)^\sigma X^{-\delta(A-\sigma)})\)，平滑 Mellin 尾由固定高阶导数支付。可先固定 \(\delta\) 再取大 \(A\)。在 \(V\le\sqrt R\,S^2\) 时，普通均值给出 \(\ll X^\epsilon\sqrt V(1+R^{1/4}S/\sqrt T)\)，\(\ell=0\) 的留数依旧单独减掉。在 \(V>\sqrt R\,S^2\) 时，保留的 \(I\ll X^\delta R^{3/2}S^2\)；临界线上的相位对整行共同，原双曲和估计是 \(\ll X^\epsilon\sqrt V(1+\sqrt{I/(RT)})\)。重选小损失后就得同一界。逆完成卷积的 \(\Theta_{3\ell}(c)\) 模为 1，因而 Type I 大高度误差为
\[
 \ll X^{1/2+\epsilon}R^{3/4}
       \left(\sqrt T+\frac{1+|\ell|}{\sqrt T}\right)
\]
另加原径向留数（限 \(\ell=0\)）。因 \(S/T\ll1+H=X^{o(1)}\)，Perron 两个端点 \(.805,\ 5/6-3\kappa/8+\rho/2\) 仍有严格正幂余量。[变换与原均值求和](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/build/sections/angular.tex#L245)
3. **平面计数只花一阶角导数。** 在固定环带，\(s\) 阶空间导数的角部分至多 \(O_s((1+|\ell|)^s |z|^{-s})\)。原模型格点估计以基本胞积分和梯度比较，在非零频率时面积项为零，误差为 \(O((1+|\ell|)L^C(1+\sqrt Y))\)。平方因子与互素反演后得到 \(O((1+|\ell|)X^\epsilon\sqrt U)\)，总模型误差在原 \(.589\) 的指数上增加 \(o(1)\)。长完成尾的角相位全是独立系数，使用原绝对筛界；其原有最坏幂次仍严格低于 \(5/6\)。[模型格点与逆完成](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/build/sections/angular.tex#L365)
4. **极端矩的平滑对偶。** 单 Gamma 比在 \(-A\) 上的次数为 \(1+2A\)，故统一截断为 \(J\ll Y^\epsilon D(1+|\ell|+|t|)^2/Z\)。在临界线上其模恰为 1，有限 Euler 因子、根数、导子相位仅是行标量，Mellin 权与行无关。极端情形中 \(Y\) 是 \(X\) 的固定正幂量级（反例序列趋向 \(B=X^{1/2+o(1)}\)）；\(|\ell|=Y^{o(1)}\)。在内部高度 \(\le Y^{.37}\) 时仍有源中的 \(J\le Y^{.74+o(1)}\)（第一种极端情形），两种二阶矩指数 \(2.16\) 与 \(2/3+2(1/3+.37)\) 仍严格小于 \(7/3\)。主导完整因子之外的角相位是所有行共用的有界系数；卷积合并时 \(\Theta_\ell(x)\Theta_\ell(y)=\Theta_\ell(xy)\)，不会把阶数乘以重复次数。在 Gram 估计中这些相位不进入径向行核。若邻域与节省无法统一，就取反例列 \((Y_i,\ell_i)\)。上述完整因子界在该列统一，其余筛和 Gram 界只要求共同的有界系数；选收敛子列固定长度指数后，原多重性矛盾对这条列仍然成立。由此可先选一个与各 \(\ell_i\) 无关的邻域和正幂节省，再用于最终分解。[原完整因子、两种极端情形与 Gram 余量](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/build/sections/angular.tex#L440) · [径向紧性论证](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/build/sections/dual.tex)

## 3. 组装与幂矩的分界

色散时保留外部 \(a\)-权径向，角因子进入系数；Cauchy 去掉第一项相位，展开成对系数后共同因子抵消。平方项、混合项与模型平方保留原 \(1,-2,1\) 消去；混合项内层使用径向 Type I。小 \(B\) 的功率宽度、允许的任意高度平移、对高度权的分部积分都保持原界。大 \(B\) 在极端处用第 2 节第 4 项，在低导子处用第 1 节。尤其在三素数过渡，\(L^{-3/2}\) 只来自径向色散短段界及 \(\sum|\alpha|^2\ll A/L^2,\sum|\beta|^2\ll B/L,\sum|\beta|\ll B/L\)；单位角因子不改变这三项。该处没有乘上任何 \(H^{O(1)}\)。[角模色散及径向混合项](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/build/sections/angular.tex#L630) · [三素过渡的原计算](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/build/sections/perron.tex#L110)

按原顺序先取 \(\gamma,\kappa,\rho,\xi\) 和固定的分箱复杂度；再固定有限多项对数节省和高度阈值；最后取 (4) 的 \(K\) 并缩小各正幂余量。Perron 高度 \(X^{1/6+\rho}\) 的截断误差只用素理想同范数的绝对重数。三素过渡有 \(O((1+\log L)^C)\) 个配置及 \(O(1+\log L)\) 个低高度块；其余项能给 \(O(X^{5/6}L^{-2})\) 或更小。于是得到 (2) 的二进版。对全范围先用绝对值处理范数 \(\le X^{1/2}\)，其余各块 \(\log y\asymp L\)，对同一 \(\ell\) 仍满足 (1) 的条件并可按长度几何求和。对于非零模，模型的素角和由 (3) 和 Abel 分部求和得到 \(O_M(X^{5/6}L^{-M})\)，从而可删去模型项。[原 Perron 参数次序](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/build/sections/perron.tex#L315)

写 \(k=3m+r,\ r=0,\pm1\)。精确恒等式 \(G(\pi)^3=-\Theta_1(\pi)\) 给出
\[
G(\pi)^{3m}=(-1)^m\Theta_m(\pi),\quad
G(\pi)^{3m+1}=(-1)^m\Theta_m(\pi)G(\pi),\quad
G(\pi)^{3m-1}=(-1)^m\overline{\Theta_{-m}(\pi)G(\pi)} .
\]
因此 (2) 给出 \(1\le|m|\le H(X),r=\pm1\) 的统一消去；\(m=0,r=\pm1\) 保留径向主项 \((6/5)c_*X^{5/6}/L\)。\(r=0,m\ne0\) 时，(3) 单独给 \(O_M(X L^{-M})\)，这不够达到 \(X^{5/6}/L\)；\(k=0\) 数的是素理想。上面取有符号的复和，不能把各项替换成绝对值。[原固定幂矩讨论](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/build/sections/angular.tex#L802)

检查器对范数 \(\le997\) 的 166 个主素元逐一从三次剩余符号和迹加性特征计算。对 160 个分裂主素元得到精确 Jacobi 和 \(J(\chi_\pi,\chi_\pi)=-\pi\)；另对其中 24 个用完整循环卷积直接验证未归一化 Gauss 和的三次方为 \(-N\pi\,\pi\)。其余六个惰性素理想的加性群环求和均精确化为正有理素数。这个核验也说明使用哪个主生成元会改变相位。频率窗口的证据来自上述分析估计。[复算程序](angular_check.py) · [逐类结果](angular_checked.json) · [随尺度收窄的角观察](phase_windows.md)
