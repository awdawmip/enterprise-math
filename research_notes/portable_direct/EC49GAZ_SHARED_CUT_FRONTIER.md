# EC49GAZ — Shared-cut Pareto frontier and exact joint residual

2026-11-27. Portable continuation of BRC16943, EC49GAY at 90792746360a7b89aef0e9b22ad2ad64370984e5 (research_notes/portable_direct/EC49GAY_EXCLUSIVE_TARGET_DEFICIT.md). AUTHOR_PROVED / EXACT_FINITE_STORED_MATCHING_REPLAY / PARTIAL_EXACT_ROOT_REPLAY / NOT_REVIEWED. No canonical acceptance or formal task completion claimed.

## Exact theorem and proof

Use the GAY partition Z,U,V,X of labeled unit-credit targets with two disjoint integer-capacity banks. Remove zero-capacity resource bits for this matching observation only. Let H be joint matching capacity, B=H_A(U)+H_B(V)+|X|, J=B-H. For bank i, write d_i=max_W(f_i(W)-c_i(W)) for the exclusive deficit, p_i(W)=d_i-f_i(W)+c_i(W)>=0, and S_i(W)={x in X: E_i(x) subset W}. GAY gives J=max_{W,V}(|S_A(W) intersect S_B(V)|-p_A(W)-p_B(V)).

Form each bank's list of (S,p) from all cuts. Discard p>=|S|. For identical S retain minimum p. Discard a pair if another pair (S',p') has S subset S' and p'<=p. Call remaining lists P_A,P_B. Then

J=max(0, max_{(S,p) in P_A,(T,q) in P_B} (|S intersect T|-p-q)).

Indeed, p>=|S| precludes a positive joint value because q>=0 and intersection cardinality<=|S|. The dominance replacement weakly increases the objective against every other-bank pair. Any nonpositive value is covered by zero: independently maximizing exclusive cuts have p=q=0 and nonnegative intersection. Hence every positive optimum is represented on retained frontiers; all retained pairs come from actual cuts. An empty frontier on either side certifies J=0. This is an exact observer factorization for one fixed target set/capacity graph and any integer threshold; physical states and original target IDs are retained for future changes. It does not identify different physical paths or imply equality of physical recoverable sets.

A second equivalent formula exposes the contracted rank structure. For Q subset X set r_A(Q)=H_A(U union Q)-H_A(U), r_B analogously. Hall gives r_A(Q)=|Q|-max_W(|Q intersect S_A(W)|-p_A(W)). The exact residual formula follows directly by expanding both rank expressions:
max_Q(|Q|-r_A(Q)-r_B(Q))
=max_{Q,W,V} (|Q intersect S_A(W)|+|Q intersect S_B(V)|-|Q|-p_A(W)-p_B(V))
=max_{W,V} (|S_A(W) intersect S_B(V)|-p_A(W)-p_B(V))=J.
In the middle expression each shared target contributes +1 if contained on both sides, 0 if contained on only one, -1 if contained on neither; maximizing over Q selects the intersection. We make no claim that the restricted cut minimum equals r_A(Q) in general; the rank formula and its expansion are the proved assertions. This uses integer branch counts and preserves cross-bank shared identity.

Complexity of the actual frontier implementation: for m_i resource classes and x=|X|, side histogram and subset zeta transform O(n_i+m_i 2^m_i), shared cut coverage O(x 2^m_i), sorting up to 2^m_i candidates and naive dominance checks worst O(4^m_i), with bitset operations charged by representation length. Final pair checks |P_A||P_B|. This is not a general asymptotic speedup claim; it replaces the cross product of full cut lists with side preparation and exact dominance pruning. All stated counts are integer operations/cut counts, not elapsed speed.

## Actual calculation

Code: bcaef98c1103921852edd6fe5222d462f94bfe96:research_artifacts/portable_direct/EC49GAZ/residual_frontier.py, blob 300ba01d57091c2d6a46662de1b37bbfe6fbb856, SHA256 68333387b133209d7a6544ff2840f12fb3c7377557a6ade4ddf4f1b595773945. Exact output: 262a743e35294480687aef105d21208566d57e2c:research_artifacts/portable_direct/EC49GAZ/residual_frontier.jsonl, blob b5afa17aa4fc74bcceddb5b2aa245fef670344b4, SHA256 0304565ec35a48943166d7ea150cf9ae69852f7dd69eeb7ed8cbfa003875e78b. Both immutable remote reads matched the actual local Git blob. The output records all 96 positive-residual indices, B,H,L.

