# 不交换代数操作与保正残差截断 v0.8

Progress-Event-ID: BRC-NONCOMMUTING-GRAM-ROUNDING-CCBF9335-20260928
Status: AUTHOR_DERIVED / FINITE_BRC_CERTIFICATES / UNREVIEWED / NOT_ADMITTED
Global-Read: cc76c431258e35d7ce71ef353401dbdf3c0e8b41
Source-Read: ad40761e2c801050b8203190a84daa453966e2a5
Parent: research_notes/BRC_PATH_RECOMBINATION_GRAM_CCBF9335_20260928.md at 0d13042c799fff617bafb040e203d9524400b5ee
Activity: RA-CCBF9335770F4460A2F947CFA000114F
Writer: EM-DIRECT-CCBF9335 / local-chat-brc-phase-ccbf9335770f4460a2f947cfa000114f（本对话本地逻辑标识，非平台认证）。

## 1. 模型修正与实际BRC

二维实保定向回路彼此交换，不能直接叫两个不交换回路。本轮继承W，明确另加代数逻辑相位V；没有证明V已由父实晶胞结点产生。对象为单个二维逻辑编码和有限相干出口，采用振幅/Born/张量桥，不改P000、六轴原生空间或物理时间。没有原生量子起源、正式准入或Shor加速宣称。

父ZIP实际SHA256607ed48efeda576195beb52a442aa4b3f05aae47b10b380c101576d7ff23e4ec。继承未改写phase_kernel.py、brc_linear.py、brc_qsqrt3.py；正权核心enterprise-math@643a098b7ae08a4fb88c1c8f4f7e65502a7904f2:src/enterprise_math/brc_weighted_recurrent.py，blob4e6b3132580e3cd70a20a0d8bd4d28792b961afb，SHA2567520822074b8f29e1c54f57b9543c043202db8bd7c6e27f3f1d6176028ac4a26。
新增四元系数表及Q[sqrt3,i]矩阵观察的非平凡系数乘加实际走Engine.paths/dot，公共尺度走normalize；零/单位/符号/指标为明确路由。正权路径与振幅相消分层，密度先匹配完整环境标签。截断保存整数积、商、余数和误差。没有三角函数、数值根或非BRC科学基线。

## 2. 不交换但四个有理系数闭合

s²=3,s>0；J=[[0,1],[-1,0]]，Z=diag(1,-1)。
E0=I，E1=sJ，E2=iZ，E3=E1E2。
E1²=-3I，E2²=-I，E3²=-3I；E1E2=E3，E2E3=E1，E3E1=3E2，反序均变号。
Φ(a,b,c,d)=aE0+bE1+cE2+dE3（四系数为实有理数）。
Φ†Φ=N I，N=a²+3b²+c²+3d²，N(xy)=N(x)N(y)。结合律及乘法表给准确四系数组合，不随字长增加基数。

W=(1/2,1/2,0,0)，V=(3/5,0,4/5,0)；都N=1。
WV=(3/10,3/10,2/5,2/5)，VW=(3/10,3/10,2/5,-2/5)；
WV-VW=(4/5)E3。I,W,V,WV的系数行列式4/25非零，
Tr(Eμ†Eν)=2wμδμν，w=(1,3,1,3)，所以准确线性操作张成维数为4。
这是忠实线性基的结论，不是所有表示的下界；固定代数域不能精确容纳任意Shor本原二进制单位根。

两个顺序相干汇合A±=(WV±VW)/2，效应分别13I/25、12I/25。
每个非零出口除以其代数平方根尺度后为幺正，按出口逆转恢复全输入及参考关联，不筛选任何出口。
一般两单位实四元操作x,y也有q±=(1±<x,y>_w)/2。并非只有交换操作才可纠正。
环境多Kraus或任意复路径系数不自动适用：I+iE2=diag(0,2)，效应diag(0,4)，不能一个标量归一成TP。

## 3. 完整跨出口Gram与独立串联

每个环境α、相干出口k的Kraus块为M(k,α)=sum r(k,α,μ)Eμ，r实有理。
C[(k,μ),(l,ν)]=sum_α r(k,α,μ)r(l,α,ν)是半正定实对称矩阵。
完整输出为sum C[(k,μ),(l,ν)] |k><l| tensor EμρEν†，对任意参考成立。
s个相干出口需(4s)×(4s)矩阵；出口已测为经典且不会再次相干汇合时才可仅留对角块。
每个M†M=N(r)I，故全仪器TP等价于sum_(k,μ)wμC[(k,μ),(k,μ)]=1。
不能访问已迹掉的环境，不能用单通道描述替代未知相干实现。

两个串联终端通道在环境新鲜独立时，C21=T(C2 tensor C1)T^T，T是E_aE_b的乘法表；完整环境Kraus展开即证。环境回流不适用。
实际核验直接四环境Kraus、Gram组合和完整Choi相等；反序不同。
完整四路径I,W,V,WV、四Hadamard出口、两环境分量已核验全Kraus、每出口完整Choi及一个跨出口Choi块。
只留出口对角块的反例：两完整输出(3I/5,4I/5)与(3I/5,-4I/5)各出口块相同，继续以首行(3/5,4/5)合并时首出口概率分别1与49/625。

## 4. 合法低精度：截因子，不直接截Gram

