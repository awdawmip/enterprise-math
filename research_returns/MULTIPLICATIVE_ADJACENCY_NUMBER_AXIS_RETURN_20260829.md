# 乘法相邻与新数轴：相邻半素数/合数的因子编辑几何 — Research Return

Task: `RS-MULTIPLICATIVE-ADJACENCY-NUMBER-AXIS`  
Publication: `TP2-180399AE7989F096D40D`  
Researcher-ID: `EM-MNA1-6B92D4`  
Claim: `chatgpt-mna1-20260829-1316-6b92d4`  
Execution record: `ER-090530731881C8CA560D`

## Terminal verdict

`SUCCESS / ADDITIVE-MULTIPLICATIVE-LOCALITY-SEPARATED / PURE-1D-MULTIPLICATIVE-AXIS-OBSTRUCTED / SEMIPRIME-PREFIX-GRAY-RAY-CONSTRUCTED / BRANCHED-SHELL-GEOMETRY-SURVIVES`

最强结论不是“找到一条能够替代普通整数轴的纯乘法数轴”，而是把问题精确拆成了三层：

1. 普通加法局部性与素因子编辑局部性存在**双向无界失真**，不是轻微重参数化；
2. 完整 M1/M2 邻接由于分支度数与素数重标号对称性，不能天然等同于一维全序的相邻图；
3. 半素数 M2 壳 nevertheless 存在一条显式、可计算、随素数窗口扩张保持前缀兼容的 Hamilton–Gray ray，但任何一维主脊保留的完整 M2 邻接边比例都趋于 0，所以它只能是**遍历坐标**，不能冒充完整乘法几何。

因此，本任务支持的最小诚实结构是：

`M1 graded divisibility-cover graph + fixed-Omega M2 replacement shells + optional symmetry-broken Gray spine`。

其中前两项属于成熟的自由交换幺半群/整除覆盖图/图的 reduced powers；项目可保留的是与普通加法相邻的精确失真定理、半素数/合数特化、前缀兼容 spine 的显式构造与局部性损失量化，不把成熟对象改名为新数学。

---

## 1. 基础恒等式：乘法编辑距离就是 gcd 剩余 token 数

设

\[
m=\prod_p p^{a_p},\qquad n=\prod_p p^{b_p},\qquad
 g=\gcd(m,n),
\]

且

\[
c_p=v_p(g)=\min(a_p,b_p).
\]

则逐坐标有

\[
|a_p-b_p|=(a_p-c_p)+(b_p-c_p).
\]

求和得到

\[
\boxed{
 d_\times(m,n)
 =\sum_p|v_p(m)-v_p(n)|
 =\Omega(m/g)+\Omega(n/g).
}
\]

同时得到更便利的形式

\[
\boxed{
 d_\times(m,n)=\Omega(m)+\Omega(n)-2\Omega(g).
}
\]

这个恒等式是 T1–T5、M1 图距离、M2 壳距离的共同核心。

### M1 图距离的精确解释

令 M1 图以全部正整数为顶点，边连接 `d_times=1` 的两点。每条边只改变一个素指数坐标 1，因此任何从 `m` 到 `n` 的路径长度至少为 `d_times(m,n)`。反过来，可以先从 `m` 逐个删除不属于 gcd 的素因子到 `g`，再逐个加入 `n/g` 的素因子，正好走

\[
\Omega(m/g)+\Omega(n/g)=d_\times(m,n)
\]

步。因此

\[
\boxed{\operatorname{dist}_{M1}(m,n)=d_\times(m,n).}
\]

换言之，`d_times` 不是任意定义的新距离，而正是整除覆盖图/素指数正交格的图距离。

---

## 2. T1 — 固定 Omega 层的偶距离定理：成立

若

\[
\Omega(m)=\Omega(n)=k,
\]

则由基础恒等式

\[
d_\times(m,n)=2\bigl(k-\Omega(\gcd(m,n))\bigr).
\]

