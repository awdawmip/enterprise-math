# R055 — Fixed-N Gravity Relaxation and Self-Centered Shape Formation

Researcher-ID: `EM-R055-4C2A71`  
Task: `RS-R055-FIXED-N-GRAVITY-RELAXATION-SELF-CENTERED-SHAPE`  
Taskbook source: `18072ad7a3ca50728b23e0fc21478b98ed027631`  
Frozen packet source: `73e48ac77f403dc468cdea3458e14d10130386e0`  
Status: `COMPLETED RESEARCH CHECKPOINT / NOT CANONICAL / DRIVER REVIEW REQUIRED`

## 1. Executive result

R055 gives a split answer.

1. **The fixed-N quadratic gravity objective itself has a disk limit at global optimum.** After the theorem/counterexample ledger and strict holdout were frozen, the post-freeze comparison layer yields a proof: every global `G` minimizer, represented by the union of triangular-lattice Voronoi cells, centered at its own centroid and area-normalized, converges in normalized symmetric difference to the equal-area Euclidean disk. A quantitative bound `O(N^{-1/4})` follows from moment stability plus an explicit lattice disk-approximant construction.
2. **The local D1 relaxation does not select a unique shape.** Exact exhaustive truth already fails at `N=6`: there are three D1 local minima, two still improvable by D2. Initial-condition independence and tie-break independence also fail at `N=6`.
3. **D1 metastability survives asymptotically.** Every centered shell `H_r` is a D1 strict local minimum. For every `r>=6` it admits a strict D2 improvement, so infinitely many centered-shell counts have multiple D1 attractors.
4. **There is no unique D1 terminal limit shape.** Centered-shell D1 terminals converge to a regular hexagon, while global-G minimizers are themselves D1 terminals and converge to a disk. Thus D1 terminal states have at least two distinct subsequential limit shapes.
5. **D2 is a useful nonlocal diagnostic, not a uniqueness oracle.** Construction and holdout multi-starts produce multiple D2 terminal classes at several N. This is bounded evidence about D2 dynamics, not a global-optimum theorem.
6. **Gravity moment, raw lattice boundary, second-moment anisotropy, radial dispersion and directional imbalance are genuinely different objectives.** Exact accepted moves exist where `G` strictly decreases while each of the four other diagnostics worsens. Global `G`- and `P_edge`-minimizer sets already differ at `N=6`.
7. **No classical circle, radius, circumference target, teacher center, tangent target or classical pi participated in relaxation or holdout.** The Euclidean disk, regular hexagon and classical pi were opened only after the frozen theorem/counterexample ledger and strict holdout were complete.

The narrow mother-question answer is therefore:

> fixed mass plus centroid feedback does create a meaningful self-centered compaction objective, but the frozen local boundary-slide law does **not** generate one reproducible terminal shape. Locality and lattice metastability survive; the disk appears as the global objective limit, not as the unique D1 dynamical attractor.

## 2. Isolation and semantic typing

R055 was executed as a new mother problem parallel to R054. No R054 frozen scoring, holdout or collapse target was consumed by the relaxation, holdout or post-freeze comparison engines.

The triangular lattice embedding, centroid and quadratic moment are the task's declared operational geometry. Under Native-Semantics Gate V3:

- lattice coordinate pairs are an implementation/declared task carrier;
- D1/D2 are derived operational dynamics;
- centroid, moments and diagnostic scalars are readouts;
- Euclidean disk/regular-hex comparison is post-freeze classical comparison;
- no result here promotes centroid, Euclidean geometry or quadratic gravity to N0-native ontology.

## 3. Stage 0 — frozen protocols

Active exact-byte freezes:

- `R055_RELAXATION_PROTOCOL_SHA256 = aa69f2bc31cb9b5ec574a85de2879b9f8f765cfdfdb6dd0cbfc625cf8feed683`
- `R055_MOVE_ENERGY_REGISTRY_SHA256 = 83d546105a3fa721ba5cadea9a1bbf217a1661fdf0d1560fcdccc6d4c9d29ceb`
- `R055_INITIAL_STATE_REGISTRY_SHA256 = 5de0e7ae6ff89cf81342f6c18125eb1eebd78c4725c0324acee2893552acd7f2`

A pre-trajectory checker found two mechanical specification defects in the first initial-state registry: the original `HEX_SHELL_GROWTH` ring walk could temporarily leave the declared graph shell, and the EDEN text did not explicitly include hole-free filtering in its per-step candidate rule. No construction or holdout trajectory had been run. The registry was corrected before consumption. The unconsumed superseded hash is preserved as provenance:

