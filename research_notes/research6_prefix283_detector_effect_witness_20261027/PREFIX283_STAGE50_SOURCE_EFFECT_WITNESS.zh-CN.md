# PREFIX-283｜Stage50来源探测效应的可辨识判据及原生接口缺口

等级：AUTHOR_SIDE_EXACT_BRC_OBSERVER_PROOF / CONDITIONAL_DETECTOR / NATIVE_NOT_ADMITTED。本文是完整的模型内数学证明，不是物理探测器实验。

## 冻结来源与权限

本轮同一GLOBAL_KNOWLEDGE_V1当前规范快照为 awdawmip/chatgpt-global-knowledge@c2658a2945f4decaf267d7f75f70eda63e6740ea；已读规范入口、P000投影与原件、ACTIVE世界观及数学/代码/EM研究规程，P000原件Git Blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc 与投影声明一致。Enterprise Math输入为 awdawmip/enterprise-math@bf16665ae130258a99c8516298361152e618c308，已读 docs/PORTABLE_RESEARCH_PROTOCOL.md、docs/HEARTBEAT_BRC_ONLY_ARITHMETIC.md、机器运算约束、原生X6世界定义和PREFIX-282报告。

PREFIX-282的原始Stage50科学归档提交为318f47839d6bc7c850a3b7cc0fcb22d48febd9ba，已有40次原始Stage50 local运行，本轮只复用已核实的前序结果，**没有重新执行原始程序**。GitHub真实身份awdawmip，对仓库admin权限；原生em_control_tasks返回CONTROL_QUOTA，em_session_start返回STATIC_READONLY_SCOPE_DENIED（operation_sent=false）。原生活跃Owner/CLAIM无法核实，作者侧成果不冒充原生Result、Driver接纳或CLAIM。

## 研究问题及有类型BRC观察

保留三个来源标签 j=0,1,2，它们**不是X6六条空间轴**。固定C4高斯有理幅值路径包

$$f=(1,4,4),\quad g=(2,5,2),\quad Z_f=Z_g=33.$$

完整自相关恰好相等：C0=33，C1=20，C2=4，之后为0。前轮原始Stage50外Port在全部来源历史差r与C4 phase设置下不能区分，但软件函数packet_variance可以通过拆解完整输入packet，逐j执行pair_observer(field_packet({j:a_j}))计算来源对角分布。这一**输入可访问软件诊断**尚不能解释为单个已准备心跳后态上的外部物理仪器。

声明本轮形式有序来源路径对BRC效应语言：对任意高斯有理C4载荷a以及候选Hermitian系数E，定义

$$\mathcal B_E(a)=\frac{1}{Z(a)}\sum_{j=0}^{2}\sum_{k=0}^{2}\overline{a_j}E_{jk}a_k,\qquad Z(a)=\sum_j|a_j|^2.$$

这是带来源/相位/全有序路径对的静态BRC候选观察，不是普通矩阵传播器或真实model_law_id。仅在0≤E≤I时将该值解释为候选二元探测概率；其它Hermitian系数用于代数恒等式核验，不宣称概率有效。

## 定理A：全部Hermitian候选效应的严格辨识判据

载荷包差给出精确来源配对差矩阵

$$Q=ff^{\mathsf T}-gg^{\mathsf T}=
\begin{pmatrix}-3&-6&0\\-6&-9&6\\0&6&12\end{pmatrix}.$$

**定理：**对任意Hermitian E，

$$\boxed{\mathcal B_E(f)-\mathcal B_E(g)=
\frac{-3E_{00}-9E_{11}+12E_{22}-12\operatorname{Re}E_{01}+12\operatorname{Re}E_{12}}{33}.}\tag{1}$$

因而某个候选效应E辨识这两个包的**充要条件**是(1)的分子非零；在实向量空间Hermitian(3)中，不辨识系数为实余维1超平面。

**证明。** 对每个(j,k)的来源路径对执行BRC配对差。对角差分别为1²−2²=−3、4²−5²=−9、4²−2²=12。非对角乘积差依次为4−10=−6、4−4=0、16−10=6。由于输入载荷实值，(j,k)及(k,j)两项合成两倍系数实部。除以Z=33，直接得到(1)，不调用心跳传播或任何经典指数。证毕。

