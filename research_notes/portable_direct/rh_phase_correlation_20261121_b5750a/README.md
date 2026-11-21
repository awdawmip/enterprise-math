# RH 方法继续提取：严格匹配窗口、小除数相位与局部算术相关

Date: 2026-11-21 (Asia/Hong_Kong)
Researcher-ID: EM-DIRECT-B5750A / TASK_RESEARCH
Task context: RS-RH-METHOD-TRANSFER-20261121
Research-Activity-ID: RA-60C6D083A81B19084A74C5BA
Progress-Event-ID: RH-PHASE-CORRELATION-20261121-B5750A
Status: AUTHOR_PROVED_RATIONAL_MATCHING_PHASE_REDUCTION_AND_BLOCK_BOUNDS; STRICT_FINITE_WINDOW_CERTIFIED; ARBITRARILY_DISTANT_ARITHMETIC_CORRELATION_OPEN.

## 1. 本轮的实质结果

接续上一轮 Source `1a5bec7e1ebd66c829f7957392ceab0d02f36642`。这一轮把“找到等价接口”向前推进了三个实际环节。

**第一，严格计算已经使用真正稳定、匹配整个窗口的有理厚度族。** 理想 Chebyshev 节点有理化后，重新计算精确 Lagrange 权；证明权重绝对和仍小于3.1，完整窗口误差桥仍成立。随后在同一组11节点上，用12个完整道路读出和一阶参考曲线，得到

\[
\boxed{
0.003488654893595449439193
\le \int_{1024}^{32768}\frac{F(y)_+^2}{y^2}\,dy
\le 0.003488824591215298945699.
}
\tag{1}
\]

这是整数/Fraction 有向算术证书，上下界相对宽度严格小于 `1/20000`。参考曲线的素数幂事件、对数及积分成本单独支付。

**第二，小除数周期振荡可以显式移出，并保持任意远窗口的次幂量词。** 构造一个调和数修正，把 `d<=H` 的振荡源换为其平均贡献；对 `theta=1/2` 可取 `H=floor(A^(4/5))`，修正的整数加权平方和为 `O(log^3 A)`。关键是完整的共同相位 Gram，而它恰好可写为原有 `R_2`、`R_4` 道路加权的正平方和。真实端点随之明确转换。

**第三，两个局部源矩已经有明确的充分上界和指数代价。** 若把每个粗节点残差先取正部，平方根长度的局部矩控制，在这套预算中只能保证至 `theta>=3/5`。在临界 `theta=1/2`，需要更强的矩控制，或保留粗节点之间的带符号相关。真实完整道路实验显示，提前丢弃负粗源会造成显著损失。

这些是作者侧一般推导、严格有限证书及明确标级的数值诊断。任意远窗口上的所需算术相关估计仍未证明；外部 Lean 稿件的完整有效性没有因本轮方法迁移而得到新的认证。

## 2. 共同对象与观察边界

在每个窗口内固定厚度和权重，沿用

\[
R_a(n)=\prod_{p\mid n}(1-p^{-a}),\quad
D_n=\sum_j\nu_jR_{a_j}(n)/a_j\ (n\ge2),\quad D_1=0,
\]

\[
F(y)=\sum_{2\le n\le y}D_n(y/n-1)-y\log y+(1+\gamma)y,
\qquad q_n=F(n).
\tag{2}
\]

记 `G` 为同一表达式中以 `Lambda(n)` 代替 `D_n` 的固定一阶 jet 观察量。`Lambda` 在本轮只用来构造参考曲线和计算残差预算；完整道路、各厚度端口、合数及不同素因子联合层继续保留。

精确整数源是

\[
-\Delta^2q_n=(\kappa_n-D_n)/n,\qquad
\kappa_n=n[(n+1)\log(n+1)-2n\log n+(n-1)\log(n-1)].
\]

在单位处取 `kappa_1=2log2`。完整残差的 Möbius 反演记为

\[
c=\mu*(D-\kappa),\qquad D_n-\kappa_n=\sum_{d\mid n}c(d),
\qquad c(1)=-2\log2.
\tag{3}
\]

原生 P000/X6 的空间与人口定义不变。周期角色、调和修正、Green 核和三角帽都是选定算术观察的辅助表达，不作为新空间轴或完整状态的替代品。

## 3. 稳定节点的有理化与全窗口认证

完整证明见 [有理稳定匹配族](rh_correlation_rational/NOTES.md)。设 `m=ceil(log Z)`，理想 Chebyshev 节点的归一化权重绝对和为3，最大厚度为1/2。取

