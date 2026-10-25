# R293 — 有效无限有理锥证明 BRC 两个负平移基底全系数严格为正

2026-10-26；作者侧解析证明与精确整数/代数数证书。继承 R288/R290 的作者侧精确生成函数，尚未取得独立 Driver 数学审查、原生 CLAIM / Source Result 或 Foundation 接纳。下述全部结论属于正权有序六边 BRC **辅助来源计数模型**，不是心跳世界原生 X6 动力学定理。

## 1. 对象、精确输入和未决命题

控制态 q=0,1,2；按来源位 0/1 的有序转移依次为 q0:(2,-1,-1)/(2,+1,-1)，q1:(0,-1,-1)/(0,+1,-1)，q2:(1,+1,+1)/(2,+1,-1)，禁止相邻 00。初始完整效果 (+1,0)，右复合 $(\epsilon,k)\star(\eta,c)=(\eta\epsilon,\eta k+c)$，初末控制态均为 0，保留所有来源词的正整数重数。$P_n(\epsilon,k)$ 表示长度 $n$ 的完整效果纤维计数。

沿用 R288/R290 的精确公式（需独立审核），令 $y=x^2$：

$$
\Delta_m^\epsilon(x)=\sum_{n\ge0}\bigl(P_n(\epsilon,-m)-P_n(\epsilon,-m-2)\bigr)x^n=x^{m+2}G_m^\epsilon(y).
$$

$$
h=y^4+(y+2y^2+y^3+y^4)h+y(1+y)^2h^2,\quad h\in y^4\mathbb N[[y]],\qquad w=(1+y)(1+h).
$$

$$
G_m^-(y)=\frac{w^{m-1}(1-yw)}{1+y}\;(m\ge2),\qquad
G_m^+(y)=\frac{w^{m+1}(1-y+y^2-yw)}{1+y}\;(m\ge1).
\tag{1}
$$

由此 $w\in\mathbb N[[y]],w(0)=1$ 且 $G_{m+1}^\epsilon=wG_m^\epsilon$。R291 精确验证过两个基底 $G_{11}^-,G_{13}^+$ 的前 50001 项正性，但不能推出无限尾部。本轮的新证明消去此剩余的无穷长度缺口。

## 2. 主定理

在以上来源—生成式对应关系成立的前提下：

$$
\boxed{[y^j]G_{11}^->0,\qquad [y^j]G_{13}^+>0\quad\text{对所有整数 }j\ge0.}
\tag{T1}
$$

更一般地，
$$
\boxed{[y^j]G_m^->0\;(m\ge11),\qquad [y^j]G_m^+>0\;(m\ge13),\quad\forall j\ge0.}
\tag{T2}
$$

结合 R286 的正/负平移镜像支配，所有长度的清洁完整效果最大值可在下列至多 28 个候选中取得：

$$
\boxed{\{(+1,k):-14\le k\le0\}\ \cup\ \{(-1,k):-12\le k\le0\}.}
\tag{T3}
$$

这解除了 R287 四基底全系数非负的条件。它**不证明**这 28 个效果中某两个中央效果一定全局最大，也不证明 $N_{\mathrm{peak}}$、$B_n=\Lambda_n$、X6 原生 Cell 物理模型或数学审核接纳。

## 3. 精确无穷比值锥

令
$$
g(y)=\sqrt{\frac{1-3y+y^2}{1+y+y^2}},\qquad f_n=-[y^n]g(y),\quad f_0=-1,\ f_n=0\ (n<0).
$$
由 $(1-3y+y^2)(1+y+y^2)g'=(2y^2-2)g$，系数比较给出整数递推
$$
(n+1)f_{n+1}=(2n-2)f_n+(n-1)f_{n-1}+(2n-2)f_{n-2}-(n-3)f_{n-3}.
\tag{2}
$$

写 $R=(3+\sqrt5)/2$，对整数 $n\ge998$ 定义
$$
L_n=R\left(1-\frac3{2n}-\frac{100}{n^2}\right),\qquad
U_n=R\left(1-\frac3{2n}+\frac{100}{n^2}\right).
$$
**引理：**
$$
\boxed{L_n<r_n:=f_n/f_{n-1}<U_n\qquad(n\ge998).}
\tag{3}
$$

