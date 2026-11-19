# OAI7-028-C r401 — Finite-type information saturation and a necessary budget test

Date: 2026-11-20. Status: Driver-side mathematical derivation and exact finite checks; not an independent Native Result/Review or formal task completion.

## Provenance and scope

Mother question: Gaussian-moat transfer of high joint residue entropy to quantitative residue coverage. Original Task `RS-OAI7-028-C-20261007-6F2A81` / publication `TP2-96FAC49786245691AE19`. Original researcher `EM-EMF6D046-5A2844` and historical contributions remain attributed. Mathematical inputs are the frozen `openai/math@adc7f1241b42e322a6451854ab7e4b4c146bf78a` `coverage-transfer.tex` and `schedule.tex`, and Enterprise Math r396 (`9725b1dab7c8d8fa293bab5f2eec54896020e729`), r398 (`23f2057225777f77409504e19c319e1e9c488176`) and r400 (`7cd30d089ec8297c3caa9652b539fed0c2f45ff7`). These Gaussian mathematical objects are external to the protected P000 native axes.

## Theorem: information saturation at identifiable conditional-law types

Let `A` be a finite random variable. Conditional on `A=a`, draw `W_1,...,W_n` iid on a fixed finite alphabet `W` with probability vector `q_a`. Let `V=q_A` be the **exact conditional-law type**, namely the vector `q_a` itself, and let its distinct possible values be `v=1,...,m` with positive prior weights `pi_v`. Define the histogram `B_n=(# {j: W_j=w})_{w in W}`. Logs are natural; zero-probability terms have their usual continuous interpretation.

For `m>=2`, set
```text
rho(u,v) = sum_{w in W} sqrt(q_u(w) q_v(w))     (u != v),
E_n = sum_{u<v} sqrt(pi_u pi_v) rho(u,v)^n,
e_n = min{1 - 1/m, E_n},
f_m(e) = h_2(e) + e log(m-1).
```
Then `0 <= rho(u,v) < 1` for distinct types, and for **every** deterministic observable `X=f(A)`,
```text
0 <= I(X;V) - I(X;B_n) <= f_m(e_n).
```
In particular,
```text
H(V) - f_m(e_n) <= I(A;B_n) = I(V;B_n) <= H(V).
```
Thus, for a fixed finite family of distinct laws, `I(X;B_n) -> I(X;V)` exponentially fast up to the entropy-continuity factor. For `m=1` all the quantities vanish.

**Proof.** For a realized word `w_1,...,w_n`, its likelihood under type `v` is `L_v=prod_j q_v(w_j)`. The multinomial likelihood of its histogram is `n!/(prod_w b_w!) prod_w q_v(w)^{b_w}`; the combinatorial factor is independent of `v`. Consequently the Bayes posterior of `V` depends only on `B_n` and the optimal classification error from ordered words is the same as that from `B_n`.

For any nonnegative class weights `z_v=pi_v L_v`, pointwise `sum_v z_v-max_v z_v <= sum_{u<v} min(z_u,z_v)`. Summing over words and using `min(x,y)<=sqrt(xy)` gives the MAP error bound
```text
P_e <= sum_{u<v} sqrt(pi_u pi_v)
          sum_{w_1,...,w_n} sqrt(prod_j q_u(w_j) q_v(w_j))
    = E_n.
```
A constant-class guess also shows `P_e<=1-max_v pi_v<=1-1/m`. Fano's elementary finite-class inequality yields `H(V|B_n)<=h_2(P_e)+P_e log(m-1)<=f_m(e_n)`; the last step uses monotonicity of `f_m` on `[0,1-1/m]`.

Because `V` is a function of `A` and `B_n` is conditionally independent of `A` given `V`, `I(A;B_n)=I(V;B_n)`. For `X=f(A)`, also `I(X;B_n|V)=0`, so the chain rule gives the **exact** gap identity
```text
I(X;V) - I(X;B_n) = I(X;V|B_n)
                           <= H(V|B_n) <= f_m(e_n).
```
The left side is nonnegative by data processing. Finally Cauchy-Schwarz gives `rho(u,v)<=1` with equality for probability vectors precisely when `q_u=q_v`, which distinct law types exclude. Finiteness completes the saturation claim. QED.

## Consequence for the pinned Gaussian coverage-transfer budget

