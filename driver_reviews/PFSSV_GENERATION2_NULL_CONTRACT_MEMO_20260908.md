# PFSSV gen2：原 Null A/B 与真实 joint prime-rank 的合同边界

日期：2026-09-08。性质：owner 内部、独立纸面分析；不是新实验、claim、正式 Driver verdict、数学 API 或新 family。

**结论：原程序的两个随机对象足以定义其已有一维残差统计的计算分布，但不唯一确定真实 `(pi(p),pi(q))` 二维 occupancy 的随机分布。** 完整 prime prefix 可以修复观测坐标；它不能替代缺失的 q-rank 随机分配合同。原任务明确要求真实二维视图及修正摘要，但没有把“每个二维格子都另行做一次 joint 检验”定义成一个完整的固定统计合同。不能默许新增 joint null，也不能借此免除未完成的 corrected-view 输出。

本轮只读下列四份科学来源。三个仓内文件实际字节与已入 main 的 `be350eb1b0eeb2a9a07a23a43ee3c8170e93b4b4` 完全相同；定向 `git diff --exit-code` 为空。没有读取 `D:/em/research-pfssv-revision-20260908` 中未冻结的新脚本，没有导入或执行原/新数学程序，没有重跑历史小核验或完整 21 cells。PREPARATION 的“尚未执行授权”是其生成时点事实，不是对 root 后来已完成 claim/runtime 授权的否定。

## 1. 必需视图与必需检验必须分别读

- 原 taskbook 第 109–115 行要求运行五种 primary views，其中 prime-rank 明确是 `(pi(p),pi(q))`；第 139–145 行要求 raw/corrected occupancy、两个 null 家族、一个 fixed normalized factor-coordinate 的跨尺度 profile、family-wise 阈值及盲 holdout。metadata `next_action` 第 11 行也期待这些 residual maps 与两个 null 比较。
- 但第 167 行的候选条件是残差在 **prime-rank 或 density-flattened** 坐标仍存在，第 168 行要求同一预声明特征通过两个 null。正文没有给出 joint rank 的二维格、二维统计量、q-rank 随机核或二维 phase 作用。这些句子不能推出“所有视图必须各有独立二维 max test”，也不能推出“二维 corrected view 可以缺省为已通过”。
- gen2 书第 72 行进一步明确：每个 scale/width、每个 required view 的 raw/corrected 摘要；原两个 null 及 support audit；原阈值或不能重建的明确说明。第 80 行允许无法提供时报告 partial/BLOCKED 和具体 residue。因此合法边界是：观测 joint 图必须真实；未定义的 joint correction/null 明确 unavailable，不能伪装为既有检验。
- 这里的“原固定检验”以实际原程序为准。本轮没有重新读取历史 manifest/freeze 文件，故不另行声称它们从未写过其他约定，也不重建历史盲态。若存在额外、明确、冻结的 joint 随机合同，应单独核对；不能从本轮所读程序或 PREPARATION 中推断它已经存在。

## 2. 原程序实际随机化了什么

原程序第 66–72 行先取合法壳窗口，随后按 `counts>0` 丢弃观测零行；第 79–99 行在 scale trim 上构造：

`C[i,r] = 第 i 个 p 窗口内 q mod 30 = r 的素数个数`，

分层键为 `(8 个粗 log-p band, p mod 30)`。**Null A 并非把整条 q-vector 作为一个整体搬运：第 103–108 行对同一层的每个 r 分量分别、独立地置换行。** 它保持每层、每 r 的 count 多重集，得到 `C'[i,r]`，再只计算

`H'[b] = sum_{i: zbin(i)=b} sum_r C'[i,r]`。

这里没有随机 q 身份、q-rank、q-gap、joint rank tensor 或目标窗口容量修复。固定小层不置换也由这段代码决定。

原程序第 203–223 行的统计对象是 15 个 discovery cells 的 24 维 density-flat、scale-trim 标准化残差 `Z[c,b]`：

`T = max_b |mean_c Z[c,b]|`。

