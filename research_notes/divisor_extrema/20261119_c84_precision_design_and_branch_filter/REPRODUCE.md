# C84 复算说明

本包继续研究原来的 `H(0,1)` 读数、原整数安排和原舍入格。证明、严格数值证书、有限枚举和探索计算的作用分别注明；程序通过不代替解析证明。

## 1. 入口与运行环境

在本目录运行：

```bash
python verify.py
```

该命令写入 `checks.json`，汇总每组检查的实际退出码、范围、耗时、环境和输入 SHA-256。必须使用正常 Python 模式；不得加 `-O`，因为精确检查使用 `assert`。实际执行环境为 Python 3.12.14、NumPy 2.3.5、SymPy 1.14.0、mpmath 1.3.0。默认检查只需要这三个第三方库；严格区间积分脚本本身只使用 Python 标准库。

本轮最终默认入口已实际执行，10 组检查全部通过，失败为 0，待接入组件为空；详细记录见 `checks.json`。

默认入口不会重跑 2048 格细积分、六支根的全部隔离或三个库存的完整原读数枚举。它会重算精确恒等式、严格证书的基础算术和粗网格包含、六个根盒的 12 个准确边界符号，并检查已存有限结果的计数与一致性。

```bash
python verify.py --full --output full_checks.json
```

`--full` 在临时副本中重新生成全部严格证书、六支根隔离和完整有限原读数目录，再逐字段比对已存结果，仅排除计时字段。原科学 JSON 不会被改写。这个入口用于需要完整独立复算时；本轮已逐项执行相关生成程序，但没有把整套 `--full` 再重复运行一次。

## 2. 默认检查的准确范围

| 检查组 | 实际核验内容 | 不由该程序单独证明的内容 |
|---|---|---|
| `finite/verify_one_dimensional.py` | 21 项准确原函数或系数恒等式，以及 16 个内层积分的高精度数值交叉比较，合计 22 项记录 | 几何形状分类、计数重数、统一渐近余项 |
| `finite/verify_certificate.py` | 有理四则、平方根包围、独立级数对数与反正切包围、二阶导数规则、已存细证书端点及一次新粗格包含；7 项记录 | 2048 格逐格重算 |
| `position/check_position.py` | 中间位置函数、两个位置的准确系数、尺度与整数时刻 Fourier 系数 | 从局部 Haar 定律推出原模型极限所需的既有定理 |
| `branches/verify_branch_identities.py` | 谱与径向导数恒等式、边界级数、六支有理 q 区间、间隔、二阶过滤门槛和源质量 | 全部宏观分支的解析分类 |
| `branches/verify_triangle_tail_series.py` | 三角尾积分的独立 256 项正有理级数、准确矩及几何余项，与已存尾区间相交 | 中间面积段的准确格点概率 |
| 六支根盒边界符号 | 在已存矩形的每个根盒两端重新计算准确有理符号，共 12 个 | 全部根的重新隔离 |
| 已存有限原读数结果 | 库存、安排数、原点组合、计数范围、端点一致性、严格收益反转及见证结构 | 逐安排重新计算所有原读数 |
| 原有限求值器来源 | 两个复用文件与冻结 C82 科学来源的 SHA-256 完全一致 | 新的全库存无碰撞定理 |
| 三角常数证书 | 已存头部、中段、尾部区间的准确求和、外包分数、脚本散列及基本区间恒等式 | 全部面积格和尾格重新计算 |
| 科学结果保存 | 所有已存科学 JSON 的散列在本次检查前后相同 | 外部同行评审 |

`checks.json` 的顶层通过数计的是这些检查组，不能和各子脚本的内部检查条数相加后解释为独立数学证明的数量。如果三角常数文件尚未全部写完，入口会在 `pending_components` 中明确报告它；最终交付的记录应为空列表。

## 3. 首个重叠区间的一维准确式

证明：`FINITE_FORMULA.md`。实现：`finite/one_dimensional.py`。

该式适用于 `1/4 < a < 1/2`，令 `A=2a`，将 C83 的准确有限方向积分化为一个有明确初等核的一维积分，只在 `z=1+A` 分段。积分中没有嵌套的数值积分。剩余 z 积分没有被宣称已获得全区间初等闭式。

`finite/one_dimensional_values.json` 是实际高精度探索输出，其中

```text
F3(1/3) ≈ 0.39704754472205144328262766100236
```

这些小数本身不带严格误差认证；严格外包见下一节。`finite/endpoint_values.json` 记录上端点前三个主项的探索对比，五项展开及其统一余项由证明文件给出。

项目内独立复推记录在 `branches/finite_geometry_review.md`；其中复核坐标变换、三角形重数 3、平行四边形重数 2、两个形状核、积分域和原函数。五项端点展开及区间证书的基础算术由根分支另行复核。

## 4. F3(1/3) 的严格证书

证明和不变量：`FINITE_CERTIFICATE.md`。

```bash
python finite/certify_one_third.py --grid 2048 --output finite/one_third_certificate.json
python finite/verify_certificate.py
```

