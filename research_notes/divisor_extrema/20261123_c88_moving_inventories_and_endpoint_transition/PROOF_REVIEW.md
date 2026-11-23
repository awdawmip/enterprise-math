# C88 integrating proof review

Date: 2026-11-23 (Asia/Hong_Kong).
Scope: the seven new analytic proof notes in this package and their report.
This is project-internal mathematical review, not external peer review,
formal verification, shared Result acceptance, or task closure.

## Native bridge

The integrating author read C82's finite spectral, cross-branch and Haar
arguments, C83's critical-transition and near-count treatment, and both new
bridge proofs. The following new dependencies were checked explicitly:

- The three-node second divided difference has a positive normalized
  second-derivative kernel, so its approximation does not lose a factor of
  `1/theta`. Rounding alone contributes `4/(L_c R_c)`.
- `lambda*s*(z-s)=L_c*A*(B-A)/sqrt(c*B)` and
  `R_c=theta*(1-theta)/(D^3/c)` have their stated constants.
- Inversion uses the outer pair; integer displacements remain `O(D)`.
  Linearization and middle interpolation errors have no hidden `B/A` loss.
- The exact zero-sum phase decomposition contains both `B1` and `B2`.
  The first two homogeneous degrees are `57/4` and `18`; cancellation of
  `-15*a+240*b` leaves `(1125/16)*b` in the second term. The leading flow
  acts nontrivially on that term. Fixed-sign analytic continuation covers
  every regular spectral chart.
- All fixed nonzero modes vanish. The proof retains the finite spectral
  slope until the Haar change of coordinates; it does not amplify a
  prematurely substituted limiting spectrum. Near-count nontransitivity
  is handled by larger regular candidate charts.
- Compactness gives tracking for moving `theta_c` and bounded positive
  `L_c`, including integer precision rounding.

An independent agent checked these same new interfaces in
`critical/INDEPENDENT_BRIDGE_REVIEW.md` and found no blocking gap.

## Uniform endpoint transition

The integrating author independently checked the phase-slice Jacobian and
the finite-width formula, including the factor `2*a^2*s`, cutoff `X<=1/a`,
and upper integration limit `1/(a*s)`. For `u>=1/a`, both relevant window
families have uniform inradius and diameter after a determinant-one
normalization and a scale `sqrt(u)`. Thus the inherited fat-window lemma
gives an integrable `O(u^-2)` tail, and the total error is `O(a^3)` uniformly
in the complete closed position interval.

The large-rho coefficient is `kappa3/sqrt(2)`. The full-source transition
uses the common integrable bound `J^2+sqrt(tau)*J^(3/2)`; no small-J region
is silently discarded. A coarse uniform expansion first confines all
low-precision maximizers to `[1/4,3/4]`; the sharper central `O(L^6)`
remainder then gives distance `O(L^(3/2))` from the midpoint.

`bridge/INDEPENDENT_TRANSITION_REVIEW.md` independently checks these steps.
No argument uses monotonicity of the probability of exactly one point
under window inclusion.

## Uniform high-precision tail and native designs

The integrating author extended the inherited tail proof using the common
bound `H_theta(a)<=min(1,21/(4*pi^2*a))`. The non-tail negative-moment
estimate and the tail truncation are therefore uniform in theta. The
coefficient `W=160*K^(-1/20)/39`, optimizer compactness, and the concavity
chord bound were checked. The rate in the low-precision optimizer
statement was strengthened after independent review.

The slowly diverging spacing construction and the two power examples were
checked by direct exponent arithmetic. `F0>F2` follows from the exact C85
integral, monotonicity and the limiting value of F2. The full-inventory
gain uses sourcewise monotonicity of uniqueness with an added readout.
For `A=1`, only a known full-macro-single-preimage source region is used
to obtain the strict gain; no global near/full interchange is made.
Its compact-L form handles integer p without a fictitious convergent
multiplier. `endpoint/INDEPENDENT_DESIGN_REVIEW.md` checks these claims,
including the adjacent-middle corollary.

## Finite separation and the unresolved joint process

The exact sign of the middle displacement is `a1=a0-h+o(1)` with
`h=L*tau*Delta B2/2`. The source phase condition is consequently
`|(sigma1-sigma0)-h|<=1+o(1)`. Integrating its triangular phase density
gives the stated piecewise quadratic q. Positive-offset intervals are
nested, as are negative-offset intervals, so only the nearest upper and
lower B2 values enter the necessary phase filter.

The integrating author proposed the strengthened loss bound
`2*integral min(F0,Q_tau)`. Its author independently verified it by fixed
regular source partitions and refinement; no independence of the two
events is assumed. The final lower bound is
`2*integral [F0-Q_tau]_+`. The exact finite-c competitors on other sheets
form coupled affine lattices; their joint limit has not been proved.

## Claims deliberately left at their proved strength

- `R_c -> infinity` is sufficient, not proved necessary.
- Native tracking is for multipliers in fixed positive compact intervals.
  Auxiliary theta/L limits do not establish arbitrary linked c/L limits.
- Finite-tau full-inventory convergence, origin-independence and strict
  global loss remain open. The filter is a necessary-condition bound,
  not an actual collision probability.
- Asymptotic optimizer location does not prove an exact optimizer at
  every sufficiently small or large finite multiplier.
- C87's integrated-kernel proof is inherited at its immutable published
  version. Its old computational certificate was not unnecessarily rerun.
- No new exhaustive arrangement computation or executable theorem test
  was performed or reported. The seven new results have analytic proofs.

All source-file references are recorded in `SOURCE_REFS.json`; the
integrity manifest serves preservation only, not theorem validation.
