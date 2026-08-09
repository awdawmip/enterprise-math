# P025 补充 05 —— Absorption Floor 的闭式素因子支持公式

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner：`program/p025-abc-support-collapse`  
依赖：P025 补充 04、Pasten arithmetic derivatives、初等素数赋值  
Hard block：`NONE`

## 1. 目标

补充 04 已经识别出精确的最小 Wronskian 吸收冗余

\[
\eta_{\min}
=
\frac{\operatorname{cont}(\widehat\alpha\wedge\beta_{\rm raw})}
{M},
\qquad
M=\frac{abc}{\operatorname{rad}(abc)},
\]

其中 `alpha_hat` 是 primitive additive-relation row，`beta_raw` 是带规范尺度的 arithmetic-Wronskian row。

该公式已经精确，但仍使用格/exterior 语言。本补充把这一层完全消掉，直接用 `a,b,c` 的 prime-support partition 与 valuation exponents 表示同一个 invariant。

整个推导不使用 abc 猜想。

## 2. Raw additive row 及其 content

令

\[
a+b=c,\qquad \gcd(a,b)=1,
\]

并记

\[
e_p=v_p(abc).
\]

由于 `a,b,c` 两两互素，每个素数恰好属于三个 support block 之一：

\[
S_a,\quad S_b,\quad S_c.
\]

Pasten 条件

\[
d(a)+d(b)=d(c)
\]

对应的 raw additive row 坐标为

\[
\alpha^{(0)}_p=
\begin{cases}
 a\,v_p(a)/p,&p\in S_a,\\
 b\,v_p(b)/p,&p\in S_b,\\
 -c\,v_p(c)/p,&p\in S_c.
\end{cases}
\]

令

\[
\boxed{
g=\gcd_{p\mid abc}|\alpha^{(0)}_p|.}
\]

则

\[
\widehat\alpha=\alpha^{(0)}/g.
\]

再记

\[
R=\operatorname{rad}(abc).
\]

## 3. P025-T15 —— 闭式 cross-support 公式

对来自 `S_a,S_b,S_c` 中**不同 support block** 的素数 `p,q`，定义

\[
\boxed{
K_{p,q}
=
\frac{R\,e_p e_q}{g\,p q}.
}
\]

则每个 `K_(p,q)` 都是正整数，并且

\[
\boxed{
\eta_{\min}(a,b,c)
=
\gcd_{
\substack{p,q\mid abc\\
\text{来自不同 support blocks}}}
K_{p,q}.
}
\]

所以最小可能 Wronskian absorption redundancy 只依赖有限 factorization data；不再需要枚举 witness，也不需要 lattice reduction。

### 证明

带规范尺度的 Wronskian row 为

\[
(\beta_{\rm raw})_p=
\begin{cases}
-b\,\alpha^{(0)}_p,&p\in S_a,\\
 a\,\alpha^{(0)}_p,&p\in S_b,\\
0,&p\in S_c.
\end{cases}
\]

考察二行矩阵

\[
[\widehat\alpha;\beta_{\rm raw}]
\]

的任意 `2x2` minor。

若 `p,q` 属于同一 support block，则相应两列在这两行上的限制成比例，所以 minor 为零。

若它们属于不同 support blocks，直接代入可得，忽略符号后

\[
\left|
\widehat\alpha_p\beta_q
-
\widehat\alpha_q\beta_p
\right|
=
\frac{abc\,e_p e_q}{g\,p q}.
\]

补充 04 已证明，全部这些 minors 的 content 正好是 Wronskian functional 在 additive witness lattice 上像的正生成元。又因为

\[
M=abc/R,
\]

把每个非零 minor 除以 `M`，恰好得到

\[
K_{p,q}
=
\frac{R e_p e_q}{g p q}.
\]

P025-T11 保证 `M` 整除所有 Wronskian values，因而也整除 image generator/minor content，所以这些 normalized terms 都是整数。对它们取 gcd 即得到 `eta_min`。∎

