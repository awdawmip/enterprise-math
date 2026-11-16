# R596 二阶辅助根漂移｜可接续交接

科学冻结输入：R462 signed BRC @18783e01e3646c72b7aab3b16d3f565e83e6446f。复用 R590@88406fcfe23c2c23c2c27887b87613f8dcd6031a 与 R595@4cdf26b98f51abc6579da8eecd2250952369ec87。
本轮定理：F_k=F+G/k+H/k^2+O(k^-3) 在每个固定复圆盘及固定导数阶一致，G=[15DF+3(F-1)]/8，H=[(-32D^3+501D^2-349D-18)F]/384+3/64-z/16。
固定简单根 ζ 有 ζ_k=ζ+l/k+m/k^2+O(k^-3)，l=-G/F'，m=-[H+G'l+F''l²/2]/F'，均在 ζ 求值。对固定共轭根对导出正型能量 k^-5、k^-6、k^-7 三项。
证据：R596_PROOF.zh-CN.md、R596_VERIFY.py、R596_EVIDENCE.txt；101个 Fraction 二项式矩/β证书 + 340项独立 Catalan 精确重构 +40项有理残差诊断 +5组65位根漂移数值检查。
实际原生服务：em_status 返回 BACKEND_IDENTITY_OR_VERSION_MISMATCH, operation_sent=false；本轮未取得新 RA、Owner 或 CLAIM。作者侧成果已独立保全，独立 Driver 数学审阅待完成。
保留 P000 X6、signed 12支路、相位、联合关系与来源。下一问题：增长零点窗口中从局部二阶漂移推至可控谱尾能量，检验 V_k=O(k^-1/2)；另可对首对根二阶 m 做严格有理隔离。
执行：python R596_VERIFY.py。下一执行者复用同一冻结源，正式 Result/Review 仍需原生角色与当前 owner。
