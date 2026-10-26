# PREFIX-272 | 受限 Z₂ 相位 BRC 探针的完整观察类、生成树最优性和环路证书

2026-10-26 · AUTHOR_SIDE_EXACT_CONDITIONAL_PROOF / NATIVE_ADMISSION_PENDING / SOURCE_IMPORT_PENDING

## 1. Source 与语义

Global Knowledge 不可变读取：awdawmip/chatgpt-global-knowledge@1109726a4b9d2244b8aa53404ef4a4b27a3ecd04（00_BOOTSTRAP、OPERATING_MANUAL、项目研究入口、P000_STARTUP 与原件、ACTIVE 世界观、数学与 BRC 研究规则）。P000 原件 blob=770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc，匹配投影声明。

Enterprise Math 科学输入：awdawmip/enterprise-math@7f073d2fb8e396773a95d1c6945215e92dc4da93。已读 docs/PORTABLE_RESEARCH_PROTOCOL.md、docs/HEARTBEAT_BRC_ONLY_ARITHMETIC.md、research_constraints/heartbeat_brc_only.json、definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json、definitions/HEARTBEAT_SELF_CONSISTENT_INSTANT_V0_1.json、definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json、research_notes/BRC_HEARTBEAT_PORT_UPDATE_LOCALIZED_MODE_20260923_92DA92.md、PREFIX-271 定理和下一问题。原生 BRC 正质量内核 src/enterprise_math/brc_weighted_recurrent.py blob=4e6b3132580e3cd70a20a0d8bd4d28792b961afb；本轮未执行 Source import。

P000 六原生空间维度、独立时间与三元平衡没有改变。下面 k 是带标签的路径支路数量，绝不等于世界的空间维度。声明的形式分支选择不等于已经授权或实现的物理操控，局部 Stage46 是 SCOPED_CONSTITUTIVE_CANDIDATE / NOT_ADMITTED。

## 2. 精确有序路径对 BRC 模型

令 a=(a₁,…,aₖ)∈Qᵏ 为有来源标签的 Z₂ 带符号幅值。对任何**声明允许的**选择 c，观测由有序路径对与相位角色给出：

I_c(a)=Σ_(i,j) |cᵢaᵢ| |cⱼaⱼ| χ(φᵢ−φⱼ)=(Σᵢcᵢaᵢ)²，其中 χ(0)=+1、χ(1)=−1。

右侧仅是本有类型 BRC 角色和的代数恒等式，不把正权路径数当振幅。设图 H=(V,E) 是**假定**允许的二支路探针图，V 为 k 个标签。现只允许单支路 I_i=I_(eᵢ) 和边 (i,j)∈E 的两支路同号合流 J_ij=I_(eᵢ+eⱼ)。不能无证据认定 H 是真实原生合法图。单支路提供 mᵢ²=I_i，mᵢ=|aᵢ|。非零两端边给出交叉项 G_ij=aᵢaⱼ=(J_ij−I_i−I_j)/2，符号 σ_ij=G_ij/(mᵢmⱼ)=±1。

令非零支持 S={i:mᵢ>0}、r=|S|，c 为 H[S] 的连通分量数。

## 3. 定理 A：受限探针的观测等价类

固定所有 mᵢ。两个幅值向量 a,b 的全部单支路及 H-边二支路强度相同，当且仅当：对 H[S] 每个连通分量 C 存在 ε_C=±1，使全部 i∈C 满足 bᵢ=ε_C aᵢ；零支路仍为零。

证明：单支路确定各平方，于是非零分量上 bᵢ=εᵢaᵢ。边上的相同强度等价于 aᵢaⱼ=bᵢbⱼ，从而 εᵢεⱼ=1。沿图边传播即得连通分量内 ε 常值；分量整体反号不改变任何允许的有序路径对观测，反向成立。

固定正幅值，在 2^r 个符号向量中，每个观测类含 2^c 个向量，观测类恰为 2^(r−c) 个。此前 PREFIX-271 的完整 Gram G=aaᵀ 恰有 2^(r−1) 个类；因此每个受限类内尚有 2^(c−1) 种未来全对可区分 Gram，额外恰需 c−1 个相对 Z₂ 比特。r=0 时唯一全零态，缺少的比特定义为0。不能通过幅值为零的顶点传播任何符号信息。

## 4. 定理 B：生成树就是完整 Gram 的最小二支路询问集

在所有非零支路的**任意二支路探针均合法**且所有单支路强度已知时，完整 Gram 可恢复当且仅当实际测量的边图在 S 上连通。恰好 r−1 个二支路查询为最坏情形所需最小数，任一生成树达下界。

充分性：边 σ_ij 沿树路传递相对符号。更精确地，对树上路径 i=v₀,…,v_ℓ=j，

G_ij=[∏_(t=0)^(ℓ−1) G_(v_t,v_(t+1))]/[∏_(t=1)^(ℓ−1) G_(v_t,v_t)]。

