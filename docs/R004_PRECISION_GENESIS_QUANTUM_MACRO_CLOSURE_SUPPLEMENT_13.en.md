# R004 precision genesis — Supplement 13: typed relation compiler and semantic activation cascades

Status: `PROVED_WIP + EXECUTABLE_CHECKED + PRIOR_ART_SPECIALIZATION + CORRECTED_BY_SUPPLEMENT_14 + P023/A4_BOUNDARY`  
Parent: `R004_PRECISION_GENESIS_QUANTUM_MACRO_CLOSURE_SUPPLEMENT_12.en.md`  
Owner branch: `research/r004-precision-genesis-closure-20260810`

Supplement 12 established that a future kernel is only an equality IR: typed quotient semantics cannot in general be reconstructed from that kernel alone. This supplement makes finite relation/witness stabilization executable. Supplement 14 later corrects one over-broad comparison sentence from the first version of this document: **raw meet is guaranteed for different observations under one fixed operation family, not for arbitrary independently compiled operation languages.** Different operation families can cross-activate and require a common fixed point.

The relation results below remain unchanged.

## 1. Typed relation channels

Let `X` be a finite state carrier and `P` a current partition. A typed relation channel `c` consists of a declared commutative monoid `(M_c, op_c, 0_c)` and edge/witness values `w_c(x,y) in M_c`.

For source state `x` and target block `B in P`, define

`Sigma_(c,P)(x,B) = op_(y in B) w_c(x,y)`.

A partition is typed-relation stable when states in the same source block have identical aggregate vectors over every declared channel and every current target block.

Common instances are:

- MAY support: `(Bool, OR, False)`;
- witness multiplicity: `(N_0,+,0)`;
- witness label/class set: finite sets under union;
- products of monoids for simultaneous semantics.

Generic weighted/monoid partition refinement is prior art; R004 uses it as a typed future-language specialization.

## 2. R004-COMP-T11 — unique coarsest stable refinement

Starting from an initial observation partition `P_0`, split each source block by its complete typed relation signature against the **current** target blocks, and repeat.

Each strict round raises the number of blocks, so termination occurs in at most

`|X|-|P_0|`

strict rounds.

The terminal partition `P_*` is the unique coarsest typed-relation-stable refinement of `P_0`.

Proof. Let `Q` be any stable refinement of `P_0` and suppose inductively that `Q` refines `P_n`. Every target block of `P_n` is a union of `Q`-blocks. Equality of monoid aggregates on each `Q`-block therefore aggregates to equality on every `P_n` block. Hence two states identified by `Q` remain identified by the next signature refinement, so `Q` refines every `P_n` and the terminal `P_*`.

## 3. R004-COMP-T12 — semantic factor-map monotonicity

Suppose channel semantics `M` and `N` are related by a monoid homomorphism `phi:M->N`, with `N` edge values obtained by pointwise application of `phi` to the `M` values.

Then every `M`-stable partition is `N`-stable and

`Compiler_M(P_0)` refines `Compiler_N(P_0)`.

Examples:

- COUNT -> MAY by `n -> (n>0)`;
- LABEL-SET -> MAY by `S -> (S nonempty)`.

This gives a structural information order between typed future semantics without reducing precision to one scalar.

## 4. R004-COMP-CE10 — equal class count does not imply equal typed precision

Take states `X={x,y,z,a,b}` and witnesses:

- `x -> a` label `p`;
- `x -> b` label `q`;
- `y -> a` label `p`;
- `y -> b` label `p`;
- `z -> a` label `p`;
- `a,b` have no outgoing witnesses.

From the universal initial observation:

- MAY gives `{{x,y,z},{a,b}}` — 2 classes;
- COUNT gives `{{x,y},{z},{a,b}}` — 3 classes;
- LABEL-SET gives `{{x},{y,z},{a,b}}` — 3 classes;
- COUNT+LABEL-SET gives `{{x},{y},{z},{a,b}}` — 4 classes.

COUNT and LABEL-SET therefore have the same class count but incomparable partitions. Class count is only a derived complexity statistic; typed precision is structural.

## 5. R004-COMP-T13 — corrected fixed-operation-family observation meet law

Fix one total finitary algebra `A`. Let `C_A(P)` be the largest `A`-congruence contained in observation kernel/partition `P`.

For two observation partitions `P,Q`,

