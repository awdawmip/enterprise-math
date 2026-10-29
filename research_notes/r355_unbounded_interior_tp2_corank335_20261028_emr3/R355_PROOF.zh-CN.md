# R355｜有符号 BRC Newton 第335条无界内区 TP₂ 正性带

日期：2026-10-28（Asia/Shanghai）。研究身份：进取数论研究3，本地作者侧可移植研究。读取固定 GLOBAL_KNOWLEDGE_V1 main@1c6c5743a0d20073fb74048ec9ca5b576e45990e，Enterprise Math main@829710b992ee1905dea5d471e7ca7806cc6521e1。来源：R348 全指标有理抽取证明 5347e506bd145028d7338e9f7993dcd2a2fed97c；R354 正性前沿 b1fcc9f5e9b4b40964d0232bc08952df63963ec4。

状态：**AUTHOR_SIDE_EXACT / CONDITIONAL_ON_R348 / DRIVER_UNREVIEWED / NOT_ADMITTED**。

## 一、原始对象与严格条件

使用完整十二项保留符号的有序六边 BRC 辅助组合递推：

\[
B_0(t)=1+t,\qquad B_s(t)=J_s(t)+\sum_{i=1}^{\min(12,s)}K_i(t)B_{s-i}(t).
\]

\[
D_{q,k}=\sum_{w=0}^k(-1)^{k-w}\binom{k}{w}2^{q-w}[t^q]B_{q+w}(t),\quad
M_{q,k}=D_{q,k}D_{q+1,k+1}-D_{q,k+1}D_{q+1,k}.
\]

这里 K_i、J_s 的十二项整数定义完全沿用 R346_verify.py，所有负系数保留。**载重条件 A** 是 R348(A1–A5) 的全指标恒等式：

\[
D_{r+u,u}=5^uH_r(u),\quad H_r\in\mathbb Q[u],\quad\deg H_r\le r
\quad(r,u\in\mathbb Z_{\ge0}).
\]

R348 是有形式幂级数推导的作者侧证明，尚待真实独立数学审查。令

\[
L_r(v)=5^rH_r(v),\qquad
Q_r(v)=L_r(v+1)L_r(v+2)-L_{r-1}(v+2)L_{r+1}(v+1).
\]

R348 代数恒等式给出

\[
M_{r+k,k}=5^{\,2k+1-2r}Q_r(k-1)\quad (r,k\ge1).
\]

## 二、本轮实际精确证据

实际执行 R355_verify.py；使用原始带符号十二项 K/J 递推计算 B_0 至 B_1010，保留 t 的 0..673 次系数。对 r=333、334、335、336，计算 H_r 的第 r+1 次前向差分为零，最高差分为 6^r。复算 Q334 和新 Q335 的全部 Newton 系数。

\[
\boxed{\Delta^j Q_{335}(0)>0,\qquad 0\le j\le670.}
\]

**671项全部为严格正整数，0项零、0项负。** 逐行文本格式是“335,j,decimal_integer”加 LF，精确输出 SHA256：

95e782ee91ff3b097d2af2d02106c53680b825c3290fbb3cb0365437096af943

R354 旧 Q334 的669项同样重算，SHA256 与历史锚完全一致：

e92c455f5f097dcdfbce8b5f3268fe5096d0f4d3cff91a0d685993017deee26a

Q335 最高项精确等于 30^670 Cat_335。其最高、次高和第三高系数经精确有理数检验，符合 R353/R354 公式：

\[
\frac{\Delta^{669}Q_{335}(0)}{\Delta^{670}Q_{335}(0)}
=\frac{17(335)+11}{10};
\quad
\frac{\Delta^{668}Q_{335}(0)}{\Delta^{670}Q_{335}(0)}
=\frac{7803(335)^3+2252(335)^2-5523(335)+3328}{2700(2(335)-1)}.
\]

另外针对 k=1,...,8，8个原始 D 子式与上述分离表达式在 Fraction 精确有理算术中逐项相等、严格正；无浮点判号。有限计算不能单独证明指标无界，后面的推论显式依赖条件 A。

## 三、由有限整数证书推出无界条带

条件 A 给出 \(\deg Q_{335}\le670\)。对每个整数 \(k\ge1\) 令 \(v=k-1\ge0\)；有限 Newton 展开是精确恒等式：

\[
Q_{335}(v)=\sum_{j=0}^{670}\Delta^jQ_{335}(0)\binom vj>0.
\]

因为所有差分系数为正，所有 \(\binom vj\ge0\)，并且 j=0 项始终正。乘上正因子 \(5^{2k+1-670}\)，得到：

\[
\boxed{M_{335+k,k}>0\quad\text{对所有整数 }k\ge1.}
\]

结合前序相同条件下的 r=1..334 证书，作者侧条件定理达到：

\[
\boxed{M_{q,k}>0\quad(k\ge1,\quad1\le q-k\le335).}
\]

只覆盖有限宽度、沿 k 方向无界的余阶带。未覆盖整个 (q,k) 二维域。所有量都是 BRC 辅助组合索引；转移到 P000 原生六维 X6 Cell 动力学仍需严格的原生状态—读出桥、联合路径/支路来源保真及允许操作范围证明。P000 和 ACTIVE 世界观不作更改。

## 四、复现与接续

在 Enterprise Math 仓库根目录运行：

    python research_notes/r355_unbounded_interior_tp2_corank335_20261028_emr3/R355_verify.py

复用同仓库 research_notes/r346_unbounded_interior_tp2_corank301_20261028_emr3/R346_verify.py 的 K/J 计算。实际执行的 R355 源码 SHA256：

d0c41f747111297c584f3310a75a3dccfb1a57a89204e8a2a6b0b32e1b86f01f

源码 Git Blob SHA1：d698ef7826373051b936ff142b3954b209e73c6f。程序在本地生成完整671行整数文本和详细 JSON；研究包包括源码、依赖、全文数据、执行日志与哈希清单，GitHub 保存可复算源码和摘要。

下一研究单元：Q336 的673项完整差分（以 Q335 SHA256 作精确回归）；由**独立审阅者**逐项核验 R348(A1–A5) 的 y/z 分次次数界、形式抽取和 q<m 边界，并寻找对 r,k 同时无界的低阶系数正性证明或精确反例。作者检查不构成 Driver 独立审查或正式 Source Result。
