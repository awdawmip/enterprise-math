# Tool Discovery Result — Native Geometry-of-Numbers / Successive-Minima Calculus

Status: `COMPLETE / RESEARCH RESULT / DRIVER REVIEW READY`

Task: `RS-TD-GON-NATIVE-GEOMETRY-OF-NUMBERS-MINIMA-CALCULUS`

Researcher-ID: `EM-TDGN-7C2A91`

Leading verdict:

`NATIVE_GEOMETRY_OF_NUMBERS_TOOLKIT_DISCOVERED`

## 0. Result in one sentence

A reusable geometry-of-numbers core survives without Euclidean volume: replace continuum volume/determinant by **finite semantic fiber capacity**, replace lattice-free by **fiber-injective**, and replace linear successive independence by the exact rank of a **fiberwise collision forest**. The resulting calculus gives sharp existence thresholds, packing/covering equalities, successive collision minima, explicit witnesses, and exact compression certificates.

This is a tool theorem over a **typed finite-state/fiber interface**. It does **not** modify the current Enterprise Foundation and does not promote an arbitrary quotient relation into N0.

## 1. Foundation and semantic typing

The task consumes the current Enterprise rules:

- classical definitions are not inherited into the native substrate merely because the classical theory succeeds;
- current plane coordinates are the three glued positive sector charts `(a,b,c) in N_0^3`, `min(a,b,c)=0`;
- the current plane has no native diagonal-shift quotient and no requirement of native negative axes;
- in a sector, the current native squared length is the sum of squares of the two active positive coordinates;
- carrier arithmetic, quotienting, metrics, or embeddings not already native must be explicitly typed as derived/task semantics.

Accordingly, the word **lattice** below is not a claim that every Enterprise state space secretly is a classical free Abelian lattice. The reusable primitive is a finite semantic-fiber relation. Classical subgroup lattices occur only as a specialization when a group/module carrier is legitimately declared.

Freeze for this result only:

`FOUNDATION_UNCHANGED = true`.

`FINITE_FIBER_CALCULUS_IS_A_TYPED_TOOL_INTERFACE = true`.

`ARBITRARY_QUOTIENT_IS_NOT_PROMOTED_TO_ENTERPRISE_N0 = true`.

## 2. Native finite-fiber geometry-of-numbers datum

Let a **finite-fiber datum** be

`F = (X, ~, pi, B)`

where:

1. `X` is a finite state set, or a locally finite state set used only through finite admissible bodies;
2. `~` is a declared or derived semantic equivalence relation on `X`;
3. `pi : X -> Q = X/~` is the fiber label map;
4. `B` is an admissible class of finite subsets of `X`;
5. when minima are requested, `B_t` is a nested body filtration indexed by a totally ordered scale set `T`.

The relation `~` must be semantically justified in the application. It may come from a native trace identity, an admitted finite relabeling quotient, a declared periodic observation, or — conditionally — a subgroup action. It is not inferred from an implementation embedding.

For a finite body `A subset X`, define:

### 2.1 Native size

`nu(A) = |A|`.

This is integer state count. It is additive on disjoint unions and monotone under inclusion.

### 2.2 Occupied fiber capacity

`kappa(A) = |pi(A)|`.

If `Q` is finite, define the global semantic capacity

`C(F) = |Q|`.

`kappa` is monotone and subadditive under union.

### 2.3 Fiber-free / witness-free body

`A` is **fiber-free** iff `pi|_A` is injective, equivalently every semantic fiber contains at most one state of `A`.

This is the intrinsic replacement for “lattice-free” at the finite-fiber layer. It becomes an actual lattice-free statement only in the subgroup specialization below.

### 2.4 Collision witness

A nontrivial witness is a pair

`x != y`, `x,y in A`, `pi(x)=pi(y)`.

The witness is the pair plus its equal-fiber certificate. A vector difference is not part of the generic output.

### 2.5 Collision defect / rank

Define

`delta(A) = nu(A) - kappa(A)`.

If the fiber occupancies are `n_q = |A intersect pi^{-1}(q)|`, then

`delta(A) = sum_q max(n_q-1,0)`.

This is not merely a lower bound. It is the exact maximum size of a fiberwise acyclic witness family: put a graph on `A`, allow an edge only between two distinct states in the same fiber, and require the chosen witness edges to form a forest. The maximum number of independent witness edges is exactly `delta(A)`.

Thus the relevant independence notion is **graphic/fiber independence**, not silently imported carrier linear independence.

## 3. The exact finite-capacity theorem

### Theorem FF-M1 — native capacity crossing

