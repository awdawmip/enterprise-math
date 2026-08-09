# P022 —— 超越本征图距离的测地线重数

状态：`ACTIVE RESEARCH NOTE / EXACT FINITE COMBINATORICS / NOVELTY UNVERIFIED`  
归属：`program/p022-geometry-v2`  
范围：本征无权图几何、`A_p` 根格、简单立方对照、最短路与区间重数  
共享依赖：P012 本征图度量；A4 的 count-enriched support 结果仅作为通用解释层

## 1. 为什么旧的测地缺陷在本征图几何上会自动坍缩

历史 A3↔A4 bridge 对一个整数度量 `rho` 定义了 radius-one graph `G_1` 以及

\[
\Gamma(x,z)=d_{G_1}(x,z)-\rho(x,z).
\]

当声明的直接度量与实际可表示的 unit-step geometry 可能不一致时，这个量很有用。

但 P022 当前研究的是**本征无权图自己的 shortest-path metric**。这时 radius-one graph 本来就是原图，因此

\[
\boxed{\Gamma\equiv0.}
\]

更一般地，设 `d` 是任意连通无权图的最短路距离，并定义

\[
R_r=\{(x,z):d(x,z)\le r\}.
\]

则所有 `r,s>=0` 都满足

\[
\boxed{R_r;R_s=R_{r+s}.}
\]

正向包含来自三角不等式；反向包含只需取一条从 `x` 到 `z` 的最短路，在至多 `r` 步处选择中间点，剩余路段自然不超过 `s`。

这是标准最短路事实，不作创新性主张。但它对当前路线有直接纠偏意义：

> **如果 FCC、SC、HCP 或其他候选使用的 `rho` 就是各自本征无权图距离，P022 不应再用 `Gamma` 区分它们。Boolean/existence 层已经完全坍缩。**

真正还能区分几何的是**重数层**。

## 2. P022-GM01 —— 测地区间层就是最小总预算下的 count coefficient

对图中两点 `x,z`，记

\[
d=d(x,z).
\]

对 `0<=a<=d` 定义测地区间层

\[
I_a(x,z)=\{y:d(x,y)=a,\ d(y,z)=d-a\}.
\]

在 count-enriched 的 two-stage support 中，最小总预算上的系数恰好是

\[
\boxed{H_{xz}(a,d-a)=|I_a(x,z)|.}
\]

所以 existence 语义只告诉我们“每一层至少有一个点”，而整数序列

\[
\boxed{\mathcal I(x,z)=(|I_0|,|I_1|,\ldots,|I_d|)}
\]

记录了每个深度仍然存在多少实际测地选择。

进一步，把 future depth 取到 `d`，并要求每一段 cost 都等于 `1`，则 cost vector

\[
(1,1,\ldots,1)
\]

的 coefficient 恰好就是 `x` 到 `z` 的最短路条数，记为

\[
g(x,z).
\]

因此本征图几何自然形成

\[
\text{distance}
\longrightarrow
\text{interval-layer multiplicity}
\longrightarrow
\text{full shortest-path multiplicity}
\]

这一层级，而且全部是有限整数对象。

## 3. P022-GM02 —— `A_p` 根格的最短路条数闭式

继续使用 P022 的工作格

\[
A_p=\{v\in\mathbb Z^{p+1}:\sum_i v_i=0\},
\]

primitive moves 为 `e_i-e_j`。

对位移 `v`，令

\[
r=d_G(0,v)=\sum_{v_i>0}v_i=\sum_{v_j<0}(-v_j).
\]

每条最短路恰好进行 `r` 次单位搬运：每一步从某个负坐标向某个正坐标转移一个单位。

正坐标作为 destination 的时间序列具有 multiplicities `v_i`，故排列数为

\[
\frac{r!}{\prod_{v_i>0}v_i!}.
\]

负坐标作为 source 的时间序列具有 multiplicities `-v_j`，故排列数为

\[
\frac{r!}{\prod_{v_j<0}(-v_j)!}.
\]

两条序列按时间位置独立配对，因此

\[
\boxed{
g_{A_p}(v)=
\frac{(r!)^2}
{\left(\prod_{v_i>0}v_i!\right)
 \left(\prod_{v_j<0}(-v_j)!\right)}.
}
\]

