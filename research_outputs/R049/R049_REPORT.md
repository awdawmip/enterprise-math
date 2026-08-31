# R049 Candidate-Blind Independent Engineering Holdout Construction

Researcher-ID: `EM-R049-6D82B4`  
Task: `RS-R049-CANDIDATE-BLIND-INDEPENDENT-ENGINEERING-HOLDOUT-CONSTRUCTION`  
Taskbook source: `cff6152a1f0e57141990b5ca2614326c3da7fbde`  
Freeze timestamp (UTC): `2026-08-13T02:40:42Z`  
Target hash: `sha256:e41cc96ecc40bf1c992ad75bc552b2e68b36a5620e4343f10e15b71d9cf64f0c`

## Return

`CANDIDATE_BLIND_INDEPENDENT_ENGINEERING_HOLDOUT_FROZEN / BLOCK_A_COMPLETE / BLOCK_B_QUOTIENTED / CALIBRATION_NOT_RUN / NOT_CANONICAL`

## Candidate-blind boundary

R049 constructs and freezes the engineering test only. It does not calibrate, score, rank, name, select, or inspect any candidate mechanism. Effective/classical definitions are target-side dependencies only; no N0/native promotion is claimed.

A mandatory account-level synchronization step incidentally exposed prohibited prior-generation-specific metadata. That material was quarantined and assigned zero influence on protocol, source, tolerance, quotient, eligibility, or pressure selection. The machine audit records this as `CONTEXT_CONTAMINATION_RISK`.

## Block A — frozen inherited-family holdouts

| Family | Frozen protocol | Measured channel | Source-stated envelope |
|---|---|---|---|
| `GEOMETRIC_MEASURE_COHERENCE` | NIST M48 tactile CMM long step-gauge metrology | contact-derived step separations | `U(k=2) ≈ 100 + 200 L nm`, L in m |
| `CYCLE_CLOSURE_AND_RELATIVE_PHASE` | NIST PMU/synchrophasor phase calibration | timestamped phase-error observations | phase-standard expanded uncertainty `<0.01°` below 5 kHz for equal amplitudes; `<0.015°` for unequal amplitudes <10:1 |
| `DIFFUSIVE_RELAXATION` | NIST FDTR optical pump-probe | corrected reflected-probe phase-lag curve vs modulation frequency | raw phase standard deviation `±0.1°` |
| `BOUNDED_MODE_SPECTRUM` | NIST 60 mm microwave cylindrical cavity + network analyzer | raw complex scattering/resonance curve vs frequency | source-defined frequency-dependent noise model + WLS one-sigma estimator covariance; cavity held within `±0.1 °C`; no invented scalar resonance tolerance |

The four Block-A protocols are pairwise materially distinct in apparatus, measurement chain, physical realization, scale, intervention, output channel, and source family. Each co-frozen pair differs in at least six listed dimensions.

## Block B — dependency quotient

### Retained: `TRANSFER_INVENTORY_BALANCE_CLOSURE`

Two independent realizations survive quotienting:

1. dynamic gravimetric liquid flow: receiving-tank mass accumulation vs through-flow, `0.022%` expanded mass-flow uncertainty over `0.22–15 kg/s`;
2. PVTt gas flow: receiving-tank state/inventory change over timed diversion, `0.02–0.05%` expanded uncertainty (`k=2`) over `1–2000 slm`.

Gas PVTt depends on calibrated volume/thermodynamic state, but the liquid realization does not. Therefore geometric calibration cannot generate the shared residual. Unit conversions and calculated meter factors are removed.

### Retained: `SOURCE_RECEIVER_INTERCHANGE_RECIPROCITY`

Two independent realizations survive quotienting:

1. three-microphone acoustic reciprocity with three transmitter/receiver pairings; frozen subrange `31.5–2000 Hz`, with source table `U(k=2)=0.07 dB` at 31.5 Hz, `0.05 dB` at 50 Hz, and `0.04 dB` from 100–2000 Hz;
2. NIST three-antenna extrapolation, three pairwise combinations with received signal vs separation; frozen `2–30 GHz` range with typical gain uncertainty `0.10 dB`.

After factoring dB/gain/sensitivity and geometry conventions, the role-interchange compatibility remains. This does not require phase-loop closure.

## Measured-versus-calculated firewall

The following are explicitly **not** independent measured evidence:

- FDTR fitted thermal conductivity, heat capacity, interface conductance/resistance;
- cavity fitted `f0`, `Q`, relative permittivity, loss tangent, and skin-depth-corrected frequency;
- converted units, meter factors, solved microphone sensitivities, solved antenna gains, or algebraically recomputed closure residuals.

Only the raw measurement chains defined in `R049_RAW_ENGINEERING_ATLAS.json` feed the frozen constraints.

## Independence / anti-leakage result

Mandatory attacks are recorded in `R049_ADVERSARIAL_TEST_RESULTS.json`. Eight return `PASS`; `TRAINING_SOURCE_REUSED_AS_HOLDOUT` returns `PASS_WITH_TOOLING_LIMITATION`: a blindness-preserving repository lookup could not establish complete negative provenance because the code-search backend reported incomplete results, and opening prior exact protocol/tolerance rows would itself violate the construction rule.

This limitation does not authorize mutation. If a later post-freeze provenance-only audit proves a protocol/source collision with the earlier construction surface, this generation becomes ineligible and must be replaced by a **new** holdout generation and hash.

## Freeze invariant

After `2026-08-13T02:40:42Z` the following cannot change in response to any later candidate information:

- protocols and controlled interventions;
- measured outputs and scale regimes;
- uncertainty/tolerance/error envelopes;
- definition-stripped constraints;
- Block-B dependency quotient;
- Block-A/Block-B eligibility;
- source provenance.

Any such change requires a new holdout generation. Candidate calibration was not run.

## Machine object

Authoritative manifest: `R049_HOLDOUT_MANIFEST.json`  
Frozen target hash: `sha256:e41cc96ecc40bf1c992ad75bc552b2e68b36a5620e4343f10e15b71d9cf64f0c`
