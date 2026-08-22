# CBRC F1 — Non-Sign Recoalescence Carrier Forward Classification Return

Status: `RAW PHASE-A PACKET / BLIND-FORWARD / FROZEN-CANDIDATE`

Date: `2026-08-22`

Researcher-ID: `EM-CBRCF1-8D27A4`

Task-ID: `RS-CBRC-F1-NONSIGN-RECOALESCENCE-CARRIER-FORWARD-CLASSIFICATION`

Owner branch:

`research/cbrc-f1-nonsign-recoalescence-carrier-forward-classification`

Taskbook source commit:

`e279377a6578ac9adb93c2c21d52b31c569bae20`

Taskbook blob SHA:

`684be33edff6c22882cb5659b67829ae50aa665d`

Primary verdict:

`F1_UNIQUE_MINIMAL_NONSIGN_CARRIER`

Hard target:

`NONSIGN_RECOALESCENCE_MINIMAL_CARRIER_CLASSIFIED = true`

## 0. Executive result

Starting only from the permitted native/BRC semantics and the two explicitly authorized F0 inherited facts,

1. the minimal conservative exact-cancellation coefficient is the signed rank-one additive layer;
2. its rank-one reversible scalar automorphisms are exactly `+1` and `-1`;

the first genuinely non-sign finite reversible transport is **not forced to increase the torsion-free additive rank**.

The unique least carrier in the declared rank-primary extension order is

`C_min = Z e ⊕ <tau | 3 tau = 0>`,

with the old signed layer embedded as

`i(n)=n e`

and forgotten by

`pi(n e + a tau)=n`.

A minimal non-sign transport is

`R(e)=e+tau`,
`R(tau)=tau`.

Hence

`R^3=id`

and the elementary occurrence has the exact orbit

`e -> e+tau -> e-tau -> e`.

The two raw choices `tau` and `-tau` are equivalent by the unique branch-reversal involution

`S(e)=e`,
`S(tau)=-tau`,

which satisfies

`S R S^{-1}=R^{-1}`.

Therefore the minimal **physical carrier/transport class is unique** after branch-role/orientation choice independence.

The old sign involution `J=-id` is not a power of `R`; it survives as an independent central operation. Exact signed dark cancellation is therefore preserved, not replaced.

No scalar readout is selected in F1.

No internal coefficient multiplication is required for path composition. In fact, if one insists that the old coefficient `e` remain a two-sided multiplicative unit and that `R` be multiplicative, there is no associative product on `C_min`. If two-sided unitality is dropped, exactly two directed associative products survive, exchanged by reversal. Thus a ring structure is not intrinsic to F1.

A crucial counterfactual is also classified: **if a new torsion-free axiom were added**, the minimal free rank would become `2`, and the primitive orbit-generated finite-order integral transports would have exactly the three derived characteristic polynomials

`x^2+x+1`,
`x^2+1`,
`x^2-x+1`

with orbit/orders `3,4,6` respectively.

That torsion-free classification is a counterfactual only. It is not the F1 answer under the issued constraints.

---

## 1. Exact frozen inputs

### 1.1 Taskbook

- source commit: `e279377a6578ac9adb93c2c21d52b31c569bae20`
- blob SHA: `684be33edff6c22882cb5659b67829ae50aa665d`

### 1.2 Original native/F0 whitelist definitions

Read at the F0 frozen base snapshot `18260c780295edabbaaca746e5210478a1d98180`:

1. `definitions/00_CURRENT_NATIVE_FOUNDATION.md`
   - blob SHA `c3140417e061932b4415f86cad397fc2de91d3c2`
2. `definitions/ENTERPRISE_THREE_POSITIVE_AXIS_OVERLAPPING_CIRCLE_CELL_PLANE_20260820.md`
   - blob SHA `393060ebfd6a86ad45f258747d78a14d9c8ac153`
3. `definitions/ENTERPRISE_NATIVE_LINE_TRACE_FORMULA_20260821.md`
   - blob SHA `b631242db84c5bd3640e6dc554b19a1d04d464f3`
