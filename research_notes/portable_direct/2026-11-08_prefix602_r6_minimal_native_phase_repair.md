# PREFIX-602-R6 — Sharp minimal repair of singular native BRC phase observers

Date: 2026-11-08 Asia/Shanghai. Science pin: `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Status: AUTHOR_PROVED / EXACT_NATIVE_CERTIFICATE_EXECUTED / UNREVIEWED / NOT_ADMITTED.
Native primitive: `PREFIX565_positive_marginal_certificate.py`, verified Git blob `7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41`. Dependencies: PREFIX-600 native incidence theorem and PREFIX-601 twelve-incidence weighted phase-discriminant theorem.

## Question

PREFIX-601 identified six independent singular strata for the *parameterized native-action-graph deformation* of the original 48-phase BRC transition, with 12 nonnegative incidence weights `t_e`. For `k` critical reciprocal incidence pairs (`4t_et_f=1`), the normalized Markov matrix `P(t)` has rank `48-2k`. Find the minimum number of additional *linear initial-phase statistics* that, combined with the full next-phase distribution `pi P(t)`, recover every initial 48-phase probability law. Construct these statistics using the original typed incidence data, rather than an arbitrary Gaussian-elimination complement.

The source action types, signs, native branches and ordered phases remain available in `PREFIX565`; only the declared one-step phase marginal is under compression. The original frozen kernel is exactly the all-`t=1` section.

## Theorem — sharp 2k repair coordinates

For nonnegative 12-vector `t`, set `B(t)=W+UDV`, `S=diag(1+2t_{e(i)})`, `Q_B=S^{-1}B(t)`, and `P(t)=[0 Q_B;Q_B 0]` in the two sign-block phase ordering. Let `k` be the number of reciprocal incidence pairs `{e,f}` with `4t_et_f=1`.

Then there exist **explicitly constructible 2k rational-coefficient linear statistics** `r_j(pi)=sum_i pi_i ell_{j,i}` (rational whenever the weights are rational), such that

`pi -> (pi P(t),r_1(pi),...,r_{2k}(pi))`

is injective for all 48-phase probability distributions. **No smaller number than 2k additional linear statistics suffices**, even when the domain is restricted to the strictly positive normalized probability simplex. Consequently the exact minimal repair count is `2k`, ranging from 0 at the original frozen kernel to 12 at the homogeneous `t_e=1/2` singular kernel.

## Direct native-incidence construction and proof

Write `D=diag(t_e)`. From the original native BRC phase graph,

`V W^{-1} U = 2J`, where `J` swaps six disjoint incidence pairs.

Choose any critical pair `{e,f}` and the row incidence vector `u^{ef}` with entries

`u_e=1, u_f=-2t_e`, all others zero.

The critical relation `4t_e t_f=1` gives exactly

`u(I+2DJ)=0`.

Set

`w=-u D V W^{-1}`.

Then `wU=-2uDJ=u`, so the map `u -> w` is injective on the critical-pair subspace. Moreover

`w B(t)=wW+wUDV=-uDV+uDV=0`.

Define `ell=wS`. It follows that

`ell Q_B=(wS)(S^{-1}B)=wB=0`.

The `k` vectors `ell` built from distinct critical pairs are independent. Lift each into the positive and negative 24-phase sign blocks of `P`; the resulting `2k` vectors form a basis `L` of the left nullspace of `P`, because PREFIX-601 proved `nullity P=2k`.

Let these row vectors be `ell_1,...,ell_{2k}`. If two probability rows `pi,pi'` have equal phase readout, their difference `d=pi-pi'` lies in `L`. If the 2k added repair readings are also equal, then `d ell_j^T=0` for all `j`. Writing `d=sum_j c_j ell_j`, this is `cG=0`, where `G_{ij}=ell_i ell_j^T` is a positive definite Gram matrix of independent real rows. Thus `c=0`, `pi=pi'`. This also gives a reconstruction: find any phase row `pi_0` with `pi_0P=z`, then solve `G c = r-r(pi_0)`, and put `pi=pi_0+sum c_i ell_i`.

For the lower bound, any additional `m<2k` real linear measurements have a nonzero common kernel direction `d in L`. Since `P1=1`, necessarily `d1=0`. The strictly positive uniform probability law `u` admits both `u+epsilon d` and `u-epsilon d` as distinct strictly positive laws for sufficiently small rational/real `epsilon>0`, and these share the original one-step phase readout plus all `m` measurements. Therefore `m>=2k` is necessary. QED.

This is a **linear repair bound for the next-phase marginal**. The proof neither merges original native action labels nor asserts full seven-reward equality. If all original phases are reconstructed, later *phase-only* operations with a specified kernel can use that restored law; branch- and action-aware operations require their corresponding original information.

## Exact executed certificate

The stdlib `Fraction` checker composes the verified native PREFIX-565 graph, PREFIX-600 incidence proof, and PREFIX-601 parameterized graph and independently constructs `P(t)`, every critical-pair repair row, the 48x(48+2k) augmented observation, and its exact rational rank. It checks each repair row annihilates the appropriate stochastic phase block, verifies all ranks by elimination, and constructs two distinct **strictly positive** 48-phase probability laws giving exactly the same next-phase law when `k>0`.

| Weights | k | rank P | minimal repairs | augmented rank |
|---|---:|---:|---:|---:|
| Original all t=1 | 0 | 48 | 0 | 48 |
| One reciprocal pair at (1/2,1/2); others 1 | 1 | 46 | 2 | 48 |
| Two reciprocal pairs at (1/4,1); others 1 | 2 | 44 | 4 | 48 |
| All t=1/2 | 6 | 36 | 12 | 48 |

Execution returned `ALL_CHECKS_PASS` using exact rational operations. Independent mathematical review and formal Source Result/Review remain open.

## Next

Extend this native-incidence repair to typed reward/branch-labelled readouts. For each singular pair, decide by an exact factorization or counterexample whether recording the original gate, axis-BRC reward, or action label automatically repairs the 2k lost phase directions; measure their positive-state and bit-cost tradeoffs.
