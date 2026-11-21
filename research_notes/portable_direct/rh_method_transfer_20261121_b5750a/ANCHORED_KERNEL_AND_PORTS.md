# RH 方法继续提取：固定原点 Gram 核、低频相干与尾端口

Date: 2026-11-21, Asia/Hong_Kong.
Contribution: collaborative mathematical derivation for the parent session; not an independently registered project Review or Task CLAIM.
Status: proved finite/limiting operator identities and a cutoff-cost theorem; the uniform RH road-energy estimate remains a research target.
Scientific input snapshot: `awdawmip/enterprise-math@9fc068244e4f1117f1e75df5eb0285c6697d21d7`.

## 1. 实际研究对象和本次推进

项目正本定义

\[
R_a(n)=\prod_{p\mid n}(1-p^{-a}),\qquad c_a=1/\zeta(1+a),\qquad
B_{a,N}=\sum_{n\le N}R_a(n)-1-c_a(N+\tfrac12).
\]

既有研究把 RH 对应到

\[
\mathcal D_a=\sum_{N\ge1}\frac{B_{a,N}^2}{N^2}=O(a),\qquad a\downarrow0.
\]

本次沿用该研究接口，没有重新审查其全部解析依赖。这里不把外部证明已经给出的结论当作我们这条道路路线自身的证明。

Ramanujan 展开正本给出

\[
u_a(n):=R_a(n)-c_a
=c_a\sum_{q\ge2\atop q\text{ squarefree}}\beta_a(q)c_q(n),\qquad
\beta_a(q)=\frac{\mu(q)}{\prod_{p\mid q}(p^{1+a}-1)}.
\]

原记录的具体下一步是保留固定原点，构造累计频率之间的二次核。本次完成该核的显式公式、低频极限及其正平方分解，并发现一个直接约束模态截断成本的端口定理。

这些都是 X6 载体上已有算术观察量的外部计算表示；频率、模数和状态字段不成为新增空间轴。

## 2. 完整复数核：保留全部固定原点交叉项

统一采用**弧度角频率**：

\[
h_N(\theta)=\sum_{n=1}^N e^{in\theta},\qquad
K(\theta,\phi)=\sum_{N\ge1}\frac{h_N(\theta)\overline{h_N(\phi)}}{N^2}.
\]

假设两频率均不属于 \(2\pi\mathbb Z\)。令 \(z=e^{i\theta},\ v=e^{-i\phi}\)，则

\[
\boxed{
K(\theta,\phi)=\frac{zv}{(1-z)(1-v)}
\left[\zeta(2)-\operatorname{Li}_2(z)-\operatorname{Li}_2(v)
+\operatorname{Li}_2(zv)\right].
}
\]

这里 \(\operatorname{Li}_2(w)=\sum_{N\ge1}w^N/N^2\) 在单位圆上按其绝对收敛级数定义，因而没有额外的对数分支选择。证明直接将

\[
h_N(\theta)=\frac{z(1-z^N)}{1-z}
\]

代入并展开。每个固定频率的 \(h_N\) 有界，所以四个级数均可逐项求和。

常数端口的交叉核同样明确：

\[
L(\theta)=\sum_{N\ge1}\frac{h_N(\theta)}{N^2}
=\frac{z}{1-z}\,[\zeta(2)-\operatorname{Li}_2(z)].
\]

对有限频率族及复系数 \(\alpha_\nu\)、常数 \(b\)，完整能量为

\[
\sum_{N\ge1}\frac{|\sum_\nu\alpha_\nu h_N(\theta_\nu)-b|^2}{N^2}
=\sum_{\nu,\eta}\alpha_\nu\overline{\alpha_\eta}K(\theta_\nu,\theta_\eta)
-2\Re\!\left(\overline b\sum_\nu\alpha_\nu L(\theta_\nu)\right)
+|b|^2\zeta(2).
\]