`f1ce65671f28fa661e2588cb2eef42e62e510553f11b8911eda21fd20d2f6250`

No later trajectory-driven protocol edit occurred.

## 4. Exact algebra

Let `S=sum_{x in C} x`, `g=S/N`, and use the triangular-lattice quadratic form

`Q(a,b)=a^2+ab+b^2`.

The exact identities are:

`I2(C)=sum_x ||x-g||^2 = (1/N) sum_{x<y} ||x-y||^2`,

hence

`G(C)=N I2(C)=sum_{x<y} Q(x-y)`.

Therefore `G` is an exact integer.

For one replacement `u -> v`, write `d=v-u` and let `L` be the bilinear polarization of `Q`,

`L((a,b),(c,d))=2ac+ad+bc+2bd`.

Then

`Delta G = N(Q(v)-Q(u)) - L(S,d) - Q(d)`.

The implementation still recomputes the full new centroid sum and full exact `G` after every accepted move; the incremental formula is used for candidate ordering/checking, not as permission to freeze the old center.

Strict-descent termination follows because, at fixed N modulo translation, a connected N-site cluster has bounded graph diameter and hence only finitely many translation classes; D6 quotienting only reduces that finite set. Every accepted move strictly lowers nonnegative integer `G`.

## 5. Exact topology update

A generation-critical performance theorem was proved rather than approximated.

Start from connected hole-free `C`. Delete boundary cell `u` and let `R=C\{u}` have `k` occupied connected components. For an empty insertion site `v`, assume `v` touches every one of the `k` components, so the new occupied cluster is connected. Inspect the six neighbors of `v` in cyclic order within `R`, and let `c` be the number of occupied cyclic runs. Then:

> `C'=(C\{u}) union {v}` is hole-free iff `c=k`.

The final C++ engine obtains `k` and component membership from one Tarjan/low-link articulation computation per state, then checks each candidate locally. The criterion was independently compared with full padded flood-fill truth for all candidate relocations over every hole-free class at `N=2..8`:

- candidate relocations checked: `259,136`;
- mismatches: `0`.

This acceleration does not change the legal move set.

## 6. Stage A — exhaustive small-N truth

All connected free polyhex classes modulo translation+D6 were enumerated through `N=12`; the frozen hole-free predicate was then applied.

| N | connected classes | hole-free classes | global G | global P_edge | D1 local minima | D1 minima still improvable by D2 | G/P minimizer sets equal? |
|---:|---:|---:|---:|---:|---:|---:|:---:|
|1|1|1|0|6|1|0|yes|
|2|1|1|1|10|1|0|yes|
|3|3|3|3|12|1|0|yes|
|4|7|7|8|14|1|0|yes|
|5|22|22|17|16|1|0|yes|
|6|82|81|29|18|3|2|**no**|
|7|333|331|42|18|3|2|yes|
|8|1,448|1,435|69|20|4|3|yes|
|9|6,572|6,505|99|22|5|4|**no**|
|10|30,490|30,086|135|22|5|4|yes|
|11|143,552|141,229|181|24|6|5|**no**|
|12|683,101|669,584|228|24|9|8|yes|

### 6.1 Smallest exact D1/D2 obstruction

At `N=6` there are three D1 local minima.

- Global G minimum: `G=29`; it is D2-minimal.
- Trap 1: `G=33`; D2 relocation `(0,0)->(2,0)` gives `Delta G=-4` and reaches `29`.
- Trap 2: `G=30`; D2 relocation `(0,0)->(1,2)` gives `Delta G=-1` and reaches `29`.

Thus `D1_LOCAL_MINIMUM => D2_RELOCATION_MINIMUM` is false, with exact smallest witness `N=6` in the exhaustive range.

### 6.2 Tie-break and initial-state dependence

A single exact `N=6` initial class

`{(0,0),(0,1),(0,2),(0,3),(1,0),(2,0)}`

reaches different D1 terminals under frozen deterministic tie rules: T0 reaches the `G=33` trap, while T1/T2 reach the `G=30` trap. Exact oriented T2 basins were computed through `N=11`; the `N=12` oriented-T2 all-state basin pass was explicitly marked `COMPUTATIONAL_CUTOFF` rather than replaced by a quotient approximation. T0/T1 basins and all D1 minima at `N=12` are exact.

