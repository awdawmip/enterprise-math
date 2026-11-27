# EC49GBR — capacity-level augmentation and weighted residual emergence
2026-11-27. AUTHOR_PROVED / EXACT_FINITE_FULL_FROZEN_UNIT_COST_CERTIFICATE_REPLAY / EXACT_FINITE_RANDOM_WEIGHTED_REPLAY / PARTIAL_EXACT_ROOT_REPLAY / NOT_REVIEWED.
Predecessor 1b29a8373dbadf27a32efa02c2ab5b15b57f926a:research_notes/portable_direct/EC49GBQ_TWO_PROBE_DELETION_CERTIFICATES.md. Same BRC16943 frozen labeled integer-mask matching observer. No new native physical attribution.

## Capacity-level augmenting construction
For fixed W, project original labeled targets to R=C\W, ignoring empty projected masks for this particular deletion objective. If R includes a zero-capacity port, strict Hall is impossible; if R is empty, cost zero. Otherwise all c_i>=1. Maintain a complete matching of accepted targets I with each port's occupant list and each target's assigned port. No capacity slots are expanded.
To augment a fresh label x, BFS from x over ports in its mask. Mark each port at its first encounter, keeping its predecessor target. If a reached port has occupancy less than its integer capacity, reverse the alternating predecessor chain (move that target into the vacancy and continue with its old port), obtaining a full augmented matching. Otherwise expand all occupants' masks. Each visited port is processed once; each matched label belongs to only one occupant list. The alternating path is simple: each predecessor target was first encountered through a previously reached port, so reversal terminates at x. If no vacancy is reached, the reached ports V are all full and every occupant's mask lies in V. No assignment has changed. This is the exact capacitated Hall obstruction and the same feasibility test as slot expansion. No assumption on the numerical size of capacities is used.
Apply GBQ's double probe: first augment x (strict Hall guarantees success); next augment a fresh copy of x with the same nonempty mask. If success, remove the temporary copy; otherwise remove x, and record the reached port mask V, tight for I since f_I(V)=c(V)-1. A rejected label's whole mask is in V. As in GBQ, tight witnesses persist under future acceptance and intersecting witnesses have tight union. Merge into disjoint blocks to obtain exact deletion optimum and dual certificate.
Cost: at most 2m searches for m projected targets and n ports. At most m+1 targets and n ports per search, O(mn+n) mask-bit inspections and O(mn) conservative vector erasure/move cost per search; merging blocks costs O(n^2) mask operations per rejection. Sorting optional weighted order costs O(m log m). Working storage O(m+n) target/port records plus O(mn+n^2) bits for masks and blocks, O(n log(1+max c_i)) capacity bits. Accounting for mask and integer bit width, this is polynomial in binary input size, with no allocation proportional to total capacity. The replay implementation uses 32-bit masks and signed 64-bit capacities/costs; its actual tests use n<=10, small capacities and weights. Unbounded arithmetic would require corresponding arbitrary-width representations. The certificate verification below uses exponential subset enumeration only as a reference, not in the construction.

## Weighted residual emergence theorem
For each original projected label x assign a nonnegative deletion cost w_x. Define rho_w(W) as minimum sum of costs of deleted labels subject to strict Hall of retained labels. Labels fully contained in W may be retained at no effect. For distinct positive weights lambda_1>...>lambda_k>0, lambda_{k+1}=0, set A_j={x:w_x>=lambda_j}. Let rho_{A_j}(W) denote the unweighted deletion threshold with only these labels.
Then
rho_w(W) = sum_{j=1}^k (lambda_j-lambda_{j+1}) rho_{A_j}(W).
Moreover one greedy pass in nonincreasing weight order constructs a common optimum deletion set D, attaining |D intersect A_j|=rho_{A_j}(W) simultaneously at every weight boundary.
Proof: for any feasible D, restriction to A_j leaves a strict Hall feasible retained subset, hence |D intersect A_j|>=rho_{A_j}(W). Layer-cake summation gives the lower bound. Run the capacity-level double-probe algorithm in nonincreasing weight order. At each weight boundary it has executed precisely the GBQ greedy algorithm on that prefix, whose disjoint tight blocks prove minimum cardinality of rejected labels. Subsequent acceptance/rejection never changes earlier label identities. The same D thus attains every bound, and layer-cake equality proves optimality. Zero weights contribute nothing and can be processed last. For arbitrary finite nonnegative real weights this argument is exact; code tests integer costs only. Prefix tight blocks give an independently verifiable weighted dual if saved at the boundaries; current code verifies weighted optimality by exhaustive subset reference, not by persisting those boundary blocks.
Corollary: strict Hall feasible labeled subsets form a matroid (hereditary; every greedy maximal independent subset on any restriction has the same cardinality by GBQ). The weighted result can also be seen as classical matroid greedy; the useful increment is its explicit application to residual emergence plus a capacity-level witness construction. A weighted budget may stop once rejected cost exceeds the budget, because each processed prefix is already cost-optimal and restriction of any full feasible deletion to the prefix is feasible. Current cap test is for unit-cost cardinality only.
Counterexample to identifying weighted and unweighted optimal sets: one port c=2 and two labels with that sole port, deletion costs 1 and 100. Either singleton deletion attains cardinality 1; only deleting the cost-1 label attains weighted optimum 1. Order/cost thus retains consequential label information; no native physical meaning or new spatial axis asserted.

