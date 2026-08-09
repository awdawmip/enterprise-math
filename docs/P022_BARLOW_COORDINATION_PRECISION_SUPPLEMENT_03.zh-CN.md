# P022 Barlow 配位精度补充 03 —— binomial-weighted sum-of-two-squares fibers

状态：`ACTIVE RESEARCH NOTE / EXACT ARITHMETIC FIBER SPECTRUM / NOVELTY_UNVERIFIED`  
归属：`program/p022-geometry-v2`  
依赖：BC04 shell drift-energy quotient 与 P022 precision-fiber methodology

## 1. shell cardinality 本身也是一个 many-to-one quotient

固定 radius `n` 时，whole-shell cardinality 只通过

\[
Q_n=\delta_n^2+\delta_{-n}^2
\]

读取 stacking：

\[
4S_n=42n^2+8-Q_n.
\]

一个 finite two-sided stacking window 在根层两侧各包含一个长度 `n` 的独立 ±1 microscopic word。因此在应用 shell-cardinality observation 以前，共有

\[
4^n
\]

个 microscopic two-sided windows。

本文精确计算这些 windows 如何 collapse 到 possible `Q_n` / `S_n` states。

## 2. one-sided absolute-drift fibers

长度 `n` 的 word 的 signed imbalance 为

\[
a\in\{-n,-n+2,\ldots,n\}.
\]

固定 signed imbalance `a` 的 word 数是

\[
\binom n{(n+a)/2}.
\]

shell cardinality 会忘掉 sign，所以对 admissible absolute drift `d>=0`：

\[
\boxed{
W_n(d)=
\begin{cases}
\binom n{n/2},&d=0,\\
2\binom n{(n+d)/2},&d>0.
\end{cases}}
\]

只有

\[
0\le d\le n,
\qquad
d\equiv n\pmod2
\]

会出现。

## 3. P022-CF01 —— shell-energy fiber spectrum

对 represented drift energy

\[
Q=d_+^2+d_-^2,
\]

microscopic two-sided fiber size 为

\[
\boxed{
F_n(Q)
=
\sum_{\substack{d_+^2+d_-^2=Q\\
0\le d_\pm\le n\\
d_\pm\equiv n\pmod2}}
W_n(d_+)W_n(d_-).}
\]

若不先 quotient signs，也可写成

\[
\boxed{
F_n(Q)=
\sum_{\substack{a^2+b^2=Q\\
a,b\equiv n\pmod2\\
|a|,|b|\le n}}
\binom n{(n+a)/2}
\binom n{(n+b)/2}.}
\]

这是一套 **binomial-weighted sum-of-two-squares spectrum**。

固定 `n` 时 `Q -> S_n` 是 injective，所以 shell-cardinality fiber spectrum 只是把 energy labels 用

\[
S_n=(42n^2+8-Q)/4
\]

重新标记。

总 fiber mass 正好恢复所有 microscopic windows：

\[
\boxed{
\sum_QF_n(Q)=4^n.}
\]

## 4. generating polynomial

定义 one-sided weighted square polynomial

\[
\boxed{
\Phi_n(z)
=
\sum_{d\equiv n\ (2)}W_n(d)z^{d^2}.}
\]

则整个 two-sided shell-energy spectrum 由

\[
\boxed{
\Phi_n(z)^2
=
\sum_QF_n(Q)z^Q
}
\]

一次编码。

所以 shell-cardinality quotient fibers 本身形成一个 finite non-negative coefficient layer，exponents 正是 quadratic drift energies。

这是 A4/P011 count-enriched 逻辑在几何中的又一个 arithmetic shadow：Boolean/cardinality observation 已经忘记了每个 represented coordination state 背后有多少 microscopic stacking histories。

## 5. P022-CF02 —— shell-cardinality 的精确 extremal bounds

最大 drift energy 出现在两侧 prefix 都 constant sign：

\[
Q_{\max}=2n^2.
\]

