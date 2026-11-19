# OAI7 r404 — Quantitative finite-horizon target-information lower bound

Date: 2026-11-20 (Asia/Shanghai). Scientific context: `RS-OAI7-028-C-20261007-6F2A81`, original researcher `EM-EMF6D046-5A2844`. This is **Driver-authored mathematical research**, not independent review or a frozen/native accepted Result. It refines [r403](2026-11-20_oai7_028c_finite_sample_target_disclosure_delay_r403.md), preserving the shared-source contribution history.

## Theorem

Let `X` be a Bernoulli target, `P(X=1)=theta in (0,1)`, and `V` take `m>=2` exact, pairwise distinct conditional probability-law types `q_1,...,q_m` on a finite profile alphabet `Omega`. Conditional on `V`, `W_1,...,W_n` are iid with law `q_V`, and `X -> V -> (W_j)` is Markov. Let `B_n` be the sample histogram.

Choose a score `g:Omega->[0,1]` with distinct expectations `lambda_v=E[g(W)|V=v]`. Such scores exist, since equalities between any two expectations exclude only finitely many proper hyperplanes in the cube. Define `Delta_v=P(V=v|X=1)-P(V=v|X=0)`, `d_r=sum_v Delta_v lambda_v^r` for `1<=r<=m-1`, and the square Vandermonde matrix `M=(lambda_v^r)_(0<=r<=m-1,1<=v<=m)`. Its smallest singular value `sigma_min(M)` is positive.

Then, in natural logarithm units,

```text
I(X;B_(m-1)) >= 2 theta(1-theta) max_(1<=r<=m-1) d_r^2
              >= [2 theta(1-theta)/(m-1)] sigma_min(M)^2 sum_v Delta_v^2.
```

For any finite target `X`, the same certificate can be applied to an arbitrary binary event `Z=1_{X in E}`, and data processing gives `I(X;B_(m-1)) >= I(Z;B_(m-1))`. Thus one can maximize over valid target partitions.

## Proof

For `r<=m-1`, the statistic `T_r=prod_(j=1)^r g(W_j)` belongs to `[0,1]`. Conditional iid sampling gives `E[T_r|X=x]=sum_v P(V=v|X=x) lambda_v^r`, hence the difference between the two target-conditional expectations is `d_r`. Therefore their total variation distance is at least `|d_r|`.

Conditional on `X=x`, the law of each ordered word is a mixture `sum_v P(V=v|X=x) prod_j q_v(w_j)`, which depends on the word only through its histogram. Consequently `I(X;B_r)=I(X;W_1,...,W_r)` and, by projecting the prefix, `I(X;B_(m-1))>=I(X;B_r)`.

Write `P_x=L(W_1,...,W_r|X=x)` and `P=(1-theta)P_0+theta P_1`. Pinsker in nats gives
```text
I(X;W_1,...,W_r)
= (1-theta)D(P_0||P)+theta D(P_1||P)
>= 2 theta(1-theta) TV(P_0,P_1)^2
>= 2 theta(1-theta) d_r^2.
```
Since `sum_v Delta_v=0`, the vector `M Delta` is `(0,d_1,...,d_(m-1))`. Vandermonde invertibility gives `sum_(r=1)^(m-1) d_r^2 >= sigma_min(M)^2 sum_v Delta_v^2`; the maximum is at least the mean. QED.

## Exact sharpness-context witness

For the r403 three-type example, let `X` be fair. Given `X=0`, choose Bernoulli type `q=0` or `q=1` equally; given `X=1`, choose `q=1/2`. For score `g(w)=w` and type ordering `(0,1/2,1)`, `Delta=(-1/2,1,-1/2)`, `d_1=0`, `d_2=-1/4`. Hence
```text
I(X;B_1)=0.
I(X;B_2)=log 2 - (3/4) h_2(1/3) = 0.2157615543388357... nats.
r404 lower bound: 2*(1/2)*(1/2)*(1/4)^2=1/32 nats.
```
The entropy value comes from an exact finite mass formula; only the decimal evaluation is approximate. The example proves that r400's decreasing-increment property for the full exact type must not be applied automatically to an arbitrary selected residue target `X`. r402's target-aware *upper* certificate remains valid, and r404 supplies a complementary finite-sample *lower* certificate.

For the pinned [Gaussian coverage transfer](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/build/coverage-transfer.tex), applying this theorem quantitatively would require actual fixed-exact-start profile-law types and target-conditional mixing probabilities, preserving independent signed-subset selection, conditional coverage, event tails and geometric inputs. No original-schedule budget failure or improvement is asserted. Scientific context: [r396](2026-11-20_oai7_028c_information_theoretic_cost_refinement_r396.md), [r402](2026-11-20_oai7_028c_targeted_cluster_twosample_info_r402.md), [r403](2026-11-20_oai7_028c_finite_sample_target_disclosure_delay_r403.md).

Native Source/Activity association, frozen Result, independent review, Task DONE and parent completion remain pending their separate current operation contracts.
