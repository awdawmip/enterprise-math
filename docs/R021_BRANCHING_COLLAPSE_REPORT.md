# R021 Branching-Collapse Tool Calculus — Final Research Return

Task `RS-R021-BRANCHING-COLLAPSE-TOOL-CALCULUS` · Researcher `EM-R021-9832F2` · Driver `EM-DVR-QSO16` · taskbook base `15e9dcb67ce1f78b320099f2078c733bcba39ebb` · `CI_NOT_REQUIRED_FOR_RESEARCH` · `NOT_CANONICAL`.

**Return:** `BRANCHING_COLLAPSE_TOOL_CORE_FOUND / EXACT_REGIME_CLASSIFIED / ON_DEMAND_COMPILER_CHECKED / PARETO_ADVANTAGE_DEMONSTRATED / NOT_CANONICAL` and `ROOTING_SUCCESS / ENTERPRISE_BRANCHING_SPECIALIZATION_SURVIVES / TOOL_CANDIDATE / NOT_CANONICAL`.

## 0. Decision

Branching collapse survives, but the universal claim is killed. It is **not** a semantic way to recover pointwise information already erased by a coarse label. Its strong reusable regime is instead:

> legitimate Boolean/result-support state + relational/union-preserving futures + exact/charged branch denotations + on-demand reachable refinement + exact-union coalescence, especially when global deterministic combination states are mostly unreachable or the support has a compact symbolic representation.

The real Pareto gain is normally global-table/precompute/reachable-slice factorization. Live information does not disappear: branch IDs, correlation tokens, subset dictionaries and decoders are part of cost.

## T01 — strict types and exactness hierarchy

Fix finite fine system `(X,q,{R_g},o)`, declared finite future language `U`, and `O(A)={o(x):x in A}`. Define point signature `Σ_U(x)=(O(R_w[{x}]))_{w in U}` and support signature `Σ_U^P(A)=(O(R_w[A]))_{w in U}`.

A branch carrier is `(B, [[-]], Cost)` with exact denotation `[[b]] subseteq X`. A live configuration `Γ` denotes `union_{b in Γ}[[b]]`. If an arbitrary subset is represented by a bitmask/dictionary/correlation ID, that data is charged.

Do not conflate:

| object | meaning |
|---|---|
| literal-alternative branch | singleton fine alternative |
| cell/fibre branch | full quotient cell |
| exact support branch | exact subset of `X` |
| refinement token | `(coarse label, hidden coordinate)` denoting a proper subset; coordinate is charged |
| on-demand branch | token/refinement created only on reached/demanded suffix |
| coalesced branch | exact union, or a forgetful hull requiring a safety test |

Exactness levels: one-step support `E1`; finite-word final support `EW(U)`; repeated collapse/re-expansion `ER`; multiplicity `EM`; provenance `EP`. For one common path model, `EP => EM => EW => E1`; converses fail. Boolean duplicate coalescence is support-exact but not multiplicity/provenance exact. One-step exactness does not imply composition exactness.

## T02 — unsafe deterministic collapse: minimal repairs and no-resurrection

For generator `g`, set `σ_g(x)=q[R_g[{x}]]`. The partition by `(q(x),σ_g(x))` is the **unique coarsest refinement of `q`** making next coarse successor-support constant on blocks: every valid block must lie inside one equal-signature class, and those classes work.

For declared language `U`, the partition by `(q(x),Σ_U(x))` is the **unique coarsest static deterministic refinement** from which all declared pointwise final supports can be recovered. A recursively executable quotient may need the stronger standard behavioural/partition-refinement congruence; final-answer sufficiency and transition closure are distinct.

**No-resurrection theorem.** Let `e(x)` be the complete initial runtime encoding, including every branch ID and hidden token. If execution reads only `e(x)` and must output exact pointwise `Σ_U(x)`, then

`e(x)=e(y) => Σ_U(x)=Σ_U(y)`.

Otherwise identical available information would be required to produce different exact outputs. Hence an exact pointwise encoder refines the future-signature kernel. A later split of the bare cell cannot discover which fine point was originally present; branching the whole fibre changes the semantic state to a support of possibilities.

This kills the strongest hypothesis that runtime branching can replace pointwise future refinement without carrying equivalent information somewhere.

## T03 — minimal branch width with honest cost

For a fixed atom dictionary `D={A_1,...,A_K}`, a configuration decodes by union. For required support `S`, let `w_D(S)` be the fewest atoms whose union is `S`; for reachable family `Reach_U`, `W_D=max_S w_D(S)`. Meaningful minimization is