4. `definitions/ENTERPRISE_BRC_MULTIPATH_ENRICHMENT_BRIDGE_20260821.md`
   - blob SHA `6ec0d73a19e28ec586c59a97d24f5798c9119771`

### 1.3 F0 inheritance boundary actually used

The current research handoff explicitly restricted usable F0 conclusions to:

`F0-I1` — the minimal conservative cancellation carrier is the sign-only signed layer;

`F0-I2` — reversible scalar transport on its rank-one generated coefficient carrier is only `±1`.

Provenance reference named by the F1 taskbook:

`research/cbrc-f0-native-recoalescence-forward-derivation@501ab10b868f27a8468b1c0863d4435153ba4a2b`.

No other F0 theorem is used as a premise in this report.

The F0 Driver review commit named by the taskbook,

`d4c7dd11287b313360be9e53a5bad5dfd7f1b502`,

was not used as a mathematical source beyond the taskbook's declaration that F0 was accepted.

### 1.4 Blindness statement

Before this raw packet freeze, this research did not load or use:

- R063 mathematical results;
- R064 mathematical results;
- R065 mathematical results;
- downstream coherent-BRC/wave free-research results;
- Hodge/Shor route results;
- external quantum/wave/amplitude/Hilbert/path-integral/gauge/readout formalisms.

No target coefficient ring, phase group, complex structure, root of unity, positive form, transform matrix, or readout law was preselected.

---

## 2. Native typed support replay needed by F1

The native plane has one circle cell as the instantaneous state. Triple intersections are incidence/transition events, not simultaneous three-cell states.

For a fixed native sector `S_ij`, line identity is the component trace

`T_{a,b}^{(ij)}=[X_i^a X_j^b]`

under adjacent `X_i X_j ~ X_j X_i` commutation.

The smallest same-terminal native multipath witness is therefore the typed `(1,1)` commuting diamond:

`p = X_i X_j`,
`q = X_j X_i`.

The two paths are distinct concrete Path-formal witnesses and share the same typed terminal.

This is the only native branch object needed in F1. No third-family carrier shortcut is admitted as a member of the same native trace.

---

## 3. F1-Q1 — rank-one no-go and extension order

### Definition 3.1 — old signed coefficient

Write the accepted F0 signed scalar generator as `e`.

Its additive carrier is

`C_0 = Z e`.

The old sign involution is

`J(n e)=-n e`.

### Theorem 3.2 — rank-one torsion-free non-sign no-go

Every additive automorphism of `Z e` is `+id` or `-id`.

#### Proof

An additive endomorphism is determined by

`e -> k e`

for one integer `k`.

It is invertible iff multiplication by `k` is bijective on `Z`, hence iff

`k=±1`.

Therefore the orbit of `e` under any reversible scalar transport has size at most `2`.

So `NONSIGN_REVERSIBLE_TRANSPORT_EXISTS` fails on the F0 carrier itself. ∎

This independently replays the minimum amount of F0-I2 required by the taskbook.

### Definition 3.3 — weak conservative extension

A weak conservative additive extension consists of an injective group homomorphism

`i: Z e -> C`

with `C` finitely generated abelian.

### Definition 3.4 — refinement-compatible conservative extension

For F1 path refinement, an enrichment must also be forgettable back to the exact F0 coefficient without changing the old signed coefficient.

Therefore define a refinement-compatible conservative extension by an additive retraction

`pi:C->Z e`

such that

`pi i = id`.

A local transport `R` is F0-compatible when

`pi R = epsilon pi`

with `epsilon in {+1,-1}`.

This is not a readout. `pi` forgets only the F1 enrichment and returns the pre-existing F0 signed coefficient.

The least carrier found below satisfies this stronger condition, so the result does not rely on weakening conservativity to mere injection.

### Lemma 3.5 — exact dark preservation is redundant

Once `i:Z e->C` is a group embedding and `R` is additive,

`i(e)+i(-e)=0`

