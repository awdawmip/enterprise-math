# C85 完整复算入口

## 阅读顺序与证明范围

先读 [C85_RESEARCH_NOTE.md](C85_RESEARCH_NOTE.md)。本轮的主要准确结果为：

| 结果 | 完整证明 | 对应准确计算 |
| --- | --- | --- |
| 半面积位置比较、中央三分之五位置区间、全局剩余积分目标 | `position/HALF_AREA_COMPARISON.md` | `position/certify_half_area.py` |
| 全相位平均的方格反例及正测度邻域 | `position/SQUARE_LATTICE_OBSTRUCTION.md` | `position/verify_square_lattice.py` |
| y≥5 的瘦格贡献严格定号 | `lattice/CUSP_POSITION_THEOREM.md` | `lattice/verify_cusp.py` |
| y≤5 的 4,348 个无向方向统一完备界 | `lattice/COMPACT_FINITE_REDUCTION.md` | `lattice/verify_compact_reduction.py` |
| 独立相位端点模型、40/41 比值和连续性模数 | `endpoint/ENDPOINT_LIMIT.md` | `endpoint/verify_endpoint.py` |
| 三角准确式、方向图上界及 1.6529<κ₃<1.9580 | `triangle/REPRODUCE.md` 中列出的四份证明 | `triangle/certify_farey_parallelogram.py` |

准确的原谱极限和旧三角矩公式沿用 C82–C84 的不可变来源，见 [SOURCE_PINS.json](SOURCE_PINS.json)。辅助 Haar 格、相位和截面没有替换原 H(0,1) 或原整数安排。新证明的范围与已完成的项目内核对见 [PROOF_REVIEW.md](PROOF_REVIEW.md)。

## 环境

本轮实际运行环境为 Python 3.12.14、SymPy 1.14.0。除 SymPy 外，准确复算仅用 Python 标准库。安装声明依赖：

```bash
python -m pip install -r requirements.txt
```

Monte Carlo 探索程序另需支持 C++17 的编译器，它不是准确复算的依赖。

## 先检查交付字节

在解压后的 C85 目录执行：

```bash
python verify.py --check-manifest
```

`SHA256SUMS` 覆盖所有科研文件、源码和结果，不包含它自身。交付压缩包中的 `PUBLICATION.json` 是随后生成的提交定位凭据；它不属于科研提交的自身摘要清单。

## 六组准确复算

```bash
python verify.py
```

该命令实际重新计算半面积常数、48 个方格有理相位实例、14 个瘦格代数与不等式检查、10 个紧致归约检查、19 个端点检查，以及三角分支的 34 个源点完整分类。三角快速步骤同时核对三份证书的有理求和、嵌套范围、源码字节绑定和最终严格界。

它会重写相应 JSON 及 `CHECKS.json`。运行时间戳会改变，因此重算后旧的交付字节清单不再用于新生成的文件。快速步骤不重新计算三角积分网格；这个区别在 `CHECKS.json` 中明确记录。

## 完整重算最终三角积分

```bash
python verify.py --recompute-integrals
```

该命令先完整运行最终生成器，再运行六组核对。最终积分包括：

- 分母为 2¹¹² 的整数定向区间；
- 面积 A 的 1/1024 网格，A<2 使用五项准确式；
- 中间面积段的短方向下界和格行必要条件上界；
- A<4 的 Euler 上界及单位平行四边形积分修正；
- 平行四边形 d 积分的 1/256 网格、完整单元界和面积向下舍入；
- r≥3 尾段的 256 项正有理级数及显式余项。

本轮已实际执行这个最终生成器，一次约 37 秒；具体机器上的时间可以不同。最终使用 `triangle/parallelogram_certificate.json`，不能把较早的 `extended_certificate.json` 或 `middle_bounds_certificate.json` 当成最新范围。

准确最终范围为

\[
\frac{8582640364445688146560089200591674}{2^{112}}
\le\kappa_3\le
\frac{10166032737163568038796686356009924}{2^{112}}.
\]

整数端点是证据；JSON 的小数只是显示值。

## 探索性采样

```bash
g++ -O3 -std=c++17 position/explore_split.cpp -o /tmp/c85_explore_split
/tmp/c85_explore_split 200000
/tmp/c85_explore_split 200000 square
```

固定随机种子为 851903；两个模型的原始输出分别是 `position/exploratory_split.json` 和 `position/square_lattice_exploratory.json`。前者在加入输出字段 `model` 之前保存；后续程序保留相同算法和种子，但 JSON 字段不要求字节相同。浮点环境也可能改变末位。

全 Haar 采样中，估计的 I₁/₄−I₁/₂ 为 −0.00174318，标准误差约 0.00005126；剩余 a<1/2 积分估计为 −0.00021682，标准误差约 0.00002669。它们均不是严格界，不参与定理。方格采样现已被准确公式和有理证书替代，仍保留为路线记录。

`triangle/explore_identity.py` 是有限构型探索，未用于声称 A≥2 的完整准确式。

## 尚未完成的结论

本包没有证明完整 Haar 平均下 I₁/₄<I₁/₂。足够的下一步是准确证明报告第 3 节的小面积加权积分小于 0.001361。紧致格形积分的有限归约已经完成，其数值或解析闭合仍待进行。普适曲线交点的唯一性、端点附近位置的全局优化，以及 A≥2 的三角准确概率公式也仍开放。

本轮验证是分析推导、准确计算及共享研究上下文内的交叉核对；外部同行复核尚待进行。
