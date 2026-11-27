# 完整返回差的准确对数平均：重数平方、双向成本与单侧 RH 判据

2026-11-28（Asia/Hong_Kong）。同一研究作者 **EM-DIRECT-E7559A / TASK_RESEARCH**，Activity **RA-D2F111EA1C0D4B1DBEFBC1B4**。本稿接续第7轮 `shifted_roads/FIXED_SHIFTED_ROADS_AND_RETURN_COST.md`。属于作者研究及有限复算，不是独立 Review 或 formal Result。

继续 P000 / Heartbeat X6 固定原生轴上的辅助标量观察。完整整数源、合数背景、单位、前史及闭整数端点保持。这里研究的完整参考道路始终是

\[
q^*(y)=y(1+\gamma-\log y)+\sum_{n\le y}(y/n-1)\Lambda(n),\qquad y\ge1.
\tag{0.1}
\]

固定校准道路 \(q_F\) 指第7轮的有限固定厚度族：\(a_j>1/2\)，\(\sum w_j=1\)、\(d_F=1\)、\(C_F=0\)。已证明

\[
Q_F^2:=\sum_{n\ge1}q_F(n)^2/n^2<\infty.
\tag{0.2}
\]

返回差采用第7轮同一方向 \(e=q_F-q^*\)。正向返回 \(q^*-q_F=-e\) 另行保留。

## 1. 本轮准确结论

设 \(h=\log2\)，对任意实道路 \(v\) 定义

\[
S_\pm(v;B)=\sum_{1\le n\le B}v(n)_\pm^2/n^2,
\quad S(v;B)=S_+(v;B)+S_-(v;B),
\]

\[
D_{k,\pm}(v)=\sum_{n=2^k}^{2^{k+1}}v(n)_\pm^2/n^2,
\quad D_k=D_{k,+}+D_{k,-}.
\tag{1.1}
\]

这里 \(v_-=(-v)_+\)。每个 \(D_k\) 都包含两个端点。

### 定理 A：RH 下的准确平均常数

在 RH 下，对每个不同非平凡零点 \(\rho=1/2+i\gamma_\rho\) 记其重数为 \(m_\rho\)，置

\[
c_\rho=\frac{m_\rho}{\gamma_\rho^2+1/4},\qquad
F(t)=\sum_{\rho\ {m distinct}}c_\rho e^{i\gamma_\rho t},
\]

\[
\mathcal A=\sum_{\rho\ {m distinct}}c_\rho^2,
\quad
\mathcal A_\pm=\lim_{T\to\infty}\frac1T\int_0^T F(t)_\pm^2\,dt.
\tag{1.2}
\]

这些均值存在，\(\mathcal A_\pm>0\)，并且

\[
\boxed{\mathcal A_++\mathcal A_-=\mathcal A.}\tag{1.3}
\]

完整闭整数道路具有准确渐近

\[
\boxed{S(q^*;B)=\mathcal A\log B+o(\log B),\qquad
S_\pm(q^*;B)=\mathcal A_\pm\log B+o(\log B).}\tag{1.4}
\]

对应闭 dyadic 块的 Cesàro 平均为

\[
\boxed{\lim_{N\to\infty}\frac1N\sum_{k=0}^{N-1}D_k(q^*)=h\mathcal A,
\qquad
\lim_{N\to\infty}\frac1N\sum_{k=0}^{N-1}D_{k,\pm}(q^*)=h\mathcal A_\pm.}\tag{1.5}
\]

同一准确绝对常数 \(\mathcal A\) 适用于每条上述固定校准道路的返回差 \(e\)。由于方向取 \(e=q_F-q^*\)，其正、负常数分别是 \(\mathcal A_-\)、\(\mathcal A_+\)。换成 \(-e=q^*-q_F\) 后恢复原顺序。常数不依赖所选固定厚度或准确校准权。

以上不需要零点简单性或频率线性独立性。重数先合并成同一频率的振幅，再平方。

### 定理 B：单侧累计能量的 RH 等价条件

