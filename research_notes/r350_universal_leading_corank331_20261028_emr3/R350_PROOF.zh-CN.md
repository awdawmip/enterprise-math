# R350 — 有符号 BRC Newton 最高差分无界闭式与 r=331 精确证书

日期：2026-10-28。AUTHOR_SIDE_PROOF / EXACT_COMPUTATION / DRIVER_UNREVIEWED / NOT_ADMITTED。
全局知识固定快照 awdawmip/chatgpt-global-knowledge@a0258d9d96fb9e336a3346482afd4d476c18c771；项目控制快照 awdawmip/enterprise-math@80f5d43a2d1266bbc3f3f163d46f9f6dc6ffbc71。载重依赖：R348 的形式幂级数抽取及次数界 (A1)–(A5)，Draft PR #1599、commit 5347e506bd145028d7338e9f7993dcd2a2fed97c；r<=330 已完成证书见 R349 的 Draft PR #1592、commit 49d33127410533545c0d5d0aad65523bca411350。

研究对象为原始十二项**保留负号**的有序六边 BRC 辅助组合递推，而非 P000 原生 X6 Cell 动力学；没有六维原生嵌入、三维切片读出或路径动力学对应定理。令

\[
B_0(t)=1+t,\quad B_s=J_s+\sum_{i=1}^{\min(12,s)}K_iB_{s-i},\quad
D_{q,k}=\sum_{w=0}^k(-1)^{k-w}\binom{k}{w}2^{q-w}[t^q]B_{q+w}.
\]
R348 所得（仍需独立数学审阅）的恒等式为：对所有整数 \(r,u\ge0\)，
\(D_{r+u,u}=5^uH_r(u)\)，\(H_r\in\mathbb Q[u]\)，\(\deg H_r\le r\)。

## 定理一：全指标最高 H Newton 差分

**在 R348 (A1)–(A5) 成立条件下，对所有 r>=0，**
\[
\boxed{\deg H_r=r,\quad [u^r]H_r=\frac{6^r}{r!},\quad
\Delta^rH_r(0)=6^r.}
\]

**完整证明。** 沿用 R348 的记号
\(K(x,t)=\sum_{i=1}^{12}K_i(t)x^i,\ U=A/(1-K),\ y=1-2x,\ t=yz\)，
\(\mathcal P=yU((1-y)/2,yz)=\mathcal N/\mathcal E\)，
\(\mathcal E=\sum_{j\ge0}E_j(z)y^j\)，
\(\mathcal P=\sum_{j\ge0}G_j(z)y^j\)，
\(G_j(z)=g_j(z)/(1-5z/4)^{j+1}\)。
R348 已证明 \(g_0=1\)，\(\deg g_j\le2j\)，且
\[
g_r=N_rE_0^r-\sum_{j=1}^r E_jg_{r-j}E_0^{j-1},
\qquad E_0=1-\tfrac54z. \tag{1}
\]

**本轮新增的准确原始 K/J 低阶抽取：**
\[
K^{(0)}(x)=2x,\quad K^{(1)}(x)=3x-x^2,\quad K^{(2)}(x)=4x^2-8x^3.
\]
这来自原始带符号的十二项 K 定义，不是拟合。令 \(x=(1-y)/2\)，则
\([y^1]K^{(1)}((1-y)/2)=-1\)，且 \(K^{(2)}(1/2)=0\)。
由 \(\mathcal E=1-\sum_{a\ge1}y^{a-1}z^a K^{(a)}((1-y)/2)\) 得
\[
\boxed{E_1(z)=-z[y^1]K^{(1)}((1-y)/2)-z^2K^{(2)}(1/2)=z.}\tag{2}
\]
在 \(z_0=4/5\) 处 \(E_0(z_0)=0\)。将 (1) 逐项代入，r>=1 时首项含 E0^r 消失、j>=2 项含 E0^{j-1} 消失，只有 j=1 保留，故
\(g_r(4/5)=-E_1(4/5)g_{r-1}(4/5)=-(4/5)g_{r-1}(4/5)\)。
由 \(g_0=1\) 归纳得
\[
\boxed{g_j(4/5)=(-4/5)^j\quad\text{对所有 }j\ge0.}\tag{3}
\]

