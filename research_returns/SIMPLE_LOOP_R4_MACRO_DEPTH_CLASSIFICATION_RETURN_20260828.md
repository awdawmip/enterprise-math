# Research Return — Simple-loop blocking graph rank 4 and macro depth

- Task: `RS-SIMPLE-LOOP-R4-MACRO-DEPTH-CLASSIFICATION`
- Publication: `TP2-9AB05574C3CA5534CB39`
- Researcher-ID: `EM-SLR4-CCE75F`
- Claim: `chatgpt-slr4-20260828-1432`
- Execution branch: `research/simple-loop-r4-macro-depth-classification-em-slr4-cce75f`
- Base: `94b655850f2097901eef949d98b603b9bbf0e99e`
- Hard-target disposition: `SIMPLE_LOOP_R4_BLOCKING_MOTIF_AND_MACRO_DEPTH_EXACTLY_REFUTED`

## 1. Executive result

The blocking-object route survives, but the proposed `rank 4 -> depth 9` hierarchy does not.

1. There is a canonical label-equivariant blocking digraph `B(gamma)` whose edges are exactly the repeated-vertex obstructions to an area-raising rhombus swap.
2. Its natural blocker-rank is the number of blocked area-raising reflex corners. On a locally locked positive simple loop every reflex corner is blocked, hence `R(gamma)` equals the number of negative cyclic turns.
3. Consequently, for every locked positive simple loop,

   `number_of_cyclic_runs = 2 R(gamma) + 3`.

   Therefore `R=4` forces **11 runs structurally**, without enumeration.
4. The first rank-4 locked locus occurs at holonomy `H=8`. Up to cyclic rotation and global `C3` relabeling there are exactly **three** minimal rank-4 classes.
5. All three have `A2=F=30`, `I=4`, `Theta=+3`, 11 runs, blocker-level sequence `[1,7,1,7]`, and all three contain an H=6-type exact unlock packet `1332 -> 2331`.
6. For every one of the three classes the intrinsic macro depth is exactly **5**, not 9. A radius-4 exhaustive adjacent-transposition certificate finds no higher-area simple endpoint; at distance 5 the packet above gives a simple endpoint with `Delta A2=Delta F=+6`, `Delta I=+3`, `Delta Theta=0`.

Thus the `11` conjecture is true for a stronger invariant reason, while the `9` conjecture is killed at the first rank-4 locus. The corrected statement is:

`LOCKED + R=4 => 11 RUNS`, but `R` does **not** measure simple-to-simple macro depth; the first rank-4 classes have `d=5` and are composite with respect to the already known H=6 four-letter unlock.

## 2. Typing and source boundary

The proof uses the derived displacement carrier only as a carrier-incidence coordinate system. Write

`G_D = Z^3 / Z(1,1,1)`

and use the chart

`chi(a,b,c)=(a-c,b-c)`.

Thus the three positive step labels are represented for incidence calculations by

- `e1 -> (1,0)`,
- `e2 -> (0,1)`,
- `e3 -> (-1,-1)`.

This does **not** identify primitive native point addresses modulo diagonal shift, does not replace the directed native line gauge, and does not identify endpoint displacement with native line trace or Path-formal/BRC identity. `A_D` and `A_E` remain semantically distinct.

The taskbook's three historical journal references were not resolvable on the current `main` snapshot through their stated paths/commit IDs. Their numerical H=6 regression packet was therefore replayed independently from the exact word and formulas stated in the taskbook; no missing journal text is used as proof.

Tool-reuse gate: existing finite symmetry/orbit machinery and typed incidence/holonomy concepts are reused semantically. No existing executable tool was found whose contract performs this exact simple-loop blocker classification. The bounded checker is task-specific evidence, not a new global tool family.

## 3. Frozen blocking object

Let a positive closed word be

`w=g_0 ... g_{N-1}`

with each `g_i in {1,2,3}` and equal total counts `H` in the three labels. Let carrier vertices be

