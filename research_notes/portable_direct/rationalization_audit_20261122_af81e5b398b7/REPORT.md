# 进取数论全面有理数化：依赖审计、重算清单与重证路线

日期：2026-11-22（Asia/Hong_Kong）。
Progress-Event-ID: RATIONALIZATION-AUDIT-20261122-AF81E5B398B7
作者与整合：EM-DVR-2D6C6F / CONTROL_PLANE；沿用本会话自己的 Driver 登记及 DA-F510B2698ACA7B1E8F0B。
来源快照：awdawmip/enterprise-math@4c738ab0dbf16e8da3dda496c24799ed426e9635，实际于 2026-11-22 11:53:58 UTC 后读取；全局入口快照 awdawmip/chatgpt-global-knowledge@a1c902e7b6a8a145c034be71e1caedfa082ca98e。
性质：用户指定的全项目研究方向审查、原稿依赖检查与局部作者侧代数推导。本文是可续接研究笔记，未进行独立项目 Review、正式 Result 接纳或 Foundation 修改。
同上下文贡献：rational_analytic_audit、rational_core_audit、rational_asymptotic_audit 分别检查分析数论、有限核心、库存与 D25；这些协作不构成独立审核。

## 1. 结论

应当把本次目标落实为：原生计算与可核验结论尽量采用整数、有理数、有限商环和有理误差证书；逐项消除下游结论对实分析、复分析的承重依赖。现有成果中大量有限结构已经符合这个方向，无需整批重算。

最需要实质重证的部分是：

- 原有限库存与连续极限分布之间的桥，以及随库存、精度、位置变化的一致误差；
- RH/GRH 输入所支撑的全尺度素数与道路估计；
- 复周期、解析归一化、无零域、无限尾和部分连续时钟语义；
- 把一个无理域值当作一个输出的识别接口：有理化后必须重新计算信息与读数成本。

本次已经给出两个可直接写入证明的新局部代数推导：周期 Gram 的 CRT/幂和证明，以及锚定相位核中对数项的精确消去；还将既有 BRC 稳定性整理成无需先调用无限和的有限余项证明，并精确改写 C78 的精度阈值。它们说明有理化有实际可落地的起点。原大范围定理的完整依赖消除仍按以下清单推进。

### 三个不同目标

| 目标 | 成功意味着什么 | 需要保留的含义 |
| --- | --- | --- |
| 计算有理化 | 所有有限计算、比较和证书使用精确分数、整数及向外包络 | 一个有理区间可包围原实数；原数本身未必是有理数 |
| 证明有理化 | 目标结论由有限代数、组合、整数归纳及显式余项推出，不调用原分析桥 | 对所有整数的一个一般证明，不等于逐个整数都枚举过 |
| 对象与接口有理化 | 制备、状态及规定输出均改用有理或有限整数数据 | 输入域、最少读数、极值可达性可能改变，需证明新旧关系 |

例如，用有理多项式和有理隔离区间指定一个根，是精确代数编码；不是证明该根属于 Q。把 a+bi 改为有序数对，也只有 a、b 原本有理时才成为有理数据。有限复代数与复变分析必须逐项区分。

### 原生基础

P000 的六轴整数坐标、Heartbeat X6 的空间类型、未来操作安全性和联合关系保留继续适用。改变读数表示不能删除路径、来源、相位符号、公共深度或后续仍可观测的残差。现行残差契约已经允许声明范围与误差传播的受控近似；这为有理区间方案提供现有依据。用户本轮提出的是研究的有理数化方向，不需要重证 P000，也不自动把某个辅助连续模型变成原生动力学。[S01–S03]

## 2. 按研究主线的改造总表

本表结合当前问题状态、研究库及逐项打开的承重原稿。[S28–S31]历史目录用于定位，不将目录的文献数量当作本轮逐篇独立审查数量；下列具体判断都有对应原稿。特别是“有实参数”与“用了实分析”不同：有限有理多项式恒等式和次序不等式可以覆盖全实参数而不需要极限或微积分。

