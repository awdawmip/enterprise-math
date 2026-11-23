# C88　中间库存趋近首端时的全库存桥接

## 0. 对象、输入与证明范围

本篇继续原三态因子路径的原始观察者 H(0,1)。源安排与全部竞争安排始终为整数标签

\[
2\le w\le v\le c,\qquad N_c=\binom c2.
\]

读取库存 \(c,c+A,c+B\)，其中 \(1\le A<B\)，增加的因子 5 均放在第一次 23 更新之前。下面的二维比例坐标、格与 Haar 分布只描述原整数标签经读数微分后的辅助计数坐标；不替换原生状态、更新次序或全部竞争者。

输入为 C82 的准确有限谱及固定阶联合导数控制、\((G,B_1,B_2)\) 几乎处处全域单原像性、正规域穷尽、格空间均匀分布证明。特别是，C82 对 \(B_1\) 的流导数非退化核验在这里直接沿用。C84 的固定有理位置结论本身不被当作移动位置的一致定理。

设

\[
z=\frac Bc,\quad s=\frac Ac,\quad
\theta=\frac AB,\quad D=\sqrt{\frac cB},\quad
\ell=\frac{D^3}{c}=\frac{\sqrt c}{B^{3/2}},
\]

\[
p_*(c,B)=\frac74\log_2c+\frac12\log_2(c/B),\qquad
L_c=2^{p-p_*(c,B)},\qquad
\lambda_c=2^pc^{-3/4}=L_c cD.
\]

对余体积为 \(a\) 的 Haar 格 \(\Lambda\)，令 \(F_0(a)\) 是三个独立均匀相位下，位移列表

\[
\{(u,u,v):(u,v)\in\Lambda\setminus\{0\}\}
\]

没有非零同格竞争者的概率。它是独立相位的端点延拓；并非在同一库存、同一格原点机械重复一次测量的概率。令

\[
J(X)=|\det d(G,B_1)(X)|,\qquad
\Phi_0(L)=2\int_{0<y<x<1}F_0(L^2J(x,y))\,dx\,dy.
\]

## 1. 全库存定理与较弱的近距定理

**定理 A（移动至端点的全库存极限）。** 若

\[
B=o(c),\qquad \frac AB\longrightarrow0,
\qquad \frac AD=A\sqrt{B/c}\longrightarrow\infty,
\qquad L_c\longrightarrow L\in(0,\infty),
\tag{1}
\]

则三次原读数允许全部库存竞争者的唯一比例满足

\[
\boxed{
\sup_{\alpha\in\mathbb T^3}
|V_c^{(3)}(\alpha)-\Phi_0(L)|\longrightarrow0.
}
\tag{2}
\]

三个舍入格原点可相互独立并随库存改变。对任一边界零面积的固定正规源区域 \(K\)，以全目录大小 \(N_c\) 为分母的唯一贡献，同样趋于 \(2\int_K F_0(L^2J)\)，竞争者仍来自全库存。

条件 \(A/D\to\infty\) 自动推出 \(B/D\to\infty\)，即 \(\ell\to0\) 或 \(B/c^{1/3}\to\infty\)。因此 (1) 已包含局部线性格极限所需条件，无须再列一个独立的立方根条件。

**定理 B（移动至端点的近距极限）。** 若仅有

\[
B=o(c),\quad B/c^{1/3}\to\infty,\quad
A/B\to0,\quad 1\le A<B,\quad L_c\to L\in(0,\infty),
\tag{3}
\]

则任取 \(r_c\to0\)、\(cr_c/D\to\infty\)，只检查距离不超过 \(cr_c\) 的竞争者所得近距唯一率，仍满足 (2)。如果源限于 C81 已证明 \((G,B_1)\) 全宏观单原像的固定区域，则这一源贡献已允许全库存竞争者。

定理 B 不要求 \(A\to\infty\)，因此包括 \(A=1\)。它不声称此时整个库存的远隔逆支已消失。定理 A 的 \(A\gg D\) 是本证明的全库存充分条件；本篇不主张它必要。

