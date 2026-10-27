# PREFIX-281｜全历史同谱BRC的平移协变操作不辨识定理

**状态：AUTHOR_SIDE_EXACT_PROOF / EXACT_TYPED_C4_BRC_CHECK_PASS / NATIVE_OP_LEGALITY_UNVERIFIED / NOT_ADMITTED。**

## 固定输入与权限边界

Global Knowledge: `awdawmip/chatgpt-global-knowledge@521f002032bb9026ea154727911276cbea709bdb`，读取了 `00_BOOTSTRAP.md`、`OPERATING_MANUAL.md`、P000 STARTUP及原件Blob (`770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc` 一致)、ACTIVE「我眼中的世界」、数学/BRC规范。Enterprise Math科学与规范：`awdawmip/enterprise-math@2bd0f301579f5dc5e4a70636302cff9609665cbd`；`docs/PORTABLE_RESEARCH_PROTOCOL.md` Git Blob `ca5de2d680d2439ff4b67c2c55fbd4159813cd5c`；`docs/HEARTBEAT_BRC_ONLY_ARITHMETIC.md` Blob `787e74952765b61904f2bd67038291f5f081af83`。复用 PREFIX-278 原始Stage50 ten-external-port恒等式、PREFIX-279同谱源包和PREFIX-280边界掩码反例。

本文件中的有限来源坐标是 **X6心跳世界的带来源载体索引**，不是额外空间轴，也不是完整六维Cell地址；来源差 `r` 不是独立物理时间。P000固定六维离散Cell空间和分别定型的时间。下面定义的源滤波门是**条件性形式操作**，不得冒充经过验证的 `H_n→H_(n+1)` 规律。

## 研究问题与观察语义

设一个有限、带来源标签的C4-BRC包包含正有理质量幅值 `w>0`、相位 `q∈Z/4`、路径来源 `j` 和支路ID。允许同一来源 `j` 上保留多个支路，强度来自其所有**有序路径对**；不得先用正质量求和代替相位联合项。以形式记账符号 `a_j=Σ_{b∈B_j}w_b i^{q_b}`，定义
[
C_r(a)=sum_j a_joverline{a_{j+r}},quad C_{-r}=overline{C_r},quad Z=C_0>0.
]
这只是C4路径对BRC的简洁代数记法，不是普通复数物理传播器。PREFIX-278原始Stage50的声明读数为：
[
E_a(r,p)=rac5{18}left(1-operatorname{Re}(i^p C_r(a)/Z)ight),quad p=0,1,2,3.
]
全部 `r,p` 读数至多区分归一化全自相关；绝对质量 `Z` 如另有读出可一并保留。

**假设性共同源滤波**：固定一个有限的带C4相位正权路径系数族 `h_k`。每条 `(j,b)` 路径按 `k` 分支到 `j+k`，新支路载荷为 `h_k a_{j,b}`，新ID保留原来源与滤波分支 `(j,b,k)`。跨源的输出同标签支路依然以完整有序路径对做BRC观察。这一操作是明确定义的形式载体映射，**未经原始Stage50/完整心跳Source验证为合法门**。在复合信号记法中为 `b=h*a`。

## 定理1：共同平移协变分支滤波维持完整同谱

对于任意有限C4路径包 `a,g`，如果
[
C_r(a)=C_r(g)quad	ext{对所有整数 }r,
]
则对任意同一个非零有限源滤波 `h`，
[
oxed{C_r(h*a)=C_r(h*g)quadorall rinmathbb Z.}
]
两组后态有相同非零总正质量 `Z'` 时，其全部Stage50型 `E(r,p)` 也相等。

**BRC有序路径对证明：**不合并来源或删去支路，对输出索引 `j` 与 `j+r` 的每一对滤波分支 `k,ell` 直接展开：
[
egin{aligned}
C_r(h*a)
 &=sum_{j,k,ell} h_koverline{h_ell}
          a_{j-k}overline{a_{j+r-ell}}\\
 &=sum_{k,ell}h_koverline{h_ell},
          C_{r+k-ell}(a).
end{aligned}
]
有限支路使重排严格合法；在第二行保留了所有共同来源、过滤支路及C4交叉关系。由于全体 `C_t(a)=C_t(g)`，右侧逐项相等；`r=0` 给出相同的输出BRC正质量；代入十外Port观察恒等式即可。证毕。

等价的有限Laurent多项式证书是 `A(z)A^#(z)=G(z)G^#(z)`，相同滤波 `H(z)` 后两边同乘 `H(z)H^#(z)`；其中 `#` 仅编码C4共轭和来源索引反向，不宣称存在普通矩阵传播器。

## 定理2：任意有限步、基于既有BRC读数的自适应滤波仍无法区分

允许每一步根据已经观察到的源自相关、总质量和 `E(r,p)` 选择同一条合法候选 `h`（选择规则仅依赖这些观察），之后执行上面的共同滤波、全局C4相位和共同来源整体平移。则从两组初始全历史同谱包出发，任意**有限**次这样的操作与读出都完全一致。

