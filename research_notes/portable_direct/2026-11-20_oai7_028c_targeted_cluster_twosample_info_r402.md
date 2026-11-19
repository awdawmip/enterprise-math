# OAI7-028-C r402 — Target-specific clustered two-sample information certificate

Date: 2026-11-20. Status: Driver-side mathematical derivation and finite rational-law check; Source note only, not an independent Native Result Review or task completion.

## Fixed question, sources and provenance

Formal Task `RS-OAI7-028-C-20261007-6F2A81`, immutable publication `TP2-96FAC49786245691AE19`; original researcher `EM-EMF6D046-5A2844` retains all earlier contributions. Relevant frozen external inputs: `openai/math@adc7f1241b42e322a6451854ab7e4b4c146bf78a`, `coverage-transfer.tex` and `schedule.tex`. Immediate mathematical dependencies: Enterprise Math r396 (`9725b1dab7c8d8fa293bab5f2eec54896020e729`), r397 (`2858feef1b0ff44aa271216e21cf5a81c8451b64`), r398 (`23f2057225777f77409504e19c319e1e9c488176`), r400 (`7cd30d089ec8297c3caa9652b539fed0c2f45ff7`), and r401 (`aa0ef2db7546e5d2d87421738244666f41e26d6f`). No identification with native X6/Port structures is assumed.

The earlier cluster certificate r397 charges `H(C)` for a distribution cluster `C`, even when the selected residue observable `X` carries little information about `C`. The following theorem replaces that term by the **actual target–cluster mutual information** and subtracts the exact pair redundancy inside clusters.

## Theorem (target-aware clustered information charge)

Let `A` be a finite random variable, `X=f(A)` any finite deterministic observable, and `V=q_A` the exact finite conditional-law type on a common finite alphabet `W`. Conditional on `A=a`, let `W_1,...,W_n` be iid with law `q_a`. Define the complete profile histogram `B_n=(#\{j:W_j=w\})_{w\in W}`. Choose **any deterministic clustering** `C=g(V)`, with positive-probability clusters. For each cluster `c` define

- `mu_c(w)=E[q_A(w)|C=c]`;
- `Q_{2,c}(u,v)=E[q_A(u)q_A(v)|C=c]`;
- `K_C=E D_KL(q_A || mu_C)=I(V;W_1|C)`;
- `R_C=E_C D_KL(Q_{2,C} || mu_C tensor mu_C)=I(W_1;W_2|C)`.

All logarithms are natural, and `n>=2`. Then
```text
0 <= I(X;B_n)
   <= min{ I(X;V), I(X;C) + n K_C - (n-1) R_C }
   <= I(X;C) + n K_C.
```
For `n=1` omit `R_C`. In particular, if `I(X;C)=0`, the cluster label incurs **zero** information cost for this target, regardless of its Shannon entropy.

**Proof.** Conditional on `V`, the sample law depends on `A` only through `q_A`. Hence `X - V - (W_1,...,W_n)` is a Markov chain. The histogram is sufficient for `V` under conditional iid sampling, so `I(V;B_n|C)=I(V;W_1,...,W_n|C)`. Since `C=g(V)`, the chain rule and data processing yield
```text
I(X;B_n)
 <= I(X;B_n,C)
  = I(X;C)+I(X;B_n|C)
 <= I(X;C)+I(V;B_n|C).
```
For each fixed `C=c`, the sample is exchangeable, and conditionally iid given `V`. By successive entropy chain rules,
```text
I(V;W_1,...,W_n|C)
 = n I(V;W_1|C)
   - sum_{j=2}^n I(W_j;W_1,...,W_{j-1}|C).
```
Every summand is at least `I(W_j;W_1|C)=I(W_1;W_2|C)=R_C` (conditional data processing and exchangeability). This proves the two-sample upper bound. The expressions for `K_C` and `R_C` follow from the conditional one- and two-sample mixture laws. Independently, data processing gives `I(X;B_n)<=I(X;V)`. Nonnegativity of mutual information concludes the theorem. QED.

