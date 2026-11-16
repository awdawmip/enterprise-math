# C77 复算说明

从本目录执行以下命令。Python 3.10 以上、SymPy、支持 C++17 和无符号 128 位整数的编译器，以及 GMP 的 C++ 开发库供全部核验使用。

```bash
python3 reproduce.py
```

程序先检验包内每个源文件的 SHA-256，再运行各项复算并逐项比较结果。check_critical_three.py 依有理矩阵准确计算三维相位盒的体积。check_three_precision.py 输出的三组缩放宽度中的对数是数值诊断，其他结论按相应证明和整数证书判定。总扫描的逐行记录已入包；需要重做新增库存的全量扫描时，在同一目录运行

```bash
c++ -O3 -std=c++17 two_blocks.cpp -o /tmp/c77_two_blocks
/tmp/c77_two_blocks 3201 3300 > /tmp/c77_rows.txt
cmp /tmp/c77_rows.txt finite_c3201_3300.txt
```

下列两种解码接口均接受一个已经测得的准确有理数。由用户给出原库存上界 c、扩大库存 n 和实际测量 g。复算包的 check_far_decoder.py 和 check_lattice_decoder.py 各自给出端到端样例。

|输入范围|入口|运行准备|
|---|---|---|
|\(n\ge72\max(c,100)\)|lattice_decoder.decode(c,n,g)|将 kernel_lll.cpp 编译为同目录的 kernel_lll，命令见文件头及 LLL_IMPLEMENTATION.md|
|\(n\ge120\max(c,100)\)，或通过逐输入充分判据|far_decoder.decode(c,n,g)|Python 标准库即可|

任意双库存定理依赖的上轮已证命题，在 ARBITRARY_STOCKS.md 和主报告给出不可变源记录。C76 的对数高度截断、整数落点连续延拓、C74 的单次穿越在本轮沿用。科研记录的出版状态为作者证明和可复算自检。
