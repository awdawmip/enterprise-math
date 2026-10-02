# Actions CI 后续任务交接

当前用户指令：把 GitHub Actions 检查发现的后续任务发布到状态机。发布人 Driver-ID: EM-DVR-E8DCE5，CONTROL_PLANE；不借 Owner 身份，不领取研究。

已完成：读取失败运行及对应配置，区分代码阻塞与账户级未知；核对现有任务去重。原始公开 CI 证据见同目录 EVIDENCE.json。知识库的完整私有日志与账户资料保留在原授权边界，接手者从原链接读取。

待执行任务：

1. RS-GOV-EM-CI-DEPENDENCY-REPAIR-20261003：补全 quality 真实依赖，并核对 pytest 参数化函数与 unittest 分片运行器的兼容性。必须证明用例真正执行；只消除 import 报错不足以关闭。
2. RS-GOV-KB-CI-DEPENDENCY-REPAIR-20261003：知识库工作流使用仓库已有受控 jsonschema 依赖入口，在干净环境执行原测试和索引检查，保留私有资料边界。
3. RS-GOV-EM-MIGRATION-BASELINE-REPAIR-20261003：修复已达目标状态被误判为 pending 的 no-op 幂等问题；特别覆盖 old == target == false。保留历史基线，真正 pending 仍须精确基线；第三状态、非目标字节与受保护语义校验继续拒绝不合法变更。

接手条件：读取对应不可变 publication、任务书、当前 Source；依法注册自身执行会话并领取适用任务。任务间不设虚构依赖，可以独立本地验证；发布不意味着自动启动或修复完成。禁止跳过失败测试、放松校验、强推、触发 Actions、部署、扩大网络/凭据权限或重做 xhome S15。远程执行须另有明确授权；本任务默认本地验证并以 [skip ci] 发布最小修改。

外部待办：账户用量需用户在 GitHub 账单页核验，现有集成读取为403；不假定余额耗尽或正常，也不把该读取权限作为三个代码修复的前置条件。当前两仓少量产物无需创建清理任务。

父目标 OBJ-GITHUB-ACTIONS-CI-BLOCKER-REPAIR-20261003 保持 OPEN，直到三项子任务各有可复核终结或明确合法承接。本次只完成后续任务发布。
