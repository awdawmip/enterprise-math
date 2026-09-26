# Heartbeat93 — 碰撞优先、完整行复用与可恢复的终端后态

Progress-Event-ID: HEARTBEAT93-COLLISION-FIRST-EXACT-ROW-REUSE-20260926
Status: AUTHOR_DERIVATION_AND_EXECUTION / SHARED_CONTEXT / UNREVIEWED / NOT_ADMITTED
Global read: 8446003d2eadf806d9589f77d1314dd3ac250d14
Source read: a1eded9795959c039b6d1ce8e16ecb8a620629c0
Publication preflight: 8d4e9c12f7492316b825e96423bc0ee36ccdee22；期间仅新增另一研究线文件，本轮不修改它们。
Local conversation provenance: HB90-0de6b47ad07848a1b6e8347fd5156ca6
Run: HB93-b1d1784deb8b4754bb03cd2514cdb6eb
Research-Activity-ID: 未取得。旧登记拒绝只有对话报告，不重放、不借用他人身份。可移植材料保存不授session/CLAIM/数学准入。

## 1. 固定父线与新增范围

父累计868ebb6f499fcc9af22a8ee97fa752ef9e8cc65f；输入bundle为82515243字节，SHA256 8e8e332d6b7b138299bce4557b4dfd4f3e74ad9dcc3515a17aef5ef787088078，先核后本地克隆。1830个父线追踪文件逐Git blob及最终新克隆字节核验不变。旧Stage76独立提交9510ec8d不在此次供应的Stage92对象数据库中，因此不声称本轮已恢复该独立ref；全部供应父材料原样保留。

全部12组低bit Shor输入、原phase3=phase4实际字两遍、其他相位次序、CF-only、失败与随机契约、工作标签和完整61实模式不改。P000六原生空间轴、独立时间、BRC-only、残差保真保持；二次概率、QFT参照和条件均匀外部随机源仍为BORROWED_REFERENCE。

本轮复用Stage92整轮K_r=(I+(-1)^r U)/2、Stage91按需工作双射、Stage89共同生成器与0C08F0作者终端调度，不重新宣称首创。新增为碰撞行先求值、完整行精确复用、带已选结果的后态表达，以及终端读数与完整后态交付两个不同成本边界。

## 2. 当前读数只预求碰撞源行

写v=sum_y |y> n_y/d，d为正二幂，S为非零工作支持，sigma为原全域可逆工作标签规则。按真实历史依次执行的内部字T=(A_last ... A_first)/Q，Q为各认证字分母之积。定义J={y in S:sigma(y) in S}。

A=sum_y<n_y,n_y>，R=sum_(y in J)<n_sigma(y),q_y>，其中q_y=A_word n_y。准确当前概率为p0=(A Q+R)/(2 A Q)，A>0。只需先对J中的源行执行原有序字；其余行仍以完整输入和真实字保留，绝不当作零或恒等。

已选结果r后，目标z的完整子行是(Q n_z+(-1)^r q_(sigma^-1(z)))/(2dQ)，然后用原reduce_state规范表示。两个支持的对称差上只有一臂，正交T保证非零；交集处已求过相位，可精确判断相消。因此选中子态的支持也可在未求其他行时确定。

原BRC和差列、完整符号配对及其线性/双线性扩展不变；没有外加普通数值传播器或三角计算。一般保真由逐行恒等式及归纳证明，具体正前缀还直接执行_pair核验范数和交叉量。

## 3. 延迟不是消除计算；整行复用是另一项优化

逐源、无共享、无逐出的本实现中，若有s源行、c碰撞源行、g个展开根字，则读前c*g次、交付完整后态还需(s-c)*g次，总量仍s*g，与所选结果无关。这是本求值器的成本恒等式，不是任意算法的普遍下界。

真正的复用以完整整数行为键：n_y=f_y r_y，f_y为带符号二幂，r_y第一非零项为正且至少一项奇数。只在全部61分量精确相同、实际有序字相同的条件下共享A_word r_y。原工作标签、比例系数、符号和所有尾项不合并。缓存仅在本prepared round内，清空后可按原输入/字重算；按范数、主分量或尾范数合并被拒绝。

12组完整后态中，不共享的延迟版本总根字行调用与Stage92逐项相同。共享后的实际完整总数：21/a2/t10为13812->13803；21/a2/t6为472->467；33/a2/t6为774->735；35/a2/t6为751->733。不能将读前/读后分账称为整机或硬件同倍率加速。

## 4. 可恢复表达与真正的终端节省范围

SelectedRecipe保存父行、父分母、原历史、实际选择结果、字序和指纹，可求某一子行或完整后态。JSON恢复要匹配父模型/程序/字/概率并实际重验，不调用随机源。哈希是完整性检查，不是平台签名。

随机源在选择前耗尽，保留父态和旧历史；选择已发生但数组尚未完成，必须保留新结果和精确表达，不重新抽样。这与把当前m、gamma当未来状态完全不同。

