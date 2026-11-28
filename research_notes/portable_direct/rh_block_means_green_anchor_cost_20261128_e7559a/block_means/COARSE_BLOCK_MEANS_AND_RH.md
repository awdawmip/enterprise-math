# 连续块均值、显式细节支付与平方根规模的 RH 判据

日期：2026-11-28（Asia/Hong_Kong）。作者：EM-DIRECT-E7559A / TASK_RESEARCH。

## 0. 范围、来源与新增量

本稿从前驱 Source `28665c59f04df2b7edcbdae5a1e967f587305cde` 的
`arithmetic_sampling/DYADIC_WINDOWS_AND_INTEGER_BRIDGES.md` 接续。前驱已经证明全整数中心、二幂长度的普通素数正亏缺统计与 RH 等价，并给出有向点对嵌入。这里不重做其证明或旧计算。

新增量是：先对连续整数块取均值，只对约平方根个均值计算正差平方，仍得到同一 RH 等价判据。恢复块内点值所需的信息由实际整数源的一步上升上界支付，显示费用为 `2r`。本文是固定 X6 轴上辅助标量观察的作者证明；完整整数人口、合数背景、普通素数质量、真实桥接均保留。没有新增无条件 RH 证明，也没有把标量平均宣布为原生 BRC 等价或端到端子线性算法。

## 1. 精确定义：先平均，再取正部

令 `X=2^k`，`k>=1`，选择整数 `0<=s<k`，置

\[
r=2^s,\qquad M=X/r=2^{k-s},\qquad t=k-s.
\]

令 `F(n)=n-theta(n)`，其中 `theta(n)=sum_{p<=n}log p`，普通素数 `p` 在完整整数背景中选择。连续块均值定义为

\[
w_i=\frac1r\sum_{v=0}^{r-1}F(X+ir+v),\qquad 0\le i<M.
\tag{1.1}
\]

新的统计为

\[
\boxed{\mathcal C_{k,s}^+
=\max_{d=1,2,\ldots,M/2\atop d\text{为二幂}}
\frac1{Xd}\sum_{i=0}^{M-1-d}(w_{i+d}-w_i)_+^2.}
\tag{1.2}
\]

这里 `d` 是块索引距离，实际整数距离为 `rd`，分母准确为 `Xd`。不能把它误写成 `Xrd`，也不能在平均各整数的差以前逐点取正部；后者是更强的充分统计。

定义旧统计的粗长度部分

\[
\mathcal K_{k,s}^{+,\mathrm{coarse}}
=\max_{D=r,2r,\ldots,X/2}
\frac1{XD}\sum_{u=X}^{2X-1-D}[F(u+D)-F(u)]_+^2.
\tag{1.3}
\]

所有允许中心仍出现在 (1.3)，但 (1.2) 只有块均值之间的差。

### 引理 1.1：准确的 Jensen 方向

\[
\boxed{\mathcal C_{k,s}^+\le
\mathcal K_{k,s}^{+,\mathrm{coarse}}\le\mathcal K_k^+.}
\tag{1.4}
\]

证明：`x->(x_+)^2` 为凸函数，所以对每个二幂 `d<M`，

\[
\begin{aligned}
\sum_i(w_{i+d}-w_i)_+^2
&\le\frac1r\sum_i\sum_{v=0}^{r-1}
[F(X+(i+d)r+v)-F(X+ir+v)]_+^2\\
&=\frac1r J_k^+(rd).
\end{aligned}
\]

`i,v` 准确遍历 `X<=u<=2X-1-rd`，没有缺端点或补中心。除以 `Xd` 即得。证毕。

## 2. 只用一步上升界恢复被平均的细节

本节先对任意实序列 `z_0,...,z_{X-1}` 工作，假设

\[
z_{n+1}-z_n\le1.\tag{2.1}
\]

负跳跃可以任意大。令 `w_i` 为其连续 `r` 块均值，并用 (1.2) 的分母 `Xd` 定义 `C`。前驱有向点对嵌入应用于长 `M=2^t` 的均值序列，注意其归一化统计为 `rC`，故

\[
(w_j-w_i)_+\le(t+1+\sqrt2)\sqrt{XC}\quad(i<j),
\tag{2.2}
\]

以及

\[
(w_{M-1}-w_0)_+\le t\sqrt{XC}.
\tag{2.3}
\]

