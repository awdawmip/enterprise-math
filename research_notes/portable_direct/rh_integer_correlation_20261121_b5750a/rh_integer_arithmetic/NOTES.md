# 完整道路残差的整除结构与稀疏端点认证

Date: 2026-11-21.

Parent task: `RS-RH-METHOD-TRANSFER-20261121`, existing author identity and Activity reused. Same-context author mathematics only; no remote control mutation, new CLAIM or independent Project Review.

Status: AUTHOR_PROVED_DIVISOR_RESIDUAL_REPRESENTATION_AND_EXACT_SPARSE_ENDPOINT_CERTIFICATE. ARBITRARILY_DISTANT_WINDOW_POSITIVE_ENERGY_CONTROL_OPEN.

## 0. 本轮推进的范围

本稿沿用 P000 / 原生 X6、联合观察保真、残差保真及完整整数道路科学快照 `enterprise-math@9fc068244e4f1117f1e75df5eb0285c6697d21d7`。控制面入口由父分支按当前全局 `ffc232ae77f01ae88f1d4501c16bfbde51156835` 与项目 `49ad3d35092358dffe64a7be005b3864306da241` 处理，本作者分支不重复远端操作。

上轮 Source 为 `cc8e2eec9e281ac2649341ec44a270c49bed6d38`，本地包为 `riemann_adaptive_window_20261121/`。主要使用其中 `rh_next_window/NOTES.md` 的精确节点残差和前史端口，以及 `rh_next_structure/STRUCTURE.md` 的正对数核。父分支本轮的 `rh_integer_kernel/POSITIVE_KERNEL_AND_LAPLACE_BOUND.md` 将核的非负性推广到任意不同正节点的原点 Lagrange 读出；本稿只消费其 `Psi(t)>=0` 结论，不重复该证明。

本轮没有再增加一类逐整数 `|D-Lambda|` 界。新增结果是：

1. 将离散背景 `kappa` 本身写成完整道路的正混合，再进行 Möbius 反演；由此得到全部残差整除项的精确奇偶层符号。
2. 将 `D_n-kappa_n` 的共同带权累计改写成有限整除核求和，保留单位与窗口前史。
3. 对一个或少量整数端点，利用加权 Möbius 递推及严格幂和包络，避免逐个展开到最大端点；完成 `N=10^6` 的有理区间认证。
4. 明确指出该表示中逐项取绝对值、以及把少量端点算法直接推广为全窗复杂度结论的损失。

整除指标、辅助核和递推缓存属于已有道路的数学观察工具，不增加空间轴。改换求和次序不是把合数人口或不同素因子联合关系删除。

## 1. 道路、读出与完整的残差背景

令不同正厚度为 `a_j`，固定实权重为 `nu_j`，且 `sum nu_j=1`。定义

\[
R_a(n)=\prod_{p\mid n}(1-p^{-a})
=\sum_{d\mid n}\mu(d)d^{-a},
\]

\[
D_n=\sum_j\frac{\nu_j}{a_j}R_{a_j}(n)\quad(n\ge2),
\qquad D_1=0,
\tag{1}
\]

\[
\Psi(t)=\sum_j\frac{\nu_j}{a_j}(1-e^{-a_jt}).
\tag{2}
\]

假设本稿需要讨论确定符号时使用的节点族满足 `Psi(t)>=0`，并且 `t>0` 时严格为正。等距多厚度公式满足此性质；父分支的一般正节点 Lagrange 公式也满足它。纯代数恒等式不需要这个符号假设。

利用 `sum_(d|n)mu(d)=1_(n=1)`，全部人口上的正确读出为

\[
\boxed{D=\mathbf1*c_D,\qquad c_D(d)=-\mu(d)\Psi(\log d).}
\tag{3}
\]

