# Heartbeat92 — 整轮重合读取、按结果构造后态与流式 Shor 精确验收

Progress-Event-ID: HEARTBEAT92-COLLISION-CONTRACTED-READER-20260926
Status: AUTHOR_DERIVATION_AND_EXECUTION / SHARED_CONTEXT / UNREVIEWED / NOT_ADMITTED
Global read: 82668746051d36b0549abf5dc67ba88c50f3f14d
Source read: 3f9c3ff9a06a26ed37d37a59c0e09c5750a3ba87
Publication preflight: 3d7e2a4bf2f19d8fea2809bf614bd2eecf6a69ad
Research-Activity-ID: 未取得。继承本对话本地来源HB90-0de6b47ad07848a1b6e8347fd5156ca6，本轮run为HB92-62510e7f604746cc80ab99617134f0a4；不是平台或服务会话。旧登记拒绝只有历史报告，不重放、不换身份绕过，不借用他人CLAIM。可移植研究保存不是数学准入。

## 1. 实际继承与新单元

父累计f1e229edbf35cef3fb4c6a322194e6b87ba6ae94；父bundle为80743613字节、SHA256 56d035784882ab847ac29c278a44564792afaa3461d757f6f574ae7a97ef9887，先核后本地克隆。1802个父文件逐Git blob原字节不改；独立Stage76引用保留。12组冻结输入、真实phase3=旧phase4字执行两次、其余相位、CF-only、失败样本、工作标签与完整61模式保持。P000六原生轴、独立时间、BRC-only及残差保真不变。二次概率、QFT靶点及外部条件均匀随机接口仍为BORROWED_REFERENCE。

复用EM-DIRECT-0C08F0已有流式整轮恒等式、Stage89共同生成器、Stage91按需置换。新增是可执行的整轮收缩：在构造两个孩子之前读取完整场的交叉量，真实抽样后只物化选中的完整后态。不是重新宣称发现Hadamard test，不是将原相位替换成理想矩阵。

## 2. 当前读数的精确充分关系

给定真实历史h和深度i，原顺序的内部相位为T_(i,h)，工作置换M_i按输入重复平方取得；U=M_i tensor T严格正交。原H4/控制/U/H4/读出轮的两个未归一化孩子为v_r=(v+(-1)^r Uv)/2。

令m=<v,v>，gamma=<v,Uv>，则孩子质量m_r=(m+(-1)^r gamma)/2；m>0时p0=(m+gamma)/(2m)。零父态只保留零分支，不归一化。真实spectator回零由两H4推出，不是重置。

