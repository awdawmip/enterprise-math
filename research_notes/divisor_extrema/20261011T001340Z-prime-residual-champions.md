# 素数残差、冠军合数与下一素数：可加基线、组合缺陷与局部约束

Progress-Event-ID: `prime-residual-champions-20261011T001340Z`
Scope: `enterprise-math / symbolic residual-interface design and external integer local-support comparison`
Status: `UNREVIEWED_RESEARCH_NOTE; NO_NATIVE_RESIDUAL_ATTRIBUTION; NO_PRIME_PREDICTOR_PROVED`
Global-read: `2415716de586c52eb2615cc10604432998460ece`
EM-source-read: `3d174bc233263dd45efebc34e5704e7506991ba5`
Research-Activity-ID: `NONE_ALLOCATED; REGISTRATION_PENDING`

## 1. 用户问题与保留边界

用户问：如果每个素数带一个残差，下一个素数的产生会不会与比它小的某种冠军合数的残差累积有关？

本轮不把残差定义成与平方数之差，不把模p余数自动提升为心跳原生残差。P000保持原义。本轮没有给原生r(p)赋数值，也没有执行原生动力学或经典物理参考计算。原生残差可以是有标签的关系状态，不预设为标量或小量；下列线性公式仅针对可加有理向量读出。

前轮已有Source：enterprise-math@b6b5005d590778e746bbf888dd16bb68f6c1ad3d:research_notes/divisor_extrema/20261010T105855Z-survey-and-exact-check.md。保留其约数极值计算，不重复生成10^18冠军表。

## 2. 可加基线的完整推导

设每个素数p有符号标签r_p（可取Q^m中的向量），且R(1)=0，R(ab)=R(a)+R(b)。则R(n)=sum_p v_p(n)r_p，这是完全加性算术函数，不构成新素数生成机制。

对任意H（不要求冠军），记A(H)=sum_{d|H}R(d)，tau(H)为正约数数。约数互补对满足R(d)+R(H/d)=R(H)，因此：

2 A(H)=tau(H) R(H).

平方H的中间约数由该双射照常处理，无特殊壳假设。故将所有约数的可加残差相加，只得到tau/2倍的整体读出，没有产生独立于(tau,R(H))的新信息。这不说明R(H)不可能有预测价值，只否定把这种求和本身当成新增信息。

均匀选取约数，对H=product p_i^a_i，指数e_i独立均匀于0..a_i。标量读出有：

E R(d)=R(H)/2；Var R(d)=sum_i a_i(a_i+2)r_i^2/12。

向量读出的协方差为sum_i a_i(a_i+2)r_i r_i^T/12。该方差描述声明的有限均匀约数族，不是物理温度或动力学涨落。

静态状态不足：严格高合成数60到120之间最小纪录者不变。已知素数61和67时，冠军均为60，但下一素数分别67和71。因此任何仅依赖固定R(60)的无其他输入的单值规则不能同时输出两者；此反例不排除还携带当前位置、完整历史或动态场的规则。

## 3. 非加性补丁与下一步必须补的接口

对具有同一可比向量读出的任意R，定义K(a,b)=R(ab)-R(a)-R(b)。则恒等式为：

K(a,b)+K(ab,c)=K(b,c)+K(a,bc)，

2 A(H)=tau(H)R(H)-sum_{d|H}K(d,H/d)。

这些是代数恒等式，不是素数定理；K被定义出来不等于已获独立原生计算规则。第一式确保整数相等且来源可安全商去时两种结合次序一致。若原生路径顺序实际可观察，则应保留路径标记而非强制同一R(n)。

补充统计Xi(H)=2A(H)/tau(H)-R(H)=-average_d K(d,H/d)。Xi非零见证这一读出的非加性；Xi=0不能推出所有支路K都为零，不能把正质量当有符号量相消。

要关联下一素数，还需把乘法组合与n->n+1的整数邻接相连。仅有R(ab)规律不自动给出候选位置的残差更新或新不可约结构的触发条件。不要把“非零”“清零”“固定阈值”未经推导设成生成标准。

一个严格的外部基线：给定所有已知素数<=q，它们生成的乘法闭包S_q={product_{p<=q}p^a_p}。最小的n>q且n不属于S_q必为下一素数：若它合成，其真因子均小于n，按最小性都在S_q，乘积也在S_q，矛盾。这是乘法闭包形式的既有素数判定，不是新的动力学解释；单个冠军的约数只覆盖一个有限指数盒，不等于整个闭包。

## 4. 贴近的已知关系：小素数局部约束与间隔

考虑两个候选位置x和x+h。对素数p，禁止的起始剩余类为0和-h；h被p整除时两个禁止类重合，否则不同。记nu_p(h)=1或2，则合法类数p-nu_p(h)。这是外部整除约束，不命名为原生残差。

固定有限质数集P，对每个合法剩余类赋正有理权1/p，使用BRC串联合成并保留(p,r)标签。由CRT，完整模Q=product(P)的合法起点数为product(p-nu_p(h))，质量为product(1-nu_p(h)/p)。这是精确有限恒等式。

