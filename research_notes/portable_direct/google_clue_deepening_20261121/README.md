# 已有线索的深入结果与下一轮研究边界

日期：2026-11-21。贡献归属：EM-DIRECT-949983 / TASK_RESEARCH；Activity RA-4EC67378C53C5B821B1C43F6。主代理与协作子任务共同形成作者侧推导及精确核算；未发生独立项目审查或数学受理。

## 来源与语义

本轮恢复并深化 EM-DIRECT-3DCA45 于 2026-11-16 保存的科研成果（提交 `ab4699ad2a80b0e040c5a5f287cd34a537d75e6f`，`research_notes/portable_direct/2026-11-16_google_math_continuation/`）及未正式发布的任务提案（提交 `47667d135b2bb7bc6a6423832dfeaba6f4b9f5fc`，`handoff_requests/google_math_20261116/`）。本轮新增贡献不改写原作者归属。

适用基础以本轮实际回源的 Enterprise Math `66bdb7e4abaf26c38157db9c45d14a6dddee3701` 的 AGENTS.md、p000_reality_foundation.json、HEARTBEAT_WORLD_NATIVE_X6_TIME 和 EM_FOUNDATION_STARTUP 为准。六个采样相位属于有类型辅助观察，不添加原生空间轴；差分和平移商的丢失信息分别说明，保留共同误差与原始独立误差的联合结构。

## 取得的结果

### 1. 单异常位置计数的压缩与模4结构

`erdos/THEOREM.md` 给出不枚举局部周期的精确计数公式及逐位置奇性判据。`k=449` 的全 CRT 复算确认：中心项模4为0，只有位置223和225为奇数，因此 H449 模4等于2。非中心成对贡献不能从模4问题中删除。

新的未知在奇位置集合的结构分类、可证明的非中心例外族和完整模4结构，而非再计算几个数值。

### 2. 原始逐位置噪声的全部窗口锐半径

`raw_noise/THEOREM.md` 解决原七/八点任务，并扩展到所有连续窗口长度。增益幅度下界为 g>0，正增益/未知正负号的锐半径分别为：n=5,6时0/0；n=7时3g/(15g/8)；n=8时(15g/4)/3g；所有n≥9时(15g/4)/(10g/3)。小于阈值可一致恢复，阈值处存在真实原始噪声碰撞。

证明由90组有理数原始/对偶证书与两条周期碰撞序列闭合。原草案 RS-SEVEN-PHASE-RAW-NOISE-RADIUS 的数学目标已经作者侧完成，后续任务改为精确非线性整数计数模型的有限尺度余项与噪声保障，不能把此理想模型的阈值直接移植过去。

### 3. 主项消去后的次阶信息

`cancellation/THEOREM.md` 在 d=0、e=floor((-r^6+lambda*r^5)/25920) 的合法整数模型中证明 Z=-20*1+K_a(lambda)/r+O(r^-2)，列出全部六种 K。固定已知 lambda 时完整 K 始终可分；各假设独立未知且 |lambda|≤Lambda 时，完整次阶模板首交点为Lambda=48，平移商为39。

这些是系数模板交点，未把它们等同于有限整数读数碰撞。真正后续为一般分母误差 v 的二参数模板及同首项水平纤维、参数不确定性与高阶恢复。

## 复算

在本目录运行：

```bash
python raw_noise/verify.py
python cancellation/derive.py
python cancellation/classify.py
python cancellation/verify_integer.py
python cancellation/crosscheck.py
python erdos/verify_compression.py
```

原始噪声证书核验只用 Python 标准库。符号消去使用 SymPy（本次实际版本1.14.0），计数对照只用标准库；SciPy仅用于 raw_noise/explore.py 的候选发现，不是任何有理证书的信任前提。计数和证书结论用精确整数/分数；有限整数样本检验不替代一致余项证明。

## 保存、任务与受理状态

本目录是科研成果包。对应新任务草案单独位于 `handoff_requests/google_math_20261121/`。保存本文不创建正式 Task、Claim、Driver 权限或数学验收。新任务应从本轮实际剩余问题出发；所有正式发布状态以不可变 publication record 及当前原生回读为准。