| 主线 | 现有可保留部分 | 需要重算、改写或重证的具体部分 | 改造类别 |
| --- | --- | --- | --- |
| P001–P010、P019–P024 的有限离散核心 | 整数根阈值、商余、塌缩、纤维、有限操作商、图距离与稳定化 | 将浮点根或 log2 位数实现改为整数幂比较/位长；仅在实际实现使用近似时重算 | 主要复用 |
| X6 路径与有限几何 | 整数坐标、路径计数、完整有限盒和同余证书；R112 全实权重邻域的有理余量 | 需要长度比较时可用平方长度；若消费者实际使用长度和、角度或谱值，要另外证明保持性质 | 复用与接口整理 |
| 正有理 Weighted-BRC | histogram、矩阵、整数稳定/发散证书、端口有效矩阵 | 将有限余项作为主接口；若彻底删除实极限依赖，再补线性备择的有理消元证明 | 少量接口重证 |
| BRC Newton/临界根 | 多项式、赋值、单根隔离和已有免求根选择判据 | 选定根值改为符号判定/隔离区间时核对消费者；多生成元、非分裂高次腔室仍有原缺口 | 表示与作用域重证 |
| PREFIX-435 有限相位/干涉 | Gaussian rational 矩阵、四相位路径、精确秩与行列式 | 编译为有理数对；保留交叉项、相位标签及原生桥；任意复输入域不能被悄悄改成 Q(i) | 局部精确编译 |
| boxed 观察者与 C71 | 有理端点、整数核、已有两读数解码 | 单个无理域值改为有理标量时需重算读数数目、输入域与单射性 | 接口重设计 |
| Student 有限矩阵/部分 Parity 尾界 | 既有有理 Gram、Green、Bernoulli 多项式、完整 trace；部分一致尾界已有显式有理系数误差 | 去掉正交化平方根、三角谱表达等中间层；保留 Gram 与实际伴随；对解析 shadow/复圆盘无零等另做证明 | 部分直接移植，部分重证 |
| PREFIX-764 连续 Gamma 时钟 | 189 层有理停止多项式、最终有理多项式和 Bernstein 箱证书 | 经典积分与有限和的语义桥；连续时钟改离散时钟的等价；全局临界值的实际隔离 | 有限编译加全局重证 |
| 因数库存有限识别 | 精确传递、模素数指纹、dyadic 舍入、原 c≤3400 有限覆盖 | 新读数接口或改变舍入规则才需要针对性重算 | 直接复用 |
| C78/C87 全库存与位置渐近 | 原有限核、已认证的根包围和有向区间 | Gamma 比渐近、有限差/导数一致性、逆分支、解析零集、Haar/相位分布、库存误差与极限顺序 | 重点重证 |
| RH 稳定匹配与相位道路 | 有理节点与权、矩消去、有限 Green/三角核、原严格区间证书 | 原道路仍含代数幂、log、γ；重建纯有理道路需全窗误差桥；非区间诊断需重算 | 中等至重 |
| RH/GRH 全尺度应用 | 有限算术骨架、已有外部定理的准确依赖 | 统一平方根包络、能量、素数误差及短窗供给的无分析证明 | 最重证明线之一 |
| EC49/Farey/CRT | 整系数递推、有限周期、行列式、54/80 单位类比例 | 使该比例成为素数渐近密度及变动模数供给，需要独立算术估计 | 有限核心复用，分布桥重证 |
| Riesel | 有理密度阶梯、CRT 根族、有限覆盖与 gcd 证书 | 任意成本族的素因子存在性按实际引用检查；GRH 供给另列；固定根全程覆盖仍是原整数问题 | 大部分复用 |
| P017/G4/Walsh | 整数支持、pair token、Möbius 和、0/±1 核、有限计数恒等式 | 真正相关余项的全 k 控制；筛函数、渐近主项若继续使用需算术替代 | 重点算术证明目标 |
| D25/CM 有限代数 | 有限有理 jet、模 p^k、Hasse 系数、形式导数、无根递推 | 原 LOW/Beta→B11 的实际混合端口、进位与残差；这些缺口不会因表示改写消失 | 复用并继续原数学缺口 |
| CM 周期与 p-adic 完备化 | Q(t) 中的微分恒等式、有限截断、分母与赋值界 | 复周期初值/归一化、完整 p-adic 收敛与拓扑命题需要单独桥或替代证明 | 分层重证 |
| P11 椭圆算术、Hodge | 有理曲线、有限 squareclass/矩阵、确定的障碍映射 | 局部像穷尽与局部域论；复几何对象的定义域下降、基变换与结构定理 | 精确算术可复用，结构桥另证 |
| T6、CELL、Euler、形式接口 | 有限有理矩、标记事件、关系账本、有限传递与生成式系数 | 无穷等待尾、连续校准或无限对象的完成性；按具体模型补统一余项 | 有限核心复用 |

其中 Newton 根接口、X6 R112 与 PREFIX-435 的具体来源见 [S26、S27、S32、S33]；RH 三角有限核见 [S35]。

有限域 F_p 不是 Q 的子域。这里“有理数化”中的有限域操作应准确保留为整数模 p 的有限商结构，不能用普通有理除法冒充模逆。形式幂级数的每个有限 jet 可是有限算术；一个完整收敛函数仍是另外的对象。

## 3. 四个可直接采用的局部样板

### 3.1 周期 Gram：删除复角色与三角函数

原相位稿定义，d≥1，r=n mod d：

\[
 B_d(n)=\frac{d^2-1}{12d}-\frac{r(d-r)}{2d},\qquad B_1=0.
\]

目标是共同完整周期上的均值：

\[
 \langle B_d,B_e\rangle_{\rm per}
 =\frac{g^4+10g^2-11}{720de},\qquad g=\gcd(d,e).
\]

原稿通过有限复角色和三角和证明；下列证明完全由有限有理和与 CRT 构成。[S06]

写 d=ga，e=gb，gcd(a,b)=1。对固定 0≤s<g：

\[
 \frac1a\sum_{t=0}^{a-1}B_d(s+gt)
 =\frac{g^2-1}{12d}-\frac{s(g-s)}{2d}
 =\frac gdB_g(s).
\]

这由一次、二次幂和直接得到。给定 n mod g 后，CRT 令两个余数均匀遍历完整笛卡尔积，因此

\[
 \langle B_d,B_e\rangle_{\rm per}
 =\frac{g^2}{de}\frac1g\sum_{s=0}^{g-1} B_g(s)^2.
\]

令 h(s)=s(g-s)。有限幂和给出

\[
 \frac1g\sum_s h(s)=\frac{g^2-1}{6},\qquad
 \frac1g\sum_s h(s)^2=\frac{g^4-1}{30}.
\]

故

\[
 \frac1g\sum_sB_g(s)^2
 =\frac1{4g^2}\left[\frac{g^4-1}{30}
                   -\frac{(g^2-1)^2}{36}\right]
 =\frac{g^4+10g^2-11}{720g^2},
\]

