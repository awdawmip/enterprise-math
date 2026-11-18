# EC49FCX — stronger carrier theorem and 32 exact six-slot signed-prefix minima

Date: 2026-11-07 (Asia/Shanghai).
Status: AUTHOR_FINITE_EXACT_PROOF / EXECUTED / UNREVIEWED / NOT_ADMITTED.
Frozen scientific input: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
Frozen model: research_notes/r4_ec49as_exact_right_neighborhood_20261030/EC49FCS_EARLY_H4_H5_LATE_H7_H8_H9_256/frozen_model.py (Git blob 7e97065ac9a0ff70435b92ee2f4bd718c9bf1859).
Observer: the frozen nine-state trap-excluding DFA; the fixed 24 original signature slots and complete signed-native ordered primitive-prefix language.
Cache L=(4,2,1) for H2–H5; M=(7,3,2) for H6–H9. Original full prefix-union witness costs 158 distinct nonempty edges.

## Theorem A: fixed-carrier elimination for arbitrary selected-slot sets

For an original designated slot d, define P(d) as its set of ALL nonempty literal signed-native primitive prefixes, and C(d)={t ≠ d: P(d) ⊆ P(t)}, computed using the original words. For any selected mutable slot set S and a subset R⊆S such that for every d∈R at least one t∈C(d) is not in S, the finite exact optimum of the original 24-word prefix union satisfies

OPT(S)=OPT(S\R).

Proof: Fix any legal words at S\R. For each d∈R choose its own original word. An unselected original carrier t already supplies all of P(d), so restoring d incurs zero extra prefixes. Every other word at d can only add prefixes to the union; its replacement cannot reduce the union supplied by fixed slots and other chosen slots. Hence every feasible assignment on S can be matched or improved by one on S\R, and the reverse inequality follows from inclusion of the latter feasible assignments. This holds simultaneously for all R. QED.

Complete original-carrier lists for six relevant slots, checked on signed primitive expansions:

2:16: {3:16,4:2,5:16,8:2,8:4,9:16}
3:16: {4:2,5:16,8:2,8:4,9:16}
5:16: {8:2,8:4,9:16}
2:32: {3:32,4:8,5:32,8:1,8:8,9:32}
3:32: {4:8,5:32,8:1,8:8,9:32}
5:32: {8:1,8:8,9:32}.

Thus changing both H8 carriers need not make H5 indispensable: an unchanged H9 carrier still eliminates the original H5 choice. This strengthens EC49FCW's at-most-one-H8-selection theorem.

## Theorem B: exact weighted trie dynamic program (general finite method)

For a selected set S of k mutable slots, let F be the signed-prefix union of all original slots outside S. Generate the complete legal candidate pool for each selected slot using the frozen multiset/DFA/signature language. Insert each candidate's FULL signed-native primitive expansion into a single rooted trie. At terminal nodes record a k-bit label mask identifying the selected slots for which an admissible word terminates there. Multiple candidates and labels may have identical signed expansions. For the edge entering child u, set c(v,u)=0 if its complete signed prefix is already in F and 1 otherwise.

For a trie node v and required-label subset mask M define D_v(M) as the minimum new-edge cost within its subtree necessary to select terminal nodes covering all labels in M. Initially Q_v(M)=0 if every label in M is terminal at v, and +infinity otherwise. For each child u, update, using the child's finalized table:

Q'_v(M)= min_{K ⊆ M} (Q_v(M\K)+D_u(K)+ 1_{K≠∅} c(v,u)).

After all children, D_v=Q_v. The global exact optimum is |F|+D_root((1<<k)-1). Reconstruct one terminal witness per label and independently replay its entire 24-slot primitive prefix union.

Correctness: Every selection of one legal word per mutable slot determines a connected union of root-to-terminal trie paths. For each node, the labels realized in different child subtries can be partitioned; each used child subtree contributes its D_u value and the incoming edge cost exactly once. Conversely, each finite DP partition yields at least one admissible terminal for every label, so gives a legal selection. An optimum using redundant multiple terminals can be reduced to one per slot without raising cost. Induction from trie leaves proves exactness. Complexity excluding the explicitly paid input generation is O(E·3^k) time and O(V·2^k) table space for E trie edges and V nodes. No independence of operator strings or unique signed expansion is presumed.

## Theorem C: complete 32 six-slot minima

For a∈{16,32}, take two matching H8 carriers and the matching H9 carrier, plus the selected H5 and any one H6 and one H7 slot:

a=16: S=(5:16,6:s6,7:s7,8:2,8:4,9:16)
a=32: S=(5:32,6:s6,7:s7,8:1,8:8,9:32)

