# 进取原生 filament 零线排列：特征缺陷与算术提升分叉

Status: `FREE_RESEARCH_EXACT_ARRANGEMENT_POINT_COUNT / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-24`

Researcher-ID: `EM-FREE-NEPS-239A6D`

## 一、零线排列

固定一个长度为 \(k\) 的原生 filament 窗口、奇素数
\[
q>\max(3,k-1)
\]
以及手性
\[
\chi\in\{+1,-1\}.
\]

原生几何给出的数值为
\[
V_j(a,b)=a+bj+\eta_j^\chi,
\qquad
\eta_j^\chi=\frac{3j^2+\chi\varepsilon_j}{2},
\]
其中 \(\varepsilon_j=1\) 当 \(j\) 为奇数，否则为 \(0\)。

条件 \(q\mid V_j\) 在参数平面 \(\mathbb F_q^2\) 中是一条仿射直线
\[
L_j^\chi.
\]

因为 \(q>k-1\)，这些直线斜率两两不同，每一对直线恰有一个交点。

记 \(n_m\) 为恰好落在 \(m\) 条零线上的参数点数量。

## 二、pair budget 与排列缺陷

每一对直线贡献一个 pair intersection，因此
\[
\sum_{m\ge2} n_m\binom m2=\binom k2.
\]

定义排列特征常数
\[
b_{k,q}^\chi=\sum_{m\ge2}n_m(m-1),
\]
以及 concurrence defect
\[
\delta_{k,q}^\chi
=\binom k2-b_{k,q}^\chi.
\]

由 pair budget，
\[
\boxed{
\delta_{k,q}^\chi
=\sum_{m\ge3}n_m\binom{m-1}{2}
}.
\]

所以：

- 普通双交点不产生缺陷；
- 一个三重交点贡献 \(1\)；
- 一个四重交点贡献 \(3\)；
- \(\delta=0\) 当且仅当没有任何三重以上共点。

这个量由整张多 Cell 零线 incidence 排列决定，不依赖于后来选择哪一个具体素数状态。

## 三、特征多项式与全 unit basin

由仿射线排列的 inclusion-exclusion，
\[
N_k(q,\chi)
=
\#\Bigl(\mathbb F_q^2\setminus\bigcup_jL_j^\chi\Bigr)
=
q^2-kq+b_{k,q}^\chi.
\]

等价地，
\[
\boxed{
N_k(q,\chi)
=q^2-kq+\binom k2-\delta_{k,q}^\chi
}.
\]

因此对应的特征多项式为
\[
\boxed{
\operatorname{Char}_{k,q}^\chi(T)
=T^2-kT+b_{k,q}^\chi
}.
\]

此前得到的 generic MDS 计数
\[
q^2-kq+\binom k2
\]
正是 \(\delta=0\) 的特例。

完整 zero-multiplicity spectrum 同样由 intersection lattice 决定：

\[
\#\{\text{恰好 }m\text{ 个零}\}=n_m,\quad m\ge2,
\]

\[
\#\{\text{恰好一个零}\}
=kq-\sum_{m\ge2}mn_m,
\]

\[
\#\{\text{没有零}\}
=q^2-kq+\sum_{m\ge2}(m-1)n_m.
\]

## 四、有限域扩张：缺陷永久保留

令
\[
Q=q^s.
\]

所有零线和 pair intersection 都已经在 \(\mathbb F_q\) 上定义。扩张到
\(\mathbb F_Q\) 只会给每条线增加新点，不会分裂、删除或新造原有共点。

所以对任意 \(s\ge1\)：
\[
\boxed{
N_k(\mathbb F_{q^s},\chi)
=q^{2s}-kq^s+b_{k,q}^\chi
}.
\]

并且所有 \(m\ge2\) 的 \(n_m\) 完全保持不变。

对应 survivor complement 的 Hasse–Weil zeta function 为
\[
\boxed{
Z_{k,q}^\chi(T)
=
\frac{(1-qT)^k}
{(1-q^2T)(1-T)^{b_{k,q}^\chi}}
}.
\]

因此 \(\delta\) 是一个 **unramified extension invariant**。

## 五、\(q\)-进加深：缺陷最终去奇异化

现在改在
\[
R_a=\mathbb Z/q^a\mathbb Z
\]
上工作。

斜率差仍然是 unit，所以每一对零线仍有唯一交点。定义精度 \(a\) 的缺陷
\[
\delta_{k,q}^\chi(a).
\]

同样有
\[
\boxed{
N_k(R_a,\chi)
=q^{2a}-kq^a+\binom k2-\delta_{k,q}^\chi(a)
}.
\]

若若干线在模 \(q^{a+1}\) 共点，则它们必在模 \(q^a\) 共点，因此
\[
\delta(a+1)\le\delta(a).
\]

原生 mixed-parity triple 的共点条件由一个明确整数控制：
\[
3(w-u)(w-v)\pm\chi.
\]

每个异常都有有限 \(q\)-进深度。一旦精度超过这些整数的最大
\(q\)-进 valuation，
\[
\delta(a)=0.
\]

所以出现精确分叉：

\[
\boxed{
\text{有限域横向扩张：缺陷保留}
}
\]

\[
\boxed{
q\text{-进纵向加精：缺陷修复}
}.
\]

## 六、sharp-nine 的精确 defect spectrum