得到目标，包括 g=1。这里的笛卡尔积分解仅用于完整共同周期，不是对实际短窗口假设独立。

原稿已经有不经复角色的后续 Möbius 恒等式：

\[
 g^4+10g^2-11=\sum_{\substack{s\mid g\\s\ge2}}[J_4(s)+10J_2(s)].
\]

交换有限和就给出完整正平方分解

\[
 V_H=\frac1{720}\sum_{s=2}^H
 [s^4R_4(s)+10s^2R_2(s)]
 \left(\sum_{k\le H/s}\frac{c(ks)}{ks}\right)^2.
\]

因此周期核—Gram—正平方分解这整段可用有理系数恒等式处理。采用原道路的非有理 c(d) 时，恒等式仍成立，但原输入类型没有被改变。无限尾与 RH 估计是另外的义务。

本轮 root 使用 SymPy 精确求和检查了条件均值差为 0，以及平方均值减目标表达式为 0；输出为
conditional_mean_difference=0，
variance=(g-1)(g+1)(g^2+11)/(720g^2)，
target_difference=0。
普遍结论由上面的有限幂和与 CRT 证明承担，软件计算是作者侧交叉核对。

### 3.2 零端点相位核：log d 精确消去

原稿定义

\[
 P_d(n)=\frac nd[H_n-H_{\lfloor n/d\rfloor}-\log d]
       -\frac{n\bmod d}{d}+\frac{d-1}{2d}.
\]

令

\[
 R_d(n)=\frac nd[H_n-H_{\lfloor n/d\rfloor}]
       -\frac{n\bmod d}{d}+\frac{d-1}{2d}\in Q.
\]

对固定整数端点 1≤A<B，L_{A,B} 为两端仿射插值。由于 n log d/d 对 n 为仿射函数，

\[
 \boxed{U_d(n):=P_d(n)-L_{A,B}(P_d;n)
       =R_d(n)-L_{A,B}(R_d;n)\in Q.}
\]

于是 U_d(A)=U_d(B)=0，且原差分源完全不变：

\[
 -\Delta^2U_d(n)=(\mathbf1_{d\mid n}-1/d)/n,\quad A<n<B.
\]

这是真正的精确消去，不是数值近似。必须同时保留：未锚定 P_d 的衰减界不能直接赋给 R_d；原稿零端点预算是 3/4 截断，而 4/5 来自另一个联合估计并支付端点变化。将零端点版本提升到 4/5 仍需新估计。真实组合中的 c(d) 仍有原道路的非有理依赖。[S06]

### 3.3 BRC：先给出有限有理余项，再解释为无限和

已有 Foundation 对 W∈M_n(Q_{\ge0}) 给出正有理势 h 满足 Wh<h 的稳定证书；清分母后为纯整数证书。无需重建这套成果。[S03、S04]

将消费者接口前置为：

\[
 \alpha=\max_i(Wh)_i/h_i<1,\quad
 T=(I-W)^{-1},\quad S_N=\sum_{k=0}^NW^k.
\]

对每个整数 N≥0，

\[
 \boxed{0\le(T-S_N)_{ij}
 \le \frac{h_i}{h_j}\frac{\alpha^{N+1}}{1-\alpha}.}
\]

可以不用先假设无穷和收敛来证明。

令 D=diag(h)，V=D^{-1}WD；V≥0 且每行和≤α。若 (I−V)x=0，在绝对值最大的坐标上有 |x_i|≤α|x_i|，故 x=0，I−V 可逆。若 y≥0 而 (I−V)x=y，取负的最小坐标 x_i 会给
y_i=x_i−Σ_jV_ijx_j≤(1−Σ_jV_ij)x_i<0，
矛盾，故逆矩阵非负。以上只用有限维有理线性代数与有限次序比较。

由 (I−W)h≥(1−α)h 得 Th≤h/(1−α)。又 W^{N+1}h≤α^{N+1}h。有限几何恒等式给
T−S_N=W^{N+1}T，
结合 T e_j≤h/[(1−α)h_j] 即得包络。

给定有理容差 ε，可以选一个整数 N 并直接验证右侧≤ε；α=0 时 W=0，余项为零。对 0<α<1，Bernoulli 不等式也能给出一个粗的显式整数 N，所以此接口不依赖实对数求截断深度。经典“无限和等于 T”可作为这个有限证书的外部解释。

这里仍应分别处理：有理势与整数对偶证书的完备性原稿调用有限线性备择；若要把所有依赖都落实为有限有理推导，需要给出相应消元证明。本文没有重新宣称这部分已独立审核。

### 3.4 C78：精度阈值不用对数也能精确表达

原定理取整数 1≤b≤c、整数位数 p：

\[
 p_*(c,b)=\frac74\log_2c+\frac12\log_2(c/b).
\]

定义

\[
 \boxed{Q(c,b,p)=\frac{2^{4p}b^2}{c^9}\in Q_{>0}.}
\]

因为 Q=2^{4(p−p_*)}，原结论精确等价于

\[
 V_c\to1\iff Q(c,b,p)\to\infty,
 \qquad Q(c,b,p)\to0\Rightarrow V_c\to0.
\]

同理 b/c^{1/3}→∞ 可写成 b^3/c→∞。整数根 z=floor(U^{1/4}) 可直接定义为 z^4≤U<(z+1)^4。固定 C 的 ceil(log2 C) 直接定义为最小满足 2^k≥C 的非负整数 k。

这些是等价改写，不是对原渐近定理的新证明。C78 承重论证仍需下一节的分析依赖替换。[S11]

