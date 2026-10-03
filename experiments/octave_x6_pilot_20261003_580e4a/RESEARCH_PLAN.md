# Octave motion benchmark and X6 residual-faithful representation pilot

Status: PREPARED, NOT YET EXECUTED. No numerical result is asserted in this plan.

Researcher: EM-DIRECT-A283B5. Activity: RA-DF59962DCA39B7350ECF5F32.
The activity is registered on Enterprise Math main at
`4c154037884c94edc4773e9b9a92552cd805ea30`; no formal task, CLAIM, review,
Working Truth, or Foundation admission is implied.

## Question and fixed scope

Can a residual-retaining, six-native-axis integer-chart representation track
three explicitly external motion benchmarks more faithfully than feeding back
the same recurrence after deleting its rounding remainder? How does it compare
with the algebraically equivalent same-parameter rational recurrence? What do
unseen initial states, later time, sensor noise, changed physical parameters,
wrapped and unwrapped phase/energy/exchange diagnostics, and exact-bit growth reveal?

This is an independent direct research unit. It does not repeat the generation-7
128-step X6 replay or seek to take over its claim. Prior replay source:
`8770476e36a10e79e6b03bdc67af3b5d8d106169`,
`experiments/brc_x6_replay_20261002_fca717/REPORT.md`.
Its hidden-response nonidentifiability remains a boundary, not a result this
pilot claims as new. The separate completed cross-axis study by EM-BRCFIT-9D72AC
at `9ab9e44f168c2a36c37c65b950eda13857179677`,
`experiments/brc_x6_transfer_20261002_9d72ac/REPORT.md`, provides hidden-return
and higher-order joint-relation counterexamples. Those results are background
with original attribution, not repeated here. Its total-variation distance is
not the position-rounding residual or energy diagnostic used in this pilot. This pilot adds Octave-generated motion, identification,
out-of-sample prediction, controlled remainder erasure, and cost measurement.

## Six spatial axes and the observation bridge

Current semantic authority is Source
`7035c8011938aa0baffbb22f3827322053f520d5`, including the direct-user amendment:
**the Enterprise coordinate system has no native plane, and all research begins
from Heartbeat World's six-dimensional native spatial world. Time is introduced
explicitly as needed and is separately typed.** No native or six-dimensional
plane is assumed here. This motion/memory problem needs ordered time; static
research is not claimed to require it.

P000 fixes six primitive native spatial axes and twelve signed primitive
directions. All six coordinates and their temporal relations are retained in
this candidate from its starting state; component plots are observer readouts,
not an independent lower-dimensional starting space. The
native chart is a torsor-relative `Z in Z^6`. Neither velocities nor time nor
remainders substitute for those six spatial axes. A six-position/six-velocity
external ODE uses twelve state variables but still has six position components.

The external reference is `q'' + gamma q' + K q = 0`, with `q in R^6`.
It is a mathematical motion benchmark, not laboratory data or a claim that
ordinary physical space has been empirically measured to have six dimensions.
Octave `ode45` generates its truth; `expm` checks the same external linear ODE.
This newly requested classical simulation is isolated from the native candidate
operations. It does not supply a native force, triadic equilibrium, rotation,
or Cell propagation theorem, and does not change any P000 premise.

The declared measurement bridge is componentwise nearest-integer rounding at
fixed resolution delta. At each sample, write the rational response as

`s = Z + R`, `Z_i = floor(s_i + 1/2)`, `-1/2 <= R_i < 1/2`, `q_read = delta*s`.

Z comprises all six signed native relative displacement coordinates. R is a
nonspatial rational representation remainder, not an extra spatial dimension.
The previous response is separately typed time-history memory. Signed raw chart
values are not exported as final nonnegative Cell addresses; no unregistered
full-X6 address codec is invented.

A sampled difference in multiple Z components is recorded as an ordered
composite path: first the signed E1 unit steps, then E2, through E6. The run-length
file preserves that chosen path witness. The ordering is a representation
convention, not an inferred microscopic trajectory. No duration is assigned to
its individual microsteps, and the external sample interval is not asserted to
be a physical heartbeat quantum.

## Models and actual BRC reuse

All fitting is performed by GNU Octave backslash. A full AR2 recurrence has 72
coefficients; the diagonal baseline has 12. The full coefficient matrix is
rounded once to denominator 2^20, before testing. No holdout result chooses that
denominator, delta, model order, training duration, or regularization.

The existing `brc_transport.py` `Affine` and `EffectHistogram` are actually
called on each exact step. Their four dependency files are byte-pinned to Source
`71d836784c9545867955e1c23cb5a964fc2a0482` in `pinned_source`, with blob/SHA256
manifest. This is `REUSE_EXECUTED` only after execution succeeds. The affine
effect acts on the current six response fields and six history fields. Its
packet dimension 12 counts decorated-state fields, not native spatial axes.

The deterministic packet has one branch of weight one. Its BRC CWM data therefore
degenerate to count=1, mass=dominant=1. No artificial branch gain is claimed.
Signs belong to the affine state, not positive branch mass. No moment compression
or hidden-path equivalence is used: the complete declared rational response and
its history are propagated.

Compare:
1. Actual BRC recurrence retaining R in feedback; fine readout delta*(Z+R)
2. Its Cell-only current readout delta*Z, while retaining R in future feedback
3. Same fitted coefficients but R deleted at every feedback step
4. Same-DOF rational-coefficient classical recurrence at matched quantized initial
   states, implemented in floating point solely as a numerical comparator
