# R5 — sharp minimum mass escaping the four-chart 16-edge atlas

Date: 2026-11-09 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / INDEPENDENT_REVIEW_PENDING / NOT_ADMITTED.

## Scientific sources and frozen scope

Continue the seven-node R5 P/Q-BRC Blackwell problem from Draft PR #1853, immutable scientific predecessor `6476f66178febab8cc1f5cd25aa763605c46f62f`, especially `research_notes/brc_r5_four_chart_quadrilateral_20261109_r5_1141/{RESEARCH.md,VERIFY.py}`. The predecessor records task scientific pins GLOBAL `a01383f825ef9d43b4b754254303298c64041568`, EM `86149263e38c22292c9def1e0f69092efa1be77e`; these are not rebased. Behavior uses current normative rules. Source observables are not native X6 spatial coordinates.

Likelihood ratios are `r=(1/10,1/2,3/4,1,5/4,3/2,19/10)`. Let `nu_j=M_j(x)` be source masses and `mu_i=M_i(y)` target masses. A Blackwell coupling `E_ij >= 0` obeys:

- `sum_j E_ij = mu_i` for all seven target rows;
- `sum_i E_ij = nu_j` for all seven source columns;
- `sum_i r_i E_ij = r_j nu_j` for all seven source columns.

Here the source physical face has `g=b`, hence `nu_4=0`. The two extremal source columns 0 and 6 must use only their diagonal edges (their conditional mean is an extremal LR node). Define `S=SA union SB`, the 16-edge union from PR #1853:

```text
SA=(0,0),(6,6),(0,1),(2,1),(0,2),(2,2),(3,2),(5,2),
   (3,3),(1,5),(2,5),(4,5),(5,5),(6,5)
SB=(0,0),(6,6),(0,1),(2,1),(0,2),(2,2),(3,2),(3,3),
   (0,5),(1,5),(3,5),(4,5),(5,5),(6,5)
```

For an unrestricted coupling, define its **S-escape mass** `eps_S(E)=sum_(i,j notin S) E_ij`. This measures exactly how much positive mass the restricted S atlas necessarily discards; it is a typed positive-mass/provenance observer, not a signed amplitude.

## Theorem — exact dual obstruction and sharp witness

For **any** seven-node nonnegative coupling of the above type with `nu_4=0`, including arbitrary admissible marginals `nu,mu` sharing the stated LR, the following universal lower bound holds:

```
eps_S(E) >= L(nu,mu)
L=(28/5)(nu_0-mu_0) + 4 nu_1 + 3 nu_2 + (51/23) nu_3
  -(84/23) mu_1 - 3 mu_2 - (51/23) mu_3 .
```

In particular, take the lawful physical source and seedless-F target:

```text
x=(999/1000,1/6,999/1000,1/20,29/240,11/160,1/120)
y=(1,2002911/10904720,26095487/40892700,
   442758619/6542832000,11037627/68154500,
   394502727/2180944000,2002911/109047200)
```

Both yield `T_P=17609/6000` and `T_Q=33857/12000`. For these specific marginals the **exact globally minimal escape mass** among *all* nonnegative 49-edge seven-node Blackwell couplings is

```
min_E eps_S(E) = 225713944957/3385915560000
                = 0.06666260305587794... .
```

This sharp lower bound is strictly stronger than the predecessor's simple row-3 deficit bound:

```
nu_3-mu_3 = 8294919533/147213720000
min_E eps_S(E) - (nu_3-mu_3) = 646866587/62702140000 > 0.
```

### Proof: an explicit dual certificate

Index the 21 equality constraints as `0..6` (target rows), `7..13` (source columns), and `14..20` (source LR moments). Choose dual coefficients:

```text
z_0=-28/5, z_1=-84/23, z_2=-3, z_3=-51/23,
z_7=28/5, z_8=6, z_9=6, z_10=163/23,
z_15=-4, z_16=-4, z_17=-112/23,
all other z_k=0.
```

For every potentially populated edge (i,j) (the 30 edges with j in {0,1,2,3,5,6}, with j=0,6 restricted to their diagonals), the explicit rational inequality is

```text
z_i + z_(7+j) + r_i z_(14+j) <= 1[(i,j) notin S].
```

These 30 inequalities are checked exactly in `VERIFY.py`, and are also a finite symbolic certificate of dual feasibility. Multiplying by `E_ij >= 0`, summing over edges and using the 21 equality constraints gives `eps_S(E) >= z^T b = L(nu,mu)`. Eliminating the source moment terms produces the displayed closed formula for L. No numerical optimization is needed for this implication.

### Proof: matching exact 13-edge primal certificate

All entries below are strictly positive; all other edges are zero. Edge notation is (target i, source j).

| Edge | Exact rational weight |
|---|---|
| (0,0) | 33553/432000 |
| (0,1) | 3997/368000 |
| (4,1) | 3997/690000 |
| (0,2) | 13091471/3762128400 |
| (2,2) | 8901809/21809440 |
| (4,2) | 170189123/37621284000 |
| (0,3) | 8294919533/677183112000 |
| (3,3) | 4095218743/29442744000 |
| (4,3) | 8294919533/188106420000 |
| (4,5) | 172449787/1363090000 |
| (5,5) | 219439/545236000 |
| (6,5) | 172449787/2180944000 |
| (6,6) | 38053/432000 |

The exact verifier confirms: 13 physical source and 13 physical target capacity slacks; source `g=b`; seedless F identities; two stop times; full P/Q normalized masses; all seven target-row, seven source-column and seven LR-moment equations; all 30 dual edge inequalities; complementary equality at all 13 positive primal edges. The sum of the primal edge weights outside S is exactly `225713944957/3385915560000`, equal to the dual value. Weak duality plus primal attainability proves the asserted **global optimum over all admissible couplings for this fixed pair**.

## Interpretation, remaining work, and reproducibility

The previous four-chart atlas cannot represent this pair at all; the new theorem quantifies its *unavoidable* off-atlas mass rather than only the sign obstruction. The dual functional L is a BRC-style observable of the already declared source/target marginals; it is constant on source observation fibers and provides a reusable certificate for other compatible pairs whenever positive. The sharp transport has 13 positive edges, so this result does not resolve whether some lawful pair requires 15 edges.

The next discriminating unit is to find a **new source-3-rerouting 14-edge support chart** whose nonnegative affine region overlaps a physically lawful neighborhood of this witness, then combine dual escape constraints with region coverage. Alternatively, search for a genuine 15-required physical pair using the unrestricted coupling support.

Run `python VERIFY.py` (only standard-library `fractions.Fraction`); `EXACT_OUTPUT.txt` records actual execution. The earlier floating LP suggested the candidate but is not part of this proof. Review/admission and any formal Task Owner/CLAIM remain separate.
