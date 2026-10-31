# Stage300-B — Interventional source mixtures, causal Bayes closure and sharp scalar-port obstruction

**Status:** `PORTABLE_AUTHOR_PROOF / EXACT_RATIONAL_EXECUTED / UNREVIEWED / NOT_ADMITTED`. 2026-10-30. This is an external finite positive-rational, source-labelled BRC-style probability model. It is not a native P000/X6 theorem, a formally claimed Task, a Source Result, an independent review or a demonstration of empirical physics.

## Input and exact predecessors

- Frozen GLOBAL_KNOWLEDGE_V1 canonical `main@59588fa6f735b9ba38e586201e3fbbbad6e55cef`; Enterprise Math control input `main@34b736ab077ed0b4cef6dcd4d19157597bf0b1d8` (separate source pin).
- At this global snapshot, `projects/enterprise-math/P000_STARTUP.json` points to full-original Git blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`, and the original was verified against that blob. Enterprise Math current P000 original, ACTIVE Heartbeat X6/time and GLOBAL_KNOWLEDGE ACTIVE residual-fidelity worldview were also read. Existing project portable protocol `docs/PORTABLE_RESEARCH_PROTOCOL.md` and scheduled-research operating protocol were read.
- Exact preceding author artifact: Stage299-B, immutable `67a953cd23517beafc224306281768a4d91d760a`, `research_notes/n12_aux_iid_stage299b_adaptive_physical_20261030_RESEARCH2/PROOF_STAGE299B.md`, with its Stage300 handoff. Prior 2-bit negative-covariance / `1/12` risk gap is **not reproved or claimed as new** here.
- Method reuse `REUSE_APPLIED`: positive rational branch weights, source, action, ordered time, independent draws conditional on retained state and future-observer typing from `definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json`. The present result extends an already active branch/observer problem; it introduces no accepted new universal toolbox family.

## 1. Exact causal mixture/commuting-kernel criterion

Let `S` range over a finite set of latent provenance sources with positive prior weights `w_s`. Let `h` be an observed ordered history, including past typed actions. For each source and each legal next action `a`, let `K_s(y|h,a)` be a finite normalized nonnegative output kernel. An examiner policy `pi(a|h)` depends only on the visible history, is the **same** for every source and for the simulator, and does not directly read `S` or simulator private seeds. The source process can have any finite horizon `T`. Let `L_s(h)` be the product of the source's output probabilities along `h`, **excluding** the factors of `pi` (and including the source's initial visible distribution).

For any history of positive pooled probability, put

`rho_s(h) = w_s L_s(h) / sum_r w_r L_r(h)`;

`K_mix(y|h,a) = sum_s rho_s(h) K_s(y|h,a)`.

**Theorem 300.1 (causal mixture closure; precise criterion).** With the correct pooled initial distribution, the single source-blind free causal simulator using `K_mix` reproduces `sum_s w_s P_s^pi` **on every visible action/output path and simultaneously for every finite visible-history-adaptive policy**. Moreover, a proposed source-blind free causal simulator `Q` reproduces that entire declared future language if and only if its next-output conditionals equal `K_mix(y|h,a)` for every action at every pooled-reachable `(h,a)` that a legal policy can choose. A history never reached under any declared policy imposes no obligation. This is an observer-relative necessary and sufficient criterion, not an assertion of implementability by an arbitrarily restricted port interface.

**Proof.** For any fixed visible history `h`, the factors `pi(a|prefix)` in its source-specific probability are identical across sources and cancel in the Bayes ratio. Thus `rho_s(h)` depends only on the visible action/output history, not on the policy that reached it. For the next allowed action, pooled conditional output is the above convex sum. Induction from the pooled initial law proves the equality of every complete action/output word for every policy. Conversely, any simulator giving the same positive-reachable path laws has the same ratios `P(h,a,y)/P(h,a)` at each available action, and hence its conditional kernel must equal `K_mix`. QED.

For an explicitly specified physical simulator class `C`, exact compression is therefore equivalent to **one globally consistent implementable mechanism in C** whose *effective visible-history predictive kernels* equal these `K_mix` kernels at all reachable `(h,a)`. It is insufficient that each action has a separately fitted output marginal; a common private state, update law and across-time joint law must realize all the kernels. In the strong, prior-independent version, equality for every hidden point mass and every prior forces identical source-conditioned output/quotient-transition kernels on each compression fiber: this is the controlled strong-lumpability condition already used in Stage293-B. A midpoint for one fixed prior can exist without strong fiber equality.

## 2. A two-source, three-bit positive-rational counterexample

A hidden source `S in {0,1}` is drawn with prior `1/2` each. First output `X` is a **fair Bernoulli bit independent of S**. There are then two ordered future steps; at each step the public examiner chooses `H` (hold) or `F` (source-sensitive intervention) based on all preceding visible actions and bits. Conditional on `S`, the output bits are independent, with exact rates:

- `H`: `Pr(Y=1 | S=s,H)=1/2` for both sources;
- `F`: `Pr(Y=1 | S=0,F)=1/4` and `Pr(Y=1 | S=1,F)=3/4`.

The source `S` remains private. There are `2 x 2 x 2^3 = 16` source-labelled binary path words under the fixed `FF` policy, all of strictly positive rational mass. For a source-fixed word `(x,y_1,y_2)`, the conditional probability is `(1/2) Ber(p_s,y_1) Ber(p_s,y_2)`. In lexicographic order `000,001,010,011,100,101,110,111`:

`P_0 = (9,3,3,1, 9,3,3,1)/32`,

`P_1 = (1,3,3,9, 1,3,3,9)/32`.

The source-pooled output law is

`M = (P_0+P_1)/2 = (5,3,3,5, 5,3,3,5)/32`.

If the examiner makes **at most one F intervention** (the other step is H), the source-pooled three-bit law is uniform on the eight words, exactly the conditionally IID triple with parameter `1/2`. If it makes two F interventions, `X` remains independent of the persistent hidden `S` while `Y_1,Y_2` share the same persistent source; the resulting `M` has `E[XY_1]=1/4` but `E[Y_1Y_2]=5/16`. The obstruction first appears at the second source-sensitive future intervention in this declared family.

By Theorem 300.1, **a free history-dependent causal simulator reproduces M for the FF policy and the exact pooled law for all adaptive H/F policies simultaneously**: it maintains the Bayesian likelihood of the hidden source as a function of the already-visible history, without reading S. This is an exact realization-flow / behavioral-strategy solution; the zero pooled free-realization discrepancy follows without numerical LP optimization.

## 3. Sharp continuum obstruction for the restricted one-scalar shared-IID port

Define the **restricted candidate compressed interface** `C_IID^3` as follows: the compressor samples **one** latent parameter `Theta in [0,1]` from an arbitrary real probability law `mu` before the first observation; conditional on Theta, `X,Y_1,Y_2` are independent and all Ber(Theta), regardless of the later examiner's `H/F` labels. This interface retains one shared rate and can observe or mask draws; it cannot perform the source-sensitive `F` retuning above. We compare **the observable FF language**, and explicitly do not pretend that this restricted physical interface implements the original F operation as a typed native update. The failure is precisely a missing update/latent tag in the proposed compression.

Write `Q_mu` for the three-bit port output law. It is exchangeable, so for each word containing `k` ones, its mass is the same `q_k=integral theta^k (1-theta)^(3-k) dmu(theta)`, and `q_0+3q_1+3q_2+q_3=1`.

**Theorem 300.2 (exact sharp unrestricted-real-mixing distance).**

`inf_{mu probability on [0,1]} TV(M,Q_mu) = 1/12`.

**Lower proof over all real mixtures.** Set `x_k=32 q_k` and `t=x_1+x_2`, so `x_0+x_3=32-3t`. The eight pathwise absolute differences yield

`64 TV(M,Q_mu) = |x_0-5|+|x_3-5| + [2|x_1-3|+|x_1-5|] + [2|x_2-3|+|x_2-5|]`.

For any real `x>=0`, `2|x-3|+|x-5| >= x-1`. Hence

`64 TV >= |22-3t| + t - 2 >= 16/3`;

the last piecewise-linear bound has its global minimum at `t=22/3`. Therefore `TV>=1/12`. This argument applies to the entire exchangeable simplex, a superset of all real pre-randomized shared-IID ports, so finite probing is not part of the proof.

**Exact rational upper certificate.** Choose

`mu_* = (1/6) delta_(1/4) + (2/3) delta_(1/2) + (1/6) delta_(3/4)`.

Then `q_0=q_3=5/32`, `q_1=q_2=11/96`, making `x_0=x_3=5`, `x_1=x_2=11/3` and reaching equality in all inequalities. Thus the continuum infimum is attained by three strictly positive rational atoms and positive rational weights, proving the exact `1/12` result. The free causal output class has zero distance to `M`, so the **fixed-FF pooled observation gap is exactly 1/12**, for these precisely declared output interfaces.

## 4. Source-labelled TV, and why a scalar risk can mask a pooled defect

Retain original source identity as an external evaluation label, and require one source-blind replacement `Q` for both source-specific complete FF laws. Define

`R_tag(Q) = (TV(P_0,Q)+TV(P_1,Q))/2`.

A direct exact sum gives `TV(P_0,P_1)=1/2`. Consequently the source-labelled triangle inequality gives `R_tag(Q)>=1/4` for **every** Q; the midpoint `M` reaches this with a free causal simulator. Unlike the pooled-distance objective, the **restricted three-IID class also achieves this scalar lower bound**, using the fully explicit finite measure

`nu = (3/16) delta_0 + (3/4) delta_(1/2) + (1/16) delta_1`.

Its three-bit law is `Q_nu=(9,3,3,3,3,3,3,5)/32`. Exact evaluation gives `TV(P_0,Q_nu)=3/16`, `TV(P_1,Q_nu)=5/16`, so `R_tag(Q_nu)=1/4`. Yet `TV(M,Q_nu)=1/8`, larger than the sharp pooled optimum `1/12`. Thus

`inf_{Q free} R_tag(Q) = inf_{mu} R_tag(Q_mu) = 1/4`, **while**

`inf_{mu} TV(M,Q_mu) - inf_{Q free} TV(M,Q) = 1/12`.

These are different declared observers / objectives; neither number subsumes the other. Their apparently conflicting statements are mathematically compatible. If a future observer sees the original source label `S` after a *single* F operation, pooled output `Y` is fair but source-conditional Bernoulli rates are `1/4` and `3/4`; replacing them by a common fair Y has exact source-labelled average TV `1/4`. Visibility of a seed or provenance tag must therefore be typed separately from hidden-seed pooling.

## 5. Interface repair, hidden seed and native boundary

- **Source tag S erased, arbitrary free causal history retained:** use `rho_s(h)` and `K_mix`. All source-blind visible-history-adaptive policies are matched exactly **as pooled laws**. It does not reproduce the joint law with an observer that reads original `S`.
- **Persistent private simulator seed J and distinct rates for X and F:** choose `J` uniformly in `{0,1}`, draw `X~Ber(1/2)` independently of J, and draw each F bit at rate `p_J`, while H uses `1/2`. This realizes every pooled adaptive law with an explicit *two-slot typed* interface. A future operation that reads J is a different observer; it needs its own source/seed joint mapping. A simulator's independently sampled J is not automatically the original S.
- **One shared scalar Theta reused unchanged across X,Y1,Y2:** Theorem 300.2 rules out exact FF pooled fidelity even with an arbitrary real-valued pre-mixture. Source-sensitive intervention cannot silently be reclassified as mere reveal/mask.
- **Action-triggered source-blind retuning:** If an admissible interface can carry the persistent private J and retune the F rate to `p_J` without modifying the X-rate, it attains zero pooled mismatch. If it allows only deterministic retuning as a function of one scalar theta, any claim of equivalence must specify and prove the whole three-step joint representation; an unconstrained new seed is additional retained structure, not a free consequence of moment matching.

All `X,Y_i,S,J` above are *external auxiliary* probability variables, not any of P000's six native spatial axes. No X6 Cell address, single-native-axis ordered path, triadic force closure, native time trace or registered six-field lossless address is constructed here. Transfer to the Heartbeat world requires an explicitly typed source/path/branch/observer/update functor and a proof that future operations commute with it. Signed or phase-interfering BRC carriers are outside this strictly positive-rational example.

## 6. Executed verification and limits

`REPRO_STAGE300B.py` runs on Python standard-library `fractions.Fraction`. In the captured executed stdout file `REPRO_STAGE300B_EXECUTED_STDOUT.txt`, it checked all 16 strictly positive source-labelled FF path laws, probability normalization and the exact word arrays; the three one-F/zero-F pooled uniform laws; the sharp rational `mu_*` upper certificate and numerical equality in the analytical dual lower bound; the exact tagged witness `nu`; and **1024 deterministic source-blind adaptive H/F examiner policies** with 16,384 positive source-labelled enumerated policy-path masses, proving the finite tests' explicit coverage. It checked exact equality between the Bayes simulator and the pooled law for every enumerated policy. This covers all deterministic two-stage policies of the declared finite language; randomized source-blind policies are convex combinations and the general Theorem 300.1 handles arbitrary finite horizons.

The universal continuum `1/12` lower bound follows from the mathematical inequality, not the finite program; no formal Lean check, external independent scientific review or native X6 program execution occurred. The quantitative `1/12` pertains **only to fixed FF three-word pooled observation under `C_IID^3`**, not the unknown simultaneous minimax over the entire adaptive H/F language. The source-labelled `1/4` equal-optimum statement pertains **only to FF source-labelled complete paths**; the adaptive multi-policy labelled minimax needs a separate check.

**Owner/authority at run:** Site read-only connection reported `research_authority_granted=false`; native control task listing returned `CONTROL_QUOTA`. Therefore no active owner, formal native session, CLAIM, Result/Review, freeze or admission is asserted. This is an independently transportable author proof prepared under the user's research delegation, not a takeover of an active task.

## Next problem

Stage301-B: Compute sharp **simultaneous** `inf_mu sup_{pi in adaptive H/F}` pooled and source-labelled TV for the single-Theta shared-IID triple, allowing arbitrary real mu; find a finite dual certificate and a matching rational or algebraic measure. Compare to the two-slot private-J repaired interface and identify the weakest causal memory / retune type that exactly implements *all* visible-history policies, including whether source-readable J forces additional labels. Independently, establish an actual typed P000-native X6/BRC path-lift or an explicit obstruction with six native axes, triadic closure, time and registered lossless address semantics. Stage278-A Bellman N=12 remains separate.
