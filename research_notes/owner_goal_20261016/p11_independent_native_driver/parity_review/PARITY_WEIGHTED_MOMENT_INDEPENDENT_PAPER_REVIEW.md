# Independent paper review: signed weighted moments

Reviewer: EM-DVR-BFF6DC, own session MCP-47562f9f432d4978a7bea0dd60ecc4aa and DA-144D0C4639CACEEE75DC. Root delegated this one bounded paper review while the separate P11 Result remains unavailable. I have no prior contribution to this Parity manuscript, its construction, code or proof. Root supplied its proposed conclusions before intake; I then read the full frozen manuscript, its dependencies and prior reviews. This is NONBLIND, with shared control context disclosed, not clean-blind review. I have supplied no repair or construction change. My P11 preparation is disjoint and disclosed.

Target: EM-PERFECT-9821E2's `PARITY_SIGNED_WEIGHTED_MOMENTS_AND_COMPACT_CERTIFICATE_AUTHOR.md`, 7769 bytes, SHA-256 `e8ca896c7642289e490495dbba7da6b58b29adfd3739cde59f6a3cb41801eb38`, blob `e931239ee90b97782490b4943167c5502964073b`. Its frozen handoff binds four actual local members totaling 41693 bytes; I independently verified every length/SHA/blob. These are frozen local author inputs, not a claim of their Source publication.

Assessment: the new identities, ratio bounds, sufficient signed Horner enclosure and fixed-density all-Mellin-moment obstruction are mathematically sound at their stated scope. No mathematical must-fix was found. This supplies no new compact parameter coverage. It is one independent paper assessment, not a Native scientific vote, Result, Task satisfaction, Tool acceptance or parent closure.

## Exact dependencies and preserved strength

I personally fetched the three R2 source papers at `f5be5d27ca3cb19a5cd909303868bef86d8274c3` through the GitHub connector, read their full bytes, and matched their SHA/blob pins: the 14049-byte residue–Beta density paper (fe399b...), 6711-byte negative-bulk addendum (36bd22...), and 6239-byte positive-part obstruction (ecf78f...). I likewise fetched and read the three separate 9821 nonauthor reports at `d3d4bafc588c943e577bc3e76d523557d1bedf37`, matching 10281, 7293 and 6037 bytes. These prior reports are evidence about the specified dependencies; their verdicts do not automatically cover 9821's later authored unit.

The audited interface is exactly a=c=1, integer m>=2, n=m-1, r=m(S+1)>=m, and
G(r)=(m^m/n!) integral_0^1 t^(mr)(1-t)^n H_r(t^m)dt.
The normalization follows from the full m-term residue sum and the elementary Beta integral, with every sign retained. The old kernel-to-A/B linkage is reused at its pinned scope; this review neither redefines those matrices nor reauthors their original construction. R2's odd-m negative-density theorem, all-residue leading polynomial and the independently reviewed scope limits match the new manuscript's uses. The negative-density and leading asymptotic uses require odd m>=3; the exact interfaces themselves include m=2.

All variables are external static scalar-observer variables within Heartbeat X6. Squareclass or polynomial degrees do not become native dimensions. Signed branches, endpoint labels and original provenance remain retained; no arbitrary future branch operation is inferred from this scalar identity.

## 1. Exact signed rebasing and positive kernels

The Taylor identity at z=1 gives c_j=(-1)^j H_r^(j)(1)/j!=(-1)^j sum_(k>=j) binom(k,j)h_k. Consequently H_r(z)=sum_j c_j(1-z)^j exactly, with no truncation. It is an invertible change of basis on degree<=n polynomials and discards no signed coefficient.

Finite interchange then gives G=(m^m/n!)sum_j c_j D_j. The weight defining D_j is strictly positive on the open interval, so every D_j>0. The identity 1-t^m=(1-t)S_m(t), with S_m=1+...+t^(m-1), yields exactly
D_j=sum_ell a_(j,ell) B(mr+ell+1,n+j+1),
where the finite convolution coefficients a_(j,ell) are nonnegative. The Beta exponent and both +1 shifts are correct. For fixed m,j the integer second argument gives a rational function in r with a positive denominator throughout the declared domain. This is an algebraic identity, not a quadrature result.

