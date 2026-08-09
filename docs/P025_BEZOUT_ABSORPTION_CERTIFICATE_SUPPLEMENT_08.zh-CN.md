# P025 补充 08 —— Absorption Floor 的 Constructive Bezout Certificates

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner：`program/p025-abc-support-collapse`  
依赖：P025 补充 04–07  
Hard block：`NONE`

## 1. 问题

补充 04–07 已经把精确 arithmetic floor

\[
\eta_{\min}
\]

与真正达到这个 floor 所需的最小 lattice radius

\[
\nu
\]

区分开。

下一问题刻意采用 constructive 形式：

> 能否只用有限、精确的整数运算，直接生成一个 absorption-optimal witness，而不需要不断扩大 witness ball 搜索？

答案是可以。构造只需要初等 Bezout/syzygy algebra。但更重要的负向结果是：这个显式构造得到的 witness 可能离 norm-optimal 非常远。

## 2. Pair syzygies

令

\[
\alpha=\widehat\alpha\in\mathbb Z^s
\]

为 primitive additive normal，并令

\[
\beta=\beta_{\rm raw}\in\mathbb Z^s
\]

为带规范尺度的 Wronskian row。

对 `i<j` 定义 pair syzygy

\[
\boxed{
 t_{ij}=\alpha_j e_i-\alpha_i e_j.
}
\]

则

\[
\alpha\cdot t_{ij}=0,
\]

所以每个 `t_ij` 都属于 additive witness lattice

\[
T=\ker_{\mathbb Z}\alpha.
\]

定义 signed minor

\[
\boxed{
m_{ij}=\alpha_i\beta_j-\alpha_j\beta_i.}
\]

则

\[
\boxed{
\beta\cdot t_{ij}=-m_{ij}.
}
\]

这些正是补充 04 中 gcd 所使用的同一组 Pluecker/minor coordinates。

## 3. P025-T23 —— Bezout floor certificate

设全部非零 minors 为

\[
m_1,\ldots,m_N,
\]

对应 pair syzygies 为

\[
t_1,\ldots,t_N.
\]

令

\[
d=\gcd(m_1,\ldots,m_N)>0.
\]

取普通整数 Bezout coefficients `z_i`，满足

\[
\sum_{i=1}^N z_i m_i=d.
\]

定义

\[
\boxed{
x_B=-\sum_{i=1}^N z_i t_i.}
\]

则

\[
\boxed{
\alpha\cdot x_B=0,
\qquad
\beta\cdot x_B=d.
}
\]

因此 `x_B` 是一个 non-degenerate additive witness，并且恰好达到 Wronskian image 的正生成元，所以

\[
\boxed{
\eta(x_B)=\eta_{\min}.
}
\]

### 证明

每个 `t_i` 都在 `ker(alpha)` 中，所以它们的整数线性组合 `x_B` 也在其中。同时

\[
\beta\cdot x_B
=-\sum_i z_i(\beta\cdot t_i)
=\sum_i z_i m_i
=d.
\]

补充 04 已证明 `d` 正是 `beta(T)` 的正生成元，因此 `d=M eta_min`。所以该构造 witness 达到精确 absorption floor。∎

### 范围纪律

Bezout identity、单行整数 syzygy 与 minors gcd 都是标准整数代数。P025 不对这个构造本身提出历史优先权主张。

项目侧价值是：现在能从紧凑的 `alpha,beta` 两行直接生成一个精确 certificate，使 absorption optimality 可以有限检查，而无需无界搜索。

## 4. P025-T24 —— 显式 radius 上界

同一个构造还有

\[
\|t_{ij}\|_\infty
=\max(|\alpha_i|,|\alpha_j|).
\]

所以

\[
\boxed{
\nu
\le
\|x_B\|_\infty
\le
\sum_i |z_i|\,
\max(|\alpha_{p_i}|,|\alpha_{q_i}|).
}
\]

因此任意一个针对非零 minors 的显式 Bezout identity，都立即给出 absorption-access radius 的纯整数上界。

这个 bound 是 constructive 的，但一般并不 sharp。

## 5. 简单构造恰好 sharp 的精确例子

### `2+3=5`

在 prime coordinates `(2,3,5)` 上，

\[
\alpha=(1,1,-1),
\qquad
\beta=(-3,2,0).
\]

signed nonzero minors 为

\[
(5,-3,2),
\]

gcd 为 1。一个 Bezout identity 给出 radius `2` 的 absorption-optimal witness，而精确值也正是

\[
\nu=2.
\]

### `2+7=9`

在 coordinates `(2,3,7)` 上，

\[
\alpha=(1,-6,1),
\qquad
\beta=(-7,0,2).
\]

minors 为

\[
(-42,9,-12),
\]

gcd 为 3。存在显式 identity

\[
(-42)+5\cdot9=3.
\]

由此构造出

\[
\boxed{x_B=(1,1,5)}
\]

并且

\[
\|x_B\|_\infty=5,
\qquad
\eta(x_B)=1.
\]

补充 07 已经得到

\[
\nu=5,
\]

