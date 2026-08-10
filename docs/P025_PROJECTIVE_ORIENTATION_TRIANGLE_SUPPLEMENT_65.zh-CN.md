# P025 补充 65 —— Projective Orientation 的导数质量三角律

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-paired-square-tail-stage61`  
依赖：P025 补充 47  
Hard block：`NONE`

## 1. Projective maximum 存在一个精确的方向选择器

对正整数定义 raw derivative mass

\[
\boxed{
U(n)=nS(n)=\sum_{p\mid n}v_p(n)\frac np.
}
\]

并约定 `U(1)=0`。

P025 的三个 projective terms 为

\[
\rho_c=\frac{c}{R(S(a)+S(b))},
\quad
\rho_b=\frac{b}{R(S(a)+S(c))},
\quad
\rho_a=\frac{a}{R(S(b)+S(c))}.
\]

`σ_proj` 的数值仍需要 weighted-radical data，但“哪个 orientation 取到最大值”这个 future query 需要的信息少得多。

## 2. P025-T131 —— 与 `c` 的比较恰好是 `U` 上的三角不等式

对正分母交叉相乘并使用 `c=a+b`：

\[
\rho_c\ge\rho_b
\iff
c(S(a)+S(c))\ge b(S(a)+S(b))
\]

\[
\iff
\boxed{U(a)+U(c)\ge U(b).}
\]

同理

\[
\boxed{
\rho_c\ge\rho_a
\iff
U(b)+U(c)\ge U(a).
}
\]

所以判断 `c` 是否支配 projective maximum，只需检验 raw derivative masses 的两条整数三角不等式。

## 3. P025-T132 —— 完整 orientation 分类

定义 side triangle defects

\[
D_a=U(a)-U(b)-U(c),
\qquad
D_b=U(b)-U(a)-U(c).
\]

二者不可能同时为正。

完整分类为：

\[
\boxed{
D_a>0
\Longrightarrow
\rho_a>\rho_c\ge\rho_b,
}
\]

\[
\boxed{
D_b>0
\Longrightarrow
\rho_b>\rho_c\ge\rho_a,
}
\]

否则

\[
\boxed{
\rho_c\ge\rho_a,\rho_b.
}
\]

`D_a=0` 或 `D_b=0` 分别给出对应 side 与 `c`-oriented term 的精确并列。

因此 side component 只有在 raw derivative mass 上打破三角不等式、成为 superdominant 时，才可能成为唯一 projective maximizer。

## 4. 小型精确样本

### `1+30=31`

\[
U(1)=0,\qquad U(30)=31,\qquad U(31)=1.
\]

因此

\[
U(30)>U(1)+U(31),
\]

`b` orientation 为唯一 projective maximum。这个例子也说明 side superdominance 本身并不要求 repeated prime factor：`30` 是 squarefree。

### `1+2=3`

\[
(U(a),U(b),U(c))=(0,1,1).
\]

所以 `D_b=0`，`b` 与 `c` 两个 projective terms 精确并列。

## 5. 经典高质量样本

对

\[
2+3^{10}\cdot109=23^5
\]

有

\[
U(2)=1,
\]

\[
U(3^{10}\cdot109)=21\,513\,519,
\]

以及

\[
U(23^5)=1\,399\,205.
\]

因此

\[
U(b)>U(a)+U(c),
\]

所以在进行任何 witness 搜索之前，就已经知道 `b`-oriented term 必须是 projective maximum。

这说明该经典 hard example 的 orientation 是 block arithmetic mass 现象，而不是 fine-lattice search artifact。

## 6. Hard unit 校准

对

\[
1+239^2=2\cdot13^4,
\]

side 并不在 derivative mass 上 superdominant，最终由 `c`-oriented term 取最大。这与 Stage 51 的解释一致：projective pressure 来自 `c` 的大 residual 除以相邻 prime-square 的极低 capacity。

## 7. 精度解释

完整 `σ_proj` 本身已经是 fine witness system 的 coarse quotient。P025-T131–T132 又为 future query

> 哪个 cyclic term 取到 projective maximum？

给出一个更粗的 exact state。

这个 selector 只需要两个整数 triangle defects 的符号：

\[
(D_a,D_b).
\]

它不需要 radicals、精确 support loads、witnesss 或 `σ_proj` 的实际数值。

因此即使在同一个 explicit observable 内部，不同 future query 仍会诱导出进一步的 exact quotient layers。

## 8. Prior-art / novelty discipline

证明只是初等交叉相乘；不主张任何一般 triangle-inequality/selector 数学的新颖性。

项目侧结果仅是：P025 projective orientation 与 arithmetic-derivative mass `U(n)` 的 superdominance 完全等价。历史 novelty 仍为 `NOVELTY_UNVERIFIED`。

## 9. 可执行资产

新增：

- `src/enterprise_math/abc_projective_orientation.py`；
- `tests/test_abc_projective_orientation.py`。

实现把 triangle-defect classifier 与独立计算的 exact cyclic projective values 做交叉核验。

## 10. 下一前沿

Hard block 不存在。继续：

1. 把 `c`-oriented failures 与 side-superdominant failures 的 tail 分开；
2. 检查高阈值 side superdominance 是否存在额外算术稀疏机制；
3. 把 derivative-mass selector 改写到经典 exceptional-set work 的 exponent-layer/anatomic 坐标；
4. 将该 selector 作为 P025 task-relative quotient poset 的又一个节点，而不是强塞进一条单一 precision axis。
