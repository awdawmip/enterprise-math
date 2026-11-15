# R106: a local central μ₃ action and the remaining global/integral lifting question

Date: 2026-11-15. Status: EXACT CONDITIONAL LEMMA / RESEARCH FRONTIER; not R106 completion or independent review.
Task: RS-EMF6D046-R106-TWO-ADIC-HERMITIAN-UNITARY, publication TP2-402BA15B13CB1466DCBD.
Parent source: R105 handoff in research_notes/EM_FREE_F6D046_R105_STATE_MACHINE_HANDOFF_20260909.md; frozen branch research/em-free-f6d046-ramanujan-period-wronskian-20260904@574f53c7b37ae6703ade390df851d8822af6364c.

## Exact conditional lemma (maximal unramified coefficient order)

Let K/Q₂ be the unramified quadratic extension, O=O_K, σ the nontrivial field involution, k=O/2O≅F₄. Let (V,h) be any nondegenerate Hermitian K-space and L⊂V a full O-lattice. Suppose its Hermitian dual quotient D=L^#/L exists as an O-module and D≅O/2O. Define U_O(L)={g∈Aut_O(L):h(gx,gy)=h(x,y) for all x,y}. The induced action ρ:U_O(L)→Aut_O(D)≅k^× is **surjective** and splits centrally, and hence U_O(L)≅ker(ρ)×C₃. Its permutation action on the three nonzero elements of D (equivalently their F₂-lines) has image C₃ and is transitive. This is independent of the Gram matrix under the stated premises.

Proof. In the unramified extension K, the Teichmüller group μ₃⊂O^× maps isomorphically to k^×. Choose ζ≠1 in μ₃. Since σ reduces to the Frobenius x↦x² on k and Teichmüller lifts are unique, σ(ζ)=ζ². Therefore ζσ(ζ)=ζ³=1. Scalar multiplication ζ·id_V preserves h and the O-module L, so ζ·id∈U_O(L), and lies in the center of this O-linear unitary group. It preserves L^# and acts on D by multiplication by ζ mod 2, which is an element α of order three. The image of ρ is thus all k^×=C₃. The central homomorphism μ₃→U_O(L) is a section of ρ through reduction, and its intersection with ker(ρ) is trivial, yielding the direct-product decomposition. The finite multiplication cycle is 1↦α↦α²↦1 using α²+α+1=0 in F₄. ∎

The action is O-linear, so its image cannot contain the F₄/F₂ Frobenius permutation; an extended semilinear group is a distinct object.

## Exactly what this lemma does and does not decide

R105 reports the unramified K-factor, the F₄-valued Prym polarization kernel, and the three degree-two principalization choices. It also reports the **global** CM scalar-unit reduction as trivial, while selecting a principalization lowers its scalar endomorphism order to R=Z₂+2O. The lemma concerns the **entire local O-stable unitary lattice group**, not the image of actual global polarized automorphisms or an arbitrary R-stable lattice. A local ζ scalar need not arise from a global automorphism of the underlying abelian fourfold, and a lattice stable only under R need not be stable under ζ. A non-scalar global automorphism may still have a nontrivial effect even when global scalar units do not.

Thus “local unitary orbit is C₃ under maximal-O lattice hypotheses” and “global principalization orbit remains unresolved” are compatible. Interpreting the R106 task simply as computing all local O-linear lattice isometries would lead to the C₃ answer under the lemma's premises; interpreting its intended action as *globally realizable*, or as isometries of a smaller coefficient-order carrier, requires additional evidence.

## Smallest discriminating research input

Extract the exact integral Hermitian Gram/module/dual carrier from the frozen R105 original proof; record separately (a) the order acting on the *underlying Prym/polarization-kernel lattice*, (b) the order acting on each *principalized carrier*, and (c) the subgroup of local U(L) induced by *global integral polarized automorphisms*. Determine which of these is the group meant by R106's “full U(L)”. Compute the exact reduction image for that group and provide a matrix/generator certificate. Preserve original R105 global scalar-order and CM claims verbatim; do not infer the global C₃ orbit merely from the local μ₃ construction. If the Gram or global lift subgroup is not recoverable, supply a scoped underdetermination witness instead.

Reproducibility for the conditional lemma: in k=F₂[a]/(a²+a+1), nonzero elements {1,a,a²} are cyclic under multiplication by a; σ(a)=a², aσ(a)=1. These are exact finite-field identities, no numerical approximations.

Remaining hard target: FULL_TWO_ADIC_HERMITIAN_UNITARY_ORBIT for the actual R105 carrier, including global/local scope reconciliation and the requested machine-checkable full-group certificate. This note is an independently proved conditional sub-lemma, **not** the full classification, a frozen Result, acceptance, or R107 proof.
