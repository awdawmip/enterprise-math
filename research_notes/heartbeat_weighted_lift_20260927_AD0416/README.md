# 心跳世界：WL 原始成果保全与后续研究入口

本目录按2026-09-27用户要求发布原始研究包 `9d04076c502f03254659ba51d3d6a839b475c444`。原文中的 LOCAL / REMOTE_PENDING 是原研究时点的历史状态，不作追溯改写；本次发布由 PUBLICATION.json 另行记录。

## 成果与代码

- [完整原始研究报告](RESEARCH_NOTE.md)
- [六项 WL 定理候选](THEOREM_LEDGER.json)
- [原始精确结果](RESULTS.json)
- [原始验证范围](VALIDATION.json)
- [BRC 执行载体与观察凭据](BRC_EXECUTION_RECEIPT.json)
- [原始工具源码](snapshot/src/enterprise_math/heartbeat_weighted_germ_lift.py)
- [原始25项测试](snapshot/tests/test_heartbeat_weighted_germ_lift.py)

## 与当前主干 WM 版本的关系

当前主干已经有另一版同名模块，来源提交 `6dd526fbf08aa97baea181548c0d8240f7c12b82`，工具源码 blob `9cb12b10890a14d179ea3aa036fcde1b08728134`，使用 HBW-WM 定理编号和不同接口。本次没有覆盖该模块、测试或注册同名方法。本目录保存 HBW-WL-001..006 及其6个接口的原始证据，不能把 WL 的25项测试算成 WM 的验证，也没有宣称两版等价。

`snapshot/` 中的源码与测试保持原字节，用于对照和精确保全；该子目录没有复制完整依赖，不是当前主干可直接替换安装的第二个包。完整可执行依赖、清单和历史在下面的独立 Git bundle 中。

## 完整研究包（Google Drive）

[heartbeat_world_weighted_germ_lift_20260927.bundle](https://drive.google.com/file/d/1ZAzCk7o_TkKTaZUJYkP5Uqeebdjlxk7U/view)

大小：398738字节。SHA-256：`882167fc6b3fbdf58d9804032805bcf09f65652257b72534594c106b51918f55`。
已通过连接器上传到 EnterpriseMath-Handoffs，并下载回读核对完整字节。原196项清单在本次发布前全部哈希匹配；本次属于保全和任务发布，不冒称重新完成数学审稿或全仓测试。

## 已发布的后续研究任务

三个任务书与对应不可变 V2 记录已在 `2d547b3e07cf21c0b54e5e5b3e0da7cc9ae1eb61` 发布，六个文件的完整读回和 blob 对应关系见 [交付核验](DELIVERY_PUBLICATION_20260927.json)。

| 顺序 | 任务与研究目标 | 不可变 V2 记录 |
| --- | --- | --- |
| 先行 | [WL/WM 范围与接口整合](../../research_tasks/RS-HBW-WL-WM-RECONCILE-20260927.md)：保留非重叠证据，明确哪些输入、观察和部分输出可互换 | [TP2-E06E64EA9A7F37145AC3](../../research_task_records/RS-HBW-WL-WM-RECONCILE-20260927/TP2-E06E64EA9A7F37145AC3.json) |
| 依赖先行任务 | [多层共同质量修复族的符号传播](../../research_tasks/RS-HBW-WEIGHTED-MULTILAYER-FAMILY-20260927.md)：整体推进修复族，保留跨层障碍、必要拆分和未展开族 | [TP2-5579F1B38B4D8C3085AB](../../research_task_records/RS-HBW-WEIGHTED-MULTILAYER-FAMILY-20260927/TP2-5579F1B38B4D8C3085AB.json) |
| 依赖先行任务 | [共同质量稳定子的像与核直接构造](../../research_tasks/RS-HBW-WEIGHTED-STABILIZER-IMAGE-KERNEL-20260927.md)：避免穷举全部支持，并交付覆盖完整性的证书 | [TP2-C593366399C0E3EF6EB6](../../research_task_records/RS-HBW-WEIGHTED-STABILIZER-IMAGE-KERNEL-20260927/TP2-C593366399C0E3EF6EB6.json) |

任务元数据为 RESEARCHER 默认 P2/MEDIUM，保留 FIRST_TIER_PORTFOLIO 标签；发布记录不自动证明当前运行时可领取、已经 CLAIM 或已经执行。实际执行继续服从当前派发、依赖和所有权门禁。本说明不授予 Driver、Working Truth 或 Foundation。

## 中断后的恢复核验

本次续接再次核对 Drive 原包完整字节及196项清单，并核对三个任务书与三个 V2 记录，没有重复上传、创建任务或重跑科学测试。控制回执的错误 Issue 指针及真实服务状态单独记录在 [CONTROL_DELIVERY_STATUS.json](CONTROL_DELIVERY_STATUS.json)：原 session_start 请求实际为 #2514，不是 #2517；原超时失败回执与当前可见的服务会话均保留，不能据此推断正式执行权限或 PRE_FINAL 通过。
