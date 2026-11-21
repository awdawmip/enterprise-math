# R762HO — Arbitrary-rank repeated-Port BRC local limit and exact odd-repetition lattice test

**Status:** AUTHOR-PROVED (Fourier/lattice argument), EXACT INTEGER CHECK, NOT_REVIEWED.  
**Task:** RS-X6-TRIADIC-CLOSURE-DYNAMICS / TP2-8B7E13C5904A2D6F1142.  
**Research provenance:** existing EM-X6-3050F6 / MCP-4b2d70a97f594366a7c94a0f8b45df38, original RUN-02913286c177dd0d71e24d11.  
**Frozen science:** `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`.  
**Direct predecessor:** R762HN @ a2f33b8bc1825c4168d31830ff60553b4aed7ae5; this paper extends its full-rank even-repetition theorem, without changing its native/composite distinction.

## Candidate and exact quantities

Take a nonempty closed named-Port word (w=(P_0,\dots,P_m=P_0)) on six distinct native spatial-axis labels; consecutive 2-Ports intersect in one label. For each event set (h_t=\mathbf1_{P_{t-1}\cup P_t}\in\mathbb Z^6), a three-axis *composite candidate* support. Let (F(z)=\prod_{t=1}^{m}(z^{h_t}+z^{-h_t})), and (Z_k=[z^0]F(z)^k). This is the count of **ordered, positive-weight BRC sign sources** after (k) entire repetitions, not cancellation of positive mass.

Set
- (L=\sum_t\mathbb Z h_t\subset\mathbb Z^6), with real span (V) and rank (r\in\{1,\dots,6\});
- (M=V\cap\mathbb Z^6) (saturated integral lattice), (q=[M:L]), and \(\Delta=\operatorname{covol}_V(M)\);
- (H=\sum_t h_t\) and (C=\sum_t h_t h_t^T), a positive semidefinite (6\times6) integer matrix of rank (r);
- (\operatorname{pdet}C\) is the product of the (r) strictly positive eigenvalues of (C).

The native six-axis space remains six-dimensional. The rank (r) describes only how many directions this **fixed composite event family** actually excites.

## Theorem HO1 — integral coset, exact zero and full rank-deficient local limit

For each integer (k\ge1), every signed displacement is in the lattice coset
\[
 kH+2L.
\]
Consequently, if (kH\notin2L), then **(Z_k=0) exactly**. Since (H\in L), this happens precisely for odd (k) when (H\notin2L).

Along **all integers (k\to\infty) satisfying (kH\in2L)**,
\[
\boxed{Z_k
=2^{mk}\,\frac{2^r q\Delta}{(2\pi)^{r/2}\sqrt{\operatorname{pdet}C}}
\,k^{-r/2}\left(1+O_w(k^{-1})\right).}
\]
The implied constant depends on the fixed word (w), not on (k).

In particular:
1. For *every even* (k), (Z_k>0), and the displayed law holds.
2. If (H\in2L), the law holds for **all sufficiently large integers (k)**, of either parity. Odd-repetition signability can fail at small (k) but is eventually guaranteed.
3. If (H\notin2L), all odd repetitions vanish exactly and even repetitions obey the same law.
4. For (r=6), (M=\mathbb Z^6) and (\Delta=1), recovering R762HN's (64q/((2\pi)^3\sqrt{\det C})\,k^{-3}).

### Proof

**Coset and eventual construction.** Any choice of signs at event occurrences has the form
\[
\sum_{t,j}\varepsilon_{t,j}h_t=kH-2\sum_t n_t h_t,
\]
where (0\le n_t\le k) counts negative occurrences for event (t). Thus zero requires (kH\in2L). When (k) is even, take (n_t=k/2) for every (t), proving (Z_k>0).

If (H\in2L), choose fixed integers (a_t) with (\sum_t a_t h_t=H/2). For sufficiently large odd (k), let (n_t=(k-1)/2+a_t); all (n_t) then lie in ([0,k]), and (kH-2\sum_t n_t h_t=0). This proves eventual odd-repetition signability without analytic assumptions.

**Saturated coordinates.** Choose an integer basis (B\in\mathbb Z^{6\times r}) of (M). Because (M\subset\mathbb Z^6) is saturated, its basis extends to a unimodular integral basis of \(\mathbb Z^6\). Each (h_t=B a_t) with (a_t\in\mathbb Z^r), and \(A=\sum_t a_t a_t^T\) is positive definite. The transformed integer lattice \(\sum_t\mathbb Za_t\) has index (q) in \(\mathbb Z^r\). With (C=B A B^T),
\[
\operatorname{pdet}C=\det(A)\det(B^TB)=\det(A)\Delta^2.
\]