这包括所有非对角项及固定原点常数。实际道路的有限模数截断中，
\(\theta_{q,r}=2\pi r/q\)、\(\alpha_{q,r}=c_a\beta_a(q)\)、\((r,q)=1\)，且 \(b=1+c_a/2\)。不能直接把这个有限式推广为任意次序的无限模态双和。

平移起点 \(m\) 会给各项乘上 \(e^{im\theta_\nu}\)。对 \(m\) 做无限平移平均，只保留相同频率间的项。这里计算的是固定起点的 Gram 核，没有进行这种平均。

## 3. 低频极限：相关性沿对数频率衰减

对固定非零实数 \(x,y\)，令 \(0\log0:=0\)。有完整复极限

\[
\boxed{
\lim_{\varepsilon\downarrow0}\varepsilon K(\varepsilon x,\varepsilon y)
=\frac{\frac\pi2(|x|+|y|-|x-y|)
+i[x\log|x|-y\log|y|-(x-y)\log|x-y|]}{xy}.
}
\]

证明中设 \(t=\varepsilon N\)。有限几何和给

\[
\varepsilon h_N(\varepsilon x)\longrightarrow
f_x(t):=\frac{e^{ixt}-1}{ix}.
\]

于是所需极限是

\[
\int_0^\infty\frac{f_x(t)\overline{f_y(t)}}{t^2}\,dt.
\]

这个 Riemann 和极限可以由统一界严格控制：在零点附近使用
\(|\varepsilon h_N|\le\varepsilon N=t\)，在无穷远使用
\(|\varepsilon h_N(\varepsilon x)|\le 2\varepsilon/|1-e^{i\varepsilon x}|\le C_x\)。
被积项在零点附近有界，在无穷远有 \(O_{x,y}(t^{-2})\) 控制。

分子实部用
\(\int_0^\infty(1-\cos at)t^{-2}dt=\pi|a|/2\) 得到；虚部将
\(-\sin xt+\sin yt+\sin(x-y)t\) 合并后分部积分，使用
\(\int_0^\infty(\cos at-\cos bt)t^{-1}dt=\log|b/a|\) 得到。合并式在零点具有所需抵消，不对单独发散的积分赋值。两项经典积分亦可先加 \(e^{-\delta t}\) 阻尼，再令 \(\delta\downarrow0\)。

同号 \(x,y\) 的实部为 \(\pi/\max(|x|,|y|)\)；异号时实部为零，**虚部一般不为零**，因此复模式不能仅保留实部。

### 实数 ± 频率配对

道路的实系数与共轭频率天然配对。定义

\[
C_N(\theta)=\sum_{n=1}^N\cos(n\theta),\qquad
K_{\cos}(\theta,\phi)=\sum_{N\ge1}\frac{C_N(\theta)C_N(\phi)}{N^2}.
\]

有恒等式

\[
K_{\cos}(\theta,\phi)=\tfrac12\Re[K(\theta,\phi)+K(\theta,-\phi)].
\]

一对复频率的系数若各为 \(w\)，配对后的 cos 幅度是 \(2w\)；自共轭的 \(\theta=\pi\) 单项只计算一次。

故对 \(x,y>0\)，

\[
\boxed{
\lim_{\varepsilon\downarrow0}\varepsilon K_{\cos}(\varepsilon x,\varepsilon y)
=\frac{\pi}{2\max(x,y)}.
}
\]

**归一化约定：**如果把 \(h_N\) 改写为 \(\sum e^{2\pi in\alpha}\)，同号复核的实部极限系数变为 \(1/[2\max(x,y)]\)，cos 核变为 \(1/[4\max(x,y)]\)。这是 \(\theta=2\pi\alpha\) 的代换，不是不同结论。

将 cos 极限核按其对角元归一化，得到

\[
\frac{\min(1/x,1/y)}{\sqrt{(1/x)(1/y)}}
=\sqrt{\frac{\min(x,y)}{\max(x,y)}}
=e^{-|\log x-\log y|/2}.
\]

