# R314 接续记录 — Newton 全 s 顶端三条精确公式

日期：2026-10-26。研究活动 RA-EMR3-20261026-R314-TOP3-2229；本对话自行分配 session=local-emr3-20261026-r314-top3-2229，不是原生 MCP 签发身份。GitHub 当前登录 awdawmip；未获取真实研究 Owner/CLAIM。

冻结全局来源 main@0dec749285c0aa4befb49b4d72a846d6ab3f2f78，项目来源 main@b622bf7e0c6164a53d621cb96faa2fdce2533821，R313 源不可变提交 d0fa19e7adf80a1ae67bd55583ef7c9fb2d31773。

本轮完成：由 R313 多项式递推求 M_s 在 z=1 的0、1、2阶导数，严格推出所有 s≥0 的 a_{s,s}=2^s、所有 s≥1 的 a_{s,s-1}=2^{s-2}(5s+1)、所有 s≥2 的 a_{s,s-2}=2^{s-5}(25s²-5s-26)。实际执行 BigInt s=0..128 的384边界系数与384导数矩核对通过。不能把本轮结果说成所有 0≤k≤s 的正性证明。

本目录的证明全文、可执行脚本和实际输出证据在同一研究 Git 提交中。状态为作者侧、Branch Source，未经 Source Task CLAIM/Result 或独立 Driver 接纳。P000、世界观不变。原生控制 dispatch/tasks CONTROL_QUOTA，session_start STATIC_READONLY_SCOPE_DENIED (operation_sent=false)，并非 Github 研究物料保存失败。

下一独立研究单元：固定 q≥3 时，a_{s,s-q} 能否从 M_s 的 q 阶 z=1 导数导出非负闭式，继而解决 q 随 s 增长的中间带？准确待覆盖区域是 s≥129 且 k≤s-3。优先验证解析式与完整六边来源，而不是重做 R313 的前129条全部对角检查。
