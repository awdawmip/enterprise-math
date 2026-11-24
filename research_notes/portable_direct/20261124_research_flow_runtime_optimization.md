# 研究流程减负：已发布实现与待部署前沿

日期：2026-11-24（香港时间）。角色：`CONTROL_PLANE_MAINTENANCE`。本记录保存工程进展，不是数学结果、研究任务发布或执行授权。

用户要求继续规划和优化，重点保持数学研究推进、自由记录、准确引用和低负担接续。本次从上轮线上实测的 Source materialization 与 native runner 重复工作入手，并补齐旧速记本的原生修订定位。

## 已完成

MCP 已发布至 main：[3571a2d7d65aa1c78134ce43bc5d56f41e126d86](https://github.com/awdawmip/em-research-mcp/commit/3571a2d7d65aa1c78134ce43bc5d56f41e126d86)。两个实现文件、两个针对性测试及五份交付文件均逐文件远端读回，正文与 Git blob 一致。

- 保留现有验证器已经返回的执行代码子树，避免后续请求重复校验历史非代码资料；当前 data tree、代码 pin 与 policy 校验保留。
- 材料缓存大小在本次调用内按替换差值更新，避免每个文件重复求整份容量总和；原淘汰和边界行为保留。
- native guard 在本次 scope 内按目录前缀检查缺失输入，省去每个目录遍历整树；按需补入、字节校验和真实枚举保留。

Nollm 已发布至 main：[ac587624411fe9c1270317cc89f816efd1ccb535](https://github.com/awdawmip/Nollm/commit/ac587624411fe9c1270317cc89f816efd1ccb535)。两源文件和一个测试逐文件远端读回一致。历史笔记可以返回 `continuation`，作用范围限定为已有 `native_revision_slot`：利用现有物理 binding 与明确的 `revises` 证据给出当前候选，保留原 ID、正文、来源和 current 状态。缺证优先标为 incomplete；独立谱系、reuse/support 与语义定理去重不在本字段范围。

## 实际验证及限制

合并后的 MCP 16 个标准 unittest 通过，其中既有 Activity 集成测试含四个依赖场景。guard 原版/候选的 29,348 组预检及 560 组真实 glob/rglob 对比无差异，完整 2,451 条规模化缺失请求一致。组合部署补丁通过 git apply 检查及四个应用后文件的完整字节比较。

Nollm 部署版本与当前主干各通过七项真实临时 field 流程，当前主干另外两项既有安装流程通过；已核验实际 6e1b 后端 show 与工具注册的开放字典透传，SDK fixture 保留 continuation。Gateway 新字段的实际线上读回留待部署后确认。

合成 20,000 条目、5,600 文件的真实 materializer 本地交替测试，冷装载中位数 2.851→2.295 秒，暖缓存且 Source 前进 1.436→1.044 秒；输出字节、文件集与请求数量一致。164 次目录预检中位数 0.21587→0.00349 秒，scope 建立 0.19756→0.20075 秒。这些是局部离线结果，不能换算成线上延迟。

完整 pytest 未运行：环境缺少 pytest，没有安装依赖或伪造替身。没有新增 CI 工作流、周期任务、研究登记要求、生产笔记、身份或 CLAIM。

## 实际部署基线与下一步

上轮部署已验收，记录仍有效：[POST_DEPLOY_CHECK](https://github.com/awdawmip/enterprise-math/blob/f4f69a9488cdf6d649f2a862548720653e1b6e6b/research_notes/portable_direct/20261124_research_flow_burden_reduction/POST_DEPLOY_CHECK.md)。最近核实的后端 app 为 6e1b2fd7...，runtime 为 e294ccd...，Nollm pin 为 ddf7dc00...。C78 只读任务查询成功，observer 共 81.7797 秒，其中装载 41.4189 秒、native 38.6776 秒。该回执没有提供初始路径数；不能套用另一任务的 5,600 条观测。

本批新代码已经发布，**尚未部署到后端主机**。当前会话没有该主机部署工具。已将所有实现、窄补丁、源版本和受影响流程验收集中在一个持久入口：

[Codex 部署提示词](https://github.com/awdawmip/em-research-mcp/blob/3571a2d7d65aa1c78134ce43bc5d56f41e126d86/docs/evidence/research-flow-optimization-20261124/CODEX_UPDATE_PROMPT.md)

优先把小改应用到实际后端和当前 Nollm 安装，不将整个新主干覆盖到不同的部署谱系。部署后沿旧 X6 v1 读取实际后续候选并回读来源；对原 C78 任务进行只读查询，比较实际阶段与输入差异。若仍慢，根据实际成本选择下一处优化，不新增预计算、索引、周期审查或研究准入流程。

对于不同角度的证明，现有修订定位能减少误读旧版本，但不能自动判断数学等价。后续研究应在实际命题与固定原文上区分同条件重做、条件推广、反例、替代证明和独立复核；不以另建登记表代替这种判断。

完整依据：[实现与验证报告](https://github.com/awdawmip/em-research-mcp/blob/3571a2d7d65aa1c78134ce43bc5d56f41e126d86/docs/evidence/research-flow-optimization-20261124/REPORT.md)；[原始验证数据](https://github.com/awdawmip/em-research-mcp/blob/3571a2d7d65aa1c78134ce43bc5d56f41e126d86/docs/evidence/research-flow-optimization-20261124/validation.json)。
