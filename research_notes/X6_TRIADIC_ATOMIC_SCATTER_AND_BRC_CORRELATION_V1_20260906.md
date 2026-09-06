# X6 triadic atomic scatter: common-Cell closure selects a correlated INNER law

Status: `FREE_RESEARCH / EXACT RESTRICTED DERIVATION / NOT_FOUNDATION`
Date: `2026-09-06`
Task: `RS-X6-TRIADIC-CLOSURE-DYNAMICS`
Consumes:
- P000 V5 and `P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md`;
- `X6_NATIVE_SPATIAL = AFFINE_TORSOR(Z^6)`;
- `X6_TRIADIC_ROTATION_GENERATORS_V1_20260906.md`;
- `X6_ROTATION_PATH_GROUPOID_V2_20260906.md`;
- current signed-X6 BRC shortest-path kernel.

## 1. Scope

P000 already fixes that the minimum nonzero primitive stable balance has exactly three force quanta and satisfies `TRIADIC_CLOSURE_E`. The open question is how such a closure can be realized as a Cell/path event without importing classical vector-sum-zero.

This note gives a smallest exact realization for the equal-unit signed-axis sector. It is not claimed to exhaust every possible future realization of `TRIADIC_CLOSURE_E`.

## 2. Primitive force-port occurrence

Fix a native Cell `c` and a signed native unit direction

`d in {+e_1,-e_1,...,+e_6,-e_6}`.

Define the incoming unit force-port occurrence at `c` by the primitive Cell transition

`F_in(c;d): c+d -> c`.

Its reversal is the outgoing occurrence

`F_out(c;d): c -> c+d`.

The label `d` is the radial port label relative to the action node; the actual incoming step is `-d`. This keeps Cell incidence separate from classical force-vector semantics.

## 3. Canonical equal-unit triadic closure realization

Let `d_1,d_2,d_3` have three distinct underlying native-axis labels. Because all distinct native axes are pairwise `PERP_E`, these three equal-unit ports meet the P000 canonical pairwise-orthogonality requirement.

Define the restricted incoming closure realization

`C_in(c;d_1,d_2,d_3)`

as the three simultaneous incoming primitive occurrences

`c+d_r -> c`, `r=1,2,3`,

with one common action Cell `c`.

The outgoing reversal `C_out` is defined analogously.

Thus the closure predicate in this restricted sector is incidence/coalescence at one atomic Cell plus three distinct native axes. No Euclidean vector addition is used.

## 4. Triadic rotation scatter

Choose an oriented 3-subset `S=(i,j,k)` and its signed-C6 generator `Q_S` from V1:

`Q_S(e_i)=-e_j`, `Q_S(e_j)=-e_k`, `Q_S(e_k)=-e_i`.

Take any signed closure triad supported on those three axes:

`d_r=sigma_r e_{s_r}`, `sigma_r in {+1,-1}`.

The macro target ports are `Q_S d_r`. Since `Q_S` is a signed permutation, the target triple again has three distinct underlying axes and is again a valid restricted closure triad.

For each token the endpoint Cell move is

`c+d_r -> c+Q_S d_r`.

It uses two distinct signed coordinate axes, so the current signed-X6 BRC theorem gives exactly two shortest two-step paths:

- `INNER_r: c+d_r -> c -> c+Q_S d_r`;
- `OUTER_r: c+d_r -> c+d_r+Q_S d_r -> c+Q_S d_r`.

Hence one joint triad macrostep has `2^3=8` shortest branch combinations before the closure law is imposed.

## 5. Atomic-node branch-selection theorem

**Theorem.** Among those eight joint shortest branch combinations, exactly one has a common midpoint Cell for all three force quanta: `INNER x INNER x INNER`.

**Proof.**

Every INNER midpoint is `c`.

For a token supported on one selected axis, `Q_S d_r` lies on a different selected axis. Therefore the OUTER displacement

`d_r+Q_S d_r`

has two nonzero axis components and cannot vanish, so no OUTER midpoint equals `c`.

The three OUTER midpoint displacements have support on the three different selected axis-pairs `{i,j}`, `{j,k}`, `{k,i}`. Two such displacements cannot be equal because one contains a nonzero component on an axis absent from the other.

Thus three midpoints coincide iff all three branches are INNER. QED.

Consequently, if one macro rotation event is required to realize one P000 atomic triadic action node at the common intermediate microstep, the BRC branch law is forced:

`TRIADIC_ATOMIC_SCATTER_SECTION = III`.

This is a scoped law for triadic atomic scatter. It does **not** choose INNER for arbitrary single-Cell rotation trajectories.

## 6. Joint-correlation consequence for BRC

Each force token separately has Boolean shortest support `{INNER,OUTER}`. The product of the three marginal supports therefore has eight elements.

The atomic closure relation selects only the correlated triple `III`.

Hence closure cannot be recovered from the three marginal branch supports after their joint provenance relation has been discarded.

This is an exact native instance of the Joint Relation Observer Preservation rule:

`MARGINAL_BRANCH_SUPPORTS != JOINT_TRIADIC_CLOSURE_STATE`.

For one six-macrostep `Q_S^6=1` cycle, an unconstrained labeled three-token shortest lift has