同一倍频区间内的极限相关至少为 \(1/\sqrt2\)。因此其非对角项与对角项同阶；对角功率控制不等于固定原点能量控制。以 \(x=1,y=2\)、相同实幅度为例，低频极限中被删去的交叉项是对角部分的 \(2/3\)。

上述极限是固定有限频率族的渐近陈述。频率数量、幅度或频率比例随参数增长时，仍须证明相应的统一误差；本稿没有把逐项渐近作为全尺度尾估计。

## 4. 可计算的正平方证书：保留相干而无需存储稠密矩阵

令 \(0<x_1\le\cdots\le x_r\)，\(v_i=1/x_i\)，\(v_{r+1}=0\)。对任意实幅度 \(a_i\)，

\[
\boxed{
\sum_{i,j=1}^r a_i a_j\min(v_i,v_j)
=\sum_{k=1}^r(v_k-v_{k+1})\left(\sum_{i=1}^k a_i\right)^2.
}
\]

证明是 \(\min(v_i,v_j)=\sum_{k\ge\max(i,j)}(v_k-v_{k+1})\)，然后交换有限求和。
乘以 \(\pi/2\) 就是上一节 cos 低频极限能量。

该式将全部相干关系转成**累计带符号幅度的正平方**，在已排序频率上只需线性次数的更新。它没有把带符号信息逐项取绝对值；平方前先完成同一端口的相加，抵消被保留。

同一核的归一化形式 \(R_{ij}=e^{-|t_i-t_j|/2}\)、\(t_i=\log x_i\)，在互异递增频率下具有三对角逆。设 \(\rho_i=e^{-(t_{i+1}-t_i)/2}\)，则

\[
z^TR^{-1}z=z_1^2+\sum_{i=2}^r\frac{(z_i-\rho_{i-1}z_{i-1})^2}{1-\rho_{i-1}^2}.
\]

证明：由递推 \(Z_1=\xi_1\)、\(Z_i=\rho_{i-1}Z_{i-1}+\sqrt{1-\rho_{i-1}^2}\,\xi_i\)，其协方差恰为 \(R\)；将三角线性变换反解即可。这里协方差只是确定该正定矩阵的代数表示，不需要把道路假设成随机过程。重复频率可先合并幅度。

BRC 可复用的是累计幅度与正平方的精确状态接口；原非负权重稳定性证书仍可负责成本上界。要用于实际道路，还要控制有限频率核与此极限核的差，以及截断后的端口残差。

### 4.1 无需低频极限的有限频率正平方证书

还可以进一步避免把有限频率近似成极限。对任意有限实系数 \(a_i\)、\(0<\theta_i\le\pi\) 和实常数端口 \(b\)，有精确恒等式

\[
C_N(\theta)=\tfrac12\cot(\theta/2)\sin(N\theta)
+\tfrac12[\cos(N\theta)-1].
\]

定义

\[
u_i=\tfrac12a_i\cot(\theta_i/2),\quad
S_N=\sum_i u_i\sin(N\theta_i),\quad
R_N=\tfrac12\sum_i a_i[\cos(N\theta_i)-1]-b.
\]

于是 \(\sum_i a_iC_N(\theta_i)-b=S_N+R_N\)。令

\[
T_u(t)=\sum_{\theta_i\ge t}u_i,\quad
T_a(t)=\sum_{\theta_i\ge t}a_i,\quad
m=\frac1\pi\sum_i u_i\theta_i.
\]

两个子能量具有**精确的正平方表示**：

\[
\boxed{
E_S:=\sum_{N\ge1}\frac{S_N^2}{N^2}
=\frac\pi2\int_0^\pi[T_u(t)-m]^2\,dt,
}
\]

\[
\boxed{
E_R:=\sum_{N\ge1}\frac{R_N^2}{N^2}
=\frac\pi8\int_0^\pi
\left[T_a(t)+2b\left(1-\frac t\pi\right)\right]^2\,dt.
}
\]

