# RS-CFD-TRAJECTORY-VERIFY-20260910 — cycle-block confirmation design 4C2F19

Status: `CONTINUATION_REQUIRED`
Researcher: `EM-CFD-VFY-BLOCK-4C2F19`

## Scope

This unit consumes the immutable 5E2C7A dependence audit and the frozen 6D3A91 native-run manifest without replay. It does not alter the frozen four-cycle manifest, does not run the unavailable native spectralDNS/shenfun/MPI/FFTW host, and does not independently accept the CFD result.

The 5E2C7A audit already proved that four six-order cycles do not justify the frozen triplet-level 18/24 exact sign calibration under arbitrary within-cycle dependence: a legal clustered null can inflate the pass probability to 5/16. The present unit asks the next exact question: **if a complete six-order cycle is treated as the inferential block, what confirmatory design is valid and how many cycles are needed for useful power?**

## 1. Cycle-level observer that preserves the frozen directional estimand

For each confirmatory gate `g in {AB, CB}` and each complete cycle, retain all six raw triplet contrasts and define one derived block bit

`S_g,c = 1{ at least 4 of the 6 strict gate contrasts are > 0 }`.

Triplet ties and nonpositive values remain non-successes. This keeps the frozen `epsilon=0` directional semantics rather than silently replacing it with a magnitude-average claim. The complete raw six-vector, literal order and timing provenance remain stored; the block bit is only the inferential observer.

Arbitrary dependence among the six observations inside a cycle is allowed. A sufficient null condition for `P(S_g,c=1)<=1/2` is central sign symmetry of the complete six-dimensional gate-difference vector. Indeed, sign reversal maps the set with at least four positive components to the disjoint set with at least four negative components. Exact enumeration over all `3^6=729` positive/zero/negative sign patterns verifies the disjointness, including zeros.

Across cycles, exact binomial calibration still requires independent block units (or another separately justified dependence calibration). More generally, independence plus per-cycle null probabilities `p_c<=1/2` is enough: the upper tail `P(sum S_c >= r)` is coordinatewise nondecreasing in every `p_c`, hence is maximized at all `p_c=1/2`. Six-order balance alone does **not** prove either block symmetry or cross-cycle independence.

## 2. A sharper global test: intersection-union, not Bonferroni, for a strictly conjunctive claim

The frozen acceptance rule requires both confirmatory propositions: `AB>0` and `CB>0`. If the scientific claim is strictly the conjunction

`H1_global = H1_AB AND H1_CB`,

then its null is the union `H0_AB OR H0_CB`. Rejecting the global null only when **both** component tests reject is an intersection-union test (IUT). Each component may therefore be tested at one-sided alpha `0.05`; no Bonferroni split is needed for the global conjunction. Under any global-null parameter, at least one component null is true, and

`P(reject both) <= P(reject the true component) <= 0.05`.

This argument does not require independence between AB and CB, so the shared B arm is not a problem for global size control. It does **not** license two separately reportable simultaneous alpha-.05 claims. If the project wants separate simultaneous AB and CB claims rather than one conjunctive acceptance statement, the prior Bonferroni `.025` per gate remains the safe contract.

This distinction materially reduces the block-count burden. At `.025`, five independent blocks are still impossible and six all-positive blocks give `1/64`. For the conjunctive IUT at `.05`, five all-positive blocks already give `1/32 = 0.03125`; four blocks remain impossible because their smallest one-sided exact probability is `1/16 = 0.0625`.

## 3. Exact power / host-budget frontier

All values below use exact rational binomial arithmetic. Power statements assume independent cycles and per-cycle alternative success probability at least `p_block`. They are marginal per-gate powers; AB/CB cross-gate dependence remains unrestricted.

For the IUT `.05` component tests, the smallest cycle counts reaching the stated marginal powers are:

- `p_block=0.7`: 37 cycles with threshold 24/37 gives power >=0.8; 53 cycles with 33/53 gives power >=0.9.
- `p_block=0.8`: **18 cycles with 13/18** has null tail `1577/32768 ~= 0.0481262` and power `3307661688832/3814697265625 ~= 0.867084`; **23 cycles with 16/23** has null tail `763/16384 ~= 0.0465698` and power `11068512973881344/11920928955078125 ~= 0.928494`.
- `p_block=0.9`: 8 cycles with 7/8 gives power `0.81310473`; 11 cycles with 9/11 gives power `0.91043814915`.

