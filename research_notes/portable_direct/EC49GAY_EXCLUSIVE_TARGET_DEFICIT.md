# EC49GAY — Exclusive-target Hall bound and exact joint residual

Continuation of BRC16943, frozen inputs unchanged, 2026-11-26. Extends EC49GAY_BANK_MASK_CUTS.md (2d25d6e4647a3c2e50ac9c16fa74c8c2df025507). Author proof; finite exact replay; not independently reviewed or canonically accepted.

## Theorem

For unit-credit labeled targets with disjoint resource banks A and B, let Z have no positive-capacity eligible resource, U have resources only in A, V only in B, and X in both. Write H for the joint maximum matching capacity and H_A(U), H_B(V) for the exclusive-side maximum capacities. Then

B = H_A(U) + H_B(V) + |X| >= H.

Every joint matching decomposes by original target identity. Its restrictions on U and V are feasible matchings in their own banks, and it matches at most |X| shared targets; Z is never matched. Hence B<=L is a sound upper-threshold certificate. A failure to certify is not a lower bound on H. Removing isolated Z from the abstract matching preserves H; never remove physical competing states.

For resource cuts W_A,W_B let f_U,f_V count exclusive targets with all their eligible resources in the corresponding cut; f_X counts shared targets with both neighborhoods contained. Set d_A=max_W(f_U(W)-c_A(W))=|U|-H_A(U), and d_B similarly. Define p_A(W)=d_A-f_U(W)+c_A(W)>=0, p_B similarly. The full Hall deficit equals

|Z|+d_A+d_B+max_{W_A,W_B}(f_X(W_A,W_B)-p_A(W_A)-p_B(W_B)).

This follows by substituting into the full contained-neighborhood Hall cut formula proved in GAW and factored in GAY. Thus the exact unresolved joint residual is

J=B-H=max_{W_A,W_B}(f_X(W_A,W_B)-p_A(W_A)-p_B(W_B))>=0.

The maximum is nonnegative because cuts attaining both individual deficits exist. B is exact iff this maximum is zero. This preserves joint identity and gives a structural continuation direction, not an assumption that residuals vanish. Any particular jointly chosen cut supplies a lower bound on J. Exclusive side upper bounds may replace exact side capacities in the pruning inequality but not in this exact residual identity.

## Actual frozen replay and timings

Reused GAQ exact side interval Hall oracle and GAY zero-mask partition. Five runs zero/exclusive/exclusive/zero/checked on 180 nodes, 360 budget cases, 87,058 directed cross checks each. Identical final graphs, scalar misses 358275, allocation nodes 41334, paired calls 14498, paired prunes 8680, extreme_yes 536. Hall side misses increased 19451 to 31172. The checked run compared all 14498 paired calls against an exhaustive cut reference, with no discrepancy.

Zero runs: 6724 direct zero hits; 7774 fallbacks; 8395 zero targets removed in fallbacks; 89611 fallback targets; 77155 processed augmentation attempts; 5818 lower stops, 1956 upper stops. Times (ns) 1282881396,1395210561.
Exclusive runs: 6724 zero hits, 1956 exclusive hits, 5818 fallbacks, 6743 zero targets removed in fallbacks, 68326 fallback targets, 67693 processed attempts, 5818 lower stops and zero upper stops in fallback. Times (ns) 1217723337,1242188097. Checked time 6642477043 ns, excluded from speed comparison. All 8680 successful upper checks now avoid joint augmentation on this frozen set. Compared with the first GAY baseline 95919 attempts, 29.43% fewer attempts. Compared within this paired timing experiment, mean 1.3390459785s to 1.229955717s, about 8.15% less time. These timings are finite measurements, not general speed guarantees. The exclusive side oracle is additional work; avoiding joint augmentation is not avoiding all matching calculations.

An independent direct replay of all 14498 stored labeled witness records using exact full and exclusive-bank cut calculations gives J=0 on 14402, J=1 on 93, J=2 on 3. All 96 positive residual cases are lower/nonprune at their actual threshold. The B<=L predicate therefore agrees with H<=L on every record, although B does not equal H generally. The 3 cases at J=2 include a concrete witness: capacities [1,3,3,1,1,3,3,1], 16 shared targets; 12 have eligibility mask 238, 4 mask 17; the latter share only two unit resources and the other 12 fit the remaining resources. H=14, B=16, L=13. Neither bound prunes at this threshold; at L=14 the full exact cut prunes but B misses, demonstrating the scope boundary.

## Preservation and reproduction

Frozen input BRC16943: ga_nodes.txt SHA256 c69d3222a0378363f8e2e238cedc6a4839edfd867435155fef83d8268c3812f0; gap_target.json 392de76fa357280c5bcf949b8280871e70bf2e1381b4cb2ed2d12db7593374a5; witness_records.json c75076272328a0d67c4a991cdb02045099e79ddccba71aea32d4824a97b495e7. Same original inputs and root references as first GAY note.

Run in the extracted reproduction directory:
python exclusive_hall.py > exclusive_hall.json
python exclusive_residual.py > exclusive_residual.json

- exclusive_hall.py at b0cd172dd3186c6430820978c9002ef7053dbacb, blob ef81ce34c237201758c63c1d6ece09b2f7ba95cc, SHA256 d8576085ccee740dde316f3aa7caa4eb755fedc1e6b0c1d7fc51e7790e3b4dcf
- exclusive_residual.py at a734184628a33e7655054b7e2fef7b84bb020e78, blob d7ea0e279fce3cf3164785ecae199f1faf02c8fc, SHA256 376f6aaa5ecea343756e456c047128e5ef74a81d1e6536baec68ee7abb3d7b0b
- exact residual census and original witnesses at 6510785c6b41bb1962828d935010cd0ace684c53:research_artifacts/portable_direct/EC49GAY/exclusive_residual.json, blob 4e926e11e1b58ae922845805e5d15265fc964349, SHA256 126c6d21ac0ab1ceb03e6d7d30dbe6d6442e4e34d7556107c2a559d38851af2c
- full raw timing and per-case counters local archive exclusive_hall.json SHA256 4383511247fe8b6d2b41864fb7a95ce5a4d6d2f42aee85bdc9ca675819cbc54e; aggregate actual counters and times reproduced above. Code and residual data remote readback verified.

## Frontier and next question

Root 2002 NO / 2003 YES (both 1787 states), exact two GAK configurations agreement; first GAY note records raw results. Preserved-evidence frontier 1966 YES / 51 NO / 376 other of 2393; GAR historical-inclusive 1972/53/368. 25<=M14<=27 unchanged. GAY cuts are not integrated into C++.

Next: quantify positive residual J without full joint matching using penalized cuts and test additional target sets and thresholds, including the L=14 counterexample. Continue fresh root 2004 onward. Keep missing GAR/GAS evidence recovery separate. RS-EC49AS read succeeded, no canonical publication directory at b5bd8b79c1a9d8cd2c7290537612bd0fa5870eee; owner projection not evaluated, no private binding confirmed, no shared CLAIM taken. Activity association and canonical integration pending. Historical provenance EM-DIRECT-23537B only.
