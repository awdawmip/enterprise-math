# R78 — Constant-event-count exact latest-source oracle without critical-cell enumeration

Date: 2026-11-11. Author-side continuation of R77 (`ef4ea3a6fa1fd2e8ae8cb9cc3abe973d7165f1a4`), preserving frozen S23/AV scientific input `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Auxiliary rational circular-source model; original source identities `(t,branch)` and lexicographic branch tie rule retained. No new native X6 interpretation is asserted.

## Domain

Take a finite collection `E` of distinct event identities `(t,branch)` with integer times and totally ordered branch labels. Observation time `j`, original boundary labels `a,b` and rational observation phase `x` are fixed. The parameter runs over a nonempty rational closed interval `I=[L,U]`.

Assume the integer floors `k_a=floor(a theta)` and `k_b=floor(b theta)` are *constant on I*, and the original-label arc is stably nonwrapping: `0 <= A(theta)=a theta-k_a < B(theta)=b theta-k_b < 1` on I. These hypotheses can be established by testing both rational endpoints. The oriented half-open arc is `[A,B)`, with lower endpoint included and upper excluded. Let `P_e(theta)` mean `{x+(t-j)theta} in [A(theta),B(theta))`, and let `W(theta)` be the greatest qualifying `(t,branch)` or `NONE` if no source qualifies.

## Lemma 1 — reduce fractional-circle membership to one affine fractional part

For each event `e=(t,branch)` define

`F_e(theta) = x+(t-j-a)theta+k_a`, `w(theta) = B(theta)-A(theta)`.

Then `0<w(theta)<1` throughout I and

`P_e(theta) <=> {F_e(theta)} < w(theta)`.

Proof. Writing the source fractional part as `S`, the affine lift `x+(t-j)theta - A(theta)` equals an integer plus `S-A`. If `S>=A`, its fractional part is `S-A`; membership is exactly `S-A<B-A`. If `S<A`, its fractional part is `1+S-A`, which is larger than or equal to `1-A>B-A`. Thus the equivalence holds even at the half-open endpoints.

## Theorem 2 — two endpoint tests plus one integer crossing are complete

Let `f_-=min(F_e(L),F_e(U))`, `f_+=max(F_e(L),F_e(U))`, and `w_max=max(w(L),w(U))<1`. Write `P_L=P_e(L)`, `P_U=P_e(U)`. The following are exact equivalences over **all real theta in I**:

**(IN)** `exists theta in I: P_e(theta)` if and only if

`P_L or P_U or ceil(f_-) <= floor(f_+)`.

**(OUT)** `exists theta in I: not P_e(theta)` if and only if

`not P_L or not P_U or floor(f_-)+1 <= f_+`.

Both statements have rational witnesses computable with a bounded number of rational operations, irrespective of how many times the source phase wraps around the circle.

Proof of IN. If `F_e(I)` contains an integer `k`, the unique parameter with `F_e(theta)=k` is IN because the fractional part vanishes and `w>0`. If there is no integer in the closed image interval, its image lies wholly in a single open unit cell `(k,k+1)`; there `{F_e}=F_e-k` is affine. Then `F_e-k-w` is affine and strictly negative at an interior parameter only if it is strictly negative at some endpoint. This proves the stated criterion. An interior integer crossing witness is `(k-x-k_a)/(t-j-a)` for `k=ceil(f_-)`; division is only used when the slope is nonzero.

Proof of OUT. If `F_e(I)` contains an integer `k` strictly above `f_-`, it contains noninteger values immediately below `k`. Their fractional parts approach `1`, whereas `w<=w_max<1`, so an OUT point exists. Specifically choose `delta=(1-w_max)/2`, `z=(max(f_-,k-delta)+k)/2`. Then `f_-<z<k<=f_+` and `{z}>w_max`; set `theta=(z-x-k_a)/(t-j-a)`. If no integer lies in `(f_-,f_+]`, the image is contained in `[k,k+1)` for one integer k (also when `f_-` itself is an integer). Hence `{F_e}=F_e-k` is affine and `F_e-k-w` is affine; an OUT point (`>=0`) then exists if and only if an endpoint is OUT. This also handles the degenerate interval `L=U` and constant F.

The two predicates determine three disjoint outcomes for each event: `ALWAYS_OUT` if IN is false, `ALWAYS_IN` if OUT is false, and `MIXED` otherwise. Strict/open endpoint handling is exact.

## Theorem 3 — latest-source classification without enumerating critical cells

Scan source identities in *decreasing* lexicographic order. For each, evaluate Theorem 2. Discard an event only after proving `ALWAYS_OUT`. Let `e*` be the first event admitting any IN parameter.

* If no `e*` exists, `W(theta)=NONE` for every theta (`STABLE_NONE`).
* If `e*` is `ALWAYS_IN`, then `W(theta)=e*` for every theta (`STABLE(e*)`).
* If `e*` is `MIXED`, use the two rational witnesses from Theorem 2. At the IN witness `W=e*`. At the OUT witness `W<e*` or `NONE`. Hence the exact answer is `CHANGES(e*,theta_in,W(theta_out),theta_out)`.

Proof. Every identity preceding `e*` in the total order was proved absent at *all* parameters, so none can defeat `e*` at its IN witness or at any parameter where `e*` qualifies. All remaining identities are strictly smaller. The three cases follow directly and exhaust all possibilities.

An implementation may use the R76 persistent ordered source index for descending traversal. With an already maintained event order, at most `|E|` event examinations are required, each with a constant number of exact rational comparisons and additions/multiplications/divisions. No operation scales with the number of distinct source-phase wraps or with the size of the R77 explicit cell list. This is an *arithmetic operation count*, not a uniform bit-time bound: operand lengths, persistent-index maintenance and the actual output witness size still matter. Sorting identities from scratch costs `O(n log n)` comparisons. The theorem is an efficient complete decision for the declared stable nonwrapping arc; R77's explicit stratification remains valid for parameter intervals with changing original labels or wrapping arcs. Such a general interval can first be cut by the original-label changes alone, before applying this oracle, leaving a separate future problem of compressed global output across many boundary changes.

## Reproducible independent verification

`check_r78.py` runs Python `fractions.Fraction` throughout. Its independent reference enumerates the full R77 critical-point strata, evaluates every rational critical singleton and open-cell midpoint, and tests additional interior rational points. Random seed: `781126`.

Local run: 256 valid randomly generated stable-arc models, 2,024 reference strata, 1,768 additional exact rational comparisons; reference classifications `STABLE_NONE=71`, `STABLE=50`, `CHANGES=135`, all matching this oracle. Single-source oscillation-family explicit-cell counts for `t=24,48,96,192,384,768` were `13,25,49,97,193,385`, whereas the oracle examines exactly one source. Very large exact t values `12*10^6` through `12*10^120` (up to 403 bits) produced directly verified rational IN/OUT witnesses. An indicative, unreplicated same-process Python comparison is in `verification.json` and is not a platform-independent benchmark. Full source and results are immutable evidence for author checking, independent mathematical review pending.

## Next unit (R79)

1. Extend the constant-event criterion to each maximal original-label stable interval and develop a compressed description of cross-boundary latest-source changes without enumerating every label change when label magnitudes are huge.
2. Incorporate the endpoint/crossing oracle into the R76 maintained AVL maxima index, measure bit operations, branch insertion/deletion amortization, historical version memory and the R75 heap rebuild crossover on equal complete-output workloads.
3. Consider observer-dependent `x(theta)` that is piecewise affine and explicit interval-width constraints; carry provenance and branch identities through all changes. Preserve P000 and the task's frozen science pin.
