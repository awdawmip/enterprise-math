# R604｜作者侧研究交接

2026-11-07，AUTHOR_SIDE_EXACT_CERTIFICATE / DRIVER_UNREVIEWED / NOT_ADMITTED。

冻结母源 R462@18783e01e3646c72b7aab3b16d3f565e83e6446f，signed BRC 十二支路；本次只研究 R590 Toeplitz–Hessenberg 辅助标量观察谱，参考 R603@41d040aff6b4c82ec29c5692046e743fc6089bd3 的 N_F(13)=N_F(14)=2。

**新结果**：对全部整数 k≥4096，N_Fk(13)=N_Fk(14)=2，13≤|z|≤14 无零点；两内根是简单非实共轭根。新增 dyadic k=2^43 移动窗口的完整计数；建立 U13<57/1000 和 U14<76/1000 的统一有理误差及每圆周65536节点的严格圆弧证书。

**复现**：运行 python3 R604_VERIFY.py；R604_EVIDENCE.txt 的终止标记是 R604_UNIFORM_K_GE_4096_TWO_CONTOURS_PASS。数学证明在 R604_PROOF.zh-CN.md。有限检查精确使用 Fraction；全参数结论来自解析不等式。作者侧结果尚未独立 Driver 审阅或正式接纳。

**下一科学单元**：从冻结 R462 联合载体识别辅助根对至原生全谱 V_k 的域、陪域、核、相位/符号/支路信息，证明在指定保真条件下的转移，或者构造辅助相同而原生能量不同的最小有限反例；随后处理剩余谱尾和 V_k=O(k^-1/2) 候选。

**原生控制现状**：2026-11-07 em_status 和 em_control_tasks 返回 BACKEND_IDENTITY_OR_VERSION_MISMATCH / operation_sent=false。GitHub 作者侧交接不等于原生 Researcher-ID/RA、活跃 Owner、CLAIM、Result 或独立 Driver 审核。恢复后按当前原生服务重新核对权限，不改冻结源。