## 4. Perfect absorption 的精确有限判据

P025-T15 立即给出

\[
\boxed{
\eta_{\min}=1
\iff
\gcd_{\text{cross-block }p,q}
\frac{R e_p e_q}{g p q}=1.
}
\]

因此存在满足

\[
|W|=M
\]

的 witness，当且仅当上面的有限算术 gcd 条件成立。

这已经是完整判据，但还不是对所有 abc triples 的一句话结构分类；它的重要意义在于，判定中已经完全没有 witness variables。

## 5. P025-T16 —— Squarefree primitive triples 具有 perfect absorption

假设三个 support blocks 中至少两个非空，并且 `a,b,c` 全部 squarefree（允许 `1` 作为空 squarefree support）。则

\[
\boxed{
\eta_{\min}(a,b,c)=1.
}
\]

### 证明

全部 valuation exponents 都等于 1。

首先 `g=1`。对任意非单位 squarefree block，对应整数记为 `n`，该 block 上的 raw-row coefficients（忽略符号）为

\[
\{n/p:p\mid n\}.
\]

这些整数的 gcd 为 1：对每个 `r|n`，系数 `n/r` 都不被 `r` 整除。因此整个 additive row 的 gcd 也是 1。

P025-T15 于是化为

\[
K_{p,q}=R/(pq).
\]

任意 `r|R` 属于某个非空 block。由于至少还有另一个 block 非空，可以选择一个包含 `r` 的 cross pair；对应的 `R/(rq)` 不再被 `r` 整除。因此没有任何 `R` 的素因子可以整除全部 cross terms。又因为所有 cross terms 都整除 `R`，所以它们的 gcd 必为 1。∎

### 解释

Squarefree support 没有重复 prime multiplicity；但该结论比简单的 `M=1` 更强：它说明 relation-adapted Wronskian lattice 实际能够达到最小非零算术尺度。

## 6. P025-T17 —— One plus squarefree 等于 prime power

设

\[
1+b=p^m,
\]

其中 `p` 为素数、`m>=1`，且 `b>1` squarefree。则

\[
\boxed{
\eta_{\min}(1,b,p^m)=m.
}
\]

### 证明

squarefree 的 `b` block 已经强制 additive-row content `g=1`。

令

\[
B=\operatorname{rad}(b)=b.
\]

则

\[
R=pB.
\]

每个非零 cross term 都由 `p` 与某个 `q|b` 配对。P025-T15 给出

\[
K_{q,p}
=
\frac{pB\cdot1\cdot m}{q p}
=m\frac{B}{q}.
\]

对全部 `q|B`，整数 `B/q` 的 gcd 为 1，所以全部 `K_(q,p)` 的 gcd 恰好是 `m`。∎

### 例子

\[
1+3=4\quad\Rightarrow\quad\eta_{\min}=2,
\]

\[
1+7=8\quad\Rightarrow\quad\eta_{\min}=3,
\]

\[
1+15=16\quad\Rightarrow\quad\eta_{\min}=4,
\]

\[
1+31=32\quad\Rightarrow\quad\eta_{\min}=5.
\]

所以，即使另一侧非单位项完全 squarefree，单个 support block 上的重复 multiplicity 仍可能形成**不可消除的 Wronskian absorption overhead**。

本命题并不声称存在无穷多个 squarefree `p^m-1`；它只是对每个满足这些条件的实际三元组给出精确公式。

## 7. P025-T18 —— 两个 prime-power support blocks

设一个实际 primitive relation 形如

\[
1+p^m=q^n,
\]

其中 `p,q` 为不同素数，`m,n` 为正整数。

此时只有两个 prime coordinates。raw additive row 为

\[
\left(
 m p^{m-1},
 -n q^{n-1}
\right),
\]

令

\[
g=\gcd\left(m p^{m-1},n q^{n-1}\right).
\]

P025-T15 给出

\[
\boxed{
\eta_{\min}
=
\frac{mn}{g}.
}
\]

因此

