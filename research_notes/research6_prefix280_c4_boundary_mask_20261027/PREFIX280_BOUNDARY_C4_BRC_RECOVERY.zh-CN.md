# PREFIX-280：C4-BRC 全历史同谱商的单边界来源掩码恢复定理

**研究状态：AUTHOR_SIDE_EXACT_PROOF / INDEPENDENT_C4_BRC_CHECK_PASS / NATIVE_GATE_UNVERIFIED / NOT_ADMITTED。**

## 来源和固定快照

GLOBAL_KNOWLEDGE_V1 为 awdawmip/chatgpt-global-knowledge@6190a3375e2e7cf63d5f0c303f9b44956700f960；规范入口 00_BOOTSTRAP.md、OPERATING_MANUAL.md，项目 P000 投影/原件（原件 Git Blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc），ACTIVE 世界观、数学和 BRC 规则已核对。科学输入为 awdawmip/enterprise-math@d47fb23de6f060c1275c521b0052c1ec31c530f4；Portable Research 的 Blob ca5de2d680d2439ff4b67c2c55fbd4159813cd5；heartbeat_brc_only 约束的 Blob 62ffa6bbdafd54496e27284a26a2aeaf2d04df99。

复用 PREFIX-278 在原始 Stage50 上验证的十外端口恒等式和 PREFIX-279 已证明的同谱来源包。本次没有再次导入原始 Stage50 软件；新测试是独立的精确有序路径对 BRC checker。来源历史差 r 不是物理时间；来源标签个数不是 X6 空间轴个数。

## 模型与可读数

连续带标签来源 j=0,...,n-1，n>=3，a_j=w_j i^(q_j)，其中 w_j 为严格正有理数，q_j 属于 Z/4。定义 Z=Σ_j |a_j|²>0 和标准化完整有序来源配对

c_r = (1/Z) Σ_{j=0}^{n-1-r} a_j conjugate(a_{j+r}),  1<=r<n.

Stage50 原始十二 Port coin 的十外 Port C4-BRC 精确观察为：

E_a(r,p)=(5/18)[1-Re(i^p c_r)],   p=0,1,2,3.

这是完整来源载体上的精确 BRC 端口观察，不是自行引入的普通复振幅物理传播器。每一历史差 r 的两个标量读数已恢复完整复相关：

Re(c_r)=1-(18/5)E_a(r,0)， Im(c_r)=(18/5)E_a(r,1)-1。

仅形式上额外允许一个带标签来源边界相位掩码 U0：
U0(a0,a1,...,a[n-1])=(-a0,a1,...,a[n-1])。相位 i²=-1，正质量与其余来源未改变。这是**条件性的来源准备/干预**，还没有原生模型律证明其为合法完整 H_n→H_(n+1) 更新。

## 定理：只增加一种边界掩码，全部归一化来源包可重建

**定理 PREFIX-280（显式逆）**：对于上述 n>=3 且每个来源非零的 C4 包，当前全部 E_a(r,p) 和同一 U0 后的全部 E_(U0a)(r,p) 严格确定 a_j/a0 (j>0) 及 |a0|²/Z。等价地，确定 a/√Z，最多余一个共同 C4 相位；若另有 Z，则确定原始包的所有幅值，最多余共同 C4 相位。实际上每个 r 只需 p=0,1。

证明：记 c'_r 为掩码后的相关，u_r=(c_r-c'_r)/2。完整有序来源对中，r>0 时唯一涉及标签0的项为 a0 conjugate(a_r)，而该项在掩码后反号，故

u_r = a0 conjugate(a_r)/Z。

记 x_j=a_j/√Z，则 u_r=x0 conjugate(x_r)。当 n>=3 时，历史差 n-2 的有序配对恰好只有 j=0 与 j=1 两项。因此

D=c_(n-2)-u_(n-2)=x1 conjugate(x_(n-1)) != 0。

乘积 conjugate(u1)u_(n-1)=|x0|² x1 conjugate(x_(n-1))=|x0|² D，于是得到显式且在合法输入上严格正实的式子

