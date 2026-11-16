# R595｜固定复根的一阶漂移接续

- 冻结研究输入：signed BRC R462@18783e01e3646c72b7aab3b16d3f565e83e6446f；前沿 R594@9596ca2b3f06b5198a978adcd325d98e0641560b；精确系数 R590@88406fcfe23c2c23c2c27887b87613f8dcd6031a。
- 结果：对辅助 Toeplitz–Hessenberg 标量谱，F_k=F+G/k+O_M(k^-2) 在每个固定复圆盘及任意固定导数阶一致，G=(15zF'+3(F−1))/8。每个极限根 ζ 的有限根满足 ζ_k=ζ+ℓ/k+O(k^-2)，ℓ=−15ζ/8+3/(8F'(ζ))。固定非实共轭根对对 V_k 有 k^-5、k^-6 两项解析系数。
- 证据：R595_PROOF.zh-CN.md、R595_VERIFY.py、R595_EVIDENCE.txt；精确有限核对为 101 项二项式矩和 340 项 Catalan 系数；数值根诊断为普通 IEEE-754 双精度，严格隔离仍以 R594 为依据。
- 原生 gateway 读取返回 BACKEND_IDENTITY_OR_VERSION_MISMATCH、operation_sent=false；本轮未取得新的原生 session/RA/Owner/CLAIM。GitHub PR #1708 作者侧存储只提供研究材料保全；数学 Driver 审阅待完成。
- 下一动作：推导二阶函数 H 并审核根的二阶漂移，随后连接 R588 增长窗口与全谱正型能量 V_k。原生 P000/X6 与 signed BRC 十二分支联合状态保持独立。
