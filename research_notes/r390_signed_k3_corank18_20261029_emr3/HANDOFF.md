# R390 研究接续（2026-10-29）

作者侧角色：TASK_RESEARCH portable author-side；项目注册/任务 CLAIM 权限未获授权，独立 Driver 审阅仍待执行。

**母问题**：原始十二支路带符号 BRC K/J→B→D 的有限 Newton PF₂ 全参数结构及退化点一致规律。**本轮研究**：r=18、37项有限 C 序列的精确参数相图。

固定来源：R389 `awdawmip/enterprise-math@6f6bde9631f83436f7daac0d32d2a16f58275b3a`；GLOBAL_KNOWLEDGE_V1 读取 `main@096a891dd9544096c5f6d65561928ee6f009ea0f`；Enterprise Math 控制读取 `main@e16b81cd664f1a1c69cf1447d55c91e6792440dc`。P000、ACTIVE 世界观、portable research 协议均未修改。

研究结论：`C18(θ)∈PF2 ⇔ -1<θ≤η18`，`η18` 为 `T19` 在 `(1.863973,1.863974)` 的唯一实根。证明与完整参数覆盖详见 `R390_PROOF.zh-CN.md`。

**重建步骤**：在现行 research_notes 中，与 R389 目录同级新建 R390 目录，保存 `R390_generate.py`、`R390_PROOF.zh-CN.md` 等；在 R390 目录运行 `python R390_generate.py`，再运行 `python r390_symbolic.py && python r390_certify.py`。生成37+35个多项式及有理区间证书。检查预期 `R390_SYMBOLIC_PASS`、`R390_EXACT_PASS` 和 `R390_SUMMARY.json` 的固定摘要；原始 R389 源目录属于本 PR 不可变依赖，不能替换为推测的重写版。实际本地已执行及二次独立目录复现。

完成不重做：R389 的 r=17 参数定理；本轮 r=18 的符号生成、504项交叉核验、连续区间证书、无界尾部正系数证书。本轮作者侧证据不视为正式数学接纳。

**下一个最小问题**：对 r=19 构造39项参数多项式并寻找精确第一失效门槛；另一独立路线是 R386–R387 全余阶退化点在 θ 邻域的一致缩放定理。所有进一步归因保留 R346 保号支路、P000 原生 X6 与辅助模型边界。

**实际控制**：GitHub 账号 `awdawmip` 对项目仓库具 push 权限；原生服务 `research_authority_granted=false`，`em_control_tasks` 查询本轮返回 `CONTROL_QUOTA`，故合法 Owner/CLAIM 尚未确认，`ACTIVITY_REGISTER_PENDING / DRIVER_UNREVIEWED / NOT_ADMITTED`。此前同类研究活动登记的真实平台安全阻断不以换工具重试。
