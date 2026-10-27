# D25 / SECOND-DIGIT-LIFT: sourced Cauchy transport and its nonvanishing Wilson cutoff

Date: 2026-10-27. **AUTHOR-SIDE / PROVED ALGEBRAIC TRANSPORT AND WILSON WEDGE / 11 EXACT INTEGER CHECKS / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / NOT_NATIVE_H0B0 / NOT_SOURCE_NATIVE_CHECKPOINT.**

Research-onhour logical lane: chatgpt-research-onhour-enterprise-math-20260923 (not maintenance chatgpt-hourly-enterprise-math-20260921). Mother: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. Source Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. **Frozen scientific Source pin remains c47e13e4aba0e006366f989d6334d443f6333ae3.** This author artifact neither asserts nor obtains Source CLAIM/session/run/Research-Activity admission.

## 1. Genuine source match and attribution

Roman Le Lan, *Series for 1/pi arising from Cauchy product*, arXiv:2604.03327v1 (2026-04-02), https://arxiv.org/html/2604.03327v1 , Lemma 1 / (3.2), identifies an exact Euler/Clausen Cauchy product whose right-hand coefficients are precisely those of our original weighted-216 series. Le Lan's Conjecture 1 concerns the distinct finite (3n-1)-weighted Cauchy truncation modulo p²; the article explicitly says it did **not** prove that supercongruence. The paper's infinite-series identity is prior art; our new finite cutoff filtration and Wilson wedge below are author-side derivations, not an assertion of external novelty or acceptance.

Work in rational p-local arithmetic for p>3. Set

\[
a_n=\frac{\binom{2n}{n}^{2}\binom{3n}{n}}{216^n},\quad
t_j=\frac{\binom{2j}{j}}{8^j},\quad
f_n=\frac{(1/3)_n(1/6)_n}{2^n(n!)^2},\quad
g_n=\frac{(2/3)_n(5/6)_n}{2^n(n!)^2},\quad
c_n=\sum_{i=0}^n f_i g_{n-i}.
\]

Keep **different** original and Cauchy truncation observers:

\[
W_p=\sum_{k=0}^{p-1}(6k+1)a_k,\quad S_p=\sum_{n=0}^{p-1}(3n-1)c_n,\quad
A_p=\sum_{k<p}a_k,\quad T_p=\sum_{j<p}t_j,\quad J_p=\sum_{j<p}jt_j,
\]
\[
E_p=\sum_{\substack{0\le j,k<p\\j+k\ge p}}\bigl(3(j+k)-1\bigr)t_j a_k.
\]

The Cauchy cutoff E is **not** the previously accepted original reflected Clausen cutoff Q/R. Do not merge these typed ports.

## 2. Theorem A: exact finite transport (all p>3)

\[
\boxed{c_n=\sum_{j=0}^n t_j a_{n-j},\qquad
2S_p=T_pW_p+3(2J_p-T_p)A_p-2E_p.}\tag{A}
\]

**Proof.** Formal Euler transformation gives
\({}_2F_1(2/3,5/6;1;z)=(1-z)^{-1/2}{}_2F_1(1/3,1/6;1;z)\).
Le Lan's exact coefficient identity gives
\({}_2F_1(1/3,1/6;1;z)^2
=\sum_{n\ge0}\binom{2n}{n}^2\binom{3n}{n}z^n/108^n\).
Multiply and take the coefficient of \(z^n\) at \(z=1/2\), which yields the first identity without any p-adic interchange of infinite series. Sum its terms over the **triangle** \(j+k<p\) with weight \(3(j+k)-1\). Completing that triangle to the finite rectangle \(0\le j,k<p\) adds **exactly E**. The rectangular moment is \((3J-T)A+3T\sum k a_k\). Use \(W=A+6\sum k a_k\) and multiply by 2. QED.

## 3. Theorem B: certified p³ reduction at the frozen CM0 branch

