# R028 — Retrospective Distinction Credit, Precision-Debt Attribution, and Rewind Calculus

Researcher-ID: `EM-R028-4D91AF`  
Task: `RS-R028-BRC-RETROSPECTIVE-DISTINCTION-CREDIT-CALCULUS`  
Taskbook source: `2a5e25835022beadac590cc0a10ca006f4473c8c`  
R022 consumed: Draft PR #497 owner head `195b2be6ac184c8073ef6eb1b425a373acebd585`  
R020 consumed: Draft PR #501 head `86d22d75d4cb1aaa5d783d4ceeabcd57ff65c39d`  
Canonical BRC semantics consumed: `EnterpriseMath/Relation/BranchRecoalescence.lean` at `main@3bbddc4661647537834953cfd64264fc965be292`  
CI: `CI_NOT_REQUIRED_FOR_RESEARCH`  
Status: `RESEARCH / NOT_CANONICAL`

## Executive verdict

The strong scalar theory does **not** survive. The stable object is a **future-relative typed credit profile**, while any ordered scalar marginal is path/order dependent.

Primary return:

`RETROSPECTIVE_DISTINCTION_CREDIT_CALCULUS_FOUND / FUTURE_RELATIVE_CREDIT_PROFILE_FROZEN / HINDSIGHT_BOUNDARY_CLASSIFIED / RECOALESCENCE_CREDIT_BRIDGE_CHECKED / NOT_CANONICAL`

Sharper negative return, simultaneously true:

`RETROSPECTIVE_CREDIT_ORDER_DEPENDENT / TELESCOPING_CORE_SURVIVES / SUBMODULARITY_AND_INTRINSIC_SCALAR_KILLED / NOT_CANONICAL`

Prior-art boundary:

`RETROSPECTIVE_CREDIT_PRIOR_ART_ROOTED / PROJECT_SPECIFIC_BRC_INTERFACE_RETAINED / NO_NEW_FOUNDATION_PRIMITIVE / NOT_CANONICAL`

The recommended stable profile for a feature/probe/checkpoint distinction is not one number but at least

`(new pair coverage, local multiplicity reduction vector, ΔM, ΔB, Δrewind, acquisition cost, storage cost, recomputation cost)`.

No scalarization is canonical without an explicitly declared objective/weighting or attribution convention.

The strongest positive conceptual bridge is exact and narrow:

> On the **support carrier** `P(X)`, let `F_U^supp = ker(A ↦ supportSignature_U(A))`. Then a support distinction has zero remaining-future credit exactly when the two supports lie in the same `F_U^supp` class; by canonical R023 `FORGETFUL_RECOALESCENCE_IFF`, this is exactly suffix-safe forgetful replacement. The analogous statement at point carrier applies only to singleton supports and must not be lifted to arbitrary supports.

No R022 theorem break was found. No R023 semantic repair is requested.

---

## 1. Exact universe and conventions

For finite `X`, current encoding and target are used only through partitions/equivalence kernels:

- `E = ker(e)`;
- `F = ker(sigma)`;
- `E' subseteq E` means `E'` is finer/more informative.

For a feature `phi`,

`E[phi] = E intersection ker(phi)`.

For a feature set `S`,

`E[S] = E intersection (intersection_{phi in S} ker(phi))`.

For each current class `C in X/E`, define

`m_C(E=>F) = # { D in X/F : C intersection D != empty }`.

Then

`M(E=>F) = max_C m_C(E=>F)`

and

`B(E=>F) = ceil(log2 M(E=>F))`.

The required distinction universe is

`P(E,F) = {{x,y} : x E y and not x F y}`.

A feature covers exactly

`Cover_phi(E,F) = {{x,y} in P(E,F) : phi(x) != phi(y)}`.

The entire report is deterministic/worst-case unless a measure is explicitly introduced. No probability distribution is inferred from finite cardinalities.

---

## 2. Positive core: debt and exact completion

### Theorem 2.1 — `M >= 1`

Every nonempty current class intersects at least one target class, hence every local multiplicity is at least one. The empty-carrier convention used by the executable also returns one, so `M>=1` uniformly.

### Theorem 2.2 — zero-debt boundary

`M(E=>F)=1` iff `E subseteq F`.

Proof: if every current class intersects exactly one target class, any two points equivalent under `E` lie in that same `F` class. Conversely, if `E subseteq F`, every `E` class is contained in a single `F` class.