and

`R(i(e))+R(i(-e))=R(0)=0`.

Hence the separate clause "embedded additive inverse remains available" is logically redundant under conservative group embedding plus additive transport.

It remains useful as an audit condition, but it adds no new mathematical restriction.

### Definition 3.6 — rank-primary extension complexity

For an admissible quadruple

`X=(C,i,pi,R)`

define the complexity tuple

`K(X)=(r,g,q,h,o,m)`,

where:

- `r = rank_Z(C/tors(C))`;
- `g =` minimum number of new additive generators required for `ker(pi)`;
- `q =` minimum number of defining additive relations on those new generators;
- `h = |tors(ker(pi))|` when the kernel is finite, and `infinity` otherwise;
- `o = |Orbit_R(i(e))|`;
- `m = 0` if composition needs only an external additive-automorphism action, `m = 1` if an internal coefficient multiplication is additionally chosen.

The order is **rank-primary lexicographic**:

first minimize `r`, then `g`, then `q`, then `h`, then `o`, then `m`.

Why rank is primary is not arbitrary: F1-Q2 explicitly asks for the smallest additive rank first.

Injectivity of `i` and the retraction equation `pi i=id` are admissibility gates, not optional complexity coordinates.

This order considers every quantity required by the taskbook and adds finite-kernel size `h` only to distinguish carriers with the same generator/relation counts.

Deliverable:

`RANK_ONE_NONSIGN_NO_GO_AND_EXTENSION_ORDER = CLASSIFIED`.

---

## 4. F1-Q2 — complete rank-one split classification

### Theorem 4.1 — rank-one refinement-compatible normal form

Let `(C,i,pi)` be a refinement-compatible conservative extension with torsion-free rank `1`.

Then

`C = Z e ⊕ T`

where `T=ker(pi)` is a finite abelian group.

Every F0-compatible additive automorphism `R` has the form

`R(e)=epsilon e + a`,
`R(t)=phi(t)` for `t in T`,

where

`epsilon in {+1,-1}`,
`phi in Aut(T)`,
`a in T`.

Conversely, every such triple `(epsilon,phi,a)` defines an additive automorphism compatible with the F0 projection.

#### Proof

Because `pi i=id`, `i(Z e)` is a direct summand of `C`.

Since the torsion-free rank is one, the complementary kernel has rank zero and is finite, hence `T=ker(pi)`.

For torsion `t`, any homomorphism `T->Z` is zero, so F0 compatibility implies `R(T)=T`.

The induced automorphism on the free quotient `C/T ~= Z` is multiplication by `epsilon=±1`.

Thus `R(e)-epsilon e` lies in `T`; call it `a`. The restriction to `T` is an automorphism `phi`.

The converse is immediate from the displayed formula. ∎

### Corollary 4.2 — all rank-one finite transport families are torsion-sheet families

At torsion-free rank one, genuinely non-sign behavior can occur only through `T`.

The iteration on the elementary occurrence is

`R^k(e)
 = epsilon^k e
 + sum_{j=0}^{k-1} epsilon^{k-1-j} phi^j(a)`.

Because `T` is finite and `Aut(T)` is finite, every such rank-one automorphism has finite order.

Thus the F1 finite-orbit condition introduces no extra hidden continuum at rank one.

### Proposition 4.3 — no kernel of size below three can work

`T=0` is the rank-one F0 no-go.

If `|T|=2`, then `T` has one nonzero element and `Aut(T)` is trivial.

The possible free quotient action is `epsilon=±1`; direct iteration gives elementary orbit size at most `2`.

Therefore any rank-one non-sign refinement-compatible carrier must have

`|T| >= 3`.

### Theorem 4.4 — unique least rank-one non-sign carrier

Take one new torsion generator `tau` with the single relation

`3 tau = 0`.

Set

`C_min = Z e ⊕ <tau | 3 tau=0>`,

`pi(n e + a tau)=n e`.

Define

`R(e)=e+tau`,
`R(tau)=tau`.

