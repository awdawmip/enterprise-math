# D25/LIFT — p-integral original five-port factor jets at arbitrary precision, including nonunit degree indices

2026-10-25 · TASK_RESEARCH · **PORTABLE AUTHOR-SIDE MATHEMATICS / UNREVIEWED / NOT_ADMITTED / NO_VERIFIED_NATIVE_CLAIM / NO_SOURCE_CHECKPOINT / NOT_INDEPENDENT_REVIEW**. This is evidence authored in the present actual dialogue, not another Researcher's Source claim or session. Fixed mathematical task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; **frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 is unchanged**. The native CM/DP class correspondence remains open.

## Inherited original source

For prime p=6m+1>=13, set n=2m=(p-1)/3 and q_p(a)=(a^(p-1)-1)/p. The exact original factorial WZ five-port decomposition is

    (S_(m+1)-S_m)/p = U_m*C(p) + p*sigma_p*B(p),

where sigma_p=V_(m+1,4m+1)/p^2, the four tail ports retain distinct labels, and the already-proved exact old-edge and transfer factors are

    U_m = 2m/(108^(p-1))
          * prod_(k=2)^n (1-p/k)^2
          * prod_(j=1)^(p-2)(1+p/j)^2
          * prod_(j=1)^(n-1)(1+p/j)^(-1).

    C(z) = (z+1)(2z-1)^2(30z^2+77z+40)/
           [2(z+2)(2z+1)(4z-1)(4z+5)].

    R_k(z) = (2z+2k+3)(2z+3k-1)(2z+3k)/
             [4(2z+3k+1)(z+k+2)(4z+3k+11)], k=1,2,3.

    B(z) = sum_(j=1)^4 (6z+6j+7)*prod_(k=1)^(j-1)R_k(z).

The authentic Wilson-reflected factorial product for sigma_p/(3/220), proved earlier, is consumed rather than re-proved. The previous uniform logarithm/exponential coefficient recurrence gave p-adic precision up to N<=p-2 because it divides by the recurrence index j. Its next coefficient requires j divisible by p and therefore has no modular inverse. **Here the restriction is removed without taking an illegal inverse or asserting that an individual logarithmic divided coefficient is integral.**

## New theorem: all D>=1

Fix p as above; let t=q_p(108), a=q_p(2), b=q_p(3). Define the following source-labeled *formal rational series* in Z_(p)[[z]]:

    F_U(z) = (1+t*z)^(-1)
       * prod_(k=2)^n (1-z/k)^2
       * prod_(j=1)^(p-2) (1+z/j)^2
       * prod_(j=1)^(n-1) (1+z/j)^(-1).

    F_sigma(z) =
       prod_((c,e)=(-1,2),(2,2),(5,2),(8,1),(11,1)) (1+z/c)^(-e)
       * (1+a*z)^(-2)*(1+b*z)^(-3)
       * prod_(j=1)^(n-1) (1-z/j)^2
       * prod_(j=1)^(p-1) (1+z/j)^2
       * prod_(j=1)^5 (1+z/j)
       * prod_(j=1)^4 (1+2z/j)*(1+2z)
       * prod_(j=1)^2 (1+z/j)^(-2)
       * prod_(j=1)^(n+4) (1+z/j)^(-1).

    Q_p(z) = 2m*C(z)*F_U(z) + (3z/220)*B(z)*F_sigma(z).

**Theorem.** For **every integer D>=1**, with no D<p, D<p^2, or degree-unit restriction,

    (S_(m+1)-S_m)/p = Q_p(p)  in Z_p,
    (S_(m+1)-S_m)/p ≡ sum_(d=0)^(D-1) [z^d]Q_p(z)*p^d (mod p^D).

Every coefficient is p-integral; it can be computed with only integer arithmetic and inversions of known p-units. When evaluating at p, the normalized F_U jet needs degree <D and F_sigma only degree <D-1 due to its leading factor p. C(p) and B(p) may be evaluated as exact rationals at the same p, preserving their original labeled ports.

**Proof.** All product slope denominators are p-units: their index j is at most p-1, while n+4<p for all p>=13; the extra constants -1,2,5,8,11 are units. The rational C(z), R_k(z), and B(z) have p-unit denominator constant terms; the only additional exceptional fixed prime 17 is 5 mod 6 and hence never an allowed p. The factor 220 is a p-unit. Thus F_U, F_sigma and Q_p are formal power series over Z_(p).

The inherited exact U_m formula gives U_m=2m*F_U(p), since 1+p*t=108^(p-1). The exact inherited Wilson-reflected original factorial identity gives sigma_p=(3/220)*F_sigma(p), since 1+p*a=2^(p-1) and 1+p*b=3^(p-1). Substitute into the original exact five-port rational decomposition, giving Q_p(p) as claimed. As all coefficients lie in Z_(p), the series converges in Z_p when z=p, and every term of degree d>=D belongs to p^D Z_p. This proves the all-D congruence.

