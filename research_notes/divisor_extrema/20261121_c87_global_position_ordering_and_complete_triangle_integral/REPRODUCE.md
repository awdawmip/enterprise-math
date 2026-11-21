# C87 复算入口

## 环境与文件

准确证明和区间程序使用 Python 3 标准库，不需要网络或第三方数值库。
只有可选的探索性程序 `positions/explore_positions.py` 使用 NumPy；探索小数不作为证书。

解压后进入 C87 目录，执行下列相对路径命令。所有计算依赖均随包提供，
包括固定的 C86 分区数据和既有 112 位区间算术。
`SOURCE_REFS.json` 记录不可变项目来源，`SHA256SUMS` 覆盖本包证据文件。

## 1. 快速核对

```bash
python verify_bundle.py
```

该命令实际执行七组核对：

1. 全部六十个 x 区间的准确接缝、完整覆盖、严格正裕量和生成器绑定；
2. 必要前件证明的原样副本与哈希；
3. 轴展开的准确抵消、完整余项、两项 192 格径向积分及十四个位置积分；
4. 低半方形的两项准确分区修正及严格正常数；
5. QT 的 1150 个有理源实例、两种消元、反射、点包围、跨界框及保存总证书；
6. QT 的独立原三维多面体体积核对，共 85 个实例；
7. 未证高半区加强所需的七个局部接缝及四个零边界恒等式。

最后一组只证明归约所需的接缝，不证明尚未定号的二阶导数。
输出 `checks.json` 明确保留这个区别。

快速核对会重算上述准确有限代数、两项径向积分和已有仿射模型的积分。
它不重新运行自适应完整 x 区间生成器，也不重新运行完整 κ₃ 外层网格。
程序中给出这一范围，避免把证书核对写成另一次完整网格复算。

## 2. 主正性证书的完整重建

```bash
python certify_integrated_kernel.py
python positions/certify_axis_midpoint.py --n 192
python positions/certify_position_values.py
```

第一条覆盖完整区间 [1/8,1]，原执行为 117 次试算、60 个最终区间，约 18.92 秒。
第二条给出完整轴邻域的系数、b₂ 积分与中点曲率，原执行约 0.22 秒。
第三条直接积分前两条产生的仿射区间模型及准确轴展开，给出十四个位置的区间值。

生成器输出含运行时间。重新生成前两个证书会改变文件哈希，即使所有数学端点完全相同。
因此第三条必须放在它们之后，更新输入证书的真实哈希。快速核对不改这三个固定证书。
若要保留发布时的原始 SHA256SUMS，应在解压副本中重建证书。

## 3. 完整 κ₃ 区间重建

```bash
python triangle/certify_qt_complete.py
```

原执行约 234.83 秒，参数：

| 参数 | 值 |
|---|---:|
| 面积网格每单位 | 1024 |
| 短方向与行函数网格 | 512 |
| 面积缓存网格每单位 | 64 |
| 平行四边形内部网格 | 256 |
| QP 每段网格 | 64 |
| 新 QT 每轴完整单元 | 64 |
| 有向算术分母 | \(2^{112}\) |

输出完整有理端点，主结论为 \(1.7101<\kappa_3<1.7833\)。
外层面积单元按已证明的单调性包围；QT 结点顺序可能改变的参数单元使用全部相容排列。
原生成器已经实际执行，不以快速验证替代这次执行事实。

## 4. 逐分支核对与文档

```bash
python positions/verify_positions.py
python positivity/certify_low_half.py
python triangle/verify_complete_qt.py
python positivity/audit_qt_integral.py
python positivity/verify_high_half_joins.py
python audit_integrated_kernel.py
```

主证明为 `INTEGRATED_KERNEL_PROOF.md` 和 `positions/GLOBAL_POSITION_THEOREM.md`。
端点展开见 `positions/ENDPOINT_AXIS_PROOF.md`，三角新积分见
`triangle/QT_POSITIVE_INTEGRAL.md`。独立内部审查分别记录主正性证书和原三维体积路线。
最后一条独立核对十二条完整接口、全部六十区间和径向分类，重算五个完整 x 区间及
两项轴积分，输出 `integrated_kernel_independent_checks.json`；它也不重跑完整搜索或 κ₃ 网格。

有限样本不能代替这些普遍分析证明。运行成功也不自动表示项目正式接受或外部同行复核。