Therefore

`B(E=>F)=0` iff `E subseteq F`.

This is the arbitrary `(E,F)` version needed for checkpoint sufficiency; it is stronger than the refinement-special wording `E=F` used in an earlier R022 pass.

### Theorem 2.3 — current-refinement monotonicity

If `E' subseteq E`, then

`M(E'=>F) <= M(E=>F)`

and consequently

`B(E'=>F) <= B(E=>F)`.

Every `E'` class lies inside an `E` class, so the set of target classes it can intersect is a subset of the old compatible target-class set.

### Theorem 2.4 — feature-cover equivalence

For any feature family `S`,

`E[S] subseteq F`

iff

`union_{phi in S} Cover_phi(E,F) = P(E,F)`.

An uncovered required pair is exactly a pair merged by current encoding and every selected feature but separated by the target. Thus Test-Cover/Set-Cover is the exact finite incidence formulation of feature/future-basis completion.

### Theorem 2.5 — nonnegative debt marginal

For `D in {M,B}`,

`C_D(phi|S)=D(E[S],F)-D(E[S union {phi}],F) >= 0`.

This is immediate from Theorem 2.3 because feature addition refines the current encoding.

### Theorem 2.6 — ordered telescoping

For an ordered sequence `phi_1,...,phi_k`,

`sum_i C_D(phi_i | {phi_1,...,phi_{i-1}}) = D(E,F)-D(E[{phi_1,...,phi_k}],F)`.

This is an algebraic telescoping identity, not an attribution uniqueness theorem. If the final feature family exactly completes `F`, the total ordered credit is the initial debt, but the allocation of that total across features can change with order.

---

## 3. Exhaustive finite laboratory

Artifact: `experiments/r028_retrospective_credit_calculus.py`.

No floating point, random sampling, or OCR is used. Partitions are canonical restricted-growth strings and all core operations are exact integer/set-partition operations.

The required partition core exhausts all partitions through `|X|=5`:

- Bell counts: `1, 2, 5, 15, 52`;
- ordered `(E,F)` pairs: `2,959`;
- current-refinement monotonicity checks: `19,583`;
- target-coarsening/debt-release checks: `19,583`;
- required-pair release checks: `19,583`;
- fixed-feature pair-credit shrink checks: `981,845`;
- single-feature debt/coverage checks: `144,117`;
- all ordered three-feature libraries through `|X|<=4`: `762,533`;
- pair-coverage diminishing-return checks through `|X|<=4`: `51,267`;
- nested-kernel conditional-regime checks through `|X|<=4`: `48,234`;
- failures in the positive core: `0`.

Support/BRC finite sanity model:

- all binary relation generators through `|X|<=3`;
- all deterministic one-generator relations at `|X|=4`;
- all observation partitions;
- all exact supports;
- finite future language consisting of powers `[0,1,2]`;
- relation generators: `786`;
- support-signature evaluations: `82,052`;
- implied support-pair signature equivalences checked/packaged: `1,147,400`;
- failures: `0`.

Focused tests: `21/21 PASS`.

`py_compile`: PASS.

This bounded evidence is not promoted to an unbounded minimality theorem unless a separate mathematical argument establishes minimality. The n=2 impossibilities and n=3/n=4 positive minimal witnesses below are, however, easy to inspect directly in the declared partition-kernel model.

---

## 4. H7 killed: marginal debt credit is order dependent

Minimal witness with **distinct feature kernels**:

- `X={0,1,2}`;
- `E={012}`;
- `F={01,2}`;
- `A={01,2}`;
- `B={0,1,2}`.

For both `M` and `B`:

- marginal of `A` at empty set = `1`;
- marginal of `A` after `B` = `0`.

Thus identical feature `A` receives different marginal credit depending on acquisition order.

`|X|=2` has only two partition kernels, and with distinct kernels there is no third nontrivial interaction configuration, so n=3 is minimal in the declared distinct-partition-feature model. If two semantically identical features are allowed as distinct library objects, the familiar two-state duplicate-feature redundancy gives an even more trivial order-dependence example; R028 freezes the cleaner distinct-kernel n=3 witness.

Consequence: there is no order-independent intrinsic marginal `M` or `B` credit in the general calculus.

---

## 5. H8 killed: debt reduction is not generally submodular

Let

