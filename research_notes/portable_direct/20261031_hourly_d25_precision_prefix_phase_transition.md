# D25/LIFT — sharp precision-dependent original-216 polynomial prefixes

2026-10-31 Asia/Hong_Kong, second portable author-side mathematical unit of the hourly TASK_RESEARCH lane chatgpt-research-hourly-enterprise-math-20260923. Distinct from maintenance conversation. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7, unchanged frozen scientific Source c47e13e4aba0e006366f989d6334d443f6333ae3; P000 ACTIVE_LOCKED. External p-adic arithmetic, AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.

## Theorem — exact precision-to-prefix table for every prime p>=5

For the original weighted-216 polynomial

\[
F_p(X)=\sum_{n=0}^{p-1} (6n+1)
\frac{\binom{2n}{n}^{2}\binom{3n}{n}}{216^n}\,X^n
\in\mathbf Z_{(p)}[X],
\]

let q_k be the **minimum** nonnegative index for which the initial prefix through n=q_k equals the full polynomial coefficientwise modulo p^k. Then, for k=1,...,6:

| precision | sharp index q_k, p>=7 | exceptional p=5 |
| --- | --- | --- |
| p^1 | floor((p-1)/3) | 1 |
| p^2 | floor((p-1)/2) | 2 |
| p^3 | floor(2p/3) | 3 |
| p^4 | p-1 | 3 |
| p^5 | p-1 | 3 |
| p^6 | p-1 | 4 |

In particular **a coefficientwise p^3 prefix saves approximately one-third of the terms, but there is no proper p^4 prefix for p>=7**. At the exceptional prime 5, the final coefficient carries *five* factors of 5 and can be omitted through precision p^5, but not p^6.

### Complete proof

Write a_n=(2n)!(3n)!/((n!)^5 216^n). Legendre gives v_p(a_n)=floor(2n/p)+floor(3n/p) for every 0<=n<p and every prime p>=5. The true weighted coefficient valuation is e_p(n)=v_p(a_n)+v_p(6n+1).

For k=1: the last valuation-zero coefficient is n=floor((p-1)/3); it is a p-unit because 6n+1 is either 2p-1 or 2p-3 depending on p mod3 (p>=5). All later terms have a_n divisible by p.

For k=2: the last coefficient with valuation below two is n=(p-1)/2 (p is odd), where v_p(a_n)=1 and 6n+1=3p-2 is a p-unit. Every later coefficient has valuation at least two.

For k=3: the last coefficient with valuation below three is n=floor(2p/3), where the two floor terms each equal 1, and 6n+1 is a p-unit: for p=6m+1 it equals 4p-3, and for p=6m+5 it equals 4p-1. Every higher coefficient has valuation at least three.

For k=4,5,6: at n=p-1, v_p(a_{p-1})=floor(2(p-1)/p)+floor(3(p-1)/p)=3; the weight is 6p-5. For any p>=7 this is a p-unit, hence the final coefficient has valuation exactly three. It is nonzero at **all** precisions p^k with k>=4: no shorter initial prefix is possible. For p=5 the final coefficient has valuation 3+v_5(25)=5, so it vanishes mod p^4 and p^5 but not mod p^6; the penultimate coefficient n=3 has valuation exactly two. Thus q_4=q_5=3 and q_6=4. All table cases follow. QED.

The k=3 target class was proved earlier (GH-172); here it is reused and extended to a **complete uniform precision filtration** including all primes p=5(mod6) and the exceptional 5-adic endpoint. The prior result that a selected scalar value at X=1 can lose tail data by cancellation remains distinct from this full **polynomial observer** bound.

## Executed precise regression and next frozen target

The accompanying Python standard-library checker enumerated all 1436 primes 5<=p<12000; verified 8616 exact (prime, precision) sharp-prefix endpoints using valuation arithmetic. For 11 anchors, independently built original integer-binomial numerators and directly checked each coefficient's divisibility modulo p^k for all k=1,...,6. Returned PASS_D25_ALL_PRIME_SHARP_PRECISION_PREFIX_FILTRATION. This finite validation checks implementation; the proof above establishes universal scope.

Examples: p373 gives q=(124,186,248,372,372,372); p5 gives (1,2,3,3,3,4). The semilinear Frobenius, H0/B0 and divided-power native experiments were NOT executed.

Use this precision/readout bound in BRC only as external arithmetic: retain (original coefficient, prime, weight, valuation wall, observer type, truncation, target precision, source) when compressing. Do not promote this to native P000 X6 geometry. The real frozen next mathematics remains a complete signed proof C+L-J+I=0 (mod p) for p mod24={13,19}; no finite scan or prefix lemma proves it. The historical own Source recovery issues awdawmip/kimi-query-bridge#6424/#6425 did not grant a winning claim, authorized run or Source checkpoint; control support #1558 and native experiment #1559 retain responsibility. No new native registration, CLAIM, OPEN, freeze, review or Result is asserted. Source pin and original task unchanged.
