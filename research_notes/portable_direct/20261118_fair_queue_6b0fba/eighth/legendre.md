# JT2 第三代范数与一阶导数同余的统一求值

对每个素数 $p\equiv13,19\pmod{24}$，令 $n=(p-1)/3$、$2t^2=1$，并令 $I_n(x)=\int_0^x P_n(v)^2\,dv$。第三代任务留下的数是 **$\varepsilon_p=0$**。因而在两支端口上均有

$$
 9P_n(t)P'_n(t)\equiv p\,[2I_n(t)+3t]\pmod{p^2}.
$$

所需的算术输入位于另一条已评审分支。第三代发布于 9 月 19 日 UTC，当时只接纳过等价归约。9 月 24 日 D24 的正式评审已经证明同一素数总体、同一分母归一化下的全部一阶单位互反。这一输入还能求出普通 Legendre 根的提升，并给出两类素数上直接提升模数的反例。[第三代任务](https://github.com/awdawmip/enterprise-math/blob/3a8cee80e6707deb8601fb2d53bf2dc85d16fcba/research_tasks/EMW59A_JT2_UR_NORM_JET_GEN3_20260920.md) · [Gen2 普通 Legendre 归约](https://github.com/awdawmip/enterprise-math/blob/969846f1d451b3e086f34a19b217e333c8a90c8d/research_returns/EMW59A_JT2_UR_SUN_PARITY_DEFECT_RETURN_EF9380_20260910.md) · [D24 正式评审](https://github.com/awdawmip/enterprise-math/blob/c082edc8ce1a7ce3f560ebd5bd62b4d20245eb02/driver_reviews/mcp/MCP-98288d02291d47c9b0ebffd45b7e3be7/354f25b387a48ff263a2/D24_UR_JT0_DRIVER_REVIEW_20260924.md)

## 一　带符号的 CM 输入

写 $p=6m+1$，$n=2m$，$P_n(x)=Q_m(x^2)$。原始一阶归一化为

$$
 c_k=\frac{(1/6)_k(1/3)_k}{(k!)^2},\quad
 g=\sum_{k=0}^{p-1}c_k2^{-k},\quad
 h=\sum_{k=0}^{p-1}(12k+1)c_k2^{-k},\quad G_{\rm div}=g/p .
$$

在 $\mathbb Z_{(p)}[t]/(2t^2-1)$ 中采用给定 CM0、SIMPLE 及已接纳的双端口变换。特别是 $P_n(t)$、$g$ 和广义 Legendre 值 $B(t)=P_{p-1}(-1/3,t)$ 已知可被 $p$ 整除，且 $Q_m'(1/2)=P'_n(t)/(2t)$ 是单位。$g/p$ 是已认证的一阶商。

引入有权截断
$$
 W_p=\sum_{k=0}^{p-1}\frac{(1/2)_k(1/3)_k(2/3)_k}{(k!)^3}(6k+1)2^{-k}.
$$
Chan–Liaw 定理 1.1 及表 6 的 $n=2$ 行给 $a_2=1/(3\sqrt3)$、$b_2=2/\sqrt3$、$H_2=1/2$。故 Ramanujan 权重斜率为 $b_2/a_2=6$。Chisholm–Deines–Long–Nebe–Swisher 定理 1（出版版第 12 页）在 $d=3,\lambda=1/2$ 给 $W_p\equiv\operatorname{sgn}\,(\frac{1-\lambda}{p})\,p\pmod{p^2}$，其中超奇异约化的 $\operatorname{sgn}=-1$。两篇期刊原文的定理与表项均可直接核对。[Chan–Liaw](https://doi.org/10.2140/pjm.2000.192.219) · [Chisholm 等](https://doi.org/10.3390/math1010009)

具体模型为 $y^2+xy+(u/27)y=x^3$，$u=(1-t)/2$，另一支取 $1-u$。$u(1-u)=1/8$，故 $\Delta=u^3(1-u)/3^9$ 在每个目标素数处为单位。两支 $j=2417472\pm1707264\sqrt2$，均属判别式 $-24$ 的 CM 类。$6,1/2$ 为 $p$ 单位，参数实且绝对值小于一，$\mathbb Q(\sqrt2)$ 在 $p$ 不分歧。两类素数均有 $(2/p)=-1$。因 $p\equiv1\pmod3$，还有 $(-3/p)=1$，故 $(-6/p)=-1$。CM 惰性给超奇异符号 $-1$，$(\frac{1-\lambda}{p})=(2/p)=-1$。因此 $W_p\equiv p\bmod p^2$ 对两类素数同时成立。[D24 模型及假设核对](https://github.com/awdawmip/enterprise-math/blob/c082edc8ce1a7ce3f560ebd5bd62b4d20245eb02/driver_reviews/mcp/MCP-98288d02291d47c9b0ebffd45b7e3be7/354f25b387a48ff263a2/D24_UR_JT0_DRIVER_REVIEW_20260924.md)

## 二　从 CM 赋值回到确切的 $P_n$ 与 $I_n$

令 $A(z)=\sum_{k\ge0}c_k z^k$、$D=z\,d/dz$。形式 Clausen 恒等式给 $A^2={}_3F_2(1/2,1/3,2/3;1,1;z)$，且 $(1+6D)A^2=A(1+12D)A$。右边保留总次数 $<p$ 再取 $z=1/2$ 恰得 $W_p$。完整有限乘积 $gh$ 的其余项满足 $i+j\ge p$。当 $k>m$ 时 $(1/6)_k$ 已含因子 $p/6$，当 $k>2m$ 时 $(1/3)_k$ 又含 $p/3$。$k<p$ 时分母均为单位。若 $i,j>m$，两项各贡献至少一个 $p$。若一个不大于 $m$，另一个至少为 $5m+1>2m$。故逐项有
$$
 gh\equiv W_p\equiv p\pmod{p^2}.
$$
模 $p$，有限多项式 $A_{<p}(z)$ 等于冻结二次变换所给的 $Q_m(1-z)$。从而 $h\equiv Q_m(1/2)-6Q_m'(1/2)=-6Q_m'(1/2)\pmod p$。在已取得 CM0 后对 $gh\equiv p$ 除以 $p$，得到实际数值
$$
 G_{\rm div}\bigl(-6Q'_m(1/2)\bigr)\equiv1\pmod p .
$$

由已接纳双端口 $B(t)/p\equiv G_{\rm div}$ 与坐标桥 $P'_n(t)=2tQ_m'(1/2)$，这个数值立即给
$$
 3 B(t)P'_n(t)\equiv-pt\pmod{p^2},\qquad
 (P_{2n}(t)+2P_n(t))P'_n(t)\equiv-pt\pmod{p^2},
$$
其中第二式使用 $3B\equiv P_{2n}+2P_n\bmod p^2$。

为固定归一化与符号，写 $f=P_n$、$C=(P_{2n}-P_n)/(3p)$。Gen2 的已接纳 Wronskian 为
$$
 (1-x^2)(fC'-f'C)\equiv I_n(x)/9-x^p/3\pmod p .
$$
两边在 $x=0$ 的积分常数按 $I_n(0)=0$ 固定，导数不可见的 $x^p$ 系数用端点及 $I_n(1)=1/(2n+1)$ 固定。先保留 $x^p$，再以 $t^p=-t\bmod p$、$1-t^2=1/2$ 求值，得到 $C(t)P'_n(t)\equiv-2I_n(t)/9-2t/3$。最后代入 $B=f+pC\bmod p^2$ 及上一行的 CM 赋值，给出
$$
 9f(t)f'(t)\equiv p\,[2I_n(t)+3t]\pmod{p^2},\qquad
 \varepsilon_p=9\frac{f(t)}p\frac{f'(t)}t-2\frac{I_n(t)}t-3\equiv0\pmod p .
$$
$I_n$ 的积分分母至多是 $2n+1<p$。所有步均作用于给定的完整多项式，交换 $t\leftrightarrow-t$ 时两个奇读数同步变号，除以单位 $t$ 得同一个基域标量。

## 三　唯一根提升及模数的边界

记 $R_m(z)=\sum_{r=0}^{2m}b_rz^r/(2r+1)$，其中 $b_r=[z^r]Q_m(z)^2$，即 $I_n(x)=xR_m(x^2)$。设 $d=Q_m'(1/2)\bmod p$、$N=R_m(1/2)\bmod p$。由上式可在仅给出模 $p$ 的系数、导数与范数读数时还原
$$
 \frac{Q_m(1/2)}p\equiv\frac{2N+3}{18d}\pmod p .
$$
因此 $Q_m$ 那个模 $p$ 同余于 $1/2$ 的根，其唯一模 $p^2$ 提升为
$$
 z_*=\tfrac12-p\,\frac{2N+3}{18d^2}\pmod{p^2}.
$$
这是 Taylor 展开 $Q_m(1/2+p v)\equiv Q_m(1/2)+pvd\bmod p^2$ 得出的根。特别，固定半点本身提升为根当且仅当 $N\equiv-3/2\bmod p$。

还有一个不同的根问题。设
$$
 D_p(z)=18Q_m(z)Q_m'(z)-p(2R_m(z)+3).
$$
已证 $D_p(1/2)\equiv0\bmod p^2$，而 $D_p'(1/2)\equiv18d^2\ne0\bmod p$。于是对每个 $v\in\mathbb F_p$，
$$
 D_p(1/2+pv)\equiv18pvd^2\pmod{p^2}.
$$
半点是该同余在其模 $p$ 剩余类里的唯一提升。$\bigl(9P_nP'_n-p(2I_n+3x)\bigr)/x=D_p(x^2)$，所以这也给出两支 CM 端口的横截性。

原式的模 $p^2$ 精度在两类素数上都不能直接改成模 $p^3$。用普通 Legendre 三项递推在 $\mathbb Q[x]$ 内算得以下精确见证。

| $p$ | $Q_m(1/2)$ | $Q_m'(1/2)$ | $I_n(t)/t$ | $D_p(1/2)$ | $D_p(1/2)/p^2\bmod p$ |
|---:|---:|---:|---:|---:|---:|
| 13 | $-13/32$ | $5/8$ | $793/9216$ | $-211081/4608$ | 2 |
| 19 | $-19/128$ | $-147/64$ | $10721/212992$ | $-5620409/106496$ | 11 |

相应的 $Q_m$ 根提升分别为 $111\bmod169$、$219\bmod361$。冻结的 LIFT 是含额外截断、二阶导数和余项的另一个标量，上表否定的是保持原式直接改换模数。

## 复算与边界

legendre_check.py 从 Rodrigues 系数生成实际 $Q_m$，逐项卷积计算 $R_m$，另行在二次环内求广义 $B(t)$，直接算 $g,h,W_p$，并回代两种根与归一化。小素数再由有理三项递推独立核对，另取 $2029,2083$ 各一支作不同长度的回归。四个 $\varepsilon_p$ 均为零，后两例的下一位分别是 $1846,1528$。详细输出见 legendre_checked.json。全素数结论来自同一对象的已证 CM 输入及有限恒等式。

第三代的数学目标由这条跨分支推论满足。本次贡献是把已证明的一阶互反接回指定积分、普通 Legendre 模 $p^2$ 范数及 Hensel 根，并给出精度边界。已有一阶互反的归属见 D24 评审。任务的正式登记仍由状态机单独处理。