所以距离必为偶数。若 `m != n` 而距离为 0，则所有素指数相同，由算术基本定理反而有 `m=n`，矛盾。因此

\[
\boxed{m\ne n,\ \Omega(m)=\Omega(n)=k
\Longrightarrow d_\times(m,n)\in 2\mathbb N_{>0}.}
\]

特别地，任何固定 `Omega` 壳中都没有 M1 边；两个不同半素数永远不可能 M1 相邻。

这证明了用户原始直觉的一种严格版本：**半素数在普通数轴上无论多接近，在“只乘/除一个素因子”的 M1 意义下都永远不是邻点。**

---

## 3. T2 — 半素数 gcd 分类：成立，并完全覆盖平方情形

对不同半素数 `m,n`，有

\[
\Omega(m)=\Omega(n)=2.
\]

故

\[
d_\times(m,n)=4-2\Omega(\gcd(m,n)).
\]

因为 `m != n`，不可能有 `Omega(gcd)=2`：若 gcd 已含两个 prime tokens，则 gcd=m=n。于是 `Omega(gcd)` 只能为 0 或 1：

\[
\boxed{d_\times(m,n)=2\iff \Omega(\gcd(m,n))=1,}
\]

\[
\boxed{d_\times(m,n)=4\iff \gcd(m,n)=1.}
\]

平方半素数没有例外。例如 `p^2` 与 `pq` 的 gcd 为 `p`，所以距离为 2；`p^2` 与 `q^2`（`p!=q`）互素，所以距离为 4。

### 对“相邻半素数一定乘法不相邻”的修正

如果把固定 `Omega=2` 壳的一次因子替换 M2 定义为 `d_times=2`，那么原命题是**假的**。最小反例已经是

\[
4=2^2,\quad 6=2\cdot3,
\]

它们既是普通顺序中的相邻半素数，又满足 `d_times(4,6)=2`。下一个例子 `6,9` 同样如此。

真正的完整分类是：相邻半素数要么 M2 相邻（共享一个 prime token），要么相距两次 M2 替换（互素）。不存在第三种情况。

### 共享因子时的 cofactor-prime 邻接约束

若相邻半素数 `m<n` 又满足 M2 相邻，则存在素数 `p` 与素数 `q<r` 使

\[
m=pq,\qquad n=pr.
\]

而且 `q,r` 必须是相邻素数。否则若存在素数 `s` 满足 `q<s<r`，则

\[
pq<ps<pr
\]

且 `ps` 也是半素数，和 `m,n` 在半素数集合中相邻矛盾。

因此 M2-相邻的加法相邻半素数，其普通差值具有精确形态

\[
\boxed{n-m=p(r-q),}
\]

即“共享素因子 × 一个素数间隙”。这是本任务与相邻素数/半素数边界研究之间最直接的结构桥。

---

## 4. T3 — 相邻合数不是 M1 相邻：成立，并可加强

设 `a<b` 是合数集合中的相邻元素。

### 4.1 首先，普通间距只能是 1 或 2

若 `b-a>=3`，则 `a+1,a+2` 都严格位于二者之间。由于 `a>=4`，这两个连续整数都大于 2，不可能同时为素数；其中至少一个是合数，矛盾。因此

\[
\boxed{b-a\in\{1,2\}.}
\]

### 4.2 间距 1 时

若 `b=a+1`，则 gcd 为 1，且二者均为合数，所以

\[
d_\times(a,b)=\Omega(a)+\Omega(b)\ge 4.
\]

### 4.3 间距 2 时

中间的 `p=a+1` 必须是素数。因为 `a,b>=4`，`p` 是奇素数，于是

\[
a=p-1,\qquad b=p+1,
\]

二者均为偶数，并且

\[
\gcd(a,b)=2.
\]

所以

\[
\boxed{
 d_\times(a,b)=
 \Omega\!\left(\frac{p-1}{2}\right)+
 \Omega\!\left(\frac{p+1}{2}\right).
}
\]