整个公式只有整数阶乘与整除，不引入连续几何或概率。

### 同一个 shell 内部已经不是同一种几何状态

在 `A_3` 的 graph radius `2` 上：

\[
(2,-2,0,0)\Rightarrow g=1,
\]

\[
(1,1,-2,0)\Rightarrow g=2,
\]

\[
(1,1,-1,-1)\Rightarrow g=4.
\]

三者距离完全相同，但最短路数相差四倍。

因此 shell cardinality 不是完整的有限几何信息。

## 4. P022-GM03 —— `A_p` 测地区间层的精确公式

设 `v` 的正坐标幅值为

\[
p_1,\ldots,p_a,
\]

负坐标幅值为

\[
n_1,\ldots,n_b,
\]

且两边总和都为 `r`。

定义整数多项式

\[
P_v(t)=\prod_{i=1}^a(1+t+\cdots+t^{p_i}),
\]

\[
N_v(t)=\prod_{j=1}^b(1+t+\cdots+t^{n_j}).
\]

一个位于第 `k` 层的 geodesic intermediate state，需要独立选择：正侧已经完成多少需求、负侧已经修复多少 deficit，并且两边完成量都恰好为 `k`。于是

\[
\boxed{
|I_k(0,v)|=[t^k]P_v(t)\,[t^k]N_v(t).
}
\]

上面三个 radius-two endpoint 因而得到：

- `(2,-2,0,0)` → `(1,1,1)`；
- `(1,1,-2,0)` → `(1,2,1)`；
- `(1,1,-1,-1)` → `(1,4,1)`。

profile 在 path reversal 下自然回文，但内部层数值仍保留被 distance 擦掉的方向/endpoint type 信息。

## 5. P022-GM04 —— simple-cubic 的同尺度对照

对 `Z^d` 的标准坐标轴 adjacency，令

\[
r=\sum_i|v_i|.
\]

最短路数是精确 multinomial：

\[
\boxed{
g_{SC}(v)=\frac{r!}{\prod_i|v_i|!}.}
\]

测地区间 profile 则为

\[
\boxed{
|I_k^{SC}(0,v)|
=[t^k]\prod_i(1+t+\cdots+t^{|v_i|}).
}
\]

因此 P022 可以在完全相同的 native graph-distance 语义下比较不同离散几何，而不是再用外加 Euclidean norm 做桥接。

## 6. P022-GM05 —— 整个 graph shell 的总最短路重数

同一距离 shell 中不同 endpoint 有不同重数。定义

\[
T(r)=\sum_{d(0,v)=r}g(v).
\]

这是一个整数总量，本身不解释成概率或 entropy。

### `A_p`

记 `n=p+1`。若 endpoint 恰好用了 `a>=1` 个正坐标、`b>=1` 个负坐标，先选择这两组互不相交的坐标，再对所有 `r` 的正整数 compositions 求 multinomial path counts 之和。

把 `r` 个有序时间位置 onto 到 `a` 个非空 destination labels 的数量为

\[
a!\,S(r,a),
\]

其中 `S(r,a)` 是第二类 Stirling 数。负侧同理。所以

\[
\boxed{
T_{A_p}(r)=
\sum_{\substack{a,b\ge1\\a+b\le p+1}}
\binom{p+1}{a}\binom{p+1-a}{b}
\,a!S(r,a)\,b!S(r,b)
}
\]

对 `r>=1` 成立，并规定 `T_{A_p}(0)=1`。

### simple cubic

如果 endpoint 恰好用了 `k` 个坐标轴，则先选择坐标轴，再选择每个轴的符号，然后统计 onto axis-label sequence。因此

\[
\boxed{
T_{SC_d}(r)=
\sum_{k=1}^{\min(d,r)}
\binom dk 2^k k!S(r,k)
}
\]

对 `r>=1` 成立，并规定 `T_{SC_d}(0)=1`。

这些是精确有限组合推导；历史独立性与创新性尚未完成 prior-art audit。

## 7. P022-GM06 —— 三维中出现指数级分离

对当前 FCC-type 工作模型 `A_3`：

\[
\boxed{
T_{A_3}(r)=
6\cdot4^r+8\cdot3^r-24\cdot2^r+12,
\qquad r\ge1.
}
\]