A complete cycle contains six A/B/C triplets and each triplet executes three arms. Thus the `p_block≈0.8` planning points correspond to:

- 18 cycles = **108 physical triplets = 324 arm executions** for >0.8 marginal power per gate.
- 23 cycles = **138 physical triplets = 414 arm executions** for >0.9 marginal power per gate.

The second point also gives a useful dependence-robust two-gate planning guarantee. If both component marginal powers are at least `0.928494`, then without assuming anything about AB/CB dependence, the Frechet lower bound for both passing is

`2*0.9284941648 - 1 = 0.8569883296`.

So 23 independent complete cycles are sufficient for a >0.8 **lower bound** on joint pass probability when `p_block>=0.8` for each gate. By contrast, five cycles are merely the first alpha-resolving design; at `p_block=0.8`, an all-positive 5/5 rule has power only `0.8^5 = 0.32768` and is not a useful production recommendation.

For reference, retaining Bonferroni `.025` per component instead would require 20 cycles (120 triplets / 360 arm runs) for >=0.8 marginal power at `p_block=.8`, and 28 cycles (168 triplets / 504 arm runs) for >=0.9. The IUT improvement is therefore a real host-budget reduction, but only for the strictly conjunctive claim.

## 4. Negative control and BRC observer audit

The frozen `AC` contrast is a diagnostic veto, not a confirmatory alternative. Its triplet-level `17/24` calibration is subject to the same clustering defect found by 5E2C7A. If a formal false-veto probability is needed, AC should be calibrated on the same independent cycle blocks. Otherwise it should stay descriptive/veto-only; a false veto reduces power but does not create false sparse-speedup acceptance.

BRC observer discipline is material here. The population is the same-trajectory A/B/C runs partitioned into complete six-order cycles; branch identity is `(gate, cycle, literal order)`. The raw carrier contains all six signed magnitudes, execution order, timestamps and correctness/cost fields. The cycle-majority bit intentionally erases magnitude, intra-cycle dependence structure and which literal orders were positive, so those coordinates remain in the durable raw evidence. The block bit is adequate only for the frozen epsilon-zero directional claim and the exact block-sign future operation. It is not adequate for a material-speedup magnitude claim or for diagnosing temporal drift.

## 5. Verification and boundary

`research_checks/RS_CFD_TRAJECTORY_VERIFY_4C2F19.py` was executed with stdlib exact `Fraction` arithmetic. It verifies all `729` sign-reversal patterns, the four/five/six-cycle resolution floors, exact `.05` and `.025` critical values, minimal cycle counts for `p_block in {0.7,0.8,0.9}` at 0.8/0.9 marginal-power targets, and the Frechet lower bound. The machine-readable design certificate is `research_artifacts/RS-CFD-TRAJECTORY-VERIFY-20260910_4C2F19/block_design_certificate.json`.

This is a finite experimental-design result only. It does not retroactively modify 6D3A91, establish that native-host cycles are independent or centrally symmetric, execute spectralDNS/shenfun/MPI/FFTW, prove a CFD speedup, establish generic industrial acceleration or a continuous-PDE theorem, or grant Working Truth/Foundation/final acceptance.

## Next action

Keep the existing frozen 6D3A91 physical/correctness protocol as historical immutable evidence and treat its four-cycle triplet-level sign statistics as descriptive unless a stronger dependence model is justified. Before collecting a new confirmatory native timing sample, freeze a successor block-level manifest. If the acceptance claim remains strictly conjunctive, use the IUT `.05` component calibration above; for a defensible planning alternative around `p_block=.8`, 23 independent complete cycles is the fail-closed recommendation when the goal is at least a 0.8 Frechet lower bound on joint pass probability. If separate simultaneous AB/CB claims are required, retain Bonferroni `.025` and its larger cycle counts. In either case, preserve every raw triplet and all existing numerical/correctness/cost diagnostics and return the immutable native checkpoint to this verifier task.
