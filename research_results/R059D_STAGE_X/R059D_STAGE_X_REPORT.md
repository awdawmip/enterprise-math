# R059D Stage X — Triaxial Unit-Step Staircase Classification

Researcher-ID: `EM-R059D-9C6B2A`  
Taskbook source commit: `994dd853d418677aae69e9a9ce0cba683a590aea`  
Taskbook Git blob: `b05292d3422dce474d165c7160e8c820d123bb50`  
Frozen parent: `8313e75a356608f64795332a397d463631b9be18`  
Owner branch: `research/r059d-stage-x-triaxial-unit-step-staircase`

## Executive result

Stage X inserts the missing exact semantics of one number-axis unit step without reintroducing translation homogeneity.

The result is a complete classification of the local integer-coordinate freedom.

For the A2/C6 CELL_ID scaffold, write

`C(a,b)=(U(a,b),V(a,b),W(a,b))`.

The unit-step requirements imply the exact general solution

`U(a,b)=a+F(b)`

`V(a,b)=-b+G(a)`

`W(a,b)=-a+H(a+b)`

where the one-dimensional integer functions satisfy

`F(n+1)-F(n) in {0,1}`

`G(n+1)-G(n) in {-1,0}`

`H(n+1)-H(n) in {0,1}`.

Origin normalization gives `F(0)=G(0)=H(0)=0`; the hard observation

`C(+u)=(1,-1,-1)`

gives

`G(1)=-1`, `H(1)=0`.

Conversely every such triple gives a path-independent integer CELL_ID -> stored-coordinate map satisfying the full unit-step staircase semantics.

Freeze:

`UNIT_STEP_STAIRCASE_SEMANTICS_SELF_CONSISTENT`.

No fixed full-vector stored increment is derived.

## Cyclic symmetric subcase

Cyclic covariance is an explicit symmetric-subcase assumption, not a hard observation.

Use

`rho(a,b)=(b,-a-b)`

and

`rho_C(U,V,W)=(W,U,V)`.

Then the three arbitrary functions reduce exactly to one:

`G(n)=F(n)-n`

`H(n)=n+F(-n)`.

Thus

`C(a,b)=(a+F(b), F(a)-a-b, b+F(-a-b))`.

The hard `+u` observation forces

`F(1)=0`

and

`F(-1)=-1`.

The cyclic first-shell coordinates are then consequences inside this declared subcase:

`C(+v)=(-1,1,-1)`

`C(+w)=(-1,-1,1)`.

They are not retyped as independent observations.

Freeze:

`CYCLIC_SYMMETRY_REDUCES_THREE_FUNCTIONS_TO_ONE`.

## Reflection and the single binary staircase

Add the explicitly typed reflection fixing the `u` ray and swapping its transverse coordinates:

`sigma(a,b)=(a+b,-b)`

`sigma_C(U,V,W)=(U,W,V)`.

This is equivalent to

`F(-n)=F(n)-n`.

Define for `n>=0`

`a_n=n-F(n)`.

Then

`C(n,0)=(n,-a_n,-a_n)`

and reflection gives

`F(-n)=-a_n`.

The exact forced conditions are

`a_0=0`

`a_1=1`

`a_(n+1)-a_n in {0,1}`.

The converse is exact: every nonnegative integer sequence satisfying those conditions determines

`F(n)=n-a_n`, `F(-n)=-a_n`

and therefore a unique global cyclic/reflection-symmetric UNIT_STEP atlas.

Hence there is a bijection:

`global cyclic/reflection UNIT_STEP atlases <-> binary staircase sequences`.

Freeze:

`TRIAXIAL_INTEGER_ATLAS_REDUCES_TO_ONE_BINARY_STAIRCASE_SEQUENCE`.

But local A2 consistency imposes no additional equation on the jump bits.

Therefore:

`PURE_AXIS_STAIRCASE_JUMPS_REMAIN_FREE`.

## Global inversion audit

Global coordinate inversion is not assumed.

In the unrestricted three-function solution, `C(-x)=-C(x)` is equivalent to each of `F,G,H` being odd. This is compatible with the minimal hard `+u` observation; therefore Stage X does not claim that the hard observation alone forbids inversion.

In the declared cyclic subcase, however, inversion requires

`F(-n)=-F(n)`.

But hard `+u` plus cyclic covariance already gives

`F(1)=0`

and

`F(-1)=-1`.

Inversion would require `F(-1)=0`.

Contradiction.

Freeze, with this scope:

`GLOBAL_INVERSION_INCOMPATIBLE_WITH_HARD_FIRST_STEP_AND_CYCLIC_UNIT_STEP_SEMANTICS`.

The contradiction arises before adding the `u`-ray reflection. Thus the earlier W-REISSUE2 inversion failure is structurally reproduced in the cyclic unit-step semantics, rather than being merely a peculiarity of its Q witness.

## Root laws become jump schedules

Only after the staircase classification are radicals introduced.

For root order `p=2..6`, if

`k^p < n < (k+1)^p`

then the legal integer stored magnitudes are

`a_n in {k,k+1}`.

At a perfect power

`n=k^p`

the value is exact:

`a_n=k`.

