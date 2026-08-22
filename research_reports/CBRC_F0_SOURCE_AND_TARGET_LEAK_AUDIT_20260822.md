# CBRC F0 Source and Target-Leak Audit

Status: `PHASE_A_BLIND_FORWARD / AUDIT`
Date: `2026-08-22`
Researcher-ID: `EM-CBRCF0-4E91C7`
Task-ID: `RS-CBRC-F0-NATIVE-RECOALESCENCE-FORWARD-DERIVATION`

## 1. Frozen mathematical source boundary

Only these mathematical sources were used:

| Source | Blob SHA | Used for |
|---|---|---|
| `definitions/00_CURRENT_NATIVE_FOUNDATION.md` | `c3140417e061932b4415f86cad397fc2de91d3c2` | current native typing/router facts |
| `definitions/ENTERPRISE_THREE_POSITIVE_AXIS_OVERLAPPING_CIRCLE_CELL_PLANE_20260820.md` | `393060ebfd6a86ad45f258747d78a14d9c8ac153` | one-cell state, triple incidence, positive axes/sectors |
| `definitions/ENTERPRISE_NATIVE_LINE_TRACE_FORMULA_20260821.md` | `b631242db84c5bd3640e6dc554b19a1d04d464f3` | component trace, shuffle paths, `(1,1)` commuting diamond, composition |
| `definitions/ENTERPRISE_BRC_MULTIPATH_ENRICHMENT_BRIDGE_20260821.md` | `6ec0d73a19e28ec586c59a97d24f5798c9119771` | Path/N/Boolean tower, typed skeleton, forgetful maps, `2->2->1` |

Taskbook source: `b3ae07ca418d3e747d3b58bf8e6e2c8ab256dd7a`.

The mathematical freeze was taken from issue base `enterprise-math/main@18260c780295edabbaaca746e5210478a1d98180`.

## 2. Forbidden preload audit

Phase A did not read or use:

- R063 Stage 1–4 material;
- R064 material;
- downstream/free-research coherent-BRC or wave candidates;
- external quantum mechanics;
- quantum walks;
- amplitude or probability-amplitude formalisms;
- wave equations;
- path integrals;
- gauge-field theory as an imported premise;
- continuum differential equations;
- downstream Hodge/Shor results.

The words “gauge” and “curvature” in the F0 packet name elementary presentation equivalence and the product ratio around a four-edge native commuting diamond. They are defined from scratch in the report and do not import an external field theory.

## 3. Target-leak inventory

Every object below is absent as a literal mathematical object from the four source files and is therefore audited.

| F0 object | Generation step | Why allowed / not imported |
|---|---|---|
| residual typed support `B(w)` | Q1: replay finite trace continuations | direct subset of allowed `X_i/X_j` next steps |
| conservative extension order | Q2: preserve old N semantics while enabling cancellation | formalizes “extension” + no-resurrection/refinement requirement |
| additive group completion | Q2: exact inverse required for a nonzero occurrence | universal consequence of conservative exact cancellation |
| signed path formal sums | group completion basiswise on concrete Path-formal witnesses | generated from existing path basis; no path data invented |
| unit edge transport `u_i,u_j` | Q3: reversible scalar action on minimal signed carrier | automorphisms of the derived scalar carrier are exactly `±1` |
| vertex gauge `g` | Q3: classify presentation changes | derived equivalence from changing local sign representatives |
| diamond curvature `kappa` | Q3: ratio of the two native `(1,1)` route transports | invariant computed from native commuting diamond |
| canonical representative `u_j=1, u_i=kappa^y` | Q3: explicit gauge representative | derived by elementary recursive gauge fixing |
| inversion count `inv(w)` | Q3: closed form for canonical path transport | counts order pairs in the existing generator word |
| twisted concatenation factor `kappa^(bc)` | Q3: composition of inversion counts | derived combinatorially from cross pairs on concatenation |
| free signed branch carrier | Q3 mixing test | finite branchwise restriction of signed path group completion |
| same-terminal aggregation `A` | Q4/final collapse | extension of existing terminal recoalescence by signed sum |
| tagged readout `D_f` | Q4 distinguishable additivity | operational construction for explicitly marked alternatives |
| scalar family `R_f` | Q4 underdetermination test | not assumed; two exact countermodels are exhibited |
| `SAME_SIGN_MARKER_ERASURE_INVARIANCE` | Q4 requested weakest extra selector | explicitly labeled counterfactual, not promoted |
| dark/constructive signed presentations | Q5 discriminator | use only two signed basis coefficients on the frozen `(1,1)` fiber |

## 4. Forbidden-premise audit

### Coefficient ring/field
Not assumed.

The calculation starts from the source's nonnegative formal sums. Additive inverses are introduced only after proving N/Boolean cancellation impossible. The signed additive group is obtained by a universal completion. Typed multiplication is then extended from path concatenation by distributivity.

### Finite/continuous phase group
Not assumed.

The two signs arise because the automorphism group of the derived infinite cyclic additive carrier has exactly two elements. No phase carrier is selected beforehand.

### Bilinear/inner-product structure
Not introduced.

### Power/norm exponent
Not assumed.

The audit explicitly proves the readout exponent/function is underdetermined by giving `|n|` and `n^2` as incompatible exact countermodels.

### Transform matrix
Not assumed.

A generic 2x2 integer update is introduced only as an exhaustive/no-go parameterization for the local mixing classification; relabeling equivariance plus invertibility reduce it to `±I, ±swap`.

### Probability/readout formula
Not assumed.

Candidate scalar laws are introduced only after the operational Q4 axioms are stated, and nonuniqueness is the conclusion.

### Continuum equation
None.

### Target algebra selected for downstream matching
None.

## 5. Native semantic guardrail audit

- one-cell instantaneous state preserved: PASS;
- triple incidence not modeled as simultaneous three-cell state: PASS;
- exactly three positive axes retained: PASS;
- no negative native axis introduced: PASS;
- no diagonal-shift coordinate quotient: PASS;
- no use of carrier `e1+e2+e3=0` as native identity: PASS;
- native line identity remains component trace: PASS;
- same carrier endpoint not used as line identity: PASS;
- Path provenance retained until an explicit forgetful/final aggregation: PASS;
- N/Boolean discarded information never resurrected: PASS;
- no new native spatial direction: PASS.

## 6. Source-to-proof trace

### Q1
Plane one-cell/triple-incidence semantics + line trace generator language imply residual support arity.

### Q2
BRC bridge's N and Boolean coefficient laws imply no exact cancellation. Conservative cancellation yields universal additive group completion.

### Q3
Path-formal typed concatenation + derived signed group imply reversible edge units `±1`. Native commuting diamond yields the gauge-invariant path-ratio classifier.

### Q4
No source supplies a scalar law. The taskbook operational requirements are tested directly and shown insufficient by exact countermodels.

### Q5
The whitelist-minimal `(1,1)` fiber supplies the smallest support on which signed aggregate `2` versus `0` can be witnessed without changing native support.

## 7. Audit verdict

`TARGET_LEAK_AUDIT_PASS`

No Phase-A kill condition was triggered.

Primary research verdict remains:

`F0_UNDERDETERMINED_BY_CURRENT_FOUNDATION`