秩1 Gram [[1,3/5],[3/5,9/25]]按1/16网格向下截各元素得到[[1,9/16],[9/16,5/16]]，行列式-1/256。
数值变化小也会给不合法的非正通道，不能当物理残差。

对已给出的完整实四元因子r做dyadic截断得rhat；令Craw=rhat rhat^T，
τ=sum_(k,α)N(rhat(k,α,:))。τ>0时Chat=Craw/τ同时保持CP和TP。
只有一次全局归一，τ独立于未知输入，不按各出口或各输入后选择；τ0拒绝并精化或原值回退。
中间相干振幅必须保留公共代数尺度1/sqrtτ；密度层除以τ。
仅给稠密Gram时的因子构造成本不免费；一般复系数和非新鲜环境不在本简化合同内。

设原完整等距V，未归一截断Vhat。
δ²=sum_(k,α,μ) wμ(rhat-r)²，则(Vhat-V)†(Vhat-V)=δ²I，Vhat†Vhat=τI。
所以||Vhat-V||=δ，|sqrtτ-1|≤δ；Vtilde=Vhat/sqrtτ给||Vtilde-V||≤2δ。
任意参考输入的输出迹范数差≤4δ，任何测量总变差≤min(1,2δ)。
一般CPTP兼容阶段串联给TV≤min(1,2sum δ_j)，不清零旧账；后选择另计放大。
归一化差还满足准确式||Vtilde-V||²=2-2κ/sqrtτ，κ=sum w rhat r；本轮执行用δ的有理界，不称一般根比较已跑。

4路径×2环境共8四元组，每系数网格2^-b给δ²≤64·2^(-2b)。
实际三档：
b4，τ141/128，δ²281/3200，TV≤3/5；
b8，τ32747/32768，δ²243/819200，TV≤7/200；
b12，τ8380959/8388608，δ²263/209715200，TV≤9/4000。
TV阈值以4δ²≤limit²有理不等式核验；是当前有限单元的最坏上界，非测得误差、完整Shor成功率或最优精度。

## 5. 实际位长与扩张边界

V^n的非零系数为A_n/5^n、B_n/5^n，A_n+iB_n=(3+4i)^n。
模5有(3+4i)²≡3+4i，所以A_n≡3、B_n≡4，分母的5不能约去；展开位长至少随n线性增长。
实际n=1,2,4,8,16,32,64,128,257均检查；n257只需10次四元合并，但分母597bit。
账本最大分子/分母各1194bit，仅是本轮账本范围，不是所有核心临时变量上界。
短指数/DAG未被此下界排除，不能把其最终读出当免费。

q个逻辑编码的张量基有4^q个独立算子，一般Gram可有16^q量级条目；由内积张量分解证明，未运行大q枚举。
单编码闭合不等于一般Shor压缩，真实收益还需局部性、低秩或指定观察证明。

## 6. 执行、可重复物料和未完成项

最终check_v08.py193项通过；22365次实际正权调用、875尺度观察、23240条账本，104条欧几里得截断读出。
首次shell整段执行200秒超时，交互container返回StreamingExecNotEnabledContainerError；之后同一脚本按AST原语句顺序在有状态Python分段完成。
输出权限错误修复后检查内存已完成前沿再续写。超时尝试不计成功，无后台运行宣称。
交付ZIP解压后，从解压目录重新加载全部模块，以相同次序完整重跑，三文件逐字节一致：
RESULTS.json SHA256 cb2d73436edd3eefe070f14a21d701be90dba2e191909fb97d7ee23415389cea；
ROUNDING_RECEIPTS.json SHA256 1f01909aa04a75930f50668de4b72004b86dcf5274889860f5d05e99f5823578；
BRC_LEDGER.jsonl.gz SHA256 3f6fbdfd4be33be39533f435b8164b1aebf0dafdbd34a9af83fb3c5073813615。
静态指定调用/浮点字面量检查不是通用运行时沙箱。

包BRC_Noncommuting_Gram_Residual_v08_20260928.zip，403387字节；
SHA25692eac4b01a8d7a0eeebd4e63a6d23bc237fb987f18ff3aab5e1fbf7c5c97c645。
内含完整13795字节中文PROOF、实际源码、原核心、manifest、账本和失败/执行边界。
Drive上传及元数据读回ID1WVyXqX3AMUYMpRbrJ78-EDDdUg5C26Dn，父19dd_3frjJu-MeL-eD-UKuNYdCo5cTZXP，名称/大小/目录匹配；未云端重下载哈希复验。
https://drive.google.com/file/d/1WVyXqX3AMUYMpRbrJ78-EDDdUg5C26Dn/view?usp=drivesdk

未执行物理晶胞/Bell实验、原生V/Born桥、多比特性能、完整Shor/FFT比较、通用复系数近似或独立审核。
保留当前RA及原有贡献；本文件持久化不是独立数学准入，活动绑定另据实际读回。

## 7. 背景与下一单元

公开原作者摘要/落地页：Oi quant-ph/0303178；Kretschmann/Schlingemann/Werner 0710.2495及quant-ph/0605009。
只核读公开摘要和题录，未读完整PDF；相干通道、扩张连续性、四元数代数不认领一般理论优先权。
没有重提上一轮被平台阻止的专用写请求，公开资料不冒充专用结果。

下一单元：两个逻辑编码加入一个确切跨编码耦合，计算跨分割算子/Gram秩如何增长，
并给每阶段可执行的秩/误差预算；原生候选结点实现V的缺口保留。
