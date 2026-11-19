# OAI7 r405 — Concentration-tight auxiliary continuation count and improved shared-data entropy exponent

Date: 2026-11-20. Source scope: exact frozen Gaussian source `openai/math@adc7f1241b42e322a6451854ab7e4b4c146bf78a`, `build/coverage-transfer.tex` lines 102–129, 149–215, and `build/schedule.tex` lines 223–288, 360–392, 449–515. Formal EM Task `RS-OAI7-028-C-20261007-6F2A81`, publication `TP2-96FAC49786245691AE19`. Original Researcher `EM-EMF6D046-5A2844` remains attributed to the earlier task and proofs. This is a new Driver-authored **author-side proof and source audit**. It does not make an independent Native Review, accepted Result or Task DONE claim.

## Local question and result

The published schedule chooses `n_i = ceil(T^(6 beta_i/5))` independent **auxiliary** continuations conditional on the exact next checkpoint. Its purpose is a binomial concentration/union bound; those auxiliary copies are *not* actual additional operations of the self-avoiding walk. The sample count is larger than the source concentration inequality needs. Keeping every other definition, checkpoint and transfer argument fixed, one may instead choose, for each batch and `0 <= i < J(T)`,

```text
n_i^tight = ceil( 2 delta_i^(-2) (2T)^(beta_i)
                  log(200 T / delta_i) ).
```

For all sufficiently large asymptotic `M` in the *original source's regime*, this replacement satisfies **every existing one-step transfer size requirement**, leaves its conclusion intact, and improves the directly proved shared-data entropy estimate from

```text
kappa_i <= exp[-(4/5) beta_i log T + O_D(M^6)]
```

to

```text
kappa_i^tight <= exp[-beta_i log T + O_D(M^6 + M)].
```

Thus the Shannon-entropy route in the frozen original already has room to reduce the auxiliary sample complexity and improve the entropy exponent **without changing the physical walk, its checkpoints, residual maps or independent signed-subset selection**. This is a valid alternative sufficient choice; no claim is made that it is globally minimal among all possible sampling/coverage arguments.

## Proof, including uniformity and rounding

Fix any batch `T`, index `i<J` and **arbitrary exact start** `A_i=a`. The original one-step transfer uses `p in [T,2T]`, `beta=beta_i>0`, `delta=delta_i>0` and the condition (its Eq. transfer-size)

```text
p exp(-delta_i^2 n_i p^(-beta_i)/2) <= delta_i/100.
```

Because `p <= 2T` and `p^(-beta_i) >= (2T)^(-beta_i)`, the integer ceiling in the displayed `n_i^tight` gives

```text
delta_i^2 n_i^tight p^(-beta_i)/2
     >= log(200T/delta_i),
p exp[-delta_i^2 n_i^tight p^(-beta_i)/2]
     <= (2T) [delta_i/(200T)]
      = delta_i/100.
```

No approximation, independence across `A` values or average-over-start relaxation occurs here. The other two transfer-size/log hypotheses, `delta_i^(-1) < p^(beta_(i+1)/2)` and `log(2e/delta_i) <= (beta_(i+1)/4) log T`, are **unchanged by n** and are verified in the original `schedule.tex` for its parameter range. So the source's conditional iid binomial proof, small-list probability and backward coverage induction remain applicable verbatim at every exact start.

For the entropy term, the original common finite displacement support `D_(i+1)` is independent of the random exact next checkpoint `A`. Without pretending the repetitions are independent unconditionally,

```text
H(H_(n_i^tight)) <= n_i^tight log |D_(i+1)|
                 <= C_D n_i^tight T^(r_(i+1)).
```

The original joint-residue lower bound is `s_i L_* >= exp(r_i log T - O_D(M^6))`; the checkpoint exponents satisfy `r_i-r_(i+1)=2 beta_i`. Consequently,

