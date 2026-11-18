# EC49FEV — Exact exclusion of H4-mixed 23-path BRC systems by signed-prefix packing
Date: 2026-11-09 (Asia/Shanghai)
Status: AUTHOR FINITE EXACT PROOF / independently checked integer certificates / NOT FORMALLY ADMITTED.
Frozen scientific input: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
Earlier frozen-science source: EC49FEJ–EC49FEU, PR #1730; prior author commit a17d237f8d42b86630e90cf41f62f878830c943a. P000 and ACTIVE worldview unchanged.

## Exact statement
Preserve original ordered signed X6 operation words, the original six-operation grammar, nine-state observation automaton, native endpoint (+2,0,0,0,0,0), and at most five *complete positive forward BRC keys*.

The eight horizon observation groups are H2,H7,H8 = {1,2,4,8} each (four paths each); H3,H5,H6,H9 = {16,32} each (two paths each); H4 = mixed B {1,8,16} (three paths). Exactly 23 complete paths are required. Different signatures, including ones from the same horizon, may use different keys in the five-key inventory.

For a high-bearing horizon h, the necessary original complete-key equation is x+y=h+1. The five high-bearing horizons are 3,4,5,6,9; their distinct keys are (3,1,1), one of four H4 keys admitting 16, one of four H5 keys admitting {16,32}, one of six H6 keys admitting {16,32}, and one of sixteen H9 keys admitting {16,32}. This is an exhaustive 4×4×6×16=1,536 typed-inventory domain.

**Theorem:** Exactly 672 of the 1,536 configurations fail H7/H8 low-signature feasibility. Every one of the remaining **864** configurations has a finite, independently validated, exact integer certificate that every complete original ordered signed-X6 23-path system using that inventory has at least **94 distinct nonempty original signed prefixes**. Consequently no such system attains the mother target cost ≤93.

By the previously verified operation-and-key involution I=(c d)(f g), J(x,y,z)=(y+2z,x-2z,z), mapping mixed B={1,8,16} to mixed C={2,4,32} while preserving legal words and native prefix cost, the mirror branch has identical cardinalities and exclusion. Therefore 3,072 typed B/C configurations are classified: 1,344 signature-infeasible, 1,728 feasible with cost at least 94. Do not interpret typed B/C cases as pairwise disjoint untyped inventories.

## Elementary certificate lemma
H2/H3 early paths have exactly four admissible early variants; each has 42 distinct original signed microstep prefixes, and the union U of all four possibilities has 54 prefixes. Give all 54 U prefixes **free** after paying only the forced 42 early edges. This grants more possible early sharing than any actual early variant and is conservative.

For each of the **17** required original signature groups (h,s), h=4,...,9, let W_(h,s) be ALL original signed expanded operation words at that horizon/signature reachable with any of the five complete keys. Every legal system selects at least one word from each group. At depth d, select only groups whose every candidate word has length at least d; the possible ordered signed length-d prefix set for such a group is P_(h,s,d). If a chosen subset S_d of these groups has pairwise disjoint possible prefix sets, and each possible set is disjoint from the gratis early prefix set U at depth d, then every legal solution must pay at least |S_d| distinct nonfree length-d edges. Distinct depths cannot identify the same edge. Hence for ANY legal choice of words or early variant:

    C_native >= 42 + sum_{d>=1} |S_d|.

The exact full 1,536-case certificate records one such selected subset S_d for each depth of each signature-feasible inventory; for all 864 feasible cases, the recorded integer sum is at least 94. The packing search **stops as soon as ≥94 is reached**: the recorded values 94..105 are conservative, partial certificates, NOT exact minimum costs. There is no requirement to prove the selected subsets maximally large; a checker verifies actual pairwise disjointness and the lower-bound sum, so neither a floating solver nor an optimization oracle is trusted.

The independent checker re-enumerates the original word grammar, original DFA, original complete BRC keys and 1,536 configurations; recomputes each feasibility result; rebuilds four early variants and checks 42/54; verifies every selected group index, length-depth requirement, signed prefix set disjointness with other picked groups and U; independently sums selected counts and checks all 864 reach ≥94. All arithmetic exact. Verified result:

    {"status":"EXACT_PASS","cases_checked":1536,"signature_infeasible":672,"feasible_excluded_le93":864,"minimum_certified_bound":94}

Certified stopped-sum distribution:
    94:106; 95:166; 96:125; 97:124; 98:134; 99:113; 100:22; 101:35; 102:16; 103:18; 105:5.

## Evidence and reproduction
The local full evidence archive EC49FEV_complete_evidence.tar.xz contains 17 files including README, original word-model dependencies (EC49FEU_STANDALONE.py, EC49FEJ_SIEVE.py, EC49FEJ_DEPTH_FILTER2.py), 1,536-case full integer witness JSON (EC49FEV_PACKING_CERT.json), independent verifier VERIFY_EC49FEV_PACKINGS.py, actual output, original exact packing enumerator EC49FEV_PACKING.py, optional earlier exploratory solvers and SHA-256 manifest. Command, with the full original-model source files alongside: `python3 VERIFY_EC49FEV_PACKINGS.py`. The proof depends on the independently checkable subset certificate, not on the exploratory solvers. Original archive SHA256 cf70786ad9d7b1ffa8d84d73dc1a07960dda1e0acb24980228eb717f5544999b.

## Scope and next scientific unit
This is **one of six H4-mixed high-bearing placements**, specifically H3,H4,H5,H6,H9, and not all late-mixed 23-path systems. EC49FEU counted 8,800 feasible typed-B H4 configurations; 864 are now excluded at ≤93, so 7,936 H4 feasible configurations remain outside this proof. Of 90,258 feasible typed-B configurations in EC49FEU across H4-H8, 89,394 remain to classify on this proof's accounting (overlap with earlier unrelated results must be checked before combining). Prior 22-path 94-edge witness remains the best recorded mother-problem upper bound; no claim of achieving ≤93.

Next EC49FEW: extend the same original signed-prefix packing certificate to other H4 high-bearing placements; use exact grouped-prefix dual or complete joint native path integer program for survivors not excluded by this certificate. Preserve full keys, original signed prefixes and frozen science; distinguish author finite proof from Source Result/Driver admission.

GitHub branch submission is author-side evidence, not an authenticated task CLAIM, native Result, independent Driver review, or parent-objective closure.
