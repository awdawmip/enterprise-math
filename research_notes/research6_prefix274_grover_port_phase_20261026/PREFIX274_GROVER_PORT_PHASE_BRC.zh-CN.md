# PREFIX-274｜Stage46 局部端口相位 BRC 的奇偶可观测性定理

**证据级别**：作者侧精确解析证明／Python Fraction 带来源有序路径对验证 PASS／独立 C++ 整数有序路径对验证 PASS。不是原生 Research Result，不代表完整心跳物理规律或独立 Driver 接纳。

## 来源快照、方法与身份
GLOBAL_KNOWLEDGE_V1 固定 main@a307e21a64150ced71df99120a1a14f0487946e9，项目 P000 投影与原件 blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc 一致，并读取 ACTIVE 世界观、研究策略及 BRC 唯一运算约束。Enterprise Math 科学输入固定 main@1a7e2a95db1d16921e71ccb7968f836bda83d6ac，读取 docs/PORTABLE_RESEARCH_PROTOCOL.md、docs/HEARTBEAT_BRC_ONLY_ARITHMETIC.md、research_constraints/heartbeat_brc_only.json、definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json、definitions/HEARTBEAT_SELF_CONSISTENT_INSTANT_V0_1.json、research_notes/BRC_HEARTBEAT_PORT_UPDATE_LOCALIZED_MODE_20260923_92DA92.md、src/enterprise_math/brc_weighted_recurrent.py，以及 PREFIX-273/274 接续资料。

前序 PREFIX-271—273 使用任意形式有理控制探针研究 Z₂ 相位 Gram、图论及割集可辨识性。本次改为 Stage46 源码文献**明确声明**的局部散射币，而不再把任意形式探针自动宣称为原生合法控制。

GitHub 认证主体为 awdawmip，具有 push 权限。原生 em_session_start 返回 STATIC_READONLY_SCOPE_DENIED，operation_sent=false；em_control_tasks 返回 CONTROL_QUOTA，故真实活跃 Task/Owner/CLAIM 未能可靠读取。作者侧活动 RA-R6P274_20261026_2345 仅追踪来源，不授予原生身份、领取任务、审查或数学接纳。

## 精确载体和 BRC 观测
固定局部顶点度数 d≥1，入端口来源标签 i=1,…,d，出端口标签 j=1,…,d。取 Stage46 局部有理 Grover 散射币

\[
C_{ji}=\frac2d-\delta_{ji}.
\]

准备等绝对幅值的纯 Z₂ 输入，相位符号 s_i∈{−1,+1}，原始来源及入端口保留，密度为 ρ_ik=s_i s_k/d。出端口 j 的**带标签有序路径对相位 BRC** 强度严格定义为

\[
P_j(s)=\frac1d\sum_{i,k=1}^d |C_{ji}|\,|C_{jk}|\,
\chi(\phi_{ji}-\phi_{jk})
=\frac1d\sum_{i,k=1}^d C_{ji}C_{jk}s_i s_k,
\]

其中非零支路的 Z₂ 符号为 sign(C_ji)·s_i。后一等式是上述有序来源路径对的字符和展开，**不是正权总质量相消或普通传播器替代 BRC**。出端口标签不合并。完整 X6 六轴、独立时间、Cell、Port、场、来源、三元闭合属于该候选之外仍需核验的原生层；d 是端口数，**不是空间维数，也不是原始作用力数**。

令 S=∑_i s_i，得到精确 BRC 恒等式

\[
\boxed{P_j(s)=\frac{(2S-ds_j)^2}{d^3}},
\qquad \sum_jP_j(s)=1.
\]

## 定理 A：一次观测的奇偶分类
按整体同时反号识别 s∼−s，共有 2^(d−1) 个来源相位轨道。

* 若 d 为奇数，带标签向量 P(s) 在上述全部轨道上一一单射，因此签名数量为 **2^(d−1)**。
* 若 d 为偶数，P 的**唯一非单射纤维**是全均匀读数 P=(1/d,…,1/d)，恰包含所有同号符号向量所成的一个轨道，及全部平衡 S=0 向量所成的 binom(d,d/2)/2 个轨道。因此该纤维有
  \[
  \boxed{F_d=1+\frac12\binom d{d/2}}
  \]
  个来源相位轨道，其余纤维均单元素。严格的不同签名数量为
  \[
  \boxed{Q_d=2^{d-1}-\frac12\binom d{d/2}}.
  \]

