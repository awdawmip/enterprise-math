# R592｜辅助整函数好圆周的可计算选择与半径 5 的零点证书

日期：2026-11-07。状态：AUTHOR_SIDE_ANALYTIC_DERIVATION + EXACT_RATIONAL_FINITE_CERTIFICATE；数学 Driver 独立审阅待完成。

## 冻结来源与对象

科学输入保持 R462 @ `18783e01e3646c72b7aab3b16d3f565e83e6446f`，直接依赖 R590 @ `88406fcfe23c2c23c2c27887b87613f8dcd6031a` 和 R591 @ `70e3d3af388f1c810e115d313cd6d9f620917eac`。辅助标量对象定义为
[
F(z)=24sum_{j=0}^inftyrac{(-8z)^j}{(2j+4)!},qquad a_j=rac{24cdot8^j}{(2j+4)!},
quad F_J(z)=sum_{j=0}^J(-1)^ja_jz^j.
]
[
F_k(z)=sum_{j=0}^{2k-1}(-1)^ja_{k,j}z^j,quad
a_{k,j}=rac{H_k(j+2)}{H_k(2)k^{2j}},
]
其中 H_k 及原始 Catalan 求和见 R590。所有源定义、原生十二条 signed BRC 支路、P000 六轴及联合观察者均未修改。本轮所有谱结论仅属于辅助标量观察者；其复谱、正型能量或零点数均不能不经保真映射声称覆盖原生联合谱。

## 定理 A：给定有理数 R≥1，可用有限有理运算构造好圆周

以前轮 R591 作者侧定理 A 为前提：对每个 R≥1，存在 rho∈(R,2R) 使
[
min_{|z|=ho}|F(z)|ge e^{-144sqrt R}.
]
本轮证明存在一个**确定性、终止的纯有理搜索程序**，输入 R∈Q, R≥1，输出 r∈Q∩[R,2R] 及可机械检查的证书
[
oxed{min_{|z|=r}|F(z)|>rac38delta_R},qquad
delta_R=2^{-lceil216sqrt Rceil}.
]
平方根取整 (lceil bsqrt Rceil) 仅需比较整数平方；(delta_R) 是严格有理数。

### 证明与算法

令 (B_R=24cdot2^{lceil8sqrt Rceil})。因为
[
M_F(3R)le24expsqrt{24R}<24e^{5sqrt R},
]
Cauchy 导数估计（以任意 |z|≤2R 为中心取半径 R 的圆）给出
[
sup_{|z|le2R}|F'(z)|le M_F(3R)/Rle B_R.
]
使用恒等式 (log2=2sum_{nge0}[(2n+1)3^{2n+1}]^{-1}>2/3)，有 (delta_Rle e^{-144sqrt R}) 且 (B_Rge24e^{5sqrt R})。

置 (n=lceil16RB_R/delta_Rceil)，取有限有理候选
[
r_ell=R+ell R/n,quad ell=0,ldots,n.
]
R591 的好半径到某个 (r_ell) 距离≤R/(2n)，所以该候选圆周最小模仍≥(delta_R-delta_R/32=31delta_R/32)。

