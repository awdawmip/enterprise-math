# PREFIX-739-R6 — 270 additional frozen-Gamma whole-cell exclusions by an exact outer-left certificate

Date: 2026-11-13 Asia/Shanghai. Parent research problem: PREFIX-675. Predecessor: PREFIX-738-R6. Frozen scientific input: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d. This is an independent two-clock Gamma auxiliary observer, not a native X6 spatial/slice claim.

Status: AUTHOR_EXACT_FRACTION_COMPUTATION / EXACT_HISTORICAL_SET_INTERSECTION / UNREVIEWED / NOT_ADMITTED.
Researcher session request: r6-prefix739-researcher-start-20261113-0345-v1 (initially QUEUED); native Researcher-ID and Activity-ID are not inferred from prior runs. Shared CLAIM/Result/Review: not performed.

## Theorem — all real q >= 2, complete continuous cells

Let Y(p,z)=max(T_p,T_z), where the two independent Gamma clocks use the frozen 189-row BRC stopped-count laws; let mu=EY, M2=E(Y²), W=M2−mu², V_q=q²W−q mu. Let e=(0,73/500), D=[0,1/2]² and R_ij=[i/384,(i+1)/384] × [j/384,(j+1)/384].

Define the 159 upper-region integer index pairs by:
- 96 <= j <= 102, 40 <= i < 58;
- j=103, 40 <= i < 55;
- j=104, 40 <= i < 52;
- j=105, 40 <= i < 46.

Every point of each of these 159 closed rectangles, and of each of their 159 distinct transposes, satisfies

    V_q(e) − V_q(p,z) > 91 q² > 0,

simultaneously for all real q >= 2. Consequently all 318 complete cells exclude global optimizers of this auxiliary Gamma model.

## Proof by exact 2×2-cell moment envelopes

The frozen survivor tails s_n(t), n=0,...,188, have 9,529 nonzero integer count positions and s_189=0. Their normalized Bernstein controls are w_(n,k)/C(n,k) in [0,1], symmetric and nondecreasing toward the middle, so s_n and hence both Gamma-max moment functions mu and M2 are coordinatewise nondecreasing on [0,1/2]². This is the already verified PREFIX-731 moment-monotonicity argument; the attached checker reconstructs the actual frozen count kernel.

For any closed subrectangle Q=[a,c]×[b,d], set L=mu(a,b), U=M2(c,d)−L²; define W_e=W(e) and mu_e=mu(e). For t=1/q in (0,1/2],

    [V_q(e)−V_q(x)]/q² = W_e−W(x)−t(mu_e−mu(x))
       >= W_e−U−t(mu_e−L).

The affine lower bound attains its minimum on [0,1/2] at one of the two endpoints, giving the exact rational certificate

    G_e(Q) = min(W_e−U, W_e−U−(mu_e−L)/2).

Each 384-grid cell is partitioned into four closed 768-grid subrectangles. Computing G_e for each subrectangle via exact integer survivor counts and Python Fraction, every one of the 159 cellwise minima is strictly >91. This covers interiors, boundaries and the entire real q-range; transposition follows symmetry of the two independent Gamma clocks.

The following values are exact floors of 10^6 times the certified per-cell rational gap. Every computed value is strictly compared as Fraction, not accepted by decimal rounding. Old-column values refer to the coarser, unrefined 384-cell envelope for witness e0=(0,3/20):

| j | upper cells | min floor(10^6 G_e) | max floor(10^6 G_e0) |
|---|---:|---:|---:|
| 96 | 18 | 91559557 | -20011808 |
| 97 | 18 | 96255680 | -16968178 |
| 98 | 18 | 100935263 | -13806781 |
| 99 | 18 | 105590543 | -10535419 |
| 100 | 18 | 110215106 | -7161288 |
| 101 | 18 | 114803847 | -3690919 |
| 102 | 18 | 119352903 | -130131 |
| 103 | 15 | 123859584 | -807413 |
| 104 | 12 | 128322290 | -93009 |
| 105 | 6 | 132740416 | -274507 |

The global minimum of new floor values is 91,559,557 at (i,j)=(40,96). Each old-witness unrefined G_e0 is strictly negative. Consequently none of these cells was accepted by the exact original PREFIX-712 fine-cell endpoint criterion; their containing 192-grid parent also cannot satisfy the same criterion, because expanding a rectangle cannot increase its valid endpoint envelope.

## Exact historical cell-set overlap

A fresh connector read of the original immutable frozen-science JSON sources and exact reflected-coordinate comparison gave:
- PREFIX-713 coupled (90 fine cells): zero intersection;
- PREFIX-713 multicompetitor: two intersections, (49,101) and (101,49);
- PREFIX-716: 46 intersections, 23 upper cells and their transposes;
- PREFIX-718: zero intersection.

The 23 upper PREFIX-716 intersections are (46,99); (46,100),(47,100); (46,101),(47,101),(48,101); (46,102),(47,102),(48,102),(49,102),(50,102); (46,103),(47,103),(48,103),(49,103),(50,103),(51,103); (46,104),(47,104),(48,104),(49,104),(50,104),(51,104). They do not overlap the PREFIX-713 multicompetitor upper intersection (49,101).

Existing PREFIX-733-A/B, PREFIX-735/736 and PREFIX-737/738 index rectangles do not intersect this outer-left index region. PREFIX-729/730/731 central exclusion is already accounted for in the inherited PREFIX-738 union, and the exact PREFIX-712 nonintersection is established above. Thus relative to the existing author-level PREFIX-738 union, the present 318 newly certified cells have 48 already-certified intersections, yielding precisely

    318−(2+46)=270 genuinely additional complete cells,
    141204+270=141474 out of 147456,
    141474/147456=23579/24576=95.9431966145833...%,
    147456−141474=5982 not-yet-certified fine cells.

This is a certified-*coverage* remainder and is not a statement about existence of global optimizers in those cells.

## Reproduction and evidence boundary

The author reconstructed the frozen 189-row integer predicate, confirmed the count 9,529 and row 189 empty, and carried out 159 exact Fraction four-piece comparisons in ten bounded row batches. The source checker repeats this rational work, verifies the displayed row min/max regression values, all 318 reflection indices and historical JSON overlaps. The four historical JSON files are: PREFIX713_R6_RESULTS.json (blob 0a12cab85b186cda25df45591e50d7904836f7fa), PREFIX713_R6_MULTICOMPETITOR_RESULTS.json (4945aa30875a70ae047f7d9bef37aed48e1bfb7a), PREFIX716_R6_RESULTS.json (ea2e3df0da8c4713c531339ce735907ee607dac5), PREFIX718_R6_RESULTS.json (af6a51b91e5bd1e3e5a884ad618e0c962c030674). Each matches scientific pin f42f2906d77f24085c123f3ccfe9667d41caa96d.

The author-level 159-cell exact calculation and a separate authenticated GitHub-source set intersection have been executed; the newly published combined checker has not itself been rerun end-to-end on the original four historical JSONs in this run. Independent review and formal shared Result admission remain pending. The scientific input pin has not changed.

Next: (1) run the combined checker in an environment with the original four JSON files, (2) use adaptive witnesses/derivative certificates on residual cells outside this strip, (3) independently review the load-bearing moment and overlap assertions before project admission. Preserve this frontier and do not repeat already checked cells absent a changed source.
