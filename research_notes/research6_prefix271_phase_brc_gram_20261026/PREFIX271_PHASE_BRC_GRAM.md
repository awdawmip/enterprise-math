# PREFIX-271｜Z2 相位 BRC 的未来安全 Gram 观察商与严格残差比特定理

**日期**：2026-10-26。**证据级别**：作者侧精确解析证明、Z2 路径对 BRC 独立语义检查 PASS；原生 Source 包调用、物理心跳演化与独立 Driver 接纳尚未完成。本文件不是正式 Researcher CLAIM 或 Result。

## 固定 Source、语义与科学边界

GLOBAL_KNOWLEDGE_V1 的不可变规范输入：awdawmip/chatgpt-global-knowledge main bd1ae1ef27a06ebb005264d08c306cb8204f55b0；已读 bootstrap、manual、P000 原件与投影（原件 Blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc 一致）、ACTIVE 世界观、研究方法及 BRC-only 条款。Enterprise Math 科学输入固定 main 8d68cd3924ae47688b3350ff482cdbe8c4d5f545；已读 docs/PORTABLE_RESEARCH_PROTOCOL.md、docs/HEARTBEAT_BRC_ONLY_ARITHMETIC.md、research_constraints/heartbeat_brc_only.json、definitions/ENTERPRISE_BRC_RECURRENT_PORT_FOUNDATION_20260903.md、Stage46 端口相位候选 BRC_HEARTBEAT_PORT_UPDATE_LOCALIZED_MODE_20260923_92DA92、HEARTBEAT_WORLD_NATIVE_X6_TIME.json 和 HEARTBEAT_SELF_CONSISTENT_INSTANT_V0_1.json。接续 PREFIX-270 的非负有理 WBRC 端口阈值结论，但不把正质量当成有符号幅值。

设具有来源标签的有限路径族 P={1,...,k}，每条路径有有理带符号幅值 a_i∈Q，非零幅值携带正有理权重 |a_i| 和 Z2 相位 φ_i。路径 ID 和顺序保留。仅为**本定理所声明的形式未来分支选择/合流上下文**，选 c∈Q^k；尚未证明 Stage46 或心跳物理程序允许任意此种控制。依照 Stage46 已定义的有序路径对带符号相位角色和，设

    I_c(a) = Σ_(i,j) |c_i a_i||c_j a_j| χ(φ_i−φ_j)
           = (Σ_i c_i a_i)^2，χ(0)=+1, χ(1)=−1。

右式是完整 Z2 路径对的代数展开，不是删除路径来源并用正质量冒充干涉。定义有标签 Gram 观察 G(a)=(a_i a_j)。

## 定理 A｜有限二分支探针恢复未来全部强度

对于任意 a,b∈Q^k，以下四项等价：（1）所有形式上下文 c∈Q^k 的 I_c(a)=I_c(b)；（2）所有 k 个单路径探针 c=e_i 和 k(k−1)/2 个双路径探针 c=e_i+e_j 强度相等；（3）G(a)=G(b)；（4）b=a 或 b=−a。

**证明**：单路径探针给出 G_ii=I_ei=a_i²，而 i≠j 时

    G_ij = [I_(ei+ej) − I_ei − I_ej]/2。

故（2）推出（3）；而 I_c=cᵀGc，又得（3）推出（1）；（1）当然推出（2）。如 G=0，所有幅值都为零。否则选 a_r≠0；b_r²=a_r²，故 b_r=s a_r，s∈{±1}，再由 a_r a_j=b_r b_j 推得每一 b_j=s a_j，所以（3）推出（4）。整体反号显然保持 I_c，反向成立。证毕。

此处的“极小”仅指**未来观测等价类的完整且不可再合并的商**。不意味着 k(k+1)/2 个 Gram 坐标是最低存储开销，亦不意味上述查询数最少，更不能对具有其他观察或控制的原生系统删除全局符号。

## 定理 B｜固定大小的 Z2 相位严格需要 k−1 bit

在 k≥1 条有标签非零路径上，已知所有 |a_i|=1，仅未知各 a_i∈{−1,+1}：共有 2^k 个符号向量，按定理 A 每一同强度类恰有 a、−a 两个。因此恰有 2^(k−1) 个可由未来合流区分的类，至少需要 k−1 bit。保存 (sign(a_1a_2),...,sign(a_1a_k)) 即用 k−1 bit 完全实现，此界可达。含零路径、未知大小、来源历史或额外可观测符号的操作都不自动满足该数字。它不是原生六维之外的新增空间轴。

