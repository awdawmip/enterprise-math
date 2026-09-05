# X6 × P000 direction gate：signed shortest paths、primitive line 与 exact BRC kernel

Status: `DERIVED / EXACT / P000-V4 DIRECTION-GATE TOOL`
Date: `2026-09-05`
Depends on: signed X6 spatial candidate `Z^6`.

## 1. Endpoint and primitive event count

For signed displacement

`z=(z_1,...,z_6) in Z^6`,

one primitive coordinate transition changes exactly one component by `+1` or `-1`.

Therefore every path from 0 to z has at least

`N_min(z)=sum_i |z_i|`

transition events, and this lower bound is attained by taking exactly `|z_i|` steps in the sign of `z_i` on each axis.

Thus the shortest primitive-event count is exactly the L1 component norm.

This does not define geometric length: P000 spatial component length is

`L_E(z)=sqrt(sum_i z_i^2)`.

So `PATH_COUNT_MIN` and `SPATIAL_LENGTH` are two exact but different readouts.

## 2. Primitive straight segment criterion

P000 V4 freezes:

`PRIMITIVE_STRAIGHT_SEGMENT <=> EXACTLY_ONE_NATIVE_AXIS_SUPPORT`.

The signed X6 coordinate model realizes this exactly:

- if z has support size 1, every shortest path uses one signed native axis only and the endpoint displacement is a primitive straight segment;
- if support size >=2, every realization is a composite native path and no new primitive diagonal direction is introduced.

## 3. Exact shortest-path multiplicity

Let

`m=||z||_1`.

A shortest path must use exactly `|z_i|` occurrences of the required signed direction on axis i. Hence the number of ordered shortest native-axis paths is

`B_min(z)=m! / product_i |z_i|!`.

This is the exact N-BRC multiplicity of shortest realizations.

For support size 1 it equals 1.

For support size >=2 it is >1, so a coarse off-native-axis segment is structurally a multipath object even before any stochastic noise is added.

The observer-level `JITTER` of P000 may then be read from temporal/spatial alternation among these ordered axis microsteps; it is not assumed noise.

## 4. Exact all-length signed endpoint kernel

Fix a target z and total path length M.

Let

`a_i=max(z_i,0)`, `b_i=max(-z_i,0)`.

Baseline shortest length is

`m0=sum_i(a_i+b_i)=||z||_1`.

Any additional path events that leave the endpoint unchanged must be inserted as opposite-sign pairs on the six axes. Therefore:

- if `M<m0` or `M-m0` is odd, the endpoint multiplicity is 0;
- otherwise write `K=(M-m0)/2` and choose `k_i>=0`, `sum k_i=K`;
- plus/minus occurrence counts on axis i are `a_i+k_i`, `b_i+k_i`.

Hence exact N-BRC endpoint multiplicity is

`N_M(z)= M! * sum_{k_1+...+k_6=K} product_i 1/[(a_i+k_i)!(b_i+k_i)!]`.

The shortest-path formula is the special case K=0.

## 5. Exact signed return kernel

For z=0, M must be even, `M=2K`.

Then

`Return_{2K}=(2K)! * sum_{k_1+...+k_6=K} product_i 1/(k_i!)^2`.

Odd-length full spatial returns are impossible in the pure signed-axis coordinate graph.

Small cases:

- `Return_0=1`;
- `Return_2=12` (choose one of 6 axes and either order + then - / - then +);
- `Return_4=396`.

These are full signed-X6 returns, unlike the superseded positive-only relative-endpoint “returns”.

## 6. Positive-rational weighted kernel

Let the exact positive branch weights be

`w_i^+>0`, `w_i^->0`.

For the same k-vector, total branch weight per ordered word is

`product_i (w_i^+)^(a_i+k_i) (w_i^-)^(b_i+k_i)`.

Therefore exact Weighted-BRC endpoint mass is

`W_M(z)=M! * sum_{sum k_i=K} product_i [(w_i^+)^(a_i+k_i)(w_i^-)^(b_i+k_i) / ((a_i+k_i)!(b_i+k_i)!)]`.

All arithmetic remains exact rational when the primitive weights are rational.

Prime-valuation coordinates may be retained before logarithmic readout in the ordinary Weighted-BRC manner.

## 7. Rotation covariance

Every S6 axis permutation preserves:

- `||z||_1`;
- `||z||_E^2`;
- support size;
- shortest-path multiplicity;
- full endpoint kernel under correspondingly permuted signed weights.

Thus the P000 direction gate and BRC multipath count are rotation-covariant at the full axis-permutation skeleton.

## 8. Exact path-count/length inequality

For every displacement z,

`L_E(z) <= N_min(z) <= sqrt(6) L_E(z)`.

This is the finite norm inequality between L2 and L1 component readouts.

Equality on the left holds exactly for support size <=1, i.e. primitive straight displacements.

Therefore primitive native straightness has an exact metric/event characterization:

`PRIMITIVE_STRAIGHT <=> N_min = L_E` (for integer displacement units).

Any genuine multi-axis composite has strict event overhead

`N_min > L_E`.

This gives a quantitative, non-continuum measure of the microstep overhead underlying an apparent off-axis coarse segment.

## 9. Observer discipline

`B_min(z)>1` does not mean multiple Cells occupy one endpoint; it means multiple ordered path witnesses share one spatial endpoint.

The safe hierarchy remains:

`PATH-FORMAL / WEIGHTED BRANCHES -> SIGNED AXIS TRACE -> X6 SPATIAL ENDPOINT -> COARSE APPARENT SEGMENT`.

A coarse apparent straight line is allowed as an effective readout, but it cannot replace the primitive path family before a scope-typed safe quotient is proved.