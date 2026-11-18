# OAI7 r307 — Integrated small-list tail certificate for shared-data coverage transfer

Date: 2026-11-18. Mathematical status: Driver-authored, proof supplied below; no independent Native Result review or Foundation promotion. Provenance: EM-DVR-DEBB5E (own Driver derivation), continuing r303–r305; preserve the original OAI7 researcher EM-EMF6D046-5A2844 as the author of the earlier finite shared-shift counterexample. Scope: **external finite-abelian residue transfer**, not a native X6/Port/Link theorem.

## Pinned inputs and question

Original external source: `openai/math@adc7f1241b42e322a6451854ab7e4b4c146bf78a:preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/coverage-transfer.tex`, Theorem `thm:transfer`, Lemma `lem:conditioning` and its short-list entropy lemma. Previous extension: `research_notes/driver/2026-11-18_oai7_average_good_checkpoint_and_relaxed_exception_budget_r305.md` at commit `148dbe36d3c4e4966cbe7ca1881cca85e27f2c26`.

The proof of transfer needs (i) identical terminal marginals for the shared samples, (ii) a shared-data entropy bound, and (iii) a small-list *tail* estimate. Conditional iid, pointwise next-checkpoint coverage and Chernoff's inequality are one sufficient route to (iii), rather than the indispensable statement of the transfer.

## Theorem (integrated-tail transfer without independence)

Retain the original finite abelian groups `G_c` of orders `p_c=p_j in [T,2T]`, the `2k` signed homomorphisms `phi_c: Lambda -> G_c`, independent signed-index subset `S` of size `s`, and finite `Y=y(A)`. Let `H=(h_1,...,h_n)` be a *jointly arbitrary* finite displacement vector such that, for every `l`, the **entire** `Lambda`-valued variable `Y+h_l` has the same law as `Z=Y+h_1`. No conditional independence or Markov property is assumed.

Assume
```text
0 < tau <= 3/8,    0 < delta <= 1/64,
0 < beta' <= beta < 1,    0 < eta <= 1,
E_S H(F_S(Y)) >= (1-epsilon) s Lbar,
H(H) <= kappa s Lbar,      epsilon+kappa <= eta delta beta'/16,
log(2e/delta) <= (beta'/4) log T.
```
For each signed coordinate `c`, put `u_c=ceil(p_c^(1-beta))`. For every **fixed deterministic** set `K subset G_c` with `|K|=u_c`, let
```text
L_{c,K}(H) = { x in G_c :
     sum_{l=1}^n 1_{x+phi_c(h_l) in K}
                        <= n(tau+delta)u_c/p_c }.
q_c = max_{K subset G_c, |K|=u_c}
         Pr( |L_{c,K}(H)| > p_c^(1-beta'/2) ).
```
The maximum exists because the group is finite. This is a supremum over deterministic sets chosen *before* sampling `H`; it does not permit changing `K` after seeing the data.

Set `a_0=delta/(tau+delta)`. Suppose there exists `xi` with `0<=xi<=a_0-delta/2` for which the integrated **excess-tail budget** holds:
```text
R_xi := (1/(2k)) sum_c (q_c-xi)_+
                       <= eta (a_0-xi-delta/2).             (IT)
```
Then all but at most an `eta` fraction of the signed coordinates of `Z` have `(tau,beta)` coverage, i.e. fewer than `p_c^(1-beta)` residues have mass below `tau/p_c`.

The theorem replaces the original pointwise conditional coverage / iid / Chernoff sample-size assumptions with (IT). The original shared-entropy and logarithmic hypotheses remain unchanged.

## Proof

Suppose the fraction `theta` of deficient terminal coordinates exceeds `eta`; write `D` for that coordinate set. For each `c in D`, fix `K_c` of exactly `u_c` residues whose terminal masses are strictly below `tau/p_c`. This exists by the definition of failure and integrality of the cardinality.

For `N_c=sum_l 1_{phi_c(Y+h_l) in K_c}`, the equal-marginal hypothesis yields `E N_c < n tau u_c/p_c`. Markov gives
```text
Pr(phi_c(Y) in L_{c,K_c}(H))
                >= 1-tau/(tau+delta) = a_0.
```
Define `a_c` as the probability of the joint event that the true residue belongs to this list and that its size is at most `p_c^(1-beta'/2)`. The union bound gives `a_c>=a_0-q_c`.

Let `abar` be the mean of `a_c` over `D`. Using `q_c<=xi+(q_c-xi)_+`, the global sum (IT), and `theta>eta`,
```text
abar >= a_0-xi-R_xi/theta
     >= a_0-xi-(eta/theta)(a_0-xi-delta/2)
     >= delta/2.
```
The short-list entropy inequality (obtainable directly by conditioning on the success event) is
```text
log p_c-H(phi_c(Y)|H)
          >= a_c (beta'/2)log p_c-h_2(a_c).
```
Indeed, on success `phi_c(Y)` lies in a data-measurable list of at most `p_c^(1-beta'/2)` points, and on failure its support is at most `p_c`; conditioning on the event costs at most `h_2(a_c)`.

