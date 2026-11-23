# T6 exact-v2(d)=5, two atoms per side: 26 -> 7 by odd-prime sixth-moment obstructions

Date: 2026-11-23 (Asia/Taipei).
Research author/checker: existing RESEARCH_DRIVER logical line EM-DVR-DEBB5E; retain original T6/maximal-prime contributions from EM-X6-FB6990 and earlier researchers. This note is scientific evidence, not a native Review, Result, CLAIM or activity association.

## Statement and exact scope

Let A,B be finite multisets of positive integer exponents, separately satisfying \(\sum_{e\in A}e,\sum_{e\in B}e\le2331\). Set \(d=e+1\) and \(H_k(X)=\sum_{e\in X}(e/(e+1))^k\). Assume \(H_0(A)=H_0(B),\ldots,H_6(A)=H_6(B)\), and exactly two occurrences of denominators with \(v_2(d)=5\) on *each* side. Reuse the already established cancellation for \(v_2(d)\ge6\).

The previously exact [342-profile / 26-candidate sieve](https://github.com/awdawmip/enterprise-math/blob/8a2cd0aab4eb61243b60dcdfccf71745c73b7301/research_notes/driver/2026-11-23_t6_p2_fifth_two_atom_budget_sieve_26.md) leaves 26 distinct unordered profile pairs \((P,Q)\) that satisfy its necessary mixed-2-adic budget constraints. Here \(P,Q\) list the odd co-factors \(j\) in \(d=32j\), preserving multiplicity. An additional sixth reciprocal-moment condition excludes **19** of those 26 pairs. Thus only **7** profile pairs remain under these combined necessary conditions. This theorem has exact-two-on-each-side scope.

## Rational-to-p-adic reduction

Define \(S_k(X)=\sum_{e\in X}(e+1)^{-k}\). The triangular binomial identity \(H_k=\sum_{i=0}^k(-1)^i\binom{k}{i}S_i\) implies \(S_6(A)=S_6(B)\).

Take an odd prime \(p\ge17\) dividing at least one profile co-factor, with \(p^2>\max(R_A,R_B)+1\). The fixed \(v_2=5\) co-factors obey \(j\le71<p^2\), so every fixed \(p\)-divisible denominator has \(v_p(d)=1\); every residual \(p\)-divisible denominator also has \(v_p(d)=1\) because its exponent cost is at most \(R_X\). Multiplication of \(S_6(A)-S_6(B)=0\) by \(p^6\), reduction modulo \(p^6\), and cancellation of the \(p\)-regular terms imply equality of the sixth powers of inverses of the \(p\)-units \(d/p\).

Let \(C_p(P)=\sum_{j\in P,\ p\mid j}(32j/p)^{-6}\pmod{p^6}\), and let

\[
U_p(R)=\left\{\sum_{u\ge1}n_u\,u^{-6}\bmod p^6:\ n_u\ge0,\ \sum_u n_u(pu-1)\le R,\ u\le\lfloor(R+1)/p\rfloor\right\}.
\]

Because \(R+1<p^2\), each \(u<p\) is invertible modulo \(p^6\). Each actual side has a residual \(p\)-primary submultiset represented in \(U_p(R)\), even after allowing other denominators to consume budget. **Therefore a necessary condition for full equality is**

\[
(C_p(P)+U_p(R_A))\cap(C_p(Q)+U_p(R_B))\ne\varnothing.
\]

When this intersection is empty, the profile pair is rigorously impossible under the original full rational moments. No assumption that individual prime layers have separately equal rational moments is used.

## Complete exact enumeration

The [standalone Python integer checker](https://github.com/awdawmip/enterprise-math/blob/fae484f29a738a92235241fce4658fca91f35d41/research_checks/T6_P2_FIFTH_ODD_PRIME_SIXTH_MOMENT_EXACT_20261123.py) first reconstructs all 342 profiles, the 1,038 -> 82 -> 33 -> 26 necessary-condition counts, and the complete 2,048-element v2=4 signature group with maximum shortest cost 813. For each admissible \(p\), it enumerates **every nonnegative multiset** of residual \(p u\) denominators within the independent side budget via exhaustive recursion over \(u=1,\ldots,\lfloor(R+1)/p\rfloor\), using Python exact integers and modular inverses, then tests the full shifted-set intersection.

The following disjoint-set certificates exclude exactly 19 numbered pairs from the original 26 ordering:

| Prime witness | Pair indices excluded |
| --- | --- |
| \(p=17\) | 2, 5 |
| \(p=19\) | 4, 16 |
| \(p=23\) | 25 |
| \(p=29\) | 20, 21 |
| \(p=31\) | 26 |
| \(p=37\) | 17, 18, 19 |
| \(p=41\) | 6, 8, 10 |
| \(p=43\) | 12, 14 |
| \(p=47\) | 24 |
| \(p=53\) | 22 |
| \(p=59\) | 15 |

No floating-point arithmetic or external libraries are involved. The checker asserts the original four counts and exactly these 19 eliminations.

The seven *not excluded* pairs are:

| Original index | \(P\) | \(Q\) | Remaining exponent mass per side |
| --- | --- | --- | ---: |
| 1 | (1,33) | (17,17) | 1245 |
| 3 | (1,65) | (33,33) | 221 |
| 7 | (1,49) | (17,33) | 733 |
| 9 | (1,57) | (25,33) | 477 |
| 11 | (3,35) | (19,19) | 1117 |
| 13 | (3,51) | (19,35) | 605 |
| 23 | (7,39) | (23,23) | 861 |

These seven retain *necessary-condition candidate* status, not full rational-moment equality. An exact next question is to test their smaller-prime or higher-valuation completions, while separately treating unequal exact-v2=5 atom counts and the global T6 mother objective.

## Control and attribution

Proof domain: original T6 model, finite exhaustion only for the stated two-atom scope. The code's set enumeration establishes the required complete finite coverage, not canonical mathematical admission. Preserve existing Author/Review/Result distinction and the original Driver's Source/Activity authority boundary.
