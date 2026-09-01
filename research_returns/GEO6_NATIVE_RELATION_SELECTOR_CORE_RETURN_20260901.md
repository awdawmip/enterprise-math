# GEO6 Native Relation Selector Core — Research Return

Task: `RS-GEO6-NATIVE-RELATION-SELECTOR-CORE`  
Publication: `TP2-46E1AB6359CBEBAA6B0D`  
Researcher: `EM-G6REL-91C7A4`  
Claim: `chatgpt-g6relcore-20260901-2055-91c7a4`  
Execution: `ER-84F85FED4E1FF5FC5732`  
Branch base: `5d5828f0c5db94bcafa1d5ca275bc9a44ccdf431`

## Terminal classification

`SUCCESS / CURRENT_LANGUAGE_THREE_SELECTOR_INDEPENDENCE_PROVED / MINIMAL_TYPED_EXTENSION_ATLAS_EXACTLY_CLASSIFIED`

Hard target:

`GEO6_NATIVE_RELATION_CORE_CONTACT_EXCLUSION_SUPPORT_TYPED_AND_CONVERSIONS_EXACTLY_CLASSIFIED`

is satisfied at the task's declared semantic-selector scope.

The decisive result is negative for any automatic current-language conversion and positive for an exact extension atlas:

1. current accepted P000/Full-Cell data do **not** force any of the six off-diagonal conversions among native contact `K`, exclusion/non-overlap `X`, and Cell×Support incidence `I`;
2. this remains true under a nontrivial finite equivariance requirement and with carrier/readout frozen;
3. the unrestricted three-relation interface has an exact information lower bound of two independent Boolean bits per unordered Cell pair plus one Boolean bit per Cell×Support slot;
4. a role-tagged common relation attains that bound but is only syntactic compression, not a semantic conversion theorem;
5. a genuine common witness-incidence primitive exists as an extension interface, but it necessarily carries separate contact/exclusion/support role information (or equivalent typing), so it is strictly stronger than any one selector;
6. genuine conversions arise only after explicit new typed laws such as an equivariant Cell↔Support self-duality or a declared support-overlap conflict law. Neither law is current accepted P000 authority.

No Working Truth, Foundation, native-geometry promotion, or novelty status is claimed.

## 1. Frozen authority and compatibility boundary

The execution freezes the current selector taskbook `sha1:7a3542eef47d600224f90ab0fb672285da11a3a6`, accepted selector review `sha1:510ed84f6ee0913eaee90372e2b591a30ebfa601`, and selector atlas `sha1:120b71b74dc07edd9a3c78474b51752676c6dae3`.

The accepted selector state relevant here is:

- `CONTACT_SELECTOR`: partially constrained, not resolved;
- `NONOVERLAP_SELECTOR`: unresolved;
- `SUPPORT_RELATION_SELECTOR`: unresolved;
- selector synthesis explicitly freezes `CONTACT != NONOVERLAP` and `CONTACT != SUPPORT_RELATION` absent a typed conversion theorem.

The accepted P000 Full-Cell axis-handle review gives the crucial current-language audit. Current full-P000 semantics provide opaque Cell identity, native adjacency/path count, six named native axes, and optional PF-10 local passage data, but no canonical cross-sort axis/channel relation. Its `S6` presentation-reindexing countermodel proves that current primitive data cannot manufacture a unique typed local attachment merely from names or carrier analogies. That review is frozen here only at its accepted definability-obstruction strength.

The Packing/Kakeya review leaves `NONOVERLAP_SELECTOR` unresolved and classifies conflict-graph packing, Hoffman/matching certificates and related finite packing machinery as classical/antecedent mathematics **after** an exclusion relation exists. It therefore cannot supply the missing native exclusion relation.

The Mahler review leaves `SUPPORT_RELATION_SELECTOR` unresolved and classifies generic FCA/Galois derivation and closure as prior art **after** a Cell×Support incidence exists. It therefore cannot supply the missing native incidence or self-dual identification.

Hence neither downstream classical machinery nor the current P000 primitive language closes this task by itself.

