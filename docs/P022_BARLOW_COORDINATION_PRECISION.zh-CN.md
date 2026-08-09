# P022 —— Barlow 配位精度与二次 drift energy

状态：`ACTIVE RESEARCH NOTE / EXACT INTEGER GEOMETRY / NOVELTY UNVERIFIED`  
归属：`program/p022-geometry-v2`  
依赖：Barlow prefix normal form 与 exact graph-shell language  
目的：把**顶点基数**所需的最小状态，与明显更丰富的**测地路径重数**所需状态严格分开

## 1. 为什么 coordination cardinality 必须单独分析精度

前面的 Barlow 结果已经说明，最短路 multiplicity 会读取很大一部分 prefix-imbalance trajectory。

对 radius-`n` 的 whole shell，精确 geodesic path total 一般需要

\[
(|\delta_{-n}|,\ldots,|\delta_n|).
\]

很容易因此误以为 shell 的**顶点数**也需要差不多的信息。

事实恰好相反。

一旦忘掉 witness multiplicity，只问 native graph shell 上“有多少 vertex 存在”，几乎整个 stacking history 都会消失。exact shell cardinality 最终只依赖 top / bottom 两个 extreme prefix imbalances 组成的一个二次整数。

同一套 intrinsic geometry 因 future observable 不同，最低精度发生巨大变化，这是 task-relative precision 的一个非常强的具体例子。

## 2. vertical-prefix support 是一个 Minkowski sum

固定 target layer `k`，记

\[
q=|k|,
\qquad
\delta=\delta_k,
\qquad
d=|\delta|,
\qquad
c=\frac{q-d}{2}.
\]

vertical witness polynomial 的 normal form 为

\[
P_k=(A+3)^cB_\pm^d.
\]

现在只保留 **support**，不再看 coefficient multiplicity。

`A+3` 的 support 是原点加六个 triangular primitive steps；其 `c` 次 Minkowski sum 正好是 triangular hex-ball

\[
H_c=\{(u,v):\max(|u|,|v|,|u+v|)\le c\}.
\]

`B_+^d` 的 support 是离散有向三角形

\[
\Delta_d^+
=\{(i,j):i,j\ge0,\ i+j\le d\},
\]

`B_-^d` 则是其反射版本。

因此

\[
\boxed{
\operatorname{supp}P_k
=H_c+\Delta_d^{\pm}.}
\]

literal interface order 已经完全消失，只剩 `(c,d)`。

## 3. P022-BC01 —— vertical support cardinality 闭式

以 plus orientation 为例，Minkowski sum 可精确写成

\[
H_c+\Delta_d^+
=
\{(q,r):
-c\le q\le c+d,
-c\le r\le c+d,
-c\le q+r\le c+d
\}.
\]

从 square

\[
[-c,c+d]^2
\]

出发，其 lattice-point side length 是

\[
2c+d+1.
\]

再删去

\[
q+r<-c
\]

与

\[
q+r>c+d
\]

两个 corner triangles。做整数计数并化简得到

\[
\boxed{
K(c,d)
=3c^2+3(d+1)c+\binom{d+2}{2}.}
\]

minus orientation 由 reflection 得到完全相同的 cardinality。

用 vertical length `q` 与 absolute imbalance `d` 重写：

\[
\boxed{
4K
=3q^2+6q+4-d^2.}
\]

所以即使在 extreme layer，cardinality 也已经擦掉 imbalance sign，只保留平方。

## 4. P022-BC02 —— 所有 non-extreme shell layers 都与 stacking 无关

固定 whole graph-shell radius `n`，目标层满足

\[
q=|k|<n.
\]

任何到该 shell layer 的 shortest path 都还需要

\[
t=n-q>0
\]

个 in-layer triangular steps。

support 层面，乘 `A^t` 会把 hex-ball component 扩大：

\[
H_c+\Delta_d
\longrightarrow
H_{c+t}+\Delta_d.
\]

exact shell layer 就是 radius-`t` expansion 与 radius-`t-1` expansion 的差，因此

\[
S_n(k)
=K(c+t,d)-K(c+t-1,d).
\]

由 BC01，

\[
K(s,d)-K(s-1,d)=6s+3d.
\]

代入

\[
s=c+t
=\frac{q-d}{2}+n-q
\]

后，所有 `d` 项完全抵消：

\[
\boxed{
S_n(k)=3(2n-q),
\qquad |k|<n.}
\]

这是一个很强的 universality theorem：

> **Barlow graph shell 的每个 non-extreme horizontal layer，其 vertex count 完全不依赖 stacking word，也不依赖 prefix imbalance。**

stacking information 在 shell cardinality 里只存活于 top / bottom 两个 extreme layers。

## 5. P022-BC03 —— extreme layers 只剩一个 quadratic drift coordinate

对 extreme layer `|k|=n`，没有任何 in-layer expansion，所以 BC01 直接给出

