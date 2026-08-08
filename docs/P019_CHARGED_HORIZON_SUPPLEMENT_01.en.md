# P019 — Charged Static Horizons, Supplement 01: Discriminant Collapse and Vertex–Edge Horizons

Status: `ACTIVE RESEARCH NOTE / PRESSURE TEST`  
Depends on: `docs/P019_DISCRETE_BLACK_HOLE_HORIZON.en.md`  
Scope: pure-integer pressure test of a Reissner–Nordström-type quadratic radial factor  
Discipline: `a,b` are currently integer coefficients only; calibration from physical mass, charge, `G,c`, and typed units is not yet complete.

## 1. Why this is a stronger pressure test than Schwarzschild

The external comparison factor for a charged static case can be written

\[
f(r)=1-\frac{a}{r}+\frac{b}{r^2},
\]

where in standard geometrized conventions `a` plays the mass-term role and `b` the charge-squared role.

P019 does not perform those physical real-valued constant operations in the integer core. It extracts only the integer polynomial

\[
\boxed{P(n)=n^2-an+b.}
\]

Because `n^2>0`, the sign of the external comparison factor is the sign of `P`.

When `b=0`,

\[
P(n)=n(n-a),
\]

so the charged observation below reduces exactly to the first-stage Schwarzschild observation rather than defining an unrelated model.

## 2. P019-RN-T01 — Completed-square identity

Status: `PROVED`

Define the integer discriminant

\[
\boxed{\Delta=a^2-4b.}
\]

Then for every integer radial state `n`,

\[
\boxed{4P(n)=(2n-a)^2-\Delta.}
\]

Thus the entire radial causal phase can be classified by comparing a perfect square whose root has the same parity as `a`,

\[
(2n-a)^2,
\]

with the integer state `Delta`.

The two-horizon problem is thereby compressed directly into the square-collapse system.

## 3. P019-RN-T02 — Exact integer horizons iff the discriminant is a square-collapse fixed point

Status: `PROVED`

`P(n)=0` is equivalent to

\[
(2n-a)^2=\Delta.
\]

Hence a nonnegative integer root exists iff

\[
\Delta\ge0
\]

and

\[
\boxed{C_2(\Delta)=\Delta.}
\]

That is, `Delta` is a perfect square.

If

\[
d=R_2(\Delta),\qquad d^2=\Delta,
\]

then

\[
\Delta\equiv a^2\pmod4
\]

forces `d` and `a` to have the same parity, so the two algebraic roots require no fractional state:

\[
\boxed{h_-=(a-d)//2,\qquad h_+=(a+d)//2.}
\]

For `Delta=0`, the two roots merge at

\[
\boxed{h=a//2.}
\]

If `b=0`, the lower root is `0`, which remains the center/denominator boundary rather than a positive-radius horizon; the positive root `a` recovers the Schwarzschild model.

## 4. P019-RN-T03 — The causal phase is determined entirely by an integer square comparison

Status: `PROVED`

By T01,

\[
P(n)>0
\iff
(2n-a)^2>\Delta,
\]

\[
P(n)=0
\iff
(2n-a)^2=\Delta,
\]

\[
P(n)<0
\iff
(2n-a)^2<\Delta.
\]

Thus no real-valued roots are needed for the classification.

### `Delta<0`

Since every square is nonnegative,

\[
P(n)>0
\]

for every integer `n`. There is no horizon/trapped boundary on the integer radial line.

### `Delta=0`

\[
P(n)\ge0
\]

and only `n=a//2` is zero. This is an extremal-type boundary: a **zero vertex without a sign change across it**.

### `Delta>0`

There is a strict negative phase given by

\[
(2n-a)^2<\Delta,
\]

with positive phase outside it.

If `Delta` is square, the boundary lands on zero vertices. If it is nonsquare, the boundary can lie between adjacent positive/negative states with no zero vertex at all.

## 5. P019-RN-C01 — A trapped band can exist with no exact zero state

Status: `COUNTEREXAMPLE TO HORIZON-MUST-BE-A-VERTEX`

Take

\[
a=5,\qquad b=5,\qquad \Delta=5.
\]

Since `5` is not a perfect square,

\[
P(n)=0
\]

has no integer solution.

But

\[
P(1)=1,
\quad
P(2)=-1,
\quad
P(3)=-1,
\quad
P(4)=1.
\]

The integer phase sequence is therefore

\[
+\;|\;-\;-\;|\;+,
\]

and the two edges

\[
(1,2),\qquad(3,4)
\]

carry the boundary roles of the two continuum horizons.

This directly refutes a potentially overstrong assumption from the first P019 stage: **a discrete horizon need not be an integer zero-radius state.**

## 6. P019-RN-T04 — A vertex–edge boundary complex unifies exact and non-exact horizons

Status: `PROVED ON THE RADIAL LINE GRAPH`

View the nonnegative integer radial states as the primitive line graph

\[
0-1-2-3-\cdots.
\]

Define the horizon boundary complex by:

1. **zero vertices**: every positive integer `n` satisfying `P(n)=0`;
2. **crossing edges**: every adjacent pair `(n,n+1)` satisfying

\[
P(n)P(n+1)<0.
\]

Radius `0` is never promoted to a horizon vertex; it remains the separate center/denominator boundary.

For `a>0,b>0`:

- `Delta<0`: 0 boundary components;
- `Delta=0`: 1 zero vertex;
- `Delta>0` and `Delta` a perfect square: 2 zero vertices;
- `Delta>0` and `Delta` nonsquare: 0 zero vertices + 2 crossing edges.

Thus the subextremal two-boundary structure always survives as **two boundary components** in the integer model. What changes is whether the components lie on primal vertices or dual edges.

This is a better prototype for a later coordinate-free causal-graph definition than forcing every horizon to align with a lattice vertex.

## 7. P019-RN-T05 — Charged finite-precision observation and exact Schwarzschild reduction

Status: `PROVED`

For `lambda>0,n>0`, define

\[
\boxed{
g_\lambda(n;a,b)
=Q_{n^2}\!\left(\lambda|P(n)|\right)
=\left\lfloor\frac{\lambda|P(n)|}{n^2}\right\rfloor.}
\]

If

\[
\lambda\mid\mu,
\qquad r=\mu/\lambda,
\]

then exactly as in the first stage,

\[
\boxed{g_\mu//r=g_\lambda.}
\]

So the charged family remains a valid observation system on P018 divisibility precision chains.

More importantly, when

\[
b=0,\qquad a=h,
\]

we have

\[
P(n)=n(n-h),
\]

and hence

\[
\boxed{
g_\lambda(n;h,0)
=
\left\lfloor\frac{\lambda|n-h|}{n}\right\rfloor
=q_\lambda(n;h).}
\]

The Schwarzschild first stage is therefore the exact `b=0` special case of this model.

## 8. P019-RN-T06 — Exact persistence criterion for a zero observation

Status: `PROVED`

If

\[
P(n)\ne0,
\]

then

\[
g_\lambda(n)=0
\iff
\lambda|P(n)|<n^2.
\]

The largest integer precision at which this non-root state can still appear as a zero observation is exactly

\[
\boxed{
\Lambda_0(n)
=
(n^2-1)//|P(n)|.
}
\]

If instead

\[
P(n)=0,
\]

then for every positive `lambda`,

\[
\boxed{g_\lambda(n)=0.}
\]

Thus a finite statement replaces an infinite-limit story:

> **A zero observation survives arbitrary precision refinement iff the primal vertex is an exact algebraic root.**

For `a>=1,b>=0` there is also a uniform, not necessarily sharp, finite terminal precision

\[
\boxed{
\lambda_*(a)=\max\{2,(2a-1)^2\}.
}
\]

At that precision, for every positive integer `n`,

\[
\boxed{
g_{\lambda_*}(n)=0\iff P(n)=0.}
\]

### Proof sketch

For `n>=2a` and `b>=0`,

\[
P(n)\ge n^2-an\ge n^2/2,
\]

so `lambda>=2` already prevents any non-root large-radius state from observing as zero.

Only the finite set

\[
1\le n<2a
\]

remains. Each non-root has `|P(n)|>=1`, so its zero-persistence bound is less than `n^2`; `(2a-1)^2` uniformly exceeds all such admissible bounds.

This provides a genuine finite P018 predicate-completeness horizon.

## 9. P019-RN-T07 — Integer scale transformations preserve the horizon regime; refinement cannot rescue a nonsquare discriminant

Status: `PROVED`

Under a uniform integer radial scale transformation

\[
n'=sn,
\qquad a'=sa,
\qquad b'=s^2b,
\qquad s>0,
\]

we have

\[
\boxed{
\Delta'=a'^2-4b'=s^2\Delta.}
\]

Therefore:

- the sign of `Delta` is preserved;
- extremality `Delta=0` is preserved;
- whether a nonnegative `Delta` is a perfect square is preserved, because `s^2 Delta` is square iff `Delta` is square.

A nonsquare discriminant therefore cannot become square merely by ordinary integer scale refinement.

More strongly,

\[
P'(sn)=s^2P(n),
\]

so

\[
\boxed{
g_\lambda(sn;sa,s^2b)=g_\lambda(n;a,b).}
\]

The dimensionless horizon observation is exactly invariant on the uniform integer scale embedding.

This forces the lesson of T04: a horizon that is not aligned with the primal lattice should be represented as an edge/dual boundary, not expected to turn into a primal zero vertex at ever finer integer scale.

## 10. P019-RN-T08 — Parity-constrained square cell of the discriminant

Status: `PROVED`

All reachable square states

\[
(2n-a)^2
\]

have roots with the same parity as `a`, so the ordinary `R_2(Delta)` is not by itself the sharpest horizon-cell coordinate.

Let

\[
u=\max\{x\ge0:x\equiv a\pmod2,\ x^2\le\Delta\}.
\]

It is recovered from the ordinary integer root by

\[
\boxed{
u=R_2(\Delta)
\text{ when the parity matches; otherwise }u=R_2(\Delta)-1.}
\]

The symmetric inner candidate states

\[
n_-=(a-u)//2,
\qquad n_+=(a+u)//2
\]

satisfy

\[
\boxed{
P(n_-)=P(n_+)
=-\frac{\Delta-u^2}{4}.}
\]

The next same-parity square `u+2` has positive residual

\[
\boxed{
\frac{(u+2)^2-\Delta}{4}>0
}
\]

except that in the exact case `u^2=Delta` the current candidates are already zero roots.

Each horizon is therefore bracketed by a pure-integer parity-sensitive square cell. This interfaces directly with the P001/P002 basin-gap/carry language and suggests a later general notion of a geometric boundary carry.

## 11. Theoretical correction: a horizon behaves more like a cut than necessarily like a point

The Schwarzschild first stage makes it tempting to identify

\[
q_\lambda=0
\]

with the horizon itself.

The RN pressure test gives a more robust hierarchy:

1. **causal phase**: integer sign/reachability structure on primitive states;
2. **boundary complex**: zero vertices plus crossing edges;
3. **precision observation**: how well nearby boundary states can be distinguished;
4. only when the boundary happens to align with a primal vertex does “zero state = horizon vertex” occur.

This moves P019 from discretizing one radial formula toward a P012-compatible geometric definition:

> **A discrete horizon is first a boundary/cut between causal phases; it may be represented by a primal vertex or by a dual edge.**

The next stage should generalize this from the one-dimensional radial line graph to an arbitrary primitive causal graph.

## 12. Physical pressure points

This supplement exposes rather than removes the physical risks:

- external RN parameters are continuous-model mass/charge parameters; P019 has not proved how arbitrary physical parameters map into integer `a,b`;
- uniform integer refinement preserves square/nonsquare arithmetic class, so “use finer precision” cannot erase that issue;
- the vertex/edge boundary solves lattice misalignment but still needs coordinate independence;
- extremal `Delta=0` is a zero vertex with no sign reversal, so a horizon cannot be defined only as a sign-change cut;
- stability of the inner/Cauchy horizon is a separate and difficult question in external GR, not treated by this static polynomial model.

The minimum unified definition must therefore accommodate both

\[
\boxed{
\text{zero-expansion vertices}
+
\text{opposite-phase crossing edges}.}
\]

## 13. Stage ledger

- `P019-RN-T01`: completed-square identity — `PROVED`
- `P019-RN-T02`: integer roots iff square-collapse-fixed discriminant — `PROVED`
- `P019-RN-T03`: integer causal phase from square/discriminant comparison — `PROVED`
- `P019-RN-C01`: trapped band without integer zero horizon — `COUNTEREXAMPLE`
- `P019-RN-T04`: vertex-edge boundary complex and component classification — `PROVED`
- `P019-RN-T05`: charged precision observation, divisible projection, Schwarzschild reduction — `PROVED`
- `P019-RN-T06`: zero-persistence limit and finite terminal zero precision — `PROVED`
- `P019-RN-T07`: uniform integer scale invariance / no square-class rescue — `PROVED`
- `P019-RN-T08`: parity-constrained discriminant horizon cell — `PROVED`

Executable checks:

- `src/enterprise_math/charged_black_hole.py`
- `tests/test_charged_black_hole.py`
- `tests/test_charged_horizon_boundary.py`

## 14. Next stage

1. abstract the boundary complex to a general directed/causal graph and define a coordinate-free outgoing-phase boundary;
2. put P018 observation fibers on boundary vertices/edges rather than only on the radial coordinate;
3. determine how an extremal “zero without sign change” boundary is expressed by local graph expansion;
4. integrate stable RN primary/context citations after the source-registry gate is available;
5. only then move to Kerr, where rotation may require face/cell-level boundaries rather than only vertices/edges.
