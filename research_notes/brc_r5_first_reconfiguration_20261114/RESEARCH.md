# Frozen R5: the first optimal-budget transition requires seven membership changes

Date: 2026-11-14. Frozen scientific input: awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551. This work continues the precise scalar integer-event checkpoint model of Draft PRs #2302, #2307 and #2312, with P000 unchanged.

## Definitions

For a finite set of distinct integers X={x_0<...<x_(N-1)}, a subset S⊆X is radius-2 feasible if d_S(x)=min_{s∈S}|x-s|≤2 for all x∈X. Define J(S)=Σ_{x∈X}d_S(x) and J_2(K)=min_{|S|=K,feasible}J(S). Let Opt(K) denote all minimizers. For a budget transition K→K+1, define

    rho_K = min_{S∈Opt(K),T∈Opt(K+1)} |S\T|.

Then there are rho_K+1 additions, and the least symmetric difference is 2rho_K+1. Exact nesting is equivalent to rho_K=0.

## Theorem 1: displacement lower bound

For radius-2 feasible sets S,T with |T|=|S|+1, letting r=|S\T| and Δ=J(S)-J(T), we have

    Δ ≤ 2r+3.

Proof: put U=S∪T. Exactly r+1 centers belong to T\S. Add these sequentially to S. At every step the cover stays feasible; the sharp integer radius-2 one-center insertion bound proved in #2312 gives J(S)-J(U)≤3(r+1). Each of the r distinct integer points in S\T has distance at least one from T but zero from U, so J(T)-J(U)≥r. Subtract: Δ=[J(S)-J(U)]-[J(T)-J(U)]≤3(r+1)-r=2r+3. For two optimal sets this yields rho_K≥max(0,ceil((J_2(K)-J_2(K+1)-3)/2)). This is a general theorem for the stated discrete radius-2 model.

## Theorem 2: frozen R5 first-transition exact reconfiguration

At the frozen R5 event-boundary coordinates, J_2(213)=1070 and J_2(214)=1064, but the exact optimum-to-optimum displacement is

    rho_213 = 3;    min |S△T| = 7.

Proof: the original 953 rational activation walls produce 954 strictly increasing integer event coordinates and 1,065 activation events. Exactly 28 adjacent coordinate gaps equal 3. Each exceeds the radius 2, so a center from one side cannot serve a point on the other side. Thus the feasible selection and objective factor into 29 blocks. Sum of the blockwise minimum center counts is 213; sum of their corresponding optimal costs is 1070. At K=214 precisely one block can receive an additional center. Exact min-plus path DP finds its maximal first marginal gain is 6, attained uniquely by zero-based block index 22 (the twenty-third block); all other blocks have gain at most 5. Therefore every global K=214 optimum uses one additional center in this block.

This block contains 38 event coordinates. After translating its leftmost position to zero, they are

    0,1,2,4,5,6,7,8,9,10,11,12,13,14,15,17,18,19,20,
    22,23,24,25,26,27,28,29,30,31,32,34,35,36,37,39,40,41,42.

An exact center-path DP with tied counts finds precisely 12 optimal sets of cardinality 9 with cost 42 and precisely 640 optimal sets of cardinality 10 with cost 36. Backtracking all equality-attaining DAG paths enumerates those 652 distinct optimal subsets. The 12×640=7680 ordered optimal pairs have the following complete histogram of removed centers:

    r=3:120; r=4:776; r=5:2016; r=6:2624; r=7:1704; r=8:440.

The minimum is exactly 3. A witnessing pair of block-relative coordinates is

    A = {1,5,10,15,20,25,30,35,40}
    B = {1,5,10,13,18,23,26,30,35,40}.

Thus A\B={15,20,25} and B\A={13,18,23,26}. All 652 individual optimal paths have their actual nearest-center distances and radius checked exactly. Choose identical local optimal centers in the other 28 blocks for both global solutions. This realizes global r=3; no global optimal pair can do better, by unique first-gain block and exhaustive local optimal-pair classification.

## Counterexample to the converse of the gain bound

A marginal improvement of 3 does not guarantee that a nested optimal pair exists. For X=(0,2,3,4,6), full subset enumeration gives the three K=2 optima {(0,4),(2,4),(2,6)} at cost 5; the unique K=3 optimum is (0,3,6) at cost 2. None of the former is included in the latter. So Δ=3 and rho_2=1. The >3 non-nesting certificate in #2312 is sufficient but not necessary.

## Complementary saturation chain

For radius R≥1 and any distinct integer X, let D_1 be the least cardinality of a radius-1 cover. The prior saturation result #2302 gives J_R(K)=N-K for every K≥D_1. Begin with one radius-1 cover of size D_1, and add the other coordinates in any order. Every set in this increasing chain is exactly optimal at its own cardinality. In R5, D_1=351; hence all 603 transitions K=351→352 through K=953→954 admit a nested chain. This is a new corollary/construction of the earlier saturation theorem, not a reproving of the saturation theorem.

## Exact verification and next question

VERIFY_R5_FIRST_RECONFIGURATION.py uses only Python 3 standard library with integers and Fraction. It independently reconstructs the 15-atom pinned data, all rational walls and blocks, performs exact blockwise min-plus DP and backtracks all optimal center paths for block 22. It checks all 7,680 optimum pairs, each of the 652 path costs and covering radii, and separately all subsets of the five-point example. EXACT_OUTPUT.json records exact counts, local witnesses and provenance. No floating-point estimates are used.

Remaining research: compute rho_K for the other 78 proven-nonnested R5 budget transitions and classify the 59 intermediate-gain (2 or 3) transitions. Independently, the original 2,520-byte certificate / native 28-coordinate / 8,192-query end-to-end experiment remains open. This result is an author-side scientific artifact, not a formal shared-task CLAIM, accepted Result, independent review or native X6 identification. Native session registration is tracked separately from this mathematical derivation.
