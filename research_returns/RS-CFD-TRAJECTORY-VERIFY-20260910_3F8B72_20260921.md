# Independent CFD trajectory verification checkpoint: R15 benchmark-design audit

Task: `RS-CFD-TRAJECTORY-VERIFY-20260910`  
Publication: `TP2-499BEE22860EFD4AD321`  
Researcher: `EM-CFD-VFY-3F8B72`  
Claim: `CLM-CFDVFY-3F8B72-20260921-2044`  
Activity: `RA-CFDVFY-3F8B72-20260921`  
State: `CONTINUATION_REQUIRED / PASS_WITH_REQUIRED_PROTOCOL_CLARIFICATIONS / ORIGINAL HOST NOT RERUN`

## Scope consumed

This independent verifier consumes R15's immutable three-arm benchmark design at:

- return `283a135c7a8b4cd7830cee4b13e05ca07531011f:research_returns/RS-CFD-SPECTRAL-HYBRID-20260910_9A4F61_20260921_R15.md`;
- design artifact `6bb66b04184ec4e791c96507e939ab4bbfb4ad35:research_artifacts/RS-CFD-SPECTRAL-HYBRID-20260910_9A4F61_R15/experimental_design.json`.

No spectralDNS/shenfun/MPI/FFTW host was rerun in this unit. The purpose is to verify the finite experimental-design mathematics before scarce native-host evidence is collected.

## Independent verdict

R15's core A/B/C design is mathematically usable, and its exact threshold arithmetic is correct, but two protocol statements must be tightened before the native run:

1. the current rule “drop ties and count usable non-tied `n`” is not automatically compatible with the claimed complete six-order balance;
2. the quoted `0.811071...` power at `n=24` is a **per-gate marginal power**, not the power that both dependent confirmatory gates pass.

The correct status is therefore `PASS_WITH_REQUIRED_PROTOCOL_CLARIFICATIONS`, not rejection and not native performance acceptance.

## 1. Exact sign-test arithmetic: PASS

For one-sided `H0: P(positive) <= 1/2` with Bonferroni `alpha=0.025` per gate, the least admissible positive counts are independently recomputed as:

| n | required k | exact tail |
|---:|---:|---:|
| 6 | 6 | `1/64 = 0.015625` |
| 12 | 10 | `79/4096 = 0.019287109375` |
| 18 | 14 | `253/16384 = 0.01544189453125` |
| 24 | 18 | `190051/16777216 = 0.011327922344207764` |
| 30 | 21 | `22964087/1073741824 = 0.02138697262853384` |

For `n=24`, `k=17` has tail `0.03195732831954956`, so it fails the stricter `0.025` gate and `18/24` is indeed the least passing count. The R15 power calculation at `P(positive)=0.8` also recomputes exactly to `0.81107105511888` **for one gate**.

Bonferroni remains valid even though `A-B` and `C-B` share arm B; it does not require the two gate statistics to be independent. If the only intended confirmatory claim were the conjunction “B beats A AND B beats C”, an intersection-union test at `alpha=0.05` per component would already control the conjunctive type-I error at 0.05; R15's `0.025` choice is therefore conservative but valid and additionally protects simultaneous component-wise claims.

## 2. Joint power: wording correction required

Because both contrasts share B, their gate outcomes can be dependent. Knowing only that each gate has marginal pass probability `0.81107105511888` does not identify the probability that **both** pass. With no joint model, the Fréchet bounds from those equal marginals are approximately `[0.62214211023776, 0.81107105511888]`.

Accordingly the native-run protocol may state “about 81.1% marginal power per gate under `P(positive)=0.8`”, but must not call that the overall two-gate acceptance power without an explicit joint dependence model or simulation.

## 3. Six-order combinatorics: PASS, with inference boundary

The declared order set

`ABC, BCA, CAB, ACB, CBA, BAC`

is exactly the six permutations of A/B/C. In one complete cycle each arm appears twice in each ordinal position, and every directed pairwise precedence relation occurs three times. Four complete cycles therefore provide exact combinatorial position balance for 24 scheduled triplets.

This balance removes deterministic first/second/third-position imbalance. It does **not** by itself prove independence or stationarity of timing signs across repeats, nor does a fixed repeating cycle neutralize arbitrary thermal/time drift. The native protocol should therefore randomize or otherwise freeze the cycle/order sequence before measurement and retain raw order plus timestamp metadata. Exact sign-test language remains conditional on the declared sign-sampling assumptions.

## 4. Tie handling: protocol amendment required before native run

