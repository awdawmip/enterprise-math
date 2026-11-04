# PREFIX-495 — Exact BRC fiber ranking, unranking and online update cost

Date: 2026-11-05 (Asia/Shanghai).
Status: AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED.
Scientific input pin: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Predecessor: PREFIX-494 (`research_notes/portable_direct/2026-11-04_prefix494_boolean_horizon_kmp_source_minimization.md`).
Researcher-ID: `EM-DIRECT-E3682C`; activity `RA-B0F3CB0D566D0E6C9BC8E905`. Author-side independent research; no CLAIM.

## 1. Exact question and native embedding

Use the Heartbeat World X6 signed directions with sixth special-axis occupancy fixed to zero; the five remaining axes are `a/A,b/B,c/C,d/D,e/E`. This is a *restricted observer and path family inside X6*, not a new lower-dimensional native world. For a path of length n define raw nonnegative direction occupancies u_i,v_i, signed displacement y_i=u_i-v_i, pair cancellation p_i=min(u_i,v_i), and BRC readout

```
V = p_b + 2 p_d + p_e;   W = p_c + p_e;
n = sum_i (u_i+v_i).
```

The full observer also carries terminal KMP state q for gate `aab` or `aba`, and first-source tag t in {N,B,C}. All future operations under this certificate are appends of one permitted signed native primitive; declared outputs are exactly (n,y,V,W,q,t). Native path provenance, other interaction observers and physical-time/phase semantics are retained upstream if subsequently requested. The observer's append closure was established in PREFIX-493 and is independently checked here.

The problem is to give a *constructive, exact rank and unrank* for the BRC base observer, combine it injectively with the finite controller, and account for preprocessing, memory, streaming update and output recovery.

## 2. Theorem — dense exact rank for the BRC integer image at fixed length

Write L=sum_i |y_i|, m=(n-L)/2. The base observer (n,y,V,W) is realizable exactly when

```
L <= n; n-L is even;
0 <= W <= m; 0 <= V <= 2m-W.
```

This is the integer polygon P_m; it has (m+1)(3m+2)/2 points. Sufficiency follows by choosing p_e in [0,W], p_c=W-p_e, then choosing p_b,p_d with p_b+2p_d=V-p_e and p_a=m-p_b-p_c-p_d-p_e>=0; the attainable intervals of p_b+2p_d for a given remaining budget overlap consecutively as p_e runs, so precisely 0..2m-W is attained. Signs and y fix u,v from p.

Order y lexicographically as ordinary signed integers, and within each fixed y order W then V ascending. Let

```
F_0(t) = P_(t/2) when t even, 0 when t odd;
S_j(t) = sum_{u=0}^t F_j(u), S_j(-1)=0;
F_j(t) = F_(j-1)(t) + 2 S_(j-1)(t-1),  j=1..5.
```

Here F_j(t) counts completions for j remaining signed displacement coordinates, with residual cancellation budget and polygon selection. Each coordinate v contributes residual cost |v|, with one zero choice and two choices for every positive magnitude. Thus the recurrence is exact. The total number of fixed-length base fibers is A_n=F_5(n).

To rank the next coordinate v when R units remain and j signed coordinates remain *after* the current coordinate, the number of completions under earlier values is

```
B(j,R,v) =
   S_j(R+v-1)                              if v<0,
   S_j(R-1)                                if v=0,
   2*S_j(R-1)+F_j(R)-S_j(R-v)              if v>0.
```

Add B for each of the five y fields and subtract |v| from R. Now R=2m; the final within-polygon rank is

```
W(2m+1) - W(W-1)/2 + V.
```

These half-open blocks partition the full consecutive range [0,A_n). Their cumulative counts are monotone, so unrank recovers each y by binary search for the greatest v with B<=residual rank, then recovers W by binary search on the quadratic row prefix and V by subtraction. Rank and unrank are mutual inverses for every valid observation and every 0<=rank<A_n. This is a dense *base* rank (all ranks are used).

The ordinary generating function is

```
sum_{n>=0} A_n z^n = ((1+z)^2 (1+2z^2))/(1-z)^8
                    = (1+2z+3z^2+4z^3+2z^4)/(1-z)^8,
A_n = C(n+7,7)+2C(n+6,7)+3C(n+5,7)+4C(n+4,7)+2C(n+3,7)
```

