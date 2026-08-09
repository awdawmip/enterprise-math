# P025 补充 09 —— 用整数区间交精确求解 Rank-Two Absorption Access

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner：`program/p025-abc-support-collapse`  
依赖：P025 补充 07–08  
Hard block：`NONE`

## 1. 范围

补充 07–08 已经把 absorption-optimal access radius 化为

\[
\nu
=\min\{\|x\|_\infty:
\alpha\cdot x=0,
\ \beta\cdot x=\pm d\},
\]

其中

\[
d=\operatorname{cont}(\alpha\wedge\beta)>0.
\]

在一般 witness dimension 下，这是 affine-lattice minimum problem。

本补充在

\[
\boxed{\omega(abc)=3}
\]

时把它完全精确求解；此时 additive witness lattice 的秩为 2。

整个求解只用整数线性代数与区间运算，并从 exact reference path 中删除 cubic witness-ball enumeration。

## 2. P025-T25 —— Floor-attaining set 是一条 primitive integer affine line

假设恰有三个 prime coordinates，且 Wronskian 在 additive witness lattice 上非退化。

令

\[
\alpha,\beta\in\mathbb Z^3
\]

分别为 primitive additive row 与 raw Wronskian row。定义 cross product

\[
c=\alpha\times\beta.
\]

其坐标 content 为

\[
\operatorname{cont}(c)=d,
\]

即补充 04 的正 Wronskian image generator。固定整体符号后定义

\[
\boxed{n_0=c/d}
\]

于是 `n_0` primitive，并且

\[
\boxed{
\ker_{\mathbb Z}\alpha
\cap
\ker_{\mathbb Z}\beta
=
\mathbb Z n_0.
}
\]

现在任取一个整数 witness `x_0` 满足

\[
\alpha\cdot x_0=0,
\qquad
\beta\cdot x_0=d.
\]

例如补充 08 已经能够 constructively 给出这样的 `x_0`。

则完整 positive-generator slice 恰为

\[
\boxed{
\{x\in\mathbb Z^3:
\alpha\cdot x=0,
\beta\cdot x=d\}
=
x_0+\mathbb Z n_0.
}
\]

negative-generator slice 正好是它的整体取负，因此具有同样的最小 `L_infinity` norm。

### 证明

因为 `alpha,beta` 的有理秩为 2，它们的 common rational kernel 就是由 `alpha x beta` 张成的一条直线。除以 content 后得到 saturated integer kernel 的 primitive generator。若 `x` 与 `x_0` 都满足同一个非齐次系统，则二者之差属于 common integer kernel，所以唯一写成 `k n_0`。反向显然。∎

## 3. P025-T26 —— 精确 radius feasibility 就是整数区间求交

写成

\[
x_0=(x_1,x_2,x_3),
\qquad
n_0=(n_1,n_2,n_3).
\]

对候选 radius `B>=0`，一个参数 `k in Z` 可行，当且仅当

\[
|x_i+k n_i|\le B
\qquad(i=1,2,3).
\]

每个坐标都给参数 `k` 一个整数区间 `I_i(B)`：

- 若 `n_i>0`，
  \[
  \left\lceil\frac{-B-x_i}{n_i}\right\rceil
  \le k\le
  \left\lfloor\frac{B-x_i}{n_i}\right\rfloor;
  \]
- 若 `n_i<0`，令 `m_i=-n_i>0`，等价写成
  \[
  \left\lceil\frac{x_i-B}{m_i}\right\rceil
  \le k\le
  \left\lfloor\frac{x_i+B}{m_i}\right\rfloor;
  \]
- 若 `n_i=0`，则只需 `|x_i|<=B`，而不对参数增加限制。

因此

\[
\boxed{
B\text{ 可行}
\iff
\bigcap_{i=1}^3 I_i(B)\cap\mathbb Z
\ne\varnothing.
}
\]

所有区间端点都只需要整数 floor/ceiling division。

## 4. P025-T27 —— 通过有限二分精确求 `nu`

`B` 的可行性关于半径单调：若某个参数在 `B` 下可行，则在任意更大半径下仍可行。

constructive Bezout witness `x_0` 给出有限上界

\[
\nu\le\|x_0\|_\infty.
\]

于是只需在有限整数区间

\[
0\le B\le\|x_0\|_\infty
\]

