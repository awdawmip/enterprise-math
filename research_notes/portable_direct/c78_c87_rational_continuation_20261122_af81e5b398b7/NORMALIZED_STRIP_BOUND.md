# 原全库存的有理归一条带界：跨同步、全部 \(1\le b\le c\)

日期：2026-11-23（Asia/Hong_Kong）。作者侧有限代数核对，服务 C78 锐判据的必要方向。沿用原库存、全部安排、三个完整终尾和原 \(g=H(0,1)\)，本文件不使用相对导数或同步分离假设。

## 1. 已证的有限命题

取有理数 \(0<\eta\le1\)，整数 \(c\ge4/\eta\)，保留原安排中的

\[
\mathcal T_{c,\eta}
=\{(V,W):\eta c\le W\le V\le c\}.
\]

记

\[
\Gamma_c(n,V,W)
=\frac{5[g(n,V,W)-1]}{27F_1(c)}.
\]

令

\[
a_0=(\eta/3)^4,\qquad H_0=\frac{18368}{\eta},
\]
\[
\boxed{C_0(\eta)=\frac{1344H_0}{a_0},}
\]
\[
\boxed{
C_1(\eta)=H_0\left(
\frac{31920}{a_0}+\frac{162109644480}{a_0^2}
\right).
}
\tag{1.1}
\]

这些是明确有理数。则每个上述原安排、每个整数 \(c\le n\le2c\) 都满足

\[
\boxed{0\le\Gamma_c(n,V,W)\le C_0(\eta),}
\tag{1.2}
\]

而对 \(c\le n<2c\)，

\[
\boxed{
|\Gamma_c(n+1,V,W)-\Gamma_c(n,V,W)|
\le\frac{C_1(\eta)}c.
}
\tag{1.3}
\]

因此对全部整数 \(1\le b\le c\)，

\[
\boxed{
|\Gamma_c(c+b,V,W)-\Gamma_c(c,V,W)|
\le C_1(\eta)\frac bc.
}
\tag{1.4}
\]

本命题允许内层同步、外层同步及改变 \(n\) 时跨越外同步点。常数非常保守，只有存在且全有理、与 \(c,b,V,W\) 无关的作用；本轮不做最优化。

## 2. 原三尾与两层分式给出的全分支公式

因为 \(W\ge4\)，上一份准确终尾证明给 \(z_1<z_2<z_3\)，以及

\[
z_3-z_1=\frac{27}{5}F_1(W)K_W,\qquad 0<K_W\le\frac{41}{6}.
\tag{2.1}
\]

上界来自 \(a_W\le1,t_W\le5/2\) 和
\[
K_W\le1+(7/3)t_W\le41/6.
\]

令内层参数为 \(D=\rho_3(V,W),T=\tau_3(V,W)\)，其两个极端值为
\[
0<l\le h<4.
\]
上界是直接分式凸组合：
\[
\frac{D+Tz}{1+Tz}
=\frac1{1+Tz}D+\frac{Tz}{1+Tz}\cdot1,
\qquad0<D<4.
\]
原中间尾始终落在这两个极端之间；同步 \(D=1\) 时三者相同。

写 \(d=h-l\)。有限分式差给

\[
d=
\frac{T|1-D|(z_3-z_1)}
{(1+Tz_1)(1+Tz_3)}.
\tag{2.2}
\]

对外层记 \(A=\rho_5(n,V),S=\tau_5(n,V)\)。不按 \(A<1\) 或 \(A>1\) 分案，直接定义

\[
D_*(A,S)=
\min\{(A+Sl)(1+Sh),\ (A+Sh)(1+Sl)\}.
\]

则原无向读数准确满足

\[
\boxed{
g(n,V,W)-1
=d\,\frac{S|1-A|}{D_*(A,S)}.
}
\tag{2.3}
\]

这是两个实际外层端点的差除以较小输出，完整保留原 max/min。特别是 \(A=1\) 时直接给零；没有除以 \(1-A\)，因而跨同步不出现相对导数的极点。