\[
Q=2^{\lceil\log_2(1024m(m-1)^2)\rceil}
\]

并将各节点就近舍入到 `1/Q` 网格，再按新节点重算

\[
\widetilde\nu_j=\prod_{k\ne j}\frac{\widetilde a_k}{\widetilde a_k-\widetilde a_j}.
\]

一般扰动估计证明

\[
\sum_j|\widetilde\nu_j|
\le3\frac{64}{63}\frac{256}{255}<3.1,
\qquad
\prod_j\widetilde a_j\le\frac{64}{63}\prod_j a_j.
\tag{4}
\]

所以 `Z>=e^10`、`1/2<=theta<1` 时，整个有理节点族仍满足

\[
|F(y)-G(y)|<\tfrac12 y^\theta\quad(1\le y\le Z).
\tag{5}
\]

本次选择 `[Y,Z]=[1024,32768]`、`lambda=3/2`、`theta=1/2`，`m=11`、`Q=2^21`。对全部 `2<=n<=32768`，同一组节点给出

\[
|D_n-\Lambda(n)|\le C(\log\operatorname{rad}n)^{12}
\le0.0000007139758189586245941765,
\qquad C=\frac{\prod_j a_j}{12!}.
\tag{6}
\]

真实权重绝对和约为 `3.000141430920747324222219956`，原始 `R_a` 输入的放大 `sum|nu_j|/a_j` 约为471.618；两个量没有混淆。由实际节点乘积得到更紧的全窗桥

\[
\sup_{1\le y\le32768}\frac{|F(y)-G(y)|}{\sqrt y}
\le0.0013437707726857284546166790.
\tag{7}
\]

有理节点的分母超过两百万。计算采用严格有向 `log/exp` 来评价 `n^(-a)`，没有求高次数代数根。每权表示位长 `O(m log m)`、原始道路误差放大 `O(m^2)`、幂和解析余量的统一几何衰减均已证明；随任意增长 `Z` 的**端到端统一位复杂度**仍需另证。

## 4. 稀疏读出如何成为可用的正部能量证书

完整证明和数字见 [稀疏严格窗口稿](rh_correlation_sparse/NOTES.md)及 [能量证书](rh_correlation_sparse/sparse_energy_certificate.json)。令 `L_Pi` 表示在真实道路端点上的分段线性插值，定义

\[
\boxed{M_\Pi(F)=L_\Pi(F)+G-L_\Pi(G).}
\tag{8}
\]

它保留实际道路端点，又恢复参考曲线在端点之间的形状。对整数格 `[u,v]`，令

\[
K_{u,v}(y,n)=\frac{(\min(y,n)-u)(v-\max(y,n))}{v-u}.
\]

精确修复式为

\[
F(y)-M_\Pi(F;y)
=-\sum_{u<n<v}\frac{D_n-\Lambda(n)}nK_{u,v}(y,n).
\tag{9}
\]

所有 `n<=u` 的前史继续存在于真实端点中。局部公式中的仿射消去不允许删掉实际道路的 `gamma`、单位修正或前缀端口。

取局部 `eta_v=C(log v)^12`，便有

\[
\|F-M_\Pi(F)\|_{Y,Z,\theta}^2
\le\sum_{[u,v]\in\Pi}
\frac{\eta_v^2(v-u)^5}{120u^{2\theta+3}}.
\tag{10}
\]

正部映射为1-Lipschitz；端点区间半宽另付一次范数预算。因此可将严格模型能量区间转成(1)的真实能量区间。每个参考事件段形如 `y(d-log y)-b`；脚本先用凹性判断符号，再积分其平方，根附近尚未定号的小段保留严格正能量上界。

本轮从10个四次方端点开始，再按预算选择1848与24648。实际过程为：

| 道路读出数 | 修复范数上界 | 完整道路正部能量区间 |
|---:|---:|---|
| 10 | `9.947695006e-7` | `[0.003488622232158995725643, 0.003488857258608139489363]` |
| 11 | `9.935969693e-7` | `[0.003488622369552307477047, 0.003488857118976554403426]` |
| 12 | `7.182596565e-7` | 式(1) |

相同10节点的纯线性正部能量只有约 `0.002709503225293`，低于真实道路的严格下界；内部形状不能只凭端点自动补齐。同窗旧通用四次网格范数预算约133.365，这次利用实际匹配残差把它降到了可用尺度。