所以这里的 Bezout 构造恰好 norm-optimal。

## 6. P025-N06 —— Constructive existence 可以离 minimum precision 极远

再次考虑

\[
1+242=243.
\]

在 coordinates `(2,3,11)` 上精确两行是

\[
\alpha=(121,-405,44),
\qquad
\beta=(121,0,44).
\]

非零 minors 为

\[
49005,
\qquad
-17820,
\]

并且

\[
\gcd(49005,17820)=4455.
\]

一个简单的 extended-Euclidean identity 是

\[
-49005+3\cdot17820=4455.
\]

当前规范实现据此得到

\[
\boxed{
x_B=(-405,11,1215)}
\]

它确实满足

\[
\eta(x_B)=5,
\]

但

\[
\boxed{\|x_B\|_\infty=1215.}
\]

独立的精确 bounded search 却在

\[
\boxed{\nu=27}
\]

就已经找到 floor-attaining witness。

例如可取

\[
(-27,-11,-27),
\]

差整体符号/约定不影响结论。

所以这个完全正确的 constructive floor witness 相对于真正最优半径的 absolute overhead 为

\[
\boxed{1215-27=1188.}
\]

### 架构后果

证明“存在一个 certificate，其 radius 不超过某显式数”并不等于知道访问该 certificate 的 minimal precision。

这正对应进取数论其它路线中已经反复出现的区分：

- 一个合法的 sufficient refinement/certificate；
- 真正 coarsest/minimal 的 task-relative refinement。

这里这个 gap 不是哲学措辞，而是在一个很小例子上就达到超过最优值四十倍的精确整数差距。

## 7. 为什么会出现这个 gap

gcd identity 发生在**minor space**。把一个 Bezout coefficient vector 通过 pair syzygies 拉回 witness lattice 时，可能产生很大的坐标放大或抵消。

所以最小化

\[
\left|\sum z_i m_i\right|=d
\]

和最小化

\[
\left\|\sum z_i t_i\right\|_\infty
\]

根本不是同一个 optimization problem。

前者是 arithmetic ideal-generation；后者是 normed lattice/coset optimization。

于是比补充 07 更精确地得到：

\[
\boxed{
\text{已知 image generator}
\not\Rightarrow
\text{已知 minimum-radius generator preimage}.
}
\]

## 8. `nu` 的下一数学形态

固定

\[
d=\operatorname{cont}(\alpha\wedge\beta).
\]

那么 absorption-optimal witness set 恰好是 affine integer slice

\[
\boxed{
\mathcal A_d
=
\{x\in\mathbb Z^s:
\alpha\cdot x=0,
\ \beta\cdot x=\pm d\}.
}
\]

因此

\[
\boxed{
\nu
=
\min_{x\in\mathcal A_d}
\|x\|_\infty.
}
\]

也就是说，补充 04–06 已经把 `d` 的 arithmetic uncertainty 完全消掉后，剩下的问题就是一个 codimension-two integer system 上的具体 closest-vector / affine-lattice minimum problem。

这个 reduction 使用的是标准 lattice optimization 语言。项目下一问题是：abc rows 的特殊结构能否让这个 affine minimum 比 generic CVP-style machinery 更显式。

## 9. 可执行资产

新增：

- `src/enterprise_math/abc_absorption_bezout.py`
  - exact multi-integer extended gcd coefficients；
  - pair syzygies；
  - nonzero Wronskian minors；
  - constructive floor-attaining witness；
  - triangle radius bound；
  - 与独立已知 optimal radius 的显式比较。
- `tests/test_abc_absorption_bezout.py`
  - gcd identity 精确重建；
  - `2+3=5` 与 `2+7=9` 的 sharp constructions；
  - `1+242=243` 上 `1215` 对 `27` 的 non-optimality boundary；
  - rank-one 校准。

## 10. 前人工作边界

以下属于成熟数学而非 P025 新发现：

- extended Euclidean / Bezout algorithms；
- 单行整数 syzygies；
- determinantal divisors；
- affine lattice closest-vector/minimum-norm problems；
- Geometry-of-Numbers short-vector 方法，包括 Pasten 在 arithmetic derivatives 上的应用 [SRC-PASTEN-2021-ARITHMETIC-DERIVATIVES]。

把 floor image generator、access radius `nu` 与 quantified existence-versus-minimum-precision gap 组合成进取数论证书精度结构，目前仍保持 `NOVELTY_UNVERIFIED`。

## 11. 下一前沿

不存在 hard block，继续：

1. 尽可能显式求解全部 rank-two witness lattices（`omega(abc)=3`）的 affine minimum；
2. 推导 `nu` 的 two-variable modular/Bezout normal form，避免 cubic brute-force enumeration；
3. 把精确 optimum 与 Pasten/Minkowski norm bounds 比较；
4. 分类 direct Bezout-minor certificate 何时已经 norm-optimal；
5. 搜索 constructive-over-optimal radius ratio 是否存在无界 family；
6. 只有完成这些以后，才判断 `nu` 或 `delta_abs` 对 abc-quality argument 是否有独立控制力。
