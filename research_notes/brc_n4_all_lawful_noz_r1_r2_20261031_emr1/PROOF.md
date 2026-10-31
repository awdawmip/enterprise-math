# BRC N=4 — sharp all-lawful no-sensor minimax for one and two code symbols

Date: 2026-10-31. **AUTHOR_ANALYTIC_PROOF / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED**. This is a portable extension of PR #1757, immutable predecessor `396bae14dba75ade9130cfc80c0410293a61b4e3`, not a formal native Task Result.

## Frozen experiment, lawful grammar, scored observation

The underlying finite BRC carrier consists of 16 strictly positive paths `(S,J,K)`, `S in {AU,AV,BU,BV}`, `J,K in {0,1}`, with `K` fair independently under the two external preparations `B=P,Q`. Raw masses **per K leaf** (denominator 240) are:

| S | Q J0/J1 | P J0/J1 |
|---|---|---|
| AU | 10/10 | 9/11 |
| AV | 20/20 | 5/5 |
| BU | 15/15 | 3/27 |
| BV | 15/15 | 30/30 |

Each prepared conditional law `L_(S,B)` starts at stage 2, carries its fixed provenance S, and samples J with conditional probabilities AU_Q=(1/2,1/2), AU_P=(9/20,11/20); AV both fair; BU_Q fair, BU_P=(1/10,9/10); BV both fair. All eight (S,B) inputs, including duplicate AV and BV preparations, remain in the scoring maximum. This is a mathematical *source preparation*, not a new spatial axis or a physical mechanism.

A common stochastic encoder `E(c|S,B)` with at most k symbols is applied **before** a future policy H is chosen. The decoder `D_H(O|c)` may depend on H and be stochastic but cannot access S, B or the actual realized J/K except through c. The output scored **in this note** is only `O=(T,Decision)`; the BU-specific noisy sensor Z is entirely suppressed, including its presence flag. In particular, the goal is *distributional reconstruction*, not reconstruction of the actual sample or joint coupling to a hidden path. Define

`R_k(F;noZ) = inf_E sup_(H in F) inf_(D_H) max_(S,B) TV(L_H(O|S,B), (E D_H)(O|S,B))`.

`F=S23` denotes the original lawful S23 causal stop/decision grammar; `F=S2` is the larger lawful grammar. Its time-two AU/BU action kernels must agree. The S23 time-three kernels additionally agree at equal contemporaneous P/Q likelihood ratios; the six distinct ratio classes are AU0=9/10, AU1=11/10, AV=1/4, BU0=1/5, BU1=9/5, BV=2. Terminal decisions are arbitrary *lawful decisions*, not required to be likelihood-optimal. Both grammars allow internal stochastic decisions and T4 continuation. Any policy H induces a law-independent stochastic kernel from the full potential path to O.

## Exact theorem

For **both** complete lawful policy families and any `0 <= epsilon <= 1/2` (the sensor is not observed),

`R_1(S23;noZ) = R_1(S2;noZ) = 3/4`,

`R_2(S23;noZ) = R_2(S2;noZ) = 1/2`.

Consequently, the earlier fixed-policy H* bound `R_1(H*;noZ)=2/3` is **not** the all-policy value; another lawful time/decision policy witnesses a sharp `3/4`. In this unrestricted all-policy minimax, deleting the BU sensor does not improve the one- or two-code optima relative to the earlier complete-observer results. This does **not** mean Z is redundant for fixed policies, larger state budgets, other observers, or native dynamics.

## Lower bound — an explicit four-class lawful policy H-dagger

Continue at time 1. At time 2 set the action `AU=BU=continue`, `AV=stop with Decision=P`, `BV=stop with Decision=Q`. At time 3, stop every remaining history; decide P for AU0 and AU1, Q for BU0 and BU1. If an inactive AV/BV third-stage action is specified for a total policy table, choose a common action within each of their equal-ratio daughter pairs. The AU/BU time-two kernels coincide exactly; no equal likelihood-ratio class is split at time three, and K is not observed. Hence H-dagger is lawful S23 and S2.

With **only** the public `(T,Decision)` output, this one policy produces four pairwise disjoint deterministic laws, independent of B and epsilon:

| Input provenance | Public terminal record |
|---|---|
| AU | `(3,P)` |
| AV | `(2,P)` |
| BU | `(3,Q)` |
| BV | `(2,Q)` |

**Packing lemma.** For G prepared inputs whose output laws have pairwise disjoint supports `U_i` under one lawful policy, and any k-symbol stochastic encoder E and decoder D, let `p_i=(ED)_i(U_i)`. Then

