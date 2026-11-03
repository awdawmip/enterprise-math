# D25: exact Gauss far-strip carry in the original 216 fixed argument

Date 2026-11-03 (+08). Author-side TASK_RESEARCH, logical Research lane `chatgpt-research-onhour-enterprise-math-20260923` only. Mother RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; immutable scientific input pin c47e13e4aba0e006366f989d6334d443f6333ae3. Status: SCOPED ALGEBRAIC PROOF / FINITE EXACT CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. The mother fixed-argument second carry and native p373 benchmark remain open.

## Theorem A: full three-strip Gauss coefficient Hensel expansion

For each prime p=6r+1>=7, put c_k=(1/6)_k(1/3)_k/(k!)^2, 0<=k<p, G(z)=sum_(k=0)^(p-1)c_k z^k. Use exact identity c_k=(-r+p/6)_k(-2r+p/3)_k/(k!)^2. Define

    M_k = prod_(i=0..k-1, i!=r)(i-r) * prod_(i=0..k-1, i!=2r)(i-2r)/(k!)^2,
    H_k = sum_(i<k, i!=r) 1/[6(i-r)] + sum_(i<k, i!=2r) 1/[3(i-2r)],
    J_k = sum_(i<k, i!=r) 1/[36(i-r)^2] + sum_(i<k, i!=2r) 1/[9(i-2r)^2].

All denominators are p-units. The precise coefficient congruences modulo p^3 are

    0<=k<=r:  c_k = M_k (1+p H_k + p^2(H_k^2-J_k)/2),
    r<k<=2r: c_k = (p/6) M_k (1+p H_k),
    2r<k<p:  c_k = (p^2/18) M_k.                              (A)

PROOF: Factor the p-adically integral numerator by its two parameter roots i=r and i=2r. Each crossed root yields exactly p/6 or p/3. Expand the remaining nonzero finite factors (1+p/(6(i-r))) and (1+p/(3(i-2r))) through the required precision; the first and second logarithmic sums are H_k and J_k, whence the quadratic coefficient (H_k^2-J_k)/2. For k<p every remaining denominator is a p-unit. The number of crossed roots is precisely 0,1,2 on these strips.

## Theorem B: closed truncated hypergeometric Gauss far observer

Define the distinct Gauss far coefficient (not the original 216 high 4F3 weighted observer)

    H_far(p)=sum_(k=2r+1)^(p-1) (c_k/p^2) 2^(-k) (mod p),
    e_p = (-1)^r (r!)^2 / [18(2r+1)^2(2r)!] (mod p).

Then

    H_far(p) = e_p 2^(-(2r+1))
        * sum_(s=0)^(4r-1) [(5/6)_s (1)_s / (5/3)_s^2] 2^(-s)  (mod p).   (B)

This is an explicitly TRUNCATED 4r-term sum; its denominators are units and no numerator-termination is asserted. PROOF: Formula (A) at k=2r+1 gives the exact base coefficient e_p after splitting (-r)_(2r+1) and (-2r)_(2r+1) at their single roots. For k=2r+1+s (s=0,...,4r-2), the original ratio c_(k+1)/c_k modulo p after removal of p^2 is

    [(s+5/6)(s+1)]/(s+5/3)^2
    = (6s+5)(3s+3)/[2(3s+5)^2].

The denominator is a unit in this exact ratio range; (B) follows by induction on s, including the final k=p-1.

## Theorem C: the far Gauss band changes the original fixed second carry

For target primes p=13,19 (mod 24), let G=G(1/2), D=(theta G)(1/2) with theta=z*d/dz, G_< =sum_(k=0)^(2r)c_k 2^(-k), D_< =sum_(k=0)^(2r)k c_k 2^(-k), A=G/p. Consume the already accepted D24 first carry G=0 (mod p), 12AD=1 (mod p) and finite Clausen square. From (A),(B) G=G_< +p^2 H_far (mod p^3), D=D_< (mod p^2), so

    (12AD-1)/p = (12(G_</p)D_<-1)/p +12(D_< modp)H_far (modp).    (C)

All p-divided expressions have integer p-adic meaning by the first carry. In particular dropping the far Gauss band while retaining original Clausen defects changes the second digit in general.

Consume the *separate sibling* signed-original-216 adjoint (commit 6e566d86091cd675165e316e850574feb6720dd6) and our finite Clausen Green theorem (commit cd6e0d6ed4d009a4c93e38e3241d7bbc9fa230f8). For a_j=(1/2)_j(1/3)_j(2/3)_j/(j!)^3, ell_j=binom(r,j)binom(2r,j), T_(j-1)=sum_(t=0)^(j-1)(6t+1)a_t/2^t, exact original E=-sum_(j=1)^r ell_j T_(j-1)/(6 j^2 a_j) modp. The fixed-argument identity W_216=G^2+12GD+p^2 E (mod p^3) gives the new FOUR-SOURCE exact reduction

    (W_216(p-1)-p)/p^2 =
        (12(G_</p)D_<-1)/p  + 12(D_< modp)H_far
        + (G/p)^2 -sum_(j=1)^r ell_j T_(j-1)/(6 j^2 a_j) (modp). (D)

Identity (D) is proved; proving that its RHS vanishes for every target prime remains OPEN. Distinct provenance is retained for Gauss low+middle, Gauss far, Gauss square, and original signed Clausen pair/triangle. This is an actual BRC COMPOSE_APPLIED source-preserving second-carry interface; it is not a P000 change or a native Frobenius computation.

## Executed exact verification and next scientific action

The companion Python integer checker independently regenerates full Gauss coefficients by original Pochhammer ratio, confirms (A) coefficient-by-coefficient, (B) as an independent far hypergeometric sum, the 216 weighted original recurrence, and (C)/(D). All 80 primes p<=1000, p=1 (mod 6) passed: 36,668 Gauss coefficient positions. All 45 target primes in that range passed (C)/(D). For p=13,19,37,43,373 respectively, [H_far; lowmid-carry, extra far-carry, square, E] =
[8;0,9,4,0], [10;18,6,7,7], [8;27,10,11,26], [7;40,3,15,28], [252;169,197,203,177].
At p373 the contributions 169+197+203+177=746=0 modulo373. If the Gauss far contribution is discarded, the remaining 169+203+177=549=176 modulo373: an explicit diagnostic for source loss, not a mother-theorem counterexample.

Next precise unit: construct a terminating WZ/contiguous or CM-normalized certificate canceling these distinct contributions for all target primes; test normalization at 13,19,373. Native H0/B0 same-original-class p373 rank, [X]U modulo139129, real semilinear Frobenius and independent replay remain NOT_EXECUTED/PENDING_OWNER, support #1559; control support #1558. Research write authority absent from the Sites status checked at 2026-11-03T04:09:53Z, so this is author-side evidence, not CLAIM, Result, registered activity, formal checkpoint or admission. Historical failed request research-onhour-20261031-0205-dispatch-r15/#6633 not replayed. Scheduler/notifications untouched.
