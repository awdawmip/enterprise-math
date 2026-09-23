# 观察并不统一消灭残差：测量完备分解与当前读出边界

Progress-Event-ID: HEARTBEAT-OBSERVATION-RESIDUAL-30346E-20260923
Researcher-ID: EM-DIRECT-30346E
Research-Activity-ID: RA-C14103043185020E79C7AA2C
Status: SCOPED_ANALYTIC_APPLICATION / NOT_ADMITTED / NO_NEW_BRC_EXECUTION

本轮问题是解释“观察时为什么某种残差似乎消失”，不是完成全部心跳物理。全局读取60b4ef7801eed2ead2b0f89e6a897608752710e9；Source读取8c2bc8500ec39b01e13cc1a1cc5e306b6cd5dc61；自己的原生登记来自Issue1333/request hb51-observation-session-20260923-73c9e1，Source e364bbab7146b63fe1c74c0198f6c18c9581394c。P000与残差保真定位不改。

复用Stage50 Source1286c0c876e082b8abc1f9787cdff96797f6251e的完整端点C4字符、路径对/Gram核及十二端口读出。REUSE_APPLIED：精确应用其已有二次观察与完整记录语义；没有新核心调用、数值模拟、三角函数或经典参考运行。内积、Born二次读出和量子仪器仍是声明的桥接假设，不从正权BRC或P000推出。保留前序贡献，不作独立复核或新基础定理首创声明。

## 一、三种不同操作

量子仪器I_m(rho)=sum_alpha M_(m,alpha)rho M_(m,alpha)^dagger，sum_(m,alpha)M^dagger M=I。

读数概率p_m=Tr I_m(rho)；已得到m后的条件态rho_m=I_m(rho)/p_m（p_m>0）；不选择结果的后态sum_m I_m(rho)。只给POVM F_m=sum_alpha M^dagger M不能确定后态。同一Z读数可以由M_0=|0><0|,M_1=|1><1|实现，也可由N_0=|0><0|,N_1=|0><1|实现；后者还重置系统。相同读数不代表同一物理观察操作。

理想Luders测量A=sum a_m P_m后，rho_m=P_m rho P_m/p_m满足(A-a_m)rho_m=0。这是所测量及选定结果的零，不是所有残差零。若P_m仅将A限制到中心a_m、宽delta的区间，则只得||(A-a_m)psi_m||<=delta/2。简并块、场与历史仍可保留区别。

## 二、完整结果的残差分解恒等式

固定同一完整出口差矢量r=a f-b g；对两项作用同一完备算符族M_mu，mu包括报告与必要隐藏Kraus标签。则

    sum_mu ||M_mu r||^2
    = <r|sum_mu M_mu^dagger M_mu|r>
    = ||r||^2.

全部结果同时使差矢量为零当且仅当原r=0。单个结果可以使非零r为零，不能把选择该结果当作全体结果清零。这是未归一化差矢量范数预算，不是能量/温度/净源的普遍守恒，也不声称CPTP保持任意密度差的范数。

对Stage50 Gamma_ab=<v_a,v_b>，令Gamma^(mu)_ab=<v_a,M_mu^dagger M_mu v_b>，则sum_mu Gamma^(mu)=Gamma。因而对既有剩余场施加同一完备仪器，不筛选结果、无反馈时，材料总读出不变。新增不同路径的条件记录不是对已汇合差矢量的同一M，不能误用本式否定路径测量的干涉效应。

## 三、约化相干的零与联合关系的非零

记录耦合|0,Dready>->|0,D0>、|1,Dready>->|1,D1>保留路径标签；可作为既有BRC完整端点的受控记录扩展。系统01相干乘以<D1|D0>；记录正交时该项为零，不取决于人是否知道结果。

例如|+>与|->被记录后为Phi_+=(|00>+|11>)/sqrt2与Phi_-=(|00>-|11>)/sqrt2。两个单系统边缘都为I/2；联合密度差Delta=|00><11|+|11><00|不为零，而其任一偏迹为零。区别保存在联合关联中，不只是指针单独状态里。

有限维Luders通道D(X)=sum P_m X P_m是Hilbert-Schmidt正交投影。R=rho-D(rho)满足D(R)=0，且Tr rho^2=Tr[D(rho)^2]+||R||_HS^2。这个零属于约化通道，不是完整幺正作用；完整等距嵌入V保持||Vr||=||r||。

## 四、干涉项消失可以使相消失配重新出现

继承p_ext=(5/18)(1-Re c)。在明确的条件可分记录模型中，新增记录重叠g_D=<D0,D1>使p_ext_new=(5/18)(1-Re(c g_D))。完美路径区分g_D=0给5/18，不是0；原本c=1的暗出口反而打开。若原c为负，变化方向可相反，不能说任何观察必然增大任何残差。

正交记录下，(|0,D0>-|1,D1>)/sqrt2=(|->|D_+>+|+>|D_->)/sqrt2，D_±=(D0±D1)/sqrt2。两记录结果概率各1/2；十二端口条件外逸分别0和5/9，总外逸仍5/18。量子擦除恢复一个子样本的暗出口，不是无条件消灭所有样本的残差。这里是沿既有BRC路径对观察的符号恒等式，未声称执行新仪器程序。

## 五、真实修复、守恒缺口与解释边界

Dj=s的有限区域边界恒等式不因读取而改变。对固定约束/源扇区Gpsi=qpsi，若[M_mu,G]=0，则G M_mu psi=q M_mu psi；非零结果不能清掉该扇区。反馈修复或仪器交换载荷须写出相应完整更新。真正多对一系统通道、局部重置和新增客观非幺正动力学并不被概念上禁止，但不能从局部看不到直接推出全局删除。

退相干解释局部交叉项被抑制；它本身不推出某次实验唯一结果为何被选中。条件更新与Born概率仍属桥接假设。精确零、分辨率下的零、条件分支零及极限小量必须分开。

安全消去的操作范围应显式给出：对所有允许未来的未归一化线性操作分支Phi以及观察效果E，Tr[E Phi(X-Y)]=0；每条分支保留其发生概率，之后才条件归一化。一次O(X)=O(Y)弱于该要求。

## 文献与验证范围

Preskill官方Chapter3页8-11的测量、条件/不选择与POVM后作用文字及页8-10截图：https://www.preskill.caltech.edu/ph219/chap3_15.pdf 。Schlosshauer arXiv:quant-ph/0312059v4摘要与§IV.B.1等相关段落；Zurek quant-ph/0105127官方摘要；Neves等0904.4242官方摘要。只引用实际读取范围，不作全面新颖性审计。

专用Issue1334/batch96cd40b1-a76f-49a5-804e-fc2a8b438e35，匹配comment5793787578、请求SHA4fa8c1ad8f7442b323c097b1dfb94a8a21b7134e6c7d9040d98126bf247b855a：外层FAILED、内层PARTIAL，真实一条Schlosshauer题录/摘要，上游总量未知，一次provider、零桥接模型。不得报作完整查询成功；原始结果保留原Issue，专业目录归档状态另记。

本轮完成有边界的解析说明及完备结果分解应用，无新数值实验、独立复核或Lean；未解决Born来源、自主物质-场-仪器动力学、真实能量和物体尺度或客观坍缩。后续可把相干记录、仅读记录、结果选择、反馈逆作用编成不同BRC指令并逐层核对，不能将它们压成同一“observe”指令。
