# R250 — Two exact spectral-collision families and a sharp generic recurrence order of 229

Date: 2026-11-17 (Asia/Shanghai). Scope: seven-source reversible sticky-reset **auxiliary positive scalar observer** inherited from R234–R249. Status: AUTHOR_PROVED / EXACT_RATIONAL_GCD_CERTIFICATE / NOT_REVIEWED. Immutable scientific input pin: 43ec6098b1330ae86d0a7863be336c5d97f6ef34. Native signed X6/BRC-port attribution is not asserted by this scalar model.

## 1. Fixed model

For \(39/100<s<41/100\), with both endpoints used only for analytic extension, set

\[
 t(s)=\frac{1691s-2615}{2615s-3539},\qquad
 a=(1/5,1/4,3/10,9/20,s,2/3,t(s)).
\]
\[
 b_0=13/60,\quad b_i=\frac5{18}|1/2-a_i|\ (1\le i\le6),\quad
 u_i=1-a_i,\quad \pi_i=b_i/u_i,
 \quad Z=\sum_{i=0}^6 b_i/u_i^2,\quad \rho_i=\frac{b_i}{Zu_i^2}.
\]

Each mask \(m=0,\ldots,62\) specifies \(D_m=\{0\}\cup\{i+1:(m\operatorname{>>}i)\mathbin{\&}1=1\}\). These are all 63 subsets containing index 0 and omitting at least one index among 1,...,6. On each D, define
\[
 (P_D)_{ij}=a_i\delta_{ij}+u_i\pi_j\ (i,j\in D),\qquad
 \Phi_n=\sum_{m=0}^{62} W_{|D_m|-1}\rho_{D_m}^{\mathsf T}P_{D_m}^{n-1}\mathbf1,
\]
where \(W=(144,576,1440,4320,17280,86400,518400)\) and \(n\ge1\). Every weight occurring in \(\Phi_n\) is positive. We study the full scalar-observer sequence, not merely its first two Perron eigenmodes.

## 2. Theorem R250

For **every** real \(s\in(39/100,41/100)\):

1. \(\Phi_n(s)\) is a positive mixture of powers of real eigenvalues \(0<\lambda<1\). Each eigenvalue of every \(P_D\) contributes a **strictly positive** scalar coefficient. Before cross-mask coalescence there are exactly 249 labeled modal terms.
2. Exactly 20 of the 63 mask characteristic polynomials possess the fixed eigenvalue \(\lambda=1/2\). Independently, masks \(m=0\) and \(m=5\) possess the fixed eigenvalue \(\lambda=5/12\). Consequently the minimal scalar linear recurrence order of \(\Phi_n(s)\) is **at most 229**, uniformly in s.
3. At \(s=2/5\), that minimal order is **exactly 229**. It is also exactly 229 for every s in the open interval outside a finite (possibly empty) exceptional set. Thus 229 is a sharp uniform upper bound.

Exact Euclidean GCD arithmetic additionally verifies exact order 229 at each of the 21 rational anchors \(s=j/1000,\ j=390,\ldots,410\). Those finite checks establish precisely their named parameter coverage.

## 3. Proof: characteristic polynomials and positivity

The rank-one matrix identity \(P_D=\operatorname{diag}(a_i)+u_D\pi_D^{\mathsf T}\), together with \(u_i\pi_i=b_i\), gives the monic characteristic polynomial
\[
q_D(x)=\det(xI-P_D)=
\prod_{i\in D}(x-a_i)
-\sum_{i\in D}b_i\prod_{j\in D\setminus\{i\}}(x-a_j). \tag{1}
\]
This polynomial identity also holds at diagonal poles by clearing the factors.

On the interval all seven a's are pairwise distinct in \((0,1)\), and all b's are strictly positive. Set \(H_D=\operatorname{diag}(\sqrt{\pi_i/u_i})\). Then
\[
 H_DP_DH_D^{-1}=\operatorname{diag}(a_i)+vv^{\mathsf T},
 \qquad v_i=\sqrt{b_i}. \tag{2}
\]
This matrix is positive definite. The positive rank-one update of a diagonal matrix with pairwise distinct entries and a nonzero component in every coordinate has simple real eigenvalues, by strict secular-root interlacing.

Substitution of the specified Möbius function t(s) yields two exact rational identities:
\[
 \sum_{i=0}^{6}\pi_i=1,\qquad
 Z=\frac{5(7153-4538s)}{16632(1-s)}>0. \tag{3}
\]
Each D is proper, so \(\Pi_D=\sum_{i\in D}\pi_i<1\) and
\(P_D\mathbf1=\mathbf1-(1-\Pi_D)u_D<\mathbf1\).
Nonnegative irreducibility gives spectral radius below one. Combining this with (2) places all eigenvalues in (0,1).

