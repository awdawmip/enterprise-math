# CBRC F0 Native Recoalescence Forward Derivation — Return

Status: `PHASE_A_RAW_PACKET / BLIND_FORWARD`
Date: `2026-08-22`
Researcher-ID: `EM-CBRCF0-4E91C7`
Task-ID: `RS-CBRC-F0-NATIVE-RECOALESCENCE-FORWARD-DERIVATION`
Taskbook source: `b3ae07ca418d3e747d3b58bf8e6e2c8ab256dd7a`
Owner branch: `research/cbrc-f0-native-recoalescence-forward-derivation`
Frozen issue base: `enterprise-math/main@18260c780295edabbaaca746e5210478a1d98180`

## 0. Primary verdict

`F0_UNDERDETERMINED_BY_CURRENT_FOUNDATION`

Top-level classification:

`NO_GO_OR_UNDERDETERMINED`

Hard target:

`NATIVE_RECOALESCENCE_MINIMAL_EXTENSION_CLASSIFIED = YES`

Meaning:

1. the native local support is exactly classifiable;
2. current Path/N/Boolean coefficient semantics cannot produce exact nonempty cancellation;
3. the minimal **conservative** cancellation-capable coefficient extension is forced by a universal group-completion property;
4. reversible path-wise sign transport on that minimal carrier is completely classifiable by a native diamond-curvature field up to gauge;
5. the current Foundation does **not** select that field, and full refinement naturality excludes genuine nontrivial branch mixing on the minimal carrier;
6. the stated readout axioms do **not** select a unique scalar law: at least two exact inequivalent laws survive all required tests.

Therefore current native BRC does not uniquely force a coherent recoalescence dynamics/readout pair. The correct F0 result is a classified minimal carrier plus a classified family/independence result, not a downstream target algebra.

Secondary tags:

- `LOCAL_NATIVE_RECOALESCENCE_SUPPORT_CLASSIFIED`
- `CURRENT_BRC_CANCELLATION_NO_GO`
- `CONSERVATIVE_SIGNED_GROUP_COMPLETION_MINIMAL`
- `LOCAL_REVERSIBLE_RECOALESCENCE_GAUGE_FAMILY_CLASSIFIED`
- `GENUINE_BRANCH_MIXING_NO_GO_ON_MINIMAL_CARRIER`
- `RECOALESCENCE_READOUT_UNDERDETERMINED`
- `MINIMAL_NATIVE_DARK_FIBER_DISCRIMINATOR_EXISTS_IN_EXTENSION`
- `TARGET_LEAK_AUDIT_PASS`

## 1. Frozen Phase-A sources

Mathematical input was restricted to the four taskbook-whitelisted files at the frozen issue base.

| Source | Blob SHA |
|---|---|
| `definitions/00_CURRENT_NATIVE_FOUNDATION.md` | `c3140417e061932b4415f86cad397fc2de91d3c2` |
| `definitions/ENTERPRISE_THREE_POSITIVE_AXIS_OVERLAPPING_CIRCLE_CELL_PLANE_20260820.md` | `393060ebfd6a86ad45f258747d78a14d9c8ac153` |
| `definitions/ENTERPRISE_NATIVE_LINE_TRACE_FORMULA_20260821.md` | `b631242db84c5bd3640e6dc554b19a1d04d464f3` |
| `definitions/ENTERPRISE_BRC_MULTIPATH_ENRICHMENT_BRIDGE_20260821.md` | `6ec0d73a19e28ec586c59a97d24f5798c9119771` |

No R063/R064 result, downstream coherent-BRC result, external quantum/wave formalism, Hodge result, or Shor result was read or used in Phase A.

## 2. Native replay

Fix a translated native sector `S_ij(P)` and trace `T_{P;a,b}^{(ij)}`.

The whitelist gives:

- instantaneous state = one circle cell;
- triple intersections = incidence/transition events, not simultaneous three-cell states;
- active trace generators = exactly `X_i, X_j`;
- a path witness retains its generator word and typed placement/terminal;
- `X_i X_j` and `X_j X_i` are distinct concrete single-cell paths with the same typed terminal in the minimal `(1,1)` commuting diamond;
- Path-formal/N/Boolean collapse for that diamond is `2 -> 2 -> 1`.

