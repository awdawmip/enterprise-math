# R5 — An exact physically lawful adjacent edge ray of minimum K_{2,3} word length FOUR

Date: 2026-11-11 (Asia/Shanghai). Researcher-ID: `EM-DIRECT-A9BC55 / TASK_RESEARCH`; Research-Activity-ID: `RA-009AD865C4F47D6D7833BB90`. Status: author-side exact proof and executed rational validation; independent scientific review pending.

## Frozen model and provenance

Use the unchanged scientific pins GLOBAL `a01383f825ef9d43b4b754254303298c64041568`, EM `86149263e38c22292c9def1e0f69092efa1be77e`. This is the auxiliary P/Q–BRC Blackwell 30-arc, 21-observation model in PRs #2017, #2021, #2026, #2032, #2034. Original strictly positive physical coupling and parameter witness: `research_notes/brc_r5_six_edge_circuits_20261111/WITNESS.txt` at Git blob `f9e3671e12604bc29ee2cc07ffc59724bafacc90`. Four variable source ports are `J={1,2,3,5}`; the forced arcs are `(0,0)`, `(6,6)`. Target ports are `i=0,...,6`, ratios `r_i=R_i/20`, `R=(2,10,15,20,25,30,38)`.

For each pair `j≠k` in J and three ordered distinct targets `a<b<c`, let `H(j,k;a,b,c)` be the six-arc residual with row j target coefficients `(r_b-r_c,r_c-r_a,r_a-r_b)`, row k their negatives, zero elsewhere. Every H lies in the kernel of the 21×30 marginal/first-moment observer matrix C and has exactly six nonzero arcs. `L(d)` denotes minimum number of such atoms with arbitrary real scalar coefficients whose sum is d.

## New theorem

There exist **two adjacent vertices V,W of the same fixed physically lawful 15-dimensional Blackwell transport fiber**, each with exactly 15 strictly positive arcs, such that their edge direction `d=(W-V)/t` satisfies

```math
\boxed{L(d)=4}.
```

Thus the earlier two-atom radius-one star (#2032) and three-atom example (#2034) extend to an **exact four-atom adjacent-ray example** inside the same frozen physical fiber.

### Exact vertex and edge direction

All omitted arcs of V and d are zero. This table lists `(target i, source j)`.

```text
V:
(0,0)=219346331/10192753200
(0,1)=7271277/135903376
(1,1)=29907399/169879220
(5,1)=7271277/339758440
(1,2)=8057361/169879220
(2,2)=9236487/679516880
(4,2)=11594739/679516880
(6,2)=196521/67951688
(2,3)=107583593/679516880
(3,3)=377644447/2548188300
(4,3)=50199461/679516880
(5,3)=14346033/339758440
(0,5)=196521/9707384
(6,5)=1375647/19414768
(6,6)=451274777/3397584400

d:
(0,1)=1/2       (1,1)=-7/10     (5,1)=1/5
(1,2)=7/10      (2,2)=-2/5      (4,2)=-4/5     (6,2)=1/2
(2,3)=2/5       (3,3)=-1        (4,3)=4/5      (5,3)=-1/5
(0,5)=-1/2      (3,5)=1         (6,5)=-1/2
```

Define `t=11594739/543613504>0`, `W=V+t d`. Exact calculations show `CV=CW=CE^0`, where E0 is the fully positive physical witness. The physical parameter pair of E0 satisfies all five equalities and 26 capacities. Both endpoints are nonnegative with exactly 15 positive arcs. Their support union contains 16 arcs and has rank(C_U)=15; hence its smallest containing face has dimension `16-15=1` and V,W are adjacent vertices. Explicit pivot step t is the first zero-mass boundary on this direction.

### Four-atom upper bound (exact identity)

```math
\boxed{d=-\tfrac12H(1,2;0,1,5)
+\tfrac59H(5,2;0,3,6)
+2H(2,3;2,3,4)
-\tfrac25H(2,3;2,4,5).}
```

The equality holds coefficient-by-coefficient on all 30 arcs, with rational arithmetic. Therefore `L(d)≤4`.

### Four-atom lower bound (exhaustive structural proof)

The four source row support sizes of d, in order j=1,2,3,5, are precisely `(3,4,4,3)`. A single H contributes exactly three target positions to each of its two source rows. The 4-supported rows j=2 and j=3 each require at least two atoms; rows j=1 and j=5 each require at least one. Any expression using three atoms has exactly six row-incidences, so its row degrees are forced to be `(1,2,2,1)`.

The lone atom involving row 1 must use the exact target triple `{0,1,5}`, while the lone atom involving row 5 must use `{0,3,6}`. Because these triples differ, rows 1 and 5 cannot be paired with each other in one atom. They must each connect to a different one of rows 2 and 3; the remaining atom must connect rows 2 and 3. Thus there are exactly **two** possible source-pair configurations, not 210^3 unrestricted cases.

Subtract the uniquely fixed low-row atoms under either configuration. The remaining row-2 residual has target supports:

- row 1 paired with row 2 and row 5 paired with row 3: `{0,2,4,5,6}`;
- row 1 paired with row 3 and row 5 paired with row 2: `{0,1,2,3,4}`.

Each remainder has **five** nonzero target positions, whereas the single remaining H between sources 2 and 3 can occupy only three. Both possibilities are impossible. Hence `L(d)≥4`; together with the identity, `L(d)=4`.

This argument allows arbitrary real coefficients and arbitrary circuit types. It does not rely on an integer coefficient restriction, numerical optimizer or a limited dictionary search.

## Verification, scope and next question

The standalone executable attached as `VERIFY_FOUR_CIRCUIT_EDGE.py` checks the exact C rank, baseline physical witness, five physical equalities, 26 capacity slacks, 21 observed equalities, 15/15 endpoint supports and ranks, 16-column union rank, boundary step, the four-atom identity and the exhaustive two-case lower bound. Its actual local result is in `EXACT_OUTPUT.txt`. SymPy Rational arithmetic is exact. The same frozen model also contains an earlier adjacent ray with L=3, so this is a distinct local increment, not a generic maximum claim. BRC reuse: the 210 signed port-labeled minimal residual atoms provide the decomposition dictionary; the physically allowed nonnegative fiber selects which composites become tangent rays.

Next discriminating task: enumerate and classify edge-ray minimum word lengths in the verified 1775-vertex radius-four ball; search for an actual L=5 adjacent ray, or prove a sharp bound for all rays of this fixed physical fiber. A candidate lower-bound shortcut is to count source-row incidences and test the remaining small exact source-pair configurations.

The live canonical dispatcher for this run selected `RS-X6-TRIADIC-CLOSURE-DYNAMICS`, not a current R5 owner claim. Accordingly this record is a separate author-side research-note checkpoint; it does not mutate any other researcher's CLAIM or assert a formal Source Result or independent review.
