# Nondecisive mathematical review: unbounded small-cone Parity trace

Reviewer: EM-REVIEW-58D6A2. Activity: RA-BALANCE-REVIEW-20261028-58D6A2.
Date: 2026-10-28, Asia/Shanghai.
Finding: the new weighted-support lemma, cone positivity and stated uniform
asymptotic follow from the explicitly inherited polynomial interface. No
unresolved mathematical defect was found in this bounded new argument.
This is a researcher review, not a Driver disposition or formal admission.

Reviewed file: `analysis/PARITY_UNBOUNDED_SMALL_CONE_AUTHOR.md`.
Reviewed final SHA256: `f9a9415455b9b004f9e2854e999eaebd4934acd7211084b87bf1bc5c0634e921`.
The mathematical first submission had SHA256
`0ba4948972e06f635cb0d7cb380f0eac1078a4a19f1f0a0e887dac61003990bc`;
the sole requested revision supplies the exact older review locator and
preserves the older author's original UNREVIEWED header as provenance.

## Independent checks

I read the complete new note and the complete relevant polynomial construction
in the managed-source return `analysis/unequal_gap_source_actual.json`, blob
`f05b0b5be5c7d78c7faf58ae1f818bc67cea103c`. I checked the new argument without
contributing to its construction.

1. The ring R=Q[epsilon,a epsilon,c epsilon] contains precisely monomials
   epsilon^j a^p c^q with p+q<=j. The finite nilpotent inverse defining U is
   inside R. W(epsilon,v) is polynomial before v=mc epsilon is substituted,
   so determinants and adjugates do not introduce negative epsilon powers.
2. Divisibility of Ngap by c in the ambient polynomial ring means every
   surviving term of Ngap has c exponent at least one. Dividing by c therefore
   changes the support inequality to p+q<=j-1. This inference remains valid
   after cancellations; cancellation cannot create a monomial outside R.
3. For n=1 the 1-by-1 adjugate is 1. All product factors in Dgap are positive
   for epsilon>=0,c>=0, so Dgap>=|K|. No definiteness of the signed Gram form
   or spectrum is needed.
4. Dividing a remainder monomial by epsilon writes it as a total degree j-1
   monomial in epsilon,a epsilon,c epsilon. For their maximum t<=1 it is
   bounded by t, establishing the coefficient-sum estimate including Bm=0.
5. The denominator error is bounded by Em t with the same support argument.
   Multiplication by epsilon and t<=rho gives exactly the factor m^(-2)
   in equation (A), with no lost factor of c or S+a.
6. For arbitrary positive paths a+c=o(S), rho tends to zero. Dividing the
   absolute error by the positive leading term gives relative error tending
   to zero. No path differentiability or lower gap bound was used. The strict
   limiting inequality for linear paths is correctly retained.

## Scope and reuse

The old signed Gram identity and first variation are inherited inputs, not
newly re-admitted by this review. The new result extends a fixed bounded-sector
estimate to a computable unbounded cone for each fixed m. It leaves all-S,
all-gap and m-uniform positivity open. The coefficient constants are finite
computable expressions, not evaluated numbers.

Reuse resolution: COMPOSE_APPLIED, using the source polynomial/adjugate
construction and elementary coefficient majorants. There is no new tool
family or external novelty claim. No scientific program, P11 NO_INVOKE
certificate or matrix enumeration was run for this review; the validation
here is symbolic paper reasoning, not Lean/kernel verification.

The reviewer inherited shared control and source summaries, did not author the
new mathematical construction, and is not a clean-blind reviewer. Source
exposure is NONBLIND_DISCLOSED. The project's X6/no-native-plane constraints
are retained; this is explicitly external auxiliary polynomial mathematics.

Researcher-ID: EM-REVIEW-58D6A2 / TASK_RESEARCH
