# Author-side crosscheck of the v=0 cancellation layer

Checked on 2026-11-21 against the adjacent `THEOREM.md` and `derived.json`.

No error was found in the stated v=0 theorem. The dedicated checker `crosscheck.py` performs three focused checks using exact symbolic arithmetic:

1. Reconstruct the generating functions of all six residue polynomials by summing polynomial sequences in `m` with `q=6m+a`. Both resulting rational functions equal the stated C and T generating functions identically. This directly checks the quasipolynomial identities rather than relying on additional interpolation samples.
2. Compute the coefficients of the rational functions at `t=1/r` by coefficient recursion, separate from the original long-division code. All 108 coefficients (six phases, three differences, six Laurent orders) match: lower orders cancel, the constant term is -20, and the next coefficient is the table K.
3. Use exact matrix ranks and linear-system solution sets to check the fifteen phase pairs. The full coefficient has no same-parameter collisions and exactly the two independent-parameter intersections stated in the theorem. The centered quotient reproduces all its listed intersections. The first symmetric parameter-box thresholds are 48 and 39 respectively.

The common numerator rounding error has magnitude at most one; multiplying it by `(r+j)^3/C(r+j)` gives an `O(r^-2)` perturbation uniformly over the seven fixed positions. This is sufficient for the stated next-order theorem. For compact lambda intervals, the positive leading denominator and the rational expansion supply the claimed uniform remainder. The threshold statement is about next-order template sets; finite integer observations at those template intersections retain a higher-order question.

These are author-side checks by a collaborating agent, not independent project review or admission.

## Concrete general-v follow-up

The original joint leading model at E=-1 has common level

`beta(v) = -4*(v^4-122*v^3+433*v^2-189*v+5)/(1+v)^4`.

Its derivative is

`beta'(v) = -4*(126*v^3-1232*v^2+1433*v-209)/(1+v)^5`.

The numerator cubic has a root near `0.170366734476440` in (-1,1). Thus unknown v need not be determined uniquely by the leading common level on the full permitted interval. A useful precise task is to derive K_a(lambda,v) and classify phase identification using the full typed observation `(beta(v),K_a(lambda,v))`, with each rival allowed its own legal `(lambda,v)`. Distinct v candidates enter next-order comparison only on the same beta fiber. The centered quotient should be studied separately because it discards that leading scalar information.

Acceptance can be stated on boxes `|v|<=delta<1`, `|lambda|<=Lambda`: give exact/verified parameter regions of separation or explicit coefficient collisions, uniform remainder bounds, and legal integer rounding/starting-index semantics. The v=0, 48/39 result is the required recovery check.
