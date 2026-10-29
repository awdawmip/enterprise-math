# R353｜有符号 BRC Newton 最高两阶差分的全指标闭式

2026-10-28。状态：AUTHOR_SIDE_PROOF / FINITE_EXACT_AUDIT / DRIVER_UNREVIEWED / NOT_ADMITTED。

固定来源：GLOBAL_KNOWLEDGE_V1 main@163fdf8de7c64b7144be359707fbcb0fb0e98733；Enterprise Math main@1a4ecdf75121035e7613f78598c88c41c930429f。R348 全指标抽取证明 A1–A5 见 Draft PR #1599、提交 5347e506bd145028d7338e9f7993dcd2a2fed97c；R350 顶差分见 Draft PR #1592、提交 2e5d76989fbce6fef0aa891514bb5045008fe293。原始12项完整有符号 K/J 定义：R346_verify.py Git Blob 1579ceb717ab1945227eca4f7a1878bf4ffa73e1。

**模型范围。** 本结果研究有序六边 BRC 辅助组合递推，不宣称已与心跳世界原生六维 X6 Cell、联合支路及动力学建立保真对应。P000 和 ACTIVE 世界观不变。

## 定理

在仍待独立数学审阅的 R348(A1–A5) 全指标抽取结论

\[
D_{r+u,u}=5^uH_r(u),\quad H_r\in\mathbb Q[u],\quad\deg H_r\le r
\quad(r,u\ge0)
\]

成立的条件下，沿用 R350 已证 \([u^r]H_r=6^r/r!\)。令 \(L_r(v)=5^rH_r(v)\)，\(Q_r(v)=L_r(v+1)L_r(v+2)-L_{r-1}(v+2)L_{r+1}(v+1)\)。对全部整数 \(r\ge1\)：

\[
\boxed{[u^{r-1}]H_r(u)=\frac{6^r}{r!}\cdot\frac{r(7r+3)}{10}}. \tag{1}
\]

\[
\boxed{[v^{2r-1}]Q_r(v)=
 \frac{30^{2r}}{(r!)^2(r+1)}\frac{r(7r+16)}5}. \tag{2}
\]

\[
\boxed{\Delta^{2r-1}Q_r(0)=\frac{17r+11}{10}\,30^{2r}\mathrm{Cat}_r>0},
\quad
\boxed{\Delta^{2r}Q_r(0)=30^{2r}\mathrm{Cat}_r>0}.
\tag{3}
\]

这里 \(\mathrm{Cat}_r=\binom{2r}{r}/(r+1)\)。当 \(r=1\) 时 (1) 为 \(H_1\) 常数项公式。

## 证明

**一、原始带符号核在低阶的精确抽取。**
从 R346 原始12项 K/J 定义逐项展开：

\[
K^{(1)}(x)=3x-x^2,\quad K^{(2)}(x)=4x^2-8x^3,\quad
K^{(3)}(x)=4x^2-8x^3-11x^4.
\]

又 \(J_1(t)=-2t-t^2\)，其余 \(J_s\) 均带 \(t^s\) 因子，因此对 \(A(x,t)=1+t+\sum_{s=1}^{10}J_s(t)x^s\) 有 \([t]A=1-2x\)。沿 R348 的 \(y=1-2x,\ t=yz\)，设 \(\mathcal E=(1-K((1-y)/2,yz))/y=\sum_jE_j(z)y^j\)，\(\mathcal N=A((1-y)/2,yz)=\sum_jN_j(z)y^j\)，严格得到

\[
E_0=1-\frac54z,\qquad E_1=z,\qquad
E_2=\frac z4-z^2+\frac{11}{16}z^3,\qquad N_1=0.
\]

这里 \([t]A(1/2)=0\)，\(K^{(3)}(1/2)=-11/16\)。置 \(z_0=4/5\)，则 \(E_0(z_0)=0\)，\(E'_0(z_0)=-5/4\)，\(E_2(z_0)=-11/125\)，故 \(E_2(z_0)E'_0(z_0)=11/100\)。

**二、分子在极点处的导数递推。**
由 R348(A2)，\(g_0=1\)，\(\deg g_r\le 2r\) 且

\[
g_r=N_rE_0^r-\sum_{j=1}^r E_jg_{r-j}E_0^{j-1}.
\]

R350 已证 \(g_j(z_0)=a^j,\ a=-4/5\)。求导并代入 \(z=z_0\)：对 \(r\ge2\)，第一项导数消失，和式只余 \(j=1,2\)，所以

\[
g'_r(z_0)=-a^{r-1}+a\,g'_{r-1}(z_0)-\frac{11}{100}a^{r-2}.
\]