- `X={0,1,2}`;
- `E={012}`;
- binary target `F={01,2}`;
- `A={02,1}`;
- `B={0,12}`.

For both `M` and `B`:

- `B` marginal at empty set = `0`;
- `B` marginal after `A` = `1`.

Each feature alone leaves one mixed cell containing both target classes, so worst-case debt remains unchanged. Together the two feature kernels refine to identity, removing the debt. This is strict complementarity/synergy and violates diminishing returns.

This one witness already kills two tempting rescue hypotheses:

- **binary target does not suffice**;
- **single current fibre does not suffice**.

A clean product witness also fails:

- `X={0,1}x{0,1}` represented by `0,1,2,3`;
- target `F={01,23}` is first coordinate;
- feature `A={03,12}` is parity;
- feature `B={02,13}` is second coordinate.

Again each feature alone has zero `M/B` marginal, while the pair pays one unit. Hence product-shaped state spaces/partitions do not rescue general submodularity.

### Positive conditional regime — nested feature kernels

If all candidate feature kernels form a chain under refinement, then the meet of any selected set is just the finest selected kernel. Therefore the total gain is

`G_D(S)=max_{phi in S} G_D({phi})`

for nonnegative singleton gains. A max-on-chain set function is monotone submodular.

So the useful formal boundary is not “debt gain is submodular”, but:

> **Nested/chain feature kernels imply submodular debt gain.**

The bounded exhaustive checker found zero failures through `|X|<=4`; the argument above is unbounded.

---

## 6. H9 killed: debt reduction is not generally supermodular

Use the redundancy witness:

- `X={0,1,2}`;
- `E={012}`;
- `F={01,2}`;
- `A={01,2}`;
- `B={0,1,2}`.

For both `M` and `B`:

- `B` marginal at empty set = `1`;
- `B` marginal after `A` = `0`.

Both features can pay the same debt, so the second becomes redundant. This violates increasing returns.

Therefore general `G_M` and `G_B` are **neither submodular nor supermodular**.

---

## 7. Pair coverage has a different, classical positive structure

Define

`G_pair(S)=| union_{phi in S} Cover_phi(E,F) |`.

This is a standard coverage function:

- monotone;
- submodular;
- ordered marginals nonnegative;
- exact completion occurs exactly when `G_pair(S)=|P(E,F)|`.

But pair coverage is not precision-debt reduction.

### Minimal positive-coverage / zero-debt witness

- `X={0,1,2}`;
- `E={012}`;
- `F={01,2}`;
- `phi={02,1}`.

The feature separates one required pair, yet

- `M: 2 -> 2`;
- `B: 1 -> 1`.

Thus pair credit is positive while both debt credits are zero.

### Equal pair count, different debt effect

A stronger witness appears first at n=5 in the exhaustive declared class:

- `E={01234}`;
- `F={012,3,4}`;
- `A={0123,4}`;
- `B={01,234}`.

Both features newly cover four required pairs, but

- `A`: `ΔM=1`, `ΔB=1`;
- `B`: `ΔM=0`, `ΔB=0`.

The reason is structural. Pair coverage counts separated edges in the required-pair graph. `M` instead asks for the largest number of target classes still cohabiting a single current/refined cell. `B` then applies a ceiling to `log2 M`, adding plateaus. These are different functionals and should remain different credit coordinates.

---

## 8. Local versus global worst-case credit

Because `M` is a maximum over current fibres, a useful feature in a non-bottleneck fibre can have global credit zero.

Minimal witness found:

- `X={0,1,2,3}`;
- `E={01,23}`;
- `F={02,13}`;
- `phi={012,3}`.

Local target multiplicities change

`[2,2] -> [2,1]`,

so one local fibre gains one unit, but global `M` stays `2` because the other fibre remains the bottleneck.

This suggests storing the **local multiplicity-reduction vector** as a profile coordinate when bottleneck migration matters, rather than reporting only scalar `ΔM`.

Any expected/weighted aggregate requires an explicit measure `mu`; no expected-information theorem follows from worst-case `M`.

---

## 9. Declared-language credit versus realized-suffix credit

Let

`F_U = intersection_{u in U} ker(o∘u)`.

For one realized suffix `u* in U`,

`F_real = ker(o∘u*)`.

Because the declared kernel intersects at least as many constraints,

`F_U subseteq F_real`.

Thus for fixed current encoding `E`, target coarsening gives