## 7. Stages B/C — construction dynamics

Construction N:

`[19,31,37,53,61,79,91,113,127,151,169,199,217]`.

For every N, all eight frozen initial families were run under primary D1/T0 to terminality. D2/T0 was then run from every frozen initial state and every corresponding D1-primary terminal. Alternative deterministic ties were run until a concrete path-dependence witness was established for each N.

| N | centered shell count? | D1 primary terminal classes | distinct D1 G values | D1 terminals improved by D2 | observed D2 G values | D1 centroid classes | tie dependent? |
|---:|:---:|---:|---:|---:|:---|---:|:---:|
|19|yes|7|7|6|912|7|yes|
|31|no|7|7|6|4092, 4106|7|yes|
|37|yes|7|7|6|6882|7|yes|
|53|no|7|7|8|20515, 20519|7|yes|
|61|yes|7|7|6|31110|7|yes|
|79|no|8|8|8|67932|8|yes|
|91|yes|7|7|6|103740, 103798, 103875|7|yes|
|113|no|8|8|8|198743, 198760|8|yes|
|127|yes|7|7|8|282283, 282318|7|yes|
|151|no|8|8|8|473838, 474379|8|yes|
|169|yes|7|7|8|665189, 665244|7|yes|
|199|no|8|8|8|1084152|8|yes|
|217|yes|7|7|8|1408170, 1408194|7|yes|

These are bounded dynamics classifications, not global-optimum claims.

### 7.1 Centered-shell theorem

Define

`H_r={(a,b): max(|a|,|b|,|a+b|)<=r}`,

`N_r=1+3r(r+1)`.

By D6 symmetry `S(H_r)=0`.

**Theorem 1 — D1 trap for every shell.** For every `r>=1`, `H_r` is a strict D1 local minimum. Any D1 move to an empty adjacent site crosses the shell and has `Q(v)-Q(u)>=r+1`, while `Q(v-u)=1`; hence

`Delta G >= N_r(r+1)-1 > 0`.

**Theorem 2 — D2 escape from every sufficiently large shell.** For every `r>=6`, remove `u=(-r,0)` and add

`v=(ceil((r+1)/2), floor((r+1)/2))`.

The relocation is connected and hole-free. If `r=2k`,

`Delta G=-2k(6k^3-15k^2-8k-1)<0`,

and if `r=2k+1`,

`Delta G=-(2k+1)(6k^3-6k^2-17k-7)<0`.

Therefore exact D1 metastability persists along infinitely many N.

The construction data reflect the threshold: complete shells at `N=19,37,61,91` are D2-stable in the tested reference, while shells at `127,169,217` are strictly improved by D2. The theorem establishes D2 improvability for every `r>=6`, not only these three observations.

## 8. Stage D — objective separation

The following remained separate throughout relaxation:

1. `G` — quadratic gravity moment;
2. `P_edge` — raw occupied-empty cut edges;
3. `A2` — second-moment anisotropy;
4. boundary squared-radius dispersion;
5. six-direction boundary imbalance.

Exact accepted-move counterexamples show that strict `G` decrease can worsen each other diagnostic. The construction witnesses occur already at `N=19`; strict holdout independently reproduces all four kinds, including `P_edge`, radial dispersion and directional imbalance worsening at step 2 of the `N=43 HEX_SHELL_GROWTH` trajectory.

The global minimizer sets for `G` and `P_edge` are already unequal at `N=6`; additional exact set inequality occurs at `N=9` and `N=11`. The stronger all-N inclusion/equivalence questions are not inferred from this finite atlas.

## 9. Stage E — theorem/counterexample freeze

Before any strict holdout N or external disk/hex comparison was opened:

`R055_THEOREM_COUNTEREXAMPLE_LEDGER_SHA256 = 159ba8ed8e664522fec5fa9771b8efc7630d0b0c78ca5a2f67e7c33c724ac660`.

At freeze time:

- pairwise identity, exact replacement delta, termination, local hole criterion and centered-shell theorems were `PROVED`;
- D1/D2 equivalence, initial independence, tie independence, unique D1 terminal shape, unique D1 centroid class and G/P minimizer-set equality had counterexamples;
- global-G limit shape and D1 terminal limit shape remained `OPEN`;
- holdout was unopened;
- Euclidean disk/regular-hex comparison was unopened;
- classical pi had not been used.

