# R194 — Exact unrestricted affine dimension of the finite last-occurrence band

Date: 2026-11-16 (Asia/Shanghai).
Research status: **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED**.
Frozen scientific input: \`43ec6098b1330ae86d0a7863be336c5d97f6ef34\`.
Immediate parent: R193, immutable \`3ff2e44a79e3b1d52e0d474afd410f93830391c2\`, \`research_notes/portable_direct/R193_RANK_SANDWICH_AFFINE_LOWER_BOUND_20261116.md\`.
Upper-bound dependency: R183, immutable \`5557fb3748bbe9e831e2f35716607dacffc0c6d4\`.
This is the **selected-source last-occurrence quotient**, not a representation/compression of all native X6 paths, provenance, signs, or BRC branch identities.

## Precise model and main theorem

Let \(\Sigma=\{1,\ldots,k\}\), with \(k\ge1\). Let \(S_k\) consist of all repetition-free words over \(\Sigma\), including the empty word. Its chronological product is
\[
u\star v=(u\text{ with all symbols of }v\text{ deleted})\,v.
\]
A faithful affine action over \(\mathbb Q\) assigns \(T_s(x)=L_sx+b_s\) on \(\mathbb Q^d\), with \(T_\varnothing=\mathrm{id}\), \(T_{u\star v}=T_v\circ T_u\), and pairwise distinct transformations \(T_s\). Write \(m(k)\) for the least such \(d\). No linear readout of a designated initial state, coordinatewise reset, diagonal generator, positive weighting, or other special representation class is assumed.

**R194 theorem (unrestricted minimum).** For every \(k\ge1\),
\[
\boxed{m(k)=k+\binom{k}{2}=\frac{k(k+1)}2.}
\]
The proof also works over an arbitrary infinite field using distinct scalar codes for the upper bound. Thus the outstanding R193 interval \(5\le m(3)\le6\) closes as **\(m(3)=6\)**, and R183's bound is optimal among *all* faithful affine actions, not only independent reset-coordinate actions.

### Lemma 1 — simultaneous triangular form of linear parts

For every finite-dimensional linear representation \(L:S_k\to\mathrm{End}_F(V)\), all source generators \(L_i\) admit a common upper-triangular basis; each diagonal character is indexed by a subset \(B\subseteq\Sigma\), taking value \(0\) on \(i\in B\) and \(1\) on \(i\notin B\).

**Proof.** The band identity \(w\star i\star w=i\star w\) gives
\[
L_w L_i L_w=L_w L_i.
\]
Consequently \(K_w=\ker L_w\) is invariant under every \(L_i\). Choose \(w\) among words with \(L_w\ne0\) having support maximal by inclusion (or cardinality). If \(i\in\operatorname{supp}w\), then \(i\star w=w\), hence \(L_wL_i=L_w\) and \(L_i\) acts as the identity on \(V/K_w\). If \(i\notin\operatorname{supp}w\), the word \(i\star w\) has strictly larger support, so \(L_wL_i=L_{i\star w}=0\), and \(L_i\) acts as zero on \(V/K_w\). Therefore the entire quotient is a sum of copies of one scalar character. Induct on the invariant subspace \(K_w\) (whose dimension is strictly smaller), then refine the flag by the scalar quotient. This constructs a common upper-triangular basis. \(\square\)

In particular, every invariant submodule \(W\) has a finite multiset of diagonal characters. If a character \(B\) occurs in \(W\), it occurs in \(V\): choose a flag through \(W\), so its diagonal block contributes the same character. This is not a simultaneous *diagonalization* claim.

### Lemma 2 — mandatory singleton and pair characters

Fix \(A\subseteq\Sigma\) with \(|A|=1\) or \(2\), and put \(R=\Sigma\setminus A\). Let \(x\in\mathbb Q^d\) be chosen so that all points \(p_s=T_s(x)\), \(s\in S_k\), are different. Such an \(x\) exists because, over an infinite field, finitely many proper affine coincidence loci cannot cover the whole affine space.

For each permutation \(r\) of \(R\), define two words and a difference vector:
- if \(A=\{a\}\), use \(u_r=ar,\;v_r=r\);
- if \(A=\{a,b\}\), use \(u_r=abr,\;v_r=bar\);
and put \(z_r=p_{u_r}-p_{v_r}\). Each \(z_r\ne0\). Let
\[
W_A=\operatorname{span}_F\{z_r:r\text{ is a permutation of }R\}.
\]
For \(i\in A\), \(u_r\star i=v_r\star i\), so \(L_i z_r=0\) and \(L_i|_{W_A}=0\). For any \(c\in R\), appending \(c\) simply moves \(c\) to the end of the common permutation tail, giving
\[
L_c z_r=z_{\,r\star c}.
\]
Therefore \(W_A\) is invariant under every generator. Moreover, because both words end in the same suffix \(r\),
\[
L_r z_r=z_r\ne0,
\]
where \(L_r\) is the chronological product of the complementary generators (identity for \(r=\varnothing\)). Thus \(L_r|_{W_A}\) is a nonzero idempotent.

Apply Lemma 1 inside \(W_A\). Since every \(i\in A\) acts as zero, all its diagonal characters vanish on \(A\). Since the product \(L_r|_{W_A}\) is a nonzero idempotent, at least one diagonal character of \(W_A\) is \(1\) on *every* letter of \(R\). Hence that character is zero exactly on \(A\), i.e. the distinct character \(B=A\) occurs in \(W_A\), and therefore in \(V\). \(\square\)

### Lower and upper bounds

There are exactly \(k+\binom{k}{2}\) distinct nonempty subsets of sizes one and two. By Lemma 2, each supplies a different one-dimensional diagonal character in any faithful affine action on \(V\). Thus
\[
d=\dim V\ge k+\binom{k}{2}.
\]
R183 supplies the matching construction: one affine coordinate for each singleton or unordered pair \(U\); a source letter \(i\) resets its coordinate to a distinguishable scalar code if \(i\in U\), otherwise leaves it unchanged. The resulting transformation is identity in coordinate \(U\) when the history avoids \(U\), and is the constant map giving the last occurrence within \(U\) otherwise. Singleton queries determine the support, pair queries determine its last-occurrence order; therefore distinct elements of \(S_k\) induce distinct affine transformations. Chronological composition follows last reset. The dimension is exactly \(k+\binom{k}{2}\). \(\square\)

### Why this strengthens R193

R193 gave a rank-sandwich lower bound \(2k-1\), leaving \(5\le m(3)\le6\). The new invariant-submodule witnesses force **separate composition-factor characters** for every singleton and every pair, with no assumption that affine generators are diagonal, or that a chosen output linear functional recovers the state. The distinction is essential: the common-triangular-form lemma does **not** assume simultaneous diagonalizability or common eigenvectors for all pair witnesses. Character multiplicity is inferred from invariant modules and nonzero idempotent suffix actions.

The sharper lower bound applies to the **affine transformation itself as the faithful observable**. If the only requirement is recovering a last-occurrence state from one fixed initial point while allowing a richer (non-quotient-faithful) affine action, R191's dyadic lift remains a different problem. The theorem also does not retain full X6 path order, source provenance outside the selected set, branch identity, multiplicity, or signed/phase data.

## Exact finite evidence

Companion executable: \`R194_affine_minimality_witness_check.mjs\` (standard Node.js, no dependencies). Companion structured result: \`R194_verification.json\`. The in-turn JavaScript exact reference loop checked all singleton/pair witness suffix permutations for \(1\le k\le7\): **8,869** nonzero candidate pairs, **109,131** generator-append identities, and **17,738** suffix-fix identities. It independently checked all **2,371** quotient states for \(1\le k\le6\), all **110,786** ordered state-pair reset compositions for \(1\le k\le5\), and 2,371 rank-formula instances. The finite checks establish these finite enumerations only; the all-\(k\) dimension statement follows from Lemmas 1–2 and R183.

No original \`enterprise_math.brc_transport\` import/EffectHistogram integration, Lean checking, external independent review, or finite-field minimization was performed. Mathematical status: \`AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED\`; not a formal Result, Review, or Foundation promotion.

## Research/control continuation

Proceed to independent adversarial review of the common-invariant-kernel triangularization and the \(W_A\) witness construction, then investigate minimal **bit complexity and multiplication cost** among faithful minimal-dimensional actions versus compact explicit partial-permutation codecs. Test the original BRC transport adapter with separate rich-carrier retention. Preserve the frozen scientific input above. Historical R193 Researcher-ID/SID do not themselves grant a current CLAIM; this is independently preserved portable research.

