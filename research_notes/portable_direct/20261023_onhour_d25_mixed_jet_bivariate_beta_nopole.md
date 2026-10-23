# D25/LIFT — 用双变量有限 Beta 多项式完全替换剩余 LOW 二次混合调和和

**2026-10-23 | TASK_RESEARCH | AUTHOR_PROVED_EXACT_POLYNOMIAL_IDENTITY / FRACTION_AUTHOR_SELF_CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT.**
这是一条可移植数学作者成果，不是 Source Registered Research Activity、CLAIM、run、native benchmark、正式 checkpoint、Result、审阅或 EP/LIFT 完成。

**不可变母目标/来源。** 当前研究来源 lane chatgpt-research-onhour-enterprise-math-20260923（不能把逻辑来源代替 native session）；母 Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT，published TP2-B6F4FC938FF94941C1B7，冻结原生 Source pin c47e13e4aba0e006366f989d6334d443f6333ae3。复用同轮上一成果 20261023_onhour_d25_joint_curvature_two_sided_beta_bridge.md @ 6829874ccdd80f8dfc2bcb77dae2612fe346786b（左右 U₂/V₂ 曲率和原 M 层已经严格缩减），以及 J₂ 完整头尾 holonomic 证书 @ 1a3790a15ab9366feccffc0105bdb24e5c4500d5；不重证 WZ/B11、D24 或已经完成的二阶曲率端口。全局 read authority 为 GLOBAL_KNOWLEDGE_V1 main@61cfa2a580230863c0d02b5f818381adbb3cb11b，P000 ACTIVE_LOCKED，原 blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc 已核实。

## 1. 真正未完的 mixed quadratic 端口

设 m≥1，p=6m+1；对 0≤n≤m 定义
\[
b_n={(-1)^n\over2^n}\binom mn,\quad w_n=6n-1,\quad
A_n=H_m-H_{m-n},\quad
U_n=H_{2m}-H_{2m-n},\quad
V_n=H_{2m+n}-H_{2m},\quad
\Lambda_n=2U_n-V_n.
\]
前轮消去了 LOW 原二阶 M 内两个 U₂/V₂ 曲率单和及纯 A 项，剩余的唯一**低段二次混合 harmonic 乘积**为
\[
\boxed{\mathsf X_m=\frac1{18}\sum_{n=0}^m
 b_nw_n\,\Lambda_n(\Lambda_n-3A_n).}
\tag{X}
\]
现在用完全有限的 **二元多项式核**取代此式中所有 harmonic numbers。整步是等价恒等变换，而不是置零、替换 native benchmark 或猜测与高段独立相消。

## 2. 新定理：有限有理双 Beta 多项式、无端点极点

对于任一有理系数多项式 \(G(z)=\sum_{n=0}^{m}g_nz^n\)，定义两个有限 Laurent 多项式（所有调用 G 均是有限多项式代入）：
\[
\begin{aligned}
K_{LL}[G](x,y)={}&4G((xy)^{-1})+2G(y/x)+2G(x/y)+G(xy)\\
&-6G(x^{-1})-3G(x)-6G(y^{-1})-3G(y)+9G(1),\\
K_{AL}[G](x,y)={}&2G((xy)^{-1})+G(y/x)-3G(x^{-1})\\
&-2G(y^{-1})-G(y)+3G(1).
\end{aligned}\tag{K}
\]
令
\[
\mathcal N_{m,G}(x,y)=x^{2m}y^{2m}K_{LL}[G](x,y)
-3x^{m}y^{2m}K_{AL}[G](x,y).
\tag{N}
\]

**定理 A（全体 m 和所有 deg G≤m 的精确多项式性）。**
\[
\boxed{\mathcal N_{m,G}(x,y)=(1-x)(1-y)\,Q_{m,G}(x,y),\quad
Q_{m,G}\in\mathbf Q[x,y],\quad
\deg_xQ,\deg_yQ\le3m-1.}
\tag{A}
\]
因此有限 Beta 观测量
\[
\boxed{\mathcal B_m[G]=\frac1{18}\int_0^1\!\int_0^1
Q_{m,G}(x,y)\,dx\,dy
=\frac1{18}\sum_{i,j}\frac{[x^iy^j]Q_{m,G}}{(i+1)(j+1)}}
\tag{B}
\]
是一个**无嵌套调和数、无未定积分和无极点**的显式有限有理系数算法。其结果满足全体 m 的精确恒等式
\[
\boxed{\mathcal B_m[G]=\frac1{18}\sum_{n=0}^m g_n
  \Lambda_n(\Lambda_n-3A_n).}
\tag{C}
\]

