# PREFIX-287｜C4-BRC相干等距与最优二值Detector

**时间：**2026-10-27。**类型：**AUTHOR_SIDE_EXACT_PROOF / FORMAL_C4_BRC / NATIVE_H_N_BRIDGE_PENDING / NOT_ADMITTED。

## 权威来源与任务范围

GLOBAL_KNOWLEDGE_V1固定快照为 awdawmip/chatgpt-global-knowledge@cc9bb8a39531f5b6dc06133d6575cf6f48d21a17；已读取00_BOOTSTRAP、OPERATING_MANUAL、TASK入口、P000启动投影和原件（Blob均指向770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc）、ACTIVE世界观、数学/代码/BRC政策。Enterprise Math科学输入固定为 awdawmip/enterprise-math@59cd706d1bd078640f8bbc218622d32e2cbca09c，其docs/PORTABLE_RESEARCH_PROTOCOL.md Blob为ca5de2d680d2439ff4b67c2c55fbd4159813cd5c。复用该快照PREFIX-286的有序来源对、八结果双Port以及PREFIX-285的奇异伙伴相位选择。

本模型的来源标签j不是X6空间轴或心跳时间。P000仍定义完整六轴离散Cell、独立时间、不存在原生平面；以下结论不声称X6原生Detector成立。

## 1. 完整四有序来源路径对模型

有限来源包a=(a_0,...,a_{n-1})∈Q(i)^n，Z=Σ|a_j|²>0，零延拓a_{-1}=a_n=0，q=i^p∈C4。对σ∈{+1,-1}、j=0,...,n，保留两个来源支路：

b_{σ,j,0}=qa_j/2，b_{σ,j,1}=σa_{j-1}/2。

输出质量来自全部四个有序来源对的精确BRC和：

M_{σ,j}=Σ_{α,β=0,1}b_{σ,j,α}conj(b_{σ,j,β})=|qa_j+σa_{j-1}|²/4，P_{σ,j}=M_{σ,j}/Z。

交叉项的正负只在同一结果的BRC有序路径对及两Port合并时合法抵消；正质量本身未作为带符号幅值处理。

## 2. 定理A：保全所有复内积，存在显式左逆

定义相干输出V_q(a)_{σ,j}=(qa_j+σa_{j-1})/2。对任意同长度a,b，

Σ_{σ,j}V_q(a)_{σ,j}conj(V_q(b)_{σ,j})=Σ_j a_j conj(b_j)。

证明：逐j展开四个来源交叉项，将σ=±合并，带σ的交叉项相消，余项是(2qa_j conj(qb_j)+2a_{j-1}conj(b_{j-1}))/4；零延拓保证两组求和各等于输入内积，因|q|²=1总和为输入内积。且V_q(a)_{+,j}+V_q(a)_{-,j}=qa_j，故a_j=conj(q)(V_q(a)_{+,j}+V_q(a)_{-,j})。

因此测量前的形式源寄存器V_q是相干等距且单射；此强于PREFIX-286的单输入总质量守恒。对输出端口作测量后能否保全信息、实际资源/损耗及物理后态均是另一问题。

## 3. 定理B：只读Port总量无法恢复隐匿相位

设C1(a)=Σ_{j=0}^{n-2}a_j conj(a_{j+1})，则逐源对展开：

P_{σ,all}(p)=Σ_jP_{σ,j}=1/2+[σ/(2Z)]Re(conj(q)C1)。

所有p∈C4的端口总量只依赖c1=C1/Z。对于a=(1,i,1)与b=(1,-i,1)，二者c1=0且Z=3，所以任意p的P_+=P_-=1/2。无论调多少统一C4相位，只要只读两个Port总量，这对来源相位无法区分。

## 4. 定理C：单bit二值事件达到既定八结果测量的TV上界

三来源端点奇异伙伴规范化为a=a0(1,r,t)、a'=a0(1,t conj(r),t)，a0>0、t∈C4、r=ρζ (ρ>0,ζ∈C4)，伙伴不同；两包有相同的全部自相关、端点质量p0=a0²/Z、对角来源质量。

定义d=(p0/2)Re(q(r-t conj(r)))。由同一输入对角质量逐bin相消，以及t conj(r-t conj(r))=-(r-t conj(r))，八结果中非零差值恰为：

