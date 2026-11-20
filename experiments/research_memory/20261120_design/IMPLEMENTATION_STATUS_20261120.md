# 研究记忆接入实施状态

记录时间：2026-11-20 22:49（UTC+08:00）。状态：代码已实现并通过本地验收；线上后端安装与真实对话验收待执行。

## 当前执行入口

主实施入口为 [em-research-mcp PR #112](https://github.com/awdawmip/em-research-mcp/pull/112)，固定实现提交 `91a05a8e396b1bc4468ecea9820648cb49ff63ec`。其中包含详细实施步骤、代码、测试要求、网关完整补丁、实际验证记录和 Codex 提示词。它是后续部署接续入口；本 EM PR 保留设计与项目侧状态，不另派重复任务。

- [实施步骤与测试范围](https://github.com/awdawmip/em-research-mcp/blob/91a05a8e396b1bc4468ecea9820648cb49ff63ec/docs/NOLLM_MEMORY_INTEGRATION_20261120.md)
- [Codex 提示词](https://github.com/awdawmip/em-research-mcp/blob/91a05a8e396b1bc4468ecea9820648cb49ff63ec/docs/NOLLM_MEMORY_CODEX_PROMPT_20261120.md)
- [真实验证记录](https://github.com/awdawmip/em-research-mcp/blob/91a05a8e396b1bc4468ecea9820648cb49ff63ec/docs/evidence/nollm-memory-20261120/VALIDATION.md)

## 已完成

1. Nollm [PR #7](https://github.com/awdawmip/Nollm/pull/7) 已补入直接 API 修复，固定提交 `ddf7dc00b2cea43dccc5d783d20aa88e21de4e0b`：保存 Host 已形成的有来源理解无需本地 Git 工作区，共享 describe 返回当前版本状态。原生几何与持久格式保留。
2. 后端实现 `em_memory_walk/show/source/save/find`，复用原连接，使用独立持久场；普通记忆调用与正式科研控制队列分开。
3. 网关扩展同一组工具，记忆预检使用轻量身份读取，精确回源直接使用现有固定提交读取；修复目录刷新覆盖现行参数的问题。
4. 新记忆工具使用线程执行，同一场保持一个访问点；实际测试证明慢原文读取期间另一条记忆读取可继续。
5. 网关正式构建、源码推送和 archive 保存已完成，候选为 **Sites v22**。待相应后端可用后再发布原插件。

## 测试结果

| 范围 | 结果 |
| --- | --- |
| Nollm 安装后 API 与原科研 CLI | 2 unittest PASS；空场/读取不改持久文件探针 PASS |
| 后端与真实 Python MCP | 9 PASS，0 FAIL |
| 网关、目录刷新与原控制回归 | 129 PASS，0 FAIL，0 SKIP |
| 网关 → 真实 Python MCP → Nollm 的本地跨层链路 | 1 PASS，0 FAIL，0 SKIP |
| Sites 正式构建及候选保存 | PASS |

本地跨层测试只替代外部 GitHub 网络输入；鉴权、MCP、MaterialService、原生导航和文件持久化实际执行。新进程可以取回与修订已有理解。真实新模型对话的取回仍属于部署后验收。

## 下一步与范围

在已有维护环境完成后端安装及原场重启保持，再发布保存的 v22，核验原插件在实际研究对话中能导航、回源、保存／修订及由后续会话取回。本次执行器缺少主机维护供值，已经把可独立完成的实现、构建和本地测试做完并持久保存。

按用户要求保持可信内部试验组件：直接复用原生核心，不新增防御框架、内部哈希或研究登记前置。当前知情研究场的接入不改变 FREE A 阶段的适用来源范围；科研净收益继续在实际研究中观察。
