# D25 — Unique Frobenius overflow port and exact high-tail boundary functional

2026-11-07 · Second same-turn author-side TASK_RESEARCH unit; **proved support theorem and finite exact checks, UNREVIEWED / NOT_ADMITTED**. Same logical Research lane chatgpt-research-onhour-enterprise-math-20260923, mother task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7 and frozen pin c47e13e4aba0e006366f989d6334d443f6333ae3. Consumes the immediately preceding three-stratum F0/F1/F2 durable author-side checkpoint and earlier normalized tail factorials.

## Theorem — Exactly one possible degree >=p source

Take p,u,v,F0,F1,F2 from the preceding general p³ harmonic lift theorem. In the 216 model, p=6m+1,u=m,v=2m, lambda=6,x=1/2, epsilon=0. In the 2304 model, p=8k+3 or 8k+5, u=k,v=3k+1,lambda=8,x=1/9, and epsilon=0 or 1 respectively. Put C(z)=1-epsilon*z (and C=1 on the A side). Then C*F0², C*F0*F1, and C*F1² all have degree <p. The **only** product in the four-port decomposition that can exceed the finite truncation cutoff is C*F0*F2. Its above-cutoff degree support is contained in

    p <= n <= p+u-1+epsilon.                         (1)

Write a_i=[z^i]F0 (0<=i<=u), and J_j=[z^j]F2 for j>v, extended by zero outside 0<=j<p. For every n in (1), the coefficient of 2*C*F0*F2 is

    d_n = 2 sum_{i=0}^u a_i (J_{n-i} - epsilon*J_{n-1-i}) mod p.  (2)

Every contributing J index is >v, so the overflow is determined **solely** by the prior proved normalized high-index p² factorial tail kernel and the zeroth-stratum binomial source. No out-of-range Gauss term is needed.

The exact F_p-valued weighted boundary functional is

    H_p = sum_{r=0}^{u-1+epsilon}
                  (1+lambda*r) x^(r+1) d_{p+r} mod p.           (3)

The full untruncated weighted evaluation of 2*C*F0*F2 minus its genuine degree-<p projection is H_p. This is a source-preserving Frobenius-cutoff correction, not an alternative native H0/B0 observation.

**Proof.** A-side degrees are deg(F0)<=m, deg(F1)<=2m, deg(F2)<=p-1 and p=6m+1. Thus F0²,F0F1,F1² have upper degrees 2m,3m,4m<p. B-side degrees are <=k,3k+1,p-1, respectively. The Euler factor adds at most epsilon<=1, hence the other three upper degrees are 2k+epsilon,4k+1+epsilon,6k+2+epsilon<p. For n>=p in the fourth product, nonzero terms have F2 index j>=p-u-1>v, while j<p since F2 has degree <p. Thus J_j gives exactly (2), and the full support satisfies (1). Applying 1+lambda D and using x^(p+r)=x^(r+1) in F_p gives (3). QED.

## Discriminating finite exact certificates

The companion checker independently constructs the full polynomial convolution and verifies both the absence of other overflow terms and formula (2) coefficient by coefficient at every eligible prime <=401 (37 A and 41 B instances). Every check PASS.

For p in {13,19,43,67,373}, the triple below denotes (maximum overflow-count, first d_p, weighted boundary H_p) over F_p:

| p | 216 | 2304 | H_A-H_B mod p |
|---:|:---:|:---:|---:|
|13|(2,1,0)|(2,7,10)|3|
|19|(3,1,12)|(2,12,3)|9|
|43|(7,42,15)|(5,17,14)|1|
|67|(11,22,21)|(8,26,46)|42|
|373|(62,315,196)|(47,97,131)|65|

This provides an exact counterexample to the candidate **that the two high-tail Frobenius overflows separately cancel**: p=13 gives 3 and p=373 gives 65, not zero. Therefore the mother-objective cancellation needs the lower-stratum and first-order self-composition ports as well. This is a scoped statement about a proposed compression, not a negation of the original supercongruence.

## Continuation

Next mathematical action: seek a signed Cartier/WZ relation pairing H_A-H_B with the other three previously derived ports under the Fricke common parameter, retaining both p=8k+3 and Euler-twisted p=8k+5 cases. Reject only candidate reductions that fail the exact five-prime discrimination. The original same-class p373 native H0/B0 [X]U mod139129 / Frobenius eta / Hesse Green kappa / independent benchmark remains pending at https://github.com/awdawmip/enterprise-math/issues/1559. No original Source request has been replayed.

On 2026-11-07 near 13:29 UTC the existing em_status and original-request reconciliation path returned BACKEND_IDENTITY_OR_VERSION_MISMATCH, subreason UPSTREAM_STATUS_TOOL_ERROR, status_error_code STATUS_DATABASE_UNAVAILABLE, operation_sent=false. Site phase CONFIGURED_NOT_LIVE_VERIFIED, research_authority_granted=false. This mathematical note conveys no native session, claim, run, checkpoint, Result, review or admitted proof.
