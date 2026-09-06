# P000 FCC 六轴原生坐标桥与旋转换图图册 — Research Return

Status: `FROZEN RESEARCH RETURN / DRIVER REVIEW REQUIRED`

Researcher-ID: `EM-P000FCC-7B4D2A`
Task-ID: `RS-P000-FCC-NATIVE-COORDINATE-BRIDGE-ROTATION-ATLAS`
Publication-ID: `TP2-0B7E6C14F3A95D208E61`
Claim-ID: `chatgpt-p000fcc-20260829-2118-7b4d2a`
Execution base: `65d1cae115e648f5154a898cd3ba83a2a2b27223`

Hard target: `P000_FCC_NATIVE_SIX_AXIS_ROTATIONAL_COORDINATE_ATLAS_EXACTLY_CLASSIFIED_OR_OBSTRUCTED`

Terminal class: `STRICT_PARTIAL_OR_GROUPOID_ATLAS_PROVED`

## 1. Terminal theorem

The FCC carrier admits an exact six-axis atlas **after** an axis-to-carrier frame is supplied, but the current frozen inputs do not canonically select that frame. The strongest exact object is therefore:

`FRAME-CONDITIONED REGULAR-COVERING ATLAS + UNFRAMED S6 FRAME GROUPOID`.

This neither reduces P000 from six native dimensions to carrier rank three nor identifies carrier collisions with native equality.

## 2. Explicit task-local native model

Use the witness model `N=Z^6` with native adjacency

`q ~ q +/- e_i`, `i=1,...,6`.

Its native L1 degree is 12. This is a task-local P000-compatible address model only; it is **not** promoted as the canonical full-P000 Cell identity law. Directed `+/-e_i` steps are declared in this model independently of FCC antipode notation.

Choose one frame

`phi0:(E1,E2,E3,E4,E5,E6) -> (L1,L3,L6,L4,L5,L2)`.

Then the four native chart supports are

- `J_A={E1,E2,E3} -> S_A={L1,L3,L6}`;
- `J_B={E1,E4,E5} -> S_B={L1,L4,L5}`;
- `J_C={E2,E5,E6} -> S_C={L2,L3,L5}`;
- `J_D={E3,E4,E6} -> S_D={L2,L4,L6}`.

Every axis occurs in exactly two charts and every chart pair overlaps in exactly one axis. Hence the four charts and six axes/line-families form the vertex-edge incidence of `K4`.

## 3. Exact 120-degree charts and transitions

With FCC representatives

`v1=(1,1,0)`, `v2=(1,-1,0)`, `v3=(1,0,1)`, `v4=(1,0,-1)`, `v5=(0,1,1)`, `v6=(0,1,-1)`,

use local orientations

- `A:(+v1,-v3,-v6)`;
- `B:(+v1,-v4,-v5)`;
- `C:(+v2,-v3,+v5)`;
- `D:(+v2,-v4,+v6)`.

In each chart all squared norms are 2, all pairwise dot products are -1, and the three oriented vectors sum to zero. Thus every chart is an exact equal-length 120-degree carrier chart.

Overlap signs are:

`AB:L1:+1`, `AC:L3:+1`, `AD:L6:-1`, `BC:L5:-1`, `BD:L4:+1`, `CD:L2:+1`.

These are carrier presentation signs, not primitive native negative axes.

## 4. Exact carrier readout and kernel

Relative to native axis order, use columns

`W=(v1,v3,v6,v4,v5,v2)`

and readout `A:Z^6 -> Z^3` with matrix

```
[1 1  0  1 0  1]
[1 0  1  0 1 -1]
[0 1 -1 -1 1  0]
```

The image is exactly the FCC lattice

`D3={(x,y,z) in Z^3 : x+y+z is even}`.

For `(x,y,z) in D3`, set

`alpha=(x+y-z)/2`, `beta=(x+z-y)/2`, `gamma=(y+z-x)/2`;

then `(x,y,z)=alpha*v1+beta*v3+gamma*v5`.

The kernel has rank three. A primitive basis is

- `k_A=(1,-1,-1,0,0,0)`;
- `k_B=(1,0,0,-1,-1,0)`;
- `k_C=(0,-1,0,0,1,1)`.

The fourth chart relation is `k_D=(0,0,1,-1,0,1)` and satisfies

`k_A-k_B-k_C+k_D=0`.