两式都保留带符号幅度的累计和。常数 \(b\) 进入第二个积分，没有在平均或截断中消失。排序后，第一积分是阶梯函数平方、第二积分是分段一次函数平方，均可以线性次数的精确代数更新计算。

证明使用 \(F(t)=\sum_{N\ge1}\cos(Nt)/N^2=\pi^2/6-\pi t/2+t^2/4\)（\(0\le t\le2\pi\)）及偶性。由于 \(\theta_i+\theta_j\le2\pi\)，直接展开得到

\[
\sum_{N\ge1}\frac{\sin(N\theta)\sin(N\phi)}{N^2}
=\frac\pi2\min(\theta,\phi)-\frac12\theta\phi,
\]

\[
\sum_{N\ge1}\frac{[\cos(N\theta)-1][\cos(N\phi)-1]}{4N^2}
=\frac\pi8\min(\theta,\phi),
\]

\[
\sum_{N\ge1}\frac{\cos(N\theta)-1}{2N^2}
=-\frac\pi4\theta+\frac18\theta^2.
\]

把 \(\min(\theta,\phi)\) 写成 \(\int_0^\pi 1_{t\le\theta}1_{t\le\phi}\,dt\) 即得上述两个积分。第二式中常数端口的平方项恰为
\(\frac\pi8\int_0^\pi[2b(1-t/\pi)]^2dt=b^2\zeta(2)\)。

完整有限模型能量 \(E\) 满足

\[
\boxed{(\sqrt{E_S}-\sqrt{E_R})^2\le E\le(\sqrt{E_S}+\sqrt{E_R})^2.}
\]

这里仅对 \(S\) 与 \(R\) 两组之间的耦合使用 Cauchy–Schwarz；各组内部的非对角相干和原点端口均精确保留。若该界太粗，§2 的完整核仍可精算组间交叉项。分别证明两组 \(O(a)\) 是全道路目标的一种充分条件，不宣称必要。

交叉项也有精确表达。设 \(\operatorname{Cl}_2(t)=\sum_{N\ge1}\sin(Nt)/N^2\)，则

\[
X_{SR}:=\sum_{N\ge1}\frac{S_NR_N}{N^2}
=\sum_i u_i\left\{
\frac14\sum_j a_j[\operatorname{Cl}_2(\theta_i+\theta_j)
+\operatorname{Cl}_2(\theta_i-\theta_j)-2\operatorname{Cl}_2(\theta_i)]
-b\operatorname{Cl}_2(\theta_i)\right\}.
\]

因此 \(E=E_S+E_R+2X_{SR}\)。若两组之间的抵消对目标不可少，可以直接保留该项，不必把三角上界固定为研究路线。

此有限频率证书直接适用于下面的 sharp 截断及端口补偿模型；其有效性不依赖频率数量固定或低频渐近误差可统一。

## 5. 有限模态到真实道路：有界窗口的严格误差

定义 sharp 模数截断

\[
B^{(Q)}_{a,N}=c_a\sum_{2\le q\le Q\atop q\text{ squarefree}}
\beta_a(q)\sum_{n\le N}c_q(n)-1-\frac{c_a}{2}.
\]

由 Euler 乘积可得 \(|c_a\beta_a(q)|\le q^{-1-a}\)。对平方自由 \(q\)，
\(|c_q(n)|=\varphi(\gcd(q,n))\le n\)。所以

\[
|B_{a,N}-B^{(Q)}_{a,N}|
\le \frac{N(N+1)}{2a}\,Q^{-a}.
\]

于是对有限 \(M\)，

\[
\left(\sum_{N=1}^M\frac{|B_{a,N}-B^{(Q)}_{a,N}|^2}{N^2}\right)^{1/2}
\le \delta_{a,Q,M}:=\frac{Q^{-a}}{2a}
\left(\sum_{N=1}^M(N+1)^2\right)^{1/2}.
\]