with C(r,7)=0 for r<7. The identity follows by multiplying the five displacement generating functions ((1+z)/(1-z))^5 by the polygon generating function (1+2z^2)/(1-z^2)^3, or directly from the recurrence. In particular A_n=n^7/420+O(n^6).

## 3. Theorem — exact joint finite-controller code and streaming algorithm

Let k_g denote the number of reachable (q,t) Moore states: 11 for aab, 10 for aba (as independently enumerated by the source automaton). Assign a permanent injective integer code i_g(q,t) in [0,k_g), using reachable-state BFS order in the certificate. For fixed n set

```
joint_code = k_g * rank_base(n,y,V,W) + i_g(q,t).
```

Division with remainder by k_g exactly decodes both components. This is a fixed-radix *injective joint code*: a subset of the k_g*A_n code positions may be unused because control states depend on the base fiber. It occupies at most ceil(log2(k_g*A_n)) bits. The number of real joint states lies between A_n and k_g*A_n, hence this code achieves the optimal information-theoretic leading term 7 log2(n)+O(1) bits at fixed n. It is not claimed to be a dense minimal rank of the joint support.

For all lengths 0<=n<=N, precompute cumulative C(n)=sum_{h<n} A_h and encode `k_g*(C(n)+rank_base)+i_g`; binary search in the cumulative table recovers n. Its exact *code-position* bound is k_g*sum_{0<=n<=N}A_n and the information-theoretic leading term is 8 log2(N)+O(1).

Precompute F_j,S_j for j=0..5 and 0<=t<=N in O(N) exact integer operations and O(N log N) bits of auxiliary table storage. A rank query uses O(1) arithmetic operations after the table; unrank uses O(log N) comparisons via five binary searches and the polygon row search. For a native append, first decode if stored ranked, then update n,y,V,W,q,t using the PREFIX-493 exact formulas, and rerank. With the table present this requires O(log N) integer comparisons/operations on O(log N)-bit operands, rather than a full path rescan. A raw path converted from scratch requires O(n) field operations. The preprocessing table is shared across streams, and its space is counted separately. Simple elementary bit-operation upper bound is O(log^2 N) per update under schoolbook arithmetic. For N larger than the precomputed range the table must be extended.

The fixed-field baseline from PREFIX-494 for fixed n uses

```
5 ceil(log2(2n+1)) + ceil(log2(n+1))
+ ceil(log2(floor(n/2)+1)) + 4 bits
```

for signed y, V, W and a 4-bit joint control state. With n=8, the baseline bound is 36 bits and the aab rank bound is 18 bits; with n=64, 57 versus 38 bits. These are representation-length upper bounds for the stated observer, not claims of fewer instruction cycles or total-system savings. Rank uses a shared O(N log N)-bit lookup table.

## 4. Executed certificate, verified range and limitations

The attached dependency-free Node.js certificate uses only BigInt exact arithmetic. It checks (i) the closed A_n formula for every n=0..64; (ii) exhaustive all nonnegative ten-direction occupancy vectors of total length n=0..8, with exact observer-image deduplication, image cardinality and injective dense ranks; (iii) inverse rank/unrank for each such distinct image; (iv) all 11,111 ordered signed-letter words of length <=4 for each of the two gates, their native append closure, and their reversible joint finite-state code; and (v) selected rank/unrank endpoints for n=8,16,32,64. The actual execution log ends `ALL_CHECKS_PASS`.

Unbounded-length correctness is proved by the lattice decomposition and block-partition arguments above. Executed finite checks are implementation evidence within the specified bounds. The joint code is proven injective but may contain holes; dense joint-support ranking with fast streaming updates and amortized table costs is the next research question. This author's derivation has not undergone independent Driver Review or mathematical admission.

## 5. Next PREFIX-496

Compute k(n,y,V,W), the number of realizable joint (q,t) states conditional on each base fiber; derive a support-aware dense rank using cumulative k, then compare its saved bits and streaming update cost with the present fixed-radix controller. Seek a constructive family where the support-dependent improvement exceeds one bit, and quantify the cost of querying k under native append. Preserve the exact X6 embedding and source/provenance observation scope.