The 12 native increments `+/-e_i` map bijectively to the 12 FCC nearest-neighbor rays. Therefore the Cayley-graph map is a regular covering onto `D3`, with deck group

`ker(A) ~= Z^3`.

Exact identity boundary:

`A(q)=A(q') iff q-q' in ker(A)`,

while native equality remains `q=q'`. Carrier kernel collisions are never native-state equality.

## 5. Exact discrete rotation atlas

Let `G=SO(3,Z)` denote orientation-preserving signed permutation matrices. Exact enumeration gives `|G|=24`.

`G` acts faithfully on the six FCC line families and the four slice charts. The induced action on the four charts is `S4`; every line stabilizer has order 4 and every slice stabilizer order 6.

For `R in G`, write

`R v_i = eps_R(i) v_{pi_R(i)}`.

Relative to a chosen frame, define the signed native-address lift

`R~ e_i = eps_R(phi0(i)) e_{phi0^{-1}(pi_R(phi0(i)))}`.

Then exactly

`A R~ = R A`.

The checker verifies all 24 equivariance cases, all `24^2=576` lift-composition identities, and invariance of `ker(A)`.

For every rotation `R` and chart `s`, there is one `tau(R,s) in {+1,-1}` such that all three locally oriented chart vectors transport with that same sign. Exact enumeration verifies 96 chart transports and all 2304 cocycle identities

`tau(R2 R1,s)=tau(R2,R1 s) tau(R1,s)`.

Thus the four overlapping 120-degree charts form an exact finite transition groupoid, not merely a visualization.

## 6. Canonical-frame obstruction

Without additional axis/carrier incidence data, six named native axes and six named FCC line families admit `6!=720` bijective frames.

Exact counts:

- no chart constraint: `720` frames;
- require only `J_A -> S_A` as a set: `36` frames;
- also require `J_B -> S_B` as a set: `4` frames;
- a full named frame selects one.

With `k` pointwise axis-line anchors, residual stabilizer orders are

`720,120,24,6,2,1,1` for `k=0,...,6`.

So five independent anchors plus bijectivity force the sixth in the maximally symmetric case. This independently agrees with the later full-Cell `AXIS_CHANNEL_FRAME` obstruction found in PR #849, but the present checker reproduces the finite frame counts directly.

Therefore an unframed global function `E_i -> L_j` is **not** currently a theorem. The canonical object before frame choice is an `S6` torsor/groupoid of possible atlases.

## 7. Coordinate-continuity criterion

Translation is exact because

`A(q+u)=A(q)+A(u)`.

No FCC stacking bit is required. Carrier coordinates reconstruct a native state only up to the deck coset `q+ker(A)` unless a native lift/initial address is retained.

Rotation transport is exact iff the atlas datum includes an axis/carrier frame and the frame is transported by the signed lift above. Without a frame, only the induced action on the frame groupoid is canonical.

## 8. HCP regression and no-overclaim boundary

The accepted HCP shell is not centrally symmetric: it contains `(1,1,1)` but not `(-1,-1,-1)`. Therefore HCP does not supply six canonical unoriented opposite line families from its 12 contacts.

The theorem is `FCC-SELECTED / NOT BARLOW-UNIVERSAL`. It makes no inference `12 carrier contacts -> 6 native axes`.

No continuous `SO(3)`/`SO(6)` geometry is imported as native truth, no carrier antipode is promoted to a primitive native axis equivalence, and no quotient by `ker(A)` is promoted to native identity.

## 9. Deterministic evidence

Checker:

`scripts/check_p000_fcc_native_coordinate_bridge_rotation_atlas.py`

Certificate:

`research_artifacts/P000_FCC_NATIVE_COORDINATE_BRIDGE_ROTATION_ATLAS/exact_certificate_20260829.json`

The exact checker covers six-line/four-slice incidence, 120-degree identities, overlap signs, `D3` surjectivity, rank-three kernel, local covering, frame torsor counts, all 24 rotations, 576 lift compositions, 96 chart transports, 2304 cocycle checks, and HCP non-central-symmetry regression.

## 10. Driver recommendation

Disposition requested: `ACCEPTED / NO FOUNDATION PROMOTION`.

If accepted, the clean successor is to decide whether a canonical native `AXIS_CHANNEL_FRAME` / axis-handle transport relation can be derived or must be explicitly added. The FCC atlas itself should remain an exact frame-conditioned readout carrier, not native six-dimensional identity.
