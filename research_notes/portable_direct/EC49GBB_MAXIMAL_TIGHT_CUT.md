# EC49GBB — maximal tight-cut reduction and true interaction residual

Status: AUTHOR_PROVED / EXACT_FINITE_FIXED_SUBSET_REDUCTION_CHECK / PARTIAL_EXACT_ROOT_REPLAY / NOT_REVIEWED. Independent portable continuation of EC49GBA (7f3002da7fa5629f12637ea196b1c64fd7623fec:research_notes/portable_direct/EC49GBA_MULTI_BANK_CONTRACTION.md), frozen BRC16943 matching observer. No new physical model, no change to P000, no claim or canonical acceptance.

## Theorem (fixed exclusive contraction, all shared subsets)

Let disjoint banks C_i have nonnegative integer resource capacities, U_i be targets with positive-capacity neighbors only in bank i, X the remaining targets with positive neighbors in at least two banks, Z the zero-neighbor targets. Remove zero-capacity edges in this matching observer only. Let f_i(W)=#{u in U_i:E(u) subset W}, d_i(W)=f_i(W)-c_i(W), delta_i=max_W d_i(W). Define W_i* as the union of all maximizers. For a subset Q of X keep U_i fixed, and write H(Q) for the original matching capacity on U union Q. Set D_i=F_i(W_i*), W*=union_i W_i*, U'=U minus union_i D_i, and delete W* edges from all remaining targets. H'(Q) is the resulting capacity on U' union Q (zero-neighbor targets may remain or be omitted).

Then W_i* is itself a maximizer; for EVERY Q subset X,

H(Q)=sum_i c_i(W_i*) + H'(Q).

Proof: for fixed E, the indicator 1_{E subset W} is supermodular, hence d_i is supermodular (capacity is modular). The family of maximizers is closed under union and intersection by the supermodular inequality and the upper bound delta_i, including the empty-resource case. For any W, d_i(W union W_i*) >= d_i(W), because d_i(W intersect W_i*) <= delta_i. The full Hall objective for U union Q is sum_i d_i(W_i) + number of Q whose entire neighborhood is contained in union W_i. Enlarging each W_i to include W_i* never decreases either term. Thus a maximum is attained among cuts containing W*. For any such cut W* union V, each removed exclusive target is confined to it; the remaining targets are counted exactly when their reduced neighborhood is contained in V. The maximum deficiency equals sum_i (|D_i|-c_i(W_i*)) + the reduced deficiency, so subtracting from original target count proves the identity. Zero-neighbor targets have no matching credit and can be omitted. This is uniform over all Q with the same fixed U and capacities, not a theorem for changes to those inputs or physical path deletion.

Strict-slack corollary: in each reduced bank, for every nonempty V of remaining positive-capacity resources, c_i(V)-f'_i(V)>0. Indeed d_i(W_i* union V)-d_i(W_i*)=f'_i(V)-c_i(V), and equality would contradict maximality of W_i*. Hence every remaining exclusive target can be matched, and any one added shared target with a nonempty residual neighborhood in that bank can also be matched with them. A shared target is a loop (zero increment in the union contraction) iff all its positive neighbors are blocked. With L the labeled set of these loops and J the GBA joint residual, J=|L|+J_live, exactly. The reduced graph is a sufficient observer for all shared subsets and integer thresholds, not a replacement for original labeled physical state.

Pair corollary: for two nonloop targets x,y, a deficiency of one occurs iff their nonempty residual bank supports both equal the same singleton {i}, and a nonempty cut V of that bank contains both residual neighborhoods with slack c_i(V)-f'_i(V)=1. Proof: if distinct banks can be chosen, strict slack gives one increment in each independently. Otherwise both supports are the same singleton; reduced Hall cuts containing neither or just one new target cannot give a positive deficiency, and a cut containing both is deficient iff its integer slack is 1. This is not a general pairwise sufficiency theorem: record 1591 has no exclusives, 12 targets with mask 990, three targets (labels 16,512,16384) with mask 33, capacities (1,4,6,4,1,1,4,6,4,1), five coordinates per bank. Mask 33 is two unit resources disjoint from mask 990; every pair of these three is matchable but the triple has rank 2. The other 12 targets fit mask 990. B=15,H=14,J=1. All one- and two-target subsets are independent in this record.

