# 完整道路的中心化尾通量、窗口 Gram 与多厚度转移代价

Date: 2026-11-21 (Asia/Hong_Kong)
Contribution: 同一主研究会话内的数学协作，供 EM-DIRECT-B5750A 接续；不是独立 Project Review。
Status: AUTHOR_DERIVED_EXACT_IDENTITIES_AND_CONDITIONAL_ENERGY_TRANSFERS
Task context: RS-RH-METHOD-TRANSFER-20261121
Scientific input: enterprise-math@9fc068244e4f1117f1e75df5eb0285c6697d21d7

本稿研究既有完整整数道路的算术观察量。厚度、积分变量、频率和窗口均为 X6 载体上既有道路观察的参数，不增加原生空间轴。每个有限观察范围内的全部整数及合数权重被保留。带符号和在平方之前完成；后文的范数上界是可选充分估计，不宣称被取绝对值的方向冗余。

## 1. 项目原对象及原点背景能量

沿用项目正本：

\[
R_a(n)=\prod_{p\mid n}(1-p^{-a}),\quad R_a(1)=1,\quad
c_a=\frac1{\zeta(1+a)},\quad S_a(t)=\sum_{n\le t}R_a(n),
\]

\[
E_a(t)=S_a(t)-c_at,\qquad E_0(t)=1_{[1,\infty)}(t).
\]

项目的原始完整道路能量是

\[
\mathcal Q_a=\int_0^\infty |E_a(t)-E_0(t)|^2\frac{dt}{t^2}.
\]

令

\[
U_a(t)=S_a(t)-1-c_at\quad(t\ge1),\qquad
q_a(Y)=\int_Y^\infty U_a(t)^2\frac{dt}{t^2}\quad(Y\ge1).
\]

由于在 \(0<t<1\) 上 \(E_a(t)-E_0(t)=-c_at\)，精确关系为

\[
\boxed{\mathcal Q_a=c_a^2+q_a(1).}
\]

不能在引用项目 \(\mathcal Q_a\) 时遗漏 \((0,1)\) 的背景能量。原正本已把 \(\mathcal Q_a=O(a)\) 作为 RH 等价条件；本稿对这个假设的使用只说明不同观察量之间的转移代价，不构成新的 RH 证明或更弱充分条件。

### 与前轮固定原点离散能量的直接比较

记

\[
B_{a,N}=S_a(N)-1-c_a(N+\tfrac12),\qquad
\mathcal D_a=\sum_{N\ge1}\frac{B_{a,N}^2}{N^2}.
\]

在 \([N,N+1)\) 上，\(U_a(t)=B_{a,N}+c_a(N+1/2-t)\)，故

\[
\int_N^{N+1}U_a(t)^2dt=B_{a,N}^2+\frac{c_a^2}{12}.
\]

以该格内的 \(t^{-2}\) 上下界相乘并求和，得到

\[
\boxed{
\frac{\mathcal D_a}{4}
\le q_a(1)
\le \mathcal D_a+\frac{c_a^2\zeta(2)}{12}.
}
\]

这里均允许能量为无穷。因 \(c_a=O(a)\)，两个接口的 \(O(a)\) 条件相互一致。这一步没有删除固定原点或其常数项。

## 2. 背景常数与精确尾积分

为避免与项目完成因子同名，用 \(\kappa_a\) 表示以下常数：

\[
\boxed{
\kappa_a:=\int_1^\infty U_a(t)t^{-2}dt
=(\gamma-1)c_a+c'_a-1,
\qquad
c'_a=-\frac{\zeta'(1+a)}{\zeta(1+a)^2}.
}
\]

这个一阶尾积分对每个 \(a>0\) 都绝对收敛；这里不要求平方能量 \(\mathcal Q_a\) 有限。

### 收敛与常数的证明

项目已有除数展开

\[
E_a(t)=-t\sum_{d>t}\frac{\mu(d)}{d^{1+a}}
-\sum_{d\le t}\frac{\mu(d)}{d^a}\{t/d\}.
\]

它给出 \(E_a(t)=O_a(t^{1-a})\) 当 \(0<a<1\)，\(O(\log t)\) 当 \(a=1\)，以及 \(O_a(1)\) 当 \(a>1\)。因此 \(E_at^{-2}\)、\(U_at^{-2}\) 均绝对可积。

对实数 \(s>1\)，已有 Abel 恒等式为