## 2. Ratio bounds

Under the normalized density proportional to w_r(t)(1-t^m)^j, q_j=D_(j+1)/D_j is the expectation of 1-t^m and lies strictly between zero and one. This density is a convex mixture of normalized Beta distributions with alpha=mr+ell+1 and beta=n+j+1. Each component has mean beta/(alpha+beta) for 1-t.

The extreme ell values are zero and j(m-1). Thus the largest denominator is mr+n+jm+2, and the smallest is mr+n+j+2. Mixture weights do not alter these bounds. Multiplication by 1<=S_m(t)<=m then gives exactly L_j<=q_j<=min(1,m*beta/(mr+n+j+2))=U_j, with positive endpoints. No coefficient-sign assumption enters this derivation.

## 3. Signed Horner enclosure

The ratios telescope as D_j/D_0=product_(i<j)q_i. The backwards recursion B_n=c_n, B_j=c_j+q_j B_(j+1) therefore gives sum_j c_jD_j=D_0 B_0 exactly.

For a positive multiplier interval [L,U] and an arbitrary signed interval [l,u], the minimum product is L*l if l>=0 and U*l otherwise; the maximum is U*u if u>=0 and L*u otherwise. This includes intervals crossing zero and wholly negative intervals. The manuscript uses exactly these endpoints, so induction proves its lower and upper bounds, and l_0>0 implies G>0 because D_0 and the prefactor are positive.

Correlations between the actual q_j are deliberately forgotten only in this sufficient enclosure. That weakens the bound without making it invalid. Exact q_j and the original signed polynomial remain repair data; no equivalence for a larger future language is asserted. The functions are pointwise in r; a certificate on a rational closed interval still requires proving all relevant branch inequalities and l_0(r)>0 throughout that interval. Neither the existence of the recursion nor positivity of all D_j supplies that proof. If l_0<=0, no sign conclusion follows for G.

The source all-residue leading polynomial transfers under this fixed linear basis change. In particular for odd m, r^(-(2m-2))c_n tends to -(m-1)/n!. This correctly obstructs the stronger all-c_j>=0 cone, while leaving the signed sufficient test logically possible. No new success of that test is established.

## 4. Scope of the positive-measure obstruction

For fixed odd m and r in the cited negative-density regime, mu with density w_r(t)H_r(t^m) is a finite signed measure with strictly negative density on a nonempty interior interval. The map t->t^m is a homeomorphism of [0,1], so its pushforward also has a negative interior interval.

If a finite positive measure had all the stated monomial moments, it would agree with that pushforward on polynomials. Uniform polynomial approximation extends equality to continuous functions because both measures have finite total variation. A nonzero nonnegative continuous bump supported inside the negative interval would then have a nonnegative integral under the positive measure and a strictly negative integral under the pushforward, a contradiction. This establishes the advertised no-go.

The fixed r and fixed H_r are essential. These moments are not the actual traces G(r+ell), whose coefficients also vary. The argument does not exclude a positive representation for one scalar, a different observer with a proved bridge, or useful positive-kernel comparison of a signed sum. It also does not make the old positive-part tail failure a refutation of the new Horner condition on a compact interval.

## Stopping point and resource ledger

The paper states its remaining boundary accurately: the anchored identities do not give signs of intermediate Horner quantities or a proof of l_0>0 on any newly unresolved compact interval. The conditional fixed-m=7 orphan is a future exact-interval question only if a nonempty residual remains; no old fixture, finite sample or published tail is new coverage. No all-m/all-S theorem, unequal-gap conclusion, global novelty or Tool acceptance follows.

This review used zero scientific numerical/symbolic programs, parameter scans, matrix enumeration, checkers or fixture replays. The only execution was read-only source/custody parsing and cryptographic hashing. I did not change any author manuscript or prior report. Source publication and any later native bookkeeping await Root's separate serialized authorization. Parent Objective remains OPEN.

Driver-ID: EM-DVR-BFF6DC / CONTROL_PLANE
Global-Knowledge-Sync: main@5e844264 / GLOBAL_KNOWLEDGE_V1