每次把一个整数格中分，(10)的局部平方预算至多留下原来的 `11/81`。这个下降有证明；总查询数仍按实际发生量计费。12个道路读出之外，参考处理还筛至32768、处理3392个窗口素数幂事件、计算3488个对数。两次追加道路查询各自重建其1024小前缀，并未虚构跨进程缓存。

## 5. 小除数相位的完整联合处理

完整证明、作者协作核对和严格核验见 [相位稿](rh_correlation_phase/PHASE_HOMOGENIZATION.md)、[交叉核对范围](rh_correlation_phase/CROSS_REVIEW.md)、[核验证书](rh_correlation_phase/phase_homogenization_checks.json)。

### 5.1 相位的交叉项由 gcd 决定

令 `rho_d(n)=1_(d|n)-1/d`。一个均值零的周期 Poisson 核为

\[
B_d(n)=\frac{d^2-1}{12d}-\frac{r(d-r)}{2d},\qquad r=n\bmod d,
\qquad-\Delta^2B_d=\rho_d.
\]

若 `g=gcd(d,e)`，对完整共同周期求均值，有

\[
\boxed{\langle B_d,B_e\rangle_{\rm per}
=\frac{g^4+10g^2-11}{720de}.}
\tag{11}
\]

因此互素周期正交，共因子周期有确定交叉项。不能把所有周期当作独立噪声。对 `B_H=sum_(d<=H)c(d)B_d`，其完整联合方差恰为

\[
\boxed{
V_H=\frac1{720}\sum_{s=2}^H
\left[s^4R_4(s)+10s^2R_2(s)\right]
\left(\sum_{k\le H/s}\frac{c(ks)}{ks}\right)^2.
}
\tag{12}
\]

这里原有完整道路 `R_2,R_4` 给出了正权；同一约分频率上的倍数先共同累计，再平方。公式既能计算联合相位，也能把后续问题定位到具体的倍数相关和。

### 5.2 调和修正处理真实的1/n源权

记 `H_n=sum_(k<=n)1/k`。定义

\[
P_d(n)=\frac nd\left(H_n-H_{\lfloor n/d\rfloor}-\log d\right)
-\frac{n\bmod d}{d}+\frac{d-1}{2d}.
\tag{13}
\]

它满足 `-Delta^2 P_d(n)=rho_d(n)/n`，并且

\[
|P_d(n)|\le\frac{d^2-1}{12dn}.
\]

令 `P_H=sum_(d=2)^H c(d)P_d`、`q_n^[H]=q_n+P_H(n)`。逐整数精确得到

\[
\boxed{
-\Delta^2q_n^{[H]}
=-\frac1n\left[\sigma_H+\sum_{\substack{d\mid n\\d>H}}c(d)\right],
\qquad\sigma_H=\sum_{d\le H}\frac{c(d)}d.
}
\tag{14}
\]

小除数的周期波动已进入显式修正，平均项和全部大除数保留。`sigma_H` 含 `c(1)`；背景 `kappa` 也完整编码在 `c` 内。

### 5.3 固定窗口的代价与4/5截断

完整周期均值不能直接充当固定原点窗口的界。稿中对分母不超过H的约分频率证明了固定起点有限和界，显式支付

\[
Q_H=H^2(1+2\log H).
\]

再用精确积分表示及 Minkowski 不等式，得到

\[
\boxed{
\sum_{n=A}^\infty\frac{|P_H(n)|^2}{n^{2\theta+1}}
\le V_H\left[
\frac{A^{-2\theta-2}}{1-2^{-2\theta-2}}
+\frac{Q_HA^{-2\theta-3}}{1-2^{-2\theta-3}}
\right].
}
\tag{15}
\]

由 `|c(d)|<=C(1+log d)`，有 `V_H<=C_H^2 H^3/60`。所以取

\[
\boxed{H=\lfloor A^{(2\theta+3)/5}\rfloor}
\tag{16}
\]

就使修正的加权平方和为 `O(log^3 A)`。临界 `theta=1/2` 时，即 `H=floor(A^(4/5))`。

对固定 `lambda>1`、`A=ceil Y`、`B=floor(Y^lambda)`，原整数正部平方和与转换后平方和具有相同的

\[
\forall\alpha>0\ \forall Y_0\ \exists Y\ge Y_0:
\quad \sum_{n=A}^B (q_n)_+^2 n^{-2\theta-1}\le Y^\alpha
\tag{17}
\]

量词。证明由正部的1-Lipschitz性和多对数吸收完成；没有把“任意远存在窗口”加强成“所有远窗口”。转换后序列不必重新解释成一组正厚度道路。