这里 `*` 为 Dirichlet 卷积，`1(n)=1`。式 (3) 自动给出 `D_1=0`；若直接把 (1) 套到 `n=1` 而不修正，会多出 `sum nu_j/a_j`。`mu(d)=0` 出现在整除求和的辅助指标上，不等于删除目标整数 `n`：每个目标整数仍由其全部平方自由除数共同贡献。

令 `f(x)=x log x`，连续定义 `f(0)=0`。将上轮 `n>=2` 的离散背景延拓为

\[
\kappa_n=n\big[f(n+1)-2f(n)+f(n-1)\big],\qquad n\ge1.
\tag{4}
\]

特别地

\[
\boxed{\kappa_1=2\log2.}
\tag{5}
\]

这个端口不是任意选择的归零项：它使原点到任意端点的离散积分恰好恢复 `n log n`。

## 2. kappa 的 Möbius 反演具有确定的联合层符号

令

\[
\alpha_k=\frac1{(k+1)(2k+1)},\qquad k\ge0.
\]

三角积分表示给出

\[
\kappa_n=2\int_0^1\frac{1-t}{1-t^2/n^2}\,dt
=\sum_{k=0}^{\infty}\alpha_k n^{-2k},\qquad n\ge1.
\tag{6}
\]

对 `n=1`，几何级数在 `[0,1)` 上单调递增，且积分有限；因此非负项的单调收敛仍证明该式，并给出 `sum alpha_k=2log2`。对 `n>=2`，这是绝对且一致收敛的几何展开。

定义

\[
b_\kappa=\mu*\kappa,\qquad
\rho_n=\frac{\operatorname{rad}(n)}n.
\]

### 定理 1：背景整除项是带奇偶符号的正道路混合

对 `n>=2`，

\[
\boxed{
b_\kappa(n)=\mu(\operatorname{rad}(n))\,\beta(n),\qquad
\beta(n)=\sum_{k=1}^{\infty}\alpha_k\rho_n^{2k}R_{2k}(n)>0.
}
\tag{7}
\]

而 `b_kappa(1)=kappa_1=2log2`。

**证明。** 有限个除数允许与绝对收敛级数交换求和。`k=0` 项为 `sum_(d|n)mu(d)=0`。对每个 `k>=1`，

\[
\sum_{d\mid n}\mu(d)(n/d)^{-2k}
=n^{-2k}\prod_{p\mid n}(1-p^{2k})
=\mu(\operatorname{rad}(n))\rho_n^{2k}
\prod_{p\mid n}(1-p^{-2k}).
\]

右边除奇偶符号外全部严格为正。□

这里出现的是整数厚度 `2k` 的原有完整道路，而不是另造一类删去合数的背景模型。

### 2.1 幅度与平方因子部分

令整数 `q=n/rad(n)>=1`。因为 `R_(2k)(n)` 随 `k>=1` 增大，

\[
\boxed{
R_2(n)(\kappa_q-1)\le\beta(n)\le\kappa_q-1.
}
\tag{8}
\]

又对任意有限素因子集合，

\[
R_2(n)\ge\prod_{j=2}^{M}(1-j^{-2})
=\frac{M+1}{2M}>\frac12
\]

只需取 `M` 不小于最大素因子。因此

\[
\tfrac12(\kappa_q-1)<\beta(n)\le\kappa_q-1.
\tag{9}
\]

平方自由 `n` 有 `q=1`，故其背景整除项幅度处于固定正常数之间：

\[
\tfrac12(2\log2-1)<\beta(n)<2\log2-1.
\tag{10}
\]

对 `q>=2`，上轮已证明的级数估计也直接给出

\[
\frac1{12q^2}<\beta(n)\le\frac1{6(q^2-1)}.
\tag{11}
\]

这些是背景的精确因子层结构，不是新的 `D-Lambda` 误差界。

若在 (7) 截到 `k=K`，`q>=2` 时的尾项有几何界

\[
0\le\sum_{k>K}\alpha_k\rho_n^{2k}R_{2k}(n)
\le\frac{\alpha_{K+1}\rho_n^{2K+2}}{1-\rho_n^2}.
\tag{12}
\]

