# PREFIX-749-R6 — Four additional complete BRC–Gamma cells excluded by exact 8×8 moment envelopes

Date: 2026-11-13 (Asia/Shanghai). Parent science: PREFIX-675. Immediate predecessor: PREFIX-748-R6. Frozen scientific input: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`. Author-side result: `AUTHOR_EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED`.

## Exact proposition

Use the exact 189-layer stopped-survivor BRC integer kernel and the two independent rate-one Gamma clocks of the frozen auxiliary model. Let `Y(p,z)=max(T_p,T_z)`, `mu(p,z)=E[Y(p,z)]`, `M2(p,z)=E[Y(p,z)^2]`, `W=M2-mu^2`, and `V_q(p,z)=q^2 W(p,z)-q mu(p,z)`. Retain the already-established competitor `e=(0,73/500)`. Define closed cells `R_ij=[i/384,(i+1)/384]x[j/384,(j+1)/384]`.

**Theorem (frozen auxiliary model).** For every real `q>=2`, every `(p,z)` in each of `R_(10,50), R_(10,51), R_(50,10), R_(51,10)` satisfies the uniform strict inequality

`V_q(e)-V_q(p,z)>3q^2>0`.

In particular these four full, closed, continuous parameter cells are excluded from maximizers of this precise auxiliary objective.

## Exact enclosure proof

The original integer survivor coefficients are nonnegative, symmetric in the two Bernoulli outcomes, and center-nondecreasing in their normalized Bernstein bases; these assertions are directly checked by the supplied frozen kernel (189 rows 0..189, empty row 189, 9,529 nonzero coefficient positions). Hence the Gamma survival tails are coordinatewise nondecreasing on `[0,1/2]^2`; integrating their positive linear kernels gives coordinatewise nondecreasing `mu` and `M2`. All stated cells are within this domain.

For an arbitrary rational closed subrectangle `Q=[a,c]x[b,d]` put `L=mu(a,b)>=0`, `H=M2(c,d)`. For each point in Q, `mu>=L`, `M2<=H`. With `t=1/q in (0,1/2]`, the normalized gap obeys

`(V_q(e)-V_q(p,z))/q^2 = W(e)-M2(p,z)+mu(p,z)^2-t(mu(e)-mu(p,z)) >= W(e)-H+L^2-t(mu(e)-L)`.

The right side is affine in `t`, so its minimum over the containing closed interval `[0,1/2]` occurs at an endpoint. Let

`B(Q)=min(W(e)-H+L^2, W(e)-H+L^2-(mu(e)-L)/2)`.

Split every R_ij into 8x8 equal rational closed subrectangles; `G_8(i,j)=min_Q B(Q)` is an exact rational lower bound valid for every parameter point in the entire closed cell and every real q>=2. Clock exchangeability gives `G_8(i,j)=G_8(j,i)`.

All moments are evaluated with integer Gamma survival sums and `fractions.Fraction`, with no floating-point input or error estimate. For each original cell, the independently executed local kernel returned these exact millionth-floor certificates:

| Cell | floor(10^6 G_2) | floor(10^6 G_4) | floor(10^6 G_8) | floor(10^6 old G_1) |
|---|---:|---:|---:|---:|
| (10,50) | -78,645,845 | -20,639,281 | **8,455,657** | -194,688,514 |
| (10,51) | -84,950,051 | -25,907,227 | **3,704,401** | -203,076,218 |

The minimum floor of the two G_8 values is `3,704,401>3,000,000`. Thus the *unrounded* exact rational G_8 in each original cell is strictly greater than 3. Transposition completes all four cells. The negative coarser and older values are inconclusive lower bounds, not counterexamples.

For provenance, the original kernel's `mu(e).numerator` SHA256 is `797121e567e6422d342b2647cd17ff01187d5000b08bde8a954730d071bed46e`, and `W(e).numerator` SHA256 is `814be93bb068b6a6e688e8ea5a466939a06e617b67ab585c177176f57afd57ae`. An independent equivalent standard-library Python implementation rebuilt all 190 rows and checked the nonzero count, Bernstein symmetry/center inequalities, moment hashes and all table entries. Each original cell's 2/4/8 calculation was repeated in its own process. This is **author exact recalculation**; an independent clean reviewer remains separate; the exact published-checker plus exact original dependency replay has now been completed, as recorded below.

## Historical-coordinate comparison and cumulative scope

The prior PREFIX-748 author-level union reported 141,980 of 147,456 full 384x384 parameter cells. Direct connector-read checks of the exact PREFIX-742..748 coordinate outputs show neither (10,50) nor (10,51) nor their transposes in those additions. The PREFIX-713 multi-competitor, PREFIX-716 and PREFIX-718 768-denominator results were checked with the necessary coordinate conversion: each new 384-grid cell (i,j) consists of four (2i+di,2j+dj), di,dj in {0,1}, on the 768-grid. None of the eight converted upper-cell children occurs in the checked extra representatives, and the 713 parent exceptions are outside these coordinates. The original PREFIX-712 single competitor's 1x1 sufficient lower bounds were also recalculated, giving the negative values in the last table column. Earlier PREFIX-729..741 regions are spatially separate as documented in their scoped notes.

Subject to the inherited author-level union (whose complete independent all-history audit remains open), the new pair plus its two transposes adds four distinct full cells:

`141980+4=141984`, `141984/147456=493/512=96.2890625%`; remaining `5472` full cells outside this author certificate union.

This is an exact auxiliary Gamma objective exclusion, not a change to P000, a proof about the original stopping-count objective, or a formal Result/Review acceptance.

## Reproducibility, artifacts and next question

Companion checker: `PREFIX749_R6_GAMMA_NEIGHBORS_4.py`; data: `PREFIX749_R6_GAMMA_NEIGHBORS_4_RESULTS.json`. Run checker next to source `PREFIX741_R6_INNER_STRIP_194.py`, whose previously read Git blob SHA1 is `d986f644ba513240ea8395e0b221af7946e0efd6`. The checker computes the 2/4/8 exact bounds and old point's 1x1 bounds afresh; it explicitly checks the complete expected floors. The exact published checker and original dependency were both replayed on 2026-11-13, as recorded below.

Next evaluate neighboring (11,52), (10,52), and farther boundary cells with exact adaptive subdivisions, and independently audit the full historical certificate union at a single coordinate scale. The isolated (11,52) 8x8 local test did not finish during this run; it contributes no claimed certification. For formal shared research, obtain a fresh exact Task/CLAIM binding separately; this independent note preserves science without appropriating another live owner.

## Post-publication exact-byte composite replay (2026-11-13)

Reconstructed both exact original GitHub bytes in one local Python standard-library environment and verified their Git blob SHA1 values before execution:

- `PREFIX741_R6_INNER_STRIP_194.py`: `d986f644ba513240ea8395e0b221af7946e0efd6` (original imported dependency).
- `PREFIX749_R6_GAMMA_NEIGHBORS_4.py`: `76bb0162a679275631a18cc0098cd3affdf4e568` (new checker committed on main).

Invoked `python PREFIX749_R6_GAMMA_NEIGHBORS_4.py` in the same directory; its parent process spawned one child Python process for each original cell, and all exact arithmetic assertions succeeded:

```text
PASS 10 50 (-78645845, -20639281, 8455657) old -194688514
PASS 10 51 (-84950051, -25907227, 3704401) old -203076218
ALL_CHECKS_PASS PREFIX749-R6 2+2=4
```

This completes the previously open **published-source exact dependency composite replay** item. Independent mathematical review and comprehensive historical certificate-union audit remain open; neither activity checkpoint nor a passing local checker grants formal acceptance.