距离等于 2 只有当这两个连续整数都为素数。连续素数中唯一的一对是 `2,3`，故 `p=5`，即唯一例外

\[
\boxed{(a,b)=(4,6),\qquad d_\times=2.}
\]

若 `p>5`，两个连续 cofactors 中的偶数大于 2，必为合数，因此距离至少 3。

综上得到比 T3 更强的全称结论：

\[
\boxed{
 a\prec_+^{\mathcal C}b
 \Longrightarrow d_\times(a,b)\ge2,
}
\]

且

- `d_times=2` 当且仅当 `(a,b)=(4,6)`；
- 若 `b-a=1`，则 `d_times>=4`；
- 除 `(4,6)` 外所有相邻合数均有 `d_times>=3`。

因此相邻合数永远不是 M1 相邻。

---

## 5. T4 — 加法距离 1、乘法距离任意大：成立

给定任意 `K>=2`，考虑同余组

\[
n\equiv0\pmod{2^K},
\qquad
n\equiv-1\pmod{3^K}.
\]

因为 `gcd(2^K,3^K)=1`，中国剩余定理保证存在解模 `6^K`。取正代表元 `n`。于是

\[
2^K\mid n,
\qquad
3^K\mid n+1.
\]

`K>=2` 保证 `n,n+1` 都是合数。又因连续整数互素，

\[
\gcd(n,n+1)=1.
\]

故

\[
\begin{aligned}
d_\times(n,n+1)
&=\Omega(n)+\Omega(n+1)\\
&\ge K+K=2K.
\end{aligned}
\]

因此

\[
\boxed{|n-(n+1)|=1\quad\text{而}\quad d_\times(n,n+1)\ge2K}
\]

可令 `K` 任意大。

---

## 6. T5 — 乘法距离 1、加法距离任意大：成立

对任意 `n>=1`，

\[
\gcd(n,2n)=n,
\]

所以

\[
d_\times(n,2n)=\Omega(1)+\Omega(2)=1.
\]

但

\[
|2n-n|=n\to\infty.
\]

即

\[
\boxed{d_\times(n,2n)=1\quad\text{而}\quad |2n-n|\to\infty.}
\]

### 双向无界失真结论

T4 排除任何统一的界

\[
d_\times(m,n)\le A|m-n|+B,
\]

T5 排除任何统一的反向界

\[
|m-n|\le A d_\times(m,n)+B.
\]

所以恒等映射在普通加法距离与素因子编辑距离之间，两个方向都不是大尺度 Lipschitz。两种“邻近”是实质不同的局部结构，而不是换一个坐标刻度即可互换。

加权距离

\[
d_{\log\times}(m,n)=\log\!\left(\frac m g\frac n g\right)
\]

也有同样现象：CRT 连续合数使它在加法距离 1 时无界，而 `n,2n` 使它恒为 `log 2`、普通差值却无界。因此单纯改用 logarithmic weight 不能消除两种局部性的分离。

---

## 7. 固定 Omega 的 M2 壳：精确图距离与成熟结构定位

在固定 `Omega=k` 壳中，M2 一步就是删除一个 prime token 再加入一个 prime token。

对同壳 `m,n`，每一步最多修正两个 `l1` 指数单位，所以任意 M2 路径长度至少 `d_times/2`。反过来，将 `m/g` 中的 unmatched tokens 与 `n/g` 中的 unmatched tokens 一一替换，恰好需要

\[
\frac{d_\times(m,n)}2
\]

步。因此

\[
\boxed{
\operatorname{dist}_{M2,k}(m,n)=\frac12d_\times(m,n)
=k-\Omega(\gcd(m,n)).
}
\]

### 成熟图论翻译

固定前 `r` 个素数 `p_1,...,p_r` 后，`Omega=k` 的 exponent vectors 正是大小为 `k` 的 multiset configurations。一次 M2 替换就是在完整图 `K_r` 上移动一个不可区分 token，允许一个顶点容纳多个 tokens。因此该图精确同构于 Hammack–Smith 意义下的 reduced power

