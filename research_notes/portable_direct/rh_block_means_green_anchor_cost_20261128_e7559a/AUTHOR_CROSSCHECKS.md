# Round 9 author crosschecks

All checks below are internal author checks under EM-DIRECT-E7559A. They are not
an independent Review and do not change the historical formal-result status.

## Block means

The moving-thickness branch checked the square-root statistic's exact denominator
`Xd`, the normalization `K(w)=rC`, Jensen's complete center range, use of the
previous whole block for the one-sided `2r` payment, and the exact `r-1+1` bridge.
It independently implemented the nonnegative source-count argument permitting
same-endpoint subtraction of cumulative interval bounds. The record and new
certificate are in `moving_shift_return/AUTHOR_CROSSCHECK_BLOCK_MEANS.md` and its
two companion files. The original block script was not imported or executed by
that check.

Root checked the subsequent quarter-scale aggregation: each new mean is the
arithmetic average of exactly `r_new/r_old` stored equal-size means. Ordinary
outward interval subtraction is then safe; no covariance assumption is used.
Jensen compares each coarse lag `d` with the finer lag `ratio*d`, including the
normalization factor. Exact aggregate counts are 88 means, 32 lag groups and 190
mean-pair terms. No sieve or prime logarithm was rerun for this aggregation.

## Original Green kernel

Root and the bounded-source branch separately checked the proof's full chain:
the original `1/t` kernel, its negative derivative jump at the peak, the uniform
positive second-derivative bound, all three clipping cases, nonnegative kernel
minorization, the `5/(4L)` negative-curvature mass, the `8/27` clipping payment,
`391/864<1/2`, and the integration-by-parts coefficient `-2`.

The transfer to an arbitrary genuine node grid uses the concavity of
`sqrt(G(n,n))`, not an unproved norm-contraction property of interpolation. The
same-mean counterexample retains all integer background and the original `1/m`.
The other branch's version-bound note is
`green_cutoff/AUTHOR_CROSSCHECK_BY_BOUNDED_SOURCE.md`.

The Green author and root also checked the actual-road connection: the
`kappa-D` decomposition, the favorable sign of higher prime powers in the upper
bound, the original endpoint chord, and
`beta_X^2=(X-X^(-3))/120` for the unit-source envelope.

## Positive bounded integer source

Root checked the original first cell, the exceptional source at n=2, C1 dyadic
joins, the unit-triangle second-difference formula, strict source bounds, and
the distinction between the smooth auxiliary P and the actual road
`Q=b+I_Z(P-b)`. The closed-window expansion, the two exact integrals and explicit
trapezoid error terms match the original weights.

For arbitrary grids, the lower bound handles length-one gaps by `(h_i-1)^5`;
the deterministic adaptive point-observation argument stays within one positive
bounded source class. The matching upper bound concerns positive interpolation
residual, while the full-energy result is only a query lower bound.

Root checked the geometric Mellin series, the formula for A(s_l), the source
Mellin multiplier `s(s-1)`, and the negative imaginary residue polynomial
`tau*(tau^4-161*tau^2+150)`. The absence of meromorphic continuation of the model's
Z_D is therefore a concrete missing structure, not an actual prime counterexample.

## Moving thickness and new energy criterion

Root checked the elementary reciprocal Mobius bound, finite Abel summation for
all `a>=alpha`, the real-floor harmonic remainder, the positive infinite-tail
comparison without a thickness upper bound, and the closed endpoint A=B case.
The bounded-ratio grid recursion proves a limsup transfer; it does not justify a
liminf for arbitrary nonnegative data. All RH and non-RH direction changes and
coefficient normalizations were checked.

For `SUBPOLYNOMIAL_ONE_SIDED_ENERGY_AND_QUARTER_MEANS.md`, root checked the genuine
unit-cell curvature payment `5S_++1/24`, the choice
`epsilon<2Re(s)-1`, local uniform Mellin convergence, Landau continuation for the
opposite nonnegative part, and nonzero zero residues. The joint quarter-scale
criterion explicitly retains the real chord-anchor budget and uses all integer
nodes only to establish the complete road-energy implication. It does not claim
that the quarter-scale prime statistic alone implies RH.

## Evidence scope

Analytical proofs carry the unbounded quantifiers. Rational and outward-interval
checks cover implementation, signs, phases, finite endpoints and displayed
constants. All unchanged scientific dependencies are pinned in the delivered
predecessor; no earlier program main or certificate was rerun.