The frozen ledger was not rewritten after later theorems. Stage-H results live in `R055_POSTFREEZE_THEOREM_ADDENDUM.json`.

## 10. Stage F — strict holdout

Strict holdout N:

`[43,67,103,139,181,241,301]`.

All frozen initial families, primary D1 rule, D2 reference, tie-breaks and diagnostics were used unchanged.

| N | D1 primary terminal classes | D1 terminals improved by D2 | combined observed D2 classes | observed D2 G values | D1 centroid classes | tie dependent? |
|---:|---:|---:|---:|:---|---:|:---:|
|43|8|8|2|10924, 10942|7|yes|
|67|8|8|1|41363|8|yes|
|103|7|8|2|150281|7|yes|
|139|8|8|1|369653|8|yes|
|181|8|8|2|816791|8|yes|
|241|8|8|1|1928999|8|yes|
|301|7|8|1|3757189|7|yes|

The strict-holdout artifact hash is

`c72b4988e9b00d022b8524b919768319876c8d11ec313933b9398efa002301f8`.

Holdout verdicts:

- D1 multi-attractor behavior survived `7/7`;
- tie-break dependence survived `7/7`;
- every one of the `56` primary D1 holdout terminals was further improved by D2;
- D1 unique centroid class failed throughout;
- D2 unique-attractor behavior did **not** survive: multiple observed D2 classes remain at `N=43,103,181`;
- objective monotonicity separation was independently reproduced.

All seven holdout sizes are off centered-shell counts, so centered shells were not the only source of metastability.

## 11. Stage G — post-freeze disk/hex comparison

Only after Sections 9 and 10 were frozen was the classical comparison layer opened.

Comparison geometry:

- each lattice site is represented by its triangular-lattice Voronoi regular hexagon of area `sqrt(3)/2`;
- the cluster region is the union of those cells;
- the disk is the equal-area Euclidean disk centered at the final centroid;
- regular-hex comparison uses an equal-area baseline and a deterministic numerical alignment/rescaling search minimizing symmetric difference;
- second moment, symmetric difference, Hausdorff-style boundary distance, normalized radial deviation and frozen lattice anisotropy diagnostics are all retained separately.

External comparison artifact:

`R055_EXTERNAL_SHAPE_COMPARISON_SHA256 = 10a043e10ca7ce27d3b72187c236b9b481de29e483db3a621417dd1e9ad8acc5`.

It covers all `205` distinct translation+D6 terminal classes actually generated by construction/holdout primary, D2 reference and alternative-tie controls.

### 11.1 Lowest-G observed D2 references

The table below deliberately isolates the lowest-G D2 terminal observed at each N, rather than averaging obvious metastable traps into the shape comparison. `SD` is normalized symmetric difference; `HD` is Hausdorff boundary discrepancy normalized by the equal-area disk radius.

| N | min observed D2 G | disk SD | best-hex SD | SD winner | disk HD | hex HD | HD winner | A2 |
|---:|---:|---:|---:|---:|---:|---:|:---:|---:|
|19|912|0.1164|0.0637|hex|0.7477|0.7037|hex|0|
|31|4092|0.1493|0.1216|hex|0.8025|0.7674|hex|0|
|37|6882|0.0914|0.0465|hex|0.8192|0.7737|hex|0|
|43|10924|0.1187|0.1209|disk|0.8326|0.7858|hex|0.002249|
|53|20515|0.1150|0.1110|hex|0.6959|0.6583|hex|0.003820|
|61|31110|0.0803|0.0365|hex|0.7184|0.6722|hex|0|
|67|41363|0.0961|0.1090|disk|0.6382|0.5959|hex|0.002627|
|79|67932|0.0939|0.0943|disk|0.5631|0.5357|hex|2.27e-5|
|91|103740|0.0803|0.0300|hex|0.5844|0.5499|hex|0|
|103|150281|0.0733|0.0844|disk|0.5670|0.5325|hex|0.000424|
|113|198743|0.0752|0.0879|disk|0.4670|0.4607|hex|0.001006|
|127|282283|0.0733|0.0901|disk|0.4739|0.4314|hex|0.001599|
|139|369653|0.0636|0.0797|disk|0.4757|0.4400|hex|0.000503|
|151|473838|0.0590|0.0728|disk|0.4132|0.3875|hex|0|
|169|665189|0.0652|0.0796|disk|0.4147|0.4361|disk|0.000174|
|181|816791|0.0578|0.0789|disk|0.4325|0.4122|hex|8.62e-5|
|199|1084152|0.0458|0.0759|disk|0.3764|0.3895|disk|0|
|217|1408170|0.0563|0.0876|disk|0.3684|0.3907|disk|0.000332|
|241|1928999|0.0539|0.0763|disk|0.3163|0.3539|disk|0.000280|
|301|3757189|0.0453|0.0800|disk|0.2908|0.3293|disk|4.17e-5|

