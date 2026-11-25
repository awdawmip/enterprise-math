# EC49GAI — Bounded exact Boolean dense-signature solver, physical witness installation

2026-11-26. Independent informed portable continuation of EC49GAH, proof 591163908f60780cb56aaad2f022dc13c59b2caf:research_notes/portable_direct/EC49GAH_DENSE_SIGNATURE_REPLAY.md; evidence branch 96884cc2bbbc3612a3f70d6344da56dde80154ff. Frozen BRC16943 inputs: fourth.json SHA256 228f907796e82fe17b7984123d636a81d6d6a1bc94e357629a6a98071b390923; ga_nodes.txt c69d3222a0378363f8e2e238cedc6a4839edfd867435155fef83d8268c3812f0; GAG recoverable_frontier.out e38afab4f6b72deedb20660b5213d816b2028569b773fd684a350e748d7f17bb. Parent archive SHA256SUMS checked; P000 unchanged, static finite observer only.

## Boolean projection theorem and actual physical reconstruction

For the fixed unit-cost binary observation language on a finite separating population I, let F_d(I) indicate existence of a complete identification tree of depth at most d. By GAG, F_d(I)=1 iff the missed-set antichain contains the empty set (and then that antichain is exactly {empty}). The exact direct projection is F_d(I)=OR over effective splits A|B of [F_{d-1}(A) AND F_{d-1}(B)], with F_d=1 for |I|<=1 and F_0=0 otherwise. If |I|>2^d or either child exceeds 2^(d-1), the corresponding feasibility is false by the binary leaf count. These tests and the recurrence suffice independently of all support-specific prunes. The GAH dense signature key (n, sorted distinct nonconstant complement-normalized masks, d) determines this Boolean observer. Child signatures are obtained by restriction and packing, and a successful key need store only one generating split, a failed key only -1. This is an exact observer projection, not a replacement for the full weighted frontier when that stronger observer is needed.

The C++ integration uses n<=16, d<=4 after the existing leaf-count gate. Enumerate support/mandatory-hole/free-hole states under cap H=14 from normalized canonical columns, check count equals n, form all 10*25 physical masks, retain a physical row/column representative for each complement-normalized dense mask. For a successful dense split, select that representative, construct both actual normalized children and recursively install successful witnesses in the original S,k memo. This works even when child normalization permutes state order: recompute the actual dense key and its representative map, not a stale parent label map. Complement swaps only answers, not the feasibility conjunction; both actual branches are installed. Induction on d proves successful physical installation; singleton leaves need no memo. Negative answers require exhaustion of all feasible splits or the leaf-count bound. Existing final replay filters each physical original state using the actual row/column query, preserving canonical-to-original column maps and checking the final singleton, budget and intermediate counts. No abstract query is treated as an actual physical query without a representative.

Cache policy: completed exact entries only; clear all when insertion would exceed L entries; L=0 means no cache. Recursion holds values, not pointers/iterators to entries across recursive calls. Eviction can remove only speed benefit, because an absent key is evaluated by the same recurrence; no unknown/cap-exhausted root result is cached. Fixed scope n<=16,d<=4, at most 250 distinct physical masks at any key; key encoding is 2 bytes plus 2 bytes per mask, at most 502 payload bytes, plus hash-table/object overhead. L=8192 bounds entry count, not the entire solver memory. The original normal-call cap is retained but dense recursive work/installation is not charged as original calls: comparisons report full wall time and dense work separately, not equal-total-work experiments.

## Actual tests

180 frozen failure-conditioned records at original depth and original depth+1, 360 cases. All 360 labels agree between original C++ solver, dense default cache, 32-entry cache, 0-entry cache, and independent Python full physical-state min-max recurrence. All 180 original-depth labels also match GAG's empty-frontier test. Independent depth histogram 4:27, 5:152, 6:1 (node index 28); 179 YES at original depth+1 and all 180 original-depth NO. 2126 actual physical-state replays in each C++ mode. No mismatches. Exact independent depth sequence (one digit per node in original order, 180 digits):
455555555454555555455545555565555554545555555555555555555555545555554545555554555545545555555554555555555555555555555555454555455545555554545554545545555555555554555455555554555554
JSON array with compact separators and newline SHA256 4194522407b0bf6514f91b84f5ef43515bcdcbeaf2894a686a1381f59701b8d2.

Default cache final counters: hits=2761, misses=286, clears=0, size=286, tested child products=1060; 32-entry: hits=3792, misses=1002, clears=31, final size=10, peak observed size=32, products=2760; 0-entry: hits=0, misses=9506, size=0, products=9320. Original normal calls 1255 vs dense 670 in 360 cases; this is not equal-work accounting.

## Fourth-layer roots

Selected only 8 previously OPEN roots, exact same frozen population and cap 250000 original calls per root. First four historical difficult roots remain OPEN at cap, not NO. Next four newly attempted roots all YES in both solver modes with 6354 independently filtered physical states replayed per mode. Exact raw rows, columns id,n,status,calls,envelopePrunes,satChecks,satPrunes,cumulative dense hits,misses,clears,entries,products:

