# PREFIX-434 — 五 Port 相干来源的精确观察纤维反例与支路修复定理

2026-11-02。研究线：进取数论研究6。分类：COUNTEREXAMPLE + PROVED（**外部五 Port 静态复来源辅助模型内**）。验证：作者侧精确有理数检查和独立符号代数交叉检查；无独立数学审阅。控制状态：PORTABLE_DIRECT / UNREVIEWED / NOT_ADMITTED / NATIVE_CLAIM_ABSENT。

## 来源与研究选择

沿用冻结科学输入 enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d 及 PREFIX-428（f05ab053db5448618c0e201e9e483f63398238fc）给出的原始五 Port 复来源。上一有效前沿 PREFIX-433（c1684669226d18dc255e93d592872a85fd65f67b）已经建立外部模型的相变曲率单调性。本轮选择更高信息增益的保真检验：保留两个基准强度、第二来源强度、第一联合强度及第五 Port 强度，是否足以读出原始第四 Port 的优化目标？

对 u,v∈C，定义 z1=u, z2=1+u, z3=v，
z4=(5+9i)/2+(3+7i)u/2+4iv，
z5=(22+15i)(1+u)/8+(5+9i)v/4，
kappa(u,v)=abs(abs(z4)^2-41)。
参数 beta=1/1000000，rho=1/1000，0≤epsilon≤beta，eta=39/2000。合法约束：
abs(abs(u)^2-1)≤epsilon；
abs(abs(1+u)^2-2)≤epsilon；
abs(v)^2≤beta；
abs(abs(1+v)^2-1)≤eta；
abs(abs(z5)^2-709/32)≤eta。

## 定理 A：相同的五个保留强度无法决定原目标

取 x=1/2000，y=-123x/245=-123/490000，v=x+iy，u_+=+i，u_-=-i。令
Q(u,v)=(abs(u)^2,abs(1+u)^2,abs(v)^2,abs(1+v)^2,abs(z5)^2)。
则 Q(u_+,v)=Q(u_-,v)，且两来源对所有 epsilon∈[0,10^-6] 在 eta=39/2000 下均满足原始完整可行性约束。但
abs(z4(u_+,v))^2=277780670077/7503125000 < 41，
abs(z4(u_-,v))^2=337821105077/7503125000 > 41，
kappa(u_-,v)-kappa(u_+,v)=172762577/3751562500>0。
因此 kappa 在 Q 的同一观察纤维上不为常数，**不存在任何使 kappa=phi∘Q 的确定性精确读出 phi**。

证明：对任意实数 x,y，直接从 z4/z5 原式展开：
abs(z5(+i,x+iy))^2-abs(z5(-i,x+iy))^2=(123x+245y)/8；
abs(z4(+i,x+iy))^2-abs(z4(-i,x+iy))^2=-8+24x+56y；
abs(z4(+i,x+iy))^2+abs(z4(-i,x+iy))^2-82=72x-40y+32(x^2+y^2)。
取 y=-123x/245，第一式严格为零，第三式在 x=1/2000 严格为正，两 z4 强度分别位于 41 的两侧，目标差恰为第三式。另有精确可行性证据：
abs(v)^2=37577/120050000000 < beta；
abs(1+v)^2=120170087577/120050000000；
abs(z5)^2=21288070856581/960400000000；
abs(abs(z5)^2-709/32)=9208356581/960400000000 < eta；
abs(abs(1+v)^2-1)<eta；
abs(u)^2=1，abs(1+u)^2=2。
所有严格大小关系由 Fraction 精确断言验证。

## 定理 B：四个基准强度的完整来源纤维与最少符号信息

对 R=abs(u)^2、S=abs(1+u)^2、T=abs(v)^2、W=abs(1+v)^2，设
a=(S-R-1)/2，d=(W-T-1)/2，U=R-a^2，V=T-d^2。
当 U>0、V>0 时，该四元组在 C² 中的来源纤维**恰为四点**：
u=a+i sigma_u sqrt(U)，v=d+i sigma_v sqrt(V)，sigma_u,sigma_v∈{-1,+1}。
证明：由强度差等式恢复两实部，由模平方恢复两虚部绝对值；四个符号组合分别成立且相互不同。

