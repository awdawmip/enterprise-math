# P025 补充 89 —— Odd-Cover Transport Spectral Gap 与 Two-Bit Qualitative State

状态：`ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation：`program/p025-cyclotomic-stage76`  
依赖：P025 补充 87–88  
硬阻断：`NONE`

## 1. Stage 87 仍把 quotient residual 当作任意整数

Stage 87 对奇 cover prime `r` 给出 exact local formula：

\[
\Lambda_{m\to rm}
=
\begin{cases}m(Q)/r,&\text{nonresonant},\\m(Q),&\text{support-resonant}.
\end{cases}
\]

单看这个公式，会形式上允许许多中间 multiplier values。但 quotient `Q` 不是任意整数，而是 prime-index cyclotomic value。

这个额外结构产生了很大的 spectral gap。

## 2. New quotient 是 cyclotomic

记

\[
X=p^m,
\qquad
Y=q^m.
\]

对 difference cover，

\[
\boxed{Q=\Phi_r(X,Y).}
\]

对 same-sign sum cover，

\[
\boxed{Q=\Phi_{2r}(X,Y).}
\]

而 `X,Y` 互素。

## 3. P025-T196 —— repeated quotient primes 必为 `1 mod 2r`

设 `s` 是 `Q` 的 repeated prime divisor。

exceptional cover prime `r` 只可能在 support-resonant locus 出现，而 Stage 87 已证明

\[
v_r(Q)=1.
\]

所以任何 repeated prime 都满足

\[
s\ne r.
\]

对 difference quotient，ratio

\[
XY^{-1}\pmod s
\]

具有 exact order `r`；对 sum quotient 则具有 exact order `2r`。

在 difference 情形，`r|s-1`；由于 `r,s` 都是奇数，同时又有 `2|s-1`，因此

\[
2r\mid s-1.
\]

sum 情形直接得到同一个 divisibility。

所以两个 sign 都有

\[
\boxed{s\equiv1\pmod{2r}.}
\]

特别地，

\[
\boxed{s\ge2r+1.}
\]

## 4. P025-T197 —— quotient residual gap

若 `Q` squarefree，则

\[
\boxed{m(Q)=1.}
\]

若 `Q` nonsquarefree，任选一个 repeated prime `s`。因为 `s` 在 `Q` 中 exponent 至少为 2，

\[
s\mid m(Q).
\]

由 P025-T196，

\[
\boxed{m(Q)\ge2r+1.}
\]

因此 odd-prime cover 中不存在

\[
\boxed{1<m(Q)<2r+1}
\]

的 quotient residual values。

这排除了 Stage 87 bare formula 所形式允许的大部分中间情形。

## 5. P025-T198 —— transport spectral gap

把 P025-T197 与 Stage 87 multiplier formula 合并。

### Nonresonant branch

若 `Q` squarefree，

\[
\boxed{\Lambda=1/r.}
\]

若 `Q` nonsquarefree，

\[
\boxed{\Lambda=\frac{m(Q)}r\ge\frac{2r+1}{r}>2.}
\]

所以 nonresonant branch 从强 attenuation 直接跳到超过两倍 amplification。

### Support-resonant branch

若 `Q` squarefree，

\[
\boxed{\Lambda=1.}
\]

若 `Q` nonsquarefree，

\[
\boxed{\Lambda=m(Q)\ge2r+1.}
\]

所以 resonant branch 从 exact preservation 直接跳到至少 `2r+1` 倍 amplification。

## 6. P025-C31 —— formal nonresonant exact resonance 实际不可能

Stage 87 的 bare formula 形式上允许 nonresonant cover 出现

\[
m(Q)=r
\]

从而

\[
\Lambda=1.
\]

P025-T197 完全排除了这种情况：

\[
\boxed{\text{nonresonant odd-prime cover 永远不可能 exact resonant}.}
\]

同样，nonresonant branch 也不存在

\[
1<\Lambda\le2
\]

的 weak amplification interval。

这是对 Stage 87 formal trichotomy 的真正修正与收紧。

## 7. P025-T199 —— qualitative transport 只需要两个 natural bits

定义

\[
R:=\mathbf1_{\{r\mid A_m\}},
\]

即 ancestor support-resonance bit；再定义

\[
S:=\mathbf1_{\{Q\text{ squarefree}\}},
\]

即 quotient-squarefree bit。

则 exact transport class 为

\[
\boxed{
\begin{array}{c|c|c}
R&S&\text{transport class}\\ \hline
0&1&\text{attenuated}\\
1&1&\text{resonant}\\
0&0&\text{amplified}\\
1&0&\text{amplified}
\end{array}}
\]

等价地，

\[
\boxed{S=0\Longrightarrow\text{amplified},}
\]

而 `S=1` 时才由 `R` 区分 attenuation 与 resonance。

因此 exact qualitative future query **不需要** `m(Q)` 的数值。

## 8. 这两个 natural bits 各自都不够

只保留 resonance bit 不够：

- `(q,p)=(11,13)` 的 `3->9` sum：`R=1`，quotient squarefree，resonant；
- `(q,p)=(7,29)`：`R=1`，quotient repeated，amplified。

只保留 squarefree bit 也不够：

- `(q,p)=(5,59)`：quotient squarefree、nonresonant，attenuated；
- `(q,p)=(11,13)`：quotient squarefree、resonant。

所以两个 one-bit natural projections 都不能 factor 三态 future query。

pair `(R,S)` 可以。

## 9. Exact fifth-cover 校准

同一个 gap 在 `r=5` 也真实存在。

### Resonant fifth cover

对 difference branch

\[
(q,p,m,r)=(19,29,2,5),
\]

quotient 含

\[
11^3,
\qquad11\equiv1\pmod{10},
\]

且

\[
m(Q)=121.
\]

edge support-resonant，并以

\[
\Lambda=121
\]

放大。

### Nonresonant fifth cover

对 sum branch

\[
(q,p,m,r)=(7,47,2,5),
\]

quotient 含

\[
41^2,
\qquad41\equiv1\pmod{10},
\]

因此

\[
m(Q)=41
\]

且

\[
\boxed{\Lambda=\frac{41}{5}>8.}
\]

同样没有 weak-amplification regime。

## 10. Precision 后果

对 future query

\[
\text{“attenuated、resonant 还是 amplified？”}
\]

full quotient factorization 完全没有必要。

natural sufficient state 是

\[
\boxed{(R,S).}
\]

它在语义上远比 full quotient residual、repeated modulus 或 cyclotomic factorization 更粗。

但这仍然是 **task-relative**。若 future query 要求 exact multiplier `Lambda`，则 `Q` nonsquarefree 时必须恢复 `m(Q)` 的数值。

所以同一 arithmetic edge 自然存在多层 precision。

## 11. Prior-art / novelty 边界

cyclotomic order arguments 都是经典数学；repeated prime divisors 的 congruence restriction 是 multiplicative order 的标准后果。

P025 不单独主张这些组成部分的新颖性。

项目侧候选是 transport spectral-gap consequence、exact two-natural-bit qualitative compiler，以及它作为 task-relative precision state 的使用。历史新颖性仍为 `NOVELTY_UNVERIFIED`。

## 12. 可执行资产

新增：

- `src/enterprise_math/abc_odd_cover_transport_gap.py`；
- `tests/test_abc_odd_cover_transport_gap.py`。

executable layer 验证 repeated support modulo `2r`、residual floor、exact fixtures 实现的四种 logical bit combinations，以及 tested covers 中不存在 weak amplification。

## 13. 下一前沿

不存在硬阻断。继续：

1. 区分 binary future query `Lambda>=1` 与 ternary transport-class query 的最小 state；
2. 推导这些 query 的 exact short-circuit observation trees；
3. 比较 information-minimal 与 computational-cost-aware observation order；
4. 只保留 future-relevant edge labels，构造 dyadic / odd-cover orbit normal form；
5. 把这一结果作为 future-relative precision 的 theorem-backed pressure test 返回 P023/A2。
