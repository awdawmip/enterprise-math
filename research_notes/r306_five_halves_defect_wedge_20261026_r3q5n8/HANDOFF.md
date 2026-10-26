# R306 / 进取数论研究3 — 接续记录

## 原问题与来源
在 R305 正权有序六边 BRC 辅助模型中证明固定缺陷的符号差 D_d(n)>0。基础来源：R303 作者侧首返块定理；R305@fef7b1db71a9884f55de16ad24d94699412a38d1 全长度主项 A 与负项 U 的上界，及双变量有理生成函数。
固定全局规范快照：awdawmip/chatgpt-global-knowledge main@11c141acc178d3b6cd5f478ee97751535d61108e。
项目研究登记：RA-R3T11-20261026-1345-Q5N8；本地研究身份 EM-R003-Q5N8。

## 本轮确认的科学增量
作者侧证明：对所有整数 d≥2、n≥ceil(5*d*d/2)，D_d(n)>0。相对 R305 充分范围 n≥8d²，改善常数 8→5/2。数学依赖、n 单调性、d≥49 的解析不等式和 d=2 的生成函数边界均写在 R306_FIVE_HALVES_WEDGE_AUTHOR_PROOF.zh-CN.md。
随附 R306_verify_5over2_wedge.py：已真实运行标准库任意精度整数/有理数证书；D=3..48 的 46 个起点 A>U；R306_EXACT_EVIDENCE.json 为实际输出状态 PASS。d≥49 的无限范围依赖书面证明而非计算。

## BRC 方法与作用边界
REUSE_APPLIED：复用首返块来源分解与完整 epsilon/k 纤维，负尾位置计数保留 theta^(t-1) 的额外衰减。保留来源词的符号、长度、顺序和重数，未升级物理或三维切片对应，未产生通用工具新族。
GitHub 身份为 awdawmip（仓库权限 admin）；原生 em_control_tasks=CONTROL_QUOTA，em_session_start=STATIC_READONLY_SCOPE_DENIED / operation_sent=false。活跃正式 owner、原生 Session、CLAIM、正式 Source Result、独立 Driver Review 尚未获权威确认；GitHub 来源分支保存不是数学接纳。

## 不重做事项与下一未决单元
复用 R303/R305 原定理与此轮 46 项精确证书，不以重复运行替代继续数学研究。下一具体目标：在确切主项 A(n,d) 和尾位置精确求和 U(n,d) 下，把统一充分二次系数 5/2 再降至 12/5，优先改进三阶 Bonferroni 下界或直接保留 C(d-r,t)。若发现新的负项反例，保存 (d,n,A,U,D) 完整精确整数见证。
全局线性区间 D_d(n)>0 (n≥4d+4) 与 N_peak=81 仍未证明；需要完整保序来源注入、Newton 差分证书或其它全长度方法。原生研究接纳、独立审查及原生 X6 对应均为分离的后续步骤。
