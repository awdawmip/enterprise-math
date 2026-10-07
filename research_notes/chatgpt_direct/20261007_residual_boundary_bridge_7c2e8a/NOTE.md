# 残差补丁 U2 接口审计：任意固定阶顺序统计不代替当前入口

Progress-Event-ID: EM-20261007-RESIDUAL-BOUNDARY-BRIDGE-7C2E8A
Status: CONDITIONAL_CIRCUIT_PROOF / EXECUTED_TYPED_BRC / UNREVIEWED_NOT_ADMITTED
Research-Activity-ID: RA-FE8AC7FAFBDC1E9AA0662D86
Researcher-ID: EM-DIRECT-6B9D98
Session-ID: MCP-5b2766aee48c4b0a9f3dbe78e1210ebc
Logical-conversation: chatgpt-six-axis-minimal-perturbation-20261007-7c2e8a (not platform attestation)
Global-read: d4b7e8a3a08512e5826d88d8d08f1a145098c20a (remote observed 2026-10-07T10:21Z)
Source-read: 564949b13c4e7c07c21c075a517e8f3b1bee98c3

## 1. Continuation and source boundary

用户继续“看看是不是需要给代数打一个残差补丁”。消费上一轮顺序扩展，不重跑其1885字词/91306断言全套，也不把候选Omega自动接为力。原程序BRC_PATCH.py位于research_notes/chatgpt_direct/20261007_residual_algebra_patch_7c2e8a/，blob e3397722b0ee88dc9810cb872a14e7889403eee5；本轮只调用其signature/readout等既有函数。

本次有来源的后续操作是既有U2 packet_router.py，位于research_notes/chatgpt_direct/20261007_cell_closure_u2_7f21d8/，blob7465f5aa16cbb8fba61ba4be80f8a6884b879c53。其README blobbd35175a2e5ca379e95a9c0b922395ce3be45ec7已明确默认40组signed incidence是候选；不是合法原生三元作用证书。本轮不改变该核、incidence、rho或占位选择律。

当前Source的INTERFACE_CERTIFICATE.md仍说明固定来源的G1/G2原生事件合法性/不可分实现、G3反作用/存储、G4时间/边界、G5占位后继缺口。准确路径：research_artifacts/mcp/RS-U2-NATIVE-OCCUPANCY-BRIDGE-20261007/MCP-1a6e3bae74c6436bae9f2b466e7042ba/94bd4acc4df02dacf568/INTERFACE_CERTIFICATE.md。该他人任务及贡献只读消费，不借CLAIM，也不把其固定来源缺口断言为全项目不存在性。

所以本结果是“既有条件电路确实读取被省略的信息”，不是原生力学已证。P000、120度PERP_E、六轴整数端点、q(z)=sum z_i^2和受保护世界观均未修改。

## 2. Actual reused operation and observer

十二端口p=0..11，对应+1,-1,+2,-2,...,+6,-6；next incoming为q xor 1。冻结rho=1/4，bulk每个出射边lambda=rho/12=1/48。材料处使用原表rho*K(q,p)，其中

K(q,p)=1/3 if q=p; 0 if q=-p; 1/15 if axis(q)!=axis(p).

这里incoming是朝向来路的端口，q=p表示回向来路，不冒称直行。K来自40个完整三轴包的分腿及正BRC聚合，不是本轮为制造区别设的新矩阵。每输入有120个腿支路；同端口40、异轴每有向端口8、反端口0。六轴响应由原axis_totals读出，不是材料位置。

实际调用原brc_weighted.py，blob3f205696709e847909958a153f8fe10d3f6b70f0，9635字节，SHA2564f3e356227a1c964d33a3ddae94922463ba28097a43b8d1b8f6cd9ca5615fc9f。U2加载器仅去掉两个未调用的相对导入，全部函数/类AST保留并校验；不是全包回归。旧顺序签名仍独立记录其实际BRC调用。

实验采用声明的可控单位电路seed，不把它冒充U2的各材料各12入口均分注入。一个预定材料Cell在路径终点，选中路径此前均在空Cell；整个传播始终有六轴十二方向。输入路径选定两条不同轴，可带符号，其余四分量显式零。没有原生二维平面或完整三维切片的宣称。每一步的未选同胞支路及衰减部门都作为未展开边界保留，不做后选择归一化；整个已展开树前沿的总正预算严格为1。

## 3. Executed distinguishing witness

