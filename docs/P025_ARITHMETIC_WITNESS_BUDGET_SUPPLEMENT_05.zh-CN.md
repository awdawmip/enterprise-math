# P025 补充 05 —— Arithmetic Wronskian Witness-Budget Chain

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner：`program/p025-arithmetic-witness-budget`  
父 payload：`program/p025-abc-support-collapse@6c854aeb`  
前人工作状态：Pasten 的 arithmetic derivatives/Wronskians 属于前人工作；有限 proof-budget 解释 `NOVELTY_UNVERIFIED`

## 1. 目标

补充 04 已经在经典多项式 Mason 证明中校准出有限 slack 分解。整数侧不能只凭类比就继承那个 degree 公式。

这里直接从 Pasten 的精确 prime-coordinate arithmetic derivative 与 arithmetic Wronskian 出发 [SRC-PASTEN-2021-ARITHMETIC-DERIVATIVES]。对 primitive triple

\[
a+b=c,
\qquad
\gcd(a,b)=1,
\]

以及一个 support-restricted、relation-adapted derivation `psi`，定义

\[
d^\psi(n)
=
\sum_{p\mid n}
\frac{n}{p}v_p(n)\psi(\xi_p).
\]

Pasten 的构造要求

\[
d^\psi(a)+d^\psi(b)=d^\psi(c)
\]

并定义

\[
W^\psi(x,y)=x d^\psi(y)-y d^\psi(x).
\]

本补充追问：从这个 witness 一路压缩到 `abc` 估计使用的 norm-only bound 时，究竟精确丢掉了哪些有限信息？

## 2. P025-T14 —— 局部 multiplicity residual 被 arithmetic derivative 吸收

对正整数 `n`，回忆

\[
m(n)=\frac{n}{\operatorname{rad}(n)}.
\]

则对任意 prime-coordinate derivation `psi`，都有

\[
\boxed{m(n)\mid d^\psi(n).}
\]

### 证明

`d^psi(n)` 的每一项为

\[
\frac{n}{p}v_p(n)\psi(\xi_p).
\]

对每个 `q|n`，`m(n)` 中 `q` 的指数是 `v_q(n)-1`。在指标 `p=q` 的项里，`n/p` 仍含有 `q^{v_q(n)-1}`；在其它项里则仍含完整的 `q^{v_q(n)}`。因此每一项都被 `m(n)` 整除，其和也被整除。

这正是“重复因子 residual 整除导数”的多项式事实在整数 prime-coordinate 公式中的精确对应，直接来自 Pasten 的 universal derivative 公式，不作为新的数论结果主张。

## 3. P025-T15 —— 完整 abc multiplicity residual 整除公共 arithmetic Wronskian

记

\[
M=m(a)m(b)m(c)
=
\frac{abc}{\operatorname{rad}(abc)}.
\]

primitive `abc` triple 的三个 prime support 两两分离，所以 `m(a),m(b),m(c)` 两两互素。

对 relation-adapted `psi`，加法性给出

\[
\begin{aligned}
W^\psi(a,b)
&=a d^\psi(b)-b d^\psi(a),\\
&=a d^\psi(c)-c d^\psi(a),\\
&=c d^\psi(b)-b d^\psi(c).
\end{aligned}
\]

除了 orientation sign 之外，它们是同一个 cyclic witness。

由 P025-T14：

- `m(a)` 整除第一种表示；
- `m(b)` 整除第一种表示；
- `m(c)` 整除第二或第三种表示。

利用两两互素性，得到

\[
\boxed{
M\mid W^\psi(a,b).
}
\]

任意 cyclic orientation 同样成立。若 witness 非退化，则

\[
\boxed{M\le |W^\psi|.}
\]

这就是 arithmetic derivative 路线里的整数 residual-to-common-witness absorber。

## 4. P025-T16 —— 精确四层整数 witness-budget chain

固定 triple 中的一个有序 pair `(x,y)`。把 arithmetic Wronskian 展开到 prime coordinates：

