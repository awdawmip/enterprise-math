# P025 补充 08 —— 一个高质量 ABC 状态的精确 Witness Precision

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner：`program/p025-high-quality-witness-exact`  
父依赖：`program/p025-degeneracy-overhead@32756663`  
前人工作状态：arithmetic derivatives / restricted minima / lattice reduction 属于前人工作；本固定状态的精确有限证书是 P025 实例结果

## 1. 目标

此前各补充已经分离出四个有限量：

\[
\lambda_{abc}
\le
\max(\lambda_{abc},\rho)
\le
\mu
\le
U_2,
\]

其中 `lambda_abc` 是 arithmetic-demand floor，`rho` 是普通 additive-lattice first radius，`mu` 是第一个 non-degenerate witness radius，`U_2` 是简单 two-coordinate generator ceiling。

小样本已经证明这些层可以不同。下一步压力测试应该进入真正的 high-quality `abc` 状态，而不是继续增加小三元组。

本补充研究精确恒等式

\[
\boxed{
2+3^{10}\cdot109=23^5.
}
\]

记

\[
a=2,
\qquad
b=3^{10}\cdot109=6{,}436{,}341,
\qquad
c=23^5=6{,}436{,}343.
\]

其 radical 为

\[
\operatorname{rad}(abc)=2\cdot3\cdot23\cdot109=15{,}042.
\]

直接整数比较得到

\[
c^2=41{,}426{,}511{,}213{,}649
>
3{,}403{,}429{,}454{,}088
=\operatorname{rad}(abc)^3.
\]

因此该状态满足 P025 指数 `3/2` 的 rational high-quality predicate。

本补充的主结果是

\[
\boxed{
\mu(a,b,c)=601.
}
\]

证明是一个精确有限 lattice certificate，不使用浮点、对数或无界搜索。

## 2. 精确 arithmetic-demand floor

prime-power 数据为

\[
\begin{array}{c|ccc}
n&\operatorname{rad}(n)&m(n)&\widehat A(n)\\
\hline
2&2&1&1\\
3^{10}\cdot109&327&19{,}683&1{,}093\\
23^5&23&279{,}841&5
\end{array}
\]

其中

\[
\widehat A(n)=
\sum_{p\mid n}\frac{\operatorname{rad}(n)}p v_p(n).
\]

补充 06 给出 normalized complementary capacities

\[
\begin{aligned}
K_{b,c}&=26{,}774,\\
K_{a,c}&=33,\\
K_{a,b}&=2{,}513.
\end{aligned}
\]

于是三个 target demand floor 分别是

\[
\lambda_a=1,
\qquad
\lambda_b=\left\lceil\frac{19{,}683}{33}\right\rceil=597,
\qquad
\lambda_c=\left\lceil\frac{279{,}841}{2{,}513}\right\rceil=112.
\]

因此

\[
\boxed{\lambda_{abc}=597.}
\]

在做任何 lattice reduction 之前，补充 06 的简单 two-coordinate 构造只能给出

\[
\boxed{U_2=59{,}049,}
\]

所以最初的认证区间只有

\[
597\le\mu\le59{,}049.
\]

下文把这个巨大区间几乎全部精确关闭。

## 3. Prime-coordinate generator rows

取有序 prime coordinates

\[
(2,3,23,109).
\]

对 relation-adapted arithmetic derivative，加法条件

\[
d^\psi(a)+d^\psi(b)=d^\psi(c)
\]

的 primitive integer normal 为

\[
\boxed{
\alpha=
(1,\ 21{,}454{,}470,\ -1{,}399{,}205,\ 59{,}049).
}
\]

因为

\[
\begin{aligned}
d^\psi(2)&=x_2,\\
d^\psi(3^{10}\cdot109)
&=21{,}454{,}470x_3+59{,}049x_{109},\\
d^\psi(23^5)&=1{,}399{,}205x_{23}.
\end{aligned}
\]

对 Wronskian orientation `(a,b)`，primitive degeneracy row 为

\[
\boxed{
\beta=(-327,\ 2180,\ 0,\ 6).
}
\]

所以

\[
T=\ker_{\mathbb Z}(\alpha),
\qquad
T^\circ=T\cap\ker_{\mathbb Z}(\beta),
\]

而 `mu` 正是 `T` 避开 `T^circ` 的 restricted first `L_infinity` minimum。Restricted successive minima 属于既有 Geometry-of-Numbers 前人工作 [SRC-HENK-THIEL-2014-RESTRICTED-MINIMA]。

