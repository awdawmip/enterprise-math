# D25 — Original W216 shortened cutoff: exact three-band p³ repair

Date 2026-11-02 (+08:00). AUTHOR-DERIVED / HAND-PROVED / FINITE-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. This is portable mathematical evidence, not an authenticated original-class H0/B0 experiment.

Parent Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; immutable scientific source c47e13e4aba0e006366f989d6334d443f6333ae3. The mother goal remains Delta_p-R_p=0 mod p for p congruent 13 or 19 mod 24.

## Objects, original source and valuations

For every prime p=6r+1>=7, let h=floor(2p/3)=4r and let

\[
b_k=\frac{(1/2)_k(1/3)_k(2/3)_k}{2^k(k!)^3}
=\frac{\binom{2k}{k}^2\binom{3k}{k}}{216^k},\quad
W_p(4r)=\sum_{k=0}^{4r}(6k+1)b_k.
\]

The original ordered index population partitions into I0={0,...,2r}, I1={2r+1,...,3r}, I2={3r+1,...,4r}; the exact p-adic valuations of b_k on these bands are 0,1,2, respectively.

The p-unit rational carriers, keeping all factorial indices and signs, are

\[
T_{0,k}=(-1)^k2^{-k}\binom{3r}{k}\binom{2r}{k}\binom{4r}{k},\quad k\in I_0;
\]
\[
T_{1,k}=\frac{(2r)!(k-2r-1)!(3r)!(4r)!}{3\,2^k(k!)^3(3r-k)!(4r-k)!},\quad k\in I_1;
\]
\[
T_{2,k}=\frac{(-1)^{r+k}(3r)!(k-3r-1)!(2r)!(k-2r-1)!(4r)!}{6\,2^k(k!)^3(4r-k)!},\quad k\in I_2.
\]

For k in I0, let the multiset of p-unit reciprocal factors for 0<=j<k be

\[
\mathcal A_k=\bigcup_{j=0}^{k-1}
\left\{\frac1{2(j-3r)},\ \frac1{3(j-2r)},\ \frac2{3(j-4r)}\right\}.
\]
\[
L_{0,k}=\sum_{a\in\mathcal A_k}a,\qquad
Q_{0,k}=\frac{L_{0,k}^2-\sum_{a\in\mathcal A_k}a^2}{2}.
\]

For k in I1 put

\[
L_{1,k}=\frac12\sum_{0\le j<k}\frac1{j-3r}
+\frac13\sum_{\substack{0\le j<k\\j\ne2r}}\frac1{j-2r}
+\frac23\sum_{0\le j<k}\frac1{j-4r}.
\]

All denominators above are prime to p; the coefficient denominator 2^k(k!)^3 is also a p-unit.

## Theorem 1: exact original-source three-band p³ expansion

For all these primes and all indices 0<=k<=4r, in the p-local rational ring,

\[
\boxed{
b_k\equiv
\begin{cases}
T_{0,k}(1+pL_{0,k}+p^2Q_{0,k}) & k\in I_0,\\
pT_{1,k}(1+pL_{1,k}) & k\in I_1,\\
p^2T_{2,k} & k\in I_2
\end{cases}\pmod{p^3}.}
\]

Proof. Substitute the exact rational identities
(1/2)=-3r+p/2, (1/3)=-2r+p/3, (2/3)=-4r+2p/3
into the three original finite Pochhammer products. The index j=2r first contributes a single p/3, the index j=3r next contributes a single p/2; j=4r is excluded by k<=4r. Extract only these explicit factors. The remaining products of negative integers evaluate with their signs and factorial endpoints exactly to T0,T1,T2. Every remaining factor is a p-unit. The finite product on I0 expands to 1+pL0+p²Q0, on I1 to 1+pL1 after restoring the first p, and on I2 to 1 after restoring p². All discarded terms vanish mod p³. The formula and exact valuation tiers follow. QED.

## Theorem 2: signed six-port carry reduction