For every finite body `A`:

`|A| > |pi(A)|  =>  A contains a nontrivial equal-fiber witness`.

If the global quotient `Q` is finite, then the structural form is

`|A| > |Q|  =>  A contains a nontrivial equal-fiber witness`.

#### Proof

If no witness exists, `pi|_A` is injective, hence `|A|=|pi(A)|<=|Q|`. Contraposition proves both statements. No Euclidean volume, convexity, determinant, real embedding, or continuum averaging enters the proof. QED.

### Corollary FF-M1k — k independent witnesses

For finite `Q`,

`delta(A) >= |A|-|Q|`.

Therefore

`|A| >= |Q| + k  =>  A contains at least k fiber-independent collision witnesses`.

#### Proof

`delta(A)=|A|-|pi(A)|` and `|pi(A)|<=|Q|`. The forest construction takes one root in every nonempty fiber and joins every additional state in that fiber to the root. It produces exactly `delta(A)` witness edges and is acyclic. QED.

### Sharpness

If every quotient class is realized and one can choose one representative from each class, a transversal has exactly `|Q|` states and is fiber-free. Hence the threshold `|Q|+1` cannot be lowered.

More generally, whenever the ambient state set contains a transversal plus `k` additional states, the bound `|Q|+k` for forcing `k` independent witness edges is attained by adding exactly those `k` states to the transversal.

So the threshold is a structural capacity threshold, not an enumeration of the entire state space.

## 4. Packing, covering, and exact compression

For a finite body `A`, define the **fiber packing number**

`P_F(A) = max{|S| : S subset A and pi|_S is injective}`.

Define the **fiber covering number**

`K_F(A) = min{|S| : S subset A and pi(S)=pi(A)}`.

Then:

`P_F(A) = K_F(A) = kappa(A)`.

#### Proof

A fiber-free set contains at most one representative from each occupied fiber, so its size is at most `kappa(A)`; selecting one representative per occupied fiber attains that value. The same one-per-fiber set is also a cover, and no cover can omit an occupied fiber. QED.

Therefore:

`delta(A) = |A| - P_F(A) = |A| - K_F(A)`.

This gives an exact compression certificate: any downstream predicate that factors through `pi` needs at most `kappa(A)` representatives, and this number is optimal in the worst case if all occupied fibers may carry different predicate values.

## 5. Composition and monotonicity laws

### FF-L1 — size

If `A intersect B = empty`, then

`nu(A union B)=nu(A)+nu(B)`.

If `A subset B`, then `nu(A)<=nu(B)`.

### FF-L2 — occupied capacity

`kappa(A union B)=kappa(A)+kappa(B)-|pi(A) intersect pi(B)|`.

Hence `kappa` is monotone and subadditive.

### FF-L3 — defect monotonicity

If `A subset B`, then

`delta(A)<=delta(B)`.

Adding one state either opens a new fiber and leaves `delta` unchanged, or enters an already occupied fiber and increases `delta` by exactly one.

### FF-L4 — exact disjoint-union defect composition

For disjoint `A,B`:

`delta(A union B)=delta(A)+delta(B)+|pi(A) intersect pi(B)|`.

Thus collision rank composes by the two internal defects plus the number of semantic fibers hit by both pieces.

### FF-L5 — product capacity

For product data `(X_1 x X_2, pi_1 x pi_2)`, global capacities multiply:

`C(F_1 x F_2)=C(F_1) C(F_2)`.

For rectangular bodies `A_1 x A_2`:

`nu(A_1 x A_2)=nu(A_1)nu(A_2)`,

`kappa(A_1 x A_2)=kappa(A_1)kappa(A_2)`.

These laws provide the discrete replacement for the determinant/volume multiplicativity role where the application genuinely factors into independent semantic channels.

## 6. Successive collision minima

Let `B_t` be any nested finite-body filtration:

`t<=u => B_t subset B_u`.

Define the `k`-th **successive collision minimum** by

`lambda_k = inf{t in T : delta(B_t) >= k}`.

For discrete `T`, use the least such `t` when it exists.

Then

`lambda_1 <= lambda_2 <= ...`.

If the global capacity is finite,

`lambda_k <= inf{t : |B_t| >= |Q|+k}`

whenever the right-hand side exists.

This hierarchy is intrinsic to the declared fiber semantics and body filtration. It is deliberately weaker than classical successive minima: it certifies increasingly many forest-independent semantic collisions, not linearly independent lattice vectors.

If an application later supplies a legitimate vector/module structure and proves that fiber-independent witnesses imply a stronger algebraic independence notion, that is an additional bridge theorem, not part of FF-M1.

