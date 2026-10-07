# 代数残差补丁：二阶顺序记录与适用边界

Progress-Event-ID: EM-20261007-RESIDUAL-ALGEBRA-PATCH-7C2E8A
Status: UNREVIEWED / NOT_ADMITTED / FINITE_TYPED_BRC_INTERFACE
Research-Activity-ID: RA-9AB8E1740FA512765F7EBCEA
Researcher-ID: EM-DIRECT-8FF435
Session-ID: MCP-934a3a1bbe474d97bbad582dd841578b
Logical-conversation: chatgpt-six-axis-minimal-perturbation-20261007-7c2e8a (not platform attestation)
Global-read: 5a13c778840c8eed2ffe200155dc7beec29478ba
Mathematical-source-read: a1033e7057c7ebed3ef221d60935e9dadb9eea86
Prior-frontier: enterprise-math@c23b729575bad73f6df58b00859f195d7452798b:research_notes/chatgpt_direct/20261007_six_axis_minimal_perturbation_7c2e8a/NOTE.md

## 当前问题与结论

用户：“继续 看看是不是需要给代数打一个残差补丁”。继续此前观察闭合判别，不重做旧结论。这里构造一个明确、有限可复验、可证明结合律的运算扩展；不宣布真实晶胞一定遵守它，也不修改整数算术、P000、平方和读数、世界观或正式任务。沿原始轴的字词只表达路径，不能冒充三元作用闭合、实际执行许可或物理时间。

端点坐标对纯路径串联本来就是闭合的：z(PQ)=z(P)+z(Q)。因此本实验没有发现端点加法错误，更没有证明“相同六轴读数的真实晶胞下一步坐标必然不同”。新增必要性只针对声明的顺序观察；实际力学是否读取这些记录仍是原生接口缺口。

## 1. 载体与BRC对应

选择参照Cell，路径P=(v_1,...,v_n)，每步v_a属于十二个带符号原生轴。实验全程六轴；短例只使用其中两轴，其他四分量显式为零，不称二维原生平面或完整三维切片。

BRC分支总体是按升序选取0..d个路径发生位置的索引组，各分支权重1；不是物理随机分支或概率。字母是带符号轴标签，正质量始终非负。保留输入完整字词作为来源。每个已选字母串的CWM系数记录其发生位置重数，串联用cwm_propagate，备选重合用cwm_recoalesce。

记C_d(P)[a_1...a_k]为k<=d的索引子序列系数。任何PQ中的子序列唯一拆成P内前段与Q内后段，故截断卷积C_d(PQ)=C_d(P)*C_d(Q)；系数的备选和串联遵守现有CWM法则。这是本扩展的对应证明。借用的不只是BRC名字：实际执行了冻结源码函数原码片段。未加载无关对数/除法模块，不能称全包回归。

源码：src/enterprise_math/brc_weighted.py@上述数学快照，Git blob 3f205696709e847909958a153f8fe10d3f6b70f0。入口：CWMState、CWM_ONE/ZERO、cwm_edge、cwm_propagate、cwm_recoalesce。Reuse: REUSE_EXECUTED + EXTEND_EXISTING_TOOL；新扩展尚未准入。

## 2. 二阶顺序残差与串联律

定义z(P)=sum_a v_a；对1<=i<j<=6，定义
Omega_ij(P)=sum_{a<b}(v_ai*v_bj-v_aj*v_bi)。
这是有符号顺序计数，不是欧氏面积、能量、力或角度。实现先分别保存正、负贡献部门与完整正CWM端口系数，再取已声明的整数观察；没有用负权质量相消。

按两次发生均在P、均在Q、一次在各段分组，严格得到
Omega(PQ)=Omega(P)+Omega(Q)+z(P) wedge z(Q)，
其中(z wedge w)_ij=z_i*w_j-z_j*w_i。

于是候选二阶状态的动作乘法是
(z,Omega) star (w,Eta)=(z+w,Omega+Eta+z wedge w)。

结合律证明：c(z,w)=z wedge w满足c(z,w)+c(z+w,u)=c(w,u)+c(z,w+u)，两边均为z wedge w+z wedge u+w wedge u。该证明覆盖任意有限轴字词，不由有限枚举冒充无限证明。这里star是动作串联，不是普通数乘；BRC备选加法则是系数逐项recoalesce，并对卷积分配。

端点投影保持普通加法；单独Omega却不闭合，因为拼接时需要两个端点。省略交叉项可让人造的分量直积运算仍然结合，但它已不再等于真实字词的顺序观察；仅检查结合律并不足以验收补丁。

## 3. 明确见证及六轴解释

P=(+1,+2)与Q=(+2,+1)都有z=(1,1,0,0,0,0)，但Omega_12分别为+1和-1。故不存在仅以六轴端点为输入、输出该顺序观察的函数。任何仅依赖端点的修正f(z)，包括一个平方和或对称度量修正，都不能区分两者。

L=(+1,+2,-1,-2)端点全零，Omega_12=2。1122与1212端点均为(2,2,0,0,0,0)，Omega_12分别4、2。它们是已执行的路径计数，不是材料运动实验。

