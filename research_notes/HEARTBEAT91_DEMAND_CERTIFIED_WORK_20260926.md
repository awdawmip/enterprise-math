# Heartbeat91 — 按需认证工作标签，保持完整流式 Shor 语义

Progress-Event-ID: HEARTBEAT91-DEMAND-CERTIFIED-WORK-20260926
Status: AUTHOR_DERIVATION_AND_EXECUTION / SHARED_CONTEXT / UNREVIEWED / NOT_ADMITTED
Global read: 2b56507b03ae288e20fbdb8943face19dda660c3
Source read: 14d532fac59ad954034e7dc346d4370a4c00ab3c
Publication base: 1050eb5130bd9d2fe289f8fb91808c8234adffd1
Research-Activity-ID: 未取得；本轮继续已授权母题的可移植数学，不重放旧对话报告的登记拒绝，不借用他人session/CLAIM。来源及本地run标识保留，保存不是准入。

## 1. 继承与改变

父累计a7650c7f23705ac1ee195269ed19771189f2a7b8；父包78964785字节，SHA256951e6bd2efe14b7ac7282c4f72d39f4b6d72eb4a67250f2c16bdb4190a95ef8f核验后本地克隆。1770个父文件逐Git blob及字节保持，旧Stage76独立引用保留。Stage78–90的输入、CASE、实际相位、1e-6门槛、CF/gcd及失败规则不改。六原生轴、独立时间、P000、BRC-only和残差保真保持；不重做缺数据的物理拟合。

Stage90已经用带源标签的单位BRC路径替代稠密矩阵，但每个乘数仍预生成整个工作域的targets及inverse。本轮用总函数规则、BRC Bézout证书及按需单列证书替代这份全表，不改变物理/振幅状态。未请求标签不是零，不把缓存集合当可达支撑，也不提前求未知阶。

## 2. 全域证书与按需BRC列

令L=2^ceil(log2 N)，域Omega=[0,L)。取得整数u,v满足bu+Nv=1、0<=u<N。定义sigma_b(y)=by mod N（y<N），padding上为y；逆为tau(z)=uz mod N（z<N），padding同样固定。两域不交，Bézout恒等式证明完整域上的双侧逆，不需穷举L个标签。

每次实际访问y时生成z,q,q_inv，核验by=Nq+z和uz=Nq_inv+y。欧几里得余数、系数递推、最终Bézout与每列乘回均通过继承signed_dot_brc的实际正路径/符号观察；商和地址divmod仍是父接口的整数标签编译，不是新概率传播器。单位边、串接和控制直和直接复用Stage90实际不变核。每条EdgeReceipt保留N,b,y,z、quotient、inverse_quotient及有效/padding类别。

对完整基标签，操作仅将work y重标记为sigma_b(y)，控制关闭则保持，其他身份、符号、61模式和参考标签不变。双射保证没有伪合流。逐基相同加线性/配对扩展，证明任意有限串接、逆和控制作用与旧完整表相同。

## 3. 缓存不是残差场

DemandPermutation保存全域规则与至多C个派生单列证书。遗漏时按同一规则重算，因此任意C>=0、请求次序、清缓存时点都不改变返回值及后续完整场。需要保存的原始规则和科学状态没有删掉；通用BRC乘积缓存也限制为128项，未将无限memo当免费资源。计算/调用证据日志的另行成本明确保留。

负对照：21/2只查过1->2后，下一个标签2应映到4。若把cache miss当identity，则平方量仍为1，但工作标签错误。非互素乘数、伪Bézout、负/越界/bool标签、误用全表迭代与负缓存容量均显式拒绝。

同一21/a2/t10/k171正轨迹：容量0需54次访问/54次边生成/0缓存；容量1且每轮清空需54访问/27生成/末0缓存；容量2需54/24、三个乘数合计6缓存；容量16需54/9、合计9缓存。所有完整终端状态、分母及各步概率精确相同。这里是指定正轨迹验证，不是无偏成功频率。

## 4. 贯通初始化与后处理

DemandStreamingProgram复用原CommonStreamingProgram.__init__代码对象，只在复制globals中注入DemandFactory；原StreamingProgram.branches直接继承不改。c.targets变成可索引总规则而不是L元tuple。

原modular_power_brc、classical_postprocess、sample_once、factor_attempts也经相同的依赖绑定使用按需列；原代码对象、CF循环、指数检验、gcd、外部随机契约和有限重试不改。全部候选全叶、所有k后处理和驱动完成后，旧dense缓存misses=0、旧eager sparse缓存misses=0。原生H4、共享spectator真实回零、工作/残差和测量时序保持；新表示误差0。

## 5. 实际十二组全叶结果

12个冻结输入全部运行：15四底数/t4及a2/t8；21三底数/t6及a2/t10；33两底数/t6；35/a2/t6。所有继承Stage90案例的非计时字段逐项相等，包括每个终端概率、完整61模式state hash、规范分母、尾量、所有前缀质量、CF/gcd状态及失败分布。

21/a2/t10连同后处理：3个不同乘数规则，旧前向表96项；本轮6156次访问中仅14次边生成、6142次命中，缓存14项。21/t6同为96->14（402次访问）。33/a2/t6为320->34（648次访问）；33/a5/t6为320->34（644次）；35/a2/t6为256->29（612次）。这是旧前向表项与本轮实际生成表项的比较，不是RAM字节或总时间比例；逆证书、header、位长和原始记录另计。

