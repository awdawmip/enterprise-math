# 两次欧拉通道记录如何分开来源混合、时钟抖动和校准偏移

**结论。** 在公开十二轮控制的一个实际轨道上，源可以先平移半个周期，读出时钟也可以跳过半个周期。单个未标时记录只能看到两种偏移的合成。对同一来源取两次三通道记录，若时钟和校准在两次读取时独立重抽，则两个复矩就能同时恢复未知的三通道校准分布和两个偏移概率，歧义恰为同时交换两个二元标签。纯来源、公平时钟或均匀校准时，任意次匿名重复都只给独立乘积律。若额外保留真实延迟标签，一次记录在更大的参数范围内就够。

本篇对应 2026-10-11 的 RR07。前置 RR02 与 RR04 的登记仍为 READY。本文把源的边界时刻和一次写入的有效参考门作为明示条件。第 78 轮研究了源与写门交错时出现超出两个端点的读数；此处在各自已确定的边界执行完整写门。第 50 轮的校准工作讨论已知相对偏移边际所容许的最优与最差记录；此处的校准分布本身未知，要从同一来源的联合读数识别。10 月 12 日的同号题另问反馈所需的闭环状态。[RR07 任务书](https://github.com/awdawmip/enterprise-math/blob/e7b9fb5084f93a9b2dbc16225629b667fb7bf46c/research_tasks/RS-EULER-RR-07-IDENTIFICATION-20261011.md) · [第 78 轮](../seventyeighth/aperture.md) · [第 50 轮](../fiftieth/calibration.md)

## 实际轨道给出两个可辨的半周期

按原顺序运行 $T=H03,U2,C$，取状态 $x=(j,s,F,w,\theta)=(0,0,010,0,0)$。从第 0 轮起，十二个实际通道依次是

$$
0,1,0,1,0,2,\quad 1,0,1,0,1,2 .
$$

源的受控核心满足 $T^6x=(1,1,010,0,0)$、$T^{12}x=x$。在一次独立准备的完整试验内选择一次 $S\sim\operatorname{Bernoulli}(\pi)$，使源起于 $T^{6S}x$。第 $i$ 次读出在名义边界 $12(i-1)$ 后再等 $6D_i$ 轮，其中 $D_i\sim\operatorname{Bernoulli}(\lambda)$。用一个新接收器执行公开的可逆门 $E(j,a_0,r)=(j,a_0,r+j-a_0)$，初始相对偏移 $B_i=r-a_0\in\mathbb Z/3$ 的分布为 $q$。假定各 $D_i,B_i$ 相互独立，也都独立于 $S$。这些是对试验的条件，各分支仍带完整正权。写门不改变原源核心，后续的 $T$ 不读已写接收器。由此得到确切的观测

$$
Y_i=(S\mathbin{\mathrm{xor}}D_i)+B_i\pmod 3 . \tag{1}
$$

同一试验中的来源 $S$ 始终不变。两个分别重抽来源的样本只有单读边际的乘积，不能替代式 (1) 的联合记录。原记载的第 12 轮返回作用于控制核心，来向、审计历史和经过的轮数仍各自保留。[原控制和轨道公式，§2](https://github.com/awdawmip/enterprise-math/blob/0b0f5d9df0e079d23746bf3334f7888cf661b641/research_notes/chatgpt_direct/20261010_EULER_PASSIVE_SAMPLING_AND_NOISE.md) · [参考门、校准与源保持，§§2–6](https://github.com/awdawmip/enterprise-math/blob/a6627d28d1e02f16ec5ca4d5118801c005cca583/research_notes/chatgpt_direct/20261011_EULER_RELATIONAL_RECORDING.md)

## 匿名双读的显式逆

令 $\omega^2+\omega+1=0$，取 $\omega$ 为原三通道的相位单位。设 $a=1-2\pi$、$b=1-2\lambda$、$Q=\sum_{j=0}^2 q_j\omega^j$、$A=(1-\omega)Q$。从相同世界中先取相位乘积再平均，得到两个复数

$$
M=\mathbb E\omega^{Y_1},\qquad
K=\mathbb E\omega^{Y_1+Y_2}-M^2 .
$$

给定 $S$，每次读数的条件相位均值为 $(1+\omega)Q/2+(-1)^S bA/2$。条件独立给出

$$
M=(1+\omega)Q/2+abA/2,\qquad
K=(1-a^2)b^2 A^2/4 . \tag{2}
$$

这是二元潜在来源的二阶矩分解。特有的可逆性来自三通道旋转。复平面中 $(1+\omega)Q$ 与 $A$ 实正交，因为 $(1+\omega)(1-\overline\omega)$ 是纯虚数。$K\ne0$ 时，$(K/|K|)\overline z$ 正是沿 $A$ 的实直线反射 $z$。于是

$$
\begin{aligned}
Q&=\frac{M-(K/|K|)\overline M}{1+\omega},&
q_j&=\frac{1+2\Re(Q\omega^{-j})}{3},\\
t&=\frac{2\Re(M\overline A)}{|A|^2}=ab,&
b^2&=t^2+\frac{4|K|}{|A|^2}.
\end{aligned} \tag{3}
$$

正方根确定 $b\ge0$ 的解，$a=t/b$；若不指定 $\lambda<1/2$，另一解是 $(-a,-b)$。它把两种来源的两个条件律及其权重同时对换，给出相同的任意阶联合律。式 (3) 已穷尽全部解。另有 $|K|=\mathbb E\omega^{Y_1-Y_2}-|M|^2$，右边是模型内实非负的配对读数；有理输入的复算可始终留在 $\mathbb Q(\omega)$。

* $K=0$ 当且仅当 $q$ 均匀、$\lambda=1/2$ 或 $\pi\in\{0,1\}$。这些情形每个长度的联合律都是单读边际的乘积。给定该边际，退化参数纤维就是上述三种条件与式 (2) 的第一式的交，增加匿名重复次数不会再缩小它。
* 一次未标时读数尚有连续歧义。固定 $q=(1/2,1/3,1/6)$，取 $(\pi,\lambda)=(1/4,1/4)$ 或 $(3/8,0)$，均有 $ab=1/4$ 和 $M=7/48+\omega/6$，三通道边际完全相同。两组均不退化，$K$ 分别是 $3/256$ 和 $15/256$。一般在概率均位于内点且 $ab\ne0$ 时，变动 $a,b$ 并保持 $ab$ 固定也给同一边际。因此匿名协议所需读取次数在该族中确为二。

## 一次读数再保留一个标签

若有独立的事件记录告诉我们该次的真实 $D$，在 $0<\lambda<1$ 时可求两个条件均值 $L_d=\mathbb E[\omega^Y\mid D=d]$。两者满足 $L_0+L_1=(1+\omega)Q$，$L_0-L_1=a(1-\omega)Q$。因此 $Q\ne0$ 时一份带标记的联合分布就恢复 $q,\pi,\lambda$，其中 $\lambda=\Pr(D=1)$。这也处理公平时钟和纯来源，且消除了方向交换。这里“一次”表示每个独立准备只写一次，估计联合律仍须多次准备。

源相关时钟会改变这个结论。令 $S$ 公平且 $D=S$，取 $q=(2/5,3/10,3/10)$。另令 $S,D$ 独立且均公平，取 $q'=(2/5,1/5,2/5)$。二者对 $D=0,1$ 的两行联合质量均为 $(1/5,3/20,3/20)$。故仅凭一次被动的真实时间标签仍不能验证时钟独立。如果不记录延迟，持久的随机钟偏也有全阶歧义：每次精确读取同一随机半周期预移的源，和在未移的源上始终使用同一个随机半周期钟偏，给出所有写入的相同联合律。两种构造就在 (1) 中互换共同随机比特。原窗口等式给出了均值层面的同一问题。[时间窗口与状态相关采样，§§6–7](https://github.com/awdawmip/enterprise-math/blob/82bd71cfa6d530a5f421b82a964f369efa9c30cd/research_notes/chatgpt_direct/20261010_EULER_TEMPORAL_APERTURE_AND_IDENTIFIABILITY.md)

## 对照：固定源通道上的三次重写

另一个明确的实验可去掉源只有半周期两种选择的条件。固定源通道 $J$，其三通道分布任意；在该通道保持期间，用三份独立且同分布的新接收器各写一次，得到 $Y_i=J+B_i\pmod3$。这次没有时钟抖动。令 $U_0=\mathbb E\omega^J$，$Q=\mathbb E\omega^{B_i}$。则一阶读数 $M=U_0Q$，两种配对读数 $T=\mathbb E\omega^{Y_1+Y_2}=\overline{U_0}Q^2$、$H=\mathbb E\omega^{Y_1-Y_2}=|Q|^2$。若 $M\ne0$，已有 $Q^3=TH/\overline M$。三个立方根正对应把源和偏移向相反方向循环改标，给出同一联合律；$U_0=M/Q$ 随即确定。若 $U_0=0$、$Q\ne0$，两次读数仅决定 $|Q|^2$，第三次给出 $\mathbb E\omega^{Y_1+Y_2+Y_3}=Q^3$。例如在均匀源上，$(1/2,1/3,1/6)$ 与 $(1/2,1/6,1/3)$ 的二读分布相同，三读可辨，两者也不互为循环平移。若 $Q=0$，任意数量接收器的记录均为独立均匀。用三阶循环矩消去公共平移是多参考对齐中已有的思想；这里的二读与三读门槛来自参考门在 $\mathbb Z/3$ 上的条件加法合同。[Bendory 等，Bispectrum Inversion With Application to Multireference Alignment](https://doi.org/10.1109/TSP.2017.2775591)

## 时钟选择与真正读后反馈

另作一个控制试验，用已知 $x$ 在第 0 轮记录并随机分臂。对照臂保持；试验臂以概率 $\eta$ 施加原 $B=U_1^2$，否则保持。分臂和选择独立于时钟、校准与来源。$B$ 在核心上只反转探针片向，不改当前通道。两臂均在确定的一轮 $T$ 后用同一校准律 $q$ 记录。对 $x$，保持给通道 1，施加 $B$ 给通道 2。若 $U$ 表示通道轮换，两臂记录律为 $Uq$ 和 $(1-\eta)Uq+\eta U^2q$，总变差恰为 $\eta\,\mathrm{TV}(q,Uq)$。当 $q$ 非均匀且已知或已由前述协议确定时，此差识别 $\eta$。上述有理 $q$ 给系数 $1/3$。若时钟可以根据分臂选择，第 5 轮的未反馈通道本来就是 2，随机改读第 5 轮就可精确复制此次两个输出；独立定时或可信事件标签在这里确实承担辨别作用。这个控制比较只检验指定的 $B$ 与保持规则。[原读后操作和两圈反转，§§1–2](https://github.com/awdawmip/enterprise-math/blob/e7b9fb5084f93a9b2dbc16225629b667fb7bf46c/research_notes/chatgpt_direct/20261011_EULER_READOUT_BACKACTION.md)

## 取样误差与复算

对 $n$ 份独立的同源双读试验，分别平均 $\omega^{Y_1}$ 与 $\omega^{Y_1+Y_2}$，得到 $\widehat M,\widehat T$。以概率至少 $1-\delta$，两估计的复误差都至多 $e=2\sqrt{\log(8/\delta)/n}$；这是对四个 $[-1,1]$ 值实分量分别用 Hoeffding 不等式并取并集。于是 $|\widehat K-K|\le3e$。若已知 $|K|\ge c>3e$，代入式 (3) 有 $|\widehat Q-Q|\le 2e+6e/c$，故各 $q_j$ 的绝对误差至多该上界的 $2/3$。这里使用 $|1+\omega|=1$ 和非零复数归一方向的不等式 $|z'/|z'|-z/|z||\le2|z'-z|/|z|$。靠近退化集时，还可直接保留满足 $|M-\widehat M|\le e$、$|K+M^2-\widehat T|\le e$ 的整组合法参数作为同置信水平的集合。

程序逐门重算公开的源核心公式，对分母 6 的全部 $q$ 及 $\pi,\lambda\in\{0,1/6,\ldots,1\}$ 复核了 1,372 个有理模型，其中 810 个匿名可逆，562 个退化，945 个满足单次带标逆的条件。固定源对照另逐项展开 784 个有理源与偏移分布组合的三读联合律，核验循环改标的精确歧义。四组算例真实调用固定版本的正权 CWM 串接与汇合，分别保留 72、18、72、36 条联合路径，质量均为 1。各复观察在有理 Eisenstein 系数中计算。复算沿公开的商状态、边界写门和正权源码进行；原会话 ZIP 的逐原语重放及记录器的物理实现各有独立的证据要求。

在仓库检出上运行 <code>python euler_check.py --repo /path/to/enterprise-math | cmp - euler_checked.json</code>。程序验证八个固定源文件的 Git blob。[复算程序](euler_check.py) · [整数与有理证据](euler_checked.json) · [公开正权内核](https://github.com/awdawmip/enterprise-math/blob/a6627d28d1e02f16ec5ca4d5118801c005cca583/src/enterprise_math/brc_weighted.py)