## 最小可复核反例

令 a=(1,1)，b=(1,−1)。两种状态的独立路径强度均为 (1,1)，若忘掉相位，其正权 CWM 均是 (count,total,dominant)=(2,2,1)；但同一形式双路径合流产生 I_(1,1)(a)=4，I_(1,1)(b)=0。Gram 分别为 [[1,1],[1,1]] 与 [[1,−1],[−1,1]]，差异是精确相位交叉项而非舍入误差。仅一条非零路径不含独立相对 Z2 相位；两条为此机制的最小反例。

## 实际有限计算与证明范围

在隔离的作者侧 Python 分数/Z2 有序路径对 BRC 语义检查器 verify_prefix271.py 中，逐支路保留 ID、正权、相位，以全部有序 (p,q) 对直接计算角色和，再由单双探针重建完整 Gram。穷举 k=1..5，字母表 {-1,0,1} 共 363 个有标签向量及各自 2^k 个二进制子集上下文；另穷举 k=3、{-1,−1/2,0,1/2,1} 共125个向量；另穷举 k=1..8 的全部 2^k 非零符号向量，验证等价类数 2^(k−1)，k=8 时128类。所有 PASS。一般 k 由上述解析证明，不由有限测试外推。

验证代码未导入原始 Enterprise Math 包，未执行原生 Cell/Port 相位物理程序或 TRIADIC_CLOSURE_E 实验，也未使用 π、经典三角、普通矩阵指数、Taylor/Padé/Cayley 模型绕行。保留有来源的 12种原生有符号方向、六维 Cell 和独立时间；本定理绝不主张形式选择次数等于心跳次数。

本次对话另保存完整中文证明、英文论文、原始精确结果 JSON、完整代码和验收回执 ZIP，归档 SHA-256：ed0d3aa08de13628ad45c97d31f8c360466cfd7607690e67c5dd97c3581d6028。最终 ZIP 已实际解压、逐文件哈希比较并从解压版本重跑 PASS。代码源文件 SHA-256 daa6ae7c2a72412e8ce9db388d891c3259304ca9b46ce9867b7b4591d6773173，完整 JSON SHA-256 eca6f46629eb72ba7f220b6ae43fb5b96d0f441f490e811785ba346bba59afb7。

## 原生桥接障碍、权限和下一问题

本轮实际读到 HEARTBEAT_WORLD_NATIVE_X6_TIME.json 的 fixed_heartbeat_program=null；HEARTBEAT_SELF_CONSISTENT_INSTANT_V0_1.json 将 H_n 定义为需要 model_law_id 的自洽瞬间，却不构成完整的心跳间 Φ:H_n→H_(n+1)；Stage46 的定向 Port 相位散射 T 仅是 SCOPED_CONSTITUTIVE_CANDIDATE，不覆盖材料、场动量、物理时间、全部边界与来源，也未证明所有形式 c 可实现。这里是有界来源审计，**不证明全仓库不存在其他候选法则**。

GitHub 认证身份 awdawmip 对研究仓库有 admin/push；原生研究服务的真实 static_machine_readonly 身份 em_session_start 返回 STATIC_READONLY_SCOPE_DENIED、operation_sent=false；em_control_tasks 返回 CONTROL_QUOTA。正式活跃 Owner/CLAIM 未可靠核实，不能派发或宣称正式 Result、Driver 接纳；GitHub 本文仅作作者侧记录。

**PREFIX-272 精确未决问题**：找到真实版本化完整 model_law_id 以及具有六维 Cell、类型化 Port、材料、场、动量、相位、时间、来源/路径、边界条件与 P000 三元闭合的 Φ。证明它允许双路径 BRC 探针并满足观察交换律，或者定位第一个不成立的操作/类型前提，保留有标签 Gram/相位交叉项而不进行物理结论升级。另需在真实 Source 环境执行相位 BRC 导入比对并保存原始结果。

**标记**：AUTHOR_SIDE_EXACT_PROOF / STANDALONE_EXACT_PHASE_BRC_PAIR_CHECK_PASS / SOURCE_IMPORT_PENDING / NATIVE_LAW_PENDING / NOT_ADMITTED.
