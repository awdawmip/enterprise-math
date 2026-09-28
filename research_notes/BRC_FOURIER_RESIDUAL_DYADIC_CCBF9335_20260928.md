# BRC 代数框架与残差傅里叶：低位观察降尺度

Progress-Event-ID: BRC-FOURIER-RESIDUAL-DYADIC-CCBF9335-20260928
Date: 2026-09-28
Status: AUTHOR_DERIVED / FINITE_BRC_CERTIFICATES / UNREVIEWED / NOT_ADMITTED
Global-Read: d597dc8ec9a9e919635f077c57736cfc53924eea
Source-Read: 8da793f7680e326f6078d50913d91c90917d6614
Parent: research_notes/BRC_SHOR_ALGEBRAIC_REDERIVATION_CCBF9335_20260928.md
Identity: EM-DIRECT-CCBF9335 / RA-CCBF9335770F4460A2F947CFA000114F / local-chat-brc-phase-ccbf9335770f4460a2f947cfa000114f（本地逻辑标识，非平台认证身份）。

用户要求进一步统一步进、相位和旋转为代数加残差，判断前期投入是否可摊销及BRC Fourier是否成为加速因素。本轮证明指定操作字和指定观察可以免展开；未证明完整经典Shor采样多项式化。维数和操作标签是有限振幅模型，不改变P000、心跳世界或原生几何；没有新物理对应。

## 1. 实际BRC接口与精确正规形

继承v0.2的正相位路径半环，保留完整工作标签、端口、非负路径权重、指数modQ、公共尺度和来源。字符chi(sum h_e[e])=sum h_e u^e保持并联与串联；相消是观察，不是正质量删除。

未改写核心：enterprise-math@643a098b7ae08a4fb88c1c8f4f7e65502a7904f2:src/enterprise_math/brc_weighted_recurrent.py；blob4e6b3132580e3cd70a20a0d8bd4d28792b961afb；SHA2567520822074b8f29e1c54f57b9543c043202db8bd7c6e27f3f1d6176028ac4a26。继承phase_kernel.Engine和v0.2 Cyclotomic类。新系数乘加调用真实BRC有符号覆盖；工作模乘是BRC正乘积之后的Euclidean-remainder观察，保存积、商和余数。整数指数/端口/正规形运算是有对应证明的标签路由。未计算三角函数、pi或数值单位根，亦未执行经典三角基线。

Q=2^m>=4，u为v0.2固定嵌入的本原Q次根。T_s|x>=|x+s modQ>，Z_t|x>=u^(tx)|x>，F|x>=Q^-1/2 sum_y u^(xy)|y>。逐基向量与有限几何和证明：

Z_t T_s=u^(ts)T_s Z_t；F T_s F^-1=Z_s；F Z_t F^-1=T_-t；F²|x>=|-x>；F⁴=I。

