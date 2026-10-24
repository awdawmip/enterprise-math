# R265：三来源正权 BRC 共同效果纤维的次阶奇偶分裂

2026-10-24。研究类别：作者侧解析证明及精确符号、整数验证；UNREVIEWED / NOT_ADMITTED。前沿：R264，提交 6498dfa6289b9e909a8666979f278f08d41592fa。本稿证明范围仅是固定的正权六槽仿射 BRC *辅助观察器*，不是 P000 原生六维 Cell 心跳动力学或原生 R193 查询、来源与时间端口。全部来源词保留顺序及整数正重数，连续分析只是事后从离散计数提取渐近系数。

## 1. 固定模型与目标

二元原始动作 a=0,1，隐藏控制态 q=0,1,2。仿射效果 (epsilon,k)，epsilon=±1，单步为 epsilon'=eta*epsilon, k'=eta*k+b；引入可逆整数标记 t=epsilon*k，于是 t'=t+epsilon'*b。每条控制态动作的 (q',eta,b) 为：

| q | a=0 | a=1 |
|---|---|---|
| 0 | (2,-1,-1) | (2,+1,-1) |
| 1 | (0,-1,-1) | (0,+1,-1) |
| 2 | (1,+1,+1) | (2,+1,-1) |

来源监测 r 在 a=0 下 0→1,1→2,2→2；在 a=1 下 0→0,1→0,2→2。初态 (q,r,epsilon,t)=(0,0,+1,0)。令 n_r(m;q,epsilon,t) 为长度 m 的完整有序路径数，定义

M_m=max_{q,epsilon,t} min_{r=0,1,2} n_r(m;q,epsilon,t)。

设 phi=(1+sqrt(5))/2，v=3/2+7 sqrt(5)/10，C=1/[5 phi sqrt(2 pi v)]，均为分析计数所需的常数。

**作者侧定理。** 对上述固定模型，

M_m=C phi^m / sqrt(m) [1 + beta_{m mod 2}/m + o(1/m)]，

beta_even=23/2−33 sqrt(5)/8≈2.27621959281337，
beta_odd=281/4−243 sqrt(5)/8≈2.32943518344389。

所有充分大的偶数 m 的唯一最优共同效果纤维为 (q,epsilon,t)=(2,+1,2)，所有充分大的奇数 m 的唯一最优共同效果纤维为 (2,-1,-3)。原始 k=epsilon*t，故分别 k=2 与 k=3。仅断言存在稳定阈值，不声称求得有效最小阈值。

## 2. 八态正权 Laurent 传输和精确生成函数

来源模式 r=1 等价于二元词不含相邻 00 且以 0 结束。令允许前缀状态按 A±=(q0,last1,epsilon±), B±=(q2,last0,epsilon±), C±=(q2,last1,epsilon±), D±=(q1,last0,epsilon±) 排序；起始视 last=1 仅用于让第一步两动作均合法。定义 T(z) 的 (target,source) 元素为相应合法动作的 z^(epsilon'*b)；路径计数在正整数半环上组合。对 (I−x T(z)) 的精确有理消元得到 B+、B− 生成函数

G_+(x,z)=x^5(x−z)/[(1+x²)(x^6−2x^4+x(z+z^(−1))−1)]，

G_−(x,z)=−x(x−z)(x³ z+x z−1)/[(1+x²)(x^6−2x^4+x(z+z^(−1))−1)]。

系数 [x^m z^t] G_epsilon 恰是 n_1(m;2,epsilon,t)。特征多项式精确为

det(lambda I−T(z))=(lambda²+1)[lambda^6−(z+z^(−1))lambda^5+2lambda²−1]。

令 z=e^s，lambda(s) 为 s=0 时等于 phi 的解析正主根。隐函数严格展开：

lambda(s)=phi+(5/4+11sqrt(5)/20)s²−(101/24+1129sqrt(5)/600)s⁴+O(s^6)。

因此 log lambda(s)=log phi + (v/2)s² +(kappa4/24)s⁴+O(s^6)，其四阶累积量为

kappa4=−153/2−1711sqrt(5)/50。

此式与以前 R261 的线性方差系数 v 兼容，但第四阶系数是本轮新增结果。

## 3. Perron 留数与整数格点局部渐近

对 G_epsilon 在 x=1/lambda(s) 的主极点取留数，写其主增长项为 C_epsilon(s)lambda(s)^m。准确得到两符号相同的主幅值 C_+(0)=C_−(0)=1/(10 phi)；归一化一、二阶导数如下：

| epsilon | a1=C'/C | a2=C''/C |
|---|---|---|
| + | (3+sqrt(5))/2 | −(99+45sqrt(5))/10 |
| − | −(1+sqrt(5)) | −(37+20sqrt(5))/5 |

单位圆上该强连通传输的谱模最大仅发生在 z=1 和 z=−1（异号单位增量的自环给出相位约束）；其余圆弧有严格谱隙。每步 t 增量为 ±1，所以 t≡m(mod 2)。在这两个主峰附近进行 Fourier-Laurent 系数展开，两个峰因格点奇偶贡献因子2。对于每个固定的允许整数 t，

n_1(m;2,epsilon,t)=C phi^m /sqrt(m) [1+beta_epsilon(t)/m+O_t(m^(−2))]，

beta_epsilon(t)=kappa4/(8 v²)−a2_epsilon/(2v)+(a1_epsilon*t−t²/2)/v。

上式通过 Taylor 积分的高斯二阶和四阶矩得到。其四阶谱项为 kappa4/(8v²)，二阶留数项为 −a2/(2v)，平移与偏态项为 (a1*t−t²/2)/v。这里的 Fourier、Gaussian、pi 仅用于对形式正整数路径计数做外部解析读出，不是项目原生 BRC 运算或时间更新。

## 4. 奇偶峰位与全局定位

每个 beta_epsilon(t) 都是严格凹二次函数，实顶点是 a1_+=(3+sqrt(5))/2≈2.618、a1_−=−(1+sqrt(5))≈−3.236；只允许 t≡m(mod2)。四种最优离散候选：

| m | epsilon=+ 最优 | epsilon=− 最优 |
|---|---|---|
| 偶 | t=2；beta=23/2−33sqrt(5)/8 | t=−4；beta=213/2−373sqrt(5)/8 |
| 奇 | t=3；beta=111/4−91sqrt(5)/8 | t=−3；beta=281/4−243sqrt(5)/8 |

不同符号赢家的确切差为 beta_+(2)−beta_−(−4)=(85sqrt(5)−190)/2>0（偶），beta_−(−3)−beta_+(3)=85/2−19sqrt(5)>0（奇）。同符号其他整数 t 因严格凹性严格较差。

**排除远离中心的随 m 变化的竞争者：** 固定 t 的局部展开不够，须控制全体整数。对 |t|≤m^(1/8) 由 Fourier 双峰上的统一解析展开得到相对余项 O((1+|t|^4)/m²)=o(1/m)，而 beta_epsilon(t)=−t²/(2v)+O(|t|+1)，故除有限个位于中心的格点以外，其他候选严格落后。对 m^(1/8)<|t|≤delta*m，用正 Laurent 传输的实指数倾斜 z=e^s（令 d/ds log lambda(s)=t/m），统一局部积分给出 O(lambda(s)^m/sqrt(m)) 因子，tilt 指数 m(loglambda(s)−logphi)−st≤−c*t²/m，不能与中心主峰竞争。对 |t|>delta*m 用符号匹配的小固定 tilt s0 得 e^(−c_delta*m) 衰减。这些常数由主根解析性、v>0 和固定有限矩阵谱隙给出，无需把有限枚举误当全范围证明。由此，充分大的全体整数 t 及两种 epsilon 均被上述唯一赢家支配。

三模式共同纤维必须末态 q=2，因为 r=0 的可达末态 q 为 {0,2}，r=1 的可达末态 q 为 {1,2}。R264 已证明相同 q=2、固定中心效果位置的 n0/n1→phi³>1，n2/n1→infinity（n2 的主增长率为2，大于 phi），故在此唯一赢家处 min(n0,n1,n2)=n1。而在任意纤维 min≤n1。夹逼即得 M_m 的次阶渐近与稳定唯一最优位置。

## 5. 验证、真实性、下一问题

以 SymPy 完全精确检验 T 的特征多项式、有理 G± 恒等式、lambda(s) 二阶和四阶系数、kappa4、C_epsilon 的导数和四个奇偶 correction；独立逐词路径解释器核对长度0..13全部 16,383 个二元词，与正整数动态规划状态逐项一致；动态规划推进 m=240，并检验每一步总质量2^m、t奇偶格点、M 与 r1 峰位。R264 的 M140 与 M200 一致。代表值：M95=211611785102211993（epsilon−,t−3），M96=340325372582384001（epsilon+,t2），M200=1263924779564116173737130828762162554832，M240=263510796143711210750650160524192163023027602312。m63/64 尚呈竞争者峰位，绝不可宣称实测已有最小稳定起点。实际执行的完整 SymPy/Python 程序及逐点机器 JSON 见同轮证据包；有限实验只验证已声明的代数与计数，不证明所有 m 的渐近断言。

沿用已验证的 T0_BRC provenance-positive affine effect law（REUSE_APPLIED），无新顶层 BRC 家族。未执行原始 enterprise_math 包、R193 原生来源/时间端口；未给出 P000 X6 Cell 原生状态保真嵌入。GitHub 非正式研究分支的保存不代表原生研究 Source Result，活跃 owner 未确认（em_control_tasks CONTROL_QUOTA；em_session_start STATIC_READONLY_SCOPE_DENIED，operation_sent=false）；缺少独立 Driver 审查，不得提升 Foundation 或 Working Truth。

Pinned sources: GLOBAL_KNOWLEDGE_V1 main@94cc7009b96256b6a59a2cf950081112c411365a；enterprise-math main@b1e773f528ecec65959c46881e698c27331190ab；R264@6498dfa6289b9e909a8666979f278f08d41592fa。
下一精确目标：求出有效且严格证实的奇偶峰位稳定阈值 m0；或求相对 1/m² 校正；保持 R193/P000 保真映射为独立未解问题。