所以 Barlow shell 的最小 cardinality 是

\[
\boxed{
S_n^{\min}=10n^2+2.}
\]

FCC 在每个 radius 都达到该下界。

单侧最小 admissible absolute drift 由 parity 强制：

\[
d_{\min}=
\begin{cases}
0,&n\text{ even},\\
1,&n\text{ odd}.
\end{cases}
\]

所以

\[
Q_{\min}=
\begin{cases}
0,&n\text{ even},\\
2,&n\text{ odd}.
\end{cases}
\]

从而最大 shell cardinality 为

\[
\boxed{
S_n^{\max}
=\left\lfloor\frac{21n^2}{2}\right\rfloor+2.}
\]

HCP 在每个 radius 都达到该上界。

因此所有 Barlow shells 都满足 sharp interval：

\[
\boxed{
10n^2+2
\le
S_n
\le
\left\lfloor\frac{21n^2}{2}\right\rfloor+2.}
\]

finite window 意义下 extremizer 并不唯一：任何拥有对应 extreme drift magnitudes 的 two-sided prefix 都会达到同一个 bound。

## 6. P022-CF03 —— parity 与 arithmetic holes

represented energies 远不是任意整数。

### even radius

所有 signed imbalances 都是 even，因此

\[
\boxed{Q\equiv0\pmod4.}
\]

令 `a=2u`、`b=2v`，represented energies 变成

\[
Q=4(u^2+v^2).
\]

### odd radius

所有 signed imbalances 都是 odd。任意 odd square 都是 `1 mod 8`，因此

\[
\boxed{Q\equiv2\pmod8.}
\]

这些 congruences 只是必要条件，并不充分。radius 增大后仍会存在 additional holes，因为并非同一 congruence class 中的每个 integer 都能写成两个 bounded parity-compatible squares 的和。

所以 possible shell-cardinality states 在 sharp interval 内构成一个 discrete arithmetic subset，而不是连续整数区间。

这给 finite precision geometry 与 classical sum-of-two-squares structure 建立了直接接口，但不主张任何 classical number-theory novelty。

## 7. shell-cardinality quotient 比 final signed drift 粗得多

对 coordinate-sensitive extreme-layer support，signed pair

\[
(\delta_n,\delta_{-n})
\]

可以由 first moments 恢复。

whole-shell cardinality 连续做了两次信息删除：

1. 两侧分别平方，擦掉 sign；
2. 两个平方再相加，擦掉 energy 在两侧如何 allocation。

所以 exact quotient chain 是

\[
\boxed{
(\delta_n,\delta_{-n})
\longmapsto
Q_n=\delta_n^2+\delta_{-n}^2
\longmapsto
S_n.}
\]

CF01 又进一步精确计数：每一个最终 fiber 中还保留了多少 microscopic ±1 histories。

## 8. P011 / P023 / P024 关系

### P011

shell-cardinality map 是另一个 finite functional quotient，并拥有 explicit fiber spectrum。generic collision statistics 仍归 P011；P022 只提供 weighted sum-of-two-squares specialization。

### P023/P024

future observable 从 signed coordinate support 改成 whole-shell cardinality 后，sufficient state 从 signed drift pair 降成一个 quadratic energy。这个 coarsening 合法，正因为 future language 不再询问 drift 发生在哪一侧、朝哪个 orientation。

### P022

P022 保留 Barlow-specific arithmetic constraints、sharp coordination bounds 与 exact microscopic fiber weights。

## 9. executable assets

新增：

- `src/enterprise_math/p022_barlow_coordination_fibers.py`；
- `tests/test_p022_barlow_coordination_fibers.py`。

测试 exhaustively 枚举所有短 two-sided microscopic ±1 windows，验证 weighted sum-of-two-squares fiber formula、总质量 `4^n`、sharp shell extrema，并确认 parity congruence 之外确实还存在 arithmetic holes。
