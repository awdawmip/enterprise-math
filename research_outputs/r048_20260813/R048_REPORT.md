# R048 Report — Post-Calibration Native Capability Debt Factorization and Second-Generation Mechanism Search

Researcher-ID: `EM-R048-2F6C91`

Task: `RS-R048-POST-CALIBRATION-NATIVE-CAPABILITY-DEBT-FACTORIZATION-GENERATION`

Taskbook source: `13605a3285d4eba319cd39d59acf1900b63dc357`  
Debt packet source: `20367fcd582acdcc1486b50d43ba1b2ab9f68d37`

Status:

`DEBT_BASIS_STRICTLY_COMPRESSED / DIVERSE_G2_NATIVE_CANDIDATES_FROZEN / MULTIPLE_DEBTS_DERIVED_FROM_SHARED_INTERNAL_MECHANISMS / TARGET_SPECIFIC_CALIBRATION_DETAILS_NOT_USED_FOR_GENERATION / NO_WINNER / NOT_CANONICAL`

## 1. Scope and isolation

R048 was executed as a two-stage generation with a hard ordering barrier:

1. **Stage A — DEBT FACTORIZATION** was completed and hashed before any G2 candidate record was admitted.
2. **Stage B — G2 generation** then consumed only the frozen Stage-A basis plus Foundational Logic / Gate V3 typing.

The failure-derived content source for Stage A was only:

`research_inputs/R048_FAILURE_DERIVED_CAPABILITY_DEBT_PACKET_20260813.md @ 20367fcd582acdcc1486b50d43ba1b2ab9f68d37`.

`AGENTS.md`, `FOUNDATIONAL_LOGIC.md`, and `native_semantics_admissibility.json` V3 were used only as repository/type-governance rules. No R046 engineering atlas/kernel/interface, PR #534 content, R047C raw 12×4 matrix, KENG protocol/tolerance details, PR #537 target-specific calibration artifacts, classical-pi numerical selection signal, or R047 candidate definition was read.

A mandatory account-level GLOBAL_KNOWLEDGE synchronization incidentally exposed a high-level prior-generation summary and the name of one historical shoulder. This is recorded as `CONTEXT_CONTAMINATION_RISK_QUARANTINED`; no raw definition, score matrix, protocol, tolerance, or historical mechanism definition was opened, and the incidental text was not used to define, modify, rank, kill, or hash the Stage-A basis or any G2 candidate.

## 2. Stage A — debt factorization

### 2.1 Frozen independent basis

The six raw debts do **not** survive as six native primitives. They factor through three independent native-side capability debts:

### NB-A — COMPOSITIONAL_REFINEMENT_INTERFACE

**Stratum:** `N0_OR_N0D_STRUCTURE_DEBT`.

Weakest admissible requirement: any candidate claiming enlargement, partition, aggregation, extensivity, or scale must exhibit a finite typed partial composition `⊙` of native presentations, associative up to N0-isomorphism on compatible triples, plus any claimed refinement/coarsening maps `ρ` with identity/composition laws.

No scalar magnitude is included. Center, distance, radius, angle, continuum measure, and engineering units remain withheld.

This is strictly weaker than D1: an extensive scalar, if it exists, is later N2 structure compatible with NB-A.

### NB-B — CONSERVATIVE_RELAXING_FINITE_ACTION

**Strata:** `N1_OPERATIONAL_SEMANTICS_DEBT` plus theorem-level N2 witnesses.

Weakest admissible requirement: a finite-information local update relation `U` must be closed on the declared state family and equivariant under the relevant N0 relabelings. If a candidate claims conservation plus genuine relaxation/recurrence, it must derive:

- a nonconstant internal finite carrier `C` invariant under every legal update; and
- a nonconstant well-founded internal quotient/potential `P` that strictly descends on a nonempty class of legal trajectories before terminal/recurrent entry.

No metric contraction, continuum time, or universal convergence is required.

Conservation and relaxation are logically independent. The basis records their **coexistence** as the missing operational capability rather than pretending one derives from the other.

### NB-C — FUNCTORIAL_FINITE_QUOTIENT_COMPARISON

**Stratum:** `N2_READOUT_OR_QUOTIENT_DEBT`.

Weakest admissible requirement: any candidate claiming fractions, rates, ordered response, separated response, or an extensive observable must derive a finite quotient `q:S→Q` from N0/N1 only; prove relabeling/choice invariance at the claimed strength; and show that the relevant composition/update descends to `Q`.