21/t10仍12端点/732实槽的单前缀快照，完整分母最大5409bit，P128=1/131072，成功权重约0.330843218193906427，尾项与父版相同。全部相位字及调用语义没减少；理想Shor全分布界仍3699/68719476736，约5.38e-8。零新增表示误差不取消原相位编译误差。

在候选完成后，另用原稠密BRC验20表/880列，含逆、padding及逆序查询；控制/源标签有符号向量的往返也实际通过。更大域只核验N=2^b-1、b=32/64/127、乘数2上的六个指定标签及逆；容量2，没有全域物化。最大域为2^127，不声称完成127bit Shor或分解。

## 6. 成本定理和终端失败

对n=ceil(log2 N)，保存完整Euclid证据为O(n)个O(n)位整数，单规则header为O(n²)位；缓存C项增加O(Cn)位。一次访问使用O(n)位标签乘除及实际BRC证书，未把大整数当单位物理操作。全证据日志、统计计数、相位库、工作振幅、两个孩子、随机及报告历史都在此界之外并明确计成本。工作支持仍可能增长，S_(i+1)包含于S_i union sigma_(b_i)(S_i)，不预先用阶r缩约。没有一般多项式时间经典分解或量子加速声明。

原driver的随机源耗尽保留真实未完成前缀和完整状态，底数耗尽、RETRY_LIMIT、偶数/非互素预检查及正轨迹都通过。新的CLI只加缓存控制：python -S -m stage91.sample --N 21 --bits 10 --base 2 --attempts 8 --cache 16 --seed 9026，实际首尝试k171、因数3和7，含后处理生成11个表项。独立解压包再次执行非计时输出相同。固定种子是重放示例，不是随机性证明。

## 7. 核验与可恢复产物

主运行470组命名检查、1661次实际不变规范BRC核心调用，包含稠密参考验证；重复读取缓存不计新核心调用。规范核bc7babbb9e890f6d5a7094430a5fbdccf66c77ad:src/enterprise_math/brc_weighted_recurrent.py，SHA2567520822074b8f29e1c54f57b9543c043202db8bd7c6e27f3f1d6176028ac4a26。继承EM-DIRECT-0C08F0的流式定理和原driver，属于共享上下文复用，不是独立评审。

累计f1e229edbf35cef3fb4c6a322194e6b87ba6ae94，START_HERE_STAGE91.md。stage91/PROOF.md、demand_permutation.py、demand_stream.py、sample.py、run.py、RESULTS、12STREAM_CASE、CACHE_INDEPENDENCE、DEMAND_PERMUTATION_CERTIFICATES、DRIVER_REPLAY、ARITHMETIC_CERTIFICATE、CLI_SAMPLE及31项manifest/边界/来源。

原58173959216ns；最终累计bundle新克隆完整重放59744779292ns。递归仅排除elapsed_ns和dense_reference_elapsed_ns，RESULTS加16gzip全部科学内容相同，3份gzip字节同，其他实际计时原件都保留。1770父文件、31manifest、fsck、两工作树干净核验。便携独立解压/新增文件字节/CLI帮助和完整seed演示通过，未声称第三次全叶重放。

bundle BRC_Heartbeat_demand_certified_stage91_20260926.bundle：80743613字节，SHA25656d035784882ab847ac29c278a44564792afaa3461d757f6f574ae7a97ef9887；Drive1grtGkg_wIMqzvDbrK2-7V2oH8XFtR1cW已上传、读元数据、返回原字节并本地逐字节/SHA一致。
ZIP Shor_Demand_Certified_Stage91.zip：46268166字节，SHA25692096a8b50a71f515de8b2e22208b4da356de01fe6bb5eec53e96145b16b4d2f。Python3.11+标准库：python -S -m stage91.run；python -S -m stage91.sample（参数如上）。外部回执/mnt/data/heartbeat91/DELIVERY.json。
证明SHA256107b504ccec5e83f63732f3f9b5c882790d3b79f48dd3169dbce0e51d4efa29d；按需实现5b34c18980365d9382c34c38b62f6f2f0e215d4d67d12d7d70ae7de04f4fd5c2；结果49a3286a8dc31103916077f744c4318494bb9c313861c4fd43daba2c702636eb。

Bézout、延迟求值和可逆模乘的一般数学不作为首创；本轮新增为既有BRC接口的按需、可逐出缓存证书及整个冻结终端流程精确验收。官方IBM Shor教程仅作模乘/重复平方背景。没有独立审查、Lean、物理标定、量子硬件或速度优势。

## Next及并行来源

继续核算原固定相位字、大整数位长与实际可达支撑的增长；不把移除全表解释成移除指数工作支持。在相同CF-only冻结合同内推进，不免费替换后处理。

发布前读到1050eb5130bd9d2fe289f8fb91808c8234adffd1:research_notes/directed_recovery/20260926_C6438C/support/HANDOFF.md，另一作者提出谱支撑与新增候选后处理的增强流程。这里只消费其明确接口及来源，不将其结果计为本轮验证；新增候选后的正成功率合同不自动替代原CF-only及理想小TV合同。发布前并行记录均保留。父研究未整体完成，保存不授数学准入。
