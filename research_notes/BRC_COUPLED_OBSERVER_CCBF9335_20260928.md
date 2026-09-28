# 双编码耦合、观察者闭合与合法低精度 v0.9

Progress-Event-ID: BRC-COUPLED-OBSERVER-CCBF9335-20260928
Status: AUTHOR_DERIVED / FINITE_BRC_CHECKS / UNREVIEWED / NOT_ADMITTED
Global-Read: 3b3374b982911636012023a795d93cca8cd3675b
Source-Read: 7136f8a40bdbbdb082d1ded73dcf063bd6219643
Activity: RA-CCBF9335770F4460A2F947CFA000114F
Writer: EM-DIRECT-CCBF9335 / local-chat-brc-phase-ccbf9335770f4460a2f947cfa000114f（本地逻辑标识，不是平台认证）。

## 来源分叉与范围

执行父本是本对话附件BRC_Noncommuting_Closure_v08_20260928.zip（107项版），128418字节，实际SHA256 e5020abd45081450d0bf40dc90ba015fd29b219b6b15593198ef2417a9f3990c。另实际消费远端193项、四元因子舍入版：enterprise-math@4a2d966c12068a1bd40eea96c0e1ccfb8b337ff6:research_notes/BRC_NONCOMMUTING_GRAM_ROUNDING_CCBF9335_20260928.md，blob599df757c5b52138dc85f839e761f10e60b13203。两者不是同字节版本，不覆盖或混报测试；本轮张量反例检验远端单编码标量范数合同的适用边界。

沿用振幅/Born/张量/新环境合同，不将逻辑耦合称为P000唯一动力学；没有物理时间、原生量子起源、正式准入或完整Shor加速结论。未改P000、Task、CLAIM或排程。

原正权BRC核心未改写：enterprise-math@643a098b7ae08a4fb88c1c8f4f7e65502a7904f2:src/enterprise_math/brc_weighted_recurrent.py；blob4e6b3132580e3cd70a20a0d8bd4d28792b961afb；SHA2567520822074b8f29e1c54f57b9543c043202db8bd7c6e27f3f1d6176028ac4a26。继承phase_kernel/brc_linear/brc_qsqrt3；新observer_kernel的非平凡系数乘加实际调用paths/dot，公共尺度调用normalize。环境标签配对后求密度；正质量不是相消振幅。无三角、浮点、数值根或非BRC参考。系数为Q[s]/(s²-3),s>0；实I,J,X,Z字符串中偶J项用于Hermitian观察。

## 1. 两编码的三个不同“秩”

Tr[(Ta⊗Tb)†(Tc⊗Td)]=4 delta_ac delta_bd，故完整线性算子基16维，一般Gram为16×16。这在两端各自允许完整单编码代数时已经成立，不是只有耦合才引起。
CZ=(II+ZI+IZ-ZZ)/2是一个Kraus的幺正通道，完整Gram秩1；跨编码系数的2×2子式-1/2证明其算子Schmidt秩2。低环境秩不等于没有跨编码关联。
span{II,ZI,IZ,ZZ}在CNOT、CZ和局部Z噪声下为四维不变观察子代数；加入W后W†ZW=-Z/2+sX/2，立即离开。Bell正负态有相同本地边缘，CNOT后第一端X期望却为±1；不能以边缘替联合态。

## 2. 公共尺度的张量反例及合法补全

单代码实四元范数性质不传到任意张量线性组合：(iZ)⊗(iZ)=-ZZ。M=II-tZZ，t1/5，M†M=(1+t²)II-2tZZ。用平均tau26/25归一，00/11的输出迹8/13，01/10为18/13>1。正Gram和正确平均迹不保证TP。

取K=M/(1+t)，H=I-K†K=diag(5/9,0,0,5/9)，把Tr(Hrho)送入正交flag则合法。H用1/3、2/3有理出口实现。这不是原不合法操作的无损修复，也不是物理吸收发现。

更具体的受控旋转：U=C_W=diag(I,W)。将W中s/2改为7/8得Uhat，效应diag(1,1,65/64,65/64)；平均归一仍产生130/129概率。改用已证收缩T=(128/129)Uhat，准确尾部H=diag(257,257,1,1)/16641。257=16²+1提供全部有理flag出口，完整效应I已执行。
433/500<s/2<7/8的有理平方证书给||Uhat-U||<9/1000。故e=||T-U||<=269/16125。任意参考联合输入的保留块迹范数差<=2e、flag迹<=2e，整体迹距离<=538/16125。此为保守证明上界，不是实测误差；不后选择。一般可按近似isometry的安全范数上界缩为收缩再补flag，证书构建仍计费。

## 3. 以观察为目标的BRC反推