## Reproduction and results

Use EC49GBA_reproduction.zip, validated 400 SHA256 manifest entries. witness_records.json SHA256 c75076272328a0d67c4a991cdb02045099e79ddccba71aea32d4824a97b495e7. Use existing GAZ residual_frontier.py (bcaef98c1103921852edd6fe5222d462f94bfe96:research_artifacts/portable_direct/EC49GAZ/residual_frontier.py). In extracted working directory run python tight_core.py > tight_core.jsonl. Code exact Git blob 51a69640052971bf599262de20f3124e5d1220ce at ecb368ae5d053dc7ac9947190758b3398062d8e5; output exact blob 146b225c6c75576531aeca861fe29533f412765a at f33932a9a53227b611a01f09756f56e7aede3284, both verified against local Git hashes. Output SHA256 d2e1e2cb7b69d9e91ee7a787a390d171757f43471082b64091af620b7d4eb9a6. Random seed 492611270230, 1500 graphs (500 each 2/3/4 banks, width 1..3, capacity 0..3, 0..19 targets); 6880 subset checks reuse the SAME reduction computed for the full graph; all passed. 14498 stored frozen graphs checked against full Hall-cut reference and original thresholds, no disagreements. No rerun of all 360 conflict constructions.

Of 114234 positive resource occurrences, 15504 removed, with 26037 exclusive target occurrences deleted and 21760 fixed matching credits; 7242 of 273126 shared edges removed. 62 of 96 positive J records are exactly a singleton loop, 31 have J=1 without loops, 3 have J=2 without loops. Total J=99 split into 62 loop credits and 37 genuine interaction losses. For the remaining 34 records exhaustive shared-subset search by increasing size gives minimum witness for the full positive remaining deficit: (J,size,count)=(1,2,30),(1,3,1),(2,3,2),(2,4,1). All labels and masks preserved in raw output. This distinguishes genuine interaction from local blocked resources; the minimum classification is finite, not a universal small-witness theorem. Cut enumeration currently exponential in bank widths, no runtime speed claim. Next improve maximal tight-cut construction via reverse residual reachability from free slots of a maximum exclusive matching, and test whether direct matching plus pair criterion helps end-to-end.

## New physical roots (old GAK solver, not new GBB algorithm)

Frozen fourth.json SHA256 228f907796e82fe17b7984123d636a81d6d6a1bc94e357629a6a98071b390923; gak_solver.cpp SHA256 9fd83afbcdb37eeef76825fc1448fcdf00b09e090943def7edcba914e2007145. Both indices OPEN. Commands: python fourth_input.py 2008 2010 600000 > gbb_roots.in; g++ -O3 -std=c++17 gak_solver.cpp -o gak; EM_WORD=1 ./gak < gbb_roots.in > gbb_word.csv; ./gak < gbb_roots.in > gbb_base.csv. Input SHA256 c90edee38cd3d58fe0e4ebf5faa18e563dbca901804506c1d5951b05d22d4afc.

Raw word:
2008,1791,1,27255,0,6,0,0,0,0,0,0,27020,20369
2009,1792,-1,142302,0,44,0,0,0,0,0,0,141921,118277

Raw base:
2008,1791,1,37484,967,41,0,0,0,0,0,0,0,0
2009,1792,-1,203375,7368,140,0,0,0,0,0,0,0,0

Both modes agree, 2009 exhaustive NO below cap, 2008 YES with 1791 labeled-state solver replay. Evidence frontier from predecessor counts: 1970 YES/53 NO/370 other of 2393; GAR-inclusive historical 1976/55/362. M14 remains [25,27]. Continue 2010 onward; GAR/GAS evidence recovery distinct.

## Control

Global entries read at main 0087edb44fd02076151e24c320fd209d292773c8; project current Source 2eec822b7130dcd886f16969b8860173f3a91b44. P000, ACTIVE worldview, joint relation observer and portable protocol read. Native task read r4-20261127-0230-ec49as-read SUCCEEDED, NO_CANONICAL_PUBLICATION_DIRECTORY, native owner projection not evaluated, execution_authorized=false. No current private identity established, historical EM-DIRECT-23537B provenance only. No shared CLAIM or substitute identity. Branch publication only; Activity linkage and canonical integration pending.