This bounded data is compatible with increasingly disk-like low-G nonlocal references, especially in symmetric difference from `N>=103` in this frozen set, but D2 is not proved globally optimal and its own multiple terminal classes remain. No D2 limit-shape theorem is claimed from the table.

## 12. Stage H — post-freeze asymptotic theorem

The frozen ledger's two open limit-shape questions can be resolved differently after the comparison gate opens.

### 12.1 Exact transfer from lattice G to continuum polar moment

Let `V` be one triangular-lattice Voronoi cell. Its area is

`alpha=sqrt(3)/2`,

and its centered polar moment is

`J_V=5 sqrt(3)/72`.

For the Voronoi union `Omega_C` of an N-cell cluster,

`J(Omega_C;g(C)) = alpha I2(C) + N J_V = alpha G(C)/N + N J_V`.

Thus at fixed N, minimizing lattice `G` is **exactly equivalent** to minimizing the continuum polar moment over admissible Voronoi unions. The disk is not inserted into the move law; it appears now as an external minimizer of the transferred moment problem.

### 12.2 Quantitative moment stability

For any measurable planar `Omega` of area `A` with centroid `g`, let `D` be the equal-area disk centered at `g`. If `m=|Omega\D|=|D\Omega|=|Omega Delta D|/2`, the cheapest possible exchange of area `m` across the disk boundary is an adjacent inner/outer annulus. Therefore

`J(Omega;g)-A^2/(2 pi) >= m^2/pi = |Omega Delta D|^2/(4 pi)`.

### 12.3 Feasible lattice disk approximants

Let

`S_m={x in Lambda: Q(x)<=m}`,

and take the smallest integer `m` for which `|S_m|>=N`. Keep all sites with `Q<=m-1` and enough sites from the outer level `Q=m` to obtain exactly N cells.

- The set is connected because every nonzero lattice site has a nearest-neighbor step of smaller Q.
- It is hole-free: `S_m` has a Q-increasing path from every exterior site to infinity; removed outer-shell sites each touch the old exterior by a Q-increasing neighbor.
- With triangular-lattice covering radius `1/sqrt(3)`, the Voronoi union lies between disks whose radii differ by `O(1)`.

Hence its symmetric-difference area from an equal-area disk is `O(sqrt(N))`, and its moment excess is `O(N^{3/2})`.

### 12.4 Global-G disk limit

A global G minimizer cannot have larger transferred polar moment than the feasible disk approximant. Combining the `O(N^{3/2})` upper excess with quantitative moment stability and area `A=Theta(N)` gives

`|Omega_N Delta D_N| / |Omega_N| = O(N^{-1/4}) -> 0`.

Therefore:

`GLOBAL_G_MINIMIZER_LIMIT_SHAPE = LIMIT_SHAPE_PROVED (EUCLIDEAN DISK, POST-FREEZE COMPARISON LAYER)`.

This theorem does not say finite-N minimizers are unique.

### 12.5 D1 has two distinct subsequential limit shapes

Every global-G minimizer is automatically a D1 terminal state, so the preceding theorem supplies a D1-terminal subsequence converging to a disk.

Separately, every centered shell `H_r` is a D1 terminal state. The scaled center sets `H_r/r` converge to the axial regular hexagon, and adding fixed-size Voronoi cells changes the boundary only by `O(1/r)` after rescaling. Thus the centered-shell D1-terminal subsequence converges to a regular hexagon.

The equal-area disk and regular hexagon have positive symmetric difference. Therefore:

`D1_TERMINAL_LIMIT_SHAPE = LIMIT_SHAPE_COUNTEREXAMPLE_FOUND`.

Equivalently:

`LOCAL_SLIDE_METASTABILITY_PREVENTS_UNIQUE_D1_LIMIT_SHAPE`.

Post-freeze theorem addendum hash:

`53d357043abf57fbb75694b9d6e7e314a25fd7ecb873cf383b0135b7984f5c0a`.

