# Author cross-check: endpoint harmonic evaluation and global allocation

Date: 2026-11-23 (Asia/Hong_Kong).  
Scope: targeted reading of `proof.md`, `certify_fast_harmonic_energy.py`, the existing `fast_harmonic_energy_certificate.json`, and the discrete-convexity argument in `../skeleton/proof.md`. This is a same-work author cross-check, not independent Project Review. The already completed full finite run was not repeated.

## 1. Finite Euler–Maclaurin terms and remainders

No sign or order error was found. Applying the finite formula to `sum_(m<k<=n) f(k)` gives the endpoint term `(f(n)-f(m))/2`. For `f(x)=1/x`,

\[
f^{(2j-1)}(x)=-(2j-1)!x^{-2j},
\]

so the displayed correction is exactly `B_(2j)/(2j) (m^(-2j)-n^(-2j))`. For `f(x)=x^(-2)`, the odd derivative is `-(2j)!x^(-2j-1)`, yielding `B_(2j)(m^(-2j-1)-n^(-2j-1))`; the H2 formula and its signs are correct.

With the conventional remainder `-integral B_(2p)({x}) f^(2p)(x)/(2p)! dx`, the absolute bounds are respectively

\[
\frac{V_{2p}}{2p}(m^{-2p}-n^{-2p}),\qquad
V_{2p}(m^{-2p-1}-n^{-2p-1}).
\]

The second coefficient is not missing a factor: `(2p+1)!/(2p)!` is canceled by integration of `x^(-2p-2)`. The code uses these finite bounds with rational Bernoulli numbers and outward integer rounding. The log-series tail and its additional outward-rounded upper term are also correct. Low-anchor harmonic accumulation and all later rounding are separately enclosed.

## 2. Support searches and moment sum

For `W(n)=an+b-cnH_n`, the exact difference is `a-c(H_n+1)`. For c>0 these differences strictly decrease. The first binary search chooses a valid peak, including the exact zero-difference tie, and the two subsequent searches find the positive integer segment. For c<0, searching the positive segment of -W correctly identifies W's negative segment; its complement contains only positive or zero values, and zero values contribute zero energy. The implementation uses nonzero c in both reported workloads. It does not advertise or implement the c=0 branch.

Every comparison must separate its interval from zero; otherwise the code raises. This is a sufficient finite verification procedure, not a claim that fixed precision resolves every possible input. Certified support decisions apply to every exact coefficient choice enclosed by the interval coefficients, so correlation discarded by interval arithmetic broadens the result but does not invalidate it.

The six prefix identities and the expanded quadratic energy formula have the correct coefficients, including `T1=(H^2+H2)/2` and `T2=(N+1)H^2-(2N+1)H+2N`. Cell interiors plus each right endpoint, with the initial endpoint separately, count the complete closed window exactly once.

## 3. Existing finite evidence and performance scope

The saved certificate agrees with the report: 1,270 samples, 1,269 cells, 13,966 harmonic arguments and 2,569 moment arguments; endpoint aggregation took 10.023028 seconds. The separate 32,768-prefix baseline checked 1,271 harmonic points, scanned 63,490 upper/lower integer values and took 0.907126 seconds. Intersecting intervals are an implementation cross-check; the enclosure proof comes from the exact identities and directed arithmetic above. The report correctly says the direct baseline is faster on this small, dense partition.

The synthetic cell has exactly 999,999,999 interior integers, uses 90 new harmonic arguments and took 0.090612 seconds. Its certified interval is within the analytic Green lower/upper bounds `(h^5-h)/(120 R^4)` and `(h^5-h)/(120 L^4)`. It is correctly identified as a known-potential synthetic source, not as a new computation of the actual arithmetic road at 10^12.

The `O(K log B)` statement counts harmonic evaluations when comparisons are resolved. The report appropriately leaves bit cost, cancellation-driven precision and the cost of obtaining the true q samples separate.

## 4. Sibling allocation proof: discrete convexity

The continuous interpolation of the exact integer shape Phi has slope

\[
-u(u+1)(4u^3+6u^2+4u+1)
\]

on `b/(u+1)<=k<=b/u`, and adjacent pieces agree at their common endpoints. As k increases, u decreases, so the slope is nondecreasing. Thus the integer marginal reductions are nonnegative and nonincreasing. Taking the largest currently available marginal reduction obeys the per-block prefix constraints and gives the exact optimum for the specified geometric Phi objective.

The continuous Hölder equality and clipped solution are correctly separated from the exact integer optimization. The saturated case `k=b` gives Phi=0. In the unsaturated lower bound, `K<=B/8` indeed changes `1/4-64K^4/B^4` into at least `15/64`, yielding the displayed constant. No extension of this general-source information bound to the more structured actual arithmetic road is made.

## Conclusion

No load-bearing mathematical or implementation error was found in this targeted reading. No code change or repeat run was needed. The new computational result is certified endpoint aggregation, and the new allocation result is an exact geometric budget optimization; the original unbounded arithmetic energy target remains separate.
