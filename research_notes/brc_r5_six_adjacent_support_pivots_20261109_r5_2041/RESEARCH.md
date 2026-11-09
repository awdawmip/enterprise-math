# R5: six exact adjacent 14-edge Blackwell support pivots beyond the (5,5) boundary

Date: 2026-11-09 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FRACTION_REPRODUCED / INDEPENDENT_REVIEW_PENDING. Mother objective: determine whether every Blackwell-feasible lawful g=b P/Q-BRC physical strategy pair has a transport with at most 14 positive edges, or find a true 15-edge-necessary pair.

## Frozen science and prior input

Reuses the seven likelihood ratios R=(1/10,1/2,3/4,1,5/4,3/2,19/10), FULL_HIST source, seedless F target, g=b, and fixed stopping times. Exact immutable predecessor [R5 four-parameter chart PR #1877](https://github.com/awdawmip/enterprise-math/blob/a402aeedef23843fb0bb618e35e2012ee244aeb2/research_notes/brc_r5_fourparameter_14edge_20261109_t1140/RESEARCH.md); source verifier is imported from that same immutable commit. Earlier frozen scientific pins (not repinned by this continuation): global `a01383f825ef9d43b4b754254303298c64041568`, EM `86149263e38c22292c9def1e0f69092efa1be77e`. Current operating rules are read separately. P000 six native spatial axes and independent time stay unchanged; transport indices are statistical, not native axes.

Physical flow order (g,a,b,u,v,w,z). The immutable predecessor fixes X0, Y, H, rho_star, U1...U4, V1...V4, the 14 edges S and weights E0; all rationals are reproduced in VERIFY.py.

## Theorem: six legal one-edge continuations

Set
```
H = 17774559/17507527960
rho_star = 17774559/225414193300
delta_max = 904888979/2817677416250
P(delta) = (p,q,r,epsilon) = (rho_star+delta,-rho_star-delta,-rho_star-delta,3H/4)
X(delta) = X0 + p U1 + q U2 + r U3 + epsilon U4
E_old(delta) = E0 + p V1 + q V2 + r V3 + epsilon V4
```
For every real 0 <= delta <= delta_max, X(delta) is a lawful FULL_HIST source with g=b, two stopping times identical to Y, and the pair (X(delta),Y) is Blackwell-feasible with <=14 positive edges. For 0<delta<=delta_max it has **six distinct explicit 14-edge support realizations**, each obtained by replacing the old edge (5,5) by exactly one of
```
(6,1), (6,2), (6,3), (0,5), (2,5), (3,5).
```
At delta=0 each realization has exactly 13 positive edges; the new edge's weight is zero. At delta_max, g=b=1 is the physical limiting constraint, while all 14 coupling weights remain strictly positive.

For a particularly simple member choose the new edge e=(3,5). Let A denote the 21-by-14 Blackwell constraint matrix on the old support S in its predecessor's order. The following exact rational column identity is verified:
```
A * alpha = column(3,5)
alpha=(0,5/9,-14/9,1,-5/9,2,-13/9,-2,4,-2,2,-1,0,0).
```
Along this physical ray the old (5,5) weight equals -16537*delta/12960. Define t=16537*delta/12960 and
```
E_new[k] = E_old[k] - t*alpha[k]     for all old k except (5,5);
E_new[(3,5)] = t;
E_new[(5,5)] = 0.
```
The exact column identity proves all 21 mass / likelihood-ratio moment equalities for every real delta. Physical capacity and edge inequalities are affine in delta; the verifier checks both rational endpoints and therefore the entire interval by convexity. At delta=0 the minimum among the 13 positive old weights is 219439/545236000; at delta=delta_max it remains 219439/545236000, while new weight is
```
t(delta_max) = 904888979/2208205800000 > 0.
```
The two stopping times remain (17609/6000,33857/12000); physical slacks are nonnegative throughout and all except g-b and (at the final endpoint) 1-g are strictly positive.

## Exhaustive one-edge pivot classification

Among the 30 allowed Blackwell edges, 16 are outside S. Exact rational elimination on the predecessor's 21-by-14 full-column-rank matrix partitions these 16 candidate new edges into three classes:

* Four outside the 14-column span: (1,1),(1,2),(1,3),(1,5).
* Six in that span with vanishing (5,5) coefficient: (2,1),(4,1),(4,2),(5,2),(0,3),(5,3).
* Six in that span with **negative** (5,5) coefficient: (6,1),(6,2),(6,3),(0,5),(2,5),(3,5). These are exactly the six feasible adjacent single-edge replacements along the specified delta>0 ray.

For each of the six negative-coefficient candidates, use t=E_old(5,5)/alpha_e(5,5)>0 and replace the (5,5) coordinate. The independent Fraction checks certify all 21 equations and positivity at both endpoints for each. Affinity proves nonnegative feasibility on the full real interval and strict positivity for delta>0.

This is a complete classification of single-new-edge replacements **of (5,5) on this specific ray**, not a universal classification of all R5 strategies or all supports.

## BRC / observer interpretation and next unit

The four physical directions have three observable probability directions and one observer-kernel residual as established in the immutable predecessor. This new ray changes marginal probabilities and crosses the old support boundary while retaining the branch-resolved transport carrier. The six support substitutions are distinct exact representatives of the same observed Blackwell marginals; their positive-branch provenance should be retained rather than quotienting to total mass without the stated observer lease.

Next: determine the affine region around each of the six new supports (not just this ray), compute overlap/chamber adjacency and search for lawful feasible pairs requiring 15 edges. Preserve task-owner/CLAIM authorization and review separation.

## Verification provenance

`VERIFY.py` extends the exact immutable predecessor checker with independent rational-column pivot identities, exact endpoint witnesses, a complete 16-candidate row-reduction test, and six sets of endpoint positivity checks. `REPRODUCTION_OUTPUT.txt` records an independently run local Python Fraction reproducer of these same mathematical claims. Finite enumeration proves precisely the stated finite 16-candidate classification; endpoint+affine reasoning supplies the continuum proof. No float or LP tolerance enters the result.

Publication in this research note is only author-side durable evidence. There is no Result, Driver review, Foundation promotion or Task CLAIM by publication alone.
