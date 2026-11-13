# S23/AV exact 79-symbol histogram and two-successor residual dynamics

Date: 2026-11-09 (Asia/Shanghai). Status: AUTHOR_SIDE / UNREVIEWED / NOT_ADMITTED.
Frozen science: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Extends: `research_notes/brc_s23_av_inverse_carry_distribution_20261109_research1/PROOF.md` at `ee984261b725af5d563cda423de5ea7abc27701c`.
Auxiliary two-point S23/AV label-1/label-4 joint-count and neutral label-3 likelihood observer. Native X6/full mother-model capacity is a separate interface.

## Exact definitions and inherited theorem

Set `r=ln(7)/ln(10/7)`, `alpha=(2074774-380295*r)/(79*r-431)`, `B=79`, `Gamma=380295+79*alpha`.
The inherited theorem establishes `1/2<alpha<2/3`, alpha irrational, and
`C_k=floor(79*{k*alpha})` for integer `k>=1`. `C_k` counts integer horizons in coarse bin k for which the candidate plateau inverse chooses its second rather than first candidate.
The exact-capacity formula `N(h)` uses additional critical-cell certificates.

## Theorem 1: exact finite prefix histogram, 79 categories

For every positive integer K and every m=1,...,78, set

`T_m(K) = sum_(k=1)^K [ floor(k*alpha+(79-m)/79) - floor(k*alpha) ]`.

Then

`T_m(K) = # {1<=k<=K : C_k>=m}`.

Writing `T_0=K, T_79=0`, the exact number of bins with `C_k=c` is

`F_c(K)=T_c(K)-T_(c+1)(K)`, for each c=0,...,78,

and the total second-candidate horizon count is
`S(K)=sum_(c=0)^78 c*F_c(K)`.

Proof: For x={k alpha} in [0,1), `floor(k alpha + (79-m)/79)-floor(k alpha)` equals 1 exactly when `x>=m/79`, equivalent to `floor(79 x)>=m`. Difference of tail counts gives the full histogram. The weighted count is its definition. QED.

**Exact computational certificate without enumerating K:** Enclose alpha by rational bounds `L<alpha<U` from the positive arctanh log expansion and explicit geometric remainder. For each shift beta=(79-m)/79 (and beta=0), compute the integer floor sums
`sum_(k=1)^K floor(k*L+beta)` and `sum_(k=1)^K floor(k*U+beta)`
with Euclid's integer floor_sum. Equality of the two total sums proves equality of *every individual floor*, because each summand is monotone in alpha and all endpoint differences are nonnegative integers. Therefore each `F_c(K)` is exact. Complexity: O(79 log Q) Euclidean steps for a rational denominator Q, conditional on a sufficient certified interval, with bit complexity retained.

For `K=10^12`, 160-term bounds certify all 79 thresholds, yielding

`S(K)=39,000,000,000,995`.

`F_0=12,658,227,832; F_1=12,658,227,844; F_39=12,658,227,849; F_77=12,658,227,850; F_78=12,658,227,864`.

Across all 79 symbols at this K, `min(F_c)=12,658,227,832`, `max(F_c)=12,658,227,869`. Exact sum `sum F_c=10^12`, weighted sum `sum c F_c=S(K)`. The executable evidence is `VERIFY_HISTOGRAM.py` and `RUN_EVIDENCE.txt`.

## Theorem 2: all-index two-successor law and residual coordinate

Let `q=floor(79 alpha)=46`, `theta=79 alpha-46` (strictly between 0 and 1), `z_k={79 k alpha}`.
For every positive integer k, the next carry symbol obeys

`C_(k+1) = (C_k + 46 + delta_k) mod 79`,

where `delta_k = floor(z_k+theta)` belongs to {0,1}.
Thus exactly two successor *possibilities* exist from each c:
`(c+46) mod79` and `(c+47) mod79`.

Proof: Put `y_k=79{k alpha}=C_k+z_k`. Rotation by alpha sends
`y_k -> (y_k+79 alpha) mod79`. Taking integer parts yields the stated rule. Since alpha is irrational, `z_k+theta != 1` and equality at the split does not arise. QED.

The needed future-observer repair coordinate is precisely the subcell phase `z_k`. Retaining only integer carry `C_k` merges two different successor branches; `(C_k,z_k)` gives a deterministic phase-aware update. This is an auxiliary arithmetic BRC provenance/observer application (`REUSE_APPLIED`), not a native-X6 dynamical law.

By irrational-rotation equidistribution, each of the 79 symbols has limiting frequency 1/79, and each of the 158 directed edges appears with limiting frequency either `(1-theta)/79` (low successor) or `theta/79` (high successor). These are all-index asymptotic statements. No Markov independence assumption is used.

## Execution/validation range

`VERIFY_HISTOGRAM.py` uses only Python standard-library Fraction, positive-series log remainder bounds, Euclidean integer floor sums, and exact integer comparison. It executes complete direct histogram comparison for 10,000 bins, independent floor-sum certification at K=10^4,10^6,10^12, and 100,000 consecutive transition checks with endpoint certification for all 100,001 symbols. All 158 allowed edges occurred in the checked prefix. The output in `RUN_EVIDENCE.txt` is a verbatim run except elapsed walltime values.

## Next research unit

Use the two-successor transition and residual-phase split to stratify the S23/AV critical-cell witness classes at candidate plateau i=412. Test whether translating a witness across a low/high successor preserves its narrow-gap coverage interval. Preserve an explicit first uncovered cell or a finite complete certificate. Separate this structural problem from the already proved carry-only formulas and retain the original exact-capacity proof standard.
