# 局部晶胞散射、环境记录秩与纠缠寿命 v0.5

Progress-Event-ID: BRC-CELL-SCATTERING-GRAM-CCBF9335-20260928
Status: AUTHOR_DERIVED / FINITE_BRC_CERTIFICATES / UNREVIEWED / NOT_ADMITTED
Global-Read: 376c3971436206603f5bb08499ff5b27476669e1
Source-Read: a15163b4a36de6053d9bea0a15e8431c37e6e551
Parent: enterprise-math@5ab8f126f089dc9c7136284866bf6b98f6196d9f:research_notes/BRC_CELL_RESIDUAL_ENTANGLEMENT_CCBF9335_20260928.md
Activity: RA-CCBF9335770F4460A2F947CFA000114F
Writer: EM-DIRECT-CCBF9335 / local-chat-brc-phase-ccbf9335770f4460a2f947cfa000114f (local logical identity, not platform authentication).

## 1. 局部整数散射，而非独立猜测K/L

六轴相对坐标中，端口i从o-E_i经一步+E_i到中心o，输出j再经一步+E_j到o+E_j。两跳均只改变一个原生坐标；不把复合路径当原生斜线。本候选将六端口分(1,2,3)、(4,5,6)两组，每组与一个同晶胞环境模式碰撞。端口不是力，未假定原生三力闭合；分组、耦合、振幅内积和Born/张量读出是额外模型选择，不是P000定理。

取非零整数g=(g1,g2,g3)、c，s=g^Tg，w=(g,-c)，H=I-2ww^T/(s+c²)。由(ww^T)²=(s+c²)ww^T得H^T H=H²=I。环境初始为零，抽取
K_g=I-2gg^T/(s+c²)，L_g=2c g^T/(s+c²)。
因此K_g^T K_g+L_g^T L_g=I。P_g=gg^T/s，D_g=I-P_g，q=(c²-s)/(c²+s)，有K_g=D_g+qP_g、K_g^n=D_g+q^nP_g。g=(1,1,1)、c3时导出v0.4的K=I-J/6、L=(1,1,1)/2，而非将这两个接口输入程序。

H²=I还给出记忆反例：同一环境保留并准确再次作用H时，两步恢复完整初态；每步换新环境时系统保留K²。e1输入的两步新环境权重11/16，而同一环境回到1。不可逆损耗依赖排出/更新/不回流合同，不是离散性单独推出。两种过程均实际BRC检查。

## 2. 不平衡与新增出口必须分开

固定g、没有额外旋转混合时，ker g^T是二维永久无损空间。静态权重不等通常改变保护方向，不会仅因不等消灭秩1出口的二维核。g=(1,1,2)、c3给q1/5、L=(2,2,4)/5：旧向量(1,0,-1)损失4/25（输入权重2），新向量(2,0,-1)永久保留。上述有理证书已执行。

一般令l_i为完整环境输出列，G=L^†L，G_ij=<l_i,l_j>。G_ii是基端口吸收权重，非对角还记录环境重叠。若K=(I-G)^(1/2)，0<=G<=I，则kerG由K原样保持，永久无损维数=3-rankL。对带额外混合的一般K，这只是瞬时核；仍须用intersection ker(LK^j)检查未来。环境等距换基不改变G。

不能保持旧K却把共同L换成I/2：v=(1,-1,0)被保留权重2，又排出1/2，总计5/2>2。本轮实际验证这一不合法“只换记录标签”的反例。环境区别必须在完整等距映射中实现。

## 3. 同基端口损耗的重叠参数族

取0<=mu<=1，环境单位记录e_i=sqrt(mu)e_common+sqrt(1-mu)e_private,i；l_i=e_i/2。所有根取非负代数根，只作符号证明。于是
G_mu=[(1-mu)I+mu J]/4，P=J/3，D=I-P，
K_mu=bP+dD，b=sqrt(3-2mu)/2，d=sqrt(3+mu)/2。

K_mu²+G_mu=I；每个G_ii=1/4且trG=3/4相同。此处只固定基端口/等权经典混合的损耗，不固定任意相干输入的损耗。mu1时d1，差分面永久保留；mu<1时G正定、d<1，全部单激发残差最终流出。只新增一个私有通道未必杀掉整个核，本参数族是三个私有记录都出现。

归一化差分输入p_n=[(3+mu)/4]^n。令eps=1-mu>0，x=eps/4，有限乘积直接给1-nx <= (1-x)^n <= 1/(1+nx)。所以半寿命步数量级为1/eps，而非把近乎共同记录等同完全永久保护。n是碰撞次数，未校准物理心跳时间。

## 4. 没有永久暗核，仍可有有限时纠缠

真空/单激发的通道取A0=diag(1,K_mu)、A_alpha=|vac><l_alpha|；完备性来自上式，可扩展为完整CPTP模型。mu0可用三个独立局部振幅阻尼实现同一受限作用。

