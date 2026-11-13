# R385｜所有余阶的带符号 BRC 次高系数定理

日期：2026-10-29。作者侧数学证明（未独立审查、未正式接纳）。仅针对原始十二支路带符号 K/J → B → D 辅助组合模型，参数 \(\theta>-1\)，唯一变形 \(K_3[t^2]=-8(1+\theta)\)。不涉及原生 X6 动力学或完整 PF₂ 相图。

## 定理

沿用 R384 由原始 D 阵列证明的全余阶抽取 \(D_{r+u,u}=5^u H_r(u;\theta)\)，其中 \(\deg_u H_r\le r\)。令

\[
\lambda=(30-16\theta)/25,\quad
F_r=(35r+25-32r\theta+32\theta)/50,\quad
G=(105+760\theta-384\theta^2)/625.
\]

对一切整数 \(r\ge2\) 及一切实数 \(\theta>-1\)，严格有

\[
\boxed{[u^{r-1}]H_r(u;\theta)=
\frac{5^r}{(r-1)!}
\big(\lambda^{r-1} F_r+(r-1)\lambda^{r-2}G\big).}\tag{1}
\]

对 \(r=1\) 有 \([u^0]H_1=6\)。R384 已证 \([u^r]H_r=5^r\lambda^r/r!\)。因此在 \(\theta=15/8\)，\(G=36/125\)、\(\lambda=0\)，得到 \([u]H_2=36/5\ne0\)，以及

\[
\boxed{\deg H_r(u;15/8)\le r-2\qquad(r\ge3).}\tag{2}
\]

对于 R384 定义的
\(L_r=5^rH_r\),
\(Q_r(v)=L_r(v+1)L_r(v+2)-L_{r-1}(v+2)L_{r+1}(v+1)\)，
由两个乘积的次数上界立即推出

\[
\boxed{\deg Q_r(v;15/8)\le 2r-4\qquad(r\ge4).}\tag{3}
\]

这严格加强 R384 在退化点的最高项消失定理，但尚不证明观察到的更强等式 \(\deg H_r=\lfloor r/2\rfloor,\ \deg Q_r=r\)。

## 全指标证明

R384 已从原始保号核证明：令 \(U=A/(1-K)\)、\(y=1-2x\)、\(t=yz\)、\(\mathcal P=y U((1-y)/2,yz)=N/E\)，写
\(N=\sum N_j(z)y^j,\ E=\sum E_j(z)y^j,\ E_0=1-5z/4\)，
\(\mathcal P=\sum g_j(z)y^j/E_0(z)^{j+1}\)，\(g_0=1\)。有精确有限展开

\[
H_r(u)=\sum_{j=0}^{r}\sum_{m=0}^{2j}
g_{j,m}5^{r-m}4^m
\binom{r+u-m+j}{j}\binom{2(r+u)-j}{r-j},\quad
g_j(z)=\sum_{m=0}^{2j}g_{j,m}z^m. \tag{4}
\]

各项关于 \(u\) 的次数不超过 \(r\)。在 \(z_0=4/5\)，精确递推

\[
g_j=N_jE_0^j-\sum_{i=1}^{j}E_i\,g_{j-i}E_0^{i-1} \tag{5}
\]

给出 \(g_j(z_0)=a^j\)，其中 \(a=-E_1(z_0)=-4/5-16\theta/25\)，\(2+a=\lambda\)。这正是 R384 的最高项证明。

为取次高项，直接由原始十二支路计算前三个 \(t\)-分次：
\(K^{(1)}(x)=3x-x^2\)，
\(K^{(2)}(x)=4x^2-8(1+\theta)x^3\)，
\(K^{(3)}(1/2)=-11/16\)。
原始 \(A^{(1)}(x)=1-2x\)，所以 \(N_1(z)=0\)。
逐项代入 \(E=(1-K((1-y)/2,yz))/y\) 得

\[
E_1(z)=z+\theta z^2,\qquad
E_2(z)=z/4-(1+3\theta)z^2+(11/16)z^3.
\]

