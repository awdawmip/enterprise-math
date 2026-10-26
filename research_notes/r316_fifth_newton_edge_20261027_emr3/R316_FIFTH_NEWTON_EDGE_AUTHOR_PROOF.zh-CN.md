# R316｜BRC Newton 第五条顶端系数的无界闭式与严格正性

日期：2026-10-27。作者侧代数证明及精确整数交叉验证；尚无原生 CLAIM、Source Result 或独立 Driver 数学审查。

## 1. 不可变来源、对象与边界

本轮 GLOBAL_KNOWLEDGE_V1 固定为 awdawmip/chatgpt-global-knowledge main@4d75b6c92823119d725fff4949699fe3fb0f07c2，已读取规范入口、Enterprise Math 路由、P000 与 ACTIVE 世界观、数学及 BRC 规则。P000_STARTUP 的 canonical_blob_sha1=770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc，与原始 P000 Git Blob 一致。Enterprise Math Source 固定为 main@45389c9c23ada9ea65cb2e5702f756b5c69f3ff8，已读 PORTABLE_RESEARCH_PROTOCOL 与控制权威。本证明复用 R313 多项式递推及 R314/R315 作者侧低阶矩结果，R315 不可变对象 1b6562f19ec6724d1b86bf003f126538438ca86c；但 R315 的原分支只读时仍停留在 bcb3a31c，不能称已成功绑定。

所研究的是正权、有序六边 BRC 辅助来源计数；完整效果是 (ε,k)，末状态为0的长度 n 来源数记 P_n(ε,k)，缺陷符号差 D_d(n)=P_n(+,2-n+2d)-P_n(-,2-n+2d)。保留来源次序与符号，不把它解释成已建立 P000 原生六维 Cell 的物理动力学。

R313 Newton 体系有

\[
K_s(s+1+h)=\sum_{k=0}^s a_{s,k}\binom{h}{k},
\quad a_{s,k}=\sum_{j=0}^{2s+1}[z^j]M_s(z)\binom{2s+1-j}{s-k}.
\tag{1}
\]

其中不合法二项式下标取零，M_0(z)=1，且对 s≥1，

\[
M_s(z)=n_s(z)(1-z)^s-\sum_{i=1}^{\min(s,12)}\delta_i(z)M_{s-i}(z)(1-z)^{i-1},\tag{2}
\]

\[
n_i(z)=-\binom3{i-1}z-\binom6{i-1}z^2+\binom8{i-2}z^3,\tag{3a}
\]
\[
\delta_i(z)=\bigl(-\binom4i+\binom2{i-1}\bigr)z+
\bigl(\binom5{i-1}-\binom5{i-2}\bigr)z^2+
\binom7{i-2}z^3-\binom9{i-3}z^4.\tag{3b}
\]

方法判定：BRC 完整效果及 Newton 旧接口 REUSE_APPLIED；本轮的精确 BigInt 多项式递推 REUSE_EXECUTED。不引入新物理模型或独立工具家族。

## 2. R316 定理

对所有整数 s≥4，有

\[
\boxed{a_{s,s-4}=\frac{2^s}{6144}
(625s^4-1750s^3-205s^2-5294s-2424).}\tag{4}
\]

且对全部这些 s，

\[
\boxed{a_{s,s-4}\ge \frac{55}{16}\,2^s>2^s>0,}\tag{5}
\]

第一个等号仅 s=4 成立。结合前沿，五条顶端边界 q=s-k=0,1,2,3,4 全部在各自自然定义域内严格正。余下中部并未被证明。

## 3. 第四阶多项式矩的全指标证明

令 A_s=M_s(1)、B_s=M'_s(1)、C_s=M''_s(1)、E_s=M'''_s(1)、F_s=M_s^{(4)}(1)。
精确复用先前已按式(2)证明的矩公式：

\[
A_s=2^s\ (s\ge0),\quad B_s=3(s+1)2^{s-2}\ (s\ge1),
\]
\[
C_s=2^{s-4}(9s^2+11s-26)\ (s\ge2),\quad
E_s=3\cdot2^{s-6}(9s^3+6s^2-119s+220)\ (s\ge3).\tag{6}
\]

由(3b)，在 z=1 所需数据为：
δ_1(1)=-2, δ'_1(1)=-1, δ''_1(1)=2；
δ_2(1)=1, δ'_2(1)=7, δ''_2(1)=14, δ'''_2(1)=6；
δ_3(1)=8, δ'_3(1)=24, δ''_3(1)=40；
δ_4(1)=11, δ'_4(1)=26；δ_5(1)=-6。

对于 s≥5，n_s(z)(1-z)^s 以及每个 i≥6 的乘积项在 z=1 的四阶导数为零。Leibniz 公式给出

