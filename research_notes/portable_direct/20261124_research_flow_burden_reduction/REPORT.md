# 研究中控读取减负：上线与实走记录

Progress-Event-ID: `20261124T032354Z-research-flow-light-read-f52de59801bc`
At: `2026-11-24T11:23:54+08:00`
Role: `CONTROL_PLANE_MAINTENANCE`
Scientific-Status: `NO_NEW_MATHEMATICAL_CLAIM`

现有 Sites 中控已上线 `em-sites-gateway-20261124-light-read-r1`，源提交 `c076ce7af761beccc01faf84b90d5b2f8b3d84b4`。普通操作的身份前置检查使用已有轻接口；显式轻状态省去内嵌 Driver 合同，完整合同仍可按需取得。相同紧凑 JSON 口径的线上轻状态返回从 23,556 字符降至 3,431 字符（减少 85.4%）；该比例只描述返回长度。

修改后的实际连接、轻身份、按需合同、原成果请求回读、RH 固定原文与 X6 当前笔记接续均已走查。X6 在此次观察时为 `X6.R90.near-directions.sharp-port.20261123.routing.v9`。旧 v1 能标记非当前，却没有直接的继任版本指针；最新证明原文需要沿该段固定 GK 链接读取，旧编号 EM sources 不能替代后续全部结论的证明。

恢复分页缺陷仍在旧线上后端出现。补丁通过真实 ControlJobs/SQLite 解析器集成；本轮另将精确 task 读取中的全部 Activity 无条件初始预取取消，保留原有精确依赖读取。固定树中相应初始预取为 2,473 个文件、10,211,809 字节。该后端改动已发布，本地输入选择及实际 transport/guard 验证通过；尚未部署，不宣称线上最终字节或时延收益。

## 可直接使用的材料

- [完整结果及实际验收范围](https://github.com/awdawmip/em-research-mcp/blob/213ef8a82431e8f539051d99269aec6a0b4a6481/docs/evidence/research-flow-20261124/REPORT.md)
- [精确源码与测试提交](https://github.com/awdawmip/em-research-mcp/commit/213ef8a82431e8f539051d99269aec6a0b4a6481)
- [Codex 部署及实际接续交接入口](https://github.com/awdawmip/em-research-mcp/blob/213ef8a82431e8f539051d99269aec6a0b4a6481/docs/evidence/research-flow-20261124/CODEX_UPDATE_PROMPT.md)

上述九个 MCP 文件已逐一回读，正文和 blob 均匹配。网关 110 项相关接口测试及构建通过；恢复解析器 3 项集成测试、隔离速记本保存/修订测试，以及精确任务输入的定向检查通过。没有新增托管 CI 或研究登记。

## 接续位置

通过现有后端部署环境整合小差异并更新实际实例，再以已有会话、已有任务和固定原文确认恢复分页与任务读取。当前会话没有该运行实例的服务器部署通道，已上线网关与待部署后端分别报告。使用交接中的部署基线补丁，保留服务器已有速记本集成；不以主干整文件覆盖实际部署版本。