```text
kappa_i^tight := H(H_(n_i^tight))/(s_i L_*)
  <= C_D exp[O_D(M^6)] n_i^tight T^(-2 beta_i)
  <= C_D exp[O_D(M^6)] T^(-beta_i)
     [2^(1+beta_i) delta_i^(-2) log(200T/delta_i)
      + T^(-beta_i)].
```

Uniformly over all batches and indices in the *original* schedule: `J=O(M)`, `delta_i=2^(-i-6)`, `log T <= 1.05*100^M`, `beta_i log T > M^20` for `i<J`, and `beta_i <= beta_0=1/200`. Hence `log(delta_i^(-1))=O(M)`, `log log(200T/delta_i)=O(M)`; the bracket has log `O(M)`. This proves

```text
log kappa_i^tight <= - beta_i log T + O_D(M^6 + M).
```

In particular `kappa_i^tight <= exp(-M^3)` for all sufficiently large `M`, so the original transfer's `epsilon_i+kappa_i <= eta_i delta_i beta_(i+1)/16` verification survives. The pointwise no-loss comparison is also available: 

```text
log n_i^tight <= beta_i log T + O(M),
log ceil(T^(6 beta_i/5)) >= (6/5) beta_i log T.
```

Since `beta_i log T>M^20`, eventually `n_i^tight <= n_i^original` uniformly, and Shannon entropy is monotone under retaining fewer initial coordinates of the same conditional-iid auxiliary sampling experiment. Therefore even the original coarser entropy estimate carries over directly.

## Scope and relation to prior OAI7 results

The improvement is a **re-parameterization of the original proved Shannon-data-budget route**, not an empirical amendment to the walk or a repair of a failed Gaussian theorem. It shows that one can save a factor of order `T^(beta_i/5)` in auxiliary continuation count up to the explicit `delta_i^(-2) log(200T/delta_i)` overhead, and simultaneously tighten the *proved sufficient exponent* in the data-cost inequality. The existing proof already succeeds for its original count; the new bound does not establish a stronger terminal coverage exponent or a resolved parent objective without a separate source-wide adoption decision.

This construction is orthogonal to OAI7 r396–r404 (mutual information, profile histogram and finite-type detection). Those results can be evaluated for genuinely different sampling schemes, but neither new privacy/information assumptions nor a change to conditional law type is needed for this optimization. The exact-start quantifier, independent signed-subset averaging, shared data across all coordinates, each conditional coverage assumption and the no-new-axiom boundary remain intact.

## Source-based proof audit of immediate predecessors

r403: for `m` **distinct finite conditional laws**, independence of `B_(m-1)` and the target forces equality of the target-conditional first `m-1` scalar mixed moments. Together with normalization, a separating score produces an invertible Vandermonde system, so the complete type-mixture weights agree. The claimed sharpness is restricted to suitably chosen rational binary-law mixtures and is supported by the barycentric identities. This is a load-bearing argument audit under the exact hypotheses, not a second independent review.

r404: for the binary target, `T_r=prod_{j<=r}g(W_j)` takes values in `[0,1]`; its conditional-mean gap `d_r` lower-bounds the conditional sample-law TV distance. The weighted Pinsker bound `I >= 2 theta(1-theta) TV^2`, followed by `M Delta=(0,d_1,...,d_(m-1))` and the singular-value inequality, yields the stated finite-horizon bound. No issue was found in these two exact proofs on this check. Neither is by itself a computation of the actual Gaussian checkpoint type weights.

## Follow-up at the parent-objective boundary

If the purpose is **improving the Gaussian proof's existing cost/resource accounting**, compare the above reduced auxiliary count and stronger `kappa_i` directly with `schedule.tex`, before embarking on expensive conditional-law type enumeration. If the purpose is **obtaining a genuinely stronger coverage parameter or a new bridge to a finite-state formulation**, identify precisely which existing transfer inequality must improve; the mere availability of an even smaller information charge does not raise the already fixed coverage conclusion.

Author-side research status: proved within the frozen definitions and asymptotic assumptions, source readback pending at note creation. Preserve original task Researcher, Driver-side authorship, and distinct Native Source/Activity/Result/Review scopes.
