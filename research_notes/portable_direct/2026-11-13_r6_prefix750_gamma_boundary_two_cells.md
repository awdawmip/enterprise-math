# PREFIX-750-R6 — Two additional closed Gamma parameter cells excluded (11,52) and transpose

Date: 2026-11-13 Asia/Shanghai. Parent: PREFIX-675; predecessor PREFIX-749-R6.
Frozen scientific source `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`. Result status `AUTHOR_EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED`.

## Theorem, exact model and proof

Keep the 189-layer BRC stopped-survivor kernel, independent rate-one Gamma clocks `T_p,T_z`, `Y=max(T_p,T_z)`, `mu=E[Y]`, `M2=E[Y²]`, `W=M2-mu²`, `V_q=q²W-q mu`, `e=(0,73/500)`. Define the closed cell `R_ij=[i/384,(i+1)/384] × [j/384,(j+1)/384]`.

**For every real q>=2 and every continuous parameter (p,z) in R_(11,52) or R_(52,11), V_q(e)-V_q(p,z)>3q²>0.** Both complete cells are therefore excluded from maximizers of this frozen Gamma auxiliary objective.

Proof: The original 189-layer kernel has nonnegative, symmetric and center-nondecreasing normalized Bernstein survivor coefficients, checked by the frozen source (9,529 nonzero survivor positions, empty final row). These imply Gamma survival tails and their positive integrated first and second moments `mu,M2` are coordinatewise nondecreasing on `[0,1/2]²`, containing both claimed cells.

For each rational closed subrectangle `Q=[a,c]×[b,d]`, put `L=mu(a,b)>=0`, `H=M2(c,d)`. Monotonicity gives `mu(p,z)>=L` and `M2(p,z)<=H` on Q. Since `t=1/q∈(0,1/2]`, exact algebra yields

`[V_q(e)-V_q(p,z)]/q² >= W(e)-H+L²-t(mu(e)-L)`.

The right side is affine in t; its minimum on `[0,1/2]` is attained at an endpoint. Define `B(Q)=min(W(e)-H+L², W(e)-H+L²-(mu(e)-L)/2)`. Partition R_(11,52) into `s×s` rational subrectangles and define `G_s=min B(Q)`. All moment calculations use integer sums and `fractions.Fraction`. For the original cell (11,52) the exact computed floors are:

| s | 2 | 4 | 8 | old comparator (0,3/20), s=1 |
|---|---:|---:|---:|---:|
| floor(1,000,000 G_s) | -86,683,906 | -26,603,110 | **3,524,919** | -206,906,474 |

Thus the *unrounded rational* `G8>3`, proving the uniform strict result for the full continuous cell and **all real** q>=2. Exchanging the two independent identically parameterized Gamma clocks establishes the transpose. Negative coarse lower bounds are inconclusive, not counterexamples.

## Duplicate-coordinate and cumulative scope

All new 384-grid coordinates were compared with exact connector-read PREFIX742–PREFIX749 result arrays. In the older 768-grid PREFIX713 multi-competitor, PREFIX716 and PREFIX718 arrays, the four 768 children `(22,104),(23,104),(22,105),(23,105)` of (11,52) are not listed as additional certified representatives; PREFIX713 parent exceptions are elsewhere. The old PREFIX712 1×1 lower bound was computed explicitly above, while the earlier historical spatial blocks PREFIX729–741 are separate as documented. Full independent all-history union audit remains open.

Relative to the inherited PREFIX749 **author-level** certified union, the two distinct cells give `141984+2=141986` of `147456` full cells, exact fraction `70993/73728 ≈ 96.2904188368%`, leaving `5470` not yet included. This does not assert canonical mathematical acceptance or a result for the original stopping-count maximization target.

## Verification, evidence and next science

The local exact source pair includes original `PREFIX741_R6_INNER_STRIP_194.py` Git blob `d986f644ba513240ea8395e0b221af7946e0efd6`; its frozen moment hashes `797121e567e6422d342b2647cd17ff01187d5000b08bde8a954730d071bed46e` and `814be93bb068b6a6e688e8ea5a466939a06e617b67ab585c177176f57afd57ae` were checked under PREFIX749, unchanged in this continuation. Isolated exact computation checked G2, G4, G8 and the old comparator G1 in one Python process. Companion source `PREFIX750_R6_GAMMA_2_CELLS.py` and `PREFIX750_R6_GAMMA_2_CELLS_RESULTS.json` reproduce the precise calculations. Exact published-checker replay and independent review remain tasks unless separately recorded.

Neighbor (10,52) yielded G8 lower-bound millionth floor `-336068` (inconclusive); investigate stronger 16x16 or more efficient bound there and around (9,51). Preserve frozen P000/science, and audit historical union on one normalized lattice.