`W*(B)=min_{Cost(D)<=B} W_D`,

not unconstrained width. With free arbitrary subset atoms, every required support becomes one atom and `W=1`: fake compression.

Bounded exhaustive oracle, universe `{0,1,2}`, required all singletons and 2-subsets:

| K atoms | max width W | raw membership bits K*3 |
|---:|---:|---:|
| 3 | 2 | 9 |
| 6 | 1 | 18 |

The Pareto points are incomparable; no canonical minimum exists without a representation class/cost order. Record at least atom/dictionary storage, transition/code storage, preprocessing, online work, serial/parallel depth, live width, cumulative branch creation, peak metadata, decoder/reconstruction, cache size, reachability fraction and query reuse. This is aligned with R014: compare only implementations of the **same semantic contract**.

## T04 — branch-on-demand split / execute / coalesce

Maintain exact reachable support invariant

`union_{C in Γ_t} C = A_t`.

Before `g`, split each exact branch by next-step `σ_g`; this is the coarsest local split making next coarse support uniform. Execute exact relational images `R_g[C]`. Recoalesce by exact set union (optionally grouped by coarse label) **without re-expanding to full fibres**.

Because relational direct image preserves union, split preserves union and exact union preserves union, induction gives exact fine support and therefore exact final result-support after every finite prefix. The oracle checks this.

Two recoalescence modes must be distinguished:

1. **lossless union**: replace `A,B` by a token denoting exactly `A union B`; always safe in Boolean relational support semantics, but the union token/configuration cost is charged;
2. **forgetful/hull**: replace exact `A` by coarser representable `H`; safe for remaining language `V` iff `Σ_V^P(A)=Σ_V^P(H)`.

Same current `q` label is not enough. Safe forgetful tests can be suffix-local/on-demand; broad repeated workloads may eventually populate the same refinement cache a global compiler would have built.

## T05 — deterministic versus branching resource Pareto

No cross-semantic comparisons are allowed. Within a fixed exact contract:

- small/high-reuse pointwise systems can favor global deterministic refinement;
- sparse/one-off workloads can favor on-demand reachable refinement;
- explicit deterministic subset/future tables can be much larger than reusable branch-atom tables;
- branching pays live-set work and metadata;
- a good symbolic deterministic program can factor the same structure, so explicit-state exponential gaps are representation-model results, not universal program-size lower bounds;
- sequential word depth is not generically reduced: both execute one dependent generator per word position. Branching can reduce precomputation latency, not the semantic word depth.

**Explicit finite table witness.** Fine point states are all `2^n` subset masks. Generator `test_i` keeps membership atom `i`; final observable is nonempty. The `n` one-letter tests distinguish all `2^n` masks. Branching stores the mask as the live set of `n` reusable atoms.

| n | deterministic future states | deterministic table entries | branch atoms | branch table cells | live bits D/B | worst work D/B |
|---:|---:|---:|---:|---:|---:|---:|
| 4 | 16 | 64 | 4 | 16 | 4/4 | 1/4 |
| 6 | 64 | 384 | 6 | 36 | 6/6 | 1/6 |
| 8 | 256 | 2048 | 8 | 64 | 8/8 | 1/8 |
| 10 | 1024 | 10240 | 10 | 100 | 10/10 | 1/10 |

Thus branching is genuinely nondominated in explicit-table static storage/precompute while **not** beating the live information lower bound and losing online work. For broad repeated queries the deterministic table can amortize and dominate runtime.

## T06 — finite oracle / exhaustive / mutations

Artifacts: `experiments/r021_branching_collapse_oracle.py`, `tests/test_r021_branching_collapse_oracle.py`, `experiments/r021_branching_collapse_results.json`.

`16` focused tests pass locally under Python 3.13. The oracle includes exact fine support, naive existential quotient, successor/future partitions, exact branch-on-demand execution, full-fibre re-expansion mutation, forgetful merge tests, branch-dictionary frontier, arithmetic benchmarks, witness cutoff and middle-incidence tests.

Exhaustive deterministic one-generator two-step quotient-composition search (`trial=(surjective q,f,start fibre)`):

| |q maps| |(q,f) systems| trials | failures |
|---:|---:|---:|---:|---:|
| n=1 | 1 | 1 | 1 | 0 |
| n=2 | 3 | 12 | 20 | 0 |
| n=3 | 13 | 351 | 837 | 84 |