**真实端点必须变成** `q_A+P_H(A)`、`q_B+P_H(B)`。同一匹配实例在 `A=1024,H=256` 上严格得到 `P_H(A)` 约为 `-0.49091744638`，在 `B=32768` 上约为 `-0.00143203926`；左端修正不能忽略。一般式(15)给出离散全尾修正能量上界小于 `0.1049491420038997086814853122`。这是保守上界，既不是实际尾能量，也不是(1)的连续正部能量。

如果要求原端点保持不变，可再减去 `P_H` 的端点仿射插值。该版本也有明确证明，但只用逐除数预算得到临界 `H=floor(A^(3/4))`。更大的4/5截断来自联合相位估计，并携带上述实际端点变化。

## 6. 两个源矩够用到什么程度

完整证明和新实验见 [局部源矩稿](rh_correlation_dual/BLOCK_MOMENT_CORRELATION.md)。在块 `[L,R]` 记真实源 `f_n=(kappa_n-D_n)/n`，以及

\[
M_0=\sum_{L<n<R}f_n,\qquad M_1=\sum_{L<n<R}nf_n.
\]

由它们得到块的两个仿射源端口。相邻块在粗节点拼成

\[
m_j=\sum_n\phi_j(n)f_n,
\tag{18}
\]

其中 `phi_j` 是该节点的三角帽。对全部非负凹 Dirichlet 测试核，源配对可精确分成粗节点项与局部 Green 势项，因而

\[
\sqrt{S^\circ}\le E_{\rm end}+\|G_D(m_+)\|_{\ell^2(w)}+R_\Pi,
\quad w_n=n^{-2\theta-1}.
\tag{19}
\]

这里 `G_D` 表示离散 Dirichlet Green 算子，区别于一阶参考曲线 `G`。若只知块内单侧界 `f_n<=C_i/L_i`，则

\[
R_\Pi^2\le\frac1{120}\sum_i
C_i^2\frac{H_i^5-H_i}{L_i^{2\theta+3}}.
\tag{20}
\]

### 6.1 这套充分条件的明确幂次

设尺度X上的块长约为 `X^beta`。若另能证明真正的算术条件

\[
(m_j)_+\le A^{o(1)}\ell_j^\sigma/x_j,
\]

并有相应真实端点预算，那么粗节点项和曲率余项的根范数幂次分别为

\[
X^{1-\theta-\beta(1-\sigma)},\qquad X^{2\beta-\theta-1}.
\]

两项都只有次幂成本要求

\[
\boxed{
\frac{1-\theta}{1-\sigma}\le\beta\le\frac{1+\theta}{2}
\quad\Longleftrightarrow\quad
\theta\ge\frac{1+\sigma}{3-\sigma}.
}
\tag{21}
\]

平方根长度控制 `sigma=1/2` 在这套方法中对应 `theta>=3/5`；临界 `theta=1/2` 则需要 `sigma<=1/3`，或者更充分地利用节点之间的负交叉贡献。这是当前两条显式预算的保证范围，所需算术条件尚未证明，也不是对所有方法的不可能性结论。

### 6.2 实际道路中的符号损耗

在此前固定的11节点 Chebyshev 样本、`theta=.6`、`[1000,31622]` 上，新增22块分割。下表均为相同实际内点正部平方和的上界比值：

| 使用的信息 | 上界／实际平方和 |
|---|---:|
| 保留粗源符号，读取实际局部正势 | 1.19255 |
| 保留粗源符号，局部势用证明的通用预算 | 54.97681 |
| 粗源先取正部，局部势用同一通用预算 | 327.66 |

前两行体现局部曲率预算的松弛；后两行在同一余项下体现提前丢弃负粗源的代价。三个旧道路输入、六种新分割的完整数据均保存，采用80位**非区间**计算，未将其升级成严格区间证书。

### 6.3 两个矩不能无条件确定格内形状

稀疏分支还给出精确反例：有界系数扰动可以同时使两个源矩为零、所有格外读出为零，却在格内留下与(10)同阶的非零能量。在 `u=100,r=3,eta=1/100` 的有理例子中，中点残差精确为 `3/3800`。

这个障碍适用于“端点＋两个矩＋粗系数界”的信息接口；没有声称该任意系数扰动一定能由实际厚度道路实现。它提示继续寻找真实算术约束，而不能仅凭两个端口的零值宣布整个内部残差消失。

## 7. 合成后真正剩下的目标