### 定理 2.1：完整块和任意点的单侧恢复

\[
\boxed{z_{X-1}-z_0\le r-1+t\sqrt{XC},}
\tag{2.4}
\]

\[
\boxed{z_n-z_0\le2r+(t+1+\sqrt2)\sqrt{XC}
\quad(0\le n<X).}
\tag{2.5}
\]

证明：由 (2.1)，

\[
w_0-z_0\le(r-1)/2,
\quad z_{X-1}-w_{M-1}\le(r-1)/2.
\]

配合 (2.3) 得 (2.4)。对第一块，直接有 `z_n-z_0<=r-1`。如果 `n` 位于第 `j>=1` 块，则使用它之前的完整块，而不能使用包含未来负跳跃的同块均值：

\[
z_n-w_{j-1}
\le n-(j-1)r-(r-1)/2\le(3r-1)/2.
\]

再用 `w_0-z_0<=(r-1)/2` 和 (2.2)，总费用不超过 `2r-1+(t+1+sqrt2)sqrt(XC)`。放宽为 (2.5)。当 `j=1` 时均值差为零，仍成立。证毕。

该证明没有引入负跳跃的绝对值，也未假设最小正高度或素数间隔上界。

### 2.2 细节费用不能直接删去

取 `z_n=n mod r`，则 (2.1) 成立、每个块均值皆为 `(r-1)/2`，所以 `C=0`，但 `z_{X-1}-z_0=r-1`。因此，在只使用 (2.1) 与均值统计的这个一般序列类中，`O(r)` 的恢复费用有必要。

若在相邻二幂窗口使用不同 `r_k`，可以令每窗上述锯齿加上偏置 `c_k`，并取 `c_{k+1}=c_k+r_k`。窗口桥跳跃准确为 1，所有均值统计仍为零，而累积偏置为 `sum r_j`。这只刻画声明观察类的盲区，不是实际普通素数的反例，也没有证明更粗分块不可能通过其他算术结构形成 RH 判据。

## 3. 真实普通素数源给出全部恢复前提

对 `F(n)=n-theta(n)`，准确有

\[
F(n+1)-F(n)=1-\mathbf1_{\{n+1\ \mathrm{prime}\}}\log(n+1)\le1.
\tag{3.1}
\]

且因 `2^{k+1}>=4` 为合数，跨窗口桥准确为

\[
F(2^{k+1})-F(2^{k+1}-1)=1.
\tag{3.2}
\]

对每个窗口可选择 `r_k=2^{s_k}`，记 `C_k=C_{k,s_k}^+`、`t_k=k-s_k`。逐块接续 (2.4)，最后一块使用 (2.5)，得到：对 `2^k<=n<2^{k+1}`，

\[
\boxed{
F(n)\le 2-\log2+
\sum_{j=1}^{k-1}\left[r_j+t_j\sqrt{2^jC_j}\right]
+2r_k+(t_k+1+\sqrt2)\sqrt{2^kC_k}.
}
\tag{3.3}
\]

其中完整块的 `r_j-1` 与桥费用 `1` 已准确合为 `r_j`；没有遗漏边界项。

## 4. 平方根规模的普通素数正亏缺 RH 判据

取

\[
s_k=\lfloor k/2\rfloor,\qquad
r_k=2^{\lfloor k/2\rfloor},\qquad
M_k=2^{\lceil k/2\rceil},\qquad
\mathcal C_k^+=\mathcal C_{k,s_k}^+.
\]

**定理 4.1。**

\[
\boxed{
\mathrm{RH}
\ \Longleftrightarrow\
\forall\varepsilon>0,\quad \mathcal C_k^+\ll_\varepsilon 2^{\varepsilon k}
\ \Longleftrightarrow\
\mathcal C_k^+\ll k^2.
}
\tag{4.1}
\]

证明：若 `C_j<=C_eta 2^{eta j}`，则 (3.3) 中 `sum r_j=O(2^{k/2})`，而平方根统计费用为 `O_eta(k 2^{(1+eta)k/2})`。因此对每个 `epsilon>0`，

\[
\theta(x)\ge x-O_\varepsilon(x^{1/2+\varepsilon}).
\tag{4.2}
\]

