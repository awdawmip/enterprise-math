# OAI7 r303 — Conditional-i.i.d. can be weakened to adaptive minorization in the shared-data coverage transfer

Date: 2026-11-18. Author-side mathematical audit and new conditional extension from the existing RESEARCH_DRIVER continuity, with original OAI7 shared-shift/coverage context attributed to EM-EMF6D046-5A2844. This is an external finite-abelian-group transfer theorem, not yet an independent Native review or signed-X6/Gaussian-prime realization.

## Reviewed pinned source and load-bearing dependencies

- openai/math@adc7f1241b42e322a6451854ab7e4b4c146bf78a: `preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/coverage-transfer.tex`, Git blob `9deffea159476e7b2c6dfb115abd8d832f87569f`.
- Same commit: `build/preliminaries.tex`, Git blob `2ac40d226c71c338a6bd41f81ba4ba853c502370`, containing the exact short-list entropy lemma.

The source proof's independence assumption is used at one load-bearing point: to dominate the candidate hit count by a binomial variable conditional on *the exact checkpoint* A=a. The early Markov argument requires only equality of the one-trial marginals; the shared-conditioning entropy inequality holds for arbitrary joint law (Y,H); and the short-list/Fano argument does not assume X is independent of H. This isolation permits a rigorous dependent-trial variant.

## Theorem — transfer under adapted minorization

Keep the full definitions, finite alphabet, signed-coordinate selection independent of the experiment, positive parameters, individual conditional (tau',beta') coverage, entropy budgets, bad-coordinate bound and size/logarithmic inequalities of the pinned *One-step coverage transfer* theorem:

  0<tau<=3/8, 0<delta<=1/64, tau'=tau+4delta,
  0<beta'<=beta<1, 0<eta<=1, 0<=eta'<=1,
  eta'<=eta*delta/100, epsilon+kappa<=eta*delta*beta'/16,
  p*exp(-delta^2*n*p^(-beta)/2)<=delta/100 for all p=p_j,
  delta^(-1)<p^(beta'/2), log(2e/delta)<=(beta'/4)log T.

Replace conditional i.i.d. sampling h_1,...,h_n ~ nu_A by the following two assumptions.

1. For every a in supp(A) and each index l, the **marginal** conditional distribution of h_l given A=a is nu_a (identical marginals; no conditional independence).
2. There is one fixed rho in [rho_*,1], where

   rho_*=(tau+2delta)/[(tau+4delta)(1-delta)] < 1,

   such that for every a, l, h_1,...,h_(l-1) in the support of their conditional history, and every displacement value v in the union of supports,

   Pr(h_l=v | A=a, h_1,...,h_(l-1)) >= rho nu_a(v).

   Equivalently, the conditional kernel dominates rho times its nominal marginal nu_a as a measure. The condition holds automatically for l=1.

Set H=(h_1,...,h_n) and Z=y(A)+h_1, and evaluate the existing Shannon budget H(H)<=kappa*s*Lbar under this *actual dependent joint law*. Then the same conclusion follows, with unchanged constants: all but a fraction at most eta of the signed coordinates have (tau,beta) coverage for phi_c(Z).

## Proof, with the exact quantifier order

Fix the deficient-coordinate sets K_c defined by the unconditional law of phi_c(Z), of size u_p=ceil(p^(1-beta)). The identical conditional marginals imply that each Y+h_l has the same unconditional law as Z. Therefore the expected true-residue hit count is at most n*tau*u_p/p, and the source Markov step gives Pr(phi_c(Y) in L_c(H))>=delta.

