# RS-R059L — STAGE A NATIVE PATH ALGEBRA

Task-ID: `RS-R059L-STAGE-A-NATIVE-PATH-ALGEBRA`
Generation: `R059L`
Status: `DRIVER_APPROVED_TASKBOOK`
Identity-policy: `AUTO_RESOLVE_OR_ALLOCATE`
Identity-lane: `R059L`
Date: `2026-08-14`
Driver: `EM-DVR-R0457K / CONTROL_PLANE`

## 0. Stage-0 acceptance boundary

Stage 0 of `RS-R059L-UNIT-PACKET-PATH-ONLY-CRYSTAL-FOUNDATIONS-V2` is accepted by Driver at frozen owner head:

`825c0cde2909d127e72d402d78bcdc7b9a40aec2`

The Stage-0 checker reports overall PASS, 9/9 required hard-rejection self-tests PASS, no path ranking, no metric fitting, no grammar search, no geometry calibration, and `stage_a_entered=false`.

Frozen Stage-0 SHA256 inputs include:

- `R059L_UNIT_PACKET_PROTOCOL.json` — `464b72fa059dee165ac7bd021cd494a16fb29b86447c06cd960e4602bcaa57cd`
- `R059L_BARE_PACKET_SUBSTRATE_PROTOCOL.json` — `cd3b72dcd07bc3f963c7f367f8b27060278c4618e1bc974c1fe356c5a6caf95f`
- `R059L_OCCUPANCY_STATIC_COUNT_PROTOCOL.json` — `b2d910f5634685600c6503e30716b502008007afb105958dc3c7da755a016810`
- `R059L_PATH_EVENT_PROTOCOL.json` — `edd3a28eb516145d86bcd301ff4700ae7b57bbbcc0a6ba41663a5b6d0737eaff`
- `R059L_PATH_COUNT_PROTOCOL.json` — `39859a41518ddcba0dd8954af2c42a06551bfb44c159914eb9b50bd559477573`
- `R059L_STATIC_DYNAMIC_COUNT_TYPE_PROTOCOL.json` — `7b162f12c6c56fc4dea38e1c3b23a62e9e42064f348d84eca142c329a8eb9fe1`
- `R059L_PRECISION_REFINEMENT_UNIT_PROTOCOL.json` — `91701a79da03b08fb5b30174286e4af8a6c3432815cb432547b89f62933a54bf`
- `R059L_IDEAL_C6_CHANNEL_EXTENSION_PROTOCOL.json` — `d737700147ad86f364b2df4ca447cfb57ea31469e0c968c38ce78cc705ea532f`
- `R059L_INGRESS_EGRESS_STATE_PROTOCOL.json` — `1232498f682b13daba632fdb4473eb8a9951c509b4a9c8e0dbfad7e1d3411f9d`
- `R059L_GEOMETRY_WITHHOLDING_PROTOCOL.json` — `8c7bc0c0287036fd42ded1165061a0595c0f4126c942053b0fa0931db38c1756`
- `R059L_NATIVE_SEMANTICS_CLAIM_LEDGER.json` — `331037216e9b19b398fa5aeb3e124da026a8c1d71255d2196af29671d32fed09`
- `R059L_COMPUTATION_REGISTRY.json` — `54cba3d26d70e02a51750fa00c88f48551e9776c50ca2ca3fbfb99c07b42c48d`

All Stage-0 artifacts remain immutable during Stage A.

---

# 1. Scientific objective

Develop the smallest exact algebra forced by native path semantics alone.

The only foundations consumed are:

```text
CRYSTAL_PACKET
ADJACENCY
TRANSITION_EVENT
PATH
PACKET_COUNT / OCCUPANCY COUNT when declared
TRANSITION_COUNT / PATH_COUNT
OPTIONAL IDEAL_C6_CHANNEL_STATE
```

No line, distance, length, straightness, shortest path, edge, boundary, geometry, area, volume, metric, energy, or physical conservation law is admitted.

Stage A asks:

> What exact integer/algebraic identities follow merely because a path is an ordered history of actual adjacency transitions and every transition counts one?

---

# 2. Core path operations to define exactly

## 2.1 Zero-transition identity path

For every packet `x`, define the zero-transition path

```text
id_x = (x)
```

with

```text
PATH_COUNT(id_x)=0.
```

Do not interpret this as zero geometric length.

## 2.2 Composable concatenation

For paths

```text
gamma=(x_0,...,x_m)
eta=(y_0,...,y_n)
```

with `x_m=y_0`, define concatenation by identifying the shared endpoint once:

```text
gamma * eta=(x_0,...,x_m=y_0,y_1,...,y_n).
```

