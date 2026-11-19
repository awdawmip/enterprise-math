# AP–Christoffel 余子式的根和与有理根分母

设 $q_m$ 是等差表原树余子式除去已知的 $t^{m-1}$ 后所得多项式，$\sigma_m$ 是它的全部根按重数求和。对每个素数 $p>2m^2$，**$\sigma_m$ 的既约分母含 $p$，当且仅当 $q_m$ 有负整数 $p$ 进赋值的根。** 此时该根唯一、单纯，属于 $\mathbf Q_p$，赋值恰为 $-1$。其余各根的赋值至少为 $-1/3$。若根和的分母不含 $p$，所有根的赋值至少为 $-1/2$。两个界都由原图的实际多项式达到。

这给出了有理根分母的大素因子筛。计算筛法只需取原图最高三层的有理矩阵。第21轮以全部端点系数排除了 $p>m^3$ 的两侧赋值，第115轮细分了正赋值根并约束有理根的分子。本次处理无穷远处的局部根。一个可提升的 $p$ 进根并不决定实区间里的交叉。全 $m$ 的实区间问题仍开。[原任务书](https://github.com/awdawmip/enterprise-math/blob/e7b9fb5084f93a9b2dbc16225629b667fb7bf46c/research_tasks/PERFECT_PRIME_AP_CHRISTOFFEL_J_TRANSVERSALITY_DEFORMATION_20260830.md) · [原局部横截性与归一化](https://github.com/awdawmip/enterprise-math/blob/e7b9fb5084f93a9b2dbc16225629b667fb7bf46c/research_returns/PERFECT_PRIME_AP_CHRISTOFFEL_J_TRANSVERSALITY_DEFORMATION_RETURN_20260830.md) · [已知首尾项，式 (5)](../twentyfirst/christoffel.md) · [第115轮的分子筛](../hundredfifteenth/christoffel.md) · [正赋值端的几何根](../hundredfifteenth/boundary.md)

## 反向分层及其费用

取 $m\ge2,\ n=m-1,\ b=m^2,\ w_i=(-1)^i\binom ni$。原二部图的第 $s$ 层边 $(i,j)$ 的权是 $w_iw_jw_s/(1+i+mj+bs)$，其中 $0\le i,j,s<m$。每条边贡献权乘关联向量的外积；删去最后一个右顶点的行、列得 $2m-1$ 阶的 $L_s$。写

$$
\det\!\left(\sum_{s=0}^nL_s t^s\right)=t^n q_m(t),\qquad
D=\deg q_m=n(2m-3),\qquad
q^*(y)=y^D q_m(1/y)=\sum_{k=0}^D c_k y^k .
$$

于是 $\det(\sum_{r=0}^nL_{n-r}y^r)=y^n q^*(y)$，且 $\sigma_m=-c_1/c_0$。取 $v_p(p)=1$。第21轮的原归一化给出

$$
c_0=(-1)^D
\frac{n^n m^{n(n+3)+m}(n!)^{2m}\prod_j\binom nj^2}
     {2(2b)!}
\frac{(m-1)^2(2m+1)}{\binom{m^3}{2b}} .
$$

因为 $2b<p$ 且 $m^3<p^2$，除了末尾的二项式，以上因子都是 $p$ 进单位。Legendre 公式给出

$$
a=\mathbf1_{\{m^3\bmod p<2b\}},\qquad v_p(c_0)=-a.
\tag{1}
$$

第 $r$ 个反向层的原分母是 $(m^3-(r+1)b,\ m^3-rb]$ 中的整数，每个只出现一次。记每个正倍数 $hp\le m^3$ 所在的层为 $r_h=\lfloor(m^3-hp)/b\rfloor$。头两层合计只有 $a$ 个这样的分母，每个只含一次 $p$。将 $r_h\ge2$ 的数 $r_h-1$ 由小到大列为 $d_1,d_2,\ldots$。有 $d_1\ge1$，相邻项至少差 2，因而 $\sum_{i=1}^j d_i\ge j^2$。

**系数界。** 若 $j(k)$ 是满足 $\sum_{i=1}^j d_i\le k$ 的最大可用项数（可取零），则

$$
 v_p(c_k/c_0)\ \ge -j(k)\ \ge-\lfloor\sqrt{k}\rfloor .
\tag{2}
$$

原割线坐标使任一固定层成为 $m$ 个非零带权平方 $[g(mj+bs)-f(mj)]^2$ 之和。这 $m$ 个线性泛函独立，因为次数不超过 $n$ 的 $f$ 可在 $m$ 个节点任意插值。模去共同常数后，特别有 $\operatorname{rank} L_n=m$。在反向行列式的逐列展开中，先丢弃正次层列少于 $n$ 个的项，此时有超过 $m$ 个完整 $L_n$ 的列。再把每个保留层拆为具体边。若两列均选择同一条含 $p$ 分母的边，秩一性使行列式为零。故初始两层合计最多贡献 $a$ 个 $p$ 分母。余下每用一条 $r\ge2$ 层的这类边，除该正次层列的基本一阶外，至少再花 $r-1$ 阶。系数 $c_k$ 来自次数 $n+k$，可用的额外阶数最多 $k$；式 (1) 消去初始两层的费用，得到 (2)。[冻结割线表示，式 (2.1)](https://github.com/awdawmip/enterprise-math/blob/1559dad7422d9ebcd9579ffaa9e53030a0e9540f/research_returns/PERFECT_PRIME_AP_RESIDUAL_MOBIUS_BERNSTEIN_COEFFICIENT_POSITIVITY_RETURN_20260903.md)

## 读出大素分母

由 (2)，$v_p(\sigma_m)\ge-1$，并有

$$
 \frac{q^*(p z)}{c_0} \equiv 1-p\sigma_m z \pmod p.
 \tag{3}
$$

左边全部系数 $p$ 整。$k\ge2$ 时 $k-\lfloor\sqrt k\rfloor\ge1$，因此约化至多一次。若 $v_p(\sigma_m)=-1$，(3) 有一个非零单根，唯一提升到 $\mathbf Z_p^\times$。在代数闭包中也没有其他 $v_p(y)=1$ 的根，因为每个这样的根必须落入同一单根的剩余类，Hensel 唯一性在任意有限扩域中仍成立。任意 $v_p(y)>1$ 使常数项独占最低赋值。若 $v_p(\sigma_m)\ge0$，(3) 约化为常数，整负赋值的 $t=1/y$ 全被排除。

(2) 同时留下可测的分数赋值间隙。把反向 Newton 多边形平移到 $(0,0)$。若一次项无极点，所有 $k\ge2$ 处的高度至少为 $-k/2$，故每个 $v_p(y)\le1/2$。若一次项有极点，第一条边从 $(0,0)$ 到 $(1,-1)$。对 $k\ge2$，$\lfloor\sqrt k\rfloor-1\le(k-1)/3$，其余点均在从 $(1,-1)$ 发出的斜率 $-1/3$ 的直线之上或线上。故剩余根均有 $v_p(y)\le1/3$。

若 $q_m(A/B)=0$ 且 $\gcd(A,B)=1,\ B>0$，则 $B$ 中每个大于 $2b$ 的素数只出现一次，且必须整除 $\operatorname{den}(\sigma_m)$。这一分母的大素部分本身平方自由；由 $j(1)>0$ 的必要条件 $d_1=1$，每个这种素数还必须整除区间 $(m^3-3b,m^3-2b]$ 中的某个正整数。至多有 $b$ 个候选素数，因为区间长度为 $b$，且任何正整数不超过 $m^3<(2b)^2$。当 $m=2$ 时没有反向第三层，候选集为空。

## 从末三层计算根和

将 $L_n$ 作有理合同变换为 $\operatorname{diag}(A,0_n)$，其中 $A$ 可逆。同一基下记 $L_{n-1}$ 为 $\left(\begin{smallmatrix}A_1&C\\C^T&B\end{smallmatrix}\right)$，$L_{n-2}$ 在核上的块为 $B_2$；当 $n=1$ 时取 $L_{-1}=0$。由 $c_0\ne0$，$B$ 可逆。沿 $A+y A_1+O(y^2)$ 做 Schur 补，另一块为 $y B+y^2(B_2-C^TA^{-1}C)+O(y^3)$。将两个行列式分别展开到各自首项的下一阶，得到

$$
 \boxed{\displaystyle
 \sigma_m=-\operatorname{tr}(A^{-1}A_1)
           -\operatorname{tr}\!\left[B^{-1}(B_2-C^TA^{-1}C)\right].}
 \tag{4}
$$

合同变换的行列式因子在比值中消去。原图整块的左上 $m$ 阶已是可逆对角阵 $A$：第 $i$ 个对角元正比于 $\sum_{j=0}^n w_j/(x+mj)=m^n n!/\prod_{j=0}^n(x+mj)$，其中 $x=1+i+bn$。若 $G$ 是右上块，核基可直接取 $\binom{-A^{-1}G}{I}$。因此只需在两个维数至多 $m$ 的空间内以有理数运算。

## 两个锐例及一次真实消去

- $m=6,\ p=109$。按原归一化，$p^a q^*(pz)\equiv79+64z\pmod{109}$，故唯一负整赋值根满足 $(1/t)/109\equiv72\pmod{109}$。同一多项式在另一端还有两根满足 $t/109\equiv9,108\pmod{109}$。[第115轮临界证书](../hundredfifteenth/christoffel_checked.json)
- $m=7,\ p=101$。反向多边形的全部下降顶点是 $(0,-1),(1,-2),(4,-3)$。原 $q_m$ 恰有一个赋值 $-1$ 的根和三个赋值 $-1/3$ 的根，达到有整根时的剩余界。
- $m=9,\ p=179$。反向第三层的区间是 $(486,567]$，含 $537=3p$，但末三层求得 $\sigma_9\equiv71\pmod{179}$，大素分母在这里消去。120次原余子式的反向下降顶点为 $(0,-1),(4,-3),(9,-4)$。故原 $q_m$ 恰有四个赋值 $-1/2$ 的根及五个赋值 $-1/5$ 的根。第一段用 $Z=y^2/p$ 得初式 $178+5Z+49Z^2$，两个单根 $86,155$ 分属非平方与平方类。每类的两根生成与 $\mathbf Q_{179}(\sqrt{179u})$ 同构的域，分别取 $u=86,155$。第二段用 $Z=y^5/p$ 得 $49+100Z$，根为 $55$。由于 $\gcd(5,178)=1$，五根构成一个五次不可约因子，各自生成与 $\mathbf Q_{179}(\sqrt[5]{179})$ 同构的域。具体地，对每个剩余单位根 $u$ 及相应的 $e=2,5$，在 $\pi^e=pu$ 的全分歧域取 $y=\pi v$；$v=1$ 是归一化初式的单根，唯一提升。根的赋值分母迫使它所生成的域至少有 $e$ 次，故恰为该域。两个二次域由不同单位平方类区分。

## 精确复算

在本目录运行 `python vieta_check.py | cmp - vieta_checked.json`，仅用 Python 标准库。程序从带符号的原边权生成末三层，用式 (4) 对 $2\le m\le12$ 做 766 组大素数核验。按 $m=5,\ldots,12$ 排列，第三层筛给出的候选数是 $6,6,14,16,24,27,37,43$，其中恰有 $(9,179)$ 一组在式 (3) 消去；$m=2,3,4$ 无候选。对 $2\le m\le6$ 另用原图的整数 Bareiss 行列式及有理插值复原全部系数，覆盖63组 $(m,p)$、1,982个系数界，并将12个非平凡剩余根各提升一位回代。

最后两个锐例还独立从完整反向图重建。令 $J=\lfloor m^3/p\rfloor$；不同极边各至多出现一次，故 $p^J q^*(y)$ 的系数全整于 $p$。在 $D+1$ 个非零整数节点上用原边权计算 $p\sum_r L_{n-r}y^r$ 的行列式模 $p^{2m}$，除以 $p^{2m-1-J}y^n$ 得 $p^J q^*(y)\bmod p^{J+1}$。由于 $D+2<p$，插值的阶乘皆为单位，且可用一个额外节点回代。未被此精度读出的系数均有赋值至少 $1$，不能影响始于高度 $-a\le0$ 的下降边。[复算程序](vieta_check.py) · [确定性结果](vieta_checked.json)