平方自由项也可用准确的总质量
`(2log2-1)-sum_(k=1)^K alpha_k` 包络剩余尾。实际有限认证可直接用 `mu*kappa` 的有限除数和，不需要运行无穷级数。

## 3. 完整残差的整除项有统一奇偶符号

令

\[
E_n=D_n-\kappa_n,\qquad c=\mu*E=c_D-b_\kappa.
\]

则 `E=1*c`。由 (3)、(7)，对 `n>=2`，

\[
\boxed{
c(n)=-\mu(\operatorname{rad}(n))\,A(n),\qquad
A(n)=\mathbf1_{n\text{ 平方自由}}\Psi(\log n)+\beta(n)>0.
}
\tag{13}
\]

单位项为

\[
\boxed{c(1)=-2\log2.}
\tag{14}
\]

所以不同素因子数为奇数的整除项 `c(n)` 严格为正，为正偶数的严格为负。这个规律同时适用于含平方因子的整数；它由 `mu(rad n)` 而不是 `mu(n)` 决定。

**必须区别两个层次。** 式 (13) 是残差的 Möbius 反演项的符号，不是 `D_n` 或 `D_n-kappa_n` 本身的符号。后两者仍是全部除数项的共同累计。把这个确定符号图误读为已经控制了它们的和，会再次丢失真正困难的相关对消。

## 4. 共同带权累计的完整整除核表示

定义对 `x>=1` 的非负核

\[
\boxed{
W(x)=xH_{\lfloor x\rfloor}-\lfloor x\rfloor
=\sum_{1\le k\le x}(x/k-1),
}
\tag{15}
\]

并对 `0<=x<1` 令 `W(x)=0`。

固定道路平滑量

\[
\mathcal H_D(y)=\sum_{2\le n\le y}D_n(y/n-1),
\qquad
F(y)=\mathcal H_D(y)-y\log y+(1+\gamma)y.
\tag{16}
\]

有限 Dirichlet 卷积换序给出

\[
\sum_{n\le y}E_n(y/n-1)
=\sum_{d\le y}c(d)W(y/d).
\tag{17}
\]

### 定理 2：整数端点的精确累计

对每个整数 `N>=1`，

\[
\boxed{
T_N:=\mathcal H_D(N)-N\log N
=\sum_{d\le N}c(d)W(N/d),
}
\tag{18}
\]

\[
\boxed{F(N)=N(1+\gamma)+T_N.}
\tag{19}
\]

上轮 Green 公式使用的 `n>=2` 加权残差恰为

\[
\boxed{
\sum_{n=2}^{N}(D_n-\kappa_n)(N/n-1)
=T_N+2(N-1)\log2.
}
\tag{20}
\]

**证明。** 离散二次差分的望远镜恒等式给出

\[
\sum_{n=1}^{N}\kappa_n(N/n-1)
=\sum_{n=1}^{N}(N-n)\Delta^2f(n)=f(N)=N\log N,
\]

其中 `f(0)=f(1)=0`。再用 `D_1=0`、`E_1=-kappa_1` 及 (17)。□

### 4.1 实数窗口与前史

令 `L_f(y)` 是 `f(y)=ylog y` 在相邻整数间的弦插值。`sum_(n<=y) kappa_n(y/n-1)` 与 `L_f` 在每个整数单元都为仿射函数，并在所有整数端点相等。因此

\[
\boxed{
F(y)=(1+\gamma)y+\sum_{d\le y}c(d)W(y/d)+\delta_f(y),
\qquad\delta_f(y)=L_f(y)-f(y).
}
\tag{21}
\]

在 `N<=y<=N+1`，凸性及 `f''=1/y` 给出

\[
0\le\delta_f(y)\le\frac{(y-N)(N+1-y)}{2N}\le\frac1{8N}.
\tag{22}
\]