Any comparison on `Q` must be internally generated — for example reachability, inclusion, divisibility, finite-fiber cardinality, or a proved monotone. Exact rational ratios of finite event/fiber counts are admissible. Conversion to engineering units is explicitly excluded and remains calibration.

Stage-A basis freeze:

`sha256:78d1dfd606304d30a51bdacc9061a9e61cc4fa4cd7a4453cebf435dc058f6d99`

### 2.2 D1–D6 disposition

| Raw debt | Stage-A action | Result |
|---|---|---|
| D1 composable extensive relational quantity | `SPLIT / RETYPE / MERGE` | composition/refinement → NB-A; local updateability → NB-B; extensive scalar → NB-C. D1 is not independent. |
| D2 recurrent process with fraction/rate semantics | `SPLIT / RETYPE / WEAKEN / MERGE` | recurrence/action → NB-B; exact finite fractions → NB-C; external clock/rate interpretation excluded from Foundation. |
| D3 conservation + relaxation + scale | `SPLIT / MERGE / RETYPE` | scale/refinement → NB-A; conservation+relaxation coexistence → NB-B; scalarized observables → NB-C. |
| D4 bounded recurrence/operator with ordered response | `SPLIT / RETYPE / WEAKEN / MERGE` | finite action/operator → NB-B; internally ordered response quotient → NB-C. No spectral/wave axis is imported. |
| D5 traceable readout/metrology | `MOVE_TO_CALIBRATION_ONLY` | a frozen native N2 observable may later be mapped to external traceable units/uncertainty, but the map cannot select or modify N0/N1. |
| D6 shared low-information state across roles | `MOVE_TO_EVALUATION_ONLY` | explanatory-compression criterion after freeze; no target-indexed state or per-domain adapter primitive. |

### 2.3 Independence witnesses

The basis is smaller than D1–D6 but is not collapsed into one vague mega-debt.

- NB-A does not imply NB-B: finite records may have associative composition/refinement with no chosen dynamics.
- NB-B does not imply NB-A: a finite transition system can relax with no composition/refinement algebra.
- NB-C does not imply either: a static relational object may have a nontrivial automorphism-invariant quotient without dynamics or gluing.
- Conservation does not imply relaxation: reversible finite actions preserve carriers but forbid a strict branch-independent monotone.
- Relaxation does not imply nonconstant conservation: the two-state map `1→0, 0→0` has a strict finite descent but every invariant scalar is constant.
- Composition plus action does not force a useful order: a transitive symmetric action may collapse all relabeling-invariant state comparisons.

The exact typed graph and per-debt weakest restatements are frozen in `R048_DEBT_FACTORIZATION.json` and `R048_INDEPENDENT_DEBT_BASIS.json`.

## 3. Stage B — six second-generation mechanisms

No winner is selected. Candidate order is an ID order only.

### G2-M1 — PAIRWISE_EQUALIZATION_REWRITE

**N0:** finite simple graph plus finite token multiplicities on vertices.  
**N1 law:** across an edge, if local multiplicities differ by at least two, move one token from the larger endpoint to the smaller.  
**N2:** total `C=Σx(v)`, quadratic finite potential `P=Σx(v)^2`, terminal predicate.

Exact laws:

- `C` is conserved.
- If `d=x(u)-x(v)≥2`, a legal move gives
  `P_after-P_before=-2(d-1)≤-2`.
- Therefore every branch terminates.

Shared capability yield: exact conservation and genuine relaxation arise from the **same one-token transfer law**, without a metric. Graph/interface composition preserves total token count.

Productive failure: arbitrary block-sum coarse states are not generally dynamically lumpable, so exact microscopic relaxation does not automatically provide refinement-scale closure. Nontrivial recurrence is absent.

Gate V3 typing: graph/token state is declared N0; legal-edge choice and update are N1; `C`, `P`, and block sums are N2. Any geometric interpretation is withheld.

Freeze SHA-256: `a12bcaa3c6b22366865670513a065b1cf6b9fd95f3941b1e6d13b38becf44f52`

### G2-M2 — SIGNED_CANCELLATION_LEDGER

**N0:** finite native type set `A`, positive/negative token multiplicities `p,n:A→N`.  
**N1 law:** cancel one opposite-sign pair of the same type.  
**N2:** signed balance vector `q_a=p(a)-n(a)`, total token count `N`, canonical normal form.

Exact laws:

- every `q_a` is conserved;
- every cancellation lowers `N` by exactly two;
- every branch terminates at the unique normal form
  `p(a)=max(q_a,0)`, `n(a)=max(-q_a,0)`;
- under finite type coarsening `f:A'→A`, signed balance pushes forward by exact integer summation.

Shared capability yield: composition, a conserved extensive quotient, finite relaxation, and quotient refinement all come from one pair-cancellation law.

Productive failure: normal-form **representatives** are not monoidal. A separately normalized `+1` and `-1` compose to a cancellable pair, while the normal form of their composite is empty. The natural compositional object is the quotient `q`, not the representative.

Freeze SHA-256: `4b4da01eee68c59d683463fbd33b5a36fd36c8ed00456197f96ba3b22e0f1dac`

### G2-M3 — BINARY_CARRY_RELAY

**N0:** finite un-oriented path of `L` cells, each carrying a bit.  
**N1:** choose one endpoint and induced successor direction; repeatedly apply the finite carry rule. The endpoint is explicitly N1 because path reversal is an N0 automorphism.  
**N2:** return periods, carry-event counts, divisibility chain.

Exact laws:

- the action is one cycle of length `2^L`;
- the first `k` cells have exact return period `2^k`;
- over a full orbit, carry reaches level `k≥1` exactly `2^(L-k)` times;
- the resulting exact finite fraction is `1/2^k`;
- return periods form the internal divisibility chain `2 | 4 | ... | 2^L`.

Shared capability yield: recurrence, compositional fraction semantics, and an ordered family of nested responses all arise from one finite carry action; no clock, angle, radian, continuous time, Fourier object, or wave axis is introduced.

Productive failures/no-go:

- no nonconstant invariant exists under the transitive full cycle;
- no genuine relaxation exists;
- the chosen endpoint cannot be promoted to N0.

Freeze SHA-256: `ad4ac85dc5dc4463edf0f584e317f23e40aee47d509062803a19309d81ffb6fa`

### G2-M4 — FINITE_UNION_PROPAGATION

**N0:** finite graph, finite atom-type set, and atom-presence predicates at vertices.  
**N1 law:** along an edge, replace both endpoint atom sets by their union.  
**N2:** global union `U`, subset order, finite deficit
`P=Σ_v(|U|-|S_v|)`.

Exact laws:

- `U` is conserved;
- every nontrivial edge update lowers `P` by exactly `|S_u △ S_v|`;
- on each connected component, every maximal nontrivial branch terminates at the constant state equal to that component's initial union.

Shared capability yield: conservation, relaxation, canonical internal order, and terminal recoalescence all come from the same idempotent finite join principle.

Productive failure: conserved union cardinality is **not extensive**. Two components carrying the same atom each have union size one, while their composite still has union size one. Therefore conservation and extensivity must remain separate semantic claims.

Freeze SHA-256: `3830eab3a05532a3df5427a7c24ce15e50f62ae10130b149a432a47094cec85c`

### G2-M5 — FINITE_REWRITE_ACTION_QUOTIENT

**N0:** finite family `S` of relational states/presentations modulo only declared N0-isomorphism.  
**N1:** a small **uniform low-description** family of local rewrites `F={f_i}`; close it under composition to transformation semigroup `M=<F>`. Arbitrary endofunction tables are not accepted as a low-information core.  
**N2:** principal reachable set `O(x)=xM`, mutual-reachability quotient, inclusion preorder, orbit-size monotone `r(x)=|O(x)|`, finite orbit-size ratios.

Exact laws:

- for every step `y=f_i(x)`, `O(y)⊆O(x)`, hence `r(y)≤r(x)`;
- mutual reachability implies equal principal reachable sets;
- sink quotient classes are exact recurrent/terminal classes of the finite action;
- independent direct-product systems satisfy
  `O((x,y))=O_M(x)×O_N(y)`, so orbit sizes multiply.

Shared capability yield: recurrence, quotient relaxation, ordered response, finite rational comparison, and system composition come from the transformation-semigroup closure itself.

Productive failure: semigroup closure alone does not imply a conserved extensive carrier, and a large arbitrary generator table can hide per-target patchwork. Low-description local derivation of the generators is theorem-critical. Gate verdict is therefore `CONDITIONAL_DERIVED`; the arbitrary-table variant is rejected as explanatory compression.

Freeze SHA-256: `be5c048b093423b07a1515f7f4b08baf99ef18d3fafceee0979c9fb5e17dee48`

