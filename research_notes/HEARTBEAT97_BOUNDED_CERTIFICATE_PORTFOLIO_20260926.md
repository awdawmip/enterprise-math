# Heartbeat97 — 有界交错证书与小规模选择：不改变残差状态的认证调度

Progress-Event-ID: HEARTBEAT97-BOUNDED-PROOF-PORTFOLIO-20260926
Status: AUTHOR_DERIVED_AND_EXECUTED / SHARED_CONTEXT / UNREVIEWED / NOT_ADMITTED
Global read: f193fa416e36636aea0813c8b02d279ae2cf6d0d
Source read and publication preflight: 87297b30fdadc10eb7384c54c8f7fe024d30f8e6
Parent executable: c6384ae983972aa86423c00b78a3dcea69caff9c
Local contribution provenance: HB90-0de6b47ad07848a1b6e8347fd5156ca6；只是本地贡献来源，不是服务或平台认证身份。
Run: HB97-aba87dc78ba74c59be25a065190d02e1
Research-Activity-ID: 未取得，REGISTER_PENDING。未借用他人session/CLAIM，未重放历史报告的登记拒绝。中立研究保存不授正式执行身份、独立审核或数学准入。

## 1. 固定母线与本轮实际工作

先核验挂载Stage96 bundle：87,563,171字节，SHA256 5aaceb5982fd3917e65ad4aed7214304c20808f15e31b256030866459c8a4005，再从本地包克隆。1916个父追踪文件逐Git blob及新克隆字节保持不变。全部12组冻结输入、真实phase3=phase4字两遍、其他相位顺序、CF-only、失败语义、61模式和后态恢复保持。P000六原生空间轴与独立时间、BRC-only、残差保真不变；内部模式与执行步骤不冒充空间维数或物理心跳。标准二次观察、QFT目标和外部条件均匀随机接口仍为BORROWED_REFERENCE。

Stage96每次进入认证先检查全长t-1个工作调度平方关系，小输入和单轨迹的设置代价可能超过搜索本身。新stage97/portfolio_certificate.py提供两个逐请求协程：直接包络E与短／长步M；采用已证明的小规模优势判据，其他配置才有界交错。全部源边仍调用未修改的DemandPermutation及其原BRC Bézout／单列观察。集合索引和调度不代替振幅运算，没有新三角、π、理想QFT或提高精度的传播器。

## 2. 两条认证路线与适用性

E从真实非零工作支持S开始，按原剩余置换逐层生成包络。每查询一条源边就检查目标是否已在当前包络；发现第一个碰撞即可返回完整失败见证，不必做完已经确定失败的整层。没有碰撞时必须完成本层才能扩展。E适用于任意一列已认证双射，不需要共同幂结构。

M复用Stage96等价：剩余ell轮、q=2^ell时，S,gS,...,g^(q-1)S两两不交，当且仅当不存在x,y属于S、1<=d<q使g^d(y)=x。它先核验仅与后缀有关的ell-1个平方关系，再构造b=2^floor(ell/2)的短表和G=ceil((q-1)/b)的长链。baby重复、长短匹配及d=q允许的端点规则不变。成功成本为(ell-1)+|S|(b-1+G)，包括设置。

若M的后缀平方关系失败，只返回SPECIALIZED_SCHEDULE_UNAVAILABLE，不是成功或碰撞证明；E仍能检查给定真实调度。此广义接口不表示修改后的调度获得冻结Shor目标的认证。原程序的类型、N、实际乘数及输入绑定仍先检查。

## 3. 选择规则与最坏额外开销定理

固定策略SMALL_SINGLETON_DOMINANCE_ELSE_BOUNDED_E_M_RACE_V2：ell=1时直接用E；|S|=1且ell<=3时也直接用E。剩余情形先让E做一次请求，再依E,M,E,M交错，每次只允许一个原BRC认证列请求。设置请求和落败方的工作均收费。