No same-terminal multiplicity exists at trace depth one. Hence `(1,1)` at depth two is the smallest same-terminal native multipath witness.

## 3. F0-Q1 — exact local incidence / branch arity

### Definition 3.1 — residual typed forward support

Let a prefix word `w` of `T_{P;a,b}^{(ij)}` contain `x` copies of `X_i` and `y` copies of `X_j`.
Its current single-cell state is

`c(P,ij;x,y)`.

Define residual counts

`r_i=a-x`, `r_j=b-y`.

The admissible next-cell support is

`B(w) = { c(P,ij;x+1,y) if r_i>0 } union { c(P,ij;x,y+1) if r_j>0 }`.

Therefore

`|B(w)| = 1_[r_i>0] + 1_[r_j>0]`.

### Theorem 3.2 — `LOCAL_NATIVE_RECOALESCENCE_SUPPORT_CLASSIFIED`

At a geometric triple-intersection event there are three incident cells, but a fixed typed forward trace does **not** create a simultaneous ternary native state.

Conditioned on:

- the current cell,
- sector/component labels `(ij)`,
- the target component trace,
- the current prefix counts,

the forward support arity is exactly:

- `2` if both residual components are positive;
- `1` if exactly one residual component is positive;
- `0` at the trace terminal.

For the minimal `(1,1)` trace, the start support has arity `2`, each one-step continuation has arity `1`, and the common terminal has arity `0`.

### Proof

The allowed line language contains only the two positive component generators `X_i,X_j`. A next trace step can only increment one still-unfinished component count by one. The third carrier-family shortcut is explicitly excluded from native line membership by the whitelist. The one-cell state rule forbids representing the three incident geometric cells as a simultaneous state. The displayed support therefore lists all and only native trace continuations. QED.

### Proposition 3.3 — coarse cell is enough for support but not for reversible recoalescence

Given `(P,ij,T_{a,b})` and the current addressed cell, the residual component counts determine the next support; full word provenance is not required merely to know which next cells are allowed.

However, coarse current-cell state is insufficient for an information-preserving recoalescence rule. In the `(1,1)` diamond,

`p = X_i X_j`,
`q = X_j X_i`

are distinct Path-formal witnesses but reach the same typed terminal cell. Any state map that keeps only that terminal cell identifies `p` and `q`, hence is at least `2 -> 1` on this fiber and cannot be inverted.

Thus provenance is not required for forward **support selection**, but is required for reversible pre-collapse **state identity**.

## 4. F0-Q2 — cancellation capability and the minimal conservative extension

### Theorem 4.1 — `CURRENT_BRC_CANCELLATION_CAPABILITY_CLASSIFIED`

The current coefficient tower cannot represent a nonempty same-terminal family whose scalar additive aggregate is zero while each participating branch is nonzero.

#### N layer

For nonnegative integers,

`n_1 + ... + n_k = 0`

implies every `n_i=0`.

Hence the N coefficient monoid is conical: nonzero positive occurrences cannot exactly cancel.

#### Boolean layer

Recoalescence is support union / Boolean OR. The OR of one or more nonzero supports is nonzero.

#### Path-formal layer

Path-formal BRC uses finite formal **N**-sums of concrete path witnesses. It retains provenance, but its coefficients are still nonnegative. Terminal summation of nonzero path coefficients therefore cannot vanish.

QED.

### Definition 4.2 — conservative extension order

Call a coefficient extension conservative when:

1. it contains the existing nonnegative coefficient monoid injectively;
2. old finite sums remain distinct exactly as before;
3. addition extends the old addition;
4. typed concatenation can still be extended compositionally.

This rules out quotient tricks that make an old multiplicity vanish.

### Theorem 4.3 — minimal universal cancellation carrier

Under the conservative-extension order, exact cancellation forces the additive group completion of the existing coefficient monoid.

At the scalar coefficient level, the submonoid generated by one elementary occurrence is `N`. Any conservative additive carrier in which that occurrence has an additive inverse must contain the infinite cyclic group generated by it. There is a unique additive map from the group completion extending the original inclusion. Thus the minimal universal scalar carrier is the additive group generated by one occurrence, canonically represented by integer coefficients.

