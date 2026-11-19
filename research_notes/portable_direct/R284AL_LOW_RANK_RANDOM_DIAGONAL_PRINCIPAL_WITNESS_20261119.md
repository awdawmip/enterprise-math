# R284AL — 非对称正权 Port 的低秩对角探测与精确主子式证书

Date: 2026-11-19. Status: AUTHOR_PROVED / EXACT_FINITE_CHECK_PASSED / NOT_REVIEWED.
Predecessors: R284AK (AK3–AK5), R284AJ, R284AE. Frozen scientific input: 43ec6098b1330ae86d0a7863be336c5d97f6ef34 (unchanged).
Scope: auxiliary exact-rational named Port observations. P000, ACTIVE Heartbeat X6, joint observer preservation and branch/provenance rules remain as protected external semantics; this study makes no claim of native X6 time dynamics or future-operation-safe state compression.

## 1. The question

Let U,V be m-by-r rational matrices of column rank r (r <= m) and C=UV^T. Define its principal rank by

\[
d(C)=\max\{|S|:\ S\subseteq[m],\ \det C[S,S]\ne0\}.
\]

Empty S has order zero. R284AK constructed strictly positive U,V with rank(C)=r arbitrarily large but d(C)=2. In the two-layer named-edit pencil

\[
M_C(u,v)=\begin{pmatrix}D_u&I_m\\ C&D_v\end{pmatrix},
\]

R284AK's polynomial identity gives first nonzero edit degree \(\nu(M_C)=2(m-d(C))\). A common full row basis detects d(C)=r but cannot determine the largest lower-order nonzero principal minor in the presence of signed Cauchy–Binet cancellation.

We establish a reduced characteristic-polynomial detector, an independently checkable exact witness extraction, a probability bound for incomplete detection and an exact deterministic noncancellation sector.

## 2. The low-rank transfer kernel (AL1)

For weights \(w\in\mathbb Q^m\), let \(D=\operatorname{diag}(w)\) and

\[
K(w)=V^TDU=\sum_{i=1}^{m}w_i v_i u_i^T\quad(r\times r),
\]

with \(u_i,v_i\) the rows of the factors, written as column vectors in the outer product. Let \(e_j(K)\) be the j-th elementary characteristic coefficient (\(\det(zI-K)=\sum_j(-1)^je_j(K)z^{r-j}\)).

**Theorem AL1.** For all \(0\le j\le r\),

\[
\boxed{e_j(K(w))=\sum_{\substack{S\subseteq[m]\\|S|=j}}
     \det C[S,S]\prod_{i\in S}w_i.}
\]

**Proof.** Sylvester's identity yields the polynomial equality
\[
\det(zI_m-DC)=z^{m-r}\det(zI_r-V^TDU).
\]
The coefficient of \(z^{m-j}\) in the left side is \((-1)^j\sum_{|S|=j}\det(DC)[S,S]\). Since \(\det(DC)[S,S]=(\prod_{i\in S}w_i)\det C[S,S]\), coefficient comparison proves AL1. The monomials indexed by distinct S are distinct because weights are independently named. Therefore the largest j with the polynomial \(e_j(K(w))\) not identically zero is exactly \(d(C)\). QED.

A probe constructs K with O(mr²) rational operations; a standard exact characteristic polynomial has polynomial arithmetic cost in r (conservative O(r⁴) using a division-free method). Full rational bit cost includes input/weight sizes and intermediate growth; O(r⁴) is not a bit-complexity claim.

## 3. One-sided exact test with an explicit probability bound (AL2)

Choose positive integers \(w_i\) independently and uniformly from F={1,...,H}. Compute all \(e_j(K(w))\) *exactly* and set \(\widehat d=\max\{j:e_j(K(w))\ne0\}\).

**Theorem AL2.** Always \(\widehat d\le d(C)\). When \(d=d(C)>0\),

\[
\Pr(\widehat d<d)\le\min(1,d/H).
\]

For T independent probes and the largest observed \(\widehat d\), the bound becomes \(\min(1,d/H)^T\) (at most \((r/H)^T\) for H>=r). The case d=0 is detected exactly. Thus \(2(m-\widehat d)\) is always an upper bound for the actual first Port activation degree, becoming exact with the stated probability.

**Proof.** A nonzero evaluated \(e_j\) entails at least one nonzero j-principal minor by AL1: no false positive degree. The polynomial \(e_d(K(w))\) is nonzero, multiaffine and has total degree d. Schwartz–Zippel over Q bounds its vanishing on uniformly selected rational weights by d/H. Independence gives the T-probe bound. QED.

A zero coefficient at a single point is an observation, not an identity proof. A nonzero exact coefficient is a valid lower-degree witness even if the trial was chosen at random.

