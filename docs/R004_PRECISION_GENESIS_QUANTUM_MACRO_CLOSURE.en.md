# R004 — Precision Genesis, Quantum–Macro Boundary, and Closure

Status: `PROVED_WIP + EXECUTABLE_CHECKED + PHYSICAL_PREMODEL`  
Source snapshot: `main@0d6b751e0d16ba0049369e912e1730e3383f0f58`  
Owner branch: `research/r004-precision-genesis-closure-20260810`  
Discipline: mathematical statements, executable checks, prior art, and physical hypotheses are separated explicitly below.

## 1. Result in one sentence

The precision-genesis idea can be made into a finite exact mathematical program, but not yet a physical cosmology: the strongest first-stage result is a branch-compatible collision-spectrum theorem showing that state-extensional relational refinement can increase available/path distinguishability without ever undoing previously merged history, while several no-go results show that refinement alone cannot identify ontic creation, cannot force geometry, cannot determine a physical `lambda_max`, and cannot by itself produce an entropy law involving ambient capacity.

## 2. Ownership and canonical dependencies

R004 does **not** create duplicate mother theories.

| Surface | R004 use | Owner / canonical home |
| --- | --- | --- |
| positive integer scale and divisibility order | scale labels and compatible forgetting | A0 / P005 |
| typed scale state | prevent type-erased fake dynamics | P009 |
| deterministic history merge / collision spectrum | deterministic degeneration and collision interpretation | A1 / P010 / P011 |
| observation and future-safe quotient | task-relative distinguishability | A2 / P018 / P023 |
| coarse-to-fine multivalued support | refinement correspondence | A4 |
| primitive adjacency, graph metric, shells/balls | emergent-geometry observables | A5 / P012 / P022 |
| quantitative physical kill tests | physics gate | P016 |

R004 owns only the **precision-cosmology composition layer**: how these existing surfaces can be assembled into a finite genesis toy model, what new cross-surface theorems follow, where the assembly necessarily fails, and what additional commitments are required before P016 can test it.

## 3. Exact finite definitions

### D1 — Precision scale chain

A finite precision chain is

\[
1=\lambda_0\mid\lambda_1\mid\cdots\mid\lambda_T=\lambda_{\max},
\]

with a finite physical state set `X_lambda` at each layer and a surjective forgetting map

\[
p_{\mu\to\lambda}:X_\mu\to X_\lambda\qquad(\lambda\mid\mu).
\]

The label `lambda=1` means **coarsest physical distinguishability**, not minimum length.

### D2 — Precision-one physical pregeometry

The strongest non-geometric definition that does not presuppose a continuum is:

1. the physical quotient `Q_1` has exactly one class;
2. every structure called *physical geometry* is defined on `Q_1` itself or factors through it;
3. no unobservable carrier relation is silently promoted to physical geometry.

Under this definition there is no nontrivial physical distance, direction, adjacency, shell, or causal separation at `lambda=1`.

### D3 — Relational refinement

For `lambda | mu`, refinement is a finite serial correspondence

\[
J_{\lambda\to\mu}\subseteq X_\lambda\times X_\mu,
\]

not a unique inverse function. In the projection-compatible case,

\[
(x,y)\in J_{\lambda\to\mu}\Longrightarrow p_{\mu\to\lambda}(y)=x.
\]

Serial means every currently occupied state has at least one admissible successor.

### D4 — State-extensional evolution

Let `H_t` be a set of path histories ending in physical states `X_t`. Evolution is **state-extensional** when all histories with the same current physical endpoint are assigned the same successor support. Equivalently, a history-indexed successor relation factors through the current-state map.

This is the exact no-hidden-history condition required for later refinement not to read distinctions that were already physically merged.

### D5 — History multiplicity

Let

\[
n_t(x)=\#\{h\in H_t: \operatorname{end}(h)=x\}.
\]

For a serial state-extensional relation `R_t subset X_t x X_(t+1)`, propagate every current history along every admissible edge:

\[
n_{t+1}(y)=\sum_{x\,R_t\,y}n_t(x).
\]

This is finite path branching, not a quantum amplitude.

### D6 — Collision/path spectrum

For `k>=1`, define

\[
W_k(n)=\sum_x {n(x)\choose k}.
\]

`W_1` is the number of represented path histories. `W_2` counts unordered pairs of distinct histories that currently share an endpoint. Higher `W_k` count merged `k`-tuples.

Also define

\[
H(n)=\sum_x n(x),\qquad
A(n)=\#\{x:n(x)>0\},\qquad
M(n)=H(n)-A(n).
\]

`A` is occupied endpoint distinguishability and `M` is merge excess: the number of represented histories beyond one representative per occupied endpoint.

## 4. R004-T01 — Branch-compatible collision-spectrum monotonicity

Status: `PROVED_WIP`; exhaustive finite regression supplied separately.

**Theorem.** Let `X,Y` be finite, `n:X->N_0`, and let `R subset X x Y` be serial on the support of `n`. Define

\[
n'(y)=\sum_{xRy}n(x).
\]

Then for every integer `k>=1`,

\[
\boxed{W_k(n')\ge W_k(n).}
\]

In addition,

\[
\boxed{M(n')\ge M(n).}
\]

### Proof

For every occupied `x`, choose one successor `f(x)` with `x R f(x)`; finiteness and seriality are enough. For each `y`, put

\[
m(y)=\sum_{f(x)=y}n(x).
\]

Because all selected edges are also edges of `R`, `n'(y)>=m(y)`. For fixed `k`, the function `a -> binom(a,k)` is nondecreasing on nonnegative integers. Moreover Vandermonde's identity gives the superadditivity

\[
{a+b\choose k}\ge {a\choose k}+{b\choose k}.
\]

Therefore, grouping sources by the chosen target,

\[
\sum_y {n'(y)\choose k}
\ge
\sum_y {m(y)\choose k}
\ge
\sum_x {n(x)\choose k}.
\]

For merge excess use `g(0)=0`, `g(a)=a-1` for `a>0`. The same grouping argument works because `g` is nondecreasing and superadditive on nonnegative integers. Hence `M(n')>=M(n)`. ∎

### Meaning

A refinement relation may create several future endpoints, but if it depends only on the current merged physical state, every branch inherits the same already-merged multiplicity. **Refinement can create new alternatives without resurrecting old history identity.**

This theorem consumes A1 collision ideas and A4 correspondence semantics; it should be relayed to those owners rather than promoted as an R004-owned replacement mother theorem.

## 5. Exact branching/merge balance

For a serial relation define the branching increment

\[
B_t=\sum_x n_t(x)(\deg_R(x)-1).
\]

Then, by direct counting,

\[
\boxed{H_{t+1}=H_t+B_t.}
\]

Since `M=H-A`, there is an exact finite balance identity

\[
\boxed{
M_{t+1}-M_t
=B_t-(A_{t+1}-A_t).
}
\]

Together with R004-T01,

\[
A_{t+1}-A_t\le B_t.
\]

This is the first precise R004 answer to the requested “opposite monotonicities” problem. New path alternatives created by relational branching either appear as newly occupied distinguishable endpoints or accumulate as additional endpoint multiplicity. No real-valued entropy is required.

**Boundary:** ambient capacity

\[
C_t=|X_t|
\]

is not present in this identity. Capacity can grow without being occupied. Therefore this balance law is **not** a conservation law between physical capacity and irreversibility.

## 6. R004-C01 — Why the fixed initial-history arrow is ill-posed

Status: `COUNTEREXAMPLE / DEFINITION CORRECTION`.

If precision-one pregeometry literally begins with one physical state and one physical history, then the number of equivalence classes of that fixed initial-history cohort is already `1`. A quantity constrained to decrease thereafter cannot express a nontrivial arrow of time.

Therefore the relevant history object cannot be only the singleton Big-Bang cohort. It must include **path histories born under later refinement/branching**. The multiplicity formulation above makes this precise.

## 7. R004-C02 — History-indexed refinement resurrects lost history

Status: `COUNTEREXAMPLE`.

Take two histories that share one current state, so `n(x)=2` and `W_2=1`. If a forbidden history-indexed rule sends the first history to `y_0` and the second to `y_1`, then the new multiplicities are `(1,1)` and `W_2=0`.

Thus the no-resurrection theorem fails immediately if refinement can inspect hidden history identity. This is not a technical nuisance; it is the exact ontology boundary.

The exhaustive toy check with two merged histories and three possible future states finds:

- `7` nonempty state-extensional successor supports, with `0` resurrection cases;
- `49` history-indexed support pairs, of which `42` resurrect/distinguish the two histories.

## 8. R004-T02 — Finite latent-master representation no-go

Status: `PROVED_WIP / PRIOR_ART-BASED IMPOSSIBILITY BOUNDARY`.

For a finite deterministic projection tower, all layers can be represented as finite views of one finite compatible-path space. In the simplest surjective chain, the top layer itself can serve as the master carrier and every lower state is its projection. More generally, take the finite set of compatible tuples in the product of all layers.

Therefore the extensional data of a finite refinement tower cannot distinguish:

- A. fine alternatives were already latent in a finite master state;
- B. refinement genuinely created new physical alternatives;
- C. alternatives existed only as relational potential and actualized later.

This does **not** reintroduce a continuum. The latent master may be finite. It shows something sharper: **finite refinement structure by itself is ontologically underdetermined.**

Consequently “Big Bang = precision opening” becomes more than a renaming only after adding a generative commitment that has operational consequences beyond the projection tower itself.

## 9. R004-T03 — Rational branching still has a finite pre-sampled completion

Status: `PROVED_WIP / PRIOR_ART-BASED IMPOSSIBILITY BOUNDARY`.

Adding finite rational probabilities does not solve the preceding problem. For any finite-horizon process with rational path probabilities, choose a common denominator `D`; replace each path of probability `a/D` by `a` equiprobable finite seed atoms. The resulting finite latent seed space reproduces the full joint distribution exactly.

Hence stochastic/branching language alone does not operationally distinguish “generated now” from “pre-sampled finitely in advance”. To separate those ontologies, R004 needs additional causal/intervention structure, not merely randomness.

The executable helper verifies the one-step building block exactly with integer multiplicities; e.g.

\[
(1/2,1/3,1/6)\leftrightarrow D=6,\ (3,2,1).
\]

## 10. Geometry emergence: theorem and failure boundary

### R004-T04 — Singleton quotient excludes nontrivial quotient geometry

Status: `PROVED_WIP`, specialization of elementary graph theory/P012.

If physical geometry is a simple graph **on the physical quotient** `Q_lambda`, then `|Q_lambda|=1` implies there are no nontrivial edges and all intrinsic distances are trivial.

### R004-C03 — One observable class does not exclude hidden geometry

Status: `COUNTEREXAMPLE + EXECUTABLE_CHECKED`.

Let a hidden carrier have three points but let the observation map send all three to one physical class. The hidden carrier admits `2^3=8` labeled simple graphs, of which `7` are nonempty and `4` are connected. Therefore

\[
|Q_1|=1\not\Rightarrow\text{“the hidden carrier has no graph”}.
\]

The strong pregeometry claim requires **quotient physicality**: unobservable primitive geometry is not counted as physical geometry.

### R004-C04 — More distinguishability does not force geometry

For every scale with `|Q_lambda|>=2`, choose the empty adjacency relation. State cardinality may grow forever while no metric geometry emerges. Therefore a finite threshold

\[
\lambda_{\rm geom}
=
\min\{\lambda:G_\lambda\text{ satisfies a declared geometry predicate}\}
\]

has content only after a separate relation-generation law is specified.

## 11. Toy universe

Status: `EXECUTABLE_CHECKED`; no claim of physical truth.

The reference model uses

\[
\lambda\in\{1,2,4,8\},\qquad X_\lambda=\{0,\ldots,\lambda-1\},
\]

with exact block forgetting

\[
p_{\mu\to\lambda}(y)=y//(\mu/\lambda)
\]

where the ratio is an integer. Refinement is the inverse-image correspondence of that projection.

The toy declares no adjacency below `lambda=4`; at `lambda>=4` it generates a finite cycle graph. Thus `lambda_geom=4` is produced by an explicit relation law, not by cardinality alone. The model computes exact graph distance, shells, balls, and geodesic multiplicity.

A minimal history sequence is:

1. one state/history;
2. precision opening `0 -> {0,1}`, producing multiplicities `(1,1)`;
3. many-to-one collapse `{0,1} -> 0`, producing multiplicity `(2)`;
4. reopening `0 -> {0,1}`, producing `(2,2)` rather than `(1,1)`.

For `W_1,W_2` the sequence is

\[
(1,0)\to(2,0)\to(2,1)\to(4,2).
\]

This is the finite closure mechanism R004 was looking for: **capacity/path alternatives can open while collision irreversibility remains monotone.**

The exhaustive small relation regression checks all `392` nonzero multiplicity cases with two current states, three future states, multiplicities `0,1,2`, and all nonempty serial successor supports. No decrease of `W_k` for `k=1,2,3` is found. This is regression evidence only; R004-T01 supplies the proof.

## 12. Ambient capacity and the absence of a universal entropy conservation law

Status: `PROVED_WIP IMPOSSIBILITY BOUNDARY`.

The two statements

\[
C_t\uparrow,\qquad\text{fixed-cohort recoverability}\downarrow
\]

alone cannot imply a conservation law. Given any finite nondecreasing positive sequence `C_t` and any nonincreasing positive sequence `A_t<=C_t`, one can construct finite state sets of size `C_t` and compatible many-to-one cohort maps having exactly `A_t` image classes.

Therefore no universal identity such as

\[
C_t+A_t=\text{constant}
\]

or a fixed exchange rate between capacity and historical loss follows from the two monotonicities. Extra resource/measure/dynamical assumptions are necessary.

What **is** exact without such assumptions is the path accounting in Section 5: `H'=H+B` and `Delta M=B-Delta A` for the represented path process.

## 13. Maximum finite precision

Status: `COUNTEREXAMPLE / PHYSICAL_HYPOTHESIS BOUNDARY`.

A finite observed prefix cannot identify whether the precision tower truly terminates there. Two models can agree exactly through all tested layers while one stops at `lambda=T` and the other continues to finer finite layers.

Thus a hard `lambda_max` written by hand is not derived physics. R004 must distinguish:

- **hard maximum:** stipulated finite endpoint;
- **emergent maximum:** transition law makes further refinement unreachable;
- **typed maximum:** different physical dimensions have different allowed endpoints;
- **process-effective maximum:** a future language cannot operationally use finer distinctions.

Planck length, Planck time, and action/`hbar` belong to distinct typed calibrations. They must not be collapsed into one dimensionless numerical step.

## 14. Finite-to-continuum recovery

Status: `PRIOR_ART / EXECUTABLE_CHECKED EXAMPLE`.

There is no mathematical obstruction to finite exact models approximating smooth laws. For the rational grid of `f(x)=x^2` on `[0,1]`, the finite left sum is exactly

\[
S_n=\frac{(n-1)(2n-1)}{6n^2}
\]

and

\[
\frac13-S_n=\frac{3n-1}{6n^2}\le\frac1{2n}.
\]

The scaled forward difference is exactly

\[
n\left[f\left(\frac{k+1}{n}\right)-f\left(\frac{k}{n}\right)\right]
=\frac{2k+1}{n},
\]

whose error relative to `2k/n` is exactly `1/n`.

This is mature numerical-analysis mathematics. R004 does not claim it as new. The open problem is harder: derive a **specific** effective continuum law from an Enterprise Math discrete dynamics with controlled error, rather than choosing a continuum target first.

## 15. Quantum–classical boundary: what survives

### 15.1 Fixed mass/size threshold is rejected

A rule of the form “above one atom size / N atoms / fixed mass the world becomes classical” is not viable. The 2026 sodium-nanoparticle matter-wave experiment demonstrates interference for particles above 7,000 atoms and 170,000 Da [SRC-PEDALINO-2026-NANOPARTICLE]. This directly pressure-tests naive size-only variants; it does not itself test an Enterprise Math model that has not supplied a quantitative visibility law.

### 15.2 Finite environment-record premodel

For two alternatives and a finite environment microstate set, let record maps be `r_0,r_1`. Define the exact rational overlap

\[
\eta=\frac{\#\{e:r_0(e)=r_1(e)\}}{|E|}.
\]

The same object size can have `eta=1`, `1/2`, or `0` under different interaction/history conditions. This provides a finite, task/environment-relative variable and is structurally closer to decoherence/environment-as-witness and quantum-Darwinism prior art [SRC-OLLIVIER-POULIN-ZUREK-2005] than to a size threshold.

But `eta` is **not** derived quantum mechanics. It contains no Hilbert-space phase, Born rule, or unitary dynamics.

### 15.3 P016 entry condition

A physical R004 model may enter P016 only after it predeclares a map

\[
\theta,\text{apparatus/environment data}
\longmapsto
(r_0,r_1,\ldots)
\longmapsto
V_{\rm predicted}
\]

or another directly measured observable. If the record maps can be chosen after seeing the data, the model is unfalsifiable. For interference the natural first gate is P016-F3; depending on the concrete dynamics F4/F6/F8/F9 may also apply.

## 16. Prior-art / novelty map

Status of the overall synthesis remains `NOVELTY_UNVERIFIED`.

- `PRIOR_ART`: divisibility/projective systems; inverse/path-space representations; finite rational probability sample spaces; graph metrics; causal sets; finite-information critiques of physical reals; partition refinement/bisimulation; decoherence and environment-as-witness; objective-collapse falsification; Riemann sums/finite differences; coarse-graining/renormalization methods.
- `PROJECT-SPECIFIC COMBINATION`: one finite ontology combining P005 scales, A4 relational refinement, A1 history collision, P023 future language, P012/P022 geometry, and P016 falsification.
- `PROVED_WIP CROSS-SURFACE RESULT`: R004-T01 collision-spectrum/merge-excess monotonicity under serial state-extensional relational branching, plus exact branching/occupied/merge balance.
- `PROVED_WIP NO-GO`: finite deterministic or rational stochastic refinement data do not identify ontic creation; singleton observation does not imply absence of hidden carrier geometry; capacity monotonicity does not determine a universal entropy law or hard `lambda_max`.
- `PHYSICAL_HYPOTHESIS`: precision opening as cosmological genesis; environment/future-language regime as part of a quantum–classical model; typed physical endpoint.

Loop quantum cosmology already provides a distinct discrete/quantum-geometry route in which the classical big-bang singularity is replaced by a bounce [SRC-ASH-PAW-SINGH-2006-LQC]. Therefore R004 cannot claim novelty merely from replacing the classical singularity with nonclassical finite structure.

## 17. Big Bang claim after the no-go theorems

The phrase

> Big Bang = precision/distinguishability opening

is mathematically meaningful only in the weak sense that one can define a finite evolution from one physical quotient class to multiple classes without a background continuum.

It becomes a **new physical model** only if the opening law also fixes unavoidable observables not shared by a finite latent-master completion. R004-T02/T03 show that neither deterministic refinement nor finite rational branching alone meets this bar.

The next decisive object is therefore a **generative intervention law**: a finite rule specifying what future interaction can do based on currently actualized relational data, together with an operational constraint that cannot be reproduced by merely pre-sampling a finite hidden seed without changing the allowed intervention structure.

## 18. Optional black-hole loop

Status: `CONJECTURAL / DEFERRED`.

“one/few classes -> many classes” and “many future classes -> one/few classes” are opposite cardinality motions, not a categorical duality. No adjunction is established until explicit objects, morphisms, functors, and unit/counit (or another precise Galois structure) are supplied.

Ordinary collapse fibers, zero-magnitude basins, clock slowdown, or causal focusing are not event horizons by definition. R004 therefore does not promote the `1 -> universe -> 1` picture.

## 19. Foundation feedback and Relay routing

### Relay #82 — should be emitted

The reusable result is R004-T01 plus the no-resurrection counterexample boundary:

- source: R004 owner branch/commit;
- status: `PROVED_WIP + EXECUTABLE_CHECKED`;
- weakest assumptions: finite state sets, nonnegative integer path multiplicities, serial state-extensional relation;
- relation class: `COMPOSABLE_INDEPENDENT / BRIDGE` to A1 collision spectrum and A4 correspondence;
- downstream actions: A1 test as relational extension of collision spectrum; A4 test as history-multiplicity functor on serial supports; P018/P023 consume as a no-hidden-history refinement invariant.

The latent-master no-go should also be relayed as a `NEGATIVE_BOUNDARY` for any route claiming that refinement structure alone proves ontic generation.

### Foundation Feedback Packet — mature question

Candidate foundation question:

> What is the weakest finite causal/intervention structure under which a state-extensional relational refinement process is **not** operationally equivalent to a finite latent-master/pre-sampled path model, while preserving P018/P023 observation/future-safe layering and A4 correspondence ownership?

This must not overwrite FQ-004's distinction between actual state, observation quotient, and future-safe quotient, nor duplicate FQ-006's partial-operation machinery. The issue is specifically the additional structure required to make “new distinguishability is generated” an operational theorem rather than an interpretation.

## 20. Next-stage split

1. **R004-A / A1↔A4 bridge:** classify equality/strictness cases for R004-T01 and determine whether the full `W_k` monotonicity has a clean relation/hypergraph formulation reusable by A4 without duplicating P011.
2. **R004-B / generative no-go:** formalize the finite latent-master and rational-seed representation theorems, then search for the weakest intervention/causal assumptions that break observational equivalence.
3. **R004-C / geometry:** require the relation-generation law to be local and projection-compatible; search for the first scale at which connectedness, shell growth, dimension-like observables, and directional/causal structure become forced rather than stipulated.
4. **R004-D / P016 physical model:** choose one predeclared finite environment-record dynamics, map apparatus variables to its parameters, and derive an unavoidable matter-wave visibility residual. Kill it against current interference data if necessary.
5. **R004-E / continuum:** derive one macroscopic equation from the toy transition family with an explicit finite error bound; do not import the continuum equation as the microscopic law.
6. **R004-F / typed endpoint:** seek a structural source of process- or dimension-dependent `lambda_max`; treat a hand-set hard cutoff as a baseline countermodel only.

## 21. Current verdict

The world-view loop has advanced to theory **only at the mathematical-architecture level**. We now have a finite exact mechanism in which:

\[
\text{precision/path opening}
+
\text{state-extensional many-to-one merge}
\Longrightarrow
\text{new alternatives without history resurrection},
\]

with a monotone integer collision spectrum and an exact branching/merge accounting law.

What remains missing for a physical theory is equally precise:

- an operationally non-latent generative law;
- a non-stipulated geometry-generation law;
- a structural finite endpoint;
- and a predeclared map to P016 observables.

Until those are supplied, `precision-one -> universe -> quantum/classical -> minimum scale` is a mathematically disciplined research program and physical premodel, not a validated cosmology.
