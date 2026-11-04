# D25: exact finite adjoint Green transport for signed original 216–2304 bridge

2026-11-04 Asia/Hong_Kong. AUTHOR-DERIVED / EXACT SCOPED PROOF / FINITE EXACT CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.

Mother Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT. Publication: TP2-B6F4FC938FF94941C1B7. Immutable scientific input: c47e13e4aba0e006366f989d6334d443f6333ae3. Research lane: chatgpt-research-onhour-enterprise-math-20260923. Maintenance lane: chatgpt-hourly-enterprise-math-20260921 (not used).

This consumes the previous D25 original coefficient and valuation results, the middle/high reciprocal theorem, and the separately sourced 2026-11-04 hourly20 dual Picard–Fuchs forcing calculation. It does not re-prove prior admissions.

## Theorem 1 — exact finite Green/adjoint source identity

For every prime p>=5 write N=p-1, and define over Q:

a_n=(2n)!(3n)!/[(n!)^5 216^n], b_n=(4n)!/[(n!)^4 2304^n],
r_j=(4j+1)(4j+2)(4j+3)/[576(j+1)^3],
g_j=(2j+1)(56j(j+1)+13)/[288(j+1)^3],
f_j=g_j a_j, 0<=j<=N-1.

Define the *backward finite Green response* by

K_(N-1)=6N+1,
K_j=6(j+1)+1+r_(j+1) K_(j+1),  0<=j<N-1.       (1)

Then the following are exact equalities over Q:

sum_(n=0)^N (6n+1)(a_n-b_n) = sum_(j=0)^(N-1) f_j K_j.  (2)

W_216(p-1)-V_2304(p-1) =
   sum_(j=0)^(N-1) g_j a_j K_j - 2 sum_(n=0)^N n b_n. (3)

Here W_216 is the original (6n+1)-weighted 216 sum, and V_2304 is the original (8n+1)-weighted 2304 sum.

Proof. Exact factorial recurrences give b_(j+1)=r_j b_j and a_(j+1)=(r_j+g_j)a_j. For D_j=a_j-b_j one obtains D_0=0 and D_(j+1)=r_j D_j+f_j. Iterating, D_n=sum_(j<n) f_j product_(i=j+1)^(n-1)r_i. Reverse this *finite* double sum after weighting by 6n+1. Its inner sum is exactly (1). This yields (2). Finally (8n+1)=(6n+1)+2n gives (3). The terminal K_(N-1) is explicit; no infinite-series endpoint is silently dropped.

For 0<=j<=p-2, all denominators 288, 576, and (j+1)^3 are units in Z_(p) (p>=5). Thus this Green transport works directly modulo p^3 without division by quartic coefficients b_n, many of which carry p-factors. One backward and one forward pass use O(p) modular operations.

## Theorem 2 — nonzero order-two seam forcing

Assume p=6r+1>=7, h=3r=(p-1)/2, chi=(6/p) as the Legendre symbol. Previously proved source endpoint: a_h/p = -2 chi (mod p). Then

v_p(f_h)=2,    f_h/p^2 = chi/18 (mod p).              (4)

Indeed 2h+1=p, h(h+1)=-1/4 (mod p), hence 56h(h+1)+13=-1 and 288(h+1)^3=36 (mod p). Therefore g_h/p=-1/36 (mod p). Multiplication by a_h/p=-2chi proves (4). This identifies one *nonvanishing second-digit boundary flux* at the true middle/high source seam, rather than supposing that all source-difference forcing has first-order size.

Further, for j<p-1, g_j (mod p) vanishes precisely at 2j+1=0 or 56j(j+1)+13=0. The quadratic has discriminant 224=16*14. For p>=5 and p!=7, its two simple roots occur exactly when the Legendre symbol (14/p)=+1, with no roots when that symbol is -1. For p=7 the quadratic factor is the nonzero constant 13. This is an index-level forcing filter, not a supercongruence theorem.

For j<p, e_j=v_p(a_j)=floor(2j/p)+floor(3j/p), and e_j>=3 implies f_j K_j=0 (mod p^3). K_j is p-integral by (1). Thus the exact Green response decomposes into source bands e_j=0,1,2, with an additional p at the seam index h.

## Independent finite exact checks

The companion Python standard-library integer checker reconstructs both original coefficient families from p-free factorials and independently compares (2)/(3) with their direct weighted sums modulo p^3. All 148 primes 7<=p<=2000, p=1 (mod 6), passed. Exact rational Fraction evaluation independently passed at p=13 and 19. These finite outcomes support the derivation and remain distinct from the still-open all-prime bridge.

Observed mod p^3 Green band contributions [e0,e1,e2,e>=3], quartic 2theta B, and resulting W-V:

p=13: [1547,1456,676,0]; 2thetaB=1482; W-V=0.
p=19: [3705,4332,5054,0]; 2thetaB=6232; W-V=0.
p=373: [43033383,33870265,45773441,0]; 2thetaB=18886855; W-V=0.
At p=373 the seam f_186/373^2=145 (mod 373), equal to chi/18.

## Checkpoint and continuation

Highest verified author-side frontier: (1)–(4) plus the previous published signed 216/2304 and original 216 middle/high source observers. Do not redo D24 UR, the established 2304 half/full theorem, the proven valuation ports, or the earlier 148-prime scans solely to reconcile task state.

Smallest next mathematical action: determine sum_j f_j K_j modulo p^3 by a genuine terminal adjoint/WZ relation equal to 2 sum_n n b_n, rather than merely re-evaluating the Green identity (3). Test every terminal and seam contribution first at p=13,19,373 and seek a uniform proof for the target prime classes. Then verify the frozen D24 Delta_p-R_p bridge independently. The new representation is exact; cancellation remains open.

Native benchmark obligation remains the original fixed-373 H0/B0 divided-power [X]U mod 139129, rank, true semilinear Frobenius and independent replay, tracked by issue #1559 (open, no assignee in 2026-11-04 read). Its execution is not supplied by this external rational hypergeometric calculation.

The 2026-11-04 Sites read-only gateway returned v0.6.11, research_authority_granted=false and write_relay_enabled=false; exact Source recovery_status/session/claim/run was unavailable in this client. Historical request research-onhour-20261031-0205-dispatch-r15 remains an original request, not replayed. This note is a neutral author-side mathematics record, not a Source CLAIM, checkpoint, Result, review or mathematical acceptance.

BRC/provenance: labelled populations are original 216/2304 terms, each with original coefficient, index, valuation and independent source; forward operation is original factorial ratio; backward operation is exact finite Green; signed observer is W-V with retained p-adic remainder and terminal. No native X6 experiment or transfer theorem is asserted.
