# C285｜187个有理夹逼区间的统一导数下界、根唯一性与简单性

日期：2026-10-25。证据等级：作者级精确有理证明与独立微分校验；未取得原生Task CLAIM、Result或独立Driver接纳。模型：C195/H168的79节点正有理辅助模型，不是P000原生六维Cell动力学。

## 固定输入与精确对象

完全沿用C275冻结的79个节点、35基本盒、权重向下取整定义、4个活动坐标I=(5,50,55,56)、两个负侧见证及正侧构造，不改函数F或阈值Q=2^128。C284证书SHA256为fcdad45cb2ed5df659b1a153762d358e2b7fa4df3e14c1be3eb505d4209ef576，每条记录[i,j,wid,k]表示沿v(t)=w+t(h-w)在[k/4096,(k+1)/4096]有严格负—正端点，且该闭段全程合法无极点。源头不可变证据：C284提交c30911099bed3ebc8c7f4c0999a4647e44ac1af1的research_handoffs/C284_187_EXACT_DYADIC_BRACKETS.json与C284_C275_FROZEN_SOURCE.py；原始输入追溯至C275不可变提交f166deb1ca690757ee837885b50d619aaaee84f3。

## 定理C285.1（统一横截性）

对C284的187条记录对应的**整个**长度1/4096的闭参数区间，原始精确正有理函数满足：

\[
\boxed{\frac{d}{dt}F(v(t))>\frac{Q}{56}>0},\quad Q=2^{128}.
\]

故每条C284夹逼区间内**恰有一个**方程F(v(t))=Q的根；根位于严格内部并且是简单根，正向横截阈值。187是带基本盒编号的**证书数**，不是187个互不相同的几何根；按见证、完整正侧端点区分，187条记录共有125条不同的端点定义参数路径。没有证明各条路径在其余参数处不存在其他根。

## 证明（无浮点决定性步骤）

把F(v)=Σ(j=0..78) M_j(v)逐项拆为79条严格正的有理支路。令d=h-w，则v_r(t)=w_r+t d_r。对固定支路j不属于I：

\[
\ell_j(t):=\frac{d}{dt}\log M_j(v(t))
=\sum_{r\in I}d_r\left[\frac1{U_j-v_r(t)}-\frac1{Z-v_r(t)}\right].
\]

对活动支路p属于I：

\[
\ell_p(t)=6v_p(t)d_p\left(\frac1{2-v_p(t)^2}+\frac1{3-v_p(t)^2}\right)
-d_p\sum_{j\notin I}\frac1{v_p(t)-U_j}
-\sum_{r\in I\setminus\{p\}}\left[\frac{d_r}{Z-v_r(t)}+\frac{d_p-d_r}{v_p(t)-v_r(t)}\right].
\]

每个分母在对应C284闭区间不为零且符号固定。每个c/(a+bt)的单调性表明其区间上下界可由两端精确有理数确定；对上式活动核6v(1/(2-v²)+1/(3-v²))，当0<v<1时严格随v增加，故同样可用两个端点严格包络。逐项有理相加得到l_j≤ℓ_j(t)≤u_j。取B_j=max(|l_j|,|u_j|)、中点m=(a+b)/2、ρ_j=B_j(b-a)/2。

精确复演对187×79个支路都验证ρ_j<1。因此沿区间对ℓ_j积分，且用exp(-x)≥1-x与exp(x)≤1/(1-x)（0≤x<1），可得：

\[
M_j(v(m))(1-\rho_j)\le M_j(v(t))\le \frac{M_j(v(m))}{1-\rho_j}.
\]

于是定义纯有理下界：

\[
D_j=\begin{cases}
M_j(v(m))(1-\rho_j)l_j,&l_j\ge0,\\
M_j(v(m))l_j/(1-\rho_j),&l_j<0.
\end{cases}
\quad
F'(t)=\sum_j M_j(v(t))\ell_j(t)\ge\sum_jD_j.
\]

C285_EXACT_UNIFORM_DERIVATIVE.py从原始函数、C284证书与以上公式逐项生成全部D_j，以Python标准库Fraction完成187次**严格整数交叉相乘比较**：56·ΣD_j>Q全部通过，没有区间再细分，没有使用浮点近似决定符号。故在各整个闭区间有F'(t)>Q/56。由C284严格异号端点和介值定理存在根；由严格单调必唯一，且非零导数说明是简单根。证毕。

## 两条互补复核与证据范围

1. 主证书复算：C285_EXACT_UNIFORM_DERIVATIVE.py，187/187全区间严格导数下界与C284两端原函数重算，结果C285_187_UNIQUE_SIMPLE_ROOTS_EXACT_PASS Q_over_56_derivative_bound。
2. 独立微分实现：C285_INDEPENDENT_DUAL_CHECK.py实现独立前向对偶数自动微分，不调用上述对数微分公式生成结果；对187条路径的中点，原始79支路乘积的自动微分值与作者对数导数精确逐项求和值逐分数一致，结果C285_INDEPENDENT_DUAL_187_EXACT_PASS。这是公式核对，不等于独立Driver数学审查。

证据依赖是C275数学输入和C284证书，程序在同目录加载原始Python文件与JSON；完整源输入、生成脚本及输出在随附可移植ZIP中。计算只说明声明的正有理辅助模型和参数线段，没有独立证明原生BRC相位、符号、端口、六维Cell路径或时间操作保真桥接；也没有宣称125条端点不同的路径产生125个不同几何根。

## 状态、来源与下一个问题

AUTHOR_EXACT_AUXILIARY / LOCAL_EXACT_FULL_REPLAY_PASS / DUAL_187_PASS / NOT_ADMITTED。原生控制dispatch本轮返回CONTROL_QUOTA，因此没有实时Owner确认、CLAIM、正式Source Result或Driver接纳。研究分支GitHub保存属于作者证据，不会更改规范任务状态。

下一研究问题：以相同的79支路ℓ_j精确区间包络，考察125条独立参数路径的[0,1]能否划分为单调段，精确判断**全路径根数量**；必要时构造符号变化区间，避免把短区间唯一性过度推广到全路径。
