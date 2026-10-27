# PREFIX-285｜C4-BRC共同卷积下的端点观察不辨识与内源强度修复

**状态**：AUTHOR_SIDE_EXACT_PROOF / 840_EXACT_PAIR_FILTER_CHECKS_PASS / SOURCE_CODE_REEXECUTED / NATIVE_DETECTOR_PENDING / NOT_ADMITTED。

## 固定来源与前沿（2026-10-27）

- GLOBAL_KNOWLEDGE_V1：`awdawmip/chatgpt-global-knowledge@6541aad83baa2b852d25138186c0110b298fddb3`，规范入口 `00_BOOTSTRAP.md`、`OPERATING_MANUAL.md`，同一快照的P000启动投影、原件（Blob均为 `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`）、ACTIVE世界观、数学/代码/EM/BRC方法规则。
- 本轮科学输入冻结在 `awdawmip/enterprise-math@b6f54b13ffdef14ba053fff06e1345c9606726fb`；依据 `docs/PORTABLE_RESEARCH_PROTOCOL.md`、`docs/HEARTBEAT_BRC_ONLY_ARITHMETIC.md`、`research_constraints/heartbeat_brc_only.json`、`definitions/HEARTBEAT_SELF_CONSISTENT_INSTANT_V0_1.json` 及前序 PREFIX-284 精确Z₂分类。
- GitHub当前认证用户实际读取为 `awdawmip`，仓库具有push/admin权限；原生会话登记调用实际返回 `STATIC_READONLY_SCOPE_DENIED`，`operation_sent=false`；原生活跃Task查询返回 `CONTROL_QUOTA`。因而只执行独立**作者侧模型内研究**，无原生CLAIM、Result或Driver接纳。来源身份标记 `EM-R006-P285` 是本轮自行分配的研究标签，不是服务端授予的原生身份；作者侧活动 `RA-R6P285-20261027-0953` 独立登记。
- 本文的来源索引j是**输入历史/Path-ID**；不是X6的六个原生空间轴；卷积次数不是心跳序数n。本轮不涉及物理动力学的 `model_law_id` 确认，也不改变P000。

## 精确问题

PREFIX-284已知三来源复相位幅值的全部归一化自相关和一个端点质量观测，在等端点奇异层最多留下两个规范化伙伴 `r ↔ t·conj(r)`。问：**在不添加来源局部相位门的情况下，允许公共平移协变的C4卷积分支操作后，反复观察自相关和两端来源质量能否破除伙伴？若增加一个内部来源的对角BRC质量读数，最少需要哪些固定探针？**

## 来源载体与BRC运算

令非零有限包 `a=(a_0,…,a_m)`，以首末非零占据确定端点。定义原始有序路径对相关与质量：

[
C_r(a)=sum_{j}a_joverline{a_{j+r}},qquad Z_a=C_0(a)>0,qquad c_r(a)=C_r(a)/Z_a,
]
[
p_L(a)=|a_ell|^2/Z_a,qquad p_R(a)=|a_u|^2/Z_a,
]

其中 (ell,u) 是首末非零来源索引。所有求和只在真实存在的路径/来源上进行。

公共有限滤波器 `h=(h_0,…,h_d)≠0` 产生带双标签分支 ((	ext{input-source }j,	ext{tap }k))，携带复幅值 (a_jh_k)，输出来源标签 (j+k)。同一输出来源的**全部有序分支对**定义对角BRC质量：

[
Q_s(h*a)=rac1{Z_{h*a}}
 sum_{j+k=s}sum_{j'+k'=s}
 (a_jh_k)overline{(a_{j'}h_{k'})}.
]

上式的整数/高斯整数展开是本轮实际运行的类型化BRC操作；不是普通传播矩阵、(pi)、三角函数或数值近似。

## 定理A：共同卷积＋两端质量的完整不辨识闭包

设两个非零有限包 (a,b) 满足全部规范化自相关相等 (c_r(a)=c_r(b))，并且首、末端质量占比各自相等：

[
p_L(a)=p_L(b),qquad p_R(a)=p_R(b).
]

对任意相同的非零有限公共卷积滤波 (h)，仍有：

[
oxed{c_r(h*a)=c_r(h*b) orall r,quad
p_L(h*a)=p_L(h*b),quad p_R(h*a)=p_R(h*b).}
]

也适用于重复卷积，以及根据此前这些观察自适应选择下一共同滤波器的任意有限轮协议；即该观测代数内两者未来不可辨识。**此结论仅限所声明的共同卷积、整体相位/平移和端点/自相关观察。**

**证明**：保留原始来源与滤波支路标签，将 (C_r(h*a)) 按全部四元索引 ((j,k,j',k')) 展开，在差值 (r=(j'+k')-(j+k)) 下重排，等价于形式Laurent路径对恒等式

[
R_{h*a}(z)=R_h(z)R_a(z),quad
R_a(z)=sum_{r}C_r(a)z^r
]

（Laurent指数约定左右可统一改号，不影响乘法）。由于 (R_a=Z_asum_r c_rz^r)、(R_b=Z_bsum_r c_rz^r)，二者卷积后的相关多项式仍按比例 (Z_a:Z_b) 相等，归一化后相等。若首末非零输入索引为 (ell,u)，滤波首末非零tap为 (s,t)，输出极端来源 (ell+s) 与 (u+t) 各仅存在**一条**非零路径对贡献，幅值分别为 (a_ell h_s)、(a_u h_t)。所以两端质量比仅由原两端质量比和共同范数倍率

