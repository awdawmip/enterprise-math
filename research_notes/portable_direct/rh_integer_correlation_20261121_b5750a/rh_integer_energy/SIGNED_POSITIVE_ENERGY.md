# 完整道路的整数正部能量：带符号源工作、真实边界与非负接触项

Date: 2026-11-21
Contribution: EM-DIRECT-B5750A 原母任务内的作者协作，unshared 数学推进；不是独立 Project Review。
Status: AUTHOR_PROVED_SIGNED_WORK_IDENTITIES_AND_FINITE_COMPARISONS
Scientific input: enterprise-math@9fc068244e4f1117f1e75df5eb0285c6697d21d7。
Previous continuation: cc8e2eec9e281ac2649341ec44a270c49bed6d38，`riemann_adaptive_window_20261121/`。

本稿把上一轮的精确整数递推接到正部平方和。新增接口是一个具有明确正系数 \(\theta(1-\theta)\) 的能量恒等式：目标正部平方和、归一化梯度、接触交叉项和微小离散修正之和，等于**带符号源项做功与真实端点通量之和**。普通离散分部求和、正部乘子及正函数变换不主张为新的通用分析工具；研究增量是完整道路实例的精确常数、全部端点/接触项、连续对应式及实际算术分解。

研究对象仍是 P000/X6 上的已声明算术标量读出；函数空间中的能量变换不增加原生空间轴。所有整数、合数层、早期道路和原点端口保留。以下有限恒等式不是 RH 证明，也没有把既有 RH 等价的 \(\mathcal Q_a=O(a)\) 改写成已经获得的弱假设。

## 1. 原始观察量与固定前史

在一个窗口内固定任意有限正厚度族和实权重，\(a_j>0\)、\(\sum_j\nu_j=1\)。沿用完整道路

\[
R_a(n)=\prod_{p\mid n}(1-p^{-a}),\qquad R_a(1)=1,
\]

\[
D_n=\sum_j\nu_jR_{a_j}(n)/a_j\quad(n\ge2),\qquad D_1=0,
\]

\[
\mathscr G(y)=\sum_{2\le n\le y}D_n(y/n-1)-y\log y+(1+\gamma)y,
\qquad q_n=\mathscr G(n).
\]

\(D_1=0\) 是已有零节点/原点修正，不可换成未经修正的 \(\sum\nu_j/a_j\)。前轮证明给出

\[
\Delta^2q_n=q_{n+1}-2q_n+q_{n-1}=\frac{D_n-\kappa_n}{n},\qquad n\ge2,
\tag{1}
\]

\[
\kappa_n=n[(n+1)\log(n+1)-2n\log n+(n-1)\log(n-1)],
\]

\[
1+\frac1{6n^2}\le\kappa_n\le1+\frac1{6(n^2-1)}.
\tag{2}
\]

固定初值为

\[
q_1=1+\gamma,\qquad q_2=2(1+\gamma-\log2).
\]

本稿在窗口左端不重新归零。实际 \(q_A,q_{A+1}\) 包含从原点到 \(A\) 的完整前史。

## 2. 精确离散正部能量恒等式

取整数 \(2\le A<B\)、\(B\ge A+2\)，固定 \(0<\theta<1\)。记

\[
u_n=(q_n)_+,\quad v_n=(q_n)_-,\quad
\omega_n=n^{1-2\theta},\quad r_n=n^\theta,\quad
c_n=\frac{\omega_n+\omega_{n+1}}2,
\quad z_n=u_n/r_n.
\]

这里 \(v_n\ge0\)，且 \(q_n=u_n-v_n\)、\(u_nv_n=0\)。定义内部目标平方和

\[
S^\circ_{A,B}=\sum_{n=A+1}^{B-1}\frac{u_n^2}{n^{2\theta+1}},
\tag{3}
\]

以及**带符号源工作**

\[
\boxed{\mathcal H_{A,B}=
\sum_{n=A+1}^{B-1}(\kappa_n-D_n)\frac{u_n}{n^{2\theta}}.}
\tag{4}
\]

源工作不是 \(\sum|\kappa_n-D_n|\) 或其正部；\(u_n\) 与完整源序列的相关性在此保留。

定义三个非负量

\[
\mathcal D_{A,B}=
\sum_{n=A}^{B-1}c_nr_nr_{n+1}(z_{n+1}-z_n)^2,
\tag{5}
\]

\[
\mathcal K_{A,B}=
\sum_{n=A}^{B-1}
\bigl(\omega_{n+1}u_{n+1}v_n+\omega_nu_nv_{n+1}\bigr),
\tag{6}
\]

