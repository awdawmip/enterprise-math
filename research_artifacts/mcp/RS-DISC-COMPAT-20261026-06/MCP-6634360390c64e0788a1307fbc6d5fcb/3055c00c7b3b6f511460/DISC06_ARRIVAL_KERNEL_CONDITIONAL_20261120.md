# DISC06: arrival-time observational kernel and an exact zero-dispersion criterion (2026-11-20)

Task: `RS-DISC-COMPAT-20261026-06` · Source class: author-side conditional mathematical reduction · Not independently reviewed.
Researcher/session: original live session `EM-X6-C7A253` / `MCP-6634360390c64e0788a1307fbc6d5fcb`.
Scope: This is **not** a claimed native propagation law, laboratory fit, GRB bound, or a new physical time unit. It answers the task's requested first step on a precisely defined effective observational class, and identifies the exact native bridge still missing.

## Declared model and observational interface

Let `S` be a set of **complete typed global states**, each containing native X6 Cell identities, channel/port incidence, phase/sign, positive branch mass, source/provenance, boundary and the joint self-consistent state. Time is a **separately typed ordered event index** `n`. One event may change the entire global state and transport activation over nonadjacent Cells; no one-Cell-per-tick rule, fixed metric, fixed duration, or local-only clock is assumed. The project-native source does not yet supply a frozen update `U` and photon/energy/detector readout.

For a specified candidate protocol `M`, a source configuration `a`, observational energy label `e`, direction setting `u`, and polarization setting `p`, let `Ω(e,u,p)` be its **allowed complete ordered global histories** ending at a declared detector event. Each path `ω` has a nonnegative weight `w_{e,u,p}(ω)` in a declared observation/readout layer and an event-index arrival `N(ω)`. The weight is **not** asserted to be a native probability, complex amplitude, or untyped substitute for signed phase/BRC provenance. Sum only over paths for which the declared detector event occurs; assume the total detected weight `Z_{e,u,p}` is finite and strictly positive. Define the **conditional detector histogram**

`H_{e,u,p}(n) = [Σ_{ω:N(ω)=n} w_{e,u,p}(ω)] / Z_{e,u,p}.`

To compare laboratory arrival time, declare a *shared* calibrated observer map `t=τ(n,u,detector)`. It may be nonlinear and must not silently identify heartbeat count with seconds. Source emission-time offsets, instrument response, redshift and energy reconstruction remain distinct nuisance/bridge fields.

## Exact theorem A: energy-independent arrival law from path-weight factorization

Fix `u,p`, source and detector geometry. Suppose there is one shared set of complete detector-reaching histories `Ω`, a shared arrival-index function `N`, and a positive scalar `c_e` for each energy label such that

`w_{e,u,p}(ω)=c_e w_{*,u,p}(ω)` for **every** complete allowed detector-reaching history `ω`.

Then `H_{e,u,p}(n)=H_{*,u,p}(n)` for every arrival index `n`. Proof: factor `c_e` from each numerator and the common normalization `Z_e=c_e Z_*`; these cancel exactly. If the observer clock `τ` and the emission/response corrections are energy independent, the entire **observed propagation-time distribution** is energy independent. Every defined energy derivative or finite-difference coefficient of that distribution is zero, including the first nonzero coefficient, which is absent on this class.

A corresponding direction/polarization independence claim requires the same factorization **across** the direction/polarization settings with a common detector/clock readout; factorization only in `e` proves no such stronger claim.

This criterion does not require a one-tick adjacent jump, a smooth dispersion relation, a Fourier operator, or a value of a lattice scale. It is a *sufficient* condition; it is not a claim that the current native X6 rules satisfy it.

## Exact theorem B: a constructive future-observation test

For a candidate effective **weighted** update on complete hidden states, let `q:S→O` retain the detector-visible state, including whether detection occurred. If for every energy label `e`, every `o,o'∈O`, and every `x∈q^{-1}(o)` the summed next-event transition weight into the fiber `q^{-1}(o')` is the same number `K(o,o')`, independent of both `x` and `e`, and all energy labels start with the same projected initial law on `O`, then the complete projected sequence of event-time observations has the same law for all `e`. Proof: conditional aggregation gives the *same* quotient transition kernel at every step; induction on finite event prefixes and then marginalization to the first-detection index proves equality of histograms.

For a deterministic global event law, replace the aggregate condition by `q(U_e(x))=F(q(x))` with one common `F` for all allowed `e,x`; the same induction applies. These are future-operation closure criteria, stronger than matching the current Cell address or current signed-port label alone. The independent `n` clock readout remains a separate bridge.

## Minimal hidden-state obstruction to invalid compression

Consider an **abstract conditional transition system**, not asserted to be a legally instantiated X6 update. Two hidden states `A,B` share the same presently visible Cell and port reading. Under the same next-event rule, `A→D` detects after one event, whereas `B→C→D` detects after two events; `C` is not detected. If a proposed photon energy readout prepares `A` under `e_1` and `B` under `e_2`, the arrival histograms are point masses at 1 and 2 respectively, despite identical present Cell/port output. Hence an observer quotient which forgets the hidden distinction fails the future-context test. To use this as **native** evidence, one must construct actual permitted global states and global `U` that realize these transitions while conserving all required native joint relations, source/provenance and BRC types. That native instantiation remains open.

## Genuine native gap and next discriminating calculation

Status under the task's required enum: `MISSING_COMPONENT` for a **native empirical prediction**; theorem A and B are established only within their explicitly declared observational models.

Required frozen fields for a native optical test:
1. `U:S×I→S`: event update on full X6/heartbeat global states (including source, environment, ordered port/BRC provenance, sign/phase and positive mass), with legal nonadjacent transfers explicitly distinguished.
2. `PhotonReadout:S→(energy, polarization, direction, emission/arrival event)` with physically calibrated units and a shared observer/excitation identification, or a detector-event distribution avoiding continuous group-velocity notation.
3. `ClockReadout:(event history, observer, detector)→physical time` and spatial separation; neither heartbeat count nor scalar residual is a calibrated number of seconds/meters.
4. Detector response and source-intrinsic lag nuisance model, reconstructed energy/redshift, and the same frozen parameters across independent sources/directions.

A direct next test is to pick two *actual legal* initial global states with the same declared photon energy label and detector/port observation but distinct retained provenance, apply one common native `U` under admissible future contexts, and compare the detector first-event histograms. If different, the proposed observational quotient lacks sufficient hidden state. If a common quotient kernel is proved, the corresponding class satisfies theorem B. Any native arithmetic uses the actually typed BRC route; no classical trigonometry/π expansion or substitute numerical update was executed here.

Previously saved literature comparison is `research_notes/discrete_light_objections_20261026_9c8ddfc415e7.md`. Its GRB limits are conditional external constraints, not coefficients derived from this research. `E_QG` is not identified with a Cell scale by this note.

Evidence class: symbolic deduction with explicit hypotheses; no code execution, no native BRC numerical step, no independent Driver review, no Task/Result completion or P000 promotion.