分别选定 \(v=q^*,e,-e\) 中任意一个，以及一个固定符号 \(+\) 或 \(-\)。则

\[
\boxed{\mathrm{RH}
\iff S_\pm(v;B)=O(\log B)
\iff \limsup_{N\to\infty}\frac1N\sum_{k=0}^{N-1}D_{k,\pm}(v)<\infty.}\tag{1.6}
\]

每一侧单独就足够。等价式没有把正、负两种能量值宣称相同。

### 定理 C：不依赖零点数值的无条件双向成本

Stieltjes 常数约定为

\[
\zeta(1+z)=z^{-1}+\gamma-\gamma_1z+O(z^2).
\tag{1.7}
\]

定义

\[
C_*=2+\gamma-\log(4\pi),
\]

\[
V=6+2\gamma+4\gamma_1+2\gamma^2-2\log(4\pi)-\pi^2/4,
\qquad P=\frac{V^2}{4C_*^2}.
\tag{1.8}
\]

本轮有限区间计算认证 \(C_*,V,P>0\)。对 \(v=q^*,e,-e\)，无条件有

\[
\boxed{\limsup_{B\to\infty}\frac{S(v;B)}{\log B}\ge V,
\qquad
\limsup_{B\to\infty}\frac{S_\pm(v;B)}{\log B}\ge P.}\tag{1.9}
\]

相应闭块平均下界为 \(hV\)、\(hP\)。特别地，两方向完整尾都发散：

\[
\boxed{\sum_{n\ge1}\frac{(q_F(n)-q^*(n))_+^2}{n^2}
=\sum_{n\ge1}\frac{(q^*(n)-q_F(n))_+^2}{n^2}=\infty.}\tag{1.10}
\]

这是按 RH 成立与否分情形证明的无条件结论。RH 成立时有定理 A 的有限准确极限；RH 不成立时，定理 B 使两侧显示的 limsup 都为无穷。没有把后者升级成未经证明的 liminf 发散。

## 2. 绝对一致收敛的规范场及其均值

复用前驱已经完整证明的道路展开，零点按重数计：

\[
q^*(y)=\log(2\pi)+\sum_\rho\frac{y^\rho}{\rho(1-\rho)}-T(y),
\quad T(y)=\sum_{j\ge1}\frac{y^{-2j}}{2j(2j+1)},
\quad\sum_\rho\frac1{|\rho(1-\rho)|}<\infty.
\tag{2.1}
\]

在 RH 下所有规范系数均正实，故 (1.2) 在全部实 t 上绝对一致收敛。共轭配对使 F 为实函数。\(\zeta\) 在实区间 \((0,1)\) 没有零点：交错级数 \(\eta(s)>0\)，而 \(1-2^{1-s}<0\)，所以 \(\zeta(s)=\eta(s)/(1-2^{1-s})<0\)。因此没有零频。

把 (2.1) 放在 y=1，使用 \(q^*(1)=1+\gamma\) 和 \(T(1)=1-\log2\)，得到

\[
\boxed{\sum_{\rho\ {m distinct}}c_\rho=C_*;\qquad |F(t)|\le C_*.}\tag{2.2}
\]

各有限截断是三角多项式。不同频率的指数平均为零，所以均值满足

\[
M(F)=0,\qquad M(F^2)=\sum_\rho c_\rho^2=\mathcal A.
\tag{2.3}
\]

这里可直接用绝对一致收敛的双重级数逐项平均；同一频率已经先合并重数，无需估计不同零点间距。

对于 \(F_+^2\)、\(F_-^2\)、\(|F|\)、\(F|F|\) 等连续复合也存在均值。一个自足论证是：先在固定紧值域 \([-C_*,C_*]\) 上以多项式一致逼近所需连续函数，再以有限三角多项式一致逼近 F。每个有限复合三角多项式有准确均值，而均值误差不超过一致范数误差，因此极限存在。

由 \(M(F)=0\)，有

