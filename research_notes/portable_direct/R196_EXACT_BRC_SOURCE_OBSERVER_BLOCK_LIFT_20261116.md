# R196 — An exact source-observer lift for native BRC affine histograms

Date: 2026-11-16 (Asia/Shanghai). Status: **AUTHOR_PROVED / EXACT_REFERENCE_CHECKED / NATIVE_PACKAGE_RUN_PENDING / NOT_REVIEWED**.
Frozen scientific input: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Own existing researcher: `EM-DIRECT-403676`, session `MCP-7c25bcbe05b441809002779d7cf3fca8`, activity `RA-AECC608A4630A932AE51F0F3`. No formal Task CLAIM is inferred.

## Source and objective

This is a continuation of R195's field-uniform, minimum-dimension source-order affine representation. The **exact native transport source** `src/enterprise_math/brc_transport.py`, Git blob `be1debe367263931bd5e93fd750be3ed54624fe1`, was read at both the frozen scientific pin and current main and found unchanged. The implementation's `Affine.then` computes later-after-earlier composition; `EffectHistogram.from_terms` coalesces by the **joint key (positive Fraction weight, Affine action)**, retaining a positive integral multiplicity. `alternatives` adds multiplicities and `then` multiplies weights, actions and multiplicities. These are the actual interface laws, not just method names.

The mathematical objective is to retain a selected-source last-occurrence observation *jointly with* each physical affine effect, and to identify exactly when native EffectHistogram's coalescence loses that observer.

Retain the wider P000/native-X6 raw ordered paths, branch identities, signed information and provenance in an independent richer carrier whenever a future operation needs them; the present result concerns the explicitly selected-source quotient and positive rational affine-effect interface only.

## Objects

For fixed k, let `S_k` consist of repetition-free words in k selected source symbols, including the empty word. The chronological product is
[
u\star v=(u\setminus\mathrm{supp}(v))v.
]
There are `N_k = sum_{r=0}^k k!/(k-r)!` possible states. Let `Aff_n(Q)` be the semigroup of all total rational affine endomorphisms on Q^n, including noninvertible resets. Define a finite tagged histogram
[
H=\sum_{(w,A,s)}c_{w,A,s}[w,A,s],\quad
w\in Q_{>0},\ c\in\mathbb N_{>0},\ A\in\mathrm{Aff}_n(Q),\ s\in S_k.
]
Canonical aggregation merges only identical triples. Alternatives sum coefficients. Chronological serial composition extends
[
[w,A,s]\cdot[v,B,t]=[wv,B\circ A,s\star t]
]
bilinearly, with integer multiplicities multiplied on each cross pair. This is an associative semiring-like positive histogram algebra with an empty additive packet and a unit packet, even when affine maps are singular.

The native forgetful map `P(H)` groups tagged terms by `(w,A)` and sums their multiplicities.

## R196A — Exact loss criterion and two counterexamples

**The native forgetful map is a homomorphism for alternatives and serial composition**, but a general source observer does not descend along it.

To prove the first assertion, the native product and tagged product use the same `wv`, `B∘A` and `c d`. Summing over source labels before or after each finite cross-product gives identical coefficients of each `(wv,B∘A)` by distributivity. Alternatives is immediate.

A necessary and sufficient condition for a readout `q(w,A,s)` on **individual tagged atoms** to factor through the native atom key on a declared domain D is fiber constancy: whenever `(w,A,s)` and `(w,A,t)` both belong to D, their q-values agree. The condition must hold also after every allowed future operation if continuation-safe descent is claimed. In particular, for the full domain of all source words, the native identity affine map `I` and equal weight 1 give two different atoms `[1,I,a]`, `[1,I,b]` (k≥2) with **identical native histograms** and different source-order readouts. This is an exact obstruction, not an implementation error.

More strongly, marginal source and physical histograms together are insufficient for joint observations. Let `A(x)=x` and `B(x)=x+1` on Q, and distinct source labels `a,b` with equal unit weights:
[
H_1=[1,A,a]+[1,B,b],\quad H_2=[1,A,b]+[1,B,a].
]
Both have the same native physical histogram `[1,A]+[1,B]` and the same source marginal `[a]+[b]`. Evaluating the physical action at `x=0` jointly with the source yields respectively `(0,a),(1,b)` versus `(0,b),(1,a)`. Therefore the correlation itself is indispensable for that declared joint observer.

## R196B — A faithful native Affine block lift

For each `U` of size one or two among the k sources use one reset feature, giving
[
d(k)=k+\binom{k}{2}.
]
For a word s, define the affine action `R_s` on Q^d: on feature U it is the identity if no U source occurred in s, otherwise the constant 0 for the last U symbol equal to U's first member, or constant 1 for the second member. For singletons, a seen source resets its feature to 0. These are 0/1 rational matrices and translations. R195 proves `s -> R_s` is a faithful representation of S_k and `R_{s\star t}=R_t\circ R_s`. An all-ones initial vector lets singleton flags recover support and pair flags recover all pairwise recency comparisons.

