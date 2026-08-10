# R004 precision genesis — Supplement 13: typed relation compiler and semantic activation cascades

Status: `PROVED_WIP + EXECUTABLE_CHECKED + PRIOR_ART_SPECIALIZATION + P023/A4_BOUNDARY`  
Parent: `R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_12.en.md`  
Owner branch: `research/r004-precision-genesis-closure-20260810`

Supplement 12 established that a future kernel is only an equality IR: typed quotient semantics cannot in general be reconstructed from that kernel alone. This supplement makes the next layer executable for finite relation/witness languages.

The main result is not a new generic bisimulation theory. Weighted bisimulation, balanced/equitable partitions, coalgebraic partition refinement, monoid-weighted networks and their stable-partition lattices are established prior mathematics. R004 uses those ideas as a typed compiler specialization and isolates one project-relevant boundary:

> total-operation congruences compose by raw kernel intersection, while quotient-relative relation/witness aggregation can require a new stabilization cascade after two separately compiled tasks are combined.

That distinction determines when the compiler may simply intersect already compiled kernels and when it must run a new fixed-point repair.

## 1. Typed relation channels

Let `X` be a finite state carrier and `P` a current partition of `X`.

A typed relation channel `c` consists of:

- a declared commutative monoid `(M_c, op_c, 0_c)`;
- an edge/witness value `w_c(x,y) in M_c`.

For one source state `x` and one current target block `B in P`, define the block aggregate

`Sigma_(c,P)(x,B) = op_{y in B} w_c(x,y)`.

The complete typed relation signature of `x` at `P` is the vector of all such aggregates over every declared channel and every current target block.

A partition `P` is **typed-relation stable** when states in the same source block have identical complete signatures.

The executable compiler treats associativity, commutativity and identity of the supplied monoid as semantic preconditions; it validates only the finite carrier/partition contract and hashability needed by the reference implementation.

## 2. R004-COMP-T10 — common finite semantics as monoid instances

Three important future languages become instances of the same finite interface.

### MAY support

Use the Boolean monoid `(Bool, OR, False)`, with `w(x,y)=True` exactly when the relation contains `(x,y)`. Then `Sigma(x,B)` asks only whether at least one target in `B` is reachable.

### Witness multiplicity

Use `(N_0, +, 0)`, with `w(x,y)` equal to the number of declared witnesses from `x` to `y`. Then `Sigma(x,B)` is the exact witness multiplicity into the target block.

### Witness label/class set

Use finite sets under union `(P_f(L), union, emptyset)`. Then `Sigma(x,B)` is the set of witness labels/classes reaching the target block.

A product of monoids preserves several typed semantics simultaneously. The implementation equivalently accepts several channels and concatenates their signatures.

## 3. R004-COMP-T11 — unique coarsest stable refinement

Starting from an initial observation partition `P_0`, define one refinement step by splitting each current source block according to the complete typed relation signature against the **current** target blocks.

Iterate `P_0 >= P_1 >= P_2 >= ...` until no strict split remains, where `>=` means "is coarser than".

Every strict round increases the number of blocks, so on a finite carrier termination occurs after at most `|X|-|P_0|` strict rounds. The terminal partition `P_*` is stable.

More importantly, it is the **unique coarsest stable refinement of `P_0`**.

Proof. Let `Q` be any stable refinement of `P_0`. Inductively assume `Q` refines `P_n`. Every target block of `P_n` is then a union of `Q`-blocks. Two states in one `Q`-block have equal aggregate into every `Q` target block by stability; associativity/commutativity of the monoid lets those equalities aggregate over unions, so the two states also have equal signatures against every `P_n` block. Therefore `Q` refines `P_(n+1)`. By induction `Q` refines the terminal `P_*`. Hence no stable refinement of `P_0` is coarser than `P_*`.

This finite proof is a specialization of established balanced/weighted partition-refinement mathematics, not a novelty claim about generic refinement.

## 4. R004-COMP-T12 — semantic factor-map monotonicity

Suppose two channel semantics use commutative monoids `M` and `N`, and there is a monoid homomorphism `phi:M->N` such that the `N`-valued edge data are obtained pointwise by applying `phi` to the `M`-valued data.

Then every `M`-stable partition is `N`-stable, because `phi(op_M values) = op_N phi(values)`. Consequently `Compiler_M(P_0)` refines `Compiler_N(P_0)`.

This supplies an information-order relation between typed future languages without reducing them to one scalar precision coordinate.

