# E001 材料工程检查点——真实数据、精度层级与运行时状态

状态：`ACTIVE RESEARCH CHECKPOINT / NOT FOUNDATION`

归属：`agent/e001-multires-collision` / Draft PR #70

## 1. 目的

E001 材料路线不再以内部曲线“看起来漂亮”为评价标准。当前硬门槛改为公开真实数据与成熟工程基准：

`真实材料观测 -> 有限整数拟合 -> 外部本构对照 -> 编译运行时状态 -> 目标硬件测试`。

负结果属于阻止错误提升的重要证据，不能隐藏。

## 2. 第一组真实材料基准

基准采用 Treloar 经典硫化橡胶实验中的 25 个单轴加载点 [SRC-TRELOAR-1944-RUBBER]，机器可读数据来自公开 thermalCANN 仓库所保留的 Steinmann 转录脉络 [SRC-THERMALCANN-2023-TRELOAR-DATA]。经典超弹性本构属于既有工程力学 [SRC-STEINMANN-2012-HYPERELASTIC]。

E001 候选在观测值声明到有限尺度后完全采用整数构造：

1. 把有限形变区间投影到 `0..A`；
2. integer root 变换 `G_r`；
3. root-basin 四分之一圆补量 / 有限 versine 基；
4. integer hardening `H_p`；
5. 一个非负整数输出尺度。

`A` 是表示精度，不作为额外材料形状拟合参数。

### 当前独立重算的加载结果

| 模型 | 拟合/形状参数数 | RMSE |
|---|---:|---:|
| Neo-Hooke 对照 | 1 | ~0.7868 |
| Mooney-Rivlin 对照 | 2 | ~0.6216 |
| Yeoh-2 对照 | 2 | ~0.2978 |
| Yeoh-3 对照 | 3 | ~0.1029 |
| E001 integer，A=8192，G8/H3 + 输出尺度 | 3 | ~0.1423 |

E001 在这一条加载曲线上已经明显具有非平凡拟合能力，并优于当前脚本中的简单/低阶对照，但**没有超过 Yeoh-3**。目前不得主张本构精度优势。

## 3. 精度层级会选择不同的可表示曲线结构

在当前有界离散搜索中，最优结构随 `A` 改变：

| A | 当前最优结构 | RMSE |
|---:|---|---:|
| 64 | G1/H1 | ~0.2760 |
| 128 | G4/H2 | ~0.1942 |
| 512 | G4/H2 | ~0.1667 |
| 1024 | G4/H2 | ~0.1594 |
| 2048 | G8/H3 | ~0.1485 |
| 8192 | G8/H3 | ~0.1423 |

这目前只是 E001 工程观察，不是“精度普遍决定模型复杂度”的定理。关于哪些 operation distinction 能在粗精度下保留的一般问题，仍应回到 P018/P023/A2。

## 4. 运行时编译前沿

`material_runtime.py` 可把拟合曲线离线编译成 `A+1` 个有限整数输出。若世界引擎已经持有归一化形变状态，运行时可直接查表；实际物理区间到形变格的映射也可以保持整数计算。

当前 Treloar 输出范围使用 2 bytes/entry 时，密集状态大小为：

- A=64：130 B；
- A=128：258 B；
- A=512：1026 B；
- A=1024：2050 B；
- A=2048：4098 B；
- A=8192：16386 B。

`material_runtime_compressed.py` 利用等输出平台做标准 lossless run-end 编码：

- A=64：39 runs / 117 B；
- A=128：47 runs / 141 B；
- A=512：180 runs / 720 B；
- A=1024：292 runs / 1168 B；
- A=2048：309 runs / 1236 B；
- A=4096：410 runs / 1640 B；
- A=8192：498 runs / 1992 B。

该压缩不会在已经声明的有限曲线上继续增加近似误差。LUT 与运行段压缩都是成熟工程技巧，不属于项目原创。

## 5. 嵌入式边界

`material_runtime_codegen.py` 可从压缩状态生成无浮点 C 头文件。独立生成的 A=128 Treloar 头文件已经在本会话用 C99 warning-fatal 参数真实编译，129 个有限输入状态与独立校验和一致。

一次仅作参考的 x86 `-O3` 微基准，对 3000 万个伪随机归一化形变格查询得到：

- A=128 密集表：约 0.064–0.072 s；
- 47-run 二分查找表：约 0.89–0.94 s；
- 三参数 Yeoh 表达式（包含 cell 到 stretch 映射）：约 0.129–0.142 s。

这**不是可迁移的性能结论**。它只暴露下一步工程选择：小内存预算足够时，密集表可以换取低延迟；朴素 run compression 虽省内存，但延迟敏感场景需要更好的访问策略。

## 6. 科学/工程硬边界

当前成果只是**一维单调加载曲线**，并没有建立完整材料理论。尚未证明：

- 三维客观应变能函数；
- 热力学一致性；
- 一个共享材料状态对多轴数据的预测能力；
- 卸载或循环响应；
- Mullins effect；
- 速率依赖或黏弹性；
- 损伤、塑性、断裂或温度依赖。

对不同加载模式分别单独拟合，也不能自动跨过上述边界。

## 7. 下一门槛：NIST 弹性冲击泡沫

下一组优先数据是 NIST elastomeric impact-mitigating foam 数据库。该公开库包含 quasi-static、intermediate-rate、DMA、drop-tower 等试验；公开 `foam_db` 示例对 VN01 准静态 stress/strain 样本拟合 N=2、6 参数 Hyperfoam。

它比 Treloar 单调加载更直接压力测试 E001 真正可能有优势的部分：

- 压缩与回程双分支；
- 有限损失/迟滞历史；
- 速率状态；
- 冲击缓冲；
- 与更复杂经典本构相比的有限部署状态。

当前执行环境尚未成功取得大体积 VN01 HDF5/ZIP 原始文件。因此目前**不存在 NIST 拟合结果**，不得从图片或相邻数据推断结果。

## 8. 续研入口

主要代码/测试：

- `src/enterprise_math/material_fit.py`；
- `tests/test_material_fit.py`；
- `experiments/e001_treloar_material_benchmark.py`；
- `src/enterprise_math/material_runtime.py`；
- `src/enterprise_math/material_runtime_compressed.py`；
- `src/enterprise_math/material_runtime_codegen.py`；
- 对应 runtime/codegen tests；
- `experiments/e001_material_runtime_frontier.py`；
- `experiments/e001_emit_treloar_c_header.py`。

前人工作/来源：

- `sources_e001_material.json`；
- `lineage_e001_material.json`；
- `docs/PRIOR_ART_E001_MATERIAL.*`。

协调入口：

- PR #70 checkpoint comment `5229980513`；
- runtime follow-up comment `5229993767`；
- Research Relay #82 comment `5229981383`。

源 PR 仍是 Draft 且并发活跃，当前执行环境也无法完成本地 GitHub checkout，因此暂不宣称 repository-wide CI 已通过。
