# R5 | exact third-threshold period at O(N) precision

Date: 2026-11-22. Status: **AUTHOR_EXACT_PROOF / EXACT_INTEGER_CROSSCHECKED / NOT_REVIEWED**. This is a separate independent portable result for the original frozen scalar model, not a native CLAIM/Result or mathematical admission.

Frozen input: true-event correction at enterprise-math@75d986aa23b68a7ecf9b29dc1006f0e322b35a15. Exact event supports, prices 214,...,314 and interpretation of the scalar cost are identical to the immediately preceding m=2 proof stored on this same branch in research_notes/portable_direct/r5_m2_o1_exact_period_20261122/RESEARCH.md.

## Theorem

For nonnegative integer multiplicities a_p indexed by 214<=p<=314, let N=sum p a_p. The fixed five support sets are

S0=[214,218], S1={214,216,217,218,219,220,221}, S2={215,216,217,218,219,220,221}, S3=[223,290], S4=[296,312].

Let f_3(N) count assignments of cost N for which **at least one** true event E_i: sum_{p in S_i} a_p < 3 holds. The least quasipolynomial coefficient period after discarding O(N) (i.e. for the degree >=2 terms) is

\[
\boxed{M_3(O(N))=229\,746\,052\,653\,717\,600.}
\]

Combined with the previously saved independent m=1 and m=2 results, the sharp period is constant for **m in {1,2,3}**.

## True joint-event generating function

For a nonempty event index subset I, set U_I=union_{i in I} S_i and define the **exact** membership B=\sigma_I(p)={i in I:p in S_i}. Group the prices of identical B as C_B={p in U_I:\sigma_I(p)=B}. For r=0,1,2 set

\[
H_{B,r}(q)=\sum_{\substack{(a_p)_{p\in C_B}\ge0\\\sum a_p=r}}q^{\sum p a_p}.
\]

In particular H_{B,0}=1, H_{B,1}=sum_{p in C_B}q^p, and

\[
H_{B,2}(q)=\sum_{\substack{p,t\in C_B\\p\le t}}q^{p+t}.
\]

Every price in U_I belongs to at least one imposed event, hence every allowed multiplicity a_p<=2. The intersection conditions are equivalent to the **five coupled capacity bounds**

\[
\sum_{B\ni i}r_B\le2\quad\text{for every }i\in I.
\]

Consequently the *exact* intersection polynomial is

\[
Q_{I,3}(q)=\sum_{\substack{r_B\in\{0,1,2\}\\
\forall i\in I:\sum_{B\ni i}r_B\le2}}\prod_{B\ne\varnothing}H_{B,r_B}(q),
\]

where absent signature classes contribute only r_B=0. This follows by partitioning each assignment into the disjoint exact-signature price classes, preserving all overlaps and multiplicities.

Multiplying the intersection generating function by D(q)=prod_{p=214}^{314}(1-q^p), then applying the 31-term inclusion/exclusion, gives the numerator

\[
R_3(q)=\sum_{\emptyset\ne I\subseteq\{0,\ldots,4\}}(-1)^{|I|+1}
Q_{I,3}(q)\prod_{p\in U_I}(1-q^p).
\]

This represents the original coupled three-event loads and the remaining two events without factorizing them incorrectly.

## Cyclotomic certificate and minimality

As for m=1,2, the denominator has zero order n_d=# {214<=p<=314:d|p} at a primitive d-th root. Only 39 orders have n_d>=3, and their least common multiple is L=229746052653717600; hence M_3(O(N)) divides L. For the 14 witness orders in the table, two independently implemented exact-integer computations of R_3(zeta_d(1+t)) modulo t^2 and Phi_d give the same **entire pair of vectors**, with the first nonzero integer basis coefficient as shown.

| d | n_d | least nonzero jet j | pole order n_d-j | zero-based coordinate | coefficient |
|---:|---:|---:|---:|---:|---:|
| 7 | 14 | 1 | 13 | 0 | 3038 |
| 9 | 11 | 1 | 10 | 0 | -3888 |
| 11 | 9 | 0 | 9 | 0 | -2 |
| 13 | 8 | 0 | 8 | 0 | -5 |
| 17 | 6 | 0 | 6 | 0 | 2 |
| 19 | 5 | 0 | 5 | 0 | 20 |
| 23 | 4 | 0 | 4 | 0 | 17 |
| 25 | 4 | 0 | 4 | 0 | -48 |
| 27 | 4 | 1 | 3 | 0 | -5751 |
| 29 | 3 | 0 | 3 | 0 | -831718 |
| 31 | 4 | 1 | 3 | 0 | 93 |
| 32 | 3 | 0 | 3 | 0 | -5280542 |
| 37 | 3 | 0 | 3 | 0 | 3 |
| 43 | 3 | 0 | 3 | 0 | 1 |

For d=7,9,27,31 the zeroth jet vanishes and the first jet survives; in all other rows the zeroth jet survives. Every remaining pole has order at least 3, so the associated primitive-root oscillation of degree at least 2 cannot be absorbed into O(N). Each such d must divide the coefficient period. The lcm of the fourteen d equals L, forcing M_3(O(N))>=L and proving the equality.

## Verification

Run the sibling m=2 verifier dependency (same branch) followed by Python 3 standard-library program VERIFY_R5_M3_O1.py, which imports the sibling reusable ring/cyclotomic arithmetic. It compares two constructions:

(A) **Per-price** dynamic programming over each event's exact count 0,1,2 and choices a_p in {0,1,2}; (B) **per-exact-signature-class** convolution using H_{B,0}, H_{B,1}, H_{B,2} and coupled event capacities. They independently build every intersection and compare the full cyclotomic zero and first jets for all 14 d.

Execution on 2026-11-22: **ALL CHECKS PASS**. SHA256 of executed verifier: 616f0aaf8aa6bafe306359e135097ac1118a6ef315932fa9a8522af1ead4b154. SHA256 of locally generated full 14-pair-vector JSON: aa8aa739ca6c5ddcfef589d2fe908fce214f2f639a38001189ec564e72c691f2. The program regenerates the full JSON. Independent research review: NOT_REVIEWED.

The exact signed cyclotomic jet representation preserves root cancellation; it is a scalar cost observable under the given frozen events, not an X6 native-dynamics theorem. BRC positive totals alone cannot detect the relevant cancellation.

## Next

Extend the exact five-capacity method to m=4 and seek a symbolic threshold generating function or a genuine phase cancellation. Compare which of the fourteen full-period witnesses remain nonzero as m grows; independently review the m=1,2,3 exact theorems. Current native owner read r5-20261122-0843-owner-onebounded-v1 concluded FAILED / SOURCE_TREE_TRUNCATED; there is no current authenticated CLAIM or Activity mutation. Preserve original scientist/provenance and do not treat this GitHub artifact as formal Result/Review.