`M(E=>F_real) <= M(E=>F_U)`

and

`B(E=>F_real) <= B(E=>F_U)`.

### Minimal strict hindsight witness

On two states:

- `E={01}`;
- declared target `F_declared={0,1}`;
- realized target `F_realized={01}`.

Then

- declared debt: `M=2`, `B=1`;
- realized debt: `M=1`, `B=0`.

A feature separating the two states has declared pair credit one but realized pair credit zero.

Therefore the inference

`REALIZED_SUFFIX_CREDIT = 0  =>  ex-ante safe deletion`

is false. The feature was irrelevant to the realized replay but necessary for another declared alternative future.

R028 freezes two different terms:

- `DECLARED_LANGUAGE_CREDIT`: online reusable-carrier relevance relative to all still-declared futures;
- `REALIZED_SUFFIX_CREDIT`: replay/hindsight relevance after the suffix is fixed.

Only the first can justify deletion in a runtime that must remain safe for the declared language.

---

## 10. Future-language shrink and exact credit release

For remaining languages

`U_0 superset U_1 superset ...`,

let

`F_t=K(U_t)`.

Then

`F_t subseteq F_{t+1}`:

the target partition can only coarsen as possible futures disappear.

For fixed `E`:

- `M(E=>F_t)` is nonincreasing;
- `B(E=>F_t)` is nonincreasing;
- `P(E,F_{t+1}) subseteq P(E,F_t)`.

Define exact released pairs

`Released_t=P(E,F_t) minus P(E,F_{t+1})`.

These are the distinctions that have lost **declared remaining-future necessity** at that transition.

A useful new positive law is stronger for pair coverage than for debt marginal:

> for a fixed feature, its unweighted pair-coverage credit cannot increase when the target coarsens, because the required-pair universe only shrinks.

The exhaustive checker performed `981,845` fixed-feature pair-credit shrink checks through n=5 with zero failures; the set-inclusion proof is immediate.

### H14 killed — individual debt marginal can increase after language shrink

Total debt goes down, but an individual feature's **marginal** `M/B` credit need not.

M witness:

- `E={01,23}`;
- `F_before={02,1,3}`;
- `F_after={012,3}` (coarser);
- `phi={012,3}`;
- marginal `ΔM: 0 -> 1`.

B witness:

- `E={0123}`;
- `F_before={0,1,2,3}`;
- `F_after={012,3}`;
- `phi={012,3}`;
- marginal `ΔB: 0 -> 1`.

Mechanisms:

1. the worst-fibre bottleneck can switch/disappear;
2. `ceil(log2 M)` can release a plateau.

So “future language shrinks” releases **total required precision and required pairs**, but does not define a monotone per-feature `M/B` attribution.

---

## 11. Exact BRC recoalescence bridge

This is the central project-specific interface.

Canonical R023 defines on exact supports `A,H subseteq X`:

`supportSignature_U(A)`

and proves

`SuffixSafe_U(A,H) iff supportSignature_U(A)=supportSignature_U(H)`.

R028 packages this as a target partition on the matching carrier `P(X)`:

`F_U^supp = ker(A ↦ supportSignature_U(A))`.

Then, exactly:

`A F_U^supp H`

iff

`supportSignature_U(A)=supportSignature_U(H)`

iff

`SuffixSafe_U(A,H)`.

Thus the statement

> “the distinction between support tokens A and H has zero remaining-future credit”

is **exactly** safe forgetful BRC recoalescence when credit is defined at the support-signature carrier.

### Point/support boundary

Point signatures give the corresponding singleton result. If `pointSignature_U(x)=pointSignature_U(y)`, then `{x}` and `{y}` are suffix-equivalent.

But zero point distinction does not authorize arbitrary support replacement.

Concrete boundary:

- `X={0,1,2}`;
- identity transition;
- observation partition `{01,2}`;
- points `0` and `1` have equal point signatures;
- supports `A={0,2}` and `H={1}` do not have equal support signatures.

Therefore

`zero point-pair credit`

must never be silently lifted to

`zero arbitrary branch/support credit`.

This is exactly why R028 leaves R023 theorem statements unchanged.

---

## 12. No resurrection and how new debt can be paid

Suppose an unexpected language extension changes the target to a finer `F_new`. If the current encoding `E` merges a pair separated by `F_new`, then `M(E=>F_new)>1`.