公式从原点计算全部整除项；窗口左端前的输入一直包含在内。若改用局部窗口递推，仍需原有的两个前史端口，不能把它们重新置零。

### 4.2 背景的两个累计端口可以完全望远镜

对 `N>=1`，

\[
\boxed{
\sum_{n=1}^{N}\frac{\kappa_n}{n}
=(N+1)\log(N+1)-N\log N,
}
\tag{23}
\]

\[
\boxed{
\sum_{n=1}^{N}\kappa_n
=N(N+1)\log(1+1/N).
}
\tag{24}
\]

第一式是二阶差分的一次望远镜；第二式是带 `n` 权的离散分部求和。若端口从 `n=2` 开始，两式均减去 `2log2`。任意整块区间的背景端口因此只需端点对数，不必逐项计算 `kappa_n`。

## 5. 共同对消与逐项绝对值不能混为一谈

核 `W` 非负，式 (13) 把真正要估计的量变成因子奇偶层之间的共同累计。它没有把这种累计变成非负和。

一个明确的范围障碍是：若在 (18) 中直接对所有项取绝对值，所得主要量至少为 `c(2)W(N/2)`。而

\[
c(2)\ge\beta(2)=\kappa_1-\kappa_2
=2\log(32/27)>0.
\]

由 `H_(floor x)>=log x`、`floor x<=x`，有 `W(x)>=x(log x-1)`，故

\[
\boxed{
\sum_{d\le N}|c(d)|W(N/d)
\ge\log(32/27)\,N[\log(N/2)-1].
}
\tag{25}
\]

同一下界也适用于只累加正 `c(d)` 的量。于是，对任意固定 `theta<1`，这种直接丢弃全部负项或先取绝对值的界自身不能成为 `O(N^theta)` 的端点控制。

这是对**这一特定估计策略**的严格障碍，不是对真实累计的增长下界，也不排除先重组已知背景、再使用更精细的带符号估计。尤其不能把它当作 RH 失败证据。

在本轮 `N=4096,h=1/16` 的严格有限计算中：

| 量 | 认证值所在的小区间的近似中心 |
|---|---:|
| 原 Green 带符号残差 `sum_(n>=2)(D-kappa)(N/n-1)` | `-830.5355335181` |
| 对同一残差逐项取绝对值后累计 | `32805.3397115825` |
| 整除表示的带符号累计 `T_N` | `-6507.4109423041` |
| 整除表示逐项取绝对值后累计 | `287392.7871177790` |

上下两组的原点补偿不同，不能交叉当作同一量；每组内部均显示了各自取绝对值造成的实际损失。严格向外区间保存在 JSON 中。

## 6. 接入正部能量时，仍须保留与真实 q 的相关性

父分支本轮的离散能量恒等式含有有限主项

\[
\mathcal E_{A,B}
=\sum_{A<n<B}(\kappa_n-D_n)\frac{(q_n)_+}{n^{2\theta}}.
\]

对每个正整数 `d`，定义非负倍数核

\[
K_d=\sum_{\substack{A<n<B\\d\mid n}}
\frac{(q_n)_+}{n^{2\theta}}\ge0.
\]

有限换序得到

\[
\boxed{
\mathcal E_{A,B}=-\sum_{d<B}c(d)K_d
=2\log2\,K_1+
\sum_{2\le d<B}\mu(\operatorname{rad}(d))A(d)K_d.
}
\tag{26}
\]

所以能量问题可以明确定位到：因子奇偶层的正幅度 `A(d)` 与真实正部读出在其倍数上的核 `K_d` 的带符号相关累计。仅给出层的符号或人口数，不能控制这个相关量。所有边界项、接触项及其它非负项仍按父分支原恒等式保留，(26) 没有改变它们。

直接评价所有 `K_d` 不必然比原始 `O(B-A)` 主项更快；本式首先是精确结构和研究接口，不声称它单独降低完整能量求和的计算复杂度。

## 7. 一个或少量端点的亚线性求值