Reproduce using predecessor EC49GAY_reproduction.zip, all 384 existing manifest entries verified. No frozen input changes. witness_records.json SHA256 c75076272328a0d67c4a991cdb02045099e79ddccba71aea32d4824a97b495e7; ga_nodes.txt SHA256 c69d3222a0378363f8e2e238cedc6a4839edfd867435155fef83d8268c3812f0. Run python residual_frontier.py > residual_frontier.jsonl in extracted directory. Compare B-J to full integer Hall cuts calculated independently from the original target masks, with subset zeta counts. 3000 seeded random graphs (bank lengths 1..4, capacities 0..4, target count 0..24), all agreed; 14498 original stored labeled paired calls, all agreed in exact H and original threshold verdict. Distribution J=0:14402, J=1:93, J=2:3. For all integer thresholds L=0..n, the exact H comparison establishes all 182392 threshold verdicts; the number missed by using only B<=L is sum J=99, across 96 records. These are additional possible thresholds, not missed original decisions. The full cut product has 3609728 pairs across these records (990 six-class, 13393 eight-class, 115 ten-class records). Local cuts scanned 451776, distinct positive candidates 13061, retained frontier pairs (sum of list lengths) 12333, cross-bank pair evaluations 4854. In 12842 records at least one frontier empty (88.58%). The count comparison excludes transformation, dominance and bit operations and does not establish runtime speedup. No rerun of full 360 conflict graphs in this unit; only actual stored matching calls and root replay.

## New fourth-layer physical roots

Reused frozen fourth.json (SHA256 228f907796e82fe17b7984123d636a81d6d6a1bc94e357629a6a98071b390923) and GAK code gak_solver.cpp (SHA256 9fd83afbcdb37eeef76825fc1448fcdf00b09e090943def7edcba914e2007145), unchanged. Run python fourth_input.py 2004 2006 600000 > gaz_roots.in (SHA256 6a0cf3f4a4f676f88caeb88b9e3cee9b4a58126cfea2f33a45b0e18507f0269f); g++ -O3 -std=c++17 gak_solver.cpp -o gak; EM_WORD=1 ./gak < gaz_roots.in > gaz_word.csv; ./gak < gaz_roots.in > gaz_base.csv. No EM_DENSE_LIMIT override. Both runs exited successfully with internal labeled replay assertions. Raw output:

EM_WORD:
2004,1788,1,82128,0,0,0,0,0,0,0,0,81935,73870
2005,1789,1,13471,0,0,0,0,0,0,0,0,13390,11967

base:
2004,1788,1,138840,918,74,0,0,0,0,0,0,0,0
2005,1789,1,21176,0,0,0,0,0,0,0,0,0,0

3577 actual labeled states per configuration replayed. These are two previously OPEN structures, 3 and 1 ordered histories respectively. New preserved-evidence frontier 1968 YES / 51 NO / 374 other of 2393. Historical-inclusive GAR count 1974/53/366 remains separate. 25<=M14<=27 unchanged. GAZ not integrated in C++.

## Control and next

Native task read r4-20261127-0030-ec49as-topic-read SUCCEEDED at Source 160ad7b22629739e2591d6c0c406131857e6f41f; NO_CANONICAL_PUBLICATION_DIRECTORY for RS-EC49AS, native owner projection not evaluated. No current private identity binding verified; historical EM-DIRECT-23537B provenance only. No shared CLAIM, no substitute identity. Activity association and canonical integration remain pending. Next: measure end-to-end costs of frontier construction vs GAY fallback, exploit fixed-budget bitsets and cache side frontiers for fixed labeled target masks, check rank formula for extensions to more than two banks, and continue root 2006 onward. Preserve missing GAR/GAS evidence separately. Source and current norms read separately; frozen pins retained.