Define
\[
S_0=\sum_{k\in I_0}(6k+1)T_{0,k},
\]
\[
S_1=\sum_{k\in I_0}(6k+1)T_{0,k}L_{0,k}
+\sum_{k\in I_1}(6k+1)T_{1,k},
\]
\[
S_2=\sum_{k\in I_0}(6k+1)T_{0,k}Q_{0,k}
+\sum_{k\in I_1}(6k+1)T_{1,k}L_{1,k}
+\sum_{k\in I_2}(6k+1)T_{2,k}.
\]

Then for every stated prime

\[
\boxed{W_p(4r)\equiv S_0+pS_1+p^2S_2\pmod{p^3}.}
\]

This is Theorem 1 summed against the exact unchanged original weight (6k+1). Thus the remaining candidate W_p(4r)=p mod p³ is equivalent to three carry obligations:

\[
S_0=0\pmod p,\quad S_0+pS_1=p\pmod{p^2},\quad
\frac{S_0+pS_1-p}{p^2}+S_2=0\pmod p.
\]

The quotient is p-integral under the preceding second obligation. The general vanishing statements are open proof targets; this reduction is proved without assuming them.

## Exact finite tests and BRC information witness

The accompanying independently executed Python standard-library checker computes the original b_k by the recurrence b_{k+1}/b_k=(2k+1)(3k+1)(3k+2)/(36(k+1)^3), and separately computes all three band carriers and deformation ports. Every prime p≡1 mod6, 7<=p<=3000 (207 primes) passed each band-level equality, full reconstruction, and the separate finite candidate W_p(4r)=p mod p³ check. For eight selected primes, additional exact integer-binomial coefficient checks were performed at band endpoints. No float operations.

Original signed band outputs mod p³:
- p=13: I0=780, I1=1937, I2=1690; total 13.
- p=19: I0=5662, I1=4826, I2=3249; total 19.
- p=373: I0=28094360, I1=38687933, I2=37008314; total 373 modulo 51895117.

At p=373, in base-373 low/middle/upper digits, the three source bands respectively are (0,347,201), (0,27,278), (0,0,266). At first nonzero place 347+27=374=1+373, so the carry is 1. At the next place 201+278+266+1=746=2·373. The full sum is 373 modulo 373³. Dropping the upper source port changes the original future mod p³ readout by exactly 373²·266. This is a source-typed BRC information-loss certificate, not a native-world experiment.

At p=373, S0=15521276, S1=16326002, S2=13625450 modulo p³; the second-stage carry (S0+373·S1-373)/373²=240 mod373, S2=133 mod373, and 240+133=373. This explicitly checks both the exact six-port formula and the observer's final carry.

## Inheritance and next proof unit

Reused rather than renaming: existing original W216 p⁴/p⁵ high tail reversal, accepted D24 CM0, Clausen and Cauchy/Picard–Fuchs interfaces. The current deliverable concerns precisely the original shortened-cutoff *lower, middle and upper* bands. BRC reuse classification: COMPOSE_APPLIED (valuation provenance, ordered signed six-port carrier and future mod p³ observer). This is p-adic scalar arithmetic, not a new native spatial axis or a Source-authorized experiment.

Next: establish a terminating/WZ or creative-telescoping certificate for the first and second carry congruences, then the third; start with exact p=13,19,373 controls. A theorem for the distinct 2304 hypergeometric coefficient is not in itself the original 216 theorem. Native fixed-p373 H0/B0 divided-power [X]U, Frobenius direction, odd Green/Hesse/kappa remain NOT_EXECUTED, PENDING_OWNER in existing support issue 1559.

Research lane status as of 2026-11-02 13:26Z: Gateway v0.6.11, UPSTREAM_CODE_REVIEW_REQUIRED, research_authority_granted=false, executor_binding_configured=false, active jobs 5/5. Historical read-only recovery #6637 and failed continuation #6638 are preserved as original receipts; no new CLAIM, OPEN, Source checkpoint, Result or acceptance is asserted. Existing control support issue 1558. Fixed logical conversation identifier per user: chatgpt-research-hourly-enterprise-math-20260923, kept distinct from maintenance lane. Scheduler and notification settings unchanged.