s=|x0|²=conjugate(u1)u_(n-1)/D >0，

a_r/a0=conjugate(u_r)/s，  1<=r<n。

因此两组来源包具有相同前后全部 C4-BRC 读数，当且仅当它们的标准化相对来源幅值一致（整体 C4 相位、总标度在读数中不可见）。证毕。计算仅用带来源的有序 BRC 路径对、C4 与高斯有理数，不引入 π、三角函数、普通矩阵指数、Taylor 或高精度非 BRC 替代。

一种足够的实现每个 r 在原状态和 U0 状态各读取 p=0,1，总计 4(n-1) 个外端口标量读数。此为**充分上界，未证明标量查询次数最优**；“一次”指增加一种来源相位操作而非只读取一个标量。

## 边界反例与已验证前沿

n=2 时，两个带标签正包 (1,2) 与 (2,1) 的 Z=5,c1=2/5；施加相同 U0 后又同为 c1'=-2/5，全部前后 C4 观察仍相同，故 n>=3 的限制不可删除。n=3 且中间来源为空时，(1,0,2) 与 (2,0,1) 也不可区分；此时 D=0，证明不能套用。

PREFIX-279 全静态同谱包 f=(1,4,4)、g=(2,5,2) 有 Z=33，全部 c_r 一致；但本逆式分别给出 s_f=1/33，来源比 (1,4,4)；s_g=4/33，来源比 (1,5/2,1)。掩码后同一 BRC 外端口 E(1,0) 分别是 35/198 和 5/18，差 10/99。该区别仅属于声明的形式操作范围。

## 精确计算与可复现证据

脚本 verify_prefix280.py 使用 fractions.Fraction、完整标签、正质量、C4 幅值相位和十外端口全部**有序路径对**。对每个来源包逐 r、p=0,1 做前后两组读数，反演复相关，再验证 u、D、s 与所有来源幅值比；同时独立比较 BRC 直接配对与原始 Stage50 解析端口观察。

枚举：n=3 的每一正权重从 {1,2,3} 取、四种 C4 相位全枚举，共 1,728 包，13,824 读数；n=4 权重从 {1,2} 取、相位全枚举，共 4,096 包，49,152 读数；n=5 各权重固定1、相位全枚举，共 1,024 包，16,384 读数。合计**6,848 个无零来源包与 79,360 次精确 BRC 外端口读数**，每项反演 PASS；f/g 和两组边界反例 PASS。运行回执 PREFIX280_INDEPENDENT_C4_BRC_BOUNDARY_MASK_PASS 6848 79360。

一般定理取决于上述解析恒等式，不取决于有限样本推断。脚本执行的是带来源路径对的**独立精确 BRC 语义检查器**；本轮未运行原始 Stage50 模块，更未做真实六维 Cell/材料/动量/完整场/边界、检测器与独立时间的物理执行。工具复用状态 REUSE_APPLIED：Stage50 C4-BRC 十外 Port 法则与 PREFIX-279 现有路径对实现；未自称发明新的通用 BRC 工具家族。

## 权限、保存和下一问题

GitHub 身份 awdawmip，enterprise-math push/admin 权限。作者侧研究活动 RA-R6P280-20261027-0452 独立登记并回读；它**不是**正式任务 CLAIM。原生 em_control_tasks 返回 CONTROL_QUOTA；em_session_start 返回 STATIC_READONLY_SCOPE_DENIED、operation_sent=false，故当前正式 owner/CLAIM 未可靠核实，本结果非正式 Result 或独立 Driver 接纳。

PREFIX-281：验证源代码中存在的单来源相位准备/掩码是否为**真实合法模型操作**（完整 model_law_id、六维 Cell、Port、物质/动量、场、来源边界、检测器、独立时间）。如可合法实施，在原始 Stage50 中执行 f/g、n=2 边界与内部零支持；如不能，则只对逐项列明的现有合法操作证明全历史自相关商的组合封闭性。不得将 source lag r 误称心跳时间，或把条件性的 U0 定理提升为物理规律。

Researcher-ID: EM-R006-P280 / TASK_RESEARCH
