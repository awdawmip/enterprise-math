# 复算 C80

使用 Python 3.11 或以上、mpmath、SymPy，以及支持 128 位整数的 C++17 编译器。下列命令均从本目录执行。

~~~sh
sha256sum -c SHA256SUMS
python3 check_native.py
python3 check_fold.py
python3 check_adaptive.py > /tmp/c80_adaptive_replay.json
cmp adaptive_512.json /tmp/c80_adaptive_replay.json
python3 check_window_increments.py > /tmp/c80_window_replay.json
cmp window_increments.json /tmp/c80_window_replay.json
~~~

check_native.py 从原制备态出发，逐因子重新计算三条完整尾概率，对 c=8 和 16 的全部安排各检验四个库存，共 592 个准确有理数。核对的 C79 函数保留原来的有向制备投影。check_fold.py 以符号运算核对移动折叠的位置、导数系数和周期切点方案。check_window_increments.py 在全部选定库存上用定向区间检验四库格号，并以有理数检验偏移曲率公式的离散矩。

[全平移扫描复算指令](grid/PHASE_GEOMETRY.md) 含两种事件扫描及 85 个小例的逐格交叉核验。JSON 中的均值、标准差为精确向外包围区间，整数极值及共同唯一条数可直接使用。

[配对弧证书](arc/ARC_PROOF.md) 给出区间验证和有理重放方式。可在 arc 子目录下执行 python3 replay_arc.py，缺省复现二次多项式控制项；欲复现更高次，以该目录中的 d*.json 次数作参数，例如 python3 replay_arc.py 5 6。高阶耗时随列数和工作位数增长。所验证的秩只对应文中指定分支盒。

预设原点次数定理与四库存增量定理具有解析证明；有限实验验证指定输入及实现。项目原物理读数的有限库公式与前置全库定理分别来自 [C79](https://github.com/awdawmip/enterprise-math/tree/9d76acb849471e4b8c411a5de04066679abca8d8/research_notes/divisor_extrema/20261116_c79_critical_window_geometry) 和 [C78](https://github.com/awdawmip/enterprise-math/tree/24881e361378245e45f27919836ca1c9db48d04f/research_notes/divisor_extrema/20261116_c78_nearby_stock_precision)。