## Executed evidence
Code 801ae64baec451ef40d65490b92263b50390ef53:research_artifacts/portable_direct/EC49GBR/compact.cpp, executed local Git blob 38cbcb6a41d12c6d71f2a59542331b2ff6cb38ae matches remote readback. SHA256 d7fe67fc7d48d509f81cf9efde6f0869053ed763c61cd1dd4d6524cb9904a8d6. Compile g++ -O3 -std=c++17 compact.cpp -o compact; ./compact < frozen.in.
Recovered unchanged witness_records.json from GBJ reproduction archive; SHA256 c75076272328a0d67c4a991cdb02045099e79ddccba71aea32d4824a97b495e7 equals GBQ. Convert each record r as print(len(r['caps']),len(r['opts']),*r['caps'],*r['opts'].values()). frozen.in SHA256 95b400c2fdf75a965bd5059f6b3b987dfc4bac589d9504a1610abe482b4546b5, same GBQ. All 14498 records, all W, positive frozen capacities, test each retained subset against all nonempty residual V, verify disjoint block sum equals deletion count. Every 16th flattened frozen W also executes fresh capped passes d=0,1,2. Random seed 20261127; 1000 models, n=1..6, m=0..8, c=1..3, masks including empty, integer weights 0..10; all W and all label subsets tested for weighted optimum. Exact stdout (SHA256 aa880cc309e8db9c67309a67a5c3af5b38243d5afccffe74554faecd2b543f57):

```
weighted_random_rows=20756 brute_subsets=1254348
frozen_rows=3609728 primal_constraints=91774090 capped_checks=676824 mismatches=0
0 435542
1 453829
2 590673
3 533080
4 437234
5 375858
6 311441
7 193389
8 130930
9 80660
10 38290
11 18180
12 7461
13 2308
14 630
15 182
16 41
```

All 17 histogram bins agree with GBQ/GBP. Wall time 6.96s including new weighted brute force and full reference constraints; not a matched benchmark, no speedup claim. Capped checks validate truncated outcomes, not time savings. No arbitrary huge-capacity experiment was run. No formal or independent review.

## Fourth-layer continuation
Verified same fourth.json SHA256 228f907796e82fe17b7984123d636a81d6d6a1bc94e357629a6a98071b390923, GAK solver 9fd83afbcdb37eeef76825fc1448fcdf00b09e090943def7edcba914e2007145, fourth_input.py 3f0ab92970a8089457ae529cb771cfa63402db391e95c0c37a610c2150a6429f; gen.py 4e57db60f4bdf82af2feba763099b58998905121a916e8dbd0a4e7633e9f4d89. python fourth_input.py 2040 2042 600000 > roots.in; g++ -O3 -std=c++17 gak_solver.cpp -o solver; ./solver < roots.in and EM_WORD=1 ./solver < roots.in. Input SHA256 b44b6a5f130d522eecf51e6cb0984243f47f441ce95c5255e5860b100ec04eea; base stdout SHA256 28b71253a7cfc9583f707bde8e4cd3e8db90676f94e683206efd94a37eb139fb; word stdout SHA256 86d9b96ec4860a8eb20ae6fb63107e27c8a85b16c14bbcceb731904c228a8b79.

```
2040,1868,1,20659,173,2,0,0,0,0,0,0,0,0
2041,1874,1,118134,3589,70,0,0,0,0,0,0,0,0
2040,1868,1,11839,0,0,0,0,0,0,0,0,11716,9649
2041,1874,1,62912,0,24,0,0,0,0,0,0,62733,55114
```

Both configurations return YES for both roots; inherited aggregate now 1990 YES, 65 NO, 338 other of 2393; M14 remains [25,27]. Next root 2042.

## Control and continuation
Verified GK entry blobs from immutable main 1d367b44583aafe4772eb4ed1400009d9d7add51; EM behavioral protocol blobs at 7277e45989ff76b3ecdba7b8d176ac5f4f37791b; P000 V4/V5, ACTIVE worldview, joint relation and residual contracts and portable research applied. Exact topic read r4-20261127-1830-ec49as-topic-read SUCCEEDED, 2026-11-27T10:28:36.204447Z, Source 7277e45989ff76b3ecdba7b8d176ac5f4f37791b, NO_CANONICAL_PUBLICATION_DIRECTORY, native operational view not evaluated, execution_authorized=false. Historical EM-DIRECT-23537B provenance only; current private identity binding unconfirmed. Independent informed portable science without shared CLAIM, replacement identity, Result or Review. Activity association and canonical integration pending.
Next: weighted horizon dual prefix extraction and direct threshold test; compare capped capacity-level vs GBQ slots with identical input and verification outside timer; examine reuse of certificates between adjacent W and integration into dynamic observers. Preserve original label map and port relations for future operations.
