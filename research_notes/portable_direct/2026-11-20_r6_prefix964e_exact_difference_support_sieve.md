# PREFIX-964E — Exact signed-residual difference sieve and gap-zero rigidity

Date: 2026-11-20. Status: **AUTHOR_PROOF / EXACT_INTEGER_TESTED / NOT_REVIEWED**.
Research type: auxiliary named-XOR integer observer (no native Heartbeat-X6/BRC event admission).
Scientific input freeze: `f42f2906d77f24085c123f3ccfe9667d41caa96d` (retained from PREFIX-963).
Continuation: PREFIX-957B (numeric signed-residual dictionary), PREFIX-958 (divisor pivot), PREFIX-959B (odd-fiber cache), PREFIX-960 (universal gap 0..6), PREFIX-963 (coarse interval support).
Historical provenance: EM-DIRECT-58C410; public identifier alone is not active CLAIM or present execution authority.

## 1. Exact question and objects

For p>=4 let H=2^(p-1), N=2^(p-2), and Q_p={H+1,H+3,...,2H-1}.
The two named XOR collisions for odd adjacent cores k,k+2 have signed residuals
c=2^i-s*2^j, C=2^I-S*2^J with 0<=i,j,I,J<p, signs s,S in {+1,-1} fixed by actual XOR source bits. Their quotient gap m=T-t satisfies

    2*a-m*b=C-c, a,b in Q_p.                                 (1)

Define the **value** dictionary D_p={2^i-s*2^j: 0<=i,j<p, s=+/-1} and difference support E_p={C-c: c,C in D_p}. Define

    S_p(m) = #{(a,b) in Q_p^2: 2*a-m*b belongs to E_p}.       (2)

This retains only the possibility of a numeric signed-residual difference. Every genuine named XOR witness satisfies (2); (2) is not sufficient for a named witness because bit-derived signs, individual source slots, positive quotients and their multiplicity still need checking. The full uncompressed (c,C,i,j,I,J,s,S,t,T,a,b) record is retained on any downstream witness-producing route.

This sieve is a **pair-first** algorithmic alternative. The PREFIX-959B generator starts from (c,C) themselves and therefore *already satisfies* (2) identically; inserting this test into that generator cannot discard its candidates. Such a tautological insertion is NOT a claimed optimization.

## 2. Theorem 964E.1: exact fiber count for every fixed gap

Let delta be an integer, 0<=m<=6 and set

    V=delta-(2-m)*(H+1).

If V is odd the number of ordered modulus pairs with 2*a-m*b=delta is zero. Otherwise W=V/2. For m odd, put z0=W mod 2 (0 or 1), r0=(W+m*z0)/2, h=m, L=2. For m even, the fiber is empty unless W is even; when W is even put z0=0, r0=W/2, h=m/2, L=1.

For m=0 the number is N if 0<=r0<N and zero otherwise. For m>0 let

    q_lo = max(0,ceil(-r0/h)),
    q_hi = min(floor((N-1-z0)/L),floor((N-1-r0)/h)).

Then the exact number of pairs is max(0,q_hi-q_lo+1). All ceilings/floors are mathematical integer operations (no floating point).

**Proof.** Write a=H+2r+1 and b=H+2z+1 with 0<=r,z<N. Equation (1) is equivalent to 2r-mz=W. For odd m the parity of W forces z=z0+2q, whence r=r0+mq. For even m, W must be even and r=W/2+(m/2)z. In either case q is an integer bounded by the two square-coordinate inequalities, giving the stated intersection of two integer intervals. The m=0 case is a constant r with N choices of z. QED.

Consequently, the exact S_p(m) is obtained by summing these O(1)-arithmetic fiber counts over **distinct** delta in E_p. The dictionary has O(p^2) distinct possible values and E_p has at most O(p^4) values; with unit-cost integer arithmetic this is an O(p^4) construction and count, independent of the exponential number N^2 of ordered pairs. The bit complexity includes integer length O(p), set construction and sorting/hashing; no claim of constant-bit-time arithmetic is made.

## 3. Theorem 964E.2: complete rigidity of the gap-zero *necessary support*

For every p>=4,

    2*a belongs to E_p with a in Q_p
       if and only if a=H+2^r-1 for exactly one r in {1,...,p-2}.

In particular,

    S_p(0)=(p-2)*N
    and the diagonal support count is exactly p-2.

**Proof.** Every element c in D_p obeys 1-H<=c<=2H. If C-c=2a>2H, necessarily C>H and c<0. A positive dictionary value above H is either C=2H or C=H+2^e for 0<=e<=p-2, because sums of two powers each <=H/2 cannot exceed H. A negative dictionary value is c=2^i-2^j with i<j. If j<=p-2 then c>=1-H/2; combining it with C<=3H/2 (unless C=2H) yields C-c<2H, so the only possible negative residuals have c=2^i-H, 0<=i<=p-2. (For the exceptional C=2H this conclusion also holds: if j<=p-2, C-c<=2H+(H/2-1), which is below 2H+2 only for some c but could exceed 2H. Treat that branch separately below.)

Case C=H+2^e. Since C-c=2H+2^e-2^i>2H, e>i. And 2a=2H+2^e-2^i is 2 modulo 4 because a is odd, H>=8. The only possible power pattern is i=1, e>=2. Thus a=H+2^(e-1)-1 with 1<=e-1<=p-3.

Case C=2H. Here the parity restriction is 2a=2H+(2^j-2^i) with c=2^i-2^j. To have 2a>2H, j>i. If j<=p-2, then 2a<=2H+H/2-1 < 2H+H, corresponding to a in Q_p, and this may yield extra solutions; but such a=H+(2^j-2^i)/2 are odd only when i=1 and j>=2. These give a=H+2^(j-1)-1 for 2<=j<=p-2, already in the previous family. If j=p-1, the same congruence gives i=1 and a=3H/2-1=H+2^(p-2)-1, the last family member.

For each 1<=r<=p-3, the explicit values c=2-H and C=H+2^(r+1) realize 2a=2H+2^(r+1)-2. For r=p-2 take c=2-H and C=2H. Therefore the listed family is exact and has p-2 members. For m=0 the value of b is arbitrary in Q_p, giving (p-2)N ordered pairs and p-2 diagonal pairs. QED.

**Interpretation:** Under a pair-first scan, gap zero is supported only at p-2 possible first moduli, despite the coarse interval sieve of PREFIX-963 admitting N/2 choices of a. This is a necessary-support statement; it does not assert that all these a admit genuine XOR signs for any fixed k.

## 4. Exact computational certificates

The accompanying `PREFIX964E_R6_EXACT_DIFFERENCE_SUPPORT.py` constructs D_p from all (i,j,s), deduplicates E_p, and evaluates Theorem 964E.1 using integer arithmetic. For p=4,...,10 it **independently enumerates all** N^2 ordered odd-modulus pairs for each of seven gap values and compares Boolean E_p membership with the fiber counts. Every comparison passes. Theorem 964E.2 was additionally checked by direct a-membership for p=11,12,16,19,25. For p=19 all seven counts are exact sums over the 33,125 distinct integer differences; no pair enumeration or statistical approximation is used.

For p=19 (N=131,072), the columns are gap m=0,1,2,3,4,5,6:

| m | PREFIX-963 coarse A_p(m) | Exact difference S_p(m) | Retained versus coarse |
|---|---:|---:|---:|
| 0 | 8,589,934,592 | 2,228,224 | 0.02593994% |
| 1 | 17,179,869,184 | 84,066,235 | 0.48932989% |
| 2 | 17,179,869,184 | 1,894,922,992 | 11.02990350% |
| 3 | 15,748,213,419 | 165,674,888 | 1.05202339% |
| 4 | 8,589,934,592 | 38,920,139 | 0.45309005% |
| 5 | 3,435,973,837 | 1,186,231 | 0.03452387% |
| 6 | 715,816,960 | 611,676 | 0.08545145% |

The p=19 residual dictionary contains 499 numeric values (consistent with PREFIX-957B); the difference set contains 33,125 distinct integers, with extrema +/-786431. The full integer output and all smaller-width evidence are in `PREFIX964E_R6_EXACT_RESULTS.json`.

## 5. Observer fidelity, source, and next work

The map from full named-source configurations to (c,C) and then delta=C-c is many-to-one. This sieve only establishes an **inclusion** of all valid named witnesses in a candidate-pair support. It must be used as a rejection-only filter with the original named sources, sign bits, quotient conditions and multiplicities restored in the actual witness verifier. No operation-preserving map into native P000 X6 Cell/Port/time triadic-event dynamics has been established. The integer gcd/floor counts are auxiliary arithmetic, not an implicit substitute for typed BRC native arithmetic.

A useful next discriminating experiment is an actual end-to-end comparison of (i) ordered pair scanning with this exact E_p membership sieve and later source recovery, versus (ii) the existing PREFIX-959B source-first odd-divisor-fiber generator. Every preprocessing, reconstruction and verification cost needs to be included; the count reduction above is **not** a measured runtime speedup.

Sources (same frozen family): `2026-11-20_r6_prefix963_all_gap_coarse_support_spectrum.md`, `2026-11-20_r6_prefix962_gap5_exact_one_fifth_support.md`, `2026-11-20_r6_prefix961_gap6_endpoint_triangle_and_source_localization.md`, `2026-11-20_r6_prefix959b_odd_divisor_fiber_memo.md`, `2026-11-20_r6_prefix957b_numeric_residual_determinant_full_joint.md`. Author proof and finite exact tests; independent review not yet undertaken. No CLAIM, Result or review status is changed by this note.
