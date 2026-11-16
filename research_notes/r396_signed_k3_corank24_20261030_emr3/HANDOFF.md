# R396｜第24余阶 signed BRC PF₂ 精确研究交接

来源：R395 上一作者侧研究提交 97e3a456eae6f256dfe970cd0c956a32736a8f3c；R346 原始 signed K/J Git blob 1579ceb717ab1945227eca4f7a1878bf4ffa73e1。GLOBAL_KNOWLEDGE_V1 固定读取 main@1f0b8985fd6ca8804198fa97a9563db09a0f0e0d；项目固定读取 main@866cf57e4ff5cb66f7d29e155cecee61a072c5df。

已完成定理：C24(θ)∈PF₂ ⇔ −1<θ≤η24，η24 为 T25 在 (1868232/10^6,1868233/10^6) 内唯一实根；T25 在 (1881908/10^6,1881909/10^6) 内有认证的次生简单根，其附近 c25<0。θ=15/8 时 T25 恰四阶、T26 恰八阶消零，T22,T23<0。c48=1289904147324(30−16θ)^48。

可复现：在 Python 3 + sympy 环境运行 python r396_symbolic.py && python r396_certify.py；从原始 K/J→B→D 生成49项 c 和47项 T，使用 Fraction 检查672项原始数值身份，用100项证书、109个连续叶区间、112次 Bernstein 检查和6563个严格正控制系数证明全参数分类。R396_EVIDENCE.json.gz 为完整原始机器证据无损保存，R396_EVIDENCE_INDEX.md 载有 SHA256 和恢复命令。大体积多项式 JSON 由源码重建。

研究状态：AUTHOR_SIDE_EXACT / DRIVER_UNREVIEWED / NOT_ADMITTED / ACTIVITY_REGISTER_PENDING。原生服务研究授权 false，任务列表 CONTROL_QUOTA，owner 未获权威确认。没有 formal CLAIM/Result/Review 或正式 Task 状态变化；P000 与 ACTIVE 世界观不变。

下一步：第25余阶51项有限 PF₂ 分类；或证明/反驳偶数余阶退化点的 T_{r+1} 四阶与 T_{r+2} 八阶规律。不得将固定有限阶证书推广为原生 X6 的动力学结论。
