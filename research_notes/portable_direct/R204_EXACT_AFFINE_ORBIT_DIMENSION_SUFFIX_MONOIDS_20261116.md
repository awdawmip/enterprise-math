# R204 — Exact minimal orbit-separating affine dimension for every suffix monoid over every finite field

Date: 2026-11-16. Status: AUTHOR_PROVED / EXACT_INTEGER_FINITE_CHECKED / NOT_REVIEWED.

Frozen scientific input: \`awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34\`. Direct predecessor: [R202](https://github.com/awdawmip/enterprise-math/blob/f721c4b479b6b387d4b27566f9be3cf3b6863f69/research_notes/portable_direct/R202_SUFFIX_AFFINE_ORBIT_RANK_LOWER_BOUND_20261116.md), especially the remaining field-size-power case. The exact native BRC affine API was inspected at this frozen pin: \`src/enterprise_math/brc_transport.py\` (blob \`be1debe367263931bd5e93fd750be3ed54624fe1\`). This theorem is a finite quotient representation result and does not change P000, the six native axes, their twelve directions, full provenance, or any physical interpretation.

## Theorem (R204-A: exact optimum)

Let \(F_q\) be any finite field of size \(q\ge2\). Let \(A\) be a finite alphabet of size \(a\ge1\), and let \(L\ge1\). Define the suffix monoid \(T_{a,L}\) as all words of lengths \(0,1,\ldots,L\), multiplying words by concatenation followed by retaining the final \(L\) letters. Let \(d_{\mathrm{orbit}}(q,a,L)\) be the smallest nonnegative integer \(D\) for which a monoid homomorphism \(\rho:T_{a,L}\to\mathrm{Aff}(F_q^D)\) has an orbit point \(p\) such that \(t\mapsto\rho(t)p\) is injective on **all** \(T_{a,L}\). Then

\[
\boxed{d_{\mathrm{orbit}}(q,a,L)=L\lceil\log_q(a+1)\rceil.}
\]

For the degenerate \(L=0\), the monoid is a singleton and the mathematical minimum is \(D=0\).

## Lower bound, including field-size-power alphabets

Put \(c=\lceil\log_q(a+1)\rceil\). In any orbit-separating affine representation, let \(O=\{\rho(t)p:t\in T_{a,L}\}\), and let \(V=\operatorname{AffSpan}(O)\), an invariant affine subspace. Restrict the representation to \(V\), write \(d=\dim V\le D\), and fix one letter \(s\in A\). The corresponding affine generator \(f_s\) has linear part \(M\) on the translation space of \(V\).

1. Every word \(ws^L\) has the same suffix \(s^L\), so \(f_s^L\) maps all of \(O\) to one point. Because an affine map constant on an affine-spanning set is constant on its affine span, \(M^L=0\) on \(V\).
2. The \(a+1\) words \(s^{L-1}\) and \(x s^{L-1}\) for all \(x\in A\) are distinct in \(T_{a,L}\): the first has length \(L-1\), the others have length \(L\) and distinct first letters. Their distinct orbit points all belong to \(f_s^{L-1}(O)\). This image lies in an affine space of dimension \(r=\operatorname{rank}(M^{L-1})\), with at most \(q^r\) points. Hence \(q^r\ge a+1\), so \(r\ge c\).
3. Since \(M^L=0\), pick \(r\) vectors \(u_i\) whose \(M^{L-1}u_i\) are linearly independent. The \(Lr\) vectors \(M^j u_i\) for \(0\le j<L\) are linearly independent. Indeed, in a putative dependence choose the smallest exponent \(j\) having a nonzero coefficient and apply \(M^{L-1-j}\); all higher powers vanish, while the surviving \(M^{L-1}u_i\) are independent.

Thus \(D\ge d\ge Lr\ge Lc\). The extra distinction between **the short word** \(s^{L-1}\) and the **full-length words** \(xs^{L-1}\) strengthens R202's previous \(L\lceil\log_q a\rceil\) lower bound. This step resolves the field-size-power case without assuming identical linear parts for different generators.

## Matching explicit construction (R204-B)

Because \(q^c-1\ge a\), choose any injection \(\gamma:A\hookrightarrow F_q^c\setminus\{0\}\). Use \(L\) registers of \(c\) coordinates each, initialized to zero. For a letter \(x\), apply

\[
(z_1,z_2,\ldots,z_L)\longmapsto(z_2,\ldots,z_L,\gamma(x)).
\]

This is an affine update of dimension \(Lc\), defined over every field \(F_q\). A word shorter than \(L\) produces left-zero padding followed by its distinct nonzero letter codes; a word of length at least \(L\) produces the final \(L\) codes. Hence the orbit of the zero vector distinguishes every suffix-monoid element. The complete affine action after any history depends only on its suffix-class: a short word acts by the corresponding shift and append, and a length-\(L\) word acts constantly. Therefore the construction descends to a monoid homomorphism. The lower bound is attained.

## Precise resource consequences

For the native selected paired event-tail alphabet \(a=12(6+1)=84\) and \(L=2\), over \(F_2\), \(c=\lceil\log_2(85)\rceil=7\), so the **exact orbit-separating affine tail dimension is 14**. This confirms the tail block optimality of R201/R202. It does not imply that the R201 complete joint observer dimension 35 is minimal, because source and tail coordinates may interact.

For the formerly open field-size-power case \(a=q^h\), \(c=h+1\), and the exact orbit minimum is \(L(h+1)\). A *faithful action representation without an injective fixed orbit* still admits dimension \(Lh\) by R202-C; those are different interfaces. For example, \(q=2,a=4,L=3\): the exact orbit minimum is 9, compared with 6 for the action-faithful shift representation and 7 for the information-only fixed-width lower bound \(\lceil\log_2(1+4+16+64)\rceil\).

## Verification and provenance

Run \`node R204_suffix_orbit_exact_minimum_check.mjs\`. The pure JavaScript exact integer script enumerates every quotient state and distinct zero-orbit output for eight prime-field sample models; it checks basis-vector equality of suffix composition on 3,476 sampled pairs, 33,512 corresponding affine evaluations, and 24 independent shift-rank witnesses. It covers \(q=2,3,5\), and \(a=84,L=2\) as the native observer-tail parameter case. Results are recorded in \`R204_verification.json\`. These finite tests verify the construction in stated models; the displayed algebraic proof establishes the arbitrary finite-field theorem.

No independent mathematical review or native installed-package execution has been performed. The existing R201 native probe remains an executable next unit, together with the unrestricted minimal dimension of the entire R200 paired source/event observer and a measured cost comparison between 14-slot suffix orbit, full 35-slot affine observer, complete joint rank codec and sparse second moments.

Research activity: independent portable research only. The existing Researcher-ID and prior Activity are historical provenance; no current Task CLAIM/Result/Review or another researcher's active ownership is asserted.
