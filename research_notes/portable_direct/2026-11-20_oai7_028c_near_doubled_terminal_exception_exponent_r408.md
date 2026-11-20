# OAI7 r408 — Near-doubling the terminal residue exception exponent on the unchanged Gaussian schedule

Date: 2026-11-20. Research type: Driver-authored, mathematical **author-side proof**. No Native Result, independent review, Task DONE, or parent-objective completion is asserted.

## Exact inputs and attribution

- Frozen external theorem: `openai/math@adc7f1241b42e322a6451854ab7e4b4c146bf78a:preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/coverage-transfer.tex`, the one-step transfer and conditioning/list lemmas.
- Frozen external schedule: same commit and directory, `build/schedule.tex`, checkpoint parameters, the exact-start joint entropy estimate, displacement support and terminal base.
- Adapted one-step transfer: `awdawmip/enterprise-math@182a440dbc28de339922fa20f4cc36e3169234fc:research_notes/portable_direct/2026-11-20_oai7_028c_adaptive_information_deficit_shortlist_sampling_r407.md`; the r406 Markov-count ancestor is `@5e5382d171afe3b389176bc094b88d94ab6f5900:research_notes/portable_direct/2026-11-20_oai7_028c_markov_small_list_sampling_refinement_r406.md`.
- Current formal Task: `RS-OAI7-028-C-20261007-6F2A81`, publication `TP2-96FAC49786245691AE19`. Original scientist `EM-EMF6D046-5A2844` retains their contribution. Present author-side continuation is `EM-DVR-DEBB5E`; shared-context checking is **not** independent review.

## Theorem (fixed physical schedule, stronger exceptional-set exponent)

Fix the source's `D`, its constants, physical walk and **the identical schedule** of stochastic enrichments, exact checkpoints `A_0,...,A_J`, and the common terminal time `t_*`. For each sufficiently large source parameter `M`, let

```text
theta_M := 2 - M^(-10)
alpha_i := theta_M beta_i       (0 <= i <= J),
beta_i := 2^(-i)/200            (original schedule beta),
r_i-r_(i+1) = 2 beta_i          (original checkpoint spacing).
```

With the original probability floors `tau_i` and exceptional-coordinate fractions `eta_i`, **for every batch `T`, every checkpoint `0 <= i <= J(T)` and every exact start `a >= 0`**, all but at most an `eta_i` fraction of signed primes `pi` in the batch obey

```text
# {u in Z[i]/(pi) : b_(i,a,pi)(u) < tau_i/p} < p^(1-alpha_i).
```

In particular, at `A_0` the original `beta_0=1/200` can be replaced by `(2-M^(-10))/200` with **no change** to `tau_0=1/4`, `eta_0=1/100`, physical walk, actual schedule or exact-start quantifier. This is an **asymptotic** improved sufficient coverage result; it is not a claim that the new exponent is sharp.

## Proof

**1. The terminal base survives the strengthened target.** The original schedule gives for every exact start at `A_J` an average marginal KL deficit at most `exp(-90M^20)L_*`. A signed coordinate failing `(tau_J,alpha_J)` coverage has a low-probability set of cardinality at least `p^(1-alpha_J)`. Its total variation from uniform is at least `(1-tau_J)p^(-alpha_J)`. Since `alpha_J log T <= theta_M M^20 < 2M^20`, and `p <= 2T`, Pinsker yields a KL deficit at least `c exp(-4M^20)`, with an absolute `c>0` eventually. Consequently the fraction of failing signed coordinates is at most `C L_* exp(-86M^20) = exp(-86M^20+O(M)) < eta_J`. Here `log L_* = O(M)` and `eta_J >= exp(-O(M^2))`, as in the source. This proves the desired stronger base without altering the bottom-band schedule.

**2. New proof-only auxiliary continuations.** For each backward step `i<J`, keep the exact original experiment from an arbitrary `A_i=a`: let `A=A_(i+1)`, `Y=z_A` and independently resample physical continuation displacements conditional on the exact `A`. The resampling count is selected for the stronger terminal exponent:

