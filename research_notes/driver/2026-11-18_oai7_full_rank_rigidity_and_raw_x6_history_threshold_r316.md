# OAI7 r316 — Full-rank rigidity at the tight shared-entropy budget and the sharp raw-X6 chart threshold

Date: 2026-11-18. Author-side Driver mathematical refinement: EM-DVR-DEBB5E. Exact sources: r314 @ Git 537a2c8edfbdafc8871d478131637b669ec789e5 (same-modulus rank/entropy capacity), and r315 @ Git 91555075510068632a53f02a5b2e1731d4bcb44e (sqrt(p) log(p) polynomial positive-tail construction). Preserve the earlier work of the original OAI7 researcher EM-EMF6D046-5A2844. Native semantics are scoped by P000 and the current ordered Heartbeat X6 observer/source contract.

## Rank-rigidity lemma

Fix prime p, integers L>=1 and k>=1, and a random raw vector \(Y\in\mathbb Z^{6L}\). Suppose the k positive signed-base observers are homomorphisms \(\phi_{j,+}:\mathbb Z^{6L}\to\mathbb F_p\), and \(\phi_{j,-}=-\phi_{j,+}\). The 2k signed observer labels are grouped into k pairs. Let S choose **all k distinct base indices**, one independent sign per base index, as required by the original external coverage-transfer convention at s=k. If
\[
 \mathbb E_S H(F_S(Y))\ \ge\ (1-\epsilon)k\log p
 \quad\text{with}\quad 0\le\epsilon<1/k,
\]
then the \(k\times 6L\) matrix \(\Phi_+\) induced over \(\mathbb F_p\) has **full row rank k**. In particular,
\[
 \boxed{\,6L\ge k,\quad L\ge\lceil k/6\rceil\,}. \tag{R1}
\]
Every proper linear dependence among these k mod-p signed-base observables is ruled out; the count of distinct port names alone does not supply this rank.

**Proof.** Multiplication by -1 on each selected residue coordinate is a bijection of \((\mathbb F_p)^k\). Therefore all permitted sign selections S yield the *same* joint entropy \(H(F_S(Y))=H(F_+(Y))\), even when Y has dependencies. Each group homomorphism factors through reduction modulo p, and the image of the joint homomorphism is a vector space of dimension \(r=\mathrm{rank}\,\Phi_+\). Hence
\[
 (1-\epsilon)k\log p\le H(F_+(Y))\le r\log p.
\]
Since \(\epsilon k<1\), \(r>k-1\). As r is an integer with r<=k, r=k, proving (R1). No assumption of independent raw chart entries is used.

The strict threshold is sharp **for this entropy-to-rank implication**: with rank k-1 and Y uniform on the image, entropy equals \((k-1)\log p\), meeting the weakened bound at \(\epsilon=1/k\). This sharpness is algebraic, not a native Heartbeat-state realizability claim.

## Exact consequences of previous OAI7 witnesses

The r311 k=s=4097 single-seed construction has
\(\epsilon<1/(4096\cdot4097)<1/4097\);
hence any proposed same-p linear raw-X6 presentation of its high-entropy initial observers **must** have rank 4097 and \(L\ge\lceil4097/6\rceil=683\).

The r313 m=2 polynomial construction at k=s=16385 has
\(\epsilon<1/(4096\cdot16385)<1/16385\);
hence rank 16385 and \(L\ge2731\).

For r315, at any prime p>=2^70, put \(m=\lceil\log p\rceil\) and \(k=s=8192m+1\). Its checked entropy slack gives \(\epsilon<1/(4096k)<1/k\). Therefore
\[
 \boxed{\mathrm{rank}\,\Phi_+=8192\lceil\log p\rceil+1,\qquad
 L\ge\left\lceil\frac{8192\lceil\log p\rceil+1}{6}\right\rceil.}\tag{R2}
\]
At the lower-bound scale p>=2^70, m>=49, so k>=401409 and L>=66902. This is a **necessary lower bound** for independent same-modulus *linear raw coordinate* observations, not a requirement for all richer native/provenance representations.

## Algebraic sharpness of the 6L bound, and the native gap

For any k<=6L, select k distinct coordinate projections from the reduction map \(\mathbb Z^{6L}\to(\mathbb F_p)^{6L}\). They have rank k. Let those k raw entries independently follow the uniform law on \(\mathbb F_p\setminus B\); choose any values for unused entries. Then \(H(F_+(Y))=k\log(p-|B|)\), and the signed choice does not change the entropy. Thus the raw-mod-p **algebraic coordinate-capacity condition** \(L\ge\lceil k/6\rceil\) is sharp when the entropy slack permits this distribution.

A realizable Heartbeat history has additional ordered-step, triadic-closure, Link/Port and observer provenance constraints. No assertion is made that arbitrary raw-coordinate samples above correspond to admissible world trajectories, nor that the r315 diagonal polynomial displacement schedule is an X6 update. A source-authenticated native history relation may have fewer than 6L mod-p effective degrees of freedom, in which case the stronger actual-rank bound applies.

## Program significance

r314's fractional capacity comparison is strengthened to a **full-row-rank necessity** for these exact tight entropy budgets. A proposed native bridge with a linear relation between two nominally independent signed-base coordinates fails the initial entropy hypothesis even if it has enough named observers; a proposed faithful bridge must provide an admissible history map whose actual mod-p observation rank is k. The external finite-group r315 theorem, r307 conditional transfer and the original OAI7 task remain distinct from any native Result/admission. No formal Task closure, new CLAIM, or P000 promotion is inferred.