[
K_h=rac{Z_{h*a}}{Z_a}=rac{Z_{h*b}}{Z_b}>0
]

决定，进而相等。若下一滤波由此前读数确定，同读数导致同滤波，归纳即得自适应结论。证毕。

**注意**：上式约束的是观测代数；未来若允许读取全部内部来源直方图，闭包结论不再适用。

## 定理B：至多两个固定C4滤波器＋一项内部对角质量必能辨识三来源Z₂伙伴

对PREFIX-284等端点奇异层，取 (a_0
e0)，设置 (r=a_1/a_0)、(t=a_2/a_0)、(|t|=1)。不同但已有观测不可辨的规范化伙伴是：

[
r^sharp=toverline r
e r,qquad |r^sharp|=|r|.
]

取**同一公共二tap滤波** (h_u=(1,u))，仅 (uin{1,i})。对滤波后内部输出来源 (s=1) 做上述BRC对角质量读出，则：

[
oxed{D_u(r)=rac{p_0|r+u|^2}{K_u}},quad
K_u=rac{Z_{h_u*a}}{Z_a}=2+2operatorname{Re}(u c_1)>0.
]

对两个规范化伙伴，(c_1,p_0,K_u,|r|) 相同，所以

[
oxed{D_u(r)-D_u(r^sharp)=
 rac{2p_0}{K_u}operatorname{Re}((r-r^sharp)overline u).}
]

当 (u=1) 时测得复差的实部；当 (u=i) 时测得虚部。由于 (r-r^sharp
e0)，**两种固定滤波中至少一个必然区分伙伴**。无需假设来源局部相位翻转，所需新增观察种类只是滤波后的**内部单来源对角质量**。这一新增读数的合法性仍须依据原生Source确认。

**证明**：内部来源1恰有两条有标签路径：((1,0)) 携幅值 (a_1)，((0,1)) 携幅值 (ua_0)。全有序BRC路径对求和等于 (|a_1+ua_0|^2)。总质量把所有输出来源和路径对求和，展开恰得 (2Z_a+2operatorname{Re}(uC_1(a)))，所以归一化倍率 (K_u) 如上且正。两伙伴的平方模差仅余交叉项，立即得到盒中公式。一个非零复数不能同时实部与虚部都为零。证毕。

## 精确C4反例：端点始终失辨，内部质量立即区分

设 (f=(1,i,1))、(g=(1,-i,1))。它们完全相同的初始观察为：

[
Z=3,quad c_1=0,quad c_2=1/3,quad p_L=p_R=1/3.
]

共同滤波 (h=(1,i))，保留每一条输入来源/tap支路后分别得到：

[
h*f=(1,2i,0,i),qquad h*g=(1,0,2,i).
]

两者的完整原始相关序列均为：

[
oxed{(C_0,C_1,C_2,C_3)=(6,-2i,2,-i)}.
]

并且两端归一化质量均为 (1/6)，但内部来源1有：

[
oxed{D_i(f)=4/6=2/3,qquad D_i(g)=0,qquadDelta=2/3}.
]

全部读数从带有输入来源与滤波tap标签的高斯整数BRC有序路径对取得，未使用浮点数。

## 实际执行与覆盖

在固定代码 `verify_prefix285.js`（此研究目录）运行 `verifyPrefix285()`：

- 枚举全部432个三来源包：首项正整数1..3，后两项正幅值1..3且各C4相位；压缩为358种 ((c_1,c_2,p_0)) 签名；
- 发现42种恰有两个不同规范化来源结构的签名（与PREFIX-284一致）；每一对检查20个非零C4共同滤波器（4个二tap、16个三tap），合计**840个伙伴—滤波对照**，全部保持完整自相关和两端概率；
- 同42对分别实施候选 (h_1=(1,1))、(h_i=(1,i))，完成**84个内部来源读出对照**；每一对至少一个滤波器将其严格分辨；
- 每个输出来源的BRC路径对质量与按来源重新合并幅值的平方模逐一精确相等；示例原始整数质量 ((1,4,0,1)) 与 ((1,0,4,1)) 得到精确差 (2/3)。

通用定理依靠解析证明；有限检查仅覆盖上述声明的432包和20种滤波器。核心源码执行后返回 `PASS`，完整机器输出见 `RESULTS_PREFIX285.json`。运行环境为 JavaScript BigInt 高斯整数的显式分支BRC语义，未重新执行原始Stage50 Python包。

## Source对应和下一证据门

PREFIX-282定位的软件 `packet_variance` 可读输入路径的来源质量，但这一能力仍需与**一个已准备完成的完整H_n之后**的Detector测量区分。本轮共同卷积 (h_u) 与内部来源读出 (Q_1) 是清晰声明的形式操作与观察，不是从Stage50或六维Cell动力学自动取得的真实合法仪器。

下一单元PREFIX-286应在原始Stage50/当前心跳Source中找可追溯的 `model_law_id`，确定一次H_n准备后的公共滤波是否为真实操作，随后确定内部来源单点读出的Port效应、归一化与测量后态。若Source仅允许Toeplitz外端口和端点读数，则定理A给出了可保持的Z₂不可辨识证书；若找到合法内部来源Detector，便用**同一个已准备后态**实际运行两种滤波后的观测，测量与准备保持类型分离。证据范围需逐项注明Cell六轴、三维切片位置与第三分量、材料动量、场、来源、边界及独立时间。

**本轮结论层级**：声明的BRC模型内精确证明与BigInt有限重算通过；原生Detector/物理心跳映射与正式Result/Driver审查待核。