式 (18) 的单纯商分组如果仍须预先计算全部 `c(d)`，并没有自动获得亚线性算法。已有完整 `D` 前缀表时，原来的两个端口甚至能在常数时间回答端点查询。这里的实际计算增量是：**不先形成长度 N 的道路或整除系数表**。

### 7.1 加权 Möbius 累计的有限递推

对实数 `a>0` 定义

\[
M_a(x)=\sum_{n\le x}\mu(n)n^{-a},\qquad
P_a(x)=\sum_{n\le x}n^{-a},\qquad M_a(0)=P_a(0)=0.
\]

因为 `(mu(n)n^(-a))*(n^(-a))` 是单位卷积，

\[
\boxed{
M_a(N)=1-\sum_{k=2}^{N}k^{-a}M_a(\lfloor N/k\rfloor).
}
\tag{27}
\]

对一段 `L<=k<=R`，若 `floor(N/k)=q` 恒定，则该段恰为

\[
[P_a(R)-P_a(L-1)]M_a(q).
\tag{28}
\]

所有内层参数小于 `N`，故有限递推是良定义的，不依赖 Mertens 渐近估计或 RH。

### 7.2 原道路端口由四类这样的前缀恢复

令含单位人口的道路端口为

\[
U_a(N)=\sum_{n\le N}R_a(n),\qquad
V_a(N)=\sum_{n\le N}\frac{R_a(n)}n.
\]

再次作有限换序，

\[
U_a(N)=\sum_{d\le N}\mu(d)d^{-a}\lfloor N/d\rfloor,
\qquad
V_a(N)=\sum_{d\le N}\mu(d)d^{-a-1}H_{\lfloor N/d\rfloor}.
\]

在每个 `floor(N/d)=q` 的最大块 `[L,R]` 上，这分别为

\[
q[M_a(R)-M_a(L-1)],
\qquad
H_q[M_{a+1}(R)-M_{a+1}(L-1)].
\tag{29}
\]

最后

\[
\boxed{
\mathcal H_D(N)=\sum_j\frac{\nu_j}{a_j}
\big[NV_{a_j}(N)-U_{a_j}(N)-(N-1)\big].
}
\tag{30}
\]

`-(N-1)` 是每个厚度的真实单位端口修正。它不能在带符号组合中省略。

计算二阶 `nu=(2,-1),a=(h,2h)` 只需 `M_h,M_(2h),M_(h+1),M_(2h+1)`，以及谐和数 `H=P_1`。所有合数由倍数计数和谐和权精确保留。

### 7.3 商闭包、操作计数与适用范围

固定单个目标 `N`，设小前缀筛界为 `B`。超过 `B` 的递推参数只可能属于

\[
\mathcal Q(N)=\{\lfloor N/k\rfloor:1\le k\le N\},
\]

因为
`floor(floor(N/i)/j)=floor(N/(ij))`。不同大参数至多 `N/B` 个；每个参数 `x` 的商块数不超过 `2sqrt x`。因此总递推商块数至多

\[
2\sqrt N\sum_{i\le N/B}i^{-1/2}\le\frac{4N}{\sqrt B}.
\tag{31}
\]

端点重建另需不超过 `2sqrt N` 个块。若每个幂和查询的计算成本为 `O(K)`，并缓存全部商端点，则对于 `m` 个厚度，算术操作量可写为

\[
\boxed{O\!\left(m\left[B+N/\sqrt B+K\sqrt N\right]\right).}
\tag{32}
\]

取 `B` 为 `N^(2/3)` 的整数上界，在固定认证精度及可控幂和 oracle 成本下，主要数量级为 `O(mN^(2/3))`；内存也是相应的有限前缀和商缓存大小。这里的小前缀可以使用 Euler 线性 Möbius 筛；当前脚本已采用该实现，每个合数仅在其最小素因子处生成一次。最初有限记录使用的普通倍数筛多出 `O(B log log B)` 筛成本，不能把它默认为线性。这里分别记录算术操作量、幂和成本与位精度，没有把大整数运算宣称为无成本。

