# D25 — Euler–Clausen square-root exceptional port and exact second-digit repair

Date: 2026-10-31 Asia/Hong_Kong. Classification: AUTHOR-SIDE / PROVED RATIONAL-COEFFICIENT THEOREM / EXECUTED EXACT MODULAR CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING.
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7.
Own logical lane: chatgpt-research-onhour-enterprise-math-20260923, distinct from maintenance lane. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3.
This document is a new author-side, source-preserving mathematical discriminator for the original 216 LIFT. It does not request or assert Source CLAIM/run, H0/B0 experiment, Result or independent approval.

## Consumed mother question and external identity

The target stays the original weighted 216 sum for p=6m+1, p congruent to 13 or 19 modulo 24:

$$A_p=\sum_{n=0}^{p-1}(6n+1)a_n,\qquad
a_n=\frac{\binom{2n}{n}^{2}\binom{3n}{n}}{216^n},\qquad
A_p\stackrel{?}{\equiv}p\pmod{p^3}.$$

The previously verified author-side five-port signed reflection reduction, three-valuation Gauss harmonic jet, and exact Green contact representation are consumed, not re-proved. The frozen observer R_p, its source indices, and the original H0/B0 experimental demand remain unchanged.

Use the *classical* Clausen and Euler hypergeometric identities in their exact formal-power-series scope:

$$G(z)={}_2F_1(\tfrac16,\tfrac13;1;z),\quad
H(z)={}_2F_1(\tfrac56,\tfrac23;1;z),\quad
E(z)=(1-z)^{1/2},$$

$$ {}_3F_2(\tfrac12,\tfrac13,\tfrac23;1,1;z)
=G(z)^2=E(z)G(z)H(z). \tag{1} $$

Here G=EH is Euler's transformation, and G² is Clausen's identity. Both are classical external mathematics, not a new project theorem. Published references: Euler transformation https://mathworld.wolfram.com/EulersHypergeometricTransformations.html ; Clausen identity https://en.wikipedia.org/wiki/Clausen%27s_formula . The mathematical increment below is the *p-local finite-truncation boundary*, not discovery of (1).

Write g_k=(1/6)_k(1/3)_k/(k!)², h_l=(5/6)_l(2/3)_l/(l!)² and e_j=(-1)^j binom(1/2,j).
For each n>=0, the following is an exact rational coefficient identity:

$$\frac{(\frac12)_n(\frac13)_n(\frac23)_n}{(n!)^3}
=\sum_{j+k+l=n} e_jg_kh_l. \tag{2}$$

Consequently, with original indices and original weight preserved:

$$A_p=\sum_{\substack{j,k,l\ge0\\j+k+l<p}}
(6(j+k+l)+1)\,2^{-(j+k+l)}e_jg_kh_l. \tag{3}$$

This is an exact finite identity (not a p-adic approximation). The three-coordinate labels j,k,l are Cauchy/source indices, not additional native X6 axes.

## Theorem 1 — all-prime square-root coefficient valuation and p³ normalization

For every prime p>=5, put j_0=(p+1)/2 and s=(-1)^{j_0}. For e_j as above, and 0<=j<p:

- v_p(e_j)=0 for 0<=j<=j_0.
- v_p(e_j)=1 for j_0+1<=j<=p-1, **without exceptions**.
- e_{j_0} is a p-adic unit with exact rational product

$$e_{j_0}=s\prod_{r=1}^{j_0}\Big(1-\frac{p}{2r}\Big). \tag{4}$$

In p-local rational arithmetic, setting H=H_{j_0}, H^{(2)}=H_{j_0}^{(2)}, the full coefficient needed modulo p³ is

$$e_{j_0}\equiv
s\left[1-\frac p2H+\frac{p^2}{8}(H^2-H^{(2)})\right]\pmod{p^3}. \tag{5}$$

For 0<=r<=(p-5)/2, every normalized upper coefficient satisfies the **exact** rational identity

$$\frac{e_{j_0+1+r}}p=
\frac{e_{j_0}}{p+3}
\prod_{t=1}^{r}\frac{p+2t}{p+2t+3}. \tag{6}$$

Define P_r=prod_{t=1}^r 2t/(2t+3)=r!/(5/2)_r and
D_r=-H/2-1/3+sum_{t=1}^r(1/(2t)-1/(2t+3)).
All displayed denominators are p-units in the stated ranges. Then the explicit second-digit port repair is

$$\frac{e_{j_0+1+r}}p
\equiv \frac{s}{3}P_r\,(1+pD_r)\pmod{p^2}. \tag{7}$$

Proof: e_{j+1}/e_j=(2j-1)/(2j+2). Since 1/2=j_0-p/2, direct reindexing of binom(1/2,j_0) gives (4). Its elementary symmetric expansion gives (5). The first high recurrence ratio equals p/(p+3); all later ratios give (6). Expand the p-unit factors to first order for (7). The single vanishing numerator p is present exactly once for each j>j_0, while j! has no p factor for j<p, establishing the valuations. No floating-point or fitted signs enter this proof.

**Scientific consequence:** In the finite Euler–Clausen representation (3), the square-root factor has three original-index ports: 0<=j<j_0 (units), the *exceptional unit* j=j_0, and j>j_0 (exact p-valuation one). Removing the exceptional port is already invalid modulo p; removing the third port is generally invalid modulo p²/p³.

## Theorem 2 — explicit exceptional double-source witness

For p=6m+1, j_0=3m+1, the exceptional port of (3) is

