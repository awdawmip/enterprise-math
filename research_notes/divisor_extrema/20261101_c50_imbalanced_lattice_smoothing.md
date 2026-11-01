# C50：失衡环境的条件格点平移与双观察辨识

Progress-Event-ID: prime-c50-imbalanced-smoothing-20261101
Date: 2026-11-01 Asia/Taipei
Status: AUTHOR_DERIVED / FINITE_EXACT_CHECKED / INDEPENDENT_REVIEW_PENDING
Global-read: 0d6024a1bc66fabd689753a0e8a99f90c8d5e433
EM-read: 996d6ef33dfbb8a3a8902ea81e9ff09b18053a56
Pre-publication-main: 1fa5f28499b71829b1f93fc45a38462b069d9939
Research-Activity-ID: NONE_ALLOCATED; REGISTRATION_PENDING

## 1. 接续与本轮对象

接续C49@5f62c2be6a376369237f3ed4a5f478824e83c288:research_notes/divisor_extrema/20261101_c49_two_scale_lattice_smoothing.md，blob fa771f579754c4ba9f0f8e7800c73559dfc7af1c；不可变项目记录及挂载复算包均已读取。母目标是研究素数—合数联合路径中整体条件与局部排列的规律；本轮将平方根数量失衡加入C49第二弱作用尺度。

固定可见2^m3^m，m>=1；隐藏5^(t+k_t)7^t，k_t/sqrt(t)->s有限，t^(3/2)gamma_t->lambda有限（含零）。全部不同完整因子词均匀参考，再乘固定正权q^(D²)，0<q<1，beta=log(1/q)。Delta上三角(1,-1,1,1,-1,gamma_t)，保留r=X23，交叉贡献S，隐藏I=X57：D=2r-m²+2S+gamma_t[2I-(t+k_t)t]。

完整整数图、词来源、rho_1和P000/X6保留。沿用C49内部状态桥：算术词与残差为X6 Cell上的内部联合记录，读出保留Cell身份。优先值和规模索引分别用于排序与规模；本轮概率律是明确的候选准备。

## 2. 条件中心发生平移，方差保留原形式

条件于可见词v及其优先位置z，h(u)为此前3次数减2次数；M=Eh、V=Var(h)、C=Cov(h,U)。间隙X~Dirichlet(1,...,1)，J=2m+1。设c=t+k_t：
S=sum_(i<=c)h(U_i)-sum_(j<=t)h(V_j)，ES=k_t M，VarS=(c+t)V。
I-ct/2=t sum_i(1/2-U_i)+c sum_j(V_j-1/2)+R_ct。
核k(u,v)=1_(u<v)+u-v-1/2对任一输入均值零，VarR=ct/12，二部核图展开给E R^(2p)<=C_p t^(2p)。

B_t=(2I-ct)/t^(3/2)可在局部测度尺度替换为L'_t=2/sqrt(t)[sum_j(V_j-1/2)-sum_i(U_i-1/2)]。误差各固定偶次矩为O(t^-p)。联合(S/sqrt(t),B_t)的极限均值(sM,0)、协方差[[2V,-4C],[-4C,2/3]]。

固定S=ell后，B_t的条件极限为N(b,tau²)，其中
b=2sMC/V，tau²=2/3-8C²/V。
并有2/3>=tau²>=(2/3)sum X_j³>=2/[3J²]。

新界|C|<=V/2：将整数h拆成嵌套阈值指标；每个指标与均匀U的协方差绝对值最多是其方差的一半，嵌套指标间协方差非负。相加得界，故|b|<=m|s|。

精确见证：v2332，间隙(1/10,1/10,1/5,2/5,1/5)，M=3/10、V=41/100、C=3/40，b=(9/82)s，tau²=137/246。s1时未条件化B均值始终0，条件S0后均值趋9/82。

## 3. 局部引理与完整联合极限

固定内部z、固定整数ell，对有界连续f，
sqrt(t) E[f(B_t)1_(S=ell)|v,z] -> exp[-s²M²/(4V)]/[2sqrt(pi)sqrt(V)] * E f(N(b,tau²))。

