# D25 — original W216 shortened cutoff: all-order three-band precision tower

Date: 2026-11-02 (+08). **AUTHOR-DERIVED / HAND-PROVED / FINITE-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING**.

Mother Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; immutable publication TP2-B6F4FC938FF94941C1B7; frozen scientific commit c47e13e4aba0e006366f989d6334d443f6333ae3. Mother objective remains Delta_p-R_p = 0 mod p for p congruent 13,19 modulo 24. Native p=373 H0/B0 remains pending in #1559. No native CLAIM, OPEN, Source checkpoint, Result or mathematical acceptance follows from this author-side file.

## Question and previously established frontier

Earlier D25 manuscript 20261102_r11_d25_w216_three_band_p3_proof.md established the six source-tagged ports modulo p^3; the CM0 bridge 20261102_r11_d25_w216_cm0_second_carry_bridge.md reduced the still-open all-target second carry to

\[
12gj+[(1+6\theta)R_A](1/2)\equiv1\pmod p.
\]

This work constructs a **precision-uniform source transport** for the same original shortened 216 sum. The distinct original full upper-tail p^5 reflection and accepted CM0/Clausen results are inherited, not re-proved. This result does not discharge the open second-carry congruence.

## Theorem 1: exact indexed rational factorization

Let p=6r+1>=7 be prime. Keep the original coefficients, sign and cutoff:

\[
b_k=\frac{(1/2)_k(1/3)_k(2/3)_k}{2^k(k!)^3}
=\frac{\binom{2k}{k}^2\binom{3k}{k}}{216^k},\quad
W_p(4r)=\sum_{k=0}^{4r}(6k+1)b_k.
\]

Label the three original parameters by

\[
\mathcal A=\{(a,n)=(\tfrac12,3r),(\tfrac13,2r),(\tfrac23,4r)\},\qquad a=-n+pa.
\]

For 0<=k<=4r define v_k=sum_(a,n) 1_(n<k) = 1_(k>2r)+1_(k>3r), and

\[
U_k=\frac{\prod_{(a,n):n<k}a}{2^k(k!)^3}
\prod_{(a,n)\in\mathcal A}\prod_{\substack{0\le j<k\\j\ne n}}(j-n).
\]

Retain a tagged multiset (with duplicate factors counted separately)

\[
X_k=\{a/(j-n):(a,n)\in\mathcal A,\;0\le j<k,\;j\ne n\},
\]

and let e_t(k) be its elementary symmetric polynomial of degree t, e_0(k)=1. The following is an **exact rational identity**:

\[
\boxed{b_k=p^{v_k}U_k\sum_{t\ge0}p^t e_t(k).}\tag{1}
\]

Proof: each original Pochhammer factor j+a=j-n+pa is pa when j=n, otherwise (j-n)(1+pa/(j-n)). Multiply the factors without dropping the parameter identity or index. In this range n=4r is never crossed. All denominators in U_k and e_t(k) are prime to p and U_k is a p-adic unit. QED.

## Theorem 2: all finite p-adic precision q>=3

Define bands I_0={0,...,2r}, I_1={2r+1,...,3r}, I_2={3r+1,...,4r} and their source-tagged signed ports

\[
C_{v,t}=\sum_{k\in I_v}(6k+1)U_ke_t(k).
\]

For **every integer q>=3**, including q>=p, one has

\[
\boxed{
W_p(4r)\equiv
\sum_{v=0}^2\sum_{t=0}^{q-1-v}p^{v+t}C_{v,t}
\pmod{p^q}.}\tag{2}
\]

Proof: truncate the exact (1) after v+t<q, multiply by the original signed weight and sum over the exact partition. This preserves valuations and individual deformation sources. There are 3q-3 **sufficient**, explicitly typed ports: q from I_0, q-1 from I_1, q-2 from I_2. No minimality claim is made. The equality is valid across q>=p since elementary-symmetric extraction introduces no division by t or t!. QED.

The q=3 ports coincide with the existing six classes. The q=4 formula has nine:
I_0 needs e_0,e_1,e_2,e_3; I_1 needs e_0,e_1,e_2; I_2 needs e_0,e_1.
The three additional fourth-digit sources are (v,t)=(0,3),(1,2),(2,1), each weighted by p^3. Previous six port values must themselves be retained to the enhanced precision when reused.