首末对称地，若 \((B-A)/B\to0\)、\((B-A)/D\to\infty\)，则定理 A 同样成立，极限仍为 \(\Phi_0\)。定理 B 也有对应的首末对称版本。

## 2. 有限二阶差商：放大的是舍入误差

写

\[
\mathcal G_c(t,X)=c^{3/4}\{g(c(1+t);cX)-1\},\qquad
U_c(X)=\mathcal G_c(0,X),
\]

\[
P_{r,c}(X)=\frac{\mathcal G_c(r,X)-\mathcal G_c(0,X)}r.
\]

取三个点 \(0,s,z\)，定义

\[
Q_c(X)=\frac2{z-s}\left[P_{z,c}(X)-P_{s,c}(X)\right].
\tag{4}
\]

这等于 C84 的 \(Q_{\theta,c}\)。对任何所需的源坐标导数，二阶差商具有积分表达

\[
Q_c(X)=2\int_{\substack{u,v\ge0\\u+v\le1}}
\partial_t^2\mathcal G_c(us+vz,X)\,du\,dv.
\tag{5}
\]

积分三角形面积为 \(1/2\)。故有限谱固定阶导数收敛给

\[
U_c\to G,\quad P_{z,c}\to B_1,\quad
P_{s,c}\to B_1,\quad Q_c\to B_2
\tag{6}
\]

于正规内紧片上一致成立，其误差不会因 \(\theta\downarrow0\) 额外放大。

若两条安排在三个库存均同格，则各准确归一读数差至多 \(\lambda_c^{-1}\)。由 (4) 的系数绝对值之和，

\[
|\Delta U_c|\le\lambda_c^{-1},\qquad
|\Delta P_{z,c}|\le\frac2{\lambda_c z},\qquad
|\Delta Q_c|\le\frac4{\lambda_c s(z-s)}.
\tag{7}
\]

准确地，

\[
\lambda_c s(z-s)
=L_c\frac{A(B-A)}{\sqrt{cB}}
=L_c\frac AD(1-\theta).
\tag{8}
\]

因此定理 A 中第三项误差趋零。二阶差商的数值近似与舍入传播误差应分开处理：式 (5) 控制前者，式 (8) 控制后者。

### 排除全部远隔宏观逆支

在 C82 的几乎处处单原像正规源点上，(6)–(8) 迫使任一三次同格竞争者的宏观极限共享 \((G,B_1,B_2)\)。C82 的单原像定理、紧性以及边界小尾控制遂迫使竞争者回到源点的同一局部正规逆片。这里不是只排除当前附近预先列出的对手，而是先保留全部库存竞争者，再使用其任意宏观聚点。

进入同一片后，使用**外端**一阶差商 \((U_c,P_{z,c})\) 的一致双 Lipschitz 反演及 (7)，得到

\[
|X'-X|\le C_K\left(\lambda_c^{-1}+(\lambda_c z)^{-1}\right)
\le C'_K\frac Dc.
\tag{9}
\]

