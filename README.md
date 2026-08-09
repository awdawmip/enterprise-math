# Enterprise Math

> **The continuum is a magnificent approximation. It is not nature's foundation. Precision is not an error bar; it is part of the number itself.**

Enterprise Math is an open research program attempting to rebuild mathematical foundations from **finite resolution, discrete state, integer-first structure, and intrinsically forward evolution**.

[Chinese version](README.zh-CN.md)

## Manifesto: the foundation of the mathematical building must be rebuilt

We choose to state the position plainly.

**We believe that, when mathematics is used to describe nature, the existing mathematical building rests on a fatal abstraction error: laws that are fundamentally discrete, finite-resolution, and finite-information have been modeled by default as continuous, infinitely divisible, and infinitely precise.**

The continuous real line is the clearest example. Between any two points there are always more points; every interval is infinitely divisible; a point is assigned an infinitely precise location. As pure formal mathematics this structure can of course be coherent, and it has supported extraordinary achievements in analysis, geometry, and physics. But **formal success does not make a structure nature's native substrate**.

For centuries, brilliant mathematicians have built higher and higher floors on this foundation. We believe the problem is not their brilliance but the inherited foundation itself. When finite precision, quantization, discretization, rounding, measurement boundaries, irreversibility, or information loss appear, the conventional route usually preserves a hidden continuous world first and then explains those phenomena as approximation, error, noise, numerical truncation, or an external limitation.

Enterprise Math reverses that order.

If nature never supplies infinite information, why should a natural "number" begin life as an infinitely precise point?

If changing scale changes which states are distinguishable, why should precision be only an error bar attached after the computation?

If a many-to-one evolution genuinely sends many states to one state, why must their difference survive as a hidden continuous remainder?

If state evolution through time is directional, why must the foundation begin with an infinitely divisible flow that is so often idealized as reversible?

Our answer is: **it does not have to.**

Enterprise Math is no longer neutral on this foundational question. Our wager is that:

- natural numerical states carry finite information;
- precision / resolution belongs to the state itself rather than being an annotation;
- discrete states and integer operations can be primitive rather than low-precision stand-ins for continuous quantities;
- collapse, quotienting, merging, and information loss can be genuine mathematical evolution rather than defects that hidden variables must repair;
- if continuity is valid at macroscopic scales, it should be **derived** as large-scale structure, limiting behavior, or an effective approximation rather than assumed at the ontological starting line.

This is a wager that can fail. If these primitives cannot rebuild sufficiently powerful algebra, geometry, dynamics, and physics, the program should be shown to fail. If they can, then what must be reconsidered is not one formula but the starting point mathematics has inherited for centuries.

**We choose to push this route all the way. Our judgment is that time and physics will ultimately show that the direction represented by Enterprise Math is the future of mathematics for describing nature.**

## Five foundational reversals

The conventional route is often:

```text
continuous reals / continuous space
    ↓
choose numerical precision
    ↓
round, discretize, mesh
    ↓
compute / measure / simulate
```

Enterprise Math attempts the reverse:

```text
finite state + explicit scale / precision
    ↓
exact integer operations
    ↓
collapse / quotient / relation / support
    ↓
intrinsically forward dynamics
    ↓
discrete geometry and observable structure
    ↓
continuous models, when useful, as derived approximations
```

That creates five foundational reversals:

1. **A number is no longer only a value.** A natural quantity should carry at least state, scale / resolution, and its physical or computational context.
2. **Precision is no longer error.** Precision determines which differences are genuinely distinguishable at the current level.
3. **Collapse no longer pretends to be reversible.** A many-to-one map may genuinely change the information structure of state space.
4. **Time no longer starts from reversibility.** Forward composition, history merging, and stabilization are first-class objects.
5. **Continuity no longer has default privilege.** Continuous structure must earn its place by emerging from the discrete substrate or by working as an effective approximation.

## A one-minute entry point

In the earliest core, the integer \(p\)-th root is

\[
R_p(n)=\max\{k\in\mathbb N:k^p\le n\}.
\]

Therefore,

\[
R_2(2)=1,\qquad R_2(200)=14,\qquad R_2(20000)=141.
\]

The associated collapse operator is

\[
C_p(n)=R_p(n)^p.
\]

Hence

\[
C_2(20000)=19881.
\]

Every integer from 19881 through 20163 has the same square-collapse image, 19881.

The conventional instinct is to ask: "Where did the missing difference go?"  
Enterprise Math first asks a different question: **why must it still be there?**

If the current scale retains only perfect-square structure, states in the same basin may genuinely merge under this evolution. We first study the mathematics generated by that discrete rule, and only then ask whether and how it corresponds to nature.

## This is already more than an idea

Enterprise Math is not merely a philosophical reinterpretation of familiar formulas. The repository has grown from the original root / collapse core into its own families of theorems, counterexamples, formalization assets, and executable research surfaces.

Canonical results already on `main` include:

- **integer roots and carry structure**: root supermultiplicativity, exact multiplicativity criteria, and carry boundaries;
- **collapse algebra**: when perfect-power collapses with different exponents commute, and fixed-point classifications for finite collapse words;
- **scale algebra**: divisibility projections, gcd/lcm scale lattices, and path-independent projection structure;
- **discrete division and typed state**: distinct quotient, same-space collapse, and reversible quotient-remainder semantics, together with descent, termination, and confluence boundaries;
- **history and irreversibility**: history merging under deterministic forward maps, preimage multiplicity, collision spectra, and integer irreversibility observables;
- **discrete geometry**: integer metrics built from primitive-step graph distance rather than from a prior embedding into continuous Euclidean space;
- **stabilization theory**: finite stabilization of monotone downward maps on well-founded orders and stable equivalence for collapse words;
- **future-safe precision**: when a coarse state remains sufficient for later operations and observations, and what information a minimal repair must restore.

