# AP 形变的无再交叉圆盘与六个不可约余因子

对所有 $m\ge2$，冻结的 AP 树余子式在 $0<|t|\le 2^{-38m}$ 无零点。因此真实归一化算子在该区间的实正部分只有规定的一条不动方向。对 $11\le m\le16$，另有独立的算术结论：删掉 $t^{m-1}$ 后，整条形变的余因子在 $\mathbf Q[t]$ 不可约。由此排除 $0<t\le1$ 的全部低次代数再交叉，包括有理参数和右端点 $1$。仅凭该不可约性还允许表列次数的代数根；同批的实区间证书另行排除了 $2\le m\le20$ 的全部再交叉。

## 冻结对象

令 $n=m-1,b=m^2,x_i=i+1,y_j=mj,w_j=(-1)^j\binom nj$，下标为 $0,\ldots,n$。原矩阵
$$
H_t(i,j)=\sum_{s=0}^n {(-1)^s\binom ns t^s\over x_i+y_j+bs}
$$
给出 $e=H_tw,d'=H_t^Tw,E=\operatorname{diag}(e),D=\operatorname{diag}(d'),W=\operatorname{diag}(w)$，$K=D^{-1}H_t^TW E^{-1}H_tW$。令 $L$ 为两部有符号图的 Laplacian，边权 $w_i w_j H_t(i,j)$，$\tau_m$ 为删去最后行列的主余子式。冻结同余和 Schur 补给出，在实区间 $0<t\le1$，$\tau_m\ne0$ 当且仅当除常数外没有不动方向。两组边缘权的无符号归一化因子 $e_i,d'_j$ 都有严格正的积分表达式，且 $w^TH_tw=\int_0^1(1-u)^n(1-u^m)^n(1-tu^b)^n du>0$。以下复数域结论直接针对多项式 $\tau_m=t^n q_m$，无需在复数上解释所有归一化因子。[原任务书](https://github.com/awdawmip/enterprise-math/blob/e7b9fb5084f93a9b2dbc16225629b667fb7bf46c/research_tasks/PERFECT_PRIME_AP_CHRISTOFFEL_J_TRANSVERSALITY_DEFORMATION_20260830.md) · [局部交叉、非正规导数反例及适用域](https://github.com/awdawmip/enterprise-math/blob/e7b9fb5084f93a9b2dbc16225629b667fb7bf46c/research_returns/PERFECT_PRIME_AP_CHRISTOFFEL_J_TRANSVERSALITY_DEFORMATION_RETURN_20260830.md)