于是整数位移 \(q=c(X'-X)\) 为 \(O_K(D)\)。若改用较短的内端差商反演，会引入不必要的 \(B/A\) 因子；这里用 (9) 避免该损失。有限正规紧片穷尽后，不能如此处理的源仅占 \(o(c^2)\)，而且结论对所有格原点同时成立。

定理 B 不使用二阶差商排除远支；近距限制加同片反演仍给 (9)。在 \((G,B_1)\) 全宏观单原像区域，外端两次读数已足以使全部竞争者进入同片。

## 3. 局部三位移与端点延拓的一致近似

对 \(|q|\le C_KD\)，准确相对格位移为

\[
a_j(X,q)=\lambda_c\{\mathcal G_c(t_j,X+q/c)-\mathcal G_c(t_j,X)\},
\quad(t_0,t_1,t_2)=(0,s,z).
\]

令

\[
\mathsf B_c(X)=\begin{pmatrix}\nabla U_c(X)\\\nabla P_{z,c}(X)\end{pmatrix},
\quad S=\begin{pmatrix}1&0\\1&1\end{pmatrix},
\quad M_c=L_cS\operatorname{diag}(D,D^{-1})\mathsf B_c.
\]

首末两个位移与 \(M_cq\) 的误差一致为

\[
O_K(D^3/c)=O_K(\ell).
\tag{10}
\]

中间位移由 (4) 的准确恒等式给出

\[
a_1-(1-\theta)a_0-\theta a_2
=-\frac{\lambda_c s(z-s)}2
\{Q_c(X+q/c)-Q_c(X)\}.
\]

故其绝对值一致为

\[
O_K\left(\frac{A(B-A)}{Bc}\right)
=O_K\bigl(\theta(1-\theta)B/c\bigr)=o(1).
\tag{11}
\]

实际列表或线性模型中任一端可同格的标签均有 \(|q|\le C_KD\)：实际列表由 (9)，模型则由 \(M_c^{-1}\) 的 \(O_K(D)\) 范数及首末两个位移的有界性。因而 (10)–(11) 控制的是两份完整有效竞争者列表。

对固定的端点坐标 \((u,v)\)，中间标记为 \((1-\theta)u+\theta v\)。可能进入碰撞窗口的向量满足 \(|u|,|v|\le1+o(1)\)，所以把 \(\theta\) 改为零，使标记改变至多 \(2\theta+o(1)\)。C82 的八角单调盒稳定性对任意个竞争者均有统一常数。因此，原点平均的唯一指标及其任一固定 Fourier 权重，都可用 \((u,u,v)\) 模型替换，总误差为

\[
O_K(\ell+B/c+\theta)=o(1).
\tag{12}
\]

特别地，若 \(q_\theta(\Lambda)\) 表示固定格的独立相位唯一概率，则

\[
|q_\theta(\Lambda)-q_0(\Lambda)|\le C\theta
\tag{13}
\]

对所有二维格及全部余体积统一成立。重复的局部标记不会破坏此稳定性；三个相位是否独立则必须另证。

## 4. 原点平均的 Haar 极限

\(q_0\) 有界连续。它满足与 C82 相同的矩阵扰动估计

\[
|q_0(T\Lambda)-q_0(\Lambda)|\le C\|T-I\|
\tag{14}
\]

当 \(T\) 充分接近恒等时成立，因为首末两个坐标仍限制全部可能竞争向量于固定有界窗口。于是源格求和到连续积分的误差为 \(O_K(D^2/c)=O_K(1/B)\)。

在准确有限谱的梯度斜率上换坐标，按 C82 将 \(\mathsf B_c\) 分解为下三角、对角及上三角因子。\(\operatorname{diag}(D,D^{-1})\) 把下三角因子压至恒等；在固定小源块冻结余体积、对角系数及密度，然后用固定区间扩张 horocycle 的 Haar 均匀分布。该证明只要求 (14)，故逐字适用于 \(q_0\)。没有先将有限谱换成极限谱再放大误差。

其结果为

\[
\int_K q_0(M_c(X)\mathbb Z^2)\,dX
\longrightarrow\int_KF_0(L^2J(X))\,dX.
\tag{15}
\]

结合 (12)、\(N_c/c^2\to1/2\) 与正规源穷尽，得到定理 A、B 所需的三原点**平均**极限。

## 5. 三个相位确实独立：移动位置下的固定模式消去

记准确源读数 \(Y_j(X)=\lambda_c\mathcal G_c(t_j,X)\)。对每个源点的完整有效位移列表，令 \(E_{c,X}\subset[0,1)^3\) 为可唯一相位集合，并置

\[
w_{k,c}(X)=\int_{E_{c,X}}e^{-2\pi i k\cdot\xi}\,d\xi,
\qquad k=(k_0,k_1,k_2)\in\mathbb Z^3.
\]

原点 Fourier 系数为

\[
\frac1{N_c}\sum_X
e^{2\pi i k\cdot Y(X)}w_{k,c}(X).
\tag{16}
\]

所有权重的绝对值至多一；在正规紧片，全方向局部 Lipschitz 界为 \(O_K(D^2)\)。有限源边界由光滑截断与穷尽处理。

### 5.1 总系数非零

若 \(K_0=k_0+k_1+k_2\ne0\)，固定整数源方向 \(h\) 与固定步数 \(r\)，源平移 \(rh/c\) 只使权重改变 \(O_{K,k,r}(D^2/c)=O(1/B)\)。相位增量为

\[
k\cdot\{Y(X+rh/c)-Y(X)\}
=rL_cDK_0\,h\cdot\nabla U_c(X)+o(1),
\tag{17}
\]

其误差包括 \(O_r(Dz+D/c)=o(1)\)。在 \(\det\operatorname{Hess}G\ne0\) 的正规片，\(h\cdot\nabla G\) 有非零梯度，因此 (17) 的一步相位模一均匀分布。先平均固定的 \(H\) 个整数源步，利用权重有界，绝对值由 Dirichlet 平均的绝对值控制；其无权源平均趋于 \(\int_0^1|H^{-1}\sum_{r=1}^He^{2\pi irt}|dt\le H^{-1/2}\)。再令 \(H\to\infty\)，(16) 趋零。这一步无需假定权重变化比振荡的连续导数更慢。

### 5.2 总系数为零：不再使用固定有理位置的整数共振

若 \(K_0=0\)，相位准确为

\[
\phi_{k,c}=k\cdot Y
=\lambda_c\left[k_1sP_{s,c}+k_2zP_{z,c}\right].
\tag{18}
\]

若 \(k_2\ne0\)，取

\[
W_c=\lambda_c z=L_cc/D\longrightarrow\infty.
\]

则

\[
\phi_{k,c}/W_c=k_2P_{z,c}+k_1\theta P_{s,c}
\longrightarrow k_2B_1
\tag{19}
\]

于所需固定阶导数上一致成立。

若 \(k_2=0\)，则非零模式必有 \(k_1\ne0\)。取

\[
W_c=\lambda_c s=L_cAD\longrightarrow\infty,
\]

最后一步仅用 \(A\ge1\)、\(D\to\infty\)。此时

\[
\phi_{k,c}/W_c=k_1P_{s,c}\longrightarrow k_1B_1.
\tag{20}
\]

因此移动至端点后，每个固定非零零和模式均由一阶库存谱消去。固定有理位置的二阶共振向量会随位置移动而增长，不能把它当作一个固定 Fourier 模式；证明也不需要对该增长频率取得一致消去率。

### 5.3 权重沿适配流统一受控

取有限谱向量场

\[
\mathcal V_c=(\operatorname{Hess}U_c)^{-1}\nabla U_c.
\]

对一段短流的任一端有效的标签，\(|q|\le C_KD\)，Taylor 展开给

\[
\mathcal V_c a_0=a_0+O_K(D^3/c).
\tag{21}
\]

若标签只在一端有效，Gronwall 仍使它沿整段的 \(a_0\) 及其流导数保持有界。又对 \(t_j\le z\)，

\[
|a_j-a_0|+|\mathcal V_c(a_j-a_0)|
\le C_KD^2t_j\le C_K.
\tag{22}
\]

对两端有效标签的并集应用角盒稳定性，得到 \(w_{k,c}\) 沿流的统一 Lipschitz 界。这里的常数与 \(\theta\) 及有效竞争者个数无关。

源和改为连续积分的误差为

\[
O_K\left(\frac{D^2+W_c}{c}\right)
=O_K(1/B+1/D)=o(1),
\tag{23}
\]

因为两种 \(W_c\) 均不超过固定倍数的 \(c/D\)。C82 已证明 \(\mathcal V B_1\) 在各正规符号片不是恒零解析函数，故其零集面积为零。在避开该零集的有限流坐标片上，(19) 或 (20) 的归一相位导数有统一正下界；对具有统一流 Lipschitz 界的权重分部积分，使 (16) 为 \(O_K(W_c^{-1})\)。去除任意小质量的例外片，所有非零模式均消失。

这证明实际三个源相位在所需的加权计数意义下趋于独立均匀。即使相对位移的前两个坐标趋于相同，真实源相位仍因 \(AD\to\infty\) 混合。

## 6. 从 Fourier 收敛到全部格原点一致

对全库存计数，移动一个安排的格号至多改变两个格的单占贡献。将某一轴原点移动距离 \(h\)，只会改变该准确读数的小数部分位于宽度 \(h\) 的相应条带内的标签。单端相位均匀分布给该标签比例 \(h+o(1)\)，对条带原点统一。因此全库存唯一率关于三轴原点渐近等度连续。

对于近距计数，使用有限个带边距正规图覆盖。把每个源图的候选取为较大同一逆图内的全部标签；(9) 保证这在源图内等于近距检查。随后逐图应用加权单占计数的同一估计，边界窄带及未覆盖源的质量可任意小。这避免将一般近距关系误当作等价关系。

在紧原点环面上，零模式由 (15) 收敛，全部非零固定模式由第 5 节消失，再用 Fejér 逼近及渐近等度连续性，即得 (2) 的上确界结论。

对 \(\theta\to1\)，令 \(h=B-A\)。零和模式中 \(k_0\ne0\) 时主尺度仍为 \(\lambda_cz\)，\(k_0=0\) 时相位为 \(k_1\lambda_c[\mathcal G_c(s)-\mathcal G_c(z)]\)，主尺度为 \(L_chD\)。其余证明首末对称，端点交换的 Haar 不变性给同一个 \(F_0\)。

## 7. 使用方式、慢增长实例与限制

端点条件可写成

\[
\boxed{\ell\ll\theta\ll1},\qquad
\ell=\frac{\sqrt c}{B^{3/2}},
\tag{24}
\]

或原整数库存的 \(D\ll A\ll B\)。它把宏观逆支分辨率与位置趋端速度联系起来。

若 \(A\asymp c^\alpha\)、\(B\asymp c^\beta\)，一个充分参数区间是

\[
0<\alpha<\beta<1,\qquad 2\alpha+\beta>1.
\tag{25}
\]

不需要给内间距指定正的幂指数。取任意 \(h(c)\to\infty\)、\(h(c)^2=o(c)\)，令

\[
A=\lceil h(c)\rceil,\qquad B=\lfloor c/h(c)\rfloor.
\tag{26}
\]

则 \(D\sim\sqrt h\)、\(A/D\sim\sqrt h\to\infty\)、\(\theta\sim h^2/c\to0\)，定理 A 适用。例如 \(h(c)=\log\log c\)；也可以选择更慢的发散函数。

由于位数 \(p\) 是整数，机械舍入 \(p_*+\text{常数}\) 未必使 \(L_c\) 收敛。本定理还蕴含不要求倍率收敛的紧区间表述：若 \(0<L_-\le L_c\le L_+<\infty\)，则在同样的库存条件下

\[
\sup_\alpha |V_c^{(3)}(\alpha)-\Phi_0(L_c)|\to0.
\tag{27}
\]

证明是对子列选取 \(L_c\to L\)，应用 (2) 和 \(\Phi_0\) 的连续性。此处仍只控制固定紧倍率窗口，未给 \(L_c\to\infty\) 或 \(L_c\downarrow0\) 的任意联动速率。

本篇未证明 \(A/D\) 有界时整个库存的全竞争者极限，也未证明 (24) 的必要性；相位混合、局部格近似、宏观逆支消除是不同步骤。对于 \(A\asymp D\)，前两步已成立，第三步只留下有限二阶谱分辨率，需另研究跨逆支整数关系。

## 来源

- C82, enterprise-math@4628b5b87d2cf41a385228ad04bf163c06aa6586：CROSS_PHASE.md、LATTICE_LIMIT.md。
- C83, enterprise-math@20c3c2a6cb769a816cedf0ec04cf199149bfa86f：CRITICAL_TRANSITION.md，尤其近距计数的原点等度连续处理。
- C84, enterprise-math@01f50954ee37548372464c68a311f7df2dba0632：READING_POSITION.md，固定位置的有限差商与辅助函数定义。

新增部分为移动端点的条件、均匀有限差商处理、固定模式分流、全竞争者定理及任意慢内间距实例。证明依赖上述已建立的有限谱与 Haar 输入，不把数值抽样当作其替代。
