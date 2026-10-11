# 从1起的重复／异类组合：正重合残差、前缀赋值极值与分圆读出

Progress-Event-ID: prime-residual-prefix-law-20261011-c3
At: 2026-10-11T13:10:35Z
Scope: enterprise-math/divisor-extrema; formal arithmetic BRC
Status: SELF_CHECKED_UNREVIEWED; CLASSICAL_IDENTITIES_REPROVED_AND_CONNECTED; NO_NATIVE_RESIDUAL_ATTRIBUTION
Global-read: 64b02b8fd4181f35ba83a102b3f5aa1672e5738b
EM-source-read: e23c8d2dfc9df6f5e00dc7220d1d8d3433a77d01
Research-Activity-ID: NONE_ALLOCATED; REGISTRATION_PENDING

## 1. 目标与续接

消费上述源版本 research_notes/divisor_extrema/00_CURRENT_RESEARCH_DIRECTION.md，blob 254786ecf0c34981caecc69452da69406911ff55。按用户纠正：先找规律，再考虑计算量；从1起包括所有初始整数；冠军按明确性质保留并列者，不先排除1和素数。本轮没有恢复效率优先目标，没有将3称作严格刷新纪录者。

本轮建立的是已有整数的形式算术关系，不给原生r_1、r_p赋值，不把经典分圆多项式或取模数值直接命名为心跳原生残差。P000不变。旧二项式、压缩与延迟观察结论保留，不把旧分类实验当作本轮新结果。

## 2. BRC实际复用及观察范围

原始源 src/enterprise_math/brc_histogram.py，固定EM-source-read，blob 9a3962ec095095f14e63a91cfe6b7ebf07d9a1d1；8138字节，SHA256 256ef167e2aee651c042195522a0013ba619f265f9e4d8fa24f07d3399695a67。复用前轮附件完整字节，并与本轮远端blob相同。实际执行原始 WeightHistogram、weight_histogram、histogram_serial、histogram_recoalesce；只用AST省略未调用的相对import rational_prime_valuations，未改这些定义。不是完整项目安装或全项目测试。

定理来源 definitions/ENTERPRISE_BRC_UNIVERSAL_HISTOGRAM_FOUNDATION_20260903.md，blob 5100aa3d893ff152e0da7a3ae2eea812cfbcaf1c，WBRC-T36/素赋值传递。载体为N[Q_positive^x]，本轮先限正整数权重。[m]保留整数m标签，不是仅保留因数个数。备择并合加重数，串联合成作乘积卷积。周期部分另用前轮已证的j mod n推前。

允许观察：乘积标签、多重数、正整数赋值极大值及明确声明的多项式观察。因数对原始来源在小例证据中保留。直方图等式只断言按乘积标签汇总后的等式，不断言来源敏感路径已等同。多项式负系数是代数观察系数，不是负支路质量；无π、三角函数、矩阵指数、物理时间或原生场计算。

## 3. 重复组合的非负残差

定义D_n=sum_{d|n}[d]，每个正约数一支路。D_1=[1]。串联D_a*D_b在标签d上的重数mu_ab(d)等于满足u|a,v|b,uv=d的有序因数对数。

支持恰为Div(ab)：按每个素数分解，0<=k<=A+B总能拆成i+j=k，0<=i<=A、0<=j<=B。因此可在每个非空结果纤维保留一条代表，其余形成正计数直方图：
E(a,b)=sum_{d|ab}(mu_ab(d)-1)[d]，并有D_a*D_b=D_ab+E(a,b)。

E(a,b)为空当且仅当gcd(a,b)=1。互素时每个素数只能来自一边，分解唯一；若共有素数p，则p至少有(p,1)与(1,p)两条来源。

总重合数C(E)=tau(a)tau(b)-tau(ab)。若v_p(a)=A_p、v_p(b)=B_p，则tau(ab)=prod_p(A_p+B_p+1)，与prod_p(A_p+1)(B_p+1)的差正是该计数。不是对普通约数重复计数，而是保留不同组合路径。

小例：
D_2*D_2=[1]+2[2]+[4]=D_4+[2]；E(2,2)=[2]。
D_2*D_3=[1]+[2]+[3]+[6]=D_6；E(2,3)=0。
E(1,n)=0只说明单位组合无重合，不意味着原生r_1为零；E(2,3)=0只说明这一重合观察为空，不意味着6无其他结构残差。

结合律给出对所有a,b,c>=1的精确正直方图恒等式：
E(a,b)*D_c+E(ab,c)=D_a*E(b,c)+E(a,bc)。
证明：两边分别与D_abc并合，都等于D_a*D_b*D_c；在整数重数中逐标签消去相同基底即可。等式双方实际保持非负状态。

