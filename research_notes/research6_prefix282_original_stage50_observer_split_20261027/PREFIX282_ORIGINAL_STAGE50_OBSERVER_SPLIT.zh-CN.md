# PREFIX-282｜原始Stage50的同谱包观察域分裂与来源对角BRC证书

**等级：AUTHOR_SIDE_EXACT_SOURCE_PROOF / ORIGINAL_STAGE50_LOCAL_40_PASS / NOT_NATIVE_ADMITTED。** 继续PREFIX-281，对以前的完整自相关同谱来源包检验原始Source是否已经有非自相关型合法声明观察，且区分输入准备、读出与物理演化。

## 固定资料、确实获得的权限

GLOBAL_KNOWLEDGE_V1 固定当前 main 4d6f9095e0c6624cd88d55a07b4f2c2f24432879，读取00_BOOTSTRAP.md、OPERATING_MANUAL.md、数学及代码约束、项目TASK入口、ACTIVE《我眼中的世界》和P000原件及投影；P000原件 Git blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc 与投影所指一致。Enterprise Math当前控制及研究输入固定 main f0bf6130ea0c79c0ac6299c93478146c0bfced8e；现行docs/PORTABLE_RESEARCH_PROTOCOL.md blob ca5de2d680d2439ff4b67c2c55fbd4159813cd5c，HEARTBEAT_BRC_ONLY_ARITHMETIC.md blob 787e74952765b61904f2bd67038291f5f081af83。

原始执行证据来自用户已经存在的私有Drive文件 BRC_Heartbeat_interference_stage50_20260923.bundle，Drive ID 1ImJLXQSA6ZSebObWVunMbdVmUyKqjl4N，37,502,868 字节，SHA256 c90254ee224498e9a4e87717ba202a73cbdc44a82a8b20abdc0a8bb75ef0dbf8，git bundle verify返回完整历史及退出码0；原始Git提交318f47839d6bc7c850a3b7cc0fcb22d48febd9ba。此原始归档的读取不是备用路径写入。准确源码SHA256：stage50/interference.py=43b23d47e5d3da191aeaeefefe4f378fea2166eefd228ae77475f7196ceca853；stage49b/gauss_brc.py=a2a16cee4d9e851aa8c676d1ab68491c7a8954f7ff9232e4cb57424f6fd31ccf；stage46/brc_port_update.py=a6bc156c789859d1aabefdef5db56b9d313565c5684d744e591e3371687baee4。

GitHub connector真实认证账户 awdawmip 对此仓库有push/admin权限。原生研究控制 tasks 请求返回CONTROL_QUOTA；session_start返回STATIC_READONLY_SCOPE_DENIED，operation_sent=false。无法核实当前活跃owner或CLAIM；作者侧文件不是原生Result/Driver接纳。

## 精确源码审查及其类型界限

原始stage50.interference.prepare将声明的有理复系数转为非负C4相位纤维，pair_observer仅对具有同一完整材料端点和同一场闭环来源的路径执行全部有序相位对；field_packet将索引j编码为g.add((),g.CYCLE,j)的闭环字段。moment(packet,r)计算已声明的自相关有序来源路径对读出，local_input(packet,r,phase)在**输入准备**中分置材料端口A、B并给B一个来源偏移及相位；local再执行Stage45/46 BRC coin与Stage49b场移位，读取十外端口质量。给定local参数r、phase并不在已经准备的同一个H_n内实施来源局部翻相门U0。three_masks是三个**材料输入Port**的遮罩而非来源索引门。stage49b.gauss_brc.translate_field根据(arc,field)条件实施完整字段闭链平移，不是C4 phase翻转。上述接口审查没有声称原生世界其他实现里绝无U0。

**在已有原始Stage50 Source中找到并实际运行另一类读出**：stage50.interference.packet_variance(packet)，它从每个单独来源载荷执行pair_observer(field_packet({j:a_j}))，再返回来源对角概率分布P_j、其方差及二倍第二矩。stage49b.gauss_brc.energy对声明闭链字段j给出对角link-cost：g.CYCLE的j倍载荷之cost等于2j²。这是源码声明的cost，不等于经过实验校准的物理能量，也不是另外一个传播器。

## 定理：完整自相关商对原始Stage50全部已定义读出不充分

设有限来源包a，完整有序C4来源路径对强度给出Z=Σ_j |a_j|²>0，C_r(a)=Σ_j a_j conjugate(a_(j+r))，越界为0。source-defined对角路径对读出为