Then:

1. `R` is additive and invertible;
2. `R^3=id`;
3. `R != ±id`;
4. `Orbit_R(e)={e,e+tau,e-tau}` has size `3`;
5. `pi R = pi`;
6. `J=-id` remains available and central;
7. exact signed cancellation is preserved.

No admissible carrier has a smaller rank, fewer new generators, fewer relations with the same rank, smaller finite kernel capable of orbit `>2`, or smaller allowed orbit.

Up to an automorphism fixing the old `e`, the two raw choices

`R(e)=e+tau`

and

`R(e)=e-tau`

are equivalent by `tau -> -tau`.

Therefore this is one equivalence class.

#### Proof of uniqueness at the least complexity

Rank zero is impossible because `Z e` must embed.

Rank one with no new generator is `Z e`, already excluded.

At rank one, one new generator with no relation raises the torsion-free rank to two, contradicting rank-primary minimality. Therefore a same-rank extension needs at least one torsion relation.

A kernel of order two gives orbit size at most two by Proposition 4.3.

The next possible finite kernel size is three; the only abelian group of order three is generated by one nonzero `tau` with `3tau=0`.

In the normal form of Theorem 4.1, exhaustive algebra over this kernel shows that the least orbit `>2` has size three and requires

`epsilon=+1`,
`phi=id`,
`a=±tau`.

The two choices are conjugate by `tau -> -tau`.

Hence one least carrier/transport class survives. ∎

### Corollary 4.5 — rank alone is not enough for uniqueness

For every integer `m>=3`, the presentation

`C_m = Z e ⊕ <tau | m tau=0>`

with

`R_m(e)=e+tau`,
`R_m(tau)=tau`

has an elementary orbit of exact size `m`.

So there is an infinite family at the same torsion-free rank.

The F1 result is unique only after applying the full issued extension/minimality order, not if one says merely "rank one".

This distinction is load-bearing.

### Proposition 4.6 — exact polynomial/order data of the minimum

Let

`N=R-id`.

Then on `C_min`:

`N(e)=tau`,
`N(tau)=0`.

Therefore

`N^2=0`,
`3N=0`.

Also

`R^3=id`.

The rationalized action is trivial because the torsion sheet disappears after tensoring with a characteristic-zero fraction field; therefore no field-valued minimal polynomial captures the non-sign information.

The exact integral annihilator facts are:

`(R-id)^2=0`,
`3(R-id)=0`,
`R^3-id=0`.

The least-degree monic annihilator is `(x-1)^2`, while the finite-order relation is `x^3-1`.

This is why the torsion solution must not be silently replaced by a preselected quadratic polynomial carrier.

### Proposition 4.7 — sign involution is independent

Every power of the least `R` acts trivially on the free quotient.

The old sign operation `J=-id` acts as `-1` on that quotient.

Hence

`J notin <R>`.

`J` commutes with `R` because both are additive and `J` is central.

The combined finite transport alphabet on the elementary occurrence is therefore exactly

`{J^s R^k(e): s in {0,1}, k in {0,1,2}}`

with six distinct states.

This six-state set is derived after the carrier is classified; it was not preselected.

Deliverable:

`MINIMAL_ADDITIVE_NONSIGN_CARRIER_FAMILY_CLASSIFIED = UNIQUE_LEAST_WITH_INFINITE_SAME_RANK_NONMINIMAL_FAMILY`.

---

## 5. Torsion refinement-consistency test

The taskbook requires torsion to be admitted or killed explicitly.

It is **admitted**.

Let a refined Path-formal state carry coefficients `c_1,...,c_n in C_min`.

Forgetting the distinguishing marker uses additive aggregation

`F(c_1,...,c_n)=sum c_j`.

Because `R` is additive,

`R(F(c_1,...,c_n))
 = sum R(c_j)`.

So transport commutes with finite refinement aggregation.

Forgetting the F1 torsion sheet uses `pi`.

Since `pi R=pi` for the minimum,

