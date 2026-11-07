# R587｜下轮便携接续

母问题：R462 冻结 signed BRC 原生联合十二支路的保真研究；本分支的局部目标是辅助逆谱 ν_k 的虚部正型能量 V_k 与 arcsine 极限。P000、ACTIVE 世界观及原生三维切片保持原状。

当前可复用前沿：R582 证明固定阶 arcsine 幂矩及紧复盘解析渐近；R585 将实际复测度收敛归结为 V_k→0；R586 给出有限阶 Wasserstein 证书及 V_k 数值候选 O(k^−1/2)。本轮 R587-A 将 R582 提升为同时对所有 k≥k_0、m≥1 成立的 |T_m/d−M_m|≤A m/(d r^m)，得出 m≤c log k 的 mesoscopic 收敛；R587-B 得出所有指数测试的 O(k^−1) 界；R587-C 将 R586 上界中的无限矩误差压缩为只依赖 V_k、k、N 的显示公式，并证明 V_k=O(k^−β) ⇒ W₁=O((log k)^−1/2)。

代码/证据：R587_VERIFY.py、R587_EVIDENCE.txt；120 项精确逆谱矩计算与24个 N 的两类二项式恒等式全部通过。结论级别 AUTHOR_SIDE_ANALYTIC_DERIVATION，尚无独立数学 Driver 审核。

下一可独立执行单元：对实际 Q_k 的 V_k 寻找 O(k^−1/2) 全参数上界/反例；若主根簇分析成本过高，先给出 r、A 的明确可计算有理常数以使 R587.1/R587.5 成为可逐 k 认证的证书。不要用复幂矩收敛替代正型观察者 V_k 的认证。

控制：本轮原生 session_start 返回 FAILED/OSError，tasks 查询 WAITING_RESOURCE/EVENT_COLLECTION_IO，reconcile 后仍 QUEUED；实际 Owner 未确认，Formal CLAIM 未取得。GitHub 身份 awdawmip 可写，材料限作者侧 Draft PR checkpoint；不创建或更改共享任务 Owner/Result/Review。实际 Git commit、PR、日志链接见本轮交接评论。