Because Stage X has already proved

`a_(n+1)-a_n in {0,1}`,

every complete perfect-power interval has one jump position

`J_(p,k) in {k^p+1,...,(k+1)^p}`.

The staircase equals `k` before `J_(p,k)` and `k+1` from `J_(p,k)` onward.

Conversely, choosing one such jump position independently for every perfect-power interval produces a legal global staircase, and therefore a legal global integer atlas.

So the local equations do not choose:

- square root versus cube/fourth/fifth/sixth root;
- floor versus ceiling;
- nearest-root control;
- power-midpoint control;
- or any other monotone legal placement of the jump.

Freeze:

`ROOT_SCHEDULE_NOT_IDENTIFIED_BY_LOCAL_ATLAS`.

`LOCAL_INTEGER_ATLAS_SELF_CONSISTENCY_ALONE_CANNOT_IDENTIFY_ROOT_ORDER_OR_COLLAPSE_JUMPS`.

`MULTIPLE_ROOT_ORDERS_REMAIN_ADMISSIBLE_UNDER_UNIT_STEP_CLASSIFICATION`.

This is stronger than merely observing multiple finite-radius CSP witnesses: the freedom is classified symbolically by the staircase theorem.

## Count-only discriminator audit

The count registry was frozen before scoring.

Exact scaffold counts include:

- positive `u`-ray prefix: `RAY(r)=r`;
- shell: `SHELL(r)=6r`;
- ball: `BALL(r)=1+3r(r+1)`;
- triangular sector: `T(r)=(r+1)(r+2)/2`;
- two-direction parallelogram block: `P(m,n)=mn`.

In particular a square block exists:

`P(k,k)=k^2`.

But the current semantics contain no independently justified relation saying that the first `n` cells on a primary ray are in bijection with a `a_n x a_n` block, nor any conservation equation or inequality that forces

`a_n^2 <= n < (a_n+1)^2`.

The key negative theorem is simple: every registered count depends only on the frozen CELL_ID scaffold. Changing the admissible staircase `a_n` changes stored coordinates but does not change any of those scaffold cell counts. Therefore scaffold-only counts are coordinate-model blind unless a new relation couples a counted region to `a_n`.

Freeze:

`SCAFFOLD_ONLY_COUNTS_ARE_COORDINATE_MODEL_BLIND`.

`MISSING_COUNT_IDENTITY_NOT_YET_IDENTIFIED`.

The existence of square-sized cell regions is therefore not yet a derivation of square-root jump thresholds.

## 5 -> 4 / 9

Because X4 does not derive a square-count identity, the old scalar control remains unresolved.

Inside the square-root schedule class,

`sqrt(5)` has legal adjacent magnitudes `2` and `3`.

There is a complete Stage-X atlas with the floor square-root schedule and

`a_5=2`,

and another complete Stage-X atlas with the ceiling square-root schedule and

`a_5=3`.

On the squared-count readout these correspond to

`5 -> 4`

and

`5 -> 9`.

Neither is selected.

Freeze:

`FIVE_TO_FOUR_OR_NINE_UNRESOLVED`.

## Relation to Stage W REISSUE2

Stage W REISSUE2 remains immutable and accepted.

Stage X explains its radius-4 underdetermination structurally: after unit-step semantics plus cyclic/reflection reduction, the remaining degree of freedom is exactly one binary staircase jump sequence. Enlarging the same local coordinate-consistency equations cannot identify its jumps, because every binary staircase extends globally.

Thus the next missing mathematical ingredient is not another local completion preference. It is an independently justified count identity or other exact relation coupling the primary count to the staircase magnitude.

The first-round homogeneous Stage-W coordinate law remains superseded and is not revived.

## Mandatory semantic statements

- `CELL_COORDINATES_ARE_INTEGER_ONLY` remains in force.
- `C(+u)=(1,-1,-1)` is retained as the hard first-step observation.
- cyclic first-shell symmetry is an explicit subcase assumption; its `+v/+w` first-shell values are then derived.
- global inversion is audited, not assumed; it is incompatible with the hard first step in the cyclic unit-step subcase, while not refuted by the minimal `+u`-only control.
- radicals are `PRECOLLAPSE_ALGEBRAIC_VALUE`, never stored coordinates.
- the stored coordinate map is path-independent because it is a function of CELL_ID.
- nontrivial root orders `p=2..6` remain admissible as jump-schedule classes; none is selected.
- local coordinate consistency does not force the lower/upper jump positions.
- no count identity currently forces square or other perfect-power thresholds.
- `5 -> 4/9` remains unresolved.
- universal BRC, probability, physical geometry, physical direction preference, force, energy and physical dimensionality are not established.

## Checker

Deterministic checker:

`89591 / 89591 PASS`.

Checks digest:

`fad58a2e8edec329c4c416ef80a350562249f57671597aa6a043a16dd3a83bac`.

The checker independently verifies finite-difference edge semantics, large families of binary staircases, cyclic/reflection covariance, the scoped inversion no-go, root-schedule legality, exact region-count formulas, count blindness, anti-triviality firewalls, and frozen-parent immutability.

`STOP_FOR_DRIVER_REVIEW`
