# D25 — leading coefficient of Sun cubic truncation defect

2026-11-04 Asia/Hong_Kong. TASK_RESEARCH author-side theorem. EXACT ALGEBRAIC PROOF / 166-PRIME EXACT CHECKED / GITHUB PUBLISHED / UNREVIEWED / NOT_ADMITTED. Continuation of the separately published Sun defect / Frobenius-order certificate; no native Source claim/run/checkpoint and no native H0/B0 experiment.

Frozen Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3. Research lane chatgpt-research-onhour-enterprise-math-20260923, never the maintenance lane.

## Explicit all-prime leading-boundary theorem

Let p>=5 be prime, alpha in Z_p, c_k=binom(alpha,k)binom(-1-alpha,k) and C=c_1=-alpha(1+alpha). Put
F(X)=sum_{k=0}^{p-1} c_k X^k,
H(t)=sum_{k=0}^{p-1} binom(2k,k)c_k t^k,
E(X)=[F(X)^2-H(X(1-X))]/p^2 mod p.

Sun's 2015 polynomial theorem establishes E in F_p[X]. The preceding exact Clausen-tail theorem establishes E=X^(p+1) Q modulo p.

**Theorem (universal leading defect).**
[X^(p+1)]E(X) = (2-6C)c_p (mod p).

Proof: write B_k=binom(2k,k), h_k=B_k c_k. By the exact infinite Clausen identity, the degree-(p+1) difference between the two truncated polynomials is precisely
D=(B_(p+1)-2)c_(p+1) - p B_p c_p - 2c_p c_1.
All coefficients are p-integral. For p>=5, Wolstenholme yields B_p=2 mod p^3, and the central-binomial recurrence gives
B_(p+1)-2 = 2+4p-4p^2 (mod p^3).
The hypergeometric recurrence gives
c_(p+1)/c_p = (p^2+p+C)/(p+1)^2
= C+p(1-2C)+p^2(3C-1) (mod p^3).
Substituting into D proves D=p^2(2-6C)c_p (mod p^3). Dividing by p^2 proves the theorem. No assumption on W-V is used.

For alpha=-1/3, C=2/9. For alpha=-1/4, C=3/16. In both cases c_p=C mod p for EVERY prime p>=5: the p-adic Lucas rule binom(alpha,p)=alpha_1 mod p uses the second p-adic digit alpha_1; for these two complementary rational parameter pairs and d=3 or 4, p≡+1 or -1 mod d causes their second digits to be either their original pair or the swapped pair. Therefore their product is alpha*(-1-alpha)=C.

Consequently, **for all primes p>=5**:
[X^(p+1)] E_216 = (2-6*(2/9))*(2/9) = 4/27 (mod p);
[X^(p+1)] E_2304 = (2-6*(3/16))*(3/16) = 21/128 (mod p).

These explicit constants are independent of the prime and are the actual first potentially surviving coefficients of the complete p^2 truncation defect. For the target p≡13,19 mod24, both are nonzero. The 216 defect is nonzero for every p>=5; the 2304 leading coefficient vanishes at p=7 but remains nonzero at every target prime. This is a polynomial-level boundary invariant, not a claim that its evaluated value or derivative cannot cancel with other coefficients.

## Independent verification

A separate Python integer checker extracts [X^(p+1)] directly from original truncated polynomial convolution:
sum_{i=2}^{p-1} c_i c_(p+1-i) -
sum_{k=ceil((p+1)/2)}^{p-1} (-1)^(p+1-k) binom(k,p+1-k) B_k c_k,
with coefficients modulo p^3. It does NOT call the just-proved omitted-tail formula and it checks both original 216 and 2304 coefficient families. All 166 primes 5<=p<=1000 passed, 332 checks, failures 0.
Sample (p,216-leading,2304-leading): (5,2,2), (7,3,0), (11,3,3), (13,4,9), (19,10,11), (97,72,57), (373,235,277), (997,74,117).

## Relevance to original D25 third-digit LIFT

Any proposed signed coefficientwise Clausen/WZ/Green transport for p^3 must reproduce both universal leading defect boundary constants 4/27 and 21/128 before specializing x_a,x_b. This is a precise falsifiable local criterion for future certificate construction. The full target W216-V2304=0 modp^3 and frozen Delta_p-R_p=0 modp are still open, as is the independent p373 native H0/B0 benchmark tracked in #1559. Preserve Frobenius evaluation after formal differentiation; the earlier exact third-digit four-term observer contains nonzero imaginary derivative parts that cancel only together with the defect.

Source references: Zhi-Hong Sun (2015), Note on super congruences modulo p², Thm 2.2, https://arxiv.org/abs/1503.03418; exact Clausen generating-series identity; classical Wolstenholme congruence. Prior author note: research_notes/portable_direct/20261104_onhour_d25_sun_cubic_defect_frobenius_order.md.

Next exact action: derive general [X^(p+2)] and a recurrence for E_a, E_b, then test whether a common signed differential operator cancels the two truncation corrections and original derivative moments, holding the two leading constants fixed. If no reduction results, return to frozen scalar Delta-R observer without imposing this auxiliary route as a gate.

Source status at 2026-11-04: em_status v0.6.11 research_authority_granted=false, CODE_UPGRADE_AVAILABLE; original continuation request onhour-d25-20261104-1702-continuation-read FAILED SOURCE_TREE_SIZE_LIMIT 20001/20000. Request not reissued; no role-bound write.