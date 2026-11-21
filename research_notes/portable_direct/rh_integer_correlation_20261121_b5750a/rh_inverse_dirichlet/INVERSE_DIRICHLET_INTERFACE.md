# 逆 Dirichlet 乘子：无梯度附加项的正部窗口等价接口

Date: 2026-11-21
Contribution: EM-DIRECT-B5750A 原母任务内作者侧 unshared 推进；不作独立 Project Review。
Status: AUTHOR_PROVED_EXACT_DUAL_INTERFACE_AND_NEW_FINITE_DECOMPOSITIONS
Scientific source: enterprise-math@9fc068244e4f1117f1e75df5eb0285c6697d21d7。
Previous published continuation: cc8e2eec9e281ac2649341ec44a270c49bed6d38。

本稿接续 `rh_integer_energy/SIGNED_POSITIVE_ENERGY.md`。上一条局部乘子恒等式包含非负梯度，直接舍去梯度会留下明显余量。这里改用有限区间的逆离散 Laplacian，得到**恰等于目标平方和的源/边界配对**，并将其平方根精确写成一类非负凹测试核上的上确界。新接口不含需要另行压小的梯度项；仍须证明对整个测试核类的算术估计。

Dirichlet Green 核、有限分部求和与 Hilbert 空间对偶是标准工具，不主张工具本身的新颖性。研究贡献是其在完整道路递推、真实端点、原点前史与既有匹配窗口中的精确接口和复算。所有整数、合数和厚度标签均保留；标量核变换不增加 P000/X6 的原生空间轴。

## 1. 真实递推与有限 Dirichlet 问题

沿用完整道路读出

\[
R_a(n)=\prod_{p\mid n}(1-p^{-a}),\quad R_a(1)=1,
\]

\[
D_n=\sum_j\nu_jR_{a_j}(n)/a_j\ (n\ge2),\quad D_1=0,
\qquad\sum_j\nu_j=1,
\]

\[
q_n=\sum_{2\le k\le n}D_k(n/k-1)-n\log n+(1+\gamma)n.
\]

原点修正和固定初值不变。前轮已证明

\[
-\Delta^2q_n=f_n:=\frac{\kappa_n-D_n}{n},
\tag{1}
\]

\[
\kappa_n=n[(n+1)\log(n+1)-2n\log n+(n-1)\log(n-1)].
\]

这里保留精确 \(\kappa_n\)，不以 1 替换。

固定整数 \(2\le A<B\)、\(M=B-A\ge2\)，内点集合为 \(I=\{A+1,\ldots,B-1\}\)。取 \(0<\theta<1\)，定义

\[
w_n=n^{-2\theta-1},\qquad u_n=(q_n)_+,
\qquad S^\circ=\sum_{n\in I}w_nu_n^2.
\tag{2}
\]

给定任意内点向量 \(h\)，Dirichlet 问题

\[
z_A=z_B=0,\qquad-\Delta^2z_n=h_n\quad(n\in I)
\tag{3}
\]

的唯一解为

\[
\boxed{
z_n=\sum_{k\in I}G_{n,k}h_k,\qquad
G_{n,k}=
\frac{(\min(n,k)-A)(B-\max(n,k))}{B-A}.
}
\tag{4}
\]

逐段二阶差分直接给 \(-\Delta_n^2G_{n,k}=\mathbf1_{n=k}\)，且两端为零。这也证明唯一性：齐次解为仿射序列，两端为零只能恒为零。

核 \(G\) 对内点严格为正且对称。所以若 \(h\ge0\)，则 \(z\ge0\)、\(\Delta^2z\le0\)，即 \(z\) 是非负凹的零边界序列；若 \(h\not\equiv0\)，则每个内点 \(z_n>0\)。这不会删除 \(q_n\le0\) 处的源项。

## 2. 精确源/边界恒等式：没有梯度附加项

### 定理 1

对任意满足 (3) 的 \(z\)，有

\[
\boxed{
\sum_{n\in I}q_nh_n
=\sum_{n\in I}\frac{\kappa_n-D_n}{n}\,z_n
+q_Az_{A+1}+q_Bz_{B-1}.
}
\tag{5}
\]

