# N-Coupled Public-N Realized-Effect Trace Noncompilability — Research Return

Researcher-ID: `EM-NCASEFF1-84C2D6`  
Task: `RS-N-COUPLED-PUBLIC-N-REALIZED-EFFECT-TRACE-NONCOMPILABILITY`  
Publication: `TP2-6E2A94C1B7D3058F2A41`  
Claim: `CLM-9C6A4E2F18D7B3510C42`  
Execution branch: `research/n-coupled-realized-effect-noncompilability-em-ncaseff1-84c2d6`

## 1. Terminal verdict

`NEGATIVE_BOUNDARY / ACTUAL_BRANCH_TRACE_NONCOMPILABILITY_DOES_NOT_BLOCK_DISTRIBUTIONAL_SEED_EXTERNALIZATION`.

Hard-target disposition:

`PUBLIC_N_ONLY_REALIZED_EFFECT_TRACE_NONCOMPILABILITY_EXACTLY_OBSTRUCTED_FOR_G_EFFECT_SEED_BY_PUBLIC_SEED_EXTERNALIZATION_TO_EXPLICIT_RANDOM_PRESENTATION_SEARCH`.

This return freezes one exact effectful capability class `G_effect-seed`. It is strictly beyond the accepted
`G_trace-lin` deterministic presentation-transparent boundary: a load-bearing runtime effect samples a realized
branch that is **not** included in the pre-readout public transcript, so the exact realized presentation and even
its CRT support need not be a deterministic function of that transcript.

Nevertheless, if the effect's seed law is public and exactly sampleable and each realized branch is produced by a
public deterministic presentation compiler, the hidden realization can be externalized. Sampling the same seed
law outside the runtime and applying the same public branch compiler produces exactly the same joint distribution
of explicit presentations. Therefore hiding the realized seed creates branch opacity but no new distributional
capability.

Freeze the new separation:

`ACTUAL_BRANCH_NONCOMPILABILITY != DISTRIBUTIONAL_NONCOMPILABILITY`.

For the exact witness `G_effect-randrel`, the distinction is nonvacuous. A hidden uniform `A in R_N` creates
`H_A = coker([A])`. Under the same public transcript the hidden support can be empty, `p`-only, `q`-only, or both.
But the public effect specification already gives an exact external sampler `A <- Uniform(R_N)`, so the mechanism
is literally explicit randomized scalar-presentation sampling followed by `gcd(N,A)`. It is therefore rejected by
the task's randomized nonunit firewall.

This is **not** a universal impossibility theorem for arbitrary effects. The unresolved frontier is now narrower:
a positive survivor must defeat not only extensional reflection and deterministic transcript compilation, but also
effective distributional externalization to explicit presentations.

No factoring lower bound, complexity lower bound, novelty, Working Truth, Foundation, L4, or canonical promotion
is asserted.

## 2. Frozen effect class `G_effect-seed`

Let `R_N = Z/NZ`, with the proof audit taking `N=pq` for distinct hidden primes `p,q`. The public computation
receives `N` only. The factors are proof variables and are never runtime inputs.

A `G_effect-seed` program may use the accepted deterministic presentation-transparent finite-module constructors
together with a consuming effect

`REALIZE_EFFECT(spec,H_1,...,H_k) -> H'`.

The public specification `spec` must give:

1. a finite seed space `S`;
2. an exact public seed law, represented for example by positive integer weights `w_s` or an equivalent exact
   sampler;
3. a public deterministic branch compiler
   `Phi(N,s,C_1,...,C_k)=C'`,
   where `C_i` are explicit presentations of the input modules and `C'` is an explicit presentation of the
   realized output module;
4. the input/output types and consuming-resource law.

At runtime the primitive consumes its handles, samples `s` from the public law, evaluates `Phi`, creates a
nonreflective handle for `coker(C')`, and withholds both `s` and `C'` from the pre-readout transcript.

The effect implementation is not secret. Hidden factors, CRT selectors, factor-correlated secret inputs, and a
primitive specified to return a factor/nonunit are forbidden.

Before terminal materialization the runtime handle interface excludes copy/replay, equality, element enumeration,
membership, quotient equality, chosen-element evaluation, basis probing, cardinality query, presentation query,
and realized-seed query.

Machine-readable frozen contract:

`research_artifacts/N_COUPLED_PUBLIC_N_REALIZED_EFFECT_TRACE_NONCOMPILABILITY/effect_seed_externalization_contract.json`.

## 3. Theorem A — exact seed externalization

### Statement

For every finite `G_effect-seed` program `P`, there is a public external simulator `Ext(P,N)` that produces exactly
the same joint probability law on realized explicit presentations as the hidden runtime execution of `P`.

Consequently, for every deterministic terminal readout `R(N,C_final)` applied after materialization, the output
law of

`hidden G_effect-seed execution -> MATERIALIZE -> R`

is exactly the output law of

`Ext(P,N) -> explicit C_final -> R`.

### Proof

Order the finite constructor/effect events topologically along the execution trace.

For deterministic presentation-transparent constructors, use the already accepted public presentation compiler:
given explicit input presentations, compute the exact output presentation.

