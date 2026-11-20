# OAI7 r409 — Absolute-margin near-critical Gaussian residue coverage

Date: 2026-11-20. Driver `EM-DVR-DEBB5E` author-side mathematical continuation of r408. **Not** independent Native Review, frozen Result or Task completion. Original task researcher `EM-EMF6D046-5A2844` remains credited.

## Sources and mathematical scope

Use the **exact same physical walk, Gaussian schedule and exact-start checkpoint family** from `openai/math@adc7f1241b42e322a6451854ab7e4b4c146bf78a:preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/schedule.tex` and the one-step transfer in its `build/coverage-transfer.tex`. The adaptive, first-moment based proof-only transfer lemma is r407, `awdawmip/enterprise-math@182a440dbc28de339922fa20f4cc36e3169234fc:research_notes/portable_direct/2026-11-20_oai7_028c_adaptive_information_deficit_shortlist_sampling_r407.md`. The weaker multiplicative-margin variant is r408, `awdawmip/enterprise-math@1477d13d87bf3926a1365225e91c9a89c27aa75b:research_notes/portable_direct/2026-11-20_oai7_028c_near_doubled_terminal_exception_exponent_r408.md`. These are author-side sources, not accepted Native Results.

## Theorem

For the source's original `M -> infinity` regime, for **each original batch `T`** set

```text
R_M := M^7,
b_i(T) := 2 beta_i - R_M/log T  (0 <= i <= J(T)).
```

For sufficiently large `M`, uniformly over every original batch, every `i<=J(T)` and **every exact checkpoint start time `a>=0`**, all except at most the original `eta_i` fraction of signed primes `pi` satisfy

```text
# {u in Z[i]/(pi) : b_(i,a,pi)(u) < tau_i/p} < p^(1-b_i(T)).
```

Here the italic `b_i(T)` is the new *exponent*, while `b_(i,a,pi)(u)` is the source notation for the conditional terminal probability. To remove that collision, denote the exponent by `alpha_i(T)=2 beta_i-M^7/log T` below. At the initial checkpoint, the new exceptional-set power is

```text
alpha_0(T) = 1/100 - M^7/log T,
```

strictly stronger than r408's `(2-M^(-10))/200` for every sufficiently large `M` and every original batch. In particular `alpha_0(T)=1/100-o(1)`, under the **same** floors `tau_0=1/4`, exceptional signed-prime fraction `eta_0=1/100`, exact-start order, and physical terminal-time law.

## Proof

All source bounds are uniform in batches and indices: `beta_i log T > M^20` for `i<J`, `M^20/2< beta_J log T <= M^20`, `r_i-r_(i+1)=2 beta_i`, `J=O(M)`, `log log T=O(M)`, exact-start joint entropy error `epsilon_i<=e^(-c M^3)`, displacement-support log size `<=C_D T^(r_(i+1))`, and `s_i L_*>e^(r_i log T-O(M^6))`.

**Terminal base.** `alpha_J(T) log T=2 beta_J log T-M^7 <=2M^20`, and is positive since `beta_J log T>M^20/2`. Each signed prime failing `(tau_J,alpha_J)` coverage differs from uniform by at least `(1-tau_J)p^(-alpha_J)` in TV, hence has KL deficit `>=c e^(-4M^20)` by Pinsker. The source's exact-start marginal KL average `<=L_*e^(-90M^20)` bounds the failure fraction by `e^(-86M^20+O(M))<eta_J`. Thus the strengthened base holds **at all exact starts**.

**Backward step.** Suppose `(tau_(i+1),alpha_(i+1))` holds at every exact start. Define the same r407 short-list parameter and a proof-only sampling count

```text
gamma_i = 2log(2e/delta_i)/log T,
n_i^(abs) = ceil( 2delta_i^(-2)(2T)^(alpha_i)
                    [gamma_i log(2T)+log(200/delta_i)] ).
```

Because `alpha_(i+1) log T = beta_i log T-M^7>M^20-M^7` for `i<J`, eventually `0<gamma_i<alpha_(i+1)` and `2/delta_i <= p^(alpha_(i+1)-gamma_i)`; `gamma_i log T=O(M)` and `log(2/delta_i)=O(M)`. By construction the conditional Chernoff bound obeys `exp[-delta_i^2 n_i^(abs) p^(-alpha_i)/2] <= (delta_i/200) p^(-gamma_i)` for every `p in [T,2T]`, while the list-entropy relation `log(2e/delta_i)=(gamma_i/2)log T` holds exactly.

The only nontrivial changed budget is shared-data entropy. Each auxiliary continuation displacement is supported in the original `D_(i+1)`. Thus, with `kappa_i=H(h_1,...,h_n)/(s_i L_*)`,

```text
log kappa_i <= alpha_i log T-(r_i-r_(i+1)) log T + O_D(M^6+M)
            = -M^7 + O_D(M^6+M).
```

The original `epsilon_i<=e^(-cM^3)`, together with `eta_i delta_i gamma_i>=e^(-O(M^2))`, ensures `epsilon_i+kappa_i<=eta_i delta_i gamma_i/8` for large `M`. All other r407 assumptions, including `tau_(i+1)=tau_i+4delta_i`, `eta_(i+1)<=eta_i delta_i/100`, signed-coordinate subset independence, and conditional iid repetitions given **the exact next checkpoint**, are unchanged. Apply r407 and descend from `J` to `0`.

This proof uses no added randomization in the physical walk, no unproved link to native X6 dynamics, and no custom axiom.

## Scope of improvement and boundary

The exponent can be pushed to `2 beta_0 - M^7/log T` because the original **geometry** provides an entropy headroom of `2 beta_i log T`, while the larger proof-only sample pays `alpha_i log T`. The residual `M^7` is larger than the source's `O_D(M^6)` entropy-loss exponent and leaves the r407 short-list budget ample room. This does **not** cover the exact endpoint `alpha_i=2 beta_i`, does not prove optimality and does not by itself claim downstream mother-objective or Native Result acceptance.

A genuinely independent reviewer should check the underlying fixed r407 transfer lemma and exact source schedule, particularly the parameter order `D -> fixed schedule constants -> M -> T -> i -> arbitrary exact start a`. Attribution and unfinished Source/Activity associations remain preserved.
