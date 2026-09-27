# Direct difference autocorrelation for a single signed bit

Status: new symbolic derivation, not yet independently reviewed or executed. No numerical speed claim or formal admission. This successor keeps the same stride-one K(g,k,R,r) contract as EM `56b191519b036c6890cae328c3b3812fbc1debb7`, `research_notes/directed_recovery/20260927_C6438C/qft_signedgap/ONE_WINDOW_REDUCTION.md`, SHA-256 `ee13a8d8bc03dd8359f3a3a3d80ac7cfdc9a0094f19deeb2af91189d75a42095`.

Let L=2^g, U=2^k, P=2U and H=L/P. Here g>=1 and 0<=k<g. The sign w(x)=(-1)^(bit_k(x)) is periodic with period P, positive on [0,U) and negative on [U,P). Define the ordinary nonnegative-displacement correlation

    A(d) = sum_{0<=x<L-d} w(x)*w(x+d),       0<=d<L.

The negative-displacement correlation is the same A(abs(d)): this is scalar symmetry of the pair product, not a rule for transposing arbitrary full-matrix seeds.

## Exact piecewise quadratic coefficient

Write d=qP+s, 0<=s<P. The full-period correlation is P-4s for 0<=s<=U and 4s-3P for U<=s<P. For s>0 the overlapping interval has H-q-1 complete periods and a final segment of length P-s. On that final segment the correlation is P-3s in the first case and s-P in the second case. Therefore

    A_low(d)  = (H-q)*(P-4s) + s,           0<=s<=U,
    A_high(d) = (H-q)*(4s-3P) - 3s + 2P,   U<=s<P.

At s=0 the first formula directly gives (H-q)P, including d=0, without using a nonexistent extra tail. At s=U both formulas agree. The nonnegative integer q satisfies 0<=q<H throughout the stated displacement range. Negative A values are legitimate.

Substituting s=d-Pq gives

    A_low = HP + (4H-2)P*q + 4*d*q - 4P*q^2 + (1-4H)*d.

Put q_plus=floor((d+U)/P) and delta=q_plus-q. Then delta is exactly 0 or 1 and selects the upper half-period. The difference between the two formulas is

    A_high - A_low
      = (8H-4)*d - 8*d*q + 8P*q^2 + (8-8H)P*q + (2-4H)P.

Equivalently it is 2*(2*(H-q)-1)*(2s-P), so its zero at s=U is explicit. Thus A=A_low+delta*(A_high-A_low), including the boundary where either branch may be used.

## Sum one displacement progression through degree-three moments

Consider d_j=b+a*j for j=0,...,n-1, with a>0 and every d_j in [0,L). Let

    M[p,t]      = sum_j j^p * floor((a*j+b)/P)^t,
    M_plus[p,t] = sum_j j^p * floor((a*j+b+U)/P)^t,
    Delta[p,t]  = M_plus[p,t] - M[p,t].

Only total degree p+t<=3 is needed. Because q_plus=q+delta and delta^2=delta, exact integer identities give

    S_delta     = Delta[0,1],
    S_jdelta    = Delta[1,1],
    S_qdelta    = (Delta[0,2]-Delta[0,1])/2,
    S_jqdelta   = (Delta[1,2]-Delta[1,1])/2,
    S_q2delta   = (2*Delta[0,3]-3*Delta[0,2]+Delta[0,1])/6.

All divisions are exact consequences of the identities, not rounded approximations. Define

    S_d       = b*n + a*n*(n-1)/2,
    S_dq      = b*M[0,1] + a*M[1,1],
    S_ddelta  = b*S_delta + a*S_jdelta,
    S_dqdelta = b*S_qdelta + a*S_jqdelta.

The entire progression contributes

    SumA = n*H*P + (4H-2)*P*M[0,1] + 4*S_dq
           - 4*P*M[0,2] + (1-4H)*S_d
           + (8H-4)*S_ddelta - 8*S_dqdelta
           + 8*P*S_q2delta + (8-8H)*P*S_qdelta
           + (2-4H)*P*S_delta.

This uses two existing degree-three floor-moment tables, at offsets b and b+U, for one arithmetic progression. It is not a statement that the current scalar moment API makes only two method calls or that all individual moment entries are free. The needed table entries, recursive nodes, typed arithmetic, cache requests and evidence must all be counted. The modulus here is the power of two P, which differs from the counting-modulus parameterization in the current window implementation.

## Recover the modular signed query

For 0<=r<R, take the nonnegative progression with head b=r and step a=R, and the strictly positive magnitude progression with head b=R-r and step a=R. For either head use no terms when b>=L; otherwise

    n = 1 + floor((L-1-b)/R).

Then

    K(g,k,R,r) = SumA(head=r) + SumA(head=R-r).

When r=0, only the first progression contains d=0; each nonzero multiple of R occurs once with each displacement sign, as required. When R is even and r=R/2, the two magnitude progressions coincide but both orientations are needed, so neither may be deduplicated. Empty progressions contribute zero without a moment query. This gives at most four degree-three tables for the entire query. It is compatible with R=1 and with R>L; those cases are not assumed to occur in any completed experiment.

## Proposed bounded implementation

Reuse the frozen actual TypedFloorMoments route (source SHA-256 `633502c9b484e60e5dc5fcf6edd0420f12d52c33c43e88851b9e1e6465ea94a2`). Build L,U,P,H, progression lengths, coefficients, moment differences and exact divisions using its typed signed/magnitude operations. Host code may choose fixed formula branches and wire public indices. Every saved expression must link to its actual operation and moment records. Retain raw denominator exponent 2g and signed values, without numerical phase propagation or an order oracle.

A first review should independently check the tail correlations, both polynomial expansions, the delta moment reductions, the r=0 and half-modulus double-count rules, and the empty-range case. Only after that review should a separately versioned observer and checker be considered. The existing nine tuples/31 values can supply hash-bound historical answers, with no repeat of the old exhaustive science. Endpoint shortcuts should remain a separate selectable route; a mathematically simpler expression is not automatically cheaper in typed digit cost.

This is a different evaluation formula for the same restricted single-negative-bit scalar correlation. It does not solve arbitrary Walsh masks, full matrix correlation growth, many-gap convolution, or period/address discovery. No literature-first novelty claim is made.

Global-Knowledge-Sync: main@f8aa9c8 / GLOBAL_KNOWLEDGE_V1
