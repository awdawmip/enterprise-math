# PREFIX-504 — Exact BRC source-state ranking with sparse V-block prefixes

Date: 2026-11-05 (Asia/Shanghai). Independent author-side research, Researcher-ID EM-DIRECT-EC4A33, RA-A1EED94347FFB90FF0942874.
Frozen scientific input: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Previous interfaces: PREFIX-496 dense exact rank, PREFIX-499/500 source support, PREFIX-501/502 signed-spatial prefix, PREFIX-503 full W-prefix.
Status: AUTHOR_PROVED / EXACT_INTEGER_CHECKED (n=0..9) / UNREVIEWED / NOT_ADMITTED. No formal CLAIM, Result or Review is asserted.

## Defined model, observer, and future scope

In the declared signed native X6 model, select the ten directions a,A,b,B,c,C,d,D,e,E, keeping sixth-axis occupation zero. For a path of length n, let y be the five signed displacements and let p_i=min(n_i+,n_i-) be the exactly typed BRC cancellation count on axis i. Preserve V=p_b+2p_d+p_e, W=p_c+p_e, terminal KMP state q for the chosen gate g in {aab,aba}, and the first B/C source t in {N,B,C}. The observable is (n,y,V,W,q,t). Future operations are arbitrary native signed-letter appends, with BRC cancellation and KMP/source updates as established in the preceding exact certificates.

The safe quotient spatial key is p=(u,v,c,s)=(y_a,y_b,abs(y_c),abs(y_d)+abs(y_e)), as proved in PREFIX-501. Put m=(n-abs(u)-abs(v)-c-s)/2. Only nonnegative integral m is admissible. Let K_g(p,W,V) be the sorted set of *actually reachable* (q,t) control/source states. The PREFIX-500 exact BRC oracle returns K_g. Its weight is k_g(p,W,V)=|K_g(p,W,V)|, zero for inadmissible states. Sufficient index ranges are 0<=W<=m and 0<=V<=2m. The PREFIX-503 W-row prefix is H_p(W)=sum_{w<W}sum_{v=0}^{2m}k_g(p,w,v).

## Theorem (sparse V-block exact lexicographic codec)

For every integer n>=0, either fixed gate g in {aab,aba}, and every integer block width b>=1, there is an explicit gapless exact rank and inverse on all reachable (y,V,W,q,t) of length n, preserving the declared native appended-step update semantics, with:

- Shared spatial, W and V-block prefix index size O((n+1)^5+(n+1)^6/b) integer words, excluding the independent constant-dimensional BRC oracle.
- Full prefix construction cost O((n+1)^6) oracle evaluations and integer prefix operations.
- Rank and inverse each need at most min(b,n+1) source-support oracle evaluations, and O(log(n+2)) additional prefix comparisons; integer arithmetic magnitudes have O(log(n+2)) bits under the bounded-length observer.
- Exact payload width ceil(log2 S_g(n)) bits where S_g(n) is the number of reachable complete joint states (zero bits for S_g(n)=1).

### Construction and proof

For each spatial key p and W row, set L=2m+1. Define, for j=0,...,ceil(L/b):

    P_{p,W}[j] = sum_{0<=v<min(j*b,L)} k_g(p,W,v).

The first entry is 0 and the last entry is H_p(W+1)-H_p(W). Store P for each row in addition to the PREFIX-502/503 spatial and W index. Given a reachable state at V, take j=floor(V/b). Its zero-based lexicographic rank is

    R = signed_spatial_prefix
      + H_p(W)
      + P_{p,W}[j]
      + sum_{j*b<=v<V} k_g(p,W,v)
      + ord_{K_g(p,W,V)}(q,t).

These five terms count, respectively, every predecessor with an earlier signed displacement; an earlier W; an earlier complete V block; an earlier V within the selected block; and an earlier control pair at this V. They are pairwise disjoint and exhaust the predecessor set. Therefore the expression is the exact lexicographic index with no gaps.