特别地 \(E_2(z_0)=-(11+240\theta)/125\)。
记 \(e=E'_1(z_0)=1+8\theta/5\)，
\(d=E'_0(z_0)=-5/4\)，
\(h=-E_2(z_0)d=-(11+240\theta)/100\)。
在 (5) 求一次 \(z\) 导数，因 \(E_0(z_0)=N_1(z_0)=0\)，只保留 \(i=1,2\) 项，归纳得到

\[
g'_j(z_0)=-j e a^{j-1}+(j-1)h a^{j-2}\quad(j\ge1).\tag{6}
\]

\(j=1\) 的第二项按零理解，绝不调用 \(a^{-1}\)。这些都是形式多项式恒等式，没有取近似极限。

在 (4) 中设 \(n=r-j\)，从有限二项乘积直接读出两个因子的次高 \(u\) 系数分别为

\[
\frac{j[r-m+(j+1)/2]}{j!},\qquad
\frac{2^n}{n!}\frac{n(3r-j+1)}4.
\]

端点 \(j=0,n=0\) 相应项取零。利用
\(\sum_m g_{j,m}z_0^m=g_j(z_0)\)、
\(\sum_m m g_{j,m}z_0^m=z_0g'_j(z_0)\)，
得到完全有限的求和式

\[
[u^{r-1}]H_r=\frac{5^r}{r!}\sum_{j=0}^r\binom rj 2^{r-j}
\left\{\left[j\left(r+\frac{j+1}{2}\right)
+\frac{(r-j)(3r-j+1)}4\right]a^j
-jz_0g'_j(z_0)\right\}. \tag{7}
\]

代 (6)，对 \((a+2)^r=\lambda^r\) 作最多两次形式微分并直接展开（不要求 \(\lambda\neq0\)），严格等于

\[
\frac{5^r}{(r-1)!}\left\{
\lambda^{r-1}\left[(r+1)a+\frac{3r+1}{2}+z_0e\right]
+(r-1)\lambda^{r-2}\left[\frac{a^2}{2}-\frac a2+z_0ea-z_0h\right]\right\}.
\]

两个方括号分别化简为 \(F_r\) 和 \(G\)，即 (1)。代入 \(\theta=15/8\) 及 R384 最高项结果给出 (2)。对 \(r\ge4\)，\(L_{r-1},L_r,L_{r+1}\) 的次数上界分别是 \(r-3,r-2,r-1\)，两个乘积都不超过 \(2r-4\)，故 (3)。证毕。

## 验证、边界与来源

在同 PR 中原始带符号核复现源码 R384_verify.py 上，8 个精确有理参数 \(-1/2,0,1/2,901/1000,902/1000,1,15/8,2\)，对全部 \(r=1,\dots,16\) 的最高与次高普通单项式系数完成 **256 项精确 Fraction 等式核验**，执行输出 R385_EXACT_PASS。有限核验用于实现回归，不是全指标推理来源。在 \(\theta=0\)，式 (1) 与既有 R353 比值 \([u^{r-1}]H_r/[u^r]H_r=r(7r+3)/10\) 一致。

原始核：R346 Git blob 1579ceb717ab1945227eca4f7a1878bf4ffa73e1；R384 全指标形式抽取及最高 Catalan 系数：commit 3cac53a3d4676e7ab0d54869d9537a971c8b091c，proof Git blob cd741b2848b88a271a782ba8e68342d537866ae4；本轮冻结 Global-Knowledge main@487467135ddd23b9886f382877e2836dd6ab4c1a、Enterprise Math main@8e7fff08126ca1224c1f28a63d9f8e72e733a8c0。P000 与 ACTIVE 世界观未修改。Gateway 研究权限报告 false、owner inventory 返回 CONTROL_QUOTA；没有 native CLAIM、Source Result、Research Activity 正式登记或独立 Driver 审阅。研究原稿与完整128组机器数据保存在对应可下载证书包中。

下一问题：验证并证明或反驳所有余阶的 Sheffer 型式 \(\sum_{r\ge0}H_r(u;\theta)s^r=A_\theta(s)B_\theta(s)^u\)。小余阶算例支持，但全指标未证；若成立，\(\theta=15/8\) 时 \(B_\theta'(0)=0\) 可导出半次数上界。也可独立推进第16余阶33项有限 PF₂ 参数相图。