### G2-M6 — CONSERVATIVE_SWAP_GROUP

**N0:** finite graph plus finite labels on vertices.  
**N1:** swap endpoint labels along one native edge; generated actions form a finite permutation group.  
**N2:** componentwise label-multiplicity quotient and finite orbit cardinalities.

Exact laws:

- componentwise label multiplicities are conserved;
- every generator is an involution and all generated actions are finite/recurrent;
- on a connected `n`-vertex graph with label multiplicities `m_a`, orbit cardinality is the finite combinatorial count `n!/∏m_a!`;
- no nonconstant `P` can be nonincreasing under every swap and strictly decreasing under any one swap.

The no-go proof is one line: for involution `s`,
`P(sx)≤P(x)` and then applying the same rule to `sx` gives
`P(x)=P(s(sx))≤P(sx)`, so equality is forced.

Shared capability yield: conservation, finite recurrence, and exact composition arise from one reversible local law.

Productive failure: strict genuine relaxation is structurally impossible without leaving the frozen reversible swap group or moving relaxation to a coarser noninvertible quotient.

Freeze SHA-256: `90dfc14872299e611c1949d5784f32ac6f071ca58752609f72b5150d5d9e30ca`

Candidate-set freeze SHA-256:

`2e1f85a3faf37a0525364c220f9449caea45408bf6a954c09045bf78646cf959`

## 4. Cross-candidate theorem/counterexample ledger

The frozen ledger contains:

- Stage-A independence constructions;
- exact conservation and descent theorems for M1;
- confluence and quotient additivity for M2;
- exact `2^L` recurrence and `2^-k` carry fractions for M3;
- exact union conservation and terminal consensus for M4;
- principal-orbit monotonicity and quotient order for M5;
- the involutive no-relaxation theorem for M6;
- explicit counterexamples to false coarse closure, false monoidality of normal representatives, false extensivity, and false implication `recurrence+conservation ⇒ relaxation`.

General theorem claims are justified by finite algebraic arguments in the ledger. Enumeration is only a regression layer.

Ledger freeze SHA-256:

`f6bd4b544dec90183873839ac2ea192d87530ddad3d904cd4d87db3f11fb6771`

## 5. Exact pressure tests

The checker `check_r048.py` performs deterministic bounded tests:

- freeze/hash/schema consistency;
- M1 paths `n=2..4`, total tokens `M=0..6`;
- M2 two native types with all counts `0..3`, exploring all cancellation branches;
- M3 complete state orbits for `L=1..8`;
- M4 all states on paths `n=2..4` with `|A|=1..3`;
- M5 all single-generator endofunction systems and a deterministic paired-generator sample on three states;
- M6 all binary label states on paths `n=2..5`.

Result:

`R048_EXACT_CHECKER_PASS total_checks=15990`

The bounded scans support only their declared finite ranges. They do not replace the general algebraic proofs in the theorem ledger.

CI is not part of this L1/L2/L3 research checkpoint:

`CI_NOT_REQUIRED_FOR_RESEARCH`

## 6. False-claim pressure tests and what failed

### False stabilization

M1 terminates but stable states are not generally unique. Therefore “strict potential descent” does not imply a unique equilibrium object.

### False conservation

M4 has a conserved global union but not an additive/extensive conserved scalar. “Conserved” cannot be upgraded to D1 extensivity.

### False recurrence

M2 and M4 have strict finite relaxation but only fixed-point recurrence. Relaxation does not create a nontrivial periodic/recurrent response family.

### False extensivity

M4 union cardinality fails additivity under overlap. M6 orbit size is also not additive under component recoalescence.

### False coarse closure

M1 block sums do not generally determine which microscopic moves are legal. A coarse readout must prove a congruence/lumpability condition before it is treated as an induced dynamics.

### False monoidal normal form

M2's quotient `q` composes exactly, but independently normalized representatives can recoalesce and cancel after composition.

### Reversibility obstruction

M6 proves that an involutive reversible action cannot support a strict branch-independent well-founded monotone under the same legal generators.

### Parameter explosion

M5 identifies the main G2 anti-patchwork risk: a transformation semigroup is mathematically exact but can be information-theoretically vacuous if its generator tables are arbitrary. Only small uniform local rewrite schemas count as serious frozen mechanisms.

## 7. Gate V3 semantic-strength audit