Any later branch key computed solely as a deterministic function of the current `E` token still factors through `E`. Canonical `NO_RESURRECTION` therefore prevents it from recreating the lost distinction.

R028 freezes four payment classes:

- `DEBT_PAYABLE_BY_METADATA`: some retained/acquired `Z` makes `E intersection ker(Z) subseteq F_new`;
- `DEBT_PAYABLE_BY_REWIND`: an earlier checkpoint (possibly with its metadata) refines `F_new`;
- `DEBT_PAYABLE_BY_EXTERNAL_REREAD`: an external fine source/replay reacquires the state-dependent distinction;
- `DEBT_UNRECOVERABLE_FROM_CURRENT_ENCODING`: none of the above is available.

Branching alone from an insufficient current token belongs to the last class. Branch count/tokens are not information ex nihilo.

This is an information interpretation of R023 `NO_RESURRECTION`, not a modification of its semantics.

---

## 13. Checkpoint rewind calculus and cost Pareto

Let progressively forgetful checkpoints satisfy

`E_0 subseteq E_1 subseteq ... subseteq E_T`.

For target `F`, define

`recoverable(t,F) : E_t subseteq F`.

With side metadata `Z_t`:

`recoverable_Z(t,F) : E_t intersection ker(Z_t) subseteq F`.

The latest exact checkpoint is

`t*(F)=max {t : recoverable(t,F)}`,

and current rewind depth is

`R(F)=T-t*(F)`.

Adding metadata only enlarges the recoverable-index set, so its rewind credit

`C_R=R_before-R_after`

is nonnegative. Like debt credit, however, attribution among multiple metadata items can be redundant/order dependent.

### Exact R022 8-state replay

Checkpoints:

- `E0`: eight singletons;
- `E1`: four pairs;
- `E2`: two quartets;
- `E3`: one 8-state block (current).

Target `F=E1`.

`E0` is dominated by `E1`. The nondominated frontier is exactly:

- `(0 side bits, rewind 2)` from `E1`;
- `(1 side bit, rewind 1)` from `E2`;
- `(2 side bits, rewind 0)` from `E3`.

If recomputation work is proportional to rewind in this fixture, the triples are `(0,2,2)`, `(1,1,1)`, `(2,0,0)`.

### Debt and rewind are not the same order

Witness A: same current `B`, different rewind.

- n=4 checkpoints `identity -> {01,2,3} -> universal`;
- target `F1={01,23}` and `F2={02,13}`;
- both current `B=1`;
- rewind depths are `1` and `2`.

Witness B: same rewind, different current `B`.

- n=3 checkpoints `identity -> universal`;
- `F1={01,2}`, `F2=identity`;
- both rewind one step;
- current `B` values are `1` and `2`.

Therefore side-bit debt and temporal rewind are independent resource axes. Checkpoint bytes, feature storage, probe/read cost and recomputation work must also be charged separately.

---

## 14. Shapley comparator: symmetric, classical, not “true credit”

For a finite feature set and chosen debt game

`v(S)=D(E,F)-D(E[S],F)`,

classical Shapley value is well-defined even when `v` is neither submodular nor supermodular. It averages ordered marginal contributions over all permutations.

R028 computes it exactly with rational arithmetic for small libraries.

Two opposite two-feature examples expose the semantic limitation:

### Pure synergy

- each feature alone has debt gain `0`;
- together gain `1`;
- ordered credits can be `[0,1]` or `[1,0]`;
- Shapley = `[1/2,1/2]`.

### Pure redundancy

- each feature alone has gain `1`;
- together still gain `1`;
- ordered credits can be `[1,0]` or `[0,1]`;
- Shapley = `[1/2,1/2]`.

The same symmetric output can arise from opposite interaction structures. Shapley removes ordering arbitrariness only after the game `v` and player library have been declared; it does not prove a unique intrinsic semantic credit, and it is not causal responsibility.

Exact computation is factorial/exponential in the feature count by direct subset/permutation formulas; approximation would need separate error accounting and is not theorem evidence here.

Classification: `PRIOR_ART_COMPARATOR_ONLY`.

---

## 15. Necessity / sufficiency types are more stable than one scalar

Relative to a declared target, feature library, and cost model, use typed classifications:

- `ESSENTIAL`: every minimum exact basis contains the feature;
- `OPTIONAL_USEFUL`: some exact basis contains it, but it is not in every minimum basis;
- `REDUNDANT_RELATIVE_TO_LIBRARY`: removing it does not change achievable target completion;
- `DOMINATED`: its relevant distinctions are covered by a no-more-expensive alternative;
- `SYNERGISTIC`: alone it may have zero `M/B` marginal but has positive joint marginal in context;
- `ZERO_FUTURE_CREDIT`: it covers no required pair for the current declared future target.

These are set-cover/backbone/dominance notions specialized to the BRC future-relative interface. Their status can change when the target language or feature library changes; they are not timeless feature properties.

---

## 16. Stable dynamic credit profile

Recommended object at time `t`:

`Credit_t(phi) = (`

`  new_pair_coverage,`

`  local_multiplicity_reduction_vector,`

`  alphabet_debt_reduction,`

`  bit_debt_reduction,`

`  rewind_reduction,`

`  acquisition_cost,`

`  storage_cost,`

`  recompute_cost`

`)`.

A feature/profile `phi` Pareto-dominates `psi` only after all compared semantics/targets are held fixed and `phi` is weakly no worse on every declared cost/benefit coordinate with at least one strict improvement.

No user/runtime objective weights => no canonical scalar score.

This is the main surviving “retrospective credit calculus”. It is an exact bookkeeping/profile interface composed from prior-art-rooted primitives, rather than a new universal scalar attribution law.

---

## 17. Runtime implications for BRC

The surviving calculus gives useful policies, but they must be classified as runtime tools rather than Foundation primitives.

### Safe verifier

Use exact target refinement / required-pair cover to verify whether acquired features complete the declared target.

### Probe acquisition

Do **not** greedily select only by immediate `ΔM` or `ΔB`: the n=3 synergy witness gives every first probe zero debt marginal although the pair is jointly sufficient. Pair-coverage/cost, Test-Cover heuristics, decision-tree policies, or lookahead may propose acquisitions; exact completion remains the verifier.

### Language shrink

When required pairs disappear:

- candidate zero-credit metadata can be evicted after matching-carrier safety verification;
- support tokens can recoalesce exactly when remaining support signatures agree.

### Language extension

When debt increases:

1. evaluate candidate side metadata/features;
2. evaluate checkpoint rewind/recompute;
3. evaluate external reread/replay;
4. compare feasible options on a declared cost Pareto frontier;
5. if none restores target refinement, return `DEBT_UNRECOVERABLE_FROM_CURRENT_ENCODING`.

### Semantic target typing

Default R028 target is deterministic/Boolean-support precision. Keep separate:

- `BOOL_SUPPORT_CREDIT`;
- `N_PATH_COUNT_CREDIT`;
- `WITNESS_PROVENANCE_CREDIT`.

R020 already establishes that witness/provenance -> path count -> Boolean support is a one-way information ladder. Credit statements do not invert it.

---

## 18. Prior-art rooting

Machine-readable matrix: `experiments/r028_prior_art_matrix.json`.

Rooted components include:

- equivalence/partition refinement and lattice language;
- sufficient/minimal-sufficient factorization analogues;
- Myhill-Nerode / behavioral equivalence and adjacent bisimulation-signature ideas;
- Set Cover / Test Cover / distinguishing families;
- optimal decision-tree complexity;
- zero-error side-information coding analogues;
- cooperative games / Shapley value;
- feature attribution;
- structural causal attribution;
- reinforcement-learning temporal credit assignment;
- checkpointing, reversible computation and time-space tradeoffs;
- information-refinement/sigma-algebra analogies.

Representative references are recorded in the JSON artifact. R028 makes **no generic novelty claim** for these components.

The project-specific residue is their exact alignment:

`remaining future language -> target kernel -> required distinction pairs -> feature/probe cover -> M/B side debt -> checkpoint sufficiency/rewind -> support-signature recoalescence`.

This exact combination may be project-specific, but the current survey is not a novelty search sufficient to call it new mathematics.

Overall classification:

`PRIOR_ART_ROOTED / PROJECT_SPECIFIC_REPACKAGING / POSSIBLY_NEW_EXACT_COMBINATION_WITHOUT_NOVELTY_CLAIM`.

---

## 19. H1–H18 law matrix

