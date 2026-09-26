# Heartbeat90 — 共同生成器接入单控制位终端 Shor，贯通稀疏模乘与后处理

Progress-Event-ID: HEARTBEAT90-STREAMING-COMMON-GENERATOR-SPARSE-PERMUTATION-20260926
Status: AUTHOR_DERIVATION_AND_EXECUTION / SHARED_CONTEXT / UNREVIEWED / NOT_ADMITTED
Global read: 441ebefd3ba2372abf9044d802fa816b4c4ef895
Source read: 5ab9c3befa50b24b26a87c63affcbf45ea4d8084
Publication base: f0e5fb6f478a5a380ab5a7533d2585f7f43ee3bf；相对读快照仅新增其他会话/活动记录，未改本研究源与约束，本条只新增独立笔记。
Research-Activity-ID: 未取得；继续用户已授权母题的可移植数学，不重放旧对话报告的登记阻断，不借用别人的session、CLAIM或独立审阅资格。保存不授准入。

## 1. 实际继承和本轮增量

父累计206433ae44e3704e13c3984db0e61531a0a21fe7；父包77032070字节，SHA256 e7e08f59d685edec827344d1503686157ce86ff2076c325aab3cdeb5b87e50ea实核后本地克隆。1732个父文件与原Git blob逐字节相同，另一Stage76提交9510ec8ddae83d469dbcd116064c610f03e82514独立ref保留。Stage78–89原CASE、相位、模幂、失败记录及1e-6门槛不改。P000、六原生轴、独立时间、BRC-only、残差保真及数学优先方向保持。

真正复用另一作者EM-DIRECT-0C08F0已完成的终端路线。Source目录research_notes/directed_recovery/20260926_0C08F0下的algorithm_intake/terminal_instrument.py和driver/shor_driver.py完整保全为stage90/vendor，Git blob分别17486fce678c5c22209f57abae07793b17ce07ba、dd4fc225e01cf24c2dca37aec35117f804f0baa4，与来源完全相等。原StreamingProgram.branches代码对象直接继承，原流式定理和有限驱动不重复声称本轮首创，也不称共享上下文复核为独立审阅。

新增：把Stage89 bank真实接入流式终端；带来源标签的稀疏BRC置换证书；贯通CF/gcd依赖的绑定；12个冻结输入的全部终端叶/全部前缀检查；可独立运行的有限重试CLI。不是再扩大39/58个局部统计量。

## 2. 一位活动控制、完整工作与61残差

bank只把旧phase3替为PowerRotor(old phase4,2)，即实际同一根字执行两次，其余相位保持。流式第i轮的模乘参数是a^(2^(t-1-i)) mod N，按原整数重复平方取得，未输入未知阶、因数或直方图。对历史h=(h0,...,h_(i-1))，相位按原c=0,...,i-1顺序执行；不假定其他实际相位可交换。

每轮仍执行原H4(active,spectator)、受控模乘、有序受控相位、同一H4、实际控制结果分支。工作和全部61个实分量连续保留。两H4之间不操作spectator，因此轮边界它严格回0，不是清零；第一H4后删去spectator=1会丢一半平方量，实际负对照通过。

设U_(i,h)=M_i tensor T_(i,h)，保留未归一化向量v_h，则
v_(hr)=(I+(-1)^r U_(i,h))v_h/2。
U正交给出m_(h0)+m_(h1)=m_h。六轮实际新字与这项已有宏式的完整孩子状态逐坐标一致。原作者的准备惰性换序/测量前移证明适用于任何保持其条件的实际内部bank，且不需要不同残差相位交换，因此对本新bank仍有：每个(k,work,internal)终端振幅等于Stage89全控制执行的对应振幅。

已测控制位只作为后续对角控制的经典历史；不授予随后重新相干访问旧控制位的权限。每次按m_child/m_parent抽样，原整数振幅和共同二幂分母不以平方根归一化。外部randrange的条件均匀性仍是借用的数学随机接口，不是Born推导。

流式调度误差0，Stage89模型替换误差仍为eta=579/2^39。t10的理想Shor全分布证书继承3699/68719476736，约5.38e-8。表示精确不消除原相位近似。

## 3. 稀疏BRC置换与完整后处理

原modular_columns在L=2^ceil(log2 N)工作空间构造L×L矩阵，P[y,z]=1[z=sigma_b(y)]，sigma_b(y)=by mod N（y<N），无效编码固定，再调用一般稠密BRC核。

gcd(b,N)=1保证sigma为双射。新证书将每个源标签y的唯一权重1边分别保留为带N,b,y,目标,逆标签的BRC路径，按来源作直和。实际不变核执行2态单位边、3态两边串接和4态控制直和。两种表示对每个基e_y同为e_sigma(y)，所以对完整有符号/控制/工作/内部/参考标签的线性扩展相等；组合胶合实际中间标签，控制直和不测量control。只适用于这一确定性双射类，不把一般图或正质量冒充振幅。

表构造仍用与Stage78相同的整数模运算作为地址编译，不先求阶。每份证书O(L)标签，无L²零矩阵；欧几里得BRC、标签位长、相位字和工作支持成本另计。O(N)仍对输入位长可能指数增长，不是一般多项式经典分解。

重要修正：CF后处理中的modular_power_brc也默认调用稠密列，不能只替换量子初始化。bound_driver用复制的globals映射绑定稀疏列，复用原modular_power/classical_postprocess/sample_once/factor_attempts的同一代码对象；原模块和源文件不改。原CF循环、指数返回检验、gcd、随机选择、失败与重试规则保持。