| Candidate | N0 | N1 | N2 | Gate result |
|---|---|---|---|---|
| M1 | graph + finite token state | legal local balancing rewrite | total/potential/stable quotient | `CONDITIONAL_DERIVED`, admissible with no geometric promotion |
| M2 | native types + signed token state | same-type cancellation | signed quotient/normal form/counts | `CONDITIONAL_DERIVED`, quotient-level composition explicit |
| M3 | un-oriented bit path | endpoint/orientation + carry action | return periods/event fractions/divisibility | `CONDITIONAL_DERIVED`; endpoint-as-N0 would be `SEMANTIC_MISMATCH` |
| M4 | graph + atom-presence relation | local union update | union/order/deficit | `CONDITIONAL_DERIVED`; no continuum propagation semantics |
| M5 | finite N0 state family | uniform local generator family + closure | reachable-set quotient/order/counts | `CONDITIONAL_DERIVED` only for low-description generator schemas; arbitrary tables fail compression |
| M6 | graph + labels | local swaps/group action | multiplicity/orbit quotient | `CONDITIONAL_DERIVED`; strict relaxation is theorem-level impossible |

No candidate promotes center, distance, radius, circle, angle, radian, continuum, Fourier, Gaussian, PDE, engineering metrology, or a classical target value into N0.

## 8. Debt coverage without winner selection

The mechanisms intentionally separate capability clusters:

- M1 derives **conservation + genuine relaxation** from one local balancing rule.
- M2 derives **composition + conserved extensive quotient + confluence/refinement** from one cancellation rule.
- M3 derives **recurrence + exact fractions + ordered nested responses** from one carry rule.
- M4 derives **conservation + relaxation + internal order** from one finite join law, while failing extensivity.
- M5 derives **recurrence + quotient relaxation + ordered response + multiplicative composition** from one action-semigroup principle, while exposing parameter-explosion risk.
- M6 derives **conservation + recurrence + reversible composition** and proves a no-go theorem for strict relaxation.

This is the intended second-generation diversity. No candidate is declared best. No candidate is ranked by unknown later calibration behavior.

## 9. Productive failures retained

The frozen productive-failure ledger contains six nonfatal failures:

1. microscopic relaxation does not imply coarse lumpability;
2. canonical quotient composition does not imply monoidal raw representatives;
3. recurrence/fraction/order does not imply conservation or relaxation;
4. conservation does not imply extensivity;
5. finite operator algebra can hide patchwork if generator description is not compressed;
6. exact reversibility blocks strict relaxation.

These are retained as design boundaries, not used as excuses to force a winner.

## 10. Contamination audit

Generation did **not** use:

- R046 engineering target details;
- PR #534;
- R047C raw 12×4 matrix;
- KENG protocol/tolerance details;
- PR #537 target-specific artifacts;
- classical pi numeric value;
- historical R047 candidate definitions;
- prior-candidate calibration score/bridge score as a selection signal.

Historical-shoulder pull count: `0`.

Incidental prior-generation context seen during mandatory global synchronization is marked `CONTEXT_CONTAMINATION_RISK_QUARANTINED` and was not used as a generative or selection signal.

Contamination-audit freeze SHA-256:

`3fc6911d9a620667e3c1f27125f29968b4bcc959674156b23f23897a6c2e20a3`

## 11. Frozen artifact set

Required artifacts:

- `R048_REPORT.md`
- `R048_DEBT_FACTORIZATION.json`
- `R048_INDEPENDENT_DEBT_BASIS.json`
- `R048_G2_CANDIDATE_SET.json`
- `R048_NATIVE_DERIVATION_LEDGER.json`
- `R048_INTERNAL_STRUCTURE_MATRIX.json`
- `R048_PRODUCTIVE_FAILURES.json`
- `R048_CONTAMINATION_AUDIT.json`
- `check_r048.py`
- `R048_EXACT_CHECK_RESULTS.json`

Stage-A factorization freeze:

`sha256:b42278ee6521b5d71161c64d964b50dc3c58c974cedf902bc315b88d3158bea0`

Stage-A independent basis freeze:

`sha256:78d1dfd606304d30a51bdacc9061a9e61cc4fa4cd7a4453cebf435dc058f6d99`

G2 candidate-set freeze:

`sha256:2e1f85a3faf37a0525364c220f9449caea45408bf6a954c09045bf78646cf959`

No winner is frozen.

Any later reopening of detailed calibration targets must treat changes to a candidate core as a **new generation** rather than editing these hashes in place.