R15 currently says that ties are excluded from usable `n`, while also describing `n=24` as four complete six-order cycles. Those statements are not automatically compatible.

`A-B` and `C-B` can tie on different repeats. Gate-specific tie deletion can therefore produce different effective sample sizes and different retained order strata for the two gates, destroying the analyzed order balance even though 24 physical triplets were scheduled. Continuing until “24 usable non-tied” observations also needs a predeclared stopping/replacement rule and changes the estimand to a conditional non-tie sign probability.

The verifier-preferred primary protocol is simpler and fail-closed:

- schedule exactly 24 physical A/B/C triplets in four complete six-order cycles;
- define a gate success as strictly `delta > 0`;
- count `delta == 0` as a non-success for that superiority gate;
- retain `n=24` and require at least `18/24` successes on both confirmatory gates.

This preserves the physical order balance and tests the unconditional probability of a strict positive contrast. If classical tie deletion is retained instead, the protocol must predeclare a bounded gate-specific replacement/stratification rule that restores order balance and explicitly state that the tested null is conditional on a non-tied contrast.

## 5. Contrast interpretation

`A-B` is the correct end-to-end contrast provided all three arms start from identical deterministic state/Source and satisfy the frozen correctness gates.

`C-B` is a materially better attribution control than R14's different-initial-condition random256 comparison, because B and C operate on the same physical trajectory and guarded wrapper. However, it identifies the effect of **allowing the sparse route inside that wrapper**. It does not, by itself, decompose a pure sparse-convolution arithmetic speedup if allowing the route also changes cache state, allocation behavior or other control-state effects. Those mechanisms remain part of the route intervention unless separately instrumented.

`A-C` is correctly treated as a diagnostic/veto rather than an acceptance gate. With the R15 sign convention, significantly positive `A-C` means the forced-fallback guarded control C is unexpectedly faster than the unmodified dense A despite executing no sparse calls; clean sparse-route attribution is then blocked until that all-fallback advantage is explained. Failure to reject `A-C > 0` remains non-equivalence evidence only.

## 6. BRC / information-preservation audit

For benchmark acceptance, the full source observer must remain the raw same-trajectory A/B/C timings, route/support logs, correctness diagnostics, setup/allocation/compilation costs, and shadow numerical counterfactuals. The sign vector is an intentionally compressed confirmatory observer.

A concrete information-loss witness is immediate: the same sequence of positive/negative signs is compatible with arbitrarily tiny positive timing deltas or with much larger positive deltas. Therefore the sign gate certifies directional repeat frequency under its sampling model; it does **not** certify a minimum practical speedup magnitude.

If a later claim needs “material” rather than merely directional speedup, a nonzero engineering margin `epsilon` must be predeclared and the confirmatory sign variable changed to `1{delta > epsilon}` (or an equivalent predeclared effect-size procedure). This verifier does not invent a numerical epsilon. Raw paired magnitudes must be retained regardless.

## 7. Hard gates retained

Performance acceptance remains downstream of correctness. A/B/C must preserve the frozen solver semantics and numerical tolerances; B must actually execute at least one sparse nonlinear call and C must execute zero sparse calls; raw ties, execution order, timestamps, route decisions and decomposed costs must remain durable. Shadow dense counterfactual work must stay outside the confirmatory production timing path.

The original provisioned spectralDNS/shenfun/MPI/FFTW rerun and subsequent independent review remain outstanding. Nothing in this checkpoint establishes generic CFD acceleration, industrial performance, a continuous-PDE theorem, mathematical acceptance, Working Truth or canonical promotion.

## Validation and durable artifacts

The standalone checker `research_checks/RS_CFD_TRAJECTORY_VERIFY_3F8B72.py` was executed locally and emitted the verifier certificate successfully. It independently recomputes the exact thresholds/powers, verifies all six permutation position and pairwise-precedence counts, verifies the `n=24` alpha-0.05 intersection-union component threshold, and records the tie/power/causal-scope boundaries. The machine-readable result is `research_artifacts/RS-CFD-TRAJECTORY-VERIFY-20260910_3F8B72/r15_design_verification.json`.

## Next action

Before the native host run, freeze the tie policy and order randomization/predeclaration in the run manifest. Then execute the three-arm 32^3 Taylor-Green matrix on an already provisioned pinned spectralDNS/shenfun/MPI/FFTW host, preferably 24 **scheduled** triplets in four complete six-order cycles, retaining every correctness and cost field required by R15 plus the verifier amendments above. Route that immutable host checkpoint back to this independent verifier task. Do not mark either CFD task DONE before the native evidence is reviewed independently.
