# common-depth 双侧首返尾律：独立分析审计

状态：`ANCHOR_EXPOSED / INDEPENDENT_ANALYTIC_AUDIT_PASS / NOT_FORMAL_V2`。

辅助工作包 `/root/exact_solver`，2026-09-07；此前未参与该首返证明。只读作者报告、其小检查源码及必要一手来源，不重跑大型枚举，不改作者源、remote、中央 catalog 或 canonical。

## 1. 审计结论与来源绑定

对完整 signed X6、十二个 primitive signed 步各权 `1/12`、首次正时间命中完整对角 fiber `ZD` 的合同，作者结论成立：

\[
F(h)=\mathbb P(\tau<\infty,H=h)
=\frac{1}{12\pi^3S^2}|h|^{-4}+o(|h|^{-4}),\qquad |h|\to\infty,
\]

其中 `S=sum_h G_Z6(hD)`，`1<S<infinity`。无须添加半线支撑、条件首返归一化或额外周期系数。未发现阻断问题。

绑定的作者报告 `research_notes/OWNER_COMMON_DEPTH_FIRST_RETURN_20260907.md` SHA-256：`60c0dd61326e6dc781a757e4f02511fc1af8bc606a7a2ab440228bdde1feda6d`。已读小检查源码 SHA-256：`ca169914e24600a1f2ee1f004f0db6ba14f205faeebe53e310edb2a140f7b56b`；本审计不把作者有限检查当成渐近证明。