\[
W^\psi(x,y)
=
\sum_{p\mid y}
 x\frac{y}{p}v_p(y)\psi(\xi_p)
-
\sum_{p\mid x}
 y\frac{x}{p}v_p(x)\psi(\xi_p).
\]

定义 **absolute-coordinate budget**

\[
B_{\rm abs}^{x,y}(\psi)
=
\sum_{p\mid y}
\left|x\frac{y}{p}v_p(y)\psi(\xi_p)\right|
+
\sum_{p\mid x}
\left|y\frac{x}{p}v_p(x)\psi(\xi_p)\right|.
\]

它忘掉了精确 prime-coordinate contribution 之间的符号抵消。

再令

\[
\|\psi\|_\infty
=
\max_{p\mid abc}|\psi(\xi_p)|
\]

并定义 pair coefficient mass

\[
H_{x,y}
=
\sum_{p\mid y}x\frac{y}{p}v_p(y)
+
\sum_{p\mid x}y\frac{x}{p}v_p(x).
\]

**norm-only budget** 为

\[
B_{\|\psi\|}^{x,y}
=
\|\psi\|_\infty H_{x,y}.
\]

它进一步忘掉各 coordinate 的具体大小，只保留最大 derivation coordinate。

对任意 non-degenerate relation-adapted witness：

\[
\boxed{
M
\le
|W^\psi(x,y)|
\le
B_{\rm abs}^{x,y}(\psi)
\le
B_{\|\psi\|}^{x,y}.
}
\]

第一步是 P025-T15；第二步是三角不等式；第三步来自 `L_infinity` norm 的定义。

四个量全部是整数。

## 5. P025-T17 —— 精确望远镜 proof-loss shells

定义

\[
\begin{aligned}
g_1&=|W^\psi|-M,\\
g_2&=B_{\rm abs}^{x,y}(\psi)-|W^\psi|,\\
g_3&=B_{\|\psi\|}^{x,y}-B_{\rm abs}^{x,y}(\psi).
\end{aligned}
\]

则

\[
g_1,g_2,g_3\ge0
\]

并且精确有

\[
\boxed{
B_{\|\psi\|}^{x,y}-M=g_1+g_2+g_3.
}
\]

三项具有不同语义：

1. `g_1` —— **absorption gap**：witness 超出 multiplicity demand 的部分；
2. `g_2` —— **cancellation gap**：抹去 prime-coordinate 符号后引入的容量；
3. `g_3` —— **norm-projection gap**：把真实 coordinate magnitude 压成单一最大范数后引入的容量。

这是一条纯有限整数的 proof-relaxation precision-shell 分解，不是额外的 `abc` 不等式。

## 6. 精确 pre-log abc envelope

因为 `M=abc/rad(abc)`，P025-T16 立即给出纯整数交叉乘形式

\[
\boxed{
abc
\le
\operatorname{rad}(abc)\,
B_{\|\psi\|}^{x,y}.
}
\]

若 `z` 是 pair `(x,y)` 的第三个补元素，约去正因子 `xy` 得到等价的经典形式

\[
\boxed{
z
\le
\operatorname{rad}(abc)\,\|\psi\|_\infty
\left(
\sum_{p\mid x}\frac{v_p(x)}{p}
+
\sum_{p\mid y}\frac{v_p(y)}{p}
\right).
}
\]

再对 reciprocal-prime/valuation sum 使用普通估计，就进入 Pasten `abc` estimate 中 derivation norm 出现的那种表达。P025 不把这个不等式或后续解析估计作为新结果；这里的目的恰恰是停在对数平滑之前，暴露精确整数 proof-loss layer。

## 7. P025-T18 —— witness precision 正是可优化的 norm-budget 因子

固定目标 `c`，对应补 Wronskian pair `(a,b)`。coefficient mass

\[
H_{a,b}
\]

只依赖 arithmetic triple，与选择哪个 relation-adapted witness 无关。

回忆补充 01 定义的精确 witness precision：

