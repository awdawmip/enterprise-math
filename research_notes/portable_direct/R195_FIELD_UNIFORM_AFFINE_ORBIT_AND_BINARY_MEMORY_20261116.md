# R195 — Field-uniform minimal affine dimension and a single-orbit binary observer

Date: 2026-11-16 (Asia/Shanghai). Status: **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED**.
Frozen scientific input: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.

Immediate parent: [R194 exact rational affine minimum](https://github.com/awdawmip/enterprise-math/blob/ebaaa44a14f87f52b6d8ce5584e506d649bc3cd5/research_notes/portable_direct/R194_UNRESTRICTED_AFFINE_LAST_OCCURRENCE_MINIMUM_20261116.md). The upper-bound reset method originates in [R183](https://github.com/awdawmip/enterprise-math/blob/5557fb3748bbe9e831e2f35716607dacffc0c6d4/research_notes/portable_direct/R183_QUADRATIC_RESET_AFFINE_SOURCE_QUERY_20261115.md), and the optimally ranked nonlinear code in [R191](https://github.com/awdawmip/enterprise-math/blob/cce5ae839dcc7719c1e30f179a3181d74136ceee/research_notes/portable_direct/R191_DYADIC_RECENCY_LIFT_AND_OPTIMAL_STATE_CODEC_20261116.md).

## Model and exact new claims

Let k≥1, and let S_k be the finite set of all repetition-free words on {1,...,k}, including the empty word. Its chronological product u⋆v deletes from u all letters present in v, then appends v. An affine action over a field F assigns T_s(x)=L_s x+b_s on F^d, with T_empty=id and T_(u⋆v)=T_v∘T_u. Faithfulness means distinct words of S_k give distinct affine *maps*, not merely different coefficient presentations.

**Theorem R195A (all characteristics).** For every field F, finite or infinite, the least possible dimension of a faithful affine action of S_k on F^d is

d_min(F,k)=k+binom(k,2)=k(k+1)/2.

This extends R194's rational/infinite-field theorem to **every finite field**, including F_2. The load-bearing change is to replace R194's common generic evaluation point with the span of **all values of affine difference maps**, which works even where no generic point exists.

**Theorem R195B (one separating orbit).** Over every field F, there is a faithful action attaining this dimension and a single starting vector x_* whose orbit {T_s(x_*):s∈S_k} has exactly N_k=Σ_(r=0)^k k!/(k-r)! distinct points. Therefore a single-orbit faithful affine realization has the same exact minimum dimension. Over F_2 its orbit state consists of exactly d_min bits.

These theorems concern the selected-source last-occurrence quotient, not a quotient of the native X6 signed-path or full BRC branch/provenance carrier.

## Lemma 1: a triangular character flag over any field

For any finite-dimensional linear action L of S_k, the generators L_i admit a common upper-triangular basis. Every resulting diagonal character has the form chi_B(i)=0 for i∈B and 1 for i∉B, with B⊆{1,...,k}.

**Proof.** Work in any nonzero invariant subspace V. Pick a word w, including the empty word if necessary, for which L_w is nonzero on V and support(w) is inclusion-maximal among such words. The band identity w⋆i⋆w=i⋆w implies L_w L_i L_w=L_w L_i. Hence K=ker(L_w|V) is invariant under every L_i.

If i belongs to support(w), the word identity i⋆w=w gives L_w L_i=L_w. Thus L_i acts as 1 on the nonzero quotient V/K. If i is outside support(w), the larger-support word i⋆w has L_(i⋆w)=L_w L_i=0 by maximality; thus L_i acts as 0 on V/K. So all generators act by one common scalar character on V/K. Induct on K, then refine the invariant flag of the scalar quotient to one-dimensional steps. Since every generator is idempotent, the diagonal entries lie in {0,1}. No infinite-field or characteristic assumption was used. QED.

If W is invariant in V, its diagonal characters also occur in the multiset of diagonal characters of V: extend an invariant flag of W to V.

## Lemma 2: singleton and pair characters are forced without generic points

Let T be an arbitrary faithful affine action of S_k over any F. Fix A⊆{1,...,k}, with |A|=1 or |A|=2, and put R={1,...,k}\A. For every permutation r of R, introduce two words:

- If A={a}, let u_r=ar and v_r=r.
- If A={a,b}, let u_r=abr and v_r=bar.

For every x∈F^d, let D_r(x)=T_(u_r)(x)-T_(v_r)(x), and define

W_A=span_F{D_r(x): r a permutation of R, x∈F^d}.

The two words in each pair are distinct elements of S_k. Faithfulness of T implies their affine maps are different, so D_r(x)≠0 for at least one x, and W_A≠0. This uses **all** x rather than a common generic x.

If i∈A, appending i to u_r and v_r yields the same word. The affine translation cancels in a difference, giving L_i D_r(x)=0.

If c∈R, appending c to both words only moves c to the end of their common R-tail. Thus L_c D_r(x)=D_(r⋆c)(x). Therefore W_A is invariant under every generator, and L_i is zero on W_A for every i∈A.

Because r is a complete permutation of R, u_r⋆r=u_r and v_r⋆r=v_r. Consequently L_r D_r(x)=D_r(x). Thus L_r|W_A is a nonzero idempotent.

By Lemma 1, W_A has a common upper-triangular character flag. A nonzero idempotent cannot be strictly upper triangular (that would make it both nilpotent and idempotent, forcing zero), so at least one character has eigenvalue 1 for L_r. Since r contains every element of R, this character is 1 on each c∈R; since L_i|W_A=0 for i∈A, it is 0 on each i∈A. It is exactly chi_A.

These forced characters are pairwise different for the k singleton choices and binom(k,2) pair choices. Each occurs in the ambient linear representation, so d≥k+binom(k,2), over **every** field. QED.

## Lemma 3: exact attainment with zeros and ones

Index d=k+binom(k,2) coordinates by all singleton features {i} and unordered-pair features {a,b}, a<b. For every source generator i, define an affine reset action:

- On its singleton coordinate {i}, write constant 0.
- On each pair {a,b} containing i, write 0 when i=a and 1 when i=b.
- On every feature not containing i, apply the identity.

All coefficients are 0 or 1 and these rules work over any field. On each feature U, a complete history acts by identity if it contains no U symbol, or as the constant map reporting the last occurring member of U otherwise. This property composes chronologically, hence the action factors through S_k.

Initialize x_*=(1,...,1). After any history, singleton coordinate {i} equals 1 if i has not occurred, and 0 if it has. If both a and b have appeared, the coordinate {a,b} equals 0 when a is the later one and 1 when b is later. The singleton flags recover the exact support, and the pair comparisons recover its total last-occurrence order. Thus s↦T_s(x_*) is injective. In particular the transformations themselves are distinct. This realizes the lower bound from Lemma 2 and proves R195A–B. QED.

**BRC interpretation.** This bit-valued affine state is only a source-selection observer. Original native branch identity, positive exact weights and multiplicities, signed X6 path and unselected source labels must remain in a separate richer carrier whenever downstream ports inspect them. Equality of two observer states is not by itself equality of two native BRC effects.

## Exact binary memory consequence and cost boundary

The selected-source quotient has N_k=Σ_(r=0)^k k!/(k-r)!=⌊e k!⌋ elements. Any exact unrestricted deterministic state codec needs B_k=ceil(log2 N_k) bits, and R191 attains B_k with a nonlinear rank/unrank algorithm. In contrast, **every affine-transition one-orbit realization over F_2 needs d bits**, and the present reset construction attains d. Therefore its exact representation-class overhead is d−B_k bits:

| k | N_k | optimal nonlinear bits B_k | minimal binary affine orbit bits d | excess |
|---:|---:|---:|---:|---:|
| 1 | 2 | 1 | 1 | 0 |
| 2 | 5 | 3 | 3 | 0 |
| 3 | 16 | 4 | 6 | 2 |
| 4 | 65 | 7 | 10 | 3 |
| 5 | 326 | 9 | 15 | 6 |
| 6 | 1957 | 11 | 21 | 10 |
| 7 | 13700 | 14 | 28 | 14 |
| 8 | 109601 | 17 | 36 | 19 |

Using Stirling's formula, B_k=k log₂ k−k log₂ e+O(log k). Thus d−B_k=k²/2−k log₂ k+O(k)=Θ(k²).

In the explicit feature implementation, each source generator writes the singleton and k−1 pair features, exactly k bit positions. Materializing or inspecting all feature coordinates for a general two-action product costs O(k²) bit operations. The nonlinear rank-code update pays for decode, update and re-encode. End-to-end BRC cost also includes carrier construction, source indexing, branch/weight storage, multiplication, serialization, observation and output recovery; no general speedup claim follows from the representation count alone.

## Validation and continuing research

The executable `R195_field_uniform_affine_orbit_check.mjs` (dependency-free Node.js) and `R195_verification.json` record exhaustive checks of all **16,071** quotient states for k=1..7 (both action and single-orbit injectivity), **109,592** generator appends for k=1..7 and **110,786** ordered state products for k=1..5. Values were computed using exact binary semantics. These tests establish the finite enumerations; the all-field theorem is proven algebraically above. Original `enterprise_math.brc_transport` integration, independent mathematical review and Source activity checkpoint are pending.

Next: implement a BRC-adapter comparison of packed F_2 affine resets, optimal ranked S_k codes and the rich provenance carrier, with **complete** conversion/composition/query bit-cost accounting. Retain frozen scientific input `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. This was independent portable research; no new formal Task CLAIM, Result, Review or P000 modification is asserted.
