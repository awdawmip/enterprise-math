# R5 — First overlap correction at N^92, with explicit finite-m sums

Date 2026-11-20. Third scientific increment in the same portable scalar nonadaptive research branch and frozen source. Author proof with independent integer combinatorial checks; NOT_REVIEWED.

## Statement

Retain the definitions of exact-cost query count, m=2f+e+1>=1, and five inclusion-minimal separating witnesses A,B,C,M,L from RESEARCH_R5_DEFECT_EXPONENT.md. Let E_S(N) count unordered query multisets of paid total N in which set S has at most m-1 occurrences. Define the exact individual counts A_m(N)=|E_A(N)|, B_m(N)=|E_B(N)| and C_m(N)=|E_C(N)|.

Set P8 = product_{k=222}^{314} k (93 unrestricted prices). Define three finite *integer* counts from the eight early labels:

AB_m = sum_{c=0}^{m-1} binom(c+2,2) sum_{r=0}^{m-1-c} (r+1)binom(r+3,3),

BC_m = sum_{s=0}^{m-1} binom(s+5,5)(m-s)^2,

ABC_m = sum_{0<=c,d, c+d<=m-1}
          binom(c+2,2)binom(d+2,2)
          [ (r+1)^2 - h(h+1)/2 ],

where r=m-1-c-d and h=max(r-d,0).

Then for **each fixed positive integer m**, as the exact integer price N tends to infinity,

Delta_m(N) - A_m(N) - B_m(N) - C_m(N)
 = R_m N^92/(92! P8) + O_m(N^91),

where R_m=ABC_m-2AB_m-BC_m is a **strictly negative integer**. Thus the first overlap (inclusion-exclusion) correction appears at order N^92, exactly one power after the seven-label B/C correction of order N^93. This theorem is a refinement in the count of scalar fixed-query designs, not an X6/native-path statement.

## Proof

For any query multiset let a be the count of label 214, b the count of label 215, c the total count across 216,217,218, and d the total count across 219,220,221. For fixed c and d there are binom(c+2,2)binom(d+2,2) distinct allocations among the six corresponding labels. The three early failure inequalities are

A: a+b+c <= m-1;
B: a+c+d <= m-1;
C: b+c+d <= m-1.

Any two failures jointly bound the multiplicities of all eight early labels: each of 214,...,221 belongs to at least one of their two separating sets, and the sum of the two witness counts is at most 2(m-1). Therefore their intersection families have finitely many admissible 8-tuples for each fixed m. The 93 other prices 222,...,314 are consecutive. For each admissible 8-tuple, the number of exact-price-N completions is

N^92/(92!P8) + O_m(N^91),

because shifting N by the fixed early price sum changes only lower-order coefficients, and nonunit root-of-unity poles of the 93-price partition product have order below 92. Thus the leading coefficient of each intersection is its exact admissible eight-tuple count.

For A∩B, fix c and a; put r=m-1-c-a. Then b and d each range from 0 to r, with b multiplicity 1 and d carrying binom(d+2,2) choices. Summing b,d gives (r+1)binom(r+3,3). Summing a,c proves the AB_m formula. A∩C has the same count by swapping a and b.

For B∩C, fix s=c+d. Then a and b independently lie in [0,m-1-s], while the total number of three-plus-three allocations with c+d=s is binom(s+5,5) by Vandermonde's identity. This gives BC_m.

For A∩B∩C, fix c,d, and r=m-1-c-d>=0. The B,C failures give 0<=a,b<=r. Of these (r+1)^2 pairs, A excludes those with a+b>r+d; their number is h(h+1)/2 where h=max(r-d,0). The weighted double sum is exactly ABC_m.

Inclusion-exclusion for A,B,C yields

|E_A union E_B union E_C|
 = A_m+B_m+C_m - |E_A∩E_B|-|E_A∩E_C|-|E_B∩E_C|+|E_A∩E_B∩E_C|.

The remaining M,L failures have at most O_m(N^32) and O_m(N^83) possibilities respectively, so they cannot affect N^92. Taking the leading coefficients of the intersections produces R_m as claimed.

For each eight-tuple meeting exactly two of the early failure conditions, the coefficient of R_m is -1; for each eight-tuple meeting all three, it is -2. Every summand is nonpositive, and the all-zero early vector meets all three conditions for every m>=1, making R_m strictly negative. QED.

## Independent exact integer cross-check

The attached VERIFY_R5_INTERSECTION_N92.py computes AB_m, BC_m, ABC_m in two separate ways: direct enumeration over a,b,c,d with exact three-label multiplicity weights, and the collapsed binomial sums above. All results agree:

| m | AB = AC | BC | ABC | R_m |
|---:|---:|---:|---:|---:|
| 1 | 1 | 1 | 1 | -2 |
| 2 | 12 | 10 | 9 | -25 |
| 3 | 72 | 54 | 48 | -150 |
| 4 | 300 | 210 | 186 | -624 |
| 5 | 990 | 660 | 586 | -2054 |
| 8 | 15444 | 9438 | 8462 | -31864 |
| 17 | 2206413 | 1225785 | 1119393 | -4519218 |

The proof is exact for all m, and the finite tests check the integer combinatorics; independent mathematical review remains NOT_REVIEWED.

## Next

Combine the explicit A/B/C individual series and this overlap coefficient to compute the fourth global polynomial coefficient of Delta_m(N). The natural next unexplored term N^91 involves next-order overlap moments and possibly additional inclusion-exclusion refinements. Frozen science pin and original adaptive interval [8335,8343] remain unchanged.
