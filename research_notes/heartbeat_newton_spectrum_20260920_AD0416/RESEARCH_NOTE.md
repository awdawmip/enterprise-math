# 心跳世界：一般整数轴混合的 Newton 进位谱与精确重复节律

Status: `SCOPED_DERIVATION / LOCALLY_EXECUTED / RESEARCH_CANDIDATE / NOT_FOUNDATION`
Date: 2026-09-20
Researcher: EM-DIRECT-AD0416
Activity: RA-37C0A30C7B1F5A338F03D186
Source snapshot: awdawmip/enterprise-math@b466463d63b0926bada2c023279708661d8d153f

<a id="section-1"></a>

## 1. 问题、边界与符号

沿用 HEARTBEAT_WORLD：原生六轴整数位移和单独类型的时间。下面的矩阵是指定动力学的宏观整数作用，不把多轴混合当成一个原始步，不改变原生 PERP_E/120 度、地址编码或 P000。没有把倍率、周期、强制随机化写成世界公理。

前一轮已证明周期 monomial（轴置换加倍率）模型的循环均值判据。本轮允许一个坐标同时参与多个输出分量。固定非奇异整数矩阵 M（原生主应用 d=6；代码支持 1..6 的子问题）。周期程序 A_0,...,A_(ell-1) 取一周期乘积 M。n 表示已重复周期数，不能混同单拍时间；仿射平移不改变下述线性余数群。

写 SNF(M^n)=diag(s_1(n),...,s_d(n)), s_i|s_(i+1)，对固定素数 p 定义 a_i(n)=v_p(s_i(n))。它们是余数群的**不变量通道**，通常不是原生 E_1,...,E_6 轴本身。Smith 整数换基并不自动是原生空间旋转。

取特征多项式 f(X)=X^d+c_1 X^(d-1)+...+c_d。使用降幂系数下标，Newton 多边形是 (0,0),(j,v_p(c_j)) 的下凸包，略去零系数；其斜率 lambda_1<=...<=lambda_d 是特征根的 p-adic 估值，按水平长度重复。Newton 多边形定理是明确使用的经典结果，见 Elsheikh–Giesbrecht [R1], §2 Fact 1，不声称首创。

<a id="section-2"></a>

## 2. 一般线性进位斜率律（HBW-NS-001）

对每个固定 M,p，存在与 n 无关的有限常数 C，使得

    |a_i(n)-n lambda_i| <= C,    i=1,...,d, n>=0.

于是

    a_d(n)-a_1(n) = n(lambda_d-lambda_1)+O_(M,p)(1).

这里 O(1) 是一个固定常数界，不是“误差小于一个 digit”。不要求 M 可对角化。

### 证明

在一个有限 p-adic 扩张 K 中把 M 化为 Jordan 形；估值按 v(p)=1 归一。每个非零特征根 eta 的 Jordan 块 J=eta I+N，经固定对角共轭可化为 eta(I+N_0)，其中 N_0 的超对角元素为 1。故存在固定 S，使

    M^n = S D_n U_n S^-1,

其中 D_n 是 eta_i^n 的对角矩阵，U_n 是块上三角幺幂矩阵。其元素是整数二项式系数；U_n 和 U_n^-1 的元素都属于 O_K，所以 U_n 属于 GL_d(O_K)。因此 D_n U_n 的局部 Smith 估值恰是排序后的 n lambda_i。

令 nu_k(T) 为所有 k 阶子式估值的最小值，它是 wedge^k(T) 的矩阵最小估值，并等于前 k 个局部 Smith 深度之和。固定左/右乘 S,S^-1 只能把 nu_k 改变一个与 n 无关的常数：由矩阵估值的超可加性，常数可取

    K_k = -nu_k(S)-nu_k(S^-1) >= 0.

故 |sum_(i<=k)a_i(n)-n sum_(i<=k)lambda_i|<=K_k。相邻两个部分和相减给出每个 a_i 的固定误差界。有限扩张只把估值单位统一缩放，结论返回 Q_p。证毕。

### 对前一轮的严格推广

monomial 的一个置换循环 C 的特征多项式是 X^|C| - product_(j in C)w_j。全部根估值为 sum_C v_p(w_j)/|C|。因而本定理严格恢复前一轮循环均值结果，不是另造不相容的规则。

不同心跳切相位的 M_t 在 Q 上相似，所以多项式和全部 lambda_i 不变；有限步余数群、余数方向和有界修正仍可不同。定理只覆盖固定周期。任意切换、非线性和状态依赖矩阵乘积不在范围内。

<a id="section-3"></a>

## 3. 有界性的有限判据和可执行全时界（HBW-NS-002）

令 s=v_p(det M)=v_p(c_d)。以下三条等价：