Since \(\rho_i=(\pi_i/u_i)/Z\), we have
\[
 \rho_D^{\mathsf T}P_D^k\mathbf1
 =\frac1Z(H_D\mathbf1)^{\mathsf T}
    (H_DP_DH_D^{-1})^k(H_D\mathbf1). \tag{4}
\]
At any eigenvalue \(\lambda\) of \(P_D\), the symmetric eigenvector has components proportional to \(\sqrt{b_i}/(\lambda-a_i)\). No eigenvalue equals a_i because (1) at x=a_i is nonzero. The secular equation therefore reads \(\sum_{i\in D}b_i/(\lambda-a_i)=1\). Its inner product with \(H_D\mathbf1\) is proportional to
\[
 \sum_{i\in D}\frac{b_i}{(1-a_i)(\lambda-a_i)}
 =\frac{\Pi_D-1}{\lambda-1}
 =\frac{1-\Pi_D}{1-\lambda}>0. \tag{5}
\]
Thus **every** eigenvalue has nonzero and positive squared modal weight in (4); the W weights preserve positivity. Since distinct exponential sequences \(\lambda^{n-1}\) are linearly independent, the minimum scalar constant-coefficient recurrence order equals the number of **distinct** eigenvalues over all blocks.

There are 63 masks containing index 0. Each of six optional indices occurs in exactly 31 (all 32 possible choices minus the excluded all-selected mask). Hence
\[
\sum_m |D_m|=63+6\cdot31=249. \tag{6}
\]

## 4. Proof: permanent collisions at 1/2 and 5/12

At \(x=1/2\), none of the a_i coincide with x, and the secular sum is especially simple:
\[
\frac{b_0}{1/2-a_0}=\frac{13}{18},\quad
\frac{b_i}{1/2-a_i}=
\begin{cases}5/18,&1\le i\le4,\\-5/18,&5\le i\le6.\end{cases}
\]
For a mask containing L selected indices from \(\{1,2,3,4\}\) and H from \(\{5,6\}\), \(q_D(1/2)=0\) iff \(13+5(L-H)=18\), or \(L-H=1\). Exactly
\[
 \binom41\binom20+\binom42\binom21+\binom43\binom22
 =4+12+4=20 \tag{7}
\]
masks meet that condition. This collision family identifies 20 occurrences into one eigenvalue, reducing distinct-mode count by 19.

Independently, \(D_0=\{0\}\) and \(D_5=\{0,1,3\}\) contain no s-dependent indices. Their characteristic polynomials factor over \(\mathbb Q\) as
\[
q_{D_0}(x)=x-\frac5{12},\quad
q_{D_5}(x)=\left(x-\frac5{12}\right)
          \left(x^2-\frac{47}{60}x+\frac{31}{240}\right). \tag{8}
\]
This adds a distinct coincidence at \(5/12\). Therefore there are at most
\[
249-(20-1)-(2-1)=\boxed{229} \tag{9}
\]
distinct eigenvalues at every parameter s, proving the uniform bound.

## 5. Proof: sharpness at s=2/5 and genericity

At rational anchor \(s=2/5\), construct all 63 monic \(q_D\) from (1) over exact \(\mathbb Q[x]\). Exhaustive Euclidean GCDs on the 1,953 unordered pairs give exactly 190 pairs (all \(\binom{20}{2}\) pairs within the half-eigenvalue family) having monic GCD \(x-1/2\), and exactly one pair \((0,5)\) having GCD \(x-5/12\). The remaining 1,762 pairs have GCD 1. Every block has simple spectrum and every eigenvalue contributes a positive scalar coefficient by (2)–(5). Hence the minimal order is 229 at this anchor.

For the generic statement, remove the permanent factors \(x-1/2\) and \(x-5/12\) from the respective monic polynomials. Their other mutual/common-root resultants are rational functions of s with no poles on the parameter interval. All are nonzero as rational functions, since their evaluation at \(s=2/5\) is nonzero by the exact GCD check. The zero set of each nonzero one-variable rational function in the interval is finite. Outside the finite union of these sets no additional eigenvalue collisions occur. Consequently order 229 is generic.

## 6. Reproduction, observer boundary, continuation

Run Python script **R250_common_eigenvalue_certificate.py** with SymPy. It checks the normalization \(\sum\pi_i=1\), positivity and distinctness of a_i, all fixed collision masks, the exact factorization (8), and every GCD for each of the 21 anchors s=390/1000 through 410/1000. Total checked pairs: \(21\cdot1953=41{,}013\), all PASS. Its output is **R250_verification.json**. The continuous assertion is derived analytically above; the executed certificate specifically covers the 21 anchors and establishes the witness of generic sharpness.

This 229-dimensional scalar recurrence is an **observer-specific** quotient retaining all future time-shifted scalar values \(\Phi_{n+k}\). Before that quotient, 249 labeled mask/eigenvalue contributions remain distinct provenance carriers, even when their eigenvalues coincide. They cannot be identified as native signed X6 ports, ordered origins or complete joint-branch state without an independent transfer map/certificate; the BRC/observer discipline retains them.

**Relation to preceding work:** a previously used order-230 Hankel representation remains a valid *upper-order* representation, but is not the minimal recurrence for the present exact 63-mask scalar observer. R250 identifies two structural causes of a smaller order and a reproducible finite witness. A subsequent executable direction is to compute the common-denominator rational generating function and fast exact coefficient extraction using the 229-dimensional least-common-multiple polynomial, followed by rigorous continuous-s interval treatment of the 270/403 dual-mode thresholds. Complexity claims must separately account for rational coefficient bit growth, preprocessing and exact output size.

Provenance: scientific pin 43ec6098b1330ae86d0a7863be336c5d97f6ef34, exact R247–R249 definitions, P000 and ACTIVE worldview unchanged. AUTHOR_PROVED, exact polynomial checking performed, independent review NOT_REVIEWED, native BRC EffectHistogram NOT_EXECUTED, formal CLAIM/Result/Review none for this portable scientific unit.
