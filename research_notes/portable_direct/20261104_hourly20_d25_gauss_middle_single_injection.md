# D25 — A single boundary injection controls the complete middle p-adic Gauss band

Date: 2026-11-04 (+08). Scope: TASK_RESEARCH author-side portable derivation, UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. This is neither a native CLAIM nor a Source checkpoint. Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication: TP2-B6F4FC938FF94941C1B7; frozen scientific pin: c47e13e4aba0e006366f989d6334d443f6333ae3. Research lane requested identity: chatgpt-research-hourly-enterprise-math-20260923 (not maintenance). Predecessor author note: 20261104_hourly20_d25_unified_euler_original_gauss_carry.md at 10cb2e6abc7a5d29f053f970397d712dd758d10a.

## Question and exact carrier

Can the unified second-digit carry recurrence be compressed *without losing the individual p-adic source bands*? The answer is yes for the middle-band coefficients, with a completely explicit one-boundary injection, independent of the earlier low-band carry coefficients. The reduction applies to exact coefficient and first-weighted-derivative observations modulo p²; it does not assert root-class vanishing or a p³ comparison.

Fix a prime p>=5, p=8q+5 or p=8q+7. Set the source integer parameters and h exactly as in the predecessor:
- p=8q+5: (a,b,c,d,h)=(5q+3,7q+4,q,3q+1,4q+3).
- p=8q+7: (a,b,c,d,h)=(7q+6,5q+4,3q+2,q,4q+4).

Write L=min(a,b)=h+q, R=max(a,b), D=max(c,d); thus 0<=L<R<p. Let J(z)=sum_{j=0}^q binom(c,j)binom(d,j)z^j and B(z)=(1-z)^h J(z). Let F_p(z)=sum_{k=0}^{p-1} f_k z^k, f_k=(1/8)_k(3/8)_k/(k!)². As previously proved, F_p=B+pC modulo p² coefficientwise, with C_0=0 and
(k+1)² C_{k+1}-(k-a)(k-b)C_k = h w_k+(3k/2+mu)B_k mod p,
where w_k=sum_{j=0}^k B_j, mu=11/32 for p mod8=5, mu=13/32 for p mod8=7.

## New theorem: exact boundary transfer and middle support

Define epsilon=+1 when p mod8=5 and epsilon=-1 when p mod8=7, and define in F_p
S_p = (epsilon*5/32) * [(-1)^h binom(D,q)] / (L+1)².
Then the entire second-digit carry in the middle band is explicitly
C_{L+1+s} = S_p * (1)_s * (1-(R-L))_s / ((L+2)_s)² mod p,
for 0<=s<R-L. All rational denominators displayed here are p-units. Moreover C_k=0 modulo p for R<k<p. Equivalently
C_middle(z)=S_p z^(L+1) sum_{s=0}^{R-L-1} [(1)_s (1-(R-L))_s / ((L+2)_s)²] z^s
and the coefficientwise reconstruction is
F_p(z) = B(z)+p C_low(z)+p C_middle(z) mod p²,
where C_low=sum_{k=1}^L C_k z^k. The polynomial middle sum is terminating and can be written as a 3F2 with numerator (1,1,1-(R-L)), denominator (L+2,L+2). This is an equality of truncated polynomials in Z/(p²)[z], not an infinite-hypergeometric identity.

For every selected prime p>=11, S_p and every C_{L+1},...,C_R are nonzero in F_p. Consequently the *original* coefficients satisfy v_p(f_k)=1 exactly for L<k<=R and v_p(f_k)>=2 for R<k<p. At p=5, S_p=0, and the p=5 exception is kept rather than silently promoted to the generic exact-one-valuation claim.

For the Gauss observers at z0=1/9, both F_p(z0) and G_p(z0)=(1+16z d/dz)F_p(z0) are recovered by adding the low-band contribution and the displayed middle contribution. The middle weighted contribution is obtained by multiplying the s-th summand by 1+16(L+1+s). The single injection S_p replaces all middle-band propagation data, but does not erase low-band contributions or p³/source provenance; the two channels remain typed.

## Proof

The polynomial B has degree L, and B(1)=0 because h>0. Hence, in F_p, B_k=0 for k>L and w_k=0 for k>=L. At k=L one of (L-a),(L-b) is zero; therefore the recurrence forgets the prior C_L and yields C_{L+1}=(3L/2+mu)B_L/(L+1)². The leading coefficient B_L is (-1)^h binom(D,q); substituting L=-1/8 mod p for p mod8=5, or L=-3/8 mod p for p mod8=7, gives (3L/2+mu)=epsilon*5/32. This proves the claimed S_p.

For each L+1<=k<R the forcing vanishes, so the recurrence is homogeneous; the consecutive multipliers are (k-L)(k-R)/(k+1)². Multiplying these factors gives the rising-factorial expression. At k=R one numerator multiplier is zero and the forcing is zero, giving C_{R+1}=0. Later recurrence forces every subsequent C_k=0. All denominators are units since k+1<p for the recurrences used. Since D<p, binom(D,q) is a p-unit, and for p>=11 the factor 5 is a unit; in the middle recurrence the numerator factors never vanish until k=R. Thus S_p and all middle C coefficients are units. B_k=0 there, so f_k/p=C_k mod p, proving exact first-order valuations. After R, B_k=C_k=0, so f_k=0 mod p². All statements are valid at p=7; p=5 retains the special zero injection.

## Exact executable evidence, BRC interface, and next action

A separate Python standard-library script builds each original Pochhammer coefficient f_k modulo p² *independently* of C, constructs B with integer binomial coefficients, extracts (f_k-B_k)/p, and checks the seed, every middle coefficient, all post-R coefficients, the exact valuations for p>=11, and the value/weighted-derivative middle observables at 1/9. Executed result: PASS for all 157 primes p<=2000 with p mod8 in {5,7}, over 36,229 middle positions. Selected exact (p,L,R,S_p,C_middle(1/9),weighted_middle(1/9)) modulo p:
(5,3,4,0,0,0), (7,4,6,1,1,2), (13,8,11,9,12,8), (23,14,20,21,15,5), (29,18,25,27,17,10), (373,233,326,289,232,368).
Checks are finite regression, not independent mathematical admission. Proof is the recurrence argument above.

BRC reuse classification: COMPOSE_APPLIED. Carrier = labeled original Gauss coefficients; low-band C_low; exact injection seed S_p; middle 3F2; zero post-R projection. Population = k=0,...,p-1, with p-adic precision p². Observer = coefficientwise F and (1+16 theta)F, including z0=1/9. Future p³, non-Gauss 216, original H0/B0 and native experiments remain outside this compression lease. The middle band is a single-injection source, not a claim that the original multiple bands can be collapsed for arbitrary observables.

Next discriminating problem: evaluate the middle 3F2 and the low C response at z0, together with J(z0) or J'(z0) in their respective p mod24 classes, to construct a *genuine all-prime second-digit cancellation certificate*; alternatively seek an exact Frobenius/CM finite-field root selector. Test any proposed identity at 13,23,29,373 and retain the p=5 exception. Frozen D24 Delta_p-R_p and signed original216-vs2304 p³ comparison remain open.

Control evidence: current gateway 0.6.11 returned research_authority_granted=false, UPSTREAM_CODE_REVIEW_REQUIRED and new native job quota 5/5; fresh read-only continuation returned CONTROL_QUOTA. Old request IDs are not replayed. This author-side artifact asserts no registered session, CLAIM, OPEN, Source checkpoint, Result, review, acceptance or native experiment.