**证明。** 有限 Green 恒等式给出

\[
\sum_{n\in I}q_n(-\Delta^2z_n)
-\sum_{n\in I}z_n(-\Delta^2q_n)
=q_Az_{A+1}+q_Bz_{B-1},
\]

其中 \(z_A=z_B=0\)，代入 (1) 与 (3) 即得。该式也可直接将三对角有限和换序验证，不需要无限和、尾极限或正则性假设。□

取

\[
h_n=w_nu_n,\qquad z=G(wu),
\tag{6}
\]

因为 \(q_nu_n=u_n^2\)，立即得到

\[
\boxed{
S^\circ=
\sum_{n\in I}\frac{\kappa_n-D_n}{n}\,z_n
+q_Az_{A+1}+q_Bz_{B-1}.
}
\tag{7}
\]

这正是目标平方和，没有额外梯度或接触成本。正部已通过右端曲率 \(h=wu\) 进入核。

**端点仍是原来的 \(q_A,q_B\)，不是 \((q_A)_+,(q_B)_+\)。** 测试核取零边界，并不使原道路端点通量消失；特别是负端点会产生有利负贡献。它们都由从原点开始的完整道路前史确定，不能重置。

若 \(S^\circ=0\)，所有内点 \(u_n=0\)，所以 \(h=0\)、\(z=0\)，(7) 两边都为零。这一情形不需要除以 \(\sqrt{S^\circ}\)。

## 3. 正部平方根与非负凹核的精确对偶

定义只依赖 \(A,B,\theta\) 的测试类

\[
\boxed{
\mathcal C_{A,B,\theta}=\left\{
z:\ z_A=z_B=0,\quad
h_n=-\Delta^2z_n\ge0,\quad
\sum_{n\in I}\frac{h_n^2}{w_n}\le1
\right\}.
}
\tag{8}
\]

\(z\ge0\) 由上述条件自动得到。定义源/边界线性泛函

\[
\boxed{
\mathscr L_D(z)=
\sum_{n\in I}\frac{\kappa_n-D_n}{n}\,z_n
+q_Az_{A+1}+q_Bz_{B-1}.
}
\tag{9}
\]

### 定理 2：精确等价接口

\[
\boxed{
\sqrt{S^\circ}
=\max_{z\in\mathcal C_{A,B,\theta}}\mathscr L_D(z).
}
\tag{10}
\]

**证明。** 对任意 \(z\in\mathcal C\)，(5) 与加权 Cauchy 给出

\[
\mathscr L_D(z)=\sum q_nh_n
\le\sum u_nh_n
\le\left(\sum w_nu_n^2\right)^{1/2}
\left(\sum h_n^2/w_n\right)^{1/2}
\le\sqrt{S^\circ}.
\]

若 \(S^\circ>0\)，选择

\[
\boxed{
h_n^*=\frac{w_nu_n}{\sqrt{S^\circ}},\qquad
z^*=Gh^*=\frac{G(wu)}{\sqrt{S^\circ}}.
}
\tag{11}
\]

其曲率范数恰为 1，且 \(\mathscr L_D(z^*)=\sqrt{S^\circ}\)，达到上界。

若 \(S^\circ=0\)，所有内点 \(q_n\le0\)，故对 \(h\ge0\) 有 \(\sum q_nh_n\le0\)；零测试 \(z=0\) 属于 \(\mathcal C\) 且给出零，所以上确界仍为零。必须保留 (8) 的 \(\le1\) 和零测试；不能不加讨论地改为范数恰等于 1。□

因此任意目标预算 \(\varepsilon\ge0\) 满足

\[
\boxed{
S^\circ\le\varepsilon^2
\quad\Longleftrightarrow\quad
\mathscr L_D(z)\le\varepsilon\quad\text{对所有 }z\in\mathcal C_{A,B,\theta}.
}
\tag{12}
\]

测试类不依赖未知的正部集合；已知 \(u\) 时可显式写出最优核，但证明统一算术界不能仅凭这个最优核公式完成。整个核类仍对应 \(M-1\) 维的非负曲率向量，并未被缩减成一个固定形状。