\[
\mathcal R_{A,B}=
\sum_{n=A+1}^{B-1}
[\Gamma_\theta(n)-\theta(1-\theta)]\frac{u_n^2}{n^{2\theta+1}},
\tag{7}
\]

其中精确离散系数为

\[
\boxed{
\Gamma_\theta(n)=n^2\left\{2-\frac12\left[
(1+1/n)^\theta+(1-1/n)^\theta
+(1+1/n)^{1-\theta}+(1-1/n)^{1-\theta}
\right]\right\}.
}
\tag{8}
\]

真实边界项为

\[
\boxed{
\begin{aligned}
\mathcal B_{A,B}={}&
c_A\frac{r_{A+1}}{r_A}u_A^2-\omega_Au_Aq_{A+1}\\
&+c_{B-1}\frac{r_{B-1}}{r_B}u_B^2-\omega_Bu_Bq_{B-1}.
\end{aligned}}
\tag{9}
\]

\(\mathcal B\) 可以为正或负，不应先替换为绝对值；两端 \(q\) 及相邻节点均为真实值。

### 定理 1：带源正部能量

有精确恒等式

\[
\boxed{
\theta(1-\theta)S^\circ_{A,B}
+\mathcal D_{A,B}+\mathcal K_{A,B}+\mathcal R_{A,B}
=\mathcal H_{A,B}+\mathcal B_{A,B}.
}
\tag{10}
\]

并且，对所有 \(n\ge2\)，

\[
\boxed{
\theta(1-\theta)\le\Gamma_\theta(n)
\le\theta(1-\theta)\left(1+\frac1{2(n^2-1)}\right).
}
\tag{11}
\]

从而

\[
\boxed{
S^\circ_{A,B}\le
\frac{\mathcal H_{A,B}+\mathcal B_{A,B}}{\theta(1-\theta)}.
}
\tag{12}
\]

右边对真实递推数据自动非负。若两端 \(q_A,q_B\le0\)，边界项为零；不能为使用这一特例而改变窗口端点值。

### 2.1 正部乘子保留下来的接触项

在一条边上直接展开，利用 \(u_nv_n=0\)，得到

\[
\begin{aligned}
\Delta(\omega u)_n\Delta q_n
={}&c_n(\Delta u_n)^2
+\tfrac12\Delta\omega_n\,\Delta(u^2)_n\\
&+\omega_{n+1}u_{n+1}v_n+\omega_nu_nv_{n+1}.
\end{aligned}
\tag{13}
\]

最后两项恰在端点异号的边上出现。直接把 \(\Delta q\) 替成 \(\Delta u\) 会漏掉它们；本稿将其完整保留为 \(\mathcal K\)。

### 2.2 分部求和与正函数变换

由 (1) 和有限分部求和，

\[
\mathcal H
=\sum_{n=A}^{B-1}\Delta(\omega u)_n\Delta q_n
-\omega_Bu_B(q_B-q_{B-1})
+\omega_Au_A(q_{A+1}-q_A).
\tag{14}
\]

对 (13) 的第二项再分部求和；对第一项使用逐边恒等式

\[
c_n(\Delta u_n)^2
=c_nr_nr_{n+1}(\Delta z_n)^2
+c_n\Delta r_n\left(\frac{u_{n+1}^2}{r_{n+1}}-
\frac{u_n^2}{r_n}\right).
\tag{15}
\]

合并后，内部 \(u_n^2\) 的系数恰为

\[
2\omega_n-
\frac{c_{n-1}r_{n-1}+c_nr_{n+1}}{r_n}
=\frac{\Gamma_\theta(n)}{n^{2\theta+1}}.
\tag{16}
\]

全部边界余项化简为 (9)。例如右端通量的另一种写法是

\[
\omega_Bu_B(q_B-q_{B-1})
-\left[\tfrac12\Delta\omega_{B-1}
+c_{B-1}\frac{\Delta r_{B-1}}{r_B}\right]u_B^2,
\]

因为 \(u_Bq_B=u_B^2\)，它与 (9) 的右端部分相等。左端同理。这证明精确恒等式。

### 2.3 正系数的证明

对 \(0<\theta<1\)，偶次二项式系数满足

\[
a_k=-\binom\theta{2k}-\binom{1-\theta}{2k}>0,
\qquad a_1=\theta(1-\theta).
\]

绝对收敛级数给出

