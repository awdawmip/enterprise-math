# PREFIX-949 — Sparse nonzero resonance theorem for adjacent odd XOR cores, with exact Q19 census

Date: 2026-11-20. Predecessors: PREFIX-947A (adjacent-core gap) and PREFIX-948/948B (determinant inversion and exact W21∩W23). Frozen scientific pin: \`f42f2906d77f24085c123f3ccfe9667d41caa96d\`. Model: auxiliary named XOR two-port trace observer. This note does not assert a native Heartbeat-X6 or typed BRC computation. Claim status: AUTHOR_PROVED / TWO_EXACT_FINITE_COUNTERS_AGREE / NOT_INDEPENDENTLY_REVIEWED / NOT_ADMITTED.

## 1. Question and definitions

Let k≥7 be odd; its adjacent odd core is l=k+2. Let the permitted source-bit indices be 0≤i,j,I,J'≤B, and let positive moduli a,b and quotients t,T obey

  (k*a XOR 2^j) - 2^i = t*b,                           (1)
  (l*a XOR 2^J') - 2^I = T*b.                          (2)

The start of the first trace is k*a; the second starts at l*a. Under the strict Q19 observer, a,b range through the 131072 odd integers from L=262145 to U=524287, B=18, and all trace endpoints must be in [0,2^32). Preserve the named bits, both separate starts and both observation ports.

Put s=1-2 bit_j(k*a), S=1-2 bit_J'(l*a), c=2^i-s2^j, C=2^I-S2^J'. Then

  k*a-t*b=c,        l*a-T*b=C.

We call the simultaneous configuration **resonant** precisely when d=l*t-k*T=0. The old determinant theorem covers d≠0. A nonzero resonance is resonant with (c,C)≠(0,0); it is not the automatic zero-offset diagonal family.

## 2. Universal signed-bit resonance spectrum theorem

**Theorem.** For ANY maximum bit index B≥1 and odd adjacent cores k≥7, a nonzero resonant *actual* witness to (1),(2) is possible only if

  k=2^m-1,    3≤m≤B-1.

Moreover every such witness necessarily has, for an integer v with 1≤v≤B-m and a positive integer r,

  t=k*r,    T=(k+2)*r,    a-r*b=2^v,
  i=m+v,    j=v,          s=+1,
  I=v,      J'=m+v,       S=-1,                        (3)

and satisfies the actual sign bits

  bit_v(k*a)=0,    bit_(m+v)((k+2)*a)=1.              (4)

Conversely (3),(4), positive allowed moduli and legal state endpoints imply two genuine named collisions. Consequently, for k≥7 outside the Mersenne list there are NO nonzero resonant joint-witness configurations, independent of a,b,t,T or the modulus range.

**Proof.** Since gcd(k,k+2)=1, d=0 implies t=k*r and T=(k+2)*r with r≥1 an integer. Eliminating a,b gives (k+2)c=kC and hence c=k*h,C=(k+2)*h with integer h. If h≠0, c and C have equal sign and 2-adic valuation. Divide their absolute values by the common 2-adic power 2^v: obtain positive odd p=k*u and q=(k+2)*u with q>p and u odd.

Every nonzero signed difference 2^i-s2^j, after removing its 2-adic power, has odd part belonging to O={2^n-1,2^n+1:n≥1}. Thus p,q∈O and q/p=(k+2)/k≤9/7. Represent p=2^m+e and q=2^n+f, e,f∈{-1,+1}. Because q>p, n≥m (a lower exponent cannot produce a larger number, including the small duplicate 3). If n≥m+1 and m≥2, then q/p≥(2^(m+1)-1)/(2^m+1)≥7/5>9/7, contradiction. For m=1, p≤3 and the next strictly larger admissible odd q is at least 5 when p=3 (or 3 when p=1); its ratio is again >9/7. Therefore n=m, with e=-1,f=+1. The ratio gives u=1, k=2^m-1, m≥3, and h=±2^v.

A negative signed two-power difference is necessarily 2^i-2^j with j>i, and its odd part is 2^(j-i)-1. Since negative C would require odd part 2^m+1 with m≥3, negative h is impossible. Hence h=2^v>0. The unique two-power signed expressions for c=2^v(2^m-1) and C=2^v(2^m+1) force exactly the source positions and signs in (3). Because k*a is odd, bit_0(k*a)=1; sign s=+1 requires v≥1. The bit window imposes m+v≤B. Substitution into the linear equations proves a-rb=2^v and the converse. QED.

This is a statement about the *resonant subset* of joint collisions. The determinant-nonzero subset may still contain off-diagonal pairs for k not in the Mersenne spectrum; e.g. PREFIX-948's k=21/23 has 6203 off-diagonal common pairs, all nonresonant.

## 3. Sharp strict-Q19/32-bit corollary

**Corollary.** With B=18, a,b∈Q19 and the 32-bit legal trace bound, an off-diagonal nonzero resonant adjacent-core pair for odd k≥7 exists if and only if k=2^m-1 for some 3≤m≤13. Each actual witness has r=1, t=k,T=k+2 and a-b=2^v for 1≤v≤18-m.

**Proof.** Since a<2b throughout Q19, a-rb=2^v>0 requires r=1. The 32-bit bound requires (k+2)a<2^32; if m≥14, then (2^m+1)(2^18+1)>2^32, so no witness is legal. For every 3≤m≤13, take a=262147=2^18+3, b=262145=2^18+1, v=1, i=m+1,j=1,I=1,J'=m+1. Modulo 4, (2^m-1)a≡1, so bit_1(k*a)=0. Since m+2≤15<18, a≡3 mod 2^(m+2), and (2^m+1)a≡3(2^m+1), whose bit m+1 equals 1. Both starts and endpoints are 32-bit legal. The exact equations are

  ((k*a XOR 2)-2^(m+1)) = k*(a-2) = k*b,
  (((k+2)*a XOR 2^(m+1))-2) = (k+2)*(a-2) = (k+2)*b.

This explicitly supplies the converse and proves sharpness. QED.

For k=21,23 the non-Mersenne obstruction proves the PREFIX-948 zero-nonzero-resonance fact *symbolically*, without a 722-pattern search. The pre-existing 131071 zero-offset diagonals and 6203 determinant-nonzero off-diagonals remain unchanged.

## 4. Exact number of nonzero resonant ordered pairs for eligible cores

Distinct pairs are counted once because (a,b) determines a-b=2^v and therefore its unique v. For each m, put k=2^m-1, l=k+2, L_m(v)=262145+2^v and U_m=min(524287,floor((2^32-1)/l)). Count odd a in that interval satisfying (4). The results for the COMPLETE declared Q19 population, independently computed by a direct odd-a scan and a congruence-residue floor count, are:

| m | (k,k+2) | distinct off-diagonal nonzero-resonant pairs |
|---:|---:|---:|
| 3 | (7,9) | 485798 |
| 4 | (15,17) | 456313 |
| 5 | (31,33) | 424864 |
| 6 | (63,65) | 392657 |
| 7 | (127,129) | 360193 |
| 8 | (255,257) | 327553 |
| 9 | (511,513) | 294784 |
| 10 | (1023,1025) | 262144 |
| 11 | (2047,2049) | 229376 |
| 12 | (4095,4097) | 196608 |
| 13 | (8191,8193) | 163760 |
| 14 | (16383,16385) | 0 (32-bit source bound) |

All m=3..14 and all v=1..18-m were checked; both counters agree for every (m,v), not just the row totals.

Independent counter B uses residue period P=2^(m+v+1). Let R be the odd residues x mod P with bit_v(kx)=0 and bit_(m+v)(lx)=1. Its exact count is

  sum_{x in R} [floor((U_m-x)/P)-floor((L_m(v)-1-x)/P)].

This finite sum contains every admissible odd a exactly once. It does not reconstruct pairs or use the direct scan. Counter A scans all admissible a, retaining the actual two signs. Both have exact integer semantics and no numerical tolerances. The attached source and result JSON allow repetition.

## 5. Scope, interpretation and next research

The table counts structural nonzero-resonance **joint-overlap** witnesses, not disjoint additions to the PREFIX-948 historical certificate union. This turn makes no new net coverage claim; the previous conditional 7,597,037,839 total remains unchanged. The finite source-bit cap, positive odd moduli, named bit signs and 32-bit event states are essential. P000 and the joint-relation preservation contract prohibit treating these auxiliary two-port projections as native six-axis dynamics or discarding the original named joint relation.

Next: for any *non-Mersenne* adjacent odd cores, exploit the proved absence of d=0,c≠0 to count the determinant-nonzero off-diagonal joint pairs by CRT residue grouping without constructing large globally sorted overlap sets; separately seek an exact formula for C_(m,v) above and test whether the Mersenne-family resonant overlaps survive historical certificate-priority subtraction. Mother objective B_fix,odd(32)∈{19,20} is still OPEN.

Historical R6 original provenance: researcher EM-DIRECT-58C410; SID MCP-31edc522830749ad8775ca012e02ef30; Activity RA-25432C4AAE9BF66A907F5115. This note is not a CLAIM, formal PROGRESS, Review or authority assertion. Original PREFIX-946 safety-rejected publication was not retried or routed elsewhere.
