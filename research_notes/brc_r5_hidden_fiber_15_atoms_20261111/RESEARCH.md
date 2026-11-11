# R5: sharp fifteen-atom hidden-fiber distance with identical source-3 data

Date: 2026-11-11 (Asia/Shanghai). Status: author-side exact rational proof and exhaustive finite certificate; independent review and formal Source Result pending.

## Frozen scientific model and predecessors

Preserve the original frozen science pins: GLOBAL `a01383f825ef9d43b4b754254303298c64041568`, Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`. This result concerns only the external P/Q–BRC Blackwell auxiliary fiber, not native X6 physical dynamics. The 28 dynamic masses are indexed by target `i=0,...,6` and source `j in {1,2,3,5}`, plus two fixed singleton arcs. The likelihood numerator vector is `R=(2,10,15,20,25,30,38)`. The frozen observer is `F={x in Q^28_{≥0}: Ax=b}`, with 7 target sums, 4 source-port sums, 4 source-port likelihood moments (row rank 13). The 2026-11-11 R5 predecessor [PR #2095](https://github.com/awdawmip/enterprise-math/pull/2095) provides the exact C-face interior state `Z` and three B-face one-atom exits. No science pin is changed.

A legal elementary atom is `H_j(v)`, `j in {1,2,5}`, where `v` is a nonzero three-target vector satisfying `sum_i v_i=sum_i R_i v_i=0`; the source-3 change is `v` and the compensator-port change is `-v`. A legal atomic path requires nonnegative masses at all intermediate states.

## Main theorem: a hidden ten-dimensional fiber has sharp generic distance 15

Fix any strictly positive `X in relint(F)`. Restrict the endpoint `Y` by `Y_(i,3)=X_(i,3)` for every target i, and by `AY=AX=b`. In a sufficiently small relative neighborhood of X, the admissible endpoint differences form a **ten-dimensional rational affine space**. There is an open dense full-Lebesgue-measure subset of that neighborhood for which the minimum **legal** six-arc BRC operation count from X to Y is **exactly 15**.

More strongly, the exact rational X and Y constructed below have (i) all 28 dynamic entries strictly positive, (ii) identical source-3 mass vector, (iii) the same full Blackwell observation, and (iv) a 15-step strictly positive legal atomic path, while every legal or even purely algebraic atomic representation of Y-X needs at least 15 atoms. Thus the sharp 15-step result has a reproducible finite witness.

The previously proved 1/2/3-step endpoint-simplex result is a special lower-dimensional family of constrained changes. The present 15-atom theorem explains what happens when the other port-local, observation-invisible degrees of freedom are released.

## Proof: rank-five per-port atoms and a ten-dimensional hidden fiber

Let `K={w in Q^7: sum_i w_i=0, sum_i R_i w_i=0}`. The two functionals are independent (all R_i distinct), so `dim K=5`. Every within-fiber difference at a compensator port j belongs to K.

If the source-3 row stays unchanged, target-sum conservation gives `w_1+w_2+w_5=0`, where `w_j=Y_(.,j)-X_(.,j)`. Conversely, any `(w_1,w_2,w_5) in K^3` satisfying this equation gives a unique observation-preserving change with source-3 row zero. Therefore its affine solution space is `K^2`, of dimension 10; strict positivity of X provides a relatively open neighborhood of legal endpoints.

For each i=1,...,5 define the three-target vector
```
h_i(0)=R_i-R_6,   h_i(i)=R_6-R_0=36,
h_i(6)=R_0-R_i,   h_i(other)=0.
```
The five `h_i` form a basis of K because their 1,...,5 coordinates are the independent coordinate axes. Consequently any pair (X,Y) in the same observation fiber has an algebraic representation in **at most 15** atoms: five at each compensator port j. If X has 28 strictly positive dynamic entries, then for sufficiently small `Y-X`, this fixed 15-move representation is legal even in its fixed order: each intermediate point stays positive by the triangle inequality.

For the lower bound, the three-target null directions form a **finite dictionary of 35 rational lines** per port. The set of `w in K` representable by at most four dictionary atoms is a finite union of proper linear subspaces of K, hence closed, nowhere dense and of five-dimensional measure zero. Each projection `(w_1,w_2)↦w_j` from K² onto K (including `w_5=-w_1-w_2`) is surjective. The complement of the union of their three exceptional preimages is open, dense and full measure in K². For every difference there, each of the three compensator ports requires at least five atoms. Every elementary atom touches exactly one compensator port, so **at least 5+5+5=15 operations** are needed, independently of ordering, intermediate support or nonnegativity. Combining with the small-neighborhood construction yields the claimed exact generic legal distance.

## Constructed rational witness, finite exhaustive lower-bound certificate

Start from the exact predecessor's C-face interior Z. The predecessor's verified `Y_3` has source-3 support B. Let `M=(Z+Y_3)/2`, with positive source-3 indices 2,3,4,5,6 and strictly positive masses at all compensator ports. Define

```
g0=H_5({0:23, 2:-36, 6:13})
g1=H_5({1:23, 2:-28, 6:5})
tau = 155682221/578268864880000000
X = M + tau*g0 + tau*g1.
```
Both directions conserve count and R-weighted moment; X has 28 strictly positive dynamic entries.

Choose the 5 coordinates of each compensator-port change (target labels 1,...,5):

```
j=1: (12,  8, 1, 13,  8)
j=2: ( 3, 13, 7,  4,  2)
j=5: (-15,-21,-8,-17,-10)
```

They sum to zero. Let `eps=1401139989/33891583906880000000`. At each port j and each i=1,...,5 take the elementary move `(-eps*c[j][i]/36)*H_j(h_i)`. Exactly 15 moves create Y with every source-3 mass unchanged. The exact verifier computes all 16 visited states; each satisfies the 15 observer equalities and is strictly positive. The least initial mass is `155682221/25142124560000000`, and the least intermediate mass is `188842534073/33891583906880000000`.

For an explicit **exact finite lower-bound certificate**, identify K with its five target coordinates (indices 1,...,5). Enumerate all 35 signed three-target elementary directions and their `C(35,4)=52360` unordered four-direction sets. Let `p=2147483647`. Every four-by-four minor of these integer direction matrices has absolute value at most `4!*36^4 = 40310784 < p`; hence a 4-set has rank 4 over Q iff it has rank 4 modulo p. Among all 4-sets, 46,198 have rank 4, 6,162 have smaller rank, and the rank-4 sets produce 3,468 distinct normalized modular hyperplane normals. The verifier evaluates each normal against all three prescribed port-coordinate vectors: **every one of the 3,468 × 3 dot products is nonzero mod p**. Thus none of the three port differences is in the rational span of four dictionary atoms; rank-smaller subsets can always be extended to a rank-four set because the dictionary spans K. Each port needs at least five atoms, establishing the legal lower bound 15 for this exact witness. The finite-field calculation certifies rational non-vanishing and does not substitute a floating tolerance.

Run `VERIFY.py` with Python 3 standard-library `fractions.Fraction`; `EXACT_OUTPUT.txt` records the executed result:
`PASS_R5_EXACT_HIDDEN_FIBER_SHARP_FIFTEEN_ATOMS`.

## Research meaning and next unit

The source-3 row is an information-losing observer even when the entire observation A is fixed: identical source-3 mass profiles can hide differences requiring 15 elementary BRC updates. This realizes a ten-dimensional residual fiber with a **generic**, rather than merely worst-case, exact local operation cost. It is a mathematical statement about the specified labeled auxiliary observation model.

Next investigate the legal atomic distance for arbitrary far-separated full-support endpoints: the algebraic upper bound 15 always holds, whereas positivity of the fixed 15-term decomposition requires a local condition. Determine whether a suitable 15-move ordering/decomposition is always legal, or construct an exact farther-pair witness requiring more than 15 moves. Formal Source Result admission and independent mathematical review remain separate.

Provenance: original R5 science pins, PR #2095 prior construction; this turn's exact arithmetic and complete finite-dictionary certificate. No existing research task CLAIM or protected world premise changed.