对三维 simple-cubic：

\[
\boxed{
T_{SC_3}(r)=
8\cdot3^r-12\cdot2^r+6,
\qquad r\ge1.
}
\]

前四个 shell：

| 半径 `r` | `A_3/FCC` shell size | `A_3/FCC` total geodesics | `SC_3` shell size | `SC_3` total geodesics |
|---:|---:|---:|---:|---:|
| 1 | 12 | 12 | 6 | 6 |
| 2 | 42 | 84 | 18 | 30 |
| 3 | 92 | 420 | 38 | 126 |
| 4 | 162 | 1812 | 66 | 462 |

shell size 只按二次多项式增长：`A_3` 为 `10r^2+2`，`SC_3` 为 `4r^2+2`。但是最短路总重数的主导增长底数不同：

\[
T_{A_3}(r)\sim6\cdot4^r,
\qquad
T_{SC_3}(r)\sim8\cdot3^r.
\]

这**不能**推出 FCC 就是物理空间。它只建立了一个比 nearest-neighbor count 和 native-distance existence 更强的数学判别量：

> 两种候选离散几何在 Boolean/existence 层都可能完全 geodesic，但仍拥有指数级不同的有限 witness structure。

## 8. 三维 shell 的 geodesic multiplicity spectrum

不做总和，区别已经存在。

`A_3`：

- `r=1`：`{1:12}`；
- `r=2`：`{1:12, 2:24, 4:6}`；
- `r=3`：`{1:12, 3:48, 6:8, 9:24}`；
- `r=4`：`{1:12, 4:48, 6:24, 12:24, 16:24, 24:24, 36:6}`。

`SC_3`：

- `r=1`：`{1:6}`；
- `r=2`：`{1:6, 2:12}`；
- `r=3`：`{1:6, 3:24, 6:8}`；
- `r=4`：`{1:6, 4:24, 6:12, 12:24}`。

这里 `{m:c}` 表示 shell 中有 `c` 个 endpoint，从原点出发恰好有 `m` 条最短路。

这个 **geodesic multiplicity spectrum** 是完全有限、整数值的 geometry signature。它恰好在 `Gamma` 已经失去区分能力的地方继续保留结构。

## 9. 与旧 A3/A4 bridge 的归属边界

通用的 count-enriched correspondence——coefficient convolution、count→existence shadow、task-relative information erasure——不会因为 P022 提供了几何实例就转归 P022。

P022 此处只拥有：

- native unweighted graph geometry 导致 `Gamma=0` 的几何纠偏；
- `A_p` / SC 最短路闭式；
- `A_p` / SC geodesic interval 闭式；
- shell-total 与 shell-spectrum 特化；
- 具体候选几何之间的比较。

谱系应写成

\[
\text{A5/P012 native graph geometry}
\longrightarrow
\text{P022 concrete lattice}
\longrightarrow
\text{A4 count observable specialization}.
\]

这是 `SPECIALIZATION / CONSUMER`，不是 A4 theorem ownership 的迁移。

## 10. 当前续研含义

P022 下一步应该优先测试那些在 native-metric geodesic collapse 之后仍不会消失的量：

1. 每个 graph shell 的 geodesic multiplicity spectrum；
2. geodesic interval profile 及其方向变化；
3. 当 future operation 真正读取 staged witness multiplicity 时的高阶 path-count coefficient tensor；
4. HCP 与其他 multi-basis / non-Bravais 候选；
5. 与历史 collapsed radial observable `D_p` 的结合——primitive graph metric 可以完全 geodesic，而 `D_p` 的 `0/1` triangle carry 仍然非平凡。

尤其是 **HCP 是下一条最重要压力测试**：FCC 与 HCP 第一配位数相同，因此 radius-one 邻居数已经无法区分；radius-two 以后的 multiplicity spectrum 是很自然的本征有限判别量。

## 11. 可执行参考

P022 v2 owner 新增：

- `src/enterprise_math/p022_geodesic_multiplicity.py`；
- `tests/test_p022_geodesic_multiplicity.py`。

测试把闭式分别与独立递归 path counting、直接 geodesic-interval 枚举，以及维数不超过三、半径不超过四的 shell 显式枚举进行对照。
