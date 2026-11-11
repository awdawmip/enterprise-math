# 由真实业务答复决定下一次复制地址

主报告 REPORT.zh-CN.md。独立复验包中，当前目录为 branchlife/，与继承的 copylife/、optimization/ 等保持相对位置。Python 3.12 标准库。在包根执行 `python3 -B verify.py --replay` 可重跑归档的六组科学结果。

|文件|核对内容|
|---|---|
|guard_proof.md, guard_checks.py|逐分支联合支撑、路径相容、按线性矩阵路由与秩、遗忘后的精确代价。|
|oracle_notes.md, oracle.py, oracle_checks.py|有限无环业务、世界集合/来源域两种递推、单一事前策略与先读门槛。|
|path_checks.py|路径一致的逐准备证书；真实回答偏离时在现场安全回退，与顺序递推独立比较。|
|memory_proof.md, memory_checks.py|非线性标记族的分割与询问树；在一套原核库存上比较线性与单标记族。|
|family_checks.py|一般多槽条件复制族：独立化简的精确极小极大计算和二槽、六槽全体剩余码的原核实跑。|
|kernel_notes.md, kernel_checks.py|原核按实际布尔和完整键分岔、错误复活、保守费用、真实保护区间。|

每个 checks.py 均可独立运行，生成对应 _results.json；传 --out 可指定结果文件。程序、报告、证据索引与来源说明保存在同一不可变科学目录。数学最优性的观察接口、单位和量词见报告。