令 \(\mathcal D^{(Q)}_{a,M}\) 为截断后的有限能量。三角不等式给出可用于有限证据的严格区间

\[
\bigl(\max\{0,\sqrt{\mathcal D^{(Q)}_{a,M}}-\delta_{a,Q,M}\}\bigr)^2
\le\mathcal D_{a,M}
\le\bigl(\sqrt{\mathcal D^{(Q)}_{a,M}}+\delta_{a,Q,M}\bigr)^2.
\]

此界随 \(M\) 增长，不能据此交换 \(M\to\infty\) 与 \(Q\to\infty\)。它使有限窗口计算的误差明确可查，也暴露了粗截断的成本。

## 6. 直接道路定理：无补偿的 sharp 模态截断需要极大频率窗口

这个结论针对上述指定截断表示，不是对真实道路的能量下界。

在第一个端口 \(N=1\)，Ramanujan 和满足 \(c_q(1)=\mu(q)\)，所以所有尾项的符号相同。设

\[
T_{a,Q}=c_a\sum_{q>Q\atop q\text{ squarefree}}
\frac1{\prod_{p\mid q}(p^{1+a}-1)}>0.
\]

Euler 乘积给

\[
\sum_{q\ge1\atop q\text{ squarefree}}
\frac1{\prod_{p\mid q}(p^{1+a}-1)}=\zeta(1+a).
\]

因此

\[
\boxed{B^{(Q)}_{a,1}=-\frac32c_a-T_{a,Q},\qquad B_{a,1}=-\frac32c_a.}
\]

固定 \(Q\) 时，\(a\downarrow0\) 使 \(B^{(Q)}_{a,1}\to-1\)，真值却趋于零。这是可定位到单一端口的信息缺失。

### 截断成本的定量下界

对 \(0<a\le1\)、整数 \(Q\ge256\)，有

\[
\boxed{T_{a,Q}\ge\frac{Q^{-a}}{32\log2}.}
\]

证明如下。令 \(A(X)=\sum_{n\le X}\mu(n)^2\)。利用
\(\mu(n)^2=\sum_{d^2\mid n}\mu(d)\)，并取 \(m=\lfloor\sqrt X\rfloor\)，得到

\[
|A(X)-X/\zeta(2)|\le m+X/m\le2\sqrt X+1.
\]

由此在 \(Y\ge256\) 时，

\[
A(2Y)-A(Y)\ge\frac{Y}{\zeta(2)}-2(\sqrt2+1)\sqrt Y-2\ge Y/4.
\]

最后一个数值不等式可用 \(1/\zeta(2)>3/5\) 核对，之后左端相对 \(Y\) 的下界单调增加。
又有
\(\prod_{p\mid q}(p^{1+a}-1)<q^{1+a}\)，且 \(\zeta(1+a)\le1+1/a\)，故 \(c_a\ge a/2\)。按 dyadic 区间求和得

\[
\sum_{q>Q}\frac{\mu(q)^2}{q^{1+a}}
\ge\frac{Q^{-a}}{2^{3+a}(1-2^{-a})}
\ge\frac{Q^{-a}}{16a\log2}.
\]

乘以 \(c_a\ge a/2\) 即得结论。

因此无补偿的 sharp 截断能量
\(\mathcal D_a^{(Q)}=\sum_N(B^{(Q)}_{a,N})^2/N^2\)
若满足 \(\mathcal D_a^{(Q)}\le Ca\)，必有

\[
\boxed{
\log Q\ge\frac{\log(1/a)-\log(1024C\log^2 2)}{2a}
=\frac{\log(1/a)}{2a}-O_C(1/a).
}
\]

这个障碍并不否定 Fourier/Ramanujan 表示；它说明无补偿地舍弃大模数时，连第一个已知端口都会被破坏。为获得 \(O(a)\) 能量而盲目扩大模数窗口，成本会很高。

## 7. 精确补偿端口，形成更合适的后续目标

第一端口的缺失量可不经无限求和精确计算：

