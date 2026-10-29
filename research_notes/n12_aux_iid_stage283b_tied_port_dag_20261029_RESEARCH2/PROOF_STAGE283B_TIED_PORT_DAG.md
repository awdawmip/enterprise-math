# Stage283-B — exact tied-port DAG obstruction and convex-hull certificate

**Research type:** portable author proof / exact finite ordered-history replay. **Status:** `UNREVIEWED / NOT_ADMITTED`; no native Task CLAIM, Source Result or independent Driver review is asserted.

**Local author label:** `EMR2-20261029-2105-STAGE283B` (a descriptive local label, **not** a service-issued Researcher/session/conversation identity). The authenticated Sites gateway has `research_authority_granted=false`; owner verification via `em_control_tasks` returned `CONTROL_QUOTA`. Formal activity/session binding is therefore `REGISTER_PENDING / SYNC_DEBT` unless subsequently registered through an authorized native route.

## Sources, declared model and prior frontier

- Global rules, single fixed canonical snapshot for this research unit: `awdawmip/chatgpt-global-knowledge main@4b3659222a1886c4643af5bdc6a867c745d65043`: `00_BOOTSTRAP.md`, `OPERATING_MANUAL.md`, relevant current math/code/BRC/activity/handoff/progress policies and `我眼中的世界.md`.
- Enterprise Math source/control snapshot: `awdawmip/enterprise-math main@8168b9667b766ce95c681e67628de6af10fdec3b`: `AGENTS.md`, `p000_reality_foundation.json`, `definitions/HEARTBEAT_WORLD_NATIVE_X6_TIME.json`, `definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json`, `control_plane/current_control_authority.json`, `docs/AUTONOMOUS_RESEARCH_OPERATIONS.zh-CN.md` and `docs/PORTABLE_RESEARCH_PROTOCOL.md`.
- Exact mathematical predecessor: Stage282-B `PROOF_STAGE282B_CAUSAL_SIMPLEX.md` and `REPRO_STAGE282B.py`, Draft PR #1571 at `6e8f1543ef98972c9ad19899613914d14da5817e`; Stage283-B task packet at the same ref. In Stage282-B, independent serial coins induce moments `(x,xy)`, whose complete feasible projection is the simplex `0<=z<=x<=1`. That theorem is *not* asserted for a coin reused along one ordered path.
- This is an **external finite decision DAG / BRC positive-weighted path model**, not a native X6 Cell, native plane, physical experiment, or P000 proof. All P000 and ACTIVE worldview claims stay unchanged and protected.

### Exact finite decision DAG

There are two strictly positive rational sources, using the established auxiliary alphabet `Sigma={0,1,2}`:

```
P(Sigma=0,1,2) = (1/8, 1/24, 5/6),
Q(Sigma=0,1,2) = (1/12, 1/12, 5/6).
```

Each source samples one symbol. The three histories branch and **reconverge** at a common controlled vertex X; the full ordered history retains the symbol and source tag. The DAG then has two ordered occurrences Y1 and Y2 of the **same source-blind policy port y**:

```
source -> symbol 0/1/2 ---> [merge X]
                                    | stop X (prob 1-x) -> T0
                                    | continue X (prob x)
                                  [Y1]
                                    | stop (prob 1-y) -> T1
                                    | continue (prob y)
                                  [Y2]
                                    | stop (prob 1-y) -> T2  [observer=1]
                                    | continue (prob y) -> T3 [observer=0]
```

At X the continue probability is `x∈[0,1]`. At both ordered Y visits, continue probability is the *same constant* `y∈[0,1]`, and the two Bernoulli draws are conditionally independent given the fixed parameter y. This tied-port identity is part of the model, not a default independence claim about distinct policies. All initial source symbol masses are strictly positive; boundary control probabilities 0 and 1 are allowed. There are 12 source-tagged, symbol-tagged complete terminal paths per source (four per symbol), including zero-mass terminal paths at boundary policies.

