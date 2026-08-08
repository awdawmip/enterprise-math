# P016 — Physical falsification contract for finite-resolution fundamental collapse

Status: `PROPOSED FALSIFICATION PROTOCOL`  
Open problem: `P016`  
Scope: physical models that instantiate finite resolution and fundamental many-to-one dynamics

## 1. What P016 can and cannot falsify

Enterprise Math currently contains a stronger physical hypothesis:

> finite-resolution many-to-one state evolution may be fundamental rather than only an effective coarse-grained description of a hidden reversible continuum.

At this level the statement is still too broad to be killed by one null experiment. A model can preserve Lorentz symmetry exactly, choose a collapse scale far beyond present reach, or couple many-to-one dynamics only to variables not measured by a particular experiment.

Therefore P016 must not pretend that “discrete physics” or “fundamental collapse” has already been experimentally excluded.

Instead, P016 establishes a **falsification contract**:

> every concrete physical realization of the hypothesis must expose at least one unavoidable quantitative observational consequence. If all consequences can be removed after seeing the data, the realization is not a falsifiable physical theory.

This document separates:

- mathematical inconsistency;
- falsification of a concrete physical realization;
- experimental pressure on a parameter region;
- failure to falsify the broad framework.

## 2. Minimal physical realization record

A physical Enterprise Math model should specify at least

\[
\mathcal M=(X,T,\Pi,\mathcal S,\mathcal Q,\theta).
\]

Here:

- \(X\): explicit physical state space;
- \(T\): fundamental forward transition law or family of transition laws;
- \(\Pi\): map from fundamental states to measurable observables;
- \(\mathcal S\): exact or emergent symmetry structure;
- \(\mathcal Q\): quantities claimed to be exactly conserved;
- \(\theta\): finite parameters such as resolution scales, collapse rates, correlation lengths, preferred directions, or coupling strengths.

A model that specifies only “nature is finite resolution” but no \(T\), \(\Pi\), symmetry realization, or observable parameter cannot yet be physically falsified.

## 3. Three different failure modes

### A. Mathematical failure

The model is internally inconsistent before experimental comparison.

Examples:

- the proposed transition is not well-defined on the claimed state domain;
- two proved conservation rules contradict each other;
- the proposed symmetry action is not compatible with the transition law;
- a claimed metric fails its own axioms.

This is a mathematical rejection, not a physical falsification.

### B. Physical falsification

The model makes an unavoidable quantitative prediction whose allowed range is disjoint from observation.

Schematically, if the model implies

\[
O\in P_{\mathcal M}
\]

for an observable \(O\), while experiment establishes

\[
O\in E
\]

with

\[
P_{\mathcal M}\cap E=\varnothing,
\]

then that model realization is falsified at the confidence level of the experimental constraint.

### C. Parameter exclusion

If only part of \(\theta\)-space is incompatible with data, the correct result is a parameter exclusion, not rejection of the entire framework.

This distinction is standard in experimental tests of Lorentz violation and objective-collapse models.

## 4. Kill test F1 — preferred-direction / rotational anisotropy

A naive fixed lattice or primitive adjacency can introduce preferred directions. If a concrete model says such anisotropy must survive into atomic, optical, inertial, or propagation observables with amplitude \(A(\theta)\), then a null anisotropy search supplies an upper bound

\[
A(\theta)\le A_{\rm exp}.
\]

The model is excluded wherever it predicts

\[
A(\theta)>A_{\rm exp}.
\]

### Existing benchmark

Sanner et al., *Optical clock comparison test of Lorentz symmetry* (2018), compared two single-ion clocks with nonparallel quantization axes. They reported no sidereal modulation at the \(10^{-19}\) fractional-frequency level and derived electron-sector Lorentz-violation constraints around the \(10^{-21}\) level in their chosen SME coefficients.

This is an example benchmark, not a universal translation into Enterprise Math parameters.

### Important non-falsification caveat

Discreteness does **not** logically imply Lorentz or rotation violation. Snyder-type discrete spacetime and causal-set approaches are prior examples of discrete structures designed to retain Lorentz symmetry or avoid a fixed preferred lattice.

