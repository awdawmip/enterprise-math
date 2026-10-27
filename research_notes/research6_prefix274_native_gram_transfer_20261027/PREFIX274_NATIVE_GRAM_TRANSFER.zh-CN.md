# PREFIX-274：有来源的相位BRC Gram转接、最少符号测量与C4剩余信息

日期：2026-10-27；状态：**AUTHOR_SIDE_EXACT_PROOF / NATIVE_TRANSFER_PENDING / NOT_ADMITTED**。

## 1. 固定来源与问题

账户知识库 GLOBAL_KNOWLEDGE_V1：`main@4d75b6c92823119d725fff4949699fe3fb0f07c2`；Enterprise Math：`main@339855dac47f83f01b2301e563ce462e2aa4ff0c`。同一知识库版本已读取两项规范入口、项目路由、P000启动投影和原件（Blob SHA1 同为 `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`）、ACTIVE世界观。已读取 Source 的 `docs/PORTABLE_RESEARCH_PROTOCOL.md`、`docs/HEARTBEAT_BRC_ONLY_ARITHMETIC.md` 及机器约束、`definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json`、`definitions/HEARTBEAT_SELF_CONSISTENT_INSTANT_V0_1.json`、Stage50干涉核（`research_notes/HEARTBEAT50_INTERFERENCE_KERNEL_20260923_6DD798.md`）、PREFIX-273正文与其 NEXT_PREFIX274。

承接此前形式 Z₂ 相位探针定理，直接复用 Stage50 **完整带来源剩余态的检测 Gram** `Γ_y(γ,δ)=⟨v_γ(y),v_δ(y)⟩` 和有序路径对BRC的强度观察；讨论从这些**声明的效应语义**到形式探针的精确关系，不声称它已由 P000 或原生心跳动力学导出。六条原生空间轴、一个独立时间维度以及三元非零稳定力作用的 P000 约束保持不变；本论文的 `k` 是带来源的路径数，不是空间维数。

当前源 `definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json` 的 `fixed_heartbeat_program=null`；暂行 `H_n` 自洽瞬间的快照契约要求具体 `model_law_id`，但不提供一个全局已核验的 `Φ:H_n→H_{n+1}`。这是转接义务，不等于已经证明任何特定候选律不存在。

GitHub实际认证 `awdawmip` 有 push 权限；原生 `em_control_dispatch` 返回 `CONTROL_QUOTA`，`em_session_start` 返回 `STATIC_READONLY_SCOPE_DENIED, operation_sent=false`；活跃正式Owner/CLAIM未核实。因此本研究文件属作者侧Source保存，**不是正式Task/Result/Driver接纳**。并未用Drive绕过原生授权拒绝。

## 2. 精确BRC Gram差分定理

取 `k≥2`，带来源标签且互不合并的分支 `1,…,k`，幅值 `m_i∈Q_{>0}`，形式目标控制系数 `c_i∈Q`，当前候选**实对称** `Γ∈Sym_k(Q)`，可比较的形式符号准备 `s∈{±1}^k`。在这一个明确载体上定义由**全部有序(i,j)来源路径对**给出的读数：

```text
I_Γ(s) = Σ_{i=1}^k Σ_{j=1}^k s_i s_j m_i m_j Γ_ij
I_c(s) = (Σ_i s_i m_i c_i)^2
Δ(s)   = I_Γ(s) - I_c(s)
D      = Σ_i m_i^2 (Γ_ii - c_i^2)
r_ij   = Γ_ij - c_i c_j                       (i<j)
B_ij   = 2 m_i m_j r_ij                      (i<j)
Δ(s)   = D + Σ_{i<j} B_ij s_i s_j
```

**定理1（严格充要）：** `I_Γ(s)=I_c(s)` 对全部声明的符号准备同时成立，当且仅当 `D=0` 且全部 `r_ij=0`。

**证明：** 对均匀枚举的 `{±1}^k`，常数字符 `1` 与各不相同的二次字符 `s_i s_j` 相互正交。于是

```text
D    = (1/2^k) Σ_s Δ(s)
r_ij = [1 / (2 m_i m_j 2^k)] Σ_s Δ(s) s_i s_j
(1/2^k) Σ_s Δ(s)^2 = D^2 + 4 Σ_{i<j} m_i^2 m_j^2 r_ij^2.
```

每个表达式均为精确有理BRC路径对等式。前两式直接恢复所有声明的残差，后式由正交性得到Parseval的**残差平方能量恒等式**。它证明残差坐标为零当且仅当形式转接在整个Z₂族上成立；非零者是该模型内的严格数学失配证书，**不自动是原生物理残差、能量或温度**。

注意：`D=0` 仅固定对角差的一个带权和，**不能**逐项推出 `Γ_ii=c_i^2`。如果合法协议另外允许同一`Γ`下单独隔离任意一条路径，并且这些单路径读数也与`c`一致，才补得每条对角式；再加两路径Z₂观察，方可得 `Γ=ccᵀ`。此增强结论以“隔离路径合法且不改变Γ”为额外前提。

