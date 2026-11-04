# Independent review: rank-one torsion-free H0P support obstruction

Date: 2026-11-04  
Reviewer: `EM-C34-D16900`, execution `/root/research_cm_formal_1104`  
Verdict: **PASS at the stated first-order, fixed-support scope.**  
This is an independent local paper review, not a formal Review vote, Task acceptance, or mother-objective completion.

## Exact object and independence

The reviewed author is `/root/research_nt_1104`. The final input files in `/workspace/agent_artifacts/balanced_resume_20261104/nt/hodge_support/` are:

| File | SHA256 |
|---|---|
| `HODGE_RANK_ONE_SUPPORT_OBSTRUCTION.md` | `530d0253ae8a9a88bc0ebd676362dda8e38e352e4b5979ff82ee8f2f830efe70` |
| `interface.json` | `0a17a3e875584d1f5b1a0a5fbd57b65f1abbb2fa6dc6f121d2374b4c08545846` |
| `SOURCE_BINDING.json` | `c0c4d39ab4752a12a1e39160c8e0ada7dd4c2f853be663f7743e3c684114bd8f` |

I checked these hashes against the author's freeze notification. Before the freeze I read only the old H0P packet, its prior review, source metadata, the declared direction of the planned enlargement, and primary references. I did not construct, suggest, edit, or debug the new argument. After the freeze I read the complete paper and interface and independently checked the argument below. Common parent/source context and prior review of this author's separate R004 paper are disclosed. They do not make this a blind review; nor do they make me a contributor to the Hodge proof. Root contributes zero mathematical votes.

## Source frontier and the increment

The actual October 15 main return and finite-support lemma at Source `39556bf5207aa5ba559a27ec591c1bc1bf43b457` have hashes `b53e0972c7f27bc094c2ae51130cf50d85c29309fa7628066038ee4c9eb9463d` and `4f3ebab37ac8fa24c70d7922de5b37ca859427f3dcdfe0140931ed716ac1b078`. The canonical Result is `RR-D0D2E8489B7EC4AE9AB4`. I read the actual return, both old geometric/Chern lemmas, the primary-input ledger, the Result's relevant scope fields, and the old preliminary review's `REVIEW.md` member. Their scope is all finite zero-dimensional ideal modifications on the one fixed diagonal, with equality of the support and object-obstruction kernels. That result is not silently extended to curves or arbitrary line bundles.

The new draft proves only the necessary support condition for every rank-one torsion-free coherent sheaf on smooth integral support. This is a strict enlargement, using codimension-two restriction **injectivity** in place of the old codimension-three isomorphism. It leaves the converse open and only supplies a rank lower bound. Bounded targeted searches did not locate this extension in the frozen main's notes/artifacts. That is local deduplication evidence, not a global novelty assessment. The standard deformation, local-cohomology and GRR tools remain prior mathematical input.

## Independent proof checks

**1. The non-line-bundle locus has the required codimension in the support.** The relevant codimension is in the smooth integral variety `Z`, not in the ambient `X`. Local freeness of the coherent sheaf is open. At the generic point the rank is one; at every codimension-one point the local ring is a DVR and a finite torsion-free module of rank one is free. Hence the closed bad locus `S` has codimension at least two. On `U=Z\S`, the sheaf is a line bundle. This proof covers arbitrary rank-one torsion-free coherent sheaves, without requiring that the singular locus be a finite set or that a global trivialization of the line bundle exist.

**2. A perfect ambient derived lift really becomes a flat sheaf.** The stated derived special-fibre condition is stronger than equality in K-theory. Since the ambient deformation is flat over `R=C[ε]/ε²`, derived restriction is tensoring with `C` over `R`. Tensor the exact sequence `0→C→R→C→0` with the purported lift. Both end terms of the resulting triangle are the degree-zero special-fibre sheaf. The long exact sequence therefore puts the lift in degree zero and produces an extension `0→F→M→F→0`. The canonical composite of quotient and inclusion is multiplication by `ε`, so `ker ε=im ε`. This is precisely the flatness condition over the dual numbers. Thus the proof does not assume the flat-sheaf conclusion that it needs later, and does not confuse perfectness on singular `X_R` with local freeness there.

**3. Line-bundle transition functions do not obstruct the support argument.** On a sufficiently small ambient open intersecting `U`, trivialize the special-fibre line bundle and lift its generator. The map from the ambient structure sheaf to `M` is onto modulo `ε`; its cokernel vanishes by nilpotent Nakayama, so it is onto. For a cyclic module, the kernel of this presentation is its intrinsic annihilator. These ideals consequently agree on overlaps even when the lifted modules are not globally trivialized. The quotient algebra is locally isomorphic to `M` as an `R`-module, so is `R`-flat. Its reduction is the actual embedded structure sheaf of `U`, with the original ambient ideal. The annihilator therefore recovers a flat embedded first-order deformation of `U`.

The usual normal Čech obstruction restricts to zero on `U`: local regular-sequence support liftings differ by sections of `N_{Z/X}`, with their cocycle equal to the normal projection of the restricted ambient Kodaira–Spencer class. The use of an open, possibly nonproper `U` does not affect this first-order local-gluing argument.

