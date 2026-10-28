# Nondecisive mathematical review: total-scale tail uniform in every second gap

Reviewer: EM-REVIEW-58D6A2. Activity: RA-BALANCE-REVIEW-20261028-58D6A2.
Date: 2026-10-28, Asia/Shanghai.
Finding: the new indefinite relative-trace perturbation estimate is valid,
including arbitrary cross-parity errors, and its two-region combination
proves the stated effective tail for every c>0 at fixed m. No unresolved
mathematical defect was found. This reviews the new unbounded-ratio argument
at its own exact version; it does not inherit a vote from an earlier scope.

Reviewed file: `analysis/PARITY_FULL_TRACE_ALL_SECOND_GAPS_SUM_TAIL_AUTHOR.md`.
SHA256: `cf9fc55ac4a4a193cc4d5c9e8355fde02dae577f0241344b05d48961dea771a0`.
I read the full frozen manuscript. Its exact common-center and metric
interfaces refer to the complete sources already read for the preceding
review: blobs f05b0b5be5c7d78c7faf58ae1f818bc67cea103c and
c94088a17f4a09dd2d16171162c09ed13807a8bf. The small-nu dependency is the
separately reviewed bounded-relative-gap manuscript at SHA256
129cad117292b1e90f3f0f8eb6c2791c2e5a050adff386c9e4a0b4c6e0d55c5e,
used only with C=1. Those immutable dependencies are unchanged.

## 1. Exact metric normalization and effective perturbation radius

From Q_r=C_r A_r C_r, a centered output monomial
(theta+r/2)^j becomes r^j*(epsilon*theta+1/2)^j. The two inverse C_r
factors leave precisely the displayed factor (n!/m)*epsilon^(-n),
so equation (5) is in the same centered metric normalization as equation
(3). It is not the uncentered metric with an unrecorded basis change.

Each Q_i is polynomial with nonnegative physical factors and Q>=1 for
epsilon>=0. The inherited finite-difference/analytic extension makes
Q*M polynomial: its apparent lower negative epsilon powers vanish, not
merely along a sampled path. Q(0)=1 and M(0)=M0 make the numerator of V
divisible by epsilon in the polynomial ring. The resulting finite
coefficient matrix E supplies an actual rational bound on epsilon in [0,1].

P=Sigma*M0 is real symmetric positive definite. Both P^(-1) and
Delta=M(epsilon)-M0 are symmetric, so their spectral norms are at most
their induced infinity norms. Therefore
||P^(-1/2)Delta P^(-1/2)||_2<=k_m*epsilon follows with exactly the proposed
product of infinity norms. No missing condition-number or dimension factor
is required. The actual signed Delta is retained, while absolute values
only bound its size. Since epsilon/v<=epsilon, the same radius controls
both endpoints for every nu>=0. The k_m=0 case is covered by the max(1,...)
definition without division by zero.

## 2. Reference congruence includes all cross-parity perturbations

E_lambda and V_B=E_lambda' D_v each commute with the parity signature Sigma.
Their positive reference forms P_A and P_B therefore commute with Sigma,
as do their positive square roots and inverses. In particular
A0=Sigma*P_A and B0=Sigma*P_B are exact identities.

The bound -eta P<=Delta<=eta P in Loewner order survives either endpoint
congruence. Normalizing by the corresponding reference square root gives
real symmetric R_A,R_B with norm at most eta and the exact factorizations
A*=P_A^(1/2)(Sigma+R_A)P_A^(1/2), and similarly for B*. This argument does
not assume that the perturbed signed forms remain block diagonal or
positive. Off-diagonal even/odd terms are part of R_A,R_B throughout.

Let C*=P_B^(-1/2)P_A^(1/2). Its lack of symmetry is harmless: it still
commutes with Sigma. Direct cyclic permutation of the full product in
tr(B*^(-1)A*) gives exactly equation (9), with C* on the left and C*^T
on the right. The reference trace is then
tr(Sigma C* Sigma C*^T)=tr(C*C*^T)=||C*||_F^2. This equality is the
positive quantity that absorbs arbitrarily large endpoint scale ratios.

## 3. Independent check of the relative trace bound

Factoring Sigma+R_B=Sigma*(I+Sigma R_B) gives the Neumann inverse bound
||H_B||_2<=eta/(1-eta) for eta<1. The three exact error terms are the
R_A term, the H_B term and their product, with no fourth missing term.
For each, the inequality
||C* X C*^T||_*<=||X||_2*||C*||_F^2 follows from the Schatten
Hilbert-Schmidt product inequality. Pairing with Sigma or H_B in operator
norm gives the three bounds stated by the author even when X is signed
and C* is nonsymmetric.

Their sum is
eta + eta/(1-eta) + eta^2/(1-eta)=2eta/(1-eta).
Thus the relative error is at most one half when eta<=1/5. The reference
trace is positive and at least n*(1+nu)^(m+1) by the already established
limiting block comparison. No positivity of actual finite-r eigenvalues
is needed for this trace estimate, and no additive error constant growing
with nu has been silently absorbed.

## 4. Joining small and unbounded relative gaps

For nu>=1, the resulting lower bound
Gap>=n*(1+nu)^(m+1)/2-n dominates n*((1+nu)^(m+1)-1)/4 because
(1+nu)^(m+1)>=8>3. For 0<nu<=1 the preceding C=1 theorem gives the
stronger half-strength bound through its exact nu-factor estimate. Taking
the maximum of the two effective rational thresholds covers every nu>0;
nu=1 lies in both domains. This preserves arbitrarily small c without
trying to force the large-gap relative-trace bound to prove small-gap
positivity on its own.

Consequently each fixed m has a threshold independent of S,a,c, after
which all c>0 satisfy the stated quarter-strength complete-trace bound.
The compact-total-scale region and m-uniform threshold are still open.
No positive-coefficient or all-parameter theorem is inferred.

## 5. Review grade, reuse and contribution boundary

This is independent symbolic paper checking. No scientific computation,
matrix scan, symbolic package, stopped m7/P11 work or proof kernel was
executed. The new contribution is the uniform relative-trace control of
the full signed forms, composed with the earlier small-nu argument.
Congruence, Neumann estimates, Schatten norm inequalities and the old
metric/secant interface are COMPOSE_APPLIED standard tools. No global
tool family or external novelty is established.

The small-cone and bounded-ratio papers remain valid provenance and proof
dependencies; their nested domains should not be counted again as separate
discoveries after this stronger interface is integrated.

Reviewer received the full manuscript only after its freeze and supplied
no construction. Shared control/source context is disclosed; this is
nonauthor NONBLIND review, not clean-blind review. The model remains
explicitly external real algebra, preserving native X6 semantics. This
report grants no formal Driver disposition, Result acceptance, Task
closure, Working Truth, Foundation or parent-objective completion.

Researcher-ID: EM-REVIEW-58D6A2 / TASK_RESEARCH
