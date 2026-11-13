# R5: exact cold-start subset recurrence and linear midpoint dynamic programming

Date: 2026-11-13. Author-side mathematical and algorithmic work. The frozen scientific source is awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551, unchanged. Extends Draft PR #2293. Native P000, six-axis observer contracts, Task ownership, Result and review are unchanged.

## Theorem A — exact construction of frozen event boundaries

Let M be a nonempty subset of the fifteen frozen labeled atoms. Define n(M)=-sum_{i in M} w_i and k(M)=-sum_{i in M} k_i. For any selected bit b in M:

\[
n(M)=n(M\setminus\{b\})-w_b,\qquad
k(M)=k(M\setminus\{b\})-k_b.
\]

Using a lowest-set-bit recurrence calculates all subset values with O(2^15) integer additions, rather than recomputing up to fifteen contributions per mask. Keep the predecessor's exact eligibility rule n>=3, 36 divides k and q=k/36 belongs to {3,12,15}; deduplicate n within each q family.

Every selected pair n>0,q>0 contributes a rational activation wall

\[
t(n,q)=\frac{1-36q/n}{23}=\frac{1-36/(n/q)}{23}.
\]

For 0<a<b, the strict inequality 1/a>1/b implies t(a)<t(b). Thus sorting exact positive rational keys n/q produces exactly the same wall order and equality classes as sorting t(n,q). A Counter on these ratios retains wall multiplicities. The event-building stage costs O(2^15+U log U) exact arithmetic/comparisons for U selected pairs, with the usual separate arbitrary-precision bit complexity. The frozen instance yields 953 distinct walls with multiplicities 869 x 1, 56 x 2, 28 x 3; its cumulative event array has length 954 and ends at 1,065.

## Theorem B — O(N min(N,2R+1)) exact lexicographic radius DP

Let x_0<...<x_{N-1} be strictly increasing integer event coordinates, R>=0 an integer, and sampling centers belong to the input indices. For a set S of centers, first minimize |S| and then J(S)=sum_b min_{p in S}|x_b-x_p|, subject to maximum distance no greater than R. We also require the exact number of optimal sets and the lexicographically first optimum.

For two consecutive selected centers p<q define

\[
m(p,q)=\min(\{b:p<b\le q,\ 2x_b>x_p+x_q\}\cup\{q+1\}).
\]

Let P_j=sum_{b<j}x_b. The exact arc cost is

\[
w(p,q)=
(P_m-P_{p+1})-(m-p-1)x_p
+(q-m+1)x_q-(P_{q+1}-P_m).
\]

Proof: boundaries between p and q are nearest to either p or q. The strict midpoint test assigns ties to p, which does not change the cost. The first term is the sum of x_b-x_p for p<b<m; the second is the sum of x_q-x_b for m<=b<=q.

At fixed p, increasing q only increases x_p+x_q; hence m(p,q) never decreases. A moving midpoint pointer requires at most one increment per traversed boundary. The radius coverage edge restriction from PR #2293 is q-p<=2R+1 (for strictly increasing integer x). Hence all p's arcs take O(min(N,2R+1)) arithmetic per p; the boundary-coverage endpoints L(p),U(p) are monotone and admit O(N) two-pointer construction. The old reverse-DAG lexicographic recurrence, tied optimal count and earliest successor are unchanged because all arc costs are identical.

Therefore time is O(N min(N,2R+1)) arithmetic operations and O(N) state words, excluding arbitrary-precision integer bit costs and construction of the original scientific input. For R=0 every boundary is a center.

## Executed verification

The companion VERIFY_LINEAR_FRONTIER.py provides the predecessor and optimized event builders and two DPs, runs exhaustive small tests and compares all thirty-seven original R5 radius results. Python standard library only; all mathematical decisions use integer or Fraction arithmetic, never floating point. The committed program's exact Git blob was checked against the locally executed program.

**Direct finite exhaustive verification:** 6,558 (sequence, radius) instances with length 1 through 7, increments {1,2,3}, radii 0 through 5; 361,414 candidate center subsets. All optimized results matched direct exhaustive enumeration and the original binary-search DP in (K,J), optimal-set count and first optimal center set.

**Frozen model verification:** both event generators reconstructed the same exact 954 integer event-boundary coordinates (ending at 1,065). The original 56-byte sampling-center encoding was checked by SHA-256 and returned (R,J)=(2,1070). The old and new DP outputs matched on every radius 0 through 36, including precise optimal counts and earliest center-index lists.

Selected exact outputs:

| R | K | J | Number of tied optimum sets |
|---:|---:|---:|---:|
| 2 | 213 | 1070 | 1338767625695954932334592000 |
| 9 | 57 | 4384 | 6350400 |
| 25 | 21 | 12146 | 140 |
| 26 | 21 | 12050 | 12320 |
| 36 | 15 | 16813 | 430 |

## Observed CPython timing

Warm alternated single-process median elapsed times in milliseconds. Event-build and event-build+DP: eleven repetitions each; DP alone: nine repetitions each. Both alternatives compute/check their results on every iteration. Results depend on machine and runtime; this is an algorithmic-subpipeline benchmark, not an independent-process RSS assessment.

| Component | R | Predecessor (ms) | New method (ms) | Relative acceleration |
|---|---:|---:|---:|---:|
| Frozen event construction | — | 69.66328 | 8.55719 | 8.14x |
| DP only | 2 | 2.48746 | 2.36540 | 1.05x |
| DP only | 9 | 8.53323 | 7.56888 | 1.13x |
| DP only | 36 | 30.52298 | 27.71729 | 1.10x |
| Event construction + DP | 2 | 71.86440 | 11.04983 | 6.50x |
| Event construction + DP | 9 | 78.80016 | 15.99595 | 4.93x |
| Event construction + DP | 36 | 101.13489 | 35.33066 | 2.86x |

The large practical speed gain comes mainly from the exact one-bit subset recurrence. The midpoint scan also improves the asymptotic DP bound, with a smaller constant-size gain on the frozen instance. Timing excludes interpreter startup, disk input, complete 28-coordinate prefix-index construction, all prefix queries, and output serialization.

## Interpretation, authority and next work

This is a scoped exact optimization of the ordered threshold/certificate selection observer. It does not identify distinct full signed X6 relational states; source/branch residuals and P000 survive. The actual formal R5 Task-ID/active CLAIM remains to be resolved from its current exact publication and canonical owner state; publication of this proof is neither CLAIM nor formal Result.

Next useful test: integrate the already archived 12/17/33/35/56-byte center codecs and 28-coordinate original prefix-query index into a fresh independent-process harness; compare full query output, cold-start RSS, peak memory, rebuild cost and batch throughput. Reuse the current frozen pin and already validated 954-boundary/1,065-event frontier.
