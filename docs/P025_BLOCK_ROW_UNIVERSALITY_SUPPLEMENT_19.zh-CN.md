# P025 补充 19 —— Primitive Positive Arithmetic Block Row 的普适实现

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-access-tail-stage18`  
依赖：P025 补充 13、16–18  
Hard block：`NONE`

## 1. 一个看似可能的逃生口

补充 16–18 对任意 primitive 正系数行

\[
b=(b_1,\ldots,b_d)
\]

研究 signed access。

一个自然希望是：真实 arithmetic-derivative block 也许只产生其中很小的一类特殊 coefficient rows，于是一般 numerical-semigroup / capacity-frontier 的复杂性与 P025 无关。

这个希望是错的。

整数 arithmetic derivative 产生的规范化 coefficient row，**恰好就是全部 primitive positive integer rows**。

## 2. 真实 arithmetic block row

令

\[
n=\prod_{i=1}^d p_i^{e_i}
\]

其中 `p_i` 为互异素数，`e_i>0`。

记

\[
R=\operatorname{rad}(n)=\prod_i p_i.
\]

补充 13 已证明 normalized derivative

\[
\frac{d_x(n)}{m(n)}
\]

在 prime `p_i` 上的 coefficient 为

\[
\boxed{
c_i=e_i\frac{R}{p_i}.}
\]

令

\[
h(n)=\gcd_i c_i.
\]

对应的 primitive positive block row 为

\[
\boxed{b_i(n)=\frac{c_i}{h(n)}.}
\]

按构造必有

\[
\gcd_i b_i(n)=1.
\]

所以每条真实 block row 都属于 primitive positive integer row 类。

## 3. P025-T56 —— 任意 primitive positive row 都可由整数 block 实现

反过来，任取

\[
\boxed{
b=(b_1,\ldots,b_d)\in\mathbb N_{>0}^d,
\qquad
\gcd(b_1,\ldots,b_d)=1.}
\]

再任取互异素数

\[
p_1<\cdots<p_d
\]

并定义 exponent

\[
\boxed{e_i=p_i b_i.}
\]

构造

\[
\boxed{
n_b=\prod_i p_i^{p_i b_i}.}
\]

那么 prime `p_i` 上的 normalized derivative coefficient 为

\[
e_i\frac{R}{p_i}
=
(p_i b_i)\frac{R}{p_i}
=
R b_i.
\]

因此整条 coefficient row 的 content 为

\[
\gcd_i(Rb_i)
=R\gcd_i b_i
=R.
\]

除以 content 后精确得到

\[
\boxed{
\left(
\frac{Rb_1}{R},\ldots,
\frac{Rb_d}{R}
\right)
=b.
}
\]

所以每个 primitive positive integer row 都是某个显式正整数 block 的 primitive arithmetic-derivative row。∎

## 4. 精确 row-class 分类

合并两个方向：

\[
\boxed{
\{\text{primitive arithmetic block rows}\}
=
\{b\in\mathbb N_{>0}^d:\gcd(b_i)=1\}.
}
\]

对每个有限维 `d>=1` 都成立。

这个构造只用于 existence；不声称所得 `n_b` 是实现同一 row 的最小整数。

## 5. 当前 pressure-test rows 的显式实现

### `(5,2)`

取 prime labels `(2,3)`。则

\[
e=(10,6),
\qquad
n=2^{10}3^6.
\]

normalized derivative coefficients 为

\[
(30,12)=6(5,2),
\]

所以 primitive row 恰为 `(5,2)`。

### `(15,10,6)`

取 labels `(2,3,5)`，则

\[
e=(30,30,30),
\]

primitive row 恰为 `(15,10,6)`。

### Stage-17 equal-Apéry counterexample rows

下列每一条

\[
(2,4,5,11),
\quad
(2,5,7,8),
\quad
(2,5,6,9)
\]

都是真实 arithmetic block row。例如统一使用 prime labels `(2,3,5,7)`，令 exponent 为 `p_i b_i` 即可。

因此 Stage 17 中 semigroup membership、labelled factorization geometry、access precision 之间的区别，不是因为研究跑出了 arithmetic-derivative domain。

## 6. P025-N08 —— 不存在隐藏的 row-class 简化

任何对某个 primitive positive row 失败的 universal theorem，都可以通过上面的构造运输到一个真实 arithmetic block。

所以 P025 的普适论证不能仅凭“这些 coefficients 来自 prime valuations”就假设 primitive row 还自动满足某种额外 combinatorial property。

尤其不能用“真实 arithmetic rows 更特殊”来消除：

- nonminimal/redundant coefficient coordinates；
- 相同 generated semigroup 但不同 labelled factorization geometry；
- 非平凡 Apéry preperiod；
- 多层 capacity frontier；
- 任意有限维 positive-row access problem。

若还想进一步简化，必须加入关于**特定 abc relation**、exponent pattern、support size 或声明 future language 的额外假设。

## 7. 架构后果

这条结果收紧了补充 16–18 的研究边界。

Numerical-semigroup 和 `L_infinity` factorization mathematics 仍属于 prior art，但 generic positive-row access layer 不再只是外部 calibration universe；它恰好完整嵌在 arithmetic-derivative blocks 的 coefficient-row universe 内。

因此 pressure-test chain 变成

\[
\boxed{
\text{integer prime/exponent block}
\twoheadrightarrow
\text{arbitrary primitive positive row}
\to
\text{signed access / Apéry / capacity frontier}.
}
\]

第一箭头在 primitive coefficient-row 层是满射。

## 8. Prior-art 纪律

构造 `e_i=p_i b_i` 与 gcd 计算只是初等算术。P025 不对这个裸 realization trick 作历史优先性主张。

项目侧价值是一个 negative boundary：generic primitive-row access complexity 确实属于 arithmetic-derivative search space，不能用“过度一般化”把它排除出去。

该架构用途的历史创新状态仍为 `NOVELTY_UNVERIFIED`。

## 9. 可执行资产

新增：

- `src/enterprise_math/abc_block_row_universality.py`
  - primitive block-row 提取；
  - 显式 realization `n_b=product p_i^(p_i b_i)`；
  - exact row reconstruction checks。
- `tests/test_abc_block_row_universality.py`
  - two-variable `(5,2)` realization；
  - Stage-17 four-coordinate rows；
  - three-coordinate `(15,10,6)` realization；
  - one-dimensional boundary；
  - 拒绝 nonprimitive 或非法 prime-labelled 输入。

## 10. 下一前沿

没有 hard block。继续：

1. 用 universality 把 generic lower bounds/counterexamples 直接运输回 arithmetic blocks；
2. 研究实现给定 row 所需的最小 exponent size，但不把该优化与 access precision 混淆；
3. 在 universality barrier 之后，寻找真正来自特定 abc relation 的额外约束；
4. 研究 multi-block simultaneous certificate targets：单个 block row 各自 universal，但 relation coupling 可能引入新结构；
5. 始终把 generic factorization theory 作为 prior art，只研究项目侧 future-language compression interface。
