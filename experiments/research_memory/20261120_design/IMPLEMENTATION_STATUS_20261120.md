# 研究记忆接入实施状态

记录时间：2026-11-21 08:31（UTC+08:00）。状态：**后端与原中控台插件已上线，本轮真实接口复审通过；坐标说明修复已随 Sites v23 发布。**

## 当前执行入口

主实施入口为 [em-research-mcp PR #112](https://github.com/awdawmip/em-research-mcp/pull/112)。最新复审材料已保存于 `4161ceeb788d5bf639517d247776b1b0b40f422d`：

- [上线复审、测试范围与结论](https://github.com/awdawmip/em-research-mcp/blob/4161ceeb788d5bf639517d247776b1b0b40f422d/docs/evidence/nollm-memory-20261121/ONLINE_AUDIT.md)
- [原始线上回执](https://github.com/awdawmip/em-research-mcp/blob/4161ceeb788d5bf639517d247776b1b0b40f422d/docs/evidence/nollm-memory-20261121/online-evidence.json)
- [独立读者试用](https://github.com/awdawmip/em-research-mcp/blob/4161ceeb788d5bf639517d247776b1b0b40f422d/docs/evidence/nollm-memory-20261121/fresh-reader.md)
- [原部署与服务重启记录](https://github.com/awdawmip/em-research-mcp/blob/55a8bf411e0b7f37529a1505475a261945ec9dfd/docs/evidence/nollm-memory-20261120/johor-live.json)

本 EM PR 保存项目侧实施与验收状态。完整内部部署材料留在原实施仓库；不另行派发重复科研任务。

## 实际版本

| 部分 | 当前对应 |
| --- | --- |
| Python 记忆业务文件 | `91a05a8e396b1bc4468ecea9820648cb49ff63ec` |
| Nollm 已安装运行库 | `ddf7dc00b2cea43dccc5d783d20aa88e21de4e0b`，原 PR #7 |
| 初始线上网关 | v22，2026-11-20 23:57:02 +08:00 发布 |
| 当前网关 | v23，`e9dc770e03f39132d8a3dd4ab5d5cd7be4f91d56`，2026-11-21 08:26:41 +08:00 发布 |
| 当前工具 | em_memory_walk / show / source / save / find |
| 工作场 | 原后端独立持久目录，代码升级复用已有场 |
| 接入方式 | 同一个 Enterprise Math MCP Gateway 插件 |

后端与 Nollm 实验分支尚未全部集成到基础分支；后续安装按精确部署依赖继续，避免仅从 main 打包时遗漏记忆模块。

## 本轮真实验收

1. 本对话直接调用五工具，读回既有科研理解，原生 Surface 导航取得所选区域正文。
2. 两段固定科研原文共 39 行与 GitHub 固定提交逐行一致；保存和修订后的来源顺序保持。
3. 一条明确工程验收记录经历 v1→v2→v3 两次原位修订。旧正文保留，current 正确，当前检索与原生召回只返回当前版；既有科研理解未改变。
4. 独立任务历史子代理未获笔记 ID/坐标，仅凭语义问题通过 3 次 walk 和 2 次 source 找到目标理解与来源。它作为子代理上下文试用单列，不冒称新的人类 ChatGPT 对话。
5. 并发修订竞争、绑定写入失败后的可恢复状态两项本地探针通过。
6. 修复后的 15 项相关网关回归、正式构建与发布通过；发布后通过原插件读到新版网关标识，原科学笔记与工程笔记均保持。

原代码的 2 个 Nollm unittest、9 个后端测试、129 个网关测试和 1 个真实本地跨层测试复用已有效证据，本轮没有重复计为新增运行。原服务重启证据来自部署记录，本轮未另行重启服务。

## 已修复的使用卡点

v23 明确 `walk.entry/cell=[layer,q,r]` 与 `save.at=[q,r]` 的对应，修订使用新的 note_id 加旧 current note ID；show 提供有序来源列表。旧部署试用已经因三元坐标误传报错一次，这次直接修在模型实际看到的工具说明中。

网关 GitHub 镜像、Nollm PR7 和本设计包的“尚未部署”状态已纠正。当前长对话的工具说明缓存仍为旧值；服务端新版本已被真实调用确认，参数不变，功能正常。

## 下一步与实际范围

当前场有 13 条既有研究理解，本轮另加一条工程记录；已有两会话样例主要延续同一 CRT 前缀系列。下一步应在实际跨研究线问题上比较记忆与直接来源读取，记录正确联系、条件误用、查询过程和形成/维护总成本。全库覆盖、自动语义连线和净算力节省尚需相应证据。

继续保持用户要求的可信内部试验组件：复用原生核心和现有来源，不新增防御框架、无谓哈希或研究登记前置。当前场用于 TASK/知情研究；FREE A 冻结前仍沿适用基础与精确问题来源。本状态更新不改变科学成果接纳或任务状态。