At the Path-formal level, because concrete path witnesses are retained independently, the same construction is performed basiswise:

`finite N-sums of [p]  ->  finite signed integer sums of [p]`.

Equivalently, the minimal additive carrier is the free additive group on typed concrete path witnesses.

Typed concatenation extends uniquely by distributivity from basis-path concatenation. This multiplication is a consequence of composition compatibility; no coefficient ring/field was assumed in advance.

### Minimality proof

A smaller quotient such as parity arithmetic can make two nonzero occurrences sum to zero, but it identifies the old multiplicity `2` with `0`. It therefore violates conservative extension and refinement/no-resurrection requirements.

Any conservative cancellation carrier must contain an additive inverse of the embedded elementary generator and therefore an embedded infinite cyclic subgroup. The group completion is initial among all such additive-group targets. No strictly smaller conservative additive completion can satisfy the requirement.

### No resurrection

The signed carrier is constructed only from Path-formal data **before** applying the forgetful maps. It is not reconstructed from N or Boolean output.

- Path-formal: full typed path word/prefix/terminal survives.
- N: only multiplicity survives.
- Boolean: only support survives.

Once Path-formal provenance is forgotten, no sign assignment to individual paths is recoverable from N/Boolean without a new primitive. The F0 construction never performs such an inversion.

## 5. F0-Q3 — local reversible recoalescence classification

The minimal signed carrier supplies additive inverses, but does not itself select how signs are transported along native path edges.

### Definition 5.1 — reversible unit transport

On each typed generator edge from prefix `(x,y)`, attach an additive automorphism of the signed scalar carrier.

The only additive automorphisms of the infinite cyclic scalar carrier are multiplication by `+1` or `-1`.

Write

- `u_i(x,y) in {+1,-1}`,
- `u_j(x,y) in {+1,-1}`.

A concrete path receives the product of the edge units along that path.

Because multiplication by a unit is invertible and the concrete path basis is retained, this transport is pre-collapse information preserving.

### Definition 5.2 — vertex gauge

A gauge is a choice `g(x,y) in {+1,-1}` at each prefix vertex. It transforms edge units by endpoint sign transport:

`u_i'(x,y)=g(x,y) u_i(x,y) g(x+1,y)^(-1)`

and similarly for `u_j`.

This changes presentation but not relative path transport around a commuting diamond.

### Definition 5.3 — diamond curvature

For the elementary native commuting diamond at prefix `(x,y)`, define

`kappa(x,y) = [u_i(x,y) u_j(x+1,y)] / [u_j(x,y) u_i(x,y+1)]`.

Because every unit is `+1` or `-1`, `kappa(x,y)` has exactly those two possible values.

It is gauge invariant.

### Theorem 5.4 — gauge classification of path-wise reversible local laws

On the simply connected positive two-generator prefix grid, two unit-transport assignments are gauge equivalent iff they have the same diamond-curvature field `kappa(x,y)`.

#### Proof sketch

Fix one base vertex gauge. Recursively choose gauges along a spanning tree so that all tree-edge units agree between the two assignments. For each remaining edge, the unique elementary-loop curvature equality forces agreement as well. Conversely, gauge transformations cancel around every elementary diamond, so curvature is invariant. QED.

Thus all path-wise reversible scalar recoalescence laws on the minimal carrier are classified, up to gauge, by a two-valued sign on each elementary commuting diamond, subject only to whatever extra covariance/homogeneity constraints are separately imposed.

Absolute translation of native placement `P` does not change this relative-prefix field. Cyclic sector transport copies the same classification to `S_23` and `S_31`. Swapping active generator names transports `(x,y)` to `(y,x)` and sends curvature to its inverse; for a sign-valued curvature the inverse equals itself. Physical classes are therefore curvature fields modulo the coordinate-swap transport.

### Corollary 5.5 — exact local dark-diamond condition

For the two routes across one commuting diamond, their coefficient ratio is exactly `kappa(x,y)`.

If each branch coefficient is a nonzero unit, the same-terminal scalar aggregate is zero iff