Therefore the kill condition is not

> “space is discrete, therefore Lorentz tests falsify it.”

It is

> “this concrete discrete realization predicts an anisotropy larger than the experimental bound.”

## 5. Kill test F2 — energy-dependent propagation / modified dispersion

Many quantum-gravity or discrete-kinematics models predict a modified dispersion relation, for example an energy-dependent photon velocity

\[
v(E)=c\,[1+\delta(E;\theta)].
\]

If finite resolution in a concrete Enterprise Math realization necessarily produces such a \(\delta\), long-baseline transient propagation is a direct test.

### Existing benchmark

The Fermi GBM/LAT analysis of GRB 090510 reported a 31 GeV photon during the prompt burst and used the short time structure plus known redshift to constrain a linear energy dependence of photon propagation speed. In the interpretation used by the collaboration, the corresponding quantum-gravity mass scale was forced above the Planck mass.

Again, this does not constrain a finite-resolution model that predicts exactly Lorentz-invariant propagation. It constrains realizations with unavoidable modified dispersion of the tested form.

### Falsification form

If a model predicts a minimum propagation delay

\[
|\Delta t(E_1,E_2,L;\theta)|\ge\Delta t_{\rm model}
\]

but observations imply

\[
|\Delta t|<\Delta t_{\rm exp}<\Delta t_{\rm model},
\]

that parameter region is excluded.

## 6. Kill test F3 — fundamental decoherence / loss of quantum interference

A genuinely many-to-one physical transition may destroy phase information. If a concrete model couples that loss to quantum superpositions, it must predict a visibility or coherence reduction.

Represent the unavoidable coherence factor by

\[
0\le\eta(m,\Delta x,t;\theta)\le1.
\]

If standard environmental decoherence is independently modeled and the fundamental model predicts

\[
V_{\rm predicted}=\eta V_{\rm ordinary},
\]

then sufficiently high observed visibility can exclude the parameter region producing too small \(\eta\).

### Existing benchmarks

Matter-wave interferometry already constrains objective-collapse models. Toroš and Bassi derived parameter exclusions for several collapse models from molecule-interference data.

Fein et al. experimentally observed quantum interference for molecules above 25 kDa, containing up to roughly 2,000 atoms, with measured fringe visibility above 90% of the quantum prediction in their experiment.

These experiments do not directly test generic Enterprise Math collapse. They become relevant only after an Enterprise Math realization provides a quantitative map from its many-to-one transition to loss of quantum coherence.

### Hard falsification rule

A model cannot evade every coherence experiment by declaring that its collapse “does not affect quantum amplitudes” unless it then specifies where the fundamental information loss is physically observable. Otherwise the model moves outside experimental reach rather than surviving a test.

## 7. Kill test F4 — spontaneous energy injection, heating, or radiation

Nonunitary stochastic collapse dynamics often inject energy. A concrete fundamental-collapse model may similarly imply a minimum heating power or spontaneous radiation rate

\[
P_{\rm collapse}(m,T,\theta),
\qquad
\Gamma_\gamma(E;\theta).
\]

If that output is unavoidable, low-background and low-temperature experiments are direct tests.

### Existing benchmarks

Piscicchia et al. analyzed spontaneous X-ray radiation and excluded broad regions of Continuous Spontaneous Localization parameter space.

Adler and Vinante showed how bulk heating constrains mass-proportional collapse-noise models.

Vinante and Ulbricht revisited spontaneous-heating constraints on Diósi–Penrose-type models and emphasized that some parameter-free versions approach exclusion from low-temperature heat-leak measurements.

These examples demonstrate the correct logic: derive an unavoidable energy-production law first, then compare with measured backgrounds.

### Falsification form

If the model implies

\[
P_{\rm collapse}\ge P_{\min}(\theta)
\]

while experiment bounds unexplained power by

\[
P_{\rm unexplained}<P_{\min}(\theta),
\]

that realization is excluded.

## 8. Kill test F5 — violation of exactly conserved charges

