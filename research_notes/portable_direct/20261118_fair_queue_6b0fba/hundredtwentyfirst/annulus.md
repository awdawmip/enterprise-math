# 在有限环带中测出合数道路的能量指数

固定 \(0\le v_1<v_2\)，只读 \(e^{v_1/a}\le n<e^{v_2/a}\) 内的原整数道路。令 \(\Theta=\sup_{\zeta(\rho)=0,\,0<\Re\rho<1}\Re\rho\)。当厚度 \(a\downarrow0\) 时，此有限环带的能量 \(D_a\) 满足无条件公式
\[
             \boxed{\displaystyle\lim_{a\downarrow0}a\log D_a=(2\Theta-1)v_2.}       \tag{1}
\]
若 RH 成立，已知该能量与 \(a\) 之比趋向一个正的有限常数。若 RH 不成立，在任意这样一个有限环带中能量都呈指数增长。更窄的结论也成立：对固定 \(v,\ell>0\)，只读 \(e^{v/a}\le n<e^{v/a+\ell}\)，无条件有
\[
      \lim_{a\downarrow0}a\log(1+D_a)=(2\Theta-1)v .                      \tag{2}
\]
在非 RH 分支，(2) 中可以去掉 \(1+\)。同样两式均适用于连续原道路。因而仅凭**一对预先固定的正数** \((v,\ell)\) 的原中点观测，右端指数是否为零就等价于 RH。这个等价式没有确定指数的值。