中间对角元均非零，给出任意跨结点交叉项。必要性：少于 r−1 条被测边必断开，定理 A 的分量整体反号保持所有已有强度，但改变跨分量 Gram。即使自适应选择，每个新双支路询问最多连结两个原先独立的相位分量；最坏情形下仍至少需 r−1 次。对已有 c 个分量，若后续有合法跨分量探针，补 c−1 条桥接边充分且必要；如果未来法律始终保持分块，则应说明准确的观察/操作范围。

## 5. 定理 C：纯 Z₂ 路径态的环路一致性 / 反例

对每条 H[S] 边从数据计算 σ_ij=(J_ij−mᵢ²−mⱼ²)/(2mᵢmⱼ)。存在一个固定、纯的、rank-one 有标签 Z₂ 幅值向量实现所有输入，当且仅当：(a) 所有 σ_ij∈{+1,−1}；(b) 每个环路的 σ 边积为 +1。

必要性：真实 σ_ij=sᵢsⱼ，环路每个符号两次出现。充分性：每个连通分量选根为+1，沿生成森林设置 sⱼ=σ_ij sᵢ；每条非树边与树路径组成的基本环保证对应边约束成立，构造出兼容全部观测的有理向量。只需验证 |E(H[S])|−(r−c) 个基本环。

例：三条非零幅值均为1，三个单探针均为1，三条边 (1,2),(2,3),(1,3) 的合流读数 (4,4,0)，则 σ=(+,+,−)，环积为−1；不存在同一纯 Z₂ 幅值向量满足这组数据。该证书只否定声明的 rank-one 模型；混合态、不同准备/历史、接口缺失或读取错误仍需单独调查，不据此宣称物理异常。

## 6. 定理 D：全部有限未来的块局部作用失辨（条件）

设来源空间被分为 V=⊕_C V_C。若每个允许的后续线性 BRC 作用均保持该分块，且每个合法强度只包含块内有序路径对之和，则对 S_ε=⊕_C ε_C Id 的独立块反号，所有有限作用组合和基于相同观测历史选择的自适应组合均不可区分。

证明：块保持的 T 与 S_ε 交换；同一块的有序路径对相位差不随共同反号变化。任意有限复合仍交换，归纳观察历史可知自适应未来也保持相同输出。若未来加入跨块相干耦合，此结论的前提不再成立，必须重新检查。

## 7. 六路径证书与实际验证

当六个来源路径的幅值均为1，仅允许 (1,2),(3,4),(5,6) 的成对观测时，r=6、c=3：可见观测8类、完整Gram32类，缺2 bit。a=(1,1,1,1,1,1)、b=(1,1,−1,−1,1,1) 的全部允许读数相同；若引入合法跨块 (2,3) 合流，则分别给出4和0。这是六个**路径标签**的形式证书，不是六个原生 Cell 轴的演化结果。

随附 verify_prefix272_compact.py 真实执行声明的有序路径对 Z₂ BRC 核，在 k=1..5 全部1099个无向标号简单图及33866个图-符号状态组合上检查观测类数、类大小、完整Gram类数和环路可实现性；另测有理幅值、零支持、六路径、矛盾三环与9步块局部形式操作，全部 PASS。一般性来自上述证明，有限覆盖仅为辅助核查。运行没有调用原始 Enterprise Math 包、没有执行原生 Φ、三元闭合或物理心跳；未使用经典π、三角、Taylor/Padé/Cayley、矩阵指数等数值绕行。

## 8. 源码边界、权限、下一步

在固定的 HEARTBEAT_WORLD_NATIVE_X6_TIME.json 中 fixed_heartbeat_program=null；暂行 HEARTBEAT_SELF_CONSISTENT_INSTANT_V0_1.json 需要 model_law_id，尚不自带完整 Φ:H_n→H_(n+1)。Stage46 仅为带局部端口幅值的候选，没有完整 Cell/Port/材料与动量/场与场动量/物理时间/边界/来源联合状态。因此尚无法从当前已读来源导出原生合法探针图，也未执行 PREFIX-271 提议的当前 Source 包导入对照。保留对应残差 UNKNOWN。

本轮真实 GitHub 身份 awdawmip 有该仓库 admin/push；原生 em_control_tasks 返回 CONTROL_QUOTA，em_session_start 返回 STATIC_READONLY_SCOPE_DENIED / operation_sent=false，活跃Owner/CLAIM与正式Result/Driver审查均未证实。此文件及相关代码只是作者侧 Source 持久化，不替代正式状态机。

下一精确任务：取得版本化完整 model_law_id 和实际合法的相位 BRC 未来效果集；判断其单探针与交叉项张成关系/来源图连通性并验证真实更新下的闭包，或证明块相位守恒并记录不可消的相位残差；再执行真实 Source-import 精确比对。对于高阶多支路效果，需另做效果线性张成分析，不把上述仅限单/双探针的必要性误推广。

Status: AUTHOR_SIDE_EXACT_CONDITIONAL_PROOF / FORMAL_CHECK_PASS / SOURCE_IMPORT_PENDING / NATIVE_LAW_PENDING / NOT_ADMITTED.