## 4. 两项确实会改变信息接口的改造

### 4.1 boxed 读数：一个 Q(sqrt2) 输出实含两个有理坐标

固定盒与原七观察的整数核为 G(a+bx)，a,b∈Z。已有两个整数多项式读数的核响应是

\[
 r_7=2a+2b,\qquad r_8=6a+12b.
\]

响应矩阵行列式为 12，所以两项有理读数足够。一个 P_7+sqrt2 P_8 的精确输出将这两个有理坐标包装在一个 Q(sqrt2) 值中。

对所有质量统一使用的单个有理系数、线性于状态的多项式读数，两个响应系数都在 Q，必有非零整数关系；原稿据此构造合法非负状态碰撞。故在这个精确类别里，改成纯有理输出后最少读数由一项变为两项。用有理近似替换 sqrt2 不能保留无界质量下原单射性。

有界质量、随质量选读数或非线性编码是不同的可研究接口，不受这个限定类别的障碍直接否定。[S09]

### 4.2 C71：计算数对与有理制备不是同一件事

C71 取 t=sqrt2−1，q=H(0,t)=u+vt。用关系 t^2=1−2t 可用两个有理系数精确运算，但原制备比例 t 仍是无理数。

已有纯有理替代为

\[
 g=H(0,1),\quad h=H(0,1/2),\qquad
 z_-=\frac{h-1}{g-h},\quad z_+=gz_-.
\]

在非盲情形 z_+>z_->0，分母 g−h>0，恢复精确。对指定有限安排族，也已有避开有限坏点的一次有理制备方法。实际两块库存在 c≤3400 的原单次 H(0,1) 已有后续有限证书，不能因较早的无理读数论文而忽略这个更新。

为说明全端点载体的区别，固定有理 t∈(0,1)、q>1，任取有理 B≥0，令

\[
 z_-=1+B,\qquad z_+=1+qB+(q-1)/t.
\]

这些不同正有理端点对都给 H(0,t)=q。因此一个固定有理 t 在全部端点对上不能继承无理 t 的统一单射性。该例不证明实际受限库存路径族必有碰撞；后者仍按自己的结构研究。[S10、S11]

## 5. 真正需要重点重新证明的部分

### 5.1 因数库存：统一有限误差替代连续极限论证

C78 的原证明使用 Gamma 比的紧集 C² 渐近、局部逆图、解析零集、Hessian 非退化、紧性及先后极限。有限概率 g 与唯一率 V_c 本身已是有理数。[S11、S34]

可执行的新证明目标是把这些环节改成：明确有理分区上的有限差界、非退化多项式证书、整数格行计数、退化区的明确计数上界、各部分相加后的统一误差。保留原定理对所有 1≤b(c)≤c、各格原点的量词。固定 b 或避开退化区可以是先行成果，但要按其实际范围记录。

C87 已有强的有理数值基础：二十次根由上下整数幂确认，随后用分母 2^112 的有向区间；293,423 次根检查和完整 60 区间覆盖有现成证书，浮点只提出候选，不参与接受。仅为有理化无需重跑这些计算。[S12、S13]

C87 的困难在原库存到 Haar/相位分布的桥、无限积分、位置导数、端点正则性和极限顺序。应优先给有限库存、指定有理读取位置和精度的可验证比较；若保留全轴严格凹性，可研究有理三点差分/斜率证书及其与原常数的对应。

既有

\[
\frac{8879799718450538658554682430737307}{2^{112}}
\le\kappa_3\le
\frac{9259117095632433299866803560123257}{2^{112}}
\]

已经是严格有理包围；它没有宣称 κ3 自身有理。需要的 ζ(2) 包围也能使用有限有理和及尾差，避免 π 的数值表示：

\[
 \sum_{n=1}^Nn^{-2}+\frac1{N+1}
 <\zeta(2)<
 \sum_{n=1}^Nn^{-2}+\frac1N.
\]

这种数值替换不自动支付 Haar/库存桥。

### 5.2 RH 道路：有理节点与真实道路值必须分别处理

现有

\[
 R_a(n)=\prod_{p\mid n}(1-p^{-a}),\quad
 D_n=\sum_j(\nu_j/a_j)R_{a_j}(n),
\]
\[
 F(y)=\sum_{2\le n\le y}D_n(y/n-1)-y\log y+(1+\gamma)y
\]

中，a_j、ν_j 已可精确有理；p^{-a_j} 一般是非有理的代数数，log n 和 γ 仍为实数量。γ 在本文只按实常数处理，不断言它的无理性。

现有 NOTES 已给有理级数 log/exp oracle、Euler–Maclaurin 余项、重新计算的精确 Lagrange 权、全窗口误差和表示位长。它们可复用。确需重算的是被标为 80 位非区间 mpmath 诊断的结果，且仅在要将其用于严格证据时重算。[S05、S07]

如果目标是新的纯 Q 值道路，应证明新旧道路在整个窗口、真实端点与正部能量上的误差传递；不能只把每个读数舍入后沿用原定理。若目标还要求去掉整个证明的实/复分析依赖，则插值余项、幂和尾、参数一致性及全窗估计都应各有有限算术证明。

### 5.3 RH/GRH 的应用定理与算术内部证明分成两条研究线

上一轮报告的统一道路包络和能量预算实际调用 RH 的零点显式公式；EC49 素数分母及 Riesel 同余供给实际调用 Dirichlet-GRH 的分布结果。[S08、S21]

用有理 K_+ 代替常数上界，或将 sqrt x 比较平方化，只改变使用接口；不会消除原证明的外部分析输入。