以12为例：(2*2)*3路径先产生[2]，再扩展为[2]+[6]；(2*3)*2路径第一次无重合，第二次E(6,2)=[2]+[6]。因此累积重合按乘积标签相同，不能仅记录每一局部残差的未加权标量和。

有限核验：1<=a,b<=16，共256对，支持/非负重建及互素等价全部通过；1<=a,b,c<=8，共512组三元组，正直方图恒等式全部通过。原始BRC串联实际执行。

## 4. 所有已有整数的赋值最高纪录

全前缀保留I_N=sum_{m=1}^N[m]。另定义明确的观察L(I)=lcm{m:[m]在I中非空}，只限非空正整数权重。

v_p(L(I))=max_m v_p(m)，因此：
L(I+J)=lcm(L(I),L(J))；L(I*J)=L(I)L(J)。
后式由max_{i,j}(a_i+b_j)=max_i a_i+max_j b_j得到。对4个固定直方图的16对输入，两条观察律分别16项核验通过。

L_N=L(I_N)=lcm(1,...,N)，L_1=1。它记录各素数标签上的最高次数，不是仅记录tau/Omega/omega最大值；也不等于先前定义的单个冠军数，可能大于N。按素数标签选极值是本轮明确声明的额外观察，不冒称用户原先已指定该指标。所有并列冠军及其原整数仍保留在I_N。

L_N并非完整前缀：例如L_5=60的约数含6、10等尚未作为前缀成员出现的联合组合。因此只把它解释为逐坐标容量，不把它的全部约数冒充历史实际对象。

定义n>=2时的继承部分A_n=gcd(n,L_(n-1))，新增倍数Delta_n=n/A_n。则L_n=L_(n-1)Delta_n。

精确分类：
- n=p为素数：A_n=1、Delta_n=p=n，出现新素数标签；
- n=p^a、a>=2：A_n=p^(a-1)、Delta_n=p，旧标签的最高次数增加1；
- n含至少两种素因子：A_n=n、Delta_n=1，各素数幂分量已经分别在较小整数中出现，新的是它们的联合。

证明：n非素数幂时，任意p^a||n均严格小于n，已经整除L_(n-1)。n=p^a时此前最高p幂是p^(a-1)。这个证明同时覆盖最初2、3、4、5、6，不用未来素数表作生成输入。它是经典算术结构定理，不是物理因果证明。

初值(n,L_(n-1),A_n,Delta_n)：
(2,1,1,2),(3,2,1,3),(4,6,2,2),(5,12,1,5),(6,60,6,1),(7,60,1,7),(8,420,4,2),(9,840,3,3),(10,2520,10,1),(11,2520,1,11),(12,27720,12,1)。

6为约数/不同种类冠军，Delta_6仍为1：冠军刷新与最高赋值扩张不是同一性质，不能据此丢掉6。3与2的三项冠军统计并列，但L前缀从2增加到6，因为3的标签不同。1是初始单位，没有空内部系数的素性判断。

## 5. 与前轮二项式BRC的精确连接

用前轮T=[1]+[2]生成H_n=T^n，其权重2^j的重数为binom(n,j)。这与第3节D_n不是同一个载体对象，虽然使用同一BRC代数。

对每个n>=2有：
g_n=gcd_{1<=j<n}binom(n,j)=Delta_n=L_n/L_(n-1)。

这是经典二项式最大公因数定理与前缀lcm性质的连接，非本轮首创。简证g_n分类：g_n整除binom(n,1)=n。对p|n写n=p^a m、p不整除m。在模p多项式中(1+X)^n=(1+X^(p^a))^m。若m>1，则内部j=p^a处系数模p为m，故p不整除g_n。若m=1，全部内部系数被p整除；j=p^(a-1)处恰含一个p，因为binom(p^a-1,j-1)模p为(-1)^(j-1)，不为0。故g_n=p。

另核对Farhi经典关系：n*lcm_{0<=j<=n-1}binom(n-1,j)=L_n。例如4层完整系数的lcm为12，下一层L_5=5*12=60。

本轮实际串联生成1..256的BRC行，并生成同范围完整前缀直方图；2..256的255项g_n=Delta_n及255项Farhi关系全部通过。分解标签仅在这些输出产生后用于独立核验，不作为状态输入。不是重报旧1..1000素性分类。

## 6. 完整形式结构：中性读数不等于零多项式

由前轮周期BRC商N[C_n]，确定性正支路移位S_n将位置j变为j+1 mod n。每条边权重为1。特征多项式det(XI-S_n)=X^n-1：n>=2的行列式展开只有全对角与完整n环两个非零置换项；n=1直接为X-1。它是正移位的代数观察，不调用仅适用于稳定相的循环zeta运行时，不把单位环当稳定衰减。

