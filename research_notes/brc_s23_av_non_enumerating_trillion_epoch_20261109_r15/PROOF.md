# Certified non-enumerating Farey-epoch risk sweep to a trillion steps

Date: 2026-11-09. Status: author-side mathematical theorem, exact finite certificate, independent review pending.
Frozen scientific source: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Immediate predecessor: `research_notes/brc_s23_av_farey_epoch_rank_select_20261109_r14/PROOF.md` at `a4d8ecd5fce5d0e91915b5a044284abd979eae6b`.
Observer: S23/AV auxiliary 79-bin irrational-circle rotation; this is an auxiliary typed BRC-labelled phase/gap model.

## Question and theorem

Let `0<theta<1` be irrational, `m>=2`, and `t_i={i theta}`. The first `m` labelled points partition the circle into historical arcs `I=[t_p,t_q)`, with `p,q<m` consecutive in clockwise order; p is included and q excluded. For `n=m+L`, let `M(I;n)` be the largest clockwise gap among the first n phase points lying in I, and define the uniform-phase optimal whole-future error risk

`R_theta(m,L) = 1 - sum_{I} M(I;m+L)`.

**Theorem (floor-sum rank/select event sweep).** Given a rationally certified interval `lo<theta<hi` whose relevant Farey neighbours, historical order and candidate max-gap decisions are invariant across it, every maximal constant-risk block through `n<=N` can be constructed without enumerating the `N` phase indices. Within each Farey epoch with lower/upper neighbours `a/b<theta<c/d`, all risk changes are among at most `3m` event positions. Their locations are found using two integer floor-sum binary searches per historical arc (one for the first qualifying index >=d, one for the last qualifying index <d). The aggregate risk is updated from the affected arc's old and new maximal affine gaps at each event. The result is a complete disjoint block covering, with an exact affine value `A+B theta` for every block.

**Proof.** The three-gap successor law from the predecessor gives the three possible lengths and starting-index ranges

`U=b theta-a` on `[0,n-b)`; `V=c-d theta` on `[d,n)`; `W=U+V` on `[n-b,d)`.

Write `S_I={i>=0:t_i in I}`. Because the first m phase points are the historical arc endpoints, the least member of `S_I` equals **p** itself: every earlier index `i<p` is a different historical endpoint and hence belongs to its own arc. Set `v_I=min(S_I intersect [d,infinity))` when relevant, and `w_I=max(S_I intersect [0,d))` when present. Therefore

`U present iff n >= b+p+1`;
`V present iff n >= v_I+1`;
`W present iff w_I exists and n <= b+w_I`.

Thus each labelled arc changes its three-type presence at no more than three thresholds. The index count for a historical arc in any integer range `[A,B]` is exactly

`C_I(A,B)=sum_{i=A}^B[floor((i-p)theta)-floor((i-q)theta)+floor(p theta)-floor(q theta)+wrap(p,q)]`,

where `wrap(p,q)=1` if `t_p>t_q`, otherwise zero. This follows by the usual indicator identity for a half-open circle arc and the floor/fractional-part decomposition. Every count is a difference of four Euclidean floor sums evaluated in `O(log Q)` quotient steps for a rational endpoint with denominator Q. Binary search using `C_I(d,x)>0` finds `v_I`; binary search using `C_I(x,d-1)>0` finds `w_I`. Event presence and selected longest-gap comparisons are certified at BOTH rational endpoints. Throughout an epoch, U,V,W are constant affine expressions. Changing only the relevant labelled arc's maximum updates `1-sum_I M(I;n)` exactly. At epoch boundaries the Farey neighbours are recomputed and the m arc maxima initialized; equal adjacent blocks are merged. The integer interval `[m,N]` is exhausted by consecutive epochs `[max(b,d)+1,b+d]` and the event partitions. QED.

For `E` epochs, `B` output blocks and `m` historical arcs, the implementation requires `O(E*m*log N*log Q + E*m*log m + B + E*log N)` integer arithmetic/compare operations after `O(m log m)` initial sorting, and `O(m+B)` memory including output. Actual bit complexity depends on the rational enclosure and the sizes of intermediate floor sums. The number E is input-dependent, and no uniform `O(log N)` epoch bound is claimed for arbitrary irrational theta. Storage of the entire labelled phase-index sequence is avoided.

## Frozen S23/AV certificate

Use `m=128`, `theta=79*alpha-46`, `alpha=(2074774-380295*r)/(79*r-431)`, `r=ln(7)/ln(10/7)`. The verifier contains a 160-term rational log-series certificate proving

`262204504569236716045286 / 10^24 < theta < 262204504569236716045287 / 10^24`.

For the COMPLETE integer interval `0<=L<=10^12` (`128<=n<=1000000000128`), the non-enumerating rank/select sweep certifies:

* 78 Farey epochs; 19,072 distinct candidate threshold positions (sum within epochs);
* exactly 9,698 maximal constant-risk blocks, all consecutive and with strictly positive risk jumps at both enclosure endpoints;
* endpoint `R(128,10^12)=-4017401528447+15321634290944 theta`, approximately `0.9999999998129876622606865` when theta is independently evaluated at high precision;
* first strict increase beyond `L=2,000,000` is `L=2,843,577`, with exact jump `455482-1737125 theta>0`, yielding `R(128,2843577)=-20701509+78951771 theta`. The preceding value `R(128,L)=-21156991+80688896 theta` holds for all integer `2000000<=L<=2843576`.

All 3,426 predecessor blocks through two million were matched row-by-row (accounting for the n-versus-L coordinate) with the previously published standalone 2M TSV. A separate direct Farey/Euclidean floor-sum evaluator was applied to 175 selected horizons including deterministic random choices, threshold neighbours and the trillion endpoint; all affine pairs matched. Direct 1T evaluation and full block generator independently agree with the predecessor's exact endpoint result.

Executable code: `VERIFY_FAST_1T.py`, which writes `n_start,n_end,A,B` TSV; extended independent direct-query validation and a longer instrumented rank/select implementation are retained as accompanying run evidence. The complete 1T TSV has SHA-256 `82a0ffdc13e5743cec32eec6985b3e31ae9cf30b8233de7aa04e1755f141245d`, and exactly 9,699 lines including header. The compact output corresponds row-for-row to the independently generated local `start_L,end_L,A,B` table (SHA-256 `85f950419ffe8a8a9480135800640dfb73684c308c26438b1ac35d0f09d6371e`).

## Scope and remaining work

The mathematical event threshold identity holds for every irrational 0<theta<1 and m>=2. The trillion-step certificate uses the specified S23/AV theta, fixed 128-step history, the certified enclosure, and the exact finite domain. This is author-side proof and integer arithmetic evidence pending independent mathematical review. The BRC carrier is the labelled residual-phase arc and type-specific gap provenance; no native X6 dynamics correspondence is claimed. Compute bit-complexity benchmarks for near-rational slopes, minimize the output event encoding, and determine whether epoch transitions can be updated without reinitializing all m arcs. The 413th S23/AV geometric capacity plateau remains a distinct branch.
