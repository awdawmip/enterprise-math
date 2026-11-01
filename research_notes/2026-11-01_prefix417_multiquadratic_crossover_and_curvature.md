# PREFIX-417｜双基准带噪切换面的代数次数界与严格负曲率

2026-11-01 · 进取数论研究6 · 作者侧数学推导与精确区间运算；UNREVIEWED / NOT_ADMITTED / NO_NATIVE_CLAIM。

## 冻结来源、权限及对象

GLOBAL_KNOWLEDGE_V1：awdawmip/chatgpt-global-knowledge main@54fa7d60d81f96fd4ff80a18304013fec0b7b94e。Enterprise Math 科学输入：awdawmip/enterprise-math main@813d9a8c66c9facccbafd5492d439f1288ade1cd。已读取规范入口、ACTIVE 世界观、P000、联合关系观察保真、Portable Research、PREFIX-413/414/415/416。GitHub 登录 awdawmip。原生服务0.6.11 research_authority_granted=false，当前控制为 UPSTREAM_CODE_REVIEW_REQUIRED；本次活跃 Owner 查询返回 CONTROL_QUOTA。仅发布作者侧可移植材料，未取得原生 CLAIM、Review 或 Admission。

本研究针对外部静态五 Port 复振幅辅助模型。BRC 使用决议 COMPOSE_APPLIED：保留正负来源叶、复相位与 Cv/I5 联合观察，不声称执行原生 typed BRC 或证明 P000 X6、三维切片第三分量、时间动力学对应。

## 模型与原矩阵

五行分别是 (4,4,0); (0,-4,4); (-5+3i,0,-3+i); (-2-2i,4+4i,2+2i); (-2,0,5+2i)。前三 Port 输出归一化为 (1,u,v)，由原矩阵反演得

\[
z_4=(5+9i)/2+(3+7i)u/2+4iv,\quad
z_5=(22+15i)(1+u)/8+(5+9i)v/4.
\]

设双基准误差半径 \(\varepsilon\)，联合观察误差半径 \(\eta\)，第三强度上界 \(\beta=10^{-6}\)。PREFIX-416 作者侧局部活跃集结论给出当 \(\varepsilon\) 足够小时，切换附近两叶最优角点为 \(u_+=i\sqrt{1-\varepsilon}\)、\(u_-=-i\sqrt{1+\varepsilon}\)。

令 \(u=iw,\ v=x+iy,\ t=x^2+y^2\)。定义
\[
P=(245+123w)/16,\quad Q=(-123+245w)/16,\quad A=36+12w,\quad B=-20+28w,
\]
\[
J=(53-8w+29w^2)/2,\quad c=709(w^2-1)/64,\quad E=53/8.
\]
精确恒等式为
\[
I_4=J+Ax+By+16t,\quad k:=I_5-709/32=c+Px+Qy+Et,\quad h:=C_v-1=2x+t.
\]
且 \(N=P^2+Q^2=37577(1+w^2)/128\)、\(AP+BQ=521w^2-61w+705\)、\(AQ-BP=-(63w^2-368w-59)/2\)。第二份独立检查器从原始 \(5\times3\) 矩阵重推了这些等式。

## 定理一：局部切换点的次数至多 16 的代数判别

以正负下标表示在 \(w_\pm\) 上取值。在已证局部活跃范围中，正叶取 \(t=\beta,\ k=+\eta\)。令
\[
K=\eta-c_+-E\beta,\ N=P_+^2+Q_+^2,\ D=N\beta-K^2,
\]
\[
L=J_+-37+16\beta+(A_+P_++B_+Q_+)K/N,\quad C=(A_+Q_+-B_+P_+)/N.
\]
在切换邻域 \(C>0,D>0\)，正叶唯一极值满足
\[
S=+\sqrt D,\quad x_+=(KP_++SQ_+)/N,\quad y_+=(KQ_+-SP_+)/N,\quad q_+=L+CS.
\]

负叶取 \(h=k=-\eta\)。令
\[
x_0=-\eta/2,\quad x_1=-1/2,\quad
y_0=(-\eta-c_--P_-x_0)/Q_-,\quad y_1=(P_-/2-E)/Q_-.
\]
则 \(x_-=x_0+x_1t,\ y_-=y_0+y_1t\)，并且
\[
F(t)=a_2t^2+a_1t+a_0=0,\quad
a_2=x_1^2+y_1^2,\quad a_1=2(x_0x_1+y_0y_1)-1,\quad a_0=x_0^2+y_0^2.
\]
取 \(R_0=45-J_--A_-x_0-B_-y_0\)，\(R_1=-A_-x_1-B_-y_1-16\)，则 \(q_-=R_0+R_1t\)。在 \(\varepsilon=0\) 时 \(R_1=43/23>0\)，故在足够小的邻域非零。

