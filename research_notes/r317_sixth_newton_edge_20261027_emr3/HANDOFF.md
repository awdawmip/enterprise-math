# R317 可接续研究记录

本轮完成：BRC/R313 整系数多项式 M_s(z) 的五阶矩无界闭式及第六条顶端 Newton 系数 q=5 的严格正性。来源、每条推导及边界在同目录 R317_ALL_S_SIXTH_NEWTON_AUTHOR_PROOF.zh-CN.md；验证函数原文见 R317_verify_sixth_newton_edge.js，执行证据见 R317_EXACT_EVIDENCE.json。

固定 GLOBAL_KNOWLEDGE_V1：main@70ca1279355440ae6e502b1b5635f5a5770c74e2；EM Source：main@9fa25611d16366078a8e8ec2f2ba61f5642897d3；已重用 R316 不可变作者侧证明 38341f858423e2612297c06c8e4997a1d4f44f03。完整有序六边来源、符号与重数，模型不是已验证的 P000 物理实现。

精确结论：所有 s≥5，a_(s,s-5)=2^s*(625s^5-3125s^4+4425s^3-14275s^2-9250s+18192)/24576 ≥ (219/32)*2^s >0。该式来自五阶导数递推的代数归纳与下降阶乘恒等式；s≤192 的 BigInt 测试只是交叉验证。

控制边界：GitHub 授权身份 awdawmip/admin。原生 control_tasks=CONTROL_QUOTA，session_start=STATIC_READONLY_SCOPE_DENIED / operation_sent=false，故 Owner 未权威核对、无新 CLAIM/Result/Driver，不能作数学接纳。活动登记如另有独立回执才确认；文件分支持久化与活动登记不同。

下一问题：先用相同公式求 M_s^(6)(1) 并推导第七条顶端系数 q=6；更有价值的中期路线是证明 s≥129、0≤k≤s-6 的统一正性或找反例。未证 D_d(n)>0 对全部 n≥4d+4，亦未证 N_peak=81。无需重做 R317 已完成推导。
