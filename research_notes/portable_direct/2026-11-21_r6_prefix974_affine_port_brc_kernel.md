# PREFIX-974 — Affine source-port quotient and exact BRC port-relation composition

Date: 2026-11-21 (Asia/Shanghai). Status: AUTHOR_PROOF / EXACT_INTEGER_CHECKED / NOT_REVIEWED.
Scientific input frozen at \`f42f2906d77f24085c123f3ccfe9667d41caa96d\`. Predecessors: PREFIX-968/970/972/973. Historical \`EM-DIRECT-58C410\` is provenance only, not current authenticated identity/CLAIM. This is the independent auxiliary odd-gap XOR observer, not native signed X6 dynamics.

## Exact model and task

For p>=4 let Q_p={2^(p-1)+1, 2^(p-1)+3, ..., 2^p-1}. Take odd k>0 with k+2<2^(p-1), odd m>0, 1<=t<=2k, and a,b in Q_p, a!=b. Full named histories (a,b,t,t+m,i,j,I,J) satisfy

    ((k*a) XOR 2^j) - 2^i = t*b,
    (((k+2)*a) XOR 2^J) - 2^I = (t+m)*b.

For a numeric source residual c=2^i-s*2^j (s=+1 or -1), retain two p-bit masks P_c and M_c of those j for which the indicated + or - source exists. For each fixed (c,j,s), the index i is unique if it exists. At product x define the exact *valid port support*

    V_c(x) = (P_c & ~low_p(x)) | (M_c & low_p(x)).

For each j there is **at most one valid named source label** at fixed (c,x): the bit of x chooses exactly one sign, and that sign determines i uniquely. Hence V is a Boolean port mask but simultaneously carries the exact count of valid labels per port (0 or 1). The two-sided histories at fixed arithmetic candidate have independent labels, so the joint port support is the Cartesian product U x V, with U=V_c(ka), V=V_C((k+2)a). All claims below refer to this precisely typed port-only observation.

## Theorem 974.1 — affine port map, exact bit-flip transport, rank

Define A_c=P_c XOR M_c. For every p-bit state x,

    V_c(x) = P_c XOR (A_c & x).

For every p-bit flip F,

    V_c(x XOR F) = V_c(x) XOR (A_c & F).

Thus the port readout is an affine map over F_2 with linear part diag(A_c). Over the full {0,1}^p input cube its rank is popcount(A_c), its image has exactly 2^popcount(A_c) elements, and x and y have identical port readout if and only if (x XOR y)&A_c=0. On the restricted odd-x slice, its rank is popcount(A_c & ~1). These statements are exact arithmetic/observer facts and make no assertion that an arbitrary bit flip is a legal native event or preserves the original two-core equations.

Proof: bitwise, for (P_j,M_j)=(0,0),(1,0),(0,1),(1,1), the valid-port bit is respectively 0,1-x_j,x_j,1. Each is P_j XOR ((P_j XOR M_j)&x_j). The image and kernel statements follow by independent free bits at the positions of A_c; fixing x_0=1 gives the odd-slice count. QED.

## Theorem 974.2 — exact positive BRC port relation / minimal quotient

Fix an arithmetic candidate (a,b,t,m) and its U,V above. For **any** nonnegative-integer (or nonnegative-rational) p-by-p port kernel K, assign weight K[j,J] to a joint named history with source ports (j,J). Its exact weighted positive mass is

    Mass_K = sum_{j=0}^{p-1} U_j * (sum_{J=0}^{p-1} K[j,J]*V_J).

No named (i,j,I,J) expansion is required. The formula follows from Cartesian independence of the two source-label sets and the at-most-one-label-per-port property. For a finite serial chain of declared port-only positive transition kernels, matrix multiplication gives the exact weighted path count U^T K1 ... Kr V, by distributing products over all intermediate port paths.

The complete family of kernels includes singleton tests K=E_{jJ}. Therefore it determines every bit of U x V. For U and V both nonempty this recovers the ordered pair (U,V) uniquely; if either is empty, all these readouts are zero and every such state belongs to the same zero-observation class. Accordingly, \`ZERO\` plus the nonempty ordered mask pairs is the **minimal sufficient quotient** for *all* two-sided port-relation observations. For a single endpoint with all singleton-j observations, V alone is the corresponding minimal sufficient quotient. This is a precise observer-relative minimality statement, not a bit-complexity lower bound for arbitrary encodings.

The formula and serial interpretation apply to positive, port-only BRC-style branching. If K depends on signed source s, output source index i, phase, native Cell/Link permission or other hidden history, further coordinates or a factorization proof are required.

## Proposition 974.3 — demonstrated information-loss obstruction

At p=4, c=6, both x=9 and x=11 are odd. Their port support is the same singleton bitmask V_6(9)=V_6(11)=2 (j=1). But at x=9 the valid source at j=1 is (i,j,s)=(3,1,+1), whereas at x=11 it is (2,1,-1):

    (9 XOR 2)-8=3=9-6;
    (11 XOR 2)-4=5=11-6.

Thus even a complete valid-port support fails to preserve signed labels or source-output positions; its exactness is limited to the declared port-only family. In the actual p=19 k=21 m=1 original two-core model, the following **two full valid histories** each have total named multiplicity one but different equal-port observation:

    (262155,501781,11,12,11,14,13,0): equal-port=0;
    (270673,473763,12,13,0,10,16,10): equal-port=1.

Therefore a total-mass/weight-histogram-only quotient cannot recover port equality even within the original model.

## Exact integer results, p=19,k=21,m in {1,3,5}

All nondiagonal integer candidates retain the previously published unique named-witness hashes. Direct mask-only arithmetic reconstruction was checked against separately built full named histories. Port relation \`equal\` means J=j. \`next cyclic\` means J=(j+1) mod p, a selected test kernel, *not* a native spatial rotation claim.

| m | Original valid named histories | Distinct (a,b) | J=j | J=(j+1) mod p |
|---:|---:|---:|---:|---:|
| 1 | 614 | 442 | 22 | 55 |
| 3 | 1,286 | 839 | 34 | 74 |
| 5 | 3 | 3 | 0 | 1 |
| Total | 1,903 | 1,284 | 56 | 130 |

The direct mask-only checker also reproduces PREFIX-973's numerical candidate count 1,420/2,826/15, zero-weight count 977/1,986/12, and full weight histograms. No claim of a comparable end-to-end runtime speedup is made.

## Validation and evidence scope

- Exact affine identity and all one-bit flip transitions exhaustively checked on 85,872 (p,c,x) inputs with p=4..9 and every distinct residual c. No floating-point arithmetic.
- For p=4..8, every eligible odd k and m in {1,3,5}: 357 independent small raw-XOR parameter cases, with complete full-named tuples equal to arithmetic reconstruction. Equal and cyclic port masses also checked against raw-XOR names.
- p=19,k=21,m=1/3/5: exact integer bounded-bucket mask calculation compared to separately enumerated named histories, full tuple SHA-256 equal to PREFIX-966/973:
  m1 \`ccbccc30c4171a809f7270ce59f0b72b368839e93ffeeed8df9ba1045720da71\`;
  m3 \`1360a9ca274b357d0b87058d35ef6ccd059d0c5aef995e4d93b0d1363e1aaae3\`;
  m5 \`c429ef59749f36ef295b4ac9171fb5171ab3a706beaa270563728d4962649c1b\`.
- \`PREFIX974_R6_PORT_AFFINE_COMPOSITION.py\` supplies the direct bounded-bucket mask checker and raw-XOR validation. \`PREFIX974_R6_REPRO.py\` is a shorter self-contained independent full-named validator. \`PREFIX974_R6_EXACT_RESULTS.json\` records the count evidence.

No formal proof assistant, independent research review, native X6 claim or scientific-result admission was performed. The mother question B_fix,odd(32) in {19,20} stays open.

## Next discriminating question

Determine the smallest signed-source-aware quotient for declared BRC port updates: the pair of valid sign masks (P&~x,M&x) recovers (i,j,s) for each source c and therefore is sufficient for one-step label queries. Characterize when this quotient remains closed under multi-step branch composition with source-dependent rules, and construct a counterexample when an omitted correlation breaks closure. Only after that compare complete representation, transition, recovery and verification costs. Preserve Activity association debt pending authenticated current-session permission; do not borrow historical Researcher identities or obtain a shared X6 CLAIM for this independent result.