Total `858` trials. Thus 3 fine states are minimal in this full-starting-fibre/coarse-output search class. First witness: `q(0)=q(1)=0,q(2)=1`; `f(0)=0,f(1)=2,f(2)=0`; from fibre 0 exact two-step q-support `{0}` but quotient-squared gives `{0,1}`. Mutation tests also detect re-expansion and future-inequivalent merge.

## T07 — arithmetic / relation pressure tests

### Floor quotient + translation

`q_r(n)=floor(n/r)`, `T_c(n)=n+c`, `g=gcd(r,c)`. In one fibre `n=rk+s`, the horizon-`h` point signature depends on `floor((s+tc)/r)`. Distinct threshold residues before the cycle repeats give exactly

`N_h = 1 + min(h, r/g - 1)`.

Eventual pointwise refinement has `r/g` classes, consecutive residue blocks of size `g`, equivalent to retaining `floor(n/g)`. If `g=1`, a long enough future reconstructs the full residue mod `r`: branching cannot avoid carrying `r` distinguishable point configurations. Example `r=10,c=1`: class counts `2,3,6,10` at `h=1,2,5,9`. For `r=12,c=8`, eventual count is only `3` because `g=4`.

Different semantic contract: if the legitimate current state is the **full q_r fibre interval**, translation preserves one exact interval of length `r`; its coarse q-support has width at most `2`, and the phase cycle has `r/g` values. This is a strong symbolic-support regime, not recovery of an unknown exact point.

### p-th-power bracket

R017/R018 already make `Q_p=(L_p,U_p)` minimal for the future interface “choose lower or upper endpoint later”. It is not arbitrary-translation pointwise complete: `Q_2(5)=Q_2(8)=(4,9)`, but after `+1`, `Q_2(6)=(4,9)` while `Q_2(9)=(9,9)`.

For the different **full open-gap support** `I_{p,k}={k^p+1,...,(k+1)^p-1}` and positive translation, the exact support stays an interval of fixed length. Since p-th-power gaps are nondecreasing to the right, that interval contains at most one exact p-th power, hence strict `Q_p` support width is at most `3` (left gap + singleton power + right gap). Cube benchmark `p=3,k=3,c=5,h=8`: gap `28..63`, max bracket width `3`, while pointwise future signatures already split it into `15` classes. The exact support itself remains two-endpoint symbolic data.

### Witness/factor cutoff

`6,10,14,22,26` all have low cutoff-2 witness set `{2}`, but cutoff 13 gives five different witness signatures. If the original exact integer must answer its own later witness query, five distinct configurations are unavoidable; branching all five changes to union-of-possibilities semantics. If the current state is genuinely the five-number support and only union results matter, support branching is exact. Correlation queries can force the distinctions back.

### Middle-incidence composition

`R={(a,b1)}`, `S={(b2,c)}`. Both have nonempty coarse middle marginal, but exact `S∘R` is empty because `b1!=b2`. Cardinality/marginal metadata is insufficient; the middle witness identity/correlation must be retained and charged. Larger arbitrary incidence can approach full relevant correlation cost.

## T08 — theorem package / language-relative compiler

Surviving package for a possible later Lean gate:

1. `NO_RESURRECTION`: pointwise exact encodings refine `ker Σ_U`.
2. `ONE_STEP_COARSEST`: `ker(q,σ_g)` is unique coarsest next-q-support refinement.
3. `FUTURE_STATIC_COARSEST`: `ker(q,Σ_U)` is unique coarsest static pointwise answer refinement.
4. `SUPPORT_BRANCH_INVARIANT`: exact branch denotations + relational execute + exact-union coalescence preserve support for finite words.
5. `FORGETFUL_RECOALESCENCE_IFF`: `A -> H` is suffix-safe iff remaining support signatures agree.
6. 3-state composition/re-expansion counterexample.
7. No generic canonical minimal branching presentation without a declared cost/representation class.

The unique deterministic future quotient and a branching presentation answer different representation questions. A `K`-atom branch system may expose `2^K` live configurations; no-resurrection still requires enough distinct configurations for pointwise futures.

## T09 — prior-art/rooting

Generic mathematics roots cleanly:

- relational/powerset support and Boolean reachability: classical; already R015/R016;
- Myhill–Nerode-style future equivalence: Nerode, *Linear Automaton Transformations* (1958), DOI `10.1090/S0002-9939-1958-0135681-9`;
- relational coarsest partition: Paige–Tarjan, *Three Partition Refinement Algorithms* (1987), DOI `10.1137/0216062`;
- saturation/completeness viewpoint: Cousot–Cousot abstract interpretation, POPL 1977, DOI `10.1145/512950.512973`;
- on-demand abstraction refinement: Clarke–Grumberg–Jha–Lu–Veith, CEGAR, CAV 2000, DOI `10.1007/10722167_15`;
- symbolic state/support representation: Burch et al., *Symbolic Model Checking: 10^20 States and Beyond* (1992), DOI `10.1016/0890-5401(92)90017-A`;
- bisimulation/transition-system behavioural equivalence: Rutten, *Universal coalgebra* (2000), DOI `10.1016/S0304-3975(00)00056-6`;
- minimum NFA-like synthesis is not a cheap generic primitive: Jiang–Ravikumar, *Minimal NFA Problems are Hard* (1993), DOI `10.1137/0222067`, where DFA→minimum equivalent NFA decision is PSPACE-complete.

Therefore the Enterprise residue is the collapse-specific **typing + no-resurrection boundary + exact support compiler invariant + two recoalescence modes + honest R014 accounting + arithmetic kill tests**, not a novelty claim over automata/abstract interpretation.

## T10 — active kill table

| hypothesis | result |
|---|---|
| branching always stronger than deterministic refinement | **killed** |
| bare coarse label can later branch back to exact point | **killed by no-resurrection** |
| one-step existential quotient implies composition exact | **killed; 3-state minimum in bounded class** |
| hidden exact subset/correlation can be free metadata | **rejected by cost model** |
| exact-union recoalescence needs global future precompute | **false; exact union is always Boolean-support safe** |
| forgetful recoalescence only needs same current q | **killed; needs remaining support-signature equality** |
| pointwise floor translation can force fine coordinate back | **yes; full residue when gcd(r,c)=1** |
| p-th bracket is universal future carrier | **killed for translation** |
| compact full-gap/fibre support can survive | **yes; separate support semantics** |
| witness/cardinality marginals preserve future correlation | **killed** |
| branching has a real resource regime after charging metadata | **yes: explicit table / sparse reachability / symbolic support** |
| generic minimum branching presentation is practical/canonical | **no** |

## Downstream routing

- **P023:** preserve deterministic future-safe theorems; add only a separate execution-presentation layer after Driver acceptance. Distinguish `POINTWISE_FUTURE_SAFE`, `FULL_FIBRE_ONE_STEP_SUPPORT_SAFE`, `SUPPORT_RELATIONAL_SAFE`, `REPEATED_REEXPANSION_SAFE`, `FUTURE_REFINEMENT_REQUIRED`.
- **P018:** preserve static precision theorems; type dynamic outputs as cell label vs exact support token vs future-refined point carrier. Never silently turn a cell label into full-fibre support after each operation.
- **R014:** add atom dictionary bits, live branch IDs, correlation metadata, transition/code size, refinement cache, width/creations, reachability fraction, reuse count, decoder/reconstruction and critical path. Compare only inside one exact semantic fibre.
- **P021:** witness/cardinality compression is unsafe when future needs origin identity, multiplicity or middle incidence; Boolean support branching is only for union/existential current-witness semantics.
- **R017/R018:** keep bracket selector theorem; do not promote bracket to pointwise translation completeness; full-gap interval support is a distinct optimization.
- **Shared tool:** after acceptance, route the oracle as a research regression/kill harness; do not update common surface in this `NOT_CANONICAL` task.

## Final mother-question answer

**Yes, but scoped.** Branching-collapse is a strong reusable **language-relative exact support compiler** when the semantic current state is a genuine result-support set, futures are union-preserving relations, supports have reusable/symbolic atoms, and sparse reachability/query volume makes global deterministic materialization wasteful. Then exact split/execute/union-coalescence is simple and real static/precompute Pareto gains exist.

**No as a universal pointwise compression.** If the future language distinguishes hidden representatives, the complete live branch configuration must distinguish them too. Branching can factor transitions and delay refinement, but cannot delete the information lower bound. Multiplicity/provenance require richer carriers and may invalidate idempotent coalescence.

The reusable object is therefore:

`exact support atoms + on-demand reachable refinement + lossless union coalescence + suffix-safe forgetful coalescence + honest resource accounting`.

That object survives all R021 kill tests.
