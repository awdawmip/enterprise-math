# 局部研究与筛选工具任务集：2026-11-01

Taskset-ID: `LOCAL-RESEARCH-AND-SCREENING-20261101-6DE891`
Author: `EM-DIRECT-6DE891` / `RESEARCHER`
Research-Activity-ID: `RA-8E6CD423FB56C546A17CFE76`
Prepared-At: `2026-11-01T14:35:00+00:00`

## 用户要求与研究原则

用户要求更新全局规则，防止把整体证明、全范围闭合或全面性能胜出当作局部研究的起步门槛；并把本轮发现的问题整理为正式任务集，发布到状态机。

全局更新已经写入现有唯一规则正文 `conclusion_contract.progression`：局部构造、特殊解、受限算法、有限精确窗口和有预算的工程试探均可独立推进。评价试探时计算命中收益、失败成本和资源取舍；结论和已证错误保留其实际范围。有效的局部成果不依赖先完成整体证明，也不强制每轮产生正例或新普适定理。

规则来源：[已发布的全局规则](https://github.com/awdawmip/chatgpt-global-knowledge/blob/c60dac11d1b5dfb7275520fbd4c9b29ee1c8aa6f/knowledge/preferences/OUTPUT_TEMPORAL_SEMANTICS_POLICY.json)。仅修改该字段；现有 46 项回归测试通过，远端精确回读一致。

## 本次正式发布

本提交将以下四份任务书与各自 V2 不可变发布记录一起原子写入。任务书状态为 `READY`；发布记录为 `ACTIVE`、`claimable=true`。四项使用真实研究员发布身份，实际级别均为 `P2/MEDIUM`；前两项保留 `P1/HIGH` 请求。发布不表示已领取或已开始执行。

| 任务 | 首个工作单元 | 可接受的局部交付 | 正式来源 |
|---|---|---|---|
| 粗素因子奇偶状态维护 | 选 K=2 或 K=3，重放一次和两次素数插入，保留精确子尺度 | 维护算法、共享状态规律、具体修复，或有信息增量的维护成本界 | [任务书](../../research_tasks/RS-ROUGH-PARITY-LOCAL-STATE-UPDATE-20261101.md) · [发布记录](../../research_task_records/RS-ROUGH-PARITY-LOCAL-STATE-UPDATE-20261101/TP2-13B36639D27B58C98C02.json) |
| 局部筛选前缀的净收益 | 固定后端、位长及 M=1000，比较既有 kernel13/learned20 与完整回退 | 一块可复现收益区域，或该预设区域的完整成本模型及无收益原因 | [任务书](../../research_tasks/RS-BRC-LOCAL-PREFIX-NET-VALUE-20261101.md) · [发布记录](../../research_task_records/RS-BRC-LOCAL-PREFIX-NET-VALUE-20261101/TP2-A2DB6A0428DC8F6E2EE0.json) |
| 免表尾部的局部成本 | 从证书/预测器共享、阶数选择或短串复用中只选一项 | 保留精确传输及两校正条件的一项资源改进，或明确局部成本边界 | [任务书](../../research_tasks/RS-BRC-TABLEFREE-TAIL-LOCAL-COST-20261101.md) · [发布记录](../../research_task_records/RS-BRC-TABLEFREE-TAIL-LOCAL-COST-20261101/TP2-7AA587095F56589D45F7.json) |
| 原稿筛选实现修复 | 重放 Lucas 和 wheel 两个失败输入，修复状态、预处理及共享预算 | 两个可验证因子的修复回归、预算终止、明确返回类型及独立验证 | [任务书](../../research_tasks/RS-FERMAT-LANDAU-SCREENING-IMPLEMENTATION-REPAIR-20261101.md) · [发布记录](../../research_task_records/RS-FERMAT-LANDAU-SCREENING-IMPLEMENTATION-REPAIR-20261101/TP2-A3769AB88B65DCB73E47.json) |

## 标识、归属与接续

### 粗素因子有界深度奇偶状态：素数插入更新与局部成本

- Task-ID: `RS-ROUGH-PARITY-LOCAL-STATE-UPDATE-20261101`
- Publication-ID: `TP2-13B36639D27B58C98C02`
- Parent Objective: `OBJ-GEOMETRY-BRC-RESIDUAL-ACCUMULATION-SYSTEMS` / `OG-7AE66316D7566C519AE0`
- Origin / lineage: `DIRECT_USER_DIRECTION` / `INTEGRATION`
- 第一行动：固定 y、K∈{2,3}、一个有限有序粗素数窗口与相应精确子尺度集合，消费已给奇偶读出式；从 F_new(T,z)=F_old(T,z)+zF_old(T/p,z) 推出二项矩/原始矩的更新，并核查一次和两次实际素数插入。

### 既有 BRC 局部前缀组合：固定预算净收益与适用区域

- Task-ID: `RS-BRC-LOCAL-PREFIX-NET-VALUE-20261101`
- Publication-ID: `TP2-A2DB6A0428DC8F6E2EE0`
- Parent Objective: `OBJ-SEMIPRIME-SQUARE-SHELL-FACTORIZATION` / `OG-94F9DC002F795C10ACF9`
- Origin / lineage: `DIRECT_USER_DIRECTION` / `CONTINUATION`
- 第一行动：调用现有 kernel13_prefix/kernel13_order、learned_cover_order、multiplier_probe_batches 与 RegimeShortcutLedger；固定一个真实求值后端、一类预先定义结构输入及独立对照分布，先比较结构顺序和固定预算前缀的成对总成本。

### 免表尾部两校正传输：证书共享、阶数选择与局部资源成本

- Task-ID: `RS-BRC-TABLEFREE-TAIL-LOCAL-COST-20261101`
- Publication-ID: `TP2-7AA587095F56589D45F7`
- Parent Objective: `OBJ-SEMIPRIME-SQUARE-SHELL-FACTORIZATION` / `OG-94F9DC002F795C10ACF9`
- Origin / lineage: `DIRECT_USER_DIRECTION` / `CONTINUATION`
- 第一行动：固定 source state mN=J²+R 与 h∈{1,2}，读取实际 lower_increment、two_correction_certificate、transport_certified_tail；列出重复幂/分母和阶数选择费用，选择其中一种机制完成一个局部优化。

### 原稿筛选实现修复：Lucas 复合、轮素因子预处理与统一预算

- Task-ID: `RS-FERMAT-LANDAU-SCREENING-IMPLEMENTATION-REPAIR-20261101`
- Publication-ID: `TP2-A3769AB88B65DCB73E47`
- Parent Objective: `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION` / `OG-AA2BAD92F59DC97880C7`
- Origin / lineage: `DIRECT_USER_DIRECTION` / `MAINTENANCE`
- 第一行动：从固定原稿提取 Lucas 二次分支和 wheel_factorial_dichotomy_factor 原实现，先在声明的解释器中重放 N=108391,B1=50,k=2 与 N=1497,D=210；固定一个共享预算/因子验证结果协议，再依次修复两个错误并加入预算终止。

两项 CONTINUATION 接续真实的半素数平方壳母任务，各自具有完整的六字段 successor gate。奇偶状态任务集成已有局部推导与插入递推；筛选修复任务维护本轮原稿实现。这两项不伪造不存在的前序 Task。四项任务均无等待全局证明的任务依赖。

## 复用与查重决定

- PrimeFusion 候选生成、既有 Hart residual streaming 成本审计、QR/CRT 隐式索引以及通用 PCF benchmark 保持其现有任务；本批复用其相关接口和证据。
- 免表源码已实现齐次 Horner 并缓存系数，本批聚焦尚未完成的共享计算和阶数费用。
- 已取得的粗因子精确窗口作为输入，任务增量是状态维护与实际成本。
- 原稿实现修复限定 Lucas 二次分支、wheel 小素因子预处理和统一预算。其他分圆分支的理论问题保留为来源中尚未完成的问题，不作为本次工程验收前提。

## 可重放的输入

- [原稿精确副本](https://github.com/awdawmip/enterprise-math/blob/a5902327c911630a2c6a387fbbc4822232edaebd/research_inputs/2026-11-01/fermat_landau_wheel_dichotomy_complete_monograph.md)：28957 bytes，SHA-256 `af082f3c0485a309346a7e92791b7b75ff62f62e2db549d970900e9a5d4b95ad`，已回读核对。
- [原稿核查与具体复算](https://github.com/awdawmip/enterprise-math/blob/1e41c0acc37b9347c91c1d4ded6327433d898edb/research_notes/2026-11-01/fermat-landau-monograph-review-6de891.md)。
- [局部研究与粗因子奇偶窗口](https://github.com/awdawmip/enterprise-math/blob/212b6f7ee3966535db9376686ee6263271533713/research_notes/2026-11-01/local-solutions-and-parity-windows-6de891.md)。
- 具体回归：Lucas 的 `N=108391, B1=50, P=3` 应得到 `V_E mod N=87421` 并提取 `107`；wheel 的 `N=1497, D=210` 应在轮素因子预处理取得 `3`。已知因子仅用于离线验证，运行时不得输入隐藏分解。

## 发布验证边界

四个候选使用未修改的原生 writer、taskbook lint、严格不可变记录审计与实际 parent-objective gate。三套母目标均为 OPEN 且代次有效；两项接续任务的 parent publication 唯一且任务书 blob 精确匹配。相关完整 Git 树与例外表用于确认新 ID、路径及 publication ID 不存在，未借用旧任务的历史豁免。

写入父提交 `8c21590456c07ad03baa2a1573cd8feffa186cb1` 上，180 项有关原件的 Git blob 与已校验来源一致；任务书和发布记录完整目录树未变。详见 [限定范围的发布前验证记录](local-research-taskset-preflight-6de891.json)。该验证只覆盖本批任务及其实际父链，不声称全库审计通过，也不授予数学证明、Working Truth 或母目标完成状态。

后续执行从各任务书的 next_action 开始，结果按所选局部输入、操作和资源条件报告。