1. sup_n(a_d(n)-a_1(n))<infinity；
2. lambda_1=...=lambda_d=s/d；
3. 对 j=1,...,d 有 d v_p(c_j)>=j s，零系数的估值视为 infinity。

第一与第二由 §2；第二与第三由 Newton 下凸包为连接 (0,0),(d,s) 的一个直线段。整数实现用交叉乘法，不使用浮点阈值；失败时给出具体系数下标和违反的不等式。

### 全时界的有限构造

令 B=M^d/p^s。单斜率保证 B、B^-1 的特征多项式系数均 p-integral，常数项均为 p-adic unit。令 nu(T) 为元素最小估值，设置

    K_plus=max(0, -min_(0<=j<d)nu(B^j)),
    K_minus=max(0, -min_(0<=j<d)nu(B^-j)).

Cayley–Hamilton 递推的系数均 p-integral，所以对所有 q>=0，nu(B^q)>=-K_plus，nu(B^-q)>=-K_minus。此处是有限检验推出无限时间界，不能替换成只看有限模拟。

写 n=dq+r，0<=r<d。由 M^n=p^(qs) B^q M^r 以及逆矩阵得到

    qs-K_plus+nu(M^r) <= a_i(n) <= qs+K_minus-nu(M^-r).

代码将这些界存成相对 n*s/d 的 d 组上下偏差。证书可重新计算核对输入摘要和所有系数；不是服务器签名。所得常数是充分界，不承诺最优，也不承诺在改变 M 的无限族中一致有界。

<a id="section-4"></a>

## 4. 比有界更强：进位谱具有精确的有限重复节律（HBW-NS-003）

单斜率时写共同斜率 alpha=a/b 为最简非负分数。令 C=M^b/p^a。存在某个 T>=1，使

    C^T in GL_d(Z_p).

因 C 的分母只可能含 p，这等价于找到整数矩阵 U，满足

    M^(bT)=p^(aT) U,  p does not divide det U.

令 H=bT, K=aT，则对所有 n>=0，恰有

    a_i(n+H)=a_i(n)+K.

证明是 M^(n+H)=p^K M^n U，而右乘局部幺模 U 不改变 p-local Smith 深度。此结论保持全体局部 Smith 因子，但不保持空间作用；U 通常不等于 I。

### 存在性证明（不依靠周期搜索成功）

对 C 和 C^-1 使用 §3 的 Cayley–Hamilton 方法，获得 nu(C^q)>=-K_plus 和 nu(C^-q)>=-K_minus，所有 q>=0。矩阵 p^K_plus C^q 均为 p-integral。把它们约化模 p^(K_plus+K_minus+1)，至多有 p^[d^2(K_plus+K_minus+1)] 个值。有限抽屉原理给出 0<=m<n 和差值 T=n-m，使 nu(C^n-C^m)>=K_minus+1。右乘 C^-m 得 nu(C^T-I)>=1。因此 C^T in I+p M_d(Z_p) subset GL_d(Z_p)。这是存在性与一个通常非常粗的有限上界。

实现只搜索有限 max_trials；返回 None 的含义是该预算未找到证书，不是否定周期存在。找到的 H 不保证最小。特别是不能因为宇宙被叫作心跳世界，就把任何模拟中的近似回返说成精确周期。

### 八拍剪切例子

取 M=8 I_6+E_12，E_12 的 (1,2) 项为1，其余为0。则

    M^n=8^n I_6+n 8^(n-1) E_12,  n>=1.

令 t_n=max(0,3-v_2(n))。其六个二进制余数深度为

    (3n-t_n,3n,3n,3n,3n,3n+t_n).

且 M^8=2^24(I+E_12)，所以 H=8、K=24 是精确证书。残余偏差按模8重复，空间依然继续剪切；不是事件返回，更不是时间倒流。

<a id="section-5"></a>

## 5. 总倍率相同却分别平衡和漂移

B=[[0,-2],[1,2]], D=[[0,-2],[1,1]]；定义六轴 M_bal=B direct-sum B direct-sum B，M_drift=D direct-sum D direct-sum D。两者每周期 det=8，每个2x2块也都真正混合两个坐标。

B 的多项式 X^2-2X+2 有两条相同的2-adic斜率1/2；D 的 X^2-X+2 则有斜率0、1。直接计算并证明：

    depths(M_bal^n)=(floor(n/2),floor(n/2),floor(n/2),ceil(n/2),ceil(n/2),ceil(n/2)),
    depths(M_drift^n)=(0,0,0,n,n,n).

平衡式可由 B^2=2U, U in GL_2(Z) 得到；漂移式由 D mod2 是非零幂等矩阵（故 D^n 有奇元素）以及 det(D^n)=2^n 得到。

以同一个整数幺模矩阵作代数共轭，构造两个跨六轴稠密混合的实际映射，有限 Smith 因子不变。这一构造用来生成对照映射，不把任意幺模换基解释为原生几何旋转。