\[
\Gamma_\theta(n)=\sum_{k=1}^\infty a_kn^{2-2k}.
\]

此外

\[
-\binom\theta{2k}
=\frac{\theta(1-\theta)}{(2k)!}
\prod_{j=2}^{2k-1}(j-\theta)
\le\frac{\theta(1-\theta)}{2k},
\]

另一项同理，所以 \(a_k\le\theta(1-\theta)/k\)。对 \(k\ge2\) 使用 \(1/k\le1/2\) 并求几何级数，得到 (11)，从而 \(\mathcal R\ge0\)。也有

\[
\Gamma_\theta(n)=\theta(1-\theta)
\left[1+\frac{\theta^2-\theta+4}{12n^2}+O_\theta(n^{-4})\right],
\]

但主恒等式和上界并不依赖此渐近式。□

## 3. 连续窗口中的完全对应式

原始完整道路函数在每个开整数格上满足

\[
\mathscr G''(y)=-1/y,
\]

并在整数 \(n\) 处有导数跳跃 \(D_n/n\)。因此在分布/有限测度意义下

\[
d\mathscr G'(y)=-dy/y+\sum_n(D_n/n)\,\delta_n(dy).
\tag{17}
\]

取任意实窗口 \(1<Y<Z\)，记 \(u(y)=\mathscr G(y)_+\)、\(z(y)=y^{-\theta}u(y)\)，以及

\[
E_+=\int_Y^Z u(y)^2y^{-2\theta-1}\,dy.
\]

定义真实连续源工作

\[
\boxed{
\mathcal H_c=
\int_Y^Z y^{-2\theta}u(y)\,dy
-\sum_{Y<n<Z}D_n n^{-2\theta}u(n),
}
\tag{18}
\]

真实连续端点通量

\[
\boxed{
\mathcal B_c=
\left[y^{1-2\theta}u(y)\mathscr G'(y)
-\tfrac12y^{-2\theta}u(y)^2\right]_{Y+}^{Z-}.
}
\tag{19}
\]

端点为整数时，左端取右导数、右端取左导数，(18) 的原子只取开区间内整数；这避免重复或遗漏端点原子。

### 定理 2：连续正部乘子

\[
\boxed{
\theta(1-\theta)E_+
+\int_Y^Z y|z'(y)|^2\,dy
=\mathcal H_c+\mathcal B_c.
}
\tag{20}
\]

证明：\(u\) 连续且分段绝对连续，几乎处处有 \(u'=\mathbf1_{\mathscr G>0}\mathscr G'\)。将 (17) 乘 \(-y^{1-2\theta}u\) 后分部积分，使用

\[
\int_Y^Z y^{1-2\theta}(u')^2\,dy
-\theta(2\theta-1)E_+
=\int_Y^Z y|z'|^2\,dy
+\theta(1-\theta)E_+
+\theta[z^2]_Y^Z.
\]

与其余端点项合并，恰得 (19)–(20)。在真实零点上 \(u=0\)，正部截断的接触测度乘子为零；跨零点的变化仍完整计入梯度能量。离散版本的 \(\mathcal K\) 则保留节点异号边的精确额外成本，不能从离散式中删除。□

这条恒等式可以直接复用上一轮正部区间。令格内

\[
\mathscr G(y)=y(A_N-\log y)-P_N,
\]

则在真实正区间内

\[
z'(y)=y^{-\theta}\left[(1-\theta)(A_N-\log y)-1
+\theta P_N/y\right].
\tag{21}
\]

因此新的梯度积分仍由上一轮同一组对数幂原函数直接求得。\(A_N,P_N\) 仍累计全部早期道路。

## 4. 可检查的充分条件，以及它仍缺少的算术信息

### 4.1 一个带明确常数的窗口充分条件

对每个匹配窗口 \(Z=Y^\lambda\)，取 \(A=\lceil Y\rceil\)、\(B=\lfloor Z\rfloor\)，并使用该窗口真实厚度族。如果

\[
\forall\alpha>0\ \forall Y_0\ \exists Y\ge Y_0:
\quad\mathcal H_{A,B}+\mathcal B_{A,B}\le Y^\alpha,
\tag{22}
\]

则由 (12)，内部正部平方和满足同一类任意远窗口次幂条件。

在前轮的匹配误差接口，或统一有界的权重绝对和条件下，两个被分离出来的端点平方项具有已有显式次幂上界。以 \(\sum|\nu_j|\le3\) 为例，

\[
q_n^+\le n[2(\log n)^2+2],
\]