## 4. Additive lattice 的精确 unimodular basis

由于 `alpha` 的第一坐标是 `1`，`T` 有显然的整数基

\[
\begin{aligned}
e_1&=(-21{,}454{,}470,1,0,0),\\
e_2&=(1{,}399{,}205,0,1,0),\\
e_3&=(-59{,}049,0,0,1).
\end{aligned}
\]

使用整数矩阵

\[
U=
\begin{pmatrix}
3&46&0\\
0&23&545\\
-20&-310&-79
\end{pmatrix}.
\]

它的行列式为

\[
\boxed{\det U=-1,}
\]

所以这是 unimodular change of basis，而不是有限指数近似。

得到精确新基

\[
\begin{aligned}
v_1&=(20,3,46,0),\\
v_2&=(10,0,23,545),\\
v_3&=(721,-20,-310,-79).
\end{aligned}
\]

因此每个 `x in T` 都唯一表示成

\[
\boxed{x=Av_1+Bv_2+Cv_3,\qquad A,B,C\in\mathbb Z.}
\]

degeneracy row 在该基上变得极简单：

\[
\boxed{
\beta(v_1)=0,
\qquad
\beta(v_2)=0,
\qquad
\beta(v_3)=-279{,}841=-23^4.
}
\]

所以

\[
\boxed{x\notin T^\circ\iff C\ne0.}
\]

non-degeneracy 被隔离成单个精确整数坐标。

## 5. P025-T24 —— 半径不超过 600 时不存在 non-degenerate witness

反设

\[
x=Av_1+Bv_2+Cv_3\notin T^\circ
\]

且

\[
\|x\|_\infty\le600.
\]

因为 `C\ne0`，beta 方程给出

\[
279{,}841|C|
=|\beta(x)|.
\]

primitive beta row 的 `L_1` norm 为

\[
327+2180+6=2513.
\]

因此

\[
279{,}841|C|
\le2513\cdot600
=1{,}507{,}800.
\]

而

\[
6\cdot279{,}841
=1{,}679{,}046
>1{,}507{,}800,
\]

故

\[
\boxed{1\le|C|\le5.}
\]

把 `x` 换成 `-x` 不改变 radius 与 non-degeneracy，因此可设

\[
1\le C\le5.
\]

### 第四坐标强迫 `B in {0,1}`

由基公式

\[
x_{109}=545B-79C.
\]

所以

\[
|545B-79C|\le600.
\]

当 `1<=C<=5` 时，

\[
\frac{-600+79C}{545}>-1
\]

且

\[
\frac{600+79C}{545}
\le\frac{995}{545}<2.
\]

`B` 为整数，所以

\[
\boxed{B\in\{0,1\}.}
\]

### 剩余十种情况的 `A` 区间全部矛盾

第一、第三坐标为

\[
\begin{aligned}
x_2&=20A+10B+721C,\\
x_{23}&=46A+23B-310C.
\end{aligned}
\]

radius bound 从 `x_2<=600` 给出

\[
A
\le
\left\lfloor
\frac{600-10B-721C}{20}
\right\rfloor,
\]

而从 `x_{23}>=-600` 给出

\[
A
\ge
\left\lceil
\frac{-600-23B+310C}{46}
\right\rceil.
\]

对唯一可能的 `C=1,...,5`、`B=0,1`，精确界如下：

\[
\begin{array}{c|c|c|c}
C&B&A_{\min}\text{ from }x_{23}&A_{\max}\text{ from }x_2\\
\hline
1&0&-6&-7\\
1&1&-6&-7\\
2&0&1&-43\\
2&1&0&-43\\
3&0&8&-79\\
3&1&7&-79\\
4&0&14&-115\\
4&1&14&-115\\
5&0&21&-151\\
5&1&21&-151
\end{array}
\]

每一行都满足

\[
A_{\min}>A_{\max}.
\]

因此不存在这样的整数 `A`，从而

\[
\boxed{\mu\ge601.}
\]

这是一张完整有限证书，而不是某个搜索范围内的数值证据。

## 6. P025-T25 —— 显式 radius-601 non-degenerate witness

取

\[
(A,B,C)=(6,0,-1).
\]

得到

\[
x=6v_1-v_3
=
\boxed{(-601,\ 38,\ 586,\ 79)}.
\]

其 radius 为

\[
\|x\|_\infty=601.
\]

按构造 `alpha*x=0`，直接计算又有

\[
\beta(x)=279{,}841\ne0.
\]

