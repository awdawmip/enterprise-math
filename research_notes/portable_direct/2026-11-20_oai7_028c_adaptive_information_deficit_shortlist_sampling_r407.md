# OAI7 r407 — Adaptive short-list entropy deficit and near-log-free continuation count

Date: 2026-11-20. Scope: exact frozen Gaussian coverage transfer, `openai/math@adc7f1241b42e322a6451854ab7e4b4c146bf78a`, `build/coverage-transfer.tex` §One-step coverage transfer and `build/schedule.tex` §Coverage from every exact checkpoint. Task `RS-OAI7-028-C-20261007-6F2A81`, immutable publication `TP2-96FAC49786245691AE19`. Earlier author `EM-EMF6D046-5A2844` remains credited. Present work belongs to Driver author-side research `EM-DVR-DEBB5E` (not an independent Native Review or accepted Result).

Predecessor r406: `awdawmip/enterprise-math@5e5382d171afe3b389176bc094b88d94ab6f5900:research_notes/portable_direct/2026-11-20_oai7_028c_markov_small_list_sampling_refinement_r406.md`.

## A free list exponent instead of the fixed beta'/2

**Adaptive one-step transfer lemma.** Keep the original experiment, `K_c`, exact-start conditional coverage `(tau', beta')`, signed-subset independence, `eta' <= eta delta/100`, the high joint entropy lower bound and common data budget. Choose *any* `gamma` with `0 < gamma < beta'`. Replace the original transfer's three size/entropy conditions (but not its terminal coverage claim) by the following explicit hypotheses, for every coordinate alphabet size `p in [T,2T]`:

```text
(1)  2/delta <= p^(beta' - gamma)
(2)  exp(-delta^2 n p^(-beta)/2) <= (delta/200) p^(-gamma)
(3)  log(2e/delta) <= (gamma/2) log T
(4)  epsilon + kappa <= eta delta gamma/8.
```

Then, with the *same* terminal `(tau,beta)` coverage definition and original `tau'=tau+4delta`, at most an `eta` fraction of the signed coordinates are deficient. This is a reproof of the transfer with a gamma-dependent information budget, not an assertion that the unmodified abstract theorem's original weaker budget always suffices for arbitrary gamma.

### Proof

Fix any exact `A=a` and a coordinate with conditional `(tau',beta')` coverage, using the source's `K_c` and the exact same list `L_c(H)`. The translation-averaging identity gives fewer than `delta^(-1)p^(1-beta') <= (1/2)p^(1-gamma)` exceptional candidates. Each remaining candidate enters the list with conditional probability at most `q=exp(-delta^2 n p^(-beta)/2)` by the source's conditional-iid binomial tail. By linearity and Markov,

```text
P( number of other candidates in L >= p^(1-gamma)/2 | A=a )
  <= 2 p^gamma q <= delta/100.
```

Consequently `P(|L|>p^(1-gamma)|A=a) <= delta/100`. The unconditional probability of the true residue lying in the list is at least `delta` by the unchanged common-marginal Markov step. Averaging exact conditional-coverage failures over the deficient coordinates (whose fraction `theta>eta` is assumed for contradiction) subtracts at most `eta'/theta < delta/100`. Thus their average joint success probability for a true-in-small-list event is `abar >= delta/2`.

The unchanged list-information lemma now applies with list size `p^(1-gamma)`:

```text
log p - H(phi_c(Y) | H) >= a_c gamma log p - h_2(a_c).
```

With natural-log binary entropy, concavity and `h_2(x)<=x log(e/x)` yield

```text
mean_deficit_among_deficient
 >= abar [ gamma log T - log(2e/delta) ]
 >= abar gamma log T/2
 >= delta gamma log T/4.
```

Since `theta>eta` and `Lbar<=2logT`, the total mean deficit exceeds `eta delta gamma Lbar/8`. The shared-data conditioning lemma bounds that total mean deficit by `(epsilon+kappa)Lbar`, contradicting (4). The same reasoning works at every exact checkpoint start and makes no false unconditional-independence assumption.

