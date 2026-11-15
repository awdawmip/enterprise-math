# R749SPU — Exactly 26 first-grid Walsh centers suffice, and are necessary, at every precision n ≥ 2

**Date:** 2026-11-15. **Status:** AUTHOR_EXACT_NOT_REVIEWED. **Research mode:** independent portable TASK_RESEARCH, no shared X6 CLAIM. **Frozen scientific input:** awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. **Predecessors:** R749SPR (PR #2457@7e876e05511b861a72cc1f03b5a880faba71a3b5), R749SPS (PR #2461), R749SPT (PR #2464@4c6e66af6dca137e5b5324c877a2a7427ab144dd).

## Exact mathematical object

Consider the frozen auxiliary **signed** 16-atom Walsh probability law

\[
p(t,s,h,u,v,w,z)[k]=\frac{1+t\chi_3(k)+s\chi_{12}(k)+h\chi_{15}(k)+u\chi_1(k)+v\chi_2(k)+w\chi_4(k)+z\chi_8(k)}{16},
\quad \chi_m(k)=(-1)^{\operatorname{popcount}(k\mathbin{\&}m)}.
\]

At \((t,s)=(1/10,1/2)\), R749SPR established the complete calibrated optimal-center polytope
\[
q_X=p(1/10,1/2,H/10,U/10,V/10,0,0),\qquad X=(H,U,V)\in K,
\]
where
\[
\begin{array}{ll}
-H-U-V\ge -2,&-H-U+V\ge -2,\\
-H+U-V\ge -2,&-H+U+V\ge -2,\\
H-U-V\ge -2,&H-U+V\ge -4,\\
H+U-V\ge -4,&H+U+V\ge -2.
\end{array}
\]
Every center in K has exact worst-case total variation risk \(\rho=\rho^{\mathrm{cal}}=9/20\). Write \(P=K\cap\mathbb Z^3\); its cardinality is 33. For any source alphabet \(A\subseteq P\), define the n-fold **observed sums**
\[
\Sigma_n(A)=\{a_1+\cdots+a_n:a_j\in A\}\subseteq nK\cap\mathbb Z^3.
\]
The underlying positive BRC-style multiset of labeled source types remains a separate carrier; \(\Sigma_n\) is only the specified averaging observer.

## Theorem: a sharp 26-type universal source alphabet for every n ≥ 2

The minimum number of first-grid types in an alphabet A satisfying
\[
\boxed{\Sigma_n(A)=nK\cap\mathbb Z^3\quad\text{for every integer }n\ge2}
\]
is **26**, and there are **exactly two** minimum alphabets.

Let F be the union of all endpoints in every **uniquely represented unordered pair sum** \(x=a+b\) with \(a,b\in P\) and \(x\in 2K\cap\mathbb Z^3\). Then \(|F|=25\) and the only two minimal alphabets are
\[
\boxed{A_{\rm zero}=F\cup\{(0,0,0)\},\qquad A_{\rm shift}=F\cup\{(-1,0,0)\}.}
\]
For every \(n\ge2\) and every \(X\in nK\cap\mathbb Z^3\), there exist \(a_1,\ldots,a_n\) in either selected alphabet with
\[
X=\sum_{j=1}^{n}a_j,\qquad
q_{X/n}=\frac1n\sum_{j=1}^{n}q_{a_j},
\qquad \sup_{p\in\mathcal P_{1/10,1/2}}TV(q_{X/n},p)=9/20.
\]
For n=1, obtaining all 33 first-grid readouts requires all 33 letters.

## Exact lower bound and uniqueness classification

The attached standard-library Python executable directly enumerates all integer lattice points in K, 2K, and 3K from the eight displayed linear inequalities and the complete scaled-coordinate bounding boxes \([-2n,2n]^3\). The respective counts are **33, 179, 531**, independently matching the R749SPS Ehrhart polynomial. It separately enumerates 561 unordered two-letter multisets of P.

Exactly **46** of the 179 second-grid target sums have only one unordered pair representation in P. The union of the endpoints of these 46 forced representations has **25** distinct members. Consequently every alphabet covering 2K must include those 25 types. Those 25 alone cover exactly 177 of the 179 targets, leaving the two holes
\[
\boxed{(-2,-1,1),\quad(-2,1,-1).}
\]
There are eight optional members of \(P\setminus F\). Exhaustively testing every one-letter extension of F confirms that both missing sums become representable only when the added type is \((0,0,0)\) or \((-1,0,0)\). Therefore any alphabet of size less than 26 fails at n=2, and precisely the two stated size-26 alphabets pass at n=2. This proves the sharp bound and exact classification of equality cases.

## Complete level-three certificate and the all-n proof

For **each** of the two 26-letter alphabets, all \(\binom{27}{2}=351\) unordered pair-source multisets are enumerated and their sums cover all **179** points of 2K. All \(\binom{28}{3}=3276\) unordered triple-source multisets are enumerated and their sums cover all **531** points of 3K. Target sets are generated independently from K's eight halfspaces; all comparisons are exact integer equalities.

R749SPT provides an explicit regular **unimodular** triangulation of K consisting of 92 tetrahedra, and proves the integer decomposition property (IDP): every \(X\in nK\cap\mathbb Z^3\) is a sum of n members of P for all n ≥ 1. For every integer n ≥ 2 there exist nonnegative a,b with n = 2a + 3b. First use IDP to write X as n letters of P. Partition these into a groups of size 2 and b groups of size 3. Replace each group by its equal-sum representation using either of the two alphabets, which exists by the complete level-2 and level-3 certificates. This produces n letters in the chosen 26-type alphabet with total exactly X.

Because the probability map is affine in X at the fixed Walsh parameters, equality of sums gives **equality of the complete signed-atom probability law** after averaging. Thus the minimax-risk identity is exact at every n ≥ 2. The infinite-scale conclusion follows from the IDP proof and the finite 2/3 certificates, not from extrapolation of finitely many tests.

## Source-provenance statistics and concrete encoder

Each 26-letter alphabet produces 351 second-grid source multisets but 179 distinct projected readouts. The maximum two-letter fiber multiplicity is 7 for both choices. At level three, each alphabet has 3276 source multisets and 531 projected readouts. The maximum source-fiber multiplicity is **29** for A_zero and **34** for A_shift. The number of readouts with unique preimage is respectively 87 versus 83 at n=2, and 88 versus 86 at n=3.

A constructive exact encoder for arbitrary n ≥ 2 is: decompose X/n using one of R749SPT's 92 unimodular tetrahedra, obtain n lattice types from integer barycentric coefficients, group into pairs and triples, and replace each group through one of the two complete finite sum lookup tables generated by the attached code. Labels and multiplicities must remain with the branch carrier whenever future operations need source recovery; the 26-type theorem is explicitly scoped to the final averaged signed-law observer.

## Validation scope, sources, and next question

The attached R749SPU_MINIMAL_WALSH_SOURCE_ALPHABET_CERT.py runs using Python's standard library, exact integer arithmetic, complete lattice enumeration and full multiset enumeration. The attached JSON records an actual successful execution, all type sets and the two/three-level fiber counts. No floating-point tolerance or Monte Carlo estimate appears. The unbounded result uses **R749SPT's author-proved, not independently reviewed** unimodular triangulation/IDP theorem; its imported proof obligation is declared rather than silently re-executed.

The result remains in the **frozen auxiliary Walsh model**, with full signed atoms and source label carrier; native P000 X6 Cell/Link/Port and V29/V39 observer-preserving transfer are unproved. No shared task CLAIM, review or mathematical Foundation promotion is asserted.

**Next science:** (i) compare the two minimal alphabets' maximal source fibers and recovery metadata for all n, seeking an exact asymptotic or extremal separation; (ii) determine a neighboring rational parameter chamber where the optimal-center polytope has a provably stable alphabet cardinality; (iii) independently review the inherited unimodular certificate and this exact 2/3-level classifier.
