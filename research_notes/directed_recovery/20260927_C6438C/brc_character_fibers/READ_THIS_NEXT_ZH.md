# 联合字符纤维：从这里继续原生 BRC 研究

本单元完成的是**联合筛选的精确计数与概率合同**，尚未运行新的 Jacobi 筛选程序，也未完成通用因数分解或 Shor。它是独立于四例邻迹实验的新证明单元；既有实验、费用、检查点和 guard 均保持原样。

## 已完成的结果

对奇素数 r 上的正规参数 k，记 sigma=Legendre(k²−4,r)、eta=Legendre(k+2,r)、alpha_r=Legendre(−1,r)。证明给出了四类参数的精确大小

    C_r(sigma,eta)=(r−2−sigma−eta−alpha_r*sigma*eta)/4。

它进一步按两个字符分别计数任意固定公开指数 E 的正返回、负返回和未返回，逐项扣除被正规性排除的特征值 +1、−1。局部类别为空时保留零权重，不制造除以零的条件分布。

在数学假设 N=pq、p 和 q 为不同奇素数，并从所有模 N 剩余类均匀提出 k 的条件下，两个可观测字符为

    J_D=Jacobi(k²−4,N)=j，J_plus=Jacobi(k+2,N)=e。

令 R=(p−2)(q−2)、alpha=Jacobi(−1,N)。满足正规性和这两个指定字符的参数总数恰好是

    Z=(R+j+e+alpha*j*e)/4。

原始均匀提案的接受概率为 Z/N；已条件于正规性的接受概率为 Z/R。两个字符并非独立公平比特，四个局部方向也不能等权平均。若 Z=0，该筛选事件为空。

令 A_r、B_r、U_r 为各局部字符类别内正返回、负返回和未返回的计数。证明中的兼容方向混合给出两个带符号主观察量至少取得一个真因子的精确概率

    1−sum(A_p*A_q+B_p*B_q+U_p*U_q)/Z。

这仍是指定提案与选择规则下的理论合同；p、q、局部阶及其公因子只用于分析，未作为算法输入或免费概率 oracle。E 必须在已选全局字符类别内固定。若还根据 k 的其他信息适应性选择指数，必须重新推导分布。

同一符号的 E 与 E+2 返回互不相交，因此两时钟的分支计数也可纳入该合同。但跨符号、跨时钟的全部四种事件不一定互斥，不能直接把它们当成四个独立类别。公开时钟 E=N−j 的负返回不饱和结论继续有效；再次筛选字符不能让本来不可能的双素因子负返回出现。

## 阅读次序与证据强度

1. [JOINT_CHARACTER_FIBERS.md](JOINT_CHARACTER_FIBERS.md)：主证明，重点是式 (2) 至 (10)、空类别以及提案分布的范围。
2. [JOINT_CHARACTER_FIBERS_SELF_REVIEW.md](JOINT_CHARACTER_FIBERS_SELF_REVIEW.md) 与 [JOINT_CHARACTER_FIBERS_REVIEW.md](JOINT_CHARACTER_FIBERS_REVIEW.md)：作者自审和共享研究上下文的交叉审阅，均通过；不是独立数学入场或定理提升。
3. [NATIVE_DUAL_CHARACTER_INTEGRATION_AUDIT.md](NATIVE_DUAL_CHARACTER_INTEGRATION_AUDIT.md)：实际源码阅读所确认的可复用接口及其计费、记录边界。它未执行新的集成。
4. [SOURCE_MANIFEST.json](SOURCE_MANIFEST.json)：本包的精确字节、SHA256、Git blob 和外部不可变来源。发布后的实际回读凭证与 manifest 分开保存，不预先声称远端写入成功。

本单元无数值试验、随机成功率测量、时间基准、重放实验或新的专业文献查询。主证明、两份审阅和集成审计的原始字节保持不变。经典字符、Lucas 与环面数学的来源地位保持明确；本次贡献是将联合分布和原生接口合同完整写出，不能据此宣称通用优势。

## 不可变前驱与实际复用边界

前驱是已完成发布和完整回读的 [邻迹科研包 2034df3](https://github.com/awdawmip/enterprise-math/tree/2034df3def543e151ef122e8e260d417331de0aa/research_notes/directed_recovery/20260927_C6438C/brc_adjacent_trace)。其中的双覆盖字符、精确返回纤维、公开 Jacobi 时钟和条件筛选器是本证明的来源。前驱四例的生产费用和验证结果不属于本单元的新测量。

通用原生 Jacobi 接口的已发布精确源码为 [typed_jacobi.py](https://github.com/awdawmip/enterprise-math/blob/951cc16cb09635fae9f93230d96030fdaa2035b3/research_notes/directed_recovery/20260927_C6438C/qft_row_queries/character_certificates/typed_jacobi.py)，SHA256 `ce7168c8724d1fff216b903f09cdaf7fe16c8074c48488f7b26fb80584060402`；对应 [证明文件](https://github.com/awdawmip/enterprise-math/blob/951cc16cb09635fae9f93230d96030fdaa2035b3/research_notes/directed_recovery/20260927_C6438C/qft_row_queries/character_certificates/JACOBI_FINAL_BIT_PROOF.md) SHA256 `fc51f6feb6134b2d1443efd9751f26621478a25512cc2d3784ae63045c5c7161`。本次包装通过 GitHub 连接器重新完整读取这两个不可变文件，验证其字节和本地已审源码一致。

复用范围是 `typed_jacobi_trace(a,N)` 的通用合同。旧文件中的 square_schedule、QFT final-bit 结论和旧测试驱动不是本单元的筛选定理。`verify_typed_jacobi` 会重新调用算术程序，属于科学重放；不能在行政封包或文件审查中把它当作免费记录核对。

## 接下来可独立推进的工作

先选择一个明确的公开指数规则和提案分布，利用已经证明的计数式推导可由公开量表达的成功率界、反例或选择信息。核心缺口仍是未知局部阶的奇数部分：字符筛选揭示了部分二次幂结构，并未自动去除奇数阶障碍。精确公式本身也不提供能够免费采样有利类别的算法。

如果推进原生集成，应把实际 Delta 与 k+2 的生产者连接到两个完整 Jacobi 证书，保留拒绝、非正规、单位、饱和和真因子结果；公开 E 的整数构造、每次提案、传播、所选 gcd、整除证书及验证均计费。按原接口直接复用 setup 时，其旧 gcd 仍须付费；只有明确改变生产者与验证合同后，才能讨论消除重复工作。新的运行另立独立单元，不修改或重跑已完成的四例。

任一获授权的对话都可以从这些不可变来源继续证明、反例、接口审阅或新的实现，无需原驾驶员、研究员或特定主机。缺少某个执行工具时仍可推进独立数学工作；实际计算保持已声明的原生算术合同。本次只完成独立源码发布与回读，研究活动检查点、guard 和知识库日志由协调者在当前大数单元结束后按合并进度更新，不能把未更新状态误记成已完成。

Global-Knowledge-Sync: main@a668c14 / GLOBAL_KNOWLEDGE_V1。实际 helper 返回有效 canonical lease；三份 canonical 入口与此前已读 b304760 快照无差异，复用其未变规则。各原始作者文件保留各自实际读取标记。
