# Heartbeat99 — 共同根平方的一次完整配对：执行与后态保真

Progress-Event-ID: HEARTBEAT99-EXECUTED-ONE-PAIR-SQUARE-20260926
Status: AUTHOR_DERIVED_AND_EXECUTED / SHARED_CONTEXT / UNREVIEWED / NOT_ADMITTED
Global read: f57848c210eee1e9adea1a9f6b2d87b7ca11130a
Source read and publication preflight: 6cc27a05bc0e4ab50b9ee9f7f8995f62563eb2dc
Parent executable: 2b1821fa01a89eb4f0f45d99ba8bfab2a003fd42 (Stage97)
Inherited theorem: research_notes/HEARTBEAT98_ORDERED_LOW_RANK_WORD_20260926.md at the Source read above.
Inherited contribution source: HB90-0de6b47ad07848a1b6e8347fd5156ca6, not a service/platform identity.
Run: HB99-e4b038a1f99a4daeade452bb39974622
Research-Activity-ID: 未取得 / REGISTER_PENDING。未借用他人session或CLAIM，未重放历史报告的登记拒绝。本文是中立科研保全，不是正式Result或独立审阅。

## 1. 当前实际执行，不改变原数学对象

本轮本地执行可用。先核验Stage97父bundle为88,882,329字节、SHA256 038f553c99cda8fb85339d4238770cf02d1af54404628da6cf3bede3b7be7685，再从本地包克隆。1941个父追踪文件保留原字节。Stage98平方公式是继承的已完成符号结果，不再次认领；本轮新增独立求值适配器、真实BRC系数与正交证书、完整基列/后态执行和成本测量。

P000六原生空间轴、独立时间、BRC-only、完整61模式、原12组输入、实际phase3=phase4同根两遍、其它相位次序、CF-only和随机/失败语义均保持。二次观察、标准QFT目标及条件均匀外部随机接口仍为BORROWED_REFERENCE。内部模式和程序调用次数不冒充空间维数或心跳。

## 2. 一次配对精确执行同一个W平方

原实际W=(2ee^T-I)(2zz^T/D-I)，z含全部补全分量，D=z^T z=S^2。令a=z0、h=z^T x，则

    (W^2 x)0 = [(D^2-4a^2D)x0+(8a^3-4aD)h]/D^2,
    (W^2 x)i = xi+zi[4aD x0-8a^2h]/D^2, i>0.

这是同一个实际门两次作用的代数展开，只需一次完整h。新原始整数分子与旧PowerRotor(W,2)逐项相同，den仍为D^2；原reduce_state的二进规范分母及recipe word指纹不改。逆作用使用W^-2=D0 W^2 D0，保留全体符号；不是把名义相位重新拟合。

常系数通过原stage83.signed_dot_brc的正两边路径及符号观察实际取得，首输出/尾修正的两输入线性列又通过rational_matrix_columns执行。完整z平方预算经相同BRC配对确认。E=(e,z)，G=[[1,a],[a,D]]，W^2=I+EA E^T/D^2，其中A=[[-8a^2D,16a^3-4aD],[4aD,-8a^2]]。实际BRC乘积核验D^2(A+A^T)+A^TGA=0。

生产求值是这些固定列与完整带符号配对的已证明线性/双线性展开，和父FixedRotor的层级一致；不是仅用Fraction或改名便称BRC。核心调用与动态行求值分别计数。没有新三角、π、理想QFT或通用数值传播器。

FusedSquareRotor仅接受已验证的原power=2与根身份。bank只替换slot3的求值器，slot4及其它相位对象不变；power、原primitive word和硬件门数保持。一般多方向有序字编译器尚未实现。

## 3. 完整空间、记录边界及原始字对照

正向/逆向各61个基输入共122项，分别比较旧两次apply_numer的原始整数分子，并另实际执行原两遍完整primitive word作独立路线核验；真实逆作用恢复完整输入。带符号多模式行的BRC配对、范数、散射及受控直和也核验。非法维数/布尔振幅/错误power或根绑定被拒绝。

若x0=0且z^T x=0，真实W^2x=x。实际构造非零尾向量x_j=z_k、x_k=-z_j，BRC配对为零但状态非零。只保存(x0,h)而删除原x会丢掉合法状态；本轮压缩的是操作，不是场。

补充程序使用原stage83.recorded_row的实际BRC指针，在W与W之间对首模式留下记录，两个结果均保留，再执行第二个W。令c=(We0)0，无中途记录概率为(2c^2-1)^2；有真实中途记录且不按结果筛选时为c^4+(1-c^2)^2。差严格为2c^2(1-c^2)>0，约0.24999999992583563，BRC有理界0.24<差<0.26通过。这是两个不同协议，不是模型错误率；不能跨真实读取融合。

新平方连续八次与原W十六次逐前缀完全相同，结果严格不等于恒等；按真实逆序恢复初态。名义W^16=I仍未被强行加入。

## 4. 冻结Shor与旧快照兼容

原Stage97完整validator代码对象复用，候选绑定新slot3，参考显式绑定旧PowerRotor，避免两侧都误用新代码。工作置换、证明引擎、其它相位、读取与CF/attempt不改。候选运行以后才加载冻结CASE。

