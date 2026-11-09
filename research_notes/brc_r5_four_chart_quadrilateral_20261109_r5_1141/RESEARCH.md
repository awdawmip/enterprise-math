# R5 — Four simultaneous 14-edge Blackwell charts and an exact coupling quadrilateral

Date: 2026-11-09 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / INDEPENDENT_REVIEW_PENDING / NOT_ADMITTED.

## Input and local question

This result continues the frozen R5 seven-node P/Q-BRC Blackwell study. Scientific pins retained from the preceding R5 research line: GLOBAL `a01383f825ef9d43b4b754254303298c64041568`, Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`. Exact predecessors: [PR #1843](https://github.com/awdawmip/enterprise-math/pull/1843) (commit `7244646fed297cc29e2af74755c3fe909c21ff01`, two 14-edge transports along a segment) and [PR #1851](https://github.com/awdawmip/enterprise-math/pull/1851) (commit `05a27b7b70d644672263b76a4b49ad3f4526583e`, 11 source observer-fiber chambers). Current behavioral rules are read separately; no rebasing of frozen scientific inputs.

**Question:** Is the previously known midpoint seam between two 14-edge transports isolated, or does it support multiple sparse couplings in a full-dimensional physically lawful neighborhood? We study the **fixed union of their 16 edges**, not all possible seven-node couplings.

Source flow satisfies `g=b`; target lies on seedless F, `Z=A/10, V-Z=9B/40`. Use nine physical parameters

```
p=(g,a,u,v,w,z,G,A,B).
x(p)=(g,a,g,u,v,w,z).
y(p)=(G,A,B,U,A/10+9B/40,W,A/10).
P=T_P(x(p)); Q=T_Q(x(p));
U=-17A/40-19B/80-G/2-P+3Q/2-1/2;
W=-7A/40-39B/80-G/2+P-Q/2-1/2.
```

The frozen seven-node masses `M(f)` and times `T_P,T_Q` are transcribed into `VERIFY.py`. Likelihood ratios are `r=(1/10,1/2,3/4,1,5/4,3/2,19/10)`. An edge `(i,j)` sends source mass from source node j to target node i, and must satisfy the 21 equations

`sum_j E[i,j]=M_i(y)`, `sum_i E[i,j]=M_j(x)`, `sum_i r_i E[i,j]=r_j M_j(x)`.

Center `p*` is the exact midpoint of the PR #1843 source and target strategies:

```
p*=(1999/2000, 2/15, 67/1600, 157/2400, 109/1600,
    11/1200, 51237/64000, 2751/12800, 30019/38400).
```

All nonidentity capacity slacks are strictly positive there.

## Theorem 1: an exact quadrilateral of couplings on 16 edges

The two predecessor supports are

```
SA=((0,0),(6,6),(0,1),(2,1),(0,2),(2,2),(3,2),(5,2),
    (3,3),(1,5),(2,5),(4,5),(5,5),(6,5));
SB=((0,0),(6,6),(0,1),(2,1),(0,2),(2,2),(3,2),(3,3),
    (0,5),(1,5),(3,5),(4,5),(5,5),(6,5)).
