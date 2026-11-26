# 两个准确 Möbius 零矩：统一完整道路尾界与临界三厚度尺度

2026-11-26（Asia/Hong_Kong）。统一作者 EM-DIRECT-E7559A / TASK_RESEARCH，沿用 Activity RA-D2F111EA1C0D4B1DBEFBC1B4。本稿是作者解析证明，不是 independent Review 或 formal Result。

直接前驱为 Source `2049a0035e7c7cda98239f32a2bb573707f78e25` 的三厚度双校准和正输出 Green 对偶。P000 / Heartbeat X6 固定原生轴辅助标量观察的范围不变；完整整数、合数、单位、背景、前史和真实端点仍按原定义使用。

## 1. 这次真正改变的匹配条件

前驱以实际支撑的绝对值平均得到三厚度完整根支付

\[
O\bigl(\varepsilon^3\sqrt B(\log B)^4\bigr),
\]

所以取 \(\varepsilon_B\asymp B^{-r}\)、\(r>1/6\) 足够。本轮使用准确密度与道路线性常数校准产生的**两个 Möbius 零矩**，在同一个完整道路上证明更强的一致界：存在常数 \(C,c>0\)，对全部充分小的正 \(\varepsilon\) 及全部实 \(y\ge1\)，

\[
\boxed{|q_\varepsilon(y)-q^*(y)|
\le C\varepsilon^3 y\exp\{-c\sqrt{\log(e y)}\}.}\tag{1.1}
\]

可把 c 减小到 \(0<c<1\)。于是任意含真实端点的节点插值、任意同一合法树的全过程最大包络，都继承同一个点值界；闭窗口根支付满足

\[
\boxed{R_B\le C'\varepsilon^3\sqrt B
\exp\{-c\sqrt{\log(e B)}\}.}\tag{1.2}
\]

不再要求 \(\varepsilon\log B\le1\)。常数对一个固定小厚度邻域统一，但本稿不宣称已经数值化该邻域和 C。

因此临界有理族

\[
\boxed{\varepsilon_B=1/\lceil B^{1/6}\rceil}
\]

已使完整根匹配趋零。任意固定对数加宽 \(\varepsilon_B\asymp B^{-1/6}(\log B)^L\) 也允许。更一般地，本轮另一个分支证明三节点的精确功能性包络可由节点乘积 \(p=a_1a_2a_3\) 统一支付；本稿所有结论随之把 \(\varepsilon^3\) 换成 p，不依赖节点形状比或总权重变差。

这是匹配差的估计。参考道路的真实无界正能量或普通素数定向亏缺上界并未作为结论获得。

## 2. 唯一新增的外部算术输入

使用已证明的无条件 Möbius 消去估计：存在绝对常数 \(a,C_0>0\)，使

\[
\mathfrak M(x):=\sum_{n\le x}\mu(n)
\quad\text{满足}\quad
|\mathfrak M(x)|\le C_0 x e^{-a\sqrt{\log(e x)}}\qquad(x\ge1).
\tag{2.1}
\]

一份实际读取的 primary source 是 Ethan Simpson Lee 与 Nicol Leong，*New explicit bounds for Mertens function and the reciprocal of the Riemann zeta-function*，arXiv:2208.06141v5，Theorem 1.1、式(9)：

<https://arxiv.org/abs/2208.06141v5>

<https://arxiv.org/pdf/2208.06141v5>

该文给出 \(x\log x\,e^{-\eta\sqrt{\log x}}\) 型无条件显式界。在减小正指数常数后吸收 log 因子，并以有限初始范围的平凡界扩大 C，得到(2.1)。本稿仅使用这种存在常数的形式，未复制其数值门槛或依赖任何未验证 RH 假设。下面的两零矩传递、厚度统一性、凹幅度和节点返回均为本稿证明。

## 3. 一般的“两零矩 → 完整道路衰减”引理

令 \(F:[0,\infty)\to\mathbb R\) 为 C¹ 函数，F(0)=0。设某个固定整数 d、固定 K 以及参数尺度 P≥0 满足

\[
|F(t)|+|F'(t)|\le KP(1+t)^d\qquad(t\ge0).
\tag{3.1}
\]

定义

\[
\nu(n)=\mu(n)F(\log n),\qquad e=1*\nu,
\]

并假设两个准确条件收敛矩为零：

\[
\sum_{n\ge1}\frac{\nu(n)}n=0,
\qquad
\sum_{n\ge1}\frac{\nu(n)\log n}{n}=0.
\tag{3.2}
\]

### 定理 3.1

在(2.1)之下，存在只依赖于 a,C₀,d,K 的 C,c>0，使全部上述 F 和 P 一致满足