5. Full unconstrained floating AR2 and diagonal AR2 with matched quantized initial
   states, plus separate high-resolution-initial-state reference controls

The retained and discarded models start from exactly the same two quantized
position observations, with zero initial remainder. Thus retention does not get
an undisclosed more accurate initial state. It preserves newly generated
representation information. Every exact trajectory is independently checked
against a common-denominator integer recurrence, without calling Affine.

## Exact representation statement

For rational response s, the pair `(round(s), s-round(s))` is a lossless
coordinate representation on the stated remainder interval. Applying the same
rational affine recurrence to its reconstruction and decomposing again gives
the same response sequence as the undecomposed rational recurrence, by induction
over steps. Hence this representation cannot intrinsically improve prediction
over that same recurrence at equal inputs/coefficients. It can improve over an
information-erasing feedback projection. This elementary representation argument
is distinct from the finite executed certificate and from a physical law.

Remainder deletion is not universally future-safe: two responses +49/100 and
-49/100 share rounded coordinate zero, but the rational gain 9/5 sends them to
values rounding to +1 and -1. This one-component witness is a statement about
the declared response/readout interface, not a new native spatial dimension or
a general native dynamical kernel.

## Fixed data and prospective controls

- Seed: 20261002; time grid 0:0.1:40
- Three K/gamma cases: independent frequencies, six-axis ring coupling, damped ring
- Eight training initial states; fitting samples end at t=8
- Four unseen initial states for external floating controls; the first two get
  full exact BRC certificates at each of delta=1/64,1/256,1/1024
- No teacher forcing after the first two initial samples
- One additional frozen-model parameter stress trajectory per case uses K*1.15;
  the changed K is used only for truth/evaluation, never passed to the predictor
- Coupled-model noisy-training stress: absolute position noise sigma=0.001,
  fixed before execution, tested at delta=1/256 on the two exact holdout states
- Conditioning/rank and training residual are retained, not replaced by R-squared
- Truth controls: ode45 versus expm and conservative energy drift

The parameter stress test is deliberately outside the model's conditioning
inputs. Failure is informative about transfer limits, not proof against P000.
Because the retained map is homogeneous and exact, the delta sweep changes the
initial quantization rather than the underlying physical recurrence. Label its
retained-model curve initial-grid convergence, not a new fitted dynamics or a
resolution-dependent physical law.

Training-noise least squares can have errors-in-variables bias; no correction is
silently fitted from the test data.

## Diagnostics and resource stopping rules

Report held-out position NRMSE, last-quarter position RMSE, sampled-velocity
energy error, modal phase error, ring-edge exchange error, per-trajectory runtime,
exact numerator/denominator bit lengths, and primitive-path length per sample.
Energy uses sampled central-difference velocity. Phase metrics include wrapped
modal-angle RMS and aligned unwrapped final drift, so whole-cycle slips are not
hidden. Energy/phase/exchange are external benchmark diagnostics, not native observable
laws. Velocity estimates use the same central difference on prediction and
reference; exact truth energy also gets its own ODE check.

Prospective scientific computation is capped at 23 exact trajectories, at most
9200 sampled transitions, cooperative soft walltime limits of 180 seconds per
trajectory and 1800 seconds total, and a 12000-bit retained-fraction limit. The
bit limit is not a claim about peak intermediate memory. An external shell
watchdog may separately cap the entire job. The exact comparisons use two paired
holdout initial states and one noise realization, not a large independent sample. First run one 40-step smoke trajectory.
Any cap/error is an explicit bounded partial result; do not silently shorten the
scientific horizon, switch to floats, or omit the failure. The full pilot may be
run only after the smoke passes and actual Octave/environment authorization is
confirmed. A later extension requires a new stated purpose.

## Reproduction after authorized environment selection

Use the actual Octave executable and record `--version`, path, and command log.

1. `octave --quiet --eval "addpath(pwd); generate_benchmarks();"`
2. `python3 run_brc.py --smoke`
3. `python3 run_brc.py`
4. `python3 run_brc.py --verify-only`
5. `octave --quiet --eval "addpath(pwd); analyze_results();"`

The first and fourth commands must really be GNU Octave, not Python output
described as Octave. Native BRC computation uses the pinned existing Python API.
Generated output, failures, metrics, PNG/SVG, source hashes, and logs are all
part of the research evidence. Smoke artifacts have their own output/smoke
directory and cannot replace full-run files. The total trajectory pipeline
runtime includes both BRC models, integer validation, readout, and I/O; separate
component timers prevent calling all of that standalone BRC cost. The squared
local-rounding-error sum is a numerical distortion diagnostic, not energy.
Verify image pixels and independently review the
finished evidence before publishing quantitative conclusions.

## Boundaries for conclusions

Keep separate: learned-model error, initial quantization error, coefficient
quantization, intentional remainder deletion, external ODE numerical error,
floating readout error, and unclassified physical discrepancy. This experiment
does not establish a unique native propagation kernel, triadic force lift,
observer map calibrated to real instruments, or a new physical law. A nonzero
error is not itself real native residual energy, force, temperature, or noise.
No model success promotes its claim to Working Truth or Foundation.

Global-Knowledge-Sync: main@0946b0848601 / GLOBAL_KNOWLEDGE_V1
