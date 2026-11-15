# R193 — Rank-sandwich obstruction for faithful affine last-occurrence bands

Date: 2026-11-16 (Asia/Shanghai).
Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.
Frozen scientific input: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Parent frontier: R192, enterprise-math immutable commit `e29269e3a4326224d0b8ec0cd908f9083c8a1374`.
Scope: the auxiliary selected-source last-occurrence observer only; the P000 six native spatial axes, independent time, full source/branch/path/multiplicity and signed information remain in the rich carrier.

## Model and theorem

For k>=1, S_k is the set of repetition-free words (including the empty word) over k labeled sources. Its chronological product is u⋆v = (letters of u not in support(v), in their original order) followed by v. A faithful rational affine representation consists of affine transformations T_s on Q^d, with T_empty=identity, T_(u⋆v)=T_v∘T_u, and T_u≠T_v whenever u≠v. Let m(k) be the least such d. This is the unrestricted map-faithful dimension: **no linear query readouts are assumed**.

**R193 theorem.** m(1)=1, m(2)=3 (R192B), and for every k>=3,

[
oxed{m(k) ge m(k-1)+2,qquad m(k) ge 2k-1.}
]

Consequently, the unrestricted k=3 problem narrows to **5<=m(3)<=6**, with the upper bound 6 given by R183's reset representation. More generally,

[
oxed{2k-1 le m(k) le k(k+1)/2quad(kge2).}
]

The lower bound holds over any infinite field for which R192B's m(2)=3 proof applies.

## Proof

**Generic orbit lemma.** For any faithful affine action of the finite monoid S_k over an infinite field, choose x such that all points p_s=T_s(x) are pairwise distinct. For s≠t, the equality locus T_s(x)=T_t(x) is a proper affine subspace. A finite union of proper affine subspaces cannot cover the affine space. The affine hull of the orbit of any submonoid M⊆S_k is invariant under M; the restricted action is faithful because the orbit points at x distinguish its elements. Consequently that hull has dimension at least the minimum faithful affine dimension of M.

Write L_s for the linear part of T_s. Let d be the dimension of an arbitrary faithful S_k action.

**Lemma 1 — singleton rank (complement sandwich).** For any letter i, rank(L_i)>=m(k-1).

Because T_i is idempotent, its affine image H_i=T_i(Q^d) is an affine subspace of dimension rank(L_i). For every word s supported outside {i}, define B_s:H_i→H_i by B_s(y)=T_i(T_s(y)). The word identity

[
(istar sstar i)star tstar i=(sstar t)star i
]

for s,t supported outside {i} gives B_(s⋆t)=B_t∘B_s and B_empty=id on H_i (since T_i fixes H_i). Thus B is an affine action of S_(k-1). It is faithful: at y=T_i(x) from a generic orbit, B_s(y)=T_(s⋆i)(x); distinct s give distinct repetition-free words s⋆i and therefore distinct points. Hence dim H_i=rank(L_i)>=m(k-1).

**Lemma 2 — two-source annihilation.** For distinct i,j, rank(L_(i⋆j))<=d-3.

Restrict the generic orbit to the five-element two-source subband S_{i,j}. Its affine hull H_{ij} has dimension at least m(2)=3 by the orbit lemma. Every u∈S_{i,j} satisfies u⋆(i,j)=(i,j). Therefore T_(i⋆j) sends all five orbit points to the same p_(i,j), so its linear part annihilates the direction space of H_{ij}. Its kernel has dimension at least 3, establishing rank(L_(i⋆j))<=d-3.

**Rank obstruction and induction.** For distinct i,j, chronological composition gives L_(i⋆j)=L_j L_i. Sylvester's rank inequality and the two lemmas imply

[
2m(k-1)-d
 le operatorname{rank}(L_jL_i)
 le d-3.
]

Thus 2d>=2m(k-1)+3. Since dimensions are integers, d>=m(k-1)+2. Taking the minimum over faithful actions gives the first asserted bound. Starting from m(2)=3, induction yields m(k)>=3+2(k-2)=2k-1. R183 gives the quadratic upper bound. QED.

## Verification and evidence

The companion `R193_rank_sandwich_check.mjs` performs exact integer word checks for 2<=k<=7: the complement-sandwich word identities, injectivity of s↦s⋆i and the right-zero identity on each two-letter subband. These cover 93,500 sandwich identities, 16,063 embedded states and 280 two-letter right-zero checks. The two-source R183 numeric-query orbit minor has exact integer determinant -2, witnessing dimension 3 for that explicit upper-bound realization. The numerical checks validate finite instances of the word algebra; the all-k inequality rests on the rank proof above. Output is `R193_verification.json`.

The proof is for the specified rational affine map action of the selected-source last-occurrence quotient. It does not compress the richer X6/BRC original carrier absent the observer/future-operation preservation hypotheses. No native enterprise_math.brc_transport execution, physical residual attribution or independent proof review was performed.

## Next discriminating problem

Decide whether a faithful affine representation of S_3 on Q^5 exists. A construction with exact generator matrices satisfying all finite band relations and 16 distinct transformations would prove m(3)=5; an unrestricted five-dimensional obstruction would prove m(3)=6. Reuse the 5<=m(3)<=6 interval and rank-sandwich lemmas, not the already completed R183/R192 proofs. Independently test the source-only observer against native Affine/EffectHistogram while retaining original branch/path identities and exact positive rational weights.

Formal Source CLAIM/Result/Review and Activity checkpoint remain separate operational states from this independently saved GitHub research note.