dense difficult:
1773,1451,0,250001,7286,0,0,18887,3716,0,3716,17113
1813,1495,0,250001,3892,0,0,31727,5612,0,5612,27444
1852,1557,0,250001,1895,0,0,34644,5984,0,5984,29526
1865,1575,0,250001,9055,0,0,43461,7146,0,7146,34922
baseline difficult:
1773,1451,0,250001,7185,193,0,0,0,0,0,0
1813,1495,0,250001,3892,183,0,0,0,0,0,0
1852,1557,0,250001,1860,100,0,0,0,0,0,0
1865,1575,0,250001,8997,173,0,0,0,0,0,0
dense fresh:
1870,1580,1,67524,1493,0,0,3630,741,0,741,3259
1877,1591,1,68618,1953,0,0,8918,1780,0,1780,7731
1878,1591,1,70272,512,0,0,10782,2011,0,2011,9068
1879,1592,1,17671,325,0,0,11317,2045,0,2045,9193
baseline fresh:
1870,1580,1,67807,1493,94,0,0,0,0,0,0
1877,1591,1,69000,1953,71,0,0,0,0,0,0
1878,1591,1,70435,512,37,0,0,0,0,0,0
1879,1592,1,17819,325,58,0,0,0,0,0,0

Sequential local single-run wall seconds / peak RSS KiB: difficult dense 12.24/126768, baseline 11.53/122656; fresh dense 2.35/36616, baseline 2.54/36204. Dense calls sum 1224089 (includes four cap attempts), fresh 224085 vs baseline 225061. No universal speedup, no deployment, no accepted C++ production change; test branch only. Cache avoided many repeated subproblems, but physical map generation and installations can outweigh this. Next: cheap single-fiber gate, conditional entry selection, actual byte/cost accounting; continue only unresolved roots. Four new canonical YES classes account for 9 ordered histories, giving 1899 YES/27 NO/467 OPEN of 2393; ordered 3840/46/809 of 4695, 25<=M14<=27 unchanged.

## Reproducibility

Use GAH archive with original sat_token.cpp SHA256 f1d819e8447386e7a6a7ae91ac1c6ec7272e4ff6ea908f461955f432ae481fc5 (FZV proof at 3c5c0de42d624482927315f142aa0a5f49095682:research_notes/portable_direct/EC49FZV_SATURATED_PHYSICAL_TOKEN_COVER.md). New code at 99778f821ba9a9463aa7804b91e1327fc27c5807:research_artifacts/portable_direct/EC49GAI/{dense_bool.hpp,build_gai.py,retry_gai.py}. All three remote blobs matched local execution. Build: python build_gai.py; g++ -O3 -std=c++17 dense_solver.cpp -o dense_solver. Generated solver SHA256 a555ed1a4b537fe50471ca29cd4c08c3b9597c7c89f13794f206c62c5d0601ce.
Generate gai_nodes.in by reading each ga_nodes.txt line k,n,*p, emit 360 cases, each original record i at d=k,k+1: header i*2+(d!=k),n,25,d,100000 (space-separated), then n successive support/hole pairs from p. Run EM_DENSE=1 ./dense_solver < gai_nodes.in and repeat with EM_DENSE_LIMIT=32 or 0; unset EM_DENSE for original baseline. Independent Python model(n,physical(st,10,25)) from multi_target.py returns full,qs,cert,split,ref,allowed; exact depth ref(full,full). Compare first three output columns across modes and with the reference; check 0 in GAG frontier for original budgets. Root inputs: python retry_gai.py 0 4 250000 > gai_roots.in; python retry_gai.py 4 8 250000 > gai_fresh.in. Run with/without EM_DENSE. Output hashes (all raw files included in local reproduction archive; timing files separately):
gai_nodes.in 3b328a56949a9b12e5b36fe3cb9b027d1ff01a4093e3132377b76a9f5eb7e5e8
gai_nodes_dense.csv e0602c7456e16e43b8636d23bc0bbea12bd5b21b3e22d2b912cc81915c04cf1b
gai_nodes_base.csv 956f186391e455c192bb88fe75e74b663df5ba08e20b23fe384de004255dbcee
gai_nodes_0.csv 612e7e0ebfbd24b2d7634f047b7f9534110c243ecc0ee685b17b14a82337456a
gai_nodes_32.csv 64007b653ab95e590954bd25258c6bebd6d491a1dc1752d411a1850dbbf3cff3
gai_roots.in d7b47f4e422cbda65045a02c999cc20c5ecc202ad5b248acd1e299bc7fc2e0e1
gai_fresh.in 107e5a8003f1dfca3fa47a6b100faac2ccd7cf2cc2d713c0c0389dee3cfae73e
gai_root_dense.csv e6500bb9a08ef99e57a1650d1a16212efa987cf5431e82e05757043db689f279
gai_root_base.csv 0df2956b30595bdf6999fe65686865ff55cd324cd46a9ba7a215e1d066f3a09c
gai_fresh_dense.csv 4f47b9d5f803063cf9bb4d0b17bb18048d22fdb475cde0a182f622a0425eaa23
gai_fresh_base.csv 2d120c4f0e6100f868ffb5f4c6574eed177d26de3cca635f457ca63d2a1a44d8

## Control status

GK canonical entry snapshot d550ce51d894468553b46611c18ccea7c62882a3; both entry blobs and relevant rules/P000/ACTIVE worldview revalidated against that immutable main; Source normative snapshot 609525b844ebe988aac82d76d95e329b2e101336. Topic read r4-20261126-0728-ec49as-read SUCCEEDED at that Source, 2026-11-25T23:28:39.065774Z, NO_CANONICAL_PUBLICATION_DIRECTORY; native operational owner projection not evaluated. Historical EM-DIRECT-23537B provenance; current private identity and Activity binding unconfirmed. No shared CLAIM or replacement identity. AUTHOR_PROVED / EXACT_FINITE_BOOLEAN_CACHE_AND_PHYSICAL_REPLAY / PARTIAL_EXACT_BRANCH_REPLAY / NOT_REVIEWED.
