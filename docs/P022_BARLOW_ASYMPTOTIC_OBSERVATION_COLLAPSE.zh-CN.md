# P022 —— Barlow 渐近观测坍缩

状态：`ACTIVE RESEARCH NOTE / EXACT CONSEQUENCE OF PROVED P022 FORMULAS / NOVELTY_UNVERIFIED`  
归属：`program/p022-geometry-v2`  
依赖：periodic geodesic-growth theorem BG03 与 coordination theorem BC06  
目的：证明当 future language 从 finite-radius exact values 改成 asymptotic leading invariants 时，observables 之间的信息偏序本身会发生变化

## 1. finite-radius observables 彼此不可比较

Barlow observation-lattice note 已经用显式有限反例证明

\[
S_n\not\Rightarrow T_n,
\qquad
T_n\not\Rightarrow S_n,
\]

其中

- `S_n` 是 shell vertex cardinality；
- `T_n` 是进入整个 shell 的 shortest paths 总数。

所以固定 finite radius 时，这两个 observables 是真正 incomparable 的。

本文证明：当 future language 换成 asymptotic leading-order language 后，这个关系会改变。

## 2. periodic stacking 只有一个 absolute drift density

设 stacking period length 为 `L`，signed period drift 为 `D`。

正负两个方向都具有同一个 asymptotic absolute drift density：

\[
\boxed{
\mu=\frac{|D|}{L}\in[0,1].}
\]

literal period order 与 finite phase 仍会影响 exact finite shells，但会从下面两个 leading asymptotic observables 中消失。

## 3. coordination leading coefficient

BC06 给出

\[
\boxed{
C_S
:=\lim_{n\to\infty}\frac{S_n}{n^2}
=\frac{21}{2}-\frac{\mu^2}{2}.}
\]

映射

\[
\mu\mapsto C_S
\]

在 `[0,1]` 上是一一的，反函数是

\[
\boxed{
\mu=\sqrt{21-2C_S}.}
\]

periodic integer-first exact representation 为

\[
C_S=\frac{21L^2-D^2}{2L^2}.
\]

## 4. geodesic-multiplicity growth exponent

BG03 给出

\[
\boxed{
\Lambda
:=\lim_{n\to\infty}T_n^{1/n}
=2+2^{(1+\mu)/2}.}
\]

这个映射在 `[0,1]` 上严格递增，因此同样一一。

real inverse 为

\[
\boxed{
\mu=2\log_2(\Lambda-2)-1.}
\]

对于 integer-first periodic state，完全不需要存 logarithm；`Lambda` 是下面整数方程中大于 `2` 的正实根：

\[
\boxed{
(\Lambda-2)^{2L}=2^{L+|D|}.}
\]

## 5. P022-AO01 —— 两个 leading asymptotic observables information-equivalent

因为 `C_S` 与 `Lambda` 都是同一个 `mu` 的 bijective functions，

\[
\boxed{
C_S
\longleftrightarrow
\mu
\longleftrightarrow
\Lambda.}
\]

因此，在 periodic Barlow stackings 这一 domain 内，并且 future language 只要求 **leading asymptotic information** 时，

\[
\boxed{
C_S\text{ 与 }\Lambda\text{ information-equivalent}.}
\]

这不与 finite-radius incomparability 冲突。asymptotic projection 主动擦掉了两边的 finite phase information，使原来不同的 shadows 同时 collapse 到一个 latent coordinate。

## 6. 显式 tradeoff curve

用

\[
\mu=\sqrt{21-2C_S}
\]

消去 `mu`，得到

\[
\boxed{
\Lambda
=2+2^{\left(1+\sqrt{21-2C_S}\right)/2}.}
\]

允许范围：

\[
10\le C_S\le\frac{21}{2},
\]

以及

\[
2+\sqrt2\le\Lambda\le4.
\]

随着 `mu` 增大：

- `C_S` 从 `21/2` 严格下降到 `10`；
- `Lambda` 从 `2+sqrt(2)` 严格上升到 `4`。

所以 periodic stacking drift 给出一条 exact asymptotic tradeoff：

\[
\boxed{
\text{每 }n^2\text{ 更少的 coordination-shell vertices}
\quad\Longleftrightarrow\quad
\text{更大的 shortest-path redundancy exponential rate}.}
\]

这只是 combinatorial statement，不表示物理上的“效率”“稳定性”或优劣。

## 7. 两个极端

### zero drift

\[
\mu=0.
\]

所以

\[
C_S=21/2,
\qquad
\Lambda=2+\sqrt2.
\]

HCP 是其中一个 periodic representative，但所有 zero-drift periodic Barlow words 都共享同一 leading pair。

### constant drift

\[
\mu=1.
\]

所以

\[
C_S=10,
\qquad
\Lambda=4.
\]

FCC 是 canonical constant-drift representative。

## 8. P022-AO02 —— aperiodic asymmetric drift 会再次打破等价

对拥有 one-sided absolute drift limits

\[
\mu_+,
\qquad
\mu_-
\]

的任意 two-sided stacking，coordination 读取

\[
\boxed{
C_S
=\frac{21}{2}
-rac{\mu_+^2+\mu_-^2}{4},}
\]

而 geodesic multiplicity 读取

\[
\boxed{
\Lambda
=2+2^{(1+\max(\mu_+,\mu_-))/2}.}
\]

在完整 two-dimensional drift domain 上，任意一个 observable 都不能单独决定另一个。

但是 pair `(C_S,Lambda)` 可以恢复 unordered drift magnitudes：

1. `C_S` 给出
   \[
   R_2=\mu_+^2+\mu_-^2=42-4C_S;
   \]
2. `Lambda` 给出
   \[
   M=\max(\mu_+,\mu_-);
   \]
3. 另一个 magnitude 为
   \[
   \sqrt{R_2-M^2}.
   \]

所以

\[
\boxed{
(C_S,\Lambda)
\longleftrightarrow
\{\mu_+,\mu_-\}
}
\]

只差交换两侧。

若要恢复 orientation label，还必须加入 one-sided observable。

## 9. horizon-induced observation-poset change

同样两类 named observable families，在不同 declared domain / horizon 上出现三种不同 information relationship。

### finite radius

\[
S_n\quad\text{与}\quad T_n
\]

不可比较。

### periodic asymptotic leading language

hidden drift vector 被 domain restriction 压到 diagonal

\[
(\mu,\mu),
\]

所以两个 observables 都通过同一个 scalar `mu` 变成等价。

### aperiodic two-sided asymptotic language

hidden state 又恢复为两个 coordinates

\[
(\mu_+,\mu_-),
\]

两个 observables 分别读取这个 vector 的 `L^2`-square statistic 与 `L^infinity` statistic。单独都不充分，但联合足够。

因此

\[
\boxed{
\text{当 future horizon/domain 改变时，observation-factorization order 本身也会改变。}}
\]

这是 P022 对更一般 precision-mathematics principle 的 concrete realization：quotient sufficiency 不仅取决于**观察什么**，还取决于**要求 observation 覆盖哪一个 future domain**。

## 10. 上游归属边界

关于 observation factorization 与 horizon-restricted equivalence 的抽象母结论，如果以后提升，应归 A2/P023/P024。

P022 只保留 exact Barlow specialization：

- finite counterexamples；
- coordination / geodesic formulas；
- drift reconstruction；
- periodic diagonal-collapse phenomenon。

这里不新建 generic quotient ontology。