The single bounded terminal observer is `F=1_{T2}`, i.e. success at the first occurrence of y followed by failure at its second occurrence. Define minimized loss `L=1-E[F]`. Observation horizon is exactly the at-most-three controlled decisions after one initial symbol; future history-dependent observables are not claimed to be preserved by a terminal-only quotient.

## Theorem 283-B.1 — exact port law and failure of the prefix-simplex LP

**Statement.** Under the above source-blind, tied-port policy, for **each** source S∈{P,Q}, the complete four-terminal mass vector is

```
(p0,p1,p2,p3) = (1-x, x(1-y), xy(1-y), xy^2).
```

Let `z=xy` and `v=xy²`. The exact feasible lifted set of single fixed policies is

```
S = {(x,z,v): 0<=x,y<=1, z=xy, v=xy^2}.
```

Equivalently, it is the semialgebraic set

```
0<=v<=z<=x<=1,    x*v=z^2.                 (1)
```

The prefix-only linear simplex relaxation

```
L_simplex = {(x,z,v): 0<=v<=z<=x<=1}       (2)
```

has a **strict optimal-value gap** for the single bounded terminal observer above:

```
min_{(x,y)∈[0,1]^2} (1-E[F]) = 3/4,
min_{(x,z,v)∈L_simplex} (1-(z-v)) = 0.
```

Thus the exact minimization gap is `3/4`, and the true optimum is uniquely at `(x,y)=(1,1/2)`.

**Proof.** Conditional on a sampled symbol, the four ordered gate strings have respective probabilities `1-x`, `x(1-y)`, `xy(1-y)` and `xy²`. Multiplication by each positive symbol probability and summation over symbols yields the stated terminal law under either source; both total masses are exactly one. The realization map yields `(1)` by direct multiplication. Conversely, if `x>0`, `0<=v<=z<=x` and `xv=z²`, set `y=z/x`; then `0<=y<=1` and `v=z²/x=xy²`. If `x=0`, nonnegativity forces `z=v=0`, realized by any y. Therefore (1) is an if-and-only-if description.

Since `E[F]=xy(1-y)`,

```
xy(1-y) = x*(1/4-(y-1/2)^2) <= x/4 <= 1/4.
```

Equality requires `x=1` and `y=1/2` exactly; hence the minimum loss equals `3/4`. The LP relaxation (2) permits `(x,z,v)=(1,1,0)`, with formal terminal law `(0,0,1,0)`, giving loss zero. This point violates the port identity by `xv-z²=-1`. It corresponds to choosing `Y1` always continue and `Y2` always stop, which would require **two different** port parameters `y1=1,y2=0`. Such depth-specific controls are *not* the declared tied-port policy. Because the loss is nonnegative on the simplex, zero is its exact optimum. QED.

The initial positive-source branch-and-merge turns this into an acyclic DAG rather than an isolated scalar three-action chain. The *mechanism* is repeated use of one port along a path, which requires at least two visits to that port; it is not a claim that this graph is globally minimal among all possible DAG counterexamples.

## Theorem 283-B.2 — exact convex hull and scoped recovery of linear optimization

**Statement.** The convex hull of the tied-port single-policy feasible image S is exactly

```
K = {(x,z,v): 0<=v<=z<=x<=1, z^2<=x*v}.    (3)
```

For every affine terminal observable on the above four-terminal categories, minimizing or maximizing its expected value over the true **single fixed (x,y)** policies has the same optimum value as optimization over K. By contrast, the larger prefix simplex (2) may change the optimum by `3/4` as above. Points of K satisfying strict inequality `xv>z²` need not be implementable by a **single** tied `(x,y)` policy.

**Proof (necessity).** For any finite convex mixture of true policies `(x_j,x_j y_j,x_j y_j²)` with coefficients λ_j≥0, Σλ_j=1, define `x=Σλ_j x_j`, `z=Σλ_j x_j y_j`, `v=Σλ_j x_j y_j²`. Positivity gives `0<=v<=z<=x<=1`, and weighted Cauchy–Schwarz applied to `sqrt(λ_j x_j)` and `sqrt(λ_j x_j)*y_j` yields `z²<=xv`. By closure, all points of conv(S) satisfy (3).