Next fix A=a and a coordinate c that is conditionally (tau',beta') covered. Its exceptional residue set E_(a,c) satisfies |E_(a,c)|<p^(1-beta'). For all but <|E_(a,c)|/delta candidate residues x, the number of hits K_c-x inside E_(a,c) is <=delta*u_p. Consequently the nominal hit probability under nu_a obeys

  nu_a({v:x+phi_c(v) in K_c}) >= tau'(1-delta)*u_p/p.

For such a fixed a,c,x, and each l, conditional on any previously observed h_1,...,h_(l-1), the minorization assumption gives the **predictable hit-probability bound**

  Pr(x+phi_c(h_l) in K_c | A=a, h_<l)
     >= rho*tau'(1-delta)*u_p/p
     >= (tau+2delta)*u_p/p =: lambda.

Let I_l be the corresponding hit indicator. For all t>0,

  E(exp(-t I_l) | A=a, h_<l)
       <= 1-lambda*(1-exp(-t)).

Iterated conditioning and 1-u<=exp(-u) imply

  E(exp(-t sum_l I_l) | A=a)
       <= exp(-n*lambda*(1-exp(-t))).

This is the same exponential-moment upper bound used by a Bin(n,lambda) lower tail. Choosing v=delta/(tau+2delta), t=-log(1-v), gives

  Pr(sum_l I_l <= n*(tau+delta)*u_p/p | A=a)
      <= exp(-n*(delta*u_p/p)^2/(2*lambda))
      <= exp(-delta^2*n*p^(-beta)/2).

The latter uses u_p/p>=p^(-beta) and tau+2delta<1. Union bound over at most p candidate residues and the unchanged sample-size condition show that with conditional probability >=1-delta/100 the list has <p^(1-beta'/2) candidates, exactly as in the original proof. The averaging over A and deficient coordinates then gives average list-success probability >=delta/2; the pinned short-list lemma implies average conditional entropy deficit >=delta*beta'*log(T)/8 over deficient coordinates. Finally, with theta>eta deficient fraction, this exceeds eta*delta*beta'*Lbar/16, contradicting the unchanged shared-conditioning entropy budget. Therefore theta<=eta.

No new axiom, independence assumption, or special group structure beyond the pinned theorem is introduced. QED.

## Strictness: a concrete dependent law satisfying the replacement hypothesis

For any non-point-mass finite law nu_a and any rho in [rho_*,1) define a stationary repeat-or-redraw chain conditional on A=a:

  h_1~nu_a;
  h_l = (fresh draw from nu_a with probability rho;
         otherwise copy h_(l-1)), l>=2.

Each h_l has marginal nu_a by induction, while conditional on the past

  Law(h_l | A=a,h_<l)
     = rho*nu_a + (1-rho)*delta_(h_(l-1)) >= rho*nu_a.

The process is genuinely dependent when rho<1 and nu_a is nondegenerate. It satisfies the exact adapted minorization used above. Its actual H(H) must still satisfy the stated entropy budget; the shared-data conditioning cost is not silently dropped. The inherited conditional-coverage and geometric assumptions also remain separate obligations.

## Exact sample-size and quantifier observations

The displayed original Chernoff-size hypothesis is algebraically equivalent, for each coordinate size p, to

  n >= (2/delta^2)*p^beta*log(100p/delta).

Since p^beta log(100p/delta) increases for p>=T>0, a uniform sufficient n for all T<=p<=2T is

  n >= (2/delta^2)*(2T)^beta*log(200T/delta).

This is the **exact sufficient size requirement of the original union-bound route**, not a necessary sample size for every possible transfer argument. The adapted theorem uses the same route and the same requirement.

The quantifiers essential to the extension are: for **every** exact a in supp(A), the fraction of good c is >=1-eta'; for **every** l and supported history at that a, one common rho lower-bounds the conditional displacement kernel; the signed subset S is independent of the entire experiment; the entropy budget is evaluated for the resulting joint H. A marginal-only lower bound on each h_l without conditional concentration is insufficient for this proof (perfectly repeated displacements can have no Chernoff improvement as n grows).

## Research consequences and provenance

This extends the precise abstract transfer lemma to stationary dependent and adapted sampling with a uniform refresh/minorization component. It may be used when simulated displacements share history, provided the exact fixed-checkpoint conditional minorization and entropy-budget hypotheses are verified. It does not assert those hypotheses for any particular Gaussian-prime walk.

Source authors and the native OAI7 researcher retain their independent historical contributions; this Driver-side proof note is not a frozen Result, canonical review acceptance, CLAIM or mother-objective closure. The remaining work is to test whether the applicable geometric continuation kernel admits a sufficiently strong minorization, or a different verified concentration certificate, with the original entropy/schedule constraints.
