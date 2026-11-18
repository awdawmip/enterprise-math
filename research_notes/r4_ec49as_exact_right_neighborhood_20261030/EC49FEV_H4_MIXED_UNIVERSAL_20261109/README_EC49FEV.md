# EC49FEV — Universal pooled-key lower bounds for all H4-mixed 23-word branches

Date: 2026-11-09 Asia/Shanghai. Research mode: AUTHOR-side exact finite certificate; awaiting independent Driver review. Frozen scientific input: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Historical prior: EC49FEU's signature-feasibility census at immutable Git commit `a17d237f8d42b86630e90cf41f62f878830c943a`. Model is exactly the original native signed-six-axis operation grammar, nine-state observation DFA and positive *full* forward BRC keys. P000 and ACTIVE worldview remain fixed.

## Exact result

Consider the original 23-word type-B construction with one mixed triple at H4 requiring signatures {1,8,16}, with H2 low quartet {1,2,4,8}, H3 high pair {16,32}, and four later high-bearing horizons S of H4..H9 (including H4 and H9), while the other late horizons use low quartets. All systems use at most five positive complete BRC keys and original signed-six-axis words with common native endpoint (+2,0,0,0,0,0). A native edge is an **ordered, signed microstep prefix**, and cost is the cardinality of the union of those nonempty prefixes across 23 paths.

**Theorem (EC49FEV, finite exact):** every legal system in this H4-mixed type-B family satisfies **C_native ≥ 101**. Six stronger per-branch bounds and original signature-feasible counts are:

| S (late high-bearing horizons) | original feasible full-key configurations | native edge lower bound |
| --- | ---: | ---: |
| 4569 | 864 | 115 |
| 4579 | 2,304 | 101 |
| 4589 | 1,920 | 108 |
| 4679 | 1,408 | 103 |
| 4689 | 1,536 | 105 |
| 4789 | 768 | 109 |
| **All H4-mixed type-B** | **8,800** | **≥101** |

The remaining four-element late-high sets excluding H9 have no signature-feasible original full-key configurations, as confirmed in EC49FEU and by the H9 high-bearing lemma. Hence all H4-mixed type-B options are included. The original BRC involution provides the corresponding C-type mirror bounds, under the exact established operation-word/prefix isomorphism; no new treatment of H5–H8 mixed placements is claimed here.

## Proof and reproducible finite certificate

Each high-bearing horizon h requires a full key with x+y=h+1. H3 has the unique high-pair key (3,1,1). Define the **pooled eligible key superset** U(S) = {(3,1,1)} ∪ K4(16) ∪ ⋃_{h∈S\{4}} Kh(16,32), where Kh(A) is every nonnegative-count positive full BRC key at horizon h whose original observer can emit every signature in A. Every original five-key inventory for this branch is a subset of U(S). In particular, allowing all pooled keys to be freely reused across any horizon can only enlarge each group's allowable words; this is a deliberate relaxation of the original five-key constraint.

For each of the 23 required (h,signature) groups g, let W_g be the complete set of original-operation words over **any** pooled key in U(S) with the exact endpoint, horizon and signature; let P(w) be that word's set of nonempty **original signed-X6 microstep prefixes**. For each of six S, a finite exact integer certificate gives nonnegative weights T_{g,p}, group guarantees γ_g, and Q=1,000,000 satisfying:

1. For every native prefix p, Σ_g T_{g,p} ≤ Q.
2. For every original pooled candidate word w∈W_g, Σ_{p∈P(w)} T_{g,p} ≥ γ_g.
3. The exact integer sum Σ_g γ_g/Q equals respectively 115,101,108,103,105,109.

For an arbitrary legal selection w_g∈W_g, sum the 23 group inequalities, then swap prefix sums and apply per-prefix capacity: Σγ_g ≤ Σ_{p∈∪_g P(w_g)} Σ_g T_{g,p} ≤ Q·|∪_g P(w_g)|. Therefore C_native≥Σγ_g/Q, and all six cases are exact bounds. The inequality is even valid for a *relaxed* system with access to every pooled key.

`EC49FEV_UNIVERSAL_H4.py` regenerates the coefficients using SciPy/HiGHS only as a **certificate search tool**. `EC49FEV_VERIFY_UNIVERSAL.py` is a separate Python-standard-library **exact integer verifier**: it re-enumerates all original words and prefixes, reconstructs 23 groups, checks all per-prefix capacities and every word inequality, validates signed-six-axis endpoint, full positive BRC key, nine-state DFA and reported integer bound. SciPy and floating-point arithmetic are not needed for certificate verification. `EC49FEV_EXACT_VERIFICATION.jsonl` records independent PASS results for each of the six branches.

The six complete coefficient arrays are stored in `UNIVERSAL_H4_*.json` within the full archive; no certificates were omitted. The six pooled universes contain 351,482 candidate words and 2,027,458 indexed group/prefix pairs in total; 1,563,014 integer dual weights are nonzero. These figures count separate branches, not distinct cross-branch words.

## Validation commands

Unpack the evidence archive, then from its `EC49FEV_20261109` directory execute:

```sh
python3 EC49FEV_VERIFY_UNIVERSAL.py UNIVERSAL_H4_4569.json UNIVERSAL_H4_4579.json UNIVERSAL_H4_4589.json UNIVERSAL_H4_4679.json UNIVERSAL_H4_4689.json UNIVERSAL_H4_4789.json
```

This is the authoritative non-numerical check of the stored certificate. Optional recomputation with NumPy/SciPy is:

```sh
OPENBLAS_NUM_THREADS=1 python3 EC49FEV_UNIVERSAL_H4.py EC49FEU_STANDALONE_REPORT_INPUT.json .
```

## Scope and next research action

This advances the mother search for ≤5 full BRC keys and C_native≤93 by completely resolving the H4-mixed 23-word branch (8,800 signature-feasible B, and its C mirror) with a stronger ≥101 bound. The remaining late-mixed B horizons H5,H6,H7,H8 contain respectively 15,812,18,426,20,568,26,652 signature-feasible candidate inventories in the historical exact census. Apply the same **pooled eligible key** method to their positive branch families; any pooled dual that does not yet exceed 93 is a precise narrowed target for coupled optimization or a more powerful group-prefix certificate.

Identity, publication, admission and owner status are separate operational checks. The scientific result here is author-side exact finite verification, not independent Driver acceptance.