归一化成两个独立单点的基线，S_P(h)=product[(1-nu_p(h)/p)/(1-1/p)^2]。当2在P、h为偶数时，相对h=2的比值为：

B_P(h)=product_{p|h,p>2,p in P}(p-1)/(p-2)。

局部指数a_p>=1后不再增加此量；增益来自不同质数的禁止类重合而非正质量的符号抵消。

所有素数版本的奇异级数为S(h)=2C2 product_{p|h,p>2}(p-1)/(p-2)（偶数h）。此函数本身是确定的，拿它描述真实素数对的渐近次数属于Hardy-Littlewood型猜想；“素数对”也不要求相邻，中间没有素数需要额外控制。

对这种增益，最小纪录者为质数阶乘：同样k种质因子，小质数成本更低且(p-1)/(p-2)更高；再增加下一种质因子提高增益，重复幂不提高增益。这不是普通tau冠军同一目标。

Goldston-Ledoan在适当素数对/三元组猜想下证明充分大的相邻素数间隔冠军为质数阶乘。这支持冠军乘法结构和间隔统计之间的联系，不证明一个低于目标素数的冠军通过残差累积决定下一素数位置。Holt-Rudd研究的是筛中剩余类间隔，其文中明确区分筛存活与最终素数存活。

## 5. 实际BRC执行与有限复核

工具源：enterprise-math@3d174bc233263dd45efebc34e5704e7506991ba5:src/enterprise_math/brc_weighted.py；全文件Git blob 3f205696709e847909958a153f8fe10d3f6b70f0。工具定理来源同ref的definitions/ENTERPRISE_BRC_WEIGHTED_LOG_FOUNDATION_20260902.md，WBRC-T01。

实际读取源前240行，保留到cwm_from_positive_weights结尾的源码节选，用AST略去未调用的两个相对import；CWMState、cwm_from_positive_weights、cwm_propagate等定义正文未改。不是完整项目安装或全项目测试。输入为有来源标签的正权剩余类或单位权指数支路；观测为有限count/total/dominant，不用于模拟符号幅值抵消。状态：REUSE_EXECUTED_SCOPED_EXCERPT。

P=(2,3,5,7,11,13)，Q=30030。对11个h逐个穷举完整30030个剩余类，与BRC计数全部一致：

|h|合法起点数|相对h=2增益|
|---:|---:|---:|
|2|1485|1|
|4|1485|1|
|6|2970|2|
|12|2970|2|
|30|3960|8/3|
|60|3960|8/3|
|120|3960|8/3|
|210|4752|16/5|
|420|4752|16/5|
|840|4752|16/5|
|2310|5280|32/9|

另对1..4种形式质因子、每个指数1..4的340个指数盒，共41370条约数支路，精确检查可加均值、方差以及二次交互的对角/非对角系数。没有为任何原生r_p拟合参数。上述有限检查支持实现与恒等式一致，不证明真实残差、素数生成或无穷外推。

复算文件：check.py、brc_weighted_source_excerpt.py、results.json。源码节选SHA256=0a591fd46d335293fbed05d1647d4d6ee15b8489c9a14cadb60ce9083b8c551f。沙盒附件不是跨对话长期来源；本笔记提供独立复写所需完整计数关系、输入和输出。

## 6. 最小后续单元

先从现有原生BRC构型取得不使用未来素数标签的r_p及组合接口，保留方向、路径、指数和观察者。以30、60、120（相同质因子支持、不同幂次）为对照，不把筛法余数当原生残差。给出候选位置x下R_x(c)与K_x(a,b)的更新律及已声明的未来观测；检验是否存在对后继候选有影响、却不能由普通整除约束和可加重复计数解释的差异。

冠军选择在看目标素数前固定。检验时比较普通整数、tau冠军和质数阶乘，控制输入规模与质因子支持；训练与后段验证分离，同时预测合数反例；报告复杂度而非把试除隐藏进残差计算。不预先宣称冠军必有优势，也不因新K非零就认作素数生成。

## 7. 来源与身份状态

- P. Haukkanen, J. K. Merikoski, T. Tossavainen, The arithmetic derivative and Leibniz-additive functions, arXiv:1803.06849v1，已读HTML的完全加性及Leibniz组合部分：https://arxiv.org/html/1803.06849v1 。
- D. A. Goldston, A. H. Ledoan, The jumping champion conjecture, arXiv:1102.4879v2，已读HTML定义、条件定理、奇异级数和primorial纪录性质：https://arxiv.org/html/1102.4879v2 。
- F. B. Holt with H. Rudd, Combinatorics of the gaps between primes, arXiv:1510.00743v2，已读HTML的筛循环和适用边界：https://arxiv.org/html/1510.00743v2 。

本轮em_session_start(request_id=divisor-residual-20261011-session-start)实际返回STATIC_READONLY_SCOPE_DENIED，operation_sent=false。没有新研究员身份、activity或CLAIM；Source研究笔记仅作授权的来源保全，不是原生登记、正式任务发布或数学准入，也没有更改定时任务。