Two exact examples:

- witness count maps to MAY support by `n -> (n>0)`;
- witness label-set maps to MAY support by `S -> (S is nonempty)`.

Thus COUNT and LABEL-SET each refine MAY whenever they are generated from the same underlying witnesses.

## 5. R004-COMP-CE10 — equal class count does not mean equal relation precision

Take states `X={x,y,z,a,b}` and initial universal observation. Declare witnesses:

- `x -> a` with label `p`;
- `x -> b` with label `q`;
- `y -> a` with label `p`;
- `y -> b` with label `p`;
- `z -> a` with label `p`;
- `a,b` have no outgoing witnesses.

The four compiled semantics are:

- MAY: `{{x,y,z},{a,b}}` — 2 classes.
- COUNT: `{{x,y},{z},{a,b}}` — 3 classes.
- LABEL-SET: `{{x},{y,z},{a,b}}` — 3 classes.
- COUNT + LABEL-SET: `{{x},{y},{z},{a,b}}` — 4 classes.

COUNT and LABEL-SET therefore have the same class count but incomparable partitions.

So even after state cardinality has been made task-relative, `number of safe classes` is not a complete typed-precision coordinate. The correct order is structural: `semantic factor map -> safe-partition refinement`. Scalar class count is only a derived complexity statistic.

## 6. R004-COMP-T13 — total-operation tasks obey a raw meet law

For a total finitary algebra, operation-compatible equivalence relations are congruences. Intersections of congruences are congruences.

Hence if two observation/task packages for the same total-operation language compile to largest compatible congruences `Theta_1` and `Theta_2`, the joint observation package compiles to `Theta_joint = Theta_1 intersect Theta_2`.

Equivalently, after each total-operation task has already been compiled, their equality kernels can be combined by raw common refinement without an additional congruence-repair cascade.

This is ordinary congruence-lattice mathematics and belongs upstream to A2/P023 operation-quotient theory. R004 records it only as the comparison half of the typed compiler boundary.

## 7. R004-COMP-CE11 — relation tasks can activate after another task refines target geometry

For quotient-relative relation aggregation the raw meet law fails.

Take three states `{0,1,2}` and the universal initial partition. Use witness-count semantics for two channels.

Channel `A` has one witness: `0 -> 1`.

Channel `B` is a directed 3-cycle: `0 -> 1`, `1 -> 2`, `2 -> 0`.

Compiled separately:

- `A` yields `P_A={{0},{1,2}}`;
- `B` yields the universal partition `P_B={{0,1,2}}`, because every state has exactly one `B` witness into the only current target block.

Their raw common refinement is still `P_A meet_raw P_B = {{0},{1,2}}`.

But that partition is **not** stable for the joint language. Once `A` exposes target block `{0}` separately from `{1,2}`, channel `B` becomes discriminating: state `1` sends its `B` witness into `{1,2}`, while state `2` sends its `B` witness into `{0}`.

So the joint compiler performs a second repair and reaches the discrete partition: `1 class -> 2 classes -> 3 classes`.

Therefore `Compiler_(A+B)(P_0) != Compiler_A(P_0) meet_raw Compiler_B(P_0)`.

This is the minimal example found within the exhaustively checked class of loopless directed simple two-channel systems: no such cascade exists on one or two states.

The point is not that relations are generically harder than operations. The point is that this relation semantics is **quotient-relative**: channel outputs are aggregates into the *current quotient target blocks*. Splitting those target blocks can reveal a distinction that did not exist at the previous quotient.

## 8. R004-COMP-CE12 — even one relation channel can have raw-meet failure

The same phenomenon occurs inside the stable-partition family of one fixed relation channel.

Take five states `{0,1,2,3,4}` and one loopless simple directed graph with edges:

- `0 -> 2,3`;
- `1 -> 2,3`;
- `2 -> 0,1`;
- `3 -> 0,1`;
- `4 -> 0,1`.

Under witness-count semantics, both partitions `P={{0,2,4},{1,3}}` and `Q={{0,3,4},{1,2}}` are stable: every state has count vector `(1,1)` into the two blocks of the corresponding partition.

Their raw common refinement is `P meet_raw Q = {{0,4},{1},{2},{3}}`.

It is not stable: state `0` points to singleton target blocks `{2}` and `{3}`, while state `4` points to `{0,4}` and `{1}`. One stabilization round splits `{0,4}`, giving the discrete partition.