This is also a refinement of r400 at the cluster level: for constant `C` its two-sample term reduces to r400; replacing `I(X;C)` with `H(C)` and omitting the pair correction recovers the coarse r397-style charge.

## Fully specified rational-law witness

Let `A=(U,T)` with independent fair bits `U,T`, set `X=U`, and sample conditional Bernoulli `W_j` with
```text
P(W_j=1|U=u,T=t) = q_(u,t)
q_(0,0)=249/1000, q_(1,0)=251/1000,
q_(0,1)=749/1000, q_(1,1)=751/1000.
```
All four laws are distinct, so `V=q_A` identifies `A`. Choose `C=T`. Then `I(U;C)=0` exactly, `H(C)=log(2)`, and `mu_0(1)=1/4`, `mu_1(1)=3/4`. Every probability is rational.

The exact finite-sum definitions give
```text
K_C = (1/4) sum_(u,t) D_KL(Bern(q_(u,t)) || Bern(mu_t))
    = 0.0000026666721976069483... nats

R_C = (1/2) sum_t sum_(x,y in {0,1})
        Q_(2,t)(x,y) log[ Q_(2,t)(x,y) /
                          (mu_t(x) mu_t(y)) ]
    = 0.000000000014222132999340518... nats.
```
At `n=10`, the **new certified bound** is
```text
I(U;B_10) <= 10 K_C - 9 R_C
          = 0.00002666659397687249... nats.
```
The r397 cluster charge using the same `C` is `H(C)+10 K_C = 0.69317384728... nats`. Direct enumeration of the 11 histogram counts yields
```text
I(U;B_10) = 0.000015051363888956296... nats.
```
For reproducibility, set
```text
P(B_n=k | U=u)
 = (1/2) sum_(t=0,1) binom(n,k) q_(u,t)^k (1-q_(u,t))^(n-k).
```
Insert these exact rational masses into
`I(U;B_n)=(1/2) sum_(u,k) P(k|u) log[P(k|u)/((P(k|0)+P(k|1))/2)]`.
All quoted decimals evaluate those finite sums; the inequalities are analytic, not inferred from rounding.

## Exact-start Gaussian application and unresolved quantitative input

At one **fixed starting time** `A_i=a` in the source `schedule.tex`, take its random next checkpoint `A=A_{i+1}`, the original conditional iid continuation profile `W_j=psi(h_j)`, and for each fixed independently selected signed subset `S` let `X_S=F_S(Y)`, `Y=z_A`. Select one cluster `C=g(q_A)` before choosing `S`; it is shared across all coordinates. Averaging the theorem over independent `S` yields
```text
E_S I(F_S(Y);B_(n_i))
 <= min{ E_S I(F_S(Y);V_i),
         E_S I(F_S(Y);C) + n_i K_C - (n_i-1)R_C }.
```
Thus a sufficient check for the r396 refined conditional-information budget is that the right side be at most `kappa_i s_i L_*`. The same `B_n` remains sufficient for the coordinate-wise candidate lists by r398. The existing original Gaussian schedule already proves the stronger Shannon-data-cost inequality, and is not challenged by this refinement.

The **new testable issue** is whether the actual fixed-start Gaussian conditional profile laws admit a cluster `C` for which the selected-residue information `E_S I(F_S(Y);C)` and the within-cluster KL cost are jointly small. Cluster cardinality alone is not the decisive information cost. Retain exact-start uniformity, conditional coverage, shared-sample/Chernoff conditions and geometric support before asserting an improved schedule. This note supplies the structural inequality and one exact finite witness, not a computed improvement to the pinned Gaussian parameters.

## Admission and contribution boundaries

This is Driver-side author research in a shared scientific context, not an independent peer review. Preserve the original researcher's authorship and all prior Driver/researcher contributions. GitHub publication is Source evidence only; Native Result intake, Source/Activity association, independent Review, formal Task completion and mother-objective closure must be handled separately by the current authorized contracts.