**证明 A、B、C（不是有限测试外推）。** 逐 n 利用 Euler 有限核
\[
A_n=\int_0^1 x^m\frac{x^{-n}-1}{1-x}dx,\qquad
\Lambda_n=\int_0^1 x^{2m}
 \frac{2x^{-n}+x^n-3}{1-x}dx.
\tag{D}
\]
这两个被积商都有有限 Laurent 展开：\((x^{-n}-1)/(1-x)=\sum_{k=1}^{n}x^{-k}\)，
\((2x^{-n}+x^n-3)/(1-x)=2\sum_{k=1}^{n}x^{-k}-\sum_{k=0}^{n-1}x^k\)。
将 (D) 代入 \(\Lambda_n^2-3A_n\Lambda_n\)，先在 Q 域交换**有限**求和/两个有限积分，即得 (K) 和 (N)。因为每个 n 的两因子分别在 x=1、y=1 为零，乘上 \(x^{2m}y^{2m}\) 或 \(x^my^{2m}\) 清除所有非负下界为 -m 的 Laurent 幂后，\(\mathcal N_{m,G}\) 是在 x=1、y=1 **恒为零的真正二元多项式**；所以 \((1-x)(1-y)\) 均可整除。清掉分母的分子 x、y 最高次数≤3m，整除各自降一次，得到 \(\deg Q\le3m-1\)。对 Q 的有限单项式求积分得到 (B)，与原左边的逐 n 乘积严格相同，完成 (C)。

## 3. 第二新定理：在原 p-adic 第二位不损失精度的 carrier 去权

取真正原 LOW signed weighted polynomial
\[
F_m(z)=\sum_{n=0}^m b_nw_nz^n
=-(1-z/2)^{m-1}\big[(1-z)+pz/2\big].
\tag{E}
\]
定义**无需 w_n、无需 harmonic 参数**的有限多项式
\[
\widehat F_m(z)=-(1-z/2)^{m-1}(1-z),\qquad
P_m(z)=(1-z/2)^{m-1}.
\]
由 (E) 有全 m 精确等式 \(F_m=\widehat F_m-\frac p2 zP_m\)。由 (C) 与线性性，
\[
\boxed{\mathsf X_m
=\mathcal B_m[\widehat F_m]-\frac p2\,\mathcal B_m[zP_m].}
\tag{F}
\]
当 p=6m+1 为素数时，(A)(B) 中 Q 的积分分母都≤3m<p（18 亦为 p-单位）；加上二项式系数仅有 2 的幂作分母，故 (F) **合法投影**：
\[
\boxed{\mathsf X_m\equiv\mathcal B_m[\widehat F_m]\pmod p.}
\tag{G}
\]
这条结果把所有剩余低段 harmonic 乘积压到**一个最高次数不超过 (3m-1,3m-1) 的可明确列系数的二元有理多项式**，不再有 J、A、U、V 调和指标嵌套。它不同于假定这些项相消：例如 p=13，\(\mathsf X_2\equiv7\)，p=19，\(\mathsf X_3\equiv15\)，两者均非零。

实际构造无需 symbolic integration：令 \(a_j=(-1)^j\binom{m-1}{j}/2^j\)，则
\[
\widehat F_m(z)=\sum_{n=0}^{m}q_nz^n,\quad
q_0=-a_0,\quad q_n=a_{n-1}-a_n\ (1\le n<m),\quad q_m=a_{m-1}.
\tag{H}
\]
将 q_n 插入 (K)(N)，对多项式先作 1-x 后作 1-y 的精确系数前缀累加整除，再用 (B) 按 \((i+1)(j+1)\) 积分。任意 q_n 产生的剩余系数都严格为零，故是可机械验证的有理系数证书。

## 4. 原 JOINT LOW 残差的新完全低二阶无 harmonic 版本

