# 稀疏谐和包络的端点求和：严格区间实现与十亿点单元

Date: 2026-11-23 (Asia/Hong_Kong).  
Status: author derivation of a certified implementation; no independent Project Review.  
Continuation provenance: EM-DIRECT-B5750A / TASK_RESEARCH, science freeze `9fc068244e4f1117f1e75df5eb0285c6697d21d7`.

## 1. What is new

The preceding batch proved six harmonic moment formulas but its actual adaptive computation still built all harmonic values through B and scanned each integer inside each cell. This continuation implements the endpoint formulas with certified nonsequential harmonic evaluation and binary sign-boundary location. It reuses the exact 1,270-point observation table; it never loads the full arithmetic road or generates new D, q or thickness parameters.

The native P000 / Heartbeat X6 basis and full integer population remain unchanged. These algorithms evaluate the auxiliary scalar observer indexed by the fixed native-axis path `c_*+nE_1`. Replacing an exact finite sum by its exact endpoint identity preserves that sum; it does not remove integer or composite states.

## 2. Finite harmonic enclosures without a full prefix

Fix an integer anchor m and a positive integer p. The implementation uses m=256 and p=24, accumulating exactly outward-rounded sums only up to m. Let B_k be the rational Bernoulli numbers and

\[
V_{2p}=\sum_{k=0}^{2p}\binom{2p}{k}|B_k|.
\]

The Bernoulli polynomial formula gives `|B_(2p)(t)|<=V_(2p)` for `0<=t<=1`; no numerical bound on a periodic polynomial is assumed. For n>m, finite Euler--Maclaurin applied to 1/x gives

\[
\begin{aligned}
H_n={}&H_m+\log(n/m)+\frac1{2n}-\frac1{2m}\\
&+\sum_{j=1}^{p}\frac{B_{2j}}{2j}
  (m^{-2j}-n^{-2j})+R_1,\\
|R_1|\le{}&\frac{V_{2p}}{2p}(m^{-2p}-n^{-2p}).
\end{aligned}
\tag{1}
\]

Likewise, for `H_n^(2)=sum_(j<=n)1/j²`,

\[
\begin{aligned}
H_n^{(2)}={}&H_m^{(2)}+\frac1m-\frac1n
+\frac1{2n^2}-\frac1{2m^2}\\
&+\sum_{j=1}^{p}B_{2j}(m^{-2j-1}-n^{-2j-1})+R_2,\\
|R_2|\le{}&V_{2p}(m^{-2p-1}-n^{-2p-1}).
\end{aligned}
\tag{2}
\]