\[
\frac{\zeta(s)}{\zeta(s+a)}
=c_a\frac{s}{s-1}+s\int_1^\infty E_a(t)t^{-s-1}dt.
\]

写 \(s=1+\varepsilon\)，使用

\[
\zeta(1+\varepsilon)=\varepsilon^{-1}+\gamma+O(\varepsilon),
\qquad
\frac1{\zeta(1+a+\varepsilon)}=c_a+c'_a\varepsilon+O_a(\varepsilon^2),
\]

则

\[
\frac1s\frac{\zeta(s)}{\zeta(s+a)}
=\frac{c_a}{\varepsilon}+(\gamma-1)c_a+c'_a+O_a(\varepsilon).
\]

由上面的绝对可积控制取 \(\varepsilon\downarrow0\)，得
\(\int_1^\infty E_at^{-2}=(\gamma-1)c_a+c'_a\)。再减去 \(\int_1^\infty t^{-2}dt=1\)，即为所述 \(\kappa_a\)。特别注意 \(c'_a\) 前的正号及最后的 \(-1\)。□

令

\[
T_a(y)=\int_y^\infty U_a(t)t^{-2}dt,
\quad b_a=\frac{c_a}{a}-1,
\quad d_a=1+\gamma+\frac{\kappa_a}{a}.
\]

上一轮的平滑道路观察量于是具有精确分解

\[
\boxed{
\mathscr G_a(y)
=y\bigl(b_a\log y+d_a\bigr)-\frac yaT_a(y).
}
\]

因为 \(c_a=a-\gamma a^2+O(a^3)\)，有

\[
\kappa_a=-(1+\gamma)a+O(a^2),\qquad b_a=O(a),\qquad d_a=O(a).
\]

这些漂移项和尾通量共同构成同一个观察量；分别估计它们时应记清各自的损失。

## 3. 尾通量的有限观察表达

对每个有限 \(z\ge1\)，逐项有限积分给出

\[
I_a(z):=\int_1^z U_a(t)t^{-2}dt
=\sum_{2\le n\le z}R_a(n)\left(\frac1n-\frac1z\right)-c_a\log z.
\]

因此

\[
\boxed{
T_a(z)=\kappa_a-I_a(z).
}
\]