Tr[O PhiL...Phi1(rho)]=Tr[Phi1*...PhiL*(O)rho]。CZ/CNOT共轭只置换I,J,X,Z字符串及符号，未增加项数；W把X/Z分成两项。全部16个双编码字符串的CZ/CNOT规则均与完整BRC矩阵对应，四个W规则同样核验。

受控W不再只是换标签：
C_W†(XI)C_W=(XI+sJJ)/2；
C_W†(IZ)C_W=(IZ+3ZZ+sIX-sZX)/4。
两式直接BRC矩阵验过，分别产生2和4项；不能把简单CZ的代价推给所有受控相位或QFT。

同一双编码任务：从|++>经CZ并分别接受Z退相干p，求图态投影Pi=(II+XZ+ZX-JJ)/4。两种真实BRC计算均得F=(1-p)²。p9/25时256/625；p1/4时9/16。后者超过可分态的1/2上界，见证为-1/16，无后选择。
最终计数将模板与求值分开：p9/25，密集Kraus准备64次核心调用、密集求值78次、稀疏求值14次；p1/4，准备64次、密集求值110次、稀疏求值14次。查询/输入模板和通用表证明不计入该表，两种路线均为同一BRC内核。单调用内部代价不同，这不是墙钟倍数或成熟Pauli模拟器对比。开发阶段174/14含64次准备，最终已分列。

同样的一端噪声边缘，共同ZZ翻转p1/4的图态F=3/4，而独立噪声为9/16，联合环境结构不能丢掉。

## 4. 查询残差与大规模限定例子

Hermitian观察中舍去DeltaO=sum c_w T_w，||DeltaO||<=sum|c_w|=eta。先前CPTP伴随unital positive保持[-eta I,eta I]，故所有输入期望误差<=eta；多次舍去可累加，二值测量概率误差<=sum eta/2。这是查询区间，不是CP通道，也不是完整采样器；函数拒绝非Hermitian实查询。根绝对值用sqrt3<7/4作有理界。测试删sqrt3 X/4给eta7/16、概率界7/32，不声称最佳精度。

非零尾部p1600/160801的Z噪声对终端ZZ严格无作用，交换标签证明即足够，零次新增数值BRC调用。若之后还允许W再测Z，这个省略失效。通道级flag裁减与查询级忽略不可混同。

128编码链：初始|0>^128，每端W，127条邻边CZ，最后每端Z噪声p9/25。只求O=X64 Z63 Z65（0-based）。反推依次为(7/25)O、(7/25)X64、-7X64/50-7sZ64/50，故期望-7s/50，正结果概率1/2-7s/100。实际383个门/噪声位置访问、最大2字符串、6次核心加2次尺度观察；每串128标签，复制/路由/位长不免费。未分配2^128态、未计算完整分布或样本，未作大规模密集对照。正确性由任意链长恒等式及小规模对应支持。

W⊗n反推Z⊗n恰有2^n个非零展开项，n1—6已检查；该例也可用n个张量因子表达，所以不是所有算法下界。一般交错受控W、模幂、端口再相干的支持数与因子秩仍无多项式保证。

## 5. 实际证据、先行研究和续接

最终92项检查；2310次正权BRC核心调用、3次公共尺度观察。独立输出目录重跑RESULTS.json与完整BRC_LEDGER.jsonl.gz逐字节相同：
RESULTS SHA2564b020052a68a5a09f69eb682521bd1a783ae38a26855ec34fb5db2081966944e；
账本SHA256ef7b10b6030d71244c7cfbb31fff241fe7f310b2e5c032882c594c1bbb1e9d2e。
完整中文证明、继承源码、新源码、计数和账本随v0.9包交付，ZIP复验另据实际回执。未做独立审核、Lean、物理实验、完整Shor/FFT比较。

公开原作者摘要/题录：Gottesman quant-ph/9807006v1；Rall等1901.09070v2，PRA99.062337(2019)。Heisenberg/Pauli传播已有理论不认领优先权，未读完整PDF。专用Issue2576、batch667dbc53-71ab-4253-835c-244dd6316819实际outer/child COMPLETED，原request SHA256e99c22b50729e7131327fa0afb4a167a3b43365eef59596694d2eaef8be07d92匹配；返回1条相关题录，n2、总覆盖未知；一次提供方查询、桥接LLM0，非全文。原comment5871588479及包内选择性字段保全，不把旧失败回执说成本轮结果。

下一具体问题：在3—6编码交错受控W和未知工作标签线路中测算反推支持/跨分割因子秩及位长，按预声明误差预算比较合法查询裁减的认证费用与精确反推。先前低秩结点/Gram和本轮特定128编码查询都不能自动替代一般Shor采样。