**Proof (sufficiency, constructive).** Take `(x,z,v)` satisfying (3). If `z=0`, then `v=0` and `(x,0,0)` is a true policy with y=0. If `z>0`, then `x,v>0`. Put

```
y_* = v/z,      α = z²/(xv).
```

The inequalities imply `0<y_*<=1`, `0<α<=1`. The exact two-point convex decomposition is

```
(x,z,v) = (1-α)*(x,0,0) + α*(x,x*y_*,x*y_*²).
```

Indeed, its second coordinate is `α*x*(v/z)=z` and third is `α*x*(v/z)^2=v`. Hence K⊆conv(S). Combined with necessity, equality holds; the two-point representation also proves closedness without a separate topological assumption. Finally, any affine functional takes a convex combination to the same convex combination of values, so its extrema over conv(S) equal those over compact S. QED.

**Strict implementability example.** `(x,z,v)=(1,1/2,1/2)` satisfies (3) strictly (`xv-z²=1/4>0`); it is a 50–50 mixture of tied policies `(x,y)=(1,0)` and `(1,1)`, but no fixed y realizes it. Its convex admissibility suffices for optimizing an affine *single terminal expectation*, not for claiming the same time/path correlations, reusing downstream operations, or maintaining the original per-visit independent-draw model inside every mixture realization.

**Minimal repair, scoped precisely.** Relative to the three lifted occupancy coordinates `(x,z,v)`, the **one scalar algebraic port residual** `R_port=xv-z²` together with positivity/order bounds is necessary and sufficient for *single fixed-port implementability*; it is zero for true policies and negative on the LP's false optimum. The weaker nonnegative residual condition `R_port>=0` gives the exact convex hull for affine terminal-observer optimization. This does not assert a globally minimal state encoding or observer safety for arbitrary history-sensitive future operations. In the BRC typing, the joined path/port relation is a genuine extra observation direction and cannot be erased merely because each visit has positive rational marginal mass.

## Evidence, mathematical status, and limits

The standard-library `fractions.Fraction` program `REPRO_STAGE283B.py` independently enumerates all **12 ordered symbol/action terminal paths** per source, including boundary-zero branches, for every one of 289 rational grid control pairs `(x,y)∈{0,1/16,…,1}²`. It checks exact P/Q conservation and the terminal law without using floating point. It also reconstructs 500 rational convex-hull sample moments with exact two-atom witnesses, compares them against both source-tagged full ordered-history replays, and checks the true optimum, relaxed optimum and strict witness. Captured stdout: `REPRO_STAGE283B_EXECUTED_STDOUT.txt`, terminal marker `STAGE283B_TIED_PORT_DAG_EXACT_PASS`.

The universal real-domain theorems above are established by the displayed algebra, completeness argument, Cauchy–Schwarz and explicit convex decomposition. **The finite grid by itself does not prove continuous optimality.** No external physical, signed/phase-cancellation, native heartbeat time, spatial address, experiment, machine formalization, independent mathematical review, Source admission or canonical task closure is claimed.

## Unresolved next step

Stage284-B: when a source-conditioned non-IID DAG has two distinct repeated-port routes which **share the same y parameter**, do per-route second-order-cone moment inequalities suffice for exact joint affine-observer optimization? Seek an exact rational counterexample to independently convexifying route fibers, or prove a compatibility theorem with one global mixing measure. Preserve initial source tags, ordered visit counts, port identity, conditional occupations, and the allowed future-observer scope. Separately preserve the open Stage278-A N=12 Bellman new-face research task. Transfer to native Heartbeat X6 requires an independently verified six-field address codec, time/port/axis path mapping and observer/future-operation preservation proof.
