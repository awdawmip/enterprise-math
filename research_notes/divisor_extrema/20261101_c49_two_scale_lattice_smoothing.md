# C49：第二弱作用尺度、条件格点展宽与局部联合读出

Progress-Event-ID: prime-c49-lattice-smoothing-20261101
Date: 2026-11-01 Asia/Taipei
Status: AUTHOR_DERIVED / FINITE_EXACT_CHECKED / INDEPENDENT_REVIEW_PENDING
Global-read: d63e70daeafb077bdd91e2cc837104b97e43c689
EM-read / pre-publication-main: 24eb5e125a7bf52366cc49f1ed2594c0cd6d5b14
Research-Activity-ID: NONE_ALLOCATED; REGISTRATION_PENDING

## 1. 继承与模型

接续C48@87bd9fbf0dc96b920cba23dcab2aef520199bf3b:research_notes/divisor_extrema/20261101_c48_critical_hidden_interaction.md，blob f2b5e19d9b833ad1833296301965e2f6bce19ac9，及本对话实际挂载复算包。

固定可见2^m3^m，m>=1固定；完整2^m3^m5^t7^t，所有不同完整因子词均匀参考，再乘固定q^(D²)，0<q<1，beta=-log q。Delta上三角仍为(1,-1,1,1,-1,gamma_t)。v为保留词，r=X23，S为隐藏交叉贡献，I=X57：

 D_t=2r-m²+2S+gamma_t(2I-t²)。

本轮证明t^(3/2)*gamma_t趋有限lambda（含零）的选后联合极限；与C48的t*gamma_t趋非零alpha分开。完整词、rho_1和来源保持，正概率与signed分数分型。可将算术词作为原生X6 Cell上的内部联合状态，观察只读取内部标签并保留Cell身份；排序变量、t和条件高斯均不添加原生空间轴或物理时间。有限DP只合并同保留位置、隐藏次数、累计分子的声明后续等价状态。

## 2. 条件展宽方差

条件于保留词及其有序优先位置z，隐藏优先值U_i,V_i独立均匀；间隙X为Dirichlet(1,...,1)，J=2m+1。h(u)记录此前3次数减2次数。设M=Eh、V=Var(h)、C=Cov(h,U)。

 S=sum_i[h(U_i)-h(V_i)]；
 I-t²/2=t sum_i(V_i-U_i)+R_t，
 R_t=sum_ij k(U_i,V_j)，k(u,v)=1_(u<v)+u-v-1/2。

核条件于任一输入均值0，|k|<=1/2，VarR=t²/12。展开2p阶矩时，含度1顶点的二部核图项为零，剩余最多2p个顶点，故E R_t^(2p)<=C_p t^(2p)。

令B_t=(2I-t²)/t^(3/2)，L_t=2/sqrt(t) sum(V_i-U_i)。联合协方差(S/sqrt(t),L_t)为[[2V,-4C],[-4C,2/3]]。限制S在固定整数附近后，B_t的极限方差是

 tau²=2/3-8C²/V，

而不是未条件化的2/3。最小二乘及每个间隙内h恒定给

 2/3 >= tau² >= (2/3)sum X_j³ >= 2/[3(2m+1)²]>0。

## 3. 本轮局部引理与尾部证明

固定内部z、整数ell，对有界连续f：

 sqrt(t) E[f(B_t) 1_(S=ell)|v,z]
 -> [1/(2sqrt(pi)sqrt(V))] E f(N(0,tau²))。

自足Fourier论证：线性部分的局部特征函数为sqrt(t)/(2pi)乘[-pi,pi]积分，integrand是exp(-i theta ell)*|integral_0^1 exp(i theta h(u)-2i xi u/sqrt(t))du|^(2t)。theta=x/sqrt(t)后的极限是exp(-Vx²+4Cx xi-xi²/3)。高度含相邻整数，远离零频率指数衰减，近零配平方给可积控制；高斯积分恰产生上述条件方差。有限正测度特征函数收敛给线性局部极限。sqrt(t)P(|2R_t/t^(3/2)|>epsilon)<=C epsilon^-2 t^-1/2，故可恢复原B_t。

