# PREFIX-573 — 六轴BRC门控观察的14阶递推最优性及门控求和后的5阶降维

Date: 2026-11-08 Asia/Shanghai. Science pin: f42f2906d77f24085c123f3ccfe9667d41caa96d (unchanged). Status: AUTHOR_PROVED / EXACT_MODULAR_CERTIFICATE_PASS / UNREVIEWED / NOT_ADMITTED.

## Scope and predecessors

The original model has 96 native ordered branch ports, 6 actions per port, and 9 admissible roots with r5=r6=0. Retain the exact observer q1=q2=q3=q4=1, x=q5, y=q6, z=gate. The observer-safe 37-class quotient was certified in PREFIX-566. PREFIX-572 (commit 47f5eb4694a477504ee890e87c6c50a0bb946615) proved the full polynomial annihilator T_z Q14,z(T_z^2)1=0, monic degree 14 in lambda. The previous proofs and their original scientific pin are reused unchanged.

Let F_{i,d}=(T_z^d 1)_i for observer class i=0,...,36. Over K=Q(x,y,z), define A_{i,m}=F_{i,2m+1} and B_{i,m}=F_{i,2m+2}, m>=0.

## Theorem A: exact GENERIC minimal recurrence order 14, for EACH class

For each of the 37 individual observer classes, both A and B have minimal eventual constant-coefficient linear recurrence order exactly 14 over K. This includes each of the 11 axis-swap fixed classes over the smaller symmetric field Q(u,v,z), u=x+y and v=xy.

Proof: PREFIX-572's exact annihilator gives order <=14 for both subsequences at every m>=0. Construct H^{odd}_i=[F_{i,2(r+c)+1}]_(r,c=0..13) and H^{even}_i=[F_{i,2(r+c)+2}]_(r,c=0..13). Each determinant is an integer polynomial in x,y,z. The attached pure-Python standard-library certificate constructs the 37-state quotient directly from unchanged native transition files, sets x=2,y=3,z=5, reduces modulo prime 1000003, then executes ordinary exact modular elimination. All 37 odd and all 37 shifted-even 14x14 determinants are nonzero modulo 1000003. Thus all are nonzero formal polynomials, so no scalar recurrence order <=13 exists over K.

The order-14 polynomial's exact constant term, as already computed symbolically in PREFIX-572, is Q14,z(0)= -1320903770112*v^5*z-3962711310336*v^5. At u=5,v=6,z=5 it is 478364 modulo 1000003, nonzero. The resulting companion shift is invertible. A nonzero Hankel determinant persists at every later shift, excluding even an eventually shorter recurrence. The upper and lower bounds prove sharpness.

## Theorem B: exactly 5 after gate summation

Set z=1, thereby summing the gate counter while keeping x and y independent. The direct 96->5 quotient of PREFIX-565 is exact for this declared observer and every future length. The new certificate independently checks that each of the 37 weighted class rows factors through those same five native classes after z=1. Cayley–Hamilton of the 5x5 matrix squared supplies order <=5 for each odd and shifted-even subsequence. At x=2,y=3 modulo 1000003 all 37 odd and 37 shifted-even 5x5 Hankel determinants are nonzero, proving order >=5 generically. The specialized five-state matrix has determinant 5184 at this point, establishing nonzero determinants for all later shifts. Thus the minimal eventual two-step order is exactly 5 over Q(x,y) for every class after z=1.

This is an exact observer-dependent 14->5 reduction. The discarded information is the separate gate-count distribution; native ordered path provenance is retained in the original 96-port source and is not claimed reconstructible from the five-class observer.

## Reproduction and coverage

Unmodified dependencies: PREFIX565_positive_marginal_certificate.py (Git blob 7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41) and PREFIX566_gate_quotient_certificate.py (Git blob 7b6613193847e4123cd0ac11107eb9b9c70290c8), both under research_notes/portable_direct. Run PREFIX573_published_certificate.py beside both, redirect JSON to PREFIX573_PUBLISHED_RESULTS.json. Pure integer/modular arithmetic, no floating-point or interpolation.

Observed status ALL_CHECKS_PASS. Generic sample (x,y,z)=(2,3,5): 37/37 odd and 37/37 shifted-even 14x14 minors nonzero; first determinants 720569 and 59929 modulo 1000003. Gate-summed sample (2,3,1): 37/37 odd and 37/37 shifted-even 5x5 minors nonzero; first 766217 and 57012. Equal-axes (2,2,7) gives zero 14x14 odd minors in all 37 classes, a special-parameter observation only. The extended local certificate additionally recomputed the 17x17 modular characteristic polynomial, exactly divided by the prior cubic and checked 1702 recurrence equations through depth 74, all PASS; full local evidence bundle retains those independent checks.

## Next research action

Use the now-sharp degree-14 recurrence to search for a positivity-preserving invariant cone or a gate-sensitive companion to the five-state z=1 core, rather than further attempts to lower generic scalar recurrence order. Quantify what gate information must be retained for each projected future operation; preserve the original native source and frozen pin.

## Authority

Native Enterprise Math service returned BACKEND_IDENTITY_OR_VERSION_MISMATCH / STATUS_DATABASE_UNAVAILABLE with operation_sent=false when session and task list were queried. The authentic live owner/native Researcher-ID and formal CLAIM remain unconfirmed. This is author-side mathematical evidence and a GitHub research note, not an admitted Result/Review.