\[
\mu(a,b,c)
=
\min_{\psi\in\mathscr T(a,b)\setminus\mathscr T^\circ(a,b)}
\|\psi\|_\infty.
\]

因此

\[
\boxed{
\min_{\psi\in\mathscr T(a,b)\setminus\mathscr T^\circ(a,b)}
B_{\|\psi\|}^{a,b}
=
H_{a,b}\,\mu(a,b,c).
}
\]

从而

\[
\boxed{
M\le H_{a,b}\,\mu(a,b,c).
}
\]

等价地，

\[
\boxed{
abc
\le
\operatorname{rad}(abc)\,H_{a,b}\,\mu(a,b,c).
}
\]

### 架构含义

这给此前的 task-relative witness precision 一个真正的 proof-resource 含义：

> `mu` 正是 target-`c` 的 norm-relaxed capacity 中唯一需要在 witness family 上优化的那个因子。

relation-conditioned witness search 与最终 norm-based `abc` proof budget 因而不只是类比关系；二者共享同一个 minimum integer precision parameter。

这个数学联系已经隐含在 Pasten 的 small-derivative program 中；P025 的作用是把它转写成 finite-collapse 语义并明确路由回 precision architecture。

## 8. 边界样本 —— 相同 radical coarse state，不同 proof-relaxation loss

此前 P025 的反例现在可以在 proof-budget 层重新解释。

### `1+2=3`

取最小 adapted witness

\[
\psi(\xi_2)=1,
\qquad
\psi(\xi_3)=1.
\]

对 target-`c` pair `(1,2)`：

\[
M=1,
\quad
|W|=1,
\quad
B_{\rm abs}=1,
\quad
B_{\|\psi\|}=1.
\]

所有 gap 都为零，且 `mu=1`。

### `1+8=9`

完整 radical triple 仍然是 `(1,2,3)`，但 relation 强制 primitive minimum witness

\[
\psi(\xi_2)=1,
\qquad
\psi(\xi_3)=2,
\]

因此 `mu=2`。对 target-`c` pair `(1,8)`：

\[
M=12,
\quad
|W|=12,
\quad
B_{\rm abs}=12,
\quad
B_{\|\psi\|}=24.
\]

于是

\[
(g_1,g_2,g_3)=(0,0,12).
\]

重复素因子 demand 被恰好吸收，也没有 sign-cancellation loss。全部松弛只发生在把完整 relation witness 坍缩为最大 norm 的步骤。

这让之前的 witness-precision separation 变成真正可操作的证明现象：同一 radical coarse state，因为 active additive relation 在 witness 的其它 coordinate 上强迫出更大值，可以需要严格更大的 norm-only proof budget。

## 9. Orientation 是 typed proof state，而不是 intrinsic slack

对 relation-adapted `psi`，三个 cyclic Wronskian 除符号外相同，因此绝对 witness level 相同；但其 envelope 可以不同。

对同一个 `1+8=9` minimum witness：

\[
\begin{array}{c|ccc}
(x,y)&|W|&B_{\rm abs}&B_{\|\psi\|}\\
\hline
(1,8)&12&12&24\\
(8,9)&12&204&312\\
(9,1)&12&12&12
\end{array}
\]

因此 `g_2,g_3` 不是抽象 witness 自身的 intrinsic property，而是 **typed proof orientation** `(target, complementary pair)` 的属性。

在固定 norm 下，norm-budget 的排序只由整数 coefficient mass `H_{x,y}` 决定，与具体 witness vector 无关。于是两类选择被拆开：

1. witness search 控制 `||psi||`；
2. proof orientation 控制 `H_{x,y}`。

对经典 target-`c` 问题，补 pair `(a,b)` 已经固定，因此 `mu` 仍是正确的 witness optimization parameter；在其它 proof-query language 里，orientation 本身则是另一层有限 selector state。

## 10. 一个非平凡 cancellation 样本

对

\[
2+3=5
\]

选择 adapted witness