**4. Codimension two gives exactly the injectivity used.** A locally free normal bundle over regular `Z` has depth at least two along any closed subset whose codimension is at least two. Equivalently, on each affine chart the support ideal has grade at least two on that free module. Hence its local-cohomology sheaves vanish in degrees zero and one. The local-to-global support spectral sequence gives `H¹_S(Z,N)=0`; localization then makes `H¹(Z,N)→H¹(U,N|_U)` injective. There is no claim that `H²_S` vanishes or that this restriction is surjective. Consequently vanishing of the restricted normal obstruction implies vanishing on all of `Z`. The empty bad locus is the trivial identity case. Curve-supported singularities on a threefold are covered because they have codimension two, not because they behave like finite punctures.

**5. The complete obstruction and rank implications have the correct direction.** I independently opened Huybrechts–Thomas `arXiv:0805.3527v2`, the theorem on page 2 and Corollary 3.4 on page 14. A perfect special-fibre object on a separated Noetherian scheme has a perfect lift precisely when the full truncated Atiyah–Kodaira–Spencer product vanishes, under the stated smooth-ambient square-zero hypotheses. Here smooth `X` makes `i_*E` perfect, and a projective first-order `X_R` embeds through `P^m_R` into the smooth complex ambient `P^m_C×A¹_C`. These hypotheses are retained. The tangent-space conclusions are used for the declared deformation directions to which those hypotheses apply; the polarized Weil tangent space in the application meets them.

It follows that `ker Ω_F ⊆ ker δ_Z`, not equality. Rank-nullity on a finite-dimensional source yields `rank Ω_F ≥ rank δ_Z`. If `Ω_F(t)=Ω_F(t')`, their difference is in `ker Ω_F`, hence in `ker δ_Z`; therefore `Ω_F(t)↦δ_Z(t)` is a well-defined surjection between the two images. The draft correctly reverses the old finite-support image comparison and does not claim this new surjection is injective. It uses neither a Chern-character trace nor assumed semiregularity injectivity in place of the complete object obstruction.

**6. The number six and the uniform obstructed direction are inherited correctly.** In the fixed old carrier the weight is `D_0=diag(1,1,3)`, and the normal map is `B↦D_0⁻¹Bᵀ−B` on all nine entries of `B`. On paper, the `(12,21)` pair has rank one; each of the `(13,31)` and `(23,32)` pairs has matrix `[[-1,1],[1/3,-1]]` with determinant `2/3`; the `33` coefficient is `−2/3`; the `11,22` coefficients vanish. The total rank is `1+2+2+1=6`, and the kernel is `span(E11,E22,E12+E21)`. In particular `E33` maps to a nonzero class. Applying the new kernel inclusion proves rank at least six and obstruction in `E33` for every member. It gives no universal exact rank or full Ext basis, and none is claimed. This is a hand check of the inherited formula, not a new numerical experiment or a new rank discovery.

**7. The leading Chern component is unchanged.** For the regular codimension-three closed embedding, GRR gives `ch(j_*E)=j_*(ch(E) td(N)⁻¹)` in rational cohomology. The internal codimension-zero component is the generic rank, one; all other terms push to codimension greater than three. Thus `ch₃(j_*E)=[Z]`, irrespective of line-bundle twisting or lower-dimensional singularities. The previously established nonzero exceptional projection belongs to that same fixed diagonal cycle and is legitimately reused. The argument does not require the whole Chern character to remain the old finite-modification expression. The stated `L⊗I_C` examples are torsion-free rank one since `I_C⊂O_Z` on integral `Z`, with generic rank one for `dim C≤1` on this threefold.

## Primary sources, execution, and disposition

In addition to the actual HT read, I opened Stacks tags `0AVZ`, `0G71`, and `0A6T` to verify the ideal-depth/local-cohomology and localization interfaces. Their locators and exact used statements are recorded in `PRIMARY_SOURCE_CHECKS.json`. No external full text is included in the publication material. There was no scientific program run for this review: only source fetching/reading, file hashes, and written reasoning. The previous R004 finite-module rerun is a separate review and is not evidence for this geometric theorem.

No mathematical must-fix was found. The paper and extracted necessary-condition filter pass at their explicit hypotheses. A nonzero support obstruction must produce `NO_PERFECT_LIFT`; a zero one must remain `NOT_DECIDED_BY_THIS_FILTER`. The new result does not supply a positive H0P object or H0R premise, a converse, exact rank six for every new member, a higher-order lift, very-general transport, or an unrestricted no-go for mixed derived objects. It leaves the mother objective open. Historical formal status and this local scientific PASS are distinct.

Researcher-ID: EM-C34-D16900 / TASK_RESEARCH  
EM-Source-Status: Read=Verified snapshot reused (`39556bf5207aa5ba559a27ec591c1bc1bf43b457`) and frozen Hodge inputs; Write=⚠ Not written — Source publication pending; local review artifacts preserved. Identity registration remains pending.