\[
E(x):=\sum_{n\le x}e_n
=O\bigl(Px e^{-c\sqrt{\log(e x)}}\bigr),
\tag{3.3}
\]

\[
\sum_{n\ge1}\frac{e_n}{n}=0,
\tag{3.4}
\]

以及完整道路恒等式和界

\[
\boxed{Q_F(y):=\sum_{n\le y}(y/n-1)e_n
=-y\int_y^\infty\frac{E(t)}{t^2}\,dt
=O\bigl(Py e^{-c\sqrt{\log(e y)}}\bigr).}\tag{3.5}
\]

各式中的 c 可以在需要时统一减小。P=0 时 F 和全部源均为零。

### 证明第一步：多项式权 Möbius 和

部分求和给

\[
N(x):=\sum_{n\le x}\nu(n)
=F(\log x)\mathfrak M(x)
-\int_1^x\mathfrak M(t)F'(\log t)\frac{dt}{t}.
\tag{3.6}
\]

在 \([1,\sqrt x]\) 用平凡界 \(|\mathfrak M(t)|\le t\)，所得为 \(O(P\sqrt x(1+\log x)^d)\)。在 \([\sqrt x,x]\) 用(2.1)；其指数因子至多 \(e^{-(a/\sqrt2)\sqrt{\log(e x)}}\)。将固定次数的对数吸收到较小正指数常数，得到

\[
N(x)=O\bigl(Px e^{-a_1\sqrt{\log(e x)}}\bigr)
\tag{3.7}
\]

且常数与 F、P 无关。x 的有限初始范围由扩大固定常数覆盖。

由(3.7)，\(\sum\nu(n)/n\) 和 \(\sum\nu(n)\log n/n\) 都条件收敛，并有例如

\[
\left|\sum_{n>D}\frac{\nu(n)}n\right|
\le\frac{|N(D)|}{D}+\int_D^\infty\frac{|N(t)|}{t^2}dt
\ll P e^{-a_2\sqrt{\log(e D)}}.
\tag{3.8}
\]

最后一个积分令 u=√log(et)，化为 \(2\int u e^{-a_1u}du\)；再减小指数常数即可。附带 log n 的尾项同理。

### 第二步：双曲线分割与第一个零矩

取实数 D=√x。准确有限恒等式为

\[
E(x)=\sum_{d\le D}\nu(d)\lfloor x/d\rfloor
+\sum_{m\le D}\{N(x/m)-N(D)\}.
\tag{3.9}
\]

第一个和等于

\[
x\sum_{d\le D}\frac{\nu(d)}d
+O\left(\sum_{d\le D}|\nu(d)|\right).
\]

利用第一个零矩、(3.8)和(3.1)，其绝对值至多

\[
O\bigl(Px e^{-a_2\sqrt{\log(e D)}}
+PD(1+\log D)^d\bigr).
\]

第二个和中 x/m≥√x；由(3.7)和 \(\sum_{m\le D}1/m\le1+\log D\)，同样得到 \(Px\) 乘一个下降的平方根指数，附带固定对数因子可吸收。这证明(3.3)。没有用绝对值把全部 d≤x 的取整余项直接相加。

### 第三步：第二个零矩与完整道路尾

令

\[
H(s)=\sum_{n\ge1}\nu(n)n^{-s}\qquad(\Re s>1).
\]

(3.7)使 H 及其一阶导数在实轴 s↓1 时连续。因此(3.2)等价于 H(1)=H′(1)=0，进而

\[
\lim_{\sigma\downarrow1}\zeta(\sigma)H(\sigma)=0.
\]

另一方面，\(\sum e_n n^{-s}=\zeta(s)H(s)\) 在 \(\Re s>1\) 绝对收敛；(3.3)又使 \(\sum e_n/n\) 条件收敛，且边界值与上述极限相同。所以(3.4)成立。这里仅需要 H 在实轴的一阶可微性，不把边界收敛误作整个左邻域的级数收敛。

现在从完整前缀出发，

\[
Q_F(y)=y\sum_{n\le y}\frac{e_n}{n}-E(y)
=-y\sum_{n>y}\frac{e_n}{n}-E(y).
\]

尾项的部分求和准确为

\[
\sum_{n>y}\frac{e_n}{n}
=-\frac{E(y)}y+\int_y^\infty\frac{E(t)}{t^2}dt.
\]

两个 E(y) 恰好消去，得到(3.5)的准确恒等式；再用(3.3)支付积分。此式对整数和非整数 y 均成立，源在端点 n=y 的核值为零。证明完成。

