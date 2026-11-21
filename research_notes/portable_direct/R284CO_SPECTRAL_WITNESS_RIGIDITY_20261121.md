# R284CO — Unique 63-site rigidity of the frozen Port coverage spectrum

2026-11-21. Status: **AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED**. Independent mathematical review has not occurred.

## Exact scope and frozen sources

This result is confined to the auxiliary 34-bit Port observer of R284CL–R284CN. It does not change the native X6 space, the BRC typed state, P000, or any shared task claim.

- Circle modulus \(P=17\,179\,869\,143\).
- Coefficients \(D=(1120832,6,13,1651128)\), \(Z=(0,390139,394465,1497639)\).
- Frozen selector \((0,1,2,4,5,6)\).
- Finite population \(X\) consists of all 65,536 **distinct** Port residues generated from the frozen 4×4 two-valued matrices, in R284CL iteration order.
- SHA-256 of the ordered eight-byte big-endian residues: \`b6ce76b2c08b9ec6b79ec83173befd2589928ca7c636643c3eaecd40405f4ff4\`.
- The 64 labeled circular closed arcs are \(A_j=[a_j,a_j+w_j]\pmod P\), reconstructed from the two monotone matrix extrema at each fixed six-coordinate selector.
- Define \(\delta_j(x)=\operatorname{dist}_{circle}(x,A_j)\); let \(d_k(x)\) denote the \(k\)-th smallest of the 64 distances, **with multiplicity**. For nonempty \(Y\subseteq X\), put \(U_k(Y)=\max_{x\in Y}d_k(x)\), for \(1\leq k\leq64\).

## Theorem: unique minimal universal spectrum witness set

In the fixed finite population \(X\):

1. \(U_1(X)=0\), and in fact \(d_1(x)=0\) for every \(x\in X\).
2. For every \(k=2,\dots,64\), exactly **one** point \(w_k\in X\) maximizes \(d_k(x)\).
3. Those 63 maximizing residues \(w_2,\dots,w_{64}\) are **pairwise distinct**.
4. Writing \(W=\{w_2,\dots,w_{64}\}\), a nonempty subset \(Y\subseteq X\) reproduces **all 64** original optimal radii if and only if \(W\subseteq Y\):
   \[
   \bigl(U_k(Y)=U_k(X)\ \forall k=1,\ldots,64\bigr)\iff W\subseteq Y.
   \]
   Therefore \(W\) is the **unique inclusion-minimal** and **unique minimum-cardinality** subset preserving the entire 64-level spectrum, and its exact size is **63**.
5. For each \(k\ge2\), removal of its essential point decreases that level by a strictly positive integer
   \[
   \Delta_k=U_k(X)-\max_{x\in X\setminus\{w_k\}}d_k(x).
   \]
   The exact minimum over all 63 levels is \(\min\Delta_k=\boxed{64}\), reached precisely at levels \(k=15,16\). At \(k=54\), \(w_{54}=6\,683\,583\,072\), its original enumeration index (zero-based) is 33760, \(U_{54}=7\,642\,302\,204\), the runner-up is \(7\,642\,302\,126\), and \(\Delta_{54}=78\).

### Proof

For items (1)–(3) and (5), enumerate the exact frozen 65,536-element domain. For each residue, evaluate all 64 integer circular distances and sort them (retaining repeated zeros). For each of 64 ranks, keep the maximum, the number of achievers, the achieving original matrix index, and the strictly next-largest value. The accompanying self-contained checker uses integer arithmetic only. It verifies the original frozen SHA-256, all 65,536 residues are distinct, the maximal-achiever counts are 65,536 for rank 1 and exactly 1 for each rank 2–64, and the 63 nontrivial achiever indices are distinct. The full vector of 64 maxima also agrees term-for-term with the separate R284CN integer-event-sweep certificate.

Define \(W\) as in (4). Each \(w_k\) witnesses \(U_k(X)\), so if \(W\subseteq Y\), every \(U_k(Y)\) with \(k\ge2\) equals the corresponding full-population maximum; rank 1 is identically zero. Conversely, if some \(w_k\notin Y\), uniqueness of the maximizer implies \(U_k(Y)<U_k(X)\). Therefore preserving every level forces inclusion of all 63 distinct \(w_k\), which establishes uniqueness and minimality. The exhaustive second-best values provide the exact strict margins. \(\square\)

### Perturbation corollary (separate from Port error correction)

Suppose a second **labeled** 64-distance array \(d'_j(x)\), defined on the same labeled finite population and ranks, satisfies
\[
\sup_{x\in X,\ 0\le j<64}|d'_j(x)-\delta_j(x)|\le\varepsilon.
\]
Sorting is 1-Lipschitz in the sup norm, hence each \(d'_k(x)\) changes by at most \(\varepsilon\). Since every original winner exceeds every competitor by at least 64, if \(2\varepsilon<64\) all 63 labels \(w_k\) remain the unique winners and distinct; their corresponding maxima shift by at most \(\varepsilon\). For integer discrepancies it suffices that \(\varepsilon\le31\). This is **winner-label stability under a uniform change to the distance table**, not a claim of 31-unit unique matrix decoding or of full X6 stability.

## Exact evidence and computational scope

- \`R284CO_spectral_witness_checker.py\`: stand-alone standard-library Python checker implementing the frozen determinant readout, SHA test, complete 4,194,304 distance evaluations and 63-site core recomputation.
- \`R284CO_spectral_witness_certificate.json\`: all 64 maxima; every k≥2 winning matrix index, residue and runner-up gap; the complete 63-site certificate; smallest margin and examples.
- Direct exact re-enumeration also reproduces R284CN's entire 64-value spectrum. This is full finite verification under the frozen model. It is not independent peer review.
- Compressing a *witness certificate* from 65,536 sites to 63 does not by itself provide a faster algorithm for finding these sites: this checker still searches the full frozen population.

## Next scientific problem

Seek a direct construction of the 63 essential residues from arc geometry, avoiding the current 4,194,304 distance computations, and determine whether spectral witnesses can be predicted from the R284CM critical-site partition or R284CN integer-event bands without exhaustive scanning. Separately measure the certificate-verification cost when the 63 candidate indices are supplied versus the cost of proving uniqueness on the full population.

Provenance: historical Port work R284CL/R284CM/R284CN, attributed there to EM-DIRECT-20B766. This document does not assert current possession of that historical private execution capability or formally claim an unrelated task. Source Activity association requires its own authenticated readback and CAS.