注意：同样总余数数量 8^n，甚至每个复特征根通常长度同为sqrt(2)，也不决定整数进位平衡。两种观察不可混同。

<a id="section-6"></a>

## 6. BRC 的余数容量曲线（HBW-NS-004）

对 G_n=coker(M^n)，精确的 p^m 消去子群大小满足

    |G_n[p^m]|=p^[sum_i min(m,a_i(n))].

这是复用原工具 torsion_killed_count 的群结构公式，不是枚举全部余数。固定非负有理数 tau，令 m=floor(tau n)，由 §2 得

    (1/n) log_p |G_n[p^floor(tau n)]| -> sum_i min(tau,lambda_i).

对固定 M,p 还有总指数误差 O(1)。这给出一条分段线性的容量曲线，拐点正是 Newton 斜率。log_p 是解析读数；执行器直接计算整数指数和有理斜率，不使用浮点对数。

例：n=20、m=10，上述两模型总余数数都为 2^60；被2^10消去的余数数分别为 2^60、2^30。若额外声明每个余数等权1/2^60，用现有 BRC WeightHistogram 得筛选后质量为1、1/2^30。均匀权重是对照实验设定，不是几何自动给出的概率。

只知道 Newton 谱通常只能恢复长期容量增长，不能恢复有限群或精确权重。精确节律证书加上一个周期内的 Smith 表，才能在该限定观察下精确外推所有 n；即便这样仍不能恢复标记路径、余数嵌入方向或任意未来加法/局部作用。

<a id="section-7"></a>

## 7. 必须保留的观察边界

令 S=2I_6，T=2(I_6+E_12)。两者在所有 n 有完全相同的特征多项式谱和 Smith 因子 (2^n,...,2^n)。但是作用在 e_2 上：

    S^n e_2=2^n e_2,
    T^n e_2=2^n(n e_1+e_2).

对应原生分量长度平方分别为 4^n 和 4^n(n^2+1)。进位深度均衡不能推出原生长度、形状或空间输运均衡。

使用原版 Affine/EffectHistogram 计算，两者忘掉作用后的权重直方图相同，实际端点支持不同。因而 NEWTON_SPECTRUM / SMITH_PROFILE 都不等于 BRC 完整作用或路径状态。

<a id="section-8"></a>

## 8. 对前序文字的小修正

前序加权循环的原 radix 特例应为倍率向量 (1,1,1,1,1,b)（允许循环移位）。若六项都等于 b，映射是 b 乘六轴置换，k 拍的六个 Smith 因子都是 b^k，并不等于前序只在一个轴位乘 b 的 staircase。前序程序公式本身正确；本条修正的是把两个特例混写的说明句。

<a id="section-9"></a>

## 9. 实际验证与复用

12组本地检查全过，无跳过。36个稠密六阶整数矩阵的特征多项式、行列式、Smith 因子与独立 SymPy 1.14.0 精确算法对照；120组旧 monomial 判据恢复；18个稠密 Eisenstein 共轭模型的全时界证书和342个有限幂核验；96个一般矩阵/素数系数判据；18组三相位真正混合程序、54个素数相位比较；八拍例子33次精确递推核验；另6个模型78次节律核验；BRC群消去计数和空间反例均实际执行。

本轮初次测试的一个夹具直接把整数 tuple 传给旧 Fraction 矩阵逆辅助函数，违反其预期输入类型并引发浮点截断；已改成显式 qmatrix 接口，并断言 U U^-1=I 后重跑全套。不修改或冒称执行了未读取的全仓库模块。

原版执行、Git blob核验：heartbeat_residual_holonomy、brc_transport、brc_histogram。后者依赖的 rational_prime_valuations 使用先前 bundle 中明确注明来源的最小函数节选；不声称执行完整 brc_rational_holonomy 模块。

这不是独立数学审稿、Lean 或全仓库/生产 Nollm 测试。一般斜率定理来自 §2 证明，有限实验只负责核验。Newton/Smith 理论是已有经典数学，本轮没有全球优先权主张。

<a id="section-10"></a>

## 10. 下一步的数学界限

本轮把固定周期的一般非奇异整数线性心跳的局部进位平衡判据闭合，并给出更强的精确重复节律。下一真正界限是状态依赖或非周期切换：每个单独矩阵平衡不保证任意时间混合乘积也平衡；必须对允许的时间语言建立共同的整数格/估值界，而不能把逐个矩阵的证书直接拼接。

[R1] Mustafa Elsheikh and Mark Giesbrecht, Relating p-adic eigenvalues and the local Smith normal form, Linear Algebra and its Applications 481 (2015), 330–349, arXiv:1401.1773v4. Read the introductory counterexample and §2 Fact 1. It does not assert universal one-step equality of Smith valuations and root valuations.
