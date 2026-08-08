# 编号研究问题权威状态索引

状态：`CANONICAL`  
生效日期：2026-08-08

本文件是进取数论编号研究问题的**权威状态账本**。`OPEN_PROBLEMS.zh-CN.md` 保留各问题最初提出时的原始问题文本，其中可能带有当时的历史性措辞；当状态描述不一致时，以本索引为准。

`RESOLVED` 表示该编号问题在其明确范围内已经有进入 `main` 的规范答案，**不**表示周边整个研究领域已经封闭。

| 问题 | 状态 | 规范范围/结果 |
|---|---|---|
| P001 | `OPEN` | 整数根乘法性仍属于非规范研究；carry-threshold Draft 已存在，但尚未进入 main。 |
| P002 | `RESOLVED` | `docs/P002_COLLAPSE_GAP_BOUND.zh-CN.md`：坍缩差具有紧盆地界 `0 <= G_p(n) <= (k+1)^p-k^p-1`，且仅在盆地最后一个状态取等号；gap 坐标在每个盆地内构成双射。 |
| P003 | `OPEN` | 坍缩算子全局交换分类仍在 Draft/非规范状态。 |
| P004 | `OPEN` | 任意有限坍缩词的不动点分类仍在 Draft/非规范状态。 |
| P005 | `RESOLVED` | `docs/P005_SCALE_LATTICE_CORE.zh-CN.md`：用正整数总尺度因子统一尺度坐标，建立整除投影、gcd/lcm 尺度格、路径无关性及 inverse refinement 非唯一性。 |
| P006 | `RESOLVED` | `docs/P006_SIGNED_STATE_EXTENSION.zh-CN.md`：明确区分通常整数序奇次根与带符号模长量化；偶次幂在整个有符号整数序上不存在通常序右伴随。 |
| P007 | `RESOLVED` | `docs/P007_DISCRETE_DIVISION.zh-CN.md`：精确商、同空间倍数坍缩、可逆商余状态是三种不同的显式离散语义。 |
| P008 | 当前 v0.1 根/商/坍缩族范围内 `RESOLVED` | `docs/P008_MINIMAL_ORDER_CORE.zh-CN.md` 与 Lean 核心：显式状态相等需要偏序语义；principal sublevel 最大元等价于所需右伴随存在；order embedding 给出精确恢复；诱导坍缩向下、单调且幂等。未来新增运算若需要更强结构，应另行证明。 |
| P009 | 最小带类型 collapse+coarsening 系统范围内 `RESOLVED` | `docs/P009_TYPED_SCALE_CORE.zh-CN.md`：严格轨道终止、无非平凡循环、纯投影到固定目标合流，而任意 collapse/project 混合调度一般不合流；非规范 inverse lift 属于另一个系统。 |
| P010 | `RESOLVED` | `docs/P010_STRICT_HISTORY_MERGE.zh-CN.md`：严格历史合流的精确可达碰撞判据与 multiplicity 增量公式。 |
| P011 | 有限确定性映射范围内 `RESOLVED` | `docs/P011_INTEGER_IRREVERSIBILITY_SPECTRUM.zh-CN.md` 及补充：超可加整数观察量、完备碰撞谱、碰撞多项式，以及后置派生的 entropy 比较。 |
| P012 | 度量基础范围内 `RESOLVED` | `docs/P012_INTRINSIC_DISCRETE_GEOMETRY.zh-CN.md`：primitive-step graph distance 给出精确整数度量；补充文档明确 metric 结构并不自动给出 inner product 或 Pythagoras。更广义离散几何仍可继续研究。 |
| P013 | `RESOLVED` | T001 与 T005 已在 `EnterpriseMath/Arithmetic/IntegerRoot.lean` 中通过 Lean 检查，固定版本且 warnings-fatal 的 Lean CI 已成功。 |
| P014 | `RESOLVED` | T010 已在 `EnterpriseMath/Scale/Compatibility.lean` 中通过 Lean 检查；`EnterpriseMath.lean` 显式 import 该模块，确保 CI 实际编译此证明。 |
| P015 | `OPEN / CONTINUOUS` | 前人工作映射是持续义务；每新增组件仍需继续检索、归因和更新 lineage。 |
| P016 | 协议层 `RESOLVED` | `docs/P016_PHYSICAL_FALSIFICATION_CONTRACT.zh-CN.md` 与 `falsification.schema.json` 定义 F1–F9 量化 kill-test 要求；这并不等于物理假说本身已被验证或证伪。 |
| P017 | `OPEN / ACTIVE RESEARCH` | Legendre 压力测试已有大量进入 main 的结构结果，但没有 Legendre 猜想证明；继续坚持压力测试与反例优先。 |
| P018 | `OPEN / ACTIVE RESEARCH` | 有限精度证明演算仍是持续扩展的基础研究计划；当前各阶段可以是规范结果，但整个编号计划保持活跃。 |

## 状态纪律

Draft PR、分支定理、有限计算或未合并形式化，都不能据此把编号问题改成 `RESOLVED`。只有在明确范围内进入 `main`，并通过适用的最终门禁后，才可在本账本升级状态。

如果一个已解决问题后来出现更强扩展，应新增研究问题，或显式扩大原问题范围；不得悄悄把旧的 `RESOLVED` 重新解释成“整个方向已经彻底封闭”。