\[
T_{a,Q}=1-c_a\left[1+
\sum_{2\le q\le Q\atop q\text{ squarefree}}
\frac1{\prod_{p\mid q}(p^{1+a}-1)}\right].
\]

定义补偿模型

\[
\widetilde B^{(Q)}_{a,N}=B^{(Q)}_{a,N}+T_{a,Q}.
\]

这等价于向被截断的增量序列补回 \(N=1\) 处的确切缺失质量。因此
\(\widetilde B^{(Q)}_{a,1}=B_{a,1}\)；其余端口仍有明确残差：

\[
B_{a,N}-\widetilde B^{(Q)}_{a,N}
=c_a\sum_{q>Q}\beta_a(q)
\left[\sum_{n\le N}c_q(n)-\mu(q)\right].
\]

这是一项有真实来源的端口补偿，没有把其余频率尾项假设为零。

固定 \(Q\) 时，补偿模型还有精确表达

\[
\widetilde B^{(Q)}_{a,N}
=c_a\sum_{2\le q\le Q}\beta_a(q)
\left[\sum_{n\le N}c_q(n)-\mu(q)\right]-\tfrac32c_a.
\]

有限频率前缀有共同周期，故其所有 \(N\) 上有界，得到
\(\sum_N|\widetilde B^{(Q)}_{a,N}|^2/N^2=O_Q(a^2)\)。因此固定 \(Q\) 的归一化能量除以 \(a\) 趋于零；任何非零的 \(a\) 阶贡献若存在，只能来自增长的频率或尺度。这与项目的逃逸尺度现象相容。

一个清楚、保留相位和端口的**充分条件型任务**是：证明存在与 \(a,Q\) 无关的 \(C\)，使

\[
\sum_{N\ge1}\frac{|\widetilde B^{(Q)}_{a,N}|^2}{N^2}\le Ca
\]

在所需全部小 \(a\) 和一列 \(Q\to\infty\) 上成立。固定 \(a,N\) 的绝对收敛保证补偿模型趋于 \(B_{a,N}\)，随后 Fatou 给出 \(\mathcal D_a\le Ca\)。

这是充分条件，**没有证明其必要性，也没有证明该统一估计**。其意义在于将原先被平移平均删除的交叉相位和常数端口全部留在可计算 Gram 形式中。低频正平方分解可服务其中一部分；实际频率核的统一误差和剩余端口耦合是下一项真正的数学工作。

## 8. 有限周期实现与复算

对有限模数族，设共同周期 \(P=\operatorname{lcm}(q)\)。每个 \(q\ge2\) 的 Ramanujan 和在一周期内均值为零，所以累计前缀及 \(B^{(Q)}\)、\(\widetilde B^{(Q)}\) 都以 \(P\) 为周期。

若 \(f_r\) 是一个周期内的完整端口值，

\[
\boxed{
\sum_{N\ge1}\frac{f_N^2}{N^2}
=\frac1{P^2}\sum_{r=1}^P f_r^2\,\psi_1(r/P),
}
\]

其中 \(\psi_1(x)=\sum_{k\ge0}(k+x)^{-2}\)。该式保留固定起点；它是周期剩余类分组，不是平移平均。周期可能很大，因此它首先提供准确的小模型验证接口。

运行 `python3 verify_anchored_kernel.py`，依赖 `mpmath`。

程序实际检查：

- 完整复核显式式与 30,000 项直接累计比较，误差小于明确的尾界 \(4/(|1-e^{i\theta}||1-e^{i\phi}|M)\)；包含同频、异频及异号频率。
- 低频复极限在 \(\varepsilon=10^{-2},10^{-3},10^{-4}\) 的实虚部收敛；cos 配对与归一化相关。
- 有符号幅度的 min 核与累计正平方公式，以有理数作精确比较。
- 完整有限频率的两个正平方积分、对应精确 Gram 式、直接级数及完整能量的上下界。
- 模数 \(2,3,5,6\)、周期 30 的 Ramanujan 全 Gram、直接前缀及周期剩余类表达，以有理数作精确比较；删除非对角项确实改变结果。该通用模型示例选择 \(b=7/5\)，不称其为 \(a=1\) 的完整道路锚点。
- 周期无穷公式与 100,000 项直接和比较，使用非负尾部的明确误差界。
- \(a=1/2,1/4,1/10\)、\(Q=256\) 的正尾端口、下界及精确补偿。