`pi R(c)=pi(c)`.

Thus "transport then forget F1" equals "forget F1 then apply the old `+id` sign transport".

No old signed coefficient is changed or identified, because `i` is injective and split.

The torsion relation `3tau=0` occurs only in the new sheet kernel; it does not imply

`3e=0`

or any other new equality in the F0 signed subgroup.

Therefore torsion does not violate the declared conservative/refinement requirements.

A torsion-free answer would require a new axiom not present in F1.

---

## 6. F1-Q3 — relabeling and reversal

### Theorem 6.1 — branch reversal must invert transport

For two reversible path roles `p,q`, define the transport comparison from `p` to `q` as `R`.

Reversing the role order compares `q` to `p`, so composition of the two comparisons must be identity.

Hence the reversed comparison is necessarily

`R^{-1}`.

This uses only reversibility and the meaning of swapping the direction of a comparison.

### Theorem 6.2 — unique reversal involution on the minimum

On `C_min`, define

`S(e)=e`,
`S(tau)=-tau`.

Then

`S^2=id`

and

`S R S^{-1}=R^{-1}`.

Among additive automorphisms fixing `e`, this `S` is the unique one that conjugates `R` to `R^{-1}`.

#### Proof

An additive automorphism fixing `e` restricts on the order-three kernel to multiplication by one of its two units:

`tau -> tau`
or
`tau -> -tau`.

The first centralizes `R`.

The second sends the shift `+tau` to `-tau`, hence sends `R` to `R^{-1}`.

So reversal uniquely selects the second. ∎

### Consequence 6.3 — what "conjugate two-sheet" means here

The additive carrier itself is not a two-sheet carrier. It has the sheet values

`0, +tau, -tau`.

What is forced is a two-orientation **transport presentation**

`{R,R^{-1}}`

paired by `S`.

Therefore:

`CONJUGATE_TWO_ORIENTATION_ACTION = FORCED`

but

`TWO_SHEET_ADDITIVE_CARRIER = NOT_FORCED`.

### Consequence 6.4 — serialization independence

Changing the serialization/name of the two `(1,1)` paths replaces `R` by `R^{-1}` and `tau` by `-tau`.

Since `S` identifies those presentations, the physical transport class is invariant.

Absolute naming of the new torsion generator is therefore eliminated.

Deliverable:

`NONSIGN_RELABELLING_TRANSPORT_CLASSIFIED = UNIQUE_REVERSAL_PAIR`.

---

## 7. F1-Q4 — path composition and diamond data

Let

`A_R={id,R,R^2}`

be the operator orbit generated by the derived least transport.

This is introduced only after proving `R^3=id`.

### Definition 7.1 — edge transport

Assign to each typed local edge `a` a power

`T(a)=R^{omega(a)}`

where `omega(a)` is one of the three power classes of `R`.

For a typed path

`p=a_1...a_n`,

define

`T(p)=T(a_n)...T(a_1)`.

Because all values are powers of the same `R`, this equals

`R^{sum omega(a_j)}`

with the exponent reduced only by the derived relation `R^3=id`.

### Theorem 7.2 — exact composition

For composable typed paths `p,q`,

`T(pq)=T(q)T(p)`.

Parenthesization at depth three or any greater finite depth is irrelevant by associativity of operator composition.

The deterministic checker exhausts exponent compositions through depth four.

### Definition 7.3 — elementary diamond ratio

For one commuting diamond with paths

`p=X_iX_j`,
`q=X_jX_i`,

define

`K(D)=T(q)T(p)^{-1}`.

Since `K(D)` is a power of `R`, write its derived exponent class as

`kappa(D)`.

The three possibilities are

`0,+1,-1`

modulo the relation `R^3=id`.

This is not a preselected three-phase group; it is simply the list of powers of the already-derived transport.

### Proposition 7.4 — gauge/choice independence

A vertex change of local coefficient frame by powers `g(v)` changes edge transports by

`T(a:v->w) -> g(w) T(a) g(v)^{-1}`.

