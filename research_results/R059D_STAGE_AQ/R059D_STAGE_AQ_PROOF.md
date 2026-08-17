# R059D Stage AQ — Proof

Researcher-ID: `EM-R059D-AQ-3A7E61`

Task: `RS-R059D-STAGE-AQ-NATIVE-CELL-ESCAPE-MULTIPATH-REACHABILITY`

Frozen source: `78f0d56edecb5cd57967b9ff0f1a2d3567550120`

Frozen parent: `c25b6d0385648c27292f25aeeeff2b816654a4ba`

## 1. Native carrier through the signed-origin A2 conjugacy

Use the old integer A2 chart only as an incidence/CELL_ID chart.  Write an auxiliary vertex as `(i,j,-i-j)` and apply the already-frozen componentwise `ENC_SIGNED` map to obtain its native signed-origin representative.  Thus an auxiliary zero component means the glued native origin component `O_E=[+1]=[-1]`; it is never a native coordinate zero.

Define two elementary triangular half-cells by their auxiliary vertex labels

- `U(i,j)={v(i,j),v(i+1,j),v(i,j+1)}`;
- `D(i,j)={v(i+1,j),v(i,j+1),v(i+1,j+1)}`.

Every pair of vertices in one listed triangle differs by one primitive A2 direction.  Hence these are exactly the two orientations of the elementary triangular incidence cell.

A direct shared-edge check gives

`N3(U(i,j))={D(i,j),D(i,j-1),D(i-1,j)}`

and

`N3(D(i,j))={U(i,j),U(i+1,j),U(i,j+1)}`.

Therefore every elementary cell has exactly three edge-adjacent cells.  No source area, angle, norm or circle is used.

The six cells incident to the auxiliary origin vertex are

`U(0,0), U(-1,0), U(0,-1), D(-1,-1), D(-1,0), D(0,-1)`.

Their native images are exactly `STAR(O_E)`.

The A2 generators

`R(i,j)=(-j,i+j)` and `F(i,j)=(j,i)`

act vertexwise.  On cells,

`R(U(i,j))=D(-j-1,i+j)`

and

`R(D(i,j))=U(-j-1,i+j+1)`;

`F` swaps `i,j` and preserves the U/D type.  Shared edges and `STAR(O_E)` are preserved, giving the required D6 action.

## 2. Exact shell certificate

Define the integer cell-index numerator

`K(U(i,j))=(3i+1,3j+1)`

and

`K(D(i,j))=(3i+2,3j+2)`.

For `K(C)=(x,y)` put

`H(C)=max(|x|,|y|,|x+y|)`.

This is an A2 incidence-label statistic.  It is not introduced as a source or target metric.

The admissible elementary-cell labels never have `H` divisible by 3.  A six-side residue check gives the successive allowed rings

`H=2,4,5,7,8,10,11,...`.

The graph layer numbered `s` is exactly the allowed H-ring

- `H=3n+2` when `s=2n`;
- `H=3n+4` when `s=2n+1`.

Equivalently,

`SHELL(C)=floor(2*(H(C)-2)/3)`.

The proof is by induction on these allowed rings.  `H=2` is precisely the six-cell origin star.  Inspecting the three neighbor formulas on each of the six A2 sides shows that crossing one dual edge changes the layer by at most one, every noninitial ring has an inward neighbor, and every ring has an outward neighbor.  Hence the formula is simultaneously an upper and lower bound for the dual-graph distance from `STAR(O_E)`.

Counting the admissible U/D residue points on one six-sided H-ring gives

`|S_s|=6*(floor(s/2)+1)`.

The same local residue check sharpens the outward-neighbor statement:

- an even-shell cell has exactly one neighbor on shell `s+1`;
- an odd-shell cell has exactly two neighbors on shell `s+1`.

All other neighbors have shell at most `s`.  Therefore

`FAR(C)=FAR_PLUS(C)={D in N3(C):SHELL(D)=SHELL(C)+1}`

for every cell.

In particular the escape score is source-free, D6-invariant and strictly outward.

## 3. Escape paths are exactly outward geodesics

Every AQ jump raises shell by exactly one.  Hence a J-jump escape path from a seed of shell `s` ends on shell `s+J`, has graph length J, and realizes the distance increase J.  It is a geodesic continuation away from the origin star.

Conversely, if a dual-graph path raises shell by one at every edge, each edge ends at a shell-maximizing neighbor and therefore belongs to `FAR`.  Thus it is an AQ escape path.

This proves both the geodesic characterization and acyclicity: shell is a strict integer Lyapunov function, so the directed escape graph has no directed cycle.

Because every odd-shell cell has two FAR successors, tied branches occur intrinsically.  Retaining all tied branches yields a canonical set-valued object while no canonical single path follows from the escape rule alone.

## 4. One-step seed theorem

The one-step AP endpoint directions in the auxiliary A2 chart are

`(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)`.

