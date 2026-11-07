# C60：隐藏组成、稀释尺度与可反推的共同极限

Progress-Event-ID: prime-c60-hidden-composition-20261107-a1
Date: 2026-11-07 Asia/Taipei
Status: AUTHOR_DERIVED / EXACT_FINITE_CHECKED / INDEPENDENT_REVIEW_PENDING
Global-read: 9f7faf96127788e9250e8fcd69c0aaabb30373ae
EM-read: 94026836203f96307897126e930ee0066e268680
Pre-publication-main: 93d1f9e7a7118bf8c71d790698bbb74ce2975a07
Research-Activity-ID: NONE_ALLOCATED_THIS_TURN; new session_start returned BACKEND_IDENTITY_OR_VERSION_MISMATCH, operation_sent=false.

## 1. 接续与模型

接续C59@fe2b64e4ac79ff5358dbd8eb364f75395c4fa62a:research_notes/divisor_extrema/20261107_c59_growing_hidden_tail.md，blob86d7daefc7d7590ab5211f994d84cf31ace45bc7及实际挂载复算包。母问题为素数—合数联合路径中的整体条件、组成与历史稳定。

保持三态0/1/2，对5的率z=(1/4,1,4)，对2/3/7均为1；下一项按率乘剩余次数归一化。2加1封顶2；前两次3确定重置用于准备，以后3以e(xi)=1/(4+xi²)保留旧态，否则回0；5/7保持。xi=2X23-n2*n3在更新前计算。真实历史3223/2332都到36、xi0，准备状态0/1。

共同可见词仍为(23)^k；本轮把隐藏尾独立变为5^c7^d，主范围c,d>=1，完整目标N=36*6^k*5^c*7^d。H=c+d，theta=c/H是状态敏感因子5的重复占比，不是区间素数密度。每次3之前xi=-2，保留率始终1/8。研究自然条件于这段可见词先出现后的状态；并非强制输入或全体路径典型性结论。

完整正分支、signed分数、rho_1和来源保持。算术词与记忆是保留Heartbeat X6 Cell身份的内部记录。共用严格正终端W(A,B)仍可施加，参考状态差与选后读数分开。

## 2. 准确递推与组成作用

每块后pi(u)=(7/8,u/8,(1-u)/8)。第一块从两历史得到u1和u0。余r个可见因子对时，s=(c/4+d,c+d,4c+d)，完整两步条件更新给
f_(r,c,d)(u)=1/(1+alpha+beta u)，
alpha=(2r+c/4+d)(2r-1+c+d)/[7(2r+4c+d)(2r-1+4c+d)]，
beta=3c alpha/(2r+H)。
最终为f1 composed ... composed f_(k-1)作用于1/0，Delta=|u0-u1|/8。它是两旧历史的条件状态TV。c=2M,d=M准确恢复C59。

## 3. 全范围两侧界及幂增长分类

准确差分倍率为beta/[(1+alpha+beta u)(1+alpha+beta v)]。r,c>=1,d>=0时，alpha>=1/448、alpha+beta<=1/7，beta在3c/[896(r+H)]与3c/[7(r+H)]之间。alpha下界来自两个比值至少1/16和1/4，alpha+beta是有序似然比除7；差分分母至多64/49。

令P=c^(k-1)H!/(H+k-1)!=product_(r=1)^(k-1)c/(H+r)。逐步相乘给
(1/8)(21/8192)^(k-1)P <= Delta <=(1/8)min{7^(-(k-1)),(3/7)^(k-1)P}。

所以logDelta=(k-1)log(c/H)-sum log(1+r/H)+O(k)，常数与c,d无关。
若c_k=ceil(k^a)、d_k=ceil(k^b)，a,b>=0，则
logDelta=-[max(1,a,b)-a]klogk+O(k)。
a>=max(1,b)时Delta=exp[-Theta(k)]。证明按H<=O(k)和H>=Omega(k)分别估计sum log(H+r)，用阶乘积分界即可。

同样隐藏总量H=k²：c1/d(k²-1)给-2klogk+O(k)，c(k²-1)/d1给指数级。有限k、c>0时状态响应秩仍2。c0边界beta0，第二块后精确同步u7/8；d0时内部差别仍可存在，但完整隐藏尾只有一种顺序，不能据内部秩宣称该尾可辨。

## 4. 同总量的有限见证

k20,H30，c=1/3/6/10/15/20/25/29时，Delta准确分数的小数依次为
7.04272765250e-44，1.15196996971e-36，1.71524737031e-33，2.41834728068e-32，1.85125970780e-32，2.77647814318e-33，1.69060838931e-34，1.07475401473e-35。

同k20,H400，c1/20/100/200/300/399时依次为8.92712696e-61、4.25388289e-38、4.79744988e-32、1.22037381e-33、5.50239871e-37、8.52431664e-42。总量和原反馈不变，组成效应非单调。

## 5. 随组成变化的共同极限与有限反推

alpha_theta=(1-3theta/4)/[7(1+3theta)^2]，beta_theta=3theta alpha_theta，F_theta(u)=1/(1+alpha_theta+beta_theta u)。唯一正固定点
u_theta=2/[1+alpha_theta+sqrt((1+alpha_theta)^2+4beta_theta)]。

对全k,c,d有
|u_(k,c,d)-u_theta|<=7^(-(k-1))+91/(72H)。

