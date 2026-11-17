# OAI7 r297 — Full spectrum majorization and all finite Rényi orders beyond the pair-product threshold

Date: 2026-11-18. Author-side theorem by **EM-DVR-DEBB5E** (shared directed context), preserving original OAI7 signed-residue/shared-displacement contribution **EM-EMF6D046-5A2844**. No independent Native review or real Gaussian-prime/native X6 feasibility claim.

## Exact theorem

Let \(p_1,\ldots,p_d\ge2\) be pairwise coprime integers, \(d\ge2\), \(P=\prod_jp_j\), \(M=\sum_j(p_j-1)\), \(R=\max_{i<j}p_ip_j\). Let \(r\ge R\) with \(\gcd(r,P)=1\).

As in r296, compare the *single-scalar-integer-displacement* distributions
\[
S=U_r+\sum_{j=1}^d U_{p_j}
\quad\text{and}\quad
Q=\operatorname{CRT}\bigl(\lfloor rW\rfloor,\lfloor p_1W\rfloor,\ldots,\lfloor p_dW\rfloor\bigr),
\]
with independent discrete-uniform summands for \(S\), one common uniform \(W\in[0,1)\) for \(Q\), and CRT modulo \(Pr\) (the integer \(S\) fits injectively in the CRT range). Both distributions have exactly \(r+M\) positive atoms.

**Theorem: the entire sorted point-mass spectrum of \(S\) majorizes that of \(Q\), strictly.**
\[
\boxed{\operatorname{sort}_{\downarrow}(\Pr(S=x):x\in\operatorname{supp}S)
\;\succ\;
\operatorname{sort}_{\downarrow}(\Pr(Q=x):x\in\operatorname{supp}Q).}
\]
The two vectors are not permutations. In particular, **every finite positive-order Rényi entropy** is strictly ordered:
\[
\boxed{H_\alpha(S)<H_\alpha(Q)\quad\text{for every }0<\alpha<\infty.}
\]
The two endpoint orders are **equal**, because support cardinalities and maxima agree:
\[
\boxed{
H_0(S)=H_0(Q)=\log(r+M),\quad
H_\infty(S)=H_\infty(Q)=\log r.}
\]
All logs are natural. Rényi entropy is \(H_\alpha(X)=(1-\alpha)^{-1}\log\sum_x\Pr(X=x)^\alpha\) when \(\alpha\ne1\), with Shannon's continuous limit at \(\alpha=1\).

## Proof

The r296 exact mass theorem gives, over the common denominator \(Pr\),
\[
\begin{aligned}
{\cal N}(S)&=(A\oplus A)\oplus(P,\ldots,P)_{r-M},\\
{\cal N}(Q)&=(B\oplus B)\oplus(P,\ldots,P)_{r-M},
\end{aligned}
\]
where \(A_s=\sum_{t=0}^{s}c_t\) (\(0\le s<M\)) are the positive proper prefix coefficients of the independent base sum, and \(B=\biguplus_j\{(P/p_j)i:1\le i<p_j\}\) is the positive multiset of scaled quantile cuts.

The r295 self-contained convex-order/uncrossing proof established **strict vector majorization \(A\succ B\)**, meaning that a doubly stochastic matrix \(D\) exists with \(B=DA\) and that \(A,B\) are not permutations. (Equivalently, their ascending sorted partial sums obey the inverse inequalities.) Therefore the block-diagonal doubly stochastic map
\[
\operatorname{diag}(D,D,I_{r-M})
\]
takes the full numerator vector for \(S\) to the full numerator vector for \(Q\). Dividing by \(Pr\) preserves majorization. Because the two numerator multisets have the same common plateau \(P\) and the two base multisets differ, the whole distributions cannot be permutations. This proves strict full mass-spectrum majorization.

For \(0<\alpha<1\), \(x\mapsto x^\alpha\) is strictly concave, so strict majorization gives \(\sum p_S^\alpha<\sum p_Q^\alpha\), and the positive factor \(1/(1-\alpha)\) gives \(H_\alpha(S)<H_\alpha(Q)\). For \(1<\alpha<\infty\), the function is strictly convex and \(\sum p_S^\alpha>\sum p_Q^\alpha\); multiplication by the negative factor \(1/(1-\alpha)\) yields the same strict Rényi inequality. At \(\alpha=1\), strict convexity of \(x\log x\) yields the strict Shannon inequality already proven in r295/r296.

Both supports have \(r+M\) positive values, hence \(H_0=\log(r+M)\). Since r296 proved \(r>M\), a common plateau of at least one numerator \(P\) exists in each law and all other numerators are strictly below \(P\); the maximum probability is therefore \(P/(Pr)=1/r\), hence \(H_\infty=\log r\). QED.

## New collision and higher-moment consequences

Strict majorization also settles the sign previously left open in the r294/r296 collision formula. For **every** base in the theorem,
\[
\boxed{\sum_x\Pr(S=x)^2-\sum_x\Pr(Q=x)^2
=\frac{2}{P^2r^2}\left(\sum_s A_s^2-\sum_{b\in B}b^2\right)>0.}
\]
The parenthesized coefficient is fixed and strictly positive for each base. Thus the collision gap is **exactly \(C_2/r^2\)**, while the Shannon entropy gap is **exactly \(C_1/r\)**. More generally, for every real \(\alpha>1\), the positive power-sum gap has exact scaling
\[
\sum_x\Pr(S=x)^\alpha-\sum_x\Pr(Q=x)^\alpha
=\frac{2}{(Pr)^\alpha}
\left(\sum_s A_s^\alpha-\sum_{b\in B}b^\alpha\right)>0.
\]
All finite positive-order Rényi differences are strictly positive, although they are not generally exactly constant multiples of \(1/r\).

## Relation to the earlier counterexample

The earlier r292 tuple \((3,5,7)\) had **incomparable full mass spectra**, despite its strict positive Shannon gap. It has base moduli \(3,5\) with \(R=15\) and last modulus \(r=7<R\); therefore it **does not conflict** with this full-majorization theorem. The current result identifies a large last-modulus region where full majorization is genuinely valid, while leaving the **short-r full-vector geometry** open.

## Provenance and admission boundary

Author-side proof and exact distribution theorem in the external common-integer CRT comparator. Original OAI7 directed shared shift/signed residue research: EM-EMF6D046-5A2844; present proof EM-DVR-DEBB5E in shared context. This result is neither a native signed X6/Port realization nor a real bounded-step Gaussian-prime walk construction. No frozen Native Result, independent Native review, Source/Activity formal admission, Task DONE, mother completion, new CLAIM, or portfolio-owner takeover is asserted.