故对固定 \(\theta\ge1/2\)，端点成本不超过

\[
A^{1-2\theta}[2(\log A)^2+2]^2
+B^{1-2\theta}[2(\log B)^2+2]^2.
\]

结合上一轮已经证明的整数/连续窗口等价及匹配桥，可把 (22) 接到既有外部零点接口。吸收固定常数时使用较小目标指数即可。

**(22) 目前是可检查的充分条件，并未证明；不主张它与目标正部条件等价。** 恒等式还含有非负梯度和接触成本，因此源工作上界可能明显强于只控制正部平方和。数值部分实际显示了这部分余量。

### 4.2 为什么当前点态粗界仍不足以完成这条估计

定义

\[
L^2=\sum_{n=A+1}^{B-1}(\kappa_n-D_n)_+^2n^{1-2\theta}.
\]

若先丢掉源工作中的有利负项再用 Cauchy，则

\[
\mathcal H\le L\sqrt{S^\circ},\qquad
\theta(1-\theta)S^\circ\le L\sqrt{S^\circ}+\mathcal B.
\]

例如可得到保守上界

\[
\boxed{
S^\circ\le
\left[
\frac{L+\sqrt{L^2+4\theta(1-\theta)\mathcal B_+}}
{2\theta(1-\theta)}
\right]^2.
}
\tag{23}
\]

在已证明的匹配 \(|D_n-\Lambda(n)|\le1/2\) 下，\((\kappa_n-D_n)_+<2\)。于是即使暂取零边界，(23) 的这条粗推导也只产出

\[
S^\circ\ll_\theta\sum_{n=A+1}^{B-1}n^{1-2\theta}
\ll_\theta B^{2-2\theta}.
\tag{24}
\]

仅用 \(\sum|\nu_j|\le3\) 的道路点态界，则多出至多对数平方成本。这里说明的是**当前点态加 Cauchy 估计的损耗**，不是道路界不可能、所有局部方法不可能，或一个任意残差构造能够反驳真实道路。

真正未被点态控制触及的是

\[
\sum_n D_n\frac{q_n^+}{n^{2\theta}}
\quad\text{与}\quad
\sum_n\kappa_n\frac{q_n^+}{n^{2\theta}}
\]

之间的带符号算术相关，并且还要保留实际 \(\mathcal B\)。\(q_n^+\) 由原点以来的全部道路共同生成，不是与 \(D_n\) 独立的固定权。仅知道某个因子层的系数符号，也尚未控制它在这个相关配对中的大小。

## 5. 三个真实匹配窗口的新能量分解

采用上轮已完成的三个 \(Y=1000\)、\(Z=Y^{3/2}\) 窗口：二阶匹配、11 节点切比雪夫、以及 \(\theta=.9\) 的一阶匹配。前两者 \(\theta=.6\)。切比雪夫样本仍明确采用旧直接误差桥的 \(A_{\max}=1/2\)，不是另一个 \(A_{\max}\le1/8\) 复背景界的数值验证。

前轮记录的真实正部区间、连续 \(E_+\) 和一阶正部矩直接复用在 `prior_window_readouts.json`。本轮仅重新生成全部有限道路来计算**新的**离散源工作、端点、梯度、接触项及连续梯度对应式，没有重跑旧正部窗口套件。

### 5.1 离散恒等式的实际拆分

全部数字均保留真实符号；表中节录便于比较。

| 量 | 二阶，\(\theta=.6\) | 切比雪夫 11，\(\theta=.6\) | 一阶，\(\theta=.9\) |
|---|---:|---:|---:|
| \(S^\circ\) | \(7.26956985\times10^{-4}\) | \(7.42900768\times10^{-4}\) | \(6.47099414\times10^{-7}\) |
| 背景配对 \(\sum\kappa_nu_n/n^{2\theta}\) | 1.1355852900 | 1.1702552256 | 0.001045503681 |
| 道路配对 \(\sum D_nu_n/n^{2\theta}\) | 1.1060874218 | 1.1406307692 | 0.000959692714 |
| 净源工作 \(\mathcal H\) | 0.02949786823 | 0.02962445641 | 0.000085810967 |
| 实际边界 \(\mathcal B\) | 0.001013025092 | 0.000963020491 | 0.000008649848 |
| \(\theta(1-\theta)S^\circ\) | 0.000174469676 | 0.000178296184 | 0.000000058239 |
| 归一化梯度 \(\mathcal D\) | 0.03033626766 | 0.03040910241 | 0.000094289960 |
| 接触成本 \(\mathcal K\) | \(1.55969724\times10^{-7}\) | \(7.82834682\times10^{-8}\) | \(1.12616032\times10^{-7}\) |
| 离散修正 \(\mathcal R\) | \(2.00528089\times10^{-11}\) | \(2.02324679\times10^{-11}\) | \(1.33254148\times10^{-14}\) |