\[
\boxed{K_r^{(k)}}.
\]

这不是 Enterprise Math 新图族。Hammack 与 Smith 在 *Cycle bases of reduced powers of graphs*, Ars Mathematica Contemporanea 12 (2017), 183–203, DOI `10.26493/1855-3974.856.4d2` 中给出了 reduced power 的该 token-configuration 定义。

若禁止重复素因子，只保留 squarefree `k`-almost-primes，则得到普通 token graph；对底图 `K_r` 即 Johnson graph `J(r,k)`。

---

## 8. 半素数 M2 壳的完整有限结构

令

\[
G_r=\{p_i p_j:1\le i\le j\le r\}
\]

按 M2 邻接成图。

### 8.1 顶点数

\[
\boxed{|V(G_r)|=\binom{r+1}{2}=\frac{r(r+1)}2.}
\]

### 8.2 度数

对平方顶点 `p_i^2`，一次替换只能把一个 `p_i` 换成其他 `r-1` 个素数，所以

\[
\deg(p_i^2)=r-1.
\]

对 squarefree 顶点 `p_i p_j (i!=j)`，可以替换第一个 token 或第二个 token，各有 `r-1` 个不同结果，故

\[
\deg(p_i p_j)=2(r-1).
\]

因此 `r>=3` 时已经存在度数大于 2 的顶点；完整半素数 M2 壳不可能本身是一条线。

### 8.3 边数

握手定理给出

\[
\boxed{|E(G_r)|=\frac{r^2(r-1)}2.}
\]

### 8.4 直径

任意两个不同半素数若共享一个因子，则距离 1；若互素，例如 `ab` 与 `cd`，则中间点 `ac` 同时与二者共享一个 token，所以距离 2。因此

\[
\boxed{\operatorname{diam}(G_r)=2\quad(r\ge2).}
\]

半素数乘法壳因此不是“稀疏的一条数轴”，而是随素数窗口增大变得高度分支、但图直径始终为 2 的离散壳。

---

## 9. 一维乘法数轴的两个独立阻碍

### 9.1 度数阻碍

离散全序的前驱/后继相邻图中，每个点度数至多为 2。

但在完整 M1 图中，对任意 `n` 与任意素数 `p`，都有

\[
n\sim_{\times,1}np.
\]

所以每个 `n` 有无穷多个向上 M1 邻居。完整 M1 图不可能等同于任何离散全序的邻接图。

固定有限 `r` 个素数也一样：只要一个点在至少三个素数方向上仍可乘入，其度数就大于 2。

更强地，取最自然的有限 simplex window `Omega<=1`，顶点为

\[
\{1,p_1,...,p_r\},
\]

M1 图就是星 `K_{1,r}`。当 `r>=3` 时它甚至没有覆盖全部顶点的 Hamilton path。因此不存在一个能够对所有这种自然窗口都保持“M1 每一步且全覆盖”的统一 Hamilton spine 方案。

### 9.2 纯乘法 canonicality 的素数重标号阻碍

正整数乘法幺半群是以所有素数为自由生成元的自由交换幺半群。任意素数置换都会唯一延伸为乘法幺半群自同构。

因此，如果所谓“纯乘法 canonical number axis”要求其严格全序仅由乘法结构决定、并在所有乘法自同构下保持不变，就会立即矛盾：假设两枚素数 `p,q` 在该严格序中有 `p<_*q`，交换 `p,q` 的自同构会迫使 `q<_*p`。

故

\[
\boxed{\text{bare multiplicative structure admits no automorphism-invariant strict total ordering of the primes.}}
\]

这与项目工具箱 `T7_FINITE_SYMMETRY_EQUIVARIANCE` 的 canonical-choice obstruction 完全一致：在无固定点的完整重标号对称下，单值 canonical choice 需要额外 symmetry-breaking datum。

