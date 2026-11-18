# 从七次 Frobenius 图像构造 Prym 的秩一对应

在特征七的实际曲线 $C=C_{46,7}$ 上，可以用 Frobenius 和已有四阶自同构的图像写出两个有理除子对应。它们在 $P=\operatorname{Prym}(C/E)$ 上给出互补的秩一幂等元。两个像均为与已知 $J(C_7)$ 同源的曲面，由七次 Frobenius 互换。本构造还能在自然 Prym 极化下精确判定这对幂等元不自伴。

冻结输入取自 R105。在 $\mathbf F_7$ 上，$\pi=\operatorname{Frob}_7$ 在 $P$ 上的多项式为 $f(t)=h(t^2)$，其中 $h(s)=s^4+5s^3+245s+2401$。令 $s=\pi^2,\ F=\mathbf Q(s),\ L=F(\pi)$。在 $\mathbf F_{49}$ 上有 $\operatorname{End}^0(P)=M_2(F)$ 及 $P\sim B^2$，其中 $B$ 为绝对单纯曲面。先前的伴随矩阵给出了两条抽象坐标线，本次在原曲线上给出具体图像组合。[R105 交接](https://github.com/awdawmip/enterprise-math/blob/c0f816e2ab6be0145a3edd1a77488bddfd42a2f6/research_notes/EM_FREE_F6D046_R105_STATE_MACHINE_HANDOFF_20260909.md) · [Honda–Tate 输入](https://github.com/awdawmip/enterprise-math/blob/574f53c7b37ae6703ade390df851d8822af6364c/research_notes/EM_FREE_F6D046_P46_P7_HONDA_TATE_20260904.md) · [原矩阵前沿](https://github.com/awdawmip/enterprise-math/blob/574f53c7b37ae6703ade390df851d8822af6364c/research_notes/EM_FREE_F6D046_P46_P7_MATRIX_IDEMPOTENT_DESCENT_20260904.md)

## 1. 曲线上的两个算子

在典范坐标 $[W:Z_0:Z_1:Z_2:Z_3]=[w:1:x:y:x^2]$ 中，仿射方程为 $y^2=x^3-6x^2+36,\ w^2=y(x^2-12)$。取 $i^2=-1$ 于 $\mathbf F_{49}$，令 $\sigma(w,x,y)=(iw,x,-y)$，$z=\sigma^2$。记 $\pi$ 也表示由 $\mathbf F_7$ 模型的七次幂态射基变换得到的曲线自映射，各图像约定以推出作用于 Jacobian。曲线上 $\pi\sigma=\sigma^{-1}\pi$，因为 $i^7=-i$。双覆盖的 Prym 上 $z=-1$，因此
$$
\sigma^2=-1,\qquad \pi\sigma=-\sigma\pi,\qquad
\sigma a(\pi)=a(-\pi)\sigma \quad(a\in L).
$$
在整个 $J(C)$ 上，$e_P=(1-z)/2$ 是对应的有理 Prym 投影。特征七曲线的完整几何自同构群正是 $\langle\sigma\rangle$。[典范坐标](https://github.com/awdawmip/enterprise-math/blob/574f53c7b37ae6703ade390df851d8822af6364c/research_notes/EM_FREE_F6D046_C46_CANONICAL_NET_AUTOMORPHISM_20260904.md) · [约化曲线和完整自同构群](https://github.com/awdawmip/enterprise-math/blob/574f53c7b37ae6703ade390df851d8822af6364c/research_notes/EM_FREE_F6D046_C46_P7_FULL_AUTOMORPHISM_20260904.md)

## 2. 范数方程及其几何实现

使用以下三个整系数多项式。
$$
\begin{aligned}
D(s)&=8s^2+168s+882,\\
U(s)&=-13s^3-372s^2-616s+3773,\\
V(s)&=2s^3+74s^2+1708s+16464.
\end{aligned}
$$
它们在整数多项式环中满足
$$
U^2+V^2-sD^2=h(s)(173s^2+9039s+118825).
$$
且 $\gcd(V,h)=1$。这些系数可从 $F(i)/F$ 中对 $s$ 解相对范数方程得到，再对共同分母做格基约化。上式可直接用乘法核验。置
$$
q(t)=\frac{U(t^2)+tD(t^2)}{V(t^2)}\pmod {f(t)},\quad
Q=q(\pi)\sigma,\quad e_\pm=\frac{1\pm Q}{2}.
$$
范数恒等式给出 $q(t)q(-t)=-1$，故 $Q^2=1$，$\pi Q\pi^{-1}=-Q$。由此 $e_+e_-=0,\ e_++e_-=1,\ \pi e_+\pi^{-1}=e_-$。在 $M_2(F)$ 中两个幂等元秩相等且秩之和为二，各为秩一。于是其像在有理 Tate 模上维数为四，分别给出同源于 $B$ 的阿贝尔曲面。

**有理除子公式。** 取 $q$ 的次数小于八的唯一代表，写为 $\sum_{j=0}^7q_jt^j$。对曲线态射 $g$ 记 $\Gamma_g\subset C\times C$ 为其图像。则
$$
\mathcal E_\pm=\frac{\Gamma_1-\Gamma_z}{4}
\ \pm\ \frac14\sum_{j=0}^7 q_j
 \bigl(\Gamma_{\pi^j\circ\sigma}-\Gamma_{\pi^j\circ\sigma^3}\bigr).
$$
它在 $J(C)$ 上诱导 $e_P(1\pm q(\pi)\sigma)/2$，从而在椭圆商的有理因子上为零，在 Prym 上为 $e_\pm$。幂等式在对应诱导的端同态中成立。逆元 $V^{-1}$ 只需在 $F$ 内求取，上式的 $q_j$ 由多项式扩展欧几里得唯一确定。

**整系数图像及双次数。** 取曲线对应
$$
K_\pm=(1-z)\bigl[V(\pi^2)\ \pm\
       (U(\pi^2)+\pi D(\pi^2))\sigma\bigr],
$$
式中的加法是图像的带符号和，乘法是复合。其作用是 $4V(\pi^2)\mathcal E_\pm$ 在 Jacobian 上的作用，故整分子的像就是相应的阿贝尔曲面。按 Frobenius 次数 $j=0,\ldots,6$ 分组，为每组只保留正项或只保留负项时，绝对重数之和依次为
$$
20237,\quad882,\quad2324,\quad168,\quad446,\quad8,\quad15 .
$$
每条 $\Gamma_{\pi^j\sigma^k}$ 向源曲线及目标曲线的投影次数分别为 $1,7^j$，后一项包含纯不可分度。故 $K_\pm$ 各可表示为两个双次数均为 $(24080,3167948)$ 的有效除子之差。该界适用于这里的整分子。低双次数的 $C_{46}\times C_7$ 除子及最优双次数仍待构造。

## 3. 图像所需的最低 Frobenius 次数恰为四

令图像范围只含 $\Gamma_{\pi^j\sigma^k}$，其中 $0\le j\le m,\ 0\le k<4$，允许任意有理系数。限制到 $P$ 上的任意组合写成 $R=A(\pi)+B_0(\pi)\sigma$，其中 $A,B_0\in\mathbf Q[t]$ 且次数至多 $m$。它的约化范数是
$$
N_R(t)=A(t)A(-t)+B_0(t)B_0(-t)\pmod f.
$$
例如把 $A+B_0\sigma$ 乘以 $A(-\pi)-B_0(\pi)\sigma$ 即得此标量。若 $m\le3$，秩一要求 $f\mid N_R$；因 $\deg N_R\le6$，只能 $N_R\equiv0$ 作为多项式。令 $t=\sqrt{-1}\,y$ 且 $y$ 为实数，两项分别为模平方，故 $A=B_0=0$。所以任何非零低于四阶的图像组合在 $P$ 上都有秩二。

四阶已经能取得上文同一对曲面像。取
$$
\begin{aligned}
A(t)&=6174+5012t-5103t^2+670t^3-1843t^4,\\
B_0(t)&=-90307+35t-5117t^2-93t^3+126t^4.
\end{aligned}
$$
直接乘法给出
$$
N_R(t)=3412525 f(t),\qquad B_0(t)\equiv q(t)A(-t)\pmod f.
$$
后式与 $q(t)q(-t)=-1$ 给出
$$
Q\bigl(A(\pi)\pm B_0(\pi)\sigma\bigr)
   =\pm\bigl(A(\pi)\pm B_0(\pi)\sigma\bigr).
$$
故整图像对应 $(1-z)[A(\pi)\pm B_0(\pi)\sigma]$ 的两个像分别等于 $\operatorname{im}e_\pm$。系数可由线性方程 $B_0=qA(-t)\bmod f$ 计算，允许两个次数至多四的多项式给出十个未知数、八个独立有理约束。每个正负有效部分的双次数为 $(114480,5621868)$，其中单条分量图像的目标投影次数最大为 $7^4=2401$。这里最优的是产生曲面像所需的最大 Frobenius 指数。前一节的六阶整分子总重数更小，两种计量给出不同界。对四阶整分子取像无需将其本身当作幂等元。

## 4. 下降和极化的可检验区别

对任意 $n\ge1$，$\pi^n Q\pi^{-n}=(-1)^nQ$。因此两条具体曲面像及它们各自的有理投影恰在 $2\mid n$ 时分别定义于 $\mathbf F_{7^n}$；奇数次扩域交换这一对。冻结的主极化商由 $\mathbf P(E[2])$ 的三条直线参数化，恰在 $3\mid n$ 时有定义于该域的选择。于是标记其中一个投影与一条主极化直线的组合在 $6\mid n$ 时有六个域有理选择，在其余情形下为零。四维 Prym 的自然极化型为 $(1,1,1,2)$。[有限 étale 下降](https://github.com/awdawmip/enterprise-math/blob/574f53c7b37ae6703ade390df851d8822af6364c/research_notes/EM_FREE_F6D046_P46_COMBINED_STRICTIFICATION_SCHEME_20260904.md)

具体投影可进一步接受自然 Rosati 对合 $\dagger$ 的检验。曲线自同构保持典范极化并限制到 Prym，故 $\sigma^\dagger=\sigma^{-1}=-\sigma$，且 $\pi^\dagger=7/\pi$。于是
$$
Q-Q^\dagger=\bigl(q(\pi)+q(-7/\pi)\bigr)\sigma.
$$
将括号内的元素模 $f$ 约到次数小于八，其常数系数为 $-865765/47654027$。所以这对投影均非自然极化的自伴投影，两条曲面像不正交。这同时给出了有理秩一分解与自然极化正交分解之间的具体见证。其余投影的自伴性和 $2$-进整 Hermitian 格仍是独立问题。

冻结的显式 genus-2 模型 $C_7$ 给出 $J(C_7)\sim_{\mathbf F_{49}}B$。当前结果确定两条像的同源类，需要额外的同源映射才能把上述对应转写到 $C_{46}\times C_7$ 上。特征零的 $P_{46,\overline{\mathbf Q}}$ 几何单纯，几何有理端同态域为 $\mathbf Q(i)$，其幂等元只有 $0,1$；故这里的投影是特征七约化所特有。冻结的连通 Sato–Tate 群为 $U(4)$，分量群为 $C_2$。[显式曲面代表](https://github.com/awdawmip/enterprise-math/blob/574f53c7b37ae6703ade390df851d8822af6364c/research_notes/EM_FREE_F6D046_B_GENUS2_WEIL_RESTRICTION_20260904.md) · [特征零和整中心](https://github.com/awdawmip/enterprise-math/blob/c0f816e2ab6be0145a3edd1a77488bddfd42a2f6/research_notes/EM_FREE_F6D046_R105_STATE_MACHINE_HANDOFF_20260909.md)

## 5. 复算

同目录运行 `python honda_check.py`，依赖 Python 3 和 SymPy。程序以有理系数验证两个不可约多项式、范数恒等式、幂等性、互补性、交换关系、Rosati 差值及整分子的双次数。它还在 $\mathbf F_{49}=\mathbf F_7[i]$ 上枚举曲线点，得到 $C_{46}$ 有 64 个仿射点加一个无穷远点，并在全部仿射点复核七次幂关系；同样直接枚举得到 $\#C_7(\mathbf F_{49})=55$。这些点数用于检查曲线模型和算子约定，秩一性由范数恒等式及端同态代数推出。
