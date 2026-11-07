# Stage332-B — global low-error confinement and exact 16-tag sign classification

Date 2026-10-31. **PORTABLE_AUTHOR_THEOREM / EXACT_INTEGER_INTERVAL_EXECUTED / UNREVIEWED / NOT_ADMITTED**. This is a theorem solely for the three-visit auxiliary Bernoulli/BRC-labelled observer; it does **not** establish native P000 X6 dynamics, the independently ordered time, the three-dimensional slice's third coordinate, triadic closure, or an observer-preserving Cell-address bridge.

## Sources, frozen inputs, permissions

Account rules frozen at `awdawmip/chatgpt-global-knowledge main@e1a931f0cd580cfaa5cbee3e3914dc2b203880d8`; project rules frozen at `awdawmip/enterprise-math main@e257f0d7f37192bf166bae9148d89d6785bf378e`. Read global bootstrap/manual, project bootstrap/TASK role, P000 startup projection (original blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc` matched), ACTIVE world, and project portable/automated research protocols. Mathematics directly resumes Stage331-B `7433a2c5da8d172d65b60bef284cbfa3dde0905e` and uses Stage328-B `fec395bea87ac0c9d464ac31bb9439c2e1bb2aef` only for the optional inherited two-source cusp consequence. Native owner enumeration returned `CONTROL_QUOTA`; no verified own CLAIM, Source Result, independent review or admission. This work is portable author evidence. No native heartbeat or phase BRC experiment is claimed; the integer/rational arithmetic here establishes a theorem about the pre-existing external auxiliary probability model, not native physical residuals.

## Exact model

For `k=0,1,2,3`, put `B_k(z)=z^k(1-z)^(3-k)` and `w=(1,3,3,1)`, `m=(61,21,9,9)`. For `x,y in [0,1]`,

`r_k(x,y) = [4 B_k(x)+B_k(y)]/5 - m_k/160`,

`b(x,y) = (5/32) * sum_k w_k |r_k(x,y)|`.

The source-tagged comparisons in the inherited objective `c(x,y)` are precisely `B_k(a)-B_k(z)` for `a in {1/4,3/4}`, `z in {x,y}`, `k=0,1,2,3` (16 comparisons), with source-specific positive outer weights. Sign at zero is a separate stratum, not a choice of positive/negative sign.

## Theorem A (standalone, all real parameters)

**For every `x,y in [0,1]`,**

`b(x,y) <= 61/10000  ==>  21/100 <= x <= 6/25 AND 1/2 <= y <= 2/3`.

Proof is a finite *exact interval cover*, not sample testing. Let `D=2^20`, `D3=D^3`, `Q_k(n)=27 n^k(D-n)^(3-k)`. On any closed dyadic interval `[a,d]/D`, the minimum of `Q_k` occurs at an endpoint for all k. The maximum is at an endpoint, except that `k=1` allows `4D3` when `D/3` is in the interval, and `k=2` allows `4D3` when `2D/3` is in the interval. This follows from direct differentiation of the four cubic polynomials (the endpoint maxima for k=0,3 and unique interior maxima for k=1,2). On a closed rectangle `(a,d,c,e)/D`, compute corresponding integer extrema `Xlo,Xhi,Ylo,Yhi`. Then for every point of this *continuous real rectangle*,

`L_k/(160*27*D3) <= r_k <= U_k/(160*27*D3)`

where `L_k=32(4 Xlo+Ylo)-27 m_k D3` and `U_k=32(4 Xhi+Yhi)-27 m_k D3`.

Set `h_k = L_k` if `L_k>0`, `-U_k` if `U_k<0`, and zero otherwise. Therefore

`b >= [sum_k w_k h_k]/[1024*27*D3]`.

The deterministic recursive checker accepts a box if (A) it lies in the asserted target rectangle, or (B) the above integer lower bound is **strictly** larger than `61/10000`. All other boxes are split exactly at the midpoint; use x if `4*(x-width)>=y-width` (unless x resolution exhausted), else y. Starting from the entire closed unit square, it terminates in **127 leaves**: **15 wholly inside the target rectangle and 112 certified b>61/10000**, maximum depth **18**. Exact integer area sum is `D^2=1099511627776`. The program rechecks the accepted labels, widths, thresholds, and covering sum, and its recursive all-children traversal establishes that no box is omitted. Shared boundaries do not weaken strict exclusions. The complete 127-leaf manifest is in `CERTIFICATE_STAGE332B.csv`; serialized data lines have SHA256 `c4f6349bef60424af9921ab47e981385c84bb45dd747f087938c109922a19125`. All calculations are unbounded integers. Consequently every real point outside the target rectangle has `b>61/10000`, proving the theorem.

## Theorem B (standalone, all 16 source-tagged comparisons)

At every real `(x,y)` with `b(x,y)<=61/10000`, the 16 tagged comparison signs are the following, in k order `k=0,1,2,3`:

| variable z | anchor a | signs `sgn[B_k(a)-B_k(z)]` |
|---|---|---|
| x | 1/4 | `- + + +` |
| x | 3/4 | `- - + +` |
| y | 1/4 | `+ + - -` |
| y | 3/4 | `- - σ +` |

Here `σ=+` for `y<y†`, `σ=0` for `y=y†`, and `σ=-` for `y>y†`, with the **only** potentially vanishing tagged comparison in the feasible region at

`y† = (1+sqrt(13))/8`, exactly the k=2 term in `B_2(3/4)-B_2(y)`.

Proof. The k=0 difference has the sign of `(z-a)` and the k=3 difference the opposite sign. The other two factor over rational polynomials:

`B_1(a)-B_1(z)=-(z-a)[z²+(a-2)z+(1-a)²]`,

`B_2(a)-B_2(z)= (z-a)[z²+(a-1)z+a(a-1)]`.

Besides the anchor root `z=a`, all roots in `(0,1)` of these differences are:

- `B_1(1/4)` : `(7-sqrt(13))/8` in `(42/100,43/100)`;
- `B_1(3/4)` : `(5-sqrt(21))/8` in `(5/100,6/100)`;
- `B_2(1/4)` : `(3+sqrt(21))/8` in `(94/100,95/100)`;
- `B_2(3/4)` : `(1+sqrt(13))/8` in `(57/100,58/100)`.

The unused companion quadratic roots lie outside `[0,1]`. Root isolation is purely rational by squaring the strict intervals `89/25<sqrt(13)<91/25` and `113/25<sqrt(21)<23/5`. By Theorem A, `x in [0.21,0.24]`, `y in [0.5,2/3]`; hence all anchor roots and all three other nontrivial roots are **outside** the corresponding parameter intervals. Only the listed y† root is inside. Signs on each connected region are fixed by one exact rational evaluation (the verifier checks z=23/100, z=11/20, and z=3/5), yielding the table; the boundaries are accounted for because no other roots lie in the intervals.

Moreover this remaining tagged-sign change **really occurs inside the low-error feasible region**. For `x=23/100` and every `y in [57/100,58/100]`, exact endpoint/critical-point interval estimates yield

`b(x,y) <= 147739/32000000 < 61/10000`.

The interval contains y† and has feasible points on both sides. Thus the two open tagged chambers and their exact zero boundary cannot be removed from the feasible search. The classification is sharp in this sense. It does not classify the public r0/r1/r3 zero boundaries or decide the global optimum.

## Corollary C (conditional use in the two-source cusp search)

Assume the inherited Stage307/316 two-source reduction `P=b(x,y)+b(x',y')`, the global per-source minimum `beta*=min b`, and the inherited Stage328 algebraic cusp budget bound `E<=epsilon†<23/10000`. Independently, direct exact evaluation at `q=(231/1000,5/9)` gives

`b(q)=2768189461/729000000000 < 19/5000`,

so `beta*<19/5000`. Every feasible pair with `P<=2 beta*+E` satisfies individually

`b_i <= beta*+E < 19/5000+23/10000=61/10000`.

Therefore the **complete** two-source constrained search through that inherited cusp may use the Theorem-B sign table for each group. It has only two open tagged sign regions per group, plus the exact y† boundary; no other source-tagged sign sector is feasible. This is a reduction of the needed full eight-parameter analysis, **not** a proof that Stage329's restricted candidate is globally optimal or that the full Pareto frontier switches at epsilon†. The numerical bound in this corollary relies on the explicitly stated inherited author proof of the cusp and minimum; the standalone Theorems A/B do not.

## Reproduction, limitations and next research question

Run `python REPRO_STAGE332B.py`. The Python standard-library verifier uses exact unbounded integers and `fractions.Fraction`, prints the 127-leaf cover summary, the tag-sign table, rational root isolation and a feasible cusp segment, then terminates with:

`STAGE332B_15_FIXED_TAGS_AND_ONE_EXACT_CUSP_GLOBAL_PASS`.

It was executed twice locally with byte-identical stdout; see `REPRO_STAGE332B_EXECUTED_STDOUT.txt`. No numeric floating-point sampling is used for the theorem. The 16-comparison sign logic is exact factorization; the independently run certificate is algorithmically reproducible from the fully included source and leaf manifest. Mathematical acceptance and task/owner authorization have not been granted.

**Stage333-B:** With the complete tagged-sign table now fixed, exhaust the six remaining public `r0,r1,r3` chambers from Stage331 and their zero boundaries under `b<=61/10000`; then derive exact KKT/corner inequalities to eliminate an off-branch global competitor or exhibit an earlier strict two-source rational competitor in `1/5000<E<=epsilon†`. Preserve sign-boundary strata, source and public word multiplicities, and all inherited theorem dependencies. Native P000 interpretation remains separately pending.