`sum_i p_i = sum_c sum_i E(i,c) D(c,U_i) <= sum_c (max_i E(i,c)) sum_i D(c,U_i) <= k`.

Since the true i-th law is supported on `U_i`, its TV error is at least `1-p_i`, so `max_i TV >= 1-k/G`. Here G=4 and one may select one preparation from each provenance. Thus for either policy family `R1 >= 3/4`, `R2 >= 1/2`, with no restriction to deterministic encoders. The bound is a one-policy witness and therefore respects the encoder-before-policy quantifier order.

## Upper bound — universal exact rational reference kernels

Let the six prepared conditional `J` laws be as above and retain the full typed `(S,J,K)` path carrier. Construct two **probability** distributions `F_L,F_R` on `(S,J)`:

```
F_L: AU0=19/80, AU1=21/80, AV0=1/4, AV1=1/4;
F_R: BU0=1/10, BU1=2/5,  BV0=1/4, BV1=1/4.
```

All unspecified atoms have zero mass. Both sum to 1. `F_L` has 1/2 of its mass on AU and 1/2 on AV. Its AU conditional is the midpoint of AU_Q/AU_P. `F_R` has 1/2 on BU and 1/2 on BV, with BU conditional `(1/5,4/5)`. The crucial coordinatewise domination facts are:

* On AU, `(19/80,21/80) <= (9/20,1/2)` coordinatewise, hence also below both AU prepared conditional rows.
* On AV, `(1/4,1/4) <= (1/2,1/2)`.
* On BU, `(1/10,2/5) <= (1/10,1/2)` coordinatewise, hence below both BU prepared conditional rows.
* On BV, `(1/4,1/4) <= (1/2,1/2)`.

Consequently for **each** of the eight original preparations, the overlap with its corresponding reference (F_L for AU/AV, F_R for BU/BV) is exactly 1/2, i.e. `TV(L_(S,B),F_group)=1/2`. Attach the same fair independent K to every row, which preserves these TV identities.

For k=2, use the deterministic encoder `AU,AV -> L`, `BU,BV -> R`. Given any lawful policy H, let `D_H(.|L)=H#F_L` and `D_H(.|R)=H#F_R`, including H's permitted internal randomness and then **projecting away Z**. Total-variation contraction under the *same* law-independent kernel H gives statewise error at most 1/2, simultaneously for all lawful S2/S23 policies. Hence `R2 <= 1/2`.

For k=1, put `F_1=(F_L+F_R)/2`. This distribution assigns 1/4 of its mass to **each** provenance S. On every prepared input's S-fiber, its pointwise mass is no greater than that input's true conditional law, while other S-fibers are disjoint. Thus `TV(L_(S,B), F_1)=3/4` for all eight inputs. Use `D_H=H#F_1`; contraction gives `R1 <= 3/4` for all lawful policies. Lower and upper bounds coincide, proving the theorem.

The decoder generates a *fresh sample* with the correct output law to the stated error, not the actual earlier J/K. This method never erases native provenance in the underlying model; suppressing Z is expressly an observer-specific quotient. H-dagger's effect remains valid even though the provenance itself is not externally supplied.

## Exact executed validation, scope and next question

`VERIFY.py` was executed with Python standard-library `fractions.Fraction`. It checks both 16-leaf strictly positive P/Q normalization, the eight conditional preparations, the full-future reference distributions' eight exact TV identities, H-dagger's four distinct pure output atoms, and all `27*64=1728` deterministic policies in the declared subfamily (three time-two action classes with each of `continue/stop P/stop Q`; six time-three likelihood-ratio class decisions P/Q). Every policy is compared on all eight preparations for each of the one- and two-code output decoders: **27,648 exact full `(T,Decision)`-distribution comparisons**, all passing; the maxima are 3/4 and 1/2. The complete potentially randomized, T4, continuum-parameter conclusion rests on the analytic pushforward/packing proof, **not** on enumerating those 1,728 policies.

Sources and immutable prior frontier: `SOURCES.md`. Concrete next research obligation: `NEXT_TASK.md`.

No claim is made that any native X6 Cell dynamics, physical sensor, heartbeat clock, or Source-issued task role has been established. This is a source-stipulated positive-rational BRC branch experiment within a possible restricted ordered X6 path representation, not a proof of the native physical BRC model. The identity of the eight preparations, branch order, and available future observers is part of the theorem's typed scope. Mathematical status remains author proof with exact finite audits, **UNREVIEWED / NOT_ADMITTED**.