At **each fixed exact start** in the original `schedule.tex`, put `A=A_{i+1}`, `W_j=psi(h_j)` (the common residue profile of the original conditionally independent continuation displacement), and `X_S=F_S(Y)` for a fixed signed subset `S`. Let `V_i=q_A` be the induced exact profile-law type and let `e_{i,n_i}` be the certified class-error bound above. Since `S` is selected independently of the fixed-start sampling experiment, the theorem applies to each `S`, and therefore
```text
E_S I(F_S(Y); V_i) - f_{m_i}(e_{i,n_i})
   <= E_S I(F_S(Y); B_{n_i})
   <= E_S I(F_S(Y); V_i).
```
Hence the proposed r396 information-budget replacement
```text
E_S I(F_S(Y); B_{n_i}) <= kappa_i s_i L_*
```
is **impossible for this original iid profile sampler** whenever the independently certified quantity
```text
E_S I(F_S(Y);V_i) - f_{m_i}(e_{i,n_i})
       > kappa_i s_i L_*.
```
This is a necessary feasibility test for that *information-budget route*, not a disproof of the original Gaussian coverage theorem or of alternative samplers/arguments. It supplements r400's upper certificates with a lower obstruction. In particular `H(V_i)` alone is not the obstruction: what matters for signed-residue coverage is `E_S I(F_S(Y);V_i)`, which may be much smaller. For a large, closely spaced family of `q_A`, the bound may be weak at the actual `n_i` even though asymptotic identification holds.

**Important exact-schedule limitation (audited against pinned `schedule.tex`, Eq. coverage-data-cost).** At the *unchanged original* schedule, `kappa_i` is defined by `H(H_i)/(s_i L_*)`, and the original proof already establishes
```text
E_S I(F_S(Y);B_{n_i}) <= H(B_{n_i}) <= H(H_i)
                         = kappa_i s_i L_* <= C_D n_i T^{r_{i+1}}.
```
Therefore the strict failure criterion immediately above **cannot trigger under the original schedule and its actual original kappa_i**. It is a discriminating test only for proposed **modified budgets, sample counts, displacement laws or schedules** not already covered by that Shannon-cost certificate. This scope is essential when interpreting r396–r401: an improved sufficient assumption need not improve a schedule whose stronger original assumption is already verified.

A positive structural consequence does follow at the original exact start: combining this old Shannon-cost certificate with r401's saturation inequality forces
```text
E_S I(F_S(Y); V_i)
    <= H(H_i) + f_{m_i}(e_{i,n_i})
    <= C_D n_i T^{r_{i+1}} + f_{m_i}(e_{i,n_i}).
```
Thus, whenever the actual finite law types are identifiable from the allowed sample count, the exact law type itself cannot reveal much more *signed-residue information* than the original shared-data cost, up to the explicit classification-error term. This does not bound the full `H(V_i)` by the same amount.

## Exact finite check (r400's two-type model)

Let `A=V` be uniform on two types, `W_j` Bernoulli with `q_0(1)=1/4`, `q_1(1)=3/4`. The exact affinity is `rho=sqrt(3)/2`. Thus `E_n=(1/2)(sqrt(3)/2)^n`. For each `n`, the full finite joint law is the pair of binomials:
```text
P(B_n=k|V=0)=binom(n,k) (1/4)^k (3/4)^(n-k),
P(B_n=k|V=1)=binom(n,k) (3/4)^k (1/4)^(n-k).
```
All count probabilities and MAP errors below are exact rationals; the mutual informations and Fano bounds are numerical evaluations of explicit finite logarithmic sums:

| n | Exact MAP error P_e | Affinity error E_n | Actual I(V;B_n), nats | Certified lower bound H(V)-h_2(E_n), nats |
|---:|---:|---:|---:|---:|
| 3 | 5/32 | sqrt(27)/16 | 0.309425366356 | 0.062742043128 |
| 10 | 6413/131072 | 243/2048 | 0.580021695271 | 0.328915927538 |
| 30 | 64284800975417/36028797018963968 | 14348907/2147483648 | 0.688546023210 | 0.653023188851 |

At `n=3`, `E_3=sqrt(27)/16`, i.e. `(1/2)(sqrt(3)/2)^3`; the table uses the same formula for all rows. In the binary case `f_2(e)=h_2(e)`. The upper limit is `H(V)=log 2` nats. For even `n`, tied binomial likelihoods are given equal Bayes weight; the error formula is unaffected by the tie convention. These results are reproducible by direct enumeration of `k=0,...,n` using the displayed rational binomial masses.

## Research decision, attribution, admission

This theorem is mathematical analysis of the existing iid sampling model, not a new hypothesis inserted into the original Gaussian paper. It identifies a quantifiable *lower* cost barrier complementary to the r396/r400 *upper* costs. The decisive unresolved original-input work is to bound the fixed-start family of profile laws `q_A`, their pairwise affinities, their identifiable type prior, and `E_S I(F_S(Y);V_i)` without replacing fixed-start quantifiers by averages across starts. Retain all original conditional coverage, geometric support and Chernoff hypotheses in a schedule comparison.

This is a Driver-side proof in a shared research/control context and uses prior r396/r398/r400 results. It is not an independent Source-native Result Review; Native Result admission, Author/Activity association and Task/mother-objective completion retain their separate authority.