12组全部控制概率、前缀权重、逐状态完整61模式振幅/规范分母/hash、尾项和CF成功/失败精确一致。表示新增误差0；10位配置到理想Shor仍继承3699/68719476736，约5.38e-8。标准21/a2/t10分母仍5409位，P(128)=1/131072，原单次CF成功权重约0.330843218193906427不变。

四组固定种子逐事件/recipe与旧实现一致：15/2/t4 seed1为k0、ZERO_PHASE_RETRY；21/2/t6 seed41为k11、因数3/7；21/2/t10 seed9026为k171、因数3/7；35/2/t6 seed3为k16、NO_FACTOR_THIS_READOUT。旧snapshot在新程序无新随机数恢复完整后态；抽样前随机源耗尽保留相同父态/历史。空底数和有限重试上限保持。固定种子不作无偏成功率证据。

## 5. 真实减少与没有减少的成本

完整回归控制读取加共享后态恢复的square调用：21/2/t6为90、21/4/t6为90、21/2/t10为1530、33/2/t6与33/5/t6各134、35/2/t6为130。每次旧完整配对2次、新1次；标准21因此3060降到1530。另6组在本次执行路径没有调用该slot，无此收益。原语义根字行仍为标准21读数6125/全恢复13803，不能改记成配对数。

标准21平方输入分子最大5184位、原始输出最大5441位；最终规范分母5409位不变。平方自身D^2为257位分母，不代表完整计算只需257位。系数更长、整数乘法、诊断、原场和日志仍有成本。物理根字仍两遍，没有硬件门数减半结论。

有限微计时取实际回归捕获的完整行，每种7批、每批80次，交替先后执行并核对输出。旧apply_numer与新不带诊断bookkeeping的evaluate内核比较，原中位批耗时（ns）：1位输入1555691/586497；1468位4237680/2570103；5184位11440267/7714234。分别为旧/新。原批数据和完整行hash保留，重复运行计时另存；不是端到端Shor、总RAM或所有机器的速度保证。

## 6. 交付与实际重放

本地累计f614af10453b382948f18bf96d3a71a6410c6f2e，START_HERE_STAGE99.md。包含stage99/fused_square.py、run.py、sample.py、boundary_checks.py、PROOF.md、RESULTS.json、12FUSED_CASE、COMPLETE_COLUMN_CERTIFICATE、SAMPLING_AND_RECOVERY、TIMING_CORPUS、BIT_COST、ARITHMETIC_CERTIFICATE、BOUNDARY_CHECKS、BOUNDARY_BRC_CALLS、PROVENANCE和MANIFEST。

主735项命名检查/998次实际BRC；边界14项/98次；合计749项/1096次。基列和重放不当独立实验累计。主原60691267473ns、最终bundle新克隆61063258378ns；边界原600691730ns、重放592401349ns。20份结果文件科学内容一致，3份字节一致；仅排除elapsed_ns、actual_elapsed_ns、compile_elapsed_ns、old_elapsed_ns、new_elapsed_ns、old_median_ns、new_median_ns七类真实计时字段。1941父文件、28manifest项、两个干净树及git fsck通过。新便携包独立解压/manifest/完整seed CLI实际执行，输出字节相同；没有第三次全树运行。验证脚本初稿误把manifest字典当裸hash比较，已修正外部验证器后全量核验，原科学文件未改。

bundle BRC_Heartbeat_one_pair_square_stage99_20260926.bundle：90256494字节，SHA256 6176db12cb0774907db760892525ee9378e868ddb0fd73894086b345412cbb01。Drive 1aQDC6XAHYx4yDmjIOyqw7dA9DdpZQGg7上传、metadata及完整原字节取回cmp/SHA一致。
ZIP Shor_One_Pair_Square_Stage99.zip：56199137字节，SHA256 28f62a7ebe110c0563d3a01f790aa3d28f707384a272820a56efbee16030195a。外部回执/mnt/data/heartbeat99/DELIVERY.json。
Python3.11+标准库：python -S -m stage99.run；python -S -m stage99.boundary_checks；python -S -m stage99.sample --N 21 --bits 10 --base 2 --attempts 8 --cache 16 --proof-cache 64 --seed 9026。CLI另计123次BRC，不混为主检查数；仍k171、因数3和7，到控制读数语义根字行82。

规范核心不变：bc7babbb9e890f6d5a7094430a5fbdccf66c77ad:src/enterprise_math/brc_weighted_recurrent.py，blob4e6b3132580e3cd70a20a0d8bd4d28792b961afb，SHA2567520822074b8f29e1c54f57b9543c043202db8bd7c6e27f3f1d6176028ac4a26。继承Stage98/89/80/83与0C08F0及Stage91–97的实际接口，不认领这些父成果。一般紧凑反射乘积已有Schreiber/Van Loan(1989) DOI10.1137/0910005及Netlib DLARFT官方文档；只读出版商摘要/官方HTML，不运行LAPACK、不声称首创一般WY或穷尽文献。无独立评审、Lean、物理Born或量子硬件/速度优势声明。

## Next

Stage98最小W平方执行欠项已关闭。下一单元是为少方向、较长真实有序字建立完整系数编译，逐字母核验精确相位2等同域合同，并比较编译/缓存、真实配对、位长和完整后态成本；不重做已通过的平方接口，不跨读取，不以主分量或范数替代残差状态。一般有序编译仍待执行，父数学目标及正式准入未整体闭合。
