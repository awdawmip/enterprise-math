# PCF restricted-routes external prior-art / duplication audit — Gen2 current-publication return

Task: `RS-PCF-RESTRICTED-ROUTES-EXTERNAL-PRIOR-ART-DUPLICATION-AUDIT`
Publication: `TP2-8D3D94C1C621740A50AB`
Current researcher: `EM-PCF-D9D300`
Current claim: `MCP-773897ff5858aaf6d7e47dd7`
Execution record: `ER-60B8A1FF82C42D8B8723`
Disposition: `PCF5_PCF6_EXTERNAL_PRIOR_ART_AND_DUPLICATION_BOUNDARY_EXACTLY_CLASSIFIED / ZERO_MATH_DRIFT / FROZEN_RESULT_REQUESTED`

## Recovery and validation basis

This generation does not replay the predecessor mathematics. The authenticated continuation frontier marks the completed PCF5/PCF6 20-row classification as `VERIFIED_COMPLETE_DO_NOT_REPLAY`, with `classification_drift=NONE`. The immutable recovery checkpoint is `research_artifacts/PCF_RESTRICTED_ROUTES_EXTERNAL_PRIOR_ART_DUPLICATION_AUDIT_GEN2_B9ADD5/handoff_checkpoint.json` at commit `18810fea1c289a6462d0fd212cd099b836b5dc93`, git blob `b1abb23c89674c34d561c0770000f4b041d271d6`, sha256 `ee09110ad7f20bdd04d71576c26cd10883e3f6d7be1092ab46d66a759ced3aaa`.

The predecessor primary classification is `RR-2DD195694C6E38A05EAB` / PR #1376 / commit `7222676f5df49120dc82aba2eee6ae592d0e059d`, corroborated by `RR-6D9A31C4F2E708B59A16`. Its machine-readable comparison matrix is `research_artifacts/PCF_RESTRICTED_ROUTES_EXTERNAL_PRIOR_ART_DUPLICATION_AUDIT/comparison_matrix_20260908.json`. Current-publication execution preserves that matrix/provenance rather than recomputing it.

## Exact 20-row classification

| Row | Classification | Boundary consequence |
|---|---|---|
| P5-1 block product polynomial → multipoint evaluation → gcd | EXACT_ANTECEDENT | Pollard–Strassen/Strassen extraction skeleton is classical; project notation is not a new factoring mechanism. |
| P5-2 m by m^2 rectangular parameterization | STRICT_ANTECEDENT | Restricted specialization/reparameterization; not a factoring speedup. |
| P5-3 subproduct/remainder-tree multipoint evaluation | EXACT_ANTECEDENT | Standard fast multipoint evaluation. |
| P5-4 batch-gcd-adjacent product/remainder-tree arithmetic | STRICT_ANTECEDENT | Batching machinery is classical; same-modulus cell-gcd list is not literally many-moduli batch gcd. |
| P5-5 exact mixed-radix cells partition | PROJECT_SPECIFIC_TYPED_RESIDUE | Retain only as exact table-coordinate lemma; no novelty inference. |
| P5-6 prime visibility iff p≤m^3+m+1 | PROJECT_SPECIFIC_TYPED_RESIDUE | Exact table-interface boundary with two-case bounded-multiple proof; not a new factoring principle. |
| P5-7 fixed-kappa P^+(N)^2≤kappa N coverage with m^2=O_kappa(N^(1/3)) cells | PROJECT_SPECIFIC_TYPED_RESIDUE | Exact covered-family support theorem only; never advertise as factoring speedup. |
| P5-8 gcd=N block refinement by gcd descent | EXACT_ANTECEDENT | Classical Strassen/Pollard–Strassen refinement logic. |
| P5-9 N=2018 guard and full-layer Omega(N^(2/3)) visibility obstruction | PROJECT_SPECIFIC_TYPED_RESIDUE | Full-layer interface obstruction only; not an integer-factorization lower bound. |
| P6-1 R_H[X]/(fg) product decomposition | EXACT_ANTECEDENT | Standard ring-theoretic CRT. |
| P6-2 coefficient CRT / product-ring split for H=pq | EXACT_ANTECEDENT | Standard CRT hidden-factor product structure. |
| P6-3 nontrivial selector idempotent and gcd extraction | EXACT_ANTECEDENT | Standard CRT idempotents already carry factor-equivalent information. |
| P6-4 h_c=(1-c)f+c g gluing | STANDARD_METHOD_REPACKAGING | Standard complementary-idempotent gluing in a product ring. |
| P6-5 c=-tr(T), det(T)=1 and companion converse | STANDARD_METHOD_REPACKAGING | Standard 2x2 characteristic-polynomial/companion-matrix linear algebra. |
| P6-6 corrected Gaussian/Eisenstein oriented free-rank-2 realization iff nontrivial CRT idempotent | PROJECT_SPECIFIC_TYPED_RESIDUE | Exact grammar-specific equivalence survives; not a general H-dependent no-go theorem. |
| P6-7 ambient order 12 and root counts 4,8,16 | STANDARD_METHOD_REPACKAGING | Standard finite-field/cyclotomic arithmetic under CRT. |
| P6-8 det(P(T_H))=Res(F,P) mod H | EXACT_ANTECEDENT | Standard companion/multiplication-operator plus resultant/Sylvester determinant identity. |
| P6-9 finite fixed H-independent determinant probes cannot universally separate semiprimes | STANDARD_METHOD_REPACKAGING | Each fixed probe reduces to a fixed integer resultant; explicit zero/nonzero resultant split limits the claim to fixed H-independent probes. |
| P6-10 H=91, c=78 pressure witness | PROJECT_SPECIFIC_TYPED_RESIDUE | Validation witness only; no novelty authority. |
| P6-11 N_ONLY_NONTRIVIAL_IDEMPOTENT_OR_EQUIVALENT_SELECTOR_GENERATOR label | PROJECT_SPECIFIC_TYPED_RESIDUE | Project routing semantics only; idempotents themselves are standard. |