这一结论适用于一个或少量端点。若对 `O(sqrt Z)` 个平方网格端点逐个重算，不能直接宣称完整窗口也获得同样的总成本下降。跨端点可以共享商缓存，但本稿未证明平方网格的联合商成本优于一次长度 `Z` 的道路筛。对于窗口代理后来证明的四次方网格，固定有理厚度下即使独立调用也得到不同结论：算术调用量为 `O(mZ^(11/12)+mKZ^(3/4))`。其准确范围、非整数窗口边缘及位成本见 `QUARTIC_COST_AND_GAMMA_APPENDIX.md`。

### 7.4 数值误差的一个统一有限控制

此节只控制计算误差，不是对真实 Möbius 累计作大小估计。若某组近似值 `M_tilde` 在商闭包上满足递推残差

\[
\left|\widetilde M_a(x)-1+
\sum_{k=2}^{x}k^{-a}\widetilde M_a(\lfloor x/k\rfloor)\right|
\le\varepsilon x^2,
\]

且小前缀误差至多 `4epsilon x^2`，则逐层归纳给出

\[
\boxed{|\widetilde M_a(x)-M_a(x)|\le4\varepsilon x^2.}
\tag{33}
\]

原因是

\[
\sum_{k=2}^{x}k^{-a}\left(\frac{\lfloor x/k\rfloor}{x}\right)^2
\le\sum_{k=2}^{\infty}k^{-2}
\le\frac14+\int_2^\infty t^{-2}dt=\frac34.
\]

因此误差归纳的右端至多 `epsilon x^2+(3/4)4epsilon x^2`。式 (33) 是可选的事后残差认证工具；本轮脚本实际使用更直接的逐运算有向区间包含性。

## 8. 严格幂和 oracle：没有把无穷尾或浮点数当作证明

脚本使用 `h=1/16`，四个 Möbius 指数为

\[
1/16,\quad1/8,\quad17/16,\quad9/8.
\]

所有区间端点是分母 `10^60` 的有向整数；每次加减、乘法及有理数缩放都分别向外取整。时间统计使用浮点，仅为诊断，不参与任何证书。

### 8.1 代数输入和对数

`n^(-1/16)` 先通过整数幂比较把 `n^(1/16)` 夹在相邻有理数之间，再取倒数。小前缀利用最小素因子递推复用这些根；其它三个指数由平方和除以 `n` 得到。

对数先做二进制缩放。对于 `1<=t<=2`，令 `z=(t-1)/(t+1)<=1/3`，以 80 项正级数及显式尾界

\[
\log t=2\sum_{k=0}^{79}\frac{z^{2k+1}}{2k+1}+R,
\qquad
0\le R\le\frac{2(1/3)^{161}}{161(1-1/9)}
\tag{34}
\]

给出严格包络。原始两项证书没有使用 `gamma` 的数值，而是直接认证 `T_N` 和 (20) 的残差累计。后续的小附录复用相同 EM 结构严格包络 `gamma`，并只定向重算一次 `N=10^6`，补齐完整的 `F(N)` 端点证书。

### 8.2 Euler–Maclaurin 的有限余量

取锚点 `b=256`、阶数 `K=16`。`P_a(b)` 直接有限累加。对 `N>b`，设 `g_a(t)=t^(-a)`，则

\[
\begin{aligned}
P_a(N)={}&P_a(b)+\int_b^N g_a(t)dt
+\frac{g_a(N)-g_a(b)}2\\
&+\sum_{r=1}^{K}\frac{B_{2r}}{(2r)!}
\big[g_a^{(2r-1)}(N)-g_a^{(2r-1)}(b)\big]+R_a.
\end{aligned}
\tag{35}
\]

其中 `B_j` 为通过有理递推定义的 Bernoulli 数。令

