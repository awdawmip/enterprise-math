# C15：有效环境倍率的临界量级与相干反推区间

Progress-Event-ID: prime-c15-environment-crossover-20261012
Date: 2026-10-12
Scope: enterprise-math/divisor-extrema / unchanged finite positive-BRC C2 model
Status: SELF_CHECKED_UNREVIEWED; CONDITIONAL_MODEL_THEOREMS; NO_PHYSICAL_OR_NOVELTY_CLAIM
Global-read: b1155d55c5c800a244721f95e12b879d09661306
EM-source-read: 2727f81e724b6b95811f622bd01194201578aa45
Research-Activity-ID: NONE_ALLOCATED; REGISTRATION_PENDING

## 1. 继承、目标与来源

消费C14：enterprise-math@153765a3716a4ca933f94beaea5e0587c0838160:research_notes/divisor_extrema/20261012_c14_frontier_participation_observer_limits.md，blob a5b715fcc15b9d5aabb9180819d1f1d008a34329。挂载12546字节全文的Git blob与本轮不可变远端读取一致。不把C14的有限倍率趋零与固定观察无限环境趋一重新报告为新发现。

保持用户方向：先找规律、计算量后置；初始整数和多性质并列冠军保留；整体可反向约束局部；整数顺序不是时间。沿同一完整乘法图和同一固定0<theta<1，不新增作用衰减参数。本轮研究环境M须比观察N大多少，以及可否从联合读数反推环境范围。

原始BRC内核src/enterprise_math/brc_histogram.py，8138字节，blob 9a3962ec095095f14e63a91cfe6b7ebf07d9a1d1，本轮当前远端元数据与本地原字节匹配；实际执行weight_histogram、histogram_serial、histogram_recoalesce。只在内存AST省略未调用的相对import brc_rational_holonomy。继承研究适配器c12_core.py（blob f704f6db254e57af4bf3bbc7d1a6a02292455644）与c13_core.py（blob f5641d9900b256089c2738d691887d0a476472a8）；它们不是生产模块或全项目测试。

## 2. 同一模型、观察及两个计数

顶点1..M；u--up是带素数p标签的边；f=(u,p,q),p<q,upq<=M为四边乘法交换关系。边符号sigma_e=+/-1，B_f为边界符号乘积。W_M=product_f(1+theta B_f)，mu_M=W_M/Z_M。完整赋值和正支路来源保留；相干符号是派生观察，不是正质量抵消。

固定P_N={p prime:p>=5,2p<=N<6p}，K_N=|P_N|，C_N为这些f_p=(1,2,p)边界的模2和。观察Xi_N(M)=E_mu_M product_(p in P_N)B_f_p，M>=N。N>=18时K_N=pi(floor(N/2))-pi(floor(N/6))~N/(3 ln N)。单一N下参与集合在扩大M时保持不变。模型从1有定义；P_N为空时乘积读数1只是空观察，不声明初始原生状态没有残差。

对p in P_N，记Q_p=floor(M/(2p))。特殊边e_p=(p,2p)参与面数精确为
 d_p=1+pi(Q_p)-1{Q_p>=2}。

以f_p为共同底面，可形成互不重叠外侧的六面单元数为
 k_p=pi(Q_p)-1{Q_p>=2}-1{Q_p>=p}。

第二式排除第三质数为2或p。q=p可以贡献一个含e_p的重复类型面，但不能成为三个不同质数的六面单元，故d_p与k_p不可混同。每个合格q要求2pq<=M，外层五面除共同底面外互不重叠。

## 3. 完整网络的双侧有限证书

定义r=(1-theta)/(1+theta)，s=(1-theta^5)/(1+theta^5)，均在(0,1)。令
 L_N(M)=product_(p in P_N) (1-r*s^k_p)/(1+r*s^k_p)，
 U_N(M)=product_(p in P_N) (1-r^d_p)/(1+r^d_p)。

则对每个有限M>=N：
 L_N(M) <= Xi_N(M) <= U_N(M)。

下界证明：C13的正耦合单调性允许把每个f_p之外未选中的面参数降为0。其k_p个共享底面单元给单环均值至少(1-r*s^k_p)/(1+r*s^k_p)。一般多体正耦合的GKS不等式E(sigma_A sigma_B)>=E(sigma_A)E(sigma_B)，可对这些面乘积逐次应用，得联合均值至少各单环均值之积。不同p的六面单元可以相互重叠；证明没有声称它们独立，也没有把不同子模型的概率直接相乘当作真实联合概率。