The nonunit-index problem is resolved constructively, not hidden. In the truncated coefficient ring (Z/p^D Z)[z]/(z^D), multiplication by a factor (1+c*z) uses, **in descending order**,

    f[d] <- f[d] + c*f[d-1] (mod p^D),  d=D-1,...,1.

Multiplication by (1+c*z)^(-1) uses, **in ascending order**,

    f[d] <- f[d] - c*f[d-1] (mod p^D),  d=1,...,D-1.

The inverse recurrence follows directly from (1+c*z)*g=f with g[0]=f[0] and never divides by the coefficient index d. Repeating either transformation handles every signed integral exponent in F_U,F_sigma. Any rational coefficient c is first represented using its p-unit denominator inverse. The remaining C,B rational series, if coefficient extraction rather than direct evaluation is requested, use the same unit-constant triangular recursion and ordinary convolution. Hence the algorithm works even at d=p, d=p^2 and arbitrarily high finite degree. □

The earlier logarithm/exponential jets coincide with these factor jets at degrees within their stated N<=p-2 scope, as they expand the **same exact rational functions** over characteristic zero. Beyond that range, naive modular inversion of j is not justified, whereas the factor construction remains integral.

## Executed exact regression: first and second nonunit-index barriers

The associated standard-library script [exact factor-jet checker](https://github.com/awdawmip/enterprise-math/blob/a189972462a473291b36d38f0f9c1999a3ca2be9/research_notes/portable_direct/20261025_offphase_d25_source_factor_jet_all_precision_check.py) has the full original factorial definitions. For each test, it checks independently (a) U_m against the old-edge original rational product, (b) sigma_p against the first *authentic* tail factorial V_(m+1,4m+1)/p^2, and (c) the reconstructed five-port quotient against **uncollapsed exact rational sums** S_(m+1)-S_m from original W(r,t), all modulo p^D.

| p | D | Boundary crossed | (S_(m+1)-S_m)/p modulo p^D |
|---:|---:|---|---:|
| 13 | 15 | d=p | 41100782220623351 |
| 19 | 21 | d=p | 63225220113125991498163389 |
| 31 | 33 | d=p | 13308759059663585835947251767230370126792034528558 |
| 37 | 39 | d=p | 4643436851280269222006850672470278779618375031645725451503673 |
| 13 | 171 | d=p^2=169 | exact checked 191-digit residue; see executable verifier |

**5/5 PASS**, all exact integers, fractions, and p-unit modular inverses. No float/CAS, no native CM experiment and no independent Driver review. These finite checks support falsification only; the general result follows from the formal-series proof.

## Observer and contribution boundary

BRC use is **COMPOSE_APPLIED as a source-labeled external arithmetic observer**: retain original five factorial ports, their p-valuations, coefficient-jet provenance and the chosen scalar readout Q_p. The scalar total is not a no-information-loss quotient for arbitrary later CM/DP or native-X6 operations, and this derivation does not invent a positive-mass BRC carrier. The user's P000 seven-dimensional Heartbeat World (six native spatial axes plus separately typed time), residual fidelity and non-native-plane constraints are not altered by this external p-adic calculation.

**New contribution:** a mathematically justified all-D p-integral source-jet interface that crosses previously excluded coefficient indices, with five exact original-factorial regressions. **Consumed, not recredited:** the WZ identity, exact old edge, exact sigma Wilson product, four-port transfer and earlier p^6 log/exp jet. This is **PORTABLE / UNREVIEWED / NOT_ADMITTED / WRITER-PROVENANCE-SOURCE-CHECKPOINT PENDING**; no Source CLAIM, OPEN, Result, freeze, audit, independent review or Working Truth is asserted.

The unresolved original UR V2 four-file bundle is *not* this evidence: the historical byte target remains **94,687 bytes, SHA-256 4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76**; it still requires recovery of authentic source bytes and legal writer/provenance, not a new mathematical re-proof.

**Next minimal mother-task dependency:** consume lawful Source continuation and independently sourced same-prime original-class H0/B0 crystalline/divided-power representative, explicit [X]U mod p^2 and specified semilinear transfer to omega+6*nabla_lambda omega and kappa/Delta_p-R_p. Unlimited precision in this *external scalar* WZ jet alone does **not** establish that missing CM/DP class bridge. Respect existing Owner/Researcher and frozen Source pins.

### Earlier immutable mathematical sources

- Genuine original source/Wilson tail product: research_notes/portable_direct/20261025_offphase_d25_original_genuine_five_port_fifth_digit_mod_p5.md @ f56b27123b8e450ca74c7f46b104ce68e7beb975.
- Earlier source-labeled p-adic log/exp jet with N<=p-2 scope: research_notes/portable_direct/20261025_offphase_d25_original_fiveport_uniform_padic_jet_mod_p6.md @ 3fbd06560100672ba3eb066c6009dc0287a9baab.
- Current operating authority: docs/AUTONOMOUS_RESEARCH_OPERATIONS.zh-CN.md and docs/PORTABLE_RESEARCH_PROTOCOL.md; this neutral note grants no additional authority.