\[
M(F_+)=M(F_-)=\tfrac12M(|F|).
\]

又由 \(F^2\le C_*|F|\) 和均值下 Cauchy 不等式，

\[
M(|F|)\ge\frac{\mathcal A}{C_*},\qquad
\boxed{\mathcal A_\pm\ge\frac{\mathcal A^2}{4C_*^2}>0.}\tag{2.4}
\]

还准确有

\[
\mathcal A_\pm=\frac{\mathcal A\pm M(F|F|)}2.
\tag{2.5}
\]

因此不能只由共轭对称和零均值就把两侧各写成 \(\mathcal A/2\)。若另有一列平移 \(\tau_j\) 使 \(F(\cdot+\tau_j)\to-F\) 一致，则均值的平移不变性确实给 \(\mathcal A_+=\mathcal A_-=\mathcal A/2\)；该额外相位对称在本稿没有从 RH 推出。

一个准确有限见证是 \(F_0(t)=\cos t+\cos2t\)。它有非负 Fourier 系数、共轭对称、零均值和平方均值 1，但

\[
M((F_0)_+^2)=\frac13+\frac{9\sqrt3}{16\pi},\qquad
M((F_0)_-^2)=\frac23-\frac{9\sqrt3}{16\pi}.
\tag{2.6}
\]

证明写 \(c=\cos t\)，则 \(F_0=(2c-1)(c+1)\)，正区间为 \(|t|<\pi/3\)；并准确展开

\[
F_0^2=1+\cos t+\tfrac12\cos2t+\cos3t+\tfrac12\cos4t.
\]

在正区间积分即得 (2.6)。此见证仅检验上述一般均值推理，不是实际 ζ 零点关系的断言。

## 3. 完整背景、整数转移和闭块端点的支付

在 RH 下，由 (2.1)，

\[
q^*(e^t)e^{-t/2}=F(t)+r(t),\qquad
|r(t)|\le(\log(2\pi)+T(1))e^{-t/2}.
\tag{3.1}
\]

平方及正负平方函数在有界区间上 Lipschitz，故完整背景的平方能量差在 \(t\in[0,\infty)\) 可积。这使

\[
\int_1^B\frac{q^*(y)_\pm^2}{y^2}\,dy
=\int_0^{\log B}F(t)_\pm^2\,dt+O(1),
\tag{3.2}
\]

绝对平方同理。这里 O(1) 仅比较两种完整场，不是声称三角均值收敛有 O(1) 余项。

再支付整数与连续观察的差。由原整数源，对非整数 y 准确有

\[
(q^*)'(y)=\gamma-\log y+\sum_{n\le y}\Lambda(n)/n.
\tag{3.3}
\]

