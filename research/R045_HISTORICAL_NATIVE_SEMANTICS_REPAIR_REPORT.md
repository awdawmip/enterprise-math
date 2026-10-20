# R045 — Historical Native-Semantics Retype and R038 N0 Repair

Status: `DONE / RETURNED / SEMANTIC_CHECKPOINT / NOT CANONICAL`

Researcher-ID: `EM-R045-812A`  
Task: `RS-R045-HISTORICAL-NATIVE-SEMANTICS-RETYPE-R038-N0-REPAIR`  
Task source: `d164ffea25203ff61d6901cf91be5583c93bcb9e`  
Frozen R044 router: `0af3c999874e0768a88f34f66c5c618900a036e4`  
Active Native-Semantics Gate V2: `a70c56e5c43772903a74d258ab237825c6045a8c`  
CI: `CI_NOT_REQUIRED_FOR_RESEARCH`

## 1. Return verdict

`R045_HISTORICAL_SEMANTIC_RETYPE_COMPLETE / CONDITIONAL_MATH_CONSERVED / R038_C05_N0_REPAIRED_OR_OPEN / R038_C06_NATIVE_PI_SCOPE_RESOLVED_OR_OPEN / DOWNSTREAM_OVERCLAIMS_ISOLATED / R043_REVIEW_STILL_SEPARATE / NOT_CANONICAL`

The frozen historical ledger contains **44 claims**: the complete R033/R034/R037/R038/R039/R041 impact surface plus `R043-TB03`, which the R044 generation spec explicitly routes through R045. Exactly **42 claims** are no-recompute preservation rows. Only `R038-C05` and `R038-C06` receive theorem-level repair.

No third theorem-level historical repair target was found.

## 2. Gate V2 invariant used

Every theorem-critical dependency is typed through the full transitive DAG. Native promotion is accepted only when the construction is from the declared N0 base, choice-independent, invariant/equivariant under the relevant N0 relabelings, and certified at the same semantic strength.

`SCALAR < QUOTIENT < RELATION < OBJECT < PRIMITIVE`.

In particular, scalar invariance does not promote a root, metric, full object or primitive.

## 3. Historical ledger / no-recompute freeze

Impact counts on the 44-row R045 scope:

- `KEEP_NATIVE`: 3
- `KEEP_BUT_RETYPE_CONDITIONAL`: 20
- `KEEP_AS_READOUT_ONLY`: 16
- `RETRACT_NATIVE_INTERPRETATION`: 3
- `RECOMPUTE_UNDER_N0`: 1
- `UNRESOLVED_NEEDS_NEW_TASK`: 1

The no-recompute certificate preserves R033 metric/readout formulas, R034 propagation mathematics, R037 replication, R039 surface/future mathematics and R041 horizon-carrier mathematics at their correct N1/N2/N3 layers. Retyping is not theorem revocation.

## 4. R038-C05 repair

Bare metric-free N0 is formalized as a pure relational language over the declared cell/contact/stacking/occupancy substrate **without a scalar sort or scalar-producing bridge**.

Two metatheorems are proved:

1. `BARE_N0_NO_SCALAR_TERM`: the language has no well-formed scalar-valued term, hence “N0 scalar is transcendental/equal to pi” is not an internal proposition.
2. `CONSERVATIVE_SCALAR_EXPANSION_UNDERDETERMINATION`: if an unconstrained scalar is later appended with no bridge axiom, the same N0 reduct admits algebraic or transcendental interpretations, so N0 alone cannot determine its arithmetic type.

Therefore:

`R038_C05_REPAIRED = ILL_TYPED_WITHOUT_ADDITIONAL_OBSERVABLE_LANGUAGE`.

The rooted FCC/HCP graph-zeta theorem is preserved as N1/N2 conditional mathematics; it has no metric-free N0 consequence.

## 5. R038-C06 repair

A native-pi candidate cannot be discussed until its output type/construction and its **pi role** are declared.

Bare N0 disposition:

- `EXISTENCE = NOT_WELL_TYPED_BARE_N0`
- `UNIQUENESS = NOT_WELL_TYPED_BARE_N0`
- `ROLE = ADDITIONAL_ROLE_LANGUAGE_REQUIRED`
- `NONEXISTENCE = NOT_PROVED`

Strongest legal conclusion:

`NATIVE_PI_NOT_WELL_TYPED_AT_N0`.

The R038 readout family still proves `pi_eff` nonuniqueness **inside that N2/N3 family**. It does not prove metric-free N0 nonexistence.

## 6. R037 evidence repair

No numerical/formula matrix was rerun. The new semantic evidence dimension is:

- `NUMERIC_OR_FORMULA_REPRODUCED`
- `SEMANTIC_TYPING_REPRODUCED`
- `ONTOLOGY_ADMISSIBILITY_NOT_IMPLIED_BY_REPLICATION`

Thus R037 remains strong independent evidence for the conditional R033/R034 mathematics and is not an ontology-promotion certificate.

## 7. Downstream correction

The affected R038 report, hypothesis dispositions, graph-zeta addendum, marked-axis witness, point-group witness and README require **retype/repair of native wording**, not mathematical recomputation. R039 and R041 have no frozen C05/C06 theorem dependency and remain preserved.

R044 itself already carries the correct semantic correction and is kept.

## 8. Mandatory controls

All eight unsafe controls are rejected, including:

- graph-definability does not make shortest path a declared N0 primitive;
- scalar automorphism invariance does not promote a full object;
- multiple readouts do not imply N0 scalar nonexistence;
- failure to find a scalar does not prove nonexistence;
- prior-art/classical convention does not import a primitive;
- infinity does not erase hidden root/order/measure/metric typing;
- replication PASS is not ontology PASS;
- semantic retyping is not theorem withdrawal.

Positive controls pass: a task that **explicitly declares** metric or continuum structure in its N0 base may use that structure natively under NSA-12.

## 9. New mother question, kept separate from R043

The remaining N0 frontier is to first declare a parameter-free, choice-free, relabeling/isomorphism-invariant scalar/object observable language over the metric-free relational substrate, and only then classify existence, arithmetic type and possible pi-role.

This is a proposed follow-up scope, not a new taskbook and not part of R043.

## 10. Required artifacts

- `research/r045_generated/R045_HISTORICAL_TYPED_CLAIM_LEDGER.json`
- `research/r045_generated/R045_NO_RECOMPUTE_PRESERVATION_LEDGER.json`
- `research/r045_generated/R045_R038_C05_N0_REPAIR.md`
- `research/r045_generated/R045_R038_C06_NATIVE_PI_DISPOSITION.md`
- `research/r045_generated/R045_R037_SEMANTIC_EVIDENCE_DELTA.json`
- `research/r045_generated/R045_DOWNSTREAM_IMPACT_MATRIX.json`
- `research/r045_generated/R045_THEOREM_COUNTEREXAMPLE_OPEN_LEDGER.json`
