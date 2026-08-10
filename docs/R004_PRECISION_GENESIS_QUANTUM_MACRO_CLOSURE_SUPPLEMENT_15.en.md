# R004 precision genesis — Supplement 15: activation-aware typed generator bases

Status: `PROVED_WIP + EXECUTABLE_CHECKED + PRIOR_ART_SPECIALIZATION + P023/A3/A4_BOUNDARY`  
Parent: `R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_14.en.md`  
Owner branch: `research/r004-precision-genesis-closure-20260810`

Supplement 14 reduced an arbitrarily large future syntax to a finite typed generator basis plus descent certificates, but left one question open: which generators are actually necessary? This supplement gives an exact finite answer for **carrier synthesis**, separates it from **semantic reconstruction**, and proves when quotient-level algebraic reconstruction makes a generator redundant before re-running the carrier compiler.

The generic ingredients — set cover/hitting set, minimal semigroup generating sets, term generation and semiring generation — are prior mathematics. R004's contribution is the activation-aware placement inside the typed Representation Compiler and the exact finite cross-domain reduction/counterexample package.

## 1. Two different basis problems

Let `G` be the complete declared typed generator set, `P_0` the initial observation partition, and

`Q* = Compile_G(P_0)`

the unique coarsest safe carrier from Supplement 14.

There are two different minimization goals.

### Carrier basis

A subset `S subset G` is a **carrier basis** when

`Compile_S(P_0)=Q*`.

It preserves exactly the distinctions needed to force the same current safe carrier.

### Semantic reconstruction basis

A subset `S subset G` is a **semantic reconstruction basis** when every requested descended generator on `Q*` can be computed from the descended generators in `S` by declared legal reconstruction rules: operation terms/compositions, semiring polynomials, semantic factor maps, or another explicitly certified quotient-natural recipe.

Carrier equality alone is not semantic equality. If `P_0` is already the discrete partition on two states, a requested swap operation does not refine the carrier at all, so the empty set is a carrier basis. But the swap is not reconstructible from the free identity term, so it must remain in the semantic basis.

Therefore the compiler must return basis **type**, not just one minimum generator count.

## 2. R004-COMP-T23 — forbidden-world hitting-set theorem

Define the finite family of forbidden coarse worlds

`U(P_0,Q*) = { P : Q* strictly refines P and P refines P_0 }`.

For each generator `g` and candidate partition `P`, define the integer kill bit

`kappa_g(P)=1` if `g` is not stable on `P`, and `0` otherwise.

Because `Q*` is stable for every generator in `G`, it is stable for every subset `S`. Hence `S` preserves the target carrier iff there is no strictly coarser `S`-stable refinement of `P_0`.

Equivalently:

`S is a carrier basis`

iff

`for every P in U(P_0,Q*), sum_(g in S) kappa_g(P) >= 1`.

Thus exact carrier-basis synthesis is a finite hitting-set problem over **forbidden partitions**, not over individual state pairs.

Proof. If some forbidden `P` is killed by no selected generator, then all selected generators are stable on `P`, so the coarsest `S`-safe refinement cannot equal the strictly finer `Q*`. Conversely, if every forbidden `P` is killed, any `S`-stable refinement of `P_0` that is coarser than or equal to `Q*` must equal `Q*`; since `Q*` itself is `S`-stable, it is the coarsest one.

Independent exhaustive verification covered every three-state initial partition, every three-element subset of total unary operations, and every retained subset: **117,000** subset/compiler cases, with exact agreement between fresh subset compilation and the hitting criterion.

## 3. R004-COMP-CE14 — pairwise merge checks are insufficient

A tempting shortcut is to test only partitions obtained by merging one pair of final classes. This is unsound.

Take

`P_0={{0,1,2},{3}}`

and the unary operation

`f: 0->1, 1->2, 2->0, 3->3`.

Add another splitter generator `h=(3,1,2,3)`. The full language `{f,h}` compiles `P_0` to the discrete partition.

Now retain only `f`.

Every three-block partition between the discrete target and `P_0` — i.e. every candidate that merges exactly one pair among `0,1,2` — is **not** `f`-stable. A local pairwise test would therefore report that every one-pair merger has been killed.

