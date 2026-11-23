# X6 R159 — Global minimum-cardinality six-witness optimizer on the fixed 17:22 weight slice

2026-11-24. AUTHOR ANALYTIC ARGUMENT WITH EXACT FINITE CERTIFICATE / NOT_REVIEWED.
Continuation of R158@613bc262ed6906e2fa0315cf6864ec6b22869d48; frozen static observer R121@8085ff663b5987c58a1bc0a4a3b1d7da3a1d89fd and R122@0687aa24f5402da3b35f914dd6907967a9805b94 unchanged. This is a parameter-space calculation on the declared three-axis slice of X6, not a two-dimensional native spatial plane or native heartbeat dynamics. No change to P000, native R063, final Cell addresses or physical attribution.

## Theorem

For Port 10 retain nonzero integer triples v=(x,y,z) with max(sum positive components, sum absolute negative components)<=10, up to overall sign, with first nonzero coordinate positive. There are 1935 representatives. Define heights (0,x+3y+6z,3x+12y+30z,7x+39y+126z), six absolute pair gaps g in order 01,02,03,12,13,23, and capacities s=(136+B,312,136+D,176+B,B+D,176+D). Set F_v=max_j g_j/s_j and eta=min_v F_v.

For every positive real B,D, eta=min_{v in W} F_v where
W={(6,-1,0),(1,0,0),(5,-1,0),(9,-5,1),(4,-1,0),(6,-4,1)}.

Moreover W is the unique smallest fixed subset of the 1935 directions that yields eta everywhere: every one of its six directions is a unique full-population minimizer at some positive rational pair. No other fixed subset with fewer than six directions works. This is a value theorem, not a classification of all ties or near members. In particular (5,-4,1) remains a possible near direction and may tie; its removal is justified for the minimum-value observer only. All six BRC gap channels are retained.

| v | B | D | unique eta | second-smallest score |
|---|---:|---:|---:|---:|
| (6,-1,0) | 1 | 1 | 3/137 | 4/177 |
| (1,0,0) | 4 | 521 | 2/175 | 8/697 |
| (5,-1,0) | 46 | 495 | 6/541 | 7/631 |
| (9,-5,1) | 91 | 430 | 6/521 | 7/606 |
| (4,-1,0) | 139 | 1119 | 6/629 | 12/1255 |
| (6,-4,1) | 1 | 1652 | 4/551 | 1/137 |

## Exact coverage proof

First, the R121/R149 integer gap-component dominance argument reduces the optimizer value to the 12 Pareto rows. The companion independently re-enumerates the 1935 sign representatives and checks every row has a Pareto dominator. The six omitted Pareto rows are (3,-7,2),(3,-4,1),(4,-4,1),(5,-4,1),(7,-1,0),(7,2,-1).

To cover all unbounded positive B,D with no sampling and no arbitrary truncation, use projective parameter coordinates b=B/(1+B+D), d=D/(1+B+D), t=1-b-d. The positive quadrant bijects the interior b>0,d>0,t>0 of the closed parameter triangle. Multiplication of all capacities by t gives the affine forms
(136t+b,312t,136t+d,176t+b,b+d,176t+d).
These are positive on the interior. Comparisons of any two scores are unchanged by this common positive multiplier. Triangle edges are certificate boundaries only, not added physical weights. This preserves the complete joint six-gap readout, not the native space.

Suppose an omitted Pareto row v strictly improves on all six W rows at a positive parameter point. By continuity it does so on an open neighborhood inside the triangle. For any positive active channel j of v with numerator n, its closed active-channel region is the intersection of six affine inequalities n*s'_k-g_k(v)*s'_j>=0. On that region, F_w>F_v iff at least one channel k of w satisfies g_k(w)*s'_j-n*s'_k>0. Thus for each active j, start with the closed triangle, clip by v's six weak inequalities, then successively intersect with each W row's union of strict halfspaces (retain closures for the clipping). An identically zero strict comparison is discarded. Polygons of zero area may be discarded: strict improvement gives an open subset, and the finitely many active-channel boundaries and selected strict affine inequalities cannot cover it by zero-area sets. Conversely any positive-area surviving polygon has an interior point in the open triangle away from the finitely many nonidentically-zero equality lines, giving actual strict improvement. Exact rational edge intersections implement closed clipping. The signed shoelace area is positive for every nondegenerate convex polygon in the maintained counterclockwise order.

The executable checks every positive active numerator for every omitted row (33 active-channel cases), with all six W comparisons. All final positive-area cell lists are empty. Therefore no strict improvement over W is possible on the positive quadrant. Since W is itself feasible, equality follows including all finite equality/tie walls by the same strict-improvement contradiction. The six exact unique-winner checks in the table evaluate every one of the 1935 rows; strict separation from the second score proves each member indispensable for ANY fixed direction subset. Thus the six-row representation is globally irredundant and unique minimum-cardinality. A scoring algorithm not based on fixed rows is not subject to this cardinality claim.

## Executed reproducible certificate

Python 3 exact integers and Fraction. Companion immutable source:
1bb93f9b2c101d026649cd01a77d3585b6283c0e:research_notes/portable_direct/x6_r159_global_six_witness_verify.py.
Executed Git blob 898d890b1607f57d2d4e6308c30d7188964c1580; SHA256 a97931ecb7144b83f767d47074427e8ae39398d937ecb9cfeaac5724b9f027b0. Remote immutable blob and full text match the submitted executed code.
Actual stdout:
```
EXCLUDED FROM OPTIMIZER BANK (3, -7, 2) [0, 0, 0, 0, 0]
EXCLUDED FROM OPTIMIZER BANK (3, -4, 1) [0, 0, 0, 0, 0]
EXCLUDED FROM OPTIMIZER BANK (4, -4, 1) [0, 0, 0, 0, 0]
EXCLUDED FROM OPTIMIZER BANK (5, -4, 1) [0, 0, 0, 0, 0, 0]
EXCLUDED FROM OPTIMIZER BANK (7, -1, 0) [0, 0, 0, 0, 0, 0]
EXCLUDED FROM OPTIMIZER BANK (7, 2, -1) [0, 0, 0, 0, 0, 0]
UNIQUE (6, -1, 0) 1 1 3/137 4/177
UNIQUE (1, 0, 0) 4 521 2/175 8/697
UNIQUE (5, -1, 0) 46 495 6/541 7/631
UNIQUE (9, -5, 1) 91 430 6/521 7/606
UNIQUE (4, -1, 0) 139 1119 6/629 12/1255
UNIQUE (6, -4, 1) 1 1652 4/551 1/137
SIX-WITNESS GLOBAL IRREDUNDANT BANK PASS
```
The proof handles the entire positive parameter domain without extrapolating the six rational witnesses. It establishes minimum bank cardinality for this fixed weight ratio, not all four weights independently.

## Continuation and status

The projective affine comparison certificate is reusable for arbitrary fixed positive first/third-weight ratios, and its homogeneous form can be lifted to a three-dimensional normalized four-weight simplex. Next determine the exact ratio intervals on which this six-row bank remains sufficient, and whether its cardinality changes when C/A moves away from 22/17. Separately unify all strict near membership pieces and audit seams without removing tied or merely near directions. Independent review and formal Result/Review remain pending; no native task CLAIM is asserted. Original own registration receipt r2-20261124-0310-r155-own-session-v1 SUCCEEDED, historical Researcher EM-DIRECT-AE5AD5 / RA-B60559848FD879270DCA6317. Current native task read r2-20261124-0710-x6-task-read was RUNNING at preparation; no native task write submitted. P000 and current worldview read; frozen science unchanged.