证明：令x2r/H、y(2r-1)/H。有限alpha与alpha_theta差<=9r/(56H)，beta差<=43r/(56H)。前式用max(15theta/4)/(1+3theta)^2=5/16和max3theta/(1+3theta)^2=1/4，后式用beta=3theta alpha/(1+x)。映射差<=13r/(14H)；外层共同1/7收缩，求和r7^(-(r-1))给91/(72H)。固定点初值项给剩余7^(-(k-1))。

因此任意k,H→infty且c/H→theta∈[0,1]时，两历史同趋pi_theta=(7/8,u_theta/8,(1-u_theta)/8)。

u_theta严格递增：令g=alpha_theta(1+3theta u)，则g_theta'=-3[18theta u-3theta-4u+9]/[28(1+3theta)^3]<0。theta<=2/9时括号最小5+15theta，否则最小9-3theta>=6。因此F_theta与唯一固定点随theta增加。

给定极限u，theta为[0,1]内唯一根：
[252(1-u)+9u²]theta²+[168(1-u)-12u²+3u]theta+28-32u=0。

theta=0/1/10/1/4/1/2/2/3/1时，u依次为.875/.909483574797/.939318503651/.966193049123/.977091224244/.991208281576（第一串theta按0、1/10、1/4、1/2、2/3、1解读）。根值均有严格有理包络。

有限读数反推：已知k,H且u_hat误差eta，将u_hat±[eta+7^(-(k-1))+91/(72H)]经单调逆映射，得到theta严格范围。k12,H100000、真实theta1/2、u误差1e-7时，向外范围[.49982809,.50015733]。它包含有限尺度误差，是确定性输入预算，不是采样置信区间。

## 6. 隐藏占优时的唯一最慢组成及稀释常数

若H/k→infty、theta→theta0>0，系数一致趋向极限，统一收缩使两轨道除初始过渡外靠近u_theta0。准确差分乘积的对数平均给
lim Delta^(1/k)=R(theta0)=beta_theta0*u_theta0²。

R随t=beta/(1+alpha)^2严格增加，因为R=(sqrt(1+4t)-1)/(sqrt(1+4t)+1)。
t(theta)=84theta(4-3theta)(1+3theta)^2/(252theta²+165theta+32)^2，
t'=-168(3theta+1)(2241theta³+1098theta²-150theta-64)/(252theta²+165theta+32)^3。
该三次多项式只有一次正号变化，且在0负、1正，故唯一正根属于(0,1)。R具有唯一最大点
theta*=.2473633613627779144274381035034...，R*=.0250815717549954082431224163582...。
两项均已给严格有理区间；这是隐藏规模占优范围中的解析最慢组成，不是从有限表选最大值。

若H/k→infty、theta→0、c>=1，则更精确地
lim [8Delta/theta^(k-1)]^(1/(k-1))=21/64。
证明为所有r<=k和u,v下alpha→1/7、beta/theta→3/7，差分倍率除theta一致趋向21/64，取正几何平均。旧历史差别消失的同时极限状态仍是(.875,.109375,.015625)，没有把剩余随机性消去。

## 7. 返回族及后续观察

对各含2r次2/3且回xi0的全部可见返回词，c,d>=1，C58唯一无22例外仍为(23)^r(32)^r。其余精确同步。例外前半段u差<=B=product_(n=r+1)^(2r-1)min{1/7,3c/[7(n+H)]}。
一次映射后u∈[7/8,448/449]，logit导数<=201601/448；共同非负核和终端正W不增项目距离，归一化TV至多该距离1/4。因此对任意组成增长、任意共用严格正W，完整隐藏尾读数差<=min{1,(201601/1792)B}<=min{1,(201601/1792)7^(-(r-1))}。仍保留全部尾顺序，而非提前压成总概率。

## 8. 实际验证、归属与保存

run_checks.py全部断言通过：576三态/递推行、192两侧界、2640差分常数、1320系数极限界、24 C59退化、160有限误差、9缺席边界；30完整词条件行/114逐词概率、60选后行、381秩分类、204返回、12正终端返回界、14同总量/20尺度配置、7根区间、16有限反推、12干预、5初始1至5、64原BRC串联/并合。计数重叠，不称独立样本。有限结果全用Fraction，没有Monte Carlo。

limit_checks.py通过39项实际断言，包括6符号身份、严格最慢组成/倍率区间及长路径数值核对。高精度数值另标近似，不代替渐近证明。原BRC8138字节/blob9a3962ec095095f14e63a91cfe6b7ebf07d9a1d1与当前EM元数据一致，字节原样执行。各脚本首次完整运行即通过。

实际公开读取Turner等PlackettLuce作者文档§1、Van Handel0708.3412作者摘要/引言、Cohen/Fausti2309.02413v2作者摘要。一般逐次排序、初态遗忘和Hilbert/TV保留既有归属；本轮组成计数、有限反推和极值推导为作者结果，独立复核、形式化、新颖性全面审查及物理标定另行开展。

完整RESEARCH_NOTE.md、hidden_composition.py、run_checks.py、limit_checks.py、精确JSON、实际日志和最小继承依赖交付于prime_quantum_hidden_composition_c60.zip。此远端是可独立恢复的科学摘要，不声称全部代码已合入。

本轮新session_start(prime-c60-hidden-composition-20261107-a1)返回BACKEND_IDENTITY_OR_VERSION_MISMATCH、operation_sent=false，无新session/activity/CLAIM；未借用任何旧凭据。科学归档与登记状态分开。

下一单元：保持同一反馈，让隐藏5/7在可见序列之间实际进入并被消耗，比较组成比例与动态组成轨迹何者足以继续预测收缩，接续当前固定未消费组成的已证明结果。
