# R319 科学接续｜BRC 第八条 Newton 顶端系数

任务母题：正权、有序六边 BRC 辅助来源计数的完整 Newton 系数正性；不能把附属计数自动升格为原生 X6 物理动力学。

固定全局读快照：awdawmip/chatgpt-global-knowledge main@5d15b2e7279bd8a5050b80eea87dd2afa007a7e5；P000 原件（GLOBAL V4）Git blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc，与 P000_STARTUP 投影一致；ACTIVE 世界观只读。EM 协议快照：awdawmip/enterprise-math main@0530a38e2bd6d9fbecd5f5cf1f76993442ceec64，docs/PORTABLE_RESEARCH_PROTOCOL.md。既有上游 R318@9566afa9519f4998f9166d6f4f2f36eba812a264。

已完成的独立作者侧科学增量（不需要重做）：七阶矩 m7(s)=9·2^s/16384·(243s^7-2268s^6-38052s^5+780850s^4-5472663s^3+16271178s²-1634008s-78016960)，对全部整数 s≥7 以原始多项式递推的导数关系归纳证明。经 Newton 下降阶乘矩恢复，精确得

a_(s,s-7) = 2^s/16515072·(15625s^7-175000s^6+910000s^5-3151750s^4+2148895s³+1397438s²+28570632s+24865344) ≥ 8035/128·2^s >0（s≥7），边界等号 s=7。

全部符号多项式差分和 u=s-7 移位正系数证书见完整 R319 证明。Node.js BigInt 原始递推对 s=0..192 实执行：全部 PASS；m7、q7、恢复式、移位、下界各 186 项（差分 185 项）。样本 a_(7,0)=8035、a_(8,1)=81306。代码与 JSON 证据置同目录。有限计算不是无限范围证明，后者来自显式代数归纳。

实际 GitHub 身份：awdawmip，EM 仓库 admin/push；原生 em_status=0.6.11，em_control_tasks=CONTROL_QUOTA，em_session_start=STATIC_READONLY_SCOPE_DENIED、operation_sent=false。无活跃 owner 权威确认，无原生 session/CLAIM/Result 和独立 Driver 数学接纳；本结果仅为作者侧证明与研究持久化，正式记录状态须以独立 Source 控制回执判定。P000/ACTIVE 未变。方法复用：R313 BRC 来源纤维与 Newton 接口，实际精确整数递推。

继承 R313 的 s≤128 全系数有限证书（仅限其原验证范围），未覆盖区域缩至 s≥129、0≤k≤s-8。下一单元：计算八阶矩 m8(s)，证明或精确证伪第九条顶端系数 a_(s,s-8)>0（s≥8）。按原始 δ_i 多项式推导 m8(s)-2m8(s-1)，以 (1-z)^{i-1} 截断 i≤9，使用旧 m0..m7，恢复 Newton q8 并尝试 u=s-8 移位多项式正系数。若该正系数法失败，应找反例或不同正性基，不得以有限测试代替证明。更远的 D_d(n)>0（d≥2、n≥4d+4）与 N_peak=81 仍开放。