\[
C_{2K}=\sum_{j=0}^{2K}\binom{2K}{j}|B_j|.
\]

因为 `B_(2K)(u)=sum_j binom(2K,j) B_j u^(2K-j)`，对 `0<=u<=1` 有 `|B_(2K)(u)|<=C_(2K)`。Euler–Maclaurin 的积分余项因此满足纯有理系数的上界

\[
\boxed{
|R_a|\le
\frac{C_{2K}(a)_{2K}}{(2K)!(a+2K-1)}
b^{1-a-2K}.
}
\tag{36}
\]

这里 `(a)_k=a(a+1)...(a+k-1)`。式 (35) 可由周期 Bernoulli 多项式逐次分部积分得到；其最后余项的绝对值不超过
`C_(2K)/(2K)! * integral_b^N |g_a^(2K)(t)|dt`，再将上限放到无穷即得 (36)。这使用的是明示、可计算的余界，不是假设渐近展开在截断后精确。

积分对 `a!=1` 是 `(N^(1-a)-b^(1-a))/(1-a)`，对 `a=1` 是 `log N-log b`；其它端点导数都是有理系数乘已包络的代数幂。锚点、阶数、Bernoulli 多项式粗界和每个最终余量都由脚本保存。

## 9. 新的有限证据及其精确范围

代码：`certify_arithmetic.py`。

结果：`arithmetic_certificate_results.json`，状态
`EXACT_INTEGER_ARITHMETIC_CERTIFICATES_PASSED`。

### 9.1 N=4096：全部人口与三种累计方式交叉核对

这个端点另行展开全部 `4095` 个非单位整数输入，使用原始素因子乘积计算道路，直接计算 `D_n-kappa_n` 及其 Green 权累计，并计算有限 Möbius 反演的整除项。三路严格区间相交；不是把同一个近似数打印三遍。

同时对 `2<=n<=4096` 的全部 `4095` 个 `b_kappa(n)` 和 `c(n)`，逐个严格认证了 (7)、(13) 的非零奇偶符号。小前缀递推方案只筛到 `256`，使用 `15` 个大商状态及 `785` 个递推商块。

### 9.2 N=1000000：没有展开全部百万道路的严格端点

此端点只使用上文的递推与幂和区间：

| 资源 | 实际数量 |
|---|---:|
| 小前缀筛界 | `10000` |
| 超过筛界的 Möbius 商状态 | `99` |
| 递推商块，四个指数共享同一块结构 | `36739` |
| 端点重建商块 | `1999` |
| 已缓存的大幂和查询，含谐和数 | `8715` |
| 代数根调用 | `1328` |

没有形成长度一百万的道路表或遍历全部目标整数。严格向外输出为

\[
\boxed{
-1599557.55961382081566258186439300
\le T_{1000000}\le
-1599557.55961382081566258186439299.
}
\tag{37}
\]

对应原 Green 带权累计为

\[
\boxed{
-213264.58478829131671873645594088
\le\sum_{n=2}^{1000000}(D_n-\kappa_n)(1000000/n-1)
\le-213264.58478829131671873645594087.
}
\tag{38}
\]

脚本还保存了未缩短的区间宽度上界。26 位小数的展示端点经过向外舍入；真实内部认证宽度更小。墙钟时间只作诊断，没有用未运行的百万道路基线来声称某个实测加速倍数。

### 9.3 没有从这些证据推出的结论

本轮固定 `h=1/16` 是算术认证的实例，不是与任意远窗口匹配的厚度族。一个百万端点、确定的奇偶层符号、或严格的商递推，都没有证明无限尺度正部能量满足次幂量词。

新增的研究目标可以由 (26) 精确表述为带真实 `q_+` 倍数核的奇偶层相关累计；新增的计算能力是对少量端点保存完整人口和前史的严格压缩求值。共同对消的数学控制仍须继续，而不能由逐项绝对值、局部符号或有限计算代替。
