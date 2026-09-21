# Native Filament — Post-audit Hyperbola/Joukowski External Prior-art and Duplication Audit Return

Task: `RS-NATIVE-FILAMENT-POSTAUDIT-HYPERBOLA-JOUKOWSKI-EXTERNAL-PRIOR-ART-AUDIT`  
Publication: `TP2-39ACFC69F85D8661CFBF`  
Claim: `CLM-NFHJPA-20260922-0658-1A7C9E`  
Researcher: `EM-NFHJPA-5B519F`  
Hard target: `NATIVE_FILAMENT_HJ_EXTERNAL_PRIOR_ART_DUPLICATION_BOUNDARY_CLASSIFIED`

## Disposition

`AUDIT_COMPLETE` for the taskbook hard target. The bounded external audit found **no `EXACT_DUPLICATE`** for any of the six frozen layers H1/H2/J1/J2/C1/C2 in the audited source set. This is not a novelty, priority, patentability, freedom-to-publish, or exhaustive-literature conclusion. It is only a duplication/antecedence classification against the sources and exact-query ledger frozen in `research_artifacts/NATIVE_FILAMENT_POSTAUDIT_HJ_PRIOR_ART_5B519F_20260922/source_matrix.json`.

The post-replication narrowing is preserved exactly: H1 remains off-diagonal/distinct-tangent unless a separate diagonal/degenerate extension is proved; H2 remains a general odd-prime-power quadratic-character statement rather than a prime-only Legendre-symbol statement; C2 retains only the numerical equality at 105 and does not acquire common provenance or a causal mechanism.

## Source-backed classification table

| Layer | Frozen target boundary | Classification | External antecedent / audited-source conclusion |
|---|---|---|---|
| H1 | Split-hyperbola tangent quotient; full-hyperbola language only after diagonal/degenerate cases are separately controlled. | `PARTIAL_ANTECEDENT` | Split multiplicative geometry is classical via algebraic tori / `G_m`; modern finite-field Dickson work also uses hyperbolic geometry/value-set decompositions. The audited sources do not state the exact tangent-concurrency quotient with the accepted off-diagonal restriction. |
| H2 | `|R/G|=[q+1+eta(BC)+eta(-BC)]/4` over odd prime-power fields. | `PARTIAL_ANTECEDENT` | Cauchy-Frobenius/Burnside orbit counting is classical, and quadratic-character counting over odd finite fields is standard in the adjacent literature. The audited set did not expose this exact project-specific specialization. |
| J1 | `lambda_s(a)=-s a-1/(2a)`; fibers from an involution; image size `[q+eta(c)]/2`, `c=(2s)^-1`, under the frozen odd-q/nondegeneracy hypotheses. | `PARTIAL_ANTECEDENT` | Dickson/Joukowski parameterization `u+a/u`, its involution, and finite-field Dickson value-set cardinalities are direct prior art. The exact normalization/domain/formula in the frozen J1 statement is a specialization not found verbatim in the audited set. |
| J2 | Extremal closure `q=2s-1 => q|25 => (q,s)=(5,3)` and `q=2s+1 => q|7 => (q,s)=(7,3)`. | `ADJACENT_METHOD` | Dickson finite-field value-set and extremal cardinality analysis is established prior method. The distinctive `q|25` / `q|7` arithmetic closure was not found in the audited set. |
| C1 | `q_b=s+2`; small-breaker `s=3,q_b=5,k*=9`; `M9=35`, `3M9=105`, terminal odd factor `53`. | `NO_MATERIAL_MATCH_IN_AUDITED_SET` | Exact-signature searches and the named finite-field/Dickson source set produced no material match for this full arithmetic closure. This is a bounded negative finding only. |
| C2 | For `s=3`, lane polynomials `6m^2±2m+1` and `6m^2+1`; equality at 105 is numerical only. | `NO_MATERIAL_MATCH_IN_AUDITED_SET` | No audited source matched the combined polynomial family plus the 105 closure. No common provenance, causal mechanism, or unified theorem is inferred. |

## Audited external sources and exact contribution boundaries

1. **Encyclopedia of Mathematics, “Algebraic torus.”** It defines split algebraic tori as products of multiplicative groups `G_m` over the ground field. This is an antecedent for the multiplicative/split geometry in H1, not for the project's tangent-concurrency quotient.  
   https://encyclopediaofmath.org/wiki/Algebraic_torus