外部依赖：[Lawler–Limic，作者原稿](https://www.math.uchicago.edu/~lawler/srwbook.pdf)，Theorem 4.3.1 及印刷 pp.81–83。web 读取超时后，读取作者已从同 URL 缓存的 PDF，实际本地 SHA-256 为 `cb10ab9e665913f5041fd12511c2492c41d3e4bbebcf2d6ba7162c78acfbd9ea`，大小 1826510 字节；以 pypdf 读取页面索引 80、81、82，与印刷页一致。网络超时不承担任何数学推理。

## 2. Green 常数、周期及相对积分

原稿定理给对称有限范围步行的 `O(|x|^{-d})` Green 余项；p.82 直接列出简单随机步行系数

\[
\frac{d\Gamma(d/2)}{(d-2)\pi^{d/2}}|x|^{2-d}.
\]

同页明确把二分周期情形归入证明。p.83 还说明更弱非对称假设可能只给较弱余项；本题正负对称的简单步律没有这种缺口。

取 d=6 得 `3/pi^3`。沿 `x=hD` 有 `|x|²=6h²`，故主系数变为 `(3/pi³)/36=1/(12pi³)`，余项变为 `O(|h|^{-6})`。这只是对声明的分量平方读数与概率步律进行经典分析，不改变原生正角或 P000。

时间上只在偶数步能到 hD，因为其坐标和 `6h` 为偶数；但 Green 已对全部时间求和且已处理二分周期，不能再乘 2。深度 h 不限于偶数：对任意 h>0，词 `E1^h ... E6^h` 的真前缀均不在 ZD，而终点为 hD；负 h 用全部反向词。于是所有非零整数 h 均有正首次质量，h=0 也由两步反向词有正首次质量。

相对编码 `Y=(Z1-Z6,...,Z5-Z6)` 的特征函数正确：

\[
\phi_Y(\theta)=\frac16\left(\sum_{i=1}^5\cos\theta_i+
\cos\sum_{i=1}^5\theta_i\right).
\]

`phi_Y=1` 只在原点模 `2pi` 出现，因为六个余弦都必须达到 1。其原点二次项为 `(sum theta_i²+(sum theta_i)²)/12`，非退化；所以 `(1-phi_Y)^-1=O(|theta|^-2)` 在五个辅助变量中局部可积。时间周期的 `phi_Y=-1` 点并不是该 Green 分母的奇点。

作者积分 (S) 的 Abel 极限也有明确控制：`phi>=0` 时 `1/(1-r phi)<=1/(1-phi)`；`phi<0` 时被积函数不超过 1。因此可用 `1+(1-phi)^-1` 支配并取 `r↑1`。辅助积分不丢弃真正 H，也没有把原生空间改称五维。

## 3. 双侧更新与无零性

首次命中 `kD` 后，完整原生位移重启到 `hD` 的剩余端点差是 `(h-k)D`，所以卷积指标必须允许 k 和 h-k 任意正负。作者有限时间更新式保持了这个差，排除了零长 excursion，也没有排除首次深度为 0 的原子。

所有概率项非负，先在有限时间分解，再用 Tonelli 求和没有交换条件缺口。沿线 Green 的 `h^-4` 主项及每个有限点的瞬态 Green 有限性给 `U in l1(Z)`，总质量 S 有限。由

`U=delta0+F*U`

得到 `S=1+pS`，所以 `p=Pr(tau<infinity)=1-1/S<1`。最短反向词保证 p>0。余项 `F^{*m}*U` 的 l1 范数为 `p^mS`，故作者的完整几何卷积展开也成立。

采用 `hat a(theta)=sum_h a(h)e^{ih theta}`，更新给

`hat U=(1-hat F)^-1`。

因为 `|hat F|<=p<1`，整圆上没有零或漏掉的奇点。反转所有 signed 步使 U、F 实偶，所以 `hat F` 实，`hat U` 实且严格正，且 `hat U(0)=S`。这一无零性来自已证缺陷更新，不是由 Green 渐近单独推断。

## 4. Fourier 倒数引理的符号与正则性

作者模板

\[
K(\theta)=\frac{\pi^4}{45}-\frac{\pi^2\theta^2}{6}
+\frac{\pi|\theta|^3}{6}-\frac{\theta^4}{24}
\]

的平均为零。独立求导得到以下接缝值：

| 阶数 j | `K^(j)(-pi)=K^(j)(pi)` |
|---|---|
| 0 | `-7pi^4/360` |
| 1 | 0 |
| 2 | `pi²/6` |
| 3 | 0 |
| 4（普通导数） | -1 |

原点零至二阶导数连续，而 `K'''(0-)=−pi`、`K'''(0+)=pi`。在圆周分布意义下，恰有

\[
D^4K=-1+2\pi\delta_0.
\]

**跳跃项的符号是正号**：三阶导的右值减左值为 `+2pi`。±pi 没有额外 delta。Fourier 系数按积分 `e^{-ih theta}` 读取，四阶导数的乘子为 `(ih)^4=h^4`，因此非零 h 的 K 系数为 `h^-4`。普通常数项 −1 只影响零模，与 delta 的零模抵消；不会再贡献一个 h 非零项。

设 `a(h)=c|h|^-4+e(h)`。本题 `e(h)=O(|h|^-6)` 确实推出

`sum_{h!=0}|h|^4|e(h)|<infinity`。

因此 `E(theta)=a(0)+sum_{h!=0}e(h)e^{ih theta}` 的零至四阶导数级数都一致绝对收敛，E 是周期 C4 函数。**不是**把只有 `a(h)~c|h|^-4` 的较弱假设当成这个结论。于是 `hat a=cK+E` 为 C2、原点两侧为 C4，只有三阶跳跃 `2pi c`。

对 `V=1/hat a`，圆周无零与紧致性使分母有正的模下界。直接链式求导：

\[
V'''=-\frac{\widehat a'''}{\widehat a^2}
+\frac{6\widehat a'\widehat a''}{\widehat a^3}
-\frac{6(\widehat a')^3}{\widehat a^4}.
\]

后两项在原点连续，故其唯一三阶跳跃为

\[
J=V'''(0+)-V'''(0-)=-\frac{2\pi c}{A^2},\qquad A=\widehat a(0).
\]

V 的接缝导数继续匹配。两侧普通四阶导数形成有界分段连续函数 g，故 `g in L1`。于是

\[
D^4V=g+J\delta_0,\qquad
h^4v(h)=\widehat g_{\rm coeff}(h)+\frac{J}{2\pi}.
\]

Riemann–Lebesgue 使 g 的系数沿 h→正无穷和负无穷均趋零，从而

`v(h)=−c A^-2 |h|^-4+o(|h|^-4)`。

这里偶数阶乘子保证负 h 不产生额外符号；没有在积分接缝忽略边界项。该衰减还直接给 v 属于 l1，不需要先使用 Wiener 逆定理或半线更新定理。

## 5. 应用与原词观察的范围

对 `a=U`，上一节的 A=S、`c=1/(12pi³)`，且

`V=1/hat U=1-hat F`。

所以 h!=0 时 `v(h)=−F(h)`。倒数的负主项再取负，恰得到正系数 `c/S²`，没有符号错误。若改为条件于首次事件发生的 H 分布，还需除以 `p=1-1/S`；作者主结论是未条件化版本，二者没有混用。

固定 n,h 的原 BRC word histogram 为 `a_n(h)[12^-n]`。F 已先取质量再跨长度求和，既不保存长度，也不保存原词身份和各个词权，不能把它升级为原有限 WeightHistogram 的等价替代。

最小系数的独立解析核对为：两步到相对零只能是十二种反向词，故 `f_2(0)=12/12²=1/12`；六步到 +D 只能每个正轴各走一次，720 个词均无较早相对返回，故 `f_6(1)=720/12^6=5/20736`。负 D 同理。这解释了为何这里可用原 `endpoint_multiplicity`，而一般时间不能把访问系数直接当首次系数。

## 6. 审计范围

本次直接核验纯分析链及一手 Green 定理，不运行作者的尾拟合、大 horizon DP 或旧步行枚举，也不新增这类程序。有限代数检查源码可支持模板的局部恒等式，不能代替无穷渐近、Tonelli 或 Riemann–Lebesgue 的适用条件；本审计逐项给出了这些条件。

在作者完整合同下，指定双侧逐点渐近可接受为本地数学结果。它不是 S 的数值区间证书、不是有效余项常数，也不自动覆盖其他步律、其他命中子格、较弱 Green 余项或完整微观 BRC 观察。无作者源修改请求。

Global-Knowledge-Sync: main@4fa7d7d / GLOBAL_KNOWLEDGE_V1
