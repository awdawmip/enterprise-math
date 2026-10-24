# C282 — 四区域父盒的分离凹二次精确正性证书

研究时间：2026-10-24（Asia/Shanghai）。研究级别：**AUTHOR-EXACT / UNREVIEWED / NOT-ADMITTED**。本文只研究 C195/H168 79 节点正有理辅助函数，不声称是原生六维 Cell、带相位或带符号 BRC 的定理。

## 1. 冻结输入与声明

- Global Knowledge: \`awdawmip/chatgpt-global-knowledge@f93bbbdb62668c802b80406b2ee324a3aafffabf\`，其 \`P000_STARTUP.json\` 与完整 P000 blob \`770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc\` 一致。
- Enterprise Math main: \`db1621f2d71ebbcc59c03966c9c3e66b1c03a5a0\`；已读研究交付协议、Task 路由、ACTIVE 世界观和数学证据政策。
- 原始79有理节点、35个基本盒、75个固定支路下取整质量、4个活动支路沿用C281/C275冻结正有理模型；精确分子分母完整内嵌 \`C282_STANDALONE_EXACT_REPLAY.py\`。
- C281 作者级前沿：\`728abbeb2c2ab004338387547ad047cd7d24e6b2\`，同一完整父盒有 \`F>(1+1/4000)Q\`。C282为同一对象更强的独立数学估计，不增加已分类区域的数量。

记 \`I=(5,50,55,56)\`、\`J={0,...,78}\I\`、\`Q=2^128\`、\`H=2^166\`、\`A=6912*50000^2/17^2\`、\`Z=141421356237309504880/10^20\`。固定节点为递增有理数 \`U_0<...<U_78\`。定义

\[
B_j=\left\lfloor\frac{QA}{H((2-U_j^2)(3-U_j^2))^3}
\prod_{r\ne j}\frac{Z-U_r}{|U_j-U_r|}\right\rfloor>0,\quad j\in J;
\]

\[
T_j(v)=B_j\prod_{k\in I}\frac{(Z-v_k)|U_j-U_k|}{(Z-U_k)|U_j-v_k|},
\]

\[
M_k(v)=\frac{QA}{H((2-v_k^2)(3-v_k^2))^3}
\prod_{j\in J}\frac{Z-U_j}{|v_k-U_j|}
\prod_{r\in I\setminus\{k\}}\frac{Z-v_r}{|v_k-v_r|},\quad
F(v)=\sum_{j\in J}T_j(v)+\sum_{k\in I}M_k(v).
\]

父盒为

\[
P=[1/135,6/409]\times[34/49,28/39]\times[60/77,87/109]\times[19/24,41/51].
\]

**C282定理**：对父盒内所有满足原始节点间隔、严格有序 \`v_5<v_{50}<v_{55}<v_{56}\` 及分母合法性的实数点，

\[
\boxed{F(v)>\bigl(1+3/5000\bigr)2^{128}.}
\]

它覆盖已知四组父盒 \`(8,18),(13,18),(18,25),(18,34)\` 的全部合法连续点。该下界的保证裕量比C281的 \`Q/4000\` 强 \`12/5=2.4\` 倍。

## 2. 通用数学引理

对79个正支路分别记为 \`S_s(v)\`，定义含正线性分子的坐标集合：固定支路 \`N_j=I\`，活动支路 \`N_k=I\setminus{k}\`。在合法有序域 \`D=P∩{v_5<v_{50}<v_{55}<v_{56}}\` 内，

\[
C_s(v)=\log S_s(v)-\sum_{r\in N_s}\log(Z-v_r)
\]

是凸函数。固定支路的变量项为 \`-Σlog|U_j-v_r|\`；活动支路还包含 \`-3log(2-v_k²)-3log(3-v_k²)-Σ_j log|v_k-U_j|-Σ_{r≠k} log|v_k-v_r|\`。在当前无极点且符号固定的凸域，负的仿射绝对值对数为凸函数，\`-log(c-x²)\` 在本次 \`|x|<1\` 且 \`c∈{2,3}\` 时二阶导数为正，因此各项均凸。坐标区间与严格有序半空间的交是凸域，从锚点到合法目标点的线段不触碰固定极点或碰撞面。

令 \`t∈D\`、\`δ=v-t\`、\`h_r\` 为父盒上端点。由于

\[
\frac{d^2}{dx^2}\log(Z-x)=-\frac1{(Z-x)^2}
\ge-\frac1{(Z-h_r)^2},
\]

凸核切线与Taylor积分余项给出

\[
\log S_s(v)\ge \log S_s(t)+\nabla\log S_s(t)\cdot\delta
-\sum_{r\in N_s}\frac{\delta_r^2}{2(Z-h_r)^2}.
\]

利用 \`e^x≥1+x\` 并按正支路相加，严格获得

\[
F(v)\ge F_0+\sum_{r=1}^{4}\left[D_r(v_r-t_r)-C_r(v_r-t_r)^2\right],
\]

其中

\[
F_0=\sum_s S_s(t),\quad
D_r=\sum_s S_s(t)\partial_r\log S_s(t),\quad
C_r=\frac{\sum_{s:r\in N_s}S_s(t)}{2(Z-h_r)^2}>0.
\]

注意一元 \`q_r(x)=D_r(x-t_r)-C_r(x-t_r)^2\` 是**凹函数**。因此在各坐标闭区间上，最小值必可在两个端点之一取得，定义精确有理证书

\[
\boxed{L_2=F_0+\sum_{r=1}^{4}\min(q_r(l_r),q_r(h_r)).}
\]

这是一项对整个父盒（因而其合法子域）有效的下界，四个最坏端点组合不必属于原始合法有序域。保留 \`δ_r²\` 比C281用半径上界 \`ρ_r²\` 替代更紧；在同一锚点上新证书 \`L_2≥L_1\`，本例严格大于。

## 3. 有理锚点与机器可重算判据

取

\[
t=(1253/125000,\;176223/250000,\;7917/10000,\;41/51).
\]

全部79支路的 \`S_s(t)\`、四维对数梯度、二次误差系数及端点比较均使用 \`fractions.Fraction\` **精确有理运算**。自包含脚本对四组父盒的几何包含关系以及原节点邻域逐项验证。下包络的端点编号为 \`(1,1,0,1)\`，其顶点为 \`(6/409,28/39,60/77,41/51)\`；它只是包络顶点，而非真实函数的极小点断言。

决定性断言是

\[
\boxed{5000L_2>5003Q}.
\]

展示值为 \`L_2/Q≈1.0006124864663668\`；此小数**不参加**证明。归一化精确分数的SHA256为 \`2aeb7a3f14669293f6da64f149989f1299bc6cb1aab714c36533a3225830a9d3\`。

程序还使用另一套不共享对数梯度公式的四元 \`Jet282\` 前向自动微分，对原始79条乘积/商/绝对值支路重新计算 \`F(t)\` 与全部四偏导数，严格检查与解析路径完全相同。这是**作者级不同算术图交叉核对**，不是独立Driver审查或Lean形式化。

## 4. 状态、BRC边界与下一问题

- 正质量79支路身份在证书中逐一保留；复用C281已建立的正有理支路工具，状态为 \`REUSE_APPLIED\`。总质量观察器不能保留相位、端口、符号或未来操作相关残差；\`NATIVE_ATTRIBUTION_PENDING_BRC_REVALIDATION\`。
- 原生 \`em_control_tasks\` 读取被 \`CONTROL_QUOTA\` 拒绝；\`em_session_start\` 返回 \`STATIC_READONLY_SCOPE_DENIED\`、\`operation_sent=false\`。未核实实时Owner，未取得CLAIM、Source Result、Driver review、Working Truth或Foundation接纳；GitHub研究分支只是作者级持久化。
- **C283具体下一研究单元**：对C275宣称存在阈值两侧的187组外包盒逐组验证两见证间的线段留在同一个无极点、原始节点间隔内的凸连通分支；若发现失败，提交精确坏例及最小修正范围。平行核对C254第3、11盒分母奇点与符号边界。

再现：运行 \`python C282_STANDALONE_EXACT_REPLAY.py\`，预期 \`C282_CONCAVE_QUADRATIC_GLOBAL_EXACT_PASS\`。本轮实际隔离验证通过的是本会话科研包中的本地精确源码；远程程序保存后回读的状态与远程执行状态应分别核对。