No row is `NO_MATERIAL_MATCH`. This is not a historical-novelty finding.

## Source anchors preserved from the verified matrix

- S1 Markus Hittmeir, *A babystep-giantstep method for faster deterministic integer factorization*, arXiv:1608.08766.
- S2 Markus Hittmeir, *Integer factorization as subset-sum problem*, Journal of Number Theory, DOI 10.1016/j.jnt.2023.02.010.
- S3 FLINT `nmod_poly` documentation: fast multipoint evaluation via subproduct trees.
- S4/S12 Bernstein FactHacks remainder/product-tree material: `https://facthacks.cr.yp.to/remainder.html`.
- S5 Stacks Project Tag 00DT, Chinese remainder theorem.
- S6 Stacks Project Tag 00EM, idempotents and product decompositions.
- S7 MathWorld, Characteristic Polynomial.
- S8 MathWorld, Companion Matrix.
- S9 Stacks Project Tag 09HY, finite fields / cyclic multiplicative group.
- S10 MathWorld, Resultant.
- S11 MathWorld, Sylvester Matrix.

## Surviving project-local boundary

PCF5 retains only: (i) the exact Perfect-Prime-Table mixed-radix cell embedding/partition; (ii) the visibility boundary `p≤m^3+m+1` with the two-case bounded-multiple proof; (iii) the fixed-public-kappa covered-family theorem `P^+(N)^2≤kappa N`; and (iv) the N=2018 guard plus full-layer-only interface obstruction.

PCF6 retains only: (i) the corrected Gaussian/Eisenstein oriented free-rank-2 typed selector equivalence within the frozen grammar; (ii) the fixed H-independent determinant-probe scope guard with explicit zero/nonzero resultant split; and (iii) the H=91 pressure witness plus N-only selector-generator routing boundary.

## Killed interpretations / scope guard

This Result does **not** claim a new factorization mechanism, factoring speedup, factoring lower bound, product-tree/batch-gcd novelty, CRT/idempotent novelty, trace/determinant novelty, resultant novelty, general H-dependent impossibility, or historical novelty from a project-specific typed residue. PCF5 remains fixed-kappa covered-family restricted support-compression only; PCF6 remains corrected free-rank-2 oriented mixed-realization obstruction only.

## Current-generation conclusion

The hard target is satisfied at the exact task scope by the verified source-backed 20-row boundary, with no classification drift in this current-publication rebind. The only remaining control action after this return is canonical Result-writer freeze, immutable readback, and independent Driver review. No new mathematical claim is introduced in this generation.