\[
(\psi(\xi_2),\psi(\xi_3),\psi(\xi_5))=(1,1,2).
\]

对 pair `(2,3)`：

\[
M=1,
\quad
|W|=1,
\quad
B_{\rm abs}=5,
\quad
B_{\|\psi\|}=10,
\]

所以

\[
(g_1,g_2,g_3)=(0,4,5).
\]

这里 residual absorption 恰好饱和，但 sign cancellation 与 norm projection 同时丢失信息。

在同一个 triple 上换另一个 adapted witness，三个 gap 的分布还会改变。因此最终 bound 通常不是 proof-provenance query 的完备状态。

## 11. 与 P018/P023 的关系及 ownership 边界

一般算术事实

\[
D\le W\le U
\Longrightarrow
U-D=(W-D)+(U-W)
\]

只是初等 accounting，不是新的 mother theorem。

同样，P023 已经拥有一般 task-relative observation/minimal-repair 结构，而当前 P018 也已经把 defect/margin coordinate 视为位于更弱 pair/kernel structure 之上的 optional state。

因此正确路由是：

- **P025 拥有** arithmetic-derivative specialization、精确样本以及 `abc` pressure-test 语义；
- **P018/P023 可以消费** 四层 chain 作为 proof-state pressure test；
- **不要**因为这条算术链有用，就再造一个重复的 generic A2 theorem。

真正值得跨路线传播的是：proof relaxation 本身也可以是 typed finite precision change，而各个 gap 只有在未来 query 会消费 proof provenance 时才应该保留。

## 12. 前人工作边界

Pasten 定义了 prime-coordinate arithmetic derivative、relation-adapted module、`L_infinity` norm、arithmetic Wronskian、non-degeneracy condition、controlled-size derivatives，以及带 derivation norm 的 `abc` estimate [SRC-PASTEN-2021-ARITHMETIC-DERIVATIVES]。

P025-T14--T18 是对这些部件加上初等整除、三角与 norm 不等式的直接精确展开与 finite-state 重组。底层不等式不主张优先权。

项目侧研究候选只有

\[
\text{relation witness precision}
\to
\text{exact proof-budget shells}
\to
\text{task-relative erasure/provenance}.
\]

历史创新性继续标为 `NOVELTY_UNVERIFIED`。

## 13. 可执行证据

本 generation 新增：

- `src/enterprise_math/arithmetic_witness_budget.py`；
- `tests/test_arithmetic_witness_budget.py`。

可执行层检查：

- `m(n)|d^psi(n)` 的精确整数样本；
- 每个 cyclic adapted Wronskian 的 residual product divisibility；
- 四层 chain 与三 gap 望远镜律；
- 两个 same-radical witness-precision 样本；
- cancellation 与 norm-projection gap 同时为正的例子；
- cyclic witness 相同但 orientation envelope 不同；
- 非 adapted / degenerate witness 的拒绝。

独立 bounded scan 对 `c<40` 的 primitive triples、support dimension 至多四、derivation coordinate 位于 `[-2,2]` 的范围，检查了 3,312 个 adapted non-degenerate witness state，即 9,936 个 cyclic pair-budget profile，没有发现 chain 或 residual divisibility 失败。这里只是回归证据，不替代证明。

## 14. 下一前沿

现在的后续问题更精确：

1. 判断最小化 `mu` 是否已经解释 Pasten norm estimate 中全部 witness-dependent loss，而剩余因子完全由 triple 决定；
2. 在高 quality triples 上比较 target-`c` coefficient mass `H_{a,b}` 与 radical/residual coordinate，寻找是否还能精确坍缩；
3. 检查 minimum witness 上三 gap vector `(g1,g2,g3)` 是否存在单调性或稀疏结构；
4. 只有真正非平凡 invariant 在压力测试后仍存活，才向 P018/P023 抽象；
5. 继续把 Pasten 的解析 `abc` estimate 与 small-derivative equivalence 当作前人工作，而不是项目证明。
