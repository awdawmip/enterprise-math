# R5 Addendum: exact 10-edge minimum and a lawful four-dimensional stratum

Date: 2026-11-10 (Asia/Shanghai). This is an author-side exact rational continuation of the **same frozen seven-likelihood-ratio P/Q–BRC model** and the eleven-edge result in sibling `RESEARCH.md`. The unchanged frozen scientific refs are GLOBAL `a01383f825ef9d43b4b754254303298c64041568` and EM `86149263e38c22292c9def1e0f69092efa1be77e`. Auxiliary parameter dimensions are not native X6 space dimensions.

## Theorem and precise contact

Take the explicitly certified 11-edge point `z11`, reduced 15x11 matrix `M11`, rational weight vector `w11>0`, and five exact basis columns `K11` of the physical eleven-edge parameter tangent space, all recomputed by sibling `VERIFY_11.py`.

Define the rational direction and step

```
direction = K11 * (-2,-2,-2,0,0)^T
h10 = 51197529884140057879542511669 / 307731914425719590471261520000000
z10 = z11 + h10 * direction.
```

At `z10`, the weight on `(5,5)` equals **exactly zero** and all ten other weights from `E11` are strictly positive. The strictly positive support is

```
E10=((0,0),(0,1),(2,2),(3,3),(4,3),(4,5),(6,5),(6,6),(2,1),(0,3)).
```

Exact verification reconstructs the original 14 physical parameters and checks all five equalities and all 26 nonnegative physical slacks: the zero slack indices are exactly `4,15,19,21,23` and the other 21 slacks are strictly positive. The original full 21-row Blackwell marginal/martingale equations are exact identities with the ten positive rational weights. Minimum positive margins are:

```
min_positive_edge_mass = 33717770209402615130756220624716236253 / 2324821376870878801488859800784670400000
min_positive_physical_slack = 2725276955204202909732432347 / 19233244651607474404453845000000
```

## Exact full-model lower bound of ten

Eight rational dual vectors `y_e`, attached to the eight forced edges `F8=F9\{(5,5)}` in `VERIFY_10.py`, are checked against **each of the full model's 30 allowed columns**:

```
C^T y_e <= indicator(e),        y_e^T q(z10) > 0.
```

Thus every feasible nonnegative coupling must use these eight edges. Their smallest exact positive forcing margin is

```
1034637395827869340694484123585660191 / 36127760324333780908917790221984000000.
```

If a solution had at most nine positive arcs, it could add at most one arc to the eight mandatory arcs. Quotienting by these eight forced columns gives a 7-dimensional quotient; a **complete exact rank test of all remaining 22 singleton support candidates** yields

```
rank([V_i | qbar]) > rank(V_i)   for every one of the 22 candidates.
```

This excludes every <=9 arc coupling. Combined with the explicit positive ten-arc solution:

```
N_min(z10) = 10.
```

## Four-dimensional local minimal-ten sheet

The reduced 15-by-10 column matrix `M10` has rank 10; its left annihilator has five rows, but after pullback to the eight physical parameters `N10*T` has exact rank **four**. Hence the affine locus on which this *specific* ten-edge support continues to solve all constraints has dimension **four**. The ten positive weights, 21 nonstructural physical slacks, and eight full-model dual lower bounds remain strictly positive in a relative-open neighborhood on this affine four-plane. All 22 smaller support spans fail by a strict linear-algebra rank exclusion at `z10`, so finite closed-subspace separation preserves the minimum-ten result locally. This establishes a **nonempty relative-open four-dimensional lawful stratum of exact minimum 10**. The statement concerns the continuation of this certified support and does not claim this is the only ten-edge locus globally.

## Actual reproducibility, limitations and next action

`VERIFY_10.py` imports sibling **byte-verified** `VERIFY_11.py`, reconstructs the exact rational point, checks the full 21 original equations, five physical equalities and 26 slacks, all eight duals against 30 columns, all 22 singleton rank exclusions and the dimension-four pullback rank. The accompanying `EXACT_OUTPUT_10.txt` records the actual stdout of this exact script, executed locally with Python/SymPy; no tolerance or floating-point optimization is needed in the certificate.

The next discriminating step is to search the ten-edge sheet for a further lawful boundary and test minimum nine or below with exact, current forced duals and complete finite support exclusions; global minimum claims follow only their exact different source scopes (e.g. PR #1945). Formal task CLAIM, Result, independent mathematical review and canonical admission are separately pending. 