对最大 \(k=9\) 窗口：

| \(q\) | \(\chi\) | \(n_2\) | \(n_3\) | \(n_4\) | \(\delta\) | \(b\) | \(N_9(\mathbb F_q)\) |
|---:|:---:|---:|---:|---:|---:|---:|---:|
| 11 | + | 18 | 4 | 1 | 7 | 29 | 51 |
| 11 | − | 18 | 4 | 1 | 7 | 29 | 51 |
| 13 | + | 24 | 4 | 0 | 4 | 32 | 84 |
| 13 | − | 27 | 3 | 0 | 3 | 33 | 85 |
| 23 | + | 24 | 4 | 0 | 4 | 32 | 354 |
| 23 | − | 24 | 2 | 1 | 5 | 31 | 353 |
| 31 | + | 30 | 2 | 0 | 2 | 34 | 716 |
| 31 | − | 30 | 2 | 0 | 2 | 34 | 716 |
| 53 | + | 30 | 2 | 0 | 2 | 34 | 2366 |
| 53 | − | 30 | 2 | 0 | 2 | 34 | 2366 |

因此
\[
N_+-N_-=b_+-b_-=\delta_- -\delta_+.
\]

只有两个 post-small 通道产生手性不平衡：

\[
q=13:\quad N_+-N_-=-1,
\]

\[
q=23:\quad N_+-N_-=+1.
\]

对应局部 zeta 比为
\[
q=13:\quad \frac{Z_+}{Z_-}=1-T,
\]

\[
q=23:\quad \frac{Z_+}{Z_-}=\frac1{1-T}.
\]

两处无权 defect charge 一正一负相消，但实际 unit-density 因子不会相消，因为特征不同：
\[
\frac{84}{85}\frac{354}{353}
=
\frac{29736}{30005}.
\]

## 七、第二层直接枚举：横向保留，纵向修复

在 \(\mathbb F_{13^2}\) 中：
\[
N_+=27072,\qquad N_-=27073.
\]

在 \(\mathbb Z/13^2\mathbb Z\) 中：
\[
N_+=N_-=27076.
\]

在 \(\mathbb F_{23^2}\) 中：
\[
N_+=275112,\qquad N_-=275111.
\]

在 \(\mathbb Z/23^2\mathbb Z\) 中：
\[
N_+=N_-=275116.
\]

四组结果均由逐点枚举验证。

因此 sharp-nine 的 \(\pm1\) 手性缺陷满足：

- 对任意有限域扩张次数 \(s\)，绝对差恒为 \(1\)；
- 相对密度差随 \(q^{-2s}\) 消失；
- 对 \(q\)-进精度 \(a\ge2\)，绝对差直接归零。

## 八、边界 discriminant 预测器

对奇长度 \(k=9\)，比较同一无限 plus-mode 排列的左右相邻窗口。

公共内部线为 \(L_1,\ldots,L_8\)。令左右边界在内部线上的交点参数分别为
\[
\beta_j^L,\qquad \beta_j^R.
\]

定义 Vandermonde boundary discriminants：
\[
D_L=\prod_{1\le i<j\le8}(\beta_j^L-\beta_i^L),
\]

\[
D_R=\prod_{1\le i<j\le8}(\beta_j^R-\beta_i^R).
\]

精确分解给出
\[
\left|\frac{D_L}{D_R}\right|
=
\boxed{\frac{91}{529}}
=
\boxed{\frac{7\cdot13}{23^2}}.
\]

在斜率不碰撞范围 \(q>8\) 内，非零 valuation 支持恰好是
\[
\boxed{\{13,23\}},
\]
正好就是两个手性 survivor 数不相等的通道。

方向也一致：

- \(v_{13}(D_L/D_R)>0\)：左边界碰撞更多，得到 \(N_+-N_-=-1\)；
- \(v_{23}(D_L/D_R)<0\)：右边界碰撞更多，得到 \(N_+-N_-=+1\)。

这把原先的 boundary flux 压缩成一个单一有理数判别器。

## 九、deletion–restriction 组合律

从 \(k\) 条线增加一条新边界线。设该新线与旧 union 的不同交点数量为 \(s\)。

则
\[
b_{k+1}=b_k+s,
\]

\[
\boxed{
\delta_{k+1}=\delta_k+k-s
}.
\]

新增一个 Cell 所贡献的 defect，恰好等于 \(k\) 个名义边界交点之间发生的碰撞数。

所以目前三个描述其实是同一对象：

\[
\boxed{
\text{boundary collision}
=
\text{arrangement defect increment}
=
\text{chiral all-unit flux}
}.
\]

## 十、当前判定

\(\delta_{k,q}^\chi\) 是目前第一个同时具有下列性质的多 Cell 原生坍缩读数：

1. 来自完整零线 incidence arrangement，而不是一个 prime/composite bit 图样；
2. 精确控制 local all-unit basin；
3. 在所有有限域扩张中保持；
4. 在 \(q\)-进精度中具有有限衰减深度；
5. 精确解释 sharp-nine 手性偏差；
6. 通过 deletion–restriction 具有可组合的跨尺度递推。

线排列特征多项式、zeta function 与 ramified/unramified lift 都是经典数学工具。当前研究对象是它们由进取原生 filament 曲率码自动选出后的统一坍缩解释；不据此主张新的经典素数频率定理。