**推论：**一切Hermitian Toeplitz效应（E00=E11=E22，E01=E12）必然有零差，因为对角项的总系数为0，第一历史差项正负抵消，第二差项系数为0。这是Stage50自相关型外观察失辨的更一般线性证书。**不是**所有非Toeplitz效应都有辨识能力；例如E=diag(0,1,3/4)仍满足(1)零差。任何外部探测器能否实现一个不在该超平面上的效应，仍须Source证明。

## 定理B：二元来源对角探测的最优资源界

设存在一个真正可施于**同一个准备完成的状态**的来源对角二元候选效应E=diag(w0,w1,w2)，0≤wj≤1，则

$$\boxed{\Delta(w)=\frac{-w_0-3w_1+4w_2}{11},\qquad
\max_{0\leq w_j\leq1}|\Delta(w)|=\frac4{11}.}\tag{2}$$

**证明。** 由(1)消去非对角项得线性表达式。正系数总和为4，负系数绝对值总和为4，所以单位立方体上绝对值至多4/11。取w=(0,0,1)达到正最大值，取w=(1,1,0)达到负最大值。对第2来源的yes事件，两包条件概率为16/33与4/33；全标签来源分布为P_f=(1,16,16)/33、P_g=(4,25,4)/33，二者总变差

$$\frac12\left(\frac3{33}+\frac9{33}+\frac{12}{33}\right)=\boxed{\frac4{11}}.$$

在**这个条件性来源对角效应类**中，等先验下单次来源标签样本最佳判别成功率恰好为

$$\boxed{\frac12(1+\frac4{11})=\frac{15}{22}}.$$

它并非所有相干仪器的上界，也不是现实物理检测成功率。证毕。

## 已执行核验及范围

随稿verify_prefix283.py用Fraction高斯有理数/C4相位和全部**有序来源路径对**直接累计BRC观察。精确逐项核验19,683个Hermitian测试系数（对角及全部非对角实、虚系数从{-1,0,1}中选取），对243个Hermitian Toeplitz系数执行同谱核验，穷举8个二元来源对角mask并证明4/11最大，另核验4种全局C4相位×8个mask的32项协变性。PASS。以上有限验证的系数域明确，不替代一般解析证明；多数测试Hermitian系数未核查0≤E≤I，属于代数证据而非物理概率。无原始Stage50新执行；无原生心跳演化实验。

## Stage50源码类型审查与真正缺口

原始packet_variance在**输入分解**中为每个单来源重新生成field_packet并计算pair_observer。它是已经可运行的源码诊断，而不是已经证实的后态探测器。原始local(packet,r,phase)更改的是**输入准备**条件及外PortBRC观察；phase不是同一H_n的来源局部相位演化门。r是来源历史差，不是心跳序号；three_masks是材料Port遮罩而非来源检测门。不能用源代码可访问a_j的事实偷换外部可以测出a_j。

若要在真实心跳世界实现定理B，需有完整Source支持的Cell/X6空间地址、Port、场/材料动量、来源与边界、独立时间、model_law_id；还需定义**作用于单个准备后完整态**的Detector/Port效应、来源选择响应、BRC有序配对归一化及测量后态/损耗规则，并给出原生-形式效果保真证据。目前不能确认这一接口存在，也不宣称不存在任何其它合法原生Detector。

## 后继PREFIX-284

以实际Source定义的合法探测器为对象，确定每个E的(1)式对比是否非零；若没有合法来源分辨接口，只在明确的Stage50外Port及其他已证有效操作的闭包中给出不可辨识证书。取得完整类型化X6 Cell、Port、材料动量、全场、来源、边界、C4相位、独立心跳与model_law_id，再判断是否可以把本轮形式定理连接到真实系统。

Research-Activity-ID: RA-R6P283-20261027-0816（本轮本地标记/作者侧登记，非原生身份或CLAIM）。
