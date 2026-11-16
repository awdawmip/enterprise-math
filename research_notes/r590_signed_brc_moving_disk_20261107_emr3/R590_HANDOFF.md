# R590｜接续交接

**母问题及冻结来源**：R462 signed BRC 十二支路结构保真；冻结输入 `18783e01e3646c72b7aab3b16d3f565e83e6446f`。当前作者侧辅助谱直接前沿 R589 @ `45a5ec929e418eb80ce7ccf44fd19896275a14bd`。

**本轮定理**：对每一固定 0<c<1/8，`sup_{|z|<=c(log k)^2}|F_k-F|=O_c(k^(-1+sqrt(8c))*log k)->0`；得到全部有限系数的精确乘积表示和全阶包络 `a_(k,j)<=e^3(k+1)(2k+1)a_j`。移动圆周的最小模 m_k 若大于该逼近误差，即以 Rouché 获得等数零点。

**可复算材料**：R590_PROOF.zh-CN.md 为完整解析证明；R590_VERIFY.py 使用整数/Fraction 对 2160 对系数、2160 对全阶包络及 270 对低阶误差界执行核对；实际运行输出 R590_EVIDENCE.txt。

**下一问题**：为 r_k≈c(log k)^2 建立 F 的移动圆周严格最小模下界，形成无条件移动零点计数；再联系 R588 能量逃逸与 V_k=O(k^(-1/2)) 候选。仍保持辅助标量观察与原生十二支路差别。

**控制状态**：原生 gateway 此轮返回 BACKEND_IDENTITY_OR_VERSION_MISMATCH / operation_sent=false，未取得新的 session/Owner/CLAIM；成果为作者侧 Draft PR，数学 Driver 独立审阅待完成。
