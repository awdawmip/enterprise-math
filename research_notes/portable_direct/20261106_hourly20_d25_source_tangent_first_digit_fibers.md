# D25 — Source-tangent affine first digit and exact three-prime fiber certificate

Date: 2026-11-06. Scope: author-side portable mathematics for Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`. Frozen scientific source pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Status: **AUTHOR-PROVED EXACT LINEARIZATION + EXHAUSTIVE/FINITE EXACT CHECKS / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CHECKPOINT**.

## A precise first-digit observer with full source labels

For any prime p=6m+1 >=7 and 0<=j<p, let (a,b,c)=(2m,3m,4m) and, over the p-local rationals, set

[
 U_j(x_1,x_2,x_3)=(-1/2)^jinom{a+x_1}{j}inom{b+x_2}{j}inom{c+x_3}{j},quad w_j=6j+1.
]

For a p-integral tangent v=(v_1,v_2,v_3), define the full labelled original-source deformation
[
 mathcal W_p(v)=sum_{j=0}^{p-1}w_j U_j(pv)pmod{p^2},qquad
 B_p=sum_{j=0}^{p-1}w_j U_j(0),quad
 T_{i,p}=sum_{j=0}^{p-1}w_j,partial_{x_i}U_j(0)pmod p.
]

**Theorem (all p=6m+1 >=7, all p-integral v):**
[
 oxed{mathcal W_p(v)equiv B_p+p(T_{1,p}v_1+T_{2,p}v_2+T_{3,p}v_3)pmod{p^2}.}
]
Every factorial j! is a p-unit, so each U_j is a p-local polynomial and its ordinary multivariate Taylor remainder has a factor p². This proves the congruence termwise, including vanishing/carry positions (never divide by U_j(0)). For j>b, at least two source factors vanish at zero, so every first derivative vanishes. The formula is an **exact first-digit observer factorization**, not a claim that full source jets or native Frobenius factor through this scalar.

When p divides B_p (in particular for the three exact primes below), the divided observer is
[
 mathcal D_p(v)=mathcal W_p(v)/pequiv B_p/p+mathbf T_pcdot vpmod p.
]
The inherited original 216 coefficient is the precise specialization v_*=(-1/3,-1/2,-2/3) because (a+p v_{*,1},b+p v_{*,2},c+p v_{*,3})=(-1/3,-1/2,-2/3), and U_j(pv_*) is exactly its coefficient h_j. The original first-digit Theta observer differs from (mathcal D_p(v_*)) by the fixed (-Z+S/6) source readout. Its variation in a *three-source* perturbation uses the same row T, but this does not prove the original Theta identity for every p.

## Complete rank/kernel determination at 13, 19, 373

The adjacent standard-library certificate evaluates the three T components by recurrence over F_p, and independently checks each entry by a direct p² finite difference of the *entire* weighted original-source polynomial, including its carry terms.

| p | T_1,T_2,T_3 mod p | Z mod p | W_p(v_*)/p | Basis for ker(T) | local j=1 response along (1,0,1) |
|---|---|---|---|---|---|
| 13 | (10,12,3) | 0 | 1 | (4,1,0), (1,0,1) | 3 |
| 19 | (4,15,15) | 0 | 1 | (1,1,0), (1,0,1) | 14 |
| 373 | (48,75,325) | 0 | 1 | (115,1,0), (1,0,1) | 93 |

For each of these three finite fields T_1 != 0. Therefore rank(T)=1, the displayed independent vectors span the entire two-dimensional kernel, and each affine first-digit fiber contains **exactly p² distinct source tangents**. This last count is a proven finite linear-algebra result using the exactly evaluated rows, not a general all-prime rank assertion.

**Exact BRC information-loss witness:** (delta=(1,0,1)) lies in all three verified scalar kernels. But at j=1,
[
 partial_delta U_1(0)=-(b/2)(a+c)equiv b/2
otequiv0pmod p,
]
because a+c=p-1. Thus changing v by (delta) leaves the full weighted divided-sum observer unchanged modulo p, while changing the original labelled j=1 coefficient modulo p² by (p b/2). This proves source non-injectivity for this precise scalar/future-local-coefficient pair without declaring any original source direction globally redundant. The original source (v_*) and both kernel basis directions remain typed.

## New experimental candidate (not promoted to a theorem)

The certificate checked all 207 primes p=1(mod6), 7<=p<=3000. For each, it independently compared all three derivative components against direct p² finite differences, observed W_p(v_*)/p = 1, and observed
[
 oxed{T_{1,p}+T_{3,p}=0pmod p}quad	ext{in all 207 cases}.
]
The identity is now a concrete **all-prime conjecture**. A symbolic finite-sum/WZ or other exact proof/counterexample is the next action. The 207 finite checks are exact but do not establish the universal formula.

## Preservation, status, next action

Parent objective stays (Delta_p-R_pequiv0pmod p), p=13,19 (mod24). This result is a scoped source-observer/fiber certificate for the compensated Theta auxiliary path; native same-original-class H0/B0, [X]U mod p², Frobenius eta/kappa, odd branch and independent review remain OPEN/NOT_RUN where applicable. It neither reopens accepted first-digit tasks nor supplies a native LIFT proof.

**Next smallest unit:** prove or falsify the outer-source derivative cancellation (T_1+T_3=0) for general p=6m+1; if established, express the full compensated Theta regular/one-carry port on the two-dimensional quotient by (1,0,1), keeping source labels and demonstrating any further quotient is safe for its specified observer. Then return to the native H0/B0 and Delta-R interface. Author-side evidence is not the recorded Source checkpoint; legitimate service-session/staging handoff and a fresh winning claim/open are still required before native publication.