with s6,s7 independently ranging over {1,2,4,8}. Thus 2×4×4=32 exact finite domains, six mutable paths, 18 original paths fixed; each mutable path ranges over its complete frozen DFA candidate pool. All 32 minima equal **158** signed primitive-prefix edges.

Exact candidate pool sizes are 12 for H5, 30 for H6, 540 or 720 for H7 according to required signature, 3150 and 1890 for the matching H8 carriers and 1680 for H9. Their unpruned product sums to 72,589,644,288,000,000 possible selections (mathematical search-space size, not executed loops).

Actual executed trie DP: at most 54,602 nodes per case; 1,697,998 cumulative trie nodes (counting each separate case); 64 mask states per node. Computed fixed-edge costs are among 122/123/132 and minimum new-edge costs among 36/35/26. The reported 32 reconstructed witnesses all replay at exactly 158 edges. The original full witness gives a feasible 158 upper bound, and the proven complete DP recurrence supplies an equal global lower bound for each enumerated finite domain; hence exact optimum 158.

Proof evidence: DECODABLE, executed Python verifier, full per-case records, original batch outputs and hashes are included in this directory. Exact 32-row certificate: EC49FCX_SIX_32_CERTIFICATE.json.gz.b64; decoded SHA-256 83cd122728f3bc84ea5ee1fb6c9f72422a49b4c091c7c991baa438cf1aa4f8e0. Generated using VERIFY_EC49FCX.py (decoded SHA-256 b2b8aaed3ef85e9997586cd455e7f1535c2798ef3e1fa134b50280261775b3ba) and VERIFY_EC49FCX_SIX.py (decoded SHA-256 1415b7109c2a498ba08002ec57c81e083d8efd3ad61121efb699c2e8fa1092b9), merged with COMBINE_EC49FCX.py (decoded SHA-256 7248677a22d4122728865d85211d63d007ee4b23d25a693a909d883a81108429). All methods are exact integer/bitmask/string set operations.

## Carrier boundary, additional exact experiments

Select all original carriers of H5:16: S=(5:16,8:2,8:4,9:16). The other 20 fixed original words cost 138 edges. Each of the 12 legal H5:16 replacements now has positive individual residual; the original 'feggf' gives the unique minimum 3, and the others give residual-size distribution {4:1,6:1,10:9}. The symmetric S=(5:32,8:1,8:8,9:32) has the same distribution with 'geffg' the unique minimum. Thus the unchanged-carrier hypothesis in Theorem A fails at this exact boundary; the fully coordinated four-slot optimum is nevertheless still 158 for both cases. Eight explicit two-/three-/four-slot boundary domains were solved by the exact trie DP. A separate direct Cartesian enumeration checks the two H5+both matching H8 three-slot cases after the safe individual improvement cap: respectively 12 and 3 full remaining tuples, no improvement, residual 7 against fixed cost 151. This second method checks only these three-slot domains, not all 32 six-slot results.

## Reproduction / provenance

All frozen source definitions and candidate languages are retained exactly. Decode each published .gz.b64 text file with 'base64 -d FILE.gz.b64 | gzip -d > FILE'. Decode EC49FCX_8_BATCHES.tar.gz.b64 with 'base64 -d ... | tar xzf -'. In a Python 3 environment run VERIFY_EC49FCX.py for the short report; run VERIFY_EC49FCX_SIX.py for each of 8 (branch,H6) combinations (A/B ×1/2/4/8); combine using COMBINE_EC49FCX.py. The combine script's '/mnt/data' default scratch path is replaceable without altering the scientific input. Original batch SHA-256 values and all 32 witness strings are present in the combined certificate. The decoded short report SHA-256 is 1a22d4d40d149e335d2331ef8c1c889b4f7dbcc420468b323cea137998e38866.

These are 32 **six-slot** results, distinct from and not added to the previously reported 8,284 **five-slot** exact searches. The complete nine-window 93-edge mother target remains open. NEXT_EC49FCY.md identifies the next discriminating unit. The signed native prefix model is a declared finite mathematical slice, not a claim of completed X6/Heartbeat causal dynamics.

Research author GitHub identity: awdawmip. Source-native status/session/owner calls returned BACKEND_IDENTITY_OR_VERSION_MISMATCH with operation_sent=false; no claimed Source CLAIM/Result, active owner or independent Driver mathematical admission. PR branch is author-side research storage. GLOBAL_KNOWLEDGE_V1 P000 and ACTIVE worldview were read unchanged.
