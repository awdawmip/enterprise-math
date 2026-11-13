# R5 — 任意顺序参数下的精确证书前缀查询

Date: 2026-11-12 Asia/Shanghai. Status: author-side finite algorithm theorem, locally executed on frozen coefficients; formal Result and independent review pending.

## Frozen object and scientific provenance

Continue [R5 predecessor](https://github.com/awdawmip/enterprise-math/blob/46cac779823b4aa62ab538ffd3ab8d8f4c363bf3/research_notes/brc_r5_batch_from_seed_20261112/RESEARCH.md) at 46cac779823b4aa62ab538ffd3ab8d8f4c363bf3 (Draft PR #2182), with the **same frozen scientific input** 435e77af0d180eac32bd1f9c4c464bc4010b7551 and earlier 2,520-byte BP/label/terminal seed. This is the external auxiliary 28-coordinate, 15-labeled-operation P/Q–BRC Blackwell model, not an asserted native X6 physical law.

The verified corpus has N=2,880 trie nodes, M=1,065 distinct terminal certificates, 953 distinct exact rational activation walls and ∑_terminal depth=6,379. Each terminal t has (q_t,n_t), q_t in {3,12,15}, n_t>0, and rational threshold τ_t=(1−36q_t/n_t)/23. It activates at r≥τ_t (including equality); at r=1/23 all terminals activate. For prefix node v the exact count is C_v(r)=# { terminal descendants t of v: τ_t≤r }. The predecessor already supplies one-prefix Wavelet queries, all-prefix linear snapshots and monotone snapshots. This continuation addresses arbitrary-order **sparse** requests (v_j,r_j).

## Theorem A: offline arbitrary-order queries by terminal Fenwick tree

For every trie node v, let [L_v,H_v) be the contiguous interval of terminal preorder ranks in its subtree. Sort the terminal events by τ_t, sort K requests by r_j (remember original positions) and sweep them together. For each event with τ_t≤r_j, add one at the terminal rank using a Fenwick tree over M ranks. Answer a request by

    C_v(r_j) = BIT.prefix(H_v) − BIT.prefix(L_v).

Restore request order after the sweep. Tied walls are processed inclusively before any request at the wall.

**Proof.** Preorder enumeration of a rooted ordered tree makes the marked terminals of every node a contiguous interval, including the node itself if terminal. Before each sorted query the event cursor has inserted exactly all terminals with τ_t≤r_j; the Fenwick interval sum therefore equals the defining C_v(r_j). Sorting is only a temporary permutation. At r=1/23 every event has already occurred since all q_t,n_t>0. One-time construction of preorder intervals costs O(N); event sorting O(M log M); query sorting O(K log K); updates and interval sums O((M+K)log(M+1)), plus O(N+M+K) integer storage. Exact-rational comparison bit costs depend on input sizes. □

The method does not need to instantiate every prefix count at every r. Unlike the previous monotone online sweep, original query order may be arbitrary because the offline algorithm restores it.

## Theorem B: ancestor-wall sorted-rank index

Construct T_v, the sorted **multiset** of terminal activation walls in the subtree of v, preserving repeated walls. For any online real/rational r, regardless of the order of earlier queries,

    C_v(r) = upper_bound(T_v,r).

This uses O(log(1+|T_v|)) comparisons per query after index construction. Furthermore,

    ∑_v |T_v| = ∑_terminal_t (depth(t)+1) = 6,379+1,065 = 7,444

on this frozen corpus.

**Proof.** Each terminal wall is contained in T_v for exactly the ancestors v of that terminal, itself included; interchange the finite sums. Binary search with upper-bound convention counts all walls ≤r, including multiplicity and equality. □

The 7,444 figure counts references to exact thresholds, not serialized bytes; Python allocation is separately measured. The result is an exact query-index variant that exchanges additional temporary memory for lower query cost.

## Completed exact original-fixture experiment

The standalone executed [local full-fixture script](research_notes/brc_r5_offline_fenwick_20261112/VERIFY_R5_OFFLINE_FENWICK_FROM_PINNED.py) was prepared as an independent CPython standard-library execution in the producing conversation. It rebuilt all original 32,768 subsets, 1,065 ordered legal certificates with 28 rational-coordinate prefix inequalities, 2,880-node trie and seed. Prior full 57,600 Wavelet-vs-batch checks were repeated. The new Fenwick and ancestor-rank engines passed **57,600 further prefix/parameter comparisons** against Wavelet, all **953** root wall checks, **384** extra arbitrary mixed-order checks, and independent direct terminal-scan comparisons on the benchmark workloads. Original fixture source program was independently retained as a full standalone local artifact; the shorter GitHub script uses the branch-pinned predecessor modules and needs its own remote-byte execution.

Same-process preliminary timings for fixed-seed rational requests (seconds; median of three except direct scan measured once):

| Request workload | Wavelet | Direct scan | Ancestor-wall index | Offline Fenwick |
|---|---:|---:|---:|---:|
| Root, 256 arbitrary r | 0.002881 | 0.594459 | **0.000817** | 0.002028 |
| Broad subtrees, 512 | 0.006462 | 0.156173 | **0.001051** | 0.003090 |
| Arbitrary prefixes, 2,048 | 0.028139 | 0.019762 | **0.001554** | 0.010123 |

For the 2,048 arbitrary-prefix requests, the prepared threshold lists were 18.11x faster than the previous Python Wavelet implementation. The arbitrary-prefix mean terminal window was 3.4854. Building the sorted ancestor lists took 0.110526 s and produced a 291,200-byte tracemalloc peak during that construction interval. Query timing excludes corpus/seed/index construction; Fenwick includes request sorting. CPU/GC affinity was not controlled; timings are specific to this implementation and workload.

Actual exact-output JSON is in EXACT_OUTPUT.json; the full local standalone verifier is also saved as a conversation artifact. GitHub's branch-oriented verifier imports the pinned predecessor in the stacked branch and is marked as an independent execution obligation until actually run from its remote bytes.

## Use and next test

For repeated arbitrary online prefix queries, ancestor-wall rank is a promising option; for many sparse unordered requests without stored per-node walls, Fenwick uses O(M) work counters; tiny terminal intervals can be scanned directly. Full shared-parameter snapshots still favor previous linear/postorder or sorted event paths.

Next discriminate **complete** initialization + build + RSS + queries; test lazy per-node wall materialization and threshold sharing using 953 event ranks; determine break-even query volume, memory budget and workload crossover. Preserve frozen source coefficients, exact source boundaries and full labeled path provenance. Formal R5 owner/CLAIM requires a completed current control read; no CLAIM or independent mathematical admission is asserted by this draft.