上界证明：任意两个不同e_p永不共面；否则它们作为同一面中两条带2标签的平行边，会要求一个素数是另一个素数乘第三个素数。给定其余边，这些特殊边条件独立。包含e_p的d_p个因子都形如1+theta epsilon_j sigma_e，故其绝对条件均值不超过(1-r^d_p)/(1+r^d_p)。条件期望后得到乘积上界；无条件Xi非负由正字符展开保证。此界包含全部未删除的外层和重叠关系。

M=N时所有k_p=0,d_p=1，两界都等于theta^K_N，恢复C14精确式。其后L、U和真实Xi均随M不减；L或U首次跨过某水平，不等于真实Xi就在那一点跨过。

精确图对照，N=30、theta=1/2，以下小数仅展示有理结果：
 M30：L=0.125000000，Xi=0.125000000，U=0.125000000；
 M42：L=0.130769231，Xi=0.131031220，U=0.200000000；
 M60：L=0.130769231，Xi=0.131043109，U=0.200000000；
 M90：L=0.149229762，Xi=0.154909909，U=0.594285714；
 M120：L=0.155601654，Xi=0.165671290，U=0.724738676。

## 4. 两种极限之间的临界量级

令c_N=M_N/N>=1，ell_N=ln N ln ln N（仅用于N趋无穷，不在初始1处使用）。固定0<theta<1，有：

 c_N/ell_N ->0  => Xi_N(M_N)->0；
 c_N/ell_N ->infinity => Xi_N(M_N)->1。

这是同一模型中同时扩展观察与环境的定理。不是新增衰减假设，也不是经验物理相变或精确临界常数。

趋零证明：p>N/6，故Q_p<3c_N，D=max d_p<=1+pi(ceil(3c_N))。由上界，Xi<=((1-r^D)/(1+r^D))^K<=1/(1+K r^D)。若c_N=o(ell_N)，素数定理和单调性给pi(3c_N)=o(ln N)，而ln K_N~ln N，故K_N r^D趋无穷。

趋一证明：p<=N/2，故Q_p>=floor(c_N)，k_p>=pi(floor(c_N))-2。单环负概率不超过r*s^k_p。即使不同环相关，奇数个负符号的事件也包含于至少一个环为负的事件，故
 1-Xi_N(M_N) <= 2K_N r*s^(pi(floor(c_N))-2)。
当c_N/ell_N趋无穷，pi(c_N)/ln N趋无穷，该上界趋零。若指数下界为负，仍为合法但可能很松的有限界；大尺度使用时pi(c_N)>2。

这里需要的素数渐近是已知pi(x)~x/ln x。本轮新连接在于：收紧K个增长的观察分量需要约ln K个外层素数方向，而提供这些方向的环境倍率c本身满足pi(c)约c/ln c，因此出现ln N ln ln N，而不是仅ln N。

## 5. 更精确的常数带与反向问题

记A_theta=ln((1+theta)/(1-theta))，B_theta=ln((1+theta^5)/(1-theta^5))。若c_N~c ell_N，则：
 c<1/A_theta => Xi_N(M_N)->0；
 c>1/B_theta => Xi_N(M_N)->1。

第二项沿前述单环并集界。第一项比使用最大度的1/(3A_theta)更强：固定一个小epsilon>0，只保留观察集合中p位于((1-epsilon)N/2,N/2]的特殊边用于上界；其数量~epsilon N/(2 ln N)，每条的d不超过pi(c_N/(1-epsilon))+O(1)。选择epsilon使A_theta*c/(1-epsilon)<1，就得到该子乘积趋零，其他因子绝对值不超过1。

对任意固定v in (0,1)，定义真正的首次跨越范围
 M_*(N;v)=min{M>=N:Xi_N(M)>=v}。
存在性由固定有限观察的C13极限或本节上侧结论；单调性来自GKS。严格有
 1/A_theta <= liminf M_*/(N ln N ln ln N)
 <= limsup M_*/(N ln N ln ln N) <=1/B_theta。

所以M_*=Theta_theta(N ln N ln ln N)。没有证明lim存在、只有一个相变点，或各v共享一个精确临界系数。theta=1/2时两个系数界为1/ln3与1/ln(33/31)，差距仍明显；不能把它们写成一个等号。

有限反推用M_nec=min{M:U_N(M)>=v}、M_suf=min{M:L_N(M)>=v}，给M_nec<=M_*<=M_suf。它们只要求正权证书，不要求直接枚举巨大完整图。theta=1/2、v=1/2的精确整数结果：