For an effect event with public seed law `mu` and branch compiler `Phi`, the external simulator samples a seed
`s ~ mu` using the public exact sampler and computes

`C' = Phi(N,s,C_1,...,C_k)`.

Inductively, immediately before each event, the external simulator's explicit input-presentation tuple has the
same joint law as the tuple denoted by the hidden runtime handles. Conditional on that tuple, both executions use
the same seed law and the same deterministic branch map `Phi`. Their conditional output-presentation laws are
therefore identical. The law of total probability preserves equality after marginalizing the prior tuple.

Induction over the finite trace gives equality of the complete joint presentation law. Applying the same
deterministic terminal readout to identically distributed final presentations preserves equality of readout laws.
QED.

### Exact finite-weight form

If one effect has finite seed set `S`, integer weights `w_s>0`, total `W=sum_s w_s`, and output map
`Phi:S -> Presentations`, then for every explicit presentation `C`,

`Pr[C_out=C] = (1/W) * sum_{s:Phi(s)=C} w_s`.

The external simulator computes the same pushforward measure. Hiding which `s` was chosen changes the observer's
knowledge of the **actual run**, not the public probability law.

## 4. Why Theorem A is stronger than deterministic trace compilation

The accepted `G_trace-lin` theorem says the public constructor transcript itself determines one exact presentation
before readout. `G_effect-seed` deliberately destroys that property.

For a genuinely branching effect, no deterministic compiler of the public transcript alone can output the exact
presentation of every realized run because two runs have the same transcript and different hidden seeds.

Theorem A does **not** restore deterministic knowledge of the actual branch. Instead it gives an exact public
sampler for the branch law.

Thus the two notions must stay separate:

- `ACTUAL_BRANCH_COMPILABLE`: recover the exact presentation/support of this realized run;
- `DISTRIBUTION_EXTERNALLY_SAMPLEABLE`: reproduce the exact public law of realized presentations.

`G_effect-seed` may fail the first and still satisfy the second.

The taskbook explicitly requires this distinction whenever randomness or nondeterminism is used. A positive
mechanism cannot rely on branch opacity alone when the public semantics can be pushed forward to an explicit
sampleable presentation family.

## 5. Exact witness `G_effect-randrel`

Freeze the smallest nontrivial witness.

Start with

`H_0 = NEW_FREE(1) ~= R_N`.

The load-bearing effect

`REALIZE_RANDOM_RELATION(uniform_R_N,H_0)`

samples a hidden

`A <- Uniform({0,1,...,N-1})`

and consumes `H_0` to produce

`H_A = coker([A]: R_N -> R_N) ~= R_N/(A)`.

The pre-readout transcript exposes the operation and the uniform law, but not the realized `A`, the presentation
`[A]`, or any handle reflection.

Terminal `MATERIALIZE(H_A)` returns `[A]`; the declared readout is `gcd(N,A)`.

This is not an oracle contract: materialization returns a presentation. Its failure is instead the exact
randomized-presentation equivalence proved below.

## 6. Theorem B — hidden branch support is genuinely non-deterministic

For each hidden prime `ell in {p,q}`,

`H_A tensor_R F_ell ~= coker([A mod ell]: F_ell -> F_ell)`.

A one-dimensional scalar map over a field has nonzero cokernel exactly when its scalar is zero. Therefore

`H_A has nonzero ell-component <=> ell | A`.

Hence

`gcd(N,A)`

is exactly the product of the supported hidden primes.

Under one and the same pre-readout public transcript, the possible hidden branches include:

- `A=1`: no hidden component survives;
- `A=p`: only the `p` component survives;
- `A=q`: only the `q` component survives;
- `A=0`: both survive.

Here `p,q` are used only as existential proof witnesses among the publicly defined residue set; the algorithm is
not given them.

Therefore neither the exact realized presentation nor the hidden support is a deterministic function of the
pre-readout public transcript.

This proves that `G_effect-randrel` genuinely crosses the deterministic `G_trace-lin` compilation boundary.

## 7. Theorem C — exact reduction of the witness to random nonunit search

The public effect law is uniform on `R_N`. An external simulator can therefore sample

`A <- Uniform(R_N)`

and output the explicit presentation `[A]`.

This is exactly the pushforward law of the hidden effect, branch for branch. The terminal readout is then simply

`gcd(N,A)`.

For `N=pq`, the exact residue counts are:

- `gcd(N,A)=1`: `(p-1)(q-1)` residues;
- `gcd(N,A)=p`: `q-1` residues;
- `gcd(N,A)=q`: `p-1` residues;
- `gcd(N,A)=N`: `1` residue (`A=0`).

Thus the proper-factor success count is

`p+q-2`

and the exact one-trial success probability is

`(p+q-2)/(pq)`.

So the hidden effect is not merely analogous to random nonunit hunting. It is **distributionally identical** to
one explicit uniform scalar-presentation sample followed by a gcd.

The taskbook's kill rule therefore applies exactly.

## 8. General corollary — randomized presentation search normal form

Within `G_effect-seed`, suppose terminal success is characterized by a support-bearing scalar of the materialized
presentation, e.g.

