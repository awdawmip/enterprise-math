# C48：临界弱隐藏作用、方向选择与连续残差极限

Progress-Event-ID: prime-c48-critical-hidden-interaction-20261101
Date: 2026-11-01 Asia/Taipei
Status: AUTHOR_DERIVED_WITH_EXPLICIT_STANDARD_LLT_DEPENDENCY / FINITE_EXACT_CHECKED / INDEPENDENT_REVIEW_PENDING
Global-read: a01383f825ef9d43b4b754254303298c64041568
EM-read: 86149263e38c22292c9def1e0f69092efa1be77e
Pre-publication-main: 2090e8686f55f25a432f1b67ac986e8062c3459e
Research-Activity-ID: NONE_ALLOCATED; REGISTRATION_PENDING

## 1. 继承与本轮范围

消费C47@64cafd5a7ac04262d34c573ed0f89e61e689a381:research_notes/divisor_extrema/20261101_c47_hidden_interaction_local_uniformity.md，blob7906b0c27a779cdb4497446a0c58a0d3fb6a8c0c及实际挂载复算包。本轮闭合C47留下的t*gamma_t有限非零时的选后局部极限，并纳入C46的平方根数量失衡。

固定可见2^m3^m，隐藏5^c7^d；全部不同完整因子词先均匀，再乘固定正终端权q^(D²)，0<q<1。Delta上三角为(1,-1,1,1,-1,gamma_t)。保留词v的r=X23，h(u)为辅助排序位置u之前3次数减2次数；S=sum h(U_i)-sum h(V_j)，I=X57。完整D=2r-m²+2S+gamma_t(2I-cd)。令d=t、c=t+k_t、k_t/sqrt(t)->s，t*gamma_t->alpha非零有限。

普通素数、全部路径、rho_1及来源标签保持。节点势只共同平移累计和中心，D不变。辅助排序/积分变量不是物理时空；算术观察不删除P000/X6信息，原生实现和检测桥接另需依据。gamma随规模的变化是本轮明确考察的候选族，不由结果倒推为自然定律。

## 2. 完整临界选择定理

给定可见优先位置0<z1<...<z_(2m)<1，间隙X为Dirichlet(1,...,1)。定义

 M_v=integral_0^1 h_v(u)du,
 V_v,alpha=Var_(U uniform)[h_v(U)-alpha U]
             =V_v,0-2alpha Cov(h_v(U),U)+alpha²/12,
 J_v(alpha,s)=E_z[V_v,alpha^(-1/2) exp(-s² M_v²/(4V_v,alpha))].

固定m、q、有限非零alpha和有限s，选后可见词概率在有限集合总变差中趋J_v/sum J。

令beta=-log q，联合(v,D)弱收敛到上述有限词分布与密度sqrt(beta/pi)exp(-beta x²)的乘积；D的全部固定阶绝对矩及与有界可见观察的混合矩收敛。因此Var(D/2)->1/(8beta)。这里联合连续极限是弱收敛，不是总变差：有限D仍是离散原子分布。

参考接受份额E0[q^(D²)]~[mean_v J_v/(4sqrt(beta))]t^(-1/2)。局部极限不依赖固定q，整体残差宽度和接受份额仍依赖q。有限局部概率仍可依赖q。

## 3. 证明依赖与关键控制

经典输入为Canfield/Janson/Zeilberger arXiv0908.2089v1 Theorem4.5式4.9。二字词逆序I_ab在a,b均为固定正倍t时，sigma²=ab(a+b+1)/12，所有整数点上一致有P(I=k)=sigma^-1 phi((k-mu)/sigma)+O(t^-5/2)，最大点质量O(t^-3/2)。该论文条件max(a,b)<=C exp(c0 min(a,b))在本轮范围成立。原文解析式和作者2012勘误已实际读取；PDF截图返回Cache miss，未声称视觉核验。一般LLT及Hoeffding方法归于已有研究。

自足应用：I-cd/2=d sum(1/2-U_i)+c sum(V_j-1/2)+R_cd，其中R条件于任何单个优先值均值0、VarR=cd/12。因此[S+gamma(I-cd/2)]/sqrt(t)在固定z下趋N(s M,2V_alpha)。仅此CLT不足以确定选择后的概率，须继续处理D=O(1)的窗口。

每个间隙内h恒定，方差分解给V_alpha>=alpha² sum X_j³/12>=alpha²/[12(2m+1)²]，不要求全部间隙远离零。

给定隐藏占用k,l，I=sum_(i<j)k_i l_j+sum I_j，各I_j独立二字词逆序。最大间隙X_j*>=1/(2m+1)，其中两类占用均>=t/[2(2m+1)]以指数高概率成立。条件于其余变量，D=K_t+2gamma_t(I_j*-mu_j*)。对连续紧支撑psi或多项式乘高斯，sum_n |psi(K_t+2gamma_t(n-mu))|=O(t)一致于平移。LLT误差乘该和为O(t^-3/2)，乘sqrt(t)后消失。

高斯主项的格距2|gamma_t|趋0，用Riemann和处理。占用多元CLT及其余间隙逆序CLT给K_t/sqrt(t)的高斯极限，其均值2sM、方差8V_alpha-4alpha²X_j*³/6；与j*内部正态部分卷积后，准确得到

 sqrt(t) E0[psi(D)|v,z] -> exp(-s²M²/(4V_alpha))/(4sqrt(pi)*sqrt(V_alpha)) * integral psi.

