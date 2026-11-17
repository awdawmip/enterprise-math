# R254 — Sharp common reduced denominator for all 63 labelled scalar masks

Scientific date: 2026-11-18 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_COMPUTATION / NOT_REVIEWED.

**Frozen scientific input:** 43ec6098b1330ae86d0a7863be336c5d97f6ef34. Direct predecessor: R253B, commit 2e7621e7c9783c333f6d6c03c68a887ed4b0f932. Also reuses the maskwise characteristic formula of R252 at e23e0150fc15b9a32df3c8b7cf94a5d9a83a07c9.

## Theorem (sharp common denominator, all event horizons)

Fix s=2/5 in the seven-source auxiliary **positive scalar observer** with the unchanged 63 proper-source masks m=0,...,62. Put D_m={0} union {i+1 : bit i of m is 1}, d_m=|D_m| and

h_{m,k}=W_{popcount(m)} rho_{D_m}^T P_{D_m}^k 1,
P_{D_m}[i,j]=a_i delta_{ij}+(1-a_i) pi_j, k>=0.

Denote by den(q) the positive reduced denominator of a nonzero rational q. For *every integer k>=3*:

**lcm_{0<=m<=62} den(h_{m,k}) = (2055053 / 7479000) * 299160^k.**

The right-hand side is an integer for k>=3. In the R252 event numbering n=k+1, this holds for every n>=4.

This is an exact, source-labelled common-denominator formula, stronger than the R253B construction with bound J L^k. Constants:

- J=2055053=7*11*13*2053;
- L=552847680=2^6*3^4*5*7*11*277, the full seven-by-seven matrix-entry denominator lcm;
- T=299160=2^3*3^3*5*277;
- K=7479000=2^3*3^3*5^3*277.

Consequently the common reduced denominator has bit length k log2(299160)+O(1), i.e. ~18.191 bits per event, instead of the earlier constructive upper bound ~29.042 bits per event. At k=64 the exact value has 1163 bits, versus 1880 bits for J L^64. This measures denominator encoding, not total output space or measured wall time.

## Proof, Part I — minimal integral spectral scaling

Write b_i=(1-a_i)pi_i. For each mask, the monic characteristic polynomial is

c_m(x) = product_{i in D_m}(x-a_i) - sum_{i in D_m} b_i product_{j in D_m,j != i}(x-a_j).

For its degree d_m, write c_m(x)=sum_{j=0}^{d_m} c_{m,j} x^j. The finite exact certificate evaluates all 249 non-leading coefficients and shows that

C_m(y) = T^{d_m} c_m(y/T) belongs to Z[y]  (every mask m),

where T=299160. The prime-adic required exponents obtained from *all* coefficients are:

max_{m,1<=j<=d_m} ceil(v_p(den(c_{m,d_m-j}))/j)
= 3 for p=2, 3 for p=3, 1 for p=5, 1 for p=277, 0 otherwise.

Thus T is the **least positive integer** making all scaled characteristic polynomials integral. This minimality is about characteristic-polynomial scaling and needs no claim about native model state compression.

## Proof, Part II — denominator divisibility for every k>=3

Let H_{m,k}=J T^k h_{m,k}. Cayley–Hamilton gives for H the integer-coefficient recurrence with monic characteristic polynomial C_m. Hence the sequence

q_{m,k}=H_{m,k}/K

obeys the same recurrence. Since 1<=d_m<=6, it suffices to prove integrality at the d_m consecutive exponents 3,...,d_m+2. The exact certificate recomputes all of these 249 rational values and checks their denominators equal 1. Induction over the integral recurrence then proves q_{m,k} belongs to Z for every m and k>=3.

Consequently den(h_{m,k}) divides the integer D_k=J T^k/K for all 63 masks.

## Proof, Part III — the denominator is attained prime by prime

Every prime dividing D_k is in {2,3,5,277,7,11,13,2053}. For each prime p, select a mask m and reduce its integer sequence q_{m,k} modulo p. The following witness table lists p, m, d_m, the initial nonzero residues (q_{m,3},...,q_{m,d_m+2}) modulo p and a nonzero recurrence unit u:

| p | m | degree | initial residues | u |
| --- | ---: | ---: | --- | ---: |
| 2 | 3 | 3 | 1,1,1 | 1 |
| 3 | 17 | 3 | 1,2,1 | 2 |
| 5 | 2 | 2 | 3,2 | 3 |
| 277 | 32 | 2 | 149,187 | 31 |
| 7 | 2 | 2 | 1,4 | 4 |
| 11 | 40 | 3 | 9,1,5 | 5 |
| 13 | 1 | 2 | 2,4 | 2 |
| 2053 | 0 | 1 | 752 | 1470 |

For every row except p=13, the scaled characteristic polynomial modulo p is y^(d_m-1)(y-u). Therefore for all k>=3+d_m the recurrence becomes q_{m,k}=u*q_{m,k-1} modulo p. All listed initial residues and u are nonzero, so q_{m,k} is nonzero modulo p for every k>=3.

For p=13, m=1, the characteristic polynomial is y^2+5y+12 modulo 13, and u=2 is a root. The initial residues 2,4 form a geometric progression of ratio 2. Thus the full sequence is geometric modulo 13 by the order-two recurrence, and nonzero for all k>=3.

For each prime p dividing D_k, some labelled numerator q_{m,k} is a p-adic unit. Its reduced denominator therefore retains the full p-exponent of D_k. The lcm of all 63 reduced denominators equals D_k. QED.

## Reproduction, scope and next research

The standalone standard-library verifier R254_sharp_common_denominator.py reconstructs the frozen a,b,pi,rho exactly at s=2/5; certifies 249 scaled characteristic coefficients, 249 finite integrality bases and eight modular witness recurrences, and independently compares exact denominator lcms at k=0,1,2,3,4,5,8,16,32,64. All listed comparisons returned PASS. These finite checks establish explicit premises of an infinite-horizon induction; the infinite claim rests on the displayed recurrence and modular arguments.

The retained population is all 63 labelled positive scalar mask contributions, with exact future powers P_D^k, not a native signed/port BRC equivalence. P000, ACTIVE Heartbeat World and frozen input are untouched. No formal CLAIM, Result/Review or independent mathematical review is asserted.

Next question: for a general rational s in (39/100,41/100), compute the minimum characteristic scaling T(s) and characterize the prime-wise sharp common denominator, including exceptional parameter values. Compare actual reduced-fraction reconstruction and compressed powering costs for k up to at least 1000, with parameter height accounted for. The continuous-real-parameter two-mode thresholds 270/403 remain open.
