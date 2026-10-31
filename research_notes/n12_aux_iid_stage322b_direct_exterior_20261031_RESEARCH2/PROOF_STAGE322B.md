# Stage322-B — direct-exterior rational certificate and eight-rate Pareto extension

**Status:** TASK_RESEARCH portable author proof, `UNREVIEWED / NOT_ADMITTED`; no native task CLAIM, Result, independent mathematical review, P000-native transfer or external physics claim. Research date: 2026-10-31 (Asia/Shanghai).

**Frozen current inputs:** `awdawmip/chatgpt-global-knowledge` canonical `main@034e6632b42f8af7c8dd39717aff08df7c63769e`, including verified P000 startup projection and original blob, ACTIVE worldview, BRC and math-research rules; `awdawmip/enterprise-math` `main@698c957b38d58886df86599a9eb2e76ba8de1cc4`, `docs/PORTABLE_RESEARCH_PROTOCOL.md`. Predecessor Stage321-B author-side proof/packet at immutable scientific commit `98c2cb373d53a281a4d148b067c825e12f000888`, PR #1736. Previously proved lemmas (with their prior author-side evidence level) are **assumptions for this continuation**: Stage307-B.2 unique algebraic public minimizer and exact root brackets, Stage315-B central-rate MAP reset and uniqueness, Stage316-B exact two-block infimal convolution. Neither those proofs nor Stage321-B are independently admitted herein.

## Model and quantitative statement

Two positive-mass hidden sources, private history `(J,W,Y)`, public `(W,Y)`, source-tagged `(S,J,W,Y)`, eight locked Bernoulli rates, three future accesses. For the all-F three-word observer, write `B_k(z)=z^k(1-z)^(3-k)`, `p=(61,21,9,9)/160`,

`r_k(x,y) = 4 B_k(x)/5 + B_k(y)/5 - p_k`,

`d(x,y) = (1/2) Σ_{k=0}^3 binom(3,k)|r_k(x,y)|`, `b(x,y)=5d(x,y)/16`,

`c(x,y) = [63 D_3(1/4,x) + D_3(3/4,x) + 9 D_3(1/4,y) + 7 D_3(3/4,y)]/256`.

Here `D_3` is the exact total variation of the product law of three independent Bernoulli trials, not a trigonometric or native-heartbeat propagator. The Stage315/316 exact reduction gives `P_3=b(x,y)+b(x',y')` and `T_3=33/1024+c(x,y)+c(x',y')` after unique central MAP reset. The unique minimizer `(x*,y*)` of `d` obeys `r_0=r_1=0`, `r_2>0`, `r_3<0`, and exact brackets

`231083940855521/10^15 < x* < 231083940855522/10^15`,

`555508857277/10^12 < y* < 555508857278/10^12`.

Let `β*=b(x*,y*)`, `P_min=2β*`, `C_3(s)=min_{b(x,y)≤s} c(x,y)`, and `F_3(z)=min_{P_3≤z} T_3` in the declared eight-rate domain.

**Theorem 322B (strict new interval).** For every real `0≤ε≤δ=1/20000`,

`F_3(P_min+ε)=33/1024+c(x*,y*)+c(x_ε,y_ε)`,

where `(x_ε,y_ε)` is the unique **rightward `r_1=0` branch** point satisfying `b=β*+ε`. For `ε>0`, precisely two eight-real-rate optimal vectors exist: one outside block carries all slack, the other is `(x*,y*)`, with the two choices interchanged by block symmetry; the four central rates are uniquely MAP-reset. At `ε=0`, the tagged optimum is unique. Along this branch the cost envelope satisfies the strict continuum curvature bound

`-46 < C_3''(s) < -34` for `β* < s < β*+δ`.

For `0<θ<ε`, the loss from splitting the full budget between the two outer blocks satisfies

`34 θ(ε-θ) < [C_3(β*+θ)+C_3(β*+ε-θ)-C_3(β*)-C_3(β*+ε)] < 46 θ(ε-θ)`.

This grows Stage321-B's `31/5,000,000` certified domain by the exact factor **`250/31` (~8.0645)**. It is an extension of the *proved auxiliary-model local Pareto germ*, not a finding of the true first optimizer-switch point.

## Lemma 1 — exact direct exterior cutoff (new)

Define the **new local rectangle**, not the former B-box,

`R=[229/1000,467/2000] × [11/20,281/500] = [0.229,0.2335]×[0.550,0.562]`.

Let the explicit rational witness be `w=(231083940855/10^12,555508857277/10^12)` and `U=d(w)≥d(x*,y*)`. For **every real `(x,y)` outside the open interior of R**,

`d(x,y)-U > 1/6250 = (16/5)δ`, hence `b(x,y)-β*>δ`.

**Complete rational covering proof.** The four closed rectangles `[0,x_L]×[0,1]`, `[x_R,1]×[0,1]`, `[x_L,x_R]×[0,y_L]`, `[x_L,x_R]×[y_R,1]` cover the complement of the interior of R. For any one of their rational subrectangles `A`, take each exact range `B_k([a,b])` using its endpoints and (only for `k=1,2`) the critical point `k/3` when included. These yield rational lower/upper residual bounds `[l_k,u_k]`; set

`L(A)=(1/2)Σ binom(3,k) max(0,l_k,-u_k) ≤ inf_A d`.

Bisect the longer side until `L(A)-U>1/6250`. The fully executed Fraction checker certifies respectively `(nodes,accepted leaves)=(269,135),(85,43),(35,18),(175,88)`; total **284 accepted covering leaves**, with **strict minimum certificate**

