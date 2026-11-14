# EC49FEN — Two additional 22-word BRC five-key families exclude native-prefix cost at most 93

**Date:** 2026-11-08. **Scientific pin:** `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. **Type:** author-side finite exact computation/proof; no Source-native Result or independent mathematical admission is claimed.

## Model and statement

Reuse the signed primitive native-X6 operators `a,c,d,e,f,g`, original complete positive BRC key `(x,y,z)`, native endpoint `(+2,0,0,0,0,0)`, nine-state observer, and native signed-step trie cost from the frozen EC49FEJ/EC49FEK code. Horizons are H2--H9. Exactly five horizons use two paths carrying `(16,32)`; the other three use four paths carrying `(1,2,4,8)`. The total is **22 distinct primitive operation words**; each horizon's rank-nine observer requirements are the unchanged frozen ones. Any of the globally at most five full BRC keys may be used within each horizon. Costs count distinct **ordered signed native-axis-step** prefixes, not operation symbols or endpoint coordinates.

Consider the following two newly classified families (numbers denote the two-path high-signature horizons):

* **F34789**: high H3,H4,H7,H8,H9; low H2,H5,H6.
* **F35679**: high H3,H5,H6,H7,H9; low H2,H4,H8.

**Finite exact result:** Every legal system in either family has `C_native >= 94`. In particular, neither family contains the mother-target system of at most five BRC keys and at most 93 native prefix edges.

## Complete finite inventory proof

Every high-signature operation word at horizon `h` requires `x+y=h+1` in the frozen grammar. Thus the five different high horizons use five different BRC keys. H3 has a unique key `(3,1,1)`; high-capable key families at H4,H5,H6,H7,H8,H9 have exact sizes `2,4,6,9,12,16` as re-enumerated by `EC49FEJ_SIEVE.py`. Each family here consequently has exactly `3456` possible full five-key inventories: `2*9*12*16` for F34789 and `4*6*9*16` for F35679.

For each key inventory, the program enumerates legal native words from the **original signed operation grammar and observer DFA**, and checks all four low-signature groups at each low horizon. This rejects 1,500 F34789 inventories (all missing at least one required H5 low signature); all 3,456 F35679 inventories pass the necessary quota test. For each quota-feasible inventory, all high and low signature groups are explicitly checked to be nonempty, so a lexicographic path choice gives an actual finite 22-word admissible system (not necessarily a minimum-cost one).

H2's four low-signature words are `ce,ec,de,ed`, and H3 has four legal choices of a pair covering `(16,32)`. Each of those four early systems has **42** native signed-prefix edges; their **union** has 54. Let `U` denote this 54-edge union, and for each H4--H9 required signature group `g` let `P_g` be the set of signed native-step paths of **every** legal word with any key in the inventory.

For each positive native depth `d`, retain groups whose **all** candidates have length at least `d`. A depth-`d` prefix covers a group if it prefixes some candidate in that group. Treat all depth-`d` prefixes in `U` as **free**, even though a real early system has only 42 such prefixes. Compute exactly by integer bitmask set-cover DP the minimum number `m_d` of other depth-`d` prefixes covering the remaining retained groups. The real selected paths must have at least `m_d` non-early prefixes at depth `d`, and early paths cost at least 42 in total. Therefore every legal system with inventory `K` satisfies

\[
 C_{\rm native}(K)\ \ge\ 42+\sum_{d\ge 1}m_d(K).
\]

This is a relaxation at every depth: the early 54-prefix union is granted for free, short candidate groups are discarded at deeper depths, and prefix choices at successive depths need not be compatible. Consequently any certified lower bound at least 94 is sufficient to exclude native cost at most 93. The exact DP stops upon reaching 94; retained stopped values are **lower bounds**, not claims of an individually attained optimum.

## Executed finite computation

| Family | Five-key inventories | Quota-infeasible | Quota-feasible | Exact lower-bound `>=94` | Unresolved |
| --- | ---: | ---: | ---: | ---: | ---: |
| F34789 | 3,456 | 1,500 | 1,956 | 1,956 | **0** |
| F35679 | 3,456 | 0 | 3,456 | 3,456 | **0** |
| **Both** | **6,912** | **1,500** | **5,412** | **5,412** | **0** |

Eleven disjoint indexed raw evidence JSON slices cover `0..3455` exactly once **per family**, preserving keys, classification, exact stopped depth-cover counts and the reported lower bound. Summary and SHA-256 for each slice are in `EC49FEN_EXACT_REPORT.json`. Both family's enumeration loops completed in the local Python runtime. Representative samples were independently tested with a distinct SciPy/HiGHS 0--1 MILP cover formulation: **78 depth-cover subproblems** match the exact integer DP; **26 legal 22-word systems / 572 signed native paths** pass endpoint, full BRC key, signature and unique-word checks. The sampled MILP is corroboration, while the all-inventory exact DP establishes the finite result.

## Cumulative frontier and next EC49FEO

EC49FEJ--EC49FEM had classified 10 of the 15 minimal 22-word signature structures: 13,248 full inventories, 6,576 quota-feasible with lower bound at least 94, and 6,672 infeasible. Adding these two families gives **12/15 classified**, totaling **20,160** full inventories: **11,988** quota-feasible and excluded at cost at most 93, **8,172** quota-infeasible. The three unclassified high-signature horizon families are `(3,5,6,8,9)`, `(3,5,7,8,9)`, `(3,6,7,8,9)`, totaling `4608+6912+10368=21888` inventories. Previous necessary signature census marked `4608+6912+4224=15744` as quota-feasible candidates; apply the depth-DP, then exact joint prefix integer optimization only where the lower bound is below 94. A different horizon path-count regime remains an independent route to the original `<=93` objective.

## Reproduction / source status

The `EC49FEN_complete_evidence.tar.xz` archive contains the actual executed enumerators, 11 complete raw outcome slices, current exact report, independent audit output and inherited frozen scientific scripts. Run `python EC49FEN_CENSUS.py 0 1000` etc. for F34789 and `python EC49FEN_EXTEND.py 3,5,6,7,9 0 500` etc. for F35679 in a single directory with frozen dependency scripts. `python EC49FEN_SUMMARY.py` reconstructs the exact summary and tar archive; `python EC49FEN_AUDIT.py` runs the independent SciPy checks. All scientific computation uses the same finite, typed BRC key/observer/native-step interfaces as the pinned model. No classical phase/π arithmetic, physical heartbeat inference or new P000 assumption is involved.

**Research admission:** This result is an author-side exactly scoped finite theorem with executed integer checks. GitHub publication records provenance, not independent Driver admission. The current native claimant/Owner status must be reported from the service separately; no CLAIΜ is inferred from GitHub author identity.