对匹配窗口 \(A=\lceil Y\rceil,B=\lfloor Y^\lambda\rfloor\)，(10) 将上一轮整数正部次幂条件精确改写成

\[
\forall\alpha>0\ \forall Y_0\ \exists Y\ge Y_0:\quad
\sup_{z\in\mathcal C_{A,B,\theta}}\mathscr L_{D_Y}(z)
\le Y^{\alpha/2}.
\tag{13}
\]

端点平方项仍使用上一轮已证明的控制，再接到完整连续窗口。与上一稿舍去梯度所得强充分条件不同，(13) 对内部平方和是等价式；**其任意远窗口估计仍未证明**。

## 4. 正三角核的线性累计算法与完整成本

令

\[
P_n=\sum_{k=A+1}^{n}(k-A)h_k,\qquad
Q_{n+1}=\sum_{k=n+1}^{B-1}(B-k)h_k.
\]

则 (4) 等价于

\[
\boxed{
z_n=\frac{B-n}{M}P_n+\frac{n-A}{M}Q_{n+1}.
}
\tag{14}
\]

一个前向累计、一个后向累计和一次逐节点合成即可完成。每次 Green 算子应用需要 \(O(M)\) 次算术操作和 \(O(M)\) 存储，不构造 \(M\times M\) 矩阵。对 \(h\ge0\)，式 (14) 的两项均非负，避免了先生成大仿射项再相减的消去。

两端邻点有简洁表达

\[
z_{A+1}=\frac1M\sum_{k\in I}(B-k)h_k,
\quad
z_{B-1}=\frac1M\sum_{k\in I}(k-A)h_k,
\]

\[
z_{A+1}+z_{B-1}=\sum_{k\in I}h_k.
\tag{15}
\]

这只是**给定有限输入之后**的核运算成本。完整道路输入的构造仍需要保存或重建各厚度直到 \(B\) 的道路：朴素素数倍数实现有

\[
O\!\left(m\sum_{p\le B}\lfloor B/p\rfloor+mB\right)
\]

次乘加，另有素数生成、对数/指数求值和精度成本；前史累计也有 \(O(B)\) 成本。本轮脚本只为新的核配对重建同一确定性有限输入，没有重跑旧的梯度或连续正部积分套件。不能把线性核运算成本写成整个数论问题的总成本。

### 4.1 单位曲率范数的精确点态包络

对 \(z\in\mathcal C\)，

\[
\boxed{
0\le z_n\le K_n:=\left(\sum_{k\in I}w_kG_{n,k}^2\right)^{1/2}.
}
\tag{16}
\]

这是加权 Cauchy；取 \(h_k=w_kG_{n,k}/K_n\) 可达到上界，故对给定节点是尖锐的。所有 \(K_n^2\) 也可用前后累计线性计算：

\[
K_n^2=
\frac{(B-n)^2}{M^2}\sum_{k=A+1}^{n}(k-A)^2w_k
+\frac{(n-A)^2}{M^2}\sum_{k=n+1}^{B-1}(B-k)^2w_k.
\tag{17}
\]

在本项目目标范围 \(1/2\le\theta<1\)，由 \(G_{n,k}\le\min(n,k)\) 得到方便的统一界

\[
\boxed{K_n\le\frac{n^{1-\theta}}{\sqrt{2\theta(1-\theta)}}.}
\tag{18}
\]

证明只需

\[
\sum_{k\le n}k^{1-2\theta}
+n^2\sum_{k>n}k^{-2\theta-1}
\le\frac{n^{2-2\theta}}{2-2\theta}
+\frac{n^{2-2\theta}}{2\theta}.
\]

因此即使匹配接口给 \((\kappa_n-D_n)_+<2\)，提前丢掉有利源项后，单位核配对的简单估计仍付出 \(O_\theta(B^{1-\theta})\) 成本。逆算子不会自动消除缺失的算术相关；其优势在于将目标准确转到非负凹核类，避免另行控制梯度。