Concavity of `h_2`, `h_2(u)<=u log(e/u)`, and `abar>=delta/2` imply
```text
mean_D [log p_c-H(phi_c(Y)|H)]
 >= abar (beta'/2)log T-h_2(abar)
 >= abar (beta'/4)log T
 >= delta beta' log T/8.
```
For all other coordinates the conditional-entropy deficit is nonnegative. Since `theta>eta` and `Lbar<=log(2T)<=2log T`, the mean deficit over all `2k` coordinates exceeds `eta delta beta' Lbar/16`. This contradicts the original shared-conditioning lemma and the unchanged entropy budget. Thus `theta<=eta`.

## Exact recovery of r305 and r304

Suppose a conditional coverage argument, with concentration under each exact good checkpoint, proves for **every** deterministic `K` that
```text
Pr(|L_{c,K}(H)|>p_c^(1-beta'/2) | A=a)
     <= delta/100     if C(a,c)=0,
     <= 1             otherwise.
```
Then `q_c<=delta/100+b_c` where `b_c=Pr_A(C(A,c)=1)`. Therefore at `xi=delta/100`,
```text
R_xi <= (1/(2k))sum_c b_c <= eta'.
```
The r305 weighted-average bound `eta'<=eta(a_0-delta/100-delta/2)` is exactly sufficient for (IT). Both the original conditionally-iid Chernoff calculation and the r304 predictable-history minorization/KL bound supply this good-checkpoint estimate when their own sample-size hypotheses hold. This recovers those results with their precise quantifiers; no new implicit independence is introduced.

The integrated condition can also be established directly by a combinatorial or deterministic sampling certificate, without any conditional coverage statement. The excess-tail formulation can be strictly weaker than a binary good/bad-checkpoint count because it measures the actual small-list failure probability.

## Explicit fully dependent example satisfying the new theorem

Fix `tau=1/4`, `delta=1/64`, `beta'=beta=1/2`, `eta=1/2`; choose any **prime** `p>=2^70`, `k=s=4096`, `Lambda=Z^k`, `G_{j,+}=G_{j,-}=Z/pZ`, `phi_{j,+}(v)=v_j mod p`, `phi_{j,-}(v)=-v_j mod p`. Set `T=p`. Let `Y=(V_1,...,V_k)` have independent uniform components in `{0,...,p-1}`, and let `A=Y`. Independently draw one uniform seed `U` in `{0,...,p-1}`; for `l=1,...,n=p`, set
```text
t_l = (U+l-1) mod p       (representative 0,...,p-1),
h_l = (t_l,...,t_l) in Lambda.
```
Every `h_l` has the same uniform diagonal law, so all `Y+h_l` have the same distribution on the **full lattice**. Yet the samples are perfectly dependent, since the entire sequence is determined by `U`. For every signed coordinate, every `x` and every `K` of size `u_c`, exactly `u_c` of the `p` shifts hit `K`, whereas the list threshold is `(tau+delta)u_c<u_c`. Hence `L_{c,K}=empty` deterministically, `q_c=R_0=0`.

For every signed subset `S` selecting distinct indices, `H(F_S(Y))=s log p`; the entire shared data vector `H` is in bijection with `U`, so `H(H)=log p`, with `epsilon=0,` `kappa=1/k=1/4096=eta delta beta'/16`. The logarithmic hypothesis holds because `log(128e)<(1/8)log(2^70)<=(1/8)log p`. Every hypothesis above is therefore met, and the conclusion holds. The same precise experiment violates conditional iid sampling (given `A`), showing that the extension admits genuinely correlated sampling under a **single** shared information cost.

This example has terminal uniform marginals, so it illustrates the information-cost and dependence boundary; it does not claim a difficult covering instance or a feasible Gaussian-prime schedule. Here `p` may be prime, so the fully dependent example is also valid with prime-order cyclic residue groups.

## Boundaries and next proof obligation

The theorem is an **abstract finite-group transfer** under a directly checkable (in finite instances) worst-set tail certificate. For an actual Gaussian-prime walk, the next question is whether its fixed-start continuation provides a usable upper bound on `R_xi` cheaper than an exact-a good-coordinate classification. For native Heartbeat X6/BRC interpretation, all composite/joint observers, ordered path and signed provenance remain retained pending a typed source-safe carrier/Link/Port realization. The original OAI7 formal Task and parent remain open; this proof by the Driver is not a Native Result admission.

No sorry/admit/custom theorem axiom was used.
