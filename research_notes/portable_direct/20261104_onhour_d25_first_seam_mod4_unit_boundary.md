# D25 — first quartic wall, exact mod-4 split and two-digit source certificate

Date: 2026-11-04, Asia/Hong_Kong. AUTHOR-SIDE PORTABLE RESEARCH / EXACT SCOPED ALGEBRA / FINITE EXACT CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.

Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT. Immutable publication TP2-B6F4FC938FF94941C1B7; scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3. Research logical lane: chatgpt-research-onhour-enterprise-math-20260923. Maintenance lane: chatgpt-hourly-enterprise-math-20260921 (not used).

## Exact original definitions and reuse
For a prime p>=5, set m=floor(p/4), L=m+1, M=(p+1)/2.
a_k=(2k)!(3k)!/((k!)^5*216^k),
b_k=(4k)!/((k!)^4*2304^k),
rho_k=(4k+1)(4k+2)(4k+3)/(576(k+1)^3).
The previously published exact two-seam Green theorem defines its first-wall flux E0*T0, with E0=rho_m(a_m-b_m) and
T0=sum_{n=L}^{M-1}(6n+1) prod_{i=L}^{n-1}rho_i.
This contribution is consumed from the earlier theorem, not re-claimed as a new Green theorem. All equalities below refer to the original rational coefficients in Z_(p), with no native-X6 interpretation.

## Theorem (exact first-wall split; all p>=5)
For p=4m+1,
rho_m/p=(p+1)(p+2)/(9(p+3)^3)=:lambda_1(p).
For p=4m+3,
rho_m/p=(p-2)(p-1)/(9(p+1)^3)=:lambda_3(p).
These are exact rational identities. Their two-digit expansions are
lambda_1(p)=(2+p)/243 (mod p^2), while
lambda_3(p)=2/9-p (mod p^2).
Consequently E0/p=lambda_delta(p)*(a_m-b_m) EXACTLY, and the existing first Green flux admits the exact p-adic reduction
E0*T0 = p*lambda_delta(p)*(a_m-b_m)*T0 (mod p^3).
Thus a_m,b_m,T0 are each needed only mod p^2, but the two p mod 4 classes genuinely have different transfer factors.

Proof: Substitute 4m=p-1 or 4m=p-3 into the original factorial ratio rho_m and use m+1=(p+3)/4 or (p+1)/4. Expand the resulting rational functions in Z_(p) to order p, using units 3,9,243. Multiply the exact expression for E0; the stated p^3 precision follows because a_m,b_m,T0 are p-integral.

## Lemma (single-binomial first-wall unit criterion)
Let R_p=a_m/b_m mod p; b_m is a p-unit. The original coefficient definitions give the exact rational ratio
a_m/b_m=(32/3)^m * binom(3m,m)/binom(4m,2m).
For p=4m+1, binom(4m,2m)=binom(p-1,2m)=1 (mod p). For p=4m+3, binom(4m,2m)=binom(p-3,2m)=-1/8 (mod p), by negative binomial reduction. Therefore:
R_p=(32/3)^m * binom(3m,m) (mod p) for p=1 (mod 4);
R_p=-8*(32/3)^m * binom(3m,m) (mod p) for p=3 (mod 4).
In particular,
E0/p=(2/243)*b_m*(R_p-1) (mod p) in the first class,
E0/p=(2/9)*b_m*(R_p-1) (mod p) in the second class.
As b_m and the prefactors are units, the exact criterion v_p(E0)>=2 is R_p=1 (mod p). This criterion is a test for exceptional first-wall suppression, not a universal claim that suppression occurs or does not occur.

## Exact finite computation and provenance
The accompanying standalone JavaScript BigInt checker uses the original independent a and b coefficient recurrences over Z/p^2, exact Euclidean inverses, a direct binomial quotient over F_p, and quartic tail T0. It checked all 301 primes 5<=p<=2000 (zero discrepancies) for lambda's p^2 expansion, the independent a/b binomial ratio and E0/p modulo p. Seven representative primes 5,7,11,13,19,97,373 were independently rebuilt from integer binomial coefficients (no recurrence in that crosscheck).

Original-source table (all entries E0/p and lambda modulo p^2; flux modulo p^3):

p | m | lambda | E0/p | T0 mod p | E0*T0
5 | 1 | 24 | 24 | 3 | 60
7 | 1 | 15 | 41 | 2 | 84
11 | 2 | 43 | 17 | 4 | 143
13 | 3 | 71 | 64 | 5 | 2132
19 | 4 | 262 | 2 | 3 | 1919
97 | 24 | 7667 | 6027 | 3 | 229599
373 | 93 | 84166 | 105683 | 355 | 23097652

No zero normalized first seam E0/p was observed among these 301 primes; this is finite evidence only. The flux numbers for 13,19,97,373 independently agree with the earlier two-seam author record. The theorem identifies an actual p mod 4 split matching the two target classes p=13,19 (mod 24) without presuming the still-open signed W216-V2304 cancellation.

## Continuation and evidence limits
Mother goal remains Delta_p-R_p=0 (mod p) for p=13,19 (mod 24), requiring original W216-V2304=0 (mod p^3) plus its frozen scalar bridge and the independent native fixed-p=373 H0/B0 divided-power execution. The next precise mathematical action is to pair this new explicit E0*T0 (including lambda's second digit) with zero-wall G0, second seam E1*T1 and quartic weighted moment, seeking a non-tautological terminal WZ/Clausen certificate. Test each signed provenance at p=13,19,97,373. Do not infer mathematical acceptance from GitHub storage; the native experiment in #1559 remains unexecuted and unassigned pending an eligible executor.

Original bridge request research-onhour-20261031-0205-dispatch-r15: issue awdawmip/kimi-query-bridge#6633 is COMPLETE/FAILED/UPSTREAM_CODE_REVIEW_REQUIRED. It was read rather than reissued. No new native Research session/CLAIM/run/Source checkpoint/Result is claimed. Three previously neutrally preserved staging files remain separate. BRC reuse classification COMPOSE_APPLIED: signed original two-family p-adic carriers and exact seam operations were retained, with future Green transfer and precision horizon p^3; no native-transfer assertion.