交叉条件 \(q_+=q_-\) 等价于 \(Z+CS=R_1t\)，其中 \(Z=L-R_0\)。消去 \(t\)，并用 \(S^2=D\) 消去根号，定义
\[
H_2=a_2C^2,\quad H_1=C(2a_2Z+a_1R_1),\quad H_0=a_2Z^2+a_1R_1Z+a_0R_1^2.
\]
得到精确必要关系
\[
\boxed{\mathcal R(\varepsilon,\eta)=(H_0+H_2D)^2-H_1^2D=0.}
\]

这里 \(Z,a_1\) 对 \(\eta\) 是仿射，\(a_0,D\) 至多二次，因此 \(\mathcal R\) 在 \(K=\mathbb Q(\sqrt{1-\varepsilon},\sqrt{1+\varepsilon})\) 上是 \(\eta\) 的次数至多四的多项式。在 \(\varepsilon=0\) 它非零，故足够接近零的有理 \(\varepsilon\) 下仍非零。由于 \([K:\mathbb Q]\le4\)，取域范数得到一个有理系数、次数至多 **16** 的非零多项式，真实局部切换点必是它的根。这是代数次数上界，不宣称最小次数恰为16。

必须再以 \(w_+>0,w_-<0,S>0,0<t<\beta\) 以及两叶原观察约束和全局最优性筛去平方或域范数造成的伪根。取 \(\varepsilon=0\)，本轮 SymPy 精确化简 \(\mathcal R(0,\eta)\) 的整系数本原部分，逐项恢复 PREFIX-413 四次多项式：
\[
\begin{aligned}
P(z)={}&411370922419157000000000000000000000000z^4\\
&+3406648973825365305852000000000000000000z^3\\
&+7207920358822113492588156702000000000000z^2\\
&-15929217691721140762689459588000000z\\
&-23522344829723509499221428663222123.
\end{aligned}
\]

## 定理二：切换曲线的二阶导数严格为负

令 \((\varepsilon,\eta)=(0,\eta_0)\) 为 PREFIX-413/416 的首次交叉点，\(t_0\) 为负叶最优的小根。上述方程 \(F(\varepsilon,\eta,t)=0\) 在基点满足 \(F_t<0\)；令 \(G(\varepsilon,\eta)=q_+ -q_-\)，基点 \(G_\eta<0\)、\(D>0\)。实解析隐函数定理给出局部解析 \(t(\varepsilon,\eta)\) 与 \(\eta_\times(\varepsilon)\)。

\[
t_i=-F_i/F_t,\quad
t_{ij}=-(F_{ij}+F_{it}t_j+F_{jt}t_i+F_{tt}t_it_j)/F_t,
\]
\[
\eta_\times'(0+)=-G_\varepsilon/G_\eta,\quad
\eta_\times''(0+)=-\frac{G_{\varepsilon\varepsilon}
+2G_{\varepsilon\eta}\eta_\times'(0+)
+G_{\eta\eta}\eta_\times'(0+)^2}{G_\eta}.
\]

由上面 \(P\) 的唯一正根和负来源二次式 \(35881(\eta^2+t^2)+63662\eta t-135424t=0\)，有理数端点判号证明
\[
1806822353106/10^{15}<\eta_0<1806822353107/10^{15},
\quad
865703047568/10^{18}<t_0<865703047570/10^{18}.
\]
本轮程序在该根隔离盒上计算全部解析偏导，使用 Python Fraction 与整数 isqrt 对平方根做严格向外舍入。验证 \(F_t<0,\ G_\eta<0\)，并得到
\[
0.6241785101433<\eta_\times'(0+)<0.6241785101437
\]
以及新的严格证书
\[
\boxed{-422.827868028<\eta_\times''(0+)<-422.827868026.}
\]

于是 \(\eta_\times(\varepsilon)=\eta_0+\eta_\times'(0+)\varepsilon+\tfrac12\eta_\times''(0+)\varepsilon^2+o(\varepsilon^2)\)，二阶系数位于 \((-211.413934014,-211.413934013)\)，故切换面在零误差处**严格负曲率**，且在某个正右邻域持续向下弯曲。本轮未给出包含完整 \(0\le\varepsilon\le10^{-6}\) 的显式有效半径。

## 验证、界限及下一问题

已实际执行 SymPy + Fraction 精确检查器，输出 PASS_PREFIX417_RESULTANT_REDUCES_TO_PREFIX413_QUARTIC 与 PASS_PREFIX417_EXACT_RATIONAL_INTERVAL_SECOND_DERIVATIVE；另执行原始矩阵独立检查器，输出 PASS_PREFIX417_INDEPENDENT_RAW_MATRIX_GENERAL_W_COEFFICIENTS。程序的浮点打印仅供显示，决定性判号为有理计算。局部最优归属继续依赖 PREFIX-413/414/416 的作者侧全局结果；未进行独立数学审阅、形式证明、原生 typed BRC 运算或 P000 桥接。

PREFIX-418：在 \(0\le\varepsilon\le10^{-6}\) 证明显式有理半径内的活跃集稳定性、域范数根的合法来源筛选与唯一性，或找出角点失效反例；另需独立证明 X6 三维切片的嵌入、第三分量与未来观察保真。