## 3. 所有量的有限有理包围

原乘积给 \(0<A,D<4\)、\(0<S,T<448\)，故 \(|1-A|,|1-D|\le3\)。

### 3.1 外层 \(A\) 的统一正下界

上一轮 \(k=5\) 的四次幂包络给

\[
A^4\ge256\frac{41}{250}
\left(\frac{V+21/8}{n+29/8}\right)^{15}.
\]

因为 \(n\le2c,c\ge4\)，有 \(n+29/8\le3c\)，而 \(V\ge\eta c\)。于是

\[
A^4\ge256\frac{41}{250}(\eta/3)^{15}
\ge(\eta/3)^{16}=a_0^4.
\]

正数四次幂比较得到 \(A\ge a_0\)。特别是
\[
D_*(A,S)\ge A\ge a_0.
\tag{3.1}
\]

### 3.2 归一化内层宽度

上一轮 \(k=1\) 包络的下界给

\[
\left(\frac{F_1(W)}{F_1(c)}\right)^4
\le\left(\frac{c+9/8}{W+9/8}\right)^3
\le(2/\eta)^3\le(2/\eta)^4,
\]

所以 \(F_1(W)/F_1(c)\le2/\eta\)。结合 (2.1)–(2.2)，

\[
\frac{5d}{27F_1(c)}
\le448\cdot3\cdot\frac{41}{6}\cdot\frac2\eta
=\frac{18368}{\eta}=H_0.
\tag{3.2}
\]

因此 \(\Gamma_c\le H_0\cdot1344/a_0=C_0\)，证明 (1.2)。同步使 \(d=0\) 时同样成立。

## 4. 跨同步的有限差分界

对任意两组 \(A,A'\in[a_0,4]\)、\(S,S'\in[0,448]\)，固定同一 \(l,h\in[0,4]\)。每个候选分母的准确差，例如

\[
(A'+S'l)(1+S'h)-(A+Sl)(1+Sh)
\]
\[
=(A'-A)(1+S'h)
+(S'-S)\{Ah+l+(S'+S)lh\},
\]

给出

\[
|\Delta D_*|
\le1793|\Delta A|+14356|\Delta S|.
\tag{4.1}
\]

这里用到了有限不等式
\[
|\min(a,b)-\min(c,d)|\le\max(|a-c|,|b-d|),
\]
所以即使两个分母在 \(A=1\) 处交换较小者，界仍成立。

对 \(N_*(A,S)=S|1-A|\)，有

\[
0\le N_*\le1344,\qquad
|\Delta N_*|\le448|\Delta A|+3|\Delta S|.
\tag{4.2}
\]

利用分母下界 \(a_0\)，直接分式相减给

\[
\left|\Delta\frac{N_*}{D_*}\right|
\le\left(\frac{448}{a_0}+
\frac{1344\cdot1793}{a_0^2}\right)|\Delta A|
\]
\[
\quad+
\left(\frac3{a_0}+
\frac{1344\cdot14356}{a_0^2}\right)|\Delta S|.
\tag{4.3}
\]

原库存一步差分准确满足

\[
\Delta_n A=-\frac{15A}{4(n+6)},\qquad
\Delta_n S=-\frac{75S}{4(n+21)}.
\]

在 \(n\ge c\) 时，
\[
|\Delta_n A|\le15/c,\qquad
|\Delta_n S|\le8400/c.
\]

乘以固定的归一化内层宽度上界 \(H_0\)，式 (4.3) 即给

\[
|\Delta_n\Gamma_c|
\le\frac{H_0}{c}
\left[\frac{31920}{a_0}+
\frac{162109644480}{a_0^2}\right].
\]

这就是 (1.3)，对 \(b\) 次有限求和得到 (1.4)。整个论证只有有限加乘除、min、绝对值及整数比较。

