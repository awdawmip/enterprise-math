# PREFIX-1057 — Recentered lower spectral bridge to 1/240

Date 2026-11-24. Parent PREFIX-1056. AUTHOR_CONDITIONAL_ANALYTIC_PROOF / EXACT_RATIONAL_CHECKED / NOT_REVIEWED.

## Scope and immutable scientific dependencies

Frozen P000 V5 at f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json. Preserve Stage46 signed W=J12−6I12, incoming −e1, bidirectional exclusion of Link {0,e1}, exactly one outgoing negative step, full native Cell–terminal-port–grade, branch, sign, multiplicity and provenance. Only the inherited auxiliary scalar observer is treated; NATIVE_ATTRIBUTION_PENDING_BRC_REVALIDATION. No new native propagation or classical phase/pi computation. Mother B_fix,odd(32) in {19,20} remains open.

Read parent 32e0744bf4e46688cdb4201b329d02f6078ba50c:research_notes/portable_direct/2026-11-24_r6_prefix1056_extended_lower_band_normalized_horner.md (blob 2a034910407dd8bf23d0e63b09eea191ef88c88b) and its normalized checker db85f6a2fec6c58f9488dd50f7f548a65577d9d4:research_notes/portable_direct/PREFIX1056_R6_NORMALIZED_HORNER_CHECK.py (blob 8f1aaac8b6d24d0510f0fe85774ae49ee1a5a572). Read PREFIX-1052 at de0250c78a0952c5b282623dacedce81c47bad90 for critical matching and the ODE. Inherit PREFIX-1054's parameter boxes and earlier certified bands; inherit the PREFIX-1056 uniform scaled tail certificate |(5/2)^n b_n|<10^−18 for n>100 in each of five modes. This last deliberately loose bound is taken from the prior computed tail bounds (largest displayed 2.400199839309111e−20), not a new independent replay of the 10000-coefficient proof. The first 101 coefficients per mode are recomputed exactly here.

## Theorem

Under these inherited auxiliary-model inputs, for c>0 the positive upper-edge density coefficient,

5g(y)/c > 400 for 1/240 <= y <= 39/16.

Together with the earlier band [39/16,36), g(y)>0 for 1/240 <= y < 36. The actually traversed lower endpoint is approximately 0.004096466110682583, slightly below 1/240. This replaces the previously unresolved interval (0,399/256) by (0,1/240). The guaranteed length of the remaining gap is at most 1/240; this removes more than 99.7% of the previous gap by length. No endpoint y=0 assertion.

## Proof: preserve all signed modes and propagate a sufficient jet

Use u=rho/c and v=U/c; v'=(y−6)u. As in PREFIX-1052,

5g/c = 4H'u + 4Hu' − 2Pu + 12(11+y)v,
H=y²(36−y)², P=y(y−36)(17y−91).