上，用 P025-T26 的区间交判据做二分，即可得到精确 optimum

\[
\boxed{
\nu
=
\min_{k\in\mathbb Z}
\|x_0+k n_0\|_\infty.
}
\]

radius 检查次数只随 constructive upper bound 的对数增长，而每次检查最多求三个整数区间的交集。

整个过程是 exact arithmetic，不需要 float optimization，也不需要 bounded witness-ball enumeration。

## 5. 再看 `1+242=243`

对

\[
1+242=243,
\]

补充 08 的 constructive floor witness 是

\[
x_0=(-405,11,1215).
\]

primitive common-kernel direction 为

\[
\boxed{n_0=(4,0,-11).}
\]

所以所有 positive-generator witnesses 都是

\[
(-405,11,1215)+k(4,0,-11).
\]

当 radius 为 `26` 时，三个坐标约束对应的整数参数区间没有公共交集。

当 radius 为 `27` 时，交集精确收缩为

\[
\boxed{k=108.}
\]

因此得到

\[
\boxed{x=(27,11,27)}
\]

并且

\[
\boxed{\nu=27.}
\]

此前 cubic enumeration 已经完全不再需要。

## 6. 校准样例

### `2+3=5`

\[
n_0=(2,3,5),
\qquad
\nu=2.
\]

直接 Bezout certificate 已经 optimal。

### `2+7=9`

\[
n_0=(4,3,14),
\qquad
\nu=5,
\]

同样与简单 Bezout certificate 一致。

### `1+242=243`

同一 exact algorithm 把 constructive upper bound `1215` 直接压到真正的 `27`，完全不搜索 ambient cube。

## 7. 架构含义

这一阶段给出如下明确链条：

\[
\boxed{
\text{minor gcd}
\to
\text{arithmetic floor }d
\to
\text{一个 floor witness }x_0
\to
\text{affine kernel direction }n_0
\to
\text{exact minimum access radius }\nu.
}
\]

每一步消掉的是不同不确定性：

- minor gcd 决定**哪个 Wronskian scale 可以达到**；
- Bezout witness 决定**至少存在一个 preimage**；
- affine direction 决定**全部替代 preimages**；
- interval intersection 决定**哪个 preimage 的 task cost 最小**。

因此，一个 certificate pipeline 可以在不枚举全部 witnesses 的情况下同时做到有限、精确。

## 8. 与成熟数学的关系

三变量中两个独立整数线性方程的解集化为 affine rank-one lattice，并在该直线上最小化凸 norm，属于标准 integer optimization / closest-lattice-point 范畴。

P025 不主张以下工具本身的新颖性：

- cross product 与 primitive integer kernel；
- one-dimensional lattice coset；
- interval feasibility；
- 对单调整数 predicate 的 binary search。

项目侧真正研究的是这些工具在 abc/Pasten witness language 上诱导出的**certificate access precision**。

## 9. 可执行资产

新增：

- `src/enterprise_math/abc_absorption_rank2.py`
  - primitive common-kernel direction；
  - 给定 radius 的 exact parameter interval；
  - 单调有限 feasibility test；
  - `omega(abc)=3` 时 `nu` 的 exact binary-search solver。
- `tests/test_abc_absorption_rank2.py`
  - 三个工作三元组的 exact directions；
  - `2+3=5`、`2+7=9` 与 `1+242=243` 的 exact optima；
  - 最后一例 radius `26` 不可行、`27` 恰为 singleton feasible parameter 的 sharp boundary。

同时，Bezout regression 已改为消费这个 exact affine solver，不再重复 cubic witness-ball scan。

## 10. 下一前沿

不存在 hard block，继续：

1. 推导 minimizing parameter `k` 的 closed 或 near-closed modular formula，而不是先二分 radius；
2. 把 rank-two solver 特化到 `1+qr=p^m` 等 structured families，并寻找 `nu` 的显式公式；
3. 比较 `nu` 与 additive witness lattice 的 first successive minimum 以及 Pasten Geometry-of-Numbers bounds；
4. 搜索 naive Bezout certificate / exact `nu` ratio 是否存在无界 family；
5. 把 affine-line 思路推广到 `omega(abc)>3` 的 quotient lattices，同时保持 existence 与 minimum access precision 的区分。
