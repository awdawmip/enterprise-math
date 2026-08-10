# P025 补充 87 —— Odd-Prime Cover 的局部 Transport 与 Support Resonance

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-cyclotomic-stage76`  
依赖：P025 补充 84–86  
硬阻断：`NONE`

## 1. Generic cover edge 只新增一个局部 quotient

设

\[
r\ge3
\]

为奇素数，并令

\[
n=rm.
\]

对 difference sign，定义

\[
A_m=p^m-q^m,
\qquad
Q^-_{m,r}:=\frac{p^{rm}-q^{rm}}{p^m-q^m}.
\]

对 same-sign sum route，由于 `r` 为奇数，它自动 admissible；定义

\[
A_m=p^m+q^m,
\qquad
Q^+_{m,r}:=\frac{p^{rm}+q^{rm}}{p^m+q^m}.
\]

Stage 84 的 cover multiplier 为

\[
\Lambda_{m\to rm}=\frac{\Gamma m(Q)}r.
\]

唯一还没局部化的数据就是 overlap factor `Gamma`。

## 2. P025-T185 —— ancestor / quotient gcd 只能是 `1` 或 `r`

记

\[
X=p^m,
\qquad
Y=q^m.
\]

对 difference quotient，

\[
Q^-_{m,r}=X^{r-1}+X^{r-2}Y+\cdots+Y^{r-1}.
\]

模

\[
X-Y
\]

有 `X=Y`，所以

\[
Q^-_{m,r}\equiv rY^{r-1}\pmod{X-Y}.
\]

由于 `Y` 与 `X-Y` 互素，

\[
\boxed{\gcd(A_m,Q^-_{m,r})=\gcd(A_m,r).}
\]

对 sum quotient，

\[
Q^+_{m,r}=X^{r-1}-X^{r-2}Y+\cdots-XY^{r-2}+Y^{r-1}.
\]

模

\[
X+Y
\]

有 `X=-Y`，每一项都退化为同一个 unit multiple 的 `Y^{r-1}`，因此同样得到

\[
\boxed{\gcd(A_m,Q^+_{m,r})=\gcd(A_m,r).}
\]

因为 `r` 是素数，该 gcd 只能是 `1` 或 `r`。

## 3. P025-D32 —— cover support resonance

当

\[
\boxed{r\mid A_m}
\]

时，称该 cover **support-resonant**。

此时 ancestor 与 new quotient 只共享 cover prime `r`。

若不 support-resonant，则两块 support 完全不重叠。

因此 radical-overlap correction 为

\[
\boxed{
\Gamma
=
\begin{cases}
r,&r\mid A_m,\\1,&r\nmid A_m.
\end{cases}}
\]

## 4. P025-T186 —— resonant prime 在 quotient 中只新增一次

假设

\[
r\mid A_m.
\]

此时 cover prime 必不同于 base primes `p,q`，否则不可能整除 `p^m\pm q^m`。

ordinary LTE 在 difference route 给出

\[
v_r(p^{rm}-q^{rm})
=v_r(p^m-q^m)+v_r(r),
\]

odd-exponent plus 版本在 sum route 给出同样结论。

因为

\[
v_r(r)=1,
\]

所以

\[
\boxed{v_r(Q_{m,r})=1.}
\]

因此 overlap prime 本身不会在 new quotient 内贡献 multiplicity residual。

两个作用由此完全分离：

- `r` 可以通过 support reuse 抵消 normalization；
- 超出这部分的 quotient amplification 必须来自其他 repeated support。

## 5. P025-T187 —— exact local odd-prime cover formula

把两种 overlap factor 代回 Stage 84，得到

\[
\boxed{
\Lambda_{m\to rm}
=
\begin{cases}
\displaystyle\frac{m(Q_{m,r})}{r},&r\nmid A_m,\\[3mm]
\displaystyle m(Q_{m,r}),&r\mid A_m.
\end{cases}}
\]

这就是所有 odd-prime same-sign covers 的 exact local transport law。

## 6. Transport classification 现在完全显式

### Resonant locus

若

\[
r\mid A_m,
\]

则

\[
\Lambda=m(Q)
\]

为正整数，所以 edge 永不 attenuate：

- `m(Q)=1`：resonant transport；
- `m(Q)>1`：amplified transport。

### Nonresonant locus

若

\[
r\nmid A_m,
\]

则

\[
\Lambda=\frac{m(Q)}r.
\]

因此：

- `m(Q)<r`：attenuation；
- `m(Q)=r`：exact resonance；
- `m(Q)>r`：amplification。

也就是说，在 support-resonance locus 外，new quotient 必须先支付完整的 factor `r`，才能抵消 exponent-normalization cost。

## 7. P025-T188 —— cover resonance 就是 prime-ratio congruence

在 resonant locus 上 `r` 自动不同于 `p,q`。定义

\[
x=pq^{-1}\pmod r.
\]

对 difference，

\[
r\mid p^m-q^m
\iff
\boxed{x^m\equiv1\pmod r}.
\]

对 sum，

\[
r\mid p^m+q^m
\iff
\boxed{x^m\equiv-1\pmod r}.
\]

因此 normalization cancellation 不是隐藏算术，而只是 prime ratio 的有限 root-of-unity condition。

它比 Stage 77–79 的 repeated-prime-power signatures 还要便宜，是第二层更粗的 congruence precision。

## 8. 重新理解 Stage 84 三态

`3->9` sum fixtures 现在完全透明。

### Attenuated：`(q,p)=(5,59)`

ancestor 不被 3 整除，quotient squarefree，所以

\[
\Lambda=\frac13.
\]

### Resonant：`(q,p)=(11,13)`

ancestor 被 3 整除，quotient squarefree，所以

\[
\Lambda=1.
\]

### Amplified：`(q,p)=(7,29)`

ancestor 被 3 整除，并且 quotient residual 为 `19`，所以

\[
\Lambda=19.
\]

nonresonant edge 同样可能 amplification，只要 quotient residual 超过 `r`；例如 `(q,p)=(3,13)` 的 `3->9` difference route。

## 9. P025-C30 —— prime two 是唯一 universal resonance cover

Stage 86 证明对 odd bases，任意 `m` 都有

\[
2\mid p^m-q^m
\]

以及

\[
2\mid p^m+q^m.
\]

所以 prime-two doubling edge 永远获得足以抵消 normalization 的 overlap factor。

任何 odd cover prime 都没有这种对所有 base states 成立的 universal property。对任意 odd prime `r`，只要取其中一个 base prime 就等于 `r`，则对应 sum / difference ancestor 不可能被 `r` 整除，因为另一个 base 在模 `r` 下非零。

因此

\[
\boxed{
2\text{ 是 odd-prime bases 上唯一 universal support-resonant 的 cover prime}.
}
\]

这正是 Stage 86 universal dyadic non-attenuation 的原因。

## 10. P025-T189 —— congruence-or-residual dichotomy

若 odd-prime cover non-attenuating：

\[
\Lambda_{m\to rm}\ge1,
\]

由 P025-T187，必有

\[
r\mid A_m,
\]

或者在 nonresonant branch 上

\[
m(Q_{m,r})\ge r.
\]

因此

\[
\boxed{
\Lambda_{m\to rm}\ge1
\Longrightarrow
\big(r\mid A_m\big)
\ \lor\ 
\big(m(Q_{m,r})\ge r\big).
}
\]

更一般地，若

\[
\Lambda\ge T,
\]

则：

- resonant branch：`m(Q)>=T`；
- nonresonant branch：`m(Q)>=Tr`。

所以每条 strong odd-prime cover 都必须通过有限 congruence precision，或通过相应更大的 new residual 付费。

## 11. Precision 解释

每条 odd-prime cover 有两个 possible payment channels：

\[
\boxed{
\text{old support resonance}
\quad\text{或}\quad
\text{new quotient multiplicity}.
}
\]

第一条很便宜：只需观察模 `r` 的一个 residue equation。

第二条在 value space 更贵，但量化得很清楚：没有 resonance 时，quotient residual 必须补偿完整的 prime normalization cost。

因此 theorem-native adaptive precision policy 是：

1. 先检查低成本 resonance congruence；
2. 只有失败后，再把 quotient multiplicity 精度提高到足以判断是否达到 `r`-scaled threshold。

## 12. Prior-art / novelty 边界

geometric-series congruence、gcd identity 与 LTE 都是经典数学。

P025 不单独主张这些组成部分的新颖性。

项目侧候选是：把它们精确组合成 local projective cover multiplier、support-resonance interpretation，以及 congruence-or-residual routing dichotomy。历史新颖性仍为 `NOVELTY_UNVERIFIED`。

## 13. 可执行资产

新增：

- `src/enterprise_math/abc_odd_prime_cover_transport.py`；
- `tests/test_abc_odd_prime_cover_transport.py`。

executable layer 检查 gcd law、resonant cover prime 的 exact quotient valuation、radical overlap、multiplier formula、ratio-congruence criterion，以及全部三种 transport classes。

## 14. 下一前沿

不存在硬阻断。继续：

1. 精确计算 support-resonance ratio classes modulo `r` 的数量；
2. 给 resonant prime-base pairs 推导 finite height-`P` incidence bound；
3. 把它与 nonresonant residual threshold `m(Q)>=Tr` 合并成 cover-level sparse-state theorem；
4. 判断 cover-resonance signatures 能否沿 Hasse paths 组合而无需保存 full prime bases；
5. 用这些结果构造 Stage 86 承诺的 orbit-normal form。