## 7. Conditional subgroup/lattice specialization

Suppose, and only suppose, that the application declares a finite Abelian group `G` and a subgroup `L<=G` as admissible semantics. Let

`pi : G -> G/L`.

Then `|Q|=[G:L]`, and FF-M1 becomes:

`|A| > [G:L]  =>  exists x!=y in A with x-y in L\{0}`.

If a declared difference body `D(A)` contains all admissible pair differences `x-y`, then it contains a nonzero element of `L`.

This is the closest finite structural analogue of the Blichfeldt-to-Minkowski mechanism. It is **conditional carrier mathematics** and must not be projected back onto the current Enterprise plane as a hidden global vector group. In particular it does not reinstate the superseded diagonal-shift quotient or negative-axis ontology.

## 8. Exact no-go boundaries

The positive toolkit also exposes precise limits.

### NO-GO-1 — cardinality alone does not determine witness behavior

Two bodies can have the same size but different witness status. For example, with two or more fibers, a two-state transversal has no collision while two states in one fiber do.

Therefore no representation-independent theorem of the form

`|A| >= T  <=>  witness`

can hold without a semantic capacity/fiber parameter, except at the trivial threshold beyond the total number of available fibers.

The minimum sufficient interface is not “volume replacement = cardinality” alone; it is **cardinality plus the admitted fiber structure/capacity**.

### NO-GO-2 — no metric-free Voronoi/CVP object

The finite-fiber datum has no notion of nearest state. Therefore Voronoi cells, Delaunay adjacency, covering radius, shortest-vector value, and closest-vector value do not exist generically. They require an additional admitted distance/order/neighborhood semantics.

### NO-GO-3 — no generic flatness theorem

Flatness needs directional/convex/width structure. A mere fiber partition plus count does not supply it. No native flatness theorem is claimed here.

### NO-GO-4 — capacity must be structural

If `|Q|` can only be obtained by exhaustively enumerating the same full state space one is trying to search, FF-M1 remains mathematically true but loses the intended algorithmic leverage. Tool-grade use therefore requires `Q`, `kappa`, or an upper bound on capacity to be available from a smaller declared relation, factorization, periodicity, trace type, product decomposition, or other independent structure.

## 9. Cross-domain demonstration A — current Enterprise sector

Work in the current native sector

`S_12 = {(a,b,0): a,b>=0}`.

No carrier negative axes and no diagonal quotient are introduced.

For a declared integer period `m>=2`, define the **derived periodic readout**

`rho_m(a,b,0) = (a mod m, b mod m)`.

This is arithmetic on the two current positive native axis ticks. It is a task-level quotient/readout, not a new N0 primitive.

Its capacity is exactly

`C_m=m^2`.

Hence every finite `A subset S_12` with

`|A|>m^2`

contains distinct native center states `P,Q` satisfying the same pair of axis residues.

The sharp fiber-free body

`R_m={(a,b,0): 0<=a<m, 0<=b<m}`

has exactly `m^2` states and one representative of every residue class. Thus `m^2+1` is sharp.

### Native-length body corollary

Using the already frozen sector law `L_E^2=a^2+b^2`, define

`B_R^E={(a,b,0): a^2+b^2<=R^2}`.

Its size is the exact integer count

`|B_R^E| = sum_{a=0}^R ( floor_sqrt(R^2-a^2) + 1 )`.

No area approximation is required. Therefore

`|B_R^E|>m^2 => B_R^E contains an equal-residue pair`.

A closed-form sufficient bound is:

`R^2>=2m^2`.

Indeed the box `0<=a,b<=m` then lies inside `B_R^E`, and the box already has `(m+1)^2>m^2` states.

The checker finds the first radius at which the pure capacity count alone guarantees collision for selected small periods:

| `m` | capacity `m^2` | first count-threshold `R` | `|B_R^E|` |
|---:|---:|---:|---:|
| 2 | 4 | 2 | 6 |
| 5 | 25 | 5 | 26 |
| 6 | 36 | 7 | 45 |
| 10 | 100 | 11 | 106 |
| 13 | 169 | 15 | 193 |
| 20 | 400 | 22 | 402 |

This is a discrete existence certificate in current Enterprise geometry. The witness output is the two native states plus their residue equality. It is not silently reinterpreted as a native vector difference.

## 10. Cross-domain demonstration B — PathSqrt component-trace fibers

Use the frozen square-norm path-root operator:

`PathSqrt_E(r^2)=disjoint_union_{(a,b) in GRoot_E(r^2)} Lambda(a,b)`.

Let

