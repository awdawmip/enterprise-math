# EC49FCB — Exact rigidity for 1,305 two-early/two-late four-slot exchanges

Date: 2026-11-06. Frozen scientific pin: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
Status: author-side exact finite computer-assisted proof; independent Driver admission pending.
Parent: EC49FCA at ddddc1b86fd8a8541c366c17af15c9be36380004.
Frozen 158-edge word witness: EC49FBU at b3b43ef6abe2fd816d979792d18a67ee5d0aad50.
Frozen candidate and primitive-prefix generator: EC49FBY at 5b10f1c296cb8826d4b69f6fd83dba89d765df1c.

## Theorem and domain

Retain the twenty required H4-H9 observation-signature slots of the exact pinned positive-BRC nine-state model; H2/H3 use the four fixed root words. H4/H5 use positive cache key L=(4,2,1,0,0,0), H6-H9 use M=(7,3,2,0,0,0). Retain the full ordered native signed-six-axis primitive expansions and the nine-state observer.

Fix any four slots comprising exactly two of the ten early H4-H6 slots and exactly two of the ten late H7-H9 slots, subject to the late pair being one of H7+H7, H7+H9, H8+H8, H8+H9, H9+H9 (the mixed H7+H8 family is treated as the next frontier). For each slot, allow any path of the *same horizon*, exact complete BRC cache key and terminal observer signature. Keep the other twenty paths fixed.

For every one of these 1,305 slot sets, the minimum number of distinct native signed primitive-prefix edges is EXACTLY 158. This is a conditional finite restricted local optimum of the pinned witness.

## Finite proof and exhaustive certificate

For any fixed four-slot set I, let R be the union of nonempty native primitive prefixes of the twenty unchanged words, and B(w) those of the candidate word w. Put K=158-|R| and D(w)=B(w)\R. A strict improvement exists precisely if there are four signature-correct choices with |D(w1) union D(w2) union D(w3) union D(w4)|<K.

Discard each single residual with size >=K; discard any candidate pair union with size >=K; and likewise any triple union with size >=K. These are exact deductions from monotonicity of set union. Identical residual sets within a slot can be collapsed because their effect on this finite objective is identical. Enumerate all remaining fourth candidates, using exact arbitrary-precision integer bitsets for signed primitive-prefix identity. The supplied checker verifies that no strict improvement occurs in all 1,305 families. The original 158-edge word family remains admissible for every set I and attains equality. This proves the stated finite optimum.

The generator enumerates legal operation words from the frozen positive BRC multiplicity equations and nine-state DFA; it expands the signed-axis sequence before assigning prefix IDs. No quotient of native path, signs, ordering, multiplicity or observation signature is used. The reusable monotone pruning argument applies to any finite path-union model with the same fixed-slot semantics.

## Executed computation (five independently run phases)

| Two late windows | Slot families | Raw word quadruples | Exact surviving fourth-candidate unions |
|---|---:|---:|---:|
| H7+H7 | 270 | 38,316,240,000 | 1,049,676 |
| H7+H9 | 360 | 137,168,640,000 | 1,275,120 |
| H8+H8 | 270 | 604,399,320,000 | 59,660 |
| H8+H9 | 360 | 548,674,560,000 | 107,550 |
| H9+H9 | 45 | 45,722,880,000 | 3,876 |
| Total | **1,305** | **1,374,281,640,000** | **2,495,882** |

The five complete per-group local reports were generated and then audited for 1,305 distinct, complete slot sets, with every minimum=158. Their original SHA-256 digests and all exact aggregate counts are in SUMMARY_EC49FCB.json. The portable verifier independently regenerates each phase's per-group data and identical integer aggregates with standard-library Python. To limit peak work, run it separately with the phase arguments H7H7, H7H9, H8H8, H8H9 and H9H9; it imports the existing immutable EC49FBY generator from the sibling directory.

A second implementation independently constructs tuple-valued prefixes from the signed integer primitive steps (rather than alphabet-encoded integer bitsets) and passed fifteen declared representative four-slot groups, checking both the exact optimum and surviving fourth-evaluation count. Its inputs and checker are supplied here; this is a targeted 15-group crosscheck, while the primary complete check covers all 1,305 groups.

## Frontier and next discriminating question

Together with EC49FBZ's 210 early-only groups and EC49FCA's 1,200 three-early/one-late groups, 2,715 of all C(20,4)=4,845 four-slot families are now exactly certified. The remaining 2,130 families are: 720 two-early+H7/H8 pairs; 1,200 one-early/three-late; 210 all-late. The H7/H8 pairs contain computationally harder overlap configurations; improve trie-specific lower bounds or exact branch-and-bound rather than assert an unexecuted result. Continue to seek a 157-edge witness or a global exact lower bound, and compare different positive BRC key schedules toward the nine-window mother objective.

No change to P000, ACTIVE worldview, task ownership, formal Result/Review or mathematical admission is asserted.