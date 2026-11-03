# D25: signed-prefix finite Green/adjoint bridge for the original 216 second carry

Date: 2026-11-03 (+08). Author-side TASK_RESEARCH; algebraically derived, finite-exact checked, UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. Frozen parent RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7, frozen input pin c47e13e4aba0e006366f989d6334d443f6333ae3. Logical Research lane chatgpt-research-hourly-enterprise-math-20260923, separate from maintenance chatgpt-hourly-enterprise-math-20260921.

## Exact reused source and new units

Consume sibling onhour result at cd6e0d6ed4d009a4c93e38e3241d7bbc9fa230f8, research_notes/portable_direct/20261103_onhour_d25_gauss_clausen_inhomogeneous_green_port.md. It proved the finite Clausen defect polynomial K(z), degree less than r, by

    t^3 K_t - Q_t K_(t-1) = (t/3) ell_t,   K_r=0,
    Q_t=(2t-1)(3t-2)(3t-1)/18,
    E_p=(1/2)[(1+6 theta) K](1/2) mod p.

All computations below are in F_p unless explicitly p-adic. For any prime p=6r+1 >= 7 let

    a_t=((1/2)_t (1/3)_t (2/3)_t)/(t!)^3,
    b_t=a_t / 2^t, ell_t=binom(r,t)binom(2r,t), 0 <= t <= r.

For 1<=t<=r all t, a_t, Q_t are units. The elementary ORIGINAL-216 ratio a_t/a_(t-1)=Q_t/t^3 converts the sibling recurrence to

    K_t/a_t - K_(t-1)/a_(t-1) = ell_t/(3t^2 a_t).

Summing to the terminal condition K_r=0 proves NEW UNIT 1, the closed Green tail:

    K_t = -(a_t/3) sum_(j=t+1)^r ell_j/(j^2 a_j) mod p, 0<=t<=r.

This is an explicit O(r) suffix algorithm and a different representation of the SAME previously proven Clausen defect, not a separate defect. It retains ordered (t,j) with t<j.

Define original signed W prefixes, with unchanged original 216 b_t and orientation:

    T_(j-1) = sum_(t=0)^(j-1) (6t+1)b_t, 1<=j<=r.

Substitution and finite triangular-sum reversal prove NEW UNIT 2:

    E_p = - (1/6) sum_(j=1)^r [ell_j/(j^2 a_j)] T_(j-1) mod p.   (SP)

Proof: E_p=1/2 sum_(t=0)^(r-1)(6t+1)2^(-t)K_t; insert the closed tail, interchange finite sums over 0<=t<j<=r. The factor is -1/6. Thus original signed 216 initial segments couple directly to the source-correct finite Clausen defect. This supplies a terminating adjoint/WZ target.

## Fixed t=1 mother-objective bridge

For target p mod 24 in {13,19}, let

    G(z)=sum_(k=0)^(p-1) ((1/6)_k (1/3)_k/(k!)^2) z^k,
    A=G(1/2)/p in Z_p, D=(theta G)(1/2) in Z_p,
    W_p=sum_(k=0)^(p-1)(6k+1)b_k, theta=z*d/dz.

The frozen accepted first-carry input is 12 A D = 1 mod p. Note D is EULER derivative; an ordinary derivative G'(1/2)=2D changes the prefactor from 12 to 6. The exact finite Clausen square and its high defect yield

    W_p = G(1/2)^2 + 12 G(1/2) D + p^2 E_p mod p^3,

hence the proved reduction

    (W_p-p)/p^2 = (12 A D -1)/p + A^2
                  - (1/6) sum_(j=1)^r [ell_j/(j^2 a_j)] T_(j-1) mod p.  (BASE)

The division by p is made after the proved first carry. The mother congruence W_p=p mod p^3 is equivalent to the vanishing of the explicit right side for the target prime class. BASE is proved; uniform vanishing remains OPEN. This reduction targets the FIXED BASELINE, unlike the completed argument-perturbation/isometry research.

## Executed arithmetic and source/observer accounting

The companion exact Python checker executed on ALL 77 target primes 13<=p<=2000 (p mod24 in {13,19}). It builds original a_k, b_k and Gauss c_k modulo p^3; verifies independent E=(W-G^2-12G*theta G)/p^2 against K recurrence and the new signed-prefix formula; verifies K via the new normalized tail, and verifies every high Clausen convolution coefficient at p=13,19,37,373. All PASS. The first-carry, square and defect residues were respectively:
p13: 9,4,0; p19: 5,7,7; p37: 0,11,26; p373: 366,203,177. In each case BASE was 0. This is FINITE exact evidence for baseline vanishing, not a universal proof.

BRC/source provenance: retain ordered original integer index pair (t,j), Gauss ell_j, signed original-216 prefix T_(j-1), truncation triangle t<j, p-adic precision, and Euler-vs-ordinary derivative orientation. This is a scope-typed factorization for the specified scalar E_p/BASE; it neither erases other observation directions nor changes P000, the ACTIVE X6 worldview, native H0/B0 status or scientific source pin.

Next scientific action: seek a terminating rational WZ / contiguous telescoper for the triangular signed-prefix term in BASE, coupling its Gauss first-carry with the original 216 source, first validating signs at p13,p19,p373. Preserve sibling's inhomogeneous Green recurrence and the upper H2 4F3 port.

## Operational status

As read on 2026-11-03, Gateway v0.6.11 returned UPSTREAM_CODE_REVIEW_REQUIRED, research_authority_granted=false, executor_binding_configured=false and 5/5 active native-control quota. Old read-only bridge #6637 was successful and the exact continuation #6638 definitively FAILED with code-review error. Neither replayed. Historical service session MCP-06f7ad61a8d841d9ba1ba1ef4d088d94 is provenance; neutral staging remains protected. No native session, CLAIM, OPEN, checkpoint, Result, independent review, admission or scheduled-task modification was performed. Control support remains #1558, native p373 benchmark remains NOT_EXECUTED at #1559.