自足Fourier证明：A_t(theta,xi)=integral exp[i theta h(u)-2i xi(u-1/2)/sqrt(t)]du，反演integrand为exp(-i theta ell) A_t^c conjugate(A_t)^t。令theta=x/sqrt(t)，极限为exp[-Vx²+4Cx xi-xi²/3+i sMx]。Gaussian积分给上述条件均值、方差与中心层密度。相邻高度保证最大格距1；远离零频率指数衰减。高阶矩控制将线性部分替换回B。

全部残差层的控制延续并核对C49：从每个高度样本抽取公平相邻二点分量，令eta=min(X0,X1)，最大点质量与指数倾斜给
sqrt(t) sup_ell E[(1+|B_t|^(2p))1_(S=ell)|z] <= C_p(1+eta^-1/2)。
Dirichlet下可积。对高斯乘多项式测试函数，按隐藏项是否大于旧格点一半拆分，得到exp(-a ell²)+(1+|ell|)^(-2p)可求和界，支持全部层、间隙边界及固定阶矩的极限交换。

令delta=m mod2，A_s=exp[-s²M²/(4V)]，定义正局部有限测度
mu_(v;lambda,s)(dx)=E_z[A_s/sqrt(V) sum_j Law(2j+delta+lambda Z)(dx)]，Z|z~N(b,tau²)。

选后(v,D)弱收敛到
Pi(v,dx)=exp(-beta x²)mu_v(dx)/sum_w integral exp(-beta y²)mu_w(dy)。
有限可见词边缘TV收敛，全部固定阶残差绝对矩及有界局部混合矩收敛。接受份额为t^-1/2乘归一化分母/[2sqrt(pi)binom(2m,m)]。

失衡分别改变中心层密度A_s、条件中心lambda*b与条件展宽lambda²tau²。lambda0恢复C46失衡局部律和格点残差；先取本规模极限再|lambda|大，趋J_v(0,s)/sumJ与连续Gaussian的乘积。一般无界lambda_t阵列另需一致估计。

## 4. 方向对称保留，周期项出现相位

互换2/3使M、C同时反号，V、tau²、A_s及b均不变，故mu_complement(v)=mu_v。任意有限s、lambda下P2332=P3223。反转词并反射优先位置使b反号、残差反射，偶终端权保留反转词等概率。局部边缘分别为s与lambda的偶函数；有限规模顺序差异继续保留。

对lambda非零，周期核为
1/2 E[A_s/sqrt(V){1+2 sum_(n>=1)(-1)^(n delta) exp[-pi²n²lambda²tau²/2] cos[pi n(x-lambda b)]}]。

若m|lambda*s|<1/2，一阶余弦在每个间隙为正，因此总体一阶周期系数严格非零，连续极限非高斯。更大参数直接使用完整相位公式。确定性求积在m2、lambda2、s1得到一阶归一化系数约-3.42983188e-5；它是数值观察，未提供该积分符号的严格区间证书。

## 5. 相同方差的不同排列，以及双观察辨识

m2三组每条词概率记PA(2233/3322)、PB(2323/3232)、PC(2332/3223)。设M2为偶格点权exp(-beta d²)的二阶矩，a_beta=-beta+2beta²M2<0。Poisson表示给a_beta=-2beta²F'/F，F'>0。

小参数准确展开：
PA=2/15-s²/30-17a_beta lambda²/11520+O(s4+s²lambda²+lambda4)；
PB=1/5+a_beta lambda²/240+O(s4+s²lambda²+lambda4)；
PC=1/6+s²/30-31a_beta lambda²/11520+O(s4+s²lambda²+lambda4)；
Var(r)=22/15-4s²/15-a_beta lambda²/288+O(s4+s²lambda²+lambda4)。

积分求导由m2各高度分组的E[M4 V^-5/2]有限、tau²有界、|b/s|<=2和终端Gaussian Fourier尾支持。位移的局部质量贡献首次出现在s²lambda²。C46失衡导数与C49展宽导数按各自准确假设复用。

