# C47：隐藏因子内部相互作用与局部均匀化

Progress-Event-ID: prime-c47-interacting-environment-20261101
Date: 2026-11-01 Asia/Taipei
Status: AUTHOR_DERIVED_WITH_EXPLICIT_STANDARD_LLT_DEPENDENCY / FINITE_EXACT_CHECKED / INDEPENDENT_REVIEW_PENDING
Global-read: 2fe28e5059254fda19a9ab74bee5171bd8acaaba
EM-read: f42f2906d77f24085c123f3ccfe9667d41caa96d
Pre-publication-main: b118a8e1cff7e63d03adc0b22d775623bab96884
Research-Activity-ID: NONE_ALLOCATED; REGISTRATION_PENDING

## 1. 接续与模型

消费C46@ee02493723050cc1661e82c802e8727b29abe510:research_notes/divisor_extrema/20261030_c46_competing_hidden_environments.md，blob8a6d7812536a363e16d4cbdc6c255391a9d7d9ab及实际挂载包。C46的gamma0定理和gamma1有限数据保持各自范围；本轮完成gamma1共同增长的局部极限。

保留2^m3^m，m固定，完整目标2^m3^m5^c7^d。素数单步图、全部不同因子词、rho_1和正路径权保留。Delta上三角为(1,-1,1,1,-1,gamma)，本轮主定理gamma=Delta57=1。均匀完整词参考P0，终端权q^(D²)，0<q<1固定。若保留词为v，r=X23(v)，间隙高度h_j=#3-#2，隐藏占用k_j/l_j，I=X57，则

 S=sum h_j(k_j-l_j), R=r+S+gamma I,
 H=m²+gamma cd, D=2r-m²+2S+gamma(2I-cd).

gamma1时D≡m²+cd mod2。每条v的扩展数(L+c+d)!/(L!c!d!)相同，L=2m。隐藏指观察中省略，完整作用不删除。共同节点势Omega²使单位系数例的正向增量保持正而不改D。辅助排序/间隙不是物理时间或原生空间，P000/X6不变；真实选择律和物理读出需独立依据。

## 2. 新主定理

令t=min(c,d)趋无穷，max(c,d)≤Bt，B固定。C_m=binom(2m,m)，delta_t=(m²+cd)mod2，Theta_delta(q)=sum_(z≡delta)q^(z²)。则在总变差中

 Law_Q(v,D) - [Uniform(V_m) × q^(z²)/Theta_delta_t(q)] -> 0.

D的各固定阶绝对矩及与有限局部观察的混合矩也收敛。delta_t改变时使用相应余类，不声称D跨奇偶具有单一极限。局部v无须分子列，各趋1/C_m。

误差阶可取O(1/t+|c-d|/t^(3/2))，常数依赖固定m,q,B。等量或平方根失衡时为O(1/t)，一般固定正比例为O(t^-1/2)；它不是已给出数值常数的有限样本置信界。

特别m2时六词各趋1/6，局部r均值每个规模即为2，方差趋5/3；一般m的极限方差为m²(2m+1)/12。此与C46 gamma0、等量环境的22/15不同。同样的因子数量并不决定局部极限，隐藏—隐藏路线差也参与。

## 3. 标准输入与自足应用证明

外部输入：Canfield/Janson/Zeilberger, The Mahonian probability distribution on words is asymptotically normal, Adv.Appl.Math.46(2011)109–124，arXiv0908.2089v1，Theorem4.5式4.9。对均匀二字词逆序数I_ab，mu=ab/2、sigma²=ab(a+b+1)/12，在max(a,b)≤C exp(c0 min(a,b))条件下，对所有整数z一致有

 P(I_ab=z)=sigma^-1 phi((z-mu)/sigma)+O(1/(sigma min(a,b))).

本轮只需a,b同阶增长，满足该定理条件。实际读取原文解析式及作者2012勘误；勘误补充经典Mann–Whitney/Diaconis/Takacs研究归属，未改本轮用的4.5。web截图返回Cache miss，公共PDF下载失败，没有声称视觉核对成功。一般逆序方差与LLT归于既有工具，本轮为下面的局部投影应用。