| Law | Status | Result |
|---|---|---|
| H1 | PROVED | `M` current-refinement monotone |
| H2 | PROVED | `B` current-refinement monotone |
| H3 | PROVED | zero debt iff current encoding refines target |
| H4 | PROVED | exact completion iff all required pairs covered |
| H5 | PROVED | marginal `M/B` credit nonnegative |
| H6 | PROVED | ordered marginals telescope |
| H7 | KILLED | individual marginal debt credit order-independent; n=3 distinct-kernel witness |
| H8 | KILLED | general debt gain submodular; n=3 synergy witness |
| H9 | KILLED | general debt gain supermodular; n=3 redundancy witness |
| H10 | PROVED / PRIOR_ART | pair coverage monotone submodular |
| H11 | PROVED | realized target never requires more precision than declared language |
| H12 | KILLED | realized zero credit => ex-ante safe deletion; n=2 witness |
| H13 | PROVED | shrinking future language cannot increase total `M/B` debt |
| H14 | KILLED | each feature's `M/B` credit must decrease under future shrink; n=4 witnesses |
| H15 | PROVED AT MATCHING SUPPORT CARRIER | zero support-signature distinction iff safe forgetful recoalescence |
| H16 | PROVED | metadata/rewind/reread can pay debt; current token branching alone cannot resurrect erased distinction |
| H17 | PROVED CONDITIONAL | nested/chain feature kernels restore submodular `M/B` gain |
| H18 | PROVED | fixed-feature pair marginal cannot increase under target coarsening |

Full executable data: `experiments/r028_credit_law_matrix.json` and `experiments/r028_minimal_counterexamples.json`.

---

## 20. Theorem/tool impact matrix

| Input surface | R028 status | Impact |
|---|---|---|
| R022 precision debt `M/B` | SEMANTICALLY_STABLE | reused unchanged; generalized arbitrary `(E,F)` form confirmed |
| R022 distinction cover | PRIOR_ART_ROOTED / SEMANTICALLY_STABLE | exact completion verifier; pair credit kept separate from debt |
| R022 adaptive acquisition | RUNTIME_TOOL_CANDIDATE | pair/cost or decision-tree heuristics preferred over debt-only greedy |
| R023 `FORGETFUL_RECOALESCENCE_IFF` | SEMANTICALLY_STABLE | exact zero-credit bridge on support carrier |
| R023 `NO_RESURRECTION` | SEMANTICALLY_STABLE | exact unpaid-debt impossibility boundary |
| R020 future-language / carrier typing | SEMANTICALLY_STABLE | Boolean/count/provenance credit targets remain distinct |
| R014 resource accounting | SEMANTICALLY_STABLE | acquisition/storage/recompute/checkpoint costs remain separate axes |
| R024 runtime selector | RUNTIME_TOOL_CANDIDATE | consume typed credit/cost Pareto profile, not intrinsic scalar |
| ordered debt calculus | NEW_DERIVED_CALCULUS | telescoping stable, allocation path dependent |
| Shapley attribution | PRIOR_ART_ROOTED / DO_NOT_PROMOTE | comparator only |
| general sub/supermodularity | COUNTEREXAMPLE_BOUNDARY | both killed |
| nested-kernel submodularity | FORMALIZATION_CANDIDATE | clean conditional positive law |

---

## 21. Answers to the taskbook's nine final questions

### 1. Can retrospective distinction credit be mathematically stable?

Yes as a **target-relative typed profile** and as ordered marginals; no as a unique intrinsic scalar in general. Pair coverage, debt reduction, rewind reduction, and cost are independently meaningful and generally incomparable.

### 2. Are `M/B` marginals naturally order dependent? Minimal counterexample?

Yes. With distinct feature kernels, n=3 is minimal in the exhaustive partition-feature model: `E={012}`, `F={01,2}`, feature `A={01,2}`, feature `B=identity`; A gets 1 before B and 0 after B for both `M` and `B`.

### 3. Is debt reduction submodular or supermodular?

Neither in general. n=3 synergy kills submodularity; n=3 redundancy kills supermodularity. Nested/chain feature kernels are a clean submodular special regime.

### 4. Relation between pair coverage and precision-debt reduction?

Coverage is a monotone submodular edge-cover functional and exactly characterizes completion, but `M` is worst residual target-class multiplicity and `B` is its fixed-width ceiling transform. They are not equal or rank-equivalent.

### 5. Exact declared-vs-realized gap?

