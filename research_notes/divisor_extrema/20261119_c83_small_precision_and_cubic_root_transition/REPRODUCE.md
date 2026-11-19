# C83 复算入口与实际检查范围

使用 Python 3、NumPy、SymPy。在本目录运行：

```bash
python verify.py
```

默认执行符号恒等式、有理截面和内积分检查、8,000 个准确格方向事件例子、尾常数最终 Fraction 算术与新生成的 8 格积分外包、三个库存的区域整数计数、c=8 的原始三态路径及舍入读数复算、16 个确定性二进制格的前两点逐行搜索/完整暴力对照。还检查已保存大结果的样本数、计数关系及适用范围。结果写入 `checks.json`，并记录每条命令、退出状态、实际范围及输入哈希。

默认不重复 512 网格证书、较大物理目录和百万 Haar 抽样。尾常数检查会从已保存的 512 网格矩端点重新计算全部后续有理界，并以新计算的小网格外包作一致性核对；它不等同于独立重算全部 512 网格节点。已有百万样本只核对数量和算术，不能由这些检查推出统计误差已受严格控制。

完整重算：

```bash
python verify.py --full
```

它另外重算 512 网格证书、五组物理读数目录和原种子的百万抽样。预期结果与已保存字段比较，时间字段除外。浮点库或平台改变可能使抽样结果的末位不同；不要把这一数值比较当作经过证明的置信区间。脚本保留原科学 JSON，完整复算结果用于比较而不覆盖它们。

单项入口：

```bash
python haar/check_small_asymptotics.py
python critical/verify_transition.py
python haar/finite_direction_integral.py
python haar/check_direction_events.py
python tail/certify_constant.py --grid 512 --output tail/constant_certificate.json
python finite/transition_readings.py --output finite/transition_readings.json
python tail/triangle_gap.py --samples 1000000 --seed 20261119 --output tail/triangle_gap_estimate.json
```

`haar/finite_direction_integral.py --quadrature 96` 提供探索性的外层浮点求积；内层分段多项式在 Fraction 输入下准确。保存的 `haar/quadrature_comparison.json` 比较两种积分坐标，不是误差认证区间。

五组物理设置为 (c,b,p)=(8,2,7)、(64,4,13)、(64,16,12)、(512,8,19)、(512,32,18)。同一库存的安排在不同间距下复用，所以共 265,692 个“安排×设置”行；三个不同 c 的目录合计 132,860 条安排。每组有八个零/半格原点，176 位是区间运算内部精度，p 是实验读取位数。有限表不代替临界相位极限的解析证明。

理论入口为 `HAAR_SMALL.md`、`HAAR_FINITE_INTERVAL.md`、`TRIANGLE_GAP.md`、`TAIL_CONSTANT.md`、`LOW_PRECISION.md` 和 `CRITICAL_TRANSITION.md`。程序支持这些文档列明的代数、证书和有限计算；它们不是解析定理的形式化证明器。
