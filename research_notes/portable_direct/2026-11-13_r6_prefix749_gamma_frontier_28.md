# PREFIX-749-R6 — 28 new complete Gamma exclusion cells by exact 8×8 refinement

Date: 2026-11-13 (Asia/Shanghai). Parent: PREFIX-675. Prior frontier: PREFIX-748-R6. Frozen scientific input: `awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d`. Researcher-ID: `EM-DIRECT-25162E`; Activity-ID: `RA-43F3FFA920B6BACBAD5770B6`. Scope: independent author-side Gamma auxiliary mathematics, no shared CLAIM or admitted Result.

## Exact proposition

For the frozen 189-layer stopped-survivor BRC count and independent unit-rate Gamma clocks `T_p,T_z`, let `Y=max(T_p,T_z)`, `mu=E[Y]`, `M2=E[Y^2]`, `W=M2-mu^2`, and `V_q=q^2 W-q mu`. For witness `e=(0,73/500)`, define `R_(i,j)=[i/384,(i+1)/384] × [j/384,(j+1)/384]` (closed).

**Theorem (auxiliary model).** For every **real** `q>=2` and every real parameter pair `(p,z)` in each of the 14 cells indexed in the table below or their 14 coordinate transposes,

`V_q(e)-V_q(p,z) > q^2/30 > 0`.

This strictly excludes the 28 complete closed parameter cells from global maximizers of this auxiliary objective.

## Proof kernel

The frozen integer recurrence has 190 rows (0..189), with row 189 empty, and 9,529 nonzero coefficient positions across rows 0..188. Nonnegative symmetric normalized Bernstein coefficients increasing toward their row center give coordinatewise nondecreasing Gamma survivor tails on `[0,1/2]^2`; therefore `mu` and `M2` are coordinatewise nondecreasing there. All listed closed cells lie in this domain.

For any closed rational subrectangle `Q=[a,c]×[b,d]`, write `L=mu(a,b)>=0`, `H=M2(c,d)`. For `t=1/q in (0,1/2]` and `(p,z) in Q`,

`(V_q(e)-V_q(p,z))/q^2 = W(e)-M2(p,z)+mu(p,z)^2-t*(mu(e)-mu(p,z))`

`>= W(e)-H+L^2-t*(mu(e)-L)`.

The right side is affine in `t`; its minimum over `[0,1/2]` is at `0` or `1/2`. Denote that exact rational lower bound by `B(Q)`. Subdivide a full closed cell into `s×s` exact rational subrectangles and put `G_s(i,j)=min_Q B(Q)`. Hence the normalized difference throughout the full cell is at least `G_s(i,j)`. Gamma-clock exchangeability proves the transposed statements. The attached checker evaluates `G_2,G_4,G_8` using exact integer recurrence and Python Fraction arithmetic from the fixed PREFIX-741 dependency.

The smallest exact `G_8` has `floor(10^6 G_8)=36384` (at (11,53)), so **`G_8 >= 36384/1000000 > 1/30`** on every listed cell. Strictness follows without rounding assumptions; the decimal floors are display-only exact integer checks.

## Recalculation table

Values are integer floors of 1,000,000 times the exact rational lower bounds. The last column uses the older `e_old=(0,3/20)` and its original unrefined `G_1` certificate.

| Cell | G2 floor | G4 floor | G8 floor | Old G1 floor |
|---|---:|---:|---:|---:|
| (7,47) | -67306677 | -12668452 | 14749094 | -176559258 |
| (7,48) | -75490081 | -19738993 | 8233883 | -186976616 |
| (8,48) | -71824562 | -16036330 | 11954081 | -183393977 |
| (8,49) | -79372852 | -22496035 | 6037447 | -193128641 |
| (8,50) | -86167146 | -28221013 | 845704 | -202072414 |
| (9,49) | -75599055 | -18687609 | 9862147 | -189432721 |
| (9,50) | -82520043 | -24545578 | 4534353 | -198489866 |
| (10,50) | -78645845 | -20639281 | 8455657 | -194688514 |
| (10,51) | -84950051 | -25907227 | 3704401 | -203076218 |
| (11,52) | -86683906 | -26603110 | 3524919 | -206906474 |
| (11,53) | -91649342 | -30582793 | 36384 | -213856733 |
| (12,53) | -87744789 | -26657420 | 3971215 | -210001739 |
| (12,54) | -92131325 | -30088112 | 1016623 | -216314021 |
| (13,53) | -83619058 | -22507063 | 8132839 | -205933937 |

The negative G2/G4 numbers are inconclusive lower bounds; the strictly positive G8 numbers prove all 14 original cells.

## Prior certificates and union accounting

The original PREFIX-712 old-comparator G1 is strictly negative for every new original cell. Scoped set-intersection reads of `PREFIX713_R6_RESULTS.json`, `PREFIX713_R6_MULTICOMPETITOR_RESULTS.json`, `PREFIX716_R6_RESULTS.json`, `PREFIX718_R6_RESULTS.json`, and explicit prior `PREFIX742` through `PREFIX748` JSONs found no overlapping candidate coordinates (accounting for transposes). Earlier PREFIX729–741 documented coverage rectangles exclude this left-edge frontier. These checks support the following **conditional author-level** update, inheriting the PREFIX-748 baseline pending a complete independent historical-union audit:

`141980+28=142008` of `147456=384^2`; fraction `5917/6144 ≈ 96.3053385416667%`; remaining `5448`.

## Verification and reproducibility

The author-side local independent implementation reconstructed all 190 recurrence rows, asserted the terminal empty row and 9,529 nonzero coefficient positions, Bernstein coefficient symmetry/monotonicity, and matched the exact witness numerator SHA256 digests from PREFIX-741:
- mean numerator `797121e567e6422d342b2647cd17ff01187d5000b08bde8a954730d071bed46e`;
- variance numerator `814be93bb068b6a6e688e8ea5a466939a06e617b67ab585c177176f57afd57ae`.

All 14 original-cell calculations were executed with exact `fractions.Fraction` for `s=2,4,8` and separately for old `s=1`; every expected integer floor assertion passed. An author-side checker using a mathematically equivalent local module proxy passed each cell in a separate process, including old-criterion checks. The newly published compact checker imports the original GitHub `PREFIX741_R6_INNER_STRIP_194.py`; a *fresh exact-byte end-to-end replay of this published source pair* is a follow-up verification, not claimed by this note.

Grade: `AUTHOR_EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED`. The model is a two-coordinate external Gamma auxiliary; no native X6/three-dimensional slice transfer is claimed. A GitHub commit records author evidence, not mathematical admission.

## Current unfinished unit

Attempt 16×16 exact rational refinement of neighboring cells `(9,51),(10,52),(11,54)`, whose 8×8 bounds were inconclusive for tested cases, without regarding negative lower bounds as counterexamples. Separately execute the exact published checker with the exact GitHub dependency and independently audit the entire historical union. Preserve the frozen science pin, Source identity, and current shared-owner boundaries.