## 13. Centroid classification

The centroid is never frozen; its exact axial numerator `S_t` is recomputed from all N cells after every accepted move. Final centroids are recorded modulo lattice translations and D6.

Small-N exact minima occupy several rational residue/stabilizer classes, and construction/holdout D1 terminals exhibit many centroid classes per N. Thus no theorem supports one universal finite set of special centroid residues for all terminal dynamics. The correct R055 status is:

- unique D1 centroid class: `COUNTEREXAMPLE`;
- universal finite special-class characterization: `OPEN`;
- asymptotic global-G centroid-centered shape: disk theorem holds after translating each minimizer to its own centroid.

## 14. Checker and reproducibility

Final combined trajectory set:

- construction D1 primary: `104` rows;
- construction D2 references: `208` rows;
- construction alternative-tie controls: `30` rows;
- holdout D1 primary: `56` rows;
- holdout D2 references: `112` rows;
- holdout alternative-tie controls: `18` rows;
- total terminal records: `528`;
- distinct translation+D6 terminal classes: `205`;
- total accepted moves: `433,531`.

Independent full arithmetic replay recomputed, from the actual occupied set after every accepted move:

- cell count/site replacement;
- D1 nearest-neighbor condition `Q(v-u)=1`;
- all-N centroid sum;
- exact full `G=N sum Q(x)-Q(S)`;
- recorded `Delta G`;
- strict descent.

Result: `433,531 / 433,531 PASS`.

Initial and terminal states of all trajectory rows received full connectivity/hole flood checks. Per-move topology in the generation engine uses the proved Tarjan/local-run criterion, with the independent `259,136`-candidate flood-fill regression described above.

C++ engine semantic-equivalence checks against the earlier full flood/reference implementation passed on:

- all 8 `N=19` primary trajectories;
- all 8 `N=43` primary trajectories;
- all three ties for the `N=31 L_SHAPE_OR_WEDGE` witness.

Unit tests: `10/10 PASS`.

CI/workflow status was not queried because ordinary L1/L2/L3 research has zero routine workflow-query budget: `CI_NOT_REQUIRED_FOR_RESEARCH`.

## 15. Main theorem/counterexample status at completion

| Question | Final R055 status |
|---|---|
| exact centroid/pairwise identity | `PROVED` |
| exact one-replacement Delta G | `PROVED` |
| strict-descent termination | `PROVED` |
| D1 minimum always D2-minimal | `COUNTEREXAMPLE`, smallest exhaustive witness N=6 |
| initial-condition independence | `COUNTEREXAMPLE` |
| tie-break independence | `COUNTEREXAMPLE` |
| unique finite D1 terminal shape | `COUNTEREXAMPLE` |
| unique D1 centroid class | `COUNTEREXAMPLE` |
| D2 unique terminal under frozen multi-starts | `FALSE AS BOUNDED OBSERVATION`; not an all-state theorem |
| global G/P_edge minimizer-set equality | `COUNTEREXAMPLE` at N=6 |
| G monotone-improves P_edge/A2/radial/directional diagnostics | `COUNTEREXAMPLE` for every diagnostic |
| centered H_r is D1 terminal | `PROVED` for all r>=1 |
| centered H_r is D2-improvable | `PROVED` for all r>=6 |
| D1 metastability persists on infinite N | `PROVED` |
| global-G limit shape | `LIMIT_SHAPE_PROVED: disk` post-freeze |
| unique D1 terminal limit shape | `LIMIT_SHAPE_COUNTEREXAMPLE_FOUND: disk + regular-hex subsequences` |
| D2 terminal limit shape | `OPEN_WITH_BOUNDED_EVIDENCE` |
| raw-P_edge global limit shape | `OPEN in R055` |
| universal finite centroid symmetry-class theorem | `OPEN` |

## 16. Interpretation boundary

R055 tests one explicit equal-mass triangular-lattice relaxation model. It does not establish that the physical universe is triangular-lattice, that physical gravity is quadratic, or that centroid is a native primitive.

The strongest justified structural statement is narrower:

> The quadratic fixed-mass objective has an asymptotically disk-shaped global optimum, but local strict boundary sliding does not reliably find or uniquely select it. The same frozen D1 law admits permanent lattice-anisotropic metastable terminals, including a regular-hex subsequence, while tie-break and initial conditions materially affect finite terminal states.

That negative dynamical result is not repaired post hoc. It is the R055 result.