**证明**：当 s 包含两种符号且 S≠0，两种标签组的输出差为 P(+)-P(−)=−8S/d²≠0。因此观察中的低强度标签集合，恰为 s 中与 S 同号的严格多数端口。只由该带标签集合，就能重建 s 的整体反号轨道，不可能与另一个混合非平衡轨道混淆。全同号输入时 P 恒为1/d；S=0 时也恒为1/d；反过来任何混合非平衡输入因两个强度层不同不可能均匀。平衡输入仅在 d 为偶数存在，共有 binom(d,d/2) 个符号向量，反号两两成对，故以上是全部碰撞。将唯一大纤维并合并计算全部 2^(d−1) 个轨道数，得到 Q_d。d=1 边界亦成立。证毕。

**最坏结构残差**：若未来观测需要在上述 F_d 个同签名轨道之间作严格区分，单次出端口读数之外至少需 ceil(log₂ F_d) bit 附加标签。这只是当前观察语言中的信息量，不是物理空间维数。

## 定理 B：单端口符号翻转的最少观察次数
令 M 翻转一个**事先固定**的入端口的符号，保留其他来源、标签与候选局部散射币。考察两次独立准备后的带标签观察 T(s)=(P(s),P(Ms))。Stage46 研究记录过一次入端口原始符号变更 (ε=2)，但物理可实施性与完整本体演化仍未证实，故本定理仅在此**声明的候选控制菜单**成立。

若 d 为偶数且 d≥4，则 T 在全部符号轨道上单射，且在“固定已知符号掩码＋原局部币＋带标签端口强度”的菜单中**两次设置严格最少**：任意固定掩码是符号轨道上的双射，故其单次观察仍有定理 A 的大纤维。对于该大纤维，原 S 的绝对值仅可能是 d（全同号）或0（平衡）；翻转一个端口后 |S'| 为 d−2 或2，均为非零且混合（d≥4）。定理 A 的已证混合非平衡单射可重建变更后的轨道，已知掩码可逆，遂重建原轨道。证毕。

当 d=2，C₂ 恰为两个端口交换矩阵，任意符号及任意已知端口符号掩码之后，观测总是 P=(1/2,1/2)；因此在此**严格受限**的观察菜单中，任何有限次数均无法区分两个相位轨道。此障碍不否定下游重新合流或更强原生操作。奇数 d 无需第二设置。

四端口最小证据：s=(+,+,+,+) 与 t=(+,+,−,−) 均产生 P=(1/4,1/4,1/4,1/4)；同翻转第一输入端口后分别获得 P(Ms)=(1,0,0,0)、P(Mt)=(0,1,0,0)，完全由有序 BRC 相位路径对精确算出。

## 实际运行证据与验证范围
verify_prefix274.py 保留每个正有理分支权重、Z₂ 相位、入端口 ID 与**全部有序 (i,k) 路径对**，逐个以 Fraction 计算 P，再独立对比解析式、归一化、碰撞轨道、两设置签名；穷举 d=1,…,8 共255个整体相位轨道，PASS。verify_prefix274.cpp 独立用 dC_ji=2−dδ_ji 的整数有序来源路径对求和，再与整数幅值平方比对，穷举 d=1,…,12 共4095个轨道，PASS。全部结果在 RESULTS_PREFIX274.json 和 RESULTS_PREFIX274_CPP.txt。

示例：d=6：32轨道、单次22签名、异常纤维11轨道、两次32；d=12：2048轨道、单次1586签名、异常纤维463轨道、两次2048。无限 d 的断言由解析证明，不依靠有限穷举外推。

执行的是**与真实 Stage46 局部法则相同的作者侧 BRC 语义检查器**，**未执行原始 stage46.brc_port_update 模块导入/源程序，亦未运行原始历史 414 断言或19次 canonical BRC power**。Grover 散射已有外部先例，不声称发明其本身；本轮不主张可实现原生心跳 H_n→H_(n+1)、物理相位传播、物理温度/作用力、TRIADIC_CLOSURE_E 实验或独立接纳。当前 fixed_heartbeat_program=null，瞬间定义要求 model_law_id 但不定义全局 Φ。

## 精确下一研究问题 PREFIX-275
用实际版本冻结的累积 standalone Stage46 原始源码读取合法入端口、相位和有序 BRC 路径对接口；运行 d=2,3,4,6,12 的有标签端口强度及端口符号翻转对照并保存完整输出。随后查找真实 model_law_id 并建立六维 Cell、Port、材料场动量、独立物理时间、来源/边界及 P000 三元闭合与局部操作的完整类型桥；若缺失，给出缺少的第一个精确类型/操作而非另造物理律。不等有理幅值及混合态需重新分类，不能直接沿用本轮纯等幅奇偶结论。

**AUTHOR_SIDE_EXACT_PROOF / TWO_EXACT_CHECKS_PASS / ORIGINAL_STAGE46_SOURCE_IMPORT_PENDING / NATIVE_LAW_PENDING / NOT_ADMITTED**