在全部候选叶、每个k的CF/gcd、指定轨迹和有限驱动完成后，旧dense modular缓存misses仍为0。之后才调用旧大图作验证。20表、880个完整工作列与旧实际BRC全部相同；完整小基二步串接和受控直和亦同。非互素21/3拒绝。143、221、437只做稀疏标签/逆验证，不冒称运行其Shor。

## 4. 全叶结果与真实成本

12组冻结输入实际完整执行：15四底数/t4及a2/t8；21三底数/t6及a2/t10；33两底数/t6；35/a2/t6。每个前缀孩子完备，前缀质量等于全部对应终端叶的质量和。全部终端控制概率与Stage89逐项有理相同；重建的规范振幅分母和完整原61模式state哈希亦相同，哈希重建覆盖535519个端点实坐标槽。它是有限计算证据，一般振幅等价由第2节证明；不称535519次独立实验。

单前缀活动快照峰值：21/t6为12端点/732实标量槽，对比旧全控制宏快照380端点；21/t10仍12/732，对比6140；35/t6为24端点/1464槽，对比752。全叶验证明确展开2^t个叶，并不只用单轨迹内存。函数输入/孩子、静态库、O(N)表、历史和重建成本也存在。

21/t10所有叶的最大分母仍5409bit，尾平方量与Stage89精确相等；P128仍1/131072，成功权重仍约0.330843218193906427。没有减少原硬件相位字长，不能由更少端点宣称量子加速。

## 5. 终端成功、合法失败及可运行接口

三个指定正轨迹15/t4/k4、21/t6/k11、21/t10/k171实际重放，概率与冻结分布对应项相同，原CF/gcd取得3,5或3,7。它们是轨迹测试，不是无偏成功频率证据。

空随机源返回INCOMPLETE_RANDOM_SOURCE及完整可恢复原状态；空底数列表返回BASE_POLICY_EXHAUSTED；两次全零读出返回RETRY_LIMIT；偶数14和非互素21/base3分别保留预检查。这些失败没有被丢掉或改成伪因数。

CLI只取N、底数、偶数控制位数≤10、有限次数和可选软件seed。一次独立执行 --N 21 --bits 10 --base 2 --attempts 8 --seed 9026，第一尝试得到k171、因数3和7，dense misses0；独立解压后的CLI再次给相同全部非计时内容。无seed用SystemRandom外部接口，不声称由残差创造随机性。不是一次必成功。

## 6. 运行、重放与产物

本轮最终336组命名检查、73次实际不变BRC调用，包含旧稠密验证器的调用；单位证书缓存/复用没有计成新调用。核心bc7babbb9e890f6d5a7094430a5fbdccf66c77ad:src/enterprise_math/brc_weighted_recurrent.py，SHA2567520822074b8f29e1c54f57b9543c043202db8bd7c6e27f3f1d6176028ac4a26。

原47426662428ns；从最终累计bundle新克隆完整重放48938275313ns。RESULTS及16个gzip科学内容全同，仅递归排除elapsed_ns和dense_reference_elapsed_ns两种实际计时字段；其中2份gzip字节相同，其他保存实际运行时间，不冒称全字节相同。1732父文件、37项manifest、fsck和两工作树干净核验通过。

早期未绑定CF依赖的探索源和结果保存在provenance，不计新实验。便携包首次入口检查发现漏带旧Stage58采样依赖，已补齐原始依赖文件，模型与驱动代码不改。最终包独立解压/新增文件字节/CLI导入以及一次完整seed演示通过；未进行第三次全叶便携重放。

累计a7650c7f23705ac1ee195269ed19771189f2a7b8；入口START_HERE_STAGE90.md。stage90/PROOF.md、streaming_common.py、sparse_permutation.py、bound_driver.py、sample.py、run.py、两份不变vendor、RESULTS、12STREAM_CASE、稀疏/整轮/驱动/算术证书、CLI_SAMPLE、边界/来源/manifest。

bundle BRC_Heartbeat_streaming_common_stage90_20260926.bundle：78964785字节，SHA256951e6bd2efe14b7ac7282c4f72d39f4b6d72eb4a67250f2c16bdb4190a95ef8f。Drive1ix_fA5fYzJ-10tkMcnmAq4phwFHrmOA1已上传、读元数据、取回完整字节并本地cmp/SHA一致。
ZIP Shor_Streaming_Common_Generator_Stage90.zip：44428611字节，SHA256a4551d9f57a2fefd4c984c7409b289bc23b09b101d8a21eef7f88756d8b177c5。Python3.11+标准库：python -S -m stage90.run；python -S -m stage90.sample --N 21 --bits 10 --base 2 --attempts 8 --seed 9026。外部回执/mnt/data/heartbeat90/DELIVERY.json。

原作者官方摘要Griffiths/Niu quant-ph/9511007和Garcia-Mata等0809.4416用于先行背景；不宣称首创半经典或单控制位Shor，不声称全文新颖性、独立评审、Lean、量子硬件、实测物理或一般速度优势。

NEXT: 继续在相同终端合同下研究按需工作标签认证和真实根字成本，不回到局部统计量无边界扩张；已测控制位需要相干回访时作为另一明确接口。原用户数学目标未整体完成，成果保存不等于正式准入。
