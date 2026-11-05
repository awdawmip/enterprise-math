# PREFIX-505 — Exact workload-optimal adaptive V-block rank in the BRC–KMP–source observer

2026-11-05 (Asia/Shanghai). Independent author-side research, Researcher-ID **EM-DIRECT-5BCCCD**, activity **RA-9BBB3ACA5369EF9C72AA5BC6**. Scientific inputs frozen at `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`. Uses PREFIX-500 exact support cardinalities, PREFIX-501–503 spatial/W codec and PREFIX-504 sparse V blocks. Research status: AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED; no formal TASK CLAIM.

## Model and exact question

In the explicitly declared native signed X6 model, select ten letters `a,A,b,B,c,C,d,D,e,E` along five native axes, with sixth-axis path occupation zero. At fixed path length n, the BRC readout retains signed displacement y and cancellation observations V,W, plus the terminal KMP state q of gate g∈{aab,aba} and first B/C source t∈{N,B,C}. Future operations are signed primitive-letter appends. This observer is a typed restricted X6 model; time-dependent physical heartbeat evolution is not assumed.

Fix the SOURCE-safe quotient spatial key p=(y_a,y_b,|y_c|,|y_d|+|y_e|), a W row and m=(n−|y_a|−|y_b|−|y_c|−|y_d|−|y_e|)/2≥0 integral. Let L=2m+1 and k_v=|K_g(p,W,v)| for v=0,…,L−1, where K_g is the PREFIX-500 exact control/source-support set. Given maximum block width b≥1, select **exactly** B=ceil(L/b) blocks, the minimum number possible, to minimize total online source-support-oracle calls across one rank (or one inverse) query for each actually reachable (V,q,t) state of this row.

## Theorem: exact optimal adaptive partition and gapless inverse

For every admissible n,p,W,g,b, there is an integer dynamic program computing the globally optimal partition within the constraints above. Its variable-boundary rank and inverse are gapless, and each needs at most min(b,L) support-oracle evaluations. It preserves the PREFIX-504 length-n observer and the inherited native append-then-reencode operation.

**Proof.** A partition has strictly increasing endpoints 0=l₀<…<l_B=L with 1≤l_j−l_(j−1)≤b. In a block [i,j), a target at V=v causes v−i+1 exact support-oracle calls (the preceding V values and its own control set), both for rank and inverse. There are k_v different reachable control/source states at that V. Thus the workload for the block is C(i,j)=Σ_{i≤v<j} k_v(v−i+1). Let F(j)=Σ_{v<j}k_v, T(j)=Σ_{v<j}(v+1)k_v. Exact integer rearrangement gives

```
C(i,j) = T(j)-T(i)-i*(F(j)-F(i)).
D(0,0)=0; D(0,j>0)=∞;
D(a,j)=min_{max(a-1,j-b)≤i<j} [D(a-1,i)+C(i,j)].
```

Any a-block partition of [0,j) has precisely one last block [i,j), leaving an admissible (a−1)-block partition of [0,i). Induction proves D(B,L) globally optimal. Backtracking yields the endpoints.

Store for each row the adaptive endpoints and cumulative support P_j=Σ_{v<l_j}k_v. Given V, choose its unique endpoint block by binary search, then compute P_j+Σ_{l_j≤h<V}k_h+ord_{K_g(p,W,V)}(q,t). For inverse, select the **rightmost** j with P_j≤r and j<B, then scan that block until the remaining offset falls within a positive k_v, recovering V and its ordered control pair. Duplicate prefix values represent zero-weight blocks; using the rightmost admissible prefix handles them. Both procedures enumerate the same contiguous lexicographic row order, so they are inverse bijections. PREFIX-503 spatial and W offsets are unchanged. Composition with the exact primitive append updater gives the declared update fidelity. QED.

**Complexity and full accounting.** F,T construction uses O(L) integer operations. Straightforward DP has O(BLb) integer-operation preprocessing and O(BL) temporary words per row. Prefix-index construction additionally evaluates each of the L supports once. Prefix counts store B+1 integers (the same count as PREFIX-504). Adaptive boundary locations add B−1 integers if 0 and L are implicit, yielding global O((n+1)^5+(n+1)^6/b) stored words across O(n⁵) quotient W rows. The online support-call maximum remains min(b,L); binary search over block endpoints adds O(log(B+1)) integer comparisons in addition to the inherited spatial/W terms. All index integers are O(log(n+2)) bits in this bounded-observer model. Across all rows, direct DP is bounded by O(n⁷) arithmetic operations and support acquisition by O(n⁶) oracle evaluations. The extra DP is a precomputation cost; end-to-end gains depend on query volume, concrete memory bytes, and native update frequency.

For a uniform distribution over actual reachable joint states within the row, dividing the workload by Σk_v gives exactly the expected oracle-call count. A multiplicity-aware nonuniform distribution can replace k_v with explicitly supplied state traffic weights and use the same recurrence. If every signed spatial fiber of a quotient row is queried equally, its common signed-fiber multiplicity multiplies all block costs and leaves the optimizer unchanged.

## Verified exact computation

The attached standalone JavaScript program independently generates every distinct complete native observer state of length n=0,…,8 for both gates, groups the resulting (q,t) sets into precise (p,W,V) supports, compares the DP cost against **all admissible partitions** for b∈{2,3,4}, and checks row-local exact rank/inverse on every reachable control state with b=2. All arithmetic stays within exactly representable safe integers. Final result: `ALL_CHECKS_PASS`.

At n=8 the distinct full native observer states are aab=60590, aba=60550. The aggregate counts below are for the quotient W rows, not duplicated by signed-spatial multiplicities; each figure is a complete single-query-per-control-state oracle workload over those rows:

| b | aab rows improved | aab calls uniform → optimal | aba rows improved | aba calls uniform → optimal | Extra adaptive boundary words (per gate) |
|---:|---:|---:|---:|---:|---:|
| 2 | 516/1287 | 12800 → 11497 | 564/1287 | 13001 → 11546 | 1220 |
| 3 | 328/1287 | 15943 → 14395 | 328/1287 | 16184 → 14526 | 417 |
| 4 | 335/1287 | 17484 → 14928 | 335/1287 | 17873 → 15081 | 341 |

Concrete strict witness for aab, n=8, (y_a,y_b,|y_c|,|y_d|+|y_e|,W)=(2,1,1,0,1): k=[7,8,8,7,0]. At b=4, fixed PREFIX-504 endpoints [0,4,5] take 75 support calls across 30 reachable row states. The adaptive endpoints [0,2,5] take 45 calls: exactly 40% fewer, retaining two blocks and maximum block width four. Exact average calls per state are respectively 5/2 and 3/2.

The n≤8 finite experiment checks the implementation and exhibits strict gains. The DP optimality and exact-inverse theorems hold for every admissible n.

## Next executable unit — PREFIX-506

Reduce optimal-partition preprocessing using the small slack Bb−L<b, test two-level variable boundaries and weighted row traffic, then benchmark real retained bytes and total build/rank/inverse/native-append time against PREFIX-504 on representative inputs. Also investigate whether PREFIX-500's mod-12 support description permits faster exact block-sum evaluation without enumerating all V values.

Mathematical provenance is the frozen source pin and PREFIX-500 through PREFIX-504 in `research_notes/portable_direct`. This work is independently published author-side evidence for the codec line; it does not alter the control plane's formal Result/Review/admission of the P0 X6 rotation task.
