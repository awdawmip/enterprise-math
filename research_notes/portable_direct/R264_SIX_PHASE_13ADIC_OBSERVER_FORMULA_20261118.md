# R264 — six-phase affine 13-adic observer with exact valuation and period

Date: 2026-11-18 (Asia/Shanghai). Status: **AUTHOR_PROVED / EXACT_COMPUTATION / NOT_REVIEWED**.

## Sources and exact scope

Independent, non-overwriting continuation of R260–R263 in the **auxiliary 63-mask positive-rational scalar model**. Frozen science pin: \`43ec6098b1330ae86d0a7863be336c5d97f6ef34\`. Parent: \`R263_ONE_MASK_PRECISION_REVERSAL_20261118.md\` at source commit \`a21165ac0d4bc144a3d405a468c041b419fc2bd8\`. Fix \`s=67/169\`, \`J=1184397599\`, \`T=989553240\`, \`K=3805974000\`. For original mask 57 and each k≥3, let q_(57,k) = J T^k h_(57,k) / K, an exact integer.

## Theorem

Write n=k−3=6t+r uniquely, with 0≤r<6 and t≥0, and let c=(54,58,150,4,156,155). For every integer k≥3,

\[
\boxed{q_{57,k}\equiv16\cdot144^{k-3}+38\cdot101^{k-3}
             \equiv c_r14^t\equiv c_r(1+13t)\pmod{169}.}
\]

Consequently the exact 13-adic valuations of these integers satisfy

\[
\boxed{v_{13}(q_{57,k})=
\begin{cases}1,&k\equiv1\pmod6,\\0,&k\not\equiv1\pmod6.\end{cases}}
\]

The output's least period modulo 13 is 6, and modulo 169 is 78. For **every integer a≥2**, singleton {57} is an optimal zero-only original-labelled observer for the predicate “all 63 masks simultaneously vanish modulo 13^a” at all k≥3. The smallest input count is exactly 1.

## Proof

**Model reconstruction.** Use the frozen s, J, T, K, and the R260 exact rational formula for the seven transitions and stationary weights. The attached standalone Python checker independently derives the mask-57 characteristic polynomial and first five normalized values. It obtains, in ascending polynomial order,

\[
C_{57}(x)=x^5+2x^4+166x^3+104x^2
=x^2(x-91)(x-101)(x-144)\pmod{169},
\]

and q_(57,3),…,q_(57,7) ≡ (54,58,150,4,156) (mod 169).

**Two roots suffice.** Define f_n=16·144^n+38·101^n (mod169). Both bases are roots of the characteristic polynomial, so f obeys the same monic fifth-order recurrence. Direct substitution shows f_0,…,f_4=(54,58,150,4,156). Monicity gives uniqueness over the ring Z/169Z by induction, so q_(57,3+n)=f_n for every n≥0. No division in the ring is used.

**Six-phase reduction.** Modular arithmetic gives 144^6=101^6=14=1+13 (mod 169). Hence f_(6t+r)=14^t f_r, and its six seed values are exactly c. The binomial theorem gives 14^t≡1+13t (mod169). The full sequence is therefore computable from r=n mod6 and t mod13 without a 78-term trajectory lookup.

**Sharp valuations.** Each c_r is nonzero modulo169. The six reductions modulo13 are (2,6,7,4,0,12); the unique 13-multiple is c_4=156=12·13. Since 14 is a unit, v13 of every exact integer q_(57,k) is 1 if r=4 and otherwise 0. The r=4 condition is k≡1 (mod6).

**Exact least periods.** Reducing the root expression modulo13 gives q_(57,3+n)≡3−10^n. The unit 10 has order 6 modulo13, hence the least mod13 output period is 6. The six-phase formula yields period 78 modulo169 because 14^13=1. Any mod169 period H must be a multiple 6h; comparing the value at n=0 gives 54(1+13h)=54 (mod169). Since 54 is a unit modulo13, 13 divides h. Thus 78 divides H, so 78 is the least period.

**All higher precisions.** For a≥2, q_(57,k) is never zero modulo13^a because v13(q_(57,k))≤1. Therefore the full 63-mask all-zero predicate is false at every event; the same is true of the singleton {57}. The empty conjunction is always true and cannot suffice, proving optimality 1 for all a≥2. At the R256 exception indices k=1093 and 2185, the affine formula gives q_(57,k)≡156 mod169, recovering the one-layer residual exactly.

## Reproducible evidence

The accompanying \`R264_six_phase_mod169_certificate.py\` uses Python standard-library Fraction and exact integer modular operations. It rebuilds the rational model, verifies its characteristic and the five initial outputs, factors the polynomial, checks the two-root/phase identities, the unit orders, least periods and exception witnesses, and writes \`R264_verification.json\`. It was executed locally on 2026-11-18 and returned \`R264 PASS\`; no floating-point computation. The induction and ring identities above extend the finite certificate to all integers k≥3.

The result preserves the *original named source label* in an **auxiliary positive-scalar observer**. It does not claim a signed native BRC Cell/Link/Port mapping; that remains an independent typed-mapping question.

## Next open unit

Classify which rational parameters permit a common zero to survive at prime-square depth, and derive a general Hensel/geometric-phase criterion that finds singleton nonvanishing witnesses without full global-period enumeration. Retain R256–R263 as precedent without repeating their original period search.