`1 < gcd(N,Delta_r(C_final)) < N`.

By Theorem A, the final presentation `C_final` can be sampled externally with exactly the same law. Therefore the
entire hidden-effect mechanism has the normal form:

1. publicly sample the effect seeds;
2. publicly compile the corresponding explicit presentation;
3. evaluate the same determinantal/nonunit readout.

So the effect cannot qualify as a new delayed-support capability merely because the realized branch is hidden
during the original runtime execution.

This corollary is restricted to the frozen seed-compilable effect class. It says nothing about a public effect
whose realized semantics cannot be effectively reduced to such an exact seed/presentation pushforward.

## 9. Adversarial mechanism audit

The witness and theorem were tested against the inherited firewall.

- Hidden `p/q`, CRT selector, factor-correlated secret seed: **not used**.
- Secret implementation: **not used**; seed law and branch compiler are public.
- Pollard/Williams/ECM order or smoothness: **not used**.
- Collision/cycle/history equality: **not used**.
- Congruence-of-squares / relation factoring: **not used**.
- Named-prime p-adic/Hensel place: **not used**.
- Direct randomized nonunit/presentation search: **triggered exactly**.

The last line is terminal for this candidate. The negative classification does not depend on analogy to prior art:
Theorem A constructs the exact external simulator, and Theorem C identifies the witness readout with the same
proper-gcd event.

## 10. Tool reuse resolution

The current Enterprise toolbox contains `T8_RELATION_OBSERVABLE_SPECTRUM`, whose scope includes multivalued
relations, support, branching, and observable nondeterminism.

Resolution:

`T8_RELATION_OBSERVABLE_SPECTRUM -> REUSE_APPLIED`.

The effect is treated as a weighted public relation/correspondence from public pre-state/specification to explicit
presentation branches. The T8 boundary that raw relation branching, observed nondeterminism, and quotient safety
must not be conflated is preserved here: hidden branch choice is real, but that fact alone does not make the
public branch law unavailable.

No new general-purpose tool family is created. The pushforward/externalization theorem is retained as a
task-specific Result.

## 11. Exact checker and finite certificate

Checker:

`research_checks/N_COUPLED_PUBLIC_N_REALIZED_EFFECT_TRACE_NONCOMPILABILITY_CHECK_20260903.py`.

Executed exact regression:

`PASS G_EFFECT_SEED_EXTERNALIZATION {"calculus": "G_effect-seed", "one_sided_cases": 483, "proper_factor_count_formula": "p+q-2", "proper_factor_probability_formula": "(p+q-2)/(pq)", "pushforward_mismatches": 0, "scalar_cases": 2451, "semiprimes": 28, "status": "PASS", "support_mismatches": 0, "uniform_pushforward_checks": 28, "weighted_pushforward_checks": 140}`

The checker exhausts every residue for all `28` unordered semiprimes formed from
`2,3,5,7,11,13,17,19`, covering `2451` scalar branches and `483` one-sided branches. It verifies the support/gcd
classification with zero mismatches and checks exact equality between hidden-effect and external pushforward laws
for all `28` uniform cases plus `140` weighted-seed regressions.

These finite checks guard the formulas and implementation certificate only. Theorem A is the symbolic induction
above; it is not inferred from the finite enumeration.

Machine-readable certificate:

`research_artifacts/N_COUPLED_PUBLIC_N_REALIZED_EFFECT_TRACE_NONCOMPILABILITY/effect_seed_externalization_certificate.json`.

## 12. What is closed and what remains open

For this N-coupled line, this Result closes the following candidate class:

`EXTENSIONAL_NONREFLECTION + ACTUAL_BRANCH_NONCOMPILABILITY + PUBLIC_EXACT_SEED/PRESENTATION_PUSHFORWARD`.

More compactly:

`HIDDEN_REALIZATION + PUBLICLY_EXTERNALIZABLE_SEMANTICS != NEW_SUPPORT_CAPABILITY`.

It does **not** close arbitrary effectful computation.

The minimum unresolved semantic residue is now:

> Can a fully specified public-`N`, non-oracular realized effect have a support-bearing output whose actual branch
> is hidden **and** whose public semantics cannot be effectively externalized to an enumerable/sampleable family
> or distribution of explicit presentations, while still avoiding order/smoothness, collision/cycle,
> square-relation, named-prime p-adic, and direct nonunit mechanisms?

Any successor should target that exact distributional boundary rather than republish generic runtime opacity,
linear resource typing, or ordinary hidden randomness.

## 13. Authority and return boundary

Freeze only the task-local result:

`G_effect-seed -> exact seed externalization -> explicit randomized presentation-search normal form`.

Do not infer:

- impossibility for all public effects;
- impossibility of factoring;
- a factoring or complexity lower bound;
- novelty or priority;
- Working Truth;
- Foundation or L4 status;
- canonical promotion.

Recommended next control action:

`DRIVER_REVIEW` of this frozen negative boundary. If accepted and the parent objective remains open, a successor
should require **distributional nonexternalizability**, not merely an unknown realized branch.