$$P_p=
e_{j_0}\,2^{-j_0}
\sum_{t=0}^{3m-1}(6(j_0+t)+1)2^{-t}
\sum_{k+l=t}g_kh_l. \tag{8}$$

Because 1/6=-m+p/6, 1/3=-2m+p/3, 5/6=-5m+5p/6, 2/3=-4m+2p/3, we have modulo p, for every index <p,

$$g_k\equiv {m\choose k}{2m\choose k},\qquad
h_l\equiv {5m\choose l}{4m\choose l}.$$

Thus the **exact finite-field source certificate** is

$$\boxed{P_p\equiv s\,2^{-(3m+1)}
\sum_{t=0}^{3m-1}(6t+4)2^{-t}
\sum_{k=0}^{t}{m\choose k}{2m\choose k}
{5m\choose t-k}{4m\choose t-k}\pmod p.} \tag{9}$$

This is a source-labeled (j_0,k,l) equality; total-only contraction may be used to test A_p but does not license deleting labels for future operators. The prior frozen R_p and Gauss high-tail F_p are different observers. A numerical coincidence at p=373 between P_373 and R_373 is **not** a general identity (P_13=5 while R_13=0).

If one naively discards e_j for j>(p-1)/2 (that is, removes j_0 and every higher term), then (2)/(3) lose the nonzero P_p modulo p; the later port is 0 modulo p. Already at the two smallest frozen primes p=13 and p=19, that naive finite transformation fails even the known necessary A_p=0 (mod p). This is a proved fixed-prime counterexample to that **specific truncation method**, not a counterexample to the original LIFT.

## Actually executed independent exact checks

Executed Python standard-library file d25_euler_sqrt_boundary_guard_20261031.py. Its arithmetic uses modular inverses in Z/p³, integer binomial coefficients, exact convolutions, and no approximations or external H0/B0 engine.

- All 60 target primes 13<=p<1500: checked the exact valuation split, formulas (5) and (7) for every displayed j/r, and evaluated (9). Every exceptional P_p in this **finite range** is nonzero; no infinite-class nonvanishing conclusion is asserted.
- Primes p=13,19,37,43,61,67,373: independently calculated the original binomial A_p and the complete three-factor Cauchy convolution (3) modulo p³, verifying equality and both additional source decompositions.
- Distinct modular binomial convolution verifies (9) independently of the rational Pochhammer recurrence.

| p | j_0 | e_{j_0} mod p | P_p mod p | incorrect j<j_0 total mod p | high j>j_0 divided by p mod p | A_p mod p³ |
|---:|---:|---:|---:|---:|---:|---:|
| 13 | 7 | 12 | 5 | 8 | 7 | 13 |
| 19 | 10 | 1 | 4 | 15 | 0 | 19 |
| 37 | 19 | 36 | 26 | 11 | 24 | 37 |
| 43 | 22 | 1 | 32 | 11 | 38 | 43 |
| 61 | 31 | 60 | 40 | 21 | 9 | 61 |
| 67 | 34 | 1 | 35 | 32 | 61 | 67 |
| 373 | 187 | 372 | 196 | 177 | 132 | 373 |

In particular, at the fixed numerical benchmark p=373, dropping the exceptional j=187 yields 177 mod373 instead of 0, and dropping the high p-valued j>187 loses normalized contribution 132 mod373. The total original 216 value is 373 modulo 373³. These are *external scalar checks*, not native fixed original-class H0/B0 data.

## BRC / observer and next scientific dependency

BRC COMPOSE_APPLIED: carrier = (p, j,k,l, e_j,g_k,h_l, original weight 6(j+k+l)+1, p-valuation and signed rational coefficient); observation = original complete weighted 216 sum; allowed future operations include first/second p-adic digit extraction and source-dependent pairing. The quotient by n=j+k+l is safe only for the specified final weighted sum, not for arbitrary future source-wise operations. This is a rational/signed arithmetic observer, not positive-mass BRC and not an independent X6/H0/B0 realization.

New exact action if the ordinary author-side mathematical route is continued: use (5)-(9) to derive and test a **single coupled cancellation certificate between the three Euler ports** of (3), with the existing signed five-port R_p observer retained as an independent readout. The check must terminate at A_p=p mod p³ on both frozen prime classes; additional equivalent parametrizations alone are not completion. The present note supplies an explicit counterexample to a specific naïve Cauchy-truncation method and a complete p³ coefficient correction.

The higher-priority independent native obligation remains unchanged: issue https://github.com/awdawmip/enterprise-math/issues/1559 , fixed original H0/B0 divided-power p=373 [X]U mod139129, actual module rank, authentic semilinear Frobenius/eta and operator, signed Green/Hesse, kappa, Delta-R and independent reproduction. As of the 2026-10-30T16:55Z read it is OPEN/PENDING_OWNER/NOT_EXECUTED. Responsible path is the canonical Source Task owner or authorized native implementation maintainer, with no confirmed executor; next action is binding an authorized actual native host and the exact benchmark without changing the object.

At that same observed time Sites EM 0.6.11 reports research_authority_granted=false, write_relay_enabled=false, source control CODE_REVIEW_REQUIRED and active native-job quota full. Own research-lane bridge historical recovery is issue #6581, earlier #6582 was explicitly rejected; these are not present Source CLAIM/run. A separate approved Site-bound backend client and securely supplied credential are required before role-bound writes. Research lane identity and immutable scientific pin are preserved; no Source session/CLAIM/Result, review or formal checkpoint is asserted by this author-side note.