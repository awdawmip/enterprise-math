# GEO6 Second-Wave Packing/Kakeya Prior-Art Exact-Set Reconciliation V3 — Research Return

Task: `RS-GEO6-SECONDWAVE-PACKING-KAKEYA-PRIOR-ART-SYNTHESIS`  
Publication: `TP2-B531F3BB4A597B7D3EAF`  
Researcher-ID: `EM-G6PA2R3-3C8F21`  
Claim: `chatgpt-g6pa2r3-20260831-0007-3c8f21`  
Execution record: `ER-70A802A96B698AB96C2E`  
Hard target: `GEO6_SECONDWAVE_PACKING_KAKEYA_PRIOR_ART_EXACT_SET_RECONCILED_AND_WRITER_CONFORMANT`

## Verdict

`AUDIT_COMPLETE / EXACT_SET_RECONCILED`

The exact historical Result set is preserved as

- `RR-830A587B1588DFB21AB1` (PR #937; 18 claim rows; 13 source records), and
- `RR-4DC6467AD05A1E3CA824` (PR #950; 14 claim rows; 12 source records).

Neither Result is selected by timestamp, neither claim matrix is discarded, and every source entry from both branches is retained in provenance. The two frozen branches agree on the operational boundary: finite Packing and fixed-independent-axis Kakeya continuations are classical/elementary once the declared model is fixed; four P000 semantic selectors remain unresolved; no mathematical successor is authorized from this audit alone.

## Exact-set reconciliation result

The two matrices differ mainly in **claim granularity**, not in the mathematical/control-plane boundary.

The unified matrix contains **21 canonical atomic claims** with the following primary classifications:

| Classification | Count |
| --- | ---: |
| `EXACT_DUPLICATE` | 4 |
| `STRICT_ANTECEDENT` | 11 |
| `ADJACENT_METHOD` | 3 |
| `NO_MATERIAL_MATCH` | 3 |
| **Total** | **21** |

The complete 32-row two-Result comparison and all 21 canonical atoms are frozen in:

`research_artifacts/GEO6_SECONDWAVE_PACKING_KAKEYA_PRIOR_ART_EXACT_SET_RECONCILIATION_V3/reconciliation_matrix_v3.json`

Every original row records its source references, formal hypothesis comparison, original classification, kill decision, canonical atom mapping, and reconciliation status.

## Reconciled differences

### 1. Carrier-S4 automorphism row

Branch A classifies its carrier-S4 invariance row as `STRICT_ANTECEDENT`; Branch B calls the corresponding row `EXACT_DUPLICATE`.

Resolution: the unified atom `U-P08` is `STRICT_ANTECEDENT`. The application to the declared carrier is exact, but graph-automorphism invariance holds for arbitrary graphs under strictly broader hypotheses. Thus the label difference is a scope convention, not a mathematical conflict. The continuation kill is identical.

### 2. Equality characterization versus exact nonconcurrent witness

Branch A combines the general equality criterion and a particular typed nonconcurrent `r=2` witness in one `STRICT_ANTECEDENT` row. Branch B splits them.

Resolution:

- `U-K05`: equality iff incidence is connected — `STRICT_ANTECEDENT`;
- `U-K06`: exact typed nonconcurrent support-7 witness — `ADJACENT_METHOD`.

Forest Euler counting decides the first statement but does not itself certify the exact project-carrier coordinate realization of the second. The witness is preserved as a regression guard, not promoted as a theorem frontier.

### 3. Dependent-direction circuit versus exact support-3 witness

Branch A packages the vector-matroid circuit fact and the explicit support-3 packet together as `STRICT_ANTECEDENT`; Branch B marks the combined row `ADJACENT_METHOD`.

Resolution:

- `U-K07`: dependence/circuit as the cycle threshold — `STRICT_ANTECEDENT`;
- `U-K08`: exact typed support-3 realization — `ADJACENT_METHOD`.

No source or witness is discarded.

### 4. Classical Kakeya relation

Branch A labels the Dvir/Ball comparison `ADJACENT_METHOD`; Branch B labels its Dvir comparison `NO_MATERIAL_MATCH`.

Resolution: `U-K09` is `ADJACENT_METHOD` **with an explicit no-exact-antecedent guard**. Classical finite-field Kakeya is genuine contextual prior art, but its direction quantifier, ambient algebra and objective do not match the fixed-six finite-path problem. This preserves both branch meanings. Search absence remains non-probative for novelty.

### 5. Row-set asymmetry

Branch B has a separate orbit-stabilizer row (`K01`) that Branch A did not isolate; Branch A has explicit selector rows (`PCK-10`, `PCK-11`, `KAK-07`) that Branch B carries only in its immutable Result residue.

Resolution: take the union and atomize. `U-K01` is preserved, and the three selector atoms are preserved with Branch B's Result-level residue as corroborating provenance.

There are **no substantive unresolved classification conflicts** after this atomic refinement.

## Unified classical boundary

The following finite/fixed-carrier statements are continuation-killed under their current hypotheses:

- declared finite non-overlap optimization -> conflict-graph independent sets;
- even coordinate torus structure, bipartiteness, `alpha(T_n)=n^6/2`, and the Hoffman `1/2` certificate;
- periodic quotient density along Følner sequences and boundary-only finite-window error;
- graph-homomorphism pullback/equal-fiber density preservation;
- declared graph-automorphism invariance;
- carrier-S4 orbit-stabilizer bookkeeping;
- independent-direction incidence forest;
- defect identity `D=6-c<=5`;
- `K_6(r)=6r-5` and the connected-incidence equality criterion;
- the vector-matroid circuit explanation for where incidence cycles may appear.

The exact typed nonconcurrent and support-3 coordinate packets remain useful only as regression/boundary witnesses.

## Surviving semantic selectors

The exact surviving selector set is:

1. `NONOVERLAP_SELECTOR`
2. `TRANSLATION_FOLNER_SELECTOR`
3. `PHYSICAL_REFINEMENT_SELECTOR`
4. `MIXED_DIRECTION_SELECTOR`

For every selector, `accepted_resolver_present=false`.

No currently accepted P000/Full-Cell datum has been identified that supplies the missing native semantics. Therefore:

`successor_authorized = false`

`NONOVERLAP_SELECTOR` remains the highest-leverage future selector because classical finite Packing machinery becomes immediately available once a canonical native exclusion relation is accepted. This is a prioritization only, **not** successor authority.

## Source reconciliation

The exact source manifest is frozen in:

`research_artifacts/GEO6_SECONDWAVE_PACKING_KAKEYA_PRIOR_ART_EXACT_SET_RECONCILIATION_V3/source_manifest_exact_set_v3.json`

It retains all **25 branch-local source records**:

- 13 from `RR-830A587B1588DFB21AB1` (11 external + 2 internal), and
- 12 external source records from `RR-4DC6467AD05A1E3CA824`.

Cross-branch alignment is recorded without deleting duplicates or choosing a preferred citation. Notable differences retained include König vs Hall for the matching bound, West/Li/Godsil-Royle for conflict-graph structure, cycle-rank vs Diestel forest references, Encyclopedia-of-Mathematics vs Oxley for matroid circuits, Branch-A-only Ball–Blokhuis–Domenzain context, and Branch-B-only orbit-stabilizer sourcing.

## Deterministic verification

Checker:

`research_checks/GEO6_SECONDWAVE_PACKING_KAKEYA_PRIOR_ART_EXACT_SET_RECONCILIATION_V3_CHECK_20260831.py`

It verifies, without network access:

- exact historical Result membership `('RR-830A587B1588DFB21AB1', 'RR-4DC6467AD05A1E3CA824')`;
- exact origin row sets (18 + 14 = 32 rows);
- exact branch source sets (13 + 12 = 25 provenance records);
- all source references resolve inside the frozen manifest/Result-level provenance;
- exact 21-atom unified set;
- classification totals `4 / 11 / 3 / 3`;
- all stated granularity/label reconciliations are present;
- no substantive conflict is silently suppressed;
- exact four-selector survivor set;
- `accepted_resolver_present=false` for every selector;
- `successor_authorized=false`;
- `NO_MATERIAL_MATCH` is not a novelty certificate.

## Control-plane recommendation

Send the writer-conformant V3 Result to Driver review. The parent GEO6 objective may consume this unified prior-art boundary instead of selecting one historical branch.

Do **not** publish a mathematical successor from this audit. A later successor must name an already accepted typed P000/Full-Cell datum capable of resolving at least one surviving selector.

## Novelty guard

`NO_MATERIAL_MATCH` and source-search absence are never novelty certificates. This task reconciles prior-art/control-plane evidence; it does not assert a new mathematical theorem or Foundation promotion.