细证书实际使用每支 2048 格、共 4096 格；其中 4094 格用区间二阶导数控制的中点误差，两个接触奇端点的格子用函数值区间直接积分。所有认证运算均在 `2^120` 的整数定点尺度上向外舍入；对数、反正切及 pi 均附准确级数余项。普通浮点数只用于最后的显示。

已证：

```text
0.397047162 < F3(1/3) < 0.397047924
```

外包宽度为 `0.000000762`。精确有理端点、各类格数和区间二阶导数上界均保存于 `finite/one_third_certificate.json`。本轮细积分生成程序实际退出码为 0；默认入口不会再重复这一细网格。

## 5. 中间库存位置的有限原读数验证

证明：`READING_POSITION.md`。完整生成程序：`position/native_reading_compare.py`。

```bash
python position/native_reading_compare.py
```

结果为 `position/native_position_comparison.json`，覆盖三个原库存和四个测量库存：

| 原库存 c | 首末库存间距 B | 逐次读取的库存 | 安排数 |
|---:|---:|---|---:|
| 8 | 4 | 8, 9, 10, 12 | 28 |
| 64 | 16 | 64, 68, 72, 80 | 2,016 |
| 256 | 64 | 256, 272, 288, 320 | 32,640 |

共 34,684 条安排、138,736 个有认证误差的原读数区间、128 行原点与精度组合记录；小库存另有 112 个准确有理读数作交叉核验。

在 c=256 时，p=10 下四分之一位置的唯一安排数为 316–352，中点为 438–487；p=20 下四分之一位置为 18,670–18,702，中点为 18,529–18,575。每段范围跨八种舍入格原点组合，两个反转均不依赖这些组合。证明中的局部 Haar 结论与这里的有限原读数观察分别陈述；不能据此提前宣称全库存高倍率极限的全局优劣。

## 6. 六个宏观分支的有理证书

证明：`BRANCH_TRANSITION.md`。

```bash
python branches/certify_six_branch_gap.py
python branches/verify_branch_identities.py
```

生成程序用准确有理数隔离六支，输出 `branches/six_branch_gap_certificate.json`；其中保留源矩形、所有根盒、q 区间和严格间距。默认总入口额外重算根盒矩形两角的 12 个准确符号；`--full` 重跑完整隔离，并逐字段与证书比较。

## 7. 三角窗口常数的严格证书

证明：`TRIANGLE_CONSTANT.md`。程序：`triangle/certify_constant.py`。

```bash
python triangle/certify_constant.py --quick
python triangle/certify_constant.py --mesh 1024 --tail-mesh 512 --output triangle/certificate.json
```

快速模式的范围是记录求和、脚本散列和基本区间恒等式；第二条命令才重新求出全部面积段与尾部段的外包。准确有理区间保存在 `triangle/certificate.json`，输出中的十进制串为展示值。总入口 `--full` 从已存证书读取两个网格参数，不依赖程序默认参数。

方向计数和短向量尾的独立复推记录在 `branches/triangle_geometry_review.md`。该记录明确区分所核的几何计数与三随机点面积密度公式的独立依据。

还可单独运行：

```bash
python branches/verify_triangle_tail_series.py
```

它用独立概率矩展开求尾积分，不复用 `g` 的闭式或原尾网格。256 项全部以 `Fraction` 求和并附几何余项，只复用已经认证的平方根与 zeta 区间算术。输出 `branches/triangle_tail_series_checks.json`，其中整数向外转换的严格显示外包是

```text
0.020908612465144493933752
  < 2 sqrt(2) integral_3^infinity psi(r) dr
  < 0.020908612465144493933753.
```

它是第 10 个有实质独立依据的检查组；没有改写三角常数主证书或重算中间面积段。JSON 中另列的普通 `decimal` 串只用于显示，严格引用应使用准确有理端点或 `strict_outward_decimal_enclosure`。

## 8. 可复算性边界

科学 JSON 是实际脚本输出或由其准确端点生成的明确显示字段，不由普通小数反推证书。文件中的证明依赖 C83 已建立的局部联合整数格和有限方向公式；本轮没有声称重新证明所有前轮基础。

`finite/explore_rectangle.py`、`finite/check_shape_kernels.py`、`finite/endpoint_exploration.py` 及 `triangle/explore_bounds.py` 是探索或交叉比较程序，普通浮点积分不能替代严格证书。这些额外探索需要 SciPy；默认复算入口不运行它们。

另有 `position/explore_global_tail.py` 与实际 50,000 个配对 Haar 样本的输出 `position/global_tail_exploration.json`。它们估计全源高倍率位置常数，属于普通浮点 Monte Carlo 探索，没有纳入严格证书或新增验证组。`position/GLOBAL_TAIL_EXPLORATION.md` 独立核对采样测度、临界缩放的矩恒等式、准确运算下的完整整数枚举以及配对标准误；四分点相对中点的样本差约 −0.00181241、Monte Carlo 标准误约 0.00010331，仅提供后续研究线索。该复核没有增加样本。θ=0 行是独立三相位的边界普适模型，不能解释为在同一库存实际重复一次读取。

本包的独立检查均为项目内部交叉复核。外部同行复核尚未完成。