给定确定性背景常数 \(c_a,c'_a\)，这个边界尾通量只需 \(n\le z\) 的有限完整道路和即可计算。这里没有假定二次全尾有限，也没有把背景常数视为免费提供的有限整数证书；它们仍按上述 zeta 定义及其可核对精度使用。

对完整窗口 \([Y,Z]\)，有

\[
\boxed{
T_a(y)=T_a(Z)+\int_y^Z U_a(t)t^{-2}dt
\quad(Y\le y\le Z).
}
\]

这使窗口内的观察量可以由两种信息组成：窗口内部的完整道路残差，以及右端的一个带符号通量。原点和早期道路的信息进入 \(T_a(Z)\)，并未消失。

## 4. 多厚度组合及不可遗漏的常数端口

固定整数 \(m\ge1\)、\(h>0\)，定义

\[
w_j=(-1)^{j+1}\binom mj\quad(1\le j\le m),
\qquad
\mathscr G_{m,h}=\sum_{j=1}^m w_j\mathscr G_{jh}.
\]

这是另一份协作稿中的 \(m\) 阶前向厚度导数观察量。满足

\[
\sum_{j=1}^m w_j=1,
\quad \sum_{j=1}^m w_jj^k=0\ (1\le k<m),
\quad \sum_{j=1}^m\frac{w_j}{j}=H_m.
\]

最后一个等式中的 \(H_m=\sum_{j=1}^m1/j\) 表明，组合尾残差的常数端口必须保留：

\[
V_{m,h}(t):=\sum_{j=1}^m\frac{w_j}{j}U_{jh}(t)
=\sum_{j=1}^m\frac{w_j}{j}S_{jh}(t)-H_m
-t\sum_{j=1}^m\frac{w_j}{j}c_{jh}.
\]

令

\[
T_{m,h}(y)=\int_y^\infty V_{m,h}(t)t^{-2}dt,
\quad b_{m,h}=\sum_jw_jb_{jh},\quad d_{m,h}=\sum_jw_jd_{jh}.
\]

精确分解为

\[
\boxed{
\mathscr G_{m,h}(y)
=y\bigl(b_{m,h}\log y+d_{m,h}\bigr)-\frac yhT_{m,h}(y).
}
\]

其中 \(T_{m,h}(Z)=\sum_j(w_j/j)[\kappa_{jh}-I_{jh}(Z)]\) 具有上一节的有限观察表达。该公式保留跨厚度的全部符号和交叉项；它没有把不同厚度的道路当作彼此独立的随机量。

### 背景漂移的高阶抵消

\(b_a,d_a\) 在 \(a=0\) 处具有可去奇点，解析延拓满足 \(b_0=d_0=0\)。固定一个小的 \(r>0\)，并令 \(mh\le r\)。对 \(f=b\) 或 \(d\)，有限差分的积分表示给出

\[
\sum_{j=1}^m w_jf(jh)
=(-1)^{m+1}
\int_{[0,h]^m}f^{(m)}(u_1+\cdots+u_m)\,du_1\cdots du_m.
\]

故若 \(M_{f,m}=\sup_{0\le a\le r}|f^{(m)}(a)|\)，则

\[
\boxed{|b_{m,h}|\le M_{b,m}h^m,\qquad
|d_{m,h}|\le M_{d,m}h^m.}
\]

这是先完成带符号组合后得到的 \(m\) 阶抵消。对每个单厚度漂移先取绝对值，只能保留通常的一阶界，不能再声称上述高阶收益。

## 5. 加权 Hardy 转移：常数在 \(\theta=1/2\) 附近保持有限

令 \(0<\theta<1\)，\(V\) 为实可测函数。只要右边有限，就有

\[
\boxed{
\int_Y^\infty y^{1-2\theta}
\left(\int_y^\infty\frac{V(t)}{t^2}dt\right)^2dy
\le \frac1{(1-\theta)^2}
\int_Y^\infty V(t)^2t^{-2\theta-1}dt.
}
\]

证明：置 \(y=e^x,t=e^v\)，\(F(v)=V(e^v)e^{-\theta v}\)。左边是

\[
\left\|\int_0^\infty e^{-(1-\theta)u}F(x+u)du\right\|^2_{L^2(x\ge\log Y)}.
\]

先把 \(F\) 在 \(x<\log Y\) 延为零，再用卷积的 \(L^1\)-\(L^2\) 不等式。核的 \(L^1\) 范数为 \(1/(1-\theta)\)，即得结论。□

相同证明对截断算子 \(\int_y^ZV(t)t^{-2}dt\) 给出

\[
\int_Y^Z y^{1-2\theta}
\left(\int_y^ZV(t)t^{-2}dt\right)^2dy
\le \frac1{(1-\theta)^2}\int_Y^ZV(t)^2t^{-2\theta-1}dt.
\]

这个有限窗口版本不要求全尾平方可积。它的常数在 \(\theta\downarrow1/2\) 时趋于 \(4\)，避免了逐点 Cauchy–Schwarz 再积分所得 \(1/(2\theta-1)\) 的常数发散。

## 6. 有限窗口的精确 Gram 核与边界交叉项

固定 \(Y<Z\)、\(0<\theta<1\)，令

\[
A_\theta(Y,t)=\frac{t^{2-2\theta}-Y^{2-2\theta}}{2-2\theta},
\qquad
\mathcal K_{\theta;Y,Z}(u,v)
=\frac{A_\theta(Y,\min(u,v))}{u^2v^2}.
\]

设 \(\tau=T_{m,h}(Z)\)、\(V=V_{m,h}\)。Fubini 在有限窗口上给出精确恒等式

\[
\begin{aligned}
\int_Y^Zy^{1-2\theta}
\left(\tau+\int_y^Z\frac{V(t)}{t^2}dt\right)^2dy
={}&\tau^2A_\theta(Y,Z)\\
&+2\tau\int_Y^Z\frac{V(t)}{t^2}A_\theta(Y,t)dt\\
&+\int_Y^Z\int_Y^Z V(u)V(v)
\mathcal K_{\theta;Y,Z}(u,v)\,du\,dv.
\end{aligned}
\]

核本身为 Gram 核，因为

\[
\mathcal K(u,v)=\int_Y^Z y^{1-2\theta}
\frac{1_{y\le u}}{u^2}\frac{1_{y\le v}}{v^2}dy.
\]

上述三项保留边界通量、窗口内相关性和二者的精确交叉项。若需要易计算的充分上界，记

\[
L_{m,h,\theta}(Y,Z)=\int_Y^Z V_{m,h}(t)^2t^{-2\theta-1}dt,
\]

则

\[
\left\|\frac yhT_{m,h}(y)\right\|_{L^2([Y,Z],y^{-2\theta-1}dy)}
\le\frac1h\left[
\frac{\sqrt{L_{m,h,\theta}(Y,Z)}}{1-\theta}
+|T_{m,h}(Z)|\sqrt{A_\theta(Y,Z)}\right].
\]

加上可显式计算的漂移范数，即可控制 \(\mathscr G_{m,h}\) 的整个平方能量，从而控制它的正部能量。使用这个三角上界可能失去有益交叉抵消；精确 Gram 式仍可使用。

特别地，在完整幂窗口 \(Z=Y^\lambda\) 与下节厚度下，若能在任意远窗口证明

\[
\boxed{
\frac1{h_Y^2}
\left[L_{m,h_Y,\theta}(Y,Y^\lambda)
+A_\theta(Y,Y^\lambda)T_{m,h_Y}(Y^\lambda)^2\right]
\le Y^{o(1)},
}
\]

则上一轮所需的正部窗口能量条件成立。这里 \(Y^{o(1)}\) 的确切含义是固定 \(m,\theta,\lambda\) 后，对每个 \(\alpha>0\)、每个起始阈值，存在更远窗口使左侧不超过 \(Y^\alpha\)。转移到给定能量指数 \(\eta>0\) 时，先取假设中的 \(\alpha=\eta/2\)，再提高窗口起点以吸收固定常数。这是一个明确但尚未证明的局部能量—边界通量充分条件。单个有限窗口通过该检查不证明无限窗口量词。

## 7. 原始 \(O(a)\) 能量假设与外推阶数的实际代价

本节用于核对接口损失，条件本身仍是项目已知的 RH 等价强假设。假设存在 \(C,r>0\)，使

\[
\mathcal Q_a\le Ca\qquad(0<a\le r).
\]

固定 \(m\)，令 \(mh\le r\) 并定义

\[
\mathfrak A_m=\sum_{j=1}^m\frac{\binom mj}{\sqrt j}.
\]

由 Minkowski 及 \(q_{jh}(1)\le\mathcal Q_{jh}\)，

\[
\left(\int_1^\infty V_{m,h}(t)^2t^{-2}dt\right)^{1/2}
\le\sqrt{Ch}\,\mathfrak A_m.
\]

对 \(1/2\le\theta<1\)，加权 Hardy 于是给出

\[
\boxed{
\int_Y^{Y^\lambda}
\left(\frac yhT_{m,h}(y)\right)^2y^{-2\theta-1}dy
\le\frac{C\mathfrak A_m^2}{h(1-\theta)^2}Y^{1-2\theta}.
}
\]

这一步的 \(1/h\) 代价没有被隐藏。

### 与多厚度窗口误差的联动

另一份协作稿证明了

\[
|\mathscr G_{m,h}(y)-G(y)|
\le\frac{h^m}{m+1}y(\log y)^{m+2}.
\]

因此对固定 \(m,\theta,\lambda\)，选

\[
\boxed{
h_Y=\left(\frac{m+1}{2}\right)^{1/m}
\frac{Y^{-\lambda(1-\theta)/m}}
{(\lambda\log Y)^{1+2/m}}.
}
\]

在全部充分大 \(Y\) 上，\(mh_Y\le r\)，并且整个窗口满足
\(|\mathscr G_{m,h_Y}-G|\le y^\theta/2\)。窗口内的 \(m\) 个厚度固定为 \(h_Y,2h_Y,\dots,mh_Y\)。

记 \(L=\lambda\log Y\)、\(Z=Y^\lambda\)。漂移范数有明确界

\[
\begin{aligned}
\mathcal B_{m,h_Y}
&:=\left(\int_Y^Zy^{1-2\theta}
(b_{m,h_Y}\log y+d_{m,h_Y})^2dy\right)^{1/2}\\
&\le \frac{m+1}{2\sqrt{2(1-\theta)}}
\frac{M_{b,m}L+M_{d,m}}{L^{m+2}},
\end{aligned}
\]

故漂移的窗口能量为 \(O_m(L^{-2m-2})\)。与尾项相合，得到

\[
\boxed{
\int_Y^{Y^\lambda}(\mathscr G_{m,h_Y}(y)_+)^2y^{-2\theta-1}dy
\ll_{m,\theta,\lambda,C}
Y^{\,1-2\theta+\lambda(1-\theta)/m}
(\log Y)^{1+2/m}
+(\log Y)^{-2m-2}.
}
\]

因此当

\[
\boxed{\theta\ge\frac{m+\lambda}{2m+\lambda}}
\]

时，固定 \(m\) 的这条转移路线给出所需次幂窗口能量。以实际外部主路的 \(\lambda=3/2\) 为例：

| 外推阶数 \(m\) | 该估计覆盖的 \(\theta\) 下界 |
|---:|---:|
| 1 | \(5/7\) |
| 2 | \(7/11\) |
| 3 | \(3/5\) |
| 4 | \(11/19\) |

对任意固定 \(\theta>1/2\)，可选有限

\[
m\ge\frac{\lambda(1-\theta)}{2\theta-1}
\]

使条件成立。这解释了高阶厚度观察怎样修复一阶转移中的尺度损失。它没有证明所假设的 \(\mathcal Q_a=O(a)\)，也不把这条已有 RH 等价条件包装成新的无条件结论。

阶数成本也必须保留：

\[
\frac{2^m-1}{\sqrt m}\le\mathfrak A_m\le2^m-1.
\]

因此上面的常数可能随 \(m\) 指数增长。论证始终先固定 \(m\)，再令窗口远移；没有把固定阶估计自动推广为 \(m=m(Y)\) 的统一界。

## 8. 本轮可直接接手的数学目标

1. 保留 \(V_{m,h}\) 的跨厚度交叉能量，尝试直接估计其窗口内核形式及右端通量，避免先用 Minkowski 消去这些相关性。
2. 研究第 6 节有限窗口条件的任意远窗口量词。其对象为完整道路观察，不先假定全局 \(\mathcal Q_a=O(a)\)。
3. 若使用整个全尾，针对 \(q_{m,h}(Y)=\int_Y^\infty V_{m,h}^2t^{-2}dt\) 证明有尺度信息的界；Hardy 给出的显式代价为 \(Y^{1-2\theta}q_{m,h}(Y)/h^2\)。

这些目标仍未证明。上述恒等式、局部 Gram 和漂移抵消为已给出的作者推导；正式独立审阅仍由对应流程判断。

## 9. 计算与来源

`verify_tail_window.py` / `tail_window_results.json` 使用 80 位 mpmath，检查：Laurent 常数；带无条件显式余界的有限一阶尾；单位格连续/离散能量比较；多厚度尾分解；有限窗口 Gram 的边界交叉项及 Hardy 上界；固定阶漂移的数值阶数。未使用区间算术，未从有限样本推断 RH 或全尾能量界。

项目来源：

- [正道路能量正本](https://github.com/awdawmip/enterprise-math/blob/9fc068244e4f1117f1e75df5eb0285c6697d21d7/research_notes/COMPOSITE_ROAD_RH_PURE_POSITIVE_ENERGY_20260906.md)：\(\mathcal Q_a\)、有限全道路 Green 能量及其既有 RH 等价状态。
- [既有道路 jet 与 Abel 表示](https://github.com/awdawmip/enterprise-math/blob/9fc068244e4f1117f1e75df5eb0285c6697d21d7/research_notes/COMPOSITE_ROAD_RH_PENETRATION_JET_HIERARCHY_20260906.md)：\(R'_0=\Lambda\)、除数展开及绝对收敛域。
- [上一轮完整窗口桥](https://github.com/awdawmip/enterprise-math/blob/d020e8a51defa2a0e45cd8a9150330805627155c/research_notes/portable_direct/rh_method_transfer_20261121_b5750a/FULL_ROAD_WINDOW_BRIDGE.md)：\(\mathscr G_a\)、固定 \(G\) 的窗口转移及未证能量目标。
- [上一轮固定原点核与端口](https://github.com/awdawmip/enterprise-math/blob/d020e8a51defa2a0e45cd8a9150330805627155c/research_notes/portable_direct/rh_method_transfer_20261121_b5750a/ANCHORED_KERNEL_AND_PORTS.md)：离散 \(\mathcal D_a\) 接口和相位、常数端口保留。

本轮多厚度差分误差引用同一协作批次的 `rh_continuation_multithickness/NOTES.md`，其最终发布路径由主会话统一绑定。标准 Abel、Taylor、Hardy 和 Gram 运算不主张为新发现；新增贡献是它们在上述道路对象与实际窗口接口中的精确组合及代价核对。