由于 \(N_1=0\)、\(g_1=-E_1=-z\)，有 \(g'_1(z_0)=-1\)。归纳可得

\[
g'_j(z_0)=-j a^{j-1}-\frac{11}{100}(j-1)a^{j-2}\quad(j\ge2);
\qquad g'_1(z_0)=-1,\quad g'_0=0.\tag{4}
\]

**三、H 的次高项是可求和的有符号二项式矩。**
由 R348(A5)（此处仍是显式条件）：

\[
H_r(u)=\sum_{j=0}^r\sum_{m=0}^{2j}
g_{j,m}5^{r-m}4^m
\binom{r+u-m+j}{j}\binom{2(r+u)-j}{r-j},
\qquad g_j(z)=\sum_mg_{j,m}z^m.
\]

两个二项多项式乘积的次高项与最高项之比为

\[
j\left(r-m+\frac{j+1}{2}\right)
+\frac{(r-j)(3r-j+1)}{4}.
\]

注意求和变量 \(m\) 使用 \(z_0=+4/5\)，而 \(a=-4/5\) 是 \(g_j(z_0)=a^j\) 的值，不能将其误置为系数抽取自变量。准确恒等式是

\[
\sum_m g_{j,m}z_0^m=g_j(z_0)=a^j,\qquad
\sum_m m g_{j,m}z_0^m=z_0g'_j(z_0).
\]

定义有符号的 \(w_j=5^r2^{r-j}a^j/[j!(r-j)!]\)，令 \(b_r=[u^{r-1}]H_r\)，\(a_r=[u^r]H_r=6^r/r!\)。代入 (4) 并整理，得到

\[
b_r=\sum_{j=0}^r w_j\left\{\frac{3r^2+r+j-j^2}{4}\right\}
-\frac{11}{100a}\sum_{j=2}^r j(j-1)w_j.
\]

由于 \(\sum w_j=a_r\)，而且由 \((2+a)^r\) 的有限求导恒等式

\[
\frac{\sum j w_j}{a_r}=-\frac{2r}{3},\qquad
\frac{\sum j(j-1)w_j}{a_r}=\frac{4r(r-1)}{9},
\]

所以

\[
\frac{b_r}{a_r}
=\frac{r(23r+13)}{36}+\frac{11r(r-1)}{180}
=\frac{r(7r+3)}{10}.
\]

这是有符号的代数恒等式；这里并未把 \(w_j\) 当作概率。于是 (1) 成立。

**四、Q 的次高项与 Newton 换基。**
记 \(\alpha_r=30^r/r!\)，\(t_r=r(7r+3)/10\)，故 \(L_r(v)=\alpha_r(v^r+t_rv^{r-1}+\cdots)\)。当 \(r=1\) 使用 \(L_0=1,t_0=0\)。平移 \(v\mapsto v+c\) 令相对次高项增加 \(rc\)。直接展开 Q 的两个乘积：

\[
[v^{2r}]Q_r=\alpha_r^2-\alpha_{r-1}\alpha_{r+1}
=\frac{\alpha_r^2}{r+1},
\]

\[
\frac{[v^{2r-1}]Q_r}{[v^{2r}]Q_r}
=4r+2(r+1)t_r-r(t_{r-1}+t_{r+1})
=\frac{r(7r+16)}5.
\]

这给出 (2)。多项式有限差分恒等式 \(\Delta^n(v^n)(0)=n!\) 与 \(\Delta^{n-1}(v^n)(0)=(n-1)!\binom n2\) 蕴涵

\[
\frac{\Delta^{2r-1}Q_r(0)}{\Delta^{2r}Q_r(0)}
=\frac{\tfrac{r(7r+16)}5+\binom{2r}{2}}{2r}
=\frac{17r+11}{10}.
\]

结合 R350 的顶差分 Catalan 恒等式得到 (3)，证毕。

## 精确有限审计与继承边界

随附 R353_VERIFY.py 重新使用完整12项有符号 K/J 定义，从 \(B_0,\ldots,B_{77}\) 和原始 \(D\) 提取 \(H_0,\ldots,H_{25}\)。实际执行命令 python R353_VERIFY.py --max-r 24 对全部 \(r=1,\ldots,24\) 逐条核对 (1)、(3)，同时检查有限范围内全部 Q Newton 差分严格正；24/24 PASS。证据在 R353_EVIDENCE_SUMMARY.json，完整机器证据由程序输出 R353_EVIDENCE.json。使用任意精度整数与 Fraction，没有浮点判号。所提交源码 Git Blob 6ce5cca30c3aea9fc0f1efa184e365b2c54aeac0 与本轮实际执行本地源码字节相同。

新结果证明对所有 \(r\ge1\) 最高与次高的 Newton 差分正性；对其他 \(0\le j\le2r-2\) 的全指标正性仍需独立研究。它不单独证明第334条完整余阶带、二维全域 TP₂ 或原生 X6 物理动力学。R348(A1–A5) 是本证明的待独立审阅载重依赖。

下一判别单元：求第三高 Newton 差分的全指标表达及严格符号，检查是否需要 K/J 四阶系数与 \(g''_j(z_0)\)；如有完整新系数证书，再独立执行 Q334 的669项精确计算。