从可分|100>开始，每步使用新环境，n步保留向量为v_n=(x_n,y_n,y_n)，x_n=(b^n+2d^n)/3，y_n=(b^n-d^n)/3。无条件态包含真空权重1-||v_n||²，不做后选择。迹掉C后，AB基00,01,10,11中的密度为
[[A,0,0,0],[0,y²,xy,0],[0,xy,x²,0],[0,0,0,0]]，A=1-x²-y²。
偏转置的00/11主子式为-(xy)²。0<mu<=1、有限n>=1给x>0、y<0，故纠缠；mu0给y0及显式可分混合。mu<1时b,d<1，最终趋真空，但每个有限正n仍可NPT。永久保留不是纠缠生成的必要条件。

负性N_n=[sqrt(A²+4x²y²)-A]/2。n>=1有A>=1/4、|xy|<=d^(2n)/3，所以N_n<=4d^(4n)/9；mu<1时趋零。mu1极限负性2(sqrt2-1)/9。代数根未作数值计算。

全有理实例mu=37/121：b17/22、d10/11，K对角19/22、非对角-1/22。L的两个共同行为(6,6,6)/22、(1,1,1)/22；每个端口再有私有8/22、4/22、2/22三行，共11行。Gram对角1/4、非对角37/484，完备性实际BRC验证。

e1输出保留(19,-1,-1)/22、排出1/4；AB无条件密度
(1/484)[[122,0,0,0],[0,1,-19,0],[0,-19,361,0],[0,0,0,0]]。
偏转置主子式-361/234256，在(1,0,0,4)/sqrt17上见证-15/4114。加入delta I/4白噪声，此固定见证在delta<30/2087仍为负，是充分条件而非纠缠阈值充要判据。完全哪路径退相干保人口却给对角可分混合。

## 5. 实际执行与交付

继承未改写phase_kernel.Engine及正权核心enterprise-math@643a098b7ae08a4fb88c1c8f4f7e65502a7904f2:src/enterprise_math/brc_weighted_recurrent.py；blob4e6b3132580e3cd70a20a0d8bd4d28792b961afb；SHA2567520822074b8f29e1c54f57b9543c043202db8bd7c6e27f3f1d6176028ac4a26。有理算子逐路径有符号覆盖对应，正质量不被当振幅相消；密度先匹配环境标签再求和。系数乘加经真实Engine.paths/dot，公共尺度经normalize。独立端点使用明确块对角密度商。没有三角/数值根/普通传播器参考。

check_v05.py通过42项数学/接口检查：220次正权核心调用、40次尺度观察，共260条账本。另有36对原生轴路由/72跳标签检查，其中18对在所选同组三端口内。ZIP解压再运行后RESULTS.json、BRC_LEDGER.jsonl.gz逐字节一致。静态函数名扫描不是通用运行时沙箱。

包BRC_Cell_Scattering_Gram_v05_20260928.zip：31604字节，SHA25698b1971b027d48fda87ecd123a085c93a18e08f8d72a944240de98579c2d4dd5。
完整中文PROOF.md：12519字节，SHA256608c56770fa716e365804752b41ea8055328045a458eaceaed2cd252a2754b44。
脚本SHA2567f654be2b818f8d50656a915998b417694ead2f086e1df20ffc9868793181fc9。
RESULTS.json SHA256b0b2fbfd9e369207f866ad0b6ff1fbec8e1b8e5f03f27e7c252ca26b48336a24。
Drive实际上传并元数据回读：1pkhPSX6H-IEWFQqtmm9OVXTsZhNG-YPd，父目录19dd_3frjJu-MeL-eD-UKuNYdCo5cTZXP，名称/大小/目录匹配；未云端下载验哈希。

本轮未做一般mu数值扫描、物理晶胞实验、全晶格动力学校准、Bell实验、Lean、独立审查或完整Shor性能实验。三端口微观规则仍是候选，不是P000唯一推导。已有RA记录已读回；原生activity checkpoint/guard状态与本文件的科学证据持久化分别处理，不由本文自我宣称成功。

## 6. 先行研究和续接

官方题录/摘要核读：Lidar/Chuang/Whaley PRL81.2594(1998), arXiv:quant-ph/9807004；Peres PRL77.1413(1996), arXiv:quant-ph/9604005；Verstraete/Wolf/Cirac Nature Physics5,633(2009), doi:10.1038/nphys1342。无退相干空间、偏转置判据、耗散态制备属于已有方法，不认领优先权；本轮未读整篇PDF。保留上一轮专用Issue2571的FAILED/PARTIAL及相关性冲突，不重新查询同一条件、不把其结果当文献证据。

下一单元：邻近结点g(x)改变时，构造保持保护方向的局部输运，并对微弱私有环境记录给整条路径的回拉出口Gram界。区分静态方向漂移、真正增秩泄漏和环境回流。固定低秩接口可预编译后只推进少量耗散因子，但准确系数位长及任意联合态/Shor工作关系并不免费。
