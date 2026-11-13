# C70 复算

[中文研究笔记](C70_RESEARCH_NOTE.md)列出准确问题、定理与边界条件。下载包包含 C64 至 C70 的证明和源码，C64/inherited 包含 C62/C63 的模型与证明。用 Python 3.12 和具有 128 位整数支持的 g++（C++17）解压后运行：

~~~bash
cd C70
python reproduce.py
~~~

程序重算五份 JSON，逐字节比对已保存证书。其中 one/verify_one.py 会编译并运行单块全库存核；two/eventual_two.py 和 one/raw_rank.py 使用 C67 的原生三态递推；deep/eighth_rank.py 复用 C69 的有限域导数核；order/sparse_stocks.py 用准确有理数核对有限桥上界和 12,805 个小库存柱集。可按需直接运行各脚本，前两类脚本的 --prior 参数分别取 ../C67/joint、../C69/arithmetic，详见源码。解析定理依赖各证明中的一般恒等式与不等式。有限检验的范围见各节，库存阈值的定量衔接仍待解决。