这三个样本的 (10) 浮点残差分别小于 \(8\times10^{-78}\)、\(2\times10^{-77}\)、\(2\times10^{-80}\)。连续对应式复用上轮输出的 35 位有效数字后，残差均小于 \(2\times10^{-35}\)。这只是 80 位非区间交叉核对；恒等式的一般依据是上文证明。

### 5.2 两种损耗不能混为一谈

| 样本 | 保留净源工作和真实边界后的 (12) 上界 / 实际 \(S^\circ\) | 丢掉有利源符号再作 Cauchy 的 (23) 上界 / 实际 \(S^\circ\) |
|---|---:|---:|
| 二阶，\(\theta=.6\) | 174.8779 | \(9.9190\times10^7\) |
| 切比雪夫 11，\(\theta=.6\) | 171.5543 | \(9.7074\times10^7\) |
| 一阶，\(\theta=.9\) | 1621.9526 | \(3.3301\times10^9\) |

保留源符号，避免了非常大的 Cauchy 损耗；但 (12) 丢掉梯度后的余量仍然明显。三个样本中，\(\mathcal H+\mathcal B\) 的主体是归一化梯度而非目标平方和。因此新能量式提供了具体研究条件，却没有自动给出理想大小的上界。

### 5.3 真实因子层的符号与配对

结果文件按实际 \(\omega(n)\) 保留全部六个非空因子层及其节点数、正节点数、背景配对和道路配对。以切比雪夫样本为例，道路配对为

| 因子层 | \(\sum_{\omega(n)=r}D_nu_n/n^{2\theta}\) |
|---:|---:|
| 1 | 1.14063076654058 |
| 2 | \(+5.15459652\times10^{-9}\) |
| 3 | \(-3.22826304\times10^{-9}\) |
| 4 | \(+7.90556480\times10^{-10}\) |
| 5 | \(-4.26305010\times10^{-11}\) |
| 6 | \(+1.78978360\times10^{-13}\) |

双素因子与三素因子层的符号与本轮父分支的一般核分析相容，但这里的有限符号结果不替代其一般证明。更关键的是：即使若干合数层的 \(D_n\) 配对很小，其 \(\kappa_n\) 背景配对仍可很大。例如该样本第 2、3 层的背景配对约为 0.47667、0.43485；完整中心化源工作的抵消发生在所有层共同作用后。不能以某层的道路系数很小为由删除那一层人口、中心项或其前史作用。

## 6. 可延续的结果与明确未完成项

本轮已经得到：

- 一个对任意有限厚度族成立、无需固定阶渐近常数的精确离散能量接口，正系数为 \(\theta(1-\theta)\)。
- 完整边界通量与非负接触项，以及正离散修正的明确双边界。
- 与实际格内式完全一致的连续源/边界/梯度恒等式。
- 对既有真实匹配窗口的新增算术分解，量化“提前取源正部”的损失和“丢掉梯度”的另一种损失。

仍需证明的不是恒等式，而是任意远窗口中的算术相关或等价的更有效估计。可继续的明确方向包括：对保持真实前史的正段研究源工作；用因子层核结构估计源与 \(q^+\) 的相关；或设计保留高频梯度贡献的乘子，避免在 (12) 中把全部梯度直接舍去。任何这样的后续步骤都必须重新证明其实际边界处理与全尺度量词。

## 7. 文件与归属

- `SIGNED_POSITIVE_ENERGY.md`：本稿。
- `verify_integer_energy.py`：仅核验新增分解的 80 位计算脚本。
- `prior_window_readouts.json`：从已发布上一轮结果选择的三条完整记录，含原文件 SHA256 与来源提交；不改写旧记录。
- `integer_energy_results.json`：新增结果与源配对的完整分层数据。

道路、原点修正及 RH 等价原始能量来自科学冻结输入；递推、\(\kappa_n\)、整数/连续窗口等价来自上一轮 `rh_next_window/NOTES.md`；正部区间及原函数来自上一轮 `rh_next_tail/ONE_SIDED_WINDOW_INTERFACE.md`。本稿所有计算和核对均为同一作者侧工作，没有远端 CLAIM、身份改变或独立 Review。