2. **Columbia University GU4041 notes, “The Cauchy-Frobenius Lemma.”** Under a finite group action on a finite set, the orbit count equals the average fixed-point count. This is a direct antecedent to the Burnside mechanism in H2, not to the exact `eta(BC),eta(-BC)` specialization.  
   https://www.math.columbia.edu/~harris/website/content/2-courses1/8-mathematics-gu4041-spring-2020-alternative/cauchy-frobenius-burnside_theorem.pdf

3. **W. S. Chou, J. Gomez-Calderon, G. L. Mullen, “Value sets of Dickson polynomials over finite fields,” Journal of Number Theory 30(3) (1988), 334–344, DOI 10.1016/0022-314X(88)90006-6.** The article determines Dickson-polynomial value-set cardinalities over finite fields. This is direct antecedent material for J1 image counting, without the project's exact normalized `lambda_s` statement or the later arithmetic closure.  
   https://pure.psu.edu/en/publications/value-sets-of-dickson-polynomials-over-finite-fields/

4. **Encyclopedia of Mathematics, “Dickson polynomial.”** It states the classical functional identity `D_n(u+a/u,a)=u^n+a^n/u^n`, exposing the standard Joukowski/Dickson involutive parameterization. This is the strongest direct antecedent for the mechanism behind J1.  
   https://encyclopediaofmath.org/wiki/Dickson_polynomial

5. **T. Brazelton, J. Harrington, M. Litman, T. W. H. Wong, “Residue sums of Dickson polynomials over finite fields,” Journal of Number Theory 264 (2024), DOI 10.1016/j.jnt.2024.04.016.** The paper gives a complete characterization of Dickson value-set size in odd characteristic and explicitly separates hyperbolic, elliptic and parabolic regimes. It is a strong modern adjacent source for H1/J1/J2 methodology, but it does not state the frozen six-layer chain or terminal 105/53 closure.  
   https://doi.org/10.1016/j.jnt.2024.04.016

6. **O. Küçüksakallı, “Value sets of Lattès maps over finite fields,” Journal of Number Theory (2014), DOI 10.1016/j.jnt.2014.04.014.** It gives an alternative computation of Dickson value sets using a singular cubic curve and extends the method to Lattès maps. This is adjacent geometric/value-set method for H1/J1, not an exact duplicate.  
   https://hdl.handle.net/11511/35051

The exact-query ledger additionally tested the distinctive formulas/signatures `q+1+eta(BC)+eta(-BC)`, `q|25` together with `q|7`, the three `6m^2±2m+1, 6m^2+1` forms, `3M_9 / 105 / 53`, and `lambda_s(a)` finite-field wording. Those searches are recorded only as bounded search evidence; failure to surface a match is not promoted into a novelty claim.

## Project-specific recombination boundary after the audit

What remains project-specific **within this audited set** is the exact recombination of: the narrowed split-hyperbola tangent quotient; the particular sign-orbit specialization; the normalized Joukowski/Dickson involution count; the `q=2s±1` extremal closure forcing `s=3`; and the subsequent `M9=35 -> 105 -> 53` / lane-polynomial arithmetic closure. The constituent ideas `G_m`/split tori, Burnside orbit counting, quadratic-character finite-field methods, Joukowski/Dickson maps, involution/value-set counting, and Dickson extremal-value-set analysis are not project-originating claims and should not be presented as such.

## Validation and reproducibility

The machine-readable matrix is `research_artifacts/NATIVE_FILAMENT_POSTAUDIT_HJ_PRIOR_ART_5B519F_20260922/source_matrix.json`; the fail-closed validator is `validate_source_matrix.py`; and `validation_certificate.json` records the PASS classification set and source-matrix Git blob. The validator enforces the six exact layers, the four-value classification vocabulary, source-ID resolution, H1/H2/C2 narrowing guards, and the no-novelty/no-exhaustiveness boundary.

BRC status: `NOT_APPLICABLE` — this task is an external literature/provenance/duplication audit, not a compute-heavy research branch requiring BRC execution.

## Unresolved residue and Driver handoff

Unresolved residue is limited to the taskbook's intentional boundary: this audit is not exhaustive prior-art clearance, and no legal/patent novelty conclusion follows. The hard target itself is satisfied because every frozen layer has a source-backed classification with exact antecedent scope/conclusion boundaries and the required classical mechanisms are explicitly treated.

Recommended Driver action: review this frozen Result for acceptance of `NATIVE_FILAMENT_HJ_EXTERNAL_PRIOR_ART_DUPLICATION_BOUNDARY_CLASSIFIED`; preserve the no-novelty and H1/H2/C2 narrowing clauses in any downstream Working Truth or successor task.