Nevertheless the much coarser partition

`{{0,1,2},{3}}`

is itself `f`-stable, and the `f`-only compiler stops there.

So local pair separation does not identify the global minimal carrier. The forbidden-world universe must include multi-class mergers unless additional structure proves a smaller certificate sufficient.

## 4. R004-COMP-T24 — inclusion-minimal and integer optimality certificates

Let `S` hit every forbidden world.

`S` is inclusion-minimal iff for every selected generator `g` there exists a **private forbidden world** `P_g` such that among the selected generators only `g` kills `P_g`.

Indeed, if no private world exists for `g`, removing `g` leaves every forbidden world hit. Conversely a private world becomes uncovered as soon as `g` is removed.

For a cardinality lower bound, call a family `D subset U` **generator-disjoint** when every available generator kills at most one member of `D`. Then every carrier basis has size at least `|D|`, because each member of `D` requires a different selected killer.

Therefore a carrier basis `S` accompanied by a generator-disjoint packing `D` with

`|S|=|D|`

has a completely integer optimality certificate.

For the four-state ping-pong pair from Supplement 14, the forbidden-world kill masks are `1,1,1,2`; the only minimum carrier basis is `{f,g}`. One `f`-private world and one `g`-private world form a generator-disjoint packing of size two, proving optimality without normalized weights or fractional dual variables.

## 5. R004-COMP-CE15 — contextual redundancy is not monotone

Generator redundancy cannot be tested only at `P_0`.

The four-state operation witness from Supplement 14 has `g` alone leaving `P_0` unchanged, so relative to the empty language `g` appears carrier-redundant. After `f` refines the target geometry, however, `g` becomes distinguishing and is necessary for the final discrete carrier.

The three-state relation activation example from Supplement 13 shows the same phenomenon for COUNT channels.

Hence a rule of the form “drop every generator that produces no immediate refinement” is unsound. The hitting formulation is activation-aware because it tests the generator against every forbidden coarse world, including worlds made visible only after other generators refine the state.

## 6. R004-COMP-T25 — quotient-natural reconstruction implies carrier redundancy

There is nevertheless a strong class of generators that can be deleted without a hitting-set search.

Suppose the full language `G` compiles to `Q*`, and `S subset G` is retained. Let an omitted generator `h` descend to `h_bar` on `Q*`.

Assume there is a reconstruction rule `F` such that

`h_bar = F((g_bar)_(g in S))`

and `F` is **coarsening-natural**: whenever a further quotient of `Q*` is compatible with the retained descended generators, applying that further quotient before or after `F` gives the same descended result.

Then `h` is carrier-redundant relative to `S`.

Proof. Suppose a partition `P` strictly coarser than `Q*` is stable for `S`. It induces a further quotient of `Q*`. Coarsening-naturality makes the reconstructed `h_bar` compatible with that quotient. Since `h` is already `Q*`-stable, this implies `h` is stable on `P`. If every omitted generator has such a reconstruction certificate, every `S`-stable coarse world is actually `G`-stable, contradicting the definition of `Q*`. Thus `Compile_S(P_0)=Q*`.

This meta-rule explains why semantic reconstruction can often be used **before** the residual carrier hitting-set stage even when the reconstruction was discovered only after the full carrier was compiled.

## 7. R004-COMP-T26 — total-operation specialization

For total operations, ordinary term evaluation is coarsening-natural.

In the unary case, if every omitted quotient transformation belongs to the transformation monoid generated by the retained quotient transformations and identity, the retained subset automatically preserves the same carrier.

This is stronger than requiring fine-level generation. An operation may fail to lie in the fine transformation monoid of the retained operations but become reconstructible after collapse.

Example: on four fine states with target partition `{{0,1},{2,3}}`, the within-block swap

`(0 1)(2 3)`

is not the fine identity, but its descended quotient transformation is exactly identity. It is therefore reconstructible from the free identity term on the quotient and is both semantically and carrier redundant for this task.

Independent exhaustive checking of three-state, three-operation families considered **102,375** retained-subset situations. In **43,940** cases all omitted quotient maps lay in the retained quotient transformation monoid; every one of those subsets compiled to the same target carrier.

