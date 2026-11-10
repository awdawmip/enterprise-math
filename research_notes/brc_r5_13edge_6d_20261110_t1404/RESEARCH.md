# R5: first exact lawful 13-edge transport and a six-dimensional minimum-support sheet

Date: 2026-11-10 (Asia/Shanghai). Scientific result type: **author-side exact rational proof with computationally exhaustive finite certificate**. This is independent research-note evidence, not an admitted Source Result or an independent referee report.

## Inputs and unchanged provenance

Continue exact frozen P/Q–BRC seven-likelihood-ratio Blackwell model from Draft PR #1954, head `6f01b6424cc5563db7976fa8131ef687c15091ca`. Retain scientific source pins GLOBAL `a01383f825ef9d43b4b754254303298c64041568` and Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`. The exact physical source/target model, 14 physical parameters, five physical equalities, 26 capacity slacks, 30 allowed transport arcs, 21 full marginal/Martingale equations, eight-dimensional parameterization `p(z)=p0+P*(tstar+z)`, and 15-row reduction are inherited without adjustment from `research_notes/brc_r5_two_facet_20261110_t1140/VERIFY.py` (PR #1950 at `c8a0ade3904507cf4dda38bfa888bdb490b1ea87`).

P000 remains locked. The seven likelihood-ratio labels in this auxiliary statistical experiment are **not** six native spatial X6 directions. Positive transport arc masses and their identities remain intact in the full 21-row check; quotient projections are used only for the exact, scoped support-exclusion argument.

## Theorem 1: a lawful rational physical point with exactly 13 required arcs

Write

```
R = 49948501046391 / 3920403670319950000
z_c = R * (-1,1,1,-1,-1,-1,-1,1)
n = (34101,-293725,-85599,42525,937899,293725,85599,-3287440)
mu0 = 16932541854726549 / 313632293625596000000
alpha = (4*3287440/(13*293725)) * mu0
      = 53523764802790621389 / 287880142016181828437500
z_13 = z_c - alpha*e5 - (293725/3287440)*alpha*e7
```

Here `e5,e7` are coordinate unit vectors with **zero-based indices** 5 and 7 within the eight auxiliary physical parameters, not P000 axes.

The exact rational point `z_13` satisfies both independent affine constraints

```
n dot (z_13-z_c) = 0,
mu_1(z_13) = 0,
rank([n; grad(mu_1)]) = 2.
```

It obeys the complete original five physical equalities and all 26 capacity nonnegativity constraints. Among the 26 physical slacks only indices `4,15,19,23` vanish; all other 22 slacks are strictly positive. Their minimum is

```
2109638658902162346909 / 10887103552611967330000000 > 0.
```

An exact nonnegative Blackwell coupling at this same point uses **exactly the following 13 edges**, all with strictly positive rational mass:

```
F = ((0,0),(0,1),(0,2),(2,2),(3,3),
     (4,3),(4,5),(5,5),(6,5),(6,6))
S3 = ((2,1),(3,2),(0,3))
support = F+S3
```

All 21 marginal/Martingale equations hold as exact identities. Its minimum positive mass is

```
33298090355215327 / 81544396342654960000 > 0.
```

In the earlier fourteen-edge basis `F+S3+((1,5),)`, the last weight becomes precisely zero. That supplies a concrete thirteen-edge **upper bound** for the exact frozen model.

## Theorem 2: 13 edges are minimal at this point

Let `C` be the rank-15 rational 15-by-30 reduction of the unchanged 21-row Blackwell matrix, and let `q=q(z_13)`. The accompanying `VERIFY_13.py` stores **ten fully explicit rational dual vectors** `y_e`, one for each `e in F`, and checks for every one of the 30 columns that

```
C^T y_e <= indicator_vector_for_edge_e
and
y_e^T q > 0 .
```

For any nonnegative transport `x` with `Cx=q`, these inequalities imply

```
x_e >= y_e^T Cx = y_e^T q > 0 .
```

Thus **every** possible coupling has the same ten forced arcs. All ten certificates are separately checked by exact rational arithmetic at `z_13` (they are not assumed from a previous nearby region).

Any hypothetical coupling with at most twelve positive edges could then use at most two of the twenty remaining arcs. Quotient out the ten forced columns using an explicit 5-by-15 rational left annihilator `L`, and put `V=L*C_other`, `qbar=L*q`. Enumerate the complete finite set

```
binom(20,2)=190
```

of two-extra-edge candidates. The executable checker confirms, for every pair `S`,

```
rank([V_S | qbar]) > rank(V_S).
```

Exactly 187 pairs have rank 2 and three pairs rank 1; all 190 are excluded. This automatically excludes every smaller support by extending its remaining arcs to a two-element subset. Therefore the exact minimum is

```
N_min(z_13) = 13.
```

This is a distinct **model-internal exact counterexample** to any proposed universal 14-edge lower bound and completes the next local case of the earlier 14/15 stratification.

## Theorem 3: a nonempty six-dimensional region of minimal 13-edge transfers

Let `m=grad(mu_1)` in the eight-dimensional auxiliary parameter space and

```
K = ker([n^T; m]) .
```

Exact rank gives `dim K=6`. The thirteen-edge reduced column matrix `M13` has rank 13, and the checker verifies

```
rank([M13 | T*v])=13
```

for each of six exact rational basis vectors `v` of `K`, where `T` is the affine physical-to-statistical right-hand-side derivative. Thus `M13` continues to solve the full constraints along all sufficiently small `K` perturbations. All thirteen basis coefficients and all nonstructural physical slacks are strictly positive at `z_13` and vary affinely. The ten strict dual lower bounds persist by continuity. The finitely many 190 rank-excluded two-extra-edge spans are closed linear subspaces omitting `qbar(z_13)`, so a common sufficiently small neighborhood also excludes all of them.

Consequently, **there exists a nonempty relative-open six-dimensional neighborhood** of `z_13` within

```
n dot (z-z_c)=0,    mu_1(z)=0
```

where **every** point is a lawful original physical strategy pair with `N_min(z)=13`.

This proves the first certified local **13-edge stratum**, adjoining the previously established 7D 14-edge wall and its two 8D 15-edge chambers. It does not assert a complete global classification of every legal parameter.

## Reproduction / finite coverage

Source `VERIFY_13.py` depends on `../brc_r5_two_facet_20261110_t1140/VERIFY.py` and reconstructs all physical and Blackwell equalities from the immutable parent. All proof-critical checks are symbolic/rational; there is no tolerance threshold, numerical floating-point acceptance, or sampling in the 190-pair exhaustion.

`EXACT_OUTPUT.txt` records output from an **actually executed independent local Python/SymPy rational reconstruction using the same exact parent formulas**, not a purported byte-for-byte execution of the published combined checker. Check separately when claiming an exact byte-for-byte run of the published checker. The argument is author-side mathematical evidence with explicit finite certificates; formal project claim, native Result, independent review, and formal proof-assistant acceptance remain separate.

## Next discriminating work

At the proven six-dimensional thirteen-edge sheet, classify which of its boundaries first cause another positive edge to reach zero, and check the compatibility of these boundary facets with all 26 physical capacities. Compute an exact rational local radius for this thirteen-edge stratum. Separately determine whether any 12-edge stratum is physically accessible outside the present neighborhood using exact new witnesses, not only quotient rank.