## 5. 源势与真实边界的另一种精确分解

定义真实端点的仿射插值

\[
\ell_n=\frac{B-n}{M}q_A+\frac{n-A}{M}q_B,
\qquad p_n=(Gf)_n.
\]

由唯一性，

\[
\boxed{q_n=\ell_n+p_n.}
\tag{19}
\]

对任意 \(h\)、\(z=Gh\)，对称性和 (15) 给出

\[
\sum f_nz_n=\sum h_np_n,
\qquad q_Az_{A+1}+q_Bz_{B-1}=\sum h_n\ell_n.
\tag{20}
\]

这些式子明确显示，源项配对与端点项之间仍可抵消。一个可检查的有限上界是

\[
\boxed{
\sqrt{S^\circ}\le
\left(\sum w_n(\ell_n)_+^2\right)^{1/2}
+\left(\sum w_n(p_n)_+^2\right)^{1/2}.
}
\tag{21}
\]

它没有上一稿的梯度附加成本，但 \(p=Gf\) 本身包含完整算术抵消，仍需全尺度估计。

若进一步删去源 \(f\) 的全部负部，并将两个端点都取正部，令

\[
\widetilde p=G(f_+),\qquad
\widetilde\ell_n=\frac{B-n}{M}(q_A)_++\frac{n-A}{M}(q_B)_+,
\]

则核的正性给出

\[
\boxed{S^\circ\le\sum w_n(\widetilde p_n+\widetilde\ell_n)^2.}
\tag{22}
\]

这是合法但可能很差的上界。下节对真实道路量化其损耗，不使用任意构造的残差作为道路反例。

## 6. 同一三个实际窗口的新计算

参数沿用上一轮：\(Y=1000,Z=Y^{3/2}\)，整数核心为 \([A,B]=[1000,31622]\)，共有 \(30621\) 个内部源节点。二阶和切比雪夫样本取 \(\theta=.6\)，一阶样本取 \(\theta=.9\)。切比雪夫仍为旧直接桥的 11 节点、最大厚度 \(1/2\)，未改称为另一个复背景定理的参数样本。

本轮仅新增 Green 累计、源/端点分解、归一化最优核与 (19) 的重建核对。原参数与旧平方和在 `inputs.json` 中以来源 SHA256 固定。每个样本中的全部道路、六个非空 \(\omega(n)\) 层以及负 \(q_n\) 处的源均保留。

### 6.1 无梯度源/端点恒等式的实际数值

| 量 | 二阶，\(\theta=.6\) | 切比雪夫 11，\(\theta=.6\) | 一阶，\(\theta=.9\) |
|---|---:|---:|---:|
| 实际 \(S^\circ\) | \(7.26956985\times10^{-4}\) | \(7.42900768\times10^{-4}\) | \(6.47099414\times10^{-7}\) |
| 源项净配对 \(\sum f_nz_n\) | \(1.73084283\times10^{-4}\) | \(1.74103311\times10^{-4}\) | \(4.74014137\times10^{-7}\) |
| 左端 \(q_Az_{A+1}\) | \(5.33010634\times10^{-4}\) | \(5.39784594\times10^{-4}\) | \(4.92082609\times10^{-7}\) |
| 右端 \(q_Bz_{B-1}\) | \(2.08620678\times10^{-5}\) | \(2.90128631\times10^{-5}\) | \(-3.18997332\times10^{-7}\) |

三项相加等于目标平方和。前两例在已合并的源工作与边界之间没有抵消；第三例的真实右端 \(q_B\approx-48.85124\)，其负通量明显降低了结果。不能因为 \(z_B=0\) 就删掉这个邻点通量。

归一化最优核的曲率范数平方均为 1，其泛函值分别为

\[
0.0269621398365134,\quad
0.0272562060375035,\quad
0.000804424896174470,
\]

分别等于对应的 \(\sqrt{S^\circ}\)。这个精确匹配核验了等价接口；不是无需算术估计即可免费获得的独立全尺度上界。

### 6.2 实际抵消仍存在于源配对内部

第一例的源工作为