For a closed diamond comparison, endpoint factors cancel.

Therefore `K(D)` is invariant.

Raw edge data are presentation dependent; diamond ratios are the local invariant.

### Proposition 7.5 — what data are sufficient

- vertex data alone describe only gauge-trivial transport when all edge data are pure vertex differences;
- edge data are sufficient to compute every path transport;
- elementary diamond data classify local path-to-path transport ratios but do not reconstruct an absolute edge lift without a gauge choice;
- no provenance beyond the already-existing typed Path-formal witness is required.

The path identity must remain available because `p` and `q` receive separate transport products before recoalescence.

### Proposition 7.6 — reversal and generator swap

Swapping the two path roles sends

`K(D) -> K(D)^{-1}`,

equivalently

`kappa -> -kappa`.

This is exactly the action of `S`.

### Proposition 7.7 — weak cyclic sector covariance

The same algebraic carrier/transport rule can be copied under the existing cyclic sector relabeling

`S_12 -> S_23 -> S_31 -> S_12`

without introducing a global cross-sector process.

This is covariance of the local classification only.

### Proposition 7.8 — exact F0 sign-dark preservation

Setting every non-sign power to `R^0=id` recovers the old sign-only transport as an exact subcase.

More strongly, for every `k`,

`R^k(e)+R^k(-e)=0`.

Thus the F0 signed dark pair remains dark after any common F1 non-sign transport.

Deliverable:

`NONSIGN_PATH_TRANSPORT_COMPOSITION_CLASSIFIED = EDGE_FUNCTOR_PLUS_DIAMOND_INVARIANT`.

---

## 8. F1-Q5 — does composition force coefficient multiplication?

### 8.1 Minimal answer: no

The coefficient carrier `C_min` is an additive group.

The old integer occurrence coefficients already act on it by repeated addition.

Typed path concatenation composes the transport operators `R^k`; it does not require multiplying two arbitrary elements of `C_min`.

Therefore the minimal construction is a module/action construction:

`integer occurrence algebra -> additive carrier C_min -> Aut(C_min)`.

No internal multiplication on `C_min` is needed.

### 8.2 Exhaustive test if an internal product is nevertheless demanded

Assume an associative bilinear product `*` on `C_min` that extends old integer multiplication:

`e*e=e`.

Because `tau` is torsion, all products involving `tau` are torsion. Write

`e*tau = a tau`,
`tau*e = b tau`,
`tau*tau = c tau`

with `a,b,c` taken modulo `3`.

Associativity gives

`a^2=a`,
`b^2=b`,
`c(a-b)=0`.

Hence `a,b` are each `0` or `1`.

Now demand that the derived non-sign transport be multiplicative:

`R(x*y)=R(x)*R(y)`.

From `R(e*tau)=R(e)*R(tau)` and `R(tau*e)=R(tau)*R(e)`, one obtains

`c=0`.

From `R(e*e)=R(e)*R(e)`, one obtains

`a+b=1`.

Therefore exactly two associative bilinear products survive:

### Left-handed product

`e*e=e`,
`e*tau=tau`,
`tau*e=0`,
`tau*tau=0`.

### Right-handed product

`e*e=e`,
`e*tau=0`,
`tau*e=tau`,
`tau*tau=0`.

They are opposites of one another and are exchanged anti-isomorphically by reversal `S`.

### Corollary 8.3 — no two-sided unital ring extension

If the old `e` were required to remain a two-sided multiplicative unit, one would need simultaneously

`a=b=1`.

But multiplicativity of `R` forces

`a+b=1 mod 3`.

`1+1 != 1 mod 3`.

Therefore no such associative two-sided-unital product exists on the minimal carrier with `R` multiplicative.

### Verdict 8.4

`COEFFICIENT_MULTIPLICATIVE_STRUCTURE_CLASSIFIED`:

- multiplication is **not forced**;
- module/operator action is sufficient and strictly lower complexity;
- a two-sided-unital internal ring extension compatible with `R` is impossible;
- if unitality is dropped, exactly two directed associative products survive and are reversal-paired.