小单标签选择不是按目标概率调参。设标签周期r仅用于证明，不输入运行器。ell=2时E上界/M冷启动成本分别为：r1为1/2、r2为1/3、r>=3为至多3/4。ell=3时r1为1/3、r2为1/4、r3为至多3/5、r4为1/5、r5为至多5/6、r6为至多3/6、r>=7为至多7/7。沿原指数4、2、1检查首次包络重合即得；排序只能更早检出。因此这些配置E不劣于M，不需要再竞争。63项实际小单标签测试核验对应不等式。

对有效幂调度且预算未截断，令C_E、C_M为这两条固定协程单独冷启动完成所需的逻辑边请求数，C_M包含设置。若C_E=1，组合只需1次；若C_E>=2，E的第C_E次请求最迟处于全局2C_E-2，M的第C_M次请求处于2C_M+1。因此

    C_port <= min(2C_E-2, 2C_M+1),  C_E>=2;
    C_port <= 2 min(C_E,C_M)+1.

直接优势分支同样满足此界。重复(N,b,y)在同次认证内可复用，因此实际DemandPermutation调用数不超过逻辑请求数。该定理只比较这两个固定逐请求认证器，不是对任意算法最优，也不是墙钟、RAM、位运算或硬件门数的二倍界。排序、哈希、证据日志和大整数成本另计。

## 4. 总预算和状态保真

label_budget为所有逻辑请求的总预算：E、M设置／搜索、落败方及命中临时缓存的重复请求都计入。恰在第B次请求完成证明可接受；下一请求尚待执行而B耗尽则UNCERTIFIED_BUDGET。预算零禁用快捷路线，包括旧证明缓存。没有找到碰撞不等于已证明无碰撞；未完成时继续原Stage93场传播，不改变概率或删除样本。

默认最多64份完成证书，结构键包含N,a,t、实际调度、深度、真实支持、预算、容量筛查和策略标识。不依赖振幅、历史具体位值或概率权重，只共享数学命题；不同场和后态绝不合并。容量排除仍只排除这个不交证书，不裁决实际概率或因数成败。未完协程目前不跨进程序列化；预算耗尽可丢弃的是可重算认证工作，不是原科学状态。

原Stage95 sampler、SuffixRecipe、continue_suffix、原CF及有限attempt使用同一代码对象，只绑定新证明供应器。restore_recipe以冷引擎重新查询真实源边并比对完整证据，不接受随机源；伪造边、调度、成本后重新计算公开hash仍会被拒绝。已选结果不能重抽。成功证书建立同一后缀谓词，其余状态走同一父传播，所以逐步概率、同随机带的报告、完整恢复场及CF结果保持。

## 5. 实际完整Shor回归与收益归因

12组冻结输入全部执行，逐前缀恢复并对照原完整作用；所有终端概率、原始前缀权重、完整61模式振幅／分母／hash、尾项与原CF成功／失败相同。全部非容量结束的胜出证书在这12个小实例中都来自E。实际收益来自避免无条件设置、逐边早停和已证明的小规模直接选择，不来自这些实例上M胜出的经验；不得把选择策略说成普遍更快。

全树实际标签查询，Stage96->Stage97：15/2/t4为9->4；15/4/t4为8->3；15/7/t4为9->4；15/14/t4为8->3；15/2/t8为13->4；21/2/t6为20->9；21/8/t6为12->4；21/4/t6为12->8；21/2/t10为24->9；33/2/t6为26->13；33/5/t6为28->16；35/2/t6为41->22。都包含本轮实际设置和落败工作，不把证明命中计为新科学执行。

单轨迹四组按相同随机带逐事件对照，含两组CF无因数结果：15/2/t4查询9->4，21/2/t6为12->4，21/2/t10为16->4，35/2/t6为27->13。标准21种子9026仍k171、因数3和7，证明缓存命中0，到控制读数仍82次根字行。

场求值未下降：21/2/t10控制读数根字行仍6125、完整恢复13803；35/2/t6仍63、733。标准21规范分母5409位、P128=1/131072、单次CF成功权重约0.330843218193906427、到理想Shor界3699/68719476736均不变。表示新增误差为0，不取消原相位近似。

## 6. 不利结果与预算边界

