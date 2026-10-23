# C37：观察窗口、共享小整数来源与高斯／非高斯残余

Progress-Event-ID: prime-c37-window-source-20261023
Date: 2026-10-23 Asia/Tokyo
Status: AUTHOR_DERIVED_FINITE_CHECKED / SELF_CHECKED_UNREVIEWED / NO_PHYSICAL_FIT
Global-read: abed76a9c866347d9c3b3ba2844853229a4e8c22
EM-source-read: af2df115aa4f2641452c5a788dab0a4cf57f594b
Research-Activity-ID: NONE_ALLOCATED; REGISTRATION_PENDING

## 1. 接续和未改变的随机模型

消费C36@2f8b170c87f643c4f1291f8aacf975520a0c7d1a:research_notes/divisor_extrema/20261023_c36_prefix_shared_sources_non_gaussian.md，blob fc8d04fe3c505ff9d285d485f12323ad3c8568b3；已读固定Source与挂载C36包。

底层仍是完整整数前缀的素数单步边(m,mp)与四边面(m,mp,mq,mpq)，p<q为不同素数。标记边符号独立，负号概率固定epsilon属于(0,1/2)，eta=1-2epsilon；全部N复用同一无限标记边空间。每面正号概率mu=(1+eta^4)/2。只改变观察，不改变旧边概率、自然动态或静态面平衡权重。未观察的边仍保留来源，不将观察选择称为删除实体。P000、世界观、初始单位保留，普通素数仍是输入；数值区间不是已证物理空间，N不是已标定的普朗克长度倍数。面集合为空时比例未定义，不赋予原生残差零。

区分两种观察：A仅要求最大顶点mpq落在(aN,bN]，仍使用全部四边来源；B要求四个顶点全部落在(alpha N,N]。两者不是同一个“只看大数”。

## 2. 任意两个面观察的准确共同来源式

对面族A，F_A为面数，d_A(e)为边参与数，T_A为共享一边的无序面对数。继承C36：
Var(Y_A)=[F_A(1-eta^8)+2T_A(eta^6-eta^8)]/(4F_A^2)。
两个不同基本面最多共享一边，故任意A、B准确有
Cov(Y_A,Y_B)=[(eta^6-eta^8)sum_e d_A(e)d_B(e)+|A交B|(1-4eta^6+3eta^8)]/(4F_AF_B)。
证明分别计算相同面、共享一边的不同面和不共享边的面；没有假定面独立。它也由C36正交投影直接得到。

## 3. 仅按终点选窗：不同大数区间保留同一个非高斯极限

令F(n)为完整前缀面数，S_n=F(n)(Y_n-mu)，C36已证Z_n=2S_n/pi(n)在L2收敛至
Z_inf=eta^3 sum_(n>=2)(1/n)sum_(p|n)(sigma_(n,p)-eta)。
其方差eta^6(1-eta^2)C2>0，三阶矩-2eta^10(1-eta^2)C3<0，C_s=sum omega(n)/n^s。

固定0<=a<b，终点窗面数F_ab=F(floor bN)-F(floor aN)，Dpi=pi(floor bN)-pi(floor aN)。准确有
Z_ab,N=2F_ab(Y_ab,N-mu)/Dpi=[pi(bN)Z_bN-pi(aN)Z_aN]/Dpi。
由PNT两系数有界且趋b/(b-a)、-a/(b-a)，和恒为1，所以Z_ab,N在同一概率空间L2收敛到同一个Z_inf；a=0省去第二项。

继承的F(n)渐近给F_ab~(b-a)N(loglogN)^2/2、Dpi~(b-a)N/logN，因此每个固定非空终点窗都有
Var(Y_ab,N)~eta^6(1-eta^2)C2/[log^2N(loglogN)^4]。
任意两个固定终点窗，即使互不重叠，相关系数都趋1。不是有限N时完全相同，也不覆盖长度随N收缩的任意短窗。

实际比较(N/4,N/2]与(N/2,N]，N100/1000/10000/100000/1000000时相关系数约0.341186/0.529301/0.769209/0.930828/0.985386。百万时两窗面数784982与1639682。另(0,N/2]与(N/2,N]的百万相关系数平方0.9801808920093901。大数终点仍复用小边，例如终点6和10的面共享1--2；这种算术共同来源不是物理超距作用或反向因果。

