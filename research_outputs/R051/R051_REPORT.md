# R051_REPORT — Candidate-Blind Quantitative Holdout Data Acquisition

**Researcher-ID:** `EM-R051-8B4D70`  
**Task:** `RS-R051-CANDIDATE-BLIND-QUANTITATIVE-HOLDOUT-DATA-ACQUISITION`  
**Status:** `CANDIDATE_BLIND_QUANTITATIVE_HOLDOUT_PACKET_FROZEN / NO_SOURCE_GROUNDED_E4_ELIGIBLE_ROWS_FOUND / CALIBRATION_NOT_RUN / NOT_CANONICAL`

## 1. Executive result

R051 upgraded the **evidence-availability audit**, but it did **not** manufacture quantitative holdouts. The frozen R049 target was independently re-hashed at exact head `220aa5647389386d6c953e6aa04f32769f90f490` and matched `e41cc96ecc40bf1c992ad75bc552b2e68b36a5620e4343f10e15b71d9cf64f0c`. Before any new numerical-source search, `R051_DATA_ACQUISITION_PROTOCOL.json` was frozen at SHA-256 `029d33ce71064dbcc584f10a757d237868dc921f5345646970b7357f1804e22f`.

After preserve-first primary/authoritative source acquisition over all eight R049 rows, **0/8 rows obtained an official condition-indexed measured-output array sufficient for a disjoint construction/holdout test**. Three rows are `PLOT_ONLY_NOT_E4_ELIGIBLE`; five are `SOURCE_INSUFFICIENT_FOR_QUANTITATIVE_HOLDOUT`. No row was marked `R049_ROW_NUMERICALLY_UPGRADED`.

Candidate-blind replacement searches were then performed only after the corresponding original-row failure. Official machine-readable candidates were discovered for some neighboring protocols, including a NIST 17.4 MB phase-calibration CSV, but no replacement was promoted because the actual numerical rows could not be acquired into this packet or the candidate failed protocol/family/uncertainty requirements. **Replacement selected count = 0.**

This zero-E4 result is an evaluation-data availability result, not a failure of any G2 mechanism. No G2 content was intentionally opened, no bridge was selected, no candidate was scored/ranked, and no G3 repair was generated.

## 2. Governing foundation rule

> Definition is not inherited. Success is evidence. Explain the success from a smaller native logic.

R051 changes only the engineering evidence surface. Effective metrology definitions remain target-side evidence; no distance, angle, PDE, spectral formula, balance law, or reciprocity theorem is promoted to native premises.

## 3. Stage 0 freeze

- R049 Draft PR #540 exact head: `220aa5647389386d6c953e6aa04f32769f90f490`
- R049 target SHA-256 recomputed: `e41cc96ecc40bf1c992ad75bc552b2e68b36a5620e4343f10e15b71d9cf64f0c` — **PASS**
- R051 acquisition protocol SHA-256: `029d33ce71064dbcc584f10a757d237868dc921f5345646970b7357f1804e22f`
- Protocol frozen before external numerical-data acquisition: **YES**
- Stage-0 protocol commit: `b1e2022fea9ab990daaea806615e78bfdfc56875`

An unavoidable account-level knowledge-sync step incidentally exposed a short candidate-specific R050 summary. This is recorded as `CONTEXT_CONTAMINATION_RISK`; it was quarantined and not used in source, row, split, tolerance, residual, replacement, eligibility, bridge, score, or ranking decisions.

## 4. Preserve-first row outcomes

| Row | Pressure family | Preserve-first result | Final status |
|---|---|---|---|
| `A1-GMC-M48-STEP-GAGE` | `GEOMETRIC_MEASURE_COHERENCE` | `SOURCE_INSUFFICIENT_FOR_QUANTITATIVE_HOLDOUT` | `PLOT_ONLY_NOT_E4_ELIGIBLE` |
| `A2-CCRP-PMU-PHASE` | `CYCLE_CLOSURE_AND_RELATIVE_PHASE` | `SOURCE_INSUFFICIENT_FOR_QUANTITATIVE_HOLDOUT` | `SOURCE_INSUFFICIENT_FOR_QUANTITATIVE_HOLDOUT` |
| `A3-DR-FDTR-PUMP-PROBE` | `DIFFUSIVE_RELAXATION` | `SOURCE_INSUFFICIENT_FOR_QUANTITATIVE_HOLDOUT` | `PLOT_ONLY_NOT_E4_ELIGIBLE` |
| `A4-BMS-CAVITY-VNA` | `BOUNDED_MODE_SPECTRUM` | `SOURCE_INSUFFICIENT_FOR_QUANTITATIVE_HOLDOUT` | `PLOT_ONLY_NOT_E4_ELIGIBLE` |
| `B1A-TIBC-LIQUID-GRAVIMETRIC` | `TRANSFER_INVENTORY_BALANCE_CLOSURE` | `SOURCE_INSUFFICIENT_FOR_QUANTITATIVE_HOLDOUT` | `SOURCE_INSUFFICIENT_FOR_QUANTITATIVE_HOLDOUT` |
| `B1B-TIBC-GAS-PVTT` | `TRANSFER_INVENTORY_BALANCE_CLOSURE` | `SOURCE_INSUFFICIENT_FOR_QUANTITATIVE_HOLDOUT` | `SOURCE_INSUFFICIENT_FOR_QUANTITATIVE_HOLDOUT` |
| `B2A-SRIR-MIC-RECIP` | `SOURCE_RECEIVER_INTERCHANGE_RECIPROCITY` | `SOURCE_INSUFFICIENT_FOR_QUANTITATIVE_HOLDOUT` | `SOURCE_INSUFFICIENT_FOR_QUANTITATIVE_HOLDOUT` |
| `B2B-SRIR-ANTENNA-3PAIR` | `SOURCE_RECEIVER_INTERCHANGE_RECIPROCITY` | `SOURCE_INSUFFICIENT_FOR_QUANTITATIVE_HOLDOUT` | `SOURCE_INSUFFICIENT_FOR_QUANTITATIVE_HOLDOUT` |


