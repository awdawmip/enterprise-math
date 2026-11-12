# PREFIX-733-R6 — Adaptive exact Gamma witness tiles on a 28×28 whole-grid block

Date: 2026-11-12, Asia/Shanghai.
Mother objective: PREFIX-675, global maximum exclusion for the auxiliary independent Gamma completion-clock model.
Frozen science: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Uses unchanged PREFIX-731 exact 189-layer BRC stopped-count/Gamma moment kernel and PREFIX-732 deduplicated baseline.
Status: AUTHOR_EXACT_INTEGER_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED. No native X6 dynamics or global optimum is claimed.

## Theorem — continuous exclusion for every real q ≥ 2

For every real q ≥ 2 and every p,z in [30/384,58/384], the comparator e=(0,73/500) strictly improves the frozen objective

V_q(p,z)=q² Var(max(T_p,T_z))−q E[max(T_p,T_z)].

Hence none of the 784 complete 384×384 fine cells in [30,58)² contains a global maximizer of this frozen auxiliary function.

## Proof and exact finite certificate

Set μ(p,z)=E[Y], M₂(p,z)=E[Y²], W=M₂−μ² and t=1/q in (0,1/2]. From the frozen normalized Bernstein survivor rows' exact symmetry and unimodality (checked by the predecessor kernel), μ and M₂ are coordinatewise nondecreasing on this rectangle, and μ≥0.

For any microrectangle R=[a,b]×[c,d], set l=μ(a,c), U=M₂(b,d)−l² and fixed μ_e,W_e at e. Monotonicity gives μ(p,z)≥l and W(p,z)≤U throughout R. Therefore

V_q(e)−V_q(p,z) ≥ q² [W_e−U−t(μ_e−l)].

The right side is affine in t∈[0,1/2], so it is strictly positive for all q≥2 if both exact endpoint gaps satisfy

g0 = W_e−U > 0;
ghalf = W_e−U−(μ_e−l)/2 > 0.

This proves exclusion of the entire continuous rectangle rather than sampled coordinates.

Partition [30/384,58/384] into 42 intervals of length exactly 1/576, producing 1764 microrectangles. Γ moments are symmetric in p,z, so there are 903 unordered representative tiles. An independent local Python integer/Fraction execution rebuilt the 189 BRC surviving rows (9529 nonzero entries), checked the four established exact-moment numerator hashes and both endpoint gaps. It found 816 base representatives positive and 87 base representatives with inconclusive coarse envelopes. Each inconclusive rectangle was quartered in both coordinates; all 348 resulting leaves have both strictly positive rational gaps. There were exactly 1164 positive leaf tests, maximum split depth 1, and minimum floored positive gap 0 (strict positivity tested as exact rational, not rounded). Symmetry supplies every other microrectangle. Inconclusive coarse bounds are not actual counterexamples.

Run from research_notes/portable_direct: python PREFIX733_R6_ADAPTIVE_GAMMA_28X28.py. The author independently executed the 189-row kernel and the old-base exact overlap calculation. The combined published modular reproducer was syntax-tested but has not yet received a separate complete post-publication rerun; this is an outstanding verification, not an alleged independent review.

## Exact set union

Prior PREFIX-732 certified total: 139140 of 147456 fine cells. The new 28×28 block contains 784 cells, of which the previous [38,50)² contributes 144. In the remaining 640 cells, exactly 136 already satisfy PREFIX-712 old comparator e0=(0,3/20) all-q exact fine-cell conditions. The previous explicit sets from PREFIX-713 coupled (90), PREFIX-713 multicomp (20), PREFIX-716 (1590), and PREFIX-718 (150) have zero overlap with the entire new block; verified using current source JSON. The earlier [40,48)² additions are inside the 144 inner cells.

The new genuinely disjoint count is 640−136=504, and the cumulative certified union becomes

139140+504=139644 out of 147456 = 3879/4096 = 94.7021484375%.

The remaining 7812 cells are not yet *certified excluded*, which does not imply that a maximum exists there. Exact checker code deterministically produces all 504 coordinate pairs, and the deposited summary records the tested counts and model/proof scope.

## Reproducibility and next question

All decisions use integer arithmetic and Python Fraction, with no floating threshold. Mathematical input remains frozen at the original source pin; current behavioral rules do not change the model. This auxiliary Gamma observer is not a complete native X6 three-dimensional slice or rotation-dynamics theorem.

Next: test wider adaptive/comparator-switching tile configurations beyond [30,58)²; seek independent reviewer scrutiny and full combined reproducer rerun before promotion. Preserve any prior active Task owner; this is a task-unbound author research artifact, not a CLAIM or Result.
