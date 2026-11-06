# EC49FDA — 228 eight-slot signed-prefix exact minima and a third-carrier lemma

Date: 2026-11-07 (Asia/Shanghai). Status: **AUTHOR_FINITE_EXACT_PROOF / EXECUTED / UNREVIEWED / NOT_ADMITTED**. This handoff belongs to Enterprise Math PR #1730, following immutable source commit f9e7b886ee18e255acb6e16bab09eaa512847451.

## Exact scientific object

Scientific input pin: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Frozen model: Git blob 7e97065ac9a0ff70435b92ee2f4bd718c9bf1859; exact trie solver: Git blob dfe7a3b596f615a26b88d48beee931459d2357eb. Reuse the previous sibling directory EC49FCZ_H4H6H7_SIGNATURE_COMPLETE_128. The original 24 designated signature slots, nine-state trap-avoiding observer, full ordered signed primitive prefixes and BRC multiset-cache keys L=(4,2,1), M=(7,3,2) remain unchanged. This is a finite optimization within the specified typed observer; original 158-edge witness remains feasible.

For an original/allowed word w, let P(w) be the set of all its distinct nonempty **literal signed primitive-step prefixes**. In any selected replacement set S, every slot outside S retains its original word; each slot in S chooses exactly one word from its **full** frozen multiset-and-DFA signature language. The cost is the size of the union of the 24 P(w) sets.

Set A(r,s,t) = {4:r,5:16,6:s,7:t,8:2,8:4,9:16}, and B(r,s,t) = {4:r,5:32,6:s,7:t,8:1,8:8,9:32}. All r,s,t range over {1,2,4,8}. Add exactly one **distinct** extra slot 6:q (q != s), or 7:q (q != t), with q from the same four signatures. Each selected set thus has eight distinct variable slots and 16 fixed slots.

**Theorem 1 (228 eight-slot cases).** For both branches, all r=1 with arbitrary s,t, and all s=t=1 with arbitrary r, including either kind of extra slot, the exact global minimum is **158 edges**. These families contain 2 × 2 × (4² × 3 + 4 × 3 − 3) = **228 distinct instances**, each proved over its entire finite candidate language. No instance in this set has an admissible cost of 157 or lower.

## Exact lower-bound proof and numerical certificate

For fixed S define F as the union of P(w) for the 16 unchanged original paths. Build the full signed-prefix trie of every admissible replacement word for each of the eight labels. A trie child edge has cost 0 if its literal prefix is already in F, otherwise 1. Terminal nodes carry a bitmask for labels whose admissible words terminate there.

Define D(v,M) as the minimum number of new edges strictly inside the subtree at node v to complete exactly the label subset M. At v, one may allocate any subset of terminal labels at zero further edge cost. For each child u, allocate a disjoint subset N of as-yet-unallocated labels, paying D(u,N) plus the child-edge cost precisely when N is nonempty. Minimize over all partitions of M. Bottom-up induction proves this recurrence covers every choice of one whole candidate word per selected label and counts each shared new prefix edge exactly once. At the root the exact total is |F| + D(root,all eight labels). All arithmetic and masks are exact integers; no numerical tolerance is used.

The reproduced original witness provides the 158 upper bound. The full-language trie DP provides the 158 lower bound in all 228 rows; hence equality is exact for these cases. The report stores keys, fixed-prefix count, full trie-node count, full solver transition count, pool sizes, exact optimum and per-process resource observation. All 228 minima are 158; fixed-prefix counts lie from 108 to 126; maximum trie size is 59,174 nodes; observed maximum resident size is 66,816 KiB; summed DP transitions are 82,852,517,952 (actual recurrence-loop iterations, not the unpruned Cartesian product).

An independently written direct literal signed-prefix set enumerator also checked **1,495,908** candidate combinations (three legal words at each of eight selected slots, times 228). Every restricted minimum is 158. This second check validates a specified restricted sublanguage; the **full-language** minimum is certified by the exact trie recurrence and full candidate generator.

The complete 228-row UTF-8 JSON is losslessly preserved in EC49FDA_228_EXACT_REPORT.json.gz.b64. Decoded report SHA-256: **81c8151d72979553fc044e985d70b132971342085a82f3779ddcfced3f6b34cf**. The original executed local computation used bounded batches (48 per run) and merged identical overlapping rows; duplicate intersections agreed on fixed-prefix counts, trie sizes, candidate pools, transition counts and optima. The published REPLAY_EC49FDA.py is the executed certificate checker and can regenerate/check rows against the sibling frozen generator and C++ solver.

## Theorem 2 (three-carrier elimination; independent analytic increment)

In the frozen **original** witness, the signed prefix set for original 5:16 = feggf is contained in those for **8:2 = feggfead, 8:4 = feggfeac and 9:16 = feggfeafg**. Likewise original 5:32 = geffg has its signed prefix set contained in those for **8:1 = geffgaed, 8:8 = geffgaec and 9:32 = geffgaegf**. The 2 × 3 exact literal-containment checks pass with the frozen signed primitive expansion (each H5 path contributes 12 nonempty signed prefixes).

For any replacement set S containing 5:16, if **at least one** of {8:2,8:4,9:16} is outside S, the optimization variable 5:16 is removable without changing the exact optimum. The analogous statement holds for 5:32 using {8:1,8:8,9:32}. Proof: one unchanged carrier supplies every original H5 prefix; reverting H5 to its original legal word adds no new edge and cannot increase any completion cost. This extends the previous H8 two-carrier condition to the H9 carrier. In Theorem 1's A/B selected sets, all three corresponding carriers are mutable, so the exact eight-slot search tests beyond that elimination condition.

## Verification and next mathematical unit

From this directory within the PR branch, using standard Python and a C++17 compiler:

    python REPLAY_EC49FDA.py --check --literal
    python REPLAY_EC49FDA.py --recompute --limit 4
    python REPLAY_EC49FDA.py --recompute

The first command verifies the complete 228-row archive, combinatorial coverage, SHA-256, and independent restricted literal audit. The second reproduces four full-language exact cases using the previous immutable sources; the third recomputes all 228 cases. Local execution completed all 228 exact cases using bounded original batches, verified the complete report and literal audit, and successfully replayed four cases through the published combined program. The full one-process combined replay was interrupted after its first 64 matches by the execution environment; original bounded batches supply the other exact results.

**Next EC49FDB:** the encompassing add-one-H6/H7 eight-slot family has 2 × 4³ × 6 = 768 instances; 228 are complete here and **540 remain**. Prioritize discriminating signatures with r != 1 and (s,t) != (1,1), then test a materially different route such as admissible BRC cache-key rearrangements or nine-slot interactions to address the open 93-edge nine-window mother target. Preserve the first explicit sub-158 witness if found.

GitHub-connected identity: awdawmip (repository push permission verified). Native Enterprise Math service returned BACKEND_IDENTITY_OR_VERSION_MISMATCH with operation_sent=false; Site connection reports research_authority_granted=false. Live owner, native CLAIM, Source Result and independent Driver mathematical admission remain unresolved. This publication is an **author-side research artifact**, with unchanged P000, ACTIVE worldview and scientific pin.