Null A 的 family-wise 参考分布来自同一 24 维对象。Null B 则对每个 `Z[c,:]` 独立循环移位 `s_c in {1,...,23}`，然后取相同的平均和 max；它没有二维轴、二维邻接、q-rank 或壳支撑的定义。它明确保持的是每条标准化残差向量的循环平移类和数值多重集；不能直接把这种保留解释成保留真实 prime gaps 或 raw q-margin。若以它落实 taskbook 所称 factor-margin information，须明确这里指这种派生 profile 信息。

因此，旧 A/B 的程序分布确实可计算；这与“粗层交换性及 phase 作用已被证明足以代表母假设”是两件事。B 的另一组随机 seed 不能补 A 丢掉的 q 信息，也不修复 A 的窗口/密度错配。

## 3. 可识别性缺口：同计数可以对应不同 joint 图

用精确非负整数总体 `n[i,q]` 表示带 `(p_i,q)` 标签的质量。旧计数观察是

`R(n)[i,r] = sum_{q: q mod 30=r} n[i,q]`。

真实 joint 网格则还要观察 `pi(q)` 所落的列。只有未来统计在 R 的每条纤维上恒定，即存在 `t` 使 `T_joint(n)=t(R(n))`，行计数随机化才直接足够。

最小符号见证：某目标行 i 的允许窗口内有两个同 residue 的实际素数 `q_alpha,q_beta`，且它们的 prime ranks 落在不同列。假设一次计数置换给该行该 residue 分配质量 1。把这一个单位给 `q_alpha`，或给 `q_beta`，均有同一个 `C'[i,r]=1` 和相同 p 边缘，却产生不同 joint 列质量。分别把两种选择固定下来，得到两种不同随机核；旧 Null A 对它们没有选择规则。这里比较的是 **synthetic null 的两种提升**，不是说已完整枚举的真实观测壳数据可以任意漏掉一个素数。真实观测的 q 集合由完整 prime prefix 和窗口确定。

若只把原 p-only 统计写成 joint 图的行和，旧 null 可继续用，因为它确实经过 R 因子化；但这个“joint 输入接口”对行内 q-rank 重排没有敏感性，不能当成新增的二维结构检验。

这是一次 BRC observer/fiber discipline 的纸面应用：保留整数质量和 `(p,q)` 标签；从带标签总体压到 residue 行计数会丢掉未来 joint 观察所需信息。未调用 BRC 程序；概率核不由正质量、精确 DIV 或 prime-prefix 证书自动推出。标准化后的 signed residual/phase 也不能混作正质量总体。

## 4. 如需 joint null，必须明确补什么

至少需要一个明确的条件随机核 `K(n' | C', 被条件化的信息)`，或等价的整数 tensor 分配合同，并指定：

1. q 候选对象是实际素数、允许 residue 的整数、prime ranks 还是抽象权重；是否保持 q 边缘、gap 信息或其他条件。它们代表不同的 null。
2. 如何把 `C'[i,r]` 分配到具体 q/rank 列；是否要求无重复、`p<=q`、原壳窗口、residue 和精确容量约束。若复制 donor 行 q 列表，目的行通常并无窗口合法性保证；若从目的行实际 q 集合取样，也可能遇到 `C'[i,r]` 大于其容量。
3. 容量不符时是禁止该置换、重新抽样、截断、允许复权还是改用其他载体。每一种都改变旧计数置换的概率律，不能把它叫作无语义变化的修补。
4. joint 归一化/格子边界及零行、空格、边界/overflow 的处理；跨 scale/width 的随机耦合；二维残差/phase 统计和 family-wise 搜索集合。

完整实际 q 枚举只给出候选支撑，不选择上述 K。用“第一个 k 个 q”、比例分摊、按观测行内比例补列、展平 24x24 后照搬 24 维循环移位，均是额外规定。其中按观测比例补列还把本来想检验的行内结构条件化保留了，零行也需要另行定义。它们并非已存在的 Null A/B。

## 5. 哪些可以修，哪些必须显式冻结