`C_A(P meet_raw Q) = C_A(P) meet_raw C_A(Q)`.

This is ordinary congruence-lattice mathematics: both closed kernels are congruences for the **same** algebra, and intersections of congruences for one algebra remain congruences.

The first version of Supplement 13 incorrectly allowed this sentence to be read as applying to different operation languages. Supplement 14 supplies a four-state counterexample and an arbitrary-length two-operation ping-pong family. The correct compiler rule is therefore:

- same fixed operation family + different observations: raw-meet theorem above;
- different operation families: compile to a common fixed point unless a stronger commutation certificate is proved.

## 6. R004-COMP-CE11 — relation tasks can activate after target geometry is refined

Take `X={0,1,2}` with universal initial partition and COUNT semantics.

Channel `A` has one witness `0->1`.

Channel `B` is the directed cycle `0->1`, `1->2`, `2->0`.

Separately:

- `A` compiles to `{{0},{1,2}}`;
- `B` leaves the universal partition stable.

Their raw common refinement remains `{{0},{1,2}}`, but it is not jointly stable. Once `A` exposes target `{0}`, channel `B` distinguishes states `1` and `2` because their witnesses land in different current target blocks. The joint compiler reaches the discrete partition.

Thus one typed requirement can activate another by changing the quotient geometry on which that requirement is evaluated.

## 7. R004-COMP-CE12 — even one relation channel can fail raw common-refinement closure

On five states use the loopless graph

- `0 -> 2,3`;
- `1 -> 2,3`;
- `2 -> 0,1`;
- `3 -> 0,1`;
- `4 -> 0,1`.

Under COUNT semantics both

`P={{0,2,4},{1,3}}`

and

`Q={{0,3,4},{1,2}}`

are stable. Their raw common refinement

`{{0,4},{1},{2},{3}}`

is not stable and must be refined to the discrete partition.

All loopless directed simple graphs on `n<=4` were exhaustively checked and no same-channel COUNT raw-meet failure was found. The displayed five-state witness is therefore minimal within that bounded class.

## 8. R004-COMP-T14 — stable common refinement requires stabilization

For a fixed typed relation language `W`, let `Stab_W(P)` be the unique coarsest stable refinement of `P`.

`Stab_W` is refinement-extensive, monotone and idempotent. For already stable `P,Q`, the stable common refinement is

`Stab_W(P meet_raw Q)`.

The five-state witness proves that the final stabilization cannot be deleted in general.

Balanced-equivalence and weighted-network theory already contain closely related stable-lattice mathematics; this is a compiler control rule, not a generic novelty claim.

## 9. Corrected compiler architecture consequence

The current lesson is **not** “operations are one-pass while relations need fixed points.”

The correct architecture is:

1. every typed semantic family supplies a closure/stabilization obligation on the current partition;
2. a raw one-pass combination is justified only by an explicit theorem for that fixed semantic family, such as the fixed-algebra congruence meet law;
3. different semantic families — including two different total operation languages — may cross-activate and must otherwise be solved by a least common fixed point;
4. quotient-relative relation aggregation has the additional stronger pathology that even two stable partitions for one fixed channel need not be raw-intersection stable.

Supplement 14 implements the resulting mixed fixed-point dispatcher and adds legality/semiring descent certificates.

## 10. Validation retained from this generation

Independent exhaustive verification checked:

- COUNT relation compiler/oracle on all loopless directed simple graphs with `n<=4` and all initial partitions: **61,769** cases, zero mismatches;
- MAY on the same family: **61,769** cases, zero mismatches;
- COUNT-result refinement of MAY-result on the same **61,769** cases: zero violations;
- all **4,165** loopless directed simple graphs on `n<=4`: no same-channel count-stable raw-meet failure;
- the displayed five-state graph: raw meet fails and stabilization yields the discrete partition.

Supplement 14 adds the operation-side correction and larger mixed validation matrix.

## 11. Ownership and prior-art boundary

Established prior mathematics includes weighted/monoid transition systems, weighted bisimulation, balanced/equitable partitions, coalgebraic partition refinement, balanced-equivalence lattices and congruence lattices of algebras.

R004's project-local contribution remains the typed Enterprise Math placement, factor-order/counterexample package and cross-owner reduction. Generic mother ownership stays with P023/A3/A4; historical novelty remains `NOVELTY_UNVERIFIED`.
