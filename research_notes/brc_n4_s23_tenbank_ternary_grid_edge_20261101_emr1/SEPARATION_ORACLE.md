# Exact one-coordinate adversarial separation for any fixed finite S23 policy-label bank

2026-11-01. **Analytic lemma** on a generic fixed bank (not specific to the ten boxes) plus an **executed exact rational instance** on the ten uniform-pair predecessor kernels. Status: author-side / UNREVIEWED / NOT_ADMITTED. A one-dimensional restriction is not the complete 11-dimensional optimization.

## Typed setup

Freeze any row-stochastic common encoder E with k source states, and any finite bank of m row-stochastic k-by-4 decoder kernels D_l. Fix ten of the eleven legal S23 behavioral stop parameters to any admissible values and vary the remaining one real parameter t in [0,1]. The complete legal source-time law F(theta) is multilinear in its eleven controls, so with ten controls fixed each prepared time law p_i(t)=(MF(theta))_i is affine in t. The reconstructed laws q_(i,l)=(M E D_l)_i are independent of t. Let G(t)=min_(1<=l<=m) max_(1<=i<=6) TV(p_i(t),q_(i,l)). Labels may depend on the policy; individual decoder kernels remain fixed.

**Generic exact separator theorem:** Define for each l,i and each sign vector sigma in {-1,+1}^4 the affine function

    f_(l,i,sigma)(t) = (1/2)*sum_(a=1)^4 sigma_a (p_i(t,a)-q_(i,l,a)).

There are at most N=16*6*m=96m such individual affine functions. Let C consist of t=0 and t=1 together with every pairwise intersection in [0,1] of two **distinct-slope** functions among those N, ignoring coincident/parallel lines. Then

    max_(0<=t<=1) G(t) = max_(t in C) G(t).

It follows that for rational fixed E,D_l and rational fixed remaining policy coordinates the right side is computable **exactly** with rational arithmetic, without any continuum search, grid tolerance or nonlinear optimizer.

**Proof:** Total variation of a signed zero-total-mass row difference equals half its L1 norm; the L1 norm is the maximum over its 16 coordinate sign dot products. Consequently

    max_i TV(p_i(t),q_(i,l)) = max_(i,sigma) f_(l,i,sigma)(t)

and G(t) is the finite minimum, over l, of those maxima. Consider any open interval between consecutive elements of C. Since no pair of distinct-slope lines crosses inside, the pointwise ordering of every f_(l,i,sigma) is constant there (identical and parallel lines are harmless). Hence each label's maximum, then the bank's minimum, is represented by one and the same affine line throughout this interval. Its maximum over the closed interval is therefore attained at an endpoint. The global maximum must occur in C. Compactness and continuity yield attainment. The proof uses only finite-alphabet total variation, affine policy restriction and precommitted decoder bank. QED.

The number of distinct candidate intersections is at most choose(N,2)+2; it can be reduced exactly by deduplicating affine forms and rational intersections. This theorem **does not** assert an efficient global separator over all eleven S23 controls, nor an all-bank optimum of the ten-label minimax problem: changing decoder kernels changes the candidate lines.

## Exact independent instance on the frozen ten uniform-pair bank

The lawful edge is the H(t) family in PROOF.md: a_A=t, a_B=1, all three b controls zero, terminal c=(1,0,1,0,0,0). The ten decoder pairs are stored verbatim in VERIFY_SEPARATION.py. The exact Python Fraction checker constructs source laws at t=0 and t=1, obtains each of the six prepared-row affine differences through the integer mixture M20/20, enumerates all 16 sign forms of each row and label, reduces duplicates, and exhaustively evaluates G(t) at every rational pairwise line crossing.

The actual check produced **190 distinct (label, affine-form) pairs**, only **29 globally distinct affine lines**, and exactly **18 rational candidate points** including the endpoints:

    0, 1/31, 1/21, 1/11, 1/4, 9/29, 1/3, 11/31, 4/9,
    9/19, 1/2, 11/21, 6/11, 19/29, 2/3, 21/31, 3/4, 1.

The maximum of this continuous one-parameter bank-loss function is **2/3** and its **unique** maximizer is **t=1/3**; the three ternary edge coordinates 0,1/2,1 all have risk 1/2. Thus the line-intersection oracle recovers precisely the adversary that the exhaustive 177147-policy midpoint grid missed. The exact whole-continuum claim follows from the generic lemma; the enumerated rational output independently validates the earlier closed-form H(t) envelope.

## Research scope and next use

Proved: all fixed-bank one-coordinate restrictions for any **real** encoder and decoder bank (finite-candidate theorem). Actually executed: exact rational separator for one concrete 10-bank H(t) edge. Not proved: a universal 11-dimensional separator, another bank achieving risk 1/2, a universal >1/2 lower bound for any bank, or native P000 X6 and time-dynamics transfer. No inference from the unrelated six statistical sources to six native spatial axes.

Next mathematical unit: in the unrestricted ten-label S23 minimax (k=4,6) use this one-coordinate separator on candidate rational banks and find a certified multi-coordinate separation argument (for example Bernstein subdivision plus exact rational interval enclosure, or an exact semialgebraic cell decomposition); separately search for an all-bank lower bound from a finite lawful rational witness set. Do not replace a continuous certificate with a ternary grid.