## 8. R004-COMP-T27 — semiring-relation specialization

For semiring-valued relation generators, semiring polynomials are coarsening-natural under the block-sum quotient homomorphism proved in Supplement 14.

Therefore if an omitted relation is `Q*`-stable and its quotient matrix lies in the semiring subalgebra generated by retained quotient matrices, the omitted relation is carrier-redundant.

The proof is the same descent argument: any coarser partition stable for the retained matrices induces a stable quotient of the `Q*` relation algebra; the reconstructed semiring polynomial is stable there, and `Q*`-stability of the omitted fine relation then lifts that stability back to the coarser fine partition.

For Boolean MAY relations on three states, **20,480** two-generator/initial-partition cases were checked. In **1,560** cases the omitted quotient relation belonged to the Boolean semiring generated by the retained quotient relation; all 1,560 retained languages produced the same final carrier.

Semantic factor maps such as COUNT -> MAY are an even stronger pre-compile instance: stronger-channel stability implies weaker-channel stability on every partition, so the dominated channel may be removed before carrier synthesis while its output remains reconstructible by the factor map.

## 9. R004-COMP-T28 — carrier basis can be strictly smaller than semantic basis

Under the coarsening-natural reconstruction assumptions above, every semantic reconstruction basis is automatically a carrier basis. Hence the derived minimum sizes satisfy

`b_carrier <= b_semantic`.

Strict inequality occurs. On the discrete two-state observation, a requested swap operation changes no carrier distinction, so the empty set is a carrier basis. But swap is not generated by the free identity transformation, so any reconstruction basis for that requested operation must retain it; here

`b_carrier=0`, `b_semantic=1`.

This inequality is only a derived cardinality statement. As Supplement 13 already showed, equal basis/class counts need not mean equal typed information. The compiler should return the actual basis, recipes and certificates, not only the number.

## 10. Activation-aware basis compiler pipeline

The current exact finite pipeline is:

1. compile the complete declared typed generator set to `Q*`;
2. apply context-independent dominance: semantic factor maps, fine-level operation-term generation, fine-level semiring generation;
3. on `Q*`, search for additional quotient-level coarsening-natural reconstruction certificates;
4. delete all reconstruction-certified generators from the carrier search;
5. enumerate/represent the remaining forbidden coarse worlds and build the integer kill matrix;
6. solve the residual hitting-set problem for one or all minimum carrier bases;
7. emit private forbidden-world witnesses and, when available, generator-disjoint packing lower bounds;
8. separately choose a semantic reconstruction basis and explicit quotient recipes for all requested future generators.

The reference module uses exact bit masks and exhaustive finite set partitions. It makes no scalability claim for large carriers; Bell-number growth is itself a reason the next frontier should seek structured forbidden-world certificates rather than a larger brute-force optimizer.

## 11. Prior-art boundary

Minimum generating sets/rank of finite semigroups and transformation semigroups are established research topics. Generic hitting set/set cover and algebraic term/semiring generation are also standard. The R004 results above do not claim those generic problems or algorithms as inventions.

The project-local contribution is narrower: the exact forbidden-partition reduction for task-relative carrier preservation, activation-aware no-gos, the carrier/semantic basis split, coarsening-natural reconstruction criterion, and their placement behind the existing typed future-language compiler.

Historical novelty of the integrated package remains `NOVELTY_UNVERIFIED`.

## 12. Validation and next frontier

Committed regressions cover the four-state optimality certificate, contextual redundancy, pairwise-merge no-go, carrier/semantic strict gap and quotient-only operation reconstruction.

Independent validation additionally includes the **117,000** hitting-characterization cases, **102,375 / 43,940** unary quotient-reconstruction audit, and **20,480 / 1,560** Boolean-relation reconstruction audit described above.

No fresh full-repository CI or canonical-main status is claimed.

The next frontier is now sharply bounded:

> Can the compiler replace exhaustive enumeration of all forbidden coarse partitions by a smaller **structural obstruction basis** derived from the typed algebra itself, while remaining exact?

The pairwise-merge counterexample proves that arbitrary local pair tests are insufficient. Any compression of the forbidden-world universe must therefore come with a theorem explaining which larger mergers it implicitly certifies.
