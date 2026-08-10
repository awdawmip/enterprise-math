# P025 补充 88 —— Cover-Resonance 精度与饱和边界

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-cyclotomic-stage76`  
依赖：P025 补充 87  
硬阻断：`NONE`

## 1. Resonance 是有限 ratio state

对奇 cover prime

\[
r\ge3
\]

与 lower exponent `m>=2`，Stage 87 已证明 support resonance 等价于

\[
x^m=1
\]

的 difference equation，或

\[
x^m=-1
\]

的 sum equation，其中

\[
x\in\mathbf F_r^\times.
\]

下一问题完全有限：

> 到底有多少 prime-ratio classes 能让 exponent normalization 消失？

## 2. P025-T190 —— difference resonance class count

令

\[
N:=r-1,
\qquad
g:=\gcd(m,N).
\]

乘法群

\[
\mathbf F_r^\times
\]

是阶为 `N` 的 cyclic group。映射

\[
x\mapsto x^m
\]

的 kernel 大小为 `g`。

因此

\[
\boxed{\#\{x\in\mathbf F_r^\times:x^m=1\}=g.}
\]

精确 unit-ratio density 为

\[
\boxed{\delta^-_{m,r}=\frac{\gcd(m,r-1)}{r-1}.}
\]

## 3. P025-T191 —— sum resonance 的可解性与 class count

sum branch 要解

\[
x^m=-1.
\]

取 cyclic group 的 generator 后，问题变成 linear congruence

\[
mt\equiv\frac N2\pmod N.
\]

其可解当且仅当

\[
g\mid\frac N2,
\]

等价于

\[
\boxed{\frac{r-1}{g}\text{ 为偶数}.}
\]

一旦可解，恰有 `g` 个 solutions。因此

\[
\boxed{
\#\{x:x^m=-1\}
=
\begin{cases}
g,&(r-1)/g\text{ 为偶数},\\0,&(r-1)/g\text{ 为奇数}.
\end{cases}}
\]

以及

\[
\boxed{
\delta^+_{m,r}
=
\begin{cases}
\displaystyle\frac{g}{r-1},&(r-1)/g\text{ 为偶数},\\[2mm]
0,&(r-1)/g\text{ 为奇数}.
\end{cases}}
\]

## 4. P025-T192 —— difference resonance 可以完全饱和

当且仅当

\[
g=r-1
\]

时，difference resonance 填满整个 unit-ratio space。

也就是

\[
\boxed{r-1\mid m.}
\]

因此 difference resonance **并不自动稀疏**。

定义 saturation set

\[
\boxed{\mathcal S_m:=\{r\ge3\text{ prime}:r-1\mid m\}.}
\]

对每个

\[
r\in\mathcal S_m,
\]

所有 unit prime ratios 都 support-resonant。

但这些 prime 必满足

\[
\boxed{r\le m+1,}
\]

所以 saturation set 是有限的，并由 lower exponent 的 divisor structure 预先决定。

## 5. P025-T193 —— sum resonance 永不完全饱和

若 sum equation 可解，则

\[
\frac{r-1}{g}
\]

为偶数，所以必有

\[
g\le\frac{r-1}{2}.
\]

因此

\[
\boxed{\delta^+_{m,r}\le\frac12.}
\]

只要 sum support-resonance observation 非空，它至少能删掉一半 unit ratio states。

## 6. P025-T194 —— large cover prime 的 resonance density 小

对任一 sign，

\[
g=\gcd(m,r-1)\le m.
\]

所以在 sum branch 可解时，以及 difference branch 始终有

\[
\boxed{\delta^{\pm}_{m,r}\le\frac{m}{r-1}.}
\]

特别地，若

\[
\boxed{r>m+1,}
\]

则 difference resonance 不可能饱和，并且两个 sign 都满足

\[
\boxed{\delta^{\pm}_{m,r}\le\frac{m}{r-1}<1.}
\]

固定 lower exponent 后，cover prime 越大，support resonance 越具选择性。

## 7. P025-T195 —— finite height incidence

固定整数 height

\[
P\ge1.
\]

令 `C` 为 P025-T190 或 P025-T191 的 exact resonance class count。

`q<=P` 中作为模 `r` 单位的选择至多有

\[
P-\left\lfloor\frac Pr\right\rfloor
\]

个。

对每个这样的 `q` 与每个 allowed ratio class，相应的 nonzero residue class 中 `p<=P` 的整数至多有

\[
\left\lceil\frac Pr\right\rceil
\]

个。

因此 resonance classes 中的 ordered integer pairs 至多为

\[
\boxed{
C
\left(P-\left\lfloor\frac Pr\right\rfloor\right)
\left\lceil\frac Pr\right\rceil,
}
\]

并当然不超过 `P^2`。

primality 与 `p>q` ordering 只会继续减少该 envelope。

## 8. Cover-level congruence-or-residual routing

Stage 87 证明

\[
\Lambda_{m\to rm}\ge1
\Longrightarrow
\text{resonance}
\ \lor\
m(Q_{m,r})\ge r.
\]

Stage 88 现在把第一支完全量化。

所以 non-attenuating odd-prime cover 必位于以下并集：

1. density 为 `delta_{m,r}` 的有限 ratio state；
2. multiplicity residual 至少为 `r` 的 quotient value state。

对 large `r>m+1`，两类 cost 位于不同坐标，但都会随 `r` 增强：

\[
\boxed{
\delta_{m,r}\le\frac{m}{r-1},
\qquad
m(Q)\ge r\text{ off resonance}.
}
\]

这就是 **large-cover dual-pressure law**。

## 9. 负边界：不要总为 congruence precision 付费

若 difference branch 上

\[
r\in\mathcal S_m,
\]

则 resonance observation 在 unit ratios 上完全饱和，没有任何 filtering value。

此时计算 ratio class 本身就是浪费 precision：它无法区分 states。

因此 adaptive policy 必须再提前一步：

1. 先检查廉价 metadata pair `(m,r)`；
2. 算 exact resonance class count；
3. 只有当 quotient genuinely nontrivial 时，才观察 prime ratio modulo `r`。

这与 Stage 80 的 modulus horizon 类似，但这里的 saturation 来自**operation / exponent pair**，而不是 numerical observation window。

## 10. 架构含义

odd-prime cover 需要的 useful precision 取决于 operation language 中已经存在的 metadata。

顺序应为

\[
\boxed{
(m,r,\pm)
\to
\text{class-count test}
\to
\text{ratio congruence if informative}
\to
\text{quotient residual if nonresonant}.
}
\]

所以 precision compiler 不应盲目请求所有 available observables；应先判断某个 observable 是否已经被 declared operation parameters 饱和。

## 11. Prior-art / novelty 边界

finite cyclic groups 与 `x^m=a` 的 root-count formula 都是标准数学；finite residue-class incidence 也是 elementary estimate。

P025 不单独主张这些组成部分的新颖性。

项目侧候选是：把它们作为 Stage 87 pressure transport 的 exact precision cost，包括 operation-induced saturation boundary 与由此确定的 adaptive observation order。历史新颖性仍为 `NOVELTY_UNVERIFIED`。

## 12. 可执行资产

新增：

- `src/enterprise_math/abc_cover_resonance_precision.py`；
- `tests/test_abc_cover_resonance_precision.py`。

executable layer 通过 finite enumeration 检查 exact root counts、difference saturation、sum 的 empty / half-density cases、Stage 87 resonance fixtures，以及 height-window incidence envelope。

## 13. 下一前沿

不存在硬阻断。继续：

1. 从 `m` 的 divisor structure 高效分类 finite saturation set `S_m`；
2. 构造 cover-normal form，把 saturated small cover primes 与 sparse large cover primes 分开；
3. 利用 cyclotomic support congruences 继续攻击 quotient-residual branch `m(Q)>=r`；
4. 把 dyadic orbits 与 odd-cover resonance signatures 合并成一个 exponent transport normal form；
5. 然后为 task-relative transport precision 生成 Foundation Feedback Packet。
