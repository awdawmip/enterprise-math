# 研究中控更新：Codex 部署交接已复核

日期：2026-11-22（Asia/Hong_Kong）
角色：CONTROL_PLANE_MAINTENANCE
用户本轮要求：确认已有修复和配套材料后给出 Codex 更新提示词；部署由后续 Codex 维护任务执行。

## 已完成

本轮只读核实当前后台接口、Sites v23 和既有记忆；对已提交的 FREE 登记修复作独立兼容复核，并生成了可应用于记录中已部署后端的最小整合补丁。

- 后端修复源：`791dff27134fff869eb87a6e87622dcfe5608b5e`。
- 记录中的部署基线：`91a05a8e396b1bc4468ecea9820648cb49ff63ec`。其 Nollm 接入在当前 main 中并不齐全，不能直接用裸 main 覆盖。
- 本次七文件部署补丁消除一处尾部空白合并冲突；实际应用及七个 blobs 相符。整合版六项焦点测试通过，整个 em_mcp AST 除 session_start 外保持原部署逻辑，五个记忆接口及原 research_memory 模块保留。
- 网关固定 v23 的五文件补丁可干净应用，SDK 描述与生成后 catalog 一致。实际发版更新 build 标识、使用真实版本回执的要求已写入提示词。
- 既有 Riesel v2、triangle v1 表达可成功读回，来源保持；未创建新生产身份、Task、CLAIM、Result、Review，未修改调度或运行 CI。

## 固定交付

所有物料已在 MCP main `5236142a8e97d3ddd1086704ad6808213e2b2961` 保存并作 scoped readback：

- [完整 Codex 提示词](https://github.com/awdawmip/em-research-mcp/blob/5236142a8e97d3ddd1086704ad6808213e2b2961/docs/evidence/research-flow-20261122/CODEX_UPDATE_PROMPT.md)
- [部署前复核及验证边界](https://github.com/awdawmip/em-research-mcp/blob/5236142a8e97d3ddd1086704ad6808213e2b2961/docs/evidence/research-flow-20261122/PREDEPLOY_REVIEW.md)
- [兼容部署补丁与原配套网关物料](https://github.com/awdawmip/em-research-mcp/tree/5236142a8e97d3ddd1086704ad6808213e2b2961/docs/evidence/research-flow-20261122)

## 剩余工作

Codex 在已有授权维护环境核对实际主机的当前版本与状态，按真实基线整合并安装后端，再更新现有 Sites 网关，验证线上 schema、既有数据读取与会话恢复，回写真实版本记录。当前记录不是强制回退目标；如已经存在更新，保留更新并只补实际缺项。

本轮确认的是补丁、兼容整合及交接材料可用，现场后端安装和配套网关发布尚未由本轮执行。后续可直接消费此交付，无需重做上一轮数学或全部主干分叉排查。