本研究对应 RS-RH-COMPOSITE-ROAD-ESCAPING-TAIL，使用原题允许的截断障碍。其登记前置 BASELINE-AUDIT 的科学审计见第24轮，正式验收仍待登记。第92轮确定了 RH 分支的指数窗轮廓，并从非 RH 时总能量无限推出每个无上限尾的结论。那里明确留下的缺口是指定的**有限**环带。以下比较的每一个上限都有限。[原始任务书](https://github.com/awdawmip/enterprise-math/blob/c0f816e2ab6be0145a3edd1a77488bddfd42a2f6/research_tasks/RS-RH-COMPOSITE-ROAD-ESCAPING-TAIL_20260909.md) · [第24轮基线](../twentyfourth/energy.md) · [第92轮极限律](../ninetysecond/zeros.md)

## 一、原始整数与一个上界

保留全部整数的原权重 \(R_a(n)=\prod_{p\mid n}(1-p^{-a})\)，写 \(S_a(x)=\sum_{n\le x}R_a(n)\)，\(c_a=1/\zeta(1+a)\)。在 \(x\ge1\) 令 \(E_a(x)=S_a(x)-1-c_ax\)，并设 \(B_{a,n}=S_a(n)-1-c_a(n+1/2)\)。上式中的 \(D_a\) 是给定窗口内 \(\sum B_{a,n}^2/n^2\)，端点用上取整得到左闭右开整数窗。连续量为 \(Q_a[X,Y]=\int_X^Y |E_a(x)|^2dx/x^2\)。

令 \(f_a(t)=\mathbf1_{t\ge0}E_a(e^t)\)。在 \(\Re s>1\) 它的双边 Laplace 变换由原正权 Euler 乘积直接给出
\[
 G_a(s)=\frac1s\left(\frac{\zeta(s)}{\zeta(s+a)}-1\right)-\frac{c_a}{s-1}.  \tag{3}
\]
\(s=1\) 的极点恰由背景校正消去。对完整单位格，去掉变权之前有 \(\int_n^{n+1}E_a(x)^2dx=B_{a,n}^2+c_a^2/12\)。因此 \(Q_a[M,H]\) 介于
\[
 \frac{M^2}{(M+1)^2}\sum_{M\le n<H}\frac{B_{a,n}^2+c_a^2/12}{n^2}
 \quad\text{与}\quad
 \sum_{M\le n<H}\frac{B_{a,n}^2+c_a^2/12}{n^2}
 \tag{4}
\]
之间。全体格内方差的总费用至多 \(\zeta(2)c_a^2/12=O(a^2)\)。

若 \(\Theta<1\)，固定 \(\Theta<\sigma<1\)。在 \(\sigma\le\Re s\le2\) 的大高度处，经典的无零点半平面估计给 \(\zeta(s),1/\zeta(s)\ll_{\sigma,\epsilon}(2+|\Im s|)^\epsilon\)。简证是在 \(2+it\) 为中心、外缘严格位于 \(\Re s>\Theta\) 的圆盘取解析 \(\log\zeta\)。多项式增长和 Borel–Carathéodory 定理在略小圆盘给 \(O_\sigma(\log |t|)\)，半径 \(1/2\) 的内盘由绝对收敛给 \(O(1)\)。在覆盖所需点的中间圆盘应用三圆定理，得到 \(O_\sigma((\log |t|)^\kappa)\)，其中 \(\kappa<1\)。对所有足够小的 \(a>0\)，这使 \(G_a(\sigma+it)\) 的平方积分一致有界；低高度用 \(\sigma+a<1\) 留出固定余量。与紧支光滑测试配对，将 (3) 从 \(\Re s=2\) 移到 \(\sigma\) 后由 Plancherel 得
\[
        \int_0^\infty |E_a(e^t)|^2e^{-2\sigma t}dt\ll_\sigma1.
\]
从而 \(Q_a[1,Y]\ll_\sigma Y^{2\sigma-1}\)。若 \(\Theta=1\)，由 \(0\le R_a(n)\le1\) 直接得 \(Q_a[1,Y]\ll Y\)。结合 (4)，两种窗口均得到 (1)、(2) 所需的指数上界。允许 \(\Theta\) 只是上确界。

## 二、在任意给定长度内消去其他右半零点

以下假设有零点 \(\rho_*\) 满足 \(\beta_*=\Re\rho_*>1/2\)，记其重数为 \(m\)，并固定 \(1/2<\sigma_1<\sigma_2<\beta_*\)。给定任意 \(b>0\)，可取 \(w\in C_c^\infty((-b,b);\mathbf C)\)，其变换 \(W(s)=\int w(v)e^{sv}dv\) 有如下性质：\(W(\rho_*)\ne0\)；每个其他 \(\Re\rho>\sigma_1\) 的零点均按**至少原重数**消去；在固定竖条上 \(W(s)/\zeta(s)\) 除目标极点外，在 \(\Re s\ge\sigma_2\) 的大高度一致快降。

这一步沿用 Stechkin–Popov 在固定短窗中抽取指定零点的思想。本题的分母为 \(\zeta(s+a)\)，高零点处须保留所有消元重数，且余估计须对厚度一致。Ingham 的密度界 \(N(\sigma_1,T)\ll T^{3(1-\sigma_1)/(2-\sigma_1)}\log^5(2T)\) 对此给出某个严格小于一的幂。取 \(\kappa<\kappa'<\eta<1\)，使上述计数含重数为 \(O(T^\kappa)\)。设
\[
 P(s)=\prod_{\Re\rho>\sigma_1,\,\rho\ne\rho_*}(1-s/\rho)^{m_\rho},
 \qquad
 W(s)=P(s)\prod_{j\ge1}
   \frac{\sinh(\epsilon_j(s-\rho_*))}{\epsilon_j(s-\rho_*)},
 \qquad\epsilon_j=c j^{-1/\eta},\quad\sum_j\epsilon_j<b.
\]
此处 \(P\) 按互异零点取积。分部求和得 \(\sum m_\rho/|\rho|<\infty\) 及 \(\log^+|P(s)|\ll1+|s|^{\kappa'}\)。每个双曲正弦因子的模至多 \(e^{|\Re z|}\min(1,1/|z|)\)，其中 \(z=\epsilon_j(s-\rho_*)\)。在 \(|z|\ge2\) 的前 \(\gg |s|^\eta\) 个因子上各得至少因子 \(1/2\) 的节省。由此 \(W\) 受 \(C\exp((\sum\epsilon_j)|\Re s|-c'|s|^\eta)\) 控制；Paley–Wiener 定理给出上述紧支撑光滑函数，且 \(W(\rho_*)=P(\rho_*)\ne0\)。

为说明除以 \(\zeta\) 后的衰减，取 \(2d<\sigma_2-\sigma_1\)。以条带内大高度 \(s\) 为中心，在 \([d,2d]\) 中选取一条距每个非平凡零点 \(\gg_d1/\log|t|\) 的圆周，可由单位高度箱零点数 \(O(\log|t|)\) 排除坏半径。圆周上 \(1/|\zeta|\le\exp(O_d(\log|t|\log\log|t|))\)。其经典局部估计来自 \(\zeta'/\zeta(z)=\sum_{|\gamma-\Im z|\le1}(z-\rho)^{-1}+O(\log |t|)\) 在 \(-1\le\Re z\le2\) 的公式，取实部从 \(2+i\Im z\) 水平积分，取极限避开穿过零点的线；更右用绝对收敛。圆内所有分母零点在大高度都已消去，最大模原理把 \(\exp(-c''|t|^\eta)\) 的上界传回中心。这一证明也给出有界竖条中所需的一致性。[Stechkin–Popov §4，式 (38.4)–(42.4)](https://www.mathnet.ru/links/da3f9b538a05557efb87b2d923fa2e71/rm1018_eng.pdf) · [第78轮的单次零矩及使用范围](../seventyeighth/edge.md)

## 三、随厚度平移的极点与短窗

考察同一实际道路的线性读数
\[
 J_a(t)=\int w(v)e^{av} f_a(t+v)dv .
\]
这里 \(e^{av}\) 保证 Mellin 端乘上 \(W(s+a)\)。将 \(G_a(s)W(s+a)e^{st}\) 从 \(\Re s=2\) 移到 \(\sigma_2\)。上节的除零估计及 \(\zeta(s)\) 多项式增长使水平边贡献趋零；新直线的积分为 \(O(e^{\sigma_2t})\)，隐常数在所有足够小的 \(a\) 上一致。紧高度的移动目标与新线有固定距离。在两直线之间，唯一留下的极点为 \(s=\rho_*-a\)。目标附近写 \(\zeta(z)=(z-\rho_*)^m U(z)\) 且 \(U(\rho_*)\ne0\)。缩小 \(a\) 可保证分子在移动极点不为零。设
\[
 A_a(z)=\frac{W(\rho_*+z)U(\rho_*+z-a)}
                   {(\rho_*-a+z)U(\rho_*+z)}, \qquad A_0(0)=W(\rho_*)/\rho_* .
\]
对 \(0\le j\le m-1\) 其 Taylor 系数一致有界。以 \(z=s-\rho_*+a\) 展开 \((1-a/z)^m\)，得精确形式
\[
 J_a(t)=e^{(\rho_*-a)t}\,aP_a(at)+O(e^{\sigma_2t}),\qquad
 P_a(y)=\sum_{j=1}^{m}{m\choose j}(-1)^j
 \sum_{k=0}^{j-1} a^{j-1-k}[z^{j-1-k}]A_a(z)\,y^k/k!.
 \tag{5}
\]
\(P_a\) 的次数为 \(m-1\)，其系数逐项趋向 \(-A_0(0)L_{m-1}^{(1)}(y)\)，这里
\(L_{m-1}^{(1)}(y)=\sum_{k=0}^{m-1}(-1)^k{m\choose k+1}y^k/k!\)。
固定 \(v>0\) 与 \(\ell>0\)，取 \(b<\ell/8\)，在 \(t=v/a+\ell/4\) 与 \(t'=v/a+3\ell/4\) 各读一次。若 \(L_{m-1}^{(1)}(v)\ne0\)，小 \(a\) 时两次的 \(|P_a|\) 都有正下界。若它为零，该根必为单根：Laguerre 微分方程 \(yL''+(2-y)L'+(m-1)L=0\) 在 \(v>0\) 正则，\(L,L'\) 同时消失将给零解。因此
\[
 P_a(at')-P_a(at)=a(\ell/2)\big[-A_0(0)(L_{m-1}^{(1)})'(v)+o(1)\big].
\]
至少一个 \(|P_a|\gg a\)。两次都在指定短窗内留出端点余量。由 (5) 及 Cauchy–Schwarz，所取任一足够小的 \(a\) 在短窗内便有
\[
 \int_{v/a}^{v/a+\ell}|E_a(e^u)|^2 e^{-u}du
     \gg_{v,\ell,\rho_*} a^4 e^{(2\beta_*-1)v/a}.                          \tag{6}
\]
若该 Laguerre 值不为零，可将 \(a^4\) 换为 \(a^2\)。指数误差 \(e^{\sigma_2t}\) 已由 \(\beta_*>\sigma_2\) 吸收，常数包括 \(e^{-2v}\)。读数 \(w\) 可为复值，因而下界没有随 \(a\) 变化的余弦相位消失问题。全文只用此读数给原正能量作对偶下界，无须把它加入原始计算协议。

整数端的 (6) 取同一对内部读数，\(a\) 足够小时其支撑也在实际从 \(\lceil e^{v/a}\rceil\) 到 \(\lceil e^{v/a+\ell}\rceil\) 的完整单位格内。由 (4) 去掉 \(O(a^2)\) 的格内方差，指数下界保持。令固定零点的实部任意接近 \(\Theta\)，得到 (2) 的非 RH 分支。在宏观环带内部固定任意 \(v_1<v<v_2\)，\(v>0\)，包含对应固定对数宽度的窗口；令 \(v\uparrow v_2\) 即得 (1) 的非 RH 分支。若 RH 成立，第92轮给出宏观环带能量除以 \(a\) 的极限 \(\int_{v_1}^{v_2}W_{92}(y)dy>0\)，这处理 (1)。对 (2)，用第一节上界及 \(\log(1+D_a)\ge0\) 即可；在 RH 分支我们没有求出固定对数宽度内的能量等价式。

同样，第92轮已核高度内的简单零点给出 \(\lambda_{\rm low}>0.02309570896296\)。将两个分支合并，获得一个真正只读有限前缀的无条件下界
\[
 \liminf_{a\downarrow0}\frac{D_a}{a}\ \ge 0.02309570896296\,(e^{-2v_1}-e^{-2v_2}) .
\]
固定宏观环带对每个厚度都是有限的。本文没有给出该渐近式的有效起算厚度；消元器依赖假定存在的固定右半零点及其余高零点，不能用现有有限零点表代替。

## 四、复算

运行 `python annulus_check.py` 需 Python 包 `python-flint==0.9.0`。程序用原始素因子权重与独立的 Möbius 除数权计算指定固定对数宽度的有限环带，复核带中心背景的 Green 双和与逐格积分并给出定向舍入上下界。它还在真正的第一非平凡零点处用 Arb 检验原 ζ 商的移位留数，并用精确有理系数比较 (5) 的两种算法、显示一个重数二的主项消失与第二次读数。该重根示例检验移动留数的代数，不作为任何 ζ 重根或右半零点的实测。[复算程序](annulus_check.py) · [有限证书](annulus_checked.json)

取 \(v=1/4,\ell=1/2\)。厚度 \(a=1/8,1/16,1/24,1/32\) 对应的左闭右开整数端点分别为 \([8,13),[55,91),[404,666),[2981,4915)\)。四窗真实 \(D_a/a\) 的近似值依次是 0.020882815、0.002229226、0.000733185、0.000442096。末窗 Green 三个原项的绝对和与相消净值之比超过 526,896，192 位区间运算仍使实际连续能量半径小于 \(2^{-130}\)。这些有限读数不检测 RH。程序按 SHA-256 锁定[第92轮原权有限求和器](../ninetysecond/zeros_check.py)，另独立完成 144 次全有理移动留数比较。对于合成双极点 \(P_a(y)=y-2\)，\(t=2/a\) 的首读精确为零，\(t=2/a+1/4\) 的第二读去指数后精确为 \(a^2/4\)，说明 (6) 中保留第二个读数的原因。