Prove exact closure as a path.

## 2.3 Path reversal

Define

```text
rev(gamma)=(x_n,...,x_0).
```

using symmetry of declared adjacency.

Reversal preserves every transition event as a transition in opposite temporal order; it does not delete events.

---

# 3. Required exact theorem targets

Stage A must prove or disprove, with exact finite combinatorics, at least the following.

## PA-T01 — identity laws

For composable paths:

```text
id_{x_0} * gamma = gamma
gamma * id_{x_n} = gamma.
```

## PA-T02 — associativity

For pairwise composable paths:

```text
(gamma * eta) * zeta = gamma * (eta * zeta)
```

as exact transition histories after the frozen shared-endpoint convention.

## PA-T03 — transition-count additivity

```text
PATH_COUNT(gamma * eta)
=
PATH_COUNT(gamma)+PATH_COUNT(eta).
```

## PA-T04 — reversal involution and count invariance

```text
rev(rev(gamma))=gamma
PATH_COUNT(rev(gamma))=PATH_COUNT(gamma).
```

## PA-T05 — reversal reverses composition order

```text
rev(gamma * eta)=rev(eta) * rev(gamma).
```

## PA-T06 — no cancellation of event history

For every nonzero path `gamma`:

```text
PATH_COUNT(gamma * rev(gamma))
=
2*PATH_COUNT(gamma) > 0.
```

Therefore `gamma * rev(gamma)` is not the zero-transition identity path unless `gamma` itself has zero transitions.

This theorem is important: immediate reversals are genuine events and are not silently quotient-cancelled.

Do not call the resulting algebra a group/groupoid if inverse cancellation is absent.

A category/path-category style classification may be recorded only as an algebraic analogy after the exact identities are proved.

---

# 4. Native arrival/departure bookkeeping

For a finite path

```text
gamma=(x_0,...,x_n),
```

define for each packet `x`:

```text
ARRIVE_gamma(x)
= #{j in {1,...,n}: x_j=x}

DEPART_gamma(x)
= #{j in {0,...,n-1}: x_j=x}.
```

These are integer event counts derived from the path history.

They are not occupancy count.

## PA-T07 — endpoint incidence identity

Prove exactly:

```text
DEPART_gamma(x)-ARRIVE_gamma(x)
=
1[x=x_0]-1[x=x_n].
```

This must hold with:

- revisits;
- loops;
- immediate reversal;
- repeated adjacency use;
- repeated occurrences of either endpoint in the interior.

For a closed path `x_0=x_n`, derive:

```text
DEPART_gamma(x)=ARRIVE_gamma(x)
```

for every packet `x`.

Do not call this divergence, flux, current, charge, momentum, or physical conservation in Stage A. It is an exact endpoint incidence identity only.

## PA-T08 — global arrival/departure totals

Prove:

```text
sum_x ARRIVE_gamma(x)=PATH_COUNT(gamma)
sum_x DEPART_gamma(x)=PATH_COUNT(gamma).
```

The sums range only over the finite packet support of the path.

---

# 5. Packet support / visit multiplicity separation

Define only if useful:

```text
VISIT_MULT_gamma(x)=#{j in {0,...,n}: x_j=x}
PATH_SUPPORT(gamma)={x_j:0<=j<=n}.
```

These are derived from path history.

Do not identify `PATH_SUPPORT` with a separately declared occupied configuration unless that equality is explicitly part of the test case.

Required regressions:

- repeated visits can increase `VISIT_MULT` without increasing support cardinality;
- loops can increase `PATH_COUNT` without increasing support cardinality;
- `PACKET_COUNT(C)` remains static object count and never becomes visit multiplicity.

Optional exact identity:

```text
VISIT_MULT_gamma(x)
=
ARRIVE_gamma(x)+1[x=x_0]
=
DEPART_gamma(x)+1[x=x_n].
```

---

# 6. Optional C6 channel decomposition

Only if `IDEAL_C6_CHANNEL_STATE` is explicitly active for the test carrier.

Do not add geometric meanings to channel labels.

For each packet `x`, verify that channel-resolved counts aggregate to the non-channel event counts:

```text
sum_d I_x[d] = ARRIVE_gamma(x)
sum_d O_x[d] = DEPART_gamma(x).
```

Therefore derive the channel-summed endpoint identity:

```text
sum_d O_x[d] - sum_d I_x[d]
=
1[x=x_0]-1[x=x_n].
```

Same-channel passages remain allowed:

```text
M_x[d,d] > 0.
```

If a passage matrix `M_x[a,b]` is used, distinguish internal paired visits from unmatched open-path endpoint events explicitly. Do not force an endpoint into an artificial ingress/egress pair merely to make a matrix square identity look cleaner.