`p_0=0`, `p_{i+1}=p_i+e_{g_i}`, `p_N=p_0`,

computed in `G_D` (or in the faithful `chi` chart). For the simple loops considered here, the vertices `p_0,...,p_{N-1}` are distinct. Since these are unit edges of the triangular carrier 1-skeleton, this vertex self-avoidance is equivalent to an embedded simple lattice boundary.

A cyclic corner `i` is **area-raising reflex** when

`omega(e_{g_i},e_{g_{i+1}})=-1`.

Swapping the two adjacent letters changes `A2` by

`Delta A2 = -2 omega(e_{g_i},e_{g_{i+1}})=+2`.

Put `a=g_i`, `b=g_{i+1}`. The original two-edge diamond is

`p_i -> p_i+e_a -> p_i+e_a+e_b`.

The swapped diamond would use the alternate middle vertex

`q_i := p_i+e_b`.

Because all other boundary vertices are unchanged by the adjacent swap, and because a simple unit-edge triangular-lattice path has no nonvertex edge crossings, the swap is simple-admissible **iff** `q_i` is not already a boundary vertex.

### Definition: blocking digraph

`B(gamma)` is the directed bipartite incidence graph with:

- one corner node `c_i` for every area-raising reflex corner;
- one boundary-occurrence node `v_j` for every `p_j`;
- an edge `c_i -> v_j` exactly when `q_i=p_j`.

Each reflex corner has outdegree at most one because the source loop is simple and hence boundary vertices are unique.

The graph is invariant under translation, cyclic re-basing, and global `C3` relabeling. The labels `i,j` are presentation indices only; the object is the incidence relation between the reflex corner occurrence and the occupied alternate lattice vertex.

### Definition: blocker-rank

Define

`R(gamma) := |E(B(gamma))|`.

For a **locally locked** loop every area-raising reflex corner is blocked, so every reflex corner contributes exactly one edge and

`R(gamma) = number_of_reflex_corners`.

This definition is not tuned to 4 or 11; it exists for every simple positive loop.

## 4. Exact repeated-vertex blocker equation

Fix a reflex corner `i`, with `a=g_i`, `b=g_{i+1}`, and suppose its alternate vertex is blocked at `p_j`.

Let `n_{i->j}=(n_1,n_2,n_3)` be the count vector of the positively oriented cyclic boundary arc from `p_i` to `p_j`. Then

`p_j-p_i = e_b` in `G_D`.

Since the kernel of the lifted map is `Z(1,1,1)`, this is equivalent to the exact integer equation

`n_{i->j} - e_b = k(1,1,1)`

for one integer `k`. Nonnegativity and the fact that the boundary arc begins with `a != b` force

`1 <= k <= H-1`.

Therefore every blocker edge has the exact form

`n_{i->j} = e_b + k(1,1,1)`, `1 <= k <= H-1`,

with arc length `3k+1`.

The complementary boundary arc has count vector

`H(1,1,1)-n_{i->j}`
`= (H-k)(1,1,1)-e_b`
`= e_a+e_c+(H-k-1)(1,1,1)`,

where `{a,b,c}={1,2,3}`.

The conditions needed to exclude false blockers are therefore all explicit:

1. `omega(e_a,e_b)=-1` (only area-raising reflex corners are tested);
2. `q_i=p_i+e_b` is derived from the actual commuting diamond;
3. `q_i` must equal an already occupied boundary vertex `p_j`;
4. the boundary occurrence is unique by simplicity;
5. equivalently the oriented arc count must satisfy the exact diagonal-kernel equation above;
6. `k>=1`, so the forward blocking occurrence is nonlocal to the two-edge diamond.

The integer `k` is an invariant edge label, called the **forward blocker level** in this report.

## 5. Structural 11-run theorem

Let `n_+` be the number of positive nonzero cyclic run-boundary turns and `n_-` the number of negative ones. Same-label adjacencies lie inside runs and contribute zero to `Theta`.