在N65537,a3,S={1}的标签测试，剩余ell=4/6/8/10时M最终胜出。单独E成本15/63/255/1023；单独冷M含后缀设置为10/20/38/72；交错逻辑请求21/41/77/145，实际去重后15/35/67/127。因此较长例中竞争比事先正确选择M更贵，最坏界不是逐例加速承诺。这些只是标签判据测试，无相位运行或因数实验。

ell10例总预算144时尚未完成，返回UNCERTIFIED_BUDGET；预算145时才通过。即使单独M可用72次完成，组合也不能把已经支付的E工作隐藏以伪造预算成功。未认证会安全回到原读取。

820个小域支持／长度配置中，完整真假判定与两条单独路线一致，严格区间端点、d=q及d=q-1、0和padding、零输入、伪字段和非幂调度均有对照。小规模直接选择另有63项测试。对合法原程序，Budget回退、不同proof-cache容量、随机中断／恢复、空底数、尝试上限、偶数和gcd预检均保持真实语义。

## 7. 实际交付、来源和重放

最终累计2b1821fa01a89eb4f0f45d99ba8bfab2a003fd42，入口START_HERE_STAGE97.md。stage97/portfolio_certificate.py、run.py、sample.py、PROOF.md、RESULTS.json、12PORTFOLIO_CASE、LABEL_CERTIFICATES、SAMPLING_AND_RECOVERY、ARITHMETIC_CERTIFICATE、CLI_SAMPLE、PROVENANCE及MANIFEST保留完整结果。

最终主程序362组命名检查、11615次实际不变BRC核心调用，包括820配置、63小单标签和12组完整Shor；不是11615次Shor实验。原主60537343974ns，最终累计bundle新克隆重放60990513100ns。仅递归排除elapsed_ns和actual_elapsed_ns，RESULTS加15份gzip科学内容全同，2份字节同；实际计时原件保存。1916父文件逐字节不变，24项新manifest、git fsck和两干净工作树核验。便携包独立解压并实际执行完整seed CLI，输出字节同；没有第三次全树重放。

规范核心bc7babbb9e890f6d5a7094430a5fbdccf66c77ad:src/enterprise_math/brc_weighted_recurrent.py；blob4e6b3132580e3cd70a20a0d8bd4d28792b961afb；SHA2567520822074b8f29e1c54f57b9543c043202db8bd7c6e27f3f1d6176028ac4a26。全部父状态和整数／有理BRC接口原样复用，不是把普通传播器换名。

bundle BRC_Heartbeat_bounded_portfolio_stage97_20260926.bundle：88,882,329字节，SHA256038f553c99cda8fb85339d4238770cf02d1af54404628da6cf3bede3b7be7685。Drive1CzBlUzTjhAzLe5t1Fg0Qf9S8iPttYHHs已上传、metadata读回、原始字节取回并逐字节及SHA一致。
ZIP Shor_Bounded_Portfolio_Stage97.zip：54,809,139字节，SHA256d58bb65a5fa1e59d6eed8f16c74cc4ef337b1ac424b7f709a93b4d2bffd24c91。外部回执/mnt/data/heartbeat97/DELIVERY.json。

Python3.11+标准库：python -S -m stage97.run；python -S -m stage97.sample --N 21 --bits 10 --base 2 --attempts 8 --cache 16 --proof-cache 64 --seed 9026。--label-budget 0安全回退，--proof-cache 0停用证明复用，--materialize-terminal支付完整后态恢复。

算法组合／单处理器交错已有Gomes与Selman的Algorithm portfolios（Artificial Intelligence126,43–62,2001）及arXiv1302.1541先行工作；短长步群作用参照Bach/Sandlund arXiv1612.03456。本轮只读出版商／官方摘要作背景，不称首创通用portfolio或Shanks方法。新增范围是本BRC证书的逐请求接口、相关后缀设置、含落败工作预算、小规模选择证明与完整Shor绑定。无独立评审、Lean、物理Born、量子硬件或速度优势声明。

## Next

本轮已关闭小输入无条件全调度开销，不再重复将该项当主要障碍。继续寻求更紧凑不变结构或有证明的选择准则，并以单轨迹、实际场求值和整数位长为独立成本；长例127比72更贵的负控制保留。父研究目标和数学准入不因保存本检查点而完成。
