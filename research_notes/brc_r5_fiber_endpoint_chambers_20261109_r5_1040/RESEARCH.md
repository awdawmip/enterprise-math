# R5 — Exact eleven-chamber decomposition of the lawful g=b observer fibers

Date: 2026-11-09 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / INDEPENDENT_REVIEW_PENDING / NOT_ADMITTED.

## Inputs, provenance, and question

This is a new author-side continuation of [PR #1849](https://github.com/awdawmip/enterprise-math/pull/1849), exact head `81e25545ee3ae6aeeab6c054c3c6bb706191fb95`; its self-contained `research_notes/brc_r5_global_observer_fiber_20261109/VERIFY.py` fixes the 13 affine FULL_HIST capacity slacks and the observer kernel. The scientific input stays pinned to GLOBAL `a01383f825ef9d43b4b754254303298c64041568` and EM `86149263e38c22292c9def1e0f69092efa1be77e`, with present-day behavioral rules read separately. P000 and original task publications are unchanged.

**Question.** On the lawful six-dimensional source face `g=b`, classify *which capacity wall* is met at the lower and upper endpoints of the complete observer fiber `f+hK`. This describes the exact geometry needed for the next A/B 14-edge chart gluing step. It does not claim a new LR transport for every pair.

Let `f=(g,a,b,u,v,w,z)`, `b=g`, and `s_0,...,s_12` be the affine slacks in the predecessor's `VERIFY.py`:

```
0:a                 1:g-a               2:1-g
3:b                 4:g-b               5:u
6:13a/40+b/80-u     7:w                 8:3a/40+21b/80-w
9:z                10:a/10-z           11:v-z
12:z+9b/40-v
```

The exact statistical observer fiber has direction

```
K=(-49400/295513,-49400/295513,-49400/295513,
   -33345/591026,132145/295513,-33345/591026,1).
```

**Important arithmetic detail:** because `s_2(f)=1-g` is affine, its directional derivative is `+49400/295513`, **not** `s_2(K)=1+49400/295513`. All directional derivatives in this result are computed as `D_i=s_i(K)-s_i(0)`; the attached verifier checks this exactly.

## Theorem 1 — exactly eleven full-dimensional strict endpoint chambers

On the relative interior of the lawful `g=b` physical source face, all twelve slacks except the identity `s_4=0` are strictly positive. The derivative vector is

```
D=(-49400/295513,0,49400/295513,-49400/295513,0,
   -33345/591026,0,-33345/591026,0,
   1,-300453/295513,-163368/295513,152253/295513).
```

For any legal source `f`, define `L_i=-s_i/D_i` when `D_i>0` and `U_j=-s_j/D_j` when `D_j<0`. Its complete legal fiber is precisely

```
L(f)=max(L_2,L_9,L_12),
U(f)=min(U_5,U_7,U_10,U_11).
f+hK is lawful iff L(f) <= h <= U(f).
```

The apparent additional upper candidates `U_0,U_3` are **globally dominated by `U_10`** on the source face: `0<=z<=a/10`, `a<=b`, and

```
U_10=(295513/300453)(a/10-z)
    <=295513*a/3004530 < 295513*a/49400=U_0
    <=U_3
```

for interior `a>0`. This reduces the naive six upper candidates to four.

For strict uniqueness of both extremal active facets, there are exactly **eleven nonempty open polyhedral chambers**, labeled by

```
(lower,upper) in
(2,5),(2,7),(2,10),(2,11),
(9,5),(9,7),(9,10),(9,11),
(12,5),(12,7),(12,10).
```

Each is relatively open, convex and full-dimensional (dimension 6) in the `g=b` source face. Every such chamber has an exact rational interior witness in the attached `VERIFY.py`. The one remaining formal pair `(12,11)` is impossible for an interior lawful point.

**Exact incompatibility proof for (12,11).** If `L_12>=L_9`, then

```
v-z >= 9b/40-(152253/295513)z
     >= [9/40-152253/2955130] b
     = (410121/2364104)b.
```

Here `z<=a/10<=b/10`. If also `U_11<=U_10`, then

```
v-z <= (163368/300453)(a/10-z)
     <= (163368/3004530)b = (27228/500755)b.
```

But `410121/2364104 > 27228/500755`, a strict rational inequality, and `b>0` in the relative interior. Hence `(12,11)` cannot occur even weakly there.

**Existence of all other eleven chambers.** The exact witness table below lists six integer numerators with common denominator 2000, in column order `(g,a,u,v,w,z)`; set `b=g`.

| lower | upper | 2000 × (g,a,u,v,w,z) |
|---|---|---|
| 2 | 5 | (1992,1985,8,132,664,53) |
| 2 | 7 | (1992,1985,662,132,8,53) |
| 2 | 10 | (1976,1951,634,197,640,171) |
| 2 | 11 | (1980,1960,642,159,647,139) |
| 9 | 5 | (1990,1980,10,112,661,10) |
| 9 | 7 | (1990,1980,659,112,10,10) |
| 9 | 10 | (1909,1818,524,191,547,91) |
| 9 | 11 | (1951,1901,593,99,605,49) |
| 12 | 5 | (1991,1982,9,465,662,27) |
| 12 | 7 | (1991,1982,660,465,9,27) |
| 12 | 10 | (1952,1903,595,533,607,142) |

For every row, exact `Fraction` evaluation verifies all physical slacks (except `s_4=0`) strictly positive, the chosen lower facet strictly greater than both alternatives, the chosen upper facet strictly less than all three other candidates and the dominated `U_0,U_3`, and `L<0<U`. All chamber inequalities are strict affine inequalities in the six source variables, so each witness proves a six-dimensional relatively open region exists. Boundary ties live in their exact hyperplane faces.

## Theorem 2 — exact canonical endpoint lifts; a reversible observer parameterization

Define `f_-(f)=f+L(f)K` and `f_+(f)=f+U(f)K`. For any real `h` for which `f+hK` remains lawful,

```
L(f+hK)=L(f)-h;   U(f+hK)=U(f)-h,
f_-(f+hK)=f_-(f); f_+(f+hK)=f_+(f).
```

This follows from the exact affine identity `s_i(f+hK)=s_i(f)+hD_i` for every slack. Hence `f_-` and `f_+` are **canonical physical fiber endpoints**, independent of the chosen representative of a fixed `(M,T_P,T_Q)` observer value. On each chamber, both maps are explicitly affine and the complete fiber is reconstructed from its lower endpoint plus one real coordinate `t∈[0,U-L]`.

The map `(f_-, t)` preserves the full seven-flow-vector as `f=f_-+tK` and therefore retains any branch, provenance or future-operation information represented in these coordinates. This is an observer-specific *reversible* chart, not an identification of distinct physical source histories and not a native six-axis spatial quotient.

## Verified computation, scope and next problem

Run `python VERIFY.py` (standard-library `fractions.Fraction` only). `EXACT_OUTPUT.txt` contains the actual stdout. The mathematical proof of the eleven-chamber completeness uses derivative signs, global domination, the exact incompatible-pair inequality, and the eleven strict rational witness checks. The endpoint lift identities hold for every real point of the frozen lawful polytope; the finite witness list proves nonemptiness of the eleven open chambers, rather than merely sampling them.

**BRC application:** population = lawful `g=b` FULL_HIST flow carriers; observer = frozen seven marginal masses plus two stop times; operation horizon = this static Blackwell existence/transport problem. The kernel coordinate is retained, rather than dropped, so future branch-sensitive operations are not silently factored. Reuse resolution = `REUSE_APPLIED` (the predecessor's typed exact observer kernel and rational capacity constraints). This is a scoped observer result, leaving native X6/path evolution independently typed.

**Next exact question:** compute the A- and B-14-edge nonnegative support inequalities on these eleven endpoint chambers after eliminating the source fiber coordinate, and decide whether a finite 14-edge support atlas covers all lawful `g=b` source–seedless-target Blackwell-feasible pairs. An alternative is an exact pair requiring 15 edges. Independent review of earlier global R5 existence PR #1831 remains open.

No native Task CLAIM, Result, independent review, or theorem admission is claimed by this author-side artifact.