For every positive simple loop in scope,

`Theta = n_+ - n_- = 3`.

The number of cyclic runs is

`r = n_+ + n_-`.

Hence

`r = 2 n_- + 3`.

For a locked loop, `n_-=R(gamma)`. Therefore

`boxed: r(gamma)=2R(gamma)+3`.

In particular,

`R=4 => r=11`.

This is an all-holonomy theorem in the frozen model. No census is used to prove the number 11.

## 6. H=6 regression replay

The taskbook regression word is

`w6 = 111112222233133233`

(`1^5 2^5 3^2 1 3^2 2 3^2`).

Exact replay gives

- `H=6`;
- `A2=F=22`;
- `I=3` from `F=2I+3H-2`;
- `Theta=+3`;
- 7 cyclic runs;
- two area-raising reflex corners, at zero-based positions `12` (`13`) and `14` (`32`).

Using `chi` coordinates:

- corner 12 has base `p_12=(3,3)`, alternate vertex `(2,2)=p_16`; its forward arc is `1332`, count `(1,1,2)=e3+1*(1,1,1)`, so blocker level `k=1`;
- corner 14 has base `p_14=(3,2)`, alternate vertex `(3,3)=p_12`; its forward count is `(5,6,5)=e2+5*(1,1,1)`, so `k=5=H-1`.

Thus `R=2` and the structural theorem gives `2R+3=7` runs exactly.

The packet

`1332 -> 2331`

produces the simple loop

`111112222233233133`

with `A2: 22 -> 28`, hence `Delta F=+6`, `Delta I=+3`, `Delta Theta=0`.

A shortest unrestricted adjacent-swap realization is

`1332 -> 3132 -> 3312 -> 3321 -> 3231 -> 2331`,

with `A2` increments `+2,+2,-2,+2,+2`. Every proper intermediate global loop is non-simple. The exact BFS certificate also finds no higher-area simple endpoint at adjacent-swap distance `1,2,3,4`; hence `d(w6)=5` under the intrinsic definition below.

## 7. First rank-4 classification

The structural theorem narrows rank 4 to exactly 11-run positive simple loops. Only after that reduction was a bounded exact atlas run for `H<=8`.

The checker fixes the first letter to `1`, which is complete modulo cyclic/C3 because every closed holonomy-H word has H occurrences of each label. It performs exact self-avoidance, `Theta=3`, 11-run, four-reflex, and blocker-equation tests, then quotients surviving words by cyclic rotation and global `C3` relabeling.

Results:

- `H=4,5,6,7`: no rank-4 locked representative;
- `H=8`: 72 first-letter-1 based representatives, collapsing to exactly 3 cyclic/C3 classes.

Canonical representatives are:

1. `111111222322122333133233`
2. `111111223221222331332333`
3. `111111223221222333133233`

All three satisfy

`H=8`, `A2=F=30`, `I=4`, `Theta=3`, `R=4`, `runs=11`.

Their blocker edges (zero-based indices) are:

### Class 1

- `c_9 (32) -> v_13`, base `(6,3)`, alternate `(6,4)`, level `k=1`, arc count `(1,2,1)`;
- `c_11 (21) -> v_9`, base `(5,3)`, alternate `(6,3)`, level `k=7`, arc count `(8,7,7)`;
- `c_18 (13) -> v_22`, base `(3,3)`, alternate `(2,2)`, level `k=1`, arc count `(1,1,2)`;
- `c_20 (32) -> v_18`, base `(3,2)`, alternate `(3,3)`, level `k=7`, arc count `(7,8,7)`.

### Class 2

- `c_8 (32) -> v_12`, base `(6,2)`, alternate `(6,3)`, level `k=1`, arc count `(1,2,1)`;
- `c_10 (21) -> v_8`, base `(5,2)`, alternate `(6,2)`, level `k=7`, arc count `(8,7,7)`;
- `c_17 (13) -> v_21`, base `(4,4)`, alternate `(3,3)`, level `k=1`, arc count `(1,1,2)`;
- `c_19 (32) -> v_17`, base `(4,3)`, alternate `(4,4)`, level `k=7`, arc count `(7,8,7)`.

