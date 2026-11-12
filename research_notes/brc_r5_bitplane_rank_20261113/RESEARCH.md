# R5 — exact bit-sliced prefix activation without per-node sorted caches

Date: 2026-11-13 (Asia/Shanghai). Status: author-side exact finite algorithm theorem; executed local original-fixture validation; independent review and formal native Result pending.

## Immutable inherited scientific model

This work retains the original P/Q–BRC Blackwell **auxiliary model** at `435e77af0d180eac32bd1f9c4c464bc4010b7551`: 28 coordinates, 15 labeled operations, 1,065 selected ordered certificates, 2,880 trie nodes, 953 distinct exact rational activation thresholds, and 2,520-byte recoverable BP/label/terminal persistent seed. The immediate predecessor is [Draft PR #2192](https://github.com/awdawmip/enterprise-math/pull/2192), head `413565fbb7b4e104a45444914eff74daf53d7461`, on which this branch is stacked. Nothing changes the source certificate selection, signs, prefix legality, `q` or `n`.

For terminal certificate `t`, `tau_t=(1-36*q_t/n_t)/23`. For trie prefix `v`, descendants occupy terminal preorder interval `[L_v,H_v)`. Let `w_0<...<w_(W-1)` list the **distinct** rational thresholds, `W=953`; let `e_i` be the rank of terminal `i`'s threshold. The parameter bound is `b(r)=upper_bound(w,r)`. Then
`C_v(r)=sum_(i=L_v)^(H_v-1) [e_i<b(r)]`.
The use of upper_bound retains equality at each activation wall and counts tied certificates individually.

## Theorem (bit-sliced interval rank comparator)

For any finite ordered tree with `M` ordered terminals and `W>=2` distinct totally ordered thresholds, put `d=ceil(log2(W))` and form bit-plane `P_j=sum_(i=0)^(M-1) (((e_i>>j)&1)<<i)` for each `0<=j<d`. For an interval `[L,H)` and integer bound `b`, define `E=((1<<(H-L))-1)<<L` and `S=0`. Process bit positions `j=d-1,...,0`. Write `Z=E & ~P_j`. When bit `j` of `b` is one, set `S=S|Z`, `E=E&P_j`; when the bit is zero, set `E=Z`. Return `popcount(S)`. Use boundary shortcuts `b<=0 -> 0` and `b>=W -> H-L`.

**Exact claim:** this returns `#{i in [L,H):e_i<b}` for every interval and integer `0<=b<=W`, including duplicate `e_i`. It has no per-prefix cache and no tree-dependent proof assumptions beyond the terminal interval property.

**Proof.** After processing every bit above `j`, `E` is precisely the set of selected terminals whose high processed code prefix agrees with the corresponding prefix of `b`; `S` is precisely those already determined smaller at an earlier bit. This is true before the first bit. At bit `j` with bound bit zero, only the zero-code positions remain equal and no new position becomes smaller. At bound bit one, each zero-code position of `E` becomes smaller and each one-code position stays equal. Hence the invariant advances. After the last bit, `S` comprises exactly positions with `e_i<b`; positions still equal to `b` do not belong to `S`. The two boundary shortcuts handle the bound outside the encoded rank range. QED.

The bit-plane logical payload is `d*M=10*1065=10650 bits=1332 bytes` when tightly packed, the same logical information content as the predecessor's packed terminal code vector, but reorganized to support **direct unsorted range rank queries**. In the executed CPython representation, the ten `int` objects collectively occupy `1680` bytes via `sys.getsizeof`; the exact sorted rational wall table and decoded seed are additional runtime memory. The persisted seed remains 2,520 bytes. This is an algorithmic representation improvement, not a new 1,332-byte universal complete-corpus encoding claim.

Each comparator uses `d` bit-plane operations on at most `M`-bit integers, plus `O(log W)` exact rational wall search. In a word-RAM accounting the bit work is `O(d*ceil(M/word_bits))` per query; constructing the planes from decoded event ranks takes `O(M*d)` elementary bit insertions. For a small window of `m_v=H_v-L_v` terminals, direct scan takes `O(m_v)` comparisons after the same wall lookup, yielding an exact hybrid that selects direct scan below a tunable `m_v` threshold and bit-plane comparison otherwise.

## Executed evidence and comparison

Executed local program `VERIFY_R5_BITSLICED_EXACT.py` reused the independently executed original-fixture source from the prior R5 continuation, rebuilding **all 32,768 operation subsets** and its frozen 1,065 certificate paths from exact rational coefficients. Compared bit-plane and threshold-based hybrid results against the original Wavelet-based exact rational implementation for all **57,600 = 2,880 * 20** prefix/parameter cases, and checked all **953** rational threshold ties at the root. Separately exhausted **99,780** ternary-vector interval/bound cases up to six entries. All passed; evidence marker `PASS_R5_BITSLICED_RANK_REAL_FIXTURE`.

Measured local CPython (median of five same-process runs, GC disabled within timed queries, source reconstruction excluded), in milliseconds:

| Workload | Requests | Direct rank scan | All bit-sliced | Hybrid cutoff 8 |
|---|---:|---:|---:|---:|
| Root | 256 | 8.181 | 1.361 | 1.346 |
| Broad 21-node pool | 512 | 4.234 | 2.762 | 2.679 |
| Random | 2,048 | 7.379 | 16.799 | 7.266 |
| Hot-node mixture | 2,048 | 19.363 | 13.805 | 12.278 |

The bit-plane representation performs well on broad/hot queries, while the random case contains many tiny subtrees where fixed ten-bit work dominates. Hybrid cutoff 8 is competitive here without materializing per-node sorted rank vectors. The measurements are a comparison of these concrete Python implementations and distributions, not a universal latency theorem.

A new portable stacked-branch verifier `VERIFY_R5_BITSLICED_FROM_PINNED.py` retains the same frozen evidence chain and checks the theorem against the parent pinned implementation. Its remote bytes are published for independent execution; the *executed local* full-fixture verification and the published portable script are distinct evidence surfaces. The full local evidence summary is `EXACT_OUTPUT.json`.

## Durable scientific frontier

**Completed:** arbitrary-order exact bit-sliced range-rank theorem; finite exhaustive comparator tests; frozen original-fixture 57,600 exact query equalities and all 953 root threshold ties; fixed workload measurements and memory accounting.

**Pending:** run the exact published portable verifier from a clean checkout; measure complete RSS, seed decode, exact wall construction and end-to-end latency including output; optimize dispatch among direct scan, bit-planes, cached sorted lists and offline Fenwick under explicit memory/query budgets; independent native mathematical review and control Source Result as authorized.

**Ownership:** this is author-side science saved in GitHub. Its branch and Draft PR are not formal CLAIM, freeze, review or P000 promotion. The R5 formal owner still requires actual authenticated control-source resolution before any claim. Prior contributor authorship is retained.