所以任何真正的一维 spine 都必须额外选择某种 gauge，例如普通素数大小顺序、权重、指定首素数或其他标签。它可以是有用坐标，但不能再声称是“仅由乘法邻接自己强制出来的唯一数轴”。

Toolbox outcome: `REUSE / T7_FINITE_SYMMETRY_EQUIVARIANCE`; no new general-purpose symmetry tool was introduced. The census/checker is task-specific evidence machinery, not a promoted toolbox family.

---

## 10. 一个 surviving candidate：半素数前缀兼容 Gray ray

虽然完整 M2 壳不是线，但可以选择一条每一步都保持 M2 邻接的主脊。

令素数按普通大小排列

\[
p_1<p_2<p_3<\cdots.
\]

定义

\[
H_1=(p_1^2).
\]

对 `j>=2`，定义新块

\[
B_j=
\bigl(
 p_{j-1}p_j,
 p_1p_j,
 p_2p_j,
 \ldots,
 p_{j-2}p_j,
 p_j^2
\bigr),
\]

其中 `j=2` 时中间列表为空。递归置

\[
\boxed{H_j=H_{j-1}\Vert B_j.}
\]

例如前几项为

\[
p_1^2,
 p_1p_2,p_2^2,
 p_2p_3,p_1p_3,p_3^2,
 p_3p_4,p_1p_4,p_2p_4,p_4^2,\ldots
\]

### Theorem H — prefix-compatible semiprime Hamilton–Gray path

对每个 `r>=1`：

1. `H_r` 恰好包含所有 `p_i p_j, 1<=i<=j<=r` 一次；
2. `H_r` 中任意连续两项都满足 M2 邻接；
3. `H_r` 是 `H_{r+1}` 的严格前缀；
4. `H_r` 的末项恒为 `p_r^2`。

#### 证明

按较大素数下标 `j` 分类，每个半素数恰好在唯一的块 `B_j` 中首次出现，所以覆盖且无重复。块 `B_j` 内所有项都含 `p_j`，连续两项共享一个 prime token；而上一块的末项是 `p_{j-1}^2`，新块首项是 `p_{j-1}p_j`，也共享一个 token。拼接只在末尾添加新块，所以前缀兼容。最后一项按定义是 `p_j^2`。证毕。

取直接极限得到一条遍历**全部半素数恰好一次**的无限 M2 Gray ray `H_infty`。

### 10.1 显式 rank

令

\[
T_{j-1}=\frac{j(j-1)}2
\]

为 `B_j` 开始前已有顶点数。使用 0-based rank：

- `rank(p_1^2)=0`；
- `rank(p_{j-1}p_j)=T_{j-1}`；
- 对 `1<=i<=j-2`，
  \[
  rank(p_ip_j)=T_{j-1}+i;
  \]
- `rank(p_j^2)=T_{j-1}+j-1=j(j+1)/2-1`。

因此一旦半素数分解已知，其 Gray-ray 坐标可直接计算。

但要注意：该构造用普通大小关系 `p_1<p_2<...` 打破了素数置换对称性，所以它是**canonical relative to the standard prime order**，不是 bare multiplicative monoid 内部唯一强制出的序。

---

## 11. 一维主脊不可避免地丢失几乎全部 M2 邻接

`G_r` 有

\[
V_r=\frac{r(r+1)}2,
\qquad
E_r=\frac{r^2(r-1)}2.
\]

任何覆盖全部顶点的 Hamilton path 都只有 `V_r-1` 条轴相邻边。即使这 `V_r-1` 条全部都是合法 M2 边，它直接保留的完整 M2 边比例也至多

\[
\frac{V_r-1}{E_r}
=\frac{r+2}{r^2}.
\]

所以

\[
\boxed{
\frac{\text{axis-retained M2 edges}}{\text{all M2 edges}}
=\frac{r+2}{r^2}\longrightarrow0.
}
\]

这是与具体 Gray code 无关的结构性上界。任何一条线都只能保留渐近为零比例的半素数乘法局部关系。