```

Let `S=SA union SB`, with exactly 16 edges, and let `C_S` be its 21-by-16 rational mass/moment coefficient matrix. Exact elimination proves

`rank(C_S)=14`, `dim ker(C_S)=2`.

Two independent exact kernel vectors (zero at all unlisted edges) are:

| edge | K1 | K2 |
|---|---:|---:|
| (0,2) | -5/13 | -15/13 |
| (0,5) | 5/13 | 15/13 |
| (2,2) | 18/13 | 28/13 |
| (2,5) | -18/13 | -28/13 |
| (3,2) | -1 | 0 |
| (3,5) | 1 | 0 |
| (5,2) | 0 | -1 |
| (5,5) | 0 | 1 |

Let `e0` be the exact 14-edge `SA` coupling at `p*`, extended by zeros to `S`. Then **all** mass-and-moment solutions within this fixed edge union have the form `e(s,t)=e0+s K1+t K2`. Its nonnegative portion is a nondegenerate bounded convex **quadrilateral**, with exactly four vertices. Each has exactly 14 strictly positive edges.

| (s,t) | zero edges in S |
|---|---|
| (0,0) | (0,5),(3,5) [SA] |
| (0,415111079/20736000000) | (3,5),(5,2) [new] |
| (1731407/691200000,415111079/20736000000) | (2,5),(5,2) [SB] |
| (120750673/1728000000,-120750673/5184000000) | (0,5),(2,5) [new] |

**Proof.** `VERIFY.py` constructs all 21 equations over `Fraction`, checks the rank and two independent kernel vectors, and exhaustively solves all `binom(16,2)=120` pairs of linearly independent active coordinate inequalities `e_i=e_j=0`. Every 2D polytope vertex must have at least two independent active inequalities. The exact test yields precisely these four feasible vertices and no other vertex; all four are 14-positive-edge points. Boundedness follows because all entries are nonnegative and their sum is 1. A strictly positive 16-edge point is obtained as an average of the four vertices; the region is therefore two-dimensional. This establishes exact quadrilateral completeness **within S only**, not within the global 49-edge transport space.

## Theorem 2: four distinct 14-edge charts coexist on a nine-parameter physical box

For each vertex remove its two zero edges from S and call the remaining 14-edge support `S_k`. Each 21-by-14 coefficient matrix has full column rank, so a compatible solution is unique. At `p*` and at `p*+e_j` for every standard basis vector `e_j` of the nine *parameter* coordinates, the attached verifier solves the 21 linear equations exactly on all four supports (40 exact solves). It checks exact compatibility of all 21 equations for every basis point. Since target vectors, 21 constraints and solutions are affine in p, the checked identities hold for **all real p**.

For each of the 56 edge masses and the 26 physical slacks of x(p) and y(p), write `h(p)=h(p*)+c·(p-p*)`. All identically zero model identities have zero slope. All others have positive center slack, and exact rational enumeration proves:

```
min_h h(p*) / sum_j |c_j| = 5194221/10938329600 > 1/2500.
```

The limiting component is the new chart with zero edges `(2,5),(5,2)`, at positive edge `(3,5)`, where `h(p*)=1731407/691200000` and `sum|c_j|=854557/162000`.

Therefore, **for every real p in the closed box**

```
||p-p*||_infinity <= 1/2500,
```

the source is physically lawful on `g=b`, the target is physically lawful and seedless on F, the two stop times agree, and **four mutually distinct strictly positive 14-edge transport certificates** coexist, each exactly satisfying all 21 equations. This is a nonempty nine-dimensional physical region, not a single path. The associated eight-dimensional observed marginal image has nonzero exact minor

`-1111424393/139968000000`.

The proof of box positivity is `h(p)>=h(p*)-||p-p*||_infinity sum|c_j|`. The quoted infimum is sharp for **these four fixed supports and these nine coordinate axes at this center**; an edge reaches zero at its limiting radius. The safe box remains strictly inside. It is not a global 14-edge upper-bound theorem.

## Scope, evidence, and next exact question

`VERIFY.py` uses the Python standard library `fractions.Fraction` and `itertools` only. It executes all 21 exact equalities, the full 120-pair finite vertex enumeration, 40 affine basis solves, capacity and edge interval bounds, and the eight-dimensional determinant. `EXACT_OUTPUT.txt` is actual stdout. Finite enumeration is a rigorous proof of the stated fixed 16-edge polygon because every vertex is covered, whereas the all-real nine-parameter box is proved algebraically by affine identities and inequalities.

BRC is reused through the frozen LR statistical observer and retained physical flow coordinates. The 2D quadrilateral is a **coupling-parameter polygon**, not a new 2D native spatial plane; the nine-dimensional parameter chart and eight-dimensional observation image are not native X6 spatial axes. No native dynamics, full R5 coverage, minimum global support, P000 change or formal mathematical admission is asserted.

**Next:** derive the four nonnegativity halfspace systems in the eight-dimensional observed quotient, and their relation to the eleven canonical physical fiber chambers. Search for finite 14-edge support atlas coverage, or an exact physical 15-edge-required instance. Existing full-model R5 PR #1831 remains for independent checking. Preserve task pins and real Owner/CLAIM and review boundaries.