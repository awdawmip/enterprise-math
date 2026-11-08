# EC49FFB — H7 mixed 23-path five-full-BRC-key native prefix obstruction

Date: 2026-11-09 (Asia/Shanghai). Status: author-side exact finite theorem; independent Driver review pending. Frozen scientific input: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. P000, ACTIVE Heartbeat World, original nine-state DFA, original six-letter signed X6 operation grammar, positive complete forward BRC keys and Source firewall are unchanged.

## Exact statement and counts

Take exactly 23 original operation words, eight horizon windows H2–H9, endpoint (+2,0,0,0,0,0) for every signed six-axis word, at most five distinct positive complete BRC keys (x,y,z), and cost C_native equal to the number of distinct nonempty **ordered signed six-axis microstep prefixes**. Require H2 low signatures (1,2,4,8), H3 high signatures (16,32), H7 mixed type B (1,8,16), three additional late windows high (16,32), and the remaining late windows low (1,2,4,8). The words at the same horizon can use different full keys from the inventory.

**Theorem:** All legal H7-mixed type-B systems satisfy C_native >= 97. The original operation/key involution I=(c d)(f g), J(x,y,z)=(y+2z,x-2z,z) preserves ordered signed prefix count and gives the same bound for the mirror type C (2,4,32). This is a universal lower bound for the declared finite family, not an assertion of sharp optimal cost for each inventory.

The prior EC49FEY exact pooled-key certificates cover high late-horizon subsets 4579, 4679, 4789, 5679 with respectively 744, 1296, 2208, 2592 feasible complete five-key inventories and lower bounds 101, 105, 108, 108. The present computation closes the remaining two:

| Late high-bearing set including H7/H9 | All candidate inventories | Signature-feasible | Certified native prefix lower bound |
|---|---:|---:|---:|
| **5789** | 9216 | **8352** | **98** |
| **6789** | 13824 | **5376** | **97** |
| Newly classified | 23040 | **13728** | **97** |

The complete original EC49FEU H7 census has 20,568 feasible inventories; 6840 earlier plus 13,728 new accounts for all of them. The remaining high-bearing sets had zero original signature-feasible inventories. By the established BRC involution the typed-C counterparts are also excluded from <=93.

## Exact finite proof

For each original five-key inventory K and each one of 23 required (h,signature) groups g, define W_g(K) as **all** legal original operation words for g, allowing any key from K; P_d(w) is the first d ordered signed native microsteps. Let L_g(K) be the minimum length of a word in W_g(K).

The complete per-inventory integer certificate selects a subset D_d(K) of required groups for each d=1,...,24. Its two checked properties are:

1. L_g(K) >= d for every selected g in D_d(K).
2. For two distinct selected groups g and g', the full sets {P_d(w): w in W_g(K)} and {P_d(w'): w' in W_g'(K)} are disjoint.

Thus every choice of one legal word per required group necessarily contributes |D_d(K)| distinct edges at depth d. Distinct depths are distinct ordered prefixes, so

C_native >= SUM_(d=1)^24 |D_d(K)|.

An exact deterministic greedy independent-set routine finds the D sets. The argument relies only on verified disjointness and coverage, **not** on the greedy routine producing a maximum independent set. Every generated record stores exact full keys, all 24 D subsets and their integral sum. The independent local validator reexpanded the original operation-word grammar and observer, checked word counts, six-axis endpoints, full key count formula, group depths, all selected pairwise prefix intersections, integer arithmetic and exhaustive original inventory-index coverage. Actual results: EXACT_INTEGER_PASS for 8352/8352 and 5376/5376, minimum checked sums 98 and 97.

The full-key enumeration fixes the necessary H3 key (3,1,1) and selects a complete high-observation-capable key independently at each of the four late high-bearing horizons. These five high horizons require different key sums x+y=h+1; a full-signature feasibility pass over **all five** keys and all required groups then eliminates invalid candidates. This covers word-level mixing of keys within a horizon, rather than forcing each window to one key.

The signed microsteps are a=(-1,-1), c=(1,2,-1,-2), d=(2,1,-2,-1), e=(3,1,1,-3), f=(1,-1), g=(2,-2). The full key equations for an h-operation word are a=z-1, e=z, c+d=x+y-h-1, f=h+1-y-2z, g=h+1-x. Those operation and observer semantics are reproduced from the frozen scientific source, with no alternate arithmetic.

## Deterministic reproduction

Use the present EC49FFB_REPRODUCE.py and the sibling prior checked module EC49FFA_H8_FIVEKEY_DEPTHWISE_20261109/h8_key_depth_sieve.py from the same PR branch. Run from the EC49FFB directory:

python3 EC49FFB_REPRODUCE.py 5789

For bounded-memory repeated runs of 6789, use six contiguous slices (the last contains 376 inventories):

for i in 0 1000 2000 3000 4000 5000; do python3 EC49FFB_REPRODUCE.py 6789 --start "$i" --limit 1000; done

Each run emits one exact JSONL certificate file and a summary JSON, with invariant checks of inventory counts, full mixed signature feasibility and group count. No LP, MIP, floating-point tolerance or randomized sampling enters this proof. The full raw bundle, 13,728 witness rows, separate executable audit, frozen word-model dependencies, logs, result histograms and SHA256 manifest are preserved as the conversation attachment EC49FFB_complete_exact_evidence.tar.xz (SHA256 b6c2887cda85e22be2b4f379b62e9818f78a8b60870dd3d84c5dc62566fe0949); the permanent GitHub source regenerates the certificates. The archive was not uploaded as a GitHub binary.

## Frontier and control boundaries

Within the specifically defined minimal-signature 23-path family with exactly one three-signature mixed horizon, the placements H2–H8 have now all been excluded at C_native <=93 (earlier EC49FEP and EC49FET, EC49FEV–FFA, and current EC49FFB); H9 mixed is structurally impossible under these constraints. The existing 22-path 94-edge construction is still the recorded mother-problem upper witness. The useful next mathematical target is non-minimal signature supports, altered word count allocations, or a constructive test at C_native<=93 with complete keys, retaining original X6 intermediate semantics.

This publication is an author-side proof and source record. Native task CLAIM/Result and independent mathematical admission depend on actual service authority, which was not available at this run's identity check.
