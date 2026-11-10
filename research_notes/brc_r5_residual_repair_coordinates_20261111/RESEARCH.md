# R5 — Exact 15-coordinate repair of the physical Blackwell coupling fiber; a 14-arc vertex

Date: 2026-11-11 (Asia/Shanghai). Status: author-side exact derivation and executed rational verification.
Frozen scientific pins (unchanged): global `a01383f825ef9d43b4b754254303298c64041568`, EM `86149263e38c22292c9def1e0f69092efa1be77e`.
Predecessor: PR #2017 and exact physical witness at `research_notes/brc_r5_six_edge_circuits_20261111/WITNESS.txt` (blob `f9e3671e12604bc29ee2cc07ffc59724bafacc90`). This is the original seven-ratio, 21-observer-row, 30-arc auxiliary Blackwell model, under its fixed original 14-variable physically lawful pair. P000 and native X6 semantics remain unchanged.

## Theorem 1: constructive lossless fiber coordinates

Let `r=(1/10,1/2,3/4,1,5/4,3/2,19/10)`, and `D={(i,j):j in {0,1,2,3,5,6},0<=i<=6, j in {0,6} implies i=j}`. A signed perturbation `h` is invisible exactly when `Ch=0`, i.e. all target marginals, source marginals, and weighted source-moment residuals vanish. Relative to the strictly positive published physical coupling `E0`, define precisely **15 free repair coordinates**

`a[j,k] = h[k,j]` for `j in {2,3,5}`, `k in {1,2,3,4,5}`.

Put `d=r[6]-r[0]=9/5`. For each such `j`, reconstruct its remaining two entries by

`h[0,j] = sum(k=1..5) (r[k]-r[6]) a[j,k]/d`,

`h[6,j] = sum(k=1..5) (r[0]-r[k]) a[j,k]/d`.

For every target `i=0..6`, use `h[i,1]=-h[i,2]-h[i,3]-h[i,5]`, and fix `h[0,0]=h[6,6]=0`. These formulas are a bijection `Q^15 -> ker_Q C`, and likewise `R^15 -> ker_R C`.

**Proof.** The source-0 and source-6 columns each contain one arc, so their source-marginal equations force zero perturbation. Each of the other four source columns has zero total and zero first ratio moment; for j=2,3,5 the displayed 2x2 Vandermonde solve uniquely determines masses at targets 0 and 6 from the five central target entries. Target-marginal equality determines the full j=1 column. Summing the four source totals and the four source first moments verifies both constraints in the j=1 column. These operations reconstruct a unique invisible perturbation from every real/rational a, and all invisible perturbations are recovered by extraction of the indicated a. QED.

Its 15 coordinate unit vectors are 15 independent, six-arc `K_(2,3)` signed circuits, with source pairs `(1,j)` and target triples `(0,k,6)`. Every one of the 210 previously classified six-arc circuits has a unique expansion in these 15 basis circuits. The attached exact checker reconstructs all 210 individually.

**Observer-safe consequence.** The augmented data `(CE,a)` uniquely reconstructs the full 30-arc coupling, relative to the fixed reference `E0`. This is a lossless static port-resolved repair of the declared Blackwell observer; future operations must use the reconstructed coupling or receive their own descent certificate.

## Theorem 2: exact 15-variable polytope, vertex criterion and an explicit vertex

For the fixed physically lawful source/target pair of the predecessor witness, the *entire* transfer fiber is represented, without quantifier loss, as

`F = { E0+B a : a in R^15, E0+B a >= 0 }`,

where the rational 30x15 matrix B consists of the basis circuits above. The original physical constraints remain fixed and the 21 original readouts are constant. The two arcs (0,0), (6,6) are fixed at the positive masses `219346331/10192753200` and `451274777/3397584400`; the other 28 coordinates give explicit affine nonnegativity inequalities. Since the total coupling mass is 1 and all masses are nonnegative, F is a bounded 15-dimensional rational polytope with E0 in its relative interior.

**Vertex test:** for any `E in F`, with positive support `S`, E is a vertex iff the columns `C[:,S]` are linearly independent. Indeed, a nonzero kernel vector supported on S permits both small positive and negative perturbations, while any nontrivial midpoint decomposition forces its difference to be supported on S. In particular each vertex has at most 15 positive arcs.

**Adjacency test:** for any two distinct vertices E,F, let `U=supp(E) union supp(F)`. The midpoint has strictly positive mass on every arc of U, so the smallest face containing the pair has dimension `|U|-rank(C[:,U])`. They are adjacent exactly when this dimension equals 1. Every adjacency difference is therefore a signed circuit supported on at least six arcs.

**Constructive 14-arc vertex:** starting at E0, choose an exact rational kernel direction restricted to the current positive support and move to the first nonnegative boundary; repeat until no kernel direction remains. The attached script uses exact SymPy nullspaces and Fraction step sizes, then verifies a final vertex with 14 positive arcs and rank 14. All 14 nonzero rational masses are recorded in `EXACT_OUTPUT.txt` and are reproduced by running `VERIFY_REPAIR.py`. No claim that 14 is the minimum vertex support is made.

## Verification and next problem

The script uses only exact `Fraction` / `sympy.Rational`. It checks rank(C)=15; rank(B)=15; C B=0; six-arc supports for the chosen basis; all 210 K2,3 reconstructions; a nontrivial positive 15-coordinate perturbation; and every intermediate/final pivot's nonnegativity and readout equality, plus rank=14 on the final support. The original physical constraints of E0 were independently verified by the preceding `VERIFY_ALL_210.py` at the cited immutable witness. Execute here from a complete repository checkout:

`python research_notes/brc_r5_residual_repair_coordinates_20261111/VERIFY_REPAIR.py`

Next: use the exact 15-coordinate inequalities and the union-support rank criterion to enumerate or bound minimum vertex supports and adjacency classes of the fixed-physical fiber. In particular, search for 7-to-13-arc vertices and test whether arbitrary adjacency circuits beyond the 210 minimal patterns occur. This research note does not perform an independent mathematical review or Source Result admission.
