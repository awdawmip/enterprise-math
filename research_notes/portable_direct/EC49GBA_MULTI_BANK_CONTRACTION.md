# EC49GBA — Multi-bank contracted rank and constructive residual certificate

2026-11-27. Portable continuation of frozen BRC16943, EC49GAZ at 3148ebcfbe07b3d9a1ac3ab5fff1a544590d192a. AUTHOR_PROVED / EXACT_FINITE_MULTI_BANK_MATCHING_CHECK / EXACT_FINITE_STORED_MATCHING_REPLAY / PARTIAL_EXACT_ROOT_REPLAY / NOT_REVIEWED. The observation is a fixed labeled unit-credit capacity graph, not the full physical decision tree or native spatial model.

## Multi-bank theorem

Let m>=1 disjoint finite banks have nonnegative integer resource capacities. Each labeled target has at most one credit and an arbitrary subset of resources in each bank. Delete zero-capacity edges for this observer only; retain original labels and graph for changed observations. Partition targets into Z (no usable bank), U_i (exactly bank i), and X (at least two usable banks). Write H_i(Y) for maximum bank-i matching rank on Y, H for full joint rank, B=sum_i H_i(U_i)+|X| and J=B-H. Then

J = max_{Q subset X} [|Q|-sum_i (H_i(U_i union Q)-H_i(U_i))].

This formula extends GAZ to arbitrary numbers of banks and does not require each shared target to be present in every bank.

For bank cut W_i let d_i=|U_i|-H_i(U_i), f_i(W_i)=number of exclusive targets whose entire neighborhood is in W_i, c_i(W_i)=sum of capacities in W_i, p_i=d_i-f_i(W_i)+c_i(W_i)>=0 and S_i(W_i)={x in X: E_i(x) subset W_i}. Inaccessible banks have empty E_i(x), so include x in S_i for every such bank. Full Hall cut formula gives

|T|-H=|Z|+sum_i d_i+max_{W_1,...,W_m}(|intersection_i S_i(W_i)|-sum_i p_i(W_i)).

Thus J is the last maximum. The single-bank Hall formula applied to U_i union Q gives r_i(Q)=H_i(U_i union Q)-H_i(U_i)=|Q|-max_{W_i}(|Q intersect S_i(W_i)|-p_i(W_i)). Substitute into |Q|-sum_i r_i(Q) and interchange finite maxima. Each x in Q contributes the number of S_i containing it minus (m-1). The maximum over Q therefore sums +1 precisely over the intersection of all S_i; zero-contribution elements may be included arbitrarily. This yields the stated formula. This is also the deficiency of the union of the contracted transversal matroid ranks; the proof above uses only integer cut counts and does not assert new classical matroid-union theory.

## Constructive matching and short certificate

First independently match each U_i to its exact maximum, then insert each shared target, preferring a free resource and otherwise following alternating augmenting paths with capacities represented by occupied target lists rather than by expanding slots. Each exclusive rank remains attained: augmentations preserve every already matched target (though resource assignment can change). No unmatched exclusive target can be the start of a successful augmentation after exclusive saturation: it would increase the number of matched exclusive targets in its sole bank beyond its maximum. After each shared insertion the matching is maximum on that prefix: adding one unmatched vertex to a maximum prefix permits at most one extra credit, and any new augmenting path must start at the new vertex (an unmatched new vertex cannot be internal to an alternating path). Standard finite augmenting-path optimality follows by symmetric difference with any larger matching, after conceptually splitting capacities into slots. The implementation visits a resource once per search, trying all of its current occupants; a reachable resource with a free slot ends the search. It preserves labeled target identity throughout.

From the final matching close the set A of all unmatched targets under arcs target->all allowed resources and resource->all matched occupants. Write W=N(A). Every reachable resource is saturated; every occupant belongs to A; every matched target in A occupies a reachable resource. Hence |A|-c(W)=|T|-H. Conversely any matching can match at most c(W) of A, so this equality independently certifies optimum. Moreover F(W)={t:E(t) subset W}=A: an unmatched t is already in A; a matched t in F(W) has its occupied resource in W, so is in A. With W split by bank, Q=X intersect A=intersection_i S_i(W_i). This Q maximizes the contracted-rank deficiency: expansion of the rank formula at these maximizing cuts yields at least J, and the theorem bounds it by J. No claim of minimum cardinality for Q.

For an implementation using adjacency lists, at most n searches each scan at most O(E+n+m_resources) entries, plus one closure and construction; capacities need not be expanded. The actual Python code uses integer bitsets and bank scans; cost includes bit length, building masks, occupancy arrays and verification. Independent cut enumeration and certificate rank checks are verification-only, not needed to compute the matching. No elapsed speed comparison is asserted.