新增TerminalOnlyDriver仅在最后一轮允许后态留作表达：前t-1轮仍完整物化。最后以后只读控制串和原CF/gcd，不做新工作/内部数值观察时，p0与选择已足够。最终共同规范分母若尚未计算，明确标null而不猜；原分母/实际字足以以后恢复。

标准21/a2/t10的512个正权末前缀全部无碰撞。全树得到全部控制读数时执行6125次根字行，随后为验证而强制展开全部终端态追加7678次，总数13803。旧完整版本13812次。对21/a4/t6，末层全部重合，终端与完整均为467次，无此节省。12组终端测试均先冻结控制概率和计数，再实际恢复全部子态核对hash/分母/尾量。

单轨迹seed9026的21/a2/t10：新终端只读执行82根字行，旧完整后态101次；k171、CF因数3和7相同，三个末态源行留在表达中。四组演示中两组没有因数，失败原样保留。JSON表达在新建相同程序中恢复，不给新随机数，完整后态与原记录轨迹完全相同。固定种子不是无偏频率证据。

## 5. 同读数、同范数仍可能是错误补态

合法21/a2/t6、history=(1,0)接口，父work1和work4均为(e0+e1)/2。模乘4将它们送到4与16，work16不参与当前交叉量。若正确计算读数后，把work16的真实T行错当成原输入行，当前p0和子态总范数都仍相同，但下一轮p0约为正确0.826640741252268、错误0.876619938943063；BRC平方/配对证书验证差绝对值严格在49/1000与1/20之间。

这是相同认证接口上的合法边界准备，不说标准Shor初态必生成它。它证明非碰撞只说明当前读数不需要此数值，绝不是以后可以按恒等处理。

## 6. 全部回归、实际成本与边界

主程序同时执行共享、不共享和Stage92，3432个孩子逐完整整数幅度/分母相等；12组全部终端概率、规范分母、尾项、61模式hash、各前缀与CF成功/失败精确一致。终端补充为相同12组的第二观察边界，不计成24种独立输入。21/t10完整规范分母仍5409bit，P128=1/131072，成功权重及到理想Shor的3699/68719476736界不变。

源行缓存和表达都有成本；最大原始未约分分母/行整数位长另记。单前缀支持、全部日志、静态bank、输入/孩子并存和恢复成本均不能免费忽略。没有减少硬件门序，不宣称一般多项式经典分解、量子加速、物理Born或独立评审。

## 7. 实际交付

累计b8b53fb56128337b9b200b3f0971615794483720，入口START_HERE_STAGE93.md。stage93/collision_first.py、terminal_only.py、run.py、verify_terminal.py、sample.py、PROOF.md、RESULTS.json、TERMINAL_RESULTS.json、12LAZY_CASE、后态/驱动/算术证书及来源/边界/manifest。

最终主427项命名检查、904次实际BRC；终端补充88项、261次，合计515项、1165次。原主66472152341ns，新最终bundle克隆主66831593609ns；终端40134797557ns、39995882051ns。只递归排除elapsed_ns及actual_elapsed_ns，两份JSON与17份gzip科学内容全同，3份gzip字节同；其余实际计时保留。1830父文件、33项manifest、git fsck、两树干净核验。便携独立解压/全部新文件/完整seed CLI通过且CLI字节同，没有第三次全叶重放。

规范BRC核心不变：commit bc7babbb9e890f6d5a7094430a5fbdccf66c77ad，src/enterprise_math/brc_weighted_recurrent.py，SHA2567520822074b8f29e1c54f57b9543c043202db8bd7c6e27f3f1d6176028ac4a26。早求读数/延迟求值/线性缓存的一般思想不称首创；Griffiths/Niu quant-ph/9511007只读官方摘要作终端背景。

bundle BRC_Heartbeat_collision_first_stage93_20260926.bundle，84533447字节，SHA256638dc71f0a286125438a5eee56232b517a3dd7655f1fc49607714dd4282fac8f。Drive 1BwfQvzgjlAy6nfgxkWqpArdBm-dBg76A已上传、metadata读取、完整原字节取回cmp/SHA一致。
ZIP Shor_Collision_First_Stage93.zip，50160374字节，SHA256d18e6d126ac3aa6f42164f0c52a06824337f02948cebbcc197e821d2b5b27e71。Python3.11+标准库：python -S -m stage93.run；python -S -m stage93.verify_terminal；python -S -m stage93.sample --N 21 --bits 10 --base 2 --attempts 8 --cache 16 --seed 9026。默认末态保留表达，--materialize-terminal真实展开，--no-row-sharing禁用整行复用。外部回执/mnt/data/heartbeat93/DELIVERY.json。

## Next

继续研究真正减少实际支撑/字长/位长的结构，而不是把延后求值冒充总运算消失。若从末态表达新增工作/内部观察，应按请求恢复所需关系；不能再次抽取已发生的结果。并行new_word_compiler新增文件仅在发布前比较中识别，不计为本轮阅读、运行或验证。父数学目标和正式准入没有由本检查点自动完成。
