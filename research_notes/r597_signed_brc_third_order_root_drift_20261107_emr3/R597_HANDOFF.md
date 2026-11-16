# R597｜三阶根漂移研究接续

研究源冻结：R462 signed 12-branch BRC @ 18783e01e3646c72b7aab3b16d3f565e83e6446f。参考 R590 @ 88406fcfe23c2c23c2c27887b87613f8dcd6031a 和 R596 @ 86ce557a824be0d598827a549fcd5dae5a14c8ed。

完成：在固定复圆盘、任意固定导数阶，F_k=F+G/k+H/k²+J/k³+O(k⁻⁴)，新 J=[(−160D⁴+359D³−1814D²+1159D+36)F]/1024−9/256−7z/64−z²/128。固定简单零点 ζ_k=ζ+ℓ/k+m/k²+n/k³+O(k⁻⁴)，n=−[J+H'ℓ+G'm+G''ℓ²/2+F''ℓm+F'''ℓ³/6]/F'；固定共轭根对的 V_k 贡献已有 k⁻⁸ 项。

在证明 R597_PROOF.zh-CN.md 中给出全部量词和余项证明；R597_VERIFY.py 由 Fraction 重建 121 项三阶形式系数及 418 项独立原始 Catalan 系数，附带 70 位 mpmath 数值诊断；实际 stdout R597_EVIDENCE.txt 已生成。运行：python R597_VERIFY.py。

状态：AUTHOR_SIDE_ANALYTIC_PROOF / FINITE_EXACT_CHECKED / NUMERIC_DIAGNOSTIC / DRIVER_UNREVIEWED / NOT_ADMITTED。原生 gateway 返回 BACKEND_IDENTITY_OR_VERSION_MISMATCH, operation_sent=false；本轮未取得新 Native Researcher-ID/RA/Owner/CLAIM。项目 owner/claim 不被 GitHub 写入替代。

下一条独立单元：为首对零点的三阶 n 建立有理复平面隔离证书；或从固定根推进到增长零点窗口，控制 F' 与根间距，再联系全谱 V_k=O(k⁻¹ᐟ²) 候选。保持辅助标量观察者与 P000/X6 原生 signed BRC 联合状态之间的类型差异。