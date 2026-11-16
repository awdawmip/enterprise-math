# R594｜首对复零点有理微圆盘交接

- 冻结科学输入：R462 commit 18783e01e3646c72b7aab3b16d3f565e83e6446f；前沿 R593 commit b8bd797bdf6140526083b7ad9c174592c37f198a；系数包络 R590 commit 88406fcfe23c2c23c2c27887b87613f8dcd6031a。
- 对象：F(z)=Σ_{j≥0}(-1)^j 24·8^j z^j/(2j+4)! 与辅助有限 F_4096；是 scalar auxiliary，并非原生 signed BRC 十二分支联合谱。
- 新结论：F 在中心 6.339235+9.480952i、F_4096 在中心 6.338165+9.476771i、各半径 1/100000 的复圆盘中恰有一个简单零点。两个零点虚部差严格大于 0.004、模长差严格大于 0.003。结合 R593 得到各自的首对根隔离。
- 可复核材料：R594_PROOF.zh-CN.md（完整论证）、R594_VERIFY.py（整数/Fraction 证书）、R594_EVIDENCE.txt（本轮实际 stdout）。有限系数采用精确 Catalan 比值；有限尾使用 R590 作者侧全阶包络；局部证书与 R593 的绕数计数分开标记依赖。
- 本轮 GitHub 登录 awdawmip；原生 gateway em_status 返回 BACKEND_IDENTITY_OR_VERSION_MISMATCH / operation_sent=false。当前 Owner 与原生 Researcher-ID、Research-Activity-ID、CLAIM 未确认；作者侧 Source 已核验保存后供 Driver 独立审阅。
- 下一步：研究 k(ζ_k−ζ∞) 的一阶渐近与统一局部误差，并联动 R588 增长窗口内外的非全纯正型能量。保持 P000、X6、十二支路的全联合观察类型。