\[
\boxed{
S_n^{\mathrm{ext}}(k)
=
\frac{3n^2+6n+4-\delta_k^2}{4}.}
\]

由于只出现 `delta_k^2`，整个 horizontal-layer cardinality 会擦掉 drift orientation/sign。

反过来，

\[
\boxed{
\delta_k^2
=3n^2+6n+4-4S_n^{\mathrm{ext}}(k).}
\]

`|delta_k|` 是非负整数且与 `n` 同奇偶，因此 extreme-layer vertex count 能精确恢复 `|delta_k|`。

所以当 top 或 bottom extreme layer 被单独标识并查询时，该 cardinality language 的 minimum stacking state 是

\[
\boxed{|\delta_{\pm n}|}
\]

（忽略有限表示值的双射重标记）。

## 6. P022-BC04 —— whole-shell cardinality 只需要一个 drift energy

中央层以及所有 non-extreme 正负 layer pairs 总和为

\[
9n^2-3n.
\]

加入两个 extreme layers。定义 radius-`n` quadratic drift energy

\[
\boxed{
Q_n=\delta_n^2+\delta_{-n}^2.}
\]

则完整 coordination shell 的 cardinality 精确为

\[
\boxed{
4S_n=42n^2+8-Q_n.}
\]

也就是

\[
\boxed{
S_n
=\frac{21n^2}{2}+2-rac{Q_n}{4}.}
\]

这个公式对任意 finite two-sided Barlow stacking window 都成立，不需要 periodicity。

并且它完全可逆：

\[
\boxed{
Q_n=42n^2+8-4S_n.}
\]

所以在“固定 radius 只问 whole-shell **vertex count**”这一 future language 下，所有 stacking history 精确 factor through 一个整数，并且不同 represented `Q_n` 不可能继续安全合并：

\[
\boxed{
\text{minimum shell-cardinality state}=Q_n
}
\]

（同样只差有限 relabeling）。

whole shell 不再知道 energy 如何分配给正负两侧。例如 `(5,1)` 与 `(1,5)` 都有 `Q_n=26`，因而 whole-shell cardinality 相同。

## 7. FCC 与 HCP 都成为直接特例

### FCC / constant drift

constant-sign stacking 满足

\[
|\delta_n|=|\delta_{-n}|=n,
\]

因此

\[
Q_n=2n^2.
\]

于是

\[
\boxed{S_n^{FCC}=10n^2+2.}
\]

正好恢复历史 `A_3` shell formula。

### HCP / alternating stacking

HCP 满足

\[
|\delta_{\pm n}|=
\begin{cases}
0,&n\text{ even},\\
1,&n\text{ odd}.
\end{cases}
\]

所以

\[
S_n^{HCP}
=
\begin{cases}
\frac{21n^2}{2}+2,&n\text{ even},\\
\frac{21n^2}{2}+\frac32,&n\text{ odd},
\end{cases}
\]

即

\[
\boxed{S_n^{HCP}=\left\lfloor\frac{21n^2}{2}\right\rfloor+2.}
\]

这与标准 HCP coordination sequence 完全吻合。

## 8. P022-BC05 —— crystal-ball cardinality 只需要 cumulative quadratic energy

定义 native graph ball size

\[
B_n=\sum_{r=0}^{n}S_r
\]

以及 cumulative drift energy

\[
\boxed{
E_n=\sum_{r=1}^{n}Q_r
=\sum_{r=1}^{n}(\delta_r^2+\delta_{-r}^2).}
\]

对 BC04 求和：

\[
\boxed{
4B_n
=4+7n(n+1)(2n+1)+8n-E_n.}
\]

反向同样精确：

\[
\boxed{
E_n
=4+7n(n+1)(2n+1)+8n-4B_n.}
\]

因此，如果 future language 只问**一个 radius-`n` ball 的 cardinality**，全部 shell-resolved stacking history 又进一步坍缩成一个整数累计能量 `E_n`。

如果查询每个 radius 的 ball count，则相邻 `E_n` 的差可以恢复每个 `Q_n`；所需状态再次取决于实际 query set。

## 9. 与 geodesic multiplicity precision 的严格对照

在同一个 radius `n`：

exact shell **path total** 一般需要

\[
(|\delta_{-n}|,\ldots,|\delta_n|),
\]

因为每一个 intermediate target layer 都会提供不同 multiplicity factor。

而 exact shell **vertex count** 只需要

\[
Q_n=\delta_n^2+\delta_{-n}^2.
\]

因此

\[
\boxed{
\text{coordination cardinality precision}
\ll
\text{geodesic multiplicity precision}.}
\]

这不是 heuristic：可以显式构造不同 stacking words，它们拥有相同 `Q_n` 因而相同 shell cardinality，但 intermediate imbalance trajectories 不同，从而 path totals / multiplicity spectra 不同。

几何没有变，改变的只是 future observable。

## 10. P022-BC06 —— asymptotic shell / ball growth 读取 drift vector 的 `L^2` 统计