## 3. 仅 1+binom(k,2) 次准备的精确转接层析

之前全Z₂枚举可用 `2^{k-1}` 个整体相位等价状态；对**此次二次残差**无需全枚举。固定 `s_k=+1`，其他位置以 `F⊆{1,…,k−1}` 指定翻号，写 `d(F)=Δ(s(F))`。只需 `F=∅`、全部单集与全部双集：

```text
N = 1+(k-1)+binom(k-1,2) = 1+binom(k,2)
C   = d(∅)
A_i = d({i}) - C
B_ij = [d({i,j}) - d({i}) - d({j}) + C]/4   (i<j<k)
B_ik = -A_i/2 - Σ_{j<k,j≠i} B_min(i,j),max(i,j)
D    = C - Σ_{i<j} B_ij
r_ij = B_ij/(2m_i m_j).
```

**证明：** 令 `x_i=1` 当第i个位置翻号，`s_i=1−2x_i`，`x_k=0`。则

```text
d(F)=C + Σ_{i<k} A_i x_i + 4 Σ_{1≤i<j<k} B_ij x_i x_j.
```

在零、一、二元激活输入上取逐阶有限差分，依次恢复所有`B_ij`与`D`，证毕。一般实对称Gram残差族的独立线性系数恰为 `1+binom(k,2)` 个；每次固定符号准备只给一个线性标量方程，故**对于重建全部一般线性残差坐标**，此`N`是最少的查询数。该下界不宣称对额外PSD/秩一承诺下的纯二值判断同样最优；亦不证明真实心跳系统支持这些实验。

当 `k=6` 条**来源路径**时，恰为 `16` 次准备，恢复15个交叉残差和1个对角总差，少于32种整体符号类。

## 4. C4原生转接边界：Z₂永远看不见Gram虚部

Stage50可能使用 Gaussian rational/C4 或更丰富相位。对于 Hermitian `Γ` 和纯实符号 `s`，有序BRC的反对称虚交叉项互相抵消，`I_Γ(s)=I_{ReΓ}(s)`（若幅值已并入），因而上述两条实定理**绝不**提供完整复Gram保真。

最小精确反例：

```text
Γ+ = [[1,  i/2],[-i/2,1]]
Γ- = [[1, -i/2],[ i/2,1]]
```

二者均Hermitian正定（主对角=1、行列式`3/4`），每个`(±1,±1)`符号输入均读出`2`。但形式C4相对相位输入`a=(1,i)`给出

```text
a* Γ+ a = 1,   a* Γ- a = 3.
```

这是精确的**Gaussian-rational有序路径对BRC证书**，不是三角函数或普通量子传播器。尚未证明此相对相位调整可由真实原生 Source、真实Source/Port/边界实施。因此合法C4观察或存储虚部Gram是进一步转接的必要义务；无论Z₂样本多大，都不能消去这个残差。

另一个纯实两模型证书：`m=c=(1,1)`，`Γ_coh=[[1,1],[1,1]]`与`Γ_tagged=[[1,0],[0,1]]`均PSD，分支对角正质量相同，而`(++),(+-)`的效应分别为`(4,0)`与`(2,2)`。这不是两股物理力，更不是已证实的原生不同演化。

## 5. 核验范围、复用及未完成义务

代码 `verify_prefix274.py` 用`fractions.Fraction`显式累加有序(i,j)路径对；附带Gaussian rational C4有序配对。实际检查`k=2,3,4,5,6`的全部`124`个Z₂符号配置，稀疏重建`40`次查询、`35`个带标签交叉系数，逐项核实Walsh与Parseval及两个反例，返回`PREFIX274_FORMAL_GRAM_TRANSFER_PASS`；结果另存`RESULTS_PREFIX274.json`。一般断言靠上述证明，非有限拟合。

工具/方法处理：Stage50完整带来源Gram及PREFIX-273路径对效应 = **REUSE_APPLIED**，且保留正权质量与有符号幅值的类型差别。本轮没有执行原始Stage46 source import、没有完成`model_law_id`或完整Cell/Port/材料与场动量/来源边界/时间的源法则对应，亦没有物理时间轨迹或三元闭合实验。这些未执行事项不得被本地验算的PASS替代。

## 6. 最小后继：PREFIX-275

索取并固定一个真实Source支持、完整类型的`model_law_id`及源合法相位BRC探针，明确Cell/Port、材料/场动量、时间、三元作用和来源边界。运行Stage46**原始**有序路径对源码，计算真实许可控制下的检测Gram；若只允许符号准备，输出本轮虚部未可观测的明确障碍；若允许C4，实测其虚部交叉项并检验转接。维持作者证明、source接口验证、正式CLAIM、独立Driver审查及Foundation接纳的严格区分。