最大点质量界和O(t)格点和另给不依赖z的可积上界；指数小坏事件和多项式乘高斯尾部均受控。故可以对z积分、乘权并归一化，得到第2节及矩收敛。未把S与I当成独立噪声。

## 4. 两端连接和方向诊断

|alpha|<=a<1时，整数高度差给V_alpha>=(1-a)²V_0。结合C46的E V_0^-1/2有限，J_v(alpha,s)在alpha->0时趋J_v(0,s)。所以可见分布的两步极限接回无隐藏直接作用的C46；D的连续极限与精确gamma0的离散格点极限分别保留。没有覆盖任意t*gamma_t->0阵列。

|alpha|大时，J_v(alpha,s)=sqrt(12)/|alpha|[1+12E Cov(h,U)/alpha+O(alpha^-2)]，因此可见词趋均匀。这是先取固定alpha的t极限、再扩大alpha的结论，不自动给随t无界alpha_t的统一界。

m2、s0时，六词按2233,2323,2332,3223,3232,3322排列。反转不改J，互换2/3等于alpha反号。alpha0时J_A=pi/2,J_B=3pi/4,J_C=5pi/8，总J=15pi/4。

对2332，令负/正高度长度a,b，u=a+b,v=b-a，V0=u-v²；给定a,b的平均Cov(h,U)=(u²+2u-3v²)/12。准确Beta积分给J'_2332(0)=15pi/128，故

 P_alpha(2332)=1/6+alpha/32+O(alpha²),
 P_alpha(3223)=1/6-alpha/32+O(alpha²).

方向概率差以alpha/16为首项；局部均值始终2，方差在alpha0只有二阶及更高变化。又E Cov(h,U)对这两词分别±1/15，大alpha方向差为4/(15alpha)+O(alpha^-2)。因此两端方向差消失，中间非零尺度可见；未宣称唯一最大点或全局单调性。

alpha1时还存在准确的辅助循环原点对称：h(u)-u的边界+1跳跃与内部正跳跃互换原点，保留方差且Dirichlet间隙律不变，得到三词组{2233,3223,3322}同J，另一组{2323,2332,3232}同J。

## 5. 极限积分近似与有限严格区间

极限J用18/36/60阶Gauss-Jacobi确定性浮点求积，非严格积分区间；alpha>=1的36与60阶概率差最大约2.6e-13，数值稳定不冒充证明。

alpha0的P2332/P3223/Var(r)为1/6、1/6、22/15；alpha0.5近似.1809112479/.1517579828/1.4835342941；alpha1为.1920864084/.1412469249/1.5141482162；alpha2为.2037311062/.1341391184/1.5750445991；alpha4为.1975435379/.1405388149/1.6343001629；alpha8为.1835630010/.1513991735/1.6579390700；强alpha端为1/6、1/6、5/3。

固定alpha1、q1/2，有限gamma=1/t的精确计数给：
 t2: P2332=.26567417695, P3223=.20914473942, Var(r)=1.00892582279, Var(D/2)=.14855327768；
 t4: .23691276463/.18113919453/1.20136420610/.17155049952；
 t8: .21679542715/.16265859927/1.33910799176/.17514711560；
 t16: .20507185015/.15235215161/1.42120865124/.17720674216；
 t32: .19874506724/.14690532796/1.46620305966/.17859972238。

最后一项极限1/(8ln2)=.18033688011112042，有正有理log级数尾区间。有限与极限前三项的证书类型不同，未混称。

有限gamma=a/b时记录整数分子M=bD。q=1/2的权2^(-M²/b²)一般无理；本轮用准确整数根夹在相邻112位二进有理数之间，并检查r^d<=2^E<(r+1)^d。保留|D|<=12，遗漏正质量及矩按最小遗漏平方权包尾。有限概率最大区间宽约9.2e-35。不将有理指数误称有理权，也没有Monte Carlo。

## 6. 实际执行和状态

1026套新DP/直接完整词计数及条件矩对照，按配置44190条直接词；1026反转直方图；234套原BRC完整直方图；144临界方差恒等式；3780逐点非退化界；2268循环原点身份；414整数根区间嵌套；初始1..5与方向导数符号积分。全部声明断言通过。

9行较大有限参数，最高等量32/32，另20/16，包含q1/2与1/4；217986668次整数系数加法。极限求积另记录订单和浮点语义；平方根失衡s1也计算了近似积分，不将有限表作为定理。

原BRC8138字节/blob9a3962ec095095f14e63a91cfe6b7ebf07d9a1d1与本轮源一致并实际执行，串联/并合各3622次。仅相同(可见位置,隐藏次数,累计分子)且后续等价状态并合。新critical_exact.py、critical_quadrature.py、run_checks.py、完整证明与结果保存在C48对话复算包；远端本文件为独立摘要。

2026-11-01 em_session_start(prime-c48-critical-hidden-interaction-20261101-a1)返回STATIC_READONLY_SCOPE_DENIED、operation_sent=false；无session/activity/CLAIM，未绕路登记。研究草稿保全与独立审核、形式化、物理验证分别记录。标准概率工具的归属明确；无全面新颖性审查或新实验。

下一单元：t*gamma_t趋0而gamma_t*t^(3/2)有限/变化时，区分局部选择和残差格距的两个过渡；或处理可见长度随环境增长的一致范围。本轮有限非零alpha、固定m定理已明确闭合。