P_j(a) = pair_observer(field_packet({j:a_j}))/packet_z(a) = |a_j|² / Z.

**断言**：存在两个来源包，其全部C_r、全部十外端口C4-BRC观察均相等，但已经存在的packet_variance所返回的P_j与精确二次矩不同。

取 f=(1,4,4)，g=(2,5,2)，有：

C0(f)=1+16+16=33=C0(g)=4+25+4；
C1(f)=1×4+4×4=20=C1(g)=2×5+5×2；
C2(f)=1×4=4=C2(g)=2×2，且|r|≥3时两边均为0，负r取共轭。

由已在PREFIX-278原始Source复现的十外端口BRC公式
E_a(r,p)=(5/18)[1-Re(i^p C_r(a)/Z)]
可知两个包在**所有**历史差r和全部四种C4 phase p的十外端口读出完全相同。

然而原始pair_observer要求完整同一来源匹配，对单来源正载荷的全部有序C4相位路径对正是|a_j|²；除以Z后，

P(f)=(1,16,16)/33，P(g)=(4,25,4)/33，尤其P_0不相等。故当允许的观察语言包含原始packet_variance时，完整自相关观察商被严格细化。证毕。

原始程序返回的两个包对角矩与source-defined cost精确为：

| 来源对角读出 | f | g | 差 f-g |
|---|---:|---:|---:|
| 来源均值 μ=ΣjP_j | 16/11 | 1 | 5/11 |
| 来源二阶矩 q=Σj²P_j | 80/33 | 41/33 | 13/11 |
| 来源方差 V=q-μ² | 112/363 | 8/33 | 8/121 |
| 源码声明闭链对角cost=2q | 160/33 | 82/33 | 26/11 |

此证明在声明C4 BRC路径对语义内严格成立，是带类型的观察区分证书，不是普通算术冒充BRC，也不需要π、三角函数或经典矩阵指数。完整自相关虽然不是充分商，但这不等于数值误差或物理结构残差已经得到外部证实。

## 原始Source执行与验证范围

本轮在哈希核验的原始提交内，实际运行同目录verify_prefix282.py（PYTHONPATH指向该原始checkout，使用python -S）。共**40次真正的原始stage50.interference.local调用**：两包 × r∈{0,1,2,3,4} × p∈{0,1,2,3}。每次验证精确概率、输入输出范数=66、g.compatible及十外端口BRC公式；两包每项相等。另各运行一回three_masks：八项Port遮罩读数逐项相同，均I3=0；各运行packet_variance以及原始pair_observer和Stage49b energy，验证上述对角数据及差值。所有Fraction/有理复相位核验PASS，运行结果原文在RESULTS_PREFIX282.json。本轮40次是真正新增原始Stage50调用；前轮的512项replay没有计为本轮新试验。

核验界限：所有r的同谱性有上面的解析证明，程序只执行r0..4；目前原始Source仍无可核验的**完整**model_law_id及H_n→H_(n+1)演化。packet_variance是对可读取完整输入packet的**软件观测函数**，尚未证明它对应在单一完整X6心跳状态中物理可实施的探测器。即使Stage50内部可以访问每个来源标签，也不能由此断定现实测量设备可以。各来源索引不是X6空间轴，r不是独立物理时间；完整物理转接仍需Cell、Port、场、材料动量、边界、来源、探测效应和时间的对应证书。

## 本轮纠偏与后继问题

PREFIX-281在仅允许全自相关式观察以及共同有限源滤波、平移、全局相位及自适应组合时的不辨识证明保持正确。PREFIX-280“U0若合法可以区分”也是正确条件命题。本轮收紧此前容易误读的结论：**若将观察扩大到原始Stage50已经定义的对角来源观测，则f/g无需假想U0即可在源码内区分**；不得将原有PREFIX-281声明的较窄观察集合冒称Stage50的全部已定义读出。

下一PREFIX-283：判定packet_variance究竟是输入准备日志/离线全态诊断还是存在合法物理Source探测效果；寻找真实model_law_id与X6心跳类型桥。若没有可实施的来源对角检测，则重新限定“可用探测器”观察代数，证明其保真或构造严格不可辨识证书。必须区别条件性操作、源码观察和物理时间演化，不改P000、不宣布物理定律。

Researcher-ID: EM-R006-P282 (author-side, native session unauthorized).