### Class 3

- `c_8 (32) -> v_12`, base `(6,2)`, alternate `(6,3)`, level `k=1`, arc count `(1,2,1)`;
- `c_10 (21) -> v_8`, base `(5,2)`, alternate `(6,2)`, level `k=7`, arc count `(8,7,7)`;
- `c_18 (13) -> v_22`, base `(3,3)`, alternate `(2,2)`, level `k=1`, arc count `(1,1,2)`;
- `c_20 (32) -> v_18`, base `(3,2)`, alternate `(3,3)`, level `k=7`, arc count `(7,8,7)`.

Thus every first rank-4 motif has forward blocker-level sequence `[1,7,1,7]`; geometrically it contains two H=6-type short blocker packets rather than a new irreducible depth-9 primitive.

## 8. Intrinsic packet support and macro depth

A **simple-to-simple packet replacement** on `gamma` is a replacement of one cyclic contiguous subword `u` by `u'` such that:

1. `u` and `u'` have the same label multiplicity vector (hence preserve holonomy and the packet endpoints in the lifted carrier);
2. the source and resulting full closed words are both positive simple loops;
3. for an unlock, `A2(gamma')>A2(gamma)`.

The **packet support length** is the length of the shortest cyclic interval supporting that replacement. This is not an adjacent-swap distance.

Define the **macro depth**

`d(gamma)`

as the minimum adjacent-transposition distance, in unrestricted closed positive-word space, from any cyclic representative of `gamma` to any positive simple loop `gamma'` with the same label counts and `A2(gamma')>A2(gamma)`. Intermediate words are allowed to be non-simple. Global `C3` relabeling is free because it acts equivariantly on both endpoints and preserves the distance and all tested invariants.

This definition reproduces the H=6 depth `d=5` and does not encode `9` anywhere.

## 9. Exact rank-4 macro-depth refutation

Each of the three minimal rank-4 classes contains a cyclic `1332` packet for which

`1332 -> 2331`

is again globally simple. The exact global targets are:

1. `111111222322122333133233`
   -> `111111222322122333233133`;
2. `111111223221222331332333`
   -> `111111223221222332331333`;
3. `111111223221222333133233`
   -> `111111223221222333233133`.

For all three:

- packet support length = 4;
- adjacent-transposition distance of the displayed packet realization = 5;
- `A2=F: 30 -> 36`;
- `I: 4 -> 7`;
- `Delta Theta=0`.

The same five-swap factorization applies:

`1332 -> 3132 -> 3312 -> 3321 -> 3231 -> 2331`,

with global `(simple?, A2)` sequence

`(true,30), (false,32), (false,34), (false,32), (false,34), (true,36)`.

To prove sharpness, the checker explores every state at adjacent-transposition distance at most 4 from every cyclic representative. For each rank-4 class the exact newly reached state counts by distance are

- distance 1: 253;
- distance 2: 1,430;
- distance 3: 5,754;
- distance 4: 18,671;

and the count of higher-area simple endpoints is zero at each of those layers. At distance 5 there are 52,262 new states and 274 higher-area simple endpoints. Therefore

`d(gamma)=5`

for all three minimal rank-4 classes.

This is a direct exact counterexample to the hypothesis that the first genuine rank-4 obstruction forces strict macro depth 9.

## 10. What survives and what fails

### Survives

- A finite invariant blocker object exists.
- The repeated-vertex obstruction is exactly a diagonal-kernel arc equation.
- Blocker-rank is intrinsic and label-equivariant.
- The 11-run statement is true, and in fact follows universally from `Theta=3` once the loop is locked.

### Fails