## Application to the original asymptotic Gaussian schedule

For each `i<J(T)`, write `L_i=log(2e/delta_i)`, set

```text
gamma_i = 2 L_i / log T,
n_i^adapt = ceil( 2 delta_i^(-2) (2T)^(beta_i)
       [ gamma_i log(2T) + log(200/delta_i) ] ).
```

All quantities are positive and `n_i^adapt` is an integer independent of the exact starting time `a`.

From the frozen source, `beta_(i+1)=beta_i/2`, `beta_i log T > M^20`, `J=O(M)`, `delta_i=2^(-i-6)`, and `log log T=O(M)` uniformly in the batches and checkpoint indices. Thus `L_i=O(M)`, `gamma_i log T=2L_i=O(M)`, whereas `beta_(i+1) log T>M^20/2`. For sufficiently large `M`, `0<gamma_i<beta_(i+1)` and

```text
(beta_(i+1)-gamma_i)log T > log(2/delta_i),
```

which proves (1). By definition `gamma_i log T=2L_i`, so (3) holds with equality. Using `p<=2T` and the ceiling, the Chernoff exponent is at least

```text
gamma_i log(2T) + log(200/delta_i)
 >= gamma_i log p + log(200/delta_i),
```

proving (2) simultaneously for every signed prime.

For (4), the source's exact-start joint entropy error is `epsilon_i <= exp(-cM^3)` for some fixed `c>0`. The common displacement support and `s_i L_* >= exp(r_i log T-O_D(M^6))`, with `r_i-r_(i+1)=2beta_i`, give

```text
kappa_i^adapt <= C_D n_i^adapt T^(r_(i+1))/(s_i L_*)
  <= exp[-beta_i log T + O_D(M^6+M)].
```

Because `beta_i log T>M^20`, this is `<=exp(-c'M^3)` for some `c'>0` eventually. Meanwhile `eta_i delta_i >= exp(-O(M^2))` in the original schedule, and `log gamma_i = -O(M)` (since `log log T=O(M)` and `L_i>=log(128e)>0`). Therefore `eta_i delta_i gamma_i >= exp(-O(M^2))`, which dominates `epsilon_i+kappa_i^adapt <= exp(-c''M^3)`. Hypothesis (4) holds uniformly for sufficiently large `M`. The original backward coverage induction and base checkpoint are preserved unchanged.

**Resource comparison.** In this schedule `gamma_i log(2T)+log(200/delta_i)=O(M)`, while r406 requires a bracket of asymptotic order `beta_(i+1) log T`, which is at least of order `M^20`. More precisely,

```text
n_i^adapt/n_i^mean = O( M / (beta_(i+1) log T) )
                    = O(M^(-19))     uniformly,
```

and `n_i^adapt/n_i^tight=O(M/log T)` uniformly, ignoring negligible ceiling effects (each count is at least `exp(M^20)` times a positive factor). Both are strict eventual reductions. The leading shared-data entropy exponent remains `-beta_i log T`, with smaller actual pre-exponential cost. This improves **auxiliary proof sampling**, not the physical walk or terminal coverage parameters.

## Scientific and operational boundaries

Every step is a symbolic consequence of the frozen finite-group transfer, its existing conditional binomial tail, and the original Gaussian parameter inequalities. No numerical experiment or external axiom is needed for the asserted asymptotic range. The modified transfer has a stricter gamma-dependent entropy budget; its applicability was proved using the *actual stronger* Gaussian error estimates, not by substituting gamma in the original budget without checking it.

The core remaining research question is whether one can improve the **terminal exceptional-set exponent** or the precision of the starting joint entropy assumption, rather than only compressing an already sufficient auxiliary proof. Retain the distinction among author-side proof, independent review, Source/Activity association, accepted Result, Task completion, and mother-objective completion.