With no known circle arc, the only orientation-neutral local seed choice is to retain every elementary cell incident to the free endpoint.  Each endpoint has six such cells.  For the base endpoint `(1,0)` they are

`D(0,-1),D(0,0),D(1,-1),U(0,0),U(1,-1),U(1,0)`.

Their shell multiset is `{0,0,1,1,2,2}`.  D6 gives the same result at the other five orientations.

Taking the geometric union over all six endpoint orientations gives exactly

`B_2=S_0 union S_1 union S_2`,

with `6+6+12=24` cells.  This statement is finite incidence, not a circle fit.

## 5. Exact all-J reachability

Let the aggregate seed set be `B_2`.

A J-jump path beginning on seed shell `s in {0,1,2}` must end on shell `s+J`.  Therefore

`END_J subset S_J union S_(J+1) union S_(J+2)`.

For the reverse inclusion, take any cell C on one of those three shells, say shell `J+s` with `s in {0,1,2}`.  Repeatedly choose an inward neighbor.  After J steps one reaches shell s, which lies in `B_2`.  Reversing that inward chain produces a shell-increasing FAR path of length J from a seed to C.  Hence

`END_J=S_J union S_(J+1) union S_(J+2)`

for every `J>=0`.

Taking the union over jump counts `0..J` immediately gives

`REACH_LE_J=B_(J+2)`.

Thus all shell cells permitted by the shell range are reachable; there is no hidden angular sector pruning.

The exact endpoint count is

`q(J)+q(J+1)+q(J+2)` with `q(s)=6*(floor(s/2)+1)`, i.e.

- `9J+24` for even J;
- `9J+21` for odd J.

The ball count is

- `6*(n+2)^2` for `J=2n`;
- `6*(n+2)*(n+3)` for `J=2n+1`.

For J>=1 the exact endpoint object is a connected three-shell annular band.  It is not a simple cycle.  The up-to-J object is a filled dual-graph ball.

## 6. Path counts and mergers

The parity theorem for FAR branching implies that every two-jump outward continuation has exactly two extensions.  From `B_2`,

`P_0=24` and `P_1=30`.

Therefore

- `P_(2n)=24*2^n`;
- `P_(2n+1)=30*2^n`.

For one fixed axis-orientation seed set, the analogous formulas are

- `6*2^n` for even `J=2n`;
- `8*2^n` for odd `J=2n+1`.

Different outward geodesics can merge.  The first aggregate merger occurs at J=2.  Endpoint multiplicity is exactly the dynamic-programming recurrence

`m_0(C)=1` on `B_2`,

`m_(J+1)(D)=sum_{C:D in FAR(C)} m_J(C)`.

Multiplicity is provenance only and never changes the endpoint set.

## 7. Circle-emergence obstruction

Only now compare with AP.

The accepted one-step visible AP circle is a six-vertex period-6 orbit.  AQ has a different output type: cells and cell paths.

At J=0, `END_0=B_2` already has 24 cells.  For every J>0, `END_J` is three full shells and has more than six cells.  Moreover every positive AQ jump raises shell, so the AQ directed graph is acyclic.

Therefore no J>=0 makes the AQ one-step endpoint family equal the six-axis AP circle, and no positive AQ path can realize its closed period-6 traversal.

This r=1 exact obstruction is sufficient to rule out a universal law `J=J(r)` that would recover the accepted circle exactly at every radius without changing the AQ output or pruning branches.

The AP axis vertices are incident to the J=0 seed cells, so a loose incidence-envelope containment is tautologically true at r=1.  It is not an emergent circle theorem.

Hence the correct disposition is that the canonical escape object is distinct from the circle.

## 8. Relation to AP collapse direction

AP and AQ answer different questions.

AP evolves endpoint/collapse states on a fixed one-step segment class and can close after six turns.  AQ evolves elementary cells in a strictly outward dual-graph DAG.

Consequently AP coherent DOWN+axis completion is not one distinguished AQ path, and neither is the broader AP `DIRECT_FORWARD_AXIS` policy.  Producing either as a cell path would require an additional endpoint-to-cell lifting rule, and any lift that followed the closed AP cycle would contradict strict shell increase.

AQ therefore does not need `COHERENT_COUPLED_COLLAPSE_DIRECTION`: it never chooses between tied FAR branches.  This bypasses the AP uniqueness question for the new reachability object; it does not prove that the AP scoping axiom was false or unnecessary for the AP theorem itself.

## 9. Final theorem

The native three-neighbor carrier exists.  The graph-distance farthest rule is strict and canonical.  All tied outward branches survive.  The resulting object is the complete family of outward dual-geodesics, with

`END_J=S_J union S_(J+1) union S_(J+2)`

and

`REACH_LE_J=B_(J+2)`

for the full one-step D6 seed family.

It is canonical and set-valued, but it is not the previously accepted circle.

Primary disposition:

`CANONICAL_SET_VALUED_ESCAPE_RESOLVER_PROVED__ESCAPE_OBJECT_DISTINCT_FROM_CIRCLE`.
