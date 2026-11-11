# C64 复算

从[中文研究笔记](C64_RESEARCH_NOTE.md)开始；实际尾读数的全排名和四项概率读取见[观测排名与两尾公式](OBSERVED_RANKS.md)。本文比较 C62 自然条件于完整共同词后的状态总变差，并用三个匹配尾的实际概率检验最优安排。高段引理、前部扰动的解析式与隐藏双字的证明分别见 [HIGH_AND_TAIL.md](HIGH_AND_TAIL.md)、[MOVING_FOURTH.md](MOVING_FOURTH.md)、[TWO_SYMBOL_SYNC.md](TWO_SYMBOL_SYNC.md)。

以下命令从本文件所在目录运行，参考环境为 Python 3.12、SymPy 1.14.0。仅单调性脚本使用 SymPy。下载包自带继承材料。在项目仓库内，使用既有 C63 程序 experiments/divisor_extrema/20261111_c63/numeric/certify_schedules.py 作为 --model 路径，并把项目 src 目录传给 brc_crosscheck.py 的 --inherited。数据为有理数、严格区间或明确标为下取整的整数值。

~~~bash
python checks/fourth_certificate.py --model inherited/certify_schedules.py --output fourth_rerun.json
python checks/observed_four.py --model inherited/certify_schedules.py --output observed_rerun.json
python checks/two_tail_observables.py
python checks/cut_stocks.py --model inherited/certify_schedules.py --output stocks_rerun.json
python checks/check_high_tail.py
python checks/check_moving_fourth.py
python checks/suffix_limits.py
python checks/observable_minimum.py
python checks/brc_crosscheck.py --inherited inherited
python checks/verify_55.py
python checks/verify_mixed.py
~~~

fourth_certificate.py 每格保留六条路径下界，覆盖一至四名。finite_certificate.py 提供共同矩阵工具，也可以使用相同的 --model/--output 参数独立运行其保留四条路径的前三名证书。cut_stocks.py 对截面 2 至 96 的全部非基准库存作向下取整的完整下界计算。高库存的无界部分使用 C63 已证不等式，推理见正文。本包所附 C62、C63 文本是前件证明，C64 的复算命令核验本轮新增步骤。

原版正权 BRC 内核来自项目 de41b8cd9e6b0ea52345d5f669af924f9379318a 的 src/enterprise_math/，包括 brc_histogram.py、brc_rational_holonomy.py 和 brc_weighted_recurrent.py。brc_crosscheck.json 记录原件标识与实际运行计数。