本轮原始histogram_serial加已证周期推前，验证n=1..40的首次返回恰为n，共820个移位步骤；形式步不是物理心跳。特征多项式等式用上述证明，并未声称运行完整特征多项式库。

取单一初始多项式Phi_1=X-1，递归
Phi_n=(X^n-1)/prod_{d|n,d<n}Phi_d。
这是经典分圆多项式，不是新造素性准则。符号X不是角度，不计算复根/三角值。

Phi_2=X+1；Phi_3=X^2+X+1；Phi_4=X^2+1；Phi_5=X^4+X^3+X^2+X+1；Phi_6=X^2-X+1。
Phi_1非零多项式，Phi_1(1)=0仅是指定观察值，不能推原生r_1=0。

n>1时经典公式Phi_n(1)=p（n=p^a），否则为1。可由n=prod_{d|n,d>1}Phi_d(1)归纳证明。因此有统一连接：
Phi_n(1)=g_n=L_n/L_(n-1)，n>=2。

更完整地，Q_N=lcm_{1<=m<=N}(X^m-1)=prod_{d=1}^N Phi_d，Q_N/Q_(N-1)=Phi_N；[Q_N/(X-1)]在X=1的值为L_N。多项式lcm取首一规范化；X-1是所有前缀共享的初始因子，非为2或3另加补丁。该完整恒等式为理论推导，未另计算所有Q_N的系数。

6处Phi_6(1)=1，但Phi_6=X^2-X+1既非零也非恒等多项式1；不能把一维中性读数当作完整结构消失。多项式负系数不代表负BRC质量。

本轮按递归精确长除生成1..128的Phi_n，128项重乘重建X^n-1通过；2..128的127项Phi_n(1)=Delta_n通过。这是明确来源与证明的BRC周期代数观察扩展，未建立任何原生物理映射。

## 7. 证据、文献和边界

本轮冻结PROTOCOL.json后运行reproduce.py；后续独立重合单元先冻结COLLISION_PROTOCOL.json，再运行collision_check.py。全部是标准库整数/分数和原始BRC接口，无浮点模型。
SHA256：
reproduce.py 501a6e1881926e54a6d803c5a6814159169fbc7804963a63d12dc557e7982522
results.json 7c1a13a6ca3019ce11c614e4e31c4504b80055f7b7e465b0d908a89846939a0a
collision_check.py 0cc5336ed578118e0fa50508e4bea54a4f223308c4179c9634018b39f589a10f
collision_results.json 3133c16f11ed45d74084d4f686b902644c249c180d867df437cb16848108cc27

原始文献读取范围：
- Carl McTague, On the Greatest Common Divisor of Binomial Coefficients, arXiv:1510.06696v5，Theorem1；已核PDF正文与第1页图。2017 Monthly DOI 10.4169/amer.math.monthly.124.4.353。该定理在其文中引为Ram1909。
- Bakir Farhi, An identity involving the least common multiple of binomial coefficients and its application, arXiv:0906.2295，已核题录/摘要公式；本轮PDF请求失败，不宣称本轮读其全文。
- B. Bzdega, A. Herrera-Poyatos, P. Moree, Cyclotomic polynomials at roots of unity, arXiv:1611.06783v2，已核第3页公式(3)、Lemma4及证明的PDF解析文本；该页截图请求失败。未开展其余根值的三角/复数计算。
- OEIS A003418核对前缀lcm定义与初值。

精确结论是已定义算术载体内的重复重合、赋值纪录增长、组合系数公因子与周期因子观察之间的关系。并未证明原生素数残差产生新素数，亦未证明单个tau/Omega/omega冠军决定全前缀；无效率优势要求，无新颖性首创或数学准入宣称。

实际em_session_start请求prime-residual-law-first-prefix-20261011-s3返回STATIC_READONLY_SCOPE_DENIED、operation_sent=false。没有identity/activity/CLAIM分配；Source笔记保全与原生登记分开。当前scope允许的科学推导和非准入笔记继续，不借用其他身份或修改定时任务。

## 8. 下一数学单元

在保留本轮全部初始关系的条件下，追踪正重合E(a,b)的带来源版本与周期因子Phi_ab的重复／异类分解之间是否有统一的结构传递；首先比较(2*2)*3与2*(2*3)的完整来源，不只比较总计数。冠军的作用按明确性质从这些关系导出，不要求独占性或低成本。原生r_1/r_p对应仍须由原生结构提供，不能将上述观察直接升级为它。