给每次因子独立均匀优先值，排序再去临时标记，准确实现原P0。条件于v，可见优先值的J=L+1个间隙X为Dirichlet(1,...,1)，不依赖v标签。给定X，k~Mult(c;X)、l~Mult(d;X)独立。给定占用，各间隙内5/7排序独立均匀，

 I=sum_(i<j)k_i l_j+sum_j I_j, I_j~I_(k_j,l_j).

S只依赖占用，与内部排列分开保留。选j*为最大间隙，则X_j*≥1/J。事件G:k_j*,l_j*≥t/(2J)的补集概率≤2 exp(-t/(8J))。G上这两个数在固定正倍t范围内，sigma_j*²=Theta(t³)。上述LLT和正态密度的全局导数界给

 sup_u |P(I_j*=u+b)-P(I_j*=u)|≤C|b|t^-3+Ct^-5/2.

给定全部占用、其他间隙内部排列，D=z与未扰动I的点事件只差整数平移r+S。去掉平移并积分恰是原二字词I_cd在k0(z)=(z+m²+cd)/2的点概率，独立于v。因此

 sup_(合法z)|P(D=z|v)-P(I_cd=k0(z))|
 ≤Ct^-3 E|r+S|+Ct^-5/2+2exp(-t/(8J)).

给定X有E(S|X)=(c-d)M、Var(S|X)=(c+d)V，M=sum hX、V=sum h²X-M²。故E|r+S|≤C_m(1+sqrt(t)+|c-d|)。再对完整I_cd用LLT，令b_cd=1/(sqrt(2pi)*sigma_cd)，得到

 |P(I_cd=k0(z))-b_cd|≤Ct^-5/2+C(z+m²)²t^-9/2.

乘q^(z²)及任意固定次|z|后求和，尾部可求和；每条v的接受权为b_cd Theta_delta(q)[1+O(e_t)]，e_t=1/t+|c-d|/t^(3/2)。均匀参考的v数有限，归一化即给主定理及矩收敛。证明只要求至少一个间隙大，未丢弃单纯形边界。

等量c=d=t时，E0q^(D²)~sqrt(3/pi)Theta_delta(q)t^-3/2。这里是接受权解释下的选择份额，不是物理速率或计算效率。一般固定可求和终端W在合法余类上有正总量时，同样有局部均匀极限；相应矩需相应可求和条件。

## 4. 整体约束仍存在；隐藏奇偶保留

联合极限中D与局部v渐近独立。q1/2时Var(D/2)沿偶/奇余类趋C44的正级数常数约0.11121660134211324和0.25778245694161250。m2、c=d=t时delta=t mod2；局部都趋均匀，整体残差仍保留环境奇偶。

令T_env=S+I-cd/2，D/2=r-m²/2+T_env。由联合矩得到Cov(r,T_env)趋-m²(2m+1)/12，Var(T_env)趋m²(2m+1)/12+K_delta(q)。整体约束可以由联合补偿实现而不把局部路径锁定。

## 5. 有限尺度顺序差别及弱作用比较

任意可见0/1词v，J=L+1，A=sum h、B0=sum h²，Vbar=(J B0-A²)/(J(J+1))，C_v=sum_(j=1..L)s_j j(J-j)，s_j是3的+1或2的-1。均匀参考条件于v有精确公式

 E S=(c-d)A/J;
 Var S=[c+d+(c-d)²/J]Vbar;
 Cov(I,S)=-cd C_v/[J(J+1)];
 Var I=cd(c+d+1)/12;
 Var(D|v)/4=gamma² VarI+VarS+2gamma Cov(I,S).

由独立优先值比较和Dirichlet二阶矩直接推导。对2332/3223、c=d=t，两者VarS都为2t/3，但Cov(I,S)分别为-2t²/15和+2t²/15。相同占用直方图在有限尺度仍有不同联合响应；渐近均匀不能授权删除有序记录。