无限层求和另有统一控制。令eta_z=min(X0,X1)，从2t个独立高度样本抽取公平相邻二点分量，二项最大点质量与E[(B+1)^-1]公式给sqrt(t)sup_ell P(S=ell)<=C eta_z^-1/2。对exp(±L_t)倾斜时单变量密度比有统一界，同一方法给所有固定阶局部矩。退化R的高阶矩接入后，

 sqrt(t)sup_ell E[(1+|B_t|^(2p))1_(S=ell)] <= C_p(1+eta_z^-1/2)。

Dirichlet下此右端可积。对高斯乘多项式psi，将|lambda_t B_t|小于/大于|2ell+2r-m²|/2分开，得到可求和的exp(-c ell²)+(1+|ell|)^(-2p)统一控制。它支持全部残差层、间隙边界、终端权及固定阶矩的极限交换，未将普通CLT替代局部选择论证。

## 4. 完整第二尺度定理

令delta=m mod2，lambda_t=t^(3/2)gamma_t->lambda属于R。定义正局部有限测度

 mu_(v,lambda)(dx)=E_z[V^-1/2 sum_(j in Z) Law(2j+delta+lambda Z_tau)(dx)]，
 Z_tau在给定z下为N(0,tau²)。

lambda0时mu=J_v sum_j Dirac_(2j+delta)，J_v=E V^-1/2。由第3节有sqrt(t) E0[psi(D_t)|v]->(1/(2sqrt(pi)))integral psi dmu。

选后联合极限准确为

 Pi_lambda(v,dx)=exp(-beta x²)mu_(v,lambda)(dx) /
                  sum_w integral exp(-beta y²)mu_(w,lambda)(dy)。

联合为弱收敛，有限可见集合的边缘为TV收敛；D所有固定阶绝对矩及有界可见观察混合矩收敛。参考接受份额为t^-1/2乘[sum_v integral W dmu]/[2sqrt(pi)binom(2m,m)]。

lambda非零时mu有连续密度，即旧格点与方差lambda²tau²的条件高斯卷积。有限词仍为离散原子总体。lambda0包括任意t^(3/2)gamma_t->0阵列，恢复C46等量环境格点极限。

## 5. 周期结构、非高斯与两端

格距2的高斯展宽核有Poisson表达

 L_(delta,sigma)(x)=1/2[1+2 sum_(n>=1)(-1)^(n delta) exp(-pi²n²sigma²/2)cos(pi n x)]。

每个有限非零lambda的一阶周期系数E[V^-1/2 exp(-pi²lambda²tau²/2)]严格为正。总体密度是exp(-beta x²)乘非恒定正周期函数，因此严格非高斯：若等于任意中心高斯，则两者的指数二次比值不可能是非恒定周期函数。

lambda趋0时，局部与D分别趋J_v/sumJ及余类离散高斯，二者独立。先完成固定lambda的t极限、再|lambda|趋无穷时，由tau²下界有

 |2L-1|<=2 sum_(n>=1)exp[-pi²n²lambda²/(3J²)]，

故联合极限族在TV中趋J_v/sumJ与密度sqrt(beta/pi)exp(-beta x²)的乘积，Var(D/2)->1/(8beta)。一般lambda_t无界的统一阵列尚需另外估计。

互换2与3给h反号，V不变、C反号而tau²不变，因此本轮极限中互补词同概率，特别P2332=P3223。与C48在gamma约1/t时的非零方向偏好形成两尺度区别。有限有序信息仍保留。

## 6. 局部概率的q依赖和准确系数

delta0时单核的终端权积分为

 A_beta(s²)=(1+2beta s²)^-1/2 sum_j exp[-4beta j²/(1+2beta s²)]。

局部权为E[V^-1/2 A_beta(lambda²tau²)]，中间lambda一般保留q依赖。对m2，三组A2233/3322、B2323/3232、C2332/3223：

 J_A=pi/2，J_B=3pi/4，J_C=5pi/8；
 E[C²V^-3/2]=(59pi/8192,pi/128,77pi/8192)；
 E[tau²V^-1/2]/J=(847/1536,7/12,1049/1920)。

