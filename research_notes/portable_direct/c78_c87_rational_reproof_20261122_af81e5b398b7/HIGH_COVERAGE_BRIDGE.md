# C78 原全库存的高覆盖有理一阶库存桥

日期：2026-11-22（Asia/Hong_Kong）
来源：enterprise-math@63eec225728612d1df6c178b516b5ecf4687ee06。
原模型、原 H(0,1)、全部安排与真实三尾均保留。
本定理由本轮有限乘积包络、同步计数和离散 jet 拼接，属于作者侧完整有限代数推导。

## 定理

取整数 h≥16、c≥16，原安排集

\[
\mathcal T_c=\{(V,W)\in\mathbb Z^2:2\le W\le V\le c\},
\qquad |\mathcal T_c|=\binom c2.
\]

定义同一个好集

\[
\mathcal G_{c,h}=
\{(V,W)\in\mathcal T_c:
|\rho_5(c,V)-1|>1/h,\
|\rho_3(V,W)-1|>1/h\}.
\tag{1}
\]

这个集合只依赖 c、h，不依赖后续比较的 b。其大小满足

\[
\boxed{
\frac{|\mathcal T_c\setminus\mathcal G_{c,h}|}{\binom c2}
\le\frac{41}{10h}+\frac{12}{c}.
}
\tag{2}
\]

对每个 (V,W)∈G，令内层三值的两个极端为 z_-<z_+，
rho=rho_5(c,V)、tau=tau_5(c,V)，并按以下方式定义端点 u,v：

- rho<1：u=z_-，v=z_+；
- rho>1：u=z_+，v=z_-。

它们都是由原有限传递得到的正有理数。定义

\[
\mathcal E_{c,V,W}
=-\frac{75}{4}
+\frac{15\rho}{4(1-\rho)}
+\frac{75\tau v}{4(1+\tau v)}
+\frac{15\rho+75\tau u}{4(\rho+\tau u)}
\in\mathbb Q.
\tag{3}
\]

则对所有整数 b≥1 满足 30bh≤c，同一个好集中的每个安排同时满足：

1. g(c,V,W)>1、g(c+b,V,W)>1；
2. 两库存的外层端点排列保持一致；
3. 原真实读数有统一的有理差商界

\[
\boxed{
\left|
\frac cb
\left[
\frac{g(c+b,V,W)-1}{g(c,V,W)-1}-1
\right]
-\mathcal E_{c,V,W}
\right|
\le\frac{5405bh}{c}.
}
\tag{4}
\]

其中 g 始终是完整三尾原 H(0,1)。可等价地将式 (4) 中大括号写成
[g(c+b,V,W)−g(c,V,W)]/[g(c,V,W)−1]。

## 证明

### A. 好集计数

SYNCHRONY_COUNT_CHECK.md 已由本轮有限四次幂乘积证书、有限幂差恒等式和有理求和证明，对 delta=1/h：

\[
N_{out}\le(c-1)[(11/10)\delta c+1+4/c],
\]
\[
N_{in}\le(200/243)\delta c(c+1)+c+21+(325/162)H_c.
\]

并集至多为二者之和；H_c≤c，c≥16，直接得到式 (2)。计数使用原有限 rho，同步带没有换成极限曲线。

### B. 三尾非盲和内层保持

原三尾为

\[
z_j=\frac{a(tA_j+B_j)}{1+atA_j},\qquad a,t>0,
\]
\[
(A_j,B_j)=(3/32,15/32),(3/2,15/8),(6,3).
\]

若三个 z_j 都等于同一个 q，则

\[
B_j=q/a+t(q-1)A_j
\]

使三个 (A_j,B_j) 共线。但三点的有向行列式为

\[
(A_2-A_1)(B_3-B_1)-(A_3-A_1)(B_2-B_1)
=-1215/256\ne0.
\]

故三个终尾值不全相等。好集上 rho_3(V,W)≠1；而内层分式满足

\[
B(z_2)-B(z_1)
=\frac{\tau_3(1-\rho_3)(z_2-z_1)}
       {(1+\tau_3z_1)(1+\tau_3z_2)}.
\]

所以内层映射严格单调，z_-<z_+。这个论证不要求端点差有正的统一下界。

### C. 所有允许 b 上保持外层分支

每个有限乘积满足 0<rho_5<4。好集给

\[
q_0=\frac{\rho}{|1-\rho|}<4h.
\]

外层 a_0=15/4，beta=75/4。因 h≥16，

\[
\max(\beta,a_0q_0)\le15h.
\]

所以 b/c≤1/(30h) 支付 DISCRETE_JET_PROOF.md §5 的条件

\[
b/c\le1/[2\max(\beta,a_0q_0)].
\]

也可直接由有限一阶差分界看出

\[
|\rho_5(c+b,V)-\rho_5(c,V)|
\le(15/4)\rho\,b/c\le1/(2h)
<|\rho-1|/2.
\]

因此外层不会跨过 rho=1，u,v 的排列对所有这些 b 都保持。
外层是严格单调分式，故两个库存的 g 都严格大于1。

### D. 一阶差商及纯分数常数

DISCRETE_JET_PROOF.md 的全有限分式证明给

\[
\left|\frac cb
\left[\frac{g(c+b)-1}{g(c)-1}-1\right]
-\mathcal E_{c,V,W}\right|
\le\frac{K_1(q_0)+K_2(q_0)b}{c},
\]

其中

\[
K_1(q)=\frac{4815+90q}{4},\qquad
K_2(q)=\frac{475260+34485q}{32}.
\]

因为 b≥1、q_0≤4h，且这些函数系数为正，

\[
K_1(q_0)+K_2(q_0)b
\le b[K_1(4h)+K_2(4h)]
=b\frac{513780+140820h}{32}.
\]

另一方面

\[
5405h-\frac{513780+140820h}{32}
=\frac{32140h-513780}{32}\ge\frac{460}{32}>0
\]

，因为 h≥16。代入得到式 (4)。

此处内层端点差在准确分式差中保留，并在相对余项中准确约消。没有把两个非常接近的端点当成同一点，没有把相关安排换成独立样本。证毕。

## 直接后果与范围

对整数序列 c→∞、b=b(c)≥1，若可选整数 h=h(c)≥16 满足
h→∞、b h/c→0，则在原全库存中一个比例趋一的共同好集上，原相对读数差商一致趋近式 (3) 的实际有限有理 Euler 系数。这个系数继续依赖 c,V,W；把它再接到固定极限谱，由本轮乘积包络与后续落点控制支付。

所有有限参数的接受条件和输出均用整数／有理数比较：集合成员判定、g、E、坏比例上界、差商误差都如此。h 可按整数不等式选择，无需求实数根。

本定理完成的是原全库存的高覆盖一阶库存桥。C78 原锐利识别阈值还涉及跨模板的同格碰撞、不同逆分支和退化 Hessian 的全域控制，按那些具体命题继续证明。

## 核验材料

- DISCRETE_JET_PROOF.md：任意阶有限差分、Newton余项及实际g分式余项。
- check_discrete_jets.py / discrete_jet_checks.json：20,046项精确检查通过。
- SYNCHRONY_COUNT_CHECK.md：上面实际有限同步计数的全部常数。
- check_synchrony_counts.py / synchrony_count_checks.json：c=16..64、五种有理delta，共245个完整参数案例全部通过。

