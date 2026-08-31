# Native Enterprise 13-state prime-incidence loop: adjacent transition classification

Status: `FREE_RESEARCH_EXACT_TRANSITION_CLASSIFICATION / NEGATIVE_HOLONOMY_RESULT / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-23`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Parent: `NATIVE_ENTERPRISE_PRIME_INCIDENCE_LOOP_CODE_13_STATE_20260823.md`

## 1. Question

Does gluing two neighboring 13-state Cell loops create an additional transition invariant not already determined by local prime residue eligibility and shared-cell incidence?

Use the three positive nearest-center directions in one sector-local triangular chart:

- E: `(u,v)->(u+1,v)`;
- N: `(u,v)->(u,v+1)`;
- NE: `(u,v)->(u+1,v+1)`.

Condition on both center cells being prime and interior so both six-vertex loops are defined inside the same chart.

## 2. Exact local model

For each direction, enumerate only:

- sector slot `sigma in C3`;
- local coordinate residues sufficient to determine all involved cell labels mod 6;
- the requirement that both center labels are in `{1,5} mod 6`;
- every binary prime/composite assignment to the remaining residue-eligible neighboring cells;
- ineligible residues are forced composite for primes greater than 3.

Each loop signature is then computed as the six edge-ANDs of the prime-indicator word around its center.

This is a complete finite local enumeration. No actual prime positions are used to generate the theoretical transition graph.

## 3. Exact transition graph sizes

The complete allowed ordered loop-pair transition sets have sizes:

- E direction: `9`;
- N direction: `9`;
- NE direction: `25`.

So the naive 169 ordered pairs from a 13-state alphabet collapse very strongly under shared-cell incidence and mod-6 eligibility.

The E and N graphs are related by the sector-local triangular symmetry of the chosen coordinate presentation; the NE direction is combinatorially distinct because it is the diagonal nearest-neighbor family in the `(u,v)` chart.

## 4. Finite prime-data completeness check

Exact prime census through shell `r<=1000` was used only after freezing the theoretical transition sets.

Among adjacent pairs whose two center cells are prime:

- E: every one of the 9 theoretically allowed transitions occurs; no forbidden transition occurs;
- N: every one of the 9 theoretically allowed transitions occurs; no forbidden transition occurs;
- NE: every one of the 25 theoretically allowed transitions occurs; no forbidden transition occurs.

Observed prime-center pair counts were:

- E: 8654;
- N: 8688;
- NE: 17303.

Thus at this scale there is no missing/extra transition suggesting a second arithmetic selection rule beyond the exact local model.

## 5. Shared-coordinate-vertex equalities

Some transition constraints are visible directly from shared incidence vertices. For example, for an E-neighbor pair with loop bits `b` and `b'`:

`b_0 = b'_2`,

`b_5 = b'_3`,

because those two coordinate vertices are literally the same triple-cell incidence events viewed from the two adjacent center cells.

Analogous shared-vertex equalities hold in the N and NE directions.

The full 9/9/25 transition classification additionally uses the hidden mod-6 eligibility phase of the surrounding cells.

## 6. Verdict

Freeze:

`ADJACENT_LOOP_TRANSITION_RESTRICTION = EXACT`.

`PAIR_LEVEL_EXTRA_PRIME_HOLONOMY = NOT DETECTED`.

The restriction is fully reproduced by local congruence eligibility plus shared prime-indicator variables. Therefore it should not be promoted as an independent new arithmetic invariant.

This closes the first pair-holonomy route rather than forcing a novelty claim.

## 7. Research consequence

The strongest surviving native structures are now separated cleanly:

1. **prime-free**: triple-cell incidence -> discrete curvature `K=2/4`;
2. **one-vertex prime support**: six-state mod-6 incidence hexacode;
3. **one-cell gluing**: exact 13-state prime-incidence loop code;
4. **two-cell gluing**: no additional invariant beyond the local model.

The next useful step should therefore change scale or observable, not keep extending the same Boolean loop transition graph.
