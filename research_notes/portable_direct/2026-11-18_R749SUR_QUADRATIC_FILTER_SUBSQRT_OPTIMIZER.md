# R749SUR — An exact sub-square-root quadratic-filter optimizer for named two-Port feedback

Date: 2026-11-18 (Asia/Shanghai). Status: `AUTHOR_EXACT_NOT_REVIEWED`. This is auxiliary finite-positive-rational WBRC-T30–T32 **named** Port mathematics, not a native X6 event or a claim on shared X6 task ownership.

## Frozen scientific inputs and provenance

- Scientific pin unchanged: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:definitions/ENTERPRISE_BRC_RECURRENT_PORT_FOUNDATION_20260903.md` (WBRC-T30–T32).
- Exact predecessor R749SUO: `161123938bc7836d62d130a755b3d6601a743182`, especially its author-proved `Q=+1` classification for every named noncanonical maximizer when `M>=116`, and the nearest-factor inverse representation.
- Exact predecessor R749SUP: the near-product witness and the originally proved `O(M^(1/4))` boundary on `M-u`, same commit as SUO.
- Immediate predecessor R749SUQ: `b813c6c8a2b79663e64173adfe784cddaec76b2a`, an `O(M^(1/2))` segmented factor sieve using `O(M^(1/4))` auxiliary words. The present construction replaces the sieve by a **single exact quadratic cutoff and one monotone factor optimization**.
- P000 and ACTIVE worldview remain unchanged: six native spatial axes, triadic primitive closure, provenance-fidelity and separately typed causal time. The matrix model is an auxiliary observer with no asserted native three-force Cell/Link/Port equivalence.

## The exact theorem

For every integer `M>=9999`, consider the noncanonical named configurations
`
1<=a,u,v,d<=M, ad-uv=1, Q=u+v-a-d,
`
and maximize `tau=max(u,v)ad`. The following deterministic algorithm returns the exact maximal `tau` **and every named maximizing configuration** in

`
O(M^(3/8)) integer arithmetic operations,
O(1) auxiliary integer words excluding enumerated output.
`

All integers handled have `O(log M)` bits; bit-complexity accounts separately for exact multiplication, division and integer square root.

### Witness and cutoff

Write `B=M+1`, `t=floor(sqrt(B))`, `k=B-t^2`. Set `j=1` if `k<=t`, otherwise `j=2`. Let `z` be the smallest nonnegative integer with `z(z+j)>=jt-k`. Set

`
x0=t-z, y0=t+z+j, n0=x0*y0<=B,
T0=(n0-1)(n0-x0-1)(n0-y0-1),
K=M(M^2+B)-T0,
Phi(x)=M^2(x^2+B)-Kx.
`

There is a unique smallest integer `x_min` in `[2,x0]` satisfying `Phi(x_min)<=0`. Find it by a monotone binary search.

For each integer `x=x_min,...,t` put `y=floor(B/x)`. Ignore a pair if `xy-x-y<1`, otherwise compute

`
T(x,y)=(xy-1)(xy-x-1)(xy-y-1).
`

Keep all pairs attaining the greatest `T`. For every such pair reconstruct

`
(a,u,v,d)=(xy-x-1, xy-1, xy-x-y, xy-y-1).
`

Swap the diagonal labels `x,y` when distinct and independently swap the two directed Port labels `u,v`. Every optimum produces exactly 2 named configurations if `x=y`, otherwise exactly 4; distinct maximizing pairs contribute additively.

### Proof 1 — complete factor parametrization and monotonic y

R749SUO proves that all noncanonical maximizers here have `Q=+1`. After orienting `u=max(u,v)`, put `x=u-a` and `y=u-d`: both are integers at least 2, and `xy=u+1<=B`. Conversely each admissible positive factor pair reconstructs a determinant-one, `Q=1` named tuple as displayed.

For a fixed integer `x>=2` and any admissible `y>=x`, all three positive factors in
`T=(xy-1)((x y)-x-1)((x-1)y-1)` strictly increase with `y`. Thus the best `y` at a fixed smaller factor `x<=t` is exactly `floor(B/x)`. It suffices to inspect the smaller factor `x=2,...,t`.

### Proof 2 — exact upper envelope and safe cutoff

For fixed `x>=2` the same monotonicity extends to real `y>=x`. Therefore, for any admissible integer `y` and `xy<=B`,

`
T(x,y)<=T(x,B/x)=M[M^2+B-M(x+B/x)].
`

The witness `x0,y0` is admissible. By AM–GM, its score obeys `T0<=F(B)`, where `F(B)=M[M^2+B-2M sqrt(B)]`. Consequently `K/M^2>=2 sqrt(B)` and `x+B/x` strictly decreases for `2<=x<=t`. Any maximizer, whose score is at least `T0`, must satisfy

`
M^2(x^2+B)<=Kx, equivalently Phi(x)<=0.
`

The witness itself satisfies `Phi(x0)<=0`. Therefore the binary-search cutoff exists and no smaller `x<x_min` can optimize. The remaining sweep is exact, including all ties.

### Proof 3 — uniform sub-square-root operation bound

Let `delta=B-x0*y0`. The minimality of `z` implies `0<=delta<=2 ceil(sqrt(t))+1`; also `0<=x0+y0-2sqrt(B)<=2`. Define for real `n,s` the score polynomial
`
f(n,s)=(n-1)^3+n(n-1)-(n-1)^2 s.
`
For `n` between `n0` and `B`, its derivative in `n` is at most `3B^2+2B`. Hence

`
0<=F(B)-T0<=2M^2+(3B^2+2B)delta.
`

Since `B>=10000`, `(3B^2+2B)/M^2<=4`. Put
`
Delta=(F(B)-T0)/M^2<=8 ceil(sqrt(t))+6.
`
Every surviving smaller factor `x<=t<=sqrt(B)` satisfies
`
(x-sqrt(B))^2/x=x+B/x-2sqrt(B)<=Delta.
`
Therefore
`
t-x <= B^(1/4) sqrt(8 ceil(sqrt(t))+6)=O(B^(3/8)).
`
In particular the cutoff leaves at most `1+B^(1/4)sqrt(8 ceil(sqrt(t))+6)` candidate integers. Building `z` takes `O(B^(1/4))` increments, binary search takes `O(log B)`, and the factor sweep takes `O(B^(3/8))`. Thus the claimed `O(M^(3/8))` integer-operation time follows. Only fixed scalar integers are needed apart from streamed/listed maximizing pairs. QED.

## Exact validation and interpretation

The attached Python-standard-library program uses only exact integers. It independently enumerates **every smaller factor** `2<=x<=floor(sqrt(M+1))` (not the cutoff) and compares exact scores, closest pairs and all named tie multiplicities with the filtered optimizer for **all 15,002 integers** `9999<=M<=25000`, plus seven sizes up to `M=10^12`. It checks the exact integer cutoff boundary and five scores reported in R749SUQ. All checks returned `PASS`. The largest filtered window in the contiguous range was 78 candidates. At `M=10^12` the filtered algorithm checked 53,328 candidate smaller factors; the independent full-factor oracle checked up to 1,000,000.

The analytical theorem depends on the explicitly cited, **author-proved but not independently reviewed** R749SUO `Q=+1` classification. The finite program validates this optimizer's independent `Q=+1` implementation; it does not independently reprove that classification or promote any new native-world conclusion.

## New questions / handoff

1. Prove a tighter universal bound on `x` (e.g. `O(M^(1/4))` width), or produce a family showing the `M^(3/8)` window cannot be improved under the same witness-only envelope.
2. Investigate output-sensitive grouping of the floor quotients `floor((M+1)/x)` without dropping named Port ties; verify actual arithmetic and memory improvements.
3. Separately construct a source-pinned native X6 three-force Cell/Link/Port event with licensed resource/causal-time transitions and a provenance-faithful observer map. No such bridge is established by this auxiliary theorem.

Provenance: original R2 portable research line; historic `EM-DIRECT-44C346` and `RA-A16A5E663104EBDBA287C665` are **historic identifiers**, not authenticated possession of a current Source session/CLAIM. Activity association may follow the current original-session process without redoing the mathematics.