对上面显式 `H_r` 还可以精确量化被压扁的边伸长。若把 `H_r` 上 rank 差作为线距离，则对 `r>=3`，原本的一条 M2 边在 spine 上的最大距离为

\[
\boxed{
\max_{uv\in E(G_r)}|rank(u)-rank(v)|
=\frac{r(r-1)}2+1.
}
\]

该最大值由 `p_1^2` 与 `p_1p_r` 达到。也就是说，完整图中距离 1 的邻居可被线性坐标拉开 `Theta(r^2)`。

因此这条 Gray ray 的正确定位是：

`GOOD TRAVERSAL / BAD COMPLETE GEOMETRY REPLACEMENT`。

---

## 12. 最强 surviving multiplicative coordinate

任务要求在一维失败后找最小正确替代物。当前最强方案是分层结构：

### 12.1 径向坐标

\[
R(n)=\Omega(n).
\]

M1 边恰好跨越相邻径向层 `k <-> k+1`。

### 12.2 壳内坐标

在 `Omega=k` 壳内使用有限支撑素指数向量

\[
\nu(n)=(v_p(n))_p,
\qquad
\sum_pv_p(n)=k.
\]

M2 是沿根方向 `e_q-e_p` 的一个单位 token transfer，壳内图距离为 `d_times/2`。

### 12.3 可选的一维遍历坐标

对于 `k=2`，可以附加 `H_infty` 的 rank 作为遍历索引；它提供唯一位置、可计算性和窗口前缀兼容，但不是完整邻接结构。

于是最诚实的对象不是“另一条实数线”，而是

\[
\boxed{
\text{graded multiplicative graph}
\quad+\quad
\text{fixed-Omega replacement shells}
\quad+\quad
\text{optional Gray spine}.
}
\]

一般结构与

\[
\mathbb N_{>0}\cong\bigoplus_{p\ \mathrm{prime}}\mathbb N_0
\]

完全兼容；这里不提出把自由交换幺半群/指数格本身当作新颖对象。

---

## 13. 精确有限普查：`1 <= n <= 10^7`

完整机器可复核数据冻结在：

`research_artifacts/MULTIPLICATIVE_ADJACENCY_NUMBER_AXIS/census_1e7.json`

复核器：

`research_checks/MULTIPLICATIVE_ADJACENCY_NUMBER_AXIS_CHECK_20260829.py --full`

独立实现使用标准库 linear sieve、exact gcd 与整数 `Omega/omega`；另一次 NumPy/Numba 独立计算得到相同结果。

### 13.1 相邻半素数

窗口内半素数总数：

\[
1,904,324.
\]

相邻半素数对：

\[
1,904,323.
\]

距离分布：

| `d_times` | 对数 | 占比 |
|---:|---:|---:|
| 2 | 41,533 | 2.180985% |
| 4 | 1,862,790 | 97.819015% |

这与 T2 完全吻合：只有共享一个 prime token 与互素两类。

`d_times=2` 的共享 gcd 素数计数：

| shared prime | 对数 |
|---:|---:|
| 2 | 28,623 |
| 3 | 10,338 |
| 5 | 1,973 |
| 7 | 514 |
| 11 | 70 |
| 13 | 15 |

在该窗口中没有共享素数 `>=17` 的相邻半素数 M2 对；这只是有限事实，不作全称外推。

相邻半素数最大普通间隙为 74：

\[
5,835,191=47\cdot124153,
\]

\[
5,835,265=5\cdot1167053,
\]

二者互素，`d_times=4`。

M2-相邻的相邻半素数中，最大普通间隙为 48：

\[
6,950,631=3\cdot2,316,877,
\]

\[
6,950,679=3\cdot2,316,893.
\]

### 13.2 M2 比例随窗口的有限趋势