For any physical affine action A on Q^n define
[
J(A,s)=A\oplus R_s \in \mathrm{Aff}_{n+d}(Q).
]
This is a **direct sum of affine actions**, i.e. block diagonal linear parts and concatenated offsets, not an identification of the project’s six native spatial axes with d auxiliary source features. Define a canonical packet map
[
\Phi(H)=\sum_{(w,A,s)}c_{w,A,s}[w,J(A,s)]
]
using precisely the native `EffectHistogram.from_terms(n+d, ...)` coalescence. Then:
[
\boxed{\Phi(H+K)=\Phi(H)\operatorname{alternatives}\Phi(K),\quad
\Phi(H\cdot K)=\Phi(H)\operatorname{then}\Phi(K).}
]
Moreover `Phi` is injective on tagged histograms. In fact, the upper-left physical block recovers A, and the source block recovers s because `R_s` is faithful. The unit packet maps to the unit packet and the empty packet maps to empty. Source order and native physical action remain *jointly* attached to the same positive weight/multiplicity.

**Proof.** Block multiplication gives `J(B,t)∘J(A,s)=(B∘A)⊕(R_t∘R_s)=J(B∘A,s⋆t)`. Thus products of individual positive terms agree. Distributivity and exact integer coefficient addition prove the histogram identities. If two image terms have the same `(w,J(A,s))`, equality of physical blocks gives A=A' and faithfulness of R gives s=s'; hence native coalescence merges exactly the desired tagged terms. The same inverse applies to every packet in the image. QED.

**Input validation:** Only the canonical image is decoded. An arbitrary mixed-block `Aff_{n+d}` map does not satisfy the stated inverse; check off-diagonal zero blocks and the exact reset-block signature on import.

## R196C — Scope-qualified resource bound

Within **block-independent rational affine source representations** faithful as transformations of S_k, the additional dimension d(k) is minimal by R195. For an existing physical dimension n, the native module stores each `Affine.a` as a dense square rational matrix and `Affine.b` as a rational vector. The exact *added number of rational slots per stored affine term* from direct block lift is
[
((n+d)^2+n+d)-(n^2+n)=\boxed{2nd+d^2+d}.
]
For fixed n this is Theta(k^4) dense rational slots because d=Theta(k^2). The code's generic `mm` uses cubic dense scalar operations for composing matrices of dimension n+d. These are costs of this **specific native dense representation**; zero-aware block algorithms, a typed tagged dictionary or the optimal rank codec can have different space/time behavior.

Under a typed source tag with a rank-code for S_k the payload requires `B_k=ceil(log2 N_k)` bits per source label, in addition to the physical action and exact weight/count. This is the information-theoretic optimum for an unrestricted fixed-size source identifier; it is not a bit-cost claim for building or composing the rank-code. For k=6, the source payload is 11 bits versus d=21 reset-bit coordinates, while native dense lifting adds `2n*21+21^2+21=42n+462` rational slots per distinct term. No end-to-end BRC speedup is claimed without conversion, arithmetic, storage and query measurements.

## Executed verification and evidence boundary

An independently coded Fraction-exact reference harness was executed locally (file `R196_brc_selected_source_lift_check.py`, companion `R196_verification.json`):
- Exhaustive source states k=1..5: **414** states; all 414 distinct reset orbits recover exactly.
- Every one-source append at k=1..5: **1,950** exact affine identities.
- Every ordered state product at k=1..4: **4,510** exact affine identities.
- Exact positive rational/multiplicity histogram alternatives and serial composition and physical projection, including rational weights 1/2,3/2,2/3 and multiplicities 1,2,3.
- The single-atom information-loss witness and two-by-two correlation counterexample.
- Reconstruction of canonical lifted packet keys and anti-cross-block input guard.

The harness reports its backend; this execution was `exact_reference_mirror`, **not an installed `enterprise_math.brc_transport` run**. The accompanying test executable has a `--native` mode that imports the real package, failing if unavailable; the reference mode follows the read native API contract. Full-source native module and frozen-pin blob equality were verified through the connected GitHub reader. The unrestricted mathematical claims are established by the symbolic proofs above; finite tests are supplementary, with independent review outstanding.

## Continuing problem

Run `python research_notes/portable_direct/R196_brc_selected_source_lift_check.py --native` from an environment with `enterprise_math` installed, compare JSON across backends, and measure construction, composition and serialization for native dense blocks, a tagged/rank-coded carrier, and a sparse structured block implementation over varying n,k, number of terms and rational bit length. Retain the full X6 path/provenance carrier whenever its declared future observers demand it. This research branch does not create a Task CLAIM, formal Result, Review, or P000 amendment.
