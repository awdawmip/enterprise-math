## 复算 C79

在解压后的目录内运行。Python 3.10 或更高版本、SymPy（参考环境为 1.14.0）以及支持 128 位中间整数的 C++17 编译器即可执行全部检查。下列入口先核对清单 SHA256SUMS，再逐字比对 7 份记录。四种库存的外推检查读取三条真实尾。平移剖面的计算直接用逐因子三态有理数，完整遍历每个轴的全部断点；分别取面积加权的均值、所有平移上的最小和最大独占数。遇精确边界时按半开格取右侧。

```bash
python3 reproduce.py
```

单库存复算的默认入口读取 100 行大库存记录并编译运行小库存核对。要从零重跑大库存的所有模板，可在同一目录执行：

```bash
c++ -O3 -std=c++17 two_blocks.cpp -o two_blocks
./two_blocks 3401 3500 > finite_replay.txt
cmp finite_c3401_3500.txt finite_replay.txt
```

### 研究与证据索引

|结果|证明或复算|
|---|---|
|临界窗口下最近同格对手的距离|[COLLISION_DISTANCES.md](COLLISION_DISTANCES.md)|
|连续读数密度与面积上界的首项|[WINDOW_CAPACITY.md](WINDOW_CAPACITY.md) · [check_capacity.py](check_capacity.py) · [check_stock_capacity.py](check_stock_capacity.py)|
|固定观测次数与重复平移设计|[FIXED_STOCK_BANK.md](FIXED_STOCK_BANK.md) · [REPEATED_ENDPOINT_PHASES.md](REPEATED_ENDPOINT_PHASES.md)|
|进位、格内小数和外推|[CRITICAL_PHASES.md](CRITICAL_PHASES.md) · [LOCAL_TEMPLATE_PHASES.md](LOCAL_TEMPLATE_PHASES.md) · [GROWING_EXTRAPOLATION.md](GROWING_EXTRAPOLATION.md) · [check_phase_carries.py](check_phase_carries.py)|
|三固定库存的全域三次律|[THREE_GLOBAL_CUBIC.md](THREE_GLOBAL_CUBIC.md) · [TURNING_MINOR_SUBLEVEL.md](TURNING_MINOR_SUBLEVEL.md) · [check_three_global.py](check_three_global.py) · [check_turning_minors.py](check_turning_minors.py)|
|有限两库存的所有平移|[check_offset_profile.py](check_offset_profile.py) · [offset_profile.json](offset_profile.json)|
|有限单库存准确识别范围|[check_finite.py](check_finite.py) · [finite_c3401_3500.txt](finite_c3401_3500.txt)|

进位记录保留全部有限整数差，极限支持以外的取值也保留。每一项报告的二进制舍入格号都由向外包围区间的两个端点得到同一整数后才采用。平移均值用整数算术精确累加，记录保留分母为 $10^8$ 的上下包围。小库存下受格偏移影响的独占比例与渐近定理中尚未确定的极限各有不同量词。

原模型及前置定理按固定版本取 [C78](https://github.com/awdawmip/enterprise-math/blob/24881e361378245e45f27919836ca1c9db48d04f/research_notes/divisor_extrema/20261116_c78_nearby_stock_precision/C78_RESEARCH_NOTE.md) 与 [C77](https://github.com/awdawmip/enterprise-math/blob/70285a17eb30dffe4cb4ba599f49b0f6666f96b0/research_notes/divisor_extrema/20261116_c77_arbitrary_stock_pairs/C77_RESEARCH_NOTE.md)。