六词的J加权平均tau²为9/16。以上由同高度Dirichlet分组、条件多项式与Beta积分准确求出。

定义Theta0=sum_j exp(-4beta j²)，M2=sum_j(2j)²exp(-4beta j²)/Theta0，a_beta=-beta+2beta²M2<0（由Poisson式的正导数得）。每条词的局部展开：

 P_A=2/15-17 a_beta lambda²/11520+O(lambda4)；
 P_B=1/5+a_beta lambda²/240+O(lambda4)；
 P_C=1/6-31 a_beta lambda²/11520+O(lambda4)；
 Var(r)=22/15-a_beta lambda²/288+O(lambda4)。

因此局部变化及q依赖具有解析证据，不只是积分误差。不同词的条件D密度通常也不同，中间尺度的联合关系需要保留。

## 7. 计算与实际结果

q1/2、m2：lambda0/0.25/0.5/1/2/4的极限Var(D/2)约为0.111216601342/0.121692799484/0.144516775010/0.174914367401/0.180305522648/0.180336877062。lambda1局部P2332=P3223约0.166737615993，Var(r)约1.466781517634。q1/16、lambda1时两词概率约0.167637508323。极限积分为18/48/64阶Gauss-Jacobi确定性近似，用准确J控制变量；48/64阶最大概率差约2.73e-10，数值稳定性不当作严格积分证书。

固定lambda1的有限平方t=4/9/16/25/36，gamma分别1/8、1/27、1/64、1/125、1/216。Var(D/2)的严格有限区间中点约0.168984587343/0.169916647874/0.171225807619/0.172189449947/0.172849720429。t36两方向概率仍为0.178731532661和0.168959569972；新定理给出其极限相同，未用有限表外推。

有限权2^(-D²)一般无理。本轮用准确log2级数、正exp级数及定向dyadic运算包络，再用遗漏正质量控制尾部；与继承整数根方法交叉检查。七个较大有限配置最大概率区间宽约8.91e-43，累计893129320次整数系数加法；大路径族通过充分状态计数，不逐词枚举。

288套新数组DP/继承DP/直接词完整计数对照，18272条直接扩展；96套原正权BRC，实际串联/并合各2536次；190权区间、812条件方差与对称性、3精确Dirichlet积分、4局部响应系数、36高精度theta身份、初始1..5。所有声明断言通过。原内核8138字节/blob9a3962ec095095f14e63a91cfe6b7ebf07d9a1d1与当前Source匹配，字节不改。

首次验证日志BRC调用字段因只遍历运行前空键集合而为空；改遍历运行后的实际键并重跑，数学数据与断言保持。完整RESEARCH_NOTE.md、四个新程序、有限区间/积分近似/准确系数和最小继承代码在prime_quantum_lattice_smoothing_c49.zip；本远端记录为独立摘要。

## 8. 文献、状态与接续

相关既有工作实际读取：Janson《Moment convergence in conditional limit theorems》J.Appl.Probab.38(2)(2001)421–437，出版者摘要与书目；Micciancio/Regev《Worst-case to Average-case Reductions based on Gaussian Measure》(2007)，作者页摘要；Regev/Stephens-Davidowitz arXiv1502.04796 HTML引言及周期高斯背景。本轮窄域Fourier局部引理、尾部和系数论证自足，通用条件极限与格点平滑工具保留既有归属；没有全面新颖性审查。

2026-11-01 em_session_start(prime-c49-lattice-smoothing-20261101-a1)返回STATIC_READONLY_SCOPE_DENIED、operation_sent=false，无session/activity/CLAIM。研究草稿保全、独立审核、形式化和物理桥接分别记录。

下一单元：纳入平方根数量失衡，或建立t^(3/2)gamma_t无界但t gamma_t趋0的一致过渡。当前等量环境、固定可见长度、有界lambda定理已完成本轮作者证明及有限自检。