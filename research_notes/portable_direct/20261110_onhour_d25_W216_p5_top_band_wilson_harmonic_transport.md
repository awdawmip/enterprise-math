# D25 / W216: exact p^5 upper-band Wilson–harmonic carry (research-onhour)

**Date:** 2026-11-10 +08. **Status:** AUTHOR_SIDE_EXACT_DERIVATION / EXACT_FINITE_CHECK / UNREVIEWED / NOT_ADMITTED / NATIVE_H0_B0_NOT_RUN.
**Original Task:** RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT.
**Publication:** TP2-B6F4FC938FF94941C1B7.
**Frozen scientific Source pin:** c47e13e4aba0e006366f989d6334d443f6333ae3.
**Research lane:** chatgpt-research-onhour-enterprise-math-20260923. Maintenance conversation is separate and is not an executor here.

## New unit and previously consumed result

The H40 author-side fourth-band note (2026-11-10_h40_d25_weighted_fourth_band_p4_author_portable.md, blob 806812e0a6e071fbb2e7fe57e2a30276d1e1aef5) proves the value of the original weighted top band modulo p^4, equivalently T_p/p^3 modulo p. Its two referenced reproducibility files were absent from canonical main at this reading. This independent research-onhour result **extends one precision digit** to T_p/p^3 modulo p^2 and supplies a new independently executable 3-route verifier. The H40 author's provenance is preserved; this is not a replacement of, adoption of, or review of H40's result.

Let p=6m+1 be prime with p mod24 in {13,19}; p>=13. Use the source-defined terms

a_k = (2k)!(3k)! / (216^k(k!)^5),  0<=k<p,
W_p = sum_(k=0)^(p-1)(6k+1)a_k,
T_p = sum_(k=4m+1)^(6m)(6k+1)a_k.

For k in the top band, v_p(a_k)=3 exactly. Put x=2k-p and y=3k-2p; both are in [0,p-1]. Let

H_n = sum_(i=1)^n 1/i  (mod p),
w_p = ((p-1)!+1)/p  (mod p), the Wilson quotient,
b_k = -2 x! y! / (216^k(k!)^5)  (mod p^2).

Every denominator is a unit modulo p^2. The following congruence holds **for every such p**:

    T_p/p^3  ≡ sum_(k=4m+1)^(6m)
         (6k+1)b_k [1+p(H_x+2H_y-3w_p)]  (mod p^2).       (1)

### Proof

For 0<=x<p, factor the first p-block in (p+x)!:

    (p+x)!/p = (p-1)! x! product_(i=1)^x (1+p/i)
             ≡ -x![1+p(H_x-w_p)]                         (mod p^2).

For 0<=y<p, factor both p-blocks in (2p+y)!:

    (2p+y)!/p^2
       = 2 ((p-1)!)^2 y!
           [prod_(i=1)^(p-1)(1+p/i)] [prod_(i=1)^y(1+2p/i)]
       ≡ 2 y! [1+2p(H_y-w_p)]                            (mod p^2).

Here H_(p-1) ≡ 0 (mod p) follows by inversion symmetry in the field, and (p-1)! = -1+p w_p (mod p^2). Multiplying the two identities and dividing only by p-unit factors 216^k(k!)^5 proves (1). No global W supercongruence is assumed.

Define base Fhat_p = sum (6k+1)b_k (mod p^2), F_p=Fhat_p mod p, and
J_p = sum ((6k+1)b_k mod p)(H_x+2H_y) (mod p).
Then (1) becomes the exact two-coordinate carry formula

    T_p/p^3 ≡ Fhat_p + p(J_p-3w_p F_p) (mod p^2).        (2)

This is a BRC source-grade precision transport: the prime-valuation carrier (k,3,b_k) is retained, and the p^5 observer requires both harmonic information and the Wilson quotient. At p^4 precision only F_p is visible.

## Independent finite checks

The accompanying standard-library Python checker preserves the original signed weight and compares three implementations:
(1) original coefficient recurrence modulo p^5; (2) direct factorial p-unit stripping for both numerator factorials modulo p^2; (3) the Wilson/harmonic first-jet formula (1).

All 312 primes 13<=p<=10000 with p mod24 in {13,19} passed all three checks in an actual run. JSON canonical row serialization (sorted keys, compact separators) has SHA256

    a135512864827fc7926a2a2672c2bbb207993d4abdb850854351d074d3ce3653

Each row contains p, T_p/p^3 mod p^2, F_p and G_p, where T_p/p^3 mod p^2=F_p+pG_p with representatives 0<=F_p,G_p<p.

| p | F_p (old precision) | T_p/p^3 mod p^2 (new) | G_p |
|---:|---:|---:|---:|
| 13 | 5 | 70 | 5 |
| 19 | 4 | 156 | 8 |
| 109 | 80 | 3677 | 33 |
| 139 | 58 | 6591 | 47 |
| 157 | 96 | 22547 | 143 |
| 163 | 107 | 12821 | 78 |
| 373 | 278 | 109567 | 293 |
| 997 | 347 | 655376 | 657 |
| 2131 | 756 | 756 | 0 |

In these 312 cases F_p is nonzero. The next digit G_p vanishes at p=2131, demonstrating that the second carry has its own cancellation structure even when the leading top-band residue does not vanish.

For p=157 the decomposition in (2) is: Wilson w_p=151, Fhat_p=1823, J_p=131, -3w_p F_p mod p=1; hence 1823+157(131+1) ≡22547 (mod 157^2). For p=373 the corresponding values are w_p=224, Fhat_p=48022, J_p=108, Wilson correction=57, giving 109567 (mod 373^2).

## Parent objective, limits and next precise action

This new p^5 coefficient is a source-preserving precision repair coordinate, not a completion of the frozen signed Delta_p-R_p cancellation. A useful next mathematics unit is to combine (2) with the existing original low/middle-band p^5 jets and seek cancellation of the full W_p-p (mod p^5) without deleting the new top-band coordinate. The frozen parent still requires all-prime Delta_p-R_p and, independently and with higher priority, native same-original-class p373 H0/B0 divided-power [X]U mod139129, rank, semilinear direction/eta, signed kappa and independent reproduction, currently NOT_RUN/PENDING_OWNER per existing Issue #1559. This note is author's GitHub evidence only; no Source-native CLAIM/OPEN, Result or Driver admission follows from it.