更精确地，令 $U_0=WE,V_0=WD$，归一化商行列式有额外因子 $w^TH_tw/(\det U_0\det V_0)$，乘上 $\tau_m$ 即得 $\det(I-Q_{m,t})$。例如 $m=2$ 时 $q_2=(13-5t)/1260$，$w^TH_tw=(350-13t)/840$。取实区间外的 $t=350/13$，$U_0,V_0$ 都可逆，$q_2=-527/5460$，归一化商行列式却为零。这说明推广到其他数域时需具体指定余子式。[归一化与冻结化约](https://github.com/awdawmip/enterprise-math/blob/e7b9fb5084f93a9b2dbc16225629b667fb7bf46c/research_returns/PERFECT_PRIME_AP_FIXED_POINT_COMPOUND_RESULT_REFREEZE_V2_RETURN_20260831.md)

## 一、全参数的定量邻域

**定理。** $m\ge2$ 时，$q_m(t)\ne0$ 对 $|t|\le2^{-38m}$ 成立。证明使用实际 $s=0,\ldots,n$ 各层的有限差分，给出一个衰减仅为单指数的保守半径。以下范数均为欧氏算子范数。

写 $c_{js}=n!/\prod_{a=1}^m(y_j+bs+a)$ 及 $c_*=c_{0,1}$。原多项式坐标中，除去共同常数后的型由各项 $w_j(-1)^s\binom ns c_{js}t^s[g(y_j+bs)-f(y_j)]^2$ 叠加而成，$\deg g,\deg f\le n$。这是冻结的割线表示，与删行列余子式相差非零常数行列式因子。[冻结割线同余式 (2.1)](https://github.com/awdawmip/enterprise-math/blob/1559dad7422d9ebcd9579ffaa9e53030a0e9540f/research_returns/PERFECT_PRIME_AP_RESIDUAL_MOBIUS_BERNSTEIN_COEFFICIENT_POSITIVITY_RETURN_20260903.md)

令 $v_j=f(y_j)-g(y_j)$，$h_j=g(y_j+b)-g(y_j)$。模共同常数，$(v,h)$ 遍历 $\mathbf C^m\oplus U$，其中 $U=\{h:w^Th=0\}$。理由是步长 $b$ 差分把 $\mathcal P_n/\mathbf C$ 同构到 $\mathcal P_{n-1}$，后者在节点上的取值恰占 $U$。令 $T_sh$ 表示步长 $bs$ 的差分取值。若 $P(j)=h_j$ 是次数至多 $n-1$ 的插值多项式，则 $(T_sh)_j=\sum_{a=0}^{s-1}P(j+ma)$。特别 $T_0=0,T_1=I$。

原型除以 $c_*$，取任意复平方根 $z^2=t\ne0$，以 $(v,h/z)$ 作合同变换。所得矩阵常数主部是
$$
M_0=\operatorname{diag}\!\left(\operatorname{diag}(w_j c_{j0}/c_*),\;-n\operatorname{diag}(w_j\rho_j)|_U\right),\qquad
\rho_j=c_{j1}/c_* . \tag{1}
$$
这里的限制为正交压缩，$U$ 取实正交基再复化。$c_{j0}\ge c_*$，且 $2^{-m}\le\rho_j\le1$，后一界源于 $y_j<b$。写 $D_1=\operatorname{diag}(w_j\rho_j)$。压缩的逆由下式限制到 $U$ 给出
$$
 D_1^{-1}-\frac{D_1^{-1}ww^TD_1^{-1}}{\delta},
 \qquad
 \delta=w^TD_1^{-1}w=(-1)^n c_*m^m(3m^2+1)/2. \tag{2}
$$
最后一式是 $P(x)=\prod_{a=1}^m(x+a)$ 在 $x=b$ 的 $n$ 次步长 $m$ 差分乘 $(-1)^n c_*/n!$，只需 $P$ 的两个最高次项。公式 (2) 的矩阵两侧都消去 $w$，与 $D_1$ 相乘会在 $U$ 上留下恒等映射的正交投影。

由 $c_*m^m\ge n!/(m+1)^m\ge32^{-m}$ 可得 $|\delta|\ge32^{-m}$。这里用 $n!\ge(n/3)^n$、$n/(m+1)\ge1/3$ 及 $m+1\le2^m$。因此
$$
 K=\max\left(1,{1\over n}\left[\max_j |w_j\rho_j|^{-1}
        +{\sum_j\rho_j^{-2}\over |\delta|}\right]\right)
 \ \ge\|M_0^{-1}\|,\qquad K\le2^{9m}. \tag{3}
$$

设 $B_s=\binom ns\max_j |w_j|c_{js}/c_*$，$r=|t|\le1$。第 1 层除其常数块后仅余 $vv$ 块和交叉块。从第 2 层起，每层是矩阵 $( -zI,T_s)$ 的加权转置平方乘 $t^{s-1}$。复数转置积依然满足算子范数乘积上界。因此余项的范数至多
$$
 E_m(r)= B_1(r+2\sqrt r)+
 \sum_{s=2}^n B_s r^{s-1}(\sqrt r+\|T_s\|)^2 . \tag{4}
$$
凡 $K E_m(r)<1$ 即可用 Neumann 级数证闭圆盘无零点；在 $t=0$ 用 $q_m(0)>0$。

给出 (4) 的统一估计。在 $0,\ldots,n$ 上用 Lagrange 插值，对每个移位节点 $j+ma$，基函数绝对值总和至多 $[2m(s+1)]^n/n!$，这是把分母 $i!(n-i)!$ 直接求和的结果。故
$\|T_s\|\le s\sqrt m[12(s+1)]^n\le 2^{6ms}$，且所有 $B_s\le 2^{2m}$。在 $r=2^{-38m}$ 处，自第 2 层起的上界取几何级数，公比 $2^{12m}r\le 1/2$，遂有 $E_m(r)\le3\,2^{-17m}+2^{3-12m}$。乘上 (3) 小于 1，定理得证。保留逐层常数可增大这个半径。例如 $m=2,5,11,16,20$ 得到的闭圆盘半径依次为 $2^{-8},2^{-30},2^{-82},2^{-126},2^{-162}$。这些数是以 (4) 保证的下界，未优化。

## 二、坏参数的素数支撑

$d=n(2m-3)$ 是 $q_m$ 的次数。前次两端割线和给出
$$
 q_{m,0}=\frac{n^n m^{n(n+3)+m}(n!)^{2m}(3b+1)\prod_j\binom nj^2}{2(2b)!},
 \quad (-1)^d\frac{q_{m,d}}{q_{m,0}}
  =\frac{(m-1)^2(2m+1)}{(3b+1)\binom{m^3}{2b}} . \tag{5}
$$
该式也可由冻结割线行列式的两端直接取得。最低总层数需 $n$ 个组各取 $\{0,1\}$，余组取 $\{0\}$；最高端反射各组选层。组内附加差分的首项系数为 $\pm k b$，余下是删去单点组的 Vandermonde。其平方求和正给 (2) 使用的交错差分，末端把步长位置换至 $b(n-1)$。[两端系数的推导](../sixteenth/bernstein.md) · [冻结割线式 (6.2)](https://github.com/awdawmip/enterprise-math/blob/1559dad7422d9ebcd9579ffaa9e53030a0e9540f/research_returns/PERFECT_PRIME_AP_RESIDUAL_MOBIUS_BERNSTEIN_COEFFICIENT_POSITIVITY_RETURN_20260903.md)

**定理。** 当 $m\ge3$，每个非零代数零点 $\alpha$ 的所有 $p$ 进赋值在 $p>m^3$ 时均为零。原边权的分母介于 1 和 $m^3$，故 $q_m\in\mathbf Z_{(p)}[t]$。首尾系数由 (5) 都是 $p$ 进单位，因 $3m^2+1\le m^3$ 对 $m\ge4$ 成立，$m=3$ 时该数为 $28$。若 $v(\alpha)>0$，常数项具有唯一最低赋值；若 $v(\alpha)<0$，最高项具有唯一最低赋值。两种情形均排除抵消。$m=2$ 时 $q_2(t)\propto13-5t$，有大素数 $13$ 例外。

于是对固定 $m\ge3$，实区间里既约分数的分子或分母只要含大于 $m^3$ 的素因子，便有无再交叉证书。例如两族 $p/(p+1)$ 与 $(p-1)/p$ 均趋于 1。更一般地，高度 $\le H$ 的有理数中，尚未被此判据排除的正分数至多 $O_m((1+\log H)^{2\pi(m^3)})$ 个，因为分子、分母的每个小素因子指数都有对数上界。

## 三、整个残差在有理数上的不可约证书

**有限定理。** 下表六个 $q_m(t)$ 在 $\mathbf Q[t]$ 中不可约。表内第一素数还使 $q_m$ 的齐次化在 $\mathbf P^1(\mathbf F_p)$ 无零点，故 $q_m$ 在相应的 $\mathbf Q_p$ 上无零点。

| $m$ | $d$ | 依次使用的素数 | 每步后仍可能的有理因子次数个数（只列 $1,\ldots,\lfloor d/2\rfloor$） |
|---:|---:|---|---|
| 11 | 190 | 1373, 1381 | 7, 0 |
| 12 | 231 | 1753, 1759 | 3, 0 |
| 13 | 276 | 2203, 2207 | 15, 0 |
| 14 | 325 | 2749, 2753, 2767 | 30, 23, 0 |
| 15 | 378 | 3391, 3407, 3413, 3433 | 15, 8, 5, 0 |
| 16 | 435 | 4099, 4111, 4127, 4129 | 23, 1, 1, 0 |

每个 $p>m^3>d$。在每个 $a\in\mathbf F_p^\times$，直接用原 $H_a$ 搭出 $L_a$，删行列求行列式并除以 $a^n$；以 (5) 补上 $a=0,\infty$。用 $0,\ldots,d$ 的差分插值得 $f=q_m\bmod p$，再把 $f$ 对全体剩余类和无穷远点逐一代回核对。对 $1\le k\le\lfloor d/2\rfloor$，计算
$$
 G_k=\deg\gcd(f,X^{p^k}-X)=\sum_{e\mid k}eN_e ,
$$
从小到大求出每个次数 $e$ 的相异不可约因子数 $N_e$。检验 $\gcd(f,f')$ 判无重根；有重根时可用无限重数作保守的次数上包络。因最高系数为 $p$ 进单位，若 $q_m$ 在 $\mathbf Q[t]$ 存在 $k$ 次因子，其首一化后在 $\mathbf Z_p[t]$ 分解为同次数的首一因子，从而 $k$ 必须是模 $p$ 因子次数的子集和。表中把各素数允许的次数集合求交，每行交集为空。这给出不可约性，不要求单个模 $p$ 的多项式不可约。例如 $m=11$ 的两个素数的小次数因子分别为 $8,22,56$ 与 $1,50$，各一次，故非空子集和无交。

有限域证书使这六个 $m$ 的每个代数零点都满足 $[\mathbf Q(t):\mathbf Q]=d$。它单独无法判别高次共轭根所在的实区间。同批的 Bernstein 系数与分段证书给出 $2\le m\le20$ 的 $q_m(t)>0$（$0\le t\le1$），故该范围内实际流在 $0<t\le1$ 全程无再交叉。原次数 HCM0 的全参数严格正性已由 $m=18$ 否定。独立的精确有理插值证出此时原行负格恰为 $279,\ldots,291$，而在 $t=1/2$ 处分出的两段各有 562 个严格正系数。全 $m$ 的实区间无再交叉仍开。[实区间与 HCM0 结果](physical_flow.md) · [精确有理复算](hcm_witness_check.py) · [全行与两段整数证书](hcm_witness_checked.json)

**复算。** 在本目录运行 `python christoffel_check.py`（Python 3、NumPy）。层间插值、逐层半径及压缩逆界用精确分数。有限域运算全用整数，最大卷积长度和模数满足 $d p^2<2^{62}$，输入每次均先约化。证书保存 $m=2,\ldots,20$ 的逐层半径界、六个多项式的 17 组射影视值摘要、各个有限域的因子次数和交集。[复算程序](christoffel_check.py) · [确定性证书](christoffel_checked.json)