For completeness, the finite formula with all j<=p boundary terms has remainder
`-integral B_(2p)({x}) f^(2p)(x)/(2p)! dx` up to the immaterial sign convention. The absolute bounds follow by integrating `(2p)! x^(-2p-1)` or `(2p+1)! x^(-2p-2)`. The finite Euler--Maclaurin formula is given in [NIST DLMF 2.10.1](https://dlmf.nist.gov/2.10.E1); the polynomial identity is [DLMF 24.2.5](https://dlmf.nist.gov/24.2.E5). The displayed bounds are deliberately elementary rational bounds derived here from these exact formulas.

The selected m,p give uniform analytic remainders less than `1.712e-92` and `3.209e-93`, respectively. All subsequent rounding is separately outward at denominator 10^80.

### Logarithms also have rational certified remainders

Write n=2^k u with `1<=u<2` and `z=(u-1)/(u+1)`, so `0<=z<=1/3`. For K>=1,

\[
0\le\log u-2\sum_{j=0}^{K-1}\frac{z^{2j+1}}{2j+1}
\le\frac{2z^{2K+1}}{(2K+1)(1-z^2)}.
\tag{3}
\]

This follows by summing the positive tail of the integrated geometric series. The same formula at z=1/3 encloses log2. The implementation uses K=100 and integer interval arithmetic for both the polynomial and tail. No floating-point rounding decision enters the certificate.

## 3. Sign support and energy use only endpoint queries

On a sample cell `[L,R]`, both the upper and lower envelopes have the form

\[
W(n)=an+b-cnH_n.
\tag{4}
\]

The interval a,b come from the true certified sample intervals and the harmonic-potential endpoints. The exact finite difference is

\[
W(n+1)-W(n)=a-c(H_n+1).
\tag{5}
\]

For c>0, the differences strictly decrease. A binary search locates a peak; two monotone binary searches locate the unique possibly empty positive integer segment. For c<0, apply the same search to -W; its positive segment is W's negative segment, so W's positive support lies in the complementary two tails. Exact zeros contribute zero energy. The implementation requires each comparison to be certified by its interval; an unresolved sign produces an explicit error, never a numerical tolerance decision. All comparisons in the reported finite runs were decided.

With `H=H_N`, `H2=H_N^(2)`, the six exact prefix moments are

\[
S_0=N,\quad S_1=H,\quad S_2=H2,
\]

\[
T_0=(N+1)H-N,\quad
T_1=(H^2+H2)/2,\quad
T_2=(N+1)H^2-(2N+1)H+2N.
\tag{6}
\]

These are the sums of 1, 1/n, 1/n², H_n, H_n/n, H_n². Their identities can be checked by first differences and zero initial values; the prior batch supplied that all-parameter argument and rational finite check. For a positive segment `[u,v]`, using the difference of the six prefixes,

\[
\sum_{n=u}^{v}\frac{W(n)^2}{n^2}
=a^2\Delta S_0+b^2\Delta S_2+c^2\Delta T_2
+2ab\Delta S_1-2ac\Delta T_0-2bc\Delta T_1.
\tag{7}
\]

This implementation newly connects (1)--(3), the sign searches, and (7). Each cell's strict interior is evaluated through (7), then its right sample is counted once; the first window endpoint is counted separately. Thus the result covers the entire closed window with no doubled endpoints.

For K cells, the structural work is O(K log B) harmonic evaluations and O(K) moment combinations when the requested interval precision resolves the comparisons. This is an evaluation-count statement. Bit cost, the precision needed after large-term cancellation, unresolved near-zero signs for other inputs, and the cost of generating the q samples remain separate. The fixed 80-digit implementation is certified for the reported finite data, not an arbitrary-magnitude fixed-precision theorem.

## 4. Actual road: same bounds, independently aggregated

Input: the already Source-published sparse observation table in `rh_adaptive_sampling_20261122_b5750a/rh_partial_frontier_20261122/sparse_sample_observations.json`, commit `c0a6ba0f7647761f5f0a018bdf03c84714149b00`. All 1,270 point values, the same final partition, upper source constant `1+1/(2*1024²)+10^-6`, and lower source constant -12 are retained.

The new implementation certifies

\[
\begin{aligned}
0.00339846140820011534999786786637322
&\le \|L_+\|_w^2,\\
\|U_+\|_w^2
&\le0.00349839766509688830248032936050626.
\end{aligned}
\]

These are the same mathematical envelope energies as the previous batch, with new outward interval enclosures. They are not a newly improved arithmetic energy bound.

The endpoint method used 13,966 distinct harmonic arguments and 2,569 moment arguments; its measured energy-evaluation time was 10.023 seconds. A separate direct construction accumulated all H_n and H_n^(2) through B=32768, checked 1,271 harmonic endpoints, and scanned 63,490 integer values for upper/lower energies in 0.907 seconds. Both resulting intervals intersect the new enclosures and the original certificates. For this small, densely partitioned window, direct scanning is faster and gives narrower intervals. The endpoint path is useful for long cells, where it avoids work proportional to the gap length.

Timing is one run in this workspace, including the operations described, with no claim of a cross-machine performance constant. The optional scan is only the validation baseline; the endpoint path itself never builds a B-length array or reads the full road.

## 5. A cell with 999,999,999 interior integers

Take `L=10^12`, `R=L+10^9`, zero endpoint samples and c=1. Then the exact positive envelope is

\[
W(n)=I_{[L,R]}(nH_n)-nH_n=G_{[L,R]}(1/n)>0
\quad(L<n<R).
\]

The implementation evaluates all of its weighted energy using 90 distinct harmonic arguments, taking 0.0906 seconds in the recorded run:

\[
\boxed{
0.00000831668958924935368267816292865
\le\sum_{L<n<R}\frac{W(n)^2}{n^2}
\le0.00000831668958924935368267816292866.
}
\tag{8}
\]

An independent elementary check follows from the positive Green operator and `1/R<=1/n<=1/L`:

\[
\frac{h^5-h}{120R^4}
\le\sum\frac{W(n)^2}{n^2}
\le\frac{h^5-h}{120L^4},\qquad h=R-L.
\tag{9}
\]

The interval (8) lies inside (9). This synthetic cell tests the summation algorithm and declared source class; it is not a computation of the actual arithmetic q at 10^12.

## 6. Reproduction and continuation

`certify_fast_harmonic_energy.py --input <sparse_sample_observations.json> --old-certificate <sparse_curvature_envelope_certificate.json>` runs the endpoint-only check. `--scan-check` adds the small-window independent scan. Results are in `fast_harmonic_energy_certificate.json`.

The next arithmetic bottleneck remains the paired prefix evaluation needed to obtain q(n). The present result makes the downstream energy summation depend on sampled cell count and certified endpoint functions rather than the full integer count. The whole-window allocation theorem in the sibling contribution separately controls how many q samples suffice.
