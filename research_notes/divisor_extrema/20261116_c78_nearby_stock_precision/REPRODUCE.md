# C78 复算说明

在解压目录运行以下命令。使用 Python 3.10 或更高版本、SymPy（本次为 1.14.0）和具有 128 位无符号整数类型的 C++17 编译器（如 GCC 或 Clang）。Python 的有理区间程序仅依赖标准库；两个符号核验使用 SymPy。

```bash
python3 reproduce.py
```

脚本先核对 SHA256SUMS，再逐字比对十二项计算与已保存的见证。它重算主证明的欧拉恒等式和幂次、Hessian 非退化、替代 Fourier 证明的有限检查、单库别名弧的有理区间、三库存立方体的相位体积，以及四种库存下的全部普通舍入格。最后核对 100 行大库存清单及库存 2 至 18 的 969 项逐因子对照。每个大库存的完整枚举在下一条命令单独重跑，可与逐行记录直接比较。

```bash
c++ -O3 -std=c++17 two_blocks.cpp -o two_blocks
./two_blocks 3301 3400 > finite_replay.txt
cmp finite_replay.txt finite_c3301_3400.txt
```

以两个块的落点 $v,w$ 遍历 $2\le w\le v\le c$，每个库存只保留本库存的指纹。程序遇到零分母、计数不符或同库重复会异常退出。若两条安排的准确 $g$ 相同，则 $g+1/g$ 的模指纹必同。因此各库存无模重复可推出各库存准确 $g$ 两两不同。单次大库存枚举的内存占用随 $c^2$ 增长。舍入计算用三条真实尾分别取极值；有限比较的格编号定义为 $\lfloor 2^p g+a/b\rfloor$，偏移分数见 critical_bins.json。可用下列指令重算指定规模。

```bash
python3 critical_bins.py 8 64 128 256
```

主证明的 C77 引用固定于 [近库存必要界](https://github.com/awdawmip/enterprise-math/blob/70285a17eb30dffe4cb4ba599f49b0f6666f96b0/research_notes/divisor_extrema/20261116_c77_arbitrary_stock_pairs/NEAR_STOCK_PRECISION.md)、[仿射刚性](https://github.com/awdawmip/enterprise-math/blob/70285a17eb30dffe4cb4ba599f49b0f6666f96b0/research_notes/divisor_extrema/20261116_c77_arbitrary_stock_pairs/SPECTRAL_RIGIDITY.md) 与 [两个固定比例库存](https://github.com/awdawmip/enterprise-math/blob/70285a17eb30dffe4cb4ba599f49b0f6666f96b0/research_notes/divisor_extrema/20261116_c77_arbitrary_stock_pairs/TWO_STOCK_PRECISION.md)。单库存计数的标准代数几何事实及论证列于 [ALIAS_HILBERT.md](ALIAS_HILBERT.md)。有限证书可以逐项复算，全称与渐近结论的依据见 [SHARP_NEAR_STOCKS.md](SHARP_NEAR_STOCKS.md)。