正轴简写P=1221、Q=2112。从同seed出发、同一终端材料布局，二者端点均z=(2,2,0,0,0,0)，长度4，全部一/二阶带符号端口子序列CWM相等，Omega亦相等。沿选中bulk路径的arrival CWM均为(1,a,a)，a=lambda^4=1/5308416。

P最后一步+1，材料入口-1；Q最后一步+2，材料入口-2。原核的下一次散射给第1轴响应：

P: C=40, W=a/12=1/63700992, M=a/480;
Q: C=16, W=a/30=1/159252480, M=a/480.

总active响应都为a/4，另有3a/4保留衰减部门。轴1之差a/20来自不同入口列，不是浮点、近似、模型新增项或正质量相消。每单位入射响应的比较为1/12与1/30；这只是明确的比率观察，不把两条历史的实际arrival重新归一化。

比较对象是带路径标签的输入贡献及保留的边界，不是同一完整确定性初态无故产生两个不同结果；也不证明原U2固定等分注入下，无外部选择即可准备两个孤立物理态。对逐项传播和允许识别这些贡献的上下文，入口分解不能删除；对完整脉冲则按来源/Cell/入口正确聚合，不要求保留每条原始字词。

完整覆盖不同轴有向字母的120个有序(a,b)对，并检查abba/baab，均有同样的对应轴读数区分。本见证比“同端点异Omega”更强：即使保留上一轮全部二阶计数，仍漏掉原有后续操作所需的入口。

## 4. All-fixed-order impossibility within the declared word/circuit family

设C_d(P)为上一轮的全部阶数<=d子序列CWM系数（发生位置分支权重1），不是只保留反对称Omega。取两个不同轴字母a,b，定义

U_0=a, V_0=b;
U_(n+1)=U_n V_n, V_(n+1)=V_n U_n.

命题：任意n>=1，U_n、V_n长度均2^n，C_n相等，但末字母不同。故对于任意预先固定的有限d，存在同端点、同长度、同C_d、同arrival CWM的允许路径，在同一个终端U2散射上给出不同轴响应。不存在仅靠固定阶C_d覆盖此族任意长历史的精确预测规则。

证明完全使用BRC的正系数卷积。假设C_d(U)=C_d(V)。任何长度<=d+1的模式在UV中按边界唯一拆成左前缀、右后缀。内部拆分的两段都长度<=d，因假设和标量CWM串联可交换，UV与VU的对应贡献相等；两端拆分的贡献为C_w(U)和C_w(V)，只是相互交换，recoalesce结果相等。因此C_(d+1)(UV)=C_(d+1)(VU)。d=0的空模式系数相同给出归纳起点。末字母在每轮互换，始终不同。由K的两不同轴列可区分得后半结论。

这是对全部有限n的符号证明，不是由n<=8检查外推。它使用有界阶子序列签名的特定定义，不宣称所有有限摘要都无效，也不声称同两条路径在所有阶都相同。固定最大路径长度时可以保留足够高阶而还原全字词。无限族中的每一对保持相同seed和布局；跨n的预定终点可变，或将布局平移到同一材料Cell而明确改变seed位置，不冒称固定seed/固定有限域的同一长时轨迹实验。

本递归属于Thue--Morse型k-binomial equivalence既有数学，不宣称经典新发现。Lejeune/Leroy/Rigo, Computing the k-binomial complexity of the Thue--Morse word, arXiv:1812.07330v1，官方题录/摘要已读取；摘要明确定义同<=k阶子序列重数。上述特定归纳证明在本记录自足给出；未宣称读完论文或其完整复杂度定理属于本项目新成果。

## 5. A smaller operational repair can outperform ever-higher order

反向实测：P=123、Q=213具有不同Omega，但端点、最后入口、arrival CWM完全相同。原核下一步全部signed-port CWM相同，继续三层同源/Cell/port传播仍逐项相同。

对于预定固定材料位置、只允许同一表的单输入线性传播，完整当前映射Phi[(source,Cell,incoming)]=CWM已足以接续：

Phi_next[b,z+d(q),-q] = recoalesce_p propagate(Phi[b,z,p], T_z(q,p)).

这是对原U2的实际复用。相同映射的一步后继相同，归纳覆盖任意有限层；无需为这个受限观察保存全部历史或Omega。若另要观察Omega，则额外保存它，不能把“不影响此算子”说成没有意义。三元整包阀门、来源联合操作、旧请求目标或未知原生力需要其它字段，12入口不是普适完整状态。