A many-to-one map need not violate charge, momentum, angular momentum, or other conserved quantities. But if a concrete transition law does, it must state the defect.

For a claimed conserved quantity \(Q\), define

\[
\Delta Q(x)=Q(Tx)-Q(x).
\]

There are two legitimate model choices:

1. impose \(\Delta Q=0\) exactly as part of the transition law;
2. predict a nonzero distribution/rate for \(\Delta Q\) and face experiment.

It is not legitimate to assert fundamental information loss and then assume conservation defects are “too small to matter” without calculating them.

### Existing benchmark

The Borexino collaboration searched for electron decay \(e\to\nu+\gamma\), a charge-nonconserving process, and reported an electron lifetime lower bound of

\[
\tau>6.6\times10^{28}\ \text{yr}
\]

at 90% confidence in that channel.

This does not mean every collapse model predicts electron decay. It means any realization that necessarily permits the tested charge-violating channel above this rate is excluded.

## 9. Kill test F6 — exact reversal / echo experiments

If a model claims that even a carefully isolated finite system undergoes irreversible many-to-one evolution at a minimum rate, then sufficiently precise reversal protocols can test it.

Let a protocol prepare a family of states, evolve forward, apply an experimentally implemented inverse control sequence, and measure return probability

\[
P_{\rm return}(t;\theta).
\]

A fundamental many-to-one loss model must specify a maximum achievable return probability below one after environmental and control errors are removed:

\[
P_{\rm return}\le1-\epsilon_{\rm fundamental}(t;\theta).
\]

If experiments establish a lower bound exceeding that prediction,

\[
P_{\rm return}^{\rm exp}>1-\epsilon_{\rm fundamental},
\]

that realization is falsified.

This category includes quantum-echo, Loschmidt-echo, error-corrected reversal, and process-tomography style tests, but P016 deliberately does not assign a universal bound until a particular Enterprise Math model specifies the observable channel.

## 10. Kill test F7 — a hard finite-resolution threshold

A concrete finite-resolution theory may claim that a physical observable has a smallest meaningful increment

\[
\delta_* >0.
\]

If the claim is ontological rather than only instrumental, it must specify what happens when an experiment compares states separated by less than \(\delta_*\).

A hard-threshold realization is falsified if experiments reproducibly distinguish two predicted-identical states or observe a response that the model says must be exactly absent below \(\delta_*\).

### Crucial caution

Measurement uncertainty smaller than the Planck length or another proposed fundamental scale is not by itself the same as directly resolving an ontological spatial interval of that size. Statistical parameter estimation can beat the scale of individual microscopic features.

Therefore the model must give an operational prediction, not merely equate “experimental precision” with “physical lattice spacing.”

## 11. Kill test F8 — symmetry algebra failure

A discrete model may claim that Lorentz, rotation, translation, gauge, or other symmetries are exact even though the underlying state space is discrete.

Then the correct mathematical question is whether the symmetry action actually exists on \(X\) and commutes/intertwines with the transition and observation maps.

For a symmetry \(g\), a strong exact requirement is

\[
T(gx)=gT(x)
\]

and an observation-covariance condition of the appropriate form.

If the model cannot satisfy its claimed symmetry algebra even before comparison with data, that is mathematical failure. If it satisfies the algebra but predicts small symmetry-breaking observables after coarse observation, those observables belong to F1/F2-type experiments.

## 12. Kill test F9 — conservation of probability / quantum-state normalization

If an Enterprise Math realization operates directly on quantum states or density matrices, it must specify whether its map is linear, completely positive, trace preserving, norm preserving, or something else.

A deterministic many-to-one map on hidden discrete states is not automatically equivalent to a nonunitary map on the quantum state accessible to experiment.

If the model predicts trace loss, negative probabilities, superluminal signaling, or other operationally forbidden behavior, those are direct mathematical/physical rejection routes.

If it instead induces a legitimate quantum channel, then experiments constrain the channel parameters through coherence, heating, spectroscopy, clocks, or other observables.

## 13. A model cannot use hidden history to evade its own ontology