Singleton marginal checks alone are insufficient: two banks A={a,b}, B={c}, all unit capacities. Exclusive e has {a,b}, f has {c}; shared x has {a,c}, y has {b,c}. B=4, H=3, J=1. Each singleton Q has incremental rank sum 1, while {x,y} has rank sum 1 and deficiency 1. Thus shared interaction cannot be dropped after local singleton checks. Exact compression is scoped to fixed graph and all integer thresholds, original physical paths retained.

## Actual finite validation

Reproduce from the predecessor EC49GAZ_reproduction.zip (all 391 SHA256 manifest entries checked). No frozen inputs changed. witness_records.json SHA256 c75076272328a0d67c4a991cdb02045099e79ddccba71aea32d4824a97b495e7, residual_frontier.py SHA256 68333387b133209d7a6544ff2840f12fb3c7377557a6ade4ddf4f1b595773945. Code multi_bank.py SHA256 84eb15f159bfd25ee8630c83c51a6b0a9e60b3d18e2942ace30d6dd29dfe99c9 Git blob 9a84cbb5164720715847de75f30742aab826de01, remote 0dada29e8b06d6d619dd59d85d927d72ad4862b3:research_artifacts/portable_direct/EC49GBA/multi_bank.py. Run python multi_bank.py > multi_bank.jsonl in extracted cwd. Output SHA256 ea6024fb2fe96d94f9a42e7e13da1143f565e7030a88b4468136e8896233baaa, blob 9699654de1cccf530011e2950625c5bdfbcf714b, remote 024ea7fc025390628e6c37228fea9dc04ae23044:research_artifacts/portable_direct/EC49GBA/multi_bank.jsonl. Both remote reads matched local Git blobs. The output retains all 96 positive-residual indices and original Q labels. Random seed 492611270130, 2000 arbitrary graphs with 2/3/4 banks (667/667/666), widths 1..3, capacities 0..3 and 0..19 targets. All match independent full-cut reference, with explicit feasible matching and Hall closure assertions. All 14498 stored frozen calls agree with exact full cuts and original threshold; residual histogram 0:14402, 1:93, 2:3. 44048 shared insertions use direct free capacity, 173 require exchange attempts (including 99 failed insertions, sum J); 99.61% direct. Total resource visits in augment searches 131343 (excluding direct checks, grouping, closure and independent reference). Q size histogram for 96 positive cases: 1:62, 2:30, 3:3, 4:1, each independently checked by bank cut ranks. This is not minimum-size evidence. No full 360 conflict graph rerun and no new multi-bank physical model claim.

## Fresh fourth-layer physical roots

Frozen fourth.json SHA256 228f907796e82fe17b7984123d636a81d6d6a1bc94e357629a6a98071b390923 and gak_solver.cpp SHA256 9fd83afbcdb37eeef76825fc1448fcdf00b09e090943def7edcba914e2007145. Run python fourth_input.py 2006 2008 600000 > gba_roots.in (SHA256 e9c48897e0d408511854067454bf1f3223fdf7a173480d34803a02b842fbe4ba); g++ -O3 -std=c++17 gak_solver.cpp -o gak; EM_WORD=1 ./gak < gba_roots.in > gba_word.csv; ./gak < gba_roots.in > gba_base.csv. Both input indices OPEN; raw output:

EM_WORD:
2006,1790,-1,63347,0,15,0,0,0,0,0,0,63110,52481
2007,1791,1,104111,0,29,0,0,0,0,0,0,103749,82238

base:
2006,1790,-1,94854,1826,74,0,0,0,0,0,0,0,0
2007,1791,1,139535,4980,75,0,0,0,0,0,0,0,0

Both modes agree; 2006 exhaustive NO below cap, 2007 YES with 1791 actual labeled states replayed per configuration. New preserved-evidence frontier 1969 YES/52 NO/372 other of 2393; historical GAR-inclusive 1975/54/364. M14 remains [25,27]. GBA not integrated in C++.

## Control and continuation

Read current global canonical main 5ab956d8d218c5261068e322bf85976b54f0f3cb and current Source c47d2367c4bc6039953742a97babaecdc7703eab, P000, ACTIVE worldview, observer contract, portable rules and predecessor exact note. Native request r4-20261127-0130-ec49as-read SUCCEEDED, NO_CANONICAL_PUBLICATION_DIRECTORY, native owner projection not evaluated. No current private identity verified; historical EM-DIRECT-23537B provenance only. No shared CLAIM or substitute identity. Activity/canonical integration pending. Next: compare warm-start solver end-to-end against GAY/GAV, exploit contracted rank singleton loops with exact joint fallback; continue root 2008 onward. Preserve GAR/GAS missing historical evidence separately.