No familiar ring has been named or selected.

---

## 9. Counterfactual: what happens if torsion-free is added

This subsection is not a premise and is not the F1 primary answer.

Suppose one adds the new axiom

`C is torsion-free`.

Rank one is then the old `Z` no-go, so rank at least two is required.

Take a primitive old occurrence `e` whose orbit generates the minimal rank-two carrier, so `{e,Re}` is an integral basis.

A finite-order `R in GL(2,Z)` with orbit `>2` cannot have only real eigenvalues `±1`; therefore its two eigenvalues are nonreal conjugate finite-order roots.

Its determinant is then `+1`.

Let `t=trace(R)`.

The characteristic polynomial is

`x^2-tx+1`.

Finite order with nonreal roots requires

`|t|<2`.

Since `t` is integral,

`t in {-1,0,1}`.

Using basis `(e,Re)`, the three companion matrices are therefore forced:

for `t=-1`:
`[[0,-1],[1,-1]]`;

for `t=0`:
`[[0,-1],[1,0]]`;

for `t=1`:
`[[0,-1],[1,1]]`.

Their exact orders are respectively

`3,4,6`.

Their characteristic/minimal polynomials are respectively

`x^2+x+1`,
`x^2+1`,
`x^2-x+1`.

The old `-id` lies in `<R>` for orders `4` and `6`, but not for order `3`.

Thus a torsion-free F1 would produce a finite three-family rank-two classification, not a unique one, before applying any additional selector.

This subsection proves that a rank-two answer requires an extra torsion-free assumption; it cannot be imported into the issued F1 silently.

---

## 10. Mandatory ablations summary

| Ablation | Smallest exact effect |
|---|---|
| remove finite-orbit requirement | infinite-order rank-two shear becomes admissible; finite alphabet is no longer forced |
| remove conservative F0 embedding | rank can drop to `0`; `(Z/2)^2` has an order-three automorphism orbit but cannot contain the old `Z` layer |
| remove explicit dark-cancellation clause | no change; it is redundant under group embedding + additive automorphism |
| remove branch relabeling covariance | `R` and `R^{-1}` become distinct serialization-dependent models |
| remove orientation reversal | the involution `S` is no longer forced |
| remove composition compatibility | nonfunctorial path assignments are admissible |
| torsion-free requirement | not used; adding it raises minimum rank to `2` and gives orders `3,4,6` |
| remove minimal-rank requirement | infinitely many enlarged carriers survive; uniqueness disappears |

Full proofs/countermodels are in:

`research_reports/CBRC_F1_ABLATION_AND_COUNTERMODEL_PACKET_20260822.md`.

---

## 11. Deterministic checker

Required checker:

`scripts/cbrc_f1_validate_nonsign_carrier_forward.py`

It uses exact integer/modular arithmetic only.

Coverage includes:

- exact `Aut(Z)={±1}` rank-one no-go;
- complete rank-one split-torsion normal-form enumeration at kernel sizes `2` and `3`, which is a complete bound for the least carrier under the declared order;
- exact orbit/order relation checks for the unique least carrier;
- `R^3=id`, `(R-id)^2=0`, `3(R-id)=0`;
- sign centrality and transported exact dark cancellation;
- unique reversal `S`;
- path composition through depth `4`;
- all `3^4=81` elementary diamond edge-exponent assignments;
- weak three-sector copy covariance;
- exhaustive `3^3=27` candidate bilinear multiplication tables on the minimal presentation, with exact associativity and `R`-multiplicativity filtering;
- the torsion-free rank-two companion counterfactual;
- every mandatory ablation countermodel.

Checker result:

`mismatch_count = 0`.

Composition cases through depth `4`:

`148`.

Diamond edge assignments:

`81`.

Diamond holonomy histogram:

`0 -> 27`,
`+1 -> 27`,
`-1 -> 27`.

Surviving internal multiplication tables:

`2`.