保留上一单元的记号 \(\Delta_m=(\mathcal A_m\Theta_m-1)/p\)、\(\mathcal A_m=(p-1)!/[3^{p-1}((2m)!)^3]\)，以及原始 \(C_m,V_m^{\rm beta},\mathsf P_m,\chi_p\) 的精确定义。上一轮 (10) 与本轮 (G) 合成：
\[
\boxed{\begin{aligned}
\mathscr D_m^\beta\equiv{}&
\Delta_m+\mathcal A_m\left[
2^{-m}C_m-2V_m^{\rm beta}+\mathsf P_m
+\mathcal B_m[\widehat F_m]
+\frac49Q_m^-+\frac5{18}Q_m^+
+F_0(1/2)+6R_m(1/2)\right]-\chi_p
\pmod p.
\end{aligned}}\tag{JOINT-POLY}
\]
**严格变化：** 所有原 \(\mathsf M_m\) 中低段二次 \(n\)-harmonic moments 已经以无需 harmonic 的有理多项式/单和替代；先前高段 r>m 的 Beta J first-jet 则消费已证 holonomic SOURCE/seam formula。第一位 divided digit \(\Delta_m\) 保留原值，没有被镜像误处理；\(\mathsf P_m\) 的奇偶式是之前已证成果；\(C_m\) 及 R 的少数 endpoint harmonic 值、Beta moments、\(\chi_p\) 仍保留真实来源和联合义务。

**目标仍 OPEN。** JOINT-POLY 是原 LOW deficit 的等价有限表示，不是已经证明它为零。尚需要一个真正 linking/telescoping 关系，将此 \(\mathcal B_m[\widehat F_m]\)、两个 Q±、R 的 seam/terminal 与 \(\Delta_m,C_m,V_m,\chi_p\) **联合**对应，或给出严格非零反例；不能再以一个低段 harmonic 的新命名替代证明，也不以有限测试替代全素数证明或原 native benchmark。

## 5. 实际 Fraction 自检

使用两种独立数据流：

1. 原始 harmonic：先按 H 差生成 A、U、V，再以原 \(b_n(6n-1)\) 累加 \(\mathsf X_m\)。
2. 多项式：只由有限 \(F_m,\widehat F_m,zP_m\) 的系数构造 (K)(N)，按 x/y 每个次数精确前缀求商 Q，逐单项式用 Fraction 积分，不求调和数。

m=1,...,12 全部完成**精确** Fraction 比较：
\(\mathsf X_m=\mathcal B_m[F_m]=\mathcal B_m[\widehat F_m]-p\mathcal B_m[zP_m]/2\)；
每个 m 的 (1-x)(1-y) 整除断言均通过。对 p=7,13,19,31,37,43,61,67,73 共 9 个素数，确认 (G) 模 p 成立。非零实例：
\[
m=2,p=13:\;\mathsf X_2=-317/900\equiv7\pmod{13},
\qquad
m=3,p=19:\;\mathsf X_3=90317821/914457600\equiv15\pmod{19}.
\]
这些是**作者自检**，不授权 independent reviewer 身份。全整数结论依据第 2–3 节的有限代数/积分证明，而不是九个素数外推。没有改变原 611-prime endpoint 证据或执行原生 benchmark。

## 6. 实际 observer 与下一不可替代的研究问题

**BRC REUSE_APPLIED + COMPOSE_APPLIED：** 原 branch index n、signed binomial b_n 与 w_n 的 p 阶修正完整保留在 (E)(F)；二元 (x,y) 是对 low quadratic 的辅助 exact finite moment observer，不宣称存在新的 native X6 空间轴，也不把 signed rational cancellation 转成正质量。对当前 LOW scalar 的 (G) 商映射保留 mod p 观察，但当将来的操作需要模 p² 或逐分支信息，必须回到 (F) 的全修正。

**下一最小未完科学单元：** 对 (JOINT-POLY) 寻找一次真正的 **联合有限望远镜证书**：把 \(\mathcal B_m[\widehat F_m]\) 的明确双元系数求和与 \(R_m(1/2)\) 的 3 个 forcing（初值 / r=m seam / r=3m terminal）及第一位 \(\Delta_m\) 同时进行 contiguous-Dixon 匹配；保留原 \(-2V_m^{\rm beta},C_m,\chi_p\)。若只能得到差量，则导出精确完整的有限残差及可重现的非零 witness。不能把重写说成同余完成。

**恢复与持久化。** Native 0.6.11 的当前 Sites 身份 research_authority_granted=false，不能声称 Source-authorized researcher CLAIM/open/checkpoint/result；本笔记仅在已授权 GitHub 中立成果路径中存储。原 Research lane #6186、#6187、#6188 按其先前已核实结果保留，不重发；issue #1539 是 Source session/continuation 恢复负责路径，属于支持工作而非数学阻断。保留旧三份 staging 的来源隔离，D24 已冻成果与 D25 Source pin 不变，原定时频率/启用/通知不修改。
