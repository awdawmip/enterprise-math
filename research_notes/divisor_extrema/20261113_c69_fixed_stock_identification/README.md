# C69 固定库存反查复算说明

[完整中文研究笔记](C69_RESEARCH_NOTE.md)给出定理、数据接口及开放问题。复算包包含本轮 C69 以及所引用的 C64、C65、C66、C67、C68 目录。C64/inherited 中保存 C62/C63 的模型与原生三态核。实验以 Python 3.12、SymPy、C++17、GMP 与 64 位 Linux 为环境。C++ 有限域核使用 128 位整数，需 g++、gmpxx 与 gmp 开发库。保留 Python 及 C++ 的断言。

解压后在 C69 目录运行以下命令，全部 18 份 JSON 都会从头生成，与保存文件逐字节核对。大规模单列检验含数十亿次模点测试，支持分项执行。

~~~bash
python reproduce.py
python reproduce.py --group arithmetic
python reproduce.py --group singleh
python reproduce.py --group depthtwo
python reproduce.py --group cert/column_35 --jobs 3
~~~

文件的子目录与对应证明如下。

| 目录 | 读数与证明 |
|---|---|
| [arithmetic](arithmetic/LOCAL_DENSITY.md) | 两个原始精确 H；2 进有理中心、各深度的秩证书与全库存计数 |
| [singleh](singleh/ONE_H.md) | 只报告一个准确 H；三个固定深度的密度一定理 |
| [depthtwo](depthtwo/BULK_PRECISION.md)、[critical](critical/CRITICAL_WINDOW.md) | 双块舍入阈值、临界区域的唯一格面积及近碰撞界 |
| [cert](cert/SINGLE_COLUMN.md) | 单个可能不带尾标的联合概率比；有限库存的全族反查、若干无界库存的构造与跨库存校准 |

区间证书的边界向外取整，有限域中的每个必要除法均验证分母可逆。整数、分数和模运算用于严格判定。单独标为渐近拟合的小样本只用于核对公式的实现。