| 上界 | 相邻半素数对 | `d=2` 对 | 比例 |
|---:|---:|---:|---:|
| `10^2` | 33 | 5 | 15.1515% |
| `10^3` | 298 | 16 | 5.3691% |
| `10^4` | 2,624 | 89 | 3.3918% |
| `10^5` | 23,377 | 602 | 2.5752% |
| `10^6` | 210,034 | 4,855 | 2.3115% |
| `10^7` | 1,904,323 | 41,533 | 2.1810% |

该下降趋势只登记为实验现象；本任务没有证明其极限存在或为 0。

### 13.3 相邻合数

窗口内合数总数：

\[
9,335,420,
\]

相邻合数对：

\[
9,335,419.
\]

普通间距：

- gap 1：8,670,842 对；
- gap 2：664,577 对；
- 无其他 gap，与第 4 节全称证明一致。

乘法距离从 2 到 26 均有出现；完整计数保存在 census JSON。

唯一 `d_times=2` 对为 `(4,6)`。

窗口内最大观测距离为 26，出现在连续整数

\[
1,048,575=3\cdot5^2\cdot11\cdot31\cdot41,
\]

\[
1,048,576=2^{20}.
\]

二者互素，因此

\[
d_\times=6+20=26.
\]

这给出了非常直观的“加法只差 1、乘法结构相距很远”样本；T4 则把这种现象提升为任意大距离的全称构造。

### 13.4 反向有限极端

在同一窗口内，

\[
5,000,000\leftrightarrow10,000,000
\]

满足 M1 距离 1，但普通差值 5,000,000。

半素数 M2 中，因 `4=2^2` 且 `9,999,998=2\cdot4,999,999`，有

\[
d_\times(4,9,999,998)=2,
\]

普通差值则为 9,999,994。

这再次显示乘法邻近与普通数值邻近可彻底脱钩。

---

## 14. 与成熟结构的去重结论

### 14.1 M1

M1 是正整数整除偏序的覆盖图；在素指数坐标中就是有限支撑非负整数格，每条边改变一个坐标 1。`d_times` 是其 `l1` 图距离。该一般结构不是新颖性来源。

### 14.2 M2

固定 `Omega=k` M2 壳是 `K_r` 的 reduced `k`th power 在有限素数窗中的算术实现；squarefree 子图是 token/Johnson 图。Hammack–Smith reduced-power 文献已覆盖一般 token-configuration 图概念。

### 14.3 Gray code

Ruskey 与 Savage, *A Gray Code for Combinations of a Multiset*, European Journal of Combinatorics 17 (1996), 493–500, DOI `10.1006/eujc.1996.0043` 已证明 multiset combinations 可按 successive combinations differ by one element 的方式生成。因此“固定 Omega 壳有 minimal-change listing”本身不能作为新颖性主张。

本任务只保留更窄的项目特化：显式半素数 `H_r` 构造、其素数窗口**前缀兼容性**、rank 公式，以及对完整 M2 邻接的 edge-retention / stretch 量化。是否已有文献给出完全相同的嵌套 prime-window 公式未在本任务中主张或排除，因此不作外部 novelty claim。

### 14.4 log 坐标

`log n` 只把乘法变成加法权重，不恢复 prime-token 支撑局部性；它不能替代 M1/M2 图。

---

## 15. 对半素数分解是否有真实新搜索信息

结论：

`NO FACTOR-BLIND FACTORIZATION GAIN ESTABLISHED`。

原因很直接：

1. 要把未知半素数 `N` 放入 M2 壳的精确 vertex / Gray-ray rank，必须知道它的两个 prime tokens，等价于已经知道分解；
2. 判断另一个半素数是否为其 M2 邻居，本质上要知道共享 prime factor；
3. `d_times` 的精确计算虽然可以通过 gcd 计算已知两数之间的关系，但对单个待分解 `N` 没有自动给出非平凡因子；
4. 当前 Gray ray 是 factor-aware traversal，不是 factor-blind search oracle。

所以该方向目前的独立价值是**局部几何与搜索顺序理论**，而不是已经实现的半素数分解加速。