证明按操作轮数归纳。共同源滤波由定理1保持同谱，整体平移及全局C4相位直接保持 `C_r` 和 `Z`，同谱保证下一步相同的观察策略选择；归纳成立。**这一结论是声明操作代数上的严格无辨识定理，不代表真实原生模型只允许这些门。**

## 明确反例与操作边界

复用PREFIX-279正整数包 `f=(1,4,4)`, `g=(2,5,2)`。两者
[
C_0=33,quad C_1=20,quad C_2=4,quad C_{|r|\ge3}=0.
]
共同正滤波 `h=(1,1)` 后，
[
h*f=(1,5,8,4),quad h*g=(2,7,7,2),
]
两者全部自相关同为
[
oxed{(C_0,C_1,C_2,C_3)=(106,77,28,4)}.
]
这属于原始Stage50的单C4角色/来源包可表示的正包**输入级**特例；**没有在本轮重新执行原始Python内核**。

与上述平移协变共同滤波严格不同，PREFIX-280声明的标签选择相位掩码 `U_0(a_0,a_1,ldots)=(-a_0,a_1,ldots)` 不与来源平移协变。前态全同谱的 `f,g` 经各自同一 `U_0` 后，
[
oxed{E_{U_0f}(1,0)=35/198
eq 5/18=E_{U_0g}(1,0)}.
]
故 `U_0` 若是**额外合法操作**，能区分；但上述定理不保证 `U_0` 已由任何真实 `model_law_id` 支持。输出并未证明“所有平移协变操作”均不辨识：证明只覆盖**在载体上可表示为共同有限C4源卷积/平移/全局相位及自适应组合**的明确操作族。尤其不包括来源依赖门、测量反馈形成的非共同滤波、非线性场作用或真实边界变化。

## 本轮新执行的精确BRC证据

`verify_prefix281.js` 在逐来源、逐滤波分支ID的C4有序路径对计算上使用BigInt整值，支持负的干涉交叉项、无浮点和三角函数、无矩阵指数；每个十外Port读数直接从两路源态的有序支路路径对累加，不用简单调用自相关结论替代独立读数。

遍历每条滤波长度 `L=1,2,3`，每个系数幅值取 `{1,2}`、相位取 `{0,1,2,3}`，共 `8+64+512=584` 个非零滤波器。对每个滤波后态的全部 `C_r` 比较 **2,840** 项；对全部正来源差与四种C4探针进行 **9,024** 对 `E(r,p)` 比较，实际逐态计算 **18,048** 个完整来源支路对Port读数；额外执行 **64** 次两轮自适应的精确读数对照。全部通过。特例 `h=(1,1)` 与 `U_0` 差别均按上式通过。完整输出为 `RESULTS_PREFIX281.json`。

有限枚举**不是**无限定理的证明；一般结论依上面的有序路径对有限重排。当前执行的是具有明确C4-BRC类型语义的独立验证器，未调用原始Stage50 Python Source，也未证明源滤波与掩码在心跳世界可实现。原始Stage50存于前序PREFIX-278通过哈希核验的历史bundle；当前GitHub固定Source上无法直接通过此前归档提交 `318f47839d6bc7c850a3b7cc0fcb22d48febd9ba` 打开源码，该Git ref不属于当前仓库可取引用，不把源码不可读误判为该操作非法。

## 本轮结论、真正的阻断与可续接前沿

- **已证明：**共同有限C4来源卷积（及明确组合）的全历史同谱不可辨识，包含自适应读取条件；严格正整数两包给出所有未来滤波序列仍不辨识的现成证书。
- **科学空缺：**需要一项可检验的、确实存在于原生Source中的来源依赖干预/门，或完整原生 `model_law_id`；不能凭 `Stage50.local` 接收预设不同的输入包推断物理 `H_n→H_{n+1}`。
- **正式状态：**GitHub作者侧的独立数学推导，不是原生CLAIM、Result、Driver审查或真实物理规律。原生 `em_session_start` 返回 `STATIC_READONLY_SCOPE_DENIED/operation_sent=false`；`em_control_tasks` 返回 `CONTROL_QUOTA`，故活跃Owner未核实。无需改变P000或ACTIVE世界观。

**下一问题 PREFIX-282：**取得经过哈希核验的原始Stage50 `local`、Stage46 Port/C4载体及完整心跳 `model_law_id` 合法门清单：第一步精确审查“来源选择门 `U_0`”是否在原生更新而非输入重新准备中定义；若无，则列出实际可用的全部作用是否落在本轮已证明同谱封闭的滤波/相位/平移族；对每个不在此代数中的真实操作给出首个分辨反例与原生Cell/Port/场/物质动量/来源边界/独立时间的类型化证书。

Researcher-ID: EM-R006-P281 / TASK_RESEARCH (author-side; native identity unavailable).