The current Enterprise Math physical route intentionally tests fundamental many-to-one evolution without assuming that every lost distinction survives in an unobserved reversible completion.

Therefore a proposed physical realization cannot answer every falsification test by adding an unlimited hidden history register that restores one-to-one microscopic evolution. Doing so changes the hypothesis back toward a reversible completion and should be classified as a different physical model.

Auxiliary variables are allowed when explicitly part of the physical state. The prohibition is semantic sleight of hand: claiming ontological loss while silently storing all lost information elsewhere.

## 14. Falsification matrix

| Model commitment | Observable signature | Kill condition |
| --- | --- | --- |
| Preferred discrete direction survives | Sidereal/orientation modulation | Predicted minimum anisotropy exceeds null-search bound |
| Modified dispersion | Energy-dependent time of flight | Predicted delay exceeds transient bound |
| Fundamental quantum decoherence | Reduced interference visibility / purity | Predicted visibility lies below observed lower bound after known decoherence |
| Collapse injects energy | Heating / spontaneous photons | Predicted unavoidable power/rate exceeds background limit |
| Collapse violates conserved charge | Forbidden decay / charge defect | Predicted rate exceeds experimental upper bound |
| Closed systems lose reversible information | Imperfect echo / return probability | Fundamental deficit exceeds measured deficit after controls |
| Hard resolution scale | Exact indistinguishability below threshold | Experiment distinguishes states the model declares identical |
| Exact symmetry claimed | Algebra/covariance relations | Model cannot realize its own symmetry or predicts excluded residual breaking |

## 15. What counts as surviving a test

A model survives a test only if its **predeclared** parameter region remains compatible with the data.

The following do not count as strong survival:

- adding a new free parameter after every null result;
- moving the collapse channel to an unobservable sector without specifying a new test;
- replacing a predicted lower bound by an arbitrarily small effect after the fact;
- introducing a complete hidden reversible history while continuing to call the dynamics fundamentally many-to-one.

A healthy research program should progressively reduce this freedom.

## 16. P016 status

P016 is resolved as a **falsification protocol**, not as an experimental verdict on the broad physical hypothesis.

The protocol says that every physical realization must expose quantitative kill conditions in at least one of the categories above. A future Enterprise Math physical model should include a machine-readable or table-form `FALSIFICATION` section containing:

1. model parameters and allowed prior ranges;
2. exact symmetry assumptions;
3. exactly conserved quantities;
4. unavoidable observable deviations;
5. experiments/data that currently constrain those deviations;
6. parameter regions already excluded;
7. one or more future observations that would reject the remaining region.

Until such an instantiation exists, the mathematically proved Enterprise Math framework must not be advertised as experimentally confirmed physics.

## 17. Prior-art and experimental benchmarks

The experimental logic used here is established physics methodology, not an Enterprise Math invention.

Primary benchmarks consulted for this draft include:

- Fermi GBM/LAT Collaboration, *Testing Einstein's special relativity with Fermi's short hard gamma-ray burst GRB090510* (2009), for energy-dependent propagation constraints;
- C. Sanner et al., *Optical clock comparison test of Lorentz symmetry* (2018), for orientation/sidereal Lorentz tests;
- Y. Y. Fein et al., *Quantum superposition of molecules beyond 25 kDa* (2019), for macromolecular coherence;
- M. Toroš and A. Bassi, *Bounds on Collapse Models from Matter-Wave Interferometry* (2016), for collapse-model exclusions from interference;
- K. Piscicchia et al., *CSL Collapse Model Mapped with the Spontaneous Radiation* (2017), for spontaneous-radiation bounds;
- S. L. Adler and A. Vinante, *Bulk Heating Effects as Tests for Collapse Models* (2018), and A. Vinante & H. Ulbricht (2021), for heating constraints;
- Borexino Collaboration, *A test of electric charge conservation with Borexino* (2015), for a charge-conservation benchmark.

These sources must receive stable `SRC-*` entries and lineage relations before this Draft becomes review-ready. Some may be classified as `CONTRAST` rather than `ADOPT`, because they constrain neighboring physical realizations rather than directly testing Enterprise Math.