`pi_trace(path)=(a,b)`

for `path in Lambda(a,b)`. Equivalently, the fiber label is the canonical component trace/root branch.

Then

`C_trace(r)=|GRoot_E(r^2)|`,

and

`nu(PathSqrt_E(r^2)) = sum_(a,b) binom(a+b,a)`.

The exact fiber packing/cover theorem says:

- the maximum set containing at most one path per component trace has size `C_trace(r)`;
- the minimum exact representative set for every downstream **trace-invariant** predicate also has size `C_trace(r)`;
- the discarded multiplicity is exactly `delta = total_paths - C_trace(r)` and remains recoverable as fiber metadata.

### N = 2500

The frozen root set is

`{(0,50),(14,48),(30,40),(40,30),(48,14),(50,0)}`,

so

`C_trace(50)=6`.

The frozen total path count is

`110,695,538,274,255,714,208`.

Therefore the exact collision defect is

`110,695,538,274,255,714,202`.

For every downstream computation whose value factors through component trace, the search interface can be reduced **exactly and optimally** from

`110,695,538,274,255,714,208`

formal paths to at most

`6`

representatives, while retaining the path multiplicities separately. This is not heuristic pruning: `P_F=K_F=6` proves both maximal fiber-free packing and minimal trace-cover size.

This supplies the task-required nontrivial search-space reduction.

## 11. Executable finite checks

Checker:

`experiments/tool_discovery_native_geometry_of_numbers_minima_calculus_20260822.py`

The checker uses only the Python standard library and validates:

1. 2,018 exhaustive small generic subset/fiber cases for the defect identity, witness-free equivalence, forest-rank extraction, and insertion monotonicity;
2. exact disjoint-union defect composition on additional exhaustive assignments;
3. sharp modular-sector transversals and enlarged-body collisions for `2<=m<=20`;
4. exact native-length ball cardinality thresholds for `2<=m<=20`;
5. square-root component fibers for every `1<=r<=128`;
6. the frozen `N=2500` root set, six path-fiber sizes, total path count, and defect.

Deterministic canonical JSON result digest from the executed checker:

`sha256:ed12f3a96a1b961183cf58a5b47de2615baae98a6e1c67819d8342f453d45385`

## 12. Volume replacement audit

### What plays the role of size?

Primary native size is integer state count `nu(A)=|A|`. The determinant/fundamental-cell role is played not by a geometric volume but by semantic quotient capacity `|Q|` or the local occupied-fiber count `kappa(A)`.

### Additivity / monotonicity / subadditivity

- `nu` is additive on disjoint unions and monotone;
- `kappa` is monotone and subadditive, with an exact inclusion-exclusion law;
- `delta=nu-kappa` is monotone and has the exact disjoint-union composition law in Section 5.

### Relabeling invariance

If `f:X->X'` is a bijection preserving the declared fiber relation and sends each admissible body `B_t` to its counterpart, then `nu`, `kappa`, `delta`, packing/covering numbers, and all `lambda_k` are unchanged.

Arbitrary relabelings that destroy the declared semantic relation are not admitted automorphisms of the datum.

### Equal size, different witness behavior?

Yes. Equal cardinality does not fix witness behavior below the capacity threshold. This is the exact reason cardinality alone is insufficient.

### Does continuous volume prove a native theorem here?

No continuum volume is required for FF-M1. Classical volume arguments remain valid effective comparison mathematics for classical lattices, but they do not define the finite Enterprise capacity observable. In applications that genuinely possess both structures, a later bridge may compare asymptotic state counts with Euclidean volume; that would be an effective recovery theorem, not the native proof of FF-M1.

## 13. Historical mechanism and conservative novelty statement

Classically, Minkowski's convex-body theorem uses a symmetric convex body in `R^n` and compares its Euclidean volume with `2^n det(Lambda)` to force a nonzero lattice point. Classical successive minima scale a body until it contains increasing numbers of linearly independent lattice points. Geometry of numbers also connects admissibility/lattice-free sets with packing, covering, Voronoi/Delaunay structure, flatness, SVP and CVP.

The closest operational ancestor of FF-M1 is the Blichfeldt/pigeonhole mechanism: quotient by a fundamental domain, force two points into the same lattice class, then take their difference. The current result extracts precisely the part of that logic that does not need Euclidean measure.

Conservative novelty:

`THE_ABSTRACT_COMBINATORICS_IS_NOT_CLAIMED_AS_A_NEW_CLASSICAL_THEOREM`.