**Fourier maxima and parity character.** The exact normalized constant-term integral becomes an (r)-torus integral:
\[
\frac{Z_k}{2^{mk}}=(2\pi)^{-r}\int_{[-\pi,\pi]^r}
\left[\prod_t\cos\langle a_t,\theta\rangle\right]^k d\theta.
\]
The absolute maxima are exactly the annihilator of (2\sum_t\mathbb Z a_t), a finite character group of order (2^r q). At any maximum (\theta_0), the integrand's base sign is (e^{i\langle \sum_t a_t,\theta_0\rangle}\in\{\pm1\}). Thus the sum of maximum phases after (k) repetitions is the character sum
\[
\sum_{\theta_0}e^{ik\langle\sum_t a_t,\theta_0\rangle}
=\begin{cases}2^r q,&kH\in2L,\\0,&kH\notin2L.\end{cases}
\]
The zero case also follows from the exact coset proof. In the allowed case all (2^r q) maxima contribute with the **same positive phase**.

Near each maximum (\theta_0+u),
\[
\log\big|\prod_t\cos\langle a_t,\theta_0+u\rangle\big|
=-\tfrac12u^T A u+O(\|u\|^4).
\]
Gaussian integration gives \((2\pi/k)^{r/2}/\sqrt{\det A}\) at each maximum, with relative error (O(k^{-1})). Away from their neighborhoods the modulus is bounded below one. Substituting \(1/\sqrt{\det A}=\Delta/\sqrt{\operatorname{pdet}C}\) proves the formula. QED.

The *lattice index* (q), *saturated covolume* \(\Delta\), *integral parity class* (H+2L), and *rank* (r) are separately necessary data. Replacing the six-dimensional determinant by a pseudodeterminant alone would lose \(\Delta\).

## Exact closed-Port special families

| Named Port cycle | m | rank r | exact (Z_k) | admissible k | leading (Z_k/2^{mk}) |
|---|---:|---:|---|---|---|
| 01→02→01 | 2 | 1 | \(\binom{2k}{k}\) | all | \(1/\sqrt{\pi k}\) |
| 01→02→03→02→01 | 4 | 2 | \(\binom{2k}{k}^2\) | all | \(1/(\pi k)\) |
| 01→02→03→01 | 3 | 3 | \(\binom{k}{k/2}^3\) for even k; 0 for odd k | even | \((2/(\pi k))^{3/2}\) |

Here the first example has \(\operatorname{pdet}C=6,\Delta=\sqrt3,q=1\), and the second has \(\operatorname{pdet}C=20,\Delta=\sqrt5,q=1\). The third has \(\operatorname{pdet}C=7,\Delta=\sqrt7,q=1\). The displayed exact binomial formulas follow because the distinct support vectors are linearly independent; each support type must separately have zero signed multiplicity.

## 14-event historical word: extension to odd repetition counts

Use the **same** R762HK/R762HN 14-event closed Port word:

`01→15→12→25→24→04→05→03→04→24→23→25→35→05→01`.

R762HN proved \(L=\{x\in\mathbb Z^6:\sum_i x_i\equiv0\pmod3\}\) using a determinant -3 minor and the 3-ones-column rule, so (q=3), (r=6), and \(\det C=3456\).

The support total is (H=(8,4,8,6,6,10)). Its half is the integer vector \((4,2,4,3,3,5)\), with coordinate sum 21 divisible by 3; hence **(H\in2L)**. Therefore the previous even-(k) asymptotic now extends to **every positive integer (k\to\infty)**:
\[
\boxed{Z_k=\frac{2^{14k}}{\pi^3\sqrt6\,k^3}(1+O(k^{-1})),\qquad k\to\infty\ \text{without a parity restriction}.}
\]

A new direct and grouped-binomial coefficient computation obtains
\[
 Z_3=1,700,835,440
\]
for 42 events, agreeing by **two different finite positive-weight integer recurrences**. The old results (Z_1=104\) and (Z_2=313080\) are reproduced for this focused crosscheck; R762HN already independently checked (Z_4=12,464,855,922,680\). The exact-to-leading probability ratios at (k=1,2,3,4) are approximately (0.48210,0.70865,0.79303,0.84084) respectively; this numerical trend is not the proof.

## Verification, status, and next questions

Run `g++ -O3 -std=c++17 -Wall -Wextra R762HO_CHECK.cpp -o r762ho && ./r762ho`. The independent group-factor vs sequential-event DP agrees for the 14-word at (k=1,2,3); rank-one/two/three exact binomial identities agree for (k=1,2,3,4). Arithmetic is unsigned 64-bit integer counting with six nonoverlapping biased byte coordinates; tested absolute displacements are at most 42. Verification output: `PASS`.

**Boundaries:** The theorem concerns finite fixed composite candidate support words; it preserves all six original axes and original BRC event provenance. It does not define the primitive force incidence, native triadic closure or physical time/rotation semantics fixed as open in P000. Analytic proof author-check only; independent Review remains `NOT_REVIEWED`. The global signability of parity-even *unrepeated* closed Port histories also remains open.

**Next discriminating questions:** classify the rank/index and odd-repetition parity classes of all small closed Port words; seek a legal Port word with coordinate-even (H) but (H\notin2L) (a hidden residual beyond coordinate parity), or prove that the Port adjacency rules exclude such words; attack signability for all single histories using graph-factor/half-path certificates. Independently construct native `TRIADIC_CLOSURE_E` typed force/Cell/Link/Port/time/rotation events.