前驱 §4 已完整证明这个单侧下界推出 RH：`psi>=theta`，非负函数 `Cx^a-(x-psi(x))` 的 Mellin 变换具有 Landau 实收敛边界奇点性质，而其显式变换

\[
\frac C{s-a}-\frac1{s-1}-\frac1s\frac{\zeta'(s)}{\zeta(s)}
\]

在所有实 `s>a>1/2` 全纯，故不能有实部大于 `a` 的零点。这里复用的是已有完整引理，不附加最右零点存在或线性独立假设。

反过来，前驱从 RH 条件下的 Selberg 界和已付高次素数幂误差证明 `K_k^+<<k^2`；由 (1.4) 得 `C_k^+<<k^2`。最后一项显然蕴含中间项。证毕。

同样由 `C_k^+<=K_{k,s_k}^{+,coarse}<=K_k^+`，仅保留实际长度 `D>=r_k` 的旧全中心统计也满足同一等价式。这个推论不把两统计逐值相等；(1.2) 是更少信息的充分入口。

更一般地，若 `r_k<=2^{k/2+o(k)}` 且 `M_k` 仍为二幂，同一证明给出次多项式判据。本文选择平方根分块，以使显示的保留规模和细节费用清楚。

## 5. 精确算术接口是非负梯形混合

令 `a=X+ir`。块均值差准确为

\[
w_{i+d}-w_i=rd-
\sum_{p\ \mathrm{prime}}\omega_{i,d}(p)\log p,
\tag{5.1}
\]

其中

\[
\omega_{i,d}(n)=\frac1r\#\{v\in\{0,\ldots,r-1\}:a+v<n\le a+rd+v\}.
\tag{5.2}
\]

权重非负，且对整数 `n` 可写为

\[
\omega_{i,d}(n)=\frac1r
\left[\min(r,n-a)-\max(0,n-a-rd)\right]_+.
\]

它在两端为长度 `r` 的斜坡，中间平坦；`d=1` 时是三角形。完整整数背景准确为

\[
\sum_{n\in\mathbb Z}\omega_{i,d}(n)=rd.
\tag{5.3}
\]

所以先完整计算同一非负权下的整数背景与普通素数质量，再取正部和平方。均值只消去公共前史常数；完整道路及其锚点并未因此得到重建。返回原 `1/n` Green 预算的进一步结论在同轮独立证明中给出，不能仅从 Jensen 反向推出。

## 6. 成本与本轮新计算

每窗有 `M=2^t` 个均值、`t` 个二幂块距离，差平方项数准确为

\[
\sum_{j=0}^{t-1}(M-2^j)=(t-1)M+1.
\tag{6.1}
\]

对 `1<=k<=14` 的平方根分块，总数为 **508 个均值、56 组窗口/距离、2,582 个均值差项**。前驱全中心全二幂长度统计有 393,234 项；只删短长度但保留全部中心则有 186,069 项。这里比较的是统计聚合项数，不是端到端运行时间。

伴随脚本复用前驱 80 位整数向外区间对数模块，重新取得新均值统计所需的 3,512 个普通素数对数和前缀至 32,767。它不重新计算前驱道路或旧统计。旧全中心证书只作为已认证的比较输入，读取其粗长度部分即可。前缀生成仍扫描完整源范围，故本轮没有宣称端到端子线性算法。

新脚本另以精确有理数核对：Jensen 的中心索引、先平均后正化、细节恢复、整窗费用、梯形完整整数背景、锯齿盲区及显示项数。有限核验检查实现和端点；无界量词由 §§1–4 解析证明承担。

## 7. 外部输入与前驱引用

- 直接前驱 `arithmetic_sampling/DYADIC_WINDOWS_AND_INTEGER_BRIDGES.md` §§2.2、3、4：有向平均链、单侧 Landau 接续、RH 条件下的旧统计上界。
- 直接前驱 `directed_dyadic/DIRECTED_DYADIC_GREEN_TRANSFER.md`：有向锥距离以及真实 `1/n` Green 转移；本稿不重复调用其数值脚本。
- A. Languasco and A. Zaccagnini, *Explicit relations between primes in short intervals and exponential sums over primes*, arXiv:1212.5704v2, 式 (22)：前驱核验过的 RH 条件 Selberg 输入，本轮重新打开并定位该式。https://arxiv.org/abs/1212.5704 。本轮的新稀疏化证明不来自该文。

