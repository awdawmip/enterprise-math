# OAI7 r406 — Mean-size rather than all-candidates concentration in the shared-coverage transfer

Date: 2026-11-20. Research status: Driver-authored mathematical **author-side** proof. It is not an independent Native Review, formal Result or Task completion. Preserve original OAI7 task Researcher EM-EMF6D046-5A2844 and Driver EM-DVR-DEBB5E attribution separately.

**Exact frozen source:** `openai/math@adc7f1241b42e322a6451854ab7e4b4c146bf78a`, `preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/coverage-transfer.tex`, especially lines 103–128 and 161–215; `build/schedule.tex` checkpoint parameters and coverage induction (the same source pin). Predecessor: `awdawmip/enterprise-math@6ddecc22d2cf7028c59ed286d78024a7a6a19205:research_notes/portable_direct/2026-11-20_oai7_028c_concentration_tight_continuation_budget_r405.md`.

## Statement — a strictly weaker sufficient concentration hypothesis

In the original one-step coverage transfer theorem, retain **all** assumptions and conclusions, except strengthen the existing size separation to

```text
2/delta <= p^(beta'/2)
```

and replace the former concentration condition `p exp(-delta^2 n p^(-beta)/2) <= delta/100` with

```text
exp(-delta^2 n p^(-beta)/2)
    <= (delta/200) p^(-beta'/2).             (M)
```

The latter is substantially weaker when `0<beta'<2` and `p` is large. The two changed hypotheses are not asserted for every arbitrary parameter instance allowed by the old abstract theorem; the concrete Gaussian checkpoint schedule satisfies both for all sufficiently large M, uniformly in its batches and indices.

**Interpretation.** The proof only needs the *list size* to be below `p^(1-beta'/2)` with high probability. Its former union bound demanded that *every one of p nonexceptional candidate residues* simultaneously pass a binomial test, which is stronger than the required event. A first-moment bound on the count of falsely retained candidates suffices.

## Proof at one exact checkpoint

Follow the original notation, fix an arbitrary exact `A=a` and a signed coordinate with conditional `(tau', beta')` coverage. Define `K_c`, `L_c(H)`, and `u_p=ceil(p^(1-beta))` exactly as in the source. Its shift-counting identity gives a deterministic exceptional-candidate set `E^*_{a,c}` of cardinality strictly smaller than

```text
delta^(-1) p^(1-beta') <= (1/2) p^(1-beta'/2).
```

For every candidate `x` outside this set, each of the `n` independent **conditional-on-A=a** trials has hit probability at least `(tau+2delta) u_p/p`; the original binomial lower-tail calculation therefore yields

```text
P(x in L_c(H) | A=a) <= q_p
       := exp(-delta^2 n p^(-beta)/2).
```

Let `W` count the candidates outside `E^*_{a,c}` that nevertheless belong to the list. No independence between the indicators indexed by candidates is needed: linearity gives `E(W|A=a) <= p q_p`. By Markov,

```text
P(W >= (1/2) p^(1-beta'/2) | A=a)
    <= 2 p^(beta'/2) q_p <= delta/100,
```

using (M). As `|E^*_{a,c}| < (1/2)p^(1-beta'/2)`, the same source conclusion follows:

```text
P(|L_c(H)| > p^(1-beta'/2) | A=a) <= delta/100.
```

This replaces only source lines 203–215. Its true-residue-in-list Markov step (149–159), conditional coverage averaging (217–238), short-list information bound (239–265), shared-data entropy lower/upper estimate and independent signed-subset averaging are unchanged. Thus the **entire transfer conclusion** remains valid, with all its original exact-start and common-data quantifiers. The improvement does not make the original theorem false or alter the physical walk.

## Application — lower auxiliary continuation count than r405

For the original Gaussian batch `p in [T,2T]`, `beta=beta_i`, `beta'=beta_(i+1)=beta_i/2`, `delta=delta_i=2^(-i-6)`, choose

```text
n_i^mean = ceil(2 delta_i^(-2) (2T)^(beta_i)
       * [ (beta_(i+1)/2) log(2T) + log(200/delta_i) ]).
```

The bracket is positive. For every `p in [T,2T]`, monotonicity gives

```text
delta_i^2 n_i^mean p^(-beta_i)/2
 >= (beta_(i+1)/2) log(2T) + log(200/delta_i)
 >= (beta_(i+1)/2) log p + log(200/delta_i),
```

so (M) holds. The extra size separation holds uniformly since the source has `beta_i log T > M^20` for `i<J`, whereas `log(2/delta_i)=O(M)` and `beta_(i+1)=beta_i/2`. The source's other transfer size/log and entropy-budget hypotheses are unchanged.

Comparison with r405's `n_i^tight=ceil(2 delta_i^(-2) (2T)^(beta_i) log(200T/delta_i))` gives, uniformly over checkpoint indices and batches as the original `M -> infinity`,

```text
n_i^mean / n_i^tight
 = (beta_(i+1)/2) (1+o(1))
 = (beta_i/4) (1+o(1)).
```

Indeed `beta_(i+1) log T > M^20/2` while `log(200/delta_i)=O(M)`; the common exponentially large factor makes ceiling effects negligible. In particular `n_i^mean < n_i^tight <= n_i^original` eventually. The sample cost is reduced by a parameter-dependent factor, potentially much smaller than a fixed numerical constant.

The same unconditional common-displacement support bound supplies

```text
kappa_i^mean <= C_D n_i^mean T^(r_(i+1))/(s_i L_*)
 <= exp[-beta_i log T + O_D(M^6+M)].
```

Thus the r405 *leading exponent* survives while its explicit sample-count prefactor is improved. Since the refined sample count is not larger than r405's, all original Shannon entropy budget inequalities remain satisfied. This is a **proof-resource** improvement; it establishes neither stronger terminal coverage parameters nor mathematical acceptance of the mother objective.

## Verification boundary and next mathematical question

This is a symbolic first-moment/Markov derivation using the source's already proved binomial bound. No finite numerical test is a substitute for its all-p, all-exact-start argument; no formal Lean checker was run. The immediate decision point is whether further reduction can avoid controlling the candidate count at the `p^(1-beta'/2)` scale (for example, a sharper list-information argument that tolerates larger random lists), while keeping the same terminal `(tau,beta)` coverage and shared entropy budget. No new Native Result/Review, Activity association, CLAIM or owner transfer is asserted.