## Theorem 3: uniform incremental computation law

Let E_k(X)=sum_t e_t(k)X^t, with U_0=1, E_0(X)=1, v_0=0. Appending the original j=k factors gives, for k<4r,

\[
U_{k+1}=\frac{U_k}{2(k+1)^3}\prod_{(a,n)\in\mathcal A}
\begin{cases}a,&k=n,\\k-n,&k\ne n,\end{cases}
\]

\[
v_{k+1}=v_k+\sum_{(a,n)}{\bf1}_{k=n},\qquad
E_{k+1}(X)=E_k(X)\prod_{(a,n):k\ne n}
(1+Xa/(k-n)).\tag{3}
\]

This is exact by the same factorization as (1). Truncate E at degree q-1 and compute in Z/(p^q). The algorithm uses O(qp) modular ring operations and O(p) p-unit inversions for a single p,q; bit complexity also depends on the q log(p) modulus length. It does not use Newton-sum divisions by t, including at q>=p. This is a reusable source-preserving precision lift, not a new native-world physical operator.

## Exact program evidence and BRC information loss

Two separately coded paths were actually run: (A) the original W216 coefficient recurrence b_(k+1)/b_k=(2k+1)(3k+1)(3k+2)/(36(k+1)^3), and (B) the tagged recurrence (3), e_t and full port reconstruction (2). All **207 primes 7<=p<=3000 with p=1 mod 6** passed the q=4 comparison, zero discrepancies. Additional exact checks q=3,4,5,7,14 include (p=7,q=7) and (p=13,q=14). Eight selected primes had 46 independent original integer-binomial coefficient checks at the band boundary indices. No floating arithmetic.

For p=373, independently computed original and port outputs:

\[
\boxed{W_{373}(248)\equiv373+323\cdot373^3\pmod{373^4},}
\]
\[
\boxed{W_{373}(248)\equiv373+323\cdot373^3+230\cdot373^4
\pmod{373^5}.}
\]

The computed digits 323 and 230 are exact **finite instances** and not general congruences. Other q=4 fourth-digit coefficients ((W-p)/p^3) mod p: p=7:2, 13:4, 19:8, 37:30, 43:32, 1171:75. The previous W=p modp^3 finite checks are not new proof credit.

At p=373, the three newly required port residues are

\[
C_{0,3}=343,\quad C_{1,2}=117,\quad C_{2,1}=323\pmod{373}.
\]

Their new q=4 contribution is 373^3(343+117+323) = 37*373^3 mod 373^4. Omitting these original-source deformations changes the fourth-digit readout by 37; this is a BRC information-loss witness with carrier (original k, coefficient and sign, valuation band, parameter tags, e_t), permitted future operation precision lifting, and observed W modulo p^q. It is about signed p-adic arithmetic rather than positive-mass BRC.

Reproducible complete author-side executable and actual JSON log: d25_w216_precision_tower_20261102.py and d25_w216_precision_tower_20261102_results.json.

## Continuation

The next unresolved scientific unit is the all-target second-carry identity

\[
12gj+[(1+6\theta)R_A](1/2)\equiv1\pmod p,\qquad p=13,19\bmod24.
\]

Seek a genuinely matching terminating hypergeometric/WZ/contiguous or cited theorem certificate. After that, investigate third-carry cancellation using the inherited signed six-port interface or the exact present precision tower. Preserve P000/ACTIVE worldview and original frozen source, contribution provenance, native experiment #1559 and control support #1558.

At 2026-11-02 status read: gateway 0.6.11, source_sync.control.state=CODE_REVIEW_REQUIRED, error UPSTREAM_CODE_REVIEW_REQUIRED, research_authority_granted=false, executor_binding_configured=false, active jobs 5/5. Historical control request states cannot establish a current authorized run. Research logical lane chatgpt-research-hourly-enterprise-math-20260923 remains separate from maintenance chatgpt-hourly-enterprise-math-20260921. This file is an author-side GitHub evidence artifact only; REGISTER_PENDING and native Source checkpoint pending.