- `blocker-rank = macro depth` or any affine rule suggested by `R=2 -> 5` and `R=4 -> 9`.
- The first rank-4 motifs are not new depth-9 simple-geometric primitives. They already contain the H=6 support-4 unlock packet.
- No new fundamental BRC generator is justified by this simple-subspace macro behavior.

## 11. All-holonomy macro-depth upper-bound attempt

The blocker equations alone do not presently give a proved all-holonomy constant upper bound. An edge label may have any

`1 <= k <= H-1`,

so the one-step obstruction object records where the alternate rhombus vertex is occupied but does not by itself certify that a chosen higher packet avoids every other boundary vertex.

A bounded adversarial extension was carried out separately from the proof-critical H<=8 atlas. It found locked examples with macro depths 6 at H=9 and 7 at H=10, so the corrected value `5` is **not** promoted to a universal all-holonomy bound. Conversely, no claim of an unbounded family or of global nonexistence/existence of some later `d=9` family is made here: those would require a new task centered on replacement-path collision chains rather than on rank-4 classification.

The decisive obstruction to extracting macro depth from the coarse blocker summary is that rank and blocker levels describe failure of single rhombus moves, while macro depth depends on collision-freeness of an entire replacement path. Even at fixed rank, distinct loops can have different macro depths. The next invariant must therefore retain interaction among blocker chords and candidate replacement trajectories, not only edge count.

This satisfies the required upper-bound attempt without converting bounded higher-H exploration into a universal theorem.

## 12. Machine certificate

Proof-critical machine replay is in:

- `artifacts/simple_loop_r4_macro_depth/check_simple_loop_r4.py`
- `artifacts/simple_loop_r4_macro_depth/atlas.json`

The checker independently verifies:

- the H=6 word, both exact blocker coordinates/equations, and the five-swap unlock;
- the structural run identity on every accepted rank-4 survivor;
- absence of rank-4 locked classes for H=4..7;
- exactly 72 first-letter-1 H=8 survivors and exactly 3 cyclic/C3 classes;
- all blocker levels and exact invariants of the three representatives;
- the common support-4 `1332 -> 2331` unlock;
- absence of higher-area simple endpoints at distances 1..4 and existence at distance 5.

Local replay result before repository freeze:

`PASS SIMPLE_LOOP_R4_BLOCKING_MOTIF_AND_MACRO_DEPTH_EXACTLY_REFUTED`.

## 13. Theorem-status table

| Required item | Status | Exact outcome |
|---|---|---|
| invariant `B(gamma)` | PROVED | directed reflex-corner -> occupied-alternate-vertex incidence graph |
| blocker equation | PROVED | `n_{i->j}=e_b+k(1,1,1)`, `1<=k<=H-1` |
| invariant rank | PROVED | `R=|E(B)|`; for locked loops equals reflex count |
| minimal rank-4 locus | CLASSIFIED | first at H=8; exactly 3 cyclic/C3 classes |
| 11-run claim | PROVED STRONGLY | locked theorem `runs=2R+3` |
| first-rank-4 depth-9 claim | REFUTED | all three minimal rank-4 motifs have `d=5` |
| sharp unlock | PROVED | support 4, `1332->2331`, distance 5, `Delta F=6`, `Delta I=3` |
| universal depth bound | OPEN | blocker equations alone do not control replacement-path collisions; no universal bound asserted |
| new BRC primitive | REJECTED | simple-subspace macro primitivity is not Path-formal/BRC algebraic primitivity |

## 14. Recommended next route

Do **not** open a task that merely asks for larger-holonomy rank census. The next mathematically justified object is a **replacement-collision dependency complex**: augment each blocker edge with the finite set of boundary vertices encountered by candidate minimal packet trajectories, and study whether acyclic/nested dependency chains control macro depth. The first target should be to explain exact H=9/H=10 depths 6 and 7 structurally, then either derive a growth theorem or produce a true unbounded family.

The current task is terminal at task scope because its first-rank-4 hard question is exactly classified and the numerical `9` hypothesis is killed without changing definitions.