## 2. Typed base signature

Let `C` be the native Cell sort and let `S` be a separately typed Support sort whenever a support extension is under discussion. The weakest selector-level relations are:

- `K subset Sym^2_neq(C)` — native contact/readout adjacency;
- `X subset Sym^2_neq(C)` — native exclusion/non-overlap;
- `I subset C × S` — Cell×Support incidence.

The symmetry/irreflexivity restriction on `K` and `X` is stronger than bare binary typing and is imposed only to make the finite countermodels more demanding. Proving independence under this restriction proves independence a fortiori for weaker pair-relation contracts.

For a declared native automorphism `g`, admissible equivariance laws are

`K(gc,gd) <-> K(c,d)`,

`X(gc,gd) <-> X(c,d)`,

and, when `g` also acts on `S`,

`I(gc,gs) <-> I(c,s)`.

No physical-refinement naturality is silently imposed. The accepted Q24/current selector boundary does not yet supply a typed Full-Cell non-equivalence scale-refinement arrow. A future refinement interface must separately declare whether each relation is exactly pulled back, pushed forward, or only monotone.

## 3. Exact current-language implication matrix

At the current accepted semantic boundary the implication matrix, in the order

`(CONTACT, EXCLUSION, SUPPORT)`,

is exactly

| from \ to | CONTACT | EXCLUSION | SUPPORT |
|---|---:|---:|---:|
| CONTACT | YES | NO | NO |
| EXCLUSION | NO | YES | NO |
| SUPPORT | NO | NO | YES |

Every `NO` is backed by a same-carrier/same-readout finite countermodel, not by absence-of-proof reasoning.

### Equivariant witness bank

Take

`C = Z/4Z`, `S = Z/4Z`,

with a constant singleton readout and simultaneous `C4` translation on both sorts. Define three `C4`-invariant Cell-pair relations:

- `cycle = {01,03,12,23}`;
- `opposite = {02,13}`;
- `empty = {}`;

and two `C4`-equivariant incidences:

- `diag = {(0,0),(1,1),(2,2),(3,3)}`;
- `shift = {(0,1),(1,2),(2,3),(3,0)}`.

Then the six directed failures are witnessed as follows:

1. `CONTACT !-> EXCLUSION`: hold `K=cycle`, `I=diag`; vary `X=opposite` versus `empty`.
2. `EXCLUSION !-> CONTACT`: hold `X=cycle`, `I=diag`; vary `K=opposite` versus `empty`.
3. `CONTACT !-> SUPPORT`: hold `K=cycle`, `X=opposite`; vary `I=diag` versus `shift`.
4. `SUPPORT !-> CONTACT`: hold `I=diag`, `X=opposite`; vary `K=cycle` versus `opposite`.
5. `EXCLUSION !-> SUPPORT`: hold `X=cycle`, `K=opposite`; vary `I=diag` versus `shift`.
6. `SUPPORT !-> EXCLUSION`: hold `I=diag`, `K=opposite`; vary `X=cycle` versus `opposite`.

All twelve pair/incidence structures occurring in these witness pairs satisfy the declared `C4` equivariance. Thus finite symmetry does not rescue any missing conversion.

## 4. Minimality theorem for the unrestricted native relation core

Let `|C|=n`, `|S|=m`, and `E=binom(n,2)`.

With no conversion law coupling `K`, `X`, and `I`, the number of independent typed triples is exactly

`2^E * 2^E * 2^(nm) = 2^(2E+nm)`.

Equivalently:

- each unordered Cell pair must be able to represent all four local states `(K,X) = 00,01,10,11`;
- each Cell×Support slot must represent two incidence states.

Therefore any lossless **local typed** common representation has the exact lower bounds

`|A_pair| >= 4`,

`|A_incidence| >= 2`.

A single Boolean Cell-pair relation cannot encode both `K` and `X` without imposing a new law. Equality, complement, or any other functional dependence is therefore an additional semantic hypothesis, not a consequence of sharing the Cell carrier.