ΔP_{+,1}=d，ΔP_{+,2}=-d，ΔP_{-,1}=-d，ΔP_{-,2}=d。

其余四个结果差为0。故所有八结果的总变差距离为TV=(1/2)Σ|ΔP|=2|d|。

定义唯一二值输出事件E={(+,1),(-,2)}，Ec=其余六项。则ΔP_E=2d，因而

|ΔP_E|=TV(P_a,P_a')。

这是固定八结果仪器的一切经典结果合并(后处理)中对这对伙伴最大可能的分布分离；并非所有物理测量的无条件最优性。选择前序已证明的p(t)=1若t=1，否则p(t)=0时，C4奇异伙伴r≠t conj(r)满足：

|ΔP_E|=2p0ρ（t=±1）；|ΔP_E|=p0ρ（t=±i）。

相比只取(+ ,1)事件的分辨差严格提升一倍。E的选择与未知伙伴是哪一个无关。

精确反例：a=(1,i,1)，b=(1,-i,1)，q=i(p=1)。按(+0,+1,+2,+3;-0,-1,-2,-3)的未归一化BRC质量分子为：
a=(1,0,4,1;1,4,0,1)，b=(1,4,0,1;1,0,4,1)；共同分母4Z=12。
Port总量双方都是1/2，二值事件却给P_E(a)=0、P_E(b)=2/3。

## 5. 实际精确程序证书

执行 node verify_prefix287.js > RESULTS_PREFIX287.json。复用PREFIX-286的Gaussian BigInt、C4相位、四有序来源路径对、原观察签名分桶；新加入跨不同输入a,b的四有序交叉来源对以检验完整内积等距，及对每对歧义伙伴检验二值事件严格分离、与八结果TV的精确等式和预言分差。

固定有限域：a0=1..4，a1=m1*i^k1、a2=m2*i^k2，m1,m2=1..4，k1,k2=0..3。恰1024包；四相位×八Port-bin=32768次精确BRC质量读出，4096次质量守恒，4096次一般交叉输入的等距比较。814个签名中110个端点奇异，66个有两个不同归一化来源解；66/66二值区分且精确达到TV。一般命题由逐项代数证明成立；枚举验证范围是上述1024包，不宣称枚举证明任意复来源输入定理。计算不使用浮点、π、三角函数、矩阵指数或普通传播器。

## 6. 实际原生桥接口审查

已在上述固定EM提交读取当前HEARTBEAT_WORLD_NATIVE_X6_TIME.json、RESIDUAL_FAITHFUL_DISCRETE_RELATIONAL_SYSTEM.json、JOINT_RELATION_OBSERVER_PRESERVATION契约、AGENTS及Portable Research协议。当前世界契约的fixed_heartbeat_program为null。直接读取该main的stage50/interference.py和stage46/model.py路径收到404；PREFIX-278/282保留早期归档原始Stage50证据，但该归档尚不能替代当前完整已准备H_n上的可实施Detector。

下一原生义务是取得真实model_law_id及六维Cell、材料动量、全场、来源/边界、独立时间的完整H_n接口，确认统一C4控制、来源移位、双Port合束与单bit事件E能够作用于**同一已准备状态**，并保全或显式更新真实测量后全态及资源损耗。Stage50的local重准备输入和packet_variance离线统计不等于原生Detector。此处已证形式BRC最优二值界；物理可实现性继续待证。

GitHub账户认证身份为awdawmip(admin)。原生任务查询回执CONTROL_QUOTA，em_session_start拒绝STATIC_READONLY_SCOPE_DENIED且operation_sent=false；活跃Owner/CLAIM未知，正式Result/独立Driver数学审查未完成，不借用其他身份。工具决议COMPOSE_APPLIED(PREFIX-285/286)，EXTEND_EXISTING_TOOL(来源交叉等距与TV二值证书)。

## 7. 后继

PREFIX-288：从真实有来源的model_law_id、原始Stage50归档及当前H_n合法操作/探测接口中判定E的可实施性；合法时在同一完整已准备态重现p=1下0与2/3并核验测后全态/资源/时间；接口不齐时记录第一个精确类型缺口并保留形式结论，不由接口缺失推出物理否定。
