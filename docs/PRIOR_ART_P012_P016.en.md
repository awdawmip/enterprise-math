# Prior-Art Appendix — P012 Geometry and P016 Physical Falsification

Status: `CANONICAL PRIOR-ART APPENDIX`  
Scope: P012 intrinsic discrete geometry and P016 quantitative falsification protocol

This appendix extends the main prior-art map without replacing it. Every source below is established prior work or an experimental benchmark; none is claimed as an Enterprise Math invention.

## 1. P012 — intrinsic discrete geometry

Mathlib's graph-metric module defines `SimpleGraph.edist` by shortest walk length, uses an extended value for disconnected vertices, and supplies the natural-valued graph distance and core metric laws. [SRC-MATHLIB-SIMPLEGRAPH-METRIC]

Enterprise Math **adopts** that established graph-distance structure. P012's project-specific choice is foundational rather than historical: primitive adjacency / one-step reachability is allowed to be explicit geometric data, and integer shortest-step distance is derived from it instead of being defined by rounding a hidden Euclidean length.

Therefore P012 does not claim novelty for shortest-path metrics, graph automorphisms, lattice `L1` distance, weighted graph metrics, or graph balls. The provisional synthesis is recorded as `EM-COMP-012`.

## 2. P016 — physical falsification protocol

P016 does not treat the broad statement “finite resolution may be fundamental” as already experimentally confirmed or refuted. A concrete realization must first map its parameters to an unavoidable measurable consequence. Existing experiments then constrain only realizations that predict the corresponding observable.

### 2.1 Preferred direction / Lorentz anisotropy

Optical-clock comparison provides a high-precision benchmark for models that necessarily generate orientation- or Lorentz-dependent frequency shifts. [SRC-SANNER-2019-LORENTZ-CLOCK]

This is a **contrast/constraint benchmark**, not evidence that every discrete model violates Lorentz symmetry. Earlier discrete-spacetime approaches already demonstrate that discreteness and Lorentz symmetry are logically distinct design questions. [SRC-SNYDER-1947] [SRC-CAUSALSET-1987]

### 2.2 Modified propagation

GRB 090510 observations provide a benchmark for realizations that necessarily predict an energy-dependent photon speed or modified dispersion. [SRC-FERMI-2009-GRB090510]

The result constrains the tested propagation law; it does not constrain a finite-resolution realization that preserves the relevant propagation symmetry exactly.

### 2.3 Coherence loss

Massive-molecule interference demonstrates experimentally accessible quantum superposition at high molecular mass. [SRC-FEIN-2019-25KDA] Established collapse-model analyses show how matter-wave data can be translated into parameter exclusions for specific objective-collapse dynamics. [SRC-TOROS-BASSI-2018-INTERFEROMETRY]

Enterprise Math cannot import those exclusions directly. A future physical realization must first derive its own quantitative coherence factor or visibility loss.

### 2.4 Spontaneous radiation and heating

CSL spontaneous-radiation analyses provide an established exclusion strategy when a collapse model predicts an unavoidable photon-emission channel. [SRC-PISCICCHIA-2017-CSL-RADIATION]

Bulk-heating calculations likewise constrain collapse models that predict unavoidable energy injection. [SRC-ADLER-VINANTE-2018-HEATING] Diósi–Penrose heating bounds provide a related benchmark for gravity-related collapse models and ultralow-temperature heat-leak measurements. [SRC-VINANTE-ULBRICHT-2021-DP-HEATING]

P016 therefore requires a concrete Enterprise Math physical model to derive its radiation/heating law before comparing with these experiments.

### 2.5 Exact conserved charges

Borexino's charge-conservation search supplies a benchmark for models that necessarily permit the tested charge-nonconserving electron-decay channel. [SRC-BOREXINO-2015-CHARGE]

Fundamental many-to-one evolution does not logically imply charge violation. A realization can impose exact conservation, or it can predict a defect and face the corresponding experiment.

## 3. Project-specific synthesis

`EM-COMP-013` is the protocol-level synthesis:

1. specify explicit physical states and forward transition law;
2. specify the observation map;
3. state exact/emergent symmetry and conservation claims;
4. state the prior allowed parameter region;
5. derive at least one unavoidable quantitative observational consequence;
6. define an explicit `falsified_if` condition before interpreting the experiment.

A null result that excludes only part of parameter space is a parameter exclusion, not a rejection of the entire Enterprise Math framework. Conversely, a model that can remove every observational consequence after seeing the data has not yet become a falsifiable physical theory.

## 4. Novelty boundary

The graph metric, Lorentz tests, gamma-ray propagation tests, matter-wave interferometry, objective-collapse exclusion methods, spontaneous-radiation/heating tests, and charge-conservation searches are established prior work.

Enterprise Math's historical novelty remains `NOVELTY_UNVERIFIED`. P012/P016 claim only a project synthesis: intrinsic finite-state geometry on one side, and a disciplined quantitative kill-test contract for later physical realizations on the other.