可以保留一个弱交叉方向：若未来能从 `N` 的 factor-blind 可观测量预测其 Gray block / shared-factor neighborhood，并在严格盲测下稳定缩减候选，才升级为分解收益。当前没有这种证据。

---

## 16. Hard-target disposition

- T1 fixed-Omega parity: `PROVED`。
- T2 semiprime gcd classification: `PROVED`，含平方情形。
- T3 adjacent composites not M1: `PROVED + STRENGTHENED`；唯一 `d=2` 相邻合数是 `4,6`。
- T4 additive-near / multiplicative-far: `PROVED BY CRT`。
- T5 multiplicative-near / additive-far: `PROVED`。
- exact finite census: `COMPLETE TO 10^7`，机器可复核。
- complete M1 as 1D axis: `IMPOSSIBLE` by degree；纯乘法 canonical total order另有 prime-relabeling symmetry obstruction。
- finite M1 Hamilton spine: `NOT UNIVERSALLY AVAILABLE`；自然 `Omega<=1,r>=3` 窗口已由 star obstruction 排除。
- fixed-Omega M2 shell: `EXACTLY CLASSIFIED` as reduced-power token geometry；壳内距离 `d_times/2`。
- semiprime M2 spine: `EXPLICIT PREFIX-COMPATIBLE HAMILTON-GRAY RAY CONSTRUCTED`。
- line-versus-shell information loss: `EXACTLY QUANTIFIED`; any Hamilton line retains fraction `(r+2)/r^2 -> 0` of M2 edges。
- prior-art dedup: `DONE / NOVELTY DOWNGRADED WHERE REQUIRED`。
- factorization gain: `NOT ESTABLISHED`。

因此任务满足 Success criterion 2：T1–T5 完成；自然的一维完整乘法数轴被结构性排除；同时给出更小而精确的 `M1 graded graph + M2 shells`，并额外构造了一个可作为遍历坐标的半素数前缀 Gray ray。

---

## 17. 可继续的高价值后继问题

本 return 不把下列问题偷偷并入当前结论，但它们值得单独发布 successor task：

1. **相邻半素数共享因子率的渐近问题**：有限窗口 `d=2` 比例从 `10^2` 的 15.15% 降至 `10^7` 的 2.18%；证明其极限、上界或与 prime-gap 统计的关系。
2. **最优一维压缩问题**：在 `G_r` 的所有 Hamilton–Gray paths 中，最小化最大 omitted-edge stretch / 平均 stretch / bandwidth；比较本文 `H_r` 的 `Theta(r^2)` 最大 stretch 是否量级最优。
3. **一般 `Omega=k` 的嵌套 Gray spine**：Ruskey–Savage 给出一般 minimal-change listing，但项目关心更强的 prime-window projective compatibility；确定对所有 `k` 是否存在 `H_{r,k}` 且 `H_{r,k}` 是 `H_{r+1,k}` 的前缀。
4. **factor-blind surrogate**：寻找不需要预先分解 `N`、但能预测其 M2 shell neighborhood 的可计算观测；必须盲测，失败则明确 no-go。

---

## 18. Reproducibility

Exact census artifact:

`research_artifacts/MULTIPLICATIVE_ADJACENCY_NUMBER_AXIS/census_1e7.json`

Checker:

`python research_checks/MULTIPLICATIVE_ADJACENCY_NUMBER_AXIS_CHECK_20260829.py --full`

The checker independently verifies:

- dense exact regression of the gcd distance identity and fixed-Omega parity;
- CRT witnesses for `K=2..32`;
- prefix-compatible semiprime Gray spines through `r=64`;
- exact Gray edge-retention formula;
- exact maximum spine stretch through `r=24`;
- the `10^6` and `10^7` census regression constants;
- no adjacent-composite M1 counterexample in the full finite census.

Local executions performed in this research session:

- `--limit 1000000`: `PASS`;
- `--full` (`10^7`): `PASS`.

No floating-point arithmetic is used for theorem truth. Finite ratios are reporting-only.