For inversion, first remove the inherited spatial prefix and W prefix using their proved inverses. The row residual r satisfies 0<=r<P[last]. Select the *largest* j with P[j]<=r via upper-bound binary search. This choice handles zero-weight blocks and duplicated prefix values: the terminal sentinel cannot be selected because r<P[last]. Subtract P[j], then scan the at most b values in [jb,min((j+1)b,L)), subtracting their exact k_g weights until the residual lies inside one nonempty control set; select the corresponding ordered control pair. This exactly inverts the rank formula, including all zero-weight rows and the n=0 boundary.

There are O((n+1)^4) quotient spatial keys and O(n+1) W rows per spatial key. Each row holds ceil((2m+1)/b)+1 words. Therefore total index storage is O((n+1)^5+(n+1)^6/b). Every row element is visited only once in construction, for O((n+1)^6) oracle evaluations. A rank or inverse scans at most min(b,n+1) V values. The PREFIX-502 spatial, PREFIX-503 W, and new block inverses use only O(log(n+2)) prefix comparisons. Exactness of native update then follows from computing the proven BRC/KMP/source next state and invoking this bijection for length n+1. QED.

### Consequences

Block width b=1 yields O(n^6) words and at most one online support query. b>=n+1 yields O(n^5) words and O(n) online queries (equivalent online complexity to PREFIX-503, with a redundant row sentinel). b=ceil(sqrt(n+1)) yields O(n^(11/2)) words and O(sqrt n) online support work. More generally b≈n^alpha for 0<=alpha<=1 gives O(n^(6-alpha)+n^5) shared words and O(n^alpha) online support calls. All formulas are integer-operation bounds; concrete bit costs, Python object overhead, and input-path decoding costs are separately accounted for in deployment.

## Exact certificate and observed results

Run Python 3 standard-library source prefix504_blocked_vprefix_certificate.py. For each g in {aab,aba} and each n=0,...,9, the program builds the complete reachable joint-state set through the exact native ten-direction recurrence, derives the BRC support lookup, builds PREFIX-503 spatial/W tables and the new block tables, and checks EVERY state against independently sorted state order in both directions (rank and inverse). Block widths checked are {1,2,3,4,8,n+1}. Each block-prefix total must equal the independent W-row total, and measured online oracle calls must not exceed b. Result: ALL_CHECKS_PASS.

At n=9: 43,054 BRC base observation fibers; 127,403 full joint states for aab, 127,298 for aba; 1,210 quotient spatial keys. Both gates have the following shared integer-word counts and maximal rank/inverse support calls:

| b | index words | extra V-prefix words | max rank calls | max inverse calls |
|---:|---:|---:|---:|---:|
| 1 | 19,644 | 8,428 | 1 | 1 |
| 2 | 17,432 | 6,216 | 2 | 2 |
| 3 | 16,070 | 4,854 | 3 | 3 |
| 4 | 15,894 | 4,678 | 4 | 4 |
| 8 | 15,250 | 4,034 | 8 | 8 |
| 10 | 15,220 | 4,004 | 9 | 9 |

Inherited PREFIX-503 prefix index alone: 11,216 integer words at n=9. These are abstract indexed integer cells, not resident memory bytes, and exclude the test harness's exhaustive K table. Timings in the exact execution JSON are host diagnostics rather than a validated speed-up claim. The harness uses a lookup-backed exact native BRC oracle to validate the codec; production should use the existing PREFIX-500 mod-12 support oracle.

The analytic theorem holds for all nonnegative n; exhaustive computational confirmation covers n<=9. The observer is the declared five-axis X6 subfamily with BRC cancellation/KMP/source; this is not an attempted proof of full six-axis rotation dynamics or physical heartbeat propagation.

## Next research unit — PREFIX-505

Investigate an adaptive per-row block width that minimizes real rank/unrank latency for a fixed memory budget, and compare it with a two-level V-prefix index. A distinct derivation route sums PREFIX-500's mod-12 Presburger support formula across complete V blocks, potentially reducing the present O(n^6) preprocessing oracle evaluations. Preserve actual construction work, byte-accurate memory, rank/inverse latency, and native-append updates in the comparison.

Scientific facts remain pinned to the frozen input. Current normative governance was independently read from canonical GLOBAL_KNOWLEDGE_V1 and Enterprise Math current portable research protocol; the proof does not modify P000/ACTIVE worldview or claim mathematical admission.
