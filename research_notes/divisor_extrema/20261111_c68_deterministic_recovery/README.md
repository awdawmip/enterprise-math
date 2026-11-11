# C68 确定安排反查复算包

[中文研究笔记](C68_RESEARCH_NOTE.md) 给出定理、模型、测量方式、证书范围和未决问题。包中 C64、C65、C66、C67、C68 是相邻目录。C64/inherited 含 C62/C63 模型说明和原生三态 BRC 概率核。C67 含本轮使用的单块及末隙前件。

需要 Python 3.12、SymPy 1.14、支持 C++17 和无符号 128 位整数的 g++，以及 GMP 的 C++ 开发库（包含 gmpxx.h，链接 gmpxx 和 gmp）。下面命令从 C68 目录运行。

~~~bash
python reproduce.py
~~~

程序在临时目录内重算全部 20 份 JSON，并与包内文件逐字节比对。可用 --group 单独选择证明组，--jobs 选择并行数。例如：

~~~bash
python reproduce.py --group twoblocks
python reproduce.py --group density
python reproduce.py --group decoder/extended
python reproduce.py --group conditioning
~~~

完整运行包含按库存比较 1,895,907,000 条双块词，精确首分歧搜索需展开逾一亿个前缀对。每项证明可以分别阅读、运行。区间证书用向外取整；有理根界、有限差分证书和素数域证书分别在对应笔记中列出判定依据。代码是可执行的精确证书，需保持 Python 及 C++ 的断言启用。

| 研究内容 | 说明与证书 |
|---|---|
| 原制备线、固定库存、所有后续的两次读数识别 | [主体证明](decoder/IDENTIFICATION.md) · [任意深度且最多 34 个 5](decoder/extended/EXTENDED_REGION.md) |
| 双块单读数及首隙渐近阈值 | [双块证明](twoblocks/HIGH_LANDING.md) |
| 每次只增加一个 5 的完整解码 | [实验与还原公式](twoblocks/TWO_STOCKS.md) |
| 增长末隙上的单列及单标量反演 | [单列编码](surplus/TERMINAL_WORDS.md) · [单标量](surplus/SCALAR_PRECISION.md) · [16,777,215 条词的精度](conditioning/CONDITIONING.md) |
| 一个增长隙及多个比例隙 | [增长位置的分类](arithmetic/MOVING_GAP.md) · [多档比例及精度](arithmetic/MACROSCOPIC.md) |
| 局部并列出现时在大规模中的密度 | [最短后缀和渐近展开](density/LIMITING_DENSITY.md) |
| 原两条历史，只给一个 H 时的全原像算法 | [分式曲线的反查算法](inverse/INVERSE.md) |

直接查询原两条历史的例子：

~~~bash
python inverse/incidence_inverse.py --checks ../C64/checks --inherited ../C64/inherited --prior ../C67/inverse --k 2 --H 269335961/264606236
~~~

这条命令返回唯一间隙向量 $(0,0,1)$。省略 --k 时，程序用 C67 的严格规模界遍历所有可行规模。