\[
\left.\frac{d^4}{dz^4}\bigl[f(z)(1-z)^{i-1}\bigr]\right|_{z=1}
=(-1)^{i-1}\frac{4!}{(5-i)!}f^{(5-i)}(1)
\quad (1\le i\le5).
\]

因此由(2)逐项严格得到

\[
\begin{aligned}
F_s={}&2F_{s-1}+4E_{s-1}-12C_{s-1}\\
&+4E_{s-2}+84C_{s-2}+168B_{s-2}+24A_{s-2}\\
&-96C_{s-3}-576B_{s-3}-480A_{s-3}\\
&+264B_{s-4}+624A_{s-4}+144A_{s-5},\quad s\ge5.
\end{aligned}\tag{7}
\]

由(2)直接计算

\[
M_4(z)=-8z^8+29z^7-36z^6+20z^5-5z^4+25z^3-9z^2,
\quad F_4=240.
\]

把(6)代入(7)并除以 2^s，得

\[
\frac{F_s}{2^s}-\frac{F_{s-1}}{2^{s-1}}
=\frac3{64}(27s^3-54s^2-415s+1234),\quad s\ge5.\tag{8}
\]

对右端三次多项式取精确离散和、以 F_4/16=15 为基例，或对候选闭式直接验证前向差，得到全整数归纳结论

\[
\boxed{F_s=\frac{3\cdot2^s}{256}
(27s^4-18s^3-911s^2+4070s-6184),\quad s\ge4.}\tag{9}
\]

## 4. Newton 第五条系数的恢复

对式(1)令 k=s-4。将关于 j 的四次多项式
\(\binom{2s+1-j}{4}\) 用下降阶乘 \(j_{\underline r}\) 展开，其 r=0,1,2,3,4 的系数分别是

\[
\frac{s(s-1)(2s-1)(2s+1)}6,\quad
-\frac{2s(s-1)(2s-1)}3,\quad
\frac{(s-1)(2s-1)}2,\quad
-\frac{s-1}{3},\quad \frac1{24}.
\]

由于 \(\sum_j[z^j]M_s(z)j_{\underline r}=M_s^{(r)}(1)\)，得到**精确恒等式**

\[
\begin{aligned}
24 a_{s,s-4}={}&4s(s-1)(2s-1)(2s+1)A_s\\
&-16s(s-1)(2s-1)B_s\\
&+12(s-1)(2s-1)C_s-8(s-1)E_s+F_s.
\end{aligned}\tag{10}
\]

代入(6)与(9)并在有理数环内化简，恰得(4)。

设 p(s)=625s^4-1750s^3-205s^2-5294s-2424。直接计算 p(4)=21120、p'(4)=69066、p''(4)=77590、p'''(4)=49500、p''''=15000。由逐阶导数正性，所有实数 s≥4 有 p(s)≥21120，等号仅 s=4；而 21120/6144=55/16，故得到全指标严格正性(5)。无界结论来源于代数归纳，非有限计算外推。

## 5. 实际精确验证、权限和未解决问题

随附的 R316_verify_fifth_newton_edge.js 以 JavaScript BigInt 根据式(2)(3)自底向上生成 M_0,...,M_192，分别计算原始多项式导数矩、二项式系数直和和矩恢复式，交叉核对(4)(7)(9)(10)。结果 PASS：次数约束 193 项；低阶矩 766 项；四阶矩闭式 189 项；四阶递推 188 项；第五边界直和 189 项；矩恢复 189 项；正性下界 189 项。s=4: F=240,a=55；s=5: F=2256,a=718。无浮点数判号。**机器核验严格仅限 0≤s≤192**，没有本轮 Lean 形式证明或独立审查。

真实 GitHub 身份 awdawmip、仓库权限 admin。原生 em_control_tasks 返回 CONTROL_QUOTA；em_session_start 返回 STATIC_READONLY_SCOPE_DENIED，operation_sent=false。因此活跃 owner 未权威核定，未创建新 Researcher 会话、CLAIM、Source Result 或 Driver 评审；本成果仅是不占用其他任务 owner 的作者侧支持研究。P000 与 ACTIVE 世界观保持不变。

以 R313 对 s≤128 的全系数有限证书为条件，仍未解决的精确区域缩小为

\[
\boxed{s\ge129,\quad 0\le k\le s-5.}\tag{11}
\]

**下一个独立单元**：推导第五阶矩 M_s^{(5)}(1)，求 q=5 的无界闭式/正性或精确反例；之后研究 q(s) 增长区间的统一证书。全缺陷 D_d(n)>0（d≥2,n≥4d+4）以及 N_peak=81 均尚未证明。

状态：R316_AUTHOR_PROVED_Q4_ALL_S / EXACT_BIGINT_192_PASS / OWNER_UNVERIFIED / DRIVER_UNREVIEWED / NOT_ADMITTED。