仅用 \(0\le\Lambda(n)\le\log n\) 及谐和和，便有 \(|(q^*)'(y)|\le C(1+\log^2y)\)。RH 下 (2.1) 还给 \(|q^*(y)|\le M\sqrt y\)。于是 \(g_\pm(y)=q^*(y)_\pm^2/y^2\) 局部绝对连续，几乎处处满足

\[
|g_\pm'(y)|
\le2MC\frac{1+\log^2y}{y^{3/2}}+\frac{2M^2}{y^2}.
\tag{3.4}
\]

此右边在 \([1,\infty)\) 可积。逐单位区间比较左端点与积分，连同末端的闭整数点，得到

\[
S_\pm(q^*;B)=\int_1^Bq^*(y)_\pm^2/y^2\,dy+O(1).
\tag{3.5}
\]

更具体地，在整数 \(X\ge2\) 的闭块上，离散与连续差为

\[
O((1+\log^2X)/\sqrt X),
\tag{3.6}
\]

其 dyadic 总和收敛。两个相邻闭块重复的端点总成本也有限，因为

\[
\sum_{k\ge0}\frac{q^*(2^k)^2}{2^{2k}}
\le M^2\sum_{k\ge0}2^{-k}<\infty.
\tag{3.7}
\]

结合 (2.3)、(3.2)、(3.5) 即得定理 A 对 q* 的所有式子。即使两个频率之差落在 \(2\pi\mathbb Z/h\)，这里仍是连续完整时段的平均；先把所有相邻块积分接起来，再作长时平均，交叉项照常消失。没有用几何节点样本的离散相位正交替代块内积分。

返回差的转移只需已证的 (0.2)。对每个 B，正部的 1-Lipschitz 性和有限维三角不等式给

\[
\left|\sqrt{S_+(e;B)}-\sqrt{S_-(q^*;B)}\right|\le Q_F,
\]

\[
\left|\sqrt{S_-(e;B)}-\sqrt{S_+(q^*;B)}\right|\le Q_F.
\tag{3.8}
\]

绝对平方同理。除以 \(\sqrt{\log B}\) 后误差趋零。闭 dyadic 块的累计中，每个整数最多出现两次，所以相应误差至多 \(\sqrt2Q_F/\sqrt N\)。因此所有准确平均常数都按方向传回 e 和 −e。

## 4. 一侧 O(log B) 为什么已经推出 RH

先证明 e 的任意一侧。由共同背景消去，e 在每个整数区间准确仿射。对正部或负部的平方使用凸性，得到第7轮同型的逐闭块比较

\[
\int_{2^k}^{2^{k+1}}e(y)_\pm^2/y^2\,dy
\le(1+2^{-k})^2D_{k,\pm}(e).
\tag{4.1}
\]

若 \(S_+(e;B)=O(\log B)\)，或者正闭块累计为 O(N)，则置 \(f_+(t)=e(e^t)_+e^{-t/2}\)，有

\[
\int_0^T f_+(t)^2dt=O(1+T).
\tag{4.2}
\]

分块 Cauchy–Schwarz 使 \(P(s)=\int_1^\infty e(y)_+y^{-s-1}dy\) 在 \(\Re s>1/2\) 绝对收敛并全纯。每个固定 \(D_{a_j}(n)\) 有界，故 \(D_F(n)\) 有界；再用 \(\Lambda(n)\le\log n\)，完整差式给 \(e(y)=O(y(1+\log^2y))\)。因此负部的 Mellin 积分 N(s) 至少在 \(\Re s>1\) 收敛，在那里

\[
N(s)=P(s)-\widehat e(s),
\quad
\widehat e(s)=\frac{\mathcal D_F(s)+\zeta'(s)/\zeta(s)}{s(s-1)},
\]

\[
\mathcal D_F(s)=\sum_j\frac{w_j}{a_j}\left[\frac{\zeta(s)}{\zeta(s+a_j)}-1\right].
\tag{4.3}
\]

对每个实 \(s>1/2\)，所有 \(s+a_j>1\)，移位分母无零点；ζ 在实 \((0,1)\) 也无零点；s=1 的可能极点由准确双校准消去。因此 \(\widehat e\) 沿实区间 \((1/2,\infty)\) 局部全纯。

使用以下非负 Mellin 引理：非负函数的 Mellin 积分若有有限收敛横坐标 \(\sigma_c\)，则其延拓在实点 \(\sigma_c\) 必有奇点。证明为：假设该点存在解析邻域，在右侧近点 \(\sigma_0\) 展开向左的 Taylor 级数。其所有系数经过 \((-1)^k\) 调整都是非负积分 \(\int v(y)(\log y)^ky^{-\sigma_0-1}dy/k!\)。在解析半径内，单调收敛把 Taylor 和恢复为更左侧的原非负积分，产生 \(\sigma<\sigma_c\) 的收敛，矛盾。

若 N 的收敛横坐标大于 1/2，右边 \(P-\widehat e\) 会使 N 在该实点解析，与引理矛盾。因此 N 也在 \(\Re s>1/2\) 全纯。于是 \(\widehat e=P-N\) 在该半平面全纯。

但每个 \(\Re\rho\ge1/2\) 的非平凡零点，返回差准确保留

\[
\operatorname{Res}_{s=\rho}\widehat e(s)=\frac{m_\rho}{\rho(\rho-1)}\ne0.
\tag{4.4}
\]

因此不存在 \(\Re\rho>1/2\) 的零点，再由反射对称推出 RH。若起初控制负部，同一论证交换 P、N 即可。对 q* 和 −e，使用 (3.8) 传递 O(log B) 条件即可；这里 (0.2) 无条件有效。

反向由定理 A。至于任意 B 与 dyadic 块累计的等价，仅用非负和的单调性以及每个整数在所有闭块中最多出现两次；不需要将重复端点当成不交区间。这完成定理 B。

## 5. 重数一次的显式基准及其认证

令 \(a_\rho=1/[\rho(1-\rho)]\)，这一节暂不假设 RH。由 (2.1) 在 \(\Re s>1\) 逐项积分，

\[
R(s):=\sum_{\rho\ {m distinct}}\frac{m_\rho a_\rho}{s-\rho}
=\widehat q^*(s)-\frac{\log(2\pi)}s
+\sum_{j\ge1}\frac1{2j(2j+1)(s+2j)}.
\tag{5.1}
\]

各边在 s=1 可解析延拓；这里使用延拓值，不假定原 Mellin 积分在 s=1 绝对收敛。完整参考道路的 Mellin 式为

\[
\widehat q^*(s)=\frac{1+\gamma}{s-1}-\frac1{(s-1)^2}
-\frac{\zeta'(s)/\zeta(s)}{s(s-1)}.
\tag{5.2}
\]

按 (1.7) 展开，

\[
\widehat q^*(1)=1+\gamma+2\gamma_1+\gamma^2.
\]

而准确部分分式给

\[
\sum_{j\ge1}\frac1{2j(2j+1)^2}=2-\log2-\frac{\pi^2}8.
\]

所以 \(2R(1)=V\)。再利用反射对称，

\[
2R(1)=\sum_\rho m_\rho a_\rho
\left(\frac1\rho+\frac1{1-\rho}\right)
=\sum_\rho m_\rho a_\rho^2.
\]

因此无条件有准确恒等式

\[
\boxed{V=\sum_{\rho\ {m distinct}}
\frac{m_\rho}{\rho^2(1-\rho)^2}.}\tag{5.3}
\]

在 RH 下每项为正实数，故

\[
\boxed{\mathcal A
=V+\sum_{\rho\ {m distinct}}
\frac{m_\rho(m_\rho-1)}{(\gamma_\rho^2+1/4)^2}
\ge V.}\tag{5.4}
\]

等号当且仅当全部非平凡零点简单。式 (5.3) 的重数一次与 Parseval 中重数平方明确不同。

脚本 `certify_log_energy_constants.py` 复用第5轮保存且已认证的 γ、γ1 区间；π 通过 Machin 恒等式及两条交错 arctan 级数给严格区间；\(\log(4\pi)=3\log2+\log(\pi/2)\) 用原 80 位向外整数区间和有限 atanh 级数支付。新的严格向外显示端点如下。

| 常数 | 下端 | 上端 |
|---|---|---|
| \(C_*\) | 0.04619141793224206762862049581299058 | 0.04619141793224206762862049581299059 |
| \(V\) | 0.00007420127287492974302501086782655 | 0.00007420127287492974302501086782656 |
| \(P=V^2/(4C_*^2)\) | 0.00000064511944366753062832059956463 | 0.00000064511944366753062832059956464 |
| \((\log2)V\) | 0.00005143240308721669877501596031126 | 0.00005143240308721669877501596031127 |
| \((\log2)P\) | 0.00000044716272350254931907953980915 | 0.00000044716272350254931907953980916 |

在 RH 情形，(2.4)、(5.4) 给 \(\mathcal A\ge V\)、\(\mathcal A_\pm\ge P\)。非 RH 情形，定理 B 使相应归一化累计和的 limsup 为无穷。两者合起来即为定理 C，而不是无条件宣称 RH 情形的有限常数存在。

## 6. 从单块 limsup 提升到块平均 limsup 的留数下界

还可以保留第7轮的每一个真实临界零点，而不只用显式基准 V。令

\[
L_{\rm av}=\limsup_{N\to\infty}\frac1N\sum_{k=0}^{N-1}D_k(e).
\]

则对任意有限组不同临界线零点 \(Z_0\)，

\[
\boxed{L_{\rm av}\ge h\sum_{\rho\in Z_0}
\left|\frac{m_\rho}{\rho(\rho-1)}\right|^2.}\tag{6.1}
\]

若有实部大于 1/2 的零点，则 \(L_{\rm av}=\infty\)。

证明不能直接复用“每块一致有界”的旧假设。若 \(L_{\rm av}<\infty\)，置 \(f(t)=e(e^t)e^{-t/2}\)、\(H(T)=\int_0^T|f(t)|^2dt\)。由 (4.1) 的绝对平方版本，先去掉有限初段，再让 \((1+2^{-k})^2\to1\)，得到

\[
\limsup_{T\to\infty}\frac{H(T)}T\le L_{\rm av}/h.
\tag{6.2}
\]

对块端点成立后，用 H 的单调性夹住一般 T 即可。该累计上界使 Mellin 积分在 \(\Re s>1/2\) 全纯，因此排除该半平面内的非零留数。

令 \(d\mu_\sigma(t)=2\sigma e^{-2\sigma t}dt\)。分部积分把平均假设准确变为

\[
\|f\|_{L^2(\mu_\sigma)}^2
=(2\sigma)^2\int_0^\infty H(t)e^{-2\sigma t}dt,
\]

\[
\limsup_{\sigma\downarrow0}\|f\|_{L^2(\mu_\sigma)}^2
\le L_{\rm av}/h.
\tag{6.3}
\]

对固定有限组频率，原 Gram 矩阵仍为

\[
G_{jk}(\sigma)=\frac{2\sigma}{2\sigma+i(\gamma_j-\gamma_k)}\to I,
\quad
b_j(\sigma)=2\sigma\widehat e(1/2+2\sigma+i\gamma_j)
\to\frac{m_j}{\rho_j(\rho_j-1)}.
\]

有限维投影不等式 \(b^*G^{-1}b\le\|f\|^2\) 与 (6.3) 给 (6.1)。整个证明只在有限频率矩阵中取极限；随后可对有限零点子集取上确界。它是真正的块平均下界，允许单块能量无统一上界。

## 7. 证据范围与接续意义

本轮新证书只计算 (1.8) 的常数及有限三角见证 (2.6)。复用旧 γ、γ1 的严格区间，新增 2 条 arctan 级数（64、20 项）、3 条 log 级数（各100项）；没有新增 ζ、零点、道路点值、素数筛或旧证书重跑。脚本将其所消费的两个旧文件及 SHA256 写入新 JSON。无界结论由本稿的解析证明承担。

新增结论准确强化第7轮返回边界：不仅完整绝对尾发散，两方向正尾都发散；在 RH 下还有与固定族无关的准确平均常数。在原单向算术目标上，这提供了更精确的返回成本及单侧强度判据，仍需另外证明实际无界层的普通素数亏缺和真实骨架锚点控制。

外部标准约定已核对 NIST DLMF §25.2 的交错级数、Stieltjes 展开及 §25.4 的完成函数归一化：

- https://dlmf.nist.gov/25.2 ，式25.2.3、25.2.4；
- https://dlmf.nist.gov/25.4 ，式25.4.3、25.4.4。

复算本轮常数：

```bash
python return_energy/certify_log_energy_constants.py \
  --previous prior/riemann_sparse_lengths_canonical_return_20261126
```

开发目录相应入口用 `research_round8/return_energy/certify_log_energy_constants.py`，前驱参数为 `deliverables/riemann_sparse_lengths_canonical_return_20261126`。作者核验与远端保存状态由统筹另行记录。
