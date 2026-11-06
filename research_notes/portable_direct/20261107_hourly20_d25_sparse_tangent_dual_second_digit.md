# D25: Exact dual sparse tangent observer and precision-sensitive support

Date 2026-11-07 Asia/Hong_Kong. AUTHOR-SIDE PROVED ALGEBRA / EXACT FINITE CERTIFICATES / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CHECKPOINT.

Scientific parent: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7, frozen pin c47e13e4aba0e006366f989d6334d443f6333ae3. Logical Research lane chatgpt-research-hourly-enterprise-math-20260923. This extends the immediately preceding exact j-labelled two-window codec without repeating its proof.

## Theorem: a directly evaluable tangent functional on the two windows

Let p=6m+1 prime, a=2m, b=3m, c=4m. Work over Z_(p), or reduce modulo any p^s, s>=1. The labelled basis is G_j(t)=binom(t-a,j)binom(t,j), 0<=j<=b. Let F_u(t)=sum_{j=0}^b u_j G_j(t) for arbitrary coefficients u_j in Z_(p). Use the (b+1) observation points t_0,...,t_b from the prior theorem: t_j=j (j<a), t_(a+r)=c+r (0<=r<=m).

Define the lower triangular p-unit matrix M_(i,j)=G_j(t_i), and the exact derivative vector ell_j=G_j'(c). Define the DUAL observation weights backwards:
 alpha_j = (ell_j - sum_{i=j+1}^b alpha_i M_(i,j))/M_(j,j), j=b,b-1,...,0.
All divisions are by p-units. Then for arbitrary coefficients and every precision:
 F_u'(c) = sum_{i=0}^b alpha_i F_u(t_i) (mod p^s).
The weights alpha_i are uniquely determined in Z_(p), independent of the input source coefficients u_j. Thus after O(b^2) one-time exact coefficient preprocessing, a new sourced tangent uses only b+1 scalar observations and O(b) arithmetic to take their weighted sum. Source labels and separate normal/carry derivatives remain recoverable by the prior triangular inverse if needed.

Proof: the recursion is exactly M^T alpha=ell. For every u, sum_i alpha_i F_u(t_i)=alpha^T M u=ell^T u=F_u'(c). Matrix M is invertible over Z_(p) by the previously proved p-unit triangular determinant. QED.

Since G_0(t)=1, ell_0=0, whence sum_i alpha_i=0. For the ACTUAL D25 family u_0=1 is supplied a priori, and F_u(0)=1. The first sample t_0=0 is unnecessary; the stronger direct formula is
 F_m'(c) = sum_{i=1}^b alpha_i (F_m(t_i)-1) (mod p^s).
It uses exactly b=(p-1)/2 scalar queries without any full j-source reconstruction. If F_m'(c) is divisible by p, its second digit follows by evaluating this integer-mod-p^2 expression, then dividing by p. This operation is p-adically exact, independent of an unproved universal vanishing conjecture.

## Closed nonzero last-query coefficient

Only the last sampling row contains G_b. Therefore its dual weight is fixed by
 alpha_b=G_b'(c)/G_b(c+m)
 =(-1)^(m-1) ((2m)!)^2 (4m)! / [m (3m)! (5m)!].
Every factor is a p-unit, so alpha_b is a p-unit. For the stated two-window observer, the query at t=c+m=5m is indispensable to recover the tangent for arbitrary labelled weights. Indeed a change in u_b is invisible at all earlier sample points and changes the derivative by u_b G_b'(c), with G_b'(c) a p-unit. This is a sharp query-necessity result for this chosen sampling architecture, and does not assert global minimality over every possible sample selection.

## A new second-digit support witness

In the unique dual vector, a coefficient may vanish modulo p and still be nonzero modulo p^2. Direct exact computation gives:
 - p=13: alpha_0=0 (mod 13), but alpha_0=104=13*8 (mod 169); this point is supplied from known u_0=1 in the D25 family.
 - p=109: alpha_17=0 (mod109), but alpha_17=6867=109*63 (mod 109^2).
 - p=373: alpha_135=0 (mod373), but alpha_135=60426=373*162 (mod 373^2). Index 135 is the high-window sample t=248+(135-124)=259.

Consequently, a mod-p sparse tangent observer can omit t=259 at p=373, but that omission is not automatically valid for the second p-adic digit. The actual lambda_373=180 check survives the full mod-373^2 dual observer. This is a concrete BRC information-fidelity witness: scalar coefficients visible only at a finer p-adic level can affect the next observer operation.

## Executed verification

The companion Python standard-library script constructs the full triangular sampling matrix, independent source derivative vector, unique dual, and closed last coefficient. For all 80 p=1 (mod6) primes <=1000, at s=1 and s=2, it verifies both the actual D25 coefficients and a synthetic variable coefficient family: 320 input-family checks PASS. At p=13,109,373 it additionally checks s=3 and both coefficient families: 6 more PASS. TOTAL 326/326. It separately verifies the fixed u_0=1 half-table direct formula, the exact last coefficient, sum alpha=0, the observed mod-p versus mod-p^2 zero supports and the previously established p=373 second digit. The code uses exact integer residues and p-unit inverses.

## Next scientific action and control

The proven direct dual may be reused for repeated normal/carry second-digit computations. The next open mathematics is to isolate an explicit prime-field correction for lambda_p=(F_m'(4m)/p) mod p and test it on the already pinned Wieferich witnesses p=1093,3511, then build the explicit map to the frozen signed H0/B0/Frobenius LIFT. Mother Delta_p-R_p=0 modulo p on primes p=13,19 (mod24) stays OPEN.

Control checked in this same 2026-11-07 Research run: em_status returned BACKEND_IDENTITY_OR_VERSION_MISMATCH, operation_sent=false; Site is CONFIGURED_NOT_LIVE_VERIFIED and research_authority_granted=false. Original request IDs em-h20-20261106-1324-d25-task-r13 and em-h20-20261106-1324-d25-cont-r13 are preserved. Native old session/staging/claim/run is unverified; no new native CLAIM/open/checkpoint is asserted. Recovery owner path: awdawmip/enterprise-math#1558.