假设 one-sided absolute drift densities 存在：

\[
\mu_+=\lim_{n\to\infty}\frac{|\delta_n|}{n},
\qquad
\mu_-=\lim_{n\to\infty}\frac{|\delta_{-n}|}{n}.
\]

BC04 除以 `n^2`：

\[
\boxed{
\lim_{n\to\infty}\frac{S_n}{n^2}
=
\frac{21}{2}
-rac{\mu_+^2+\mu_-^2}{4}.}
\]

又因为

\[
E_n
\sim
\frac{\mu_+^2+\mu_-^2}{3}n^3,
\]

BC05 给出

\[
\boxed{
\lim_{n\to\infty}\frac{B_n}{n^3}
=
\frac72
-rac{\mu_+^2+\mu_-^2}{12}.}
\]

所以 asymptotic coordination growth 读取的是 two-sided drift vector

\[
(\mu_+,\mu_-)
\]

的平方 Euclidean size。

而前面的 aperiodic geodesic-growth theorem 读取的是

\[
\mu_*=\max(\mu_+,\mu_-),
\]

也就是同一 drift vector 的 `L^infinity` size。

两个 observables 对同一 hidden stacking state 读取了真正不同的低精度 shadows。

## 11. P022-BC07 —— 两个 asymptotic observables 联合恢复两侧 drift magnitudes

记

\[
C_S
=\lim_{n\to\infty}\frac{S_n}{n^2}.
\]

由 BC06，

\[
\boxed{
R_2:=\mu_+^2+\mu_-^2
=42-4C_S.}
\]

再记 shell-total geodesic multiplicity 的 growth constant 为

\[
\Lambda
=\lim_{n\to\infty}T_n^{1/n}.
\]

aperiodic drift theorem 给出

\[
\Lambda=2+2^{(1+M)/2},
\qquad
M=\max(\mu_+,\mu_-).
\]

右侧对 `M in [0,1]` 严格单调，因此 `Lambda` 唯一决定 `M`。

另一个较小的 drift magnitude 就是

\[
\boxed{
m=\sqrt{R_2-M^2}.}
\]

因此两个 asymptotic observables

\[
\boxed{(C_S,\Lambda)}
\]

联合恢复 hidden drift magnitudes 的无序对：

\[
\boxed{\{\mu_+,\mu_-\}.}
\]

whole-shell observable 对交换 top/bottom 两侧具有对称性，所以无法恢复方向标签；只要增加 one-sided shell 或单独 extreme-layer observable，就能恢复 orientation information。

这是一条非常具体的 reconstruction theorem：两个单独都不充分的 low-precision shadows，联合以后恰好足以恢复两个 hidden drift magnitudes。

## 12. 周期 stacking 的 exact rational coefficients

周期长度为 `L`、absolute period drift 为 `|D|` 时，两侧都有

\[
\mu=|D|/L.
\]

shell quadratic coefficient 是精确有理数

\[
\boxed{
\frac{21}{2}-\frac{\mu^2}{2}
=
\frac{21L^2-D^2}{2L^2}.}
\]

ball cubic coefficient 为

\[
\boxed{
\frac72-\frac{\mu^2}{6}
=
\frac{21L^2-D^2}{6L^2}.}
\]

都可以保存为约分后的 integer numerator/denominator pair，不需要 floating-point asymptotic state。

## 13. 同一 geometry 暴露出的 precision ladder

Barlow family 现在给出多个彼此严格不同的 exact state requirements：

### layer `k` 上 coordinate-sensitive endpoint distance + path count

\[
\delta_k.
\]

### 整个 horizontal layer 的 geodesic path total

\[
|\delta_k|.
\]

### radius-`n` 整个 geodesic path total

\[
(|\delta_{-n}|,\ldots,|\delta_n|).
\]

### 单独标识的 extreme-layer vertex count

\[
|\delta_{\pm n}|.
\]

### radius-`n` whole-shell vertex count

\[
Q_n=\delta_n^2+\delta_{-n}^2.
\]

### 单个 radius-`n` ball vertex count

\[
E_n=\sum_{r\le n}Q_r.
\]

### periodic geodesic-growth exponent

\[
|D|/L.
\]

### aperiodic asymptotic coordination coefficient

\[
\mu_+^2+\mu_-^2.
\]

因此根本不存在一个统一 scalar “几何精度”可以正确支配这些需求。精度必须由 declared operation / observation language 索引。

这是目前 P022 对 P023/P024 future-language principle 最强的一批 concrete specializations 之一。

## 14. executable assets

新增：

- `src/enterprise_math/p022_barlow_coordination.py`；
- `tests/test_p022_barlow_coordination.py`。

测试会把 support 与 shell formulas 对照 explicit Barlow polynomial/contact-graph enumeration，覆盖所有短周期 patterns，验证 FCC/HCP 特例，并检查 shell/ball cardinality 到 quadratic drift energy 的 exact inverse maps。
