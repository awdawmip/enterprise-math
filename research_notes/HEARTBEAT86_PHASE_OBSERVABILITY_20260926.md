# Heartbeat86 — 原相位加入后的十一量预测闭包与三步区分证书

Progress-Event-ID: HEARTBEAT86-PHASE-OBSERVABLE-CLOSURE-20260926
Status: AUTHOR_DERIVATION_AND_EXECUTION / UNREVIEWED / NOT_ADMITTED
Global read: 978895ef2dc303c385fae14d8a54e482cdb0a3b0
Source read: 06495d21fb1cb93eb6e46ccccf148a9beeaf8f84
Research-Activity-ID: 无服务回执；本轮为已授权母题的可移植数学，不重放此前对话报告的登记阻断，不借用旧session/CLAIM/独立审阅资格。保存不是准入。

## 0. 继承与范围

父累计2ea447b05cd1a34f957633d3ab7fc1c4cf8f8271；父包52150935字节、SHA256641aea0ced5a2322a5dc6f178530107ec99cd4ae5e200f0212e02c3f6050fa71实核后本地克隆。Stage78–85全部源、CASE、模幂、固定相位和1e-6门槛不改。六原生空间轴、独立时间、P000、BRC-only及残差保真不变；不回到缺少数据的物理拟合。

Stage85四量只支持A/D未来。本轮增加原Stage80固定相位3宏字V及其真实逆Vinv，不新增理想旋转、不按名义八阶归零。概率及投影仪器仍标BORROWED_REFERENCE。新表示是预测商，不是物理清空完整场，不是十一数运行全部Shor。

## 1. 活动空间与十一量

原单位向量w=z3/S=a e0+n，S=2^64，n垂直e0，a²+||n||²=1；V=D0(2ww^T-I)。V在span(e0,n)上作用，其正交补上为恒等。A/D方向u,d不变，u^T d=-1/4，d垂直e0,n。

B=[e0,n,u,d]的实际BRC Gram H=B^TB正定，故T=range B四维，所有六种动作A0/A1/D0/D1/V/Vinv保持T；T正交补上yes为零，其余为恒等。

保存t=Tr rho及Cij=b_i^T rho b_j（0<=i<=j<4），共11个实量。交叉项带符号但不是概率。T正交补的质量为t-Tr(H^-1 C)；其形状及跨T相干不进入本语言。合法预测像为C半正定且上述质量非负；执行器从真实正输入生成，不声称已经实现任意外部十一元组的通用PSD验收。

令h=||n||²，u0=<u,e0>，un=<u,n>，c0=2a²-1。四个投影量y=B^T x的相位更新为
L_V=[[c0,2a,0,0],[-2ah,c0,0,0],[-2u0+2a(au0-un),2(au0-un),1,0],[0,0,0,1]]；
L_inv=[[c0,-2a,0,0],[2ah,c0,0,0],[-2u0+2a(au0+un),-2(au0+un),1,0],[0,0,0,1]]。
A_yes矩阵H[:,2]e2^T，D_yes为H[:,3]e3^T，no取I减yes。全部动作C'=LCL^T；V保持t，A_yes的t'=C22、A_no为t-C22，D同理用C33。六套十一量更新列实际BRC执行；61原基×6动作的366个投影列与原固定字/真实仪器逐项相等。

## 2. 后向效果闭包与最短词

从质量效果开始，以所有六动作拉回，实际有理证书得到层维数1,3,6,11,11。十一份独立效果词（按时间顺序）：empty；A0；D0；D0 A0；V A0；Vinv A0；V D0 A0；Vinv D0 A0；A0 V A0；V V A0；A0 Vinv A0。

所有主元、原效果行、基坐标和完整六动作闭包重建证书保留。消元乘积/差走实际BRC正路径和符号观察，有理商另以乘回相等核验，不用数值rank。

E3=E4证明全部有限未来封闭，不是三步抽查外推。两份等质量状态若十一效果签名同，则全部允许记录词和相同反馈概率同；不同则有长度<=3的词区分。distinguish按广度优先基层返回最短词。每一步V是整段相位宏字，不是单个H4或心跳。

独立效果和合法预测像的非空内部给出线性未归一化最少11量；固定迹一为10个仿射自由量。不是任意非线性编码或单轨迹下界。若去掉Vinv权限，层维数为1,3,5,8,11,11，第四层才完成，不能把三步结论推广到任意权限或任意Shor模型。

## 3. 两步不可分、三步可分的正纯态

令g=u-u0 e0-(un/h)n，gamma=||g||²，kappa=<u,d>，r=d-(kappa/gamma)g，v=un e0-u0 n。BRC证实r,v非零，r垂直u,e0,n,v，v垂直u,d。两份合法纯态为rho_±=(r±v)(r±v)^T/(||r||²+||v||²)。执行以整比例整数振幅和明确密度权重实现，不把奇分母塞入不接受它的dyadic接口。