`F_declared subseteq F_realized`, hence realized debt is no larger. A feature can have zero realized credit and positive declared credit; n=2 is already strict. Hindsight zero therefore does not justify ex-ante deletion.

### 6. What credit is released as language shrinks?

The target coarsens, total `M/B` debt cannot increase, and required pairs are removed monotonically. Exact released pairs are `P(E,F_t) \ P(E,F_{t+1})`. Fixed-feature pair credit cannot increase, but individual `M/B` marginal can increase because bottlenecks/ceilings change.

### 7. On which carrier does zero credit equal safe recoalescence?

Exactly on the **support-signature carrier**: `F_U^supp = ker(supportSignature_U)`. Then zero support distinction is equivalent to canonical R023 suffix safety. Point-signature zero only justifies singleton substitution, not arbitrary support replacement.

### 8. How do metadata, acquisition and rewind pay debt?

All are ways to restore a complete encoding that refines the new target. Metadata/features refine the current/checkpoint token; rewind selects an earlier sufficient checkpoint; external reread reacquires erased information. Their bits, bytes, reads and recomputation are separate Pareto coordinates. Branching from the insufficient current token alone cannot pay the debt.

### 9. What is actually useful to BRC runtime, and what is repackaged prior art?

Useful project-specific interface: target-relative required-pair release, exact `M/B` side debt, support-level zero-credit recoalescence, no-resurrection payment classification, and checkpoint/metadata/recompute Pareto selection. Set/Test Cover, decision-tree optimization, Shapley attribution, generic checkpointing and causal/RL credit assignment are prior art; R028 does not relabel them as new Foundation primitives.

---

## 22. Downstream routing

### Lean formalization?

**YES, narrowly.** Recommend a new task formalizing only:

1. arbitrary-partition `M` monotonicity and zero iff;
2. feature-cover iff exact completion;
3. ordered telescoping;
4. declared-vs-realized target monotonicity;
5. future-language shrink debt/pair release;
6. support-carrier zero-credit ↔ R023 suffix-safe recoalescence bridge;
7. minimal H7/H8/H9/H12/H14 counterexample fixtures;
8. optional nested-kernel submodularity.

Do not formalize Shapley or runtime heuristics as Foundation surface.

### Return to R022?

`NO`. Precision-debt and distinction-cover core survived independent replay.

### Return to R023?

`NO`. The interpretation must be carrier-typed; canonical theorem is stable.

### Connect to R024/runtime?

`YES, AS TOOL CANDIDATE`. Feed the typed credit/cost Pareto profile, with exact completion/signature checks as verifier. Do not feed a single “true credit” score.

---

## 23. Resource accounting

The executable distinguishes/charges:

- feature alphabet/kernel, not assumed free;
- feature/probe count and acquisition cost;
- side-label alphabet `M`;
- fixed-width bits `B`;
- checkpoint storage bytes (runtime input, not inferred from semantic partition alone);
- rewind steps;
- recomputation work;
- external reread/replay cost;
- branch/support tokens;
- any materialized target/future-signature storage.

Shapley exact comparison uses rational subset/permutation weights and has exponential/factorial combinatorial cost; no approximation result is used as theorem evidence.

---

## 24. Final classification

R028 found a real, stable calculus, but not the originally tempting one-dimensional attribution theory.

The surviving structure is:

`future-relative target semantics`

`+ exact required distinctions`

`+ several non-equivalent marginal resource reductions`

`+ explicit hindsight/declared-language typing`

`+ support-carrier recoalescence equivalence`

`+ metadata/rewind/recompute Pareto accounting`.

Strong intrinsic-scalar, universal-submodularity, universal-supermodularity, pair-credit=debt-credit, hindsight-safe-deletion and per-feature-shrink-monotonicity claims are all false.

Therefore:

`RETROSPECTIVE_DISTINCTION_CREDIT_CALCULUS_FOUND / FUTURE_RELATIVE_CREDIT_PROFILE_FROZEN / HINDSIGHT_BOUNDARY_CLASSIFIED / RECOALESCENCE_CREDIT_BRIDGE_CHECKED / NOT_CANONICAL`

and simultaneously:

`RETROSPECTIVE_CREDIT_ORDER_DEPENDENT / TELESCOPING_CORE_SURVIVES / SUBMODULARITY_AND_INTRINSIC_SCALAR_KILLED / NOT_CANONICAL`.