A role-tagged sum relation reaches the lower bound exactly by storing two bits on every Cell pair and one bit on every Cell×Support slot. This is optimal storage but yields the same diagonal implication matrix. Renaming three channels as one relation symbol does not identify their semantics.

The deterministic checker exhaustively verifies the lossless encoding for `n=3,m=2`: there are `E=3`, `nm=6`, hence `12` independent bits and exactly `4096` triples. Every triple round-trips through both the optimal role-tagged representation and the canonical witness-incidence representation below.

## 5. Finite typed signature atlas

### SIG0 — Independent typed triple

Primitives: `K`, `X`, `I` as above.

This is the safe minimum interface when no conversion has been justified. It does **not** assert current existence of those relations; it states the minimum typing required if they are introduced independently.

Implication matrix: diagonal only.

### SIG1 — Role-tagged sum

Use one syntactic relation container whose tagged restrictions are exactly `K`, `X`, and `I`.

This is lossless and information-minimal, but it is semantically equivalent to SIG0. No selector conversion is gained.

Implication matrix: diagonal only.

### SIG2 — Typed witness incidence

Introduce a witness sort `W`, a role map

`rho: W -> {CONTACT, EXCLUSION, SUPPORT}`,

and one incidence

`J subset C × W`.

For CONTACT and EXCLUSION witnesses impose degree two; for SUPPORT witnesses retain a typed support label. Define `K` and `X` by co-incidence in their respective role fibers and define `I` by incidence with SUPPORT witnesses.

This is a genuine shared **mechanism**: one incidence primitive projects to all three selectors. It can represent every finite triple exactly.

However, it is not a selector equivalence. Knowledge of one projection does not determine the other role fibers. The selector-level implication matrix therefore remains diagonal.

Minimality: if CONTACT and EXCLUSION witnesses are not role-distinguished, the construction forces `K=X`, contradicting the explicit same-carrier witness bank. If SUPPORT witnesses are not separately typed, the construction either loses the `Cell×Support` target sort or silently inserts a Cell↔Support identification. Thus three semantic role fibers, or an equivalent amount of typed information, are necessary for a universal witness-incidence representation.

### SIG3 — Explicit self-dual contact/support extension

Add an equivariant bijection

`delta: C <-> S`

and the law

`I(c,delta(d)) <-> K(c,d)`.

Now CONTACT and SUPPORT are mutually recoverable through `delta`; EXCLUSION remains independent.

The implication matrix becomes

| from \ to | CONTACT | EXCLUSION | SUPPORT |
|---|---:|---:|---:|
| CONTACT | YES | NO | YES |
| EXCLUSION | NO | YES | NO |
| SUPPORT | YES | NO | YES |

This is a legitimate typed conversion theorem **only after** the extra law is supplied. It is not current authority because `SELF_DUAL_IDENTIFICATION_SELECTOR` remains unresolved.

### SIG4 — Explicit support-overlap exclusion extension

Declare conflict semantics by

`X(c,d) <-> [c != d and exists s: I(c,s) and I(d,s)]`.

Then SUPPORT determines EXCLUSION, while EXCLUSION does not determine the underlying incidence. The checker finds an exact collision: distinct incidences with the same overlap graph.

The implication matrix becomes

| from \ to | CONTACT | EXCLUSION | SUPPORT |
|---|---:|---:|---:|
| CONTACT | YES | NO | NO |
| EXCLUSION | NO | YES | NO |
| SUPPORT | NO | YES | YES |

CONTACT remains independent.

Again, this is an explicit semantic extension, not something supplied by generic packing or FCA machinery.

## 6. What does and does not count as a conversion theorem

A selector conversion is forced only when the signature contains enough typed law to reconstruct the target relation from the source relation and the already accepted native data.

Accordingly:

- placing `K` and `X` on the same Cell carrier is not a conversion;
- calling `X` a conflict graph is not a construction of `X`;
- taking Boolean complement does not create a native support incidence and would add an unjustified law even as a pair conversion unless separately motivated;
- generic FCA begins after `I` and cannot manufacture `I`;
- a carrier contact relation does not become native `K` by notation;
- a role-tagged union is not a conversion because deleting the role tag destroys recoverability;
- SIG3 and SIG4 do give exact conversions because their added laws are explicit and checker-verifiable.

This separates semantic authorization from downstream mathematics.

## 7. Downstream interface

### Packing

Once `X` is natively typed, define the conflict graph `G_X=(C,X)` and only then invoke independent-set, matching, spectral, periodic or packing machinery. `K` alone does not authorize `G_X`.

### Mahler/FCA

Once `I subset C×S` is natively typed, standard derivation operators and Galois/FCA closure become available. Those are classical after the incidence is supplied. Neither a self-dual identification nor a Mahler geometric interpretation follows from `I` alone.

### Contact/readout

Once `K` is supplied or derived, native contact neighborhoods/readout constraints may be formulated. FCC/HCP first-shell contact remains comparison evidence rather than an identity theorem for `K`.

### Shared witness extension

If SIG2 is later authorized, all three downstream adapters are exact projections of `J`, with the role map retained in every certificate. This can reduce ontology fan-out without falsely equating the selectors.

## 8. Equivariance and refinement obligations

The relation core must be compatible with whatever native automorphism action is actually accepted. The finite witness bank already shows that equivariance alone does not force conversions.

For any future physical refinement `r_C:C'->C` and support refinement `r_S:S'->S`, a successor must explicitly choose and prove one of:

- exact pullback;
- exact pushforward;
- one-sided monotonicity;
- or a separately typed transport relation.

No such refinement law is smuggled into this Result. This respects the accepted current-language no-model-change-arrow boundary.

## 9. Tool reuse

No new general-purpose tool is proposed.

The execution reuses the accepted enterprise boundaries:

- `T7_FINITE_SYMMETRY_EQUIVARIANCE` for the nontrivial `C4` equivariance audit and canonical-choice discipline;
- `T8_RELATION_OBSERVABLE_SPECTRUM` as the declared-relation analysis boundary: once a relation exists it can be analyzed, but the tool does not choose or invent the semantic relation.

The deterministic checker is task-local evidence, not a new toolbox family.

## 10. Verification

Task-local checker:

`python research_checks/GEO6_NATIVE_RELATION_SELECTOR_CORE_CHECK_20260901.py`

Expected and reproduced output:

`PASS equivariant_nonimplications=6 exhaustive_triples=4096 independent_bits_n3_m2=12 pair_local_alphabet_min=4 incidence_local_alphabet_min=2 signature_classes=5 selfdual_roundtrip=8 support_overlap_collision=1`

The machine-readable theorem/countermodel atlas is frozen at:

`research_artifacts/GEO6_NATIVE_RELATION_SELECTOR_CORE/TYPED_RELATION_CORE_CERTIFICATE.json`.

## 11. Residue and Driver handoff

The task is terminally classified, but the parent GEO6 objective remains open.

What remains is an **ontology choice/derivation problem**, not a missing finite relation theorem:

- current P000 does not yet derive `K`, `X`, `I`, SIG2 witness incidence, SIG3 self-duality, or SIG4 support-overlap conflict semantics;
- any future adoption must be justified by native P000 structure and reviewed at its exact type strength;
- if the Driver wants one shared relation primitive without false selector equivalence, SIG2 is the smallest genuine common-mechanism candidate identified here;
- if no such extra native structure is justified, SIG0 is the exact safe interface and the three selectors remain independent.

Recommended Driver disposition:

`ACCEPT / EXACT_RELATION_SELECTOR_BOUNDARY`.

Do not publish a successor merely to rename SIG0 or SIG1. Reopen relation-core mathematics only if new accepted P000 data supplies a concrete native relation, a self-dual Cell↔Support map, a support-overlap conflict law, or a smaller typed witness mechanism that beats the lower bound without collapsing selector distinctions.

No Working Truth, Foundation, canonical native-geometry promotion, classical theorem transfer, or novelty certificate is granted.
