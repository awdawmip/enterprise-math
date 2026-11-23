# R284GG — Sharp four-phase capacity for every read-noise budget in the high-omission region

Date: 2026-11-24 Asia/Shanghai. Author-proved with exact finite rational certificate coverage; NOT independently reviewed. Informed portable TASK_RESEARCH, continuing R284GE/R284GF, same frozen R284CO/R284FM Boolean auxiliary observer. P000 and ACTIVE worldview unchanged. No shared CLAIM or formal Result.

## Result

For all integers u>=1 and q>=4u+1, in the original fixed four-phase binary tag model,
    
    n_min(q,u) = 4q+8u+2.

The model is four distinct fixed binary words in cyclic order, with each nominally changing bit attempted once on its publication edge, at most q failed attempts per edge, arbitrary persistence of old omissions, at most u adversarial bit flips per read, stateless decoder, correct stable reads, no third-phase success during a prefix, and no newer-then-older successful read on one publication edge. Fixed attempted order as in the frozen prior model.

The missing implication from R284GF is now proved: if the nonconstant histogram has total <=4q+8u+1, satisfies both opposite-phase stable separations and all four exact adjacent no-rollback constraints, at least two types in {3,5,6} have multiplicity >=2q+2u. Both q and u are unbounded; no per-parameter numerical extrapolation is used.

## Proof of the missing implication

Normalize c0=0 (complement individual columns), and write x_p for nonconstant pattern multiplicities, where bit i-1 of p is c_i, i=1,2,3. Constant columns can be discarded: they never change; their nominal values are fixed for all physical states and a decoder can be simulated by restoring the constants with zero read flips on those columns. The remaining total is at most the original width. Our bound is an inequality, not an equality, so no padding argument is needed.

Use nine real variables x1,...,x7,q,u, constrained by x_p>=0, q>=0, u>=1, q>=4u+1, and sum x_p<=4q+8u+1. On the physical integer domain, failure of the desired two-heavy conclusion means one of the three pairs (3,5),(3,6),(5,6) has both multiplicities <=2q+2u-1. Add these two affine inequalities separately for each case. This real relaxation retains all hypothetical physical counterexamples.

The exact stable cut R284FM for the two diagonals uses K_(2,2) with four edge types. For (0,2) the two disjoint edge pairs are (3,6),(2,7); for (1,3) they are (3,6),(1,4). A separating cut must contain one edge with sum >=2q+2u+1, two incident edges with sum >=3q+2u+1, or all four with sum >=4q+2u+1. The three-vertex subsets consist of exactly two incident edges; two nonincident edges require four vertices and are subsumed by the all-four choice because x>=0. Thus there are exactly nine sufficient disjuncts per diagonal. The integer strict cut is replaced by its equivalent affine +1 threshold before real relaxation.

For each publication edge, the actual last-change source groups of changing patterns are:
    
    0 -> 1: {1}, {3}, {5,7}
    1 -> 2: {2}, {6}, {1,5}
    2 -> 3: {4}, {3}, {2,5}
    3 -> 0: {7}, {6}, {4,5}.

R284GE gives the exact adjacent requirement sum_e (N_e-q)_+ >= q+4u+1, where N_e is the sum of the multiplicities in one listed source group. Since sum_e (N_e-q)_+ = max over group subsets J of sum_(e in J)(N_e-q), this requirement is exactly the disjunction over seven nonempty group subsets:
    
    sum_(e in J) N_e >= (|J|+1)q+4u+1.

Both the diagonal incidence and source grouping are reconstructed directly from the seven bit patterns in the accompanying verifier, not inferred from an unlabeled Hamming radius. The six disjunctions have 9,9,7,7,7,7 choices.