### A1 — geometric measure coherence

The M48 source provides real repeatability/control/reproducibility evidence and source uncertainty, but the condition-indexed frozen step-separation measurements were not found in a source table/data file. The relevant repeated measurements are graphical. Plot digitization was therefore rejected.

### A2 — cycle closure and relative phase

NIST PMU sources state the calibration architecture, test volume, synchronization/phase-setting uncertainty and graphical characterization, but no source table/array of the frozen per-condition PMU phase-error observations was located.

### A3 — diffusive relaxation

The FDTR source states the 100 Hz–20 MHz, 40-point sweep and ±0.1 degree phase standard deviation, but the located primary surface provides phase-response curves rather than a source-supplied numerical phase-lag array. No values were reconstructed from plots.

### A4 — bounded mode spectrum

The cavity/Q sources describe repeated 201-point resonance curves and a source WLS noise/covariance treatment. The raw 201-point cavity curve arrays were not publicly acquired; fitted f0/Q or dielectric outputs were not substituted for the measured S-parameter carrier.

### B1 — transfer inventory balance closure

The liquid standard states that time-stamped weighing/environment data are acquired and provides a 5-setpoint × 10-measurement calibration design, but its public sample report exposes downstream factors rather than the required accumulated-mass/time arrays. The gas PVTt source similarly supplies apparatus/range/uncertainty and graphical comparisons but not the required condition-indexed P/T/time states. Consequently neither liquid→gas nor gas→liquid transfer can be frozen.

### B2 — source/receiver interchange reciprocity

The microphone primary source supplies the three-microphone protocol and frequency-dependent uncertainty table, but not directed-pair voltage-ratio arrays. The antenna source describes the generalized three-antenna acquisition and results, but no directed-pair received-signal-by-separation array was acquired. Neither realization alone can be promoted, and reciprocity theory is not counted as empirical data.

## 5. Replacement search ledger

Replacement searches began only after original-row insufficiency was recorded. No replacement was selected:

- `GEOMETRIC_MEASURE_COHERENCE`: official BIPM step-gauge comparison located; the accessible KCDB surface chiefly exposes derived degrees of equivalence and points to final-report measurement tables that were not ingested. Derived DoE/En was not relabeled as raw measurement.
- `CYCLE_CLOSURE_AND_RELATIVE_PHASE`: official NIST PDR dataset `AWG_LSNA_25KHz.csv` (17.4 MB; source SHA-256 frozen in the registry) located; file rows were not retrievable in the present acquisition environment, so dataset existence did not become E4.
- `DIFFUSIVE_RELAXATION`: raw NIST thermographic data source located, but no matching diffusive-relaxation uncertainty/split packet was acquired; no family stretching.
- `BOUNDED_MODE_SPECTRUM`: official NIST S-parameter archive located but rejected as an on-wafer calibration protocol, not a bounded resonator.
- Block B: no candidate-blind replacement satisfied the required paired realizations with directed/condition-indexed numerical observations.

## 6. Construction/holdout split result

The deterministic split rule was frozen in Stage 0, but **no split indices were instantiated**, because no row met the minimum data eligibility preconditions. This avoids using an empty or inadequate array to create a nominal holdout. No observation is shared between fit and holdout.

## 7. Uncertainty and metrology debt

All source uncertainty semantics already attached to R049 were preserved with displayed precision. They are not enough to create E4 without the corresponding condition-indexed measured values. No covariance was invented, no typical/global uncertainty was silently converted into per-condition uncertainty, and no unit conversion creates additional evidence.

Because no E4 target exists, no realization-specific metrology constant is fitted or shared. Potential constants/dependencies are listed by name in `R051_METROLOGY_CONSTANT_LEDGER.json` only as future calibration debt.

## 8. Adversarial results

All thirteen required kill tests were executed. Twelve are `PASS`; `TRAINING_SOURCE_COLLISION_NOT_AUDITED` is `PASS_WITH_SEARCH_LIMITATION`: exact candidate-blind replacement source tokens were searched in the repository and returned no hits, but a non-hit is not treated as proof. A later proven collision invalidates the affected generation without mutating this frozen target.

## 9. Final eligibility counts

- `E4_ELIGIBLE_TARGET`: **0**
- `E3_ONLY_CONSTRUCTION_DATA_NO_INDEPENDENT_HOLDOUT`: **0**
- `STRUCTURAL_ONLY_NO_NUMERIC_OBSERVATIONS`: **0**
- `PLOT_ONLY_NOT_E4_ELIGIBLE`: **3**
- `SOURCE_INSUFFICIENT_FOR_QUANTITATIVE_HOLDOUT`: **5**
- `REPLACED_BY_NEW_CANDIDATE_BLIND_ROW`: **0**

No E4 is forced. This is the strongest source-grounded conclusion available under the frozen R051 protocol.

## 10. Calibration firewall

`G2_OPENED = false`  
`CALIBRATION_RUN = false`  
`BRIDGE_SCORING = false`  
`CANDIDATE_RANKING = false`  
`G3_GENERATION = false`
