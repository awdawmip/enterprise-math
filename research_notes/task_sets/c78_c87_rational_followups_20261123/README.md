# C78／C87 有理化重证后续任务集

Taskset: `TS-C78-C87-RATIONAL-FOLLOWUPS-20261123`  
Parent objective: `OBJ-INVENTORY-RATIONALIZATION-20261123`  
Publisher: `EM-DVR-2D6C6F`  
Prepared at: `2026-11-23T00:08:58.063875+00:00`

依据用户“发布后续任务到状态机和中控台”的指令，本批首次建立一个承担组合定理及有限误差闭合的母任务，和四个可并行研究的后续任务。既有重证以固定 direct research 来源继承，母任务没有被回填为历史任务或既往完成结果。

## 正式任务

| 任务 | 优先级 | 基础权重 | 依赖 |
|---|---|---:|---|
| [因数库存有理化重证：全范围定理与有限误差集成](../../../research_tasks/RS-INVENTORY-RATIONAL-REPROOF-INTEGRATION-20261123.md) | P2 | 20 | 四项子任务 |
| [C77 正比例库存差的有理重证](../../../research_tasks/RS-C77-RATIONAL-POSITIVE-RATIO-20261123.md) | P1 | 30 | 无相互硬依赖 |
| [C78 原全库存的有限识别误差与可复算阈值](../../../research_tasks/RS-C78-EFFECTIVE-RATIONAL-IDENTIFICATION-20261123.md) | P1 | 30 | 无相互硬依赖 |
| [C87 原全库存到 Haar 联合模型的原点一致有效桥](../../../research_tasks/RS-C87-EFFECTIVE-NATIVE-HAAR-BRIDGE-20261123.md) | P1 | 30 | 无相互硬依赖 |
| [C87 高精度位置排序的有效余项与起效倍率](../../../research_tasks/RS-C87-EFFECTIVE-HIGH-PRECISION-ORDER-20261123.md) | P2 | 20 | 无相互硬依赖 |

## 科学边界与接续

C77 补齐固定正比例差的有理充分性；C78 将渐近结论变成明确域内的有限识别界；C87 两项分别支付原库存分布误差与高倍率尾余项。两项 C87 可并行，回到有限库存的排序才合并其误差。
C78 的有限 c0 携带库存差的定量域或收敛模。C87 的 L0 针对固定位置对或有分离余量的位置族。任务保留完整原目录、三条尾和全局舍入原点量词，研究方法开放。
母任务验收同一归一化和非空共享输入域中的组合定理及 Delta_main > R1+R2+E1+E2 的有限排序条件；未闭合预算保持为具体缺口。
已完成近库存锐阈值、代数及差分工具、有限相位证书和最低精度作为证据复用。来源状态仍为作者证明/准确计算，独立 Review 与正式接纳保持各自真实状态。

## 谱系、去重与权重

读取当前完整任务 ID 子树并核对相关任务书。现有 RS-INVENTORY-DIVISOR-SUM-INTERFACE-20261122 处理约数和及 RH 接口；本批不改其目标、owner 或优先级。
母任务 `RS-INVENTORY-RATIONAL-REPROOF-INTEGRATION-20261123` 为本批首次发布的 INTEGRATION；四子为真实 CONTINUATION，并各自保存 successor_gate。母依赖四子，子不反向依赖母，领取依赖图无环。
P1/P2 采用当前基础权重 30/20；沿用等待和方向轮转规则。全局权重策略未改变。

## 出版证据

五份任务书使用当前 canonical prepare、dispatch lint、prepared-content validation、build_record facade 和 scoped immutable-record audit。任务书与匹配 V2 记录在一次非强制 CAS 提交中共同发布；远端按实际提交进行范围明确的回读，中控台状态随后由原生 exact-task 查询核实。

[机器可读任务集](TASKSET.json)

## 固定科学起点

- [research_notes/portable_direct/c78_c87_rational_continuation_20261122_af81e5b398b7/REPORT.md](https://github.com/awdawmip/enterprise-math/blob/c9d661935fc64e300c0a0d5dd7fb42de213e6401/research_notes/portable_direct/c78_c87_rational_continuation_20261122_af81e5b398b7/REPORT.md)
- [research_notes/portable_direct/c78_c87_rational_reproof_20261122_af81e5b398b7/REPORT.md](https://github.com/awdawmip/enterprise-math/blob/46eec634a39fd202babd05e66b251d90945be948/research_notes/portable_direct/c78_c87_rational_reproof_20261122_af81e5b398b7/REPORT.md)
