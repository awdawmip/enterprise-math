# D25 continuation: proved quadratic parity balance and exact sextic zero-port criterion

Date: 2026-11-07 (Asia/Hong_Kong). Same TASK_RESEARCH author-side lane chatgpt-research-onhour-enterprise-math-20260923; not the maintenance lane. Source scientific publication TP2-B6F4FC938FF94941C1B7, pin c47e13e4aba0e006366f989d6334d443f6333ae3. Parent: 20261107_onhour_d25_pfaff_sextic_torus_port.md, original previous Gauss-jet frontier commit 3c1cc1c84b99047689dacfb690da784e1f362286.

## Setup

For prime p=6m+1>3 let f(x)=x^5(x+1)^2(2x+1), v(x)=f(x)^m in F_p, with v=0 at the three distinct roots 0,-1,-1/2. Let mu_6 be the six sixth roots of unity, and N_u=#{x in F_p : v(x)=u} for u in mu_6. The earlier *proved* finite-field bridge is S_m=-sum_x v(x) modp and A_1=2^{-m} A_5, where A_j=sum_x v(x)^j.

## New Theorem A: full quadratic-sign population (proved for ALL p=6m+1)

Let eps=(2/p) in {+1,-1}, and let N_+ and N_- count non-root inputs with v(x)^3=+1 and -1, respectively. Then, as **exact integer equalities**,

N_+ = (p-4-eps)/2,     N_- = (p-2+eps)/2,

hence A_3=sum_x v(x)^3 = -eps-1 (as an integer, not merely modulo p).

Proof: (f(x)/p)=(x(2x+1)/p) for x different from -1; at x=-1 the former is 0 and the latter is 1. The standard nondegenerate quadratic-polynomial character sum gives sum_x (x(2x+1)/p)=-(2/p) since 2x²+x has leading coefficient 2 and discriminant 1. Therefore sum_x (f(x)/p)=-eps-1. Since f has exactly three distinct F_p roots, N_++N_-=p-3 and N_+-N_-=-eps-1. Solve the two integer equations.

In particular, for the target p=13,19 mod24 (eps=-1), both populations have exactly (p-3)/2 elements. For the split cases eps=+1 they are (p-5)/2 and (p-1)/2. This is a universal **proved** sign-parity result for the exact original sextic observer, rather than an extrapolation from finite tests.

## New Theorem B: target zero port iff exact opposite-bucket equidistribution

For each target prime p=13 or 19 mod24, the following statements are equivalent:

(i) S_m == 0 mod p;
(ii) A_1=sum_x v(x) == 0 in F_p;
(iii) N_u=N_{-u} as **ordinary integers**, simultaneously for every u in mu_6.

Proof: (i)<->(ii) is the proved power-sum/Pfaff bridge. For target eps=-1 Theorem A gives A_3=0; reciprocal projective involution gives A_5=2^m A_1. Hence (ii) makes all three odd sixth-character Fourier moments A_1,A_3,A_5 zero. Discrete Fourier inversion on the six-element group mu_6 (6 invertible mod p) says the antisymmetric bucket count N_u-N_{-u} is 0 in F_p for each u. Each count lies between 0 and p-3, so its difference has absolute value less than p and equality modp lifts uniquely to literal integer equality. Conversely the opposite-bucket pairing cancels A_1. QED.

Thus the unproved first-digit mother subgoal is now a **finite exact equidistribution / bijection problem** in three pairs of sextic residue buckets, rather than a cancellation in F_p where signs and multiplicities are merged.

## Compatibility with three-valued orbit observer

For target primes the prior tau(x)=-(2x+1)/(2(x+1)) has no fixed point and sends character value v to c/v, c=2^{-m} with c³=-1. Its unordered two-element orbit contributes v+c/v, and the possible contributions are exactly {0,t,-t} for any chosen nonzero t among them.

Proof: c³=-1 implies -c is a cube root of unity. Hence v²=-c has precisely two solutions in mu_6, accounting for one zero-sum tau orbit of values; the other four sixth roots give two nonzero tau-orbit pairs, and v->-v exchanges their contributions and changes their signs. Consequently the observed first-digit congruence is equivalent to the integer equality of counts of +t and -t orbits. The new six-bucket criterion is a stronger witness format: it retains the original individual x and residue labels, not just the signed total.

## Executed arithmetic and labels

Two separate stdlib checkers were executed:
- d25_inert_orbit_balance_check_20261107.py : all 77 target/inert primes <=1999, proved three-valued label identity PASS; finite observation #(+t)=#(-t) for every tested input.
- d25_quadratic_sextic_balance_check_20261107.py : all 148 primes p=1mod6 <=1999 plus 5113, proved exact quadratic population formula and Fourier moment identity PASS, 77 inert inputs observed exact N_u=N_-u in all sixth-root buckets.

Exact witnesses (p, eps, N_plus quadratic, N_minus quadratic, S_m): (7,+1,1,3,4), (13,-1,5,5,0), (19,-1,8,8,0), (31,+1,13,15,21), (67,-1,32,32,0), (373,-1,185,185,0), (5113,+1,2554,2556,5019). For inert projective orbit labels with t=min nonzero residue, (p,t,count+t,count-t,count0)=(13,2,2,2,1),(19,6,4,4,0),(67,31,8,8,16),(373,90,68,68,49).

The universal Theorem B is an **equivalence**. The numerical assertion N_u=N_-u for all target primes remains UNPROVED. Theorem A gives an unconditional exact quadratic-level balance; the remaining step is to refine quadratic parity into full sixth-character opposite buckets for all target primes. This is a directly discriminating next research action, e.g. construct an explicit bucket-preserving sign-reversing bijection or establish the relevant two remaining character moments by algebraic trace.

## BRC / source provenance / native separation

Typed population x in F_p with original f(x), nonzero sixth-character u, projective tau orbit, quadratic parity and integer bucket multiplicity; operations: field power-sum, projective involution, Fourier observer, exact integer count lift. Theorem A is a proof of the **coarser parity balance**, Theorem B preserves necessary finer sixth-character bucket differences rather than asserting redundant information. Existing Pfaff and Gauss-jet sources reused; no native BRC engine executed, and the auxiliary field curve is not P000 native geometry.

Original pending Source request onhour11-20261106-1400-exact-research-lane-continuation retained; current gateway read at 2026-11-06T20:02:54Z reports CONFIGURED_NOT_LIVE_VERIFIED and research_authority_granted=false; em_status, original receipt, checkpoint reads rejected with BACKEND_IDENTITY_OR_VERSION_MISMATCH operation_sent=false. Historical checkpoint revision22; session/claim/run NOT_VERIFIED. Original native p373 H0/B0 benchmark #1559 remains NOT_EXECUTED/PENDING_OWNER. This is an author-side exact research checkpoint, not a Source CLAIM, Result, independent review or admission.