`kappa(x,y) = -1`.

Therefore exact cancellation on **every** elementary commuting diamond is one gauge class:

`kappa(x,y) == -1` for all `(x,y)`.

A canonical representative of the constant class is

- `u_j(x,y)=1`,
- `u_i(x,y)=kappa^y`.

Then a path word `w` has weight

`kappa^(inv(w))`

where `inv(w)` is the number of prior `X_j` letters crossed by later `X_i` letters.

For `kappa=-1`, the two `(1,1)` words have weights `+1` and `-1`.

The checker verifies the exact composition identity

`weight(wv)=weight(w) weight(v) kappa^(b*c)`

for prefixes with component counts `(a,b)` and suffix counts `(c,d)`, through total path depth four. The correction exponent is derived from counting cross-order pairs and satisfies associativity.

### Important underdetermination

The whitelist does not select a curvature field.

- `kappa=+1` is the flat constructive class.
- `kappa=-1` is the uniformly dark commuting-diamond class.
- provenance-dependent nonconstant fields are also compatible with typed locality because provenance is explicitly retained.

If the **extra operational demand** is “every native commuting diamond must cancel”, that demand selects `kappa=-1`. The native Foundation itself does not.

### Theorem 5.6 — genuine branch-mixing no-go on the minimal carrier

Consider a two-branch signed coefficient vector and a local integer-linear reversible update `U` that is representation-independent under swapping the two branch serializations.

Exact equivariance gives `UP=PU` for the swap matrix `P`. Therefore

`U = [[a,b],[b,a]]`.

Reversibility over the minimal integer carrier requires determinant `+1` or `-1`:

`det(U)=(a-b)(a+b)=±1`.

Both integer factors must be `+1` or `-1`, giving only

`+I, -I, +P, -P`.

These are global sign and/or branch permutation, not genuine mixing.

Under full finite refinement naturality the restriction is stronger. A natural endomorphism of the free signed branch carrier with respect to every refinement/forgetful set map is fixed by its value on a singleton. Singleton injections force the map on every basis vector to be the same scalar multiple. Reversibility then leaves only `±I`.

Hence `NONTRIVIAL_MIXING` is impossible on the minimal conservative carrier if branch relabeling and full finite refinement naturality are enforced.

Nonclassical cancellation remains possible through path-wise reversible sign transport plus final same-terminal aggregation; genuine branch mixing would require an additional coefficient or branch-structure primitive not supplied by current native BRC.

`LOCAL_REVERSIBLE_RECOALESCENCE_FAMILY_CLASSIFIED = YES`.

## 6. F0-Q4 — scalar readout classification

A crucial typing boundary is required.

Before final collapse, the state is the full signed Path-formal sum

`z = sum_p n_p [p]`.

For one same-terminal fiber define the irreversible terminal aggregation

`A(z)=sum_p n_p`.

This map can cancel and is not injective; it is therefore part of the declared final recoalescence/readout boundary, not an information-preserving pre-collapse update.

### Tagged readout

For explicitly distinguishable path markers, define a tagged total by adding branch readouts:

`D_f(z)=sum_p f(|n_p|)`.

This directly satisfies `DISTINGUISHABLE_SUM_ADDITIVITY`.

Path-wise unit transport changes only coefficient signs, so it preserves `|n_p|` and hence conserves `D_f` during reversible pre-collapse evolution.

### Recoalesced scalar readout

After same-terminal marker erasure/aggregation, let

`R_f(z)=f(|A(z)|)`,

where `f(0)=0`, `f(n)>0` for `n>0`, `f(1)=1`, and the composition-scaling requirement is satisfied whenever

`f(mn)=f(m)f(n)`.

Finite refinement followed by forgetting is presentation independent because the aggregate `A(z)` is unchanged by splitting/merging explicit markers that preserve the signed sum.

### Theorem 6.1 — `RECOALESCENCE_READOUT_LAW_CLASSIFIED`

The taskbook's minimum operational axioms do not force a unique scalar readout.

Two exact inequivalent models are:

1. `f_1(n)=n`, giving `R_1(z)=|A(z)|`;
2. `f_2(n)=n^2`, giving `R_2(z)=A(z)^2`.