## 4. Extracting an explicit named minor (AL3)

**Theorem AL3.** Given weights w with \(e_j(K(w))\ne0\) and \(j\ge1\), at most \(m(m+1)\) further r-by-r characteristic-polynomial evaluations suffice to find a subset S of cardinality exactly j such that \(\det C[S,S]\ne0\).

**Algorithm.** Scan every currently nonzero coordinate i and tentatively set \(w_i=0\). Keep the deletion exactly when \(e_j\) remains nonzero. Repeat scans while the support has more than j coordinates. Return the nonzero support S, and independently evaluate its exact principal determinant.

**Proof.** For the homogeneous squarefree degree-j polynomial \(p(w)=e_j(K(w))\) and current nonzero support W,

\[
\sum_{i\in W}p(w\mid w_i=0)=(|W|-j)p(w).
\]

When \(|W|>j\), p is nonzero, so at least one deletion leaves p nonzero. Each successful scan removes at least one coordinate, and every trial preserves the nonzero p invariant. After at most m-j successful scans (each at most m trials), |S|=j. Only the monomial indexed by S remains, hence
\[
e_j(K(w))=\det C[S,S]\prod_{i\in S}w_i\ne0.
\]
This provides an independently checkable exact certificate. QED.

An unsuccessful deletion must be retested after later removals: signed cancellation may change. The naive exact arithmetic bound is O(m²(mr²+r⁴)); using cached rank-one changes of K reduces it to O(m²r⁴ + m²r²), excluding rational bit-growth. The verifier can check S and the actual nonzero determinant without trusting the probe's random choice.

## 5. Explicit positive nonsymmetric cancellation example

Take

\[
U=\begin{pmatrix}1&1\\1&2\\1&3\end{pmatrix},\qquad
V=\begin{pmatrix}1&1\\1&2\\1&1\end{pmatrix},\qquad
C=UV^T=\begin{pmatrix}2&3&2\\3&5&3\\4&7&4\end{pmatrix}.
\]

Both factors and C have rank 2, and every entry is strictly positive. Its three 2-by-2 principal minors are 1, 0, -1. Thus d(C)=2. Yet at uniform w=(1,1,1), their sum cancels: \(e_2(K)=0\), and \(\widehat d=1\). At w=(1,1,2), \(e_2(K)=1-2=-1\), giving the correct degree 2 and a nonzero extracted principal minor. This directly refutes unweighted spectral-coefficient detection for general positive nonsymmetric factors; it is not a counterexample to the Gram case.

## 6. Deterministic sign-coherent sector (AL4)

**Corollary AL4.** If C is a P0 matrix, meaning all its principal minors are nonnegative, then uniform positive weights w=(1,...,1) determine d(C) exactly from the single reduced characteristic polynomial: \(e_j(K(1))>0\) if and only if some j-principal minor is nonzero.

**Proof.** Each term in the AL1 sum is nonnegative. Their sum is positive exactly when at least one is positive. QED.

In particular C=UU^T has squared Gram principal minors and recovers R284AJ. Merely positive *entries* do not establish the P0 hypothesis.

## 7. Exact regression and scope

Reproducible Python/SymPy 1.14.0 script: R284AL_random_diagonal_principal_witness_checker.py. Output: R284AL_exact_verification.json.

The deterministic seeded exact-rational run covers the 3-by-3 cancellation example; 192 strictly positive factor instances over m=3..6 and r=1..3 with 5,568 exhaustive principal subset determinant comparisons; and k=2..5 members of the R284AK principal-rank gap family. The 192 single-probe estimates equal the enumerated exact d(C); 192 nonzero principal witnesses are independently checked; four rank-gap instances have verified degree-two witnesses. No floating-point tests are used. The finite PASS suite checks examples and implementation, not the universal AL1–AL4 proofs or the Monte Carlo error guarantee.

This is an observer *diagnostic* for independent named Port edges, not a license to collapse the joint state, path multiplicity, signs, amplitudes, provenance, or future edit operations. AL1 is ordinary exact rational algebra, not a native BRC–Shor computation or a physical heartbeat claim.

## 8. Next frontier

Determine whether a polynomial **bit**-complexity, deterministic upper certificate for d(C) exists under useful structural constraints beyond P0, or a bounded-treewidth/BRC joint-path graph certificate avoids signed cancellation without exponentially large substitution weights. Benchmark end-to-end input-factorization, rational bit growth and witness extraction against R284Y principal-minor enumeration and R284AE graded Schur expansion, with named future-operation scope preserved.

This is independent portable research; no formal CLAIM, Result, independent Review, or new P000 interpretation is inferred. Activity registration/checkpoint association is an operationally separate step.