## 5. 保留安排的比例

令 \(m=\lceil\eta c\rceil\)。被删除的仅是 \(2\le W<m\)，其数量至多

\[
(m-2)(c-1)\le\eta c(c-1).
\]

因此

\[
\boxed{
\frac{|\mathcal T_c\setminus\mathcal T_{c,\eta}|}{\binom c2}
\le2\eta.
}
\tag{5.1}
\]

本条带界不要求再删除靠近同步线的安排，也不要求远离 \(V=W\) 或 \(V=c\)。给定任何固定小的有理 \(\eta\)，其常数固定，覆盖比例可以任意接近 1。

## 6. \(\Xi\to0\) 的全库存唯一率结论

若原两个轴的舍入格宽均为 \(2^{-p}\)，各轴格原点可任意独立平移，则对 \(\Gamma_c\) 而言共同格宽为

\[
\delta=\frac{5\,2^{-p}}{27F_1(c)}.
\]

写 \(z=b/c,\ r=c\delta,\ \lambda=r^2/z\)。对所有保留安排，

\[
0\le X:=\Gamma_c(c)\le C_0,\qquad
|Y-X|:=|\Gamma_c(c+b)-\Gamma_c(c)|\le C_1z.
\]

任一第一轴格区间内，第二轴的可能值区间长度至多 \(\delta+2C_1z\)。故所占二维格数至多

\[
\left(\frac{C_0}{\delta}+2\right)
\left(\frac{2C_1z}{\delta}+3\right)
=O_\eta(1+\delta^{-1}+z\delta^{-2}),
\tag{6.1}
\]

其中用了 \(z\le1\)。这个界对所有格原点统一。

能唯一占格的保留安排数至多上述格数；其他安排即使全部算作唯一，比例也至多 \(2\eta\)。于是

\[
V_c\le2\eta+
O_\eta\left(\frac1{c^2}+\frac1{cr}+\frac1\lambda\right).
\tag{6.2}
\]

对新的纯有理判据

\[
\Xi=\frac{2^{4p}b^2}{c^9},
\]

准确计算为

\[
\boxed{
\lambda^2\Xi=
\frac{625}{27^4F_1(c)^4c^3}.
}
\tag{6.3}
\]

上一轮有限乘积包络给，对所有 \(c\ge1\)，

\[
\boxed{
\frac{729}{4913}
\le F_1(c)^4c^3
\le\frac{18225}{11008}.
}
\tag{6.4}
\]

下界是 \((9/8)^3[c/(c+9/8)]^3\ge(9/17)^3\)，
上界是 \((50/43)(9/8)^3\)。

所以 \(\Xi\to0\) 等价于 \(\lambda\to\infty\)。又因为 \(b\ge1\)，

\[
(cr)^2=cb\lambda\ge c\lambda\to\infty.
\]

固定任意有理 \(\eta>0\)，先令 \(c\to\infty\)，式 (6.2) 给
\(\limsup V_c\le2\eta\)。再令 \(\eta\downarrow0\)，得到

\[
\boxed{
\Xi\to0\quad\Longrightarrow\quad V_c\to0,
\qquad\text{全部 }1\le b\le c.
}
\tag{6.5}
\]

这一方向甚至不需 \(b=o(c)\)。它只依赖准确有限条带界、有限格数计数和最后的数量极限，不需要同步分离内片的 \(C^2\) 桥。

## 7. 范围

本文件为 \(\Xi\to0\) 的必要尺度方向提供直接有限重证，允许同步穿越和任意舍入平移。它不单独证明 \(\Xi\) 有界时存在统一正歧义比例，也不单独证明 \(\Xi\to\infty\) 时唯一率趋一；那两项沿各自的同步带下计数和跨逆支充分性证明处理。

本轮未扩大库存实验。所有常数及式 (6.3)–(6.4) 已按原有限乘积公式和整数算术核对。这里保存的是作者侧证明，不是独立项目 Review。