Both are:

- zero-definite;
- positive on a nonzero elementary witness;
- branch-relabeling invariant;
- additive on explicitly distinguished alternatives via `D_f`;
- conserved by reversible `±1` path transport at the tagged pre-collapse level;
- multiplicative under independent integer composition;
- consistent under finite refinement followed by the same forgetful aggregation.

They disagree already at aggregate `2`:

`R_1(2)=2`, `R_2(2)=4`.

Therefore uniqueness is disproved.

The underdetermination is larger than a single power exponent: any positive normalized completely multiplicative function on positive integers gives another exact scalar countermodel under the stated discrete requirements.

### Weakest additional selector justified in F0

A minimal operational strengthening that does not import a target algebra is:

`SAME_SIGN_MARKER_ERASURE_INVARIANCE`:

> if finitely many explicitly distinguished elementary alternatives all carry the same sign and terminal type, erasing only their distinguishing markers does not change scalar readout.

Together with tagged additivity, elementary normalization, and gauge sign invariance, this forces

`R(n)=|n|`

on the integer aggregate.

The square model fails this extra axiom because two same-sign tagged unit alternatives have tagged readout `2` but untagged square readout `4`.

No native source supplies this extra axiom, so it is not adopted as Foundation truth in F0. In particular, no square/power exponent is imported or selected.

## 7. F0-Q5 — minimal native dark-fiber discriminator

Use the whitelist-minimal same-terminal fiber

`p=X_iX_j`,
`q=X_jX_i`.

Both are individually nonzero typed Path-formal witnesses and have the same typed terminal.

On the signed extension:

### Constructive presentation

`z_+ = [p] + [q]`.

Terminal aggregate:

`A(z_+)=2`.

Readouts:

- absolute model: `2`;
- square model: `4`.

### Dark presentation

`z_- = [p] - [q]`.

Terminal aggregate:

`A(z_-)=0`.

Both individual branches remain nonzero before aggregation; native support is unchanged.

Readout is `0` in both exact models.

This sharply separates:

- Boolean support: still nonempty;
- N multiplicity: still `2` before signed extension;
- signed Path-formal aggregate: can be zero only at the declared final aggregation.

At the minimal normalized two-branch fiber, integer-unit coefficients permit aggregate values only `-2,0,2`. Hence there is no strictly positive intermediate reduction between constructive magnitude `2` and dark `0` without introducing nonunit magnitudes or a richer carrier. The exact dark case is already a strict reduction and is the smallest discriminator.

`MINIMAL_NATIVE_DARK_FIBER_DISCRIMINATOR = (1,1) COMMUTING DIAMOND`.

## 8. Counterfactual ablation summary

| Removed requirement | What ceases to be forced |
|---|---|
| pre-collapse information preservation | conservative embedding/minimal group completion; a parity quotient can cancel while destroying old multiplicity/provenance |
| branch relabeling equivariance | sign/transport assignments may depend on arbitrary serialization names; curvature no longer represents a physical class |
| local conservation | reversible steps may carry arbitrary readout rescalings; scalar classification widens |
| refinement consistency | duplication/parity-sensitive quotients become admissible; the refinement-natural mixing no-go disappears |
| nontrivial mixing | no loss of dark-fiber capability; diagonal reversible sign transport is already sufficient |
| exact cancellation/dark-fiber requirement | no signed coefficient extension is required at all; the original Path/N/Boolean tower suffices for provenance/multiplicity/support |

Full countermodels are in `research_reports/CBRC_F0_ABLATION_AND_COUNTERMODEL_PACKET_20260822.md`.

## 9. Required proof obligations

### P1 Source replay
PASS — `(1,1)` commuting diamond replayed directly from the whitelist.

### P2 No resurrection
PASS — all signed enrichment occurs before N/Boolean forgetting; discarded path data are never reconstructed.

### P3 Universality/minimality
PASS for the conservative coefficient extension — additive group completion is initial/minimal. Genuine dynamic/readout completion is not unique, and is reported as such rather than overclaimed.

