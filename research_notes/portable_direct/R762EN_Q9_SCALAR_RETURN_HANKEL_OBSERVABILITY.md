# R762EN — One scalar return trace has the full BRC spectral order

**Date:** 2026-11-18. **Research line:** RS-X6-TRIADIC-CLOSURE-DYNAMICS / historical researcher EM-X6-3050F6. **Status:** AUTHOR_PROVED / EXACT_MODULAR_CERTIFICATE / NOT_REVIEWED. **Formal Source checkpoint:** not asserted. **Antecedent:** R762EM, Draft PR #2724 @ b21958c0178439717e77947be3cfee43570533a6.

## Question and exact model

Does observing the coefficient of the identity endpoint alone lose the minimum recurrence information carried by the complete positive six-branch three-coordinate BRC terminal vector?

Work **after** preserving the six separately named positive branches; this is a terminal observer theorem, not an observer-safe representation of signed native X6 Cell/Link/Port events.

Let \(G\) be any finite abelian group of order \(M\), and \(P=\sum_{g\in G}p_g g\in\mathbb Z[G]\). All statements below hold with arbitrary integer \(p_g\) (positivity is not needed for the spectral multiplicities). Write
\[
a_n=[1_G]P^n\quad (n\ge0),\qquad
\lambda_\chi=\sum_{g\in G}p_g\chi(g),
\]
where \(\chi\) ranges over the \(M\) complex characters of \(G\). Let \(\Lambda\) be the set of distinct character values, \(r=|\Lambda|\), and \(m_\lambda=\#\{\chi:\lambda_\chi=\lambda\}\).

## Theorem A: full spectral observability from a single return-count trace

**For every** finite abelian \(G\) and integer group-ring element \(P\),
\[
a_n=\frac1M\sum_{\lambda\in\Lambda}m_\lambda\lambda^n,\qquad
H_r=(a_{i+j})_{0\le i,j<r},
\]
and the exact Hankel determinant satisfies
\[
\boxed{
\det H_r=M^{-r}\Bigl(\prod_{\lambda\in\Lambda}m_\lambda\Bigr)
   \prod_{\{\lambda,\mu\}\subset\Lambda}(\mu-\lambda)^2
  \in\mathbb Z\setminus\{0\}.}
\]
An arbitrary ordering of the distinct roots may be used; the squared Vandermonde is symmetric.

Consequently the **least** degree of a common rational constant-coefficient homogeneous recurrence satisfied by \((a_n)_{n\ge0}\) **starting at index zero**, in the standard convention \(\sum_{j=0}^d c_j a_{n+j}=0\) for every \(n\ge0\) with \(c_d=1\), is exactly \(r\). Its unique monic minimal polynomial is
\[
\boxed{\mu_P(T)=\prod_{\lambda\in\Lambda}(T-\lambda)\in\mathbb Z[T].}
\]
This is exactly the minimum polynomial of multiplication by \(P\) on \(\mathbb Q[G]\); thus **one infinite scalar return trace has the same rational spectral recurrence order as the full terminal count vector**.

**Proof.** Character orthogonality gives \([1_G]A=M^{-1}\sum_\chi\chi(A)\) for any \(A\in\mathbb C[G]\). Apply to \(A=P^n\), including \(n=0\), and group equal eigenvalues. Let \(V_{i,\lambda}=\lambda^i\) for \(0\le i<r\), and \(W=\operatorname{diag}(m_\lambda/M)\). Then \(H_r=VWV^\mathsf T\); all diagonal entries of \(W\) are nonzero and the Vandermonde matrix \(V\) is invertible. The displayed exact determinant follows. It is an integer because all \(a_n\) are integers.

For an order-\(d\) recurrence with \(d<r\), the \((d+1)\)-column Hankel matrix has a column dependence; in particular the infinite Hankel rank would be at most \(d\), contradicting invertibility of \(H_r\). The product of distinct character eigenvalues annihilates each exponential \(\lambda^n\), giving the matching upper bound. The characteristic values of an integral group-ring convolution operator are algebraic integers and collectively Galois stable, hence this monic rational polynomial has integer coefficients. QED.

**Exact recovery interface.** The first \(2r\) values \(a_0,\ldots,a_{2r-1}\) determine \(\mu_P\) uniquely by the nonsingular integer Hankel system \(H_r(c_0,\ldots,c_{r-1})^\mathsf T=-(a_r,\ldots,a_{2r-1})^\mathsf T\). This is a reconstruction of an observable recurrence, **not** a reconstruction of original named branch histories or a future-operation-safe native-state quotient.

## Theorem B: q=9 optimal orders and the index-zero anomaly

Specialize to \(G=(\mathbb Z/9\mathbb Z)^3\) and
\[
P=1+X+Z+XY+YZ+XYZ.
\]
R762EM's complete exact 729-character certificate has \(r=127\) distinct eigenvalues, of which precisely one is zero (with character multiplicity 60). Therefore:
\[
\boxed{\text{least scalar return-trace recurrence order for }n\ge0=127,}
\]
\[
\boxed{\text{least recurrence order of shifted trace }b_n=a_{n+1},\ n\ge0=126.}
\]
Indeed \(a_{n+1}=M^{-1}\sum_{\lambda\ne0}m_\lambda\lambda^{n+1}\), and each remaining weight \(m_\lambda\lambda/M\) is nonzero. Apply the same Vandermonde proof to the 126 remaining distinct roots. In particular an order-126 recurrence is only valid for the positive-time shifted trace, whereas including \(a_0=1\) requires the extra factor \(T\).

## Independent exact modular witness for the lower bounds

The accompanying Python-standard-library program directly multiplies six explicit branch shifts in the 729-position group ring modulo **two distinct primes** \(p=1000000007\) and \(p=998244353\), for all \(n=0,\ldots,319\). For each prime it computes Hankel determinants by field elimination, and a 254-sample Berlekamp–Massey recurrence, then checks that recurrence against all 320 samples. The results are:

| prime | det(H_127) mod p | det(H_128) mod p | det(shifted H_126) mod p | det(shifted H_127) mod p | BM(254) |
|---:|---:|---:|---:|---:|---:|
| 1000000007 | 744077255 | 0 | 898733877 | 0 | 127 |
| 998244353 | 403897829 | 0 | 389987108 | 0 | 127 |

A **single** nonzero 127-by-127 determinant residue already proves the corresponding integral Hankel determinant is nonzero; the second prime checks the implementation independently at another modulus. The shifted 126-by-126 residues similarly prove that the positive-time minimal order is at least 126. Upper bounds use R762EM's exact full spectrum. No floating-point arithmetic and no statistical inference are involved.

The exact first-nine return values are \(a_0=\cdots=a_8=1\); at \(n=9\), \(a_9=6\). The only all-return loop paths before time 9 use the identity branch at every update, and at time 9 the other five individual nonzero branches can each be repeated nine times. This provides a small independent coefficient sanity check.

## Relationship to the mother objective and next question

The theorem establishes **spectral sufficiency for an all-time zero-endpoint scalar terminal observer**. It does not assert preservation of signed paths, Cell incidence, time-dependent event permission, source types, three-force balance, or arbitrary future operations. The project P000 and joint-observer fidelity constraints remain in force; no branch or provenance information is discarded from the research source. The q=9 factorization R762EM remains author-proved / not independently reviewed; this note adds independent modular **lower-bound** certificates and an unconditional general Hankel theorem.

Next: (i) reconstruct the order-127 integer recurrence directly from 254 return counts and compare exact coefficients with the 27 R762EM factors; (ii) use its 3-adic structure to seek coefficientwise nondivisibility for the all-horizon q=9 content problem; (iii) independently determine actual Source-authorized signed native TRIADIC_CLOSURE_E event predicates and V17/V29/V39 transport before any native promotion. Scientific input remains frozen; no claim/Source/admission status follows from this portable note.

## Exact source and reproducibility

- Frozen P000: enterprise-math @ a72226e2430ffa4786321ac86e7f0c599d5f0389, p000_reality_foundation.json; immutable taskbook @ e3f42efac29a2da2d95be391f3231a664e2fade0.
- Predecessor: research_notes/portable_direct/R762EM_Q9_EXACT_SPECTRAL_FACTORIZATION_THEOREM.md and R762EM_Q9_SPECTRAL_EVIDENCE.json @ b21958c0178439717e77947be3cfee43570533a6.
- This release: R762EN_VERIFY.py (standard-library exact mod-prime simulation and linear algebra); R762EN_EVIDENCE.json (complete run summary, first-254 return-trace hashes, explicit limitations).

**Review:** NOT_REVIEWED. **Formal Source publication:** not asserted. **Data exposure:** non-sensitive mathematics, no credentials.
