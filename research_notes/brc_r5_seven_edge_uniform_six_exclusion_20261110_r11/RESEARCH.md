# R5 | A uniform quantitative gap between the seven-edge sheet and all six-edge Blackwell targets

Date: 2026-11-10 (Asia/Shanghai). Status: author-side exact lemma, locally checked by an independent Fraction/SymPy reconstruction; the composite repository verifier is provided for independent execution and review.

**Frozen scientific inputs (unchanged):** Global Knowledge `a01383f825ef9d43b4b754254303298c64041568`; Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`. Base immutable author certificate: [PR #1976, commit b9d0da58](https://github.com/awdawmip/enterprise-math/blob/b9d0da58b74a18fe45f4b29bb238b70df79b96bc/research_notes/brc_r5_exact_seven_edge_polygon_20261110_t1640/RESEARCH.md). The exact object is the original **seven-likelihood-ratio auxiliary P/Q–BRC Blackwell transport observer**, with 30 allowed positive-mass columns, 21 unabridged equations, and the 15-row rescaled exact linear system. This result is about the transport observer, not a new P000 or physical-time theorem.

## New theorem: a uniform open tube excludes all six-edge solutions

Use the same ordered 15-row rescaling, 30-column matrix `C`, and two-dimensional closed five-vertex lawful seven-edge physical parameter polygon `\mathcal P_7` from PR #1976. Its support is
```text
S7 = [(0,0),(3,3),(4,3),(4,5),(6,5),(6,6),(0,3)]
F6 = [(0,0),(3,3),(4,3),(4,5),(6,5),(6,6)]
```
For each point `z` in the entire polygon, write `q(z)` for the **rescaled 15-coordinate right-hand-side** and `N_min(q)` for the minimum number of strictly positive entries among nonnegative solutions `C e=q` (provided a solution exists).

Define the *exact positive rational constant*
```text
r_q = 2502770274125/3676504873334904
    = 0.0006807471662222423... .
```
**Theorem A.** For **every** `z in \mathcal P_7` and every `q' in Q^{15}` or `R^{15}` with `||q'-q(z)||_infinity < r_q`, every nonnegative coupling solving `C e=q'` uses **at least seven** positive edges. In particular the same ball cannot contain a feasible right-hand side with minimum support at most six. At its center `q(z)`, the exact minimum is seven (the antecedent certificate supplies the seven-edge positive coupling).

The result is uniform across the complete **closed** five-vertex sheet, including its capacity-boundary vertices. It excludes all 6-edge supports in the full **30-column** model, not only subsets of the displayed seven edges.

**Theorem B (physical parameter version).** With exactly the frozen eight-dimensional auxiliary parameter map `q(z)=q_0+Tz` from the prior verifier, exact rational reconstruction gives
```text
||T||_(infinity -> infinity) = 405/2,
r_z = r_q / (405/2) = 500554054825/148898447370063612
    = 0.000003361714401097493... .
```
For every `z in \mathcal P_7`, any physically lawful parameter `z'` satisfying `||z'-z||_infinity < r_z` has **no** Blackwell transport with at most six positive edges. If `z'` admits a transport, its minimum is at least seven. This does not impose a new physical-feasibility assertion off the sheet; the original physical constraints and coupling existence govern admissibility.

These radii are **certified sufficient bounds from the displayed seven functionals**, not a determination of the true nearest six-edge stratum. They provide a rigorous exclusion neighborhood for subsequent support-switch search.

## Complete finite linear proof

PR #1976 provides six exact dual columns `y_f in Q^{15}`, one for each `f in F6`, satisfying simultaneously, for every one of the 30 permitted columns `C_e`,
```text
y_f^T C_e <= 1 if e=f, and <= 0 otherwise.
```
Every nonnegative solution therefore satisfies `e_f >= y_f^T q'`. The predecessor's **exact five-vertex enumeration** yields the following six strictly positive *uniform* minima `beta_f = min_{z in P7} y_f^T q(z)`:

| Forced edge | beta_f | ||y_f||_1 |
|---|---|---|
| (0,0) | 570031933801575355927/3025154085489542635200 | 1 |
| (3,3) | 9386098186912477/52340117054042400 | 212/5 |
| (4,3) | 5506094603075/179341701138288 | 451/10 |
| (4,5) | 95758167010/1245428480127 | 119/5 |
| (6,5) | 239395417525/4981713920508 | 297/13 |
| (6,6) | 16939155808730941927/3025154085489542635200 | 142/25 |

The new simple annihilator (coordinates indexed **0..14** in the rescaled 15-row system) is
```text
ell[3] = -5/23,  ell[10] = 25/23, ell[14] = -1/23,
all other ell[i] = 0.
```
Direct multiplication against the 30-column construction verifies
`ell^T C_f=0` for every `f in F6`, and `ell^T C_(0,3)=1`; thus `||ell||_1=31/23`. Since every sheet point is exactly represented on `S7`, its seventh-edge weight equals `ell^T q(z)`. Its exact uniform minimum from PR #1976 is
```text
beta_7 = min_{z in P7} ell^T q(z)
       = 1196977087625/89670850569144 > 0.
```

For any vector `d`, the elementary `L1-Linfinity` inequality gives `|v^T d| <= ||v||_1 ||d||_infinity`. Hence, when `||q'-q(z)||_infinity < r`, each dual still forces its named edge and `ell^T q' > 0`, provided
```text
r <= min( min_(f in F6) [beta_f/||y_f||_1],
          beta_7/||ell||_1).
```
Exact rational comparison yields
```text
min (...) = beta_(4,3)/(451/10)
          = 2502770274125/3676504873334904 = r_q.
```
A coupling with at most six positive edges must then use exactly the six forced edges, which would give `ell^T q'=0`; this contradicts its strict positivity. Theorem A follows without a 6-support enumeration. Theorem B follows from the exact row-wise `L1` norm of `T`.

A closed-ball variant uses `||q'-q(z)||_infinity <= r_q/2 = 2502770274125/7353009746669808`. The choice of **strict** inequality for the larger open bound is mathematically intentional.

## Execution scope and follow-up

`VERIFY_TUBE.py` is a compositional executable checker atop the **immutable predecessor** `../brc_r5_exact_seven_edge_polygon_20261110_t1640/VERIFY_7.py` in this stacked research branch. It first redoes the preceding exact seven-edge/polygon certificate, then verifies every new dual inequality over 30 columns, the explicit annihilator, all seven vertex-derived minima, the rational radius, and the exact 8D parameter Jacobian norm. No approximation controls any assertion.

The separately archived `EXACT_OUTPUT.txt` records an actually executed independent self-contained reconstruction of these same new identities using Python Fraction/SymPy. It does **not** claim a byte-for-byte local execution of the published stacked composite verifier. The five-vertex/minimum data are source-backed from the immutable predecessor, reused rather than represented as freshly independently discovered.

**Next precise research unit:** compare the physical six-edge diagonal family already constructed in PR #1945 with the present bounded seven-edge polygon. Parameterize one lawful interpolation or facet-crossing path and solve its exact support feasibility at its first six-edge contact. Theorem B supplies an explicit initial exclusion radius for that search. Preserve the frozen source pins; do not turn auxiliary 8D parameter ranks into native X6 dimension claims.

Admission: author-side proof/computation awaiting independent scientific review. Source publication and activity/ownership are separate.
