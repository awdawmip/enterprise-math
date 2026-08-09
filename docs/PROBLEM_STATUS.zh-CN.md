# 编号研究问题权威状态索引

状态：`CANONICAL`  
生效日期：2026-08-09

本文件是进取数论编号研究问题的**权威状态账本**。`OPEN_PROBLEMS.zh-CN.md` 保留各问题最初提出时的原始问题文本，其中可能带有当时的历史性措辞；当状态描述不一致时，以本索引为准。

`RESOLVED` 表示该编号问题在其明确范围内已经有进入 `main` 的规范答案，**不**表示周边整个研究领域已经封闭。

| 问题 | 状态 | 规范范围/结果 |
|---|---|---|
| P001 | `RESOLVED` | `docs/P001_ROOT_MULTIPLICATIVITY.zh-CN.md`：整数根总是超乘性的；乘法性恰好等价于盆地乘积的 carry load 未跨越下一个完全幂阈值；同时得到精确 carry count、向下闭合的无进位区域和 floor-division 边界。 |
| P002 | `RESOLVED` | `docs/P002_COLLAPSE_GAP_BOUND.zh-CN.md`：坍缩差具有紧盆地界 `0 <= G_p(n) <= (k+1)^p-k^p-1`，且仅在盆地最后一个状态取等号；gap 坐标在每个盆地内构成双射。 |
| P003 | `RESOLVED` | `docs/P003_COLLAPSE_COMMUTATION.zh-CN.md`：完全幂坍缩算子全局交换，当且仅当正指数在整除序下可比；若 `p|q`，两个复合都等于 `C_q`；指数不可比时由 `2^max(p,q)` 给出显式素数幂见证。可比方向已在 `EnterpriseMath/Arithmetic/CollapseCommutation.lean` 中通过 Lean 检查；反向分类仍由普通证明与可执行见证回归支撑。 |
| P004 | `RESOLVED` | `docs/P004_COLLAPSE_FIXED_POINTS.zh-CN.md`：任意正指数坍缩算子的有限词，其不动点集合恰好是完全 `L` 次幂，其中 `L` 为这些指数的最小公倍数（空词取 `L=1`）。词序与重复可能改变瞬态作用，但不改变固定点集合；穷举有限词回归用于审计该分类。 |
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
| P018 | `OPEN / ACTIVE RESEARCH` | 有限精度证明演算仍是持续扩展的基础计划。PR #249 已把 P018↔P023 的有界 quotient-root future-action basis canonicalize 并通过 Lean：`O_a(q)=R_r(floor(q/a))` 在 `0,...,N` 上分离全部精确状态，当且仅当正 action set 包含所有 `b<=N` 的正 `r`-power-free 整数，从而得到唯一最小 separating action set。PR #270 又加入了已建立 Stage-8 near-diagonal factor-proof slack 的 canonical executable centered-prime-radius 重写；它只在明确 left-prime/size 假设下成立，不声称每个中心都有对称素数对，也不证明 Goldbach 类命题。精确资产与 prior-art 边界见共享研究面。整个编号计划继续活跃。 |
| P019 | `RESOLVED` | `docs/P019_COLLAPSE_WORD_STABILIZATION.zh-CN.md`：良基偏序上的单调向下自映射会稳定到初态下方最大不动点；因此任意固定坍缩词精确稳定到 `C_L(n0)`，最终盆地就是普通 `L` 次盆地，且坍缩词半群按稳定等价取商后恰为 lcm join-semilattice。 |
| P020 | `RESOLVED` | `docs/P020_WELL_FOUNDED_STABILIZATION.zh-CN.md` 与 `EnterpriseMath/Order/WellFoundedStabilization.lean`：Lean 证明在 `WellFoundedLT` 偏序上，任意单调向下自映射的有限普通迭代会到达初态下方最大的原始不动点；所选稳定化映射单调、向下、幂等，并与原映射具有完全相同的不动点集合。 |
| P021 | `OPEN / ACTIVE RESEARCH` | 有限 causal-boundary 可执行核心已经进入 `main`：`src/enterprise_math/causal_boundary.py` 与 `tests/test_causal_boundary.py` 给出 program-specific 的有限无向图 + 整数 expansion boundary 层，并复用 P018 observation/refinement 工具。更广的 causal focusing、方向/witness 复合及物理解释继续保持活跃研究。 |
| P022 | `OPEN / ACTIVE RESEARCH` | Canonical executable geometry 现已包括 `lattice_geometry.py`；PR #262 的精确 `A_p`/simple-cubic geodesic multiplicity 与整数坐标 ABAB HCP contact-graph core；以及 PR #288 的 periodic Barlow stacking core，后者包含精确 graph distance/geodesic multiplicity、FCC/HCP reconstruction，以及针对声明 root-to-target-layer query 的 cumulative interface-sign-count compression。Barlow 压缩是 task-relative；Barlow precision、periodic-growth、coordination-observable 与 observation-history theory 不在此次 promotion 范围内。更广几何与跨 owner 接口继续活跃。 |
| P023 | `OPEN / ACTIVE RESEARCH` | `docs/P023_COMPOSITION_SAFE_COLLAPSE.zh-CN.md` 及补充：只有相关未来观察/运算能够通过粗商下沉时，该有限精度商才对所要求的未来计算合法；当前规范阶段覆盖 fiber 常值因子化、最粗修复、有限运算族闭包、商/倍数坍缩的精确兼容分类、one-bit 最小修复、reductive gap 到 borrow 的搬运、borrow 望远镜化、safe-selector semigroup 的稳定等价，以及 PR #249 的 canonical Lean-checked 有界 quotient-root action-basis 特化。一般 partition refinement/Test Cover 与 power-free arithmetic 属于前人工作，更广义 safe-precision 结构继续活跃。 |
| P024 | `OPEN / ACTIVE RESEARCH` | `docs/P024_ACTION_LANGUAGE_PRECISION.zh-CN.md`：把 P023 特化到整数平移动作语言与有序阈值观测。当前已证明范围把精度胞元识别为可达边界轨道 `B-M`，给出单向 numerical-semigroup 精确类别数、gcd 过细缺陷等于相关 semigroup holes 数、conductor 局域非均匀边界层、真正双向动作完备化为 `g Z`，以及有限循环周期化后的自动子群完备化。state-dependent 与高维动作语言精度仍保持开放。 |

## 状态纪律

Draft PR、分支定理、有限计算或未合并形式化，都不能据此把编号问题改成 `RESOLVED`。只有在明确范围内进入 `main`，并通过适用的最终门禁后，才可在本账本升级状态。

如果一个已解决问题后来出现更强扩展，应新增研究问题，或显式扩大原问题范围；不得悄悄把旧的 `RESOLVED` 重新解释成“整个方向已经彻底封闭”。
