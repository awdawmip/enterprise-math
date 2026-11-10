# R5 — Exact three-circuit edge ray in the fixed lawful transport polytope

Date: 2026-11-11 (Asia/Shanghai). Author-side exact rational result; checker executed locally; independent review pending. Companion to RESEARCH.md in this Draft PR.

## Frontier and question

PR #2032 proved that the **18 rays at one specified 14-arc vertex** of the fixed P/Q–BRC Blackwell fiber have minimum K_{2,3} word length 1 or 2. The present calculation asks whether an actual edge ray at another vertex of that *same* fixed physically lawful fiber can require three or more six-arc circuits.

**Theorem.** One of the 15-arc vertices directly adjacent to the pinned 14-arc vertex of PR #2026 has an incident edge ray d with

$$\boxed{\left|\operatorname{supp}(d)\right|=14,\qquad L_{K_{2,3}}(d)=3.}$$

Its target neighbor also has 15 positive arcs. Both belong to the same source/target and 21-observer fiber as PR #2017. This is a concrete edge-adjacent example at graph distance 1 from the 14-arc anchor, not only a generic interior-kernel residual.

## Exact construction

Use the same original 21-by-30 matrix C with r=(1/10,1/2,3/4,1,5/4,3/2,19/10), 30 allowed arcs, and the 14-support vertex X exactly reconstructed in PR #2026's VERIFY_ADJACENCY.py (whose 14 nonzero masses appear in the companion executable here).

First introduce the two initially missing arcs (1,2) and (4,2) with direction weights (1/2,1/4), solving the original-support masses so that Cd1=0. The first exact nonnegative boundary occurs at

$$t_1=\frac{8057361}{84939610}.$$

The resulting vertex V has 15 positive arcs and rank(C_supp(V))=15.

From V, insert the absent arc (3,5) with direction coefficient 1, uniquely solving its original 15 supported arc coefficients from the observer equations Cd=0. This direction is exactly the following rational vector of 14 nonzero entries:

| Arc (target,source) | d |
|---|---:|
| (0,1) | 1/2 |
| (1,1) | -7/10 |
| (5,1) | 1/5 |
| (1,2) | 7/10 |
| (2,2) | -21/20 |
| (4,2) | 7/20 |
| (2,3) | 21/20 |
| (3,3) | -1 |
| (4,3) | -7/20 |
| (5,3) | -1/5 |
| (6,3) | 1/2 |
| (0,5) | -1/2 |
| (3,5) | 1 |
| (6,5) | -1/2 |

Every other allowed arc coefficient is zero. The exact first nonnegative boundary is

$$t_2=\frac{1113619}{118915454}.$$

Set W=V+t_2 d. The attached executable verifies Cx=CV=CW, all nonnegative entries, rank(C_supp(W))=15, and

$$|\operatorname{supp}(V)\cup\operatorname{supp}(W)|=16,\quad \operatorname{rank}(C_{\operatorname{supp}(V)\cup\operatorname{supp}(W)})=15.$$

The supporting face has dimension 16-15=1, hence V and W are adjacent polytope vertices.

## Exact sparse-circuit certificate and optimality

Use the *ratio-normalized* minimal circuit H(j,k;a,b,c) of PR #2032: at source j it carries (r_b-r_c,r_c-r_a,r_a-r_b) on targets a,b,c, and at source k the negatives of those entries.

Direct coordinate calculation gives

$$\boxed{
d=-\frac12H(1,3;0,1,5)
-\frac75H(2,3;1,2,4)
-\frac59H(3,5;0,3,6).
}$$

The right side equals d at all 30 arc coordinates and every constituent H has zero observer readout.

Because d has **14 nonzero arc coordinates** and the union of supports of any two six-arc circuits has at most 12 coordinates, it cannot be represented by two circuits. The displayed expression uses three. Thus its minimum word length is exactly three.

The original X, its neighbors and their entire positive line segments satisfy the original physical constraints because physical source/target parameters remain fixed and all couplings are nonnegative with the same observer vector. No source parameter or capacity is changed by either pivot.

## Reproducibility and consequence

VERIFY_THREE_CIRCUIT_ADJACENCY.py independently reconstructs C and X from rational constants; solves both pivots in exact SymPy rational arithmetic; checks exact equality, vertex rank, face dimension, the 14-support direction, its explicit three-circuit decomposition, and the length-2 lower bound. EXACT_OUTPUT_THREE_CIRCUIT.txt is the actually executed local transcript.

This sharpens PR #2032: the local at-most-two bound for the 18 rays of X already fails at an immediately adjacent vertex in its complete first graph shell. The earlier bound remains correct at its stated anchor.

Next: survey all 19 vertices at graph distance ≤1 (or all 1775 vertices within the proven distance-four ball) and classify maximum word lengths of their incident rays, including whether four circuits are necessary.