## 4. 全支撑窗口的一般集中与高斯定理

固定0<alpha<1，四顶点都在(alpha N,N]等价m>alpha N、mpq<=N，故pq<1/alpha且
F_alpha(N)=sum_(p<q,pq<1/alpha)[floor(N/(pq))-floor(alpha N)]。
当0<alpha<1/6时F_alpha=c_alpha N+O(1)，c_alpha=sum(1/(pq)-alpha)>0；alpha>=1/6时没有本类四边面，因为最小不同素数乘积为6。这只是当前观察不存在，不是对象没有结构。

令R=floor(1/alpha)，一条边作为下侧或上侧，每类至多pi(R)-1种面，因此面关联度<=D=2(pi(R)-1)。面依赖图连共享边的面，最大度<=4(D-1)，与N无关。断开的面族使用不交的独立边集，具有真正联合独立性。

所以在固定epsilon属于(0,1/2)时，Var(Y_alpha,N)=Theta(1/N)，且标准化后的Y_alpha,N分布趋标准高斯。

自足证明：总正面数X的方差由非负协方差下界为F_alpha(1-eta^8)/4，上界O(F_alpha)。有界变量的r阶联合累积量有仅依r的界；若索引分成两独立组则为0。固定有界度依赖图只有O_r(F_alpha)个有贡献的连通r元组（允许重复），故总和r阶累积量O_r(N)。标准化后r>=3均为O_r(N^(1-r/2))趋0。矩—累积量关系给高斯矩；高阶偶矩有界保证子列一致可积，二阶矩保证紧性；高斯矩满足Carleman唯一性，因此得到分布收敛。另与Feray 1605.03836第4.1节/Janson判据逐条对照：界常数、方差Theta(N)、取s=3。一般依赖图中心极限定理不是本轮首创。

## 5. (N/12,N]的完整依赖组分类和准确常数

此窗只允许方向(2,3)、(2,5)。记A_m为底部m的(2,3)面、B_m为(2,5)面；
f6=floor(N/6)-floor(N/12)，f10=floor(N/10)-floor(N/12)。
同类型面不能共享边。跨类型仅有两种：A_m与B_m共享下方2边；A_(5r)与B_(3r)共享上方2边，N/36<r<=N/30。一个A面不可能同时处于两种关系：前者底部<=N/10，后者>5N/36。故全部依赖组至多3面。

三面组A_(3r)--B_(3r)--A_(5r)，准确组数为
c3=floor(N/30)-floor(N/36)，c2=f10-c3，c1=f6-f10-c3。
各组分别有4/7/10条不同来源边，不同组边集不交。因此完整正面计数分布是c1单面、c2双面、c3三面分布的准确卷积，不是假定每面独立。

F=f6+f10~N/10；T=f10+c3~N/45，所以
N Var(Y_local,N) -> kappa_eta=(5/2)(1-eta^8)+(10/9)(eta^6-eta^8)>0。
sqrt(N)(Y_local,N-mu)趋Normal(0,kappa_eta)。epsilon10%时kappa_eta=2.1854272。
百万时F100000、T22223、c1=61110、c2=11111、c3=5556，准确方差0.000002185430870016。完整前缀方差约0.000015393981274000918，仅上半终点窗约0.000012223699543772645，三者均值都0.7048。

本地窗仍使用2、3、5这些小素数方向；被排除的是固定小整数边的重复共用，而不是小素数因子本身。N>12K时它不使用上端<=K的任意边。

## 6. 两类残余渐近独立，以及很小的跨界权重何时主导

记G_N=sqrt(N)(Y_local,N-mu)，Z_N为完整前缀残余。准确有联合极限
(G_N,Z_N) -> (G,Z_inf)，G与Z_inf独立。
证明：Z_inf先截断到上端n<=K，N>12K时与G_N依赖不交边集，精确独立；用C36的L2收敛及极限级数L2尾界，先N趋无穷再K趋无穷，通过有界Lipschitz测试转移独立性。有限N的全局/本地观察并不独立，计算保留准确交叉协方差。其相关系数平方从N100的0.112464降至百万的0.000532511。

