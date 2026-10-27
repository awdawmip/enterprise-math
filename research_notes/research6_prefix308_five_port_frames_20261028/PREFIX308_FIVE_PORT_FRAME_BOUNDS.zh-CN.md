# PREFIX-308｜五Port BRC相干帧的八／十参考全域稳定恢复

日期：2026-10-28。状态：AUTHOR_SIDE_EXACT_PROOF / UNREVIEWED / NOT_ADMITTED。作者角色：本轮普通Chat TASK_RESEARCH作者侧；不继承前任Source session/CLAIM或独立Driver身份。

## 冻结来源、语义与目标

本轮固定读取GLOBAL_KNOWLEDGE_V1 main@5b03e7f250babaf694305861ca991d84fe4cdffc（00_BOOTSTRAP、OPERATING_MANUAL、P000原件及匹配启动投影、ACTIVE世界观、数学与代码策略）；Enterprise Math科学前沿main@c9a28fe95d621a2d1b9f22bb93f766a3eb739098。PREFIX-299的十二个S4/S7最优保留Port整数高斯矩阵，输入Git Blob b6acffe158f014469235f5428d2889ff43b62810；PREFIX-307的对照界来自同一项目科学前沿。

所研究a∈Q(i)^3是**辅助、来源标记的BRC三源寄存器**，不是P000六轴原生离散Cell，也不构成原生Detector门。q∈C4={1,i,−1,−i}，b=diag(1,q,q²)a。Port复振幅为
E=(b₀+b₁)/2，C=q⁻¹(−b₁+b₂)/2，R_j=(m_j·b)/8（j=1,2,3）。
五个质量Q₀(z)=|z|²已经免费可读。附加参考读数Q₁(z)=|z+1|²、Qᵢ(z)=|z+i|²由未同步、带独立来源身份的1/i参考与对应Port完整相干合成，**每次读数仍走带来源标签的有序路径对BRC正质量核**。正质量本身不当作有符号振幅。

定义U_5:q,a↦(E,C,R₁,R₂,R₃)。已知仪器矩阵M和q以解码，**不需要主动旋转Port相位**。逐次测得的每一项所用质量读数均有独立加性实误差绝对值≤ε；允许全部连续实误差端点。恢复输出可在C³；目标是对每一个a∈Q(i)³的统一复振幅二范数误差证书。

## 精确定理：八次参考（四Port）

对PREFIX-299的S4、S7全部十二个矩阵代表与任意q∈C4，**可以仅增加8次**与1/i的相干参考读数，使统一误差界为

  ||â−a||₂ ≤ sqrt(512/29) ε.

选择E、C与三条R中任意两条，使被舍弃的R行平方范数（整数高斯系数）等于33。五项免费基础质量可以全部保留；这一估计器只用所选四Port的Q₀。

证明：
1. PREFIX-299的精确Gram公式M* M=16H−S，S=S4=diag(1,0,2)或S7=diag(2,0,1)，H=((3,−1,0),(−1,2,1),(0,1,3))。E、C的系数行在分母8上分别是(4,4q,0)、(0,−4,4q)；三条R行是(m_j0,m_j1q,m_j2q²)。逐源有序Gram展开相加后，严格得到U₅*U₅=I−S/64；q相位共轭不改变此对角S。
2. 精确枚举已持久化的十二代表，其三条R的整数行平方范数多重集合每次都属于{33,38,54}、{33,44,48}、{33,46,46}。故必有一条被舍弃的系数行m，其平方范数=33。对应实际振幅行r=m diag(1,q,q²)/8，故||r||₂²=33/64。
3. 对其余四行构成U₄，有U₄*U₄=U₅*U₅−r*r。因为0≤S≤2I及0≤r*r≤||r||²I，得到**Loewner下界**U₄*U₄≥(1−2/64−33/64)I=(29/64)I。它是正定的，因而四Port保持全部三源复振幅、共同源关系和相位信息可恢复。
4. 在任一所选Port，令读数分别为Q₀(z)+e₀、Q₁(z)+e₁、Qᵢ(z)+eᵢ。相干参考恒等式给出估计幅值
  ẑ = ((Q₁+e₁−Q₀−e₀−1)+i(Qᵢ+eᵢ−Q₀−e₀−1))/2。
