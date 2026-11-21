# 线索深研后的新任务包（待正式发布）

日期：2026-11-21。提交人：EM-DIRECT-949983 / TASK_RESEARCH；Activity：RA-4EC67378C53C5B821B1C43F6。

**当前状态：本包是可审核、不可领取的草案。三项正式Task与新父目标尚未创建。** 科研成果已保存并回读于 [固定科研提交](https://github.com/awdawmip/enterprise-math/tree/7ad53ff4d8168f4800fc49270b197f14defd0b4c/research_notes/portable_direct/google_clue_deepening_20261121)。原作者EM-DIRECT-3DCA45的模型、证明与2026-11-16提案继续保留原归属。

## 为什么改写旧提案

本轮不是简单重发原三份草案：

| 已取得的结果 | 本次真正未解的任务 |
|---|---|
| 局部空/单例计数闭式；所有k的精确模4算法；449的非中心反例 | 非中心奇位置的定位、例外参数族与结构分类 |
| 所有连续窗口的原始噪声锐半径及90份有理证书 | 非线性整数计数模型的有限尺度余项、合法观察实验和认证噪声保障 |
| v=0的六个次阶模板；未知参数下完整系数/平移商首交点48/39 | 一般v的同首项水平纤维与次阶分类、交点处高阶恢复 |

原 RS-SEVEN-PHASE-RAW-NOISE-RADIUS 从未正式发布，其数学问题已作者侧解决，因此不会为它伪造完成事件；新的有限尺度问题使用新ID。模4与消去层原ID继续承载其尚未解决的母问题，正文已明确已解边界。

## 三项任务

- [RS-ERDOS1063-SINGLE-EXCEPTION-MOD4.md](RS-ERDOS1063-SINGLE-EXCEPTION-MOD4.md)：单异常模4计数的非中心奇位置结构。
- [RS-PHASE-RAW-NOISE-FINITE-SCALE-BRIDGE.md](RS-PHASE-RAW-NOISE-FINITE-SCALE-BRIDGE.md)：原始噪声定理到有限整数计数的有效桥梁。
- [RS-SEVEN-PHASE-CANCELLATION-LAYER.md](RS-SEVEN-PHASE-CANCELLATION-LAYER.md)：一般分母误差下的消去层分类与高阶恢复。

三项均有具体对象、固定来源、边界和验收；不预设研究方法或强制思考顺序。P2/MEDIUM是当前研究者草案档位，不表示已生效的任务排序或领取。

## 待建立的父目标

[proposed_objective.json](proposed_objective.json) 保留原拟议ID OBJ-GOOGLE-20261116-ERDOS1063-SEVEN-PHASE，并按新结果修订范围。其内容覆盖二项整除联合计数和精确计数的有限相位观察，不扩大到泛化的所有公开数学问题。

本轮读取22个现有父目标head，其中18个OPEN的完整scope，未找到真正覆盖本批来源与对象的现成目标。明细在 open_objective_scope_review.json。不能仅因标题类似，将本批错绑到其他来源/定理的目标。

用户“仔细研究一下找到的线索，发布新的任务”已授权科研和普通Task发布。现行research_role_policy.json允许RESEARCHER直接发布普通Task，但driver_activation要求当前对话明确启用Driver；research_objective_contract.json又将新父目标的发布/选头限定为RESEARCH_DRIVER。当前未发生这项角色启用，故还没有实际OPEN父代次。具体规则和本轮窄范围核验见 DRIVER_ACTIVATION_NARROW_REVIEW.md。

下一项仅需当前对话明确启用该组任务范围的Research Driver，之后以本会话自有身份完成原生DA，建立并选定父目标，再正式发布任务。无需重新确认科研、成果保存或普通Task发布，也不借用其他会话的权限。

## 发布材料与核验状态

- bundle.json：科学来源、旧题处置及当前精确未完成状态。
- taskset.json：草案、未来正式路径和研究价值。
- proposed_objective.json：完整目标正文，无虚构代次或发布者。
- prepare_google_taskset.py：在实际仓库中调用当前原生writer；没有远端调用。需真实Driver和已同步的权威材料，产生本地目标/任务候选事务后仍须原子CAS及固定提交回读。
- draft_validation.json：实际运行当前原生taskbook结构检查。每份草案仅有预期的未发布authority项（校验器要求PUBLISHED_REGISTERED，而草案诚实保留PENDING_PUBLICATION）；没有篡改状态来消除该项。完整目标/任务权威审计尚未运行。
- control_observations.json：本轮原生精确任务查询的真实回执字段；目录缺席只证明固定Source未见正式记录，不赋予owner或执行权。
- source_blobs.json：本轮使用的原生合同/脚本来源固定信息。

真实发布时，应读取当时必要的现行权威与同项状态；若已有发布或父目标，核对原事务而不重复创建。保持本包固定科研证据，无需把数学成果随控制面新头重算。按实际父代次准备Taskbook与不可变publication record，两者同批集成；核对全部源字节、父代次及原生运行状态。正式发布本身不产生CLAIM或数学受理。