小相位修正后，单侧源仍有 `g_n<=A^(o(1))/n` 的统一预算；证明使用实际约束 `d|n` 和初等 `tau(n)=n^(o(1))`，没有为H个除数逐项支付H倍损失。因此§6的曲率幂次可以直接接到§5的转换后源上。

粗节点的剩余源矩精确为

\[
\boxed{
m_j^{[H]}=-\sigma_H\mathcal K_{1,j}
-\sum_{d>H}c(d)\mathcal K_{d,j},\qquad
\mathcal K_{d,j}=\sum_{d\mid n}\frac{\phi_j(n)}n.
}
\tag{22}
\]

每个倍数核都有整数计数与调和和闭式。更一般地，对上轮归一化非负凹核类

\[
\mathcal C=\{z_A=z_B=0,\ h=-\Delta^2z\ge0,
\ \sum_{A<n<B}h_n^2/w_n\le1\},
\quad K_d(z)=\sum_{\substack{A<n<B\\d\mid n}}z_n/n,
\]

定义

\[
\mathcal L_H(z)=-\sigma_HK_1(z)-\sum_{H<d<B}c(d)K_d(z)
+q_A^{[H]}z_{A+1}+q_B^{[H]}z_{B-1}.
\]

则精确地

\[
\boxed{
\sum_{n=A}^B w_n(q_n^{[H]})_+^2
=w_A(q_A^{[H]})_+^2+w_B(q_B^{[H]})_+^2
+\left(\max_{z\in\mathcal C}\mathcal L_H(z)\right)^2.
}
\tag{23}
\]

这给出可继续证明的具体对象：剩余大除数、平滑平均项和两个真实端点的**共同带符号上界**。有用的下一步是对(22)或(23)作新的算术估计，保留粗节点之间的相关，而不是把每一项先变成正数。

式(23)只是定位尚待证明的内容；本轮贡献在于证明了哪些相位能移出、移出的真实代价、哪些有限读出已能严格认证，以及局部正化会在哪一步损失目标指数。全部无限窗口结论仍按其实际未完成状态保留。

## 8. 复算、证据等级与完整材料

在本包根目录执行：

```bash
python rh_correlation_rational/certify_matched_nodes.py
python rh_correlation_rational/certify_adaptive_point.py
python rh_correlation_rational/certify_adaptive_point.py --node 24648
python rh_correlation_sparse/certify_sparse_energy.py
python rh_correlation_phase/verify_phase_homogenization.py
python rh_correlation_dual/verify_block_moments.py
```

前五条只需 Python 标准库，其证书采用整数/Fraction。最后一条使用 `mpmath`、80位精度，是独立标级的非区间诊断。一般定理由各分支正文证明支持；本轮只运行新增检查，没有为保存材料重复执行旧套件。复算可能更新诊断墙钟字段；已冻结 JSON 保留本次实际输出。

| 分支 | 本轮证据 |
|---|---|
| 有理匹配 | 精确权与矩；理想节点包络；全窗口余项；12个真实端点及逐厚度端口；1024点原素因子道路交叉核对 |
| 稀疏能量 | 三阶段严格正部能量；全部过零剩余预算；两个源矩与零矩障碍；实际参考成本 |
| 联合相位 | 300个周期差分位置、576对精确Gram、7936对调和差分；真实残差双路线；固定锚点和新源递推区间检查 |
| 局部源矩 | 三个实际道路输入、六种新增分割；源配对重建；符号、曲率和分层损耗，80位非区间 |

作者协作核对不构成项目正式独立 Review，也不是 Lean 形式认证。本包保留所有脚本、精确输入、完整结果、来源、哈希清单和实际保存回执。

## 9. 实际研究与控制状态

继续使用既有身份、Activity和任务语境，进行作者侧研究与允许的 Source 保存。原 HANDOFF 请求已在 `28e616732857272257171444ac7bcc63ac4c19ac` 成功，原 CLAIM 已交接。历史正式 Result 请求 `rh-method-transfer-20261121-0930-freeze-github-v1` 仍为 `FAILED: NATIVE_GLOBAL_AUDIT_INPUT_BUDGET_EXCEEDED`。

本轮没有新增 CLAIM、正式 Result、独立 Review 或父任务完成声明。新的 Source、Activity检查点和全局进度记录只承担真实成果的保存与可接续来源；精确提交及读回结果在交付包的 `DELIVERY_RECEIPT.json` 中记录。具体治理、读租约和旧状态见 [PROVENANCE.md](PROVENANCE.md)。