按完整工作标签写v=sum_y |y>v_y，S为非零工作支持，sigma为按需全域双射。只有C=S intersect sigma(S)参与gamma=sum_(y in C)<v_y,T v_(sigma^-1(y))>，内部dot保留全部61分量及符号。C空则当前读数严格各半，两个孩子支持为S union sigma(S)；C非空仍可因符号抵消得到gamma=0。令q=sum_C||v_y||²、q'=sum_C||(Uv)_y||²，则gamma²<=q q'，概率偏置不超过sqrt(q q')/(2m)。平方根只在证明中，实际核验平方有理关系。

两口和差矩阵通过继承rational_matrix_columns的实际BRC符号覆盖核验；范数与完整匹配dot采用继承正路径及符号观察的双线性扩展。六个真实N21前缀又逐项调用BRC配对对照。不把正支路总质量当有符号振幅，不跨工作标签合流。

## 3. 当前读取量不是后续状态：一个精确见证

同一N15/a2/t4的最后两轮接口、history=(0,0)，工作乘数依次4、2。取r=e0+e1及合法单位输入v_±=(|1>r ± |2>r)/2。M4将{1,2}映到{4,8}，两份输入当前m=1、gamma=0、p0=1/2。

条件于先读0，完整未归一化后态分别为w_+=(|1>+|2>+|4>+|8>)r/4及w_-=(|1>-|2>+|4>-|8>)r/4。M2使前者不变、后者反号，下一位p0分别1和0。原始两步事件第一份P00=1/2，第二份P00=0、P01=1/2。两份均与原完整H4仪器逐后态核验。

这是相同认证接口上的合法准备，不声称标准初态会自行产生这两份边界。它否定只保留(m,gamma)就能预测全部未来；当前读取器仍保存v和Uv，抽样后继续保留完整选中孩子。

## 4. 真正实现的调度及边界

prepare_round先生成完整Uv并算p0，此时没有孩子数组。choose成功返回r后，才构造(v+(-1)^r Uv)/2。随机带耗尽时保存本轮以前的真实状态和历史，不构造任何孩子，不默认返回0或1。全叶验证器可请求两个孩子，生产sample只构造一个。

原始整数v=n/d、Uv=k/e下，A=sum n²、R=sum_matched n*k，p0=(A e+R d)/(2 A e)。d,e为二幂，选中孩子对齐q=max(d,e)，分母2q，再用原规范约去；不用概率平方根，不把分母相乘，不删除尾项。

原展开H4将一工作行复制到四个active/spectator标签，active=1的两份spectator行重复执行相同内部相位。本轮利用已有整轮恒等式只计算一次。物理H4和实际根门没有从协议删除；相位3仍实际调用共同根两次，其他相位不调序。仅在原轮边界声明等价，中途新增干预需展开或另证。

当前实现计算完整Uv，不声称已经只为碰撞行求相位。输入、Uv、选中孩子可能同时驻留，单状态快照减小不等于总RAM减半。新sampler是实际新代码；原CF后处理及有限factor_attempts代码对象保持。原modules/globals/父文件不变。

## 5. 实际结果

12组冻结Shor全叶运行，3432个孩子逐原幅度/分母与Stage91完整H4流程比较，所有条件概率、零历史、层质量、终端概率、规范分母、尾项和完整61模式hash相同。读取冻结CASE在候选运行后，未将阶/因数/目标分布输入运行器。全部前缀质量等于对应终端叶质量和；CF/gcd成功及失败相同，dense/eager表misses均0。

N21/a2/t10：新最大单状态快照6端点/366实槽，旧12/732；N35/a2/t6为12/732对旧24/1464。N21/t10全叶literal-root-row代数求值27624->13812，phase-row24564->12282，不是BRC调用数或物理门数。1023个正前缀中513个工作支持不交，另8个有交集但gamma为0。最终规范分母仍5409bit，P128=1/131072、成功权重约0.330843218193906427及原理想Shor界3699/68719476736原样保持。新表示误差0不取消原相位近似。

四组seed单轨迹与旧驱动全部events/CF相同，每个完成轮次只物化一个孩子。其中两组未取得因数，保留失败。N21/t10 seed9026得到k171、3与7，十轮构造十个孩子。空随机带零孩子、完整可恢复状态相同；底数耗尽、重试上限、偶数/gcd预检均保持。固定seed不作随机频率证明。

## 6. 运行与产物

355项命名检查、1299次实际不变规范BRC调用；3432个孩子比较不是独立实验数。规范核心bc7babbb9e890f6d5a7094430a5fbdccf66c77ad:src/enterprise_math/brc_weighted_recurrent.py，SHA256 7520822074b8f29e1c54f57b9543c043202db8bd7c6e27f3f1d6176028ac4a26。

累计868ebb6f499fcc9af22a8ee97fa752ef9e8cc65f；START_HERE_STAGE92.md；stage92/PROOF.md、collision_reader.py、run.py、sample.py、RESULTS、12CONTRACTED_CASE、COLLISION_CERTIFICATE、DRIVER_REPLAY、ARITHMETIC_CERTIFICATE及边界/来源/manifest。原62781667331ns，最终bundle新克隆62438933347ns；仅递归排除elapsed_ns，RESULTS及15gzip科学内容全同，2gzip字节同，其余实际计时原件保留。1802父文件、27manifest、fsck和两工作树干净核验。便携独立解压/新增字节/完整seed CLI与原CLI文件字节相同；未作第三次全叶重放。

bundle BRC_Heartbeat_collision_reader_stage92_20260926.bundle：82515243字节，SHA256 8e8e332d6b7b138299bce4557b4dfd4f3e74ad9dcc3515a17aef5ef787088078。Drive 1c_7wK6AndPAvbTdkZPYyUGjgiMbp772o已上传、metadata读取、完整原字节返回并cmp/SHA一致。
ZIP Shor_Collision_Reader_Stage92.zip：48085549字节，SHA256 f7c955fb14af849ccabff281c6d533386590ed07404ca5d47ebc55744649b376。Python3.11+标准库：python -S -m stage92.run；python -S -m stage92.sample --N 21 --bits 10 --base 2 --attempts 8 --cache 16 --seed 9026。
证明SHA256 5b52a025fe7c4d6b751eb419e9f0e6685c8870548907612595b27e6e65df6b2c；代码d912f93f61327e27757d2e9c4b89efa19529118e9961f1ad23a89aeb62f17f42；结果acb6defab00fd1688a79af12d937fae1be46eb63cb87e8077acbddcb95a2405f。外部回执/mnt/data/heartbeat92/DELIVERY.json。

已有背景为Hadamard受控重合读取和半经典QFT；仅使用Griffiths/Niu quant-ph/9511007及Patti等2206.14999官方摘要，不宣称一般首创、PDF全文、独立审阅、Lean、物理拟合、Born推导、量子硬件或速度优势。

## Next及并行前沿

在同一终端合同中研究碰撞行的相位预求与选中后态的其余按需完成；当前完整Uv实现保留，需另给保真与实际成本证书。不能将当前p0=1/2当成删场许可。真正工作支持和整数位长仍未被消除。

发布前消费Source 3d7e2a4bf2f19d8fea2809bf614bd2eecf6a69ad中C6438C的next_cf_only/HANDOFF.md与next_distribution/HANDOFF.md，仅为其他作者的已有前沿和范围，不计本轮执行/独立审查。其K33原CF全位宽成功与固定截断分布边界，未自动绑定到本共同根变体；当前低bit冻结合同不变。所有并行活动/源文件不改。父研究及数学准入未整体完成。