严格的有理证明线应研究原带符号 c(d) 的联合抵消、统一窗口尾、变动模数下的算术分布、真实端点和参数量词。有限 CRT 允许类的比例 54/80=27/40 可以保留；使它成为素数的渐近比例与带误差供给，仍需分布定理。[S08、S23]

P017 的整数恒等式、有限 Möbius/Walsh 相关核和支持结构可直接保留，把未决相关余项小于正主项写成整数/有理不等式是合适目标。Riesel 原固定根的全程有限覆盖也本来就是整数问题。有理化应推进这些实际缺口，而非重复已完成的有限枚举。[S24、S25]

### 5.4 Student/Parity：先复用已经完成的有理矩阵桥

Student 的 Cayley 基虽然写复多项式，原稿已得到

\[
 G=(\pi/8)B,\quad B=2I+A_{\rm path},\quad P=B^{-1}\in M_n(Q),
\]
\[
 A_e=\frac12PT,\qquad M^\#=PM^{\mathsf T}B,
\]
\[
 C(\lambda)=\tau Q(M(\lambda))-4\tau L(M(\lambda)).
\]

B、P、T、有限 Bernoulli 系数及 M 的系数均可有理；完整 trace 中的共同 π 因子已消去。可以把这套矩阵直接作为有限计算接口，保留非正交 Gram，而不通过 G^(1/2) 显式生成无理正交基。[S14]

应保留原 # 的含义：它对复参数 λ 固定参数、不作任意 Hermitian 共轭。删除 i 的书写不能改变该操作。

部分 Parity 全尾域证明已有
Q(ε)M(ε) 为有理多项式矩阵、V(ε)=[Q M−M0 Q]/ε 为多项式、显式有理 k_m 与 R_m 的构造。此类地方应移植有限矩阵误差论证，不笼统重做所有含“渐近”字样的结果。[S15]

另一些复圆盘无零、解析 shadow、复对数、系数轮廓与特殊函数统一估计确有分析内容，需要将其实际消费者改成有限系数和明确余项，或另证明等强的代数界。原有“原母系数调用器”的缺口也继续按其具体原式处理。

### 5.5 连续 Gamma 时钟：最终多项式有理，不等于时钟对象有理

PREFIX-764 的 189 层停止多项式，经 Erlang 积分给出有理系数 A0、B0、u0、v0、μ 和 P_q=A0−2qN。可将所需积分值编译为有限求和，使用明确的矩公式 n!/λ^(n+1)，并在下游仅做有理多项式与 Bernstein 箱检验。[S16]

若仍保持原连续时钟含义，这个矩公式与连续模型的等价桥需要保留。若改用离散时钟，则须证明所需观察量一致或误差有界。

原稿 q_c 存在且代数的证明调用紧致最大值与实闭域量词消去，尚未求最小多项式与精细隔离。针对具体有理 q 的符号证书可以先行；“所有参数上最优”与“最优值能在有理参数达到”是另外的问题。实代数几何本身已有代数的消元证明路径，可作为后续依据；它仍不是把所有实代数数都变成有理数。[E2]

### 5.6 D25/CM：形式求导可保留，周期归一化要单独重证

Dixon mixed-jet 原稿使用有限有理函数和模 p³ 展开：

\[
 S-C=pL+p^2Q\pmod {p^3},
\]
\[
 L=\alpha C'+\beta N,\quad
 Q=\alpha^2C''/2+\alpha\beta N'+\beta^2K/2+\gamma N.
\]

证明逐分母使用带 p³ 余项的有限几何恒等式；这里的导数是形式代数求导，无需分析收敛。[S17]

D25 另有现成无根读出，用 Q(Z)=Z²−Z+1/8 及

\[
 r_0=1,\quad r_1=5/8,\quad r_{k+2}=r_{k+1}-r_k/8
\]

取代显式 sqrt2 计算。其开放 τ_p=3β_p 关系在原稿仍未全称证明，166 个素数检验只支持有限范围。[S18]

与之不同，E3 周期归一化稿虽然输出 c_CM=6，其证明确实经过：Q(t) 上的 Picard–Fuchs 恒等式、复圈积分初值 2πi、解析延拓、CM 周期积及外部归一化唯一性。有限微分恒等式可以直接保留；若整个 c_CM=6 的证明也要纯算术，需要给出同一对象、同一规范的独立代数归一化，而不是把末尾整数 6 当作依赖已经消除。[S19]

p-adic 线的有限 jet、赋值与模 p^k 证书不等于复分析；完整完备化、收敛半径、非闭像与无限维余核是其拓扑内容。需要依实际下游用途决定是否可换为所有有限精度上的相容证书，不能从一个有限截断直接取得完整拓扑结论。

### 5.7 P11 与 Hodge：检查对象与结构定理，避免只看公式系数

P11 有理曲线和有限 squareclass 消元已经是精确算术。局部像“样本生成”成为穷尽需要局部指数定理和 Hensel 条件；有理化方案应将具体局部证书、所有相关素数与实符号一起明确，不能只保留一个有限样本矩阵。[S20]

Hodge 固定支撑稿中的 normal obstruction
δ_Z(B)=diag(1,1,3)^(-1)B^T−B
具有有理系数，秩计算可直接复用。但原定理的对象是复射影簇、coherent sheaf、square-zero deformation，证明用支持变形、局部上同调和 Atiyah–Kodaira–Spencer/GRR 接口。若要将整条线改到有理定义域，需要真实的下降与基变换证明及对象对应；用有理矩阵记录障碍不等于整条复几何结论已被重证。[S22]