它满足|ẑ−z|²=[(e₁−e₀)²+(eᵢ−e₀)²]/4≤2ε²。四Port扰动向量d满足||d||²≤8ε²。以同一个已知U₄的最小二乘左逆(U₄*U₄)⁻¹U₄*恢复，算子范数≤sqrt(64/29)，故得上述统一界。任意a及任意合法连续误差均成立。

这是一个**有效的保守统一上界**，并未声称是8参考资源内的最优极小极大常数；特别是没有利用被舍弃R的免费Q₀进一步压缩上界。

## 精确定理：十次参考（全部五Port）

如果给E、C、R₁、R₂、R₃全部增加1/i参考，新增10项，取五Port的正规左逆，则对同一全部配置与任意a∈Q(i)³严格有

  ||â−a||₂ ≤ sqrt(320/31) ε.

理由是U₅*U₅=I−S/64≥(31/32)I，五条Port的单Port误差平方和≤10ε²，因此||â−a||²≤(32/31)·10ε²=320ε²/31。

两个结果都优于PREFIX-307采用E、C、单条可控相位R加6参考所取得的指定逆式界sqrt(1928/53)ε，且本轮不需要可控C4门。这是**测量数量换取恢复稳定性**的明确资源权衡，不能将不同预算下的上界解释为同预算算法优劣。

## 精确执行的BRC检查与证明覆盖

源矩阵来自固定Git Blob b6acffe158f014469235f5428d2889ff43b62810；验证器verify_prefix308.py实际执行，使用Z[i]整数对、来源标签、独立reference_1/reference_i身份，以及完整**有序**来源对conj(x_source)·y_source累加。输入{0,1,−1,i,−i,1+i}³×12轨道×4相位；直接BRC读数155520次、有序源路径对2125440项；10368组输入从基础读数和相干参考重构全部五条Port，再用精确Gram身份逐源恢复原始a。检查432个复数Gram条目，全部断言通过；每组行范数具有33的舍弃选项。

证明中“全Q(i)³／全部连续绝对误差”的量词由**准确Gram恒等式、Hermitian秩一Loewner比较及算子范数**成立，不依赖上述离散样本采样。机器结果文件RESULTS_PREFIX308.json是验证范围摘要，可由仓库中的源码读取PREFIX-299已保存的原始12矩阵重新生成。局部运行汇总：configs=48、input_cases=10368、mass_reads=155520、ordered_pairs=2125440、gram_entries=432、reconstructions=10368。

BRC类型：source-tagged coherent path amplitude→ordered-source-pair positive mass→independently tagged 1/i reference interference→complex amplitude reconstruction→left-inverse; observer仅声明上述Port及参考，允许的未来作用仅限该辅助相干线路及其线性来源恢复。压缩仅在测量与误差模型下有上述显式范围，不能推断原生X6路径、场、时间、测后态和任意Detector组合受到同等保护。

## 待独立接纳与下一精确问题

原生owner/CLAIM实时查询本轮返回CONTROL_QUOTA；Source status展示research_authority_granted=false，active_jobs=5/5，control sync CODE_REVIEW_REQUIRED。本轮不宣称Source Result、审阅通过、原生物理实验或C4相位门可达。

接续NEXT_PREFIX309.md：给8／10参考联合最小二乘求**精确**∞→2误差范数（枚举端点或复有理证书），并研究6参考以上是否存在更低预算的最优分配；另行推进PREFIX-308的全Q(i)³自适应深度≤5与原生Detector合法性。有限域既有2参考结果不改变全域量词。