若gamma=alpha/t，则精确有Var(D|v)/4=t[alpha²/6+2Vbar-2alpha C_v/(J(J+1))]+alpha²/12。gamma*t是未选择方差的比较量；本轮未将其当成选后临界分布定理。

## 6. 任意小的固定倒数作用与非交换极限

取gamma=1/a，a固定正整数，原q保持不变。Dtilde=aD=2(ar+aS+I)-(a m²+cd)，且q^(D²)=(q^(1/a²))^(Dtilde²)。隐藏内部系数为1，其他作用只乘固定a，第3节证明仍适用，所以每个固定a下局部均匀。

对m2、c=d=t的选后局部方差F(t,gamma)：
 lim_(a→∞)lim_(t→∞)F(t,1/a)=5/3;
 lim_(t→∞)lim_(a→∞)F(t,1/a)=22/15.

第二式内极限由有限词族的连续权重给出，再用C46。固定a的常数不对a一致；这是明确的非交换极限，不是物理相变断言。一般实gamma及随t衰减的完整极限分别待研究。有限执行核验了倒数作用的整数分子/奇偶恒等式，没有将非整数指数权声称为有理数运算。

## 7. 精确数据与验证

q1/2、gamma1、c=d=t时，t1/5/10/30/50的局部方差约0.8359150800、1.5993531433、1.6545253908、1.6657702933、1.6663805256；TV到六词均匀约0.2136783730、0.0338723258、0.0143035957、0.0044776835、0.0026729887。

t50六词概率为0.1666283865、0.1666767167、0.1693195552、0.1640702383、0.1666767167、0.1666283865。有限有序偏好仍可见。t49的Var(D/2)约0.2577820726，t50为偶余类近似；两者沿各自子列收敛。

固定比例c=2d，d5/10/20/30的局部方差约1.641361179、1.641356213、1.648939846、1.653489439；有限值不要求单调。q1/3与2/3、t20的方差约1.664376296、1.664376601。

1085套有理gamma条件矩；868套稠密整数DP/旧字典DP/直接词完整计数对照，含360套原BRC对照；14431条直接扩展；72项原BRC正权总和；144尾界、72奇偶/矩、48方差多项式、4无选择控制及4初始空/单类路径。另144二字词矩、124有序间隙完整联合对照（14142扩展）、10080倒数缩放恒等式。两个扩展覆盖可能重合，未合称独立总样本。所有声明断言通过。

18行较大参数结果，最高等量50/50，另60/30；340949471次整数系数加法。保留|D|≤16后对遗漏正质量与非负矩用最小遗漏q^(D²)给有理上下界，展示概率最大区间宽约1.66e-56，无Monte Carlo。规模结论由定理而非数表外推。

原BRC8138字节/blob9a3962ec095095f14e63a91cfe6b7ebf07d9a1d1与本轮EM源一致并实际执行，串联/并合各13402次。新DP只并合(保留位置,隐藏次数,分数)相同且后续等价的状态，signed观察不抵消positive mass。

完整RESEARCH_NOTE.md、interacting_environment.py、run_checks.py、gap_checks.py、精确结果和最小继承源码在C47对话复算包；本文件为独立摘要，未声称所有代码合入远端。

公开来源：arXiv0908.2089v1 Theorem4.5；作者修订页https://sites.math.rutgers.edu/~zeilberg/mamarim/mamarimhtml/mahon.html及mahonerratum.pdf。一般统计原理有既有归属，本轮无全面新颖性审核。

2026-11-01 session_start(prime-c47-interacting-environment-20261101-a1)实际返回STATIC_READONLY_SCOPE_DENIED、operation_sent=false，无session/activity/CLAIM，未绕路登记。作者推导、自检、独立审核、形式化与物理验证分别记录。

下一义务：gamma_t*t保持有限时的完整选后局部极限；局部长度也随隐藏环境增长时的平滑范围。当前单元的固定局部、单位作用、同阶隐藏规模定理已经明确闭合，保留其标准LLT依赖。