Active work continues on the Legendre pressure test, finite-precision proof calculus, composition-safe collapse, action-language precision, root-lattice geometry, causal boundaries, and engineering-physics experiments involving materials, collisions, and world-state evolution.

These layers do not all have the same proof status. Exact status is controlled by the [authoritative problem-status index](docs/PROBLEM_STATUS.en.md) and the corresponding theorem/result documents.

## We are building a foundation, not a single operator

The goal of Enterprise Math is not to turn \(C_p\) into another isolated special function. It is to build a mathematical stack capable of standing on its own:

- **A0 — primitive discrete state algebra**: integer roots, collapse, gap / basin coordinates, scale, quotient-remainder, signed and typed state;
- **A1 — forward dynamics**: composition, collision, history merge, stabilization;
- **A2 — precision and observation**: observation, quotient, future-safe equality, minimal repair;
- **A3 — relation state**: integer relations between states rather than forcing all structure back into a single scalar value;
- **A4 — support and correspondence**: multivalued relations, witnesses, common targets, and composition-preserving structure;
- **A5 — intrinsic discrete geometry**: distance, shells, and geometry built from discrete primitives and reachability;
- **application layer**: number-theory pressure tests, collisions, materials, causal boundaries, and world-state evolution.

The long-term objective is one discrete foundational chain from **number → precision → algebra → dynamics → geometry → physics**, rather than repeatedly approximating downward from a continuous world whenever discreteness appears.

## Confidence does not mean abandoning evidence discipline

If Enterprise Math is serious about challenging a foundation, it must be easier to attack than an ordinary new idea, not harder.

The repository therefore distinguishes:

1. **Definitions** — the discrete primitives we choose.
2. **Proved mathematical results** — strict consequences of those primitives that have reached canonical `main`.
3. **Executable / finite validation results** — useful for discovery, counterexamples, and regression, but not automatically proofs.
4. **Physical and ontological claims** — claims about whether nature is actually like this, which must face experiment and observation.

We will not make the foundational position directionless merely to sound "careful," and we will not turn unproved claims into theorems merely to sound "confident."

**The direction may be radical. The evidence must be ruthless.**

## Originality does not come from ignorance of prior work

Enterprise Math does not treat prior art as a threat.

If a tool already exists, we absorb it. If a theorem is classical, we attribute it. If one of our structures is only a specialization of known mathematics, we say so precisely. The originality worth pursuing is not "we never read anyone else." It is whether:

- we chose different foundational primitives;
- we organized previously separate structures into a new unified system;
- that system produces new theorems, counterexamples, algorithms, geometry, or physical predictions;
- it explains phenomena that the continuous framework usually treats as error or external repair.

Historical priority for individual components remains tracked through `sources.json`, `lineage.json`, and the [prior-art lineage and novelty boundary](docs/PRIOR_ART_AND_NOVELTY.en.md). A claim that a specific result is "first" still requires evidence. That does not prevent us from saying clearly: **Enterprise Math is building a mathematical system of its own.**

## Where to start

Core entry points:

- [shared research surface](docs/RESEARCH_COMMON_SURFACE.en.md)
- [authoritative problem-status index](docs/PROBLEM_STATUS.en.md)
- [proved propositions](docs/THEOREMS.en.md)
- [counterexamples](docs/COUNTEREXAMPLES.en.md)
- [open problems](docs/OPEN_PROBLEMS.en.md)
- [roadmap](docs/ROADMAP.en.md)
- [prior-art lineage and novelty boundary](docs/PRIOR_ART_AND_NOVELTY.en.md)
- [physical falsification contract](docs/P016_PHYSICAL_FALSIFICATION_CONTRACT.en.md)

The reference implementation lives under `src/enterprise_math/`. The Lean entry point is `EnterpriseMath.lean`.

Python regression suite:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

The reference implementation is an executable specification, counterexample finder, and research tool. It is not a substitute for mathematical proof.

## Come attack it

You do not need to believe Enterprise Math first.

The most valuable contribution is not "this is interesting." It is to:

- find a broken definition;
- construct a counterexample to a candidate theorem;
- identify a weaker and more exact hypothesis;
- prove an open statement;
- find prior work we missed;
- formalize a stable result in Lean;
- design an experiment that can directly kill a physical claim;
- or prove that continuous structure cannot be recovered from the discrete substrate we chose.

If this route is wrong, we want to discover exactly where it breaks as early as possible.  
If it is right, we intend to push it until it is strong enough to replace the old foundation.

See [CONTRIBUTING.md](CONTRIBUTING.md).

## Bilingual rule and license

All canonical prose is maintained as pure-English / pure-Chinese semantic pairs, with neither language secondary. Canonical prose changes must update both versions in the same change set.

Code and repository documentation are released under the MIT License. The root `LICENSE` file is the sole legal license text.

## Status

Enterprise Math remains in **Research Beta**. A complete geometry, calculus, physics, and thermodynamics are still far from finished, and many research lines remain open.

That no longer means we lack a judgment about the direction.

**We remain skeptical about details, ruthless about evidence, and unwilling to retreat on the foundational direction.**

Continuous mathematics has already proved itself to be a magnificent tool. Enterprise Math now asks a larger question:

> **If nature was never continuous to begin with, where should mathematics begin again?**