Let \(p=6m+1\) with \(p\bmod24\in\{13,19\}\). **Consume**, rather than redo, accepted CM0/UR: \(M_p=\sum_{n<p} f_n\equiv0\bmod p\). The same exact Clausen coefficient identity yields
\(
 A_p=M_p^2-\sum_{0\le i,j<p,\ i+j\ge p} f_i f_j.
\)
Here \(v_p(f_n)=0\) for \(n\le m\), 1 for \(m<n\le2m\), and 2 for \(2m<n<p\). Thus every tail pair has total valuation at least 2, so \(A_p\equiv0\bmod p^2\). Independently, the finite-field identity
\(
\sum_{j<p}\binom{2j}{j}x^j
\equiv(1-4x)^{(p-1)/2}\bmod p
\)
and its derivative at \(x=1/8\) give \(2J_p-T_p\equiv0\bmod p\). At both target residue classes \((2/p)=-1\), so \(T_p\equiv-1\bmod p\) and is a unit. Therefore equation (A) loses no information modulo p³ when dropping its **provably p³-divisible** third-moment term:

\[
\boxed{2(S_p+E_p)\equiv T_pW_p\pmod{p^3}.}\tag{B}
\]
\[
\boxed{W_p\equiv p\pmod{p^3}\iff
2(S_p+E_p)\equiv pT_p\pmod{p^3}.}\tag{B'}
\]

This is an exact alternative observer bridge, NOT automatically a lower-complexity all-prime proof. The prior author-side source-port equivalence
\((W_p-p)/p^2=\Delta_p-R_p\bmod p\)
is preserved at its original unreviewed status, as are the frozen R, \(\kappa\), and Green/Hesse observables.

## 4. Theorem C: the unique order-p Wilson boundary wedge (all p=6m+1>3)

For \(0\le j,k<p\), factorial valuations are exact:
\[
v_p(t_j)=
\begin{cases}0&j\le3m\\1&j>3m\end{cases},
\quad
v_p(a_k)=
\begin{cases}0&k\le2m\\1&2m<k\le3m\\2&3m<k\le4m\\3&k>4m.\end{cases}
\]

If \(j+k\ge p\), then every pair except the wedge
\(j=p-r,\ 1\le r\le2m,\ r\le k\le2m\)
has \(v_p(t_ja_k)\ge2\). Indeed \(j\le3m\Rightarrow k\ge3m+1\), while \(j\ge3m+1,k\ge2m+1\Rightarrow v_p(t_ja_k)\ge2\). All remaining permissible pairs are exactly the claimed wedge. In particular \(p\mid E_p\). For each \(1\le r\le2m\), Wilson's theorem yields

\[
\frac1p\binom{2p-2r}{p-r}
\equiv-\frac{(r-1)!^2}{(2r-1)!}
=-\frac2{r\binom{2r}{r}}\pmod p.
\]

Since \(8^{-(p-r)}\equiv8^{r-1}\bmod p\), define
\(\mu_r=-2\,8^{r-1}/(r\binom{2r}{r})\bmod p\).
Its denominators are p-units on the full range, and it obeys the simple recurrence \(\mu_1=-1,\ \mu_{r+1}=4r\mu_r/(2r+1)\). Thus the entire leading divided cutoff has the independent **finite-field** certificate

\[
\boxed{\frac{E_p}{p}\equiv
 \sum_{r=1}^{2m}\mu_r\sum_{k=r}^{2m}(3(k-r)-1)a_k\pmod p.}\tag{C}
\]

This is an all-prime theorem for that valuation and cutoff *digit*, not a statement that the right side is a particular constant.

## 5. Distinct Sun conjecture: narrow, explicit unfinished certificate

In the two frozen D25 residue classes \((-6/p)=-1\), Le Lan/Sun's external conjectured value is \(S_p\equiv p\bmod p^2\). By the already accepted first digit \(W_p\equiv p\bmod p^2\), \(T_p\equiv-1\bmod p\), and (B), this separate external conjecture is **equivalent**, within the declared D25 classes, to

\[
\boxed{\frac{E_p}{p}\equiv-\frac32\pmod p
\iff
\sum_{r=1}^{2m}\mu_r\sum_{k=r}^{2m}(3(k-r)-1)a_k=-\frac32
\quad\text{in }\mathbb F_p.}\tag{D}
\]

**(D)'s constant-value assertion remains OPEN**, not a proved theorem here. This new reduction of an external source question cannot be called completion of original D25/LIFT or a native H0/B0 run.

## 6. Actual reproducible integer certificates and negative controls

A sibling Python standard-library exact checker independently calculates (i) each original \(a_k\) by a hypergeometric ratio and by integer binomial coefficients, (ii) each \(c_n\) by direct Le Lan \(f*g\) and by Euler/Clausen \(t*a\), (iii) the full \(E\) and only its Wilson wedge, and (iv) exact (A),(B),(C). It ran and passed at primes \(7,13,19,31,37,43,61,67,73,211,373\): **11 tested primes**, eight in the two target classes, three out-of-scope controls. Tests are finite regression, not a uniform proof.

At \(p=373\), with \(p^2=139129,\ p^3=51895117\):

- \(W_{373}\equiv373\pmod{p^3}\), \(S_{373}\equiv8,487,242=373+61\cdot373^2\pmod{p^3}\).
- \(E_{373}\equiv1,042,908=373\cdot2,796\pmod{p^3}\).
- \(T_{373}\equiv51,100,\ J_{373}\equiv94,928,\ A_{373}\equiv0\pmod{p^2}\).
- \(E_{373}/373\equiv185=-3/2\pmod{373}\).
- Joint check: \(2(S+E)=19,060,300=373\cdot51,100\pmod{p^3}\).
- **Noncommuting truncation witness:** \(S_{373}-W_{373}=61\cdot373^2\not\equiv0\bmod373^3\). Silently truncating the *infinite* analytic identity erases a real second-digit residual.
- **Necessary residue-class control:** at \(p=73\equiv1\bmod24\), \(E_{73}/73\equiv36\) while \(-3/2\equiv35\bmod73\). One must not generalize the target-class constant conjecture to every prime \(p\equiv1\bmod6\).

## 7. BRC / source / handoff classification

BRC resolution: **COMPOSE_APPLIED**, with original, jointly labeled ordered \((j,k)\) population, valuations, target residue-class labels, signed boundary and declared operation (finite Cauchy product, cutoff and exact division by p). Safe compression is **only** the complement of the Wilson wedge at first divided precision (p²), justified by valuation proof. For original LIFT modulo p³ the *full* E must stay. Auxiliary ring coordinates are not a replacement for P000's native Heartbeat X6 and separately typed time.

**Highest outstanding source evidence**: original same-class H0/B0 divided-power benchmark at p373 under existing https://github.com/awdawmip/enterprise-math/issues/1559 (PENDING_OWNER / NATIVE_NOT_EXECUTED), including real \([X]U\bmod139129\), native rank, Frobenius direction/eta, signed odd Green/Hesse, original kappa, Delta-R and independent validation. No surrogate here addresses that evidence. Preserve accepted D24 UR/CM0 and all Source contributor histories; do not repeat the completed WZ/Green, earlier weighted216 bands or E3 comparator guards.

**Next precise mathematical action on this alternative branch**: prove or refute finite-field wedge constant (D) in both target classes, with an exact source-based chain; using the route for LIFT also requires the *next* p-adic digits of E and S and genuine complexity reduction. **Next parent-native action**: lawful executor actually runs #1559. This separate author artifact has no Source Researcher write authority, registration, CLAIM/open, accepted Result, review, or freeze. Own prior continuation request onhour-20261027T1705-D25-exact-continuation was SUCCEEDED for read but execution_authorized=false; no replay or maintenance identity use.

References: Le Lan arXiv:2604.03327v1 (external published identity/explicit open conjecture); accepted D24 CM0/UR Source reports; 2026-10-26 original scalar source-port alignment (author/unreviewed); existing issue #1559 for the native object.