`min_A[L(A)-U] = 203575833018695602516057268618433 / 1250000000000000000000000000000000000 > 1/6250`.

Every leaf is a closed rational rectangle; finite branch-and-bound supplies exhaustive continuum coverage. Multiplication by `5/16` proves the b-gap. This step avoids both the earlier uniform B-box cusp estimate and the former `1/50000` coarse exterior floor.

## Lemma 2 — local 16-tile branch and curvature certificate (new)

Split R into a **4×4 grid of closed rational rectangles**. The attached exact Fraction checker evaluates interval operations on each of the sixteen tiles and verifies all of the following *for every real point of R*:

1. `r_2>0`, `r_3<0`. Hence, using `Σ binom(3,k) r_k=0`,
   `d=3r_2+[r_0]_+ +3[r_1]_+=max_{e0,e1∈{0,1}}(3r_2+e0 r_0+3e1 r_1)`.
2. The **sixteen individual Bernoulli-sign conditions** (four base rates × four future counts) are fixed throughout R. Therefore the exact gradients of tagged cost are, with no hidden absolute-value kink inside R,
   `c_x=-(1-x)(189-183x)/256`, `c_y=3y(1-y)/64`; in particular `c_x<0<c_y`.
3. For all four smooth public-error chambers, `det(∇b,∇c)≠0`: its sign is positive only in chamber `(e0,e1)=(0,0)`, negative in the remaining three. On `r_0=0` and `r_1=0`, the y-derivative is strictly negative and `|dy/dx|<25/2`. The opposite residual changes strictly monotonically along each kink, so the two curves have only the stated common root locally.
4. Along all four oriented kink arms, `|db/dx|>4/25`; increasing public-error directions point away from the root. Exact disjoint slope enclosures for `dc/db` are:
   `r_1/right∈(-5/4,-11/10)`, `r_0/right∈(-1,-4/5)`,
   `r_1/left∈(17/10,19/10)`, `r_0/left∈(27/10,7/2)`.
   The first is strictly cheapest at every matched positive budget.
5. Along `r_1=0/right`, implicit differentiation `v=y'=-r_{1x}/r_{1y}`, `w=y''=-(r_{1xx}+r_{1yy}v²)/r_{1y}` and `B'=b_x+b_yv`, `B''=b_{xx}+b_{yy}v²+b_yw`, `E'=c_x+c_yv`, `E''=c_{xx}+c_{yy}v²+c_yw` gives
   `C_3''=(E''B'-E'B'')/(B')³∈(-46,-34)` uniformly. The checker tests this by rational intervals on *all* 16 tiles, not a mesh of selected parameter points.

## Global completion of theorem

Lemma 1 forces each admissible single-block pair with `b≤β*+δ` into the interior of R. Since the root-to-R margins are all positive, choose the exact x-extension `L=1/2500`. By Lemma 2, the four kink graphs continue within R over `x*±L` because `|dy/dx|<25/2<13` and `13L` is smaller than the smallest y margin. Each oriented public-error rise exceeds `(4/25)L=1/15625>δ`; all four arms therefore reach *every* requested budget in `[0,δ]`.

A minimizer with unused budget is impossible because `c_x<0` and every feasible point lies in the interior of R. At an interior smooth-chamber budget boundary, `det(∇b,∇c)≠0` excludes a stationary constrained minimum. Thus all positive-budget minima lie on kink arms. The four slopes in Lemma 2 have strict disjoint order from their common root, so the unique cheapest single-block minimizer is `r_1/right`, with budget binding. The interval second derivative is strictly negative, making `C_3` strictly concave. Stage316's exact two-block infimal convolution is therefore minimized only by endpoint allocations `θ=0` or `θ=ε`. Integrating `-46<C_3''<-34` over the rectangle `[0,θ]×[0,ε-θ]` gives the strict displayed budget-split penalty. Stage315's unique central reset and the two source-group symmetry choices finish the eight-dimensional uniqueness statement. QED, conditional on the explicitly named established source theorems.

## Independent exact execution, scope and limits

`REPRO_STAGE322B.py` is a stand-alone Python 3 standard-library Fraction checker. Its actual stdout was saved as `REPRO_STAGE322B_EXECUTED_STDOUT.txt`, with final `STAGE322B_50_MICRO_GLOBAL_GERM_EXACT_PASS`. All branch-and-bound comparisons, rectangle enclosures, strict inequalities and endpoint margins use *exact rational arithmetic*; no float is used in a mathematical assertion. Finite numbers of *interval tiles covering the continuum* are rigorous because enclosure semantics and exhaustive coverage are proved above. The script does not independently execute the prior Stage307/315/316 theorems, does not assert a full global Pareto branch-switch location, and is not a Lean proof or external scientific validation.

The public observer `(W,Y)` and tagged observer `(S,J,W,Y)` here are external probability-model interfaces; native P000-X6 six-axis paths, selected three-dimensional slice with third coordinate, triadic closure, ordered time evolution and six-field registered Cell-address observer-preservation bridge remain **unproved separate obligations**.

## Next

Stage323-B: strengthen the direct exterior certificate by expanding R and using adaptive tiled curvature/branch bounds, pushing beyond `δ=1/20000` while distinguishing formal proof boundaries from the actual first optimizer switch. Independently test whether an interior split or the Stage314 algebraic competitor ever becomes globally optimal, with exact public/tagged atoms and algebraic sign certificates. Preserve and re-use Stage322's 284-leaf/16-tile exact certificate rather than re-running it without a mathematical change.
