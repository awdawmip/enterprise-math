# R5 — Pairwise strict-cone decision certificate for shared history gates

Date: 2026-11-05 Asia/Shanghai. Status: `AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY`.

## Mother question, authority and scope

Mother R5: can a strictly positive finite P/Q stopping BRC have identical full four-observer convex hulls under full-history and seedless likelihood-ratio policies, while their **actual real-behavior images** differ? This note gives an **all-directions test for a globally valid one-shared-gate Bellman reduction**, plus an independently verified **open four-dimensional separation neighborhood** in the prior strictly positive four-stage model S. The mother question remains open.

Frozen scientific references: Global `a01383f825ef9d43b4b754254303298c64041568`; Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`. Immediate predecessor: EM `e1c2bd1fbdac55ec223036e973a75ab69e482375`, `research_notes/brc_r5_tag_channel_order_20261105_t2244/RESEARCH.md`; predecessor exact mincut: `126745428ba15d75358743e88952144389dc06a6`. Current normative control and P000/ACTIVE worldview are read separately from these science pins. The P/Q tree is an auxiliary finite BRC observer experiment and makes no new X6 dynamics claim.

## Theorem 1: exact pairwise directional criterion

Let `d>=1`, `m>=2`, and `W0,b_i,c_i in Q^d` (or real vectors). Independent upstream real probabilities `a_i in [0,1]` lead to one downstream shared real probability `z in [0,1]`. For seedless observer and full-history observer respectively define

`W_L(a,z)=W0+sum_i a_i b_i+sum_i a_i z c_i`,

`W_F(a,z_1,...,z_m)=W0+sum_i a_i b_i+sum_i a_i z_i c_i`.

These are *observation vectors*, not probability vectors; affine coefficients may be signed. This reduction must already be valid for the declared observation, including all other choices, if used as a global BRC support calculation.

For `n in R^d`, put `A_i=n·b_i`, `u_i=n·c_i`, `M_i=max(0,A_i,A_i+u_i)`. The two support functions are

`h_F(n)=n·W0+sum_i M_i`,

`h_L(n)=n·W0+max{sum_i (A_i)_+, sum_i(A_i+u_i)_+}`.

Consequently, `h_F(n)>h_L(n)` **iff** there are two (necessarily distinct) histories `i,j` satisfying

`n·b_i>0`, `-n·c_i>0` (history i strictly prefers stop),

`n·(b_j+c_j)>0`, `n·c_j>0` (history j strictly prefers continue).

Let `M_ij` be the 4-by-d matrix with rows `b_i,-c_i,b_j+c_j,c_j`. The following are equivalent:

1. `conv O_F != conv O_L`;
2. some ordered pair `(i,j)`, `i!=j`, admits a real `n` with `M_ij n>0` componentwise;
3. some pair admits a rational solution of `M_ij n >= (1,1,1,1)` if all vectors are rational;
4. some pair's strict system has **no** nonzero vector `lambda>=0` satisfying `M_ij^T lambda=0`.

Therefore `conv O_F = conv O_L` iff **for every ordered pair** one can supply a nonzero nonnegative dual dependence `M_ij^T lambda=0`. For rational inputs the primal or dual admits rational witnesses; denominators can be cleared. This is `m(m-1)` homogeneous strict linear-feasibility checks in `d` unknowns, without enumerating a grid of four-observer support directions. It addresses the globally reducible single-gate model, not an arbitrary multi-gate P/Q tree.

**Proof.** Fix `n` and `z`. Every upstream control maximizes independently, producing `sum_i(A_i+zu_i)_+`. Convexity in scalar `z` places a maximum at `z=0` or `z=1`. FULL can maximize each `z_i` independently, giving `sum_i M_i`. The difference from the `z=1` face is positive exactly if some `i` has `A_i>0,u_i<0`; the difference from the `z=0` face is positive exactly if some `j` has `A_j+u_j>0,u_j>0`. Both are necessary and sufficient because `h_L` is the maximum of the two faces. Each strict system is homogeneous; rescaling a real solution yields inequalities `>=1`. Rational strict linear inequalities have rational solutions. Gordan's strict linear theorem of the alternative says exactly one of `M_ij n>0` and nonzero `lambda>=0, M_ij^T lambda=0` holds. Equality of compact observation-set convex hulls is equivalent to equality of supports in all `n`. QED.

For exactly two histories with the strict pattern `i=1,j=2`, the gap on that direction simplifies to

`D(n)=min{ min(A_1,-u_1), min(A_2+u_2,u_2) } > 0`.

The existing finite-history min-cut theorem supplies the corresponding general finite-tag deficit. This paper contributes a **direction search/dual certificate interface** using its strict-positivity condition.

## Theorem 2: observer-safe co-oriented increments

If `c_i=k_i c` for one fixed vector `c` and nonnegative scalars `k_i`, then **the actual real-behavior images are equal**, `O_F=O_L`, for arbitrary upstream `b_i`.

**Proof.** A FULL realization has downstream contribution `c * sum_i k_i a_i z_i`. Write `S=sum_i k_i a_i`. If `S>0`, choose one seedless gate `z=(sum_i k_i a_i z_i)/S` in `[0,1]`; for `S=0` choose arbitrary `z`. This reproduces the same observation vector with the original `a_i`. Conversely the LR strategy is a FULL strategy using all `z_i=z`. QED.

This is an exact scope-typed observer quotient certificate: all history-specific gate choices are invisible under the declared linear observation whenever they affect only one common nonnegative-direction increment. For example with `c_1=c_2=(0,0,1,0)` and `b_1=(1,0,0,0), b_2=(0,1,0,0)`, each ordered-pair strict system has Gordan dual `lambda=(0,1,0,1)`, because the two increment rows cancel. The real images agree by the constructive formula, not merely their hulls.

## Exact positive four-stage BRC model S: source-derived coefficients

The tree is the immutable model S from EM `8275f4043ca50e00ca8078d52bb7448c54189243`:

- time-2 ratios `(3/4,5/4)` with Q masses `(1/2,1/2)`;
- time-3 ratios `(1/2,1,3/2)` with conditional Q rows `(13/20,1/5,3/20)` and `(1/40,9/20,21/40)`;
- time-4 ratios `(1/10,1,19/10)`; Q rows for time-3 ratio 1 from 3/4 and 5/4 are respectively `(1/90,44/45,1/90)` and `(67/162,14/81,67/162)`; for ratio 1/2 the Q row is `(509,382,9)/900`; for ratio 3/2 it is `(9,382,509)/900`.

Each row is strictly positive, sums to 1, and has ratio mean equal to its parent; the P transition is `Q(s|history)*s/r`. These identities are checked again in the accompanying program.

At support direction `n0=(-1,-1,-3/25,+1/50)` on `W=(P[declare Q],Q[declare P],E_P tau,E_Q tau)`, restrict to time-1 continue, Bayes stop/declaration at all other nodes except that each time-2 history has upstream continuation `a,b` and the shared time-3 ratio-1 gate uses common continuation `z`. Exact tree integration gives

`W=W0+a B1+b B2+az C1+bz C2`

with already-weighted coefficient vectors

```
W0 = (3/8, 1/2, 2, 2)
B1 = (-9/80, 3/40, 3/8, 1/2)
C1 = (-19/9000, 1/900, 1/10, 1/10)
B2 = (37/160, -19/80, 5/8, 1/2)
C2 = (-1273/7200, 67/720, 9/40, 9/40).
```

The four strict cone margins at `n0` are

`(n0·B1,-n0·C1,n0·(B2+C2),n0·C2)=(1/400,9/1000,1/400,49/800)`.

Thus the shared-gate loss on this exposed choice cone is `D(n0)=1/400`. To establish *global* support values, the Fraction program independently enumerates all 5,832 deterministic **seedless LR** policies and optimizes all full-history actions with exact backward induction; these give respectively `h_LR(n0)=-429/400` and `h_FULL_HIST(n0)=-107/100`. Both include all legal P/Q declarations, time-1 stop, and off-cone stop/continue choices. The strict difference `1/400` is therefore an actual full-tree hull-separation certificate.

## Theorem 3: a certified open four-dimensional separation neighborhood

For any finite stopping tree with `1<=tau<=4`, an observation vector has coordinates in `[0,1]^2 x [1,4]^2`. Thus for directions `n,n0`, the oscillation of `(n-n0)·W` over the union of either policy's feasible observations is at most `8||n-n0||_infinity`. Fix a FULL optimizer at `n0` and compare against the LR support at `n`. Then

`h_FULL(n)-h_LR(n) >= h_FULL(n0)-h_LR(n0)-8||n-n0||_infinity`.

For positive model S, if `||n-n0||_infinity<=1/6400`, then

`h_FULL_HIST(n)-h_LR(n)>=1/800>0`.

**Proof.** Let `W_F` maximize `n0` over FULL. Then `h_FULL(n)>=n0·W_F+(n-n0)·W_F`. Also `h_LR(n)<=h_LR(n0)+sup_{W in O_LR}(n-n0)·W`. Subtract and bound the difference between the two linear evaluations by the coordinate box oscillation `(1+1+3+3)||n-n0||_infinity`. Substitute the exact gap `1/400`. QED.

This open neighborhood holds for all real behavior probabilities and *all* stop/declaration alternatives, irrespective of whether nearby Bellman ties change. It is an explicit bounded slice of the previously unresolved four-dimensional sign-direction analysis, not the complete fan.

## Execution evidence and next question

`VERIFY.py` uses Python stdlib `Fraction` and enumerates all `3*3^2*3^3*2^3=5832` deterministic seedless LR policies. It checks positive P/Q rows and martingale moments, independently recomputes the four coefficient vectors from the tree, performs a full-history dynamic program, confirms exact gap and robust radius, and checks an exact Gordan dual dependence. All assertions pass; `EXACT_OUTPUT.txt` contains the actual execution.

`REUSE_APPLIED`: prior BRC positive branch mass + provenance and four-observer semantics; finite-tag min-cut theorem; strict-cone/Farkas alternative (classical convex optimization, no new proof priority assigned). `REUSE_EXECUTED`: direct exact Fraction P/Q tree/observer check and complete deterministic LR count. Approximation/large input/physical X6 transfer are outside this statement. Exact complexity: O(m^2) strict feasibility problems for a fixed one-gate reduction, with rational LP arithmetic/bit size plus all cost of deriving correct Bellman coefficient cells for an actual multi-stage model.

**Next discriminating unit:** derive all active `b_i(n),c_i(n)` Bellman coefficient cells (including tie boundaries) in one strictly positive four-stage merger where at least two histories reach the common node with distinct kernels. Within each cell apply the pairwise primal/dual strict-cone test; for any candidate with no separating cell, separately check nonconvexity of the actual seedless behavioral image. This permits a finite, exact all-direction hull equality check without a brute force direction grid, when the correct cell decomposition is available.
