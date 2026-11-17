# EC49FRU — Four independent original named-observer costs: exact global phase diagram

Date: 2026-11-17. Original pinned science: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Provenance: EC49FRS–FRT, PR #2648 @ `4f745adfb05c8dea4e4436cc24ecc4832870aeaf`. Status: AUTHOR_PROVED / EXACT_FINITE_BELLMAN_CHECKED / NOT_REVIEWED. Independent portable research only; no formal CLAIM, Result or Review.

## Exact model

Use original BRC class 16943, 310 configurations, 141 **complete named** states, all 228 original physically labeled observations (144 terminal, 84 root), and the uniform named-state prior `lambda=0`. Fix root/terminal base-cost ratio `x=1` and terminal cost `t>0`. Reprice only original terminal physical observers `q32,q34,q140,q142` by nonnegative real additive surcharges `a,b,c,d`: their costs are respectively `t(1+a),t(1+b),t(1+c),t(1+d)`. All other original observations cost `t`. Full exact response vectors, native root keys, state provenance, and query identities are retained. Every legal policy is a complete deterministic adaptive tree identifying all 141 named states.

For any tree `Q`, let `U(Q)` be the summed number of query executions on all 141 state paths; `n_j(Q)` counts executions of the **original labeled** observation j. Its normalized expected cost is

`C_Q/t = (U+a*n32+b*n34+c*n140+d*n142)/141.`

### Theorem A (unrestricted four-dimensional global optimum)

For **every** real `a,b,c,d>=0`,

`V(a,b,c,d)/t = min{ 296/141+a, 296/141+b, 298/141+c, 298/141+d, 299/141 }.`

This equality is the Bellman minimum across **all** admissible original-native adaptive trees, not a comparison restricted to previously proposed strategies.

### Exhaustive integer anchors and direct native witnesses

Let integer `z=(A,B,C,D)` encode surcharges `(a,b,c,d)=z/141`. For each state mask S, the exhaustive integer recurrence is

`F_z(S) = min_{j splitting S} { (141+z_j)*|S| + sum_{response fibers T} F_z(T) }`, `F_z(singleton)=0`.

Each 228-action exact Bellman call visited 13063 cached subsets, retaining all original physical observation identities. Original 94-family master SHA256: `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`. Profile CSV SHA256: `a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f`.

| z | Bellman integer F_z(all) | Every optimal first original observation |
|---|---:|---|
| (0,0,0,0) | 41736 = 141*296 | 32,34 |
| (2,2,0,0) | 42018 = 141*298 | 32,34,140,142 |
| (3,3,1,1) | 42159 = 141*299 | 32,34,46,93,140,142 |

Five **complete** original physical-query trees were replayed against all 141 original named state response vectors:

| Tree | First query | Total U | (n32,n34,n140,n142) |
|---|---:|---:|---|
| A | 32 | 296 | (141,0,0,0) |
| A' | 34 | 296 | (0,141,0,0) |
| B | 140 | 298 | (0,0,141,0) |
| B' | 142 | 298 | (0,0,0,141) |
| T | 46 | 299 | (0,0,0,0) |

A,A',B,B' are optimal native trees reconstructed at integer prices (0,10,10,10), (10,0,10,10), (10,10,0,10), (10,10,10,0), respectively. The previously extracted T46 original tree from EC49FRT was replayed independently using the original query index/response map. The five witnesses prove the theorem's upper bound everywhere.

### Proof of the global lower bound

Put `p=min(a,b)`, `q=min(c,d)`. Nonnegative original physical-query incidence implies coordinatewise price monotonicity, hence `V(a,b,c,d)>=V(p,p,q,q)`. Define `X=141p`, `Y=141q` and `G(X,Y)=141^2 V(X/141,X/141,Y/141,Y/141)/t`. The infimum of the exact affine tree costs is concave and separately nondecreasing. The three integer Bellman anchors give

`G(0,0)=41736`, `G(2,0)=42018`, `G(3,1)=42159`.

From native witness costs, `G(X,Y)<=H(X,Y):=min{41736+141X,42018+141Y,42159}`.

1. On `0<=X<=2,Y=0`, concavity between (0,0) and (2,0) gives `G>=41736+141X`; witness A matches. Separate monotonicity extends equality to all `0<=X<=2,Y>=0`.
2. On `(X,Y)=(2+s,s)`, `0<=s<=1`, concavity between the exact endpoints (2,0) and (3,1) gives `G>=42018+141s`; witness A matches. Monotonicity in Y extends equality to `2<=X<=3,Y>=X-2`.
3. If `0<=Y<=1,X>=2+Y`, monotonicity in X gives `G(X,Y)>=G(2+Y,Y)=42018+141Y`; witness B matches.
4. If `X>=3,Y>=1`, monotonicity gives `G(X,Y)>=G(3,1)=42159`; witness T matches.

These four sets cover the nonnegative (X,Y)-quadrant, and in each set the indicated matching witness attains H. Therefore `G(X,Y)=H(X,Y)` everywhere. In particular `V(p,p,q,q)/t=min(296/141+p,298/141+q,299/141)`. Coordinatewise monotonicity supplies this as a lower bound for the original four individual surcharges, while the five witness trees attain that same expression at the least-charged named query of each pair (or avoid the four queries). QED.

### Theorem B (minimal universal policy menu)

Exactly **five** fixed complete native deterministic trees are necessary and sufficient to achieve V at every nonnegative four-dimensional price vector. The five witnesses suffice.

For necessity, each tree has one affine price function whose gradient is `(n32,n34,n140,n142)/141`. The proven value has five nonempty open full-dimensional chambers with distinct gradients `e32,e34,e140,e142,0`: each single-coordinate A/A'/B/B' chamber is open under strict price inequalities, as is the constant 299 chamber `min(a,b)>3/141, min(c,d)>1/141`. An affine function that equals V on an open subset of a chamber must have that chamber's gradient; one tree cannot match two different chamber gradients. Any universal finite fixed-tree menu therefore needs at least five members, achieved by A,A',B,B',T. QED.

## Exact checks and limits

Three additional four-coordinate integer price probes gave: `z=(1,7,10,3):41877` (first q32), `z=(5,4,0,9):42018` (first q140), `z=(4,6,2,3):42159` (first q46 or q93). All used 228 physical queries and 13063 cached subsets. The complete machine certificate includes all five explicit identifying trees, 141-state replays and native observer-use counts; the local self-contained source/evidence archive carries the raw pinned inputs. This is an exact finite + analytic model-internal result; separate review remains pending. It does not alter P000, X6 spatial identity or any formal Source ownership state.

**Next:** identify the first exact native incidence-Pareto change under strictly positive query **discounts** (`a,b,c,d>-1`), or under a fifth separately repriced original physical query. Preserve the joint original-response semantics and native per-query labels.