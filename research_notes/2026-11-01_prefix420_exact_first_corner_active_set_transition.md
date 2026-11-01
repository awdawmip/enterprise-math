# PREFIX-420｜五 Port 联合误差模型的首次固定角点活跃集切换

2026-11-01 · 进取数论研究6 · 作者侧解析证明、精确有理区间检查和独立原始矩阵复核。数学状态：AUTHOR_VERIFIED；原生 Result、独立 Review、Admission 均未取得。

## 1. 研究对象与来源

沿 PREFIX-419 已经证明的全局来源优化继续向更大联合观测误差半径 η 推进。固定先前的科学输入 pin `f42f2906d77f24085c123f3ccfe9667d41caa96d`，主要前沿为 `research_notes/2026-11-01_prefix419_full_source_global_optimality.md@ec59dcda9a146df692e3ed540d89336035eb1322`；本轮行为规范使用 GLOBAL_KNOWLEDGE_V1 `main@d63e70daeafb077bdd91e2cc837104b97e43c689`，EM 控制读取 `main@24eb5e125a7bf52366cc49f1ed2594c0cd6d5b14`。P000、ACTIVE 心跳世界/X6、联合观察保真约束保持不变。

原始五 Port 复矩阵各行为

\[
(4,4,0),\;(0,-4,4),\;(-5+3i,0,-3+i),\;
(-2-2i,4+4i,2+2i),\;(-2,0,5+2i).
\]

将前三 Port 相干输出规范化为 (1,u,v) 后，可从矩阵唯一反演来源，后两 Port 为

\[
z_4=(5+9i)/2+(3+7i)u/2+4iv,\qquad
z_5=(22+15i)(1+u)/8+(5+9i)v/4.
\]

令 \(\beta=10^{-6}\)，\(0\le\varepsilon\le\beta\)，
\(187/100000\le\eta\le1/500\)，允许的联合测量是

\[
\big||u|^2-1\big|\le\varepsilon,\quad
\big||1+u|^2-2\big|\le\varepsilon,\quad
|v|^2\le\beta,\quad
\big||1+v|^2-1\big|\le\eta,\quad
\big||z_5|^2-709/32\big|\le\eta.
\]

研究第五项条件与第四 Port 目标 \(|z_4|^2\) 的共同相干来源。以下固定两个双基准观测角点 \(u_+=i\sqrt{1-\varepsilon}\) 与 \(u_-=-i\sqrt{1+\varepsilon}\)，分别严格优化所有合法 v；当 \(\varepsilon=0\)，这两个 u 即为全部合法来源，所述分支优化也是全来源优化。对 \(\varepsilon>0\) 的其余 u 仍需进一步分析。

## 2. 精确首个活跃集切换定理

在负相位角点 \(u_-=-iw\)，\(w=\sqrt{1+\varepsilon}\)，定义

\[
P=(245-123w)/16,\;Q=(-123-245w)/16,\;
c=709\varepsilon/64,\;E=53/8,
\]
\[
A=36-12w,\;B=-20-28w,\;
J=(53+29(1+\varepsilon))/2+4w.
\]

对 \(v=x+iy,t=x^2+y^2\)，记联合观察

\[
h=|1+v|^2-1=2x+t,\qquad
k=|z_5|^2-709/32=c+Px+Qy+Et,
\]
\[
I_4=|z_4|^2=J+Ax+By+16t.
\]

定义 \(a=P/2-1\)、\(b=(P/2-E)\beta-c\)，以及代数函数

\[
F_\varepsilon(\eta)=
\frac{(\eta+\beta)^2}{4}
+\frac{(a\eta+b)^2}{Q^2}-\beta.
\]

**定理 420-A**：每个 \(0\le\varepsilon\le10^{-6}\) 的 \(F_\varepsilon\) 在
\((187/100000,1/500)\) 中恰有一个根 \(\eta_c(\varepsilon)\)，而且 \(\eta_c\) 随 \(\varepsilon\) 严格递增。在完整上述参数矩形内，固定负相位角点的第四 Port 强度有唯一全局最小来源，且依次遵循以下活跃集：

(1) 若 \(\eta<\eta_c(\varepsilon)\)，唯一最优满足 \(h=k=-\eta\) 且 \(0<t<\beta\)。它由

\[
x=-(\eta+t)/2,\quad
y=\frac{a\eta-c+(P/2-E)t}{Q},\quad
t=x^2+y^2
\]

在 \(0<t<\beta\) 中唯一确定。

(2) 若 \(\eta>\eta_c(\varepsilon)\)，唯一最优满足 \(k=-\eta\)、\(t=\beta\)，且 \(h>-\eta\)。设 \(K=-\eta-c-E\beta,\ N=P^2+Q^2,\ S=\sqrt{N\beta-K^2}\)，则

\[
\boxed{(x,y)=\frac{K(P,Q)+S(Q,-P)}{N}}.
\]

(3) 等号 \(\eta=\eta_c(\varepsilon)\) 时两个表示一致，并同时达到 \(h=k=-\eta,\ t=\beta\)。固定角点最优值是连续、分段解析函数，右导数与左导数之差大于 \(11/4\)；此处是真实的活跃集改变。

**定理 420-B**：相同参数范围，固定正相位角点 \(u_+=i\sqrt{1-\varepsilon}\) 的第四 Port 全局最大值仍由唯一来源达到，其活跃集始终为 \(k=+\eta,\ t=\beta\)，并且 \(-\eta<h<\eta\)。

在无双基准噪声时，\(\varepsilon=0,\ P=61/8,\ Q=-23,\ c=0\)，精确消元得到

\[
\boxed{35881\eta^2+63662\beta\eta+35881\beta^2-135424\beta=0},
\quad \beta=10^{-6},
\]
\[
\boxed{\eta_c(0)=\frac{1840\sqrt{1435239919}-31831}{35881\cdot10^6}}.
\]

严格有理根隔离为

\[
\frac{1941856698303}{10^{15}}<\eta_c(0)<
\frac{1941856698304}{10^{15}},
\]
\[
\frac{1942078678057}{10^{15}}<\eta_c(10^{-6})<
\frac{1942078678058}{10^{15}}.
\]

## 3. 下段：全来源 v 的唯一最小性

对于固定的负角点 u，设
\(\mu=B/Q,\ \lambda=(A-\mu P)/2,\ d=16-\lambda-E\mu\)。
由原矩阵可精确消去 x,y：

\[
I_4=J-\mu c+\lambda h+\mu k+d\,t.
\]

在完整参数范围直接界定 \(\lambda>3,\mu>2,-3<d<0\)。固定 \(h=k=-\eta\)，相应 \(x(t),y(t)\) 给出 \(g(t)=x(t)^2+y(t)^2\)。在 \(\eta\in[L,\eta_c]\) 上 \(g(0)>0,\ g(\beta)\le\beta,\ |g'(t)|<3/1000\)（\(0\le t\le\beta\)），故 \(t=g(t)\) 有且只有一个 \(0<t\le\beta\) 的解；在临界点以外严格 \(t<\beta\)。

以此为 \(v_*\)，对任一其它可行 v 令 \(\Delta h=h+\eta\ge0,\Delta k=k+\eta\ge0\)。由精确仿射来源反演

\[
(x,y)=\left(h/2,\frac{k-c-Ph/2}{Q}\right)+
t\left(-1/2,\frac{P/2-E}{Q}\right),
\]

每个相关向量范数有上界 \(3/5,1/22,3/5\)，并且 \(|v|,|v_*|\le10^{-3}\)。故

\[
|\Delta t|\le
\frac{(3/2500)\Delta h+(1/11000)\Delta k}{1-3/2500}.
\]

代回 I4 得到

\[
I_4(v)-I_4(v_*)\ge
\left(\lambda-\frac{9/2500}{1-3/2500}\right)\Delta h+
\left(\mu-\frac{3/11000}{1-3/2500}\right)\Delta k.
\]

右侧两个系数严格为正。等号则 \(\Delta h=\Delta k=\Delta t=0\)，恢复 \(v=v_*\)。下段在连续可行 v 全域唯一最优。

## 4. 上段：带有平方剩余项的全局支持恒等式

令 \(v_*=(x_*,y_*)\) 为上段显示构造；其 \(x_*,y_*<0,\ t_*=\beta,\ k_*=-\eta\)。记 \(a_*=-x_*>0,b_*=-y_*>0\)。联立观察得到

\[
|Q|b_*=Pa_*-\eta-c-E\beta,\qquad
1/5<b_*/a_*<P/|Q|<31/92.
\]

其它严格区间界：

\[
15/2<P<31/4,\quad23\le|Q|<93/4,\quad
239/10<A<241/10,\quad479/10<-B<481/10,
\]
\[
9/10000<a_*<1/1000,\qquad b_*>1/5000.
\]

定义

\[
\mu_*=\frac{Ay_*-Bx_*}{Py_*-Qx_*}
=\frac{Ab_*-Ba_*}{Pb_*+|Q|a_*},\quad
D=-\frac{A-\mu_*P}{2x_*},\quad
\tau=D-16+E\mu_*.
\]

这些纯代数界推出 \(21/10<\mu_*<9/4,\ D>3000,\ \tau>0\)。且

\[
(A-\mu_*P,B-\mu_*Q)=-2D(x_*,y_*).
\]

对于每一个合法 v，展开平方得到**恒等式**

\[
\boxed{I_4(v)-I_4(v_*)=
\mu_*[k(v)+\eta]+\tau[\beta-t(v)]+D|v-v_*|^2}.
\]

三个加项都非负，且严格等号唯一为 \(v=v_*\)；故这是一份全域充分证书。剩余的 h 可行性：\(\eta_c\) 处 \(h_*=-\eta_c\)，之后

\[
\frac{d}{d\eta}\big(\eta+h(v_*)\big)
=1+2\frac{-P+QK/S}{N}>1-\frac{2P}{N}>0.
\]

所以 \(\eta>\eta_c\) 时 \(h_*>-\eta\)，并由 \(x_*<0,\ t=\beta<\eta\) 得 \(h_*<\eta\)。唯一最优已证。

## 5. 正支路、尖点及参数变化

固定 \(u_+=i\sqrt{1-\varepsilon}\) 时，定义

\[
P_+=(245+123w_+)/16,\ Q_+=(-123+245w_+)/16,\ 
A_+=36+12w_+,\ B_+=-20+28w_+,
\]
\[
c_+=-709\varepsilon/64,\ N_+=P_+^2+Q_+^2,\ 
K_+=\eta-c_+-E\beta,\quad
S_+=\sqrt{N_+\beta-K_+^2}.
\]

取 \(v_+=(K_+(P_+,Q_+)+S_+(Q_+,-P_+))/N_+\)，以及

\[
\delta=A_+Q_+-B_+P_+,\qquad
\lambda_+=\frac{A_+P_++B_+Q_+-\delta K_+/S_+}{N_+}.
\]

严格区间验证 \(\delta>0,\ 19/10<\lambda_+<21/10,\ 16-E\lambda_+>0\)，并且 \(0<h(v_+)<L\le\eta\)。向量恒等式 \((A_+-\lambda_+P_+,B_+-\lambda_+Q_+)=(\delta/S_+)v_+\) 与 Cauchy–Schwarz 支持不等式给出圆盘和 \(k\le\eta\) 下的唯一最优；h 条件仍松弛。

负支路在临界点下方的包络导数为
\(I_{4,-}'=-(\lambda+\mu)+d\,t'(\eta)<-5\)，其中 \(t'(\eta)>0,d<0\)；上方右导数为 \(-\mu_*>-9/4\)，故两导数之差严格大于 \(11/4\)。根函数 \(F_\varepsilon\) 在所述区域对 η 严格增、对 ε 严格减（按 P,Q,c 的显式导数逐项可验），因此 \(\eta_c'(\varepsilon)>0\)。

## 6. 证明覆盖、证据与后继

对于 ε=0，约束直接强制 \(u=\pm i\)。故本轮证明完整负相位来源分支在 \(\eta\in[L,R]\) 的首个活跃约束切换；与 PREFIX-419 对 \([7/4000,L]\) 的已验证优化拼接，得到 \(\eta_c(0)\) 为合并区间 \([7/4000,R]\) 上的首次切换。并未将负分支的角点切换等同于第四 Port 全局最小偏差的来源分支切换。

对于 ε>0，定理覆盖整个噪声盒的**固定双基准角点**下的全部 v，尚未涵盖角点外的所有 u；下一步证明全 r,s 角点最优，或构造角点失效的严格相干反例。

BRC 方法复用判定 COMPOSE_APPLIED：使用联合 Port 观察、相干来源分支及纤维保真，不将相位幅值误记为正质量，也没有执行 native typed BRC。外部静态五 Port 研究与 P000 X6 空间/原生心跳动力学之间的对应保持为单独问题。

实际执行并保存了标准库 Fraction/isqrt 严格有理检查程序、独立 SymPy 原始 5×3 复矩阵程序及其原始 stdout 日志。与本研究说明共同发布的文件分别是：

- research_notes/prefix420_exact_certificate.py (Git blob 74bf684ac3cb9e2881045a04f5e0363b7b1c627f)
- research_notes/prefix420_exact_execution.log (Git blob cf9434ff509f071e0523dbb81bc7a6fcf901de33)
- research_notes/prefix420_independent_raw_matrix.py (Git blob 9a629d199fd3cdd239b00ddf7868890d4dbae48b)
- research_notes/prefix420_independent_execution.log (Git blob 3f22e8fb4f6e697e6c2861414e0bccd0b0490184)

原始程序运行结束标志分别为 PASS_PREFIX420_FIXED_SOURCE_FIRST_ACTIVE_SET_CHANGE_EXACT_CERTIFICATE 与 PASS_PREFIX420_INDEPENDENT_RAW_MATRIX_PROVENANCE。矩阵程序检查无噪声两个源支路及原始 Port 系数；连续 ε、η 证明来自上述解析推导和严格区间界，而非将有限抽样推断为全域定理。

GitHub 认证身份 awdawmip，具备仓库 push 权限。原生 Enterprise Math Sites Gateway 本轮为静态只读配置，research_authority_granted=false；实时任务查询返回 CONTROL_QUOTA。活跃 owner、CLAIM、原生 Result/Review 仍待具备相应权限的原生控制途径验证；本文件只是作者研究来源，未改变共享任务状态或原生接纳级别。

**PREFIX-421**：证明 \(\eta\in[L,R]\) 且 \(0<\varepsilon\le10^{-6}\) 时，固定角点以外的每个合法 \(r=|u|^2,s=|1+u|^2\) 能否由全局观察支持不等式排除；首选重用 PREFIX-419 的 \(H(r,s)\) 偏导判据并适配本轮切换后的 KKT 对偶证书。任何严格更优 u 是可接受的反例与下一研究路径。