任意该生成族单一路径字有正规形G(k,s,t,j)=u^k T_s Z_t F^j，k,s,t modQ，j mod4。W(k,s,t)W(k',s',t')=W(k+k'+t s',s+s',t+t')；Fourier共轭phi(k,s,t)=(k-st,-t,s)，所以G1G2=W1 phi^j1(W2)F^(j1+j2)。每次合并固定数量的O(logQ)位整数操作；显式L字需O(L)读取与合并，同一编译字重复n次可O(logn)合并。非交换项ts'不能因它看似全局相位就在受控分支相遇前丢掉。

Q=2^40，G(k17,s13,t19,j1)重复10^12+39次，本轮实际56次标签合并。此项只编译算子描述，不是56步完成状态模拟、测量或因数分解。一般代数旋转不自动属于这四字段族；“有代数表示”不等于残差小或可快速读出。

## 2. 精确残差组合与增长位置

U_i=G_i(I+R_i)，Rtilde_2=G1^-1 R2 G1，则

U2U1=G2G1[I+R1+Rtilde_2+Rtilde_2 R1]。

这是结合律的直接展开；本轮实际检查一组有理残差算子，包含交叉项时相等，删去交叉项时不相等。该测试算子不宣称为量子酉门。

若R由k个Weyl项组成，Fourier共轭逐项重标记及移位系数相位，不增加Weyl支持数；残差乘法却最多产生k1*k2项。短DAG、低秩和区间原子是可选载体，均需自己的未来观察保真。主要待控费用是非结构化相乘、工作标签相遇、系数位长和最终查询，不是每经过一次F都必须展开完整幅度表。

## 3. 模幂步进的边界残差及严格观察范围

工作群上M_b表示乘b，U_f|x,w>=|x,w a^x>。0<=s<Q，P_s投影到x>=Q-s，P_0=0。指数差s-Q floor((x+s)/Q)逐基向量证明

U_f(T_s tensor I)U_f^-1=(T_s tensor M_(a^s))[I+P_s tensor(M_(a^-Q)-I)]。

不需要已知阶r。单步残差只占一个指数切片，不表示整个联合算子秩1或范数小。若a^Q!=1，均匀图态上的单次s步bulk误差平方是2s/Q；没有允许把它当永久零。

N21,a2,Q512：a^Q=4、a^-Q=16；回绕乘数2*16=11，末端工作标签2乘11归1，漏回绕乘2得到4。完整循环后的bulk差是全局工作重标记，单独第一寄存器终测对此不可见；本例只证明相应联合/工作/未来观察不能无条件删进位，不单独证明Shor概率受损。

直接概率反例：第5节最低两位中h3应有权重4-3=1；擅自换成4会使b2的结果(4-4-4)/16=-1/4，正确值则为1/8。有限窗口重数不能随意改成循环无边界重数。

## 4. 不输入r的低位Fourier降尺度恒等式

gcd(a,N)=1，Q=2^m，d=2^k|Q，M=Q/d，g=a^M modN，zeta_d=u^M。P_k(b)=Pr[c mod d=b]观察整数c的最低k位，不是最高位/连续频率区间。原始联合字符概率为

P_Q(c)=Q^-2 sum_(x,x':a^x=a^x') u^(c(x-x'))。

先对c=b+d j求和，字符正交sum_(j=0)^(M-1)u^(dj(x-x'))=M*1_(M divides x-x')。因此

P_k(b)=1/(Qd) sum_(x congruent x' modM, a^x=a^x')u^(b(x-x'))。

再写x=j+My，x'=j+My'。a可逆使工作相等条件成为g^y=g^y'，M个j的和完全相同，归一化后得到

P_k(b)=1/d² sum_(0<=y,y'<d,g^y=g^y')zeta_d^(b(y-y'))。

按正负距离分组，有精确式

P_k(b)=[d+sum_(h=1)^(d-1)(d-h)*1_(g^h=1)*(zeta_d^(bh)+zeta_d^(-bh))]/d²。 (A)

所以Q点完整频谱的此项边缘分布，恰好等于底数g、长度d的同型问题。来源方向的消去有字符正交和归一化证明，不是把不同工作标签相消。未知阶r不在程序输入中。

g需O(logQ)模乘，候选返回掩码可逐步用d-1次模乘建立；单b的(A)只有d-1个候选距离。代数比较、所有b的计算、完整采样和输入位长不是免费。这是指定局部观察的真实结构化缩减，不是完整Shor的复杂度结论。

## 5. 逐位观察恰是主项一半加有符号残差

下一层g'=a^(Q/(2d))，g'^2=g，zeta_(2d)^2=zeta_d。将(A)的偶h/奇h分开，偶项严格给父项一半，奇项在b与b+d之间翻号，故

P_(k+1)(b+beta d)=P_k(b)/2+(-1)^beta R_k(b)，beta=0,1；                 (B)

R_k(b)=1/(4d²) sum_(1<=h<2d,h odd)(2d-h)*1_(g'^h=1)
                  *(zeta_(2d)^(bh)+zeta_(2d)^(-bh))。                  (C)

父概率p=P_k(b)>0时，条件概率是1/2+(-1)^beta R_k(b)/p。p=0不可达前缀禁止相除。子概率非负蕴含|R_k(b)|<=p/2。R是精确结构差额，不假定小；根塔、模幂塔及返回来源必须保留，单个p并非完整未来状态。

若|p-p_hat|<=eta_p<p，|R-R_hat|<=eta_R，则条件概率误差<= (eta_R+eta_p/2)/(p-eta_p)。这是用|R|<=p/2展开比值直接得到。阈值比较可按需要精化代数区间，但本轮未实现采样器；罕见前缀的除法会放大绝对误差，不能统一当作低精度无害。逐步条件误差的合成仍需预算，不清零既有研究误差。

令R=ord_N(g)。若R>=d，所有1<=h<d无返回，P_k(b)=1/d精确均匀。若原阶r=2^v r_odd，k<=m-v，则R=r_odd，故2^k<=r_odd范围有此盲区。r仅用于分析，不作为运行输入。这个特定观察盲区不是所有经典算法下界。

N21,a2,Q512：P1=(1/2,1/2)，P2=(3/8,1/4,1/8,1/4)；R1(0)=1/8，R1(1)=0。给定最低位0下一位0概率3/4，给定最低位1则1/2。
N21,a2,Q=2^40：实际直接计算最低两位同一分布，仅57条本次BRC/尺度账本记录；未枚举2^40状态或完整40位输出。
N77,a2,Q8192：最低1、2、3位均匀，第四位开始非均匀；由模返回掩码实际取得，不提供阶输入。廉价均匀前缀不等于已获得有用周期样本。

## 6. 实际证书、物料和未完成项

check_v03.py本轮213项作者检查通过，其中符号标签测试与真实振幅检查分开；4209次实际正权BRC调用、297次公共尺度观察、306次模余数观察。新原始参考只在N7/a2/Q8、N21/a2/Q16做同一BRC字符的完整联合双路径求和，逐项核对d2、4、8所有低位输出与概率总和。Q8的64个端点验证F-Weyl对应；另验证残差交叉项、二进制精化、盲前缀和边界反例。

从交付ZIP重新解压执行，RESULTS.json、BRC_LEDGER.jsonl.gz、CYCLOTOMIC_OPERATIONS.json.gz、ROUTING_AND_MODULAR_RECEIPTS.json全部逐字节相同。静态指定函数名扫描未见sin/cos/tan/exp/sqrt等调用；不是通用运行时沙箱。

完整证明、源码、原核心、manifest及账本：BRC_Algebraic_Residual_Fourier_v03_20260928.zip，103451字节，SHA256333056f0c9320f41393eefe3ff83948999604050428a04f70ce1f7afcbf93de7。
Google Drive上传并元数据读回：11pB30NXiM40pAyJIIV74oOjhitQuC6AV；父目录19dd_3frjJu-MeL-eD-UKuNYdCo5cTZXP；名称、大小和目录相符。未宣称云端重新下载哈希校验。
https://drive.google.com/file/d/11pB30NXiM40pAyJIIV74oOjhitQuC6AV/view?usp=drivesdk

未执行未知阶完整条件采样、代数区间抽样器、端到端分解、相对FFT的性能比较、Lean或独立审核。逐层d翻倍至Q的成本仍可能O(Q)或更大。前期预计算只能在相同有效范围内摊销：通用操作框架可复用，换N/a后的返回掩码不能免费复用。

当前活动记录已实际读回，但checkpoint数组仍空；本文Source/Drive保全不等于原生activity checkpoint/guard闭环。没有新增Task、CLAIM、run、Result、数学接纳或排程修改。

## 7. 文献状态与下一单元

公开主来源：Gottesman arXiv:quant-ph/9807006；Van den Nest arXiv:1201.4867（QIC13,2013,1007–1037）；Griffiths–Niu arXiv:quant-ph/9511007（PRL76,1996,3228）。本轮查到并阅读公开题录/摘要，不冒称读完PDF或重算论文。上述算子演算、normalizer和半经典QFT有既有文献基础，不作优先权认领。

专用缓存PQ-20260927-KQB2556-SCHOLAR-HEISENBERG及其实际raw已恢复读取；外层FAILED、子项PARTIAL、记录CONFLICT及1998/1999两条同研究题录保持，不伪报新专用查询或完整原文。公开arXiv信息另作核对。

下一具体问题：为(C)的未知奇返回距离建立不逐个扫描全部候选的有证书块摘要，或实现随机阈值驱动的代数区间精化；按实际模乘数、残差项、位长、回退率及有用恢复事件比较。不要重复v0.2等价推导或把本轮群关系当成新发现。