For each nonheavy pair we construct a finite tree. At an internal node choose any unused one of the six disjunctions, and create one child for every alternative. Each leaf contains a nonnegative rational Farkas multiplier vector for the accumulated inequalities A_i v<=b_i (including the base inequalities). The verifier checks exactly that sum lambda_i A_i=0 and sum lambda_i b_i<0. The weighted sum would imply 0<0 in the sense 0<=negative, a contradiction. Every full choice of the six disjunctions either reaches a certified contradictory prefix or would reach an uncovered leaf; the verifier rules out the latter. Hence none of the three nonheavy systems has a real solution, proving the desired two-heavy implication. No q or u upper bound is imposed.

The first fixed-order branch run produced 589,365,1015 certified leaves respectively, with maximum denominator 40; an adaptive choice of the next disjunction reduced this to 157,159,157 leaves, total 473. SciPy 1.17.0/HiGHS was used only to propose multipliers and select the branch order. Every certificate and the entire branch coverage was independently checked in exact Python Fraction arithmetic. The standard-library replay embeds the complete adaptive tree (38331 uncompressed bytes, SHA256 e4f5712be8d86aa7b865c0423e14b3194d6548535bcdf294457c52140c69b166). No optimization solver is needed to replay. The local run also independently reconstructed all six incidence/group lists and returned the same three leaf counts. The standalone packaged version uses the same data and exact checks; remote bytes are verified separately.

Certificate source: 1d92030a09b96f41661247bc2bae837ed8ff1899:research_notes/portable_direct/R284GG_exact_general_u_certificate.py (Git blob ba7765bbac3869c2996e378173f81b051229784b). Run with python3 without -O, as assertions are the verifier.

## Complete capacity deduction

Any valid code with n<=4q+8u+1 must satisfy these six necessary conditions, hence lies in the two-heavy sector. R284GF excludes every such code for q>=4u+1 and u>=1 by its explicit diagonal-prefix witness. Consequently n_min>=4q+8u+2.

R284FE uses two independent Gray groups of length K=2q+4u+1, with one group changing per cycle edge. Each group decodes logical 0 at observed Hamming weight <=q+u and logical 1 at weight >=K-q-u, otherwise RETRY. Completed groups have at most q residual errors; a read adds at most u more. In a 0->1 write, physical weight is nondecreasing, and physical weights permitting old success are <=q+2u, while those permitting new success are >=K-q-2u=q+2u+1. The reverse edge is symmetric. An unchanged group is always read correctly. Therefore no third phase or rollback is possible, and stable reads are correct. This construction attains 2K=4q+8u+2, completing the sharp formula.

Examples: (q,u)=(9,2) requires 54 bits, (13,3) requires 78, (17,4) requires 102. The existing u=1 all-q result for q>=2 is retained; the present theorem adds an unbounded two-parameter sector, not the lower-q general-u sector.

## Frozen sources and scope

- R284FM: 1d1c5dd412719c7aaf016187b6493b77253cd9f9:research_notes/portable_direct/R284FM_NOISY_OBSERVER_FLOW_CUT_AND_ADDITIVE_LOWER_BOUND_20261123.md
- R284GE: a112519ea319ef0e0bdf10ee01d817e10fd3dcd5:research_notes/portable_direct/R284GE_EXACT_ADJACENT_ROLLBACK_CAPACITY_20261124.md
- R284GF: 85801535d3b34cca713f28703b4984baf80975f3:research_notes/portable_direct/R284GF_UNIFORM_TWO_HEAVY_DIAGONAL_BARRIER_20261124.md
- R284FE: 9974b3b5a1031bb5c841ab5a4950a9c55baed9e0:research_notes/portable_direct/R284FE_GRAY_EPOCH_SHARP_SEPARABLE_CAPACITY_20261123.md

This is an auxiliary Boolean observation/residual model; provenance of each last-change slot is retained. It does not alter the native X6/P000 foundation or claim a native geometry result. This is author checking with exact reproducible certificates, not independent mathematical Review. Next: weaken q>=4u+1, starting at q=4u and q=4u-1; identify whether the two-heavy implication or diagonal witness is the first obstruction. Then analyze joint tag/data-bank omission capacity and cache horizon under the frozen observer.