因此对每个足够小非零lambda，存在唯一小的s²>=0使局部方差准确等于22/15：
s²=-(5a_beta/384)lambda²+O(lambda4)。
存在性由s²方向负导数、lambda²方向正导数及中值定理；局部负导数给唯一性。在这条曲线上PA=2/15-a_beta lambda²/960+O(lambda4)，PB=1/5+a_beta lambda²/240+O(lambda4)，PC=1/6-a_beta lambda²/320+O(lambda4)。所以同方差仍为不同排列。

(PA,PB)对(s²,lambda²)的一阶Jacobian行列式=-a_beta/7200>0。导数连续且在小的凸非负参数矩形一致接近可逆矩阵，沿线段积分给局部可辨。使用(Var(r),PB)同样可行，行列式=-a_beta/900。这些偶观察辨识参数平方。

q1/2时，准确theta和log2有理尾界给a_beta约-0.2656723700594862，等方差曲线|s|/|lambda|趋0.0588156072。令M4为离散残差四阶矩、b_beta=1-4beta M2+2beta²(M4-M2²)，则沿该曲线Var(D/2)=K0(q)+(9/64)b_beta lambda²+O(lambda4)。准确证书给1.291302<b_beta<1.291304，系数约0.181589497455。整体残差宽度也是额外区分量。

## 6. 实际结果与证据范围

固定s1、lambda1、q1/2，平方t下k=sqrt(t)、gamma=t^-3/2。有限t4/9/16/25/36的两方向概率分别为
.1865861864/.1582131527；.1802033764/.1606203743；.1796491909/.1646792290；.1803477080/.1682343819；.1813097456/.1711422694。
局部方差分别1.4759175902、1.4711355642、1.4439184933、1.4194525029、1.3997289980；整体Var(D/2)分别.1688931966、.1726353889、.1744545207、.1753809785、.1758887908。

48阶极限求积给两方向同为.193634243626，局部方差1.260648291799，整体方差.176270471338。有限行有严格有理权区间；极限积分是确定性浮点近似。32/48阶重点配置最大概率差约3.26e-9，局部方差差约2.42e-8，不把精度一致当作积分证书。

q1/2、lambda1，s0/.5/1/2的局部方差约1.466781518/1.405242009/1.260648292/.929488738。lambda1、s1、q1/16的两方向概率约.196047696458。

精确检查：288完整直方图与84080直接扩展、288反转、80原BRC；1800条件平移界和互补身份、450反转协方差；1920固定间隙扩展及5套联合矩；7符号响应身份、24移位theta高精度身份、初始1..5。全部声明断言通过。BRC串联/并合各4728次，原核8138字节/blob9a3962ec095095f14e63a91cfe6b7ebf07d9a1d1与当前源核对后原样复用。

七个较大有限配置最高隐藏42/36，准确整数系数加法1055085234次，概率最大区间宽约1.1301e-42。另有七个平方规模到t225的条件逆序矩，均为准确有理数。一次48阶全参数积分在45秒上限停止，随后完成48阶两个重点配置；未完成全表不计入证据。

完整RESEARCH_NOTE.md、五个新脚本、严格有限区间、积分近似、准确系数及最小继承依赖随C50复算包交付；远端为独立摘要。

## 7. 文献与状态

实际读取Janson《Moment convergence in conditional limit theorems》J.Appl.Probab.38(2)(2001)421–437作者全文第2节，Theorem2.3明确处理条件值偏离均值平方根量级时的均值修正。作者PDF解析正文取得，截图服务Cache miss。本轮窄域Fourier局部引理、尾部、算术参数与观察系数有自足推导；一般条件Gaussian回归和Poisson求和保留已有归属。

2026-11-01 em_session_start(prime-c50-imbalanced-smoothing-20261101-a1)返回STATIC_READONLY_SCOPE_DENIED、operation_sent=false；无session/activity/CLAIM。作者证明、自检、独立审核、形式化与物理读出桥接分别记录。

下一单元：可见长度随环境增长时，条件方差下界和联合状态的有效范围；或为本轮双观察映射建立有测量误差的参数区间。本轮固定m、有限s与lambda的条件联合极限已完成作者推导与有限核验。