复算用于检查推导和实现；一般恒等式与下界由以上证明支持。程序没有计算全部 RH 尾项，也未运行外部 175,187 模块 Lean 工程。

### 8.1 对真实道路系数的有限成本试算

`python3 probe_road_certificates.py` 将真实 \(c_a\beta_a(q)\) 按共轭频率合并，保留 \(q=2\) 的单个自共轭项，并使用 §7 的确切第一端口补偿。试算采用 50 位小数精度；它是有限模型的数值检查，不是区间认证或统一上界证明。

输出 `road_certificate_probe.json` 记录 \(a\in\{0.5,0.25,0.1,0.05\}\)、\(Q\in\{16,64,256\}\) 的 12 组结果。在 \(Q=256\) 时共有 7,034 个 cos 模式，正平方表达仍只需排序后的线性更新。

| a | Q | E_S/a | E_R/a | CS 上界 / a |
|---:|---:|---:|---:|---:|
| 0.5 | 256 | 0.0458513 | 1.1318555 | 1.6333255 |
| 0.25 | 256 | 0.1008620 | 1.3013195 | 2.1267607 |
| 0.1 | 256 | 0.2895892 | 1.4940151 | 3.0991279 |
| 0.05 | 256 | 0.3082987 | 1.1884998 | 2.7074397 |

同一 \(a\) 下增大 \(Q\) 时，分项能量并非都下降。例如 \(a=0.1\) 的 CS 上界除以 \(a\)，随 \(Q=16,64,256\) 分别为 1.37838、2.16012、3.09913。有限观察不能据此推出发散或有界；它明确说明应追踪模数增长的成本，必要时利用已保留的 \(X_{SR}\) 抵消，不能把一次小窗口的成功当作逃逸尾项的统一证书。

## 9. 来源

均为指定项目科学快照，文件状态按正本保留：

1. [正道路能量](https://github.com/awdawmip/enterprise-math/blob/9fc068244e4f1117f1e75df5eb0285c6697d21d7/research_notes/COMPOSITE_ROAD_RH_PURE_POSITIVE_ENERGY_20260906.md)，blob `962505f62c8b4a3367dc9a5dbc87865a094bd1f0`。
2. [离散 l2 与逃逸尺度](https://github.com/awdawmip/enterprise-math/blob/9fc068244e4f1117f1e75df5eb0285c6697d21d7/research_notes/COMPOSITE_ROAD_RH_DISCRETE_L2_NONCOMMUTATION_20260906.md)，blob `2c682f0d2f5c7a1bc161ce6bd33f59fa825efc17`。
3. [Ramanujan 相位相干](https://github.com/awdawmip/enterprise-math/blob/9fc068244e4f1117f1e75df5eb0285c6697d21d7/research_notes/COMPOSITE_ROAD_RH_RAMANUJAN_PHASE_COHERENCE_20260906.md)，blob `837b730839bca08bf0138db2e8ad7df226abb6fd`。
4. [Möbius Gram 与 Mellin 接口](https://github.com/awdawmip/enterprise-math/blob/9fc068244e4f1117f1e75df5eb0285c6697d21d7/research_notes/RH_MOBIUS_FLUX_RENYI_GRAM_HIERARCHY_20260908.md)，blob `be051767d010f295fc19d5a00acb4b84410cd06c`。

外部 theta/Parseval 证明的本次深读由协作中的另一支负责；本稿不把自行推导的核公式、截断成本或补偿模型归属给外部作者，也不宣称它们是未见于既有文献的新定理。