`8^6 = 262144`

joint branch words, whereas repeated atomic triadic closure selects exactly one all-`III` word.

The reduction is law-driven, not an observer-safe quotient available before the closure law is specified.

## 7. Relation to the Viète OUTER selection

The existing Viète C12 result selected OUTER for a **single phase trajectory** under the requirement that the intermediate phase remain nonzero and carry the half-angle ray.

The present force-closure result selects INNER for a **three-force atomic event** under the requirement that all three action occurrences meet at one Cell.

Therefore there is no observer-independent universal answer to “INNER or OUTER”. The correct branch depends on the typed physical/research law:

- phase-refinement law -> OUTER in the declared Viète interface;
- atomic triadic-force law -> joint `III` in the present interface.

This is a positive reason to retain BRC provenance until the consuming law is known.

## 8. Triadic phase memory: C3 is the exact repair coordinate

For a sign-coherent ordered triad on `S`, the labeled `Q_S` orbit has six phases.

If token correspondence/order is forgotten and only the unordered set of three occupied signed ports is retained, the readout alternates only between the positive and negative sign sheets, hence has period two.

Thus the forgetful phase map is

`C6 -> C2`,

with kernel `C3`.

Therefore a `C3` cyclic matching variable is the exact repair coordinate needed to reconstruct the six-phase triadic rotation from the two-sheet static closure observer.

This phase variable is provenance/internal state, not an additional spatial axis.

## 9. Equal-unit larger-population triadic decomposition theorem

Consider a finite equal-unit force population attached to one Cell. Let

`d_i >= 0`

be the number of occurrences whose underlying native axis is `i`, ignoring sign but retaining each occurrence's sign as provenance.

Suppose the population is to be decomposed into `m` restricted triads, each using three distinct underlying axes.

**Theorem.** Such a decomposition exists iff

`sum_i d_i = 3m`

and

`max_i d_i <= m`.

Necessity is immediate: every triad contributes three occurrences and uses an axis at most once.

For sufficiency, sort the remaining degrees decreasingly. If `m>0`, the third largest degree is positive, otherwise the total would be at most `2m < 3m`. Choose the three largest axes for one triad and decrement them. Any unchosen degree is at most `m-1`; otherwise four degrees would all equal `m`, forcing total at least `4m > 3m`. The reduced degree sequence therefore satisfies the same conditions with `m-1`. Induction completes the construction.

Signs can be carried by the selected occurrences because the existence proof constrains only repeated underlying-axis use inside one triad.

This gives a constructive `O(m log 6)` greedy decomposition algorithm after degree maintenance.

## 10. BRC polynomial for decomposition provenance

Let

`H(x_1,...,x_6)=sum_{|S|=3} product_{i in S} x_i`.

Then for `sum d_i=3m`, the coefficient

`[x_1^d_1 ... x_6^d_6] H^m`

counts ordered type-level triadic decompositions.

For the six-force population `d=(1,1,1,1,1,1)`, the ordered count is `20`, while the unordered partition count is `10`.

Thus stable populations larger than three can have genuine decomposition provenance even when their aggregate axis counts are identical. A total-only stable-force observer is therefore not generally operation-safe.

## 11. Explicit apparent-two-force triadic lift witness

Fix distinct visible native axes `i,j`. Define an effective scalar observer `O_ij` on force-port labels by

- `+e_i -> +1`, `-e_i -> -1`;
- `+e_j -> -1`, `-e_j -> +1`;
- every port on the other four native axes -> `0`.

For every hidden axis `k notin {i,j}` and hidden sign `sigma`, the native restricted triad

`{+e_i,+e_j,sigma e_k}`

is mapped to the same effective visible readout `{+1,-1,0}` and hence to the same apparent equal/opposite two-force pair after the zero branch is suppressed.

There are exactly `4*2=8` such hidden-force lifts for this fixed observer and fixed visible pair.

This is a downstream observer witness only. It does not define native balance by scalar summation. It proves concretely that apparent two-force equilibrium can be a many-to-one projection of primitive triadic closure and that the hidden third branch is not reconstructible from the two-force readout alone.

## 12. Current status

Closed in this restricted equal-unit sector:

- a typed Cell-incidence realization of canonical triadic closure;
- exact covariance under the associated `Q_S` triadic rotation;
- unique common-Cell shortest scatter branch `III` for all selected-axis sign patterns;
- joint-correlation/BRC obstruction to marginal factorization;
- exact `C3` phase-repair coordinate above the two-sheet static triad observer;
- necessary-and-sufficient degree criterion for larger equal-unit triadic decomposition;
- exact decomposition-provenance polynomial and a 10-fold unordered nonuniqueness witness;
- an explicit eight-fold apparent-two-force triadic-lift witness.

Still open:

1. unequal-quantum triadic closure and interaction laws;
2. whether the atomic scatter section `III` is the unique physically admitted triadic law beyond the shortest-path sector;
3. coupling triadic event synchrony to the native time task;
4. interaction between triadic force state and Cell/channel/internal state;
5. whether repeated triadic scatter generates additional dynamical invariants beyond the frame group and path history.

No external novelty or Foundation promotion is claimed.