对单条路径，末字母是一个12值标签（空路径另有单位标记），不是新空间维度。对多路径混合，要保留按入口分别聚合的联合CWM，不是只记一个平均方向。若只要当前一阶total响应，可用非负12向量x；若还要C/M或来源，保留相应更强载体。

精确最小性（仅下一步12个有向端口total观察）：原核x->y是单射。令h_j=x_(j,+)+x_(j,-)，d_j=x_(j,+)-x_(j,-)，S=sum x，则

b_j=y_(j,+)+y_(j,-)=rho*(h_j/5+2S/15);
c_j=y_(j,+)-y_(j,-)=rho*d_j/3;
S'=sum y=rho*S.

所以h_j=(5b_j-(2/3)S')/rho，d_j=3c_j/rho，x_(j,+/-)=(h_j+/-d_j)/2。每个不同入口预算向量都被该观察区分，不能做非平凡合并。只有在线性数值参数化内才能进一步称rank=12；不排除等价编码，不冒称必需12个任意类型字段。只看即时六个unsigned-axis totals时，仅h可辨，不能沿用12维必要性。

36项正BRC输入（12纯端口+24明确有理混合）实际验证该观察逆关系；未执行普通矩阵求逆或谱参考。正/负差仅为保留正数据后的声明观察，不是负支路质量。

## 6. Resolution boundary and scientific meaning

对于U_d/V_d的实际seed，a=lambda^(2^d)，对应轴响应差Delta=a*rho/5。任何从同C_d返回同标量预测的规则，在该对输入中的最大绝对误差至少Delta/2；由|y1-y2|<=|y1-t|+|y2-t|立即证明。

Delta对每个有限d严格正，但随长度增长而衰减；没有统一正下界，不证明有限分辨率下永远可见。近似压缩可以有合法尺度/误差范围，不能把精确不可合并偷换为物理可检出性。关系深度不是时间，响应不是力、能量或材料位移。原六轴平方和读数未失败；改变的是状态充分性判断。

本轮收获：残差补丁应由后续操作的输入接口来选择，不能只按历史统计阶数堆叠。顺序关系记录有其保真范围；当前入口则是这一个现有算子的必要边界数据。真正原生作用是否读取哪个残差仍需G1/G2及其对应证明，而非本轮凭空指定。

## 7. Execution, persistence and next

check_bridge.py为本轮新检查器，普通Python标准库，无远端计算；依赖两份已有固定Source与旧signature文件。完整运行5430主断言及1694旧读出辅助断言。120个有向跨轴对；d=1..8、最长256步的递归对；36个输入向量；相同边界的三层未来读回。上述类别不冒称全X6动力学完备。

实际U2内核调用：edge3066、propagate36306、recoalesce94470；旧顺序接口：edge2946、propagate503964、recoalesce503964。完整results.json为193406字节，SHA256 64afd915dae19d8ddfc41c04a466e37ad46896c210c7ec3246ca256236fb11cd。会话复验包保留全部正部门、同胞边界、样本和输出；Source检查器可逐字重建。重复运行属同作者复验，不是独立审核。

当前逻辑会话重新登记成功，Issue2878，Source活动0435c14acb55f04701fc7baa1e566bee06cce099。继承前轮EM-DIRECT-8FF435及两个事件贡献，不借他人会话。无Task/CLAIM/open/Result/Driver/数学准入。上一轮pre-final2860实际终态FAILED/GITHUB_HTTP_403，不再称排队或通过。新轮最终门独立处理。

外部专用检索Issue2883，batch08b381ae-d3eb-4b5d-ac88-a40e8cdf1a05，原request摘要97cd940a0a72c9cd094d6dc4ea3ba7d76c36199089df9c5fa4c966e51c434179已匹配：返回3项题录摘要，子项PARTIAL/retrieval_verified=true，外层state=FAILED；如实保留这两个状态，不用外层标签抹掉实际字段，也不宣称批次全成功。关键原文另由官方arXiv核对。

下一最小科学单元：给出原生事件Lift_E及合法signed incidence后，审计该接口究竟区分哪些输入状态；只有有来源的原生桥改变后，才能将当前核相对的必要性提升到晶胞物理判断。现有二阶/全固定阶见证及其检查无需重做。与当前母题相关的三元阀门、源别、旧anchor缺口保留原作者证据，不重命名为本轮发现。
