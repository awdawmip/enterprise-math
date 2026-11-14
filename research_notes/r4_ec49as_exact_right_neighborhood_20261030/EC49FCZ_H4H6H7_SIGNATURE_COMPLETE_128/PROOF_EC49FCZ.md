# EC49FCZ — complete H4/H6/H7-signature seven-slot exact minima (128/128)

Date: 2026-11-07 (Asia/Shanghai). Status: AUTHOR_FINITE_EXACT_PROOF / LOCAL_COMPUTATION_EXECUTED / UNREVIEWED / NOT_ADMITTED.

## Frozen model and exact statement

Scientific input pin: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Keep the nine-state trap-avoiding observer, 24 original signed-native paths and their complete nonempty ordered primitive-step prefixes, and the BRC keys L=(4,2,1), M=(7,3,2). The authoritative candidate language is the previously pinned EC49FCS frozen_model.py, Git blob 7e97065ac9a0ff70435b92ee2f4bd718c9bf1859.

For all r,s,t in {1,2,4,8}, replace the seven original paths in either of two branches, each by one legal word in its frozen observer language:

- A(r,s,t) = {4:r, 5:16, 6:s, 7:t, 8:2, 8:4, 9:16}.
- B(r,s,t) = {4:r, 5:32, 6:s, 7:t, 8:1, 8:8, 9:32}.

The 17 unselected original paths stay fixed. **For every one of these 2*4*4*4=128 precisely specified finite domains, the minimum number of distinct nonempty native signed ordered primitive prefixes across all 24 paths is exactly 158.** Eight (s=t=1) were previously computed in EC49FCY; this round completes another 120 distinct seven-slot domains.

## Exact proof by labelled prefix-trie dynamic programming

Let F be the union of prefixes of all 17 fixed paths and let T be the common rooted trie of every legal signed-primitive expansion for the seven mutable slot languages. At trie edge e (entering prefix p), define c(e)=0 if p is in F and c(e)=1 otherwise. A terminal is labelled by every slot for which the terminal word is legal; multiple labels on the same terminal are preserved.

Define D_v(M) to be the minimum total added edge cost in the subtree at node v sufficient to cover each required slot label in subset M. Initialize Q_v(M)=0 if M is a subset of the terminal-label set of v, and +infinity otherwise. For each child u, update

    Q'_v(M) = min_{K subseteq M} [ Q_v(M \ K) + D_u(K) + c(v,u)*1_{K nonempty} ].

After all children, let D_v=Q_v. The exact value is |F|+D_root(AllSevenLabels). Every legal choice of candidate words generates such a feasible covering of terminal labels and a rooted union of paths, hence is considered by the recurrence. Every finite recurrence value selects legal terminal paths; if a label is covered more than once, discard redundant terminals without increasing its edge-union cost. Induction on trie height proves the recurrence's exactness. For fixed k=7, this takes O(E 3^7) exact integer operations and O(V 2^7) memory after candidate generation. Prefixes are literal signed words: no scalar, unordered, unsigned or total-only quotient is applied.

The unchanged original 24-word witness occurs in each full candidate language and has exactly 158 distinct prefixes, establishing an upper bound of 158. The exact trie DP yields a matching lower bound of 158 for all 128 complete candidate languages; equality follows in each domain.

## Actually executed evidence

All 128 instances were generated from the frozen operator counts, nine-state transition table and signed primitive-step expansion; each was processed with the compiled C++ labelled trie solver (g++ -O3 -std=c++17). Each case has candidate sizes H4=12, H5=12, H6=30, H7 in {540,720}, the two H8 pools {3150,1890}, and H9=1680. The uncompressed Cartesian product per case is 23,332,385,664,000,000 or 31,109,847,552,000,000 mathematical combinations, not executed combinations.

- Complete-language results: 128/128 exact minimum 158.
- New domains beyond EC49FCY: 120.
- Trie nodes per case: at most 54,674.
- DP transition evaluations per case: 113,454,999–119,569,851; cumulative 14,862,156,534.
- Published EC49FCY regression: all eight cases match their earlier fixed edge counts, trie nodes, added edge counts and exact transition counts (8/8).
- Independent literal signed-prefix enumeration of 64 restricted seven-slot submodels, two candidates per selected slot, matched the same compiled C++ DP exactly (64/64). This independent check covers the restricted submodels; complete 128-language lower bounds rest on the full-language DP and the induction proof.

All original executed Python, C++ source, actual 128-row and 64-row evidence, and run log are packaged as **EC49FCZ_full_exact_evidence.tar.xz.b64** in this directory. Decode its base64 to an xz-compressed tar archive (base64 -d | tar -xJf -); the original binary archive SHA-256 is 023489e1090ad07e5f3fbbd1f2bd2af6bb07146db70dce646c4de538ea2cdfd1. Rebuild the large trie instances from RUN_EC49FCZ.py rather than storing repeated intermediate text. The local frozen_model.py is a source-semantics adaptation of the pinned EC49FCS script; the authoritative frozen source is its immutable Git blob given above.

## Frontier and next experiment

EC49FDA: preserve this finite observer and test eight-slot domains with an additional H6 or H7 path variable, thereby allowing two independently mutable paths in one later window while retaining both H8 carriers; seek a legal <158 witness or certify further local minima. A distinct route changes legal BRC L/M cache-key placement and accounts for the full resulting construction cost. The full nine-window 93-edge mother target is open.

On this run the Enterprise Math native gateway returned BACKEND_IDENTITY_OR_VERSION_MISMATCH (operation_sent=false); Owner, CLAIМ/Result and independent Driver review are unconfirmed. This is preserved as an author-side scientific result only.