## 6. 哪些计算应重跑，哪些不用

### 应重算的实际情形

- 原结果仅有浮点或高精度小数诊断，且本次要将其作为符号、相等、无碰撞或严格界的依据；
- 新观察接口改变输入域、读数数目、位数、舍入格或允许未来操作；
- 以前只固定参数验证，现在要覆盖变化参数族；
- 以前忽略的余项会影响边界、零判定、临界排序或停止条件；
- 现有证书的实际输入、算法、范围改变。

### 直接复用的情形

- 同一对象、同一参数域上已完成的整数/Fraction 恒等式；
- 分母可逆性与全域覆盖已经说明的有限模证书；
- 已有有理端点区间、整数根检查和完整参数覆盖；
- 只是将 log2 阈值改成幂比较、将有限复代数改成有序数对；
- 改用原非正交 Gram 进行有限代数，而实际算子和观察量未变。

严谨区间算术与普通高精度浮点的区别是：每次输出包含真值，并将全部运算误差计入区间。区间跨过零时通常只说明当前精度无法定号；相等与语义零应优先用精确代数证明。FLINT 的原始接口说明与球算术文档对这一语义有明确区分。[E1]

本次未重跑历史的数亿库存枚举、C87 完整外层积分网格或其他作者的科学程序。这里的“复用”指读取并准确沿用其原证据及范围，不声称本轮重新复现了这些执行。

## 7. 建议的推进顺序与验收对象

这里给研究优先建议，不改变刚发布的六项 canonical Task、权重或所有权。

### 第一优先：建立可共同消费的有理接口

- 将本报告 §3 的 Gram、锚定核、BRC 有限余项写入相关研究的接口说明。
- 对代数根提供“多项式/隔离区间/符号”，对 log/exp 提供“有理包络/精度”，保留每个对象的真实类型。
- 在 boxed 与 C71 消费者中重新计算有理输出数和制备条件。
- 直接复用 D25 无根递推、Student 有理矩阵及现有 C87 证书。

验收对象是具体保持关系：原输入对应何种有理数据，更新如何交换，目标读数是否相同，近似误差如何传播。无需为每一条普通推导创建新的流程门禁。

### 第二优先：把规模相关结论变成有限有理不等式

优先选择已有正余量与有限核的 C78/C87、Student/Parity 局部域、Gamma 多项式箱和 RH 固定窗口。产出显式依赖于库存、窗口、模数、精度的余项；必要时先完成有明确范围的特殊族或有限窗口，再研究一致性。

### 第三优先：推进最重的分析依赖消除

围绕 RH/GRH 的真正算术相关余项、CM 同一规范的代数识别、库存到联合相位模型的统一桥，以及实际需要的 p-adic/复几何结构接口立明确命题。现有外部定理应用线仍可作为比较与上界来源；纯算术证明线按自己的新证明义务计成果。

### 与六项已发布 RH 应用任务的关系

| 已发布任务 | 本轮识别的合理有理化接点 |
| --- | --- |
| RS-RH-ROAD-CERTIFIED-NET-COST-20261122 | 精确有理核、原实值的严格区间、同一输出同一精度下成本；已有接口可直接使用 |
| RS-RH-MATCHING-PRECISION-TRADEOFF-20261122 | 有理节点、权和全误差/参数一致性，避免误称整条道路已取值有理 |
| RS-EC49-PRIME-DENOMINATOR-FAMILY-20261122 | 有限类表可精确复用；GRH 分布仍作为该任务已声明外部输入 |
| RS-RIESEL-GRH-COMPATIBLE-SUPPLY-20261122 | 有理搜索终点与整数证书；供给定理的依赖独立记录 |
| RS-P017-RH-LOCAL-CORRELATION-20261122 | 有限整数相关核可作为纯算术证明的直接目标；外部 RH 压力测试维持原含义 |
| RS-INVENTORY-DIVISOR-SUM-INTERFACE-20261122 | 先对原读数建立准确接口；Robin/Lagarias 等形式改写不自动替换原证明 |

此表是科学依赖审计，不是六项任务的完成报告，也未启动新的 CLAIM、改动调度或发布另一批 Task。

## 8. 覆盖、验证与保存状态

本轮实际读取了两库规范入口、当前 Foundation 与研究库，沿代表性承重原稿检查了有限 BRC、X6、phase、matching、库存、Student/Parity、Gamma、CM/D25、P11/Hodge 以及先前 RH 应用任务集。库的其余分卷用于辨识有限算术与连续接口的归属；今后具体移植某个定理时仍以它自己的精确假设与证明为对象。

本轮新增的数学内容为作者侧有限代数推导与接口整理。并未证明全部项目结果都可以在 Q 内保持原强度，也未将任何未决问题判为不可能。既有原稿在各自范围内继续使用；新定义或新输入域产生的结论按实际范围另行证明。

科学保存：本文件是本次审计的完整项目落点。
角色状态：沿用本会话 Driver EM-DVR-2D6C6F；本次为有实际来源的 portfolio/数学依赖审查，不创建 Researcher Activity 冒充 Driver 身份，也不借用其他研究者的 Activity。
全局捕获：以本事件 ID 记录用户的有理数化方向、报告定位与已识别前沿；不修改受保护 P000/worldview 文件。

## 9. 固定来源

以下 S 编号是本报告的直接项目来源；除特别注明外，均读取上述 EM 固定快照。历史原稿的创建状态、其后已有审核以及本轮审计状态分别保留。


