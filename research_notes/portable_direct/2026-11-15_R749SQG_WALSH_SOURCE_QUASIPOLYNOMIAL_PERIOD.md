# R749SQG — Exact period 420 and first oscillatory correction for Walsh missing-source counts

Date: 2026-11-15. Research state: **AUTHOR_EXACT_NOT_REVIEWED**. Researcher: **EM-DIRECT-5AD5C5**; activity: **RA-23D649E29465155706DB0336** (activity association is a separate Source operation).

## 1. Exact object and inherited premises

This is an independent portable continuation of [R749SQF](https://github.com/awdawmip/enterprise-math/blob/f52082a0613cdf4a3b88841467437ca30dd05d0d/research_notes/portable_direct/2026-11-15_R749SQF_CONFLUENT_WALSH_PROVENANCE_SPLINE.md), preserving its frozen scientific pin **awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389**.

The object is the **auxiliary 16-atom signed Walsh source model**, with fixed $(t,s)=(1/10,1/2)$. It does not assert any native X6 signed-Port or three-dimensional-slice identification. The inherited positive-slack source alphabet has 23 labeled types, with slack multiset

| Slack $s$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Multiplicity $m_s$ | 3 | 4 | 6 | 4 | 3 | 2 | 1 |

Thus $\sum_s m_s=23$, $\sum_s sm_s=79$ and $W=\prod_s s^{m_s}=94,058,496,000$. As in SQF, for integers $r\ge1$ define
\[
C_r=\#\left\{m\in\mathbb Z_{\ge0}^{23}:\sum_{i=1}^{23}s_i m_i\le r-1\right\},
\quad C_r=0\ (r\le0).
\]
The uniform source-residual law of SQF depends exactly on the integer sequence $C_r$. The preceding 33-grid-point / 25-forced-source classification is inherited at author level.

## 2. Theorem: exact quasi-period, dominant parity correction

**Theorem (all $r\ge1$).** $C_r$ is a rational-coefficient quasipolynomial of degree 23, with **least quasipolynomial period exactly 420**. There exist rational polynomials $P_{23}$ and $Q_9$ of degrees 23 and 9, uniquely determined as the respective pole contributions at $z=1$ and $z=-1$, and a rational 420-quasipolynomial $R_{420}$ with no $z=1$ or $z=-1$ spectral component and constituent degree at most 7 such that
\[
\boxed{C_r=P_{23}(r)+(-1)^{r-1}Q_9(r)+R_{420}(r).}
\]

Write $[x^j]$ for an ordinary Taylor coefficient at zero. The following expressions specify the **entire** two polynomials, without interpolation:
\[
\begin{aligned}
G(x)&=\prod_{s=1}^{7}
 \left(\frac{x}{1-(1-x)^s}\right)^{m_s}
 =\sum_{j\ge0}g_jx^j,\\
H(x)&=\frac1{2-x}
 \prod_{\substack{1\le s\le7\\s\ {\rm even}}}
 \left(\frac{x}{1-(1-x)^s}\right)^{m_s}
 \prod_{\substack{1\le s\le7\\s\ {\rm odd}}}
 \left(\frac1{1+(1-x)^s}\right)^{m_s}
 =\sum_{j\ge0}h_jx^j,\\
P_{23}(r)&=\sum_{j=0}^{23}g_j {r+22-j\choose23-j},\\
Q_9(r)&=\sum_{j=0}^{9}h_j {r+8-j\choose9-j}.
\end{aligned}
\]
In particular the initial coefficients are
\[
\boxed{g_0=\frac1W,\quad g_1=\frac{28}{W},\quad
h_0=\frac1{9\cdot2^{28}},\quad h_1=\frac{35}{9\cdot2^{28}}.}
\]
Consequently, as $r\to\infty$ through positive integers,
\[
\begin{aligned}
P_{23}(r)&=\frac{r^{23}}{23!\,W}
       +\frac{39\,r^{22}}{22!\,W}+O(r^{21}),\\
Q_9(r)&=\frac{1}{9\cdot 2^{28}}
       \left(\frac{r^9}{9!}+\frac{39r^8}{8!}+O(r^7)\right),\\
\boxed{C_r-P_{23}(r)
 &=(-1)^{r-1}\frac{r^9}{9!\,9\cdot2^{28}}+O(r^8).}
\end{aligned}
\]
Hence the first nonconstant residue-class effect below the degree-23 polynomial part is a parity oscillation of degree **9**, while all other root-of-unity contributions have degree at most **7**.

### Proof

The exact integer generating function is
\[
F(z)=\sum_{r\ge1}C_rz^{r-1}
=\frac1{1-z}\prod_{s=1}^7(1-z^s)^{-m_s}.
\]
All its poles are roots of unity of exact orders $d\in\{1,2,3,4,5,6,7\}$. The pole order at a primitive $d$th root is $\sum_{d\mid s}m_s$, with one extra order for $d=1$ from the cumulative $(1-z)^{-1}$ factor. Thus the exact pole-order vector is
\[
\boxed{(24,10,8,4,3,2,1)\quad\text{for }d=(1,2,3,4,5,6,7).}
\]
The numerator is the constant 1, so each listed pole is genuine. Partial fractions give an exact sum of terms $\zeta^{-(r-1)}p_\zeta(r)$, with $\deg p_\zeta$ exactly one less than its pole order. All such frequencies have order dividing $\operatorname{lcm}(1,\ldots,7)=420$, giving period at most 420. Any quasipolynomial representation of period $T$ has generating-function poles only at $T$th roots; the genuine primitive-order poles $2,3,4,5,6,7$ force $T$ to be divisible by each, so the least period is 420.

Set $z=1-x$. The factorization is $F(1-x)=x^{-24}G(x)$, whence the pole-$1$ coefficient at $z^{r-1}$ is the displayed $P_{23}(r)$. Next set $z=-1+x$. Every even-weight factor vanishes simply and the odd-weight factors do not vanish; the factorization is $F(-1+x)=x^{-10}H(x)$. Its coefficient at $z^{r-1}$ is $(-1)^{r-1}Q_9(r)$. After removing both principal parts, only primitive orders $3,4,5,6,7$ remain, of maximum pole order 8. This proves the exact remainder bound and quasi-periodicity.

At $x=0$, every $(1-(1-x)^s)/x$ equals $s$, giving $g_0=1/W$. Its first-order expansion $s[1-(s-1)x/2+\cdots]$ yields $g_1/g_0=\sum_s m_s(s-1)/2=(79-23)/2=28$. At $z=-1$, the odd factors equal $2$ and the even factors contribute their weights; the product gives $h_0=1/(9\cdot2^{28})$. Logarithmic differentiation of the regularized factor yields
\[
h_1/h_0=\tfrac12+\tfrac12\sum_{s\ {\rm odd}}sm_s
           +\tfrac12\sum_{s\ {\rm even}}(s-1)m_s
        =\frac{1+79-10}{2}=35.
\]
Expansion of the two binomial bases gives the stated degree-23/22 and parity-9/8 coefficients. All claims follow. $\square$

**Corollary (integer finite-difference diagnostic).** Let $\Delta C_r=C_{r+1}-C_r$. Then
\[
\boxed{\Delta^{24}C_r=(-1)^{r-1}\frac{r^9}{144\cdot9!}+O(r^8).}
\]
This annihilates the full polynomial part and exposes the leading parity provenance oscillation. It is a sequence-level residual detector, not a new native BRC operator.

## 3. Exact reproducibility and finite validation

Run:
\`\`\`bash
python3 research_notes/portable_direct/R749SQG_WALSH_QUASIPOLYNOMIAL_CERT.py \
  > research_notes/portable_direct/R749SQG_WALSH_QUASIPOLYNOMIAL_RESULTS.json
\`\`\`

The standard-library verifier uses integer partition dynamic programming for $C_r$ and exact \`Fraction\` Taylor recurrences for every $g_j$ ($0\le j\le23$) and $h_j$ ($0\le j\le9$). On **all $r=1,\ldots,3780$**, it computes $C_r-P_{23}(r)-(-1)^{r-1}Q_9(r)$, and for **all 420 residue classes** checks the exact eighth 420-step forward difference on nine consecutive samples. The locally executed result is **PASS**, without floating-point tolerance. The saved JSON exposes the full two coefficient vectors and selected exact counts. The universal theorem follows from the pole proof; finite verification is independent consistency evidence.

## 4. Frontier and boundaries

This result operates on R749SQF's 23-source integer deficit alphabet, not an independently authenticated native signed-Port/X6 observer. Its proof is conditional only on the inherited exact slack multiset, and does not need the earlier spline formula to establish the quasipolynomial. The entire calculation is ordinary combinatorial counting, so the typed native heartbeat/BRC-only arithmetic restriction is not invoked.

Next discriminating research unit: compute the primitive third-root degree-7 component explicitly, then use the fully separated frequency expansion to obtain a sharp residue-class first-order Kolmogorov correction for the finite optional-source tail $C_{r-3k}/C_r$ and its optimal uniform constant. Independently audit the inherited 23-type slack classification against the immutable frozen eight-facet source before any stronger source-admission claim.