No `opp(d)`, angle, straight, turn, displacement, or vector semantics may be introduced unless already present in the frozen Stage-0 extension. Stage A must not enrich C6 semantics.

---

# 7. Algebraic classification target

After proving the exact identities, classify the structure at the weakest justified algebraic level.

Candidate statement to test:

> Packets as objects, finite adjacency paths as composable histories, zero-transition paths as identities, and concatenation form a path category / free-category-like structure; path reversal is an involutive order-reversing operation because adjacency is symmetric; transition count is an additive nonnegative-integer grading; reversal is not an inverse because event history does not cancel.

Do not use category terminology as a premise. Derive the concrete laws first, then state the classification as a compression of proved identities.

A particularly important negative result is expected:

```text
REVERSAL_IS_NOT_CANCELLATIVE_INVERSE
```

unless a later quotient semantics is deliberately introduced. No such quotient is authorized in this Stage.

---

# 8. Forbidden Stage-A work

Strictly forbidden:

- line construction;
- straightness;
- shortest path / geodesic;
- distance / metric / length;
- path ranking or efficiency;
- endpoint displacement magnitude;
- Q(a,b)=a^2+ab+b^2 metric use;
- angle / slope / curvature;
- edge / boundary / perimeter / chord;
- area / volume interpretation;
- Voronoi geometry;
- circle / square / rectangle / cube / pi;
- R057/R058S fitted or collapse rules;
- conservation-law physical interpretation;
- temperature/absolute-zero physical inference;
- path cancellation quotient;
- grammar search / optimizer / teacher fitting.

Coordinates, if used for tiny examples, remain I0 adjacency implementation only.

---

# 9. Deterministic finite regression registry

Use a compact exact registry including at least:

1. zero-transition identity path;
2. one-hop path;
3. two-hop path;
4. immediate reversal `A,B,A`;
5. repeated adjacency `A,B,A,B,A`;
6. triangle/short closed loop where admitted;
7. open path that revisits its start in the interior;
8. open path that revisits its end before final arrival;
9. concatenation of two open paths;
10. concatenation of a path with its reversal;
11. C6 same-channel passage case when C6 is active;
12. closed C6 path bookkeeping case when C6 is active.

All bookkeeping must be integer exact.

---

# 10. Required artifacts

Freeze at least:

1. `R059L_PATH_COMPOSITION_PROTOCOL.json`
2. `R059L_PATH_REVERSAL_PROTOCOL.json`
3. `R059L_PATH_COUNT_ALGEBRA.json`
4. `R059L_ARRIVAL_DEPARTURE_PROTOCOL.json`
5. `R059L_ENDPOINT_INCIDENCE_IDENTITY.json`
6. `R059L_PATH_SUPPORT_VISIT_MULTIPLICITY.json`
7. `R059L_C6_CHANNEL_BOOKKEEPING_IDENTITY.json` if C6 lane is active
8. `R059L_NATIVE_PATH_ALGEBRA_THEOREM_LEDGER.json`
9. `R059L_STAGE_A_REGRESSION_RESULTS.json`
10. `R059L_STAGE_A_NATIVE_PATH_ALGEBRA_CHECKPOINT.json`
11. deterministic independent checker output

The theorem ledger must distinguish:

- `PROVED_EXACT`
- `DISPROVED`
- `CONDITIONAL_ON_C6_EXTENSION`
- `NOT_TESTED`

No empirical/statistical language is needed for finite exact identities.

---

# 11. Mandatory checker gates

The Stage-A checker must verify at least:

- all frozen Stage-0 hashes unchanged;
- identity paths count zero;
- concatenation closure;
- associativity on the regression registry;
- path-count additivity;
- reversal involution;
- reversal count invariance;
- reversal composition-order law;
- no event cancellation under `gamma * rev(gamma)`;
- endpoint incidence identity including revisit/reversal cases;
- arrival/departure global totals;
- packet count remains distinct from visits and transitions;
- same-channel C6 remains allowed when C6 is active;
- no geometry/metric/physical-conservation leakage.

The checker must reject any attempt to:

- set `gamma * rev(gamma)=id` by cancellation;
- treat `PATH_COUNT` as length;
- treat arrival/departure identity as a physical flux law at N0;
- rank paths by efficiency/shortness;
- attach angle/straight/turn semantics to C6 labels.

---

# 12. Stop condition

After freezing the Stage-A checkpoint and all hashes, stop for Driver review.

Do not proceed to path statistics, quotient/cancellation semantics, refinement algebra, direction, length, geometry, or physical calibration.