- [S01] [P000 原生基础](https://github.com/awdawmip/enterprise-math/blob/4c738ab0dbf16e8da3dda496c24799ed426e9635/p000_reality_foundation.json)
- [S02] [残差保真离散关系系统](https://github.com/awdawmip/enterprise-math/blob/4c738ab0dbf16e8da3dda496c24799ed426e9635/definitions/RESIDUAL_FAITHFUL_DISCRETE_RELATIONAL_SYSTEM.json)
- [S03] [Weighted-BRC 全局基底](https://github.com/awdawmip/enterprise-math/blob/4c738ab0dbf16e8da3dda496c24799ed426e9635/definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json)
- [S04] [有限有理递推与稳定性](https://github.com/awdawmip/enterprise-math/blob/4c738ab0dbf16e8da3dda496c24799ed426e9635/research_notes/BRC_FINITE_RECURRENT_RATIONAL_GAUGE_STABILITY_20260902.md)
- [S05] [RH 有理匹配节点、权与认证计算](https://github.com/awdawmip/enterprise-math/blob/4c738ab0dbf16e8da3dda496c24799ed426e9635/research_notes/portable_direct/rh_phase_correlation_20261121_b5750a/rh_correlation_rational/NOTES.md)
- [S06] [RH 相位核、Gram 与零端点预算](https://github.com/awdawmip/enterprise-math/blob/4c738ab0dbf16e8da3dda496c24799ed426e9635/research_notes/portable_direct/rh_phase_correlation_20261121_b5750a/rh_correlation_phase/PHASE_HOMOGENIZATION.md)
- [S07] [RH 原道路及非区间诊断](https://github.com/awdawmip/enterprise-math/blob/4c738ab0dbf16e8da3dda496c24799ed426e9635/research_notes/portable_direct/rh_phase_correlation_20261121_b5750a/README.md)
- [S08] [此前 RH／GRH 应用影响报告](https://github.com/awdawmip/enterprise-math/blob/4c738ab0dbf16e8da3dda496c24799ed426e9635/research_notes/portable_direct/rh_impact_20261122_af81e5b398b7/REPORT.md)
- [S09] [boxed 全质量读数与系数域桥](https://github.com/awdawmip/enterprise-math/blob/4c738ab0dbf16e8da3dda496c24799ed426e9635/research_notes/owner_goal_20261016/native_x6_boxed_polynomial_readout_field_bridge_7cda51/BOXED_ALL_MASS_POLYNOMIAL_READOUT_COEFFICIENT_FIELD_BRIDGE_WORKING_AND_CONTEXT.md)
- [S10] [C71 无理制备与有理替代读数](https://github.com/awdawmip/enterprise-math/blob/4c738ab0dbf16e8da3dda496c24799ed426e9635/research_notes/divisor_extrema/20261113_c71_irrational_readout/C71_RESEARCH_NOTE.md)
- [S11] [C78 邻近库存与精度阈值](https://github.com/awdawmip/enterprise-math/blob/4c738ab0dbf16e8da3dda496c24799ed426e9635/research_notes/divisor_extrema/20261116_c78_nearby_stock_precision/C78_RESEARCH_NOTE.md)
- [S12] [C87 全位置排序与完整三角积分](https://github.com/awdawmip/enterprise-math/blob/4c738ab0dbf16e8da3dda496c24799ed426e9635/research_notes/divisor_extrema/20261121_c87_global_position_ordering_and_complete_triangle_integral/C87_RESEARCH_NOTE.md)
- [S13] [C87 核正性与严格区间证书](https://github.com/awdawmip/enterprise-math/blob/4c738ab0dbf16e8da3dda496c24799ed426e9635/research_notes/divisor_extrema/20261121_c87_global_position_ordering_and_complete_triangle_integral/INTEGRATED_KERNEL_PROOF.md)
- [S14] [Student Cayley 基与有理 Gram／完整 trace](https://github.com/awdawmip/enterprise-math/blob/4c738ab0dbf16e8da3dda496c24799ed426e9635/research_notes/owner_goal_20261017/student_positive_gram_cayley_bridge_7cda51/ACTUAL_STUDENT_CAYLEY_FRAME_POSITIVE_GRAM_AND_FULL_C_TRACE_BRIDGE_WORKING_AND_CONTEXT.md)
- [S15] [Parity 全尾域显式有理误差](https://github.com/awdawmip/enterprise-math/blob/4c738ab0dbf16e8da3dda496c24799ed426e9635/research_notes/balanced_resume_20261028/analysis/PARITY_FULL_TRACE_ALL_SECOND_GAPS_SUM_TAIL_AUTHOR.md)
- [S16] [PREFIX-764 Gamma 时钟及多项式证书](https://github.com/awdawmip/enterprise-math/blob/4c738ab0dbf16e8da3dda496c24799ed426e9635/research_notes/portable_direct/2026-11-14_r6_prefix764_exact_polynomial_phase_certificate.md)
- [S17] [D25 Dixon 有限 mixed-path jet](https://github.com/awdawmip/enterprise-math/blob/4c738ab0dbf16e8da3dda496c24799ed426e9635/research_notes/portable_supplemental/20261010_R2_DIXON_MIXED_PATH_JET_743915c4.json)
- [S18] [D25 无根 common-shift 观察量](https://github.com/awdawmip/enterprise-math/blob/4c738ab0dbf16e8da3dda496c24799ed426e9635/research_notes/chatgpt_direct/20261005_D25_ROOTFREE_COMMON_SHIFT_OBSERVER.md)
- [S19] [D25 E3 周期规范与 CM 标量](https://github.com/awdawmip/enterprise-math/blob/4c738ab0dbf16e8da3dda496c24799ed426e9635/research_artifacts/mcp/RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT/MCP-bb6f343045854a798ca781ee73de2e39/10feb8dcbcb6a881b15f/D25_E3_PERIOD_GAUGE_CM_SCALAR.md)
- [S20] [P11 固定曲线局部 Kummer 像](https://github.com/awdawmip/enterprise-math/blob/4c738ab0dbf16e8da3dda496c24799ed426e9635/research_notes/owner_goal_20261016/p11_fixed_curve_paper/P11_LOCAL_KUMMER_IMAGE_PAPER_LEMMA.md)
- [S21] [已经发布的六项 RH 应用任务集](https://github.com/awdawmip/enterprise-math/blob/4c738ab0dbf16e8da3dda496c24799ed426e9635/research_notes/task_sets/rh_applications_20261122/README.md)
- [S22] [Hodge 秩一支撑障碍](https://github.com/awdawmip/enterprise-math/blob/4c738ab0dbf16e8da3dda496c24799ed426e9635/research_notes/balanced_resume_20261104/nt/hodge_support/HODGE_RANK_ONE_SUPPORT_OBSTRUCTION.md)
- [S23] [EC49FWS Farey／CRT 有限观察者](https://github.com/awdawmip/enterprise-math/blob/95507f064ee46910b32e26d1c49e6df4a05b84fc/research_notes/portable_direct/EC49FWS_FAREY_ONE_HOLE_FIBER_OBSERVER_THEOREM.md)（冻结分支 95507f064ee4）
- [S24] [P017×P018 Generation 4 相关前沿](https://github.com/awdawmip/enterprise-math/blob/90251d026b4d422a98de007f76de2a1e3de9337e/docs/P017_P018_SQUARE_DIAGONAL_GENERATION_4_WIP.md)（冻结分支 90251d026b4d）
- [S25] [Riesel 精确观察者与固定根下界](https://github.com/awdawmip/enterprise-math/blob/4c738ab0dbf16e8da3dda496c24799ed426e9635/research_notes/portable_direct/riesel_observers_20261122/README.md)
- [S26] [X6 R112 十二方向有理邻域证书](https://github.com/awdawmip/enterprise-math/blob/4c738ab0dbf16e8da3dda496c24799ed426e9635/research_notes/portable_direct/2026-11-22_r2_x6_r112_dual_open_twelve_chambers.md)
- [S27] [PREFIX-435 精确四相位探针](https://github.com/awdawmip/enterprise-math/blob/4c738ab0dbf16e8da3dda496c24799ed426e9635/research_notes/portable_direct/2026-11-02_prefix435_exact_four_phase_probe_tomography.md)
- [S28] [项目问题状态导航](https://github.com/awdawmip/enterprise-math/blob/4c738ab0dbf16e8da3dda496c24799ed426e9635/docs/PROBLEM_STATUS.en.md)
- [S29] [项目研究库导航](https://github.com/awdawmip/enterprise-math/blob/4c738ab0dbf16e8da3dda496c24799ed426e9635/docs/RESEARCH_LIBRARY.md)
- [S30] [分支结果索引，仅用于定位](https://github.com/awdawmip/enterprise-math/blob/4c738ab0dbf16e8da3dda496c24799ed426e9635/research_notes/balanced_resume_20261028/RESULTS_INDEX.md)
- [S31] [研究库第二轮归档整理，仅用于定位](https://github.com/awdawmip/enterprise-math/blob/4c738ab0dbf16e8da3dda496c24799ed426e9635/docs/research_library/20261104/SECOND_PASS.md)
- [S32] [Newton 单根交接与共振](https://github.com/awdawmip/enterprise-math/blob/4c738ab0dbf16e8da3dda496c24799ed426e9635/definitions/ENTERPRISE_BRC_NEWTON_HANDOFF_RESONANCE_FOUNDATION_20260904.md)
- [S33] [Newton 二次非分裂根选择](https://github.com/awdawmip/enterprise-math/blob/4c738ab0dbf16e8da3dda496c24799ed426e9635/definitions/ENTERPRISE_BRC_NEWTON_QUADRATIC_SELECTOR_FOUNDATION_20260904.md)
- [S34] [C78 锐邻近库存阈值承重证明](https://github.com/awdawmip/enterprise-math/blob/4c738ab0dbf16e8da3dda496c24799ed426e9635/research_notes/divisor_extrema/20261116_c78_nearby_stock_precision/SHARP_NEAR_STOCKS.md)
- [S35] [RH 三角相关核与固定树有限结构](https://github.com/awdawmip/enterprise-math/blob/4c738ab0dbf16e8da3dda496c24799ed426e9635/research_notes/portable_direct/rh_triangle_correlation_20261122_b5750a/REPORT.md)

外部原始资料：

- [E1] [FLINT：Ball arithmetic — rigorous inclusion semantics](https://flintlib.org/doc/guide/types/ball-arithmetic.html)，本轮直接读取。
- [E2] Cyril Cohen、Assia Mahboubi，[Formal Proofs in Real Algebraic Geometry: From Ordered Fields to Quantifier Elimination](https://lmcs.episciences.org/844)，Logical Methods in Computer Science 8(1), 2012，DOI: 10.2168/LMCS-8(1:2)2012；本轮直接读取。仅作为代数消元方法依据，不将其算作项目已完成的重证。