选择整数 J，使对所有 0≤r≤2R 的严格有理尾界
[
T_J(2R)=rac{a_{J+1}(2R)^{J+1}}
{1-rac{16R}{(2J+8)(2J+7)}}<delta_R/16
]
成立（增大 J 必然成功）。再取 (M=lceil64RB_R/delta_Rceil)，在每一候选圆上检查有限节点
[
z_{ell,m,sigma}=r_ell,sigma
rac{1-t_m^2+2it_m}{1+t_m^2},quad
t_m=m/M,quad m=0,ldots,M,quadsigma=pm1.
]
另外两个象限利用 (overline{F(z)}=F(ar z)) 对称覆盖。因为有理参数化满足 (|u'(t)|le2)，任意圆周点到一个节点或其共轭的距离≤(2r_ell/Mle4R/M)。结合导数界，模长变差≤(delta_R/16)。

对各 (ell) 逐一采用**完全有理的判据**：对所有 ((m,sigma))，检查
[
|F_J(z_{ell,m,sigma})|^2>(delta_R/2)^2.
]
R591 的好圆周附近选出的候选在所有节点上满足
[
|F_J(z_{ell,m,sigma})|ge
delta_R-delta_R/32-delta_R/16
=29delta_R/32>delta_R/2,
]
因此有限搜索必终止。成功候选在任意圆周点的模长至少严格大于
(delta_R/2-delta_R/16-delta_R/16=3delta_R/8)，得证。

该通用上界是**可计算性定理，不是实用复杂度保证**：n 和 M 可能随 (sqrt R) 指数膨胀。实际工程优先使用更粗、经过验证的自适应有理网格，不改变以上存在/终止保证。

## 推论 B：可计算的有限 k 零点匹配

对搜索输出 r，直接以精确分数计算
[
E_k(r)=sum_{j=0}^{2k-1}|a_{k,j}-a_j|r^j+
sum_{jge2k}a_jr^j.
]
末项用上述首项/比率法给出严格有理上界。若证出 (E_k(r)<3delta_R/8)，则 Rouché 定理给出
[
N_{F_k}(r)=N_F(r).
]
无需数值寻根和浮点零点计数。结合 R590 的增长圆盘误差，选择任意有理 (R_kin[rac c2(log k)^2,c(log k)^2])，其中 c=1/40000（充分大 k 才有 R_k≥1），便可使算法最终输出 R591 匹配窗口中的可计算半径：由 (216log2<162) 有 (delta_{R_k}ge	frac12 k^{-0.81})，而 R590 在 |z|≤2c(log k)² 的误差为 (O(k^{-0.98}log k))，故充分大 k 的严格 Rouché 判据成立。这里非有理的 log 仅用于数学渐近分析；实际算法输入可用任意有理 (R_k) 及精确系数误差检验。

## 定理 C：半径 5 的无零圆盘、两个有限 k 的精确零点匹配

这是**不依赖 R591 好圆周存在性证明的独立有理证书**。取 J=18、r=5、M=256，程序直接计算
[
T=sum_{j>18}a_j5^j quad	ext{的严格上界},qquad
Dgesup_{|z|le5}|F'(z)|,
]
其中 (D) 由前 18 阶导数正项和及自第 19 项起的严格几何尾界构造。

使用上述 514 个复有理节点，精确检查
[
min operatorname{Re}F_{18}(z_{mathrm{node}})
>rac1{10}+T+rac{2rD}{M},
quad
min|F_{18}(z_{mathrm{node}})|^2>
left(rac15+T+rac{2rD}{M}ight)^2.
]
每项比较在 Q 中精确进行；输出中的十进制仅供阅读。由覆盖与导数界，圆周全体有
[
oxed{operatorname{Re}F(z)>rac1{10}},qquad
oxed{|F(z)|>rac15}quad (|z|=5).
]
调和函数 (operatorname{Re}F) 的最小值原理给出 (operatorname{Re}F(z)>1/10) 对所有 (|z|le5) 成立，故 F 在闭盘无零点。

再次使用**原始** Catalan 系数公式，以全有理运算得到 k=64 和128 时 (E_k(5)<1/5)，均满足 Rouché 条件，故
[
oxed{N_F(5)=N_{F_{64}}(5)=N_{F_{128}}(5)=0}.
]
实际计算的误差上界十进制近似分别为 0.170946296 与 0.0850013902；数值不是判断依据。

运行 `python R592_VERIFY.py` 可复验全部有限输入，结果保存在 R592_EVIDENCE.txt；无限 k 的最终增长窗口结论依赖 R590/R591 的作者证明，等待独立审阅。

## 价值、状态与下一问题

R591 的纯存在性半径选择被转化为可执行的有理数证书算法；给出了新的 r=5 零点空域及两个真正有限 k 的零点计数证书。局部辅助标量零点计数既不自动确定其全谱正型能量 V_k，也不直接决定原生 signed BRC 联合状态。

下一步：（1）把指数级兜底网格改成多项式/准多项式可用的自适应证书与更大 r 的实例；（2）将匹配的增长窗口零点与 R588 的能量逃逸分开量化；（3）独立审阅 R590–R592 的解析承重引理，保留 R462 的科学 pin 与原生联合支路保真问题。无本轮 Source-native CLAIM/Result/Review。
