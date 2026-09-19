# BRC 作用—残差研究扩展

这是已运行精确测试的研究原型，不是生产版本或已接纳的 Foundation。

运行（Python 3.10 或更高版本，无第三方依赖）：

```sh
python verify_extension.py
```

在进取数论仓库中可使用原有包：

```sh
PYTHONPATH=src python research_notes/brc_transport_extension_20260919_AD0416/verify_extension.py
```

`RESEARCH_NOTE.md` 给出对象、组合律、证明、失效条件与实际测试范围。
`brc_transport.py` 是新增研究实现；`verification_results.json` 是本次输出。

`reference_brc/brc_histogram.py` 与 `reference_brc/predictive_quotient.py` 是从
EM@d20fbca83ae79b354a9ce2b0659477065a83993b 读取并核对 Git blob 的未修改文件。
`reference_brc/brc_rational_holonomy.py` 仅包含其依赖的三条原版函数及最小导入；
不是完整原版 holonomy 模块，也不声称运行了完整模块测试。

仿射矩摘要只保留质量、一阶和二阶坐标观察。身份、完整路径、精确权重分布、
阈值与非线性观察不能默认由该摘要恢复。28 个有理数量不等于恒定比特内存。

生产 Nollm、原有 BRC Foundation 与控制面均未在本次修改。
