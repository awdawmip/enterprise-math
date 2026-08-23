# CBRC F3R — Regularity and Ablation Packet

Researcher-ID: `EM-CBRC-F3R-AA5925`

Primary stage verdict:

`F3R_CURRENT_AXIOMS_STRICTLY_UNDERDETERMINE_MIXING`

## 1. Baseline survivor family used for controls

For distinct primes `p!=r`:

`q_{p,r}(n,a)=1/2*(1_{p does not divide n}+1_{r does not divide n})`.

For every

`A in S_{p,r}`

with monomial reductions of opposite permutation type modulo `p` and `r`, the scalar is exactly conserved and the elementary split is `1/2+1/2`.

The controls below are counterfactual only and are not used in the main verdict.

## 2. GLOBAL_ZERO_SEPARATION

Control:

`z!=0 => q(z)>0`.

For every support-splitting law:

`q_{p,r}(pr e)=0`

while `pr e !=0`.

Therefore every exhibited support-splitting `(M,q_{p,r})` model dies.

For the accepted canonical `(A0,B=0,D=I)` representative, the frozen F3 theorem already classified its complete scalar family as `q_delta`, and every member has

`q_delta(6e)=0`.

Hence the canonical representative itself has no scalar in that frozen complete family satisfying global zero separation.

Verdict:

`GLOBAL_ZERO_SEPARATION_KILLS_SUPPORT_SPLIT_SCALARS_AND_CANONICAL_Q_DELTA_FAMILY`.

This does not become a Foundation premise.

## 3. INTEGER_COPY_MONOTONICITY

Control:

larger positive free copies do not decrease scalar.

For every support-splitting law:

`q_{p,r}(e)=1`,
`q_{p,r}(p e)=1/2`.

Thus monotonicity fails immediately.

The canonical six-periodic scalar likewise has

`q(e)=1`,
`q(2e)=1/2`.

Verdict:

`INTEGER_COPY_MONOTONICITY_KILLS_SUPPORT_SPLIT_SCALARS_AND_CANONICAL_Q_DELTA_FAMILY`.

## 4. FINITE_COPY_NONDEGENERACY

Control:

no nonzero old signed multiple `n e` has zero scalar.

Again

`q_{p,r}(pr e)=0`.

For the canonical complete scalar family,

`q_delta(6e)=0`.

Verdict:

`FINITE_COPY_NONDEGENERACY_KILLS_SUPPORT_SPLIT_SCALARS_AND_CANONICAL_Q_DELTA_FAMILY`.

## 5. TAGGED_REFINEMENT_NONAMPLIFICATION

Control:

a tagged refinement may not increase total scalar above the pre-refinement elementary value unless another accepted operation supplies the difference.

For every F3R survivor satisfying M6,

`Q(Mz)=Q(z)`.

Thus, on the declared mixing/refinement operation, the control holds with equality.

Accepted unary transports also leave `q` invariant.

Verdict:

`TAGGED_REFINEMENT_NONAMPLIFICATION_REDUNDANT_WITH_M6_ON_DECLARED_F3_OPERATIONS`.

## 6. Physical-equivalence ablation

If inverse orientation is not quotiented, every physical class can split into at most two orientation classes. If marker swap is not quotiented, presentation copies similarly multiply by a finite factor.

Neither ablation changes the infinite-family conclusion because the free presentation group orbit is finite whereas the arithmetic survivor family is infinite.

Verdict:

`FINITE_PRESENTATION_ABLATIONS_DO_NOT_REMOVE_INFINITE_UNDERDETERMINATION`.

## 7. Torsion-sensitivity ablation

For torsion-blind `q_{p,r}`, every free survivor admits all

`3888`

torsion/cross lifts.

On the six-periodic stratum, adding

`delta*1_{3|n and torsion!=0}`, `delta>0`

reduces the lift family exactly to

`36`.

Thus torsion sensitivity is genuinely load-bearing for lift selection but does not select a unique free mixing family.

Verdict:

`TORSION_SENSITIVITY_REDUCES_3888_TO_36_BUT_FREE_UNDERDETERMINATION_REMAINS`.

## 8. New-axiom boundary

The first three strengthened controls kill the support-splitting pathology precisely because they add information about finite copies that F3 deliberately omitted.

They therefore identify a clean future selector boundary:

- zero separation;
- monotonic finite-copy behavior;
- finite-copy nondegeneracy.

Any one may be scientifically investigated later, but importing it into F3R would change the axioms and invalidate the blind-forward scope.

Deliverable:

`F3R_REGULARITY_COUNTERFACTUALS_CLASSIFIED`.