基底 $n=998,999,1000$ 由 (2) 的无界整数直接计算，并用整数平方根提供 $\sqrt5$ 的严格有理界，核对三项全严格且 $f_{997},\ldots,f_{1000}>0$。

归纳时把 (2) 改写为
$$
r_{n+1}=F_n(r_n,r_{n-1},r_{n-2}),\quad
F_n(a,b,c)=\frac{2n-2+(n-1)/a+\bigl(2n-2-(n-3)/c\bigr)/(ab)}{n+1}.
$$
在 $n\ge1000$ 的正锥范围，$F_n$ 随 $a,b$ 严格递减，随 $c$ 严格递增。只需检验
$$
F_n(U_n,U_{n-1},L_{n-2})-L_{n+1}>0,\quad
U_{n+1}-F_n(L_n,L_{n-1},U_{n-2})>0.\tag{4}
$$
两个有理代数函数通分，代 $n=t+1000$ 后分子、分母均成为 $\mathbb Q(\sqrt5)[t]$ 多项式，且**每个非零系数都形如 $A+B\sqrt5$，$A,B\in\mathbb Q_{\ge0}$ 且 $A+B>0$**。随附 INFINITE_CERTIFICATE.json 给出全部展开的 $A,B$ 精确分数；Python/SymPy 程序逐个符号核查。故对整个 $t\ge0$ 的无限域成立，从而 (3) 归纳成立。

## 4. 固定多项式滤波器把比值锥转为严格单调

设
$$
A=1+2y^2-y^3,\quad C=1-y^3,\quad E=(1-y)(1-3y+y^2),
$$
则 $w=(A-Cg)/(2y)$、$C^2g^2=CE$。定义整数多项式 $P_0=1,Q_0=0$，
$$
P_{r+1}=AP_r-EQ_r,\qquad Q_{r+1}=AQ_r-CP_r.\tag{5}
$$
恒等式 $(A-Cg)^r=P_r+Q_rg$ 随即归纳成立。对两基底分别定义：
$$
p_-=2P_{10}-P_{11},\quad q_-=2Q_{10}-Q_{11},\quad(d_-,T_-)=(10,2048);
$$
$$
p_+=2(1-y+y^2)P_{14}-P_{15},\quad q_+=2(1-y+y^2)Q_{14}-Q_{15},\quad(d_+,T_+)=(14,32768).
$$
则精确地
$$
H_\pm:=(1+y)G^\pm_{11/13}=\frac{p_\pm+q_\pm g}{T_\pm y^{d_\pm}},\qquad
\deg q_-=33,\;\deg q_+=45.
\tag{6}
$$

设 $H_\pm(y)=\sum H_jy^j$ 且 $q(y)=\sum_{s=0}^S q_sy^s$。$j\ge50000$ 时多项式 $p$ 不再参与。令 $N=j+d$，
$$
H_j-H_{j-1}=-\frac1T\sum_{s=0}^S q_s(f_{N-s}-f_{N-s-1}).
\tag{7}
$$

固定 $N\ge50000$，记 $\theta_N=R(1-3/(2N))$、$\tau=1/\theta_N$、$\delta=10^{-7}$。对于 $0\le s\le45$，由 (3) 的两个显式界有
$$
\left|\frac{r_{N-s}}{\theta_N}-1\right|
\le\frac{\frac32\frac{45}{50000(50000-45)}+\frac{100}{(50000-45)^2}}
{1-\frac3{2\cdot50000}}<\delta.
\tag{8}
$$
精确有理界 $\alpha=381966/10^6$, $\beta=381979/10^6$ 进一步保证 $\alpha\le\tau\le\beta$。

**滤波器定量证书**：对 $q=q_-,q_+$，精确有理数验证同时得到
$$
q(\alpha)<-40,\quad q'(\alpha)<0,\quad
\frac{(\beta-\alpha)^2}{2}\sum_{s\ge2}|q_s|s(s-1)\beta^{s-2}<1,\quad
\sum_s|q_s|\beta^s<400000.
\tag{9}
$$
故 Taylor 定理给出 $q(\tau)<-39$。

令 $X_s=(f_{N-s}-f_{N-s-1})/f_N$。利用
$$
X_s=\frac{f_{N-s}}{f_N}\left(1-\frac1{r_{N-s}}\right)
$$
和 (8) 对每个倒比值的限制，可直接估计
$$
|X_s-\tau^s(1-\tau)|\le
\tau^s\frac{(s+1)\delta}{(1-\delta)^{s+1}}
<\frac{\tau^s}{200000}\quad(0\le s\le45).
\tag{10}
$$
于是
$$
\sum_s q_sX_s\le(1-\tau)q(\tau)+\frac{400000}{200000}
<-\frac35\cdot39+2<0.
\tag{11}
$$
由于 $f_N>0,T>0$，式 (7) 表明 **所有 $j\ge50000$ 均有 $H_j>H_{j-1}$**。注意这个无限量词来自 (3)—(11)，不是未量化的渐近 $O(j^{-1})$。

对 $c_j=[y^j]G$，因 $H=(1+y)G$，
$$
\boxed{c_j-c_{j-2}=H_j-H_{j-1}>0,\quad j\ge50000.}\tag{12}
$$
所以只要区间 $0\le j\le50000$ 的奇偶两条序列均正，就对所有后续长度正。

## 5. 真实执行的有限证书、结论强度和来源

R293_verify_finite_prefix.js：标准 Node.js BigInt，按 (2)、(5)、(6) 核验 $0\le j\le50000$ 的两个完整基底各 **50001** 个系数严格正，整除处检查余数；首十系数与已发布 R290 证据相同，独立原始六边 DP 完整效果比较覆盖 $n\le160$ 的 **147** 项，输出 FINITE_CERTIFICATE.json，状态 PASS。前缀的最小整数系数均为 1。

R293_verify_global_certificate.py：精确 $\mathbb Q(\sqrt5)$ 符号与 Python Fraction 运算；检查 (3) 三个有限基底、(4) 两个无穷系数正锥、(8) 及 (9)—(11) 每项严格不等式，输出 INFINITE_CERTIFICATE.json，状态 PASS。证书中携带分子/分母按 $t=n-1000$ 展开后的 **全部精确系数**，而非数字抽样或浮点近似。

将 (12) 与已穷尽的前缀结合，证明 (T1)。从 $w\in\mathbb N[[y]]$、$w(0)=1$ 逐次相乘得 (T2)；由 R286 镜像正半线的支配得 (T3)。

真实性边界：脚本经过实际执行，但还没有 Lean/Coq 形式化或独立 Driver 复核；R288 源头生成式与 R286 镜像结论仍分别是作者侧依赖。未得到正式数学 Source 接纳。

固定全局读取快照 awdawmip/chatgpt-global-knowledge canonical main@5cfafe5408d59d3f2bb26a7ba8376099c30e54f3，P000 原件 blob=770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc 与启动投影一致；EM 主控制初始 main@d8ef3afd87836ca5b1a83d28bef8d75aa16699d4。R290 作者证明/证据 7dce1f201dd27b90a745ef8b8f2895cde63fed70；R291 独立扩大有限前缀 0393556ce9ff988f5792c55e1bbd08e6ff12ca99。BRC 工具方法状态 REUSE_APPLIED（精确代数计数、整数递推、来源留存），并未伪称原生 X6 物理对应。

当前 GitHub 认证身份 awdawmip，仓库可写；原生 em_control_tasks 回 CONTROL_QUOTA，因此当期活跃 Owner、当前 CLAIM 未能权威核验；没有自赋研究/审查身份。P000、ACTIVE 世界观不修改。研究文件仅为作者侧非规范证据。

**下一数学单元**：对已缩小的最多 28 个完整效果建立能覆盖全部相关长度的中央峰值支配证书（须保留固定 $n$ 的奇偶及来源计数），得明确 $N_{\mathrm{peak}}$；之后再分别审查六通道 clean/dirty 条件及 $B_n=\Lambda_n$。对 R288 的精确式和本轮无限代数锥安排独立 Driver 数学审查。

**状态**：R293_TWO_BASE_ALL_COEFFICIENT_POSITIVITY_AUTHOR_PROVED / EXACT_QSQRT5_INFINITE_CERT_PASS / FINITE_BIGINT_100002_PASS / RAW_DP_147_PASS / OWNER_UNVERIFIED / DRIVER_UNREVIEWED / NOT_ADMITTED.