一般右拼接一步+e_i给出：z'=z+e_i，Omega'_jk=Omega_jk+z_j*delta_ki-z_k*delta_ji。只有涉及轴i的五个关系通道可能变化；相应其余轴分量非零时该通道确实变化。其余五个z_j仍不变。这个精确区别是“五条关系记录受影响”，不是“五个坐标必然同时变化”。也没有导出全局即时传导、力学最小作用量或最小扰动选择律。

六轴共有15个反对称轴对记录，不是15个新增空间维度，也不是完整状态的普适最小参数数。

## 4. 整数合法性与不可随意补值

实际轴字词的可达二阶对恰好满足Omega_ij == z_i*z_j (mod 2)。必要性：模2忽略符号和先后，所有i/j发生配对数为n_i*n_j，且n_i==z_i、n_j==z_j。充分性：先按轴编号排块实现z，该路径Omega_ij=z_i*z_j；再拼接有向四步回路，每次独立改变某一Omega_ij的±2而不改z。因此任意满足该奇偶约束的对都有有限字词实现。此实现只证明路径代数可达，不证明物理许可。

等价整数补丁坐标kappa_ij=(Omega_ij-z_i*z_j)/2具有kappa'=kappa+lambda-z_j*w_i。这依赖选择的轴排序基准；Omega形式较对称。不能随意加入不可达的残差半格。

更换端点依赖的基准Omega->Omega+f(z)，不会改变同一端点两条路径的残差差值。形式上端点余边界f(z)+f(w)-f(z+w)关于z,w对称，不能抹去非零反对称交换差2*z wedge w。非零顺序差不是仅靠一个端点函数就能消去的坐标记账差；仍不因此成为物理能量。

## 5. 补丁的反例边界

空路径和(+1,-1)具有同(z,Omega)，但步数不同，所以二阶对不能替代全部来源。

更强见证：1221与2112有相同完整一阶、二阶带符号端口子序列系数，步数也相同；但三阶系数不同。比如模式122在前者出现1次、后者0次。因此即使保留所有二阶记录，也不能冒充任意高阶观察完整。两者的后续端点仍可相同；本见证区分的是已声明三阶观察，而非偷偷添加的物理更新。

最小充分状态必须相对观察与合法后续语言定义。对于本二阶观察及任意有限前后串联，(z,Omega)的乘法律保证精确保真；若增加步数、三阶模式、来源识别或真实内部场作用，须重新检查，不能沿用该压缩许可。

## 6. 实际检查与证据

BRC_PATCH.py可用Python 3.10+直接执行，仅标准库；系数函数为已取回的源码片段。已执行独立文件形式及合并文件形式，输出results.json逐字一致；同作者重复执行，不是独立复验。

完整枚举十二方向长度0..3的1885个字词，检验其7369个全部切分；另检查1728个单位字词三元组的结合律，并检查上述明确见证与每个枚举字词的奇偶条件。最终91306断言通过；实际调用cwm_edge 27168次、cwm_propagate 183266次、cwm_recoalesce 183266次。这些断言不是91306个独立物理实验。

执行文件SHA256：8b74d37eec97457b71e5873426db6b800a5001039da0f48e813a73b6870da96c。
完整results.json SHA256：c20876f74f7f4b62db24755fa4434fd5e05fb2e5845b9abbbb67d22398d01182。运行程序重新生成完整原始输出；会话复验包也保留该文件。无新增经典三角、pi、普通传播器或高精度参考运行。

## 7. 外部先例、研究结论与下一接口

这不是全新经典代数：Conrad的Group cohomology and group extensions讲义第2页明确给出扩展乘法、结合律的2-cocycle条件及截面变换。已读取并截图公式页。Diehl、Ebrahimi-Fard、Tapia，Tropical time series, iterated-sums signatures and quasisymmetric functions，arXiv:2009.08443v3；本轮实际读取官方题录/摘要，其任意交换半环上的迭代和与先后信息是直接先例，不声称读完全文。本工作是面向原生轴字词/BRC类型约束的明确应用，不宣称首次发现中心扩张或顺序签名。

公开来源：https://math.stanford.edu/~conrad/210BPage/handouts/gpext.pdf；https://arxiv.org/abs/2009.08443v3。

本轮判断：需要防止“把完整晶胞状态等同于端点数字”的过度压缩，已构造可检验关系补丁；没有证据要求把现行q(z)=sum z_i^2改为q+epsilon，或把2*2改成4+epsilon。位置代数、动作代数、观察代数和能量本构必须分别定型。

下一真正物理接口是给出有独立来源的原生作用/闭合规则F，并检验同z异Omega的合法完整状态是否产生不同后续z或其它原有观察。若F只看z，本补丁对其端点预测不必要；若F看Omega，则需要它或等价充分状态；若F还区分上述同二阶异三阶见证，二阶补丁不够。不可把这三种判断提前写进F，更不能直接把Omega视作力。

控制说明：本轮GitHub原生控制session_start已成功，Issue2850，注册Source提交ab0726f8b380d38e80a952afcc41f9bf301367ad。它修复此前只读MCP未登记的问题，未借身份、未领取Task/CLAIM/open、未创建Result或数学准入。研究持久化不是审核通过。