On (0,4) represent u as the four analytic R_j(y−4) modes and the separately retained signed cusp (4−y)^(3/2) C_4(y−4), with weights in the exact hundredth boxes from PREFIX-1054. Integrate each mode from y=4 to obtain its primitive component; include v(4) as a sixth independent constant-mode weight. This is a linear decomposition of the actual six-component auxiliary jet (u,u',u'',u''',u'''',v); no new native projection or erasure is asserted.

At y0=39/16, X=4−y0=25/16=(5/4)^2, so derivatives of both the analytic modes (alpha=0) and cusp (alpha=3/2) are rational-term sums. Set D=100, R=5/2, q0=X/R=5/8, T=10^−18. The inherited scaled coefficient tail bound gives for derivative j=0,...,4

E_j <= T X^(alpha−j) q0^(D+1) (D+3)^j j! / (1−q0)^(j+1).

Indeed |(D+1+k+alpha)_j| <= (D+3)^j (k+1)^j, and sum_(k>=0) (k+1)^j q^k <= j!/(1−q)^(j+1). The primitive tail error is at most 6 X E_0 since 0<=x<=X and |y−6|<=6. The finite sums use exact rational coefficients and the exact rational square root 5/4; outward round only the stored interval endpoints.

For each ordinary center y_i, choose r_i=min(y_i,4−y_i)/8 and t=(y_i−y)/r_i. The next center is y_(i+1)=y_i−r_i/2. The full segment is t in [0,1/2]. Transform the inherited fifth-order polynomial differential equation sum_(j=0)^5 a_j(y) D_y^j u=0 into sum_j A_j(t) D_t^j u=0 with A_j(t)=(-r_i)^(-j) a_j(y_i−r_i t). The checker contains the exact six polynomials.

Write u=sum c_n t^n. Let L=max_j(5−j+deg A_j), and set

W_l(n)=sum_(j=0)^5 [t^(l−5+j)] A_j(t) (n−l)_j,

using zero for absent or negative polynomial coefficient indices. Comparing coefficients of t^(n−5) yields W_0(n)c_n + sum_(l=1)^L W_l(n)c_(n−l)=0 for n>=5 (omit negative indices). W_0=A_5(0)(n)_5 is nonzero at these ordinary centers. The initial c_j=(-r_i)^j u^(j)(y_i)/j! for j=0,...,4 carry the actual jet and its interval uncertainty.

## New local all-order tail certificate

Take N=120 and express W_l(N+z)=sum_(k=0)^5 w_lk z^k. After multiplying all by a common positive denominator, choose s=sign(w_05). If each s*w_0k>0 and

beta=max_(0<=k<=5) [sum_(l>=1)|w_lk|/(s*w_0k)] <1,

then for every real n>=N the triangle inequality on the polynomials with z>=0 implies sum_(l>=1)|W_l(n)|/|W_0(n)|<=beta. Thus B=max_(N−L<=n<N)|c_n| bounds all coefficients beyond N by induction. This uses ordinary centers and small relative radius; there is no need to increase the global Frobenius recurrence order as the singular endpoint is approached. The coefficientwise comparisons are exact and repeated at every center; no assertion about a uniform contraction at centers that were not tested.

For a subinterval 0<=t<=q<=1/2, derivative j tail from n>=N is bounded by

B N^j j! q^(N−j) / (r_i^j (1−q)^(j+1)).

This follows from the same geometric-moment bound. The primitive v obeys dv/dt=−r_i(y_i−6−r_i t)u, so integrating the truncated polynomial is exact up to interval endpoint rounding, and the omitted primitive tail is at most 6 r_i q B q^N/(1−q). These estimates propagate the entire five-derivative jet and primitive to the next center, rather than treating a scalar g value as a sufficient initial condition.

For all finite interval operations, use integer endpoint grids with denominator 10^70, exact rational coefficient ratios, outward floor/ceil in scaling and multiplication, and interval Horner on the normalized t coordinate. At each step divide [0,1/2] into eight equal closed subintervals, evaluate the contrast of each independent mode, then multiply by its weight box and sum. This gives coverage of every real point of the segment. At the endpoint propagate all six state entries, including the four higher derivative/primitive entries not needed to read the contrast. Coefficient intervals, analytic tail, and connection-weight uncertainty remain distinct.

## Executed evidence

The final local Python/SymPy/Fraction checker was run to its exact terminal assertions. 100 ordinary centers, 120 coefficients per mode/center, 800 closed subintervals. All coefficientwise tail tests satisfied beta<1. The exact endpoint comparison and the lower-bound comparison both passed: y_end<1/240 and min_lower>400*10^70.

Terminal output:
    98 y 0.004660868108154406 lower 2535.3823997404033 ratio 0.8016510587236154 width 2.8837839636476375e-12
    99 y 0.004369563851394755 lower 1425.785463514352 ratio 0.8016749179440912 width 4.711863956207711e-12
    100 y 0.004096466110682583 lower 419.343050077939 ratio 0.8016972834211358 width 7.699234848702072e-12
    PREFIX1057_RECENTERED_LOWER_CERTIFICATE_PASSED

Exact terminal y:
169249585838356043378989610158366330670274311887470310403098994609174960456290416621616401471328572370111942291259765625 / 41315998049390537434494706752048189989275292685267576205290549704650361952269459114074325652482205302974450751563959894016.

Displayed lower 419.343050077939 is diagnostic, not the exact assertion. Width is the maximum u interval width across independent mode states, not the physical weighted contrast width. The checker is at 45b5c2473ea65a63239d2f9c00ced6a3d7a1f0c8:research_notes/portable_direct/PREFIX1057_R6_RECENTERED_LOWER_CHECK.py, remote Git blob 4d0ab25b16d6f1fb97a47ff658f1f3194742d493 matches the locally executed blob, local SHA256 7e3324c7f8245108779596fce19f1c9dda7a0aaa6fcf16f880807d86caf72038. Full remote text readback matched. Final local stdout SHA256 f41fdd605c7fd1b14bc651d7ba1fd899d894f3834230240e110840e40ceb30dd; salient stdout and exact assertions above. No independent review.

## Failed extension and next action

An exploratory 101st step (same r, N and interval scheme) produced a lower enclosure about −492.3209, so a trial targeting y<1/256 failed. This is an enclosure failure, not evidence that g is negative. The final program certifies only the 100 completed segments. Since independent mode-state widths were still tiny at step 100, inspect the contribution of the inherited connection-weight boxes, their correlations and the interval dependency in the contrast before increasing precision or order. Use exact endpoint identities if supported by the frozen source, or tighten the connection parameter boxes with the existing exact connection machinery. The remaining bridge is (0,1/240); a previous endpoint asymptotic must be supplied with an explicit compatible remainder bound to finish it. Do not repeat the certified bands.

Control: original registration r6-20261123-2358-session-start-own-v1 SUCCEEDED; historical EM-DIRECT-780BBE / RA-0ABD84561C86E53067DB0322. Original receipt checkpoints empty. Read-only owner query r6-20261124-1550-sites-leased-observe-v1 SUCCEEDED, error=null, no LEASED tasks in fixed snapshot as_of 2026-11-24T07:52:45.458148Z, Source f4f69a9488cdf6d649f2a862548720653e1b6e6b. The Sites read is not adoption of ordinary-Chat private binding or live execution authority. No CLAIM, formal PROGRESS, or Activity mutation performed here.
