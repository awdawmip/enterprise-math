# R309 — 进取数论研究3，研究接续与回执

Date: 2026-10-26 (Asia/Shanghai)
Research-Activity-ID: `RA-EMR3-20261026-R309-12OVER5`
Researcher-ID: `EM-DIRECT-R309-EMR3-20261026`（本轮本地标识，不是 MCP Source 签发身份）
Identity: GitHub `awdawmip`；Enterprise Math repository permission `admin`。

## 输入冻结与接续
- GLOBAL_KNOWLEDGE_V1: `awdawmip/chatgpt-global-knowledge main@b1c6f9e87fc51617f9b75e37235682850b279b20`；入口、P000 V4、ACTIVE 世界观和项目/数学/BRC 规则已从该快照读取。
- Enterprise Math portable research / control: `awdawmip/enterprise-math main@746af7de62532857cbe85857e340a3d582015c76`。
- 上游 R303（首返块）；R305 `fef7b1db71a9884f55de16ad24d94699412a38d1`（A/U 与有理生成函数）；R306-5/2 来源分支 `research/r306-five-halves-defect-wedge-20261026-r3q5n8`。
- 并行信息：R306 线性条带已覆盖 `2<=d<=200` 的无限 n，R307 Newton 已覆盖 `2<=d<=400` 的无限 n；本轮专门处理所有 d 的统一二次楔形，不重复这两个有限参数结论。

## 已完成的新增数学
`D_d(n)=P_n(+,2-n+2d)-P_n(-,2-n+2d)` 是六边正权、有序 BRC 模型的完整仿射效果符号差。严格证明：
```
forall integer d>=2, n>=ceil(12*d*d/5): D_d(n)>0
```
比先前统一充分阈值 `ceil(5d*d/2)` 更强，始终保留来源顺序、尾符号和计数重数。

证明采取三段：
1. `d=2`：生成函数给出 `D_2(n)=n-9`（n>=9）。
2. `3<=d<=298`：用精确 majorant `A>U` 在 `n0(d)=ceil(12d*d/5)` 的296个起点逐一通过。 `A/binom(n,d-2)` 随 n 增、`U/binom(n,d-2)` 不增，故已验证每个 d 的全部无上界长度，而非有限长度窗口。
3. `d>=299`：五阶 Bonferroni 精确有理证书 `g_297(17/20)=1426166179906813/3353353344000000>17/40`；尾部负项 `U/B<=4d^2/(4d-3)`；最终差的通分分子 `16d^3-832d^2+85d+510>0`。

验证程序 `R309_verify_12over5_wedge.js` 是**同一次真实执行所用函数的完整源码**，且通过 GitHub 写入后的内容一致性回读。原始机器汇总 `R309_EXACT_EVIDENCE.json` 记录 296/296 PASS，最小 A−U=21（d=3,n=22），最小 A/U 位于 d=30,n=2160。

## 项目交付
本轮持久化的非典范研究来源（同一研究分支 `research/r309-12over5-defect-wedge-20261026-emr3`）：
- `R309_TWELVE_FIFTHS_WEDGE_AUTHOR_PROOF.zh-CN.md` — 完整中文证明；
- `R309_verify_12over5_wedge.js` — 可执行精确证书；
- `R309_EXACT_EVIDENCE.json` — 实际机器输出；
- `HANDOFF.md` — 本接续材料。
所有来源以最终不可变 Git commit 回读为准；此文字本身不构成已完成的回读回执。

## 真实权威、用途与剩余问题
GitHub 写入权限确认；原生 `em_control_tasks` 实际失败 `CONTROL_QUOTA`，原生 `em_session_start` 实际失败 `STATIC_READONLY_SCOPE_DENIED` / `operation_sent=false`。因此无法权威确认活跃 owner、正式 CLAIM、原生研究会话、独立 Driver review 或数学接纳。活动登记仅是 GitHub 追溯事实，不是任务所有权。P000、ACTIVE 世界观均未更改。

模型仅为正权有序 BRC 辅助来源计数；未建立与原生 X6 Cell、三维切片、物理相位、时间或 Shor 效果的映射，不能据此宣称相关物理结论。

下一独立问题：更锐利估计 `A/U` 以尝试全缺陷阈值 `ceil(47*d*d/20)`（须防止粗上界失效），或证明 R307 中 `K_s(d)=Delta^(d-1-s)P_d(4d+4)>0` 对所有 `0<=s<=d-1` 的统一证书；候选 `N_peak=81` 仍需要独立的中央28效果全长比较。
