# Native Enterprise C3 prime allocation: presentation ablation

Status: `FREE_RESEARCH_EXACT_INVARIANCE / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-23`

Researcher-ID: `EM-FREE-NEPS-239A6D`

## 1. Common within-sector permutation

Fix shell r and its r side positions. Let `pi_r` be any permutation of `{0,...,r-1}`. Apply the same permutation in all three cyclic sector blocks:

`N_pi(r,t,sigma)=B_r+pi_r(t)+sigma*r`.

This is the broadest purely combinatorial within-shell reordering that preserves the same C3 correspondence between the three sectors.

For fixed r, as t runs over all side states, `pi_r(t)` also runs over all residues `0,...,r-1`. Therefore the unordered collection of folded C3 fibers is exactly unchanged:

`{{B_r+j, B_r+j+r, B_r+j+2r}: 0<=j<r}`.

## 2. Exact invariant consequences

Hence every quantity depending only on the unordered shell-fiber collection is invariant under arbitrary common C3-equivariant within-sector permutation. In particular:

- the statement that every fiber is a 3-term AP with gap r;
- the universal fully-prime gate `6|r`;
- whole-shell full-bright count `T(r)`;
- projective forbidden slopes for each numeric fiber;
- the shell local-factor enhancement when a prime divides r;
- the primorial shell resonance ladder.

These do not depend on choosing a visually convenient side traversal.

Cyclic choice of which sector block is named first only permutes `sigma` and likewise leaves the folded fiber collection unchanged.

## 3. What is not invariant under arbitrary permutation

The identification of a particular geometric address, such as the equal-coordinate sector midpoint, with a particular numeric offset j can change under an arbitrary `pi_r`.

Therefore the sharpened midpoint bouquet and its 210 gate require a stronger local-coordinate condition, such as the unit-step monotone side allocation used in the conditional-uniqueness note.

This gives a clean hierarchy:

`PRESENTATION-ROBUST CORE`

= shell C3 AP decomposition + 6 gate + T(r) resonance + projective sieve + primorial ladder;

`LOCAL-ORDER-DEPENDENT SHARPENING`

= geometric midpoint -> symmetric quadratic bouquet -> 210 gate -> four-color divisor activation spectrum.

## 4. Research consequence

The strongest native prime-distribution claim should therefore be based first on the whole-shell C3-fold invariants, not on a single visually bright ray.

The midpoint remains valuable because it is selected by additional natural local structure (equal coordinates, reflection symmetry, minimum complexity, maximal gate), but it is a refinement of the presentation-robust shell phenomenon rather than the sole evidence for it.