R348 的 (A5) 给出具有明确全指标次数界的有限式
\[
H_r(u)=\sum_{j=0}^r\sum_{m=0}^{2j}g_{j,m}5^{r-m}4^m
 \binom{r+u-m+j}{j}\binom{2(r+u)-j}{r-j},
\quad g_j(z)=\sum_{m=0}^{2j}g_{j,m}z^m.
\]
对固定 j,m，两个二项多项式的最高 u 系数分别为
\(1/j!\) 与 \(2^{r-j}/(r-j)!\)。因此
\[
\begin{aligned}
[u^r]H_r
 &=\sum_{j=0}^r\frac{5^r2^{r-j}}{j!(r-j)!}g_j(4/5)\\
 &=\frac{5^r}{r!}\sum_{j=0}^r\binom rj2^{r-j}(-4/5)^j
 =\frac{5^r}{r!}(2-4/5)^r=\frac{6^r}{r!}.
\end{aligned}
\]
该系数非零，结合次数上界 \(\deg H_r\le r\) 得精确次数 r。
r 次前向差分等于 r! 倍最高项系数，故 \(\Delta^rH_r(0)=6^r\)；
r=0 同样成立。证毕。

## 定理二：全部余阶的 Catalan 顶差分

令 \(L_r(v)=5^rH_r(v)\)；对 \(r\ge1\) 令
\(Q_r(v)=L_r(v+1)L_r(v+2)-L_{r-1}(v+2)L_{r+1}(v+1)\)。
**在同一 R348 载重前提下，对全部 r>=1，**
\[
\boxed{\deg Q_r=2r,\quad
\Delta^{2r}Q_r(0)=30^{2r}\frac{1}{r+1}\binom{2r}{r}>0.}
\]
证明：定理一给出 \([v^r]L_r=30^r/r!\)，自变量平移不改变最高项。
两项乘积的 \(v^{2r}\) 系数分别为
\(30^{2r}/(r!)^2\)、\(30^{2r}/((r-1)!(r+1)!)\)；
其差为 \(30^{2r}/((r!)^2(r+1))\)，严格为正。乘以 (2r)!
即是最高前向差分并等于 \(30^{2r}\mathrm{Cat}_r\)。证毕。

这把此前每个 r 有限核对的 Catalan 最高差分恒等式提升为**作者侧无界定理**，但不控制其它 2r 个 Newton 系数，故不能据此推出全二维 TP₂ 或原生物理效应。

## 新精确计算：余阶331

复用 R346_verify.py 中完整原始 K/J（包含所有负项），重新计算 B0..B998 和全部所需的 t^0..t^665，直接构造 H329..H332 的每行 r+2 个原始 D 值；额外 r+1 阶差分为0，最高 r 阶差分精确为 \(6^r\)。
R349 的 Q330 全661项规范字节 SHA256 回归一致：
7c319fc417fce95229b11341427f7de5271da80627c885a7252ee58a362c3d56。

本轮**新** r=331 的 Q331 共663项完整 Newton 差分全部严格正（0零项、0负项），其规范逐行 r,i,decimal_integer 换行 SHA256：
65eb081346caaa5a373437169ec27bf419537cdd69af14601017e197c2283356。
Catalan 最高项核对精确相符，最小系数在 i=0。另检查 k=1..6 六个直接原始 D 行列式，全部严格正且与 \(5^{2k+1-2r}Q_r(k-1)\) Fraction 精确一致。全程使用任意精度整数与 Fraction，不用浮点判号。完整663行可由随附实际执行程序 R350_verify.py 生成；原始执行日志和全量证书另保存在本轮交付附件。

因 \(Q_{331}\) 次数为662，全部663个 Newton 系数严格正，故当且仅在上述 R348 抽取前提下可推出 \(M_{331+k,k}>0\) 对每个整数 \(k\ge1\) 成立。合并 R349 已验证范围，作者侧条件无界差分带达 **331 条**：\(1\le q-k\le331,\ k\ge1\)。这不是双指标全域正性证明。

## 权限与下一问题

工具复用：T0_BRC、原有 R346 signed K/J 与有限差分接口；RESULT_ONLY / REUSE_EXECUTED（本地实际执行）。研究活动 RA-EMR3-20261028-R348-0718-D61C8A7B，真实身份仅为本轮 local-emr3-20261028-0718-D61C8A7B；GitHub 登记不授 CLAIM/Driver 权限。
原生 em_control_tasks 本轮返回 CONTROL_QUOTA；活跃 Owner 未获权威确认。R348 与本轮证明均尚未得到独立 Driver 数学审阅或 Source 正式接纳。P000 与 ACTIVE 世界观未变。

后继：独立检查 R348 (A1)–(A5) 的形式换元、次数和 q<m 边界以及本轮 g(4/5) 递推；精确计算第332余阶完整665个 Newton 差分；优先构造 R349 带符号乘积核中的抵消正性机制/反例以覆盖 r、k 同时增长。
