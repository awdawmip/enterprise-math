# EC49FVS — Saturating the 11-adic divisor lattice: a 65-layer certified rational-phase mesh

Date: 2026-11-21 (Asia/Shanghai). Scientific status: AUTHOR_PROVED / EXACT_INTEGER_PERIOD_CERTIFICATE / PARENT_DEPENDENT / NOT_REVIEWED / NOT_ADMITTED.
Frozen scientific input: BRC16943, unchanged. Parent: awdawmip/enterprise-math@99d3830c3f745676f51f89d2b119c0423528113f:research_notes/portable_direct/EC49FVR_ADAPTIVE_TWO_SCALE_MESH_THEOREM.md. This work is a portable rational Bernoulli observation-model calculation, not an X6 native operation or new formal CLAIM.

## New theorem and exact value

Let S_H consist of reduced rational phases 0<h/d<1, d<=H, whose inherited **complete projective mod-11 no-root certificate** proves that no rational detection width x in (0,1) of the frozen Bernoulli observation model yields t(x)=h/d. The certified rational phases include the following 65-layer construction.

**Theorem.** For every integer H>=256 and every real interval I contained in [0,1],

    |I| > 1365/(506 H)  implies  I intersects S_H.

The new coefficient is 1365/506 = 2.697628458498..., compared to EC49FVR's 490/143 = 3.426573426573... (exact relative improvement 137/644 = 21.273291925...%).

With j=floor(log_2 H), k=2^j, and rho=H/k in [1,2), take L=84915883381329, C=2L=169831766762658, M=14080 C=2391231276018224640. Let

    R = {odd integers r: 1<=r<=127, r divides L}
      = {1,3,7,9,11,13,21,23,27,29,31,33,39,47,53,61,
         63,69,77,87,91,93,99,117}.
    D = {(r,e): r in R, ceil(log_2 r)<=e<=7}.

For r=1 the lower endpoint is e=0. This gives exactly 65 distinct (r,e) pairs: the 46 inherited pairs, plus 19 additional pairs. For each (r,e) and ell in {0,1}, admit the denominator

    d_(r,e,ell)=r * 2^(j+ell-e) <= H.

For j>=8 these are positive integers; ell=0 layers always enter at rho=1. The ell=1 layers enter when rho>=2r/2^e. Denote the union of all certified reduced fractions with these admitted denominators by T_j(H), a subset of S_H.

**Exact stagewise maximum, fully saturated menu:**

    parity of j      sup_(1<=rho<2) rho * k * (periodic maximum phase gap)    witness ratio t and prior gap*k
    even             160/63                                              t=11/8; prior gap*k=1280/693
    odd              1365/506                                            t=91/64; prior gap*k=480/253

Each value is the exact supremum of the *continuous-rho stagewise certificate bound*, approached from below at the stated entrance. The odd value dominates. This exactness does not assert that a particular integer H realizes equality, or that 1365/506 is optimal for all of S_H.

## Complete residue certificate and proof

The inherited complete projective certificate C_11(h,n) for positive integer exponent pair h,n is computed in the companion verifier. Its equivalent periodic test is

    C_11(h,n) = [ (h mod 10, n mod 10) belongs to P ] and [(9h+10n) mod 11 != 0],

where P consists of the 44 accepted residue pairs derived by checking every finite point z!=3 and the projective point. The z=3 collision is covered by the separate linear residual; the verifier also checks the original collision formula directly. It compares the complete direct projective test and the residue test for every 1<=h,n<=110 (12,100 comparisons).

In the common exact integer coordinate y=C k * (h/d), the ell-th layer has step

    s_(r,e,ell)=C * 2^e/(2^ell r)  (integer).

In one circle of length M, its formally periodic mask is

    P_(j,r,e,ell) = { s h: 1<=h<M/s, gcd(h,2r)=1,
                     C_11(h, r*2^(j+ell-e)-h)=1 }.

The residual predicate is evaluated via modular residues even at formal period points beyond the physical interval 0<h<d. For actual phases in [0,1], these points have 0<h<d and are valid reduced fractions. The extension is used only to measure interval gaps. The integer M/s = 14080*2^ell*r/2^e is divisible by lcm(110,2r) for each menu pair; hence the mask is genuinely periodic in y mod M. For positive exponents, 2^a mod 110 has period 20, so all cases j>=8 are represented by j=14,...,33. This proves that the finite set of 20 exact scans exhausts every dyadic scale.

At each entrance t in sorted order, form the union of the always-present ell=0 masks and all ell=1 masks with entrance <=rho. Between successive entrances this union is constant. If G is the maximum cyclic integer gap in the current period, then each phase interval longer than G/(Ck) hits the periodic union. On the half-open stage rho<t the height-weighted gap is bounded by t*G/C. Exhausting all 20 j-classes and all entrances produces the table above. The periodic mask restricted to (0,1) contains only genuine certified fractions; extending beyond [0,1] does not add an internal false witness. Consequently |I|>1365/(506 H) forces a certified fraction inside I.

**Restricted optimality.** D is the entire grid of odd divisors of this frozen L with r<=127 and ceil(log_2 r)<=e<=7. For the fixed two-scale ell={0,1} construction, deleting any layers only removes phase points at every rho, so cannot reduce the maximum-gap bound at any stage. Therefore 1365/506 is the least *continuous-height stagewise upper-bound constant* among all submenus of this declared 65-pair grid. This does not cover new odd factors, e>7, extra admissible levels or independent mod-p certificates.

## Reproducibility, scope and follow-up

Run the companion Python 3 standard-library verifier. It uses exact integers and Fraction, reconstructs P, checks 12,100 direct finite-field projective evaluations, computes every j mod 20 and every entrance with strict rational comparisons, and independently enumerates 24 finite-height fraction collections for j=8,9,10,11. Each full two-scale period has exactly 133,600 distinct points. The archived output terminates ALL PASS.

Source status: author proof and exact executable finite certificate; Bernoulli-to-projective reduction and scientific input remain parent-dependent; independent mathematical review, formal Result and admission are pending.

Next research: enlarge the arithmetic grid beyond divisors of L or use mixed-prime certificates; compare improvements against the exact 65-grid stagewise optimum. Investigate integer-H extremal constants separately from the continuous-rho upper bound, and preserve source provenance for overlapping fraction layers.
