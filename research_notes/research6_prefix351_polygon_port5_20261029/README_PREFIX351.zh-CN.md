# PREFIX-351｜四行相位多边形与第五 Port 饱和不相容：真实来源分歧区间的精确收紧

**2026-10-29；作者侧精确辅助模型证明；实际执行的标准库 Fraction/isqrt 检查器 PASS；UNREVIEWED / NOT_ADMITTED。**

冻结 GLOBAL_KNOWLEDGE_V1 main@38898088a2f45ce1a8fdd5be7b115e617b2fe83d，Enterprise Math 科学输入 main@b7e005a480e17723d1fced8e1886681e78a3e88d。GitHub 实际账户 awdawmip；原生 Sites 的 research_authority_granted=false，活跃任务请求返回 CONTROL_QUOTA；未声称已取得原生 CLAIM、Source Result、活跃 owner 或独立 Driver 准入。

## 精确模型和来源

沿用 PREFIX-350 辅助静态复三维五 Port 模型：

$$
A=\begin{pmatrix}
4&4&0\\
0&-4&4\\
-5+3i&0&-3+i\\
-2-2i&4+4i&2+2i\\
-2&0&5+2i
\end{pmatrix},\quad y=Ac,\quad q_j=|y_j|^2.
$$

初始强度 $q^{(0)}=(2125/3721,200/3721,29125/29768,5825/7442,31525/59536)$，严格正终点 $q^+=(4,1,1,1,1)$。令 $q(t)=(1-t)q^{(0)}+tq^+$、$0\le t\le1$。先前 PREFIX-350 利用三项 Cauchy–Schwarz 必要条件证明 $t\ge2502575/3187239$ 时无真实复来源。此处证明一个更强的必要条件，并在饱和边界通过第五 Port 取得**严格不可实现性**。不更改 P000 或其它模型的定义。

## 定理 1：多边形必要条件、单调性及唯一根

直接逐列检查高斯整数行关系：

$$
(-5-9i)y_1+(-3-7i)y_2-8iy_3+2y_4=0.
$$

若 $y=Ac$，三角不等式给出必要条件

$$
g(t):=\sqrt{106q_1(t)}-\sqrt{58q_2(t)}-8\sqrt{q_3(t)}-2\sqrt{q_4(t)}\le0.
$$

对 $a_j=q_j(0)$，在 $[2/5,1]$ 有 $q_1\le4,\ q_2\ge t\ge2/5,\ q_3\ge a_3>9/10,\ q_4\ge a_4>3/4$；又 $\sqrt{106}>10,\sqrt{58}<8,\sqrt{2/5}>3/5$。对各根式导数用最不利端点界，得到完全有理的**严格导数证书**

$$
g'(t)>\frac52(4-a_1)-\frac{20}{3}-\frac{40}{9}(1-a_3)-\frac43(1-a_4)
=\boxed{\frac{101801}{66978}}>0.
$$

以 $t_-=470271288587/10^{12}$、$t_+=470271288588/10^{12}$ 为端点，Python 检查器对每个正有理 $x$ 使用

$$
m=\lfloor 10^{18}\sqrt{x}\rfloor,\qquad
m/10^{18}\le\sqrt{x}<(m+1)/10^{18}
$$

的整数平方根实现，使用精确 Fraction 对四根式取外包区间。实际断言结果为 $\overline g(t_-)<0<\underline g(t_+)$，没有用浮点数判定符号。连续性和上述导数界给出**唯一**多边形饱和根

$$
\boxed{\frac{470271288587}{10^{12}}<t_\triangle<
\frac{470271288588}{10^{12}},\quad g(t_\triangle)=0.}
$$

因此对所有 $t>t_\triangle$ 均有 $g(t)>0$，无真实复来源。注意 $g(t)\le0$ 是必要但远非充分条件，不能由左端负号宣称存在来源。

## 定理 2：饱和边界同样无真实来源

假设 $t=t_\triangle$ 有来源。三角等号强制 $(-3-7i)y_2,-8iy_3,2y_4$ 三项共享同一相位。除去真实全局相位，可以取

$$
y_2=(-3+7i)\sqrt{q_2/58},\quad y_3=i\sqrt{q_3},\quad y_4=\sqrt{q_4}.
$$

逐列精确验证第五行的关系：

$$
y_5=\left(\frac{46}{53}+\frac{61i}{212}\right)y_2
+\left(\frac{19}{212}-\frac{13i}{212}\right)y_3
+\left(\frac{245}{424}-\frac{123i}{424}\right)y_4.
$$

代入饱和相位后有

$$
424y_5=(-1958+2210i)\sqrt{q_2/58}+(26+38i)\sqrt{q_3}
 +(245-123i)\sqrt{q_4}.
$$

$q_2,q_3,q_4$ 在所给严格小区间内递增。用左右端有理数的整数平方根夹逼，并对各正、负系数取相应端点，得到严密区间证书

$$
0<\operatorname{Re}y_5<1/4,\qquad
0<\operatorname{Im}y_5<1/2.
$$

所以 $|y_5|^2<5/16$。但第五 Port 的要求是

$$
|y_5|^2=q_5(t_\triangle)>q_5(t_-)>3/4,
$$

矛盾。因此 $t_\triangle$ 也无来源。**本轮无条件辅助模型结论：**

$$
\boxed{\forall t\in[t_\triangle,1],\
\{c\in\mathbb C^3:|Ac|^2=q(t)\}=\varnothing.}
$$

这项“闭区间不可实现”证明只依赖固定 A 的两组精确行恒等式和有理区间检查，**不需要 PREFIX-349 六个来源全域穷尽性**。

## 与真实分歧的关系、限制和后继

若额外采用 PREFIX-342/349 尚待独立核查的“起点存在六个相异且非奇异的真实射影来源、有限射影测量映射”前提，则六条实分支在 $t=0$ 局部稳定，而 $t=t_\triangle$ 无实来源。由射影紧致性、严格正报告和局部逆函数定理，至少一个真实临界点位于

$$
\boxed{0<t_*<t_\triangle<0.470271288588}.
$$

相较上一轮 $t_*<2502575/3187239\approx0.785$ 有严格改进。**这不是首次临界点的准确定位**，没有认证 $t<t_\triangle$ 的来源个数或分歧类型，也不是 PREFIX-349 的旧报告参数 h 的恢复风险临界根。

外部背景：Király 与 Ehler（2014），The Algebraic Approach to Phase Retrieval and Explicit Inversion at the Identifiability Threshold，arXiv:1402.4053，讨论代数相位恢复；其研究不直接证明上述具体矩阵强度线段的不相容证书，本轮不声明外部首创。

精确检查器 verify_prefix351.py 再次核验45项保留 (Port,k,l) 来源的有序 BRC 路径对、原始强度、行恒等式、导数、两端符号和第五 Port 饱和矛盾。它属于**辅助静态代数**，未运行 BRC 时间演化，也不是以普通 Fraction 冒充原生 BRC；未使用 π、经典三角函数、矩阵指数或动力学数值替代。向 P000 原生 X6、三维切片第三分量、联合未来观察、Detector、时间演化及残差归因的保真映射均尚待证明。

执行命令：python verify_prefix351.py。实际退出码 0，返回 PASS_AUTHOR_SIDE_EXACT_POLYGON_OBSTRUCTION_AND_PORT5_BOUNDARY_EXCLUSION；运行产生 RESULTS_PREFIX351.json，机器输出详见 RUN_PREFIX351.txt。项目科研活动登记和原生 checkpoint 权限仍需独立处理。本轮下一问题见 NEXT_PREFIX352.md。