An exhaustive search over every loopless directed simple graph with at most four states found no pair of count-stable partitions whose raw common refinement is unstable. Thus this five-state witness is minimal within that bounded class.

## 9. R004-COMP-T14 — stable meet is stabilization of raw meet

Let `Stab_W(P)` denote the unique coarsest stable refinement of `P` for one fixed typed relation language `W`.

Then `Stab_W(P)` refines `P`; `Stab_W` is idempotent; and if `P` refines `Q`, then `Stab_W(P)` refines `Stab_W(Q)`.

For already stable `P,Q`, the meet in the stable-partition lattice is therefore `P meet_W Q = Stab_W(P meet_raw Q)`. The five-state example proves that the final `Stab_W` cannot in general be deleted.

This stable-lattice structure has direct prior art in balanced-equivalence and weighted-network theory. R004 uses the formula as a compiler control rule.

## 10. Compiler architecture consequence

Supplement 12 gave the interface `Exact Carrier + Typed Future Language -> Minimal Safe Carrier + Descended Typed Semantics`.

This supplement sharpens how the typed future language must be dispatched.

### Total-operation semantics

Elementary contexts are fixed functions on the fine carrier. Their compatible kernels form a congruence family closed under intersection. Compilation can therefore reuse the A2/P023 operation-congruence engine, and independently compiled task kernels compose by raw meet.

### Quotient-relative relation/witness semantics

The observable for one source state is not merely a fixed list of exact target identities. It is an aggregate over the **current quotient target blocks**.

The compiler must therefore run a fixed point: `current target geometry -> source signatures -> refined target geometry -> new source signatures -> ...`.

Independent relation channels should be compiled simultaneously by product signatures, or equivalently by repeated stabilization to a common fixed point. Compiling each channel once and intersecting the resulting carriers is not sound in general.

This is the first exact **semantic activation cascade** in the R004 compiler: one typed requirement can make another previously invisible requirement become state-distinguishing by refining the quotient on which that requirement is evaluated.

## 11. Ownership and prior-art boundary

Established mathematics, not Enterprise Math novelty claims, includes weighted and monoid-valued labelled transition systems and weighted bisimulation; balanced/equitable partitions of networks; generic coalgebraic partition refinement; coarsest invariant refinement algorithms; complete lattices of balanced equivalence relations; and congruence lattices of total algebras.

Relevant source IDs are recorded in `sources_r004_typed_relation_compiler.json`.

R004's WIP addition is narrower:

1. place those structures behind the already established typed future-language compiler interface;
2. expose MAY/COUNT/LABEL-SET as explicit task semantics rather than one untyped "relation";
3. use semantic factor maps to order safe quotients;
4. record the exact total-operation raw-meet versus quotient-relative relation stabilization split;
5. provide minimal finite activation/cascade witnesses and executable controls;
6. route mother ownership back to P023/A4 rather than creating a competing generic theory.

Historical novelty of this exact Enterprise Math packaging remains `NOVELTY_UNVERIFIED`.

## 12. Validation

Committed regressions cover the explicit typed-order and cascade examples.

Independent exhaustive verification additionally checked:

- all loopless directed simple graphs on `n<=4` and every initial partition under COUNT semantics: **61,769** compiler/oracle cases, zero mismatches;
- the same family under MAY semantics: **61,769** compiler/oracle cases, zero mismatches;
- COUNT-result refinement of MAY-result on the same **61,769** cases: zero violations;
- all **4,165** loopless directed simple graphs on `n<=4`: no same-channel count-stable raw-meet failure;
- the displayed five-state graph: raw meet fails and stabilization gives the discrete partition.

The oracle enumerated all set partitions satisfying the declared stability contract and selected the unique coarsest stable refinement; it was independent of the iterative compiler implementation.

The new module's five direct `unittest` regressions pass in the available private Python environment. No fresh full-repository CI, Lean proof or canonical-main status is claimed.

## 13. Next frontier

The compiler boundary is now much narrower. The next question is not "how do we refine a relation partition?" Generic refinement is prior art.

The project question is:

> Given a **typed future language** containing operations, quotient-relative relations, witness identity classes, MAY/MUST requirements and possibly partial legality, can the compiler automatically construct the weakest product of semantic domains, route each part to the correct stabilization engine, and emit explicit descent certificates showing that every requested future composition remains legal on the compiled carrier?

This is a P023/A3/A4 interface question. R004 should continue supplying finite reduction theorems and counterexamples, not seize the mother abstraction.
