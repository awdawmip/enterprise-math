# S23 tagged-AV: a constructive all-parameter n^{-1/2} reconstruction-overlap bound

Date: 2026-11-06. Status: AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_CHECKS_EXECUTED / UNREVIEWED / NOT_ADMITTED.
Frozen scientific input: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34. Auxiliary conditional AV tagged model, not a claimed bridge to the original ten-label S23 mother problem. Predecessor: all-n lower convergence result in Draft PR #1777.

## Exact theorem

For `(a,c) in [1/2,7/8]^2`, set `z=(1-a)c`, `q=(1-a)(1-c)`, and `P_(z,q)=(1-z-q,z,q)` on tags `(stop1,stop3,stop4)`. Let `B_z=(z,1-z)` be the compressed experiment. With `n` independent repetitions sharing one unknown `(a,c)`, define

`delta_n = inf_{K: B^n -> P^n} sup_{(a,c)} TV(P_(z,q)^{tensor n}, B_z^{tensor n} K)`, where `K` is any parameter-independent stochastic kernel.

**Theorem:** For every integer `n >= 1`, there is an explicit parameter-independent stochastic kernel `K_n` such that

`sup_(a,c) TV(P_(z,q)^{tensor n}, B_z^{tensor n} K_n) <= 1 - C/sqrt(n)`,

where `C = (336/18755)*exp(-789/125) > 0`. Consequently,

`1-delta_n >= C/sqrt(n)`, for all `n >= 1`.

The kernel is constructed using only the observed compressed word and an independent uniform random variable. It is universal across the entire lawful parameter box, not only the fixed `z=1/4` hidden fiber.

## Explicit kernel

On receiving a compressed n-word `y`, count its observed `stop3` symbols and define `z_hat = clip((number of stop3)/n, [1/16,7/16])`. Draw `q_prime` uniformly in `[1/128,1/4]`, independently of `y`. Output `n` conditionally independent tagged symbols from the categorical distribution

`P_prime = (1-z_hat-q_prime, z_hat, q_prime)`.

This is always a valid probability vector: `z_hat >= 1/16`, `q_prime >= 1/128`, and `1-z_hat-q_prime >= 5/16`. A reconstruction kernel may output any valid tagged-word law; the random generating parameters need not themselves correspond to lawful `(a,c)`.

## Proof

The lawful parameter box implies

`1/16 <= z <= 7/16` and `1/64 <= q <= 1/4`.

For a fixed true `(z,q)`, the observed compressed indicators are i.i.d. Bernoulli(z); denote their empirical frequency by `z_bar`. Clipping cannot increase the distance to the true `z`, so

`E_z = {|z_hat-z| <= 11/(20 sqrt(n))}`

has probability at least `1 - (1/(4n))/(121/(400n)) = 21/121` by Chebyshev's inequality. Independently, since `q` belongs to `[1/128,1/4]`, an interval of length at least `1/(20 sqrt(n))` lies in `[1/128,1/4]` within distance `1/(20 sqrt(n))` of `q`. The support length is `31/128`, hence

`Pr(E_q) >= (1/(20 sqrt(n)))/(31/128) = 32/(155 sqrt(n))`,

where `E_q = {|q_prime-q| <= 1/(20 sqrt(n))}`. These events are independent.

On `E_z intersect E_q`, the one-symbol laws `P=(1-z-q,z,q)` and `P_prime` are strictly positive. The standard bound `KL(P||P_prime) <= chi_square(P||P_prime)` (from `log x <= x-1`) gives

`KL(P||P_prime) <= (16/5)(Delta_z+Delta_q)^2 + 16 Delta_z^2 + 128 Delta_q^2`,

because the three coordinates of `P_prime` are at least `5/16`, `1/16`, and `1/128`, respectively. Therefore

`n KL(P||P_prime) <= (16/5)(3/5)^2 + 16(11/20)^2 + 128(1/20)^2 = 789/125`.

Let `A(P,R)=sum_i sqrt(P_i R_i)` be Hellinger affinity. Jensen's inequality gives `A(P,R) >= exp(-KL(P||R)/2)`. Cauchy-Schwarz gives `TV(P^{tensor n},R^{tensor n}) <= sqrt(1-A(P,R)^{2n})`. For `0<=v<=1`, `1-sqrt(1-v)>=v/2`. Combining these inequalities on the good event,

`1-TV(P^{tensor n},P_prime^{tensor n}) >= (1/2) exp(-n KL(P||P_prime)) >= (1/2)exp(-789/125)`.

The actual reconstructed distribution `Q_z=B_z^{tensor n}K_n` is the mixture of `P_prime^{tensor n}` over `y` and `q_prime`. Since `R -> 1-TV(P^{tensor n},R)=sum_x min(P^{tensor n}(x),R(x))` is concave in `R`,

`1-TV(P^{tensor n},Q_z) >= E_{y,q_prime}[1-TV(P^{tensor n},P_prime^{tensor n})]`.

Restricting to the independent good events gives

`1-TV(P^{tensor n},Q_z) >= (21/121)*(32/(155 sqrt(n)))*(1/2)*exp(-789/125) = C/sqrt(n)`.

This holds uniformly over the lawful parameter box and every `n>=1`, completing the proof.

## Interpretation, verification, and next scientific question

This constructive upper bound for `delta_n` complements the earlier author-side asymptotic lower bound `delta_n >= 1-O(sqrt(log(n)/n))` for the same auxiliary model. Taken together, the reconstruction *overlap* `1-delta_n` lies between a positive constant times `n^{-1/2}` and an earlier certified upper bound of order `sqrt(log(n)/n)`. The logarithmic gap remains an exact open problem for this auxiliary experiment.

`VERIFY.py` performs exact rational arithmetic checks of the probability-domain bounds, Chebyshev and uniform-interval constants, the full KL/chi-square coefficient, and stress-tests the local chi-square inequality on a finite grid of lawful rational inputs and rational good-event shifts at square n. These finite tests support the algebra; the all-real/all-n statement follows from the proof above.

Observer/BRC scope: three tagged branches and their multiplicities are retained in the output; the compressed observation merges stop1 and stop4, while the kernel explicitly randomizes the missing q coordinate. All calculation here is ordinary exact probability algebra; no native heartbeat or BRC arithmetic primitive is asserted. The ten-label S23 mother-problem transfer awaits a valid encoder/decoder/observer bridge.
