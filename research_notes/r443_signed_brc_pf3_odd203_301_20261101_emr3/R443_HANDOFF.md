# R443 接续：signed BRC PF3 奇数尾段

来源：R441 Schur/LR 无限Toeplitz完整归约；R442 已精确检查99—201奇数行。R443 本轮只在同一 signed BRC 辅助标量模型上计算奇数 r=203—301 的50行。

已经完成且不重复：用双整数公式检查12,550项系数；完整列组合共140,218,875个一至三阶Schur归约子式严格正；三阶138,604,200项由严格误差界认证且33,812项整数抽查，0回退；r203另由整数法完整1,414,909项交叉核验。全部50行具有24项Leibniz直接算出的严格负四阶子式。最大PF阶数=3（此50行），仍属作者侧未审阅结果。

代码路径：R443_GENERATE.py -> R443_INPUTS.txt（2,349,510字节，SHA256=58110cfb7715a59adce6b9266623567870d7a2bff13944fc2fece2ea76aa11c9）-> R443_CERTIFIED.cpp -> R443_CERTIFIED_STDOUT.txt；R443_PF4_WITNESS.py 独立输出负证；R443_INTEGER_EXHAUST.cpp 为完全整数锚点。全部校验和、严格误差界与复现命令见 R443_PROOF.zh-CN.md / R443_EVIDENCE.json。

下一确切问题：针对所有奇数 r>=99 的三阶普通Schur子式，建立随 r 参数变化的统一非负证明，或在 r>=303 找到最早的精确负例。优先考虑 Catalan 比率结构与有理函数不等式；不要将有限样本当无限归纳。正式 Source owner 查询 CONTROL_QUOTA、定向研究 authority_granted=false，保留 REGISTER_PENDING、UNREVIEWED、NOT_ADMITTED，不冒认CLAIM/Result/独立Review，不改变P000或ACTIVE。便携材料属同一PR的中立存储。
