# CBRC F0 Ablation and Countermodel Packet

Status: `PHASE_A_RAW_PACKET / REQUIRED_ABLATIONS`
Date: `2026-08-22`
Researcher-ID: `EM-CBRCF0-4E91C7`

## 0. Baseline classified structure

Baseline uses:

- typed Path-formal provenance;
- conservative signed group completion;
- reversible path-wise unit transport;
- branch relabeling/gauge transport;
- composition compatibility;
- finite refinement consistency;
- pre-collapse information preservation;
- positive final readout;
- exact cancellation tested on the minimal `(1,1)` same-terminal fiber.

Baseline primary verdict:

`F0_UNDERDETERMINED_BY_CURRENT_FOUNDATION`.

The ablations below remove one named requirement at a time.

## 1. Remove `PRECOLLAPSE_INFORMATION_PRESERVATION`

### Countermodel

Map multiplicity to parity at the terminal:

`1 -> 1`,
`2 -> 0`.

Then the two nonzero `(1,1)` paths can give a zero terminal coefficient without introducing a conservative signed carrier.

### What breaks

Old N multiplicity is not embedded: multiplicity `2` is identified with `0`. Path provenance can also be discarded before the final readout.

Therefore the universal/minimal **conservative** group-completion conclusion is no longer forced.

### Ablation verdict

`INFORMATION_PRESERVATION_LOAD_BEARING_FOR_CONSERVATIVE_MINIMALITY = true`.

## 2. Remove `BRANCH_RELABELING_EQUIVARIANCE`

### Countermodel

Order the two concrete paths by an arbitrary serialization and assign coefficients:

`first -> +1`,
`second -> -1`.

A different serialization swaps the assignment.

The same native support therefore receives a different enriched presentation solely because of a non-native list order/name choice.

### What breaks

No physical equivalence forces these assignments to agree. The curvature/gauge class can no longer be treated as independent of serialization.

### Ablation verdict

`RELABELING_EQUIVARIANCE_LOAD_BEARING_FOR_CHOICE_INDEPENDENCE = true`.

## 3. Remove `LOCAL_CONSERVATION`

### Countermodel

Keep the state update equal to the identity (hence reversible), but multiply the reported pre-collapse scalar by `2` after every local step.

Composition can still be made consistent by multiplying the scale factors along the path.

### What breaks

The scalar value can drift under an information-preserving update. The Q4 family becomes strictly larger because arbitrary positive multiplicative local rescalings are admitted.

### Ablation verdict

`LOCAL_CONSERVATION_LOAD_BEARING_FOR_READOUT_NORMALIZATION = true`.

## 4. Remove `REFINEMENT_CONSISTENCY`

### Countermodel

Use parity of the number of explicitly represented copies as the coefficient/readout.

One copy is nonzero; representing the same coarse occurrence as two refined copies gives zero.

### What breaks

Pure presentation refinement changes the physical result. Quotient carriers that collapse old multiplicities become admissible, and the naturality proof excluding nontrivial branch mixing no longer applies.

### Ablation verdict

`REFINEMENT_CONSISTENCY_LOAD_BEARING_FOR_PRESENTATION_INDEPENDENCE = true`.

## 5. Remove `NONTRIVIAL_MIXING`

### Countermodel / survival witness

Use the diagonal path-wise signed transport class with `kappa=-1` on the minimal diamond.

No branch vector is mixed with another. The two concrete paths remain independently retained, yet their final signed terminal aggregate is zero.

### What survives

- exact cancellation;
- reversibility before final aggregation;
- support preservation;
- branch relabeling/gauge classification;
- composition.

Therefore genuine branch mixing is **not** load-bearing for the minimal dark-fiber effect.

### Ablation verdict

`NONTRIVIAL_MIXING_NOT_LOAD_BEARING_FOR_EXACT_CANCELLATION = true`.

## 6. Remove `EXACT_CANCELLATION / DARK_FIBER_REQUIREMENT`

### Countermodel

Use the original whitelist tower unchanged:

`PATH_FORMAL_BRC -> N_BRC -> BOOLEAN_BRC`.

It already correctly represents:

- full path provenance;
- multiplicity;
- support.

### What breaks / disappears

No additive inverse is needed, no signed coefficient completion is forced, and no negative-curvature diamond condition is selected.

### Ablation verdict

`EXACT_CANCELLATION_LOAD_BEARING_FOR_SIGNED_EXTENSION = true`.

## 7. Pairwise conclusions

The minimal dependency structure is:

`EXACT_CANCELLATION + CONSERVATIVE_INFORMATION_PRESERVATION`
`=> additive inverse required`
`=> universal signed group completion`.

Then:

`BRANCH_RELABELING + PRESENTATION/GAUGE INDEPENDENCE`
`=> enriched path transport classified by gauge-invariant diamond data`.

Then:

`FULL_REFINEMENT_NATURALITY + MINIMAL_INTEGER_CARRIER`
`=> no genuine branch mixing beyond sign/permutation`.

Separately:

`Q4 operational axioms`
`!=> unique scalar readout`.

This separation is important: coefficient minimality, transport classification, branch mixing, and readout uniqueness are not one theorem and do not share the same load-bearing axioms.

## 8. Exact minimal countermodel table

| Ablation | Smallest witness | Result |
|---|---|---|
| no information preservation | two occurrences modulo 2 | cancels but destroys old multiplicity |
| no relabel equivariance | two serialized paths | arbitrary sign by list order |
| no local conservation | one reversible identity step | arbitrary scalar drift |
| no refinement consistency | one occurrence split into two | parity flips under refinement |
| no nontrivial mixing | `(1,1)` signed diamond | dark fiber still exists |
| no cancellation | original `(1,1)` N/Boolean tower | no signed extension needed |

## 9. Checker coverage

The deterministic checker contains an executable witness for every row above and reports mismatch count `0`.

Checker deterministic digest:

`362738cc8a1a0f87c291d897308c4476e385c3266240f1f8b598cda1c50194ca`

## 10. Ablation packet verdict

`MANDATORY_COUNTERFACTUAL_ABLATIONS_COMPLETE = true`
