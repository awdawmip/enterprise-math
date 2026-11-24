# 研究流程减负：实现与线上效果

日期：2026-11-24（香港时间）。角色：`CONTROL_PLANE_MAINTENANCE`。

## 19:17 独立复核：已部署，接续改善；端到端提速未得到验证

本轮实际读取新 runtime、消费原部署验收回执，并通过当前 gateway 走通旧笔记、当前候选、固定来源。没有重新提交长任务查询、生产笔记、身份或 CLAIM。

- 线上 app 已于 **17:23:55 HKT** 切换为 `8e61d334f02fe2d0b38d8aeb02fe362b44ead472`，本轮轻量 status 读到 runtime `89a8b5b81124723e449342788ac938f7e6700840b1fa76801a23992f9059dcd3`，与部署记录一致。
- Nollm 已将窄补丁回移到 `945ec6f83f1983a08cc56c8232ad317079176ada`；EM reviewed code 仍是 `b9520e62e47016fc45e702b1cbfa17af8a38774f`。
- 旧 X6 `routing.v1` 经 gateway 返回 `native_revision_slot / unique`，实际候选为 `routing.v9`、坐标 `[0,2,-1]`；候选 `current=true`。旧 v1 的全部原有字段、1,345 字符正文与四条来源和之前快照一致。当前 v9 的 4,823 字符正文与四条来源也保持一致。
- 顺着候选的来源 #3，回读 `59e7d1e4...:research_notes/portable_direct/2026-11-23_r2_x6_r130_class_iv_port10_D_ray.md#L1-L20`，与 GitHub 固定提交逐行一致。三次工具往返为 1.002、1.164、1.432 秒；这是单次现场观察，不作严格速度归因。

**先前“尚未部署”与“gateway 新字段待验证”两项已关闭。** 作用范围仍是原生修订位置；没有据此宣布全局语义定理去重或改变证明接纳状态。

### 最近一次完整任务验收的真实耗时

原请求 `flow-optimization-postdeploy-20261124-c78-task-v1` 为 `SUCCEEDED`、error=null。本轮只消费这个原回执。它于 17:24–17:26 HKT 执行，Source 为 `f3e2a822d4578da4430b7928ff250cf7f78217eb`。

| Observer 墙钟阶段 | 先前验收 | 新部署验收 |
|---|---:|---:|
| 材料准备 | 41.4189 秒 | 50.0043 秒 |
| 原生 runner | 38.6776 秒 | 38.6749 秒 |
| 事件页复核 | 未出现 | 22.7609 秒 |
| 其余阶段合计 | 1.6832 秒 | 2.5016 秒 |
| 总计 | 81.7797 秒 | 113.9417 秒 |

本次增加 32.1620 秒，约 39.3%；新增复核占差额约 70.8%，材料准备增加约 8.5854 秒，native 基本未变。即便仅作算术扣除复核阶段，余下仍为 91.1808 秒，不能据此声称整体已经加速。

两次任务书 blob、reviewed code、1,774 条事件及事件 hash 相同；Source 前进 50 个提交，190 个路径变化。因此这不是严格同输入 A/B，不能把材料准备增时因果归给本批改动，也不能把离线样例降幅当作线上收益。

### 事件复核的触发边界

实际部署源码 `EventCollection._ensure_issue` 比较旧 spool 的 `id/comments/updated_at`；本次旧缓存 1,773 条与当前 1,774 条不同，触发新 generation。following 读取复用 `current_read_collector`，同一缓存世代在 guard 未变化时不应为同一差异反复重建。进程重启、collector 重建、Issue 再变化或特定 freshness 错误会重新触发检查。`restart_reason` 会留在 admission 中，后续回执仍显示旧理由不等于重新支付该阶段耗时。本轮没有另起长查询证明后续缓存命中耗时。

下一步应定位仍占约 50 秒的材料准备和约 39 秒的原生状态计算内部成本；事件复核按实际复用行为观察，不直接删除一致性检查。速记本接续已产生可用收益；正式任务读取的主要等待仍需优化。没有新增 CI、周期巡检、登记入口或科学准入步骤。

依据：[部署完成记录](https://github.com/awdawmip/em-research-mcp/blob/46ecd63f0aefb1e893458d6d2d57980e9784865c/docs/evidence/research-flow-optimization-20261124/DEPLOYMENT_COMPLETION.md)；[实际 EventCollection](https://github.com/awdawmip/em-research-mcp/blob/8e61d334f02fe2d0b38d8aeb02fe362b44ead472/src/control_event_collection.py)；[实际共享 collector 调用](https://github.com/awdawmip/em-research-mcp/blob/8e61d334f02fe2d0b38d8aeb02fe362b44ead472/src/control_jobs.py)。

---

## 16:50 交付时记录（历史保留，以以上更新为当前状态）

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