\[
\underbrace{0.9754073907974053}_{\sum\kappa_nz_n/n}
-\underbrace{0.9752343065146022}_{\sum D_nz_n/n}
=0.0001730842828031.
\]

切比雪夫样本对应

\[
0.9973027708618704-0.9971286675510114
=0.0001741033108590.
\]

因此梯度附加成本虽已消除，精细的算术抵消没有消失。用

\[
\frac{\sum|f_n|z_n+|q_Az_{A+1}|+|q_Bz_{B-1}|}{S^\circ}
\]

量化提前拆成绝对值的成本，三例分别为 **2371.4035、2372.9517、1297.8027**。

### 6.3 保留源势符号后的上界，以及删源负部的代价

| 样本 | 源势/边界正部三角上界 (21) / 实际 \(S^\circ\) | 删源负部并将端点取正部的 (22) / 实际 \(S^\circ\) | 上一稿舍去梯度的上界 / 实际 \(S^\circ\) |
|---|---:|---:|---:|
| 二阶，\(\theta=.6\) | 1.188958 | \(2.9794\times10^6\) | 174.8779 |
| 切比雪夫 11，\(\theta=.6\) | 1.186187 | \(2.9159\times10^6\) | 171.5543 |
| 一阶，\(\theta=.9\) | 4.182867 | \(1.9253\times10^7\) | 1621.9526 |

这些比较均针对同一个实际整数目标。它们表明源势接口在所选有限样本中避免了上一条梯度舍弃损失；同时，再次说明不能把源符号信息提前丢掉。计算 \(p=Gf\) 本身利用了完整源序列，这些有限比值不建立 \(p\) 的任意远窗口估计。

### 6.4 正部曲率的支持不等于允许保留的源人口

三个样本的 \(h_n=w_n(q_n)_+\) 分别仅在 **28714、29106、754** 个内点为正；然而各自的 \(z=Gh\) 在全部 **30621** 个内点严格为正。特别是第三例中，绝大部分 \(q_n\le0\) 的位置仍对逆核源工作作出贡献。

这是一条具体的数据保真要求：正部选择作用于乘子的曲率，不代表可以删除其余整数或合数源。结果文件为每个真实 \(\omega(n)\) 层同时记录了完整源节点数和 \(q_n\le0\) 的源节点数。

## 7. 证据范围与下一步

`verify_inverse_dirichlet.py` 以 80 位非区间浮点运行，三个样本全部通过：

- 每个节点的 Dirichlet 方程残差小于 \(3\times10^{-81}\)。
- 源势加真实端点插值重建 \(q\) 的最大误差小于 \(2\times10^{-74}\)。
- 原始能量恒等式误差小于 \(6\times10^{-79}\)。
- 归一化最优核的对偶恒等式误差小于 \(2\times10^{-77}\)。

一般结论依靠上文有限代数证明；数值结果不是区间认证。上一轮连续正部积分和梯度能量套件均未重跑。

本轮得到的可延续目标是：**对 (8) 的非负凹零边界测试核，直接证明完整道路源与真实端点泛函的统一上界。** 它是内部正部平方和的精确等价接口，避免要求额外梯度能量也次幂；仍须保留源内部抵消和实际端点。现阶段没有证明该全尺度界，也没有使用或重新宣称证明已有 RH 等价的原始 \(\mathcal Q_a\) 条件。

## 8. 文件与归属

- `INVERSE_DIRICHLET_INTERFACE.md`：本稿。
- `inputs.json`：三个既有窗口的参数、旧平方和与来源文件哈希。
- `verify_inverse_dirichlet.py`：新的线性累计算子、配对及对偶核验。
- `inverse_dirichlet_results.json`：完整新结果，包括全部因子层和负端点。

完整道路定义、原点端口和科学约束来自冻结项目输入；整数递推与窗口等价来自上一轮 `rh_next_window/NOTES.md`；所复用的有限窗口来自 `rh_next_tail/`；梯度损失的对照来自本轮 `rh_integer_energy/`。所有研究为原作者侧协作，不作远端写入、CLAIM、身份改变或独立 Review。