## 4. 准确双校准正好给出两个零矩

现在令 h(s)=1/ζ(s)。对任意准确质量一的有限正厚度实权族，定义

\[
F_{\boldsymbol a}(t)
=\sum_jw_j\frac{e^{-a_jt}-1}{a_j}+t.
\tag{4.1}
\]

完整源差准确为

\[
D_{\boldsymbol a}-\Lambda=1*\nu_{\boldsymbol a},
\qquad \nu_{\boldsymbol a}(n)=\mu(n)F_{\boldsymbol a}(\log n).
\tag{4.2}
\]

特别地 F(0)=0，单位值没有被改变。其 Dirichlet 因子为

\[
H_{\boldsymbol a}(s)
=\sum_jw_j\frac{h(s+a_j)-h(s)}{a_j}-h'(s).
\tag{4.3}
\]

利用 h(1)=0、h′(1)=1、h″(1)=−2γ，得到

\[
\boxed{H_{\boldsymbol a}(1)=d_{\boldsymbol a}-1,\qquad
C_{\boldsymbol a}=H'_{\boldsymbol a}(1)
+(\gamma-1)H_{\boldsymbol a}(1).}\tag{4.4}
\]

所以准确 d=1,C=0 等价于 H(1)=H′(1)=0，也正是(3.2)。这里第二个算术矩是 \(\sum\nu(n)\log n/n=-H'(1)\)，符号已保留。

### 等距三厚度的全参数包络

前驱给出 M₁,M₂=O(ε³)、a_j=jε、总变差有界。由负指数的 Taylor 积分余项，在全部 t≥0 上都有

\[
\left|F_\varepsilon(t)-\frac{M_1t^2}{2}
+\frac{M_2t^3}{6}\right|
\le\frac{\sum_j|w_j|a_j^3}{24}t^4.
\tag{4.5}
\]

对 t 导数同理，余项由 \((\sum|w_j|a_j^3)t^3/6\) 支付。因此

\[
|F_\varepsilon(t)|+|F'_\varepsilon(t)|
\ll\varepsilon^3(1+t)^4\qquad(t\ge0),
\tag{4.6}
\]

没有小量 εt≤1 的限制。应用定理3.1即得(1.1)。

### 任意小正三节点的乘积尺度

本轮第三阶源分支通过精确 Newton 差商证明：对所有不同的 \(0<a_1<a_2<a_3\le a_0\)，准确双校准唯一可解，并有

\[
|F_{\boldsymbol a}(t)|+|F'_{\boldsymbol a}(t)|
\le C(a_1a_2a_3)(1+t)^4.
\tag{4.7}
\]

常数不依赖节点间距和比值。把 P=p=a₁a₂a₃ 代入定理3.1，得到乘积版本的(1.1)—(1.2)。这是一条功能性稳定界；节点接近时实权本身及实现精度仍可能增长。

## 5. 凹幅度使任意真实插值与同树包络统一返回

缩小 c 到 0<c<1，令

\[
\Phi_c(y)=y\exp\{-c\sqrt{\log(e y)}\}\qquad(y\ge1).
\]

写 u=log(ey)≥1，直接微分可得

\[
\Phi_c''(y)
=-\frac{c e^{-c\sqrt u}}{4y u^{3/2}}
\bigl(2u-c\sqrt u-1\bigr)\le0.
\tag{5.1}
\]

若真节点误差满足 \(|e(x_i)|\le CP\Phi_c(x_i)\)，则每段非负重心组合给

\[
|I_\Pi e(y)|\le CP I_\Pi\Phi_c(y)\le CP\Phi_c(y).
\tag{5.2}
\]

同一合法插入树的每个阶段都有这个界；两个逐点最大包络之差也受同一界控制。节点和树可以按实际数据选择，结论仍然统一。

闭整数根预算可直接估计。对 1≤n≤B，

\[
\sqrt{\log(eB)}-\sqrt{\log(en)}
=\frac{\log(B/n)}{\sqrt{\log(eB)}+\sqrt{\log(en)}}
\le\tfrac12\log(B/n).
\]

所以

\[
\sum_{n=1}^B e^{-2c\sqrt{\log(en)}}
\le e^{-2c\sqrt{\log(eB)}}B^c\sum_{n=1}^Bn^{-c}
\le\frac{B}{1-c}e^{-2c\sqrt{\log(eB)}}.
\tag{5.3}
\]

于是任意闭子窗口 [A,B]、任意真端点网格和同树包络，统一根差均不超过

\[
\boxed{\frac{C}{\sqrt{1-c}}P\sqrt B
e^{-c\sqrt{\log(eB)}}.}\tag{5.4}
\]

该论证没有要求 A 与 B 保持固定比例，也没有遗漏小端点的插值影响。

## 6. 临界尺度、对数加宽与有理实现

对 a_j=jε，p=6ε³。取 ε_B=1/ceil(B^(1/6))，(5.4)趋零。固定任意 L≥0，若

\[
\varepsilon_B\asymp B^{-1/6}(\log B)^L,
\]

则根差为 \(O((\log B)^{3L}e^{-c\sqrt{\log(eB)}})\to0\)。对每个固定整数 L，可用 \(k_B=\max(1,\lfloor\log_2B\rfloor)\) 及最小正整数 N_B 满足 \(N_B^6k_B^{6L}\ge B\)，定义准确有理 ε_B=1/N_B；不需要用浮点近似判定六次根边界。

更一般地，只要 max a_j≤a₀ 且 \(p_B\sqrt B e^{-c\sqrt{\log(eB)}}\to0\)，就有完整匹配趋零。这里是充分条件，没有宣称其为所有厚度设计的必要边界。

准确双校准的实权与有理近似继续区分。对于上述固定形状临界族，取前两个权的有理近似，绝对误差各至多 2^(−P_B)，第三权由质量一决定；令 P_B=ceil(log₂B)，总系数误差 δ_B≤4/B。前驱完整正支撑估计给额外根差

\[
\delta_B S_Be^{3\varepsilon_BS_B}\sqrt B
=O((\log B)/\sqrt B)\to0.
\tag{6.1}
\]

因此有限有理实现同样具有完整窗口趋零匹配，但有理权的密度和 C 残差不宣称准确为零。若节点形状退化，权重的整数部分、节点分离度和求值精度另须计入；功能性乘积界不自动给统一位复杂度。

## 7. 与本轮 Green 算术目标接合

设 Π₀ 为真实粗网格，Π 为其整数细化，e=q_D−q*。把各单元残差拼接，有

\[
V_{\Pi,D}-V_{\Pi,\Lambda}=I_\Pi e-I_{\Pi_0}e.
\]

粗节点上的残差准确为零，闭单元重复端点不增加费用。因此正部1-Lipschitz给

\[
\boxed{|\mathcal E_\Pi(D)-\mathcal E_\Pi(\Lambda)|
\le\|I_\Pi e\|_w+\|I_{\Pi_0}e\|_w\le2R_B.}\tag{7.1}
\]

这项支付保留完整匹配误差的相关性，包含真实粗端点。临界 ε_B≈B^(−1/6) 时，逐源绝对包络的旧估计 η_B√B 可能只给 O(log⁴B)，但(7.1)仍趋零。后续普通素数归约可以先在参考源 Λ 上支付背景和高次幂，再用(7.1)返回实际道路；不必把逐源绝对包络趋零当作新的必要条件。

这改进的是匹配返回成本。对归一化凹 Green 测试证明真实普通素数质量下界，以及控制真实粗骨架自身，仍是未完成的算术工作。

## 8. 统一领先误差场

本轮第三阶源分支还证明，令 p=a₁a₂a₃、a_max=max a_j，在全 t≥0 上有

\[
F_{\boldsymbol a}(t)=pP(t)+O\bigl(pa_{\max}(1+t)^5\bigr),
\quad
F'_{\boldsymbol a}(t)=pP'(t)+O\bigl(pa_{\max}(1+t)^4\bigr),
\]

\[
P(t)=t^4/24-\lambda_2t^3/6+\lambda_1t^2/2.
\]

准确族与领先场各自具有两个零矩，因此差也具有两个零矩。对差应用定理3.1，得到全道路统一展开

\[
\boxed{q_{\boldsymbol a}(y)-q^*(y)
=pQ_S(y)+O\bigl(pa_{\max}y e^{-c\sqrt{\log(e y)}}\bigr).}\tag{8.1}
\]

Q_S 是与三节点形状无关的固定完整领先场；S=1*(μP(log))。当 a_max→0 时，这是比仅写三个点的实权渐近更强的全道路展开。相关差商定义、λ、支撑和四阶有限支付见第三阶源分支。这里的解析尾界与该分支的显式有限对数界可以分别用于合适场景，没有把未知常数的渐近式当成数值认证区间。

## 核对性质

本稿所有新结论由上述解析证明承担，不生成伪装成无限验证的有限证书。第三阶源作者已核对两零矩身份、全 t 包络和任意节点插值的凹幅度返回；Green 作者已核对(7.1)及粗端点费用。外部输入仅为(2.1)，已经实际读取 primary source；没有重跑前驱的 1,270 点或旧证书。