\[
\boxed{
\eta_{\min}=1
\iff
n\mid p^{m-1}
\quad\text{且}\quad
m\mid q^{n-1}.
}
\]

正向是因为 `eta_min=1` 等价于 `g=mn`；反向则因为两个整除条件使两个 raw coefficients 都被 `mn` 整除，而精确整数公式又强制 `g|mn`。

### Catalan/Mihăilescu 工作样例

对

\[
1+2^3=3^2,
\]

有

\[
g=\gcd(12,6)=6=mn,
\]

所以

\[
\eta_{\min}=1.
\]

这里只把这个经典数值等式当作结构样本，不对 Catalan 定理本身提出任何新结论。

## 8. 这对 radical collapse 说明了什么

补充 04 把 witness search radius 与 absorption redundancy 分开。P025-T15 进一步说明，第二个轴并不是神秘的隐藏 lattice information；它已经由

\[
\boxed{
\text{support partition}
+
\text{valuation exponents}
+
\text{additive-row content}
}
\]

完整编码。

因此现在出现三个不同 compression levels：

1. **只有 radical support** —— 只记哪些素数出现；
2. **support + valuation structure** —— 已足以计算精确 absorption floor `eta_min`；
3. **完整 normed witness generator** —— 才需要用于 search-radius / Pareto tradeoff structure。

这把“multiplicity matters”进一步细化为：面对不同 future certificate queries，并不是所有 multiplicity 信息都需要以同样形式保留。

## 9. High-quality examples 并没有消掉这个新轴

此前使用的几个 high-quality examples 恰好都有 perfect absorption：

\[
1+8=9,
\]

\[
1+4374=4375,
\]

\[
2+3^{10}\cdot109=23^5.
\]

对它们，P025-T15 都得到

\[
\eta_{\min}=1.
\]

这只是一项有限结构观察。它**不能**推出 high abc quality 会导致 perfect absorption；在没有专门搜索反例和渐近证据前，P025 不采用这一猜想。

## 10. 可执行资产

新增：

- `src/enterprise_math/abc_absorption_formula.py`
  - raw additive relation row 与 content；
  - 精确 cross-block normalized minor list；
  - `eta_min` 的 closed support formula；
  - squarefree perfect-absorption verifier；
  - `1 + squarefree = prime power` 特化；
  - two-prime-power-block 公式与 perfect-absorption criterion。
- `tests/test_abc_absorption_formula.py`
  - 精确工作样例；
  - 对全部 `c<100` primitive triples，support formula 与 exterior/determinantal formula 穷举一致；
  - squarefree family samples；
  - prime-power family samples；
  - 此前使用的 high-quality triples。

`c<100` 穷举用于验证实现；一般公式由上面的证明建立，而不是由穷举建立。

## 11. 前人工作边界

Pasten 明确提供 arithmetic derivative、selected additive relation 和 arithmetic Wronskian 公式 [SRC-PASTEN-2021-ARITHMETIC-DERIVATIVES]。Determinantal divisors 与 primitive integer kernels 属于标准代数。

本阶段的定向来源检索没有建立 normalized invariant `eta_min`、上述 support formula 或这些 family classifications 的历史优先权。因此全部仍标记为

`NOVELTY_UNVERIFIED`。

定向检索未发现不等于原创证据。

## 12. 下一前沿

不存在 hard block，继续：

1. 推导 `eta_min` 的 `l`-adic valuation formula，把 gcd criterion 化为逐素数 local obstruction data；
2. 分类哪些 multiplicity patterns 强制 `eta_min>1`，哪些允许 `eta_min=1`；
3. 专门搜索 high-quality 且 `eta_min>1` 的 triples，因为只要一个反例就能否掉任何 naive 的 quality/perfect-absorption implication；
4. 比较 `eta_min` 与完整 Pareto frontier，判断何时真正 bottleneck 是 absorption obstruction 而不是 search radius；
5. 用新的 local obstruction coordinates 重读 Pasten 的 Geometry-of-Numbers argument，再决定任何 novelty claim。