所以它是合法 non-degenerate relation-adapted witness，得到

\[
\boxed{\mu\le601.}
\]

结合 P025-T24：

\[
\boxed{\mu=601.}
\]

## 7. P025-T26 —— 该 high-quality witness profile 几乎由 demand 饱和

前面已经证明

\[
\lambda_{abc}=597.
\]

additive lattice 含有 `v_1=(20,3,46,0)`，所以

\[
\rho\le46<597.
\]

因此即使不精确求解 unrestricted shortest-vector problem，也有

\[
\max(\lambda_{abc},\rho)=597.
\]

再结合 `mu=601`：

\[
\boxed{
\mu-\max(\lambda_{abc},\rho)=4.
}
\]

所以在这个 high-quality state 上，arithmetic multiplicity demand 已经解释了几乎全部 exact certificate precision；独立 relation/degeneracy layer 只比最强已认证 lower floor 多出四个 `L_infinity` 单位。

这与小状态 `1+53=54` 形成鲜明对比，后者的 independent non-degeneracy overhead 为 `18`。

同时，简单 two-coordinate ceiling 仍极其宽松：

\[
U_2=59{,}049.
\]

所以 compact local generator minor 虽足以证明 finiteness，却在四坐标状态里可能离真实 restricted minimum 很远。完整 lattice relation 可以远强于 cheapest coordinate-pair certificate。

## 8. 相比此前架构真正增加了什么

这个例子第一次在真正 high-quality integer state 上闭合整条链：

\[
\boxed{
\text{radical/residual state}
\to
\text{arithmetic demand }597
\to
\text{relation/degeneracy flag}
\to
\text{exact restricted witness }601.
}
\]

它带来三个有用结论。

第一，P025 witness precision 已经通过一个精确值与 hard `abc`-quality sample 接上，而不再只依赖小范围例子。

第二，certificate sandwich 可以真正诊断误差来源：这里 arithmetic lower certificate 几乎紧，而 naive sparse upper certificate 极不紧。

第三，剩余 uncertainty 的来源被隔离：additive lattice 早已有小状态，四单位差值才是真正位于 demand floor 之上的 certificate restriction，而此前 `U_2` 的绝大部分 gap 只是 construction inefficiency。

## 9. 前人工作与创新边界

Pasten 的 arithmetic derivative/witness framework 属于前人工作 [SRC-PASTEN-2021-ARITHMETIC-DERIVATIVES]。把 `mu` 解释为避开 `T^circ` 的 shortest lattice point 是 restricted-successive-minimum 特化，属于 Henk--Thiel / Geometry-of-Numbers 的前人邻域 [SRC-HENK-THIEL-2014-RESTRICTED-MINIMA]。Unimodular lattice basis change 与 lattice reduction 同样是既有数学。

P025 不把这些方法作为新发明。

项目侧数学 payload 是：对这个固定 `abc` state 给出显式精确证书，并把该值与此前已证明的 `lambda_abc`、`rho`、`U_2` 结构接起来。数值 `601` 对这个特定 arithmetic-derivative witness problem 的历史优先性尚未专门审计，因此只能作为项目实例结果，不作“首次”主张。

## 10. 可执行资产

本 generation 新增

- `src/enterprise_math/abc_high_quality_witness.py`；
- `tests/test_abc_high_quality_witness.py`。

可执行证书检查：

- 精确 high-quality 不等式；
- generator rows `alpha,beta`；
- canonical / reduced lattice basis；
- unimodularity `det U=-1`；
- reduced basis 上 degeneracy functional 的对角化；
- 完整十行 radius-600 obstruction table；
- 显式 radius-601 witness；
- `lambda_abc=597`、additive radius certificate `<=46`、`U_2=59049`。

证明不需要把所有 witness 穷举到 radius 601。

## 11. 下一前沿

精确值 `mu=601` 把下一问题大幅收窄：

1. 不依赖一次性 reduced basis，直接从 quotient/flag geometry 解释四单位 gap `mu-lambda_abc=4`；
2. 在其它 high-quality / exceptional triples 上测试 `mu/lambda_abc` 是通常接近一，还是可以很大；
3. 把 Henk--Thiel 的一般 restricted-minimum bounds 与 P025 arithmetic-specific lower floor、exact reduced-basis certificate 做比较；
4. 主动寻找反例后，再考虑是否存在“arithmetic floor 与 restricted minimum 相差 `O(1)`”之类的定理；
5. 继续把结果定位为 pressure test，而不是 ABC 猜想已经被证明的证据。
