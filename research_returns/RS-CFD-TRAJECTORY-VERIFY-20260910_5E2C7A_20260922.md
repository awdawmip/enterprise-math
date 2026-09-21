# RS-CFD-TRAJECTORY-VERIFY-20260910 — dependence audit 5E2C7A

## Scope and claim reconciliation

This unit consumes the immutable R15/6D3A91 native-run manifest without replay. The predecessor verifier claim `CLM-CFDVFY-84A2D7-20260921-2141` had exceeded its 120-minute owner lease before this unit was claimed, and its execution branch `research/cfd-verify-dependence-84a2d7-20260921` still pointed exactly to its dispatch base `e11d2742abdad0f9ccf087dccf573fec514df654`; no durable predecessor research output existed to preserve or repeat.

Frozen object under audit:

- commit: `af956e55af72cedb44288bc8a6157da1670705a0`
- path: `research_artifacts/RS-CFD-TRAJECTORY-VERIFY-20260910_6D3A91/native_run_manifest.json`
- blob: `0e903688ac6ffaba079f88449c3f170f33d2ffbc`

The manifest schedules 24 same-trajectory A/B/C triplets in four cycles of six orders, with `AB>0` and `CB>0` confirmatory sign gates requiring at least 18/24 positives at Bonferroni one-sided alpha 0.025 per gate.

## Result: order balance does not establish sign independence

The nominal 18/24 exact sign-test tail is

`P[Binomial(24,1/2) >= 18] = 190051/16777216 ≈ 0.0113279223`.

That calibration requires a valid triplet-level null model, in particular independence/exchangeability sufficient for the binomial sign distribution. The frozen six-order balance by itself does not provide it.

An exact finite counterexample preserves every frozen order-balance property. Let the four cycle latents `Z_1,...,Z_4` be independent fair Bernoulli variables and set all six triplet signs inside cycle `c` equal to `Z_c`. Then every individual triplet sign is marginally fair, every cycle still contains each of the six A/B/C orders exactly once, every arm appears 8 times in each execution position over 24 triplets, and every directed pair precedence occurs 12 times. Nevertheless the positive count is

`S = 6 K`, where `K ~ Binomial(4,1/2)`.

Hence the frozen 18/24 gate passes iff `K>=3`, so under this legal clustered null

`P[S>=18] = (C(4,3)+C(4,4))/16 = 5/16 = 0.3125`.

This is not a small perturbation of the nominal tail: the same nominal threshold can have a 31.25% false-pass rate under perfect within-cycle clustering while all order/position balancing checks still pass.

The frozen `AC>=17/24` negative-control veto has the same `5/16` probability under this six-per-cycle clustered model, since `ceil(17/6)=3`. Because AC is a veto rather than an acceptance gate, this primarily damages power/interpretability rather than creating false sparse-speedup acceptance.

## Exact resolution floor if cycle is the independent unit

If only the four cycles can be treated as independent symmetric sign units, the smallest nonzero one-sided exact sign probability is the all-positive event `1/16 = 0.0625`, which is already larger than the frozen per-gate alpha `0.025`.

Even five independent blocks are insufficient: `1/32 = 0.03125 > 0.025`. Six independent blocks are the first count for which the all-positive event reaches `1/64 = 0.015625 <= 0.025`.

Therefore there is no nonrandomized exact one-sided sign-only confirmatory test at alpha 0.025 using only four arbitrary-dependence cycles. A future distribution-free block-sign design needs at least six genuinely independent symmetric blocks if it relies on the all-positive event. That is a design implication for a future predeclared manifest, not permission to alter 6D3A91 retroactively.

## Consequences for the frozen manifest

1. The 18/24 AB and CB counts retain confirmatory-alpha meaning only if the native run can justify triplet-level sign independence or an alternative sufficient dependence model/calibration before the timing result is interpreted.
2. Six-order balance, position balance and pairwise-precedence balance are useful drift/order controls but are not substitutes for independence.
3. Bonferroni across AB and CB remains mathematically valid only after each marginal p-value is valid. It cannot repair a miscalibrated triplet-level sign test.
4. If within-cycle clustering cannot be ruled out, the frozen 18/24 counts should be reported as descriptive/diagnostic, not as exact alpha-controlled confirmatory evidence.
5. The frozen 6D3A91 manifest remains unchanged. Any revised >=6-independent-block confirmatory design must be frozen before observing new native timing data.

A sensitivity check for perfect sign clusters shows how strongly the nominal 18/24 threshold depends on the effective independent block size. Exact false-pass probabilities are: block size 1: `190051/16777216`; 2: `299/4096`; 3: `37/256`; 4: `7/64`; 6 (the actual cycle size): `5/16`; 8: `1/8`; 12: `1/4`; 24: `1/2`.

## Verification

The stdlib-only exact checker `research_checks/RS_CFD_TRAJECTORY_VERIFY_5E2C7A.py` uses `Fraction`, verifies all four frozen cycles contain all six literal orders, verifies 8-per-position arm balance and 12-per-direction pair precedence, recomputes the exact nominal 18/24 and 17/24 tails, exhaustively enumerates all `2^4=16` cycle-latent sign configurations, verifies the `5/16` clustered pass/veto probabilities, checks the cluster-size sensitivity table, and verifies the four/five/six-block alpha-resolution boundary. Local `py_compile` and execution both passed before publication.

## Boundary and next action

This is a finite experimental-design/dependence audit only. No spectralDNS/shenfun/MPI/FFTW native host was run; no speedup/slowdown, generic CFD or industrial acceleration, continuous-PDE theorem, Working Truth, or final acceptance is asserted.

Next, on an already provisioned pinned native host, preserve the frozen 6D3A91 physical/correctness protocol. Before granting exact sign-test confirmatory meaning, either establish a defensible triplet-level dependence calibration from the run protocol/host process, or explicitly downgrade the existing 18/24 statistic to descriptive status. If distribution-free cycle-level confirmation is required, freeze a new >=6-independent-block design before collecting its timing data. The resulting immutable native checkpoint still returns to `RS-CFD-TRAJECTORY-VERIFY-20260910` for independent review.