同一边状态上定义凸混合观察Y_mix=(1-lambda_N)Y_local+lambda_N Y_global，0<=lambda_N<=1。lambda是观察权重，不是新增扰动概率。令s_N=pi(N)/(2F(N))，r_N=lambda_N sqrt(N)s_N，则
sqrt(N)(Y_mix-mu)=(1-lambda_N)G_N+r_N Z_N。
因此：r_N趋0时极限是G；r_N趋r属于(0,infty)时极限G+rZ_inf且两项独立，三阶矩r^3 E Z_inf^3<0，故非高斯；r_N趋无穷时，除以lambda_N s_N后的残余趋Z_inf。

两类贡献同量级的观察权重是2F(N)/(sqrt(N)pi(N))~logN(loglogN)^2/sqrt(N)，趋0。于是跨界权重本身趋0也未必足以消除算术非高斯残余。此为明确观察族的尺度判据，不是有限N系数1的临界点、物理相变或现实仪器结论。

## 7. 实算和来源边界

原brc_histogram.py8138字节/blob9a3962ec095095f14e63a91cfe6b7ebf07d9a1d1，与当前Source和C36附件一致后复用；原c12_core.py6525字节不改，继承加载器只在内存略去未调用相对import。实际正权走weight_histogram、histogram_serial、histogram_recoalesce；筛、关联计数为整数结构，中心矩/协方差/归一化为观察，无数值三角或指数传播。

六份结果文件：480全支撑窗，11568面、43705活跃边、9001依赖组检查；355终点窗对；35一般窗口检查。9个代表组分布共3504条加权活跃边历史，9个完整小窗共61488条加权历史，对照全部概率而非只比矩。N6/8/10/12共18752个不同完整边状态，12套终点窗概率检查；同一批状态另作4个全局/本地联合协方差检查，不重复宣称是新的不同状态。另175项共同来源计数、157对互不重叠大数窗，以及至100万的准确计数与矩公式。大图不作全分布枚举。六个成功日志BRC串联4856、并合966仅为运行来源。全部所述断言通过；不是全项目测试、独立审核或形式化检查。

完整英文证明RESEARCH_NOTE.md、window_fluctuations.py、window_mixture.py、disjoint_bands.py、精确JSON和继承最小代码位于C37复算包。本Source为独立中文摘要，不与英文全文冒称字节相同。

公开原文实读Feray 1605.03836引言、2.2、4.1定义和定理4.3；Janson1988出版者摘要，其完整页失败；NIST DLMF27.12；Abiya/Ambika2010.12153引言与任意整除边定义。后者图不同，不能互换结论。未完成全面新颖性审查。

专用Scholar Issue6203，batch ddde5d12-2786-4cdf-9e63-6d8d026ef9c8，turn 52490643-1065-4fcd-aeee-1de1bb6e945f，conversation em-prime-residual-continuation；request摘要67205c6c6ca430905b25a8e5c01091cb02f1440879edf461c4bca1b92bc0b70f本地、受理及结果匹配。受理2026-10-23T10:26:13.795642Z，完成10:26:25.237247Z，结果评论6362805192。1次提供方查询、0次桥接模型调用、1轮实际读回；返回2条相关元数据，coverage不完整，未返回所指定原论文。相关2026论文2610.04452公开链接Cache miss，未用于证明。原始结果在Issue，本地是标明的元数据子集；专业catalog整理ARCHIVE_PENDING。公开原文读取与专用状态分开。

本轮session_start(prime-c37-window-source-20261023-a1)实际返回STATIC_READONLY_SCOPE_DENIED，operation_sent=false；无新session/activity/CLAIM，未绕换通道。笔记保全不等于数学／物理准入。没有新增物理数据、E/J、能量、长度、心跳或素数生成证明。

下一问题：窗口下界alpha_N随N趋零或有独立依据的有限可达规则时，何种来源复用增长率改变极限；不为得到高斯或非高斯预先选择物理窗口。完整前缀与有限比率窗只是两类已证明的观察协议，当前不能由曲线形状单独选择真实稳定机制。