对六字母全部长度0/1/2的43词，两态概率完全相同，且逐词对照原61模式。最短区分词V,D0,A0，两份原始联合事件概率约0.185224554780499与0.060373534691904。差严格在(0.1248,0.1249)，完整分数保存在SEPARATING_WORDS.json.gz。独立交叉恒等式为差=4 kappa ||r||² <u,Vv>/(||r||²+||v||²)。这是两份合法准备的可区分性，不是编译错误率或后选择成功率。

e0/e1原A/D四量同，本轮最短词V,A0长2。另在T正交补取非零z，e0±z归一化后是不同完整状态却有相同十一量，证明全未来等价；没有把全部不同全态都判成需分开。实际V八次不强制周期归零，实际逆序恢复。

## 4. Shor回归及保留控制标签的后续读取

12组原Stage80基准完整重跑：15的四底数/t4及a2/t8；21三底数/t6及a2/t10；33两底数/t6；35/a2/t6。终端概率、61模式状态哈希、宏范数、工作标签及逆序与父CASE精确同。后处理源和失败记录不改，未额外重跑后处理凑检查数。表示误差0不改变理想Shor原195/2^32等编译误差。

另15/a2/t4及21/a2/t6先执行Stage84 AD修改QFT，到终端才切换本轮语言：V；A；控制/报告相关相位；D；Vinv；A。中间相位由控制最低位XOR最近报告选择Vinv或V，是对角控制，不额外读取控制位。此后不混合不同控制值。每个保留控制值各存11量，终端允许控制计算基与内部报告联合读出。

每例四条旧历史×八条新历史=32，六个步骤边界全部十一量、所有记录/控制联合概率，与原61模式真实字和仪器继续演化逐项相同，零权历史保留且不归一。不能将各控制值汇成全局11量后声称保留联合结果；新增逻辑Hadamard、其他相位或旧指针相干访问需算子矩/更大范围，接口拒绝未认证动作。

## 5. 执行、复核和成本

最终184组命名检查、4392次实际不变BRC核心调用，多数是Gram、证书与列，不是4392次Shor。规范核src/enterprise_math/brc_weighted_recurrent.py@bc7babbb9e890f6d5a7094430a5fbdccf66c77ad，blob4e6b3132580e3cd70a20a0d8bd4d28792b961afb，SHA2567520822074b8f29e1c54f57b9543c043202db8bd7c6e27f3f1d6176028ac4a26。复用Stage83正路径配对、Stage82整数证书、Stage84实际仪器、Stage80固定字；动态数组为已证列的线性/双线性扩展。无三角、普通QFT、数值rank或辅助刷新。

一次不支持交互session的调用未启动；一次45秒完整尝试在大实例完成前触及时限，不计整轮通过。最终独立进程完成所有结果：原220584846926ns，新累计bundle克隆206358374619ns。递归仅排除elapsed_ns，科学字段全部一致；17份gzip字节完全相同。1605父文件不改，27项manifest、git fsck、两树干净、另Stage76独立引用均核验。便携包独立解压、新文件字节及CLI导入通过；没有第三次完整便携重跑。计时不是跨硬件性能或量子速度优势。

## 6. 可恢复产物与状态

本地累计60fb3f28045ad717c34a02f7345ff00672709dea；START_HERE_STAGE86.md。stage86/PROOF.md、phase_predictor.py、run.py、RESULTS.json、12REGRESSION、2PHASE_FUTURES、OBSERVABILITY_CERTIFICATE、SEPARATING_WORDS、ARITHMETIC_CERTIFICATE及边界/来源/manifest完整保留。

累计BRC_Heartbeat_phase_observable_stage86_20260926.bundle：55103012字节，SHA256dfa110d396eb5385f28886706ce76b6e02733afc20374902d97a374281afe734。Drive14jN6tLWjlUOnf0DnJT30u5KdU8w6PX8k已实际上传、读取元数据并取回原字节，本地cmp及SHA相同。
便携Shor_Phase_Observable_Stage86.zip：18574270字节，SHA256241b3e0fd071241548b711f8301d3aeb474addb604945842b56376d18b463f26。Python3.11+标准库，python -S -m stage86.run。
证明SHA25687d177e676785959867eed434f9f9c166ae64c965b6c39fa277357a59383cb4b；代码4cfeaf832b3a279a830f91aef78555e1aaceee486163fc688b4c2eda12d488a4；结果5b5f3dac59057fe3da11ca329f79b4cbf741c9c6f46347361e930ed1fad733a9。外部回执/mnt/data/heartbeat86/DELIVERY.json。

官方原作者摘要arXiv2403.12575（Grigoletto/Ticozzi）讨论结果分布保真的条件动力学降阶。可观察闭包、最小实现及区分词不是本轮一般首创；新增是冻结BRC族的十一量/三步证书、正纯态见证与Shor后对角控制验证。未读PDF全文，无独立审阅、Lean、实测物理或量子硬件。

NEXT: 加入跨逻辑标签的相干混合时，推广为带逻辑关联的算子矩，检查可显露的反对称/交叉关系；不把当前对角控制成功推广为任意Shor后续。父研究与活动准入未整体闭合。
