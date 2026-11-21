# DISCCOMPAT: the minimal 2×2×2 experimental readout is underdetermined

Date 2026-11-21. Task RS-DISC-COMPAT-20261026-00 (TP2-20EC0ABD05545665A8D3). Author EM-X6-C7A253. Status: NOT_REVIEWED; exact **conditional specification-obstruction**, not a physical incompatibility theorem.

## Exact two-party protocol and native/observer boundary

Two receiver stations A and B; local settings x,y ∈ {0,1}; local binary outputs a,b ∈ {0,1}. The target is one joint distribution P(a,b|x,y), normalized for every input pair. The native world carrier has X6 Cell positions with six typed axes, separately typed event/heartbeat time when operations demand it, branch/provenance/joint-residual state and the native triadic invariants. None of those native types identifies an output bit or a measurement instrument. There is no extra native plane or seventh spatial dimension.

Declare a model capsule C=(S,P,U,H_A,H_B,R_A,R_B,K,D,θ), with S an admissible typed joint native state, P a preparation family indexed by settings, U the declared allowed relational/heartbeat update and its event schedule, H_i the native instrument coupling, R_i the bit readouts, K any probabilistic law/rule over the prepared histories, D the externally calibrated apparatus/timing/error model, and θ shared frozen parameters. Interactions and statistics must be evaluated on joint histories, not only the two marginals. The current task/book and pinned P000/Heartbeat/Residual/Joint-Observer constraints specify the *types and invariants*, but do not provide a unique executable family P,U,H_i,R_i,K,D.

## Exact witness to nonuniqueness from the missing readout

Conditional hypothesis: there is at least one admissible native preparation/trajectory (S,P,U) satisfying the protected typing, and no additional physical readout law is supplied. Hold all its native objects, their future operations, and all settings unchanged. Consider two deterministic **candidate external observation completions**, not certified physical measurements:

- C0: for every native history and every setting (x,y), R_A=0 and R_B=0.
- C1: for every native history and every setting (x,y), R_A=1 and R_B=1.

Their complete conditional output tables are

| (x,y) | C0: P(00),P(01),P(10),P(11) | C1: P(00),P(01),P(10),P(11) |
|---|---|---|
| 00 | (1,0,0,0) | (0,0,0,1) |
| 01 | (1,0,0,0) | (0,0,0,1) |
| 10 | (1,0,0,0) | (0,0,0,1) |
| 11 | (1,0,0,0) | (0,0,0,1) |

Each table is normalized, nonnegative, independent of remote setting, and admits a deterministic joint distribution with zero added random bits. For identical native P,U, the output laws differ. Neither completion changes the underlying Cell graph, triadic rule, branch mass, time type or provenance; a later native operation may still inspect the full native state. Consequently, *without a constrained observer/instrument bridge*, the specified native axioms alone do not determine a unique P(a,b|x,y). The witness is a missing-interface result, not a no-go for future constrained models and not evidence that constant-output instruments describe the actual experiment.

The example does not rely on declaring arbitrary residuals to fit real data; the two fixed completions are declared before any data and only demonstrate formal non-identifiability. A later physical protocol might exclude both, or select one, through its measurement and calibration laws.

## Audit table and minimum next executable unit

| Component | Current status | Required typed field |
|---|---|---|
| X6 spatial identity and triadic primitive layer | FIXED PROJECT BASELINE | native Cell identity; path/branch provenance; P000 |
| Relational/heartbeat time type | DEFINED TYPE, DYNAMICS OPEN | event order, actual update/selection schedule |
| Common/joint residual and safe compression | DEFINED CONSTRAINT, SPECIFIC STATE OPEN | concrete joint S, future-operation language and permitted quotient |
| Setting-conditioned preparation | MISSING_COMPONENT | P(s|x,y), setting-to-operation binding, no retroactive data conditioning |
| Update and permitted port interactions | MISSING_COMPONENT | U with H/typed port permissions, stopping/readout time |
| Local instruments and bit readout | MISSING_COMPONENT | H_A,H_B,R_A,R_B with calibration and observer boundary |
| Statistical/randomness law | MISSING_COMPONENT | K over complete histories (determinism is also an explicit admissible choice) |
| Empirical comparison | NOT YET RUN | preregistered θ, data split, apparatus D, uncertainty/errors and joint count table |

Accepted result within this exact scope: **MISSING_COMPONENT**, with minimal missing element a constrained state-to-observer/output bridge (and actual update, preparation and statistics for a positive prediction). No measured dataset, target probability, physical timescale, or instrument was read in this step; therefore no experiment is labelled COMPATIBLE_WITHIN_SCOPE or EXCLUDED_WITHIN_SCOPE.

Next science: choose a specified externally operational 2×2×2 experiment and one X6-native candidate instrument coupling, fix full ModelCapsule and shared parameters before reading held-out counts, then compute/test a unique joint prediction; if the typed coupling cannot be defined, return the exact unfilled port/readout operation instead of inventing distribution.

Pinned source categories consumed: RS-DISC-COMPAT-20261026-00 taskbook and TP2-20EC0ABD05545665A8D3; native X6 Heartbeat, residual and joint observer contracts at enterprise-math@64044ada5e3e2b5d7b3c327942ee028da6e2a967. The preceding 2026-10-26 discrete-light literature memo is background, not experimental confirmation. Preserve NOT_REVIEWED and other authorship; no Foundation or external science admission.
