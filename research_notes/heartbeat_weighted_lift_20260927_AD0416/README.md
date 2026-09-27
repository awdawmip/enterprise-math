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

## 待发布研究方向

1. WL/WM 范围与接口对照，保留所有非重叠证据并明确不能互换的观察条件。
2. 将一位仿射修复族整体推进到更深精度，保留跨层障碍、必要拆分和未展开族。
3. 直接构造质量稳定子的置换像与核，避免穷举全部森林支持或动作匹配。

任务是否正式存在，以后续不可变 V2 任务记录为准；这份说明本身不授予 CLAIM、Driver、Working Truth 或 Foundation。