|N|K_N|乘积上界首次达标M_nec|下界首次达标M_suf|合并本轮直接计算后的M_*区间|
|---:|---:|---:|---:|---|
|30|3|78|1378|[121,1378]|
|100|9|430|10034|[430,10034]|
|1000|57|7898|224734|[7898,224734]|
|10000|408|122978|3811826|[122978,3811826]|

每个证书门槛同时检查M-1未达标、M达标。N30的必要界另由精确Xi_30(120)<1/2提高到121。区间很宽，说明当前证书尚未定位真正临界点；不是实验测量或误差条。只能在theta和观察定义已独立确定后用于反推；未知theta与未知M不能凭一个相干读数同时唯一识别。

## 6. 拟合意义与边界

本轮把C14的两种不同极限接成一个可检验的环境倍率量级，允许较大整体反过来约束同一批局部观察。参与集合不是自由拟合的K，但普通素数仍是算术输入，未生成素数序列。固定正耦合、无额外直接边界钉扎和所选多环相位观察是定理前提。

数值N和M不是已校准的物理长度；不能直接把M/N当作实验室空间半径比，也未把ln N ln ln N解释为普朗克到宏观的实际过渡。Xi趋一是这一联合相位相容，不等于机械稳定或量子消失；Xi趋零也不代表内部活动停止。没有新增时间演化、能量计算或量子实验数据。

这给物理拟合一个压力测试：若将来某实验确实对应此联合观察，固定theta且环境倍率受限会强制大N相干衰减；保留非零相干需要改变经验证的环境关系、作用强度或观察对应之一。不能事后仅重命名尺度来获得希望的结果。

## 7. 新增精确核验和可复算范围

PROTOCOL.json先于新数值输出保存，是数学核验协议，不是独立物理预注册。python reproduce.py执行：
- 132项完整网络Xi与两侧证书对照，M属于18,24,30,42,60,66,70,90,120，N属于18,24,30,36,42,60,90,120且N<=M，theta=1/4,1/2,3/4；最大闭合关系维数13。
- M=18..360共343张完整几何图；10109项单环关联面数、外层第三素数数目和外侧面互不重复核验；2143项选定特殊边互不共面的集合检查。
- 170次反推证书求值，保存四组门槛前后的完整有理分数。N10000等大例只计算已证明上下界，不声称枚举其完整图。
- 最终成功运行记录新适配器20899次和继承适配器8064次原始histogram_serial调用，合计28963次；不把调用数当效率成果。

数值Xi使用已证的正填充比值：GF2消元得到闭合面集合与目标边界纤维，按选取面数聚合非负整数重数，再由原始BRC串联/并合求质量。证书使用单正支路的串联乘积，重复幂由其结合律计算；最后的比值和中心化属于已声明观察。没有普通三角、圆周率、矩阵指数或提高精度替代BRC。

首次运行数学断言通过到N1000反推，但保存完整大整数分数时触发Python十进制字符串4300位限制。随后只调整序列化限制并完整重跑；模型、参数、算术结果未改，原错误日志保留。该问题是文件输出，不是科学精度或源码来源欠项。

原始内核与继承适配器、model.py、reproduce.py、协议、finite_results.json、inverse_results.json、summary.json及日志在复算包中。Source本文包含可独立重写的模型、证明、算法、代表结果及边界；沙盒附件不是永久仓库源码。

## 8. 文献、状态与下一单元

NIST DLMF27.12本轮实际打开，使用素数定理。Forsstrom/Viklund arXiv2502.19942v2的HTML本轮请求失败；其GKS结果沿已读C13保留，同时实际检索到Forsstrom的Pure Perimeter Laws for Wilson Lines Observables（J.Stat.Phys.193,86，2026-06-29，DOI10.1007/s10955-026-03648-5）公开正文第3节Lemma3.1及证明，明确给出乘积关联不等式并引用前文Proposition6.3。本轮不使用它的物理模型结论、不分析图表、不宣称新颖性全面审计。
https://dlmf.nist.gov/27.12
https://link.springer.com/article/10.1007/s10955-026-03648-5

当前科学状态SELF_CHECKED_UNREVIEWED。此前平台阻止的session登记没有在本轮换通道重试；未取得新session/activity/CLAIM。笔记保全不是注册或数学/物理准入，不修改P000、受保护世界观和定时任务。

下一精确问题：同量级c_N=c ln N ln ln N内，真实临界系数与响应宽度是什么，能否缩小1/A_theta到1/B_theta的证书带？同时以至少两个有明确路径的联合观察辨识环境范围与局部theta，避免用一个可见度同时拟合两个未知机制。实际宏观实验对应仍独立待证。