At the pure finite-set level, FF-M1 is a sharpened partition/pigeonhole identity and the forest-rank statement is elementary graphic-matroid combinatorics. The Enterprise contribution established here is the **typed refoundation**: a reusable object/size/capacity/minima/packing API that obeys current native semantics, separates carrier lattices from native state spaces, proves exact compression/witness bounds, and works unchanged across current spatial-sector and path-root problem families.

Historical comparison sources:

- Encyclopedia of Mathematics, “Minkowski theorem”: https://encyclopediaofmath.org/wiki/Minkowski_theorem
- Encyclopedia of Mathematics, “Geometry of numbers”: https://encyclopediaofmath.org/wiki/Geometry_of_numbers
- A. Basu, “Geometry of Numbers,” in *Convexity and its Applications in Discrete and Continuous Optimization*, Cambridge University Press, 2025, DOI `10.1017/9781108946650.006`.

## 14. TOOL API

### Input

`FiberDatum(X, fiber_label=pi, admissible_body=A or filtration B_t)`

Required:

- finite body or finite stage;
- exact/evaluable fiber label;
- semantic typing for the relation behind `pi`.

Optional:

- finite global capacity `C=|Q|` or a structural upper bound `C_hat`;
- ordered body filtration for minima.

### Output

- `size(A) = |A|`;
- `occupied_capacity(A) = |pi(A)|`;
- `is_fiber_free(A)`;
- `collision_defect(A)=|A|-|pi(A)|`;
- `witness(A)` = equal-fiber pair when defect > 0;
- `witness_forest(A)` with exactly `delta(A)` independent edges;
- `packing_number(A)=|pi(A)|`;
- `covering_number(A)=|pi(A)|`;
- `lambda_k(B_t)` when a filtration is supplied.

### Laws

- `|A|>|Q| => witness`;
- `|A|>=|Q|+k => k independent witness edges`;
- `P_F(A)=K_F(A)=kappa(A)`;
- `delta(A)=|A|-kappa(A)`;
- inclusion monotonicity of `delta`;
- exact disjoint-union composition;
- multiplicative global capacity under product fibers;
- invariance under fiber-preserving admitted relabelings.

### Failure modes

- fiber relation not native/derived/declared at the claimed semantic layer;
- capacity available only by full exhaustive enumeration, eliminating leverage;
- request for nearest/shortest/Voronoi/flatness without a metric/direction semantics;
- interpreting a generic equal-fiber pair as a vector difference without a declared group/module action;
- using cardinality alone as if it determined witness behavior;
- using a quotient readout to rewrite the current Foundation ontology.

## 15. Claim ledger

`CLAIM_FF_GON_TOOL`:

- declared base carrier: finite/local-finite state set plus an explicitly typed fiber relation;
- N0 requirement: only the application’s already declared native states/relations;
- introduced operation/readout: fiber label `pi` when not already native;
- implementation carrier: none required by the abstract theorem;
- N2/N1 structures: application-specific quotient/readout or filtration when introduced;
- N3 continuum objects used in proof: none;
- mature concepts retained: lattice, volume, packing, covering, successive minima, Voronoi/Delaunay, flatness, SVP/CVP for comparison/refoundation;
- effective definitions withheld from native premise: Euclidean volume, determinant, convex body, Euclidean nearest-distance, classical lattice vector independence;
- target leakage: none in FF-M1; the theorem uses only finite counts and the declared fiber relation;
- relabeling certificate: all outputs are invariant under fiber-preserving bijections, with minima additionally requiring filtration equivariance;
- admissibility verdict: `NATIVE_ADMISSIBLE_RELATIVE_TO_DECLARED_FIBER_DATUM`; application-specific introduced quotients remain `CONDITIONAL_DERIVED` unless separately promoted;
- weakest valid restatement: exact finite semantic-capacity existence/compression calculus, not a universal native Euclidean geometry.

## 16. Final acceptance check

The task acceptance gate is met:

- explicit reusable object/size/witness interface: **yes**;
- nontrivial existence/obstruction theorem: **yes**, FF-M1 / FF-M1k plus no-go boundaries;
- minima/packing/covering/lattice-free calculus with laws: **yes**;
- two genuinely different Enterprise families: **yes**, current sector geometry and path-valued integer-square-root fibers;
- at least one nontrivial search-space reduction: **yes**, `N=2500` exact trace compression from ~`1.106955e20` paths to 6 representatives;
- exact carrier/native and size-semantics boundaries: **yes**;
- Euclidean volume not used as decisive native quantity: **yes**.

Therefore the leading verdict remains:

`NATIVE_GEOMETRY_OF_NUMBERS_TOOLKIT_DISCOVERED`.