Two-sided-unital survivors:

`0`.

Deterministic checker digest:

`d3e570e05b76fc4f6d3269ac5fd58f9f833ce537f9121403b09f9c7fad132080`.

---

## 12. Proof-obligation closure

### Conservative old-layer embedding

PASS.

`i:Z e -> C_min` is injective and split by `pi`.

### Finite non-sign orbit

PASS.

Elementary orbit size is exactly `3`.

### Exact dark preservation

PASS, and proved redundant as an independent axiom.

### Branch relabeling

PASS.

The two raw shifts are one equivalence class under the unique reversal involution.

### Orientation reversal

PASS.

`SRS^{-1}=R^{-1}`.

### Composition

PASS.

Operator transport is functorial to all depths by associativity; checker covers depth `<=4`.

### Native typing

PASS.

No cell, sector, axis, endpoint, or trace identity is altered.

### Provenance

PASS.

Path-formal witnesses remain distinct until aggregation; the carrier adds a coefficient sheet, not a simultaneous multi-cell state.

### Readout non-import

PASS.

No scalar readout is defined or selected.

### Target leak

PASS.

See dedicated audit.

---

## 13. Primary and secondary verdicts

Primary:

`F1_UNIQUE_MINIMAL_NONSIGN_CARRIER`.

Secondary:

`F1_MINIMAL_TORSION_FREE_RANK = 1`

`F1_NEW_ADDITIVE_GENERATORS = 1`

`F1_NEW_ADDITIVE_RELATIONS = 1`

`F1_MINIMAL_KERNEL_PRESENTATION = <tau | 3tau=0>`

`F1_MINIMAL_ELEMENTARY_ORBIT_SIZE = 3`

`F1_MINIMAL_TRANSPORT_RELATION = R^3=id`

`F1_SIGN_INVOLUTION_IN_R_SUBGROUP = false`

`F1_REVERSAL_CLASS = {R,R^{-1}} / S`

`F1_PATH_COMPOSITION = OPERATOR_ACTION_WITH_DIAMOND_INVARIANT`

`F1_INTERNAL_MULTIPLICATION_REQUIRED = false`

`F1_TWO_SIDED_UNITAL_MULTIPLICATION_COMPATIBLE_WITH_R = false`

`F1_DIRECTED_NONUNITAL_MULTIPLICATION_FAMILY_SIZE = 2`

`F1_READOUT_SELECTED = false`

`F1_TORSION_FREE_COUNTERFACTUAL_RANK = 2`

`F1_TORSION_FREE_COUNTERFACTUAL_ORDERS = {3,4,6}`

---

## 14. Unresolved assumptions / boundaries

1. The rank-primary minimality order is mandated by F1-Q2's "smallest additive rank" wording; another future stage may choose a different cost model only by explicitly changing the task.
2. Torsion is allowed because the issued F1 does not forbid it and the exact refinement/forgetful tests pass.
3. No readout has been selected, so the operational observability of the torsion sheet is outside F1.
4. No global three-sector coherent process is claimed.
5. No Foundation promotion is claimed.
6. No claim is made that the minimal carrier is realized by nature or by any external physical theory.
7. The optional internal multiplication analysis shows underdetermination/impossibility at the minimal carrier; it is not promoted into the carrier definition.

---

## 15. Hard target closure

The stage classifies the first conservative finite non-sign coefficient carrier and its local transport, relabeling, composition, torsion status, and multiplication boundary without preselecting a target algebra.

Freeze:

`NONSIGN_RECOALESCENCE_MINIMAL_CARRIER_CLASSIFIED = true`.

`FIRST_NONSIGN_CARRIER_IS_RANK_ONE_WITH_ONE_DERIVED_ORDER_THREE_TORSION_SHEET = true`.

`TORSION_FREE_RANK_TWO_IS_COUNTERFACTUAL_NOT_PREMISE = true`.

`NO_READOUT_SELECTED = true`.

`NO_DOWNSTREAM_COMPARISON_PERFORMED = true`.