| 类型 | 合法工作与必须保留的边界 |
|---|---|
| 实现/观测修补 | 用完整 prime prefix 计算真正 `pi(p),pi(q)`；修正 row-order 冒名；持久化实际 joint 图、全 24-bin profiles、全部 cell/trim/边界、support mask 和随机选择；按当前原生算术合同给 exact/interval readout。这些不需要新 q-null 就有数据价值，但也不给 joint corrected 图或科学接受标签。 |
| gen2 已授权的同母问题修正 | 恢复几何合法零行并审计支撑；或明确另一个有理由的条件目标。它在同一母问题内，却改变原 `counts>0` 条件化后的有限 null 分布。保留旧数值/阈值作历史，实际新分布和暴露状态必须冻结；不能称为原阈值原样复现或恢复了盲性。 |
| 新统计合同 | q-rank 分配核、容量修复、joint phase 作用、逐视图联合扫描/新 family-wise 集合、改动固定 primary statistic 或原随机作用的支持。即使仍服务同一母问题，也须 owner/Driver 明确选择并冻结，不能由实现者默许；本 memo 不授权这些变化。 |

仅更换精确计算后端不会建立 coarse-stratum 交换性。增加零行也不自动证明得到正确的无条件 local-density null。既有 512/4096 次抽样、固定 seeds 和漂亮输出不能回答这些定义问题。

## 6. 对 full 21 cells 的实际决策含义

PREPARATION 的八项计划已经明确“不用 scalar p counts 偷造 q-rank 分配”“unavailable corrected view 保持 unavailable”以及 post-exposure reanalysis；这些边界应保留。

若本次交付明确是：完整观测修补、可追踪的旧一维检验修正重算、各 scale/width 的 residual/profile 和三个历史缺陷账本，21 cells 有有限判别价值，能说明该一维筛选对支撑修正的敏感性。它不能据此给未定义的 joint correction、历史 blind gate 或整个科学硬目标补上完成状态。

若预计用此次执行判定真实二维 rank 残差在两个 null 下被解释/存活，则在确定 K、phase/统计对象和可识别性边界之前，**跑满 21 cells 仍不会消除本 memo 的缺口**。应先选择明确接受 partial/reanalysis 的交付，或另行明确所需统计合同；不能仅因原生程序可运行就执行并把输出当成原硬目标的充分检验。

这不是对现有 gen2 claim 的否定，也不是正式 REQUEST_REVISION/终局判词。没有新实验结论或 all-scale 结论。

## 7. 精确来源与执行边界

仓内读取根：`D:/em/integration-pfssv-review-20260908`。冻结 main 来源：`be350eb1b0eeb2a9a07a23a43ee3c8170e93b4b4`。

| 来源 | SHA256 |
|---|---|
| `research_tasks/PRIME_FACTOR_SEMIPRIME_SHELL_RESIDUAL_VALIDATION_20260827.md` | `b4e6011b736026ab2a5fc247f8a3750163cd33909fe25cf04bec6391078157d3` |
| `research_tasks/PRIME_FACTOR_SEMIPRIME_SHELL_RESIDUAL_VALIDATION_REVISION_20260908.md` | `e1b35c812f66f105a55af54ad258d3f5381f8de33ac598ff3d806ba7b0ca0c0f` |
| `scripts/check_prime_factor_semiprime_shell_residual_validation.py` | `8772484435d77abf74e87a6f053a0edaf4fa9395bdbade93ede2413083f22140` |
| `D:/em/TEMP/pfssv-gen2-startup-preparation-20260908-EM-PFSSV-E500C7/PREPARATION.json` | `1d762ab3330521011408a782338fee86df9d4d919fe815a8c41c2c513e68c643` |

前三者的 main Git blobs 依次为 `079343422a312abc99eebba5696c03538820b024`、`e531ab46096e3b5f92cc3da6881deebc5459585f`、`c2e6319ab0f52a2ac7d0ad4845d345c96177eb8d`。仅使用文本读取、元数据 hash 和定向 Git 字节比较；没有数值结果、数值测试 PASS 或新盲测。

全局已实际运行原样 shipped-sync 缓存脚本（SHA256 `f11fda350ae622c605106ce220514e0ff8e0fa49e073d401b7c4def5b163b5a1`），返回 `LEASE_REUSED`，并读同 SHA 三入口及 BRC observer policy。checkout 自身没有该脚本，未改变 checkout 或重造同步逻辑。

Global-Knowledge-Sync: main@b2d9cef / GLOBAL_KNOWLEDGE_V1