### P4 Choice independence
PASS at classification level — absolute translation, generator relabeling, branch serialization swap, and cyclic sector transport act by explicit transport/gauge on the curvature family.

### P5 Associativity/composition
PASS — path edge multiplication is associative; the canonical constant-curvature representative obeys the exact twisted concatenation identity and the checker verifies all cases through depth four.

### P6 Positive/readout safety
PASS for the declared readout models — outputs are nonnegative and zero-definite on the domain.

### P7 Countermodels
PASS — readout uniqueness is refuted by two exact inequivalent models; all mandatory ablations have explicit smallest countermodels.

### P8 Target leak audit
PASS — see dedicated audit report.

## 10. Checker

Required path:

`scripts/cbrc_f0_validate_native_recoalescence_forward.py`

Command:

`python3 scripts/cbrc_f0_validate_native_recoalescence_forward.py`

Deterministic result digest:

`362738cc8a1a0f87c291d897308c4476e385c3266240f1f8b598cda1c50194ca`

Regression summary:

- minimal same-terminal words: `ij`, `ji`;
- path/N/Boolean: `2 -> 2 -> 1`;
- exact residual support arities reproduced;
- exhaustive `S_2` relabel transport through total depth four;
- exact twisted-composition cases through depth four: `258`;
- relabeling cases: `62`;
- integer relabeling-equivariant unimodular 2x2 candidates in `[-4,4]`: exactly `4` (`±I, ±swap`);
- constructive minimal aggregate: `2`;
- dark minimal aggregate: `0`;
- both readout countermodels checked for zero-definiteness and composition scaling on the declared finite window;
- all six ablation countermodels replayed;
- mismatch count: `0`.

Enumeration is regression evidence only; the infinite/minimality statements above are theorem arguments.

## 11. Definitions introduced in F0

1. `RESIDUAL_TYPED_FORWARD_SUPPORT`.
2. `CONSERVATIVE_COEFFICIENT_EXTENSION`.
3. `SIGNED_PATH_GROUP_COMPLETION`.
4. `REVERSIBLE_UNIT_EDGE_TRANSPORT`.
5. `VERTEX_SIGN_GAUGE`.
6. `NATIVE_DIAMOND_CURVATURE kappa`.
7. `SAME_TERMINAL_SIGNED_AGGREGATION A`.
8. `TAGGED_PRECOLLAPSE_READOUT D_f`.
9. `RECOALESCED_SCALAR_READOUT R_f`.
10. `SAME_SIGN_MARKER_ERASURE_INVARIANCE` (counterfactual selector only; not adopted).

Every introduced object is traced to a specific F0 requirement in the target-leak audit.

## 12. Unresolved assumptions / exact boundary

1. The native sources do not select a curvature field `kappa(x,y)`.
2. If “exact cancellation” is required only for the first `(1,1)` diamond, later diamond curvatures remain free.
3. If cancellation is required uniformly on every elementary commuting diamond, `kappa==-1` is forced up to gauge, but that uniform dark-diamond requirement is an extra operational condition, not a source theorem.
4. The current readout axioms do not select a unique scalar function.
5. Full refinement naturality prevents genuine branch mixing on the minimal integer carrier; richer mixing requires extra structure and is not classified as native.
6. The F0 result is sector-local with only the cyclic covariance required by the taskbook; no global cross-sector process is claimed.
7. No Foundation promotion is authorized by this packet.

## 13. Final hard-target statement

`LOCAL_NATIVE_RECOALESCENCE_SUPPORT_CLASSIFIED = true`

`CURRENT_BRC_CANCELLATION_CAPABILITY_CLASSIFIED = true`

`LOCAL_REVERSIBLE_RECOALESCENCE_FAMILY_CLASSIFIED = true`

`RECOALESCENCE_READOUT_LAW_CLASSIFIED = true`

`MINIMAL_NATIVE_DARK_FIBER_DISCRIMINATOR = true`

`TARGET_LEAK_AUDIT_PASS = true`

`NATIVE_RECOALESCENCE_MINIMAL_EXTENSION_CLASSIFIED = true`

Primary verdict remains:

`F0_UNDERDETERMINED_BY_CURRENT_FOUNDATION`