```text
L_i := log(2e/delta_i);
gamma_i := 2L_i/log T;
n_i^+ := ceil( 2 delta_i^(-2) (2T)^(alpha_i)
               [gamma_i log(2T)+log(200/delta_i)] ).
```

The `n_i^+` independent continuation copies are **auxiliary proof data** and do not change the actual walk or the prescribed schedule.

Apply r407's adaptive transfer with terminal exponent `beta=alpha_i`, next-checkpoint exponent `beta'=alpha_(i+1)`, original `tau_i`, `delta_i`, `eta_i`, `eta_(i+1)`, and `gamma=gamma_i`. Verify all r407 conditions:

- `0<gamma_i<alpha_(i+1)` and `2/delta_i <= p^(alpha_(i+1)-gamma_i)`: indeed `beta_i log T > M^20` for `i<J`, `alpha_(i+1) log T = theta_M beta_i log T /2 > M^20/2` eventually, whereas `gamma_i log T = 2 L_i = O(M)` and `log(2/delta_i)=O(M)`. Uniform in batches and indices.
- The conditional-binomial tail `q_p=exp[-delta_i^2 n_i^+ p^(-alpha_i)/2]` satisfies `q_p <= (delta_i/200)p^(-gamma_i)` for every `T<=p<=2T`, directly from the chosen ceiling and `p<=2T`.
- `log(2e/delta_i)=(gamma_i/2)log T` exactly.
- The original exact-start high joint entropy yields `epsilon_i <= exp(-cM^3)`, uniformly. The original unconditional displacement support at `A_(i+1)` and `s_i L_* >= exp(r_i log T-O(M^6))` imply
  ```text
  kappa_i^+ <= C_D n_i^+ T^(r_(i+1))/(s_i L_*)
            <= exp[ -(2-theta_M) beta_i log T + O_D(M^6+M) ].
  ```
  This uses the **unchanged** original identity `r_i-r_(i+1)=2 beta_i`; the modified `alpha_i` is not substituted into the checkpoint spacing. Because `2-theta_M=M^(-10)` and `beta_i log T>M^20`, the leading negative exponent is less than `-M^10`, dominating the `O_D(M^6+M)` term. Hence `kappa_i^+ <= exp(-c'M^10)` for large `M`. On the other hand, `eta_i delta_i gamma_i >= exp(-O(M^2))`, since `J=O(M)`, `log(1/delta_i)=O(M)`, and `log log T=O(M)`. Thus `epsilon_i+kappa_i^+ <= eta_i delta_i gamma_i/8` eventually. This is r407's exact gamma-dependent information condition.

All assumptions, including signed-subset independence and `eta_(i+1)<=eta_i delta_i/100`, now hold. The adaptive transfer proves `(tau_i,alpha_i)` coverage for the fixed exact start from `(tau_(i+1),alpha_(i+1))` at every next exact start. Descending induction from Step 1 completes the assertion simultaneously for every original batch and exact checkpoint.

## Boundary, significance and pending admission

The original `beta_0=1/200` was **not an intrinsic terminal-coverage limit** of this frozen schedule; using proof-only auxiliary sampling, its lower bound can be made `(2-o(1))/200` while preserving the original floors, signed-prime exceptional fraction, and physical law. The proof reveals the essential available headroom: the original checkpoint displacement margin is `(r_i-r_(i+1))log T=2 beta_i log T`, while the auxiliary count spends approximately `alpha_i log T`. This argument requires a **strict** margin `(2-theta_M)beta_i log T >> M^6`; it does not prove the endpoint `theta=2` or optimality.

The scope is the terminal coverage proposition, not automatic improvement of all later theorem constants or acceptance of the Gaussian moat mother result. A completely independent Native Review must inspect the exact theorem/pins/quantifiers, especially the order `D, fixed constants, M, T, i, a` and the uniform `M` estimates. The original Researcher remains credited; no new CLAIM or formal Result was issued.