因此额外保留两个相位支路符号位可以完全恢复 (u,v)。如果声明的未来观察族包含所有以固定参考振幅 1 为首项的复线性来源强度，那么不同 (u,v) 一定可被某个该族观察区分；同一强度四元组的四点至少需要四种不同编码标签，即在通常二进制编码下至少两个额外位。精确有限分离公式为：
Re(z)=(abs(1+z)^2-abs(1-z)^2)/4，
Im(z)=(abs(1-iz)^2-abs(1+iz)^2)/4，
分别用于 z=u,v。U=0 或 V=0 时对应支路退化，符号信息量相应降低。

这是对**声明的全部辅助线性强度观察族**的最小性结论；对仅有固定五个 Port 且带约束的个别纤维，不作“四点均合法”断言。定理 A 已在原约束内给出至少一位支路信息确有必要的直接证据。

## 定理 C：共同相位 Gram 载体与有限后续操作误差界

设 X=(1,u,v)^T，G=XX*，其中 * 为共轭转置。任意复线性行观察 c 的强度满足 I_c(X)=abs(cX)^2=cGc*。因此 G 是所有此类观察的精确充分载体。任意压缩 E 对**全部** c 的强度均可精确读出，当且仅当
E(X)=E(Y) => XX*=YY*。
必要性可由复极化等式或定理 B 的有限分离探针得到；充分性由 I_c=cGc* 给出。固定首分量 X0=1 时，G 精确恢复 (u,v)。对受限观察族更小的压缩仍可能足够，不声称 G 是所有范围的最小载体。

对已声明的辅助复线性更新 A=A_n...A_1，有 G_n=A G_0 A*。若近似矩阵的每个元素误差 abs(DeltaG_jk)≤d，则任何终端行 c 的强度误差满足
abs(c A DeltaG A* c*) ≤ d (sum_j abs((cA)_j))^2 ≤ d ||c||_1^2 product_k ||A_k||_infinity^2，
其中矩阵无穷范数为最大行绝对值和。证明是展开双重和后使用三角不等式及诱导范数次乘性。作用域为明确给出的有限辅助操作序列；不声称无限时间稳定性或原生物理误差定律。

## BRC / P000 桥接条件及其边界

P000 的原生空间固定为六个离散空间轴，时间是单独的类型；相位、分支与路径须保留，三维研究对象是原生六维内有明确嵌入的切片。这里的 C³ 和 Gram 不作为原生空间维数，也不把普通分数运算称为 typed BRC。

可检验的**条件充分性命题**：若存在满足 P000 来源、联合关系及路径语义的原生状态映射 psi:Omega→C³，且对声明的原生更新 U_k 和原生观察 O_c，分别有 psi(U_k omega)=A_k psi(omega)、O_c(omega)=abs(c psi(omega))²，则 G(omega)=psi(omega)psi(omega)* 在该观察/更新范围内严格保真，并满足定理 C 的误差界。目前没有给出或执行这样的原生 psi、A_k 和合法 typed BRC 内核，所以此处保持 **NATIVE_BRIDGE_PENDING**。本轮没有执行本项目心跳/BRC-Shor 的普通经典替代数值模拟，不作原生残差归因。

## 实际可复现证据与下一问题

同一 Git 树提供：
prefix434_exact_observer_witness.py（标准库 Fraction 的原始五 Port 精确实现和全部可行性断言）；
prefix434_independent_sympy.py（独立从原式符号展开三条差式）；
PREFIX434_EXACT_WITNESS.log；
PREFIX434_INDEPENDENT_SYMBOLIC.log。
前者返回 PASS_PREFIX434_EXACT_COMPLEX_RATIONAL_OBSERVER_WITNESS，后者返回 PASS_PREFIX434_INDEPENDENT_SYMBOLIC_ORIGINAL_PORT_EXPANSIONS。两套均为作者侧交叉验证而非独立审稿；定理 B/C 的普遍量词由上述解析代数证明支撑，没有 Lean 形式验证。

下一问题 PREFIX-435：读取指定版本的真实 typed BRC 载体和 Port 观察接口，检验是否存在作用在合法 X6 来源上的 psi 与最小支路修复符号，使五 Port 联合强度和声明的后续操作可以在**真正 BRC** 内精确读出；若当前类型缺字段，构造保留支路、来源、第三切片坐标与路径信息的最小候选接口并用定理 A 的同纤维异目标见证判定它。原生 CLAIM/Result/Review/Admission 依当前控制权限另行办理，不因 portable GitHub 提交自动形成。
