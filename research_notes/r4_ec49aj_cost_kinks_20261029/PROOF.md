# EC49AJ — exact global cost kinks after EC49AI

Date 2026-10-29. Author-side portable research; unreviewed and NOT canonically admitted. Mathematical domain: *auxiliary 18+18 strictly positive probabilistic BRC observer*, not native signed/phase BRC or the six-axis heartbeat world.

## EC49AJ-1: sharp theorem for every real lawful causal strategy

Fix the exact original EC49AI model with eta=3/10, k=177/172, C1=43/48, C2=7/8−epsilon, and H=alpha−k beta. For EVERY real epsilon in [0,3/32], and every lawful real behavioral policy using fresh independent post-observation coins and never recovering forgotten history, the maximum of H is

    0 <= eps <= 3/128:
        Hmax = 919/8256 - (49/860) eps

    3/128 <= eps <= 179/2592:
        Hmax = 4451/41280 + (79/860) eps

    179/2592 <= eps <= 3/32:
        Hmax = 249/2752 + (59/172) eps.

There are **two genuinely sharp global cost-support slope transitions** at epsilon=3/128 and 179/2592. Equivalent second-stage costs: C2=109/128 and C2=2089/2592. Sharp endpoint H values are 36319/330240, 50899/445824, and 675/5504, respectively. The exact cost interval is C2 in [25/32,7/8]. The first subinterval reuses EC49AI; the second and third subintervals and the proof of a second kink are new.

## Source laws, observation erasure, and costs

Each history w in {0,1,2}, first signal u in {0,1}, and second signal z in {0,1,2} gives one of 18 leaves under each source:

    t(w,u) = 1/2 + (2u−1)(1−w)*(3/10)
    P(w,u,z) = t(w,u) * (1/6 if z=w, else 1/12)
    Q(w,u,z) = t(w,u)/9.

All 36 leaves are strictly positive; each source sums to 1; the (w,u) marginal is identically t(w,u)/3 under P and Q. First-stage behavioral actions A0,A1,B0,B1,STOP have costs 1,1,2,2,0. A paid action reveals only its action label c and the bit u; it does NOT preserve history w or the first-stage random seed. A new independent coin on each (c,u) decides whether to buy sensor S (cost 1, revealing z), then a new terminal acceptance coin can depend on (c,u,z). An unpurchased or STOP outcome can accept or reject only with its available information. Both stage expected costs are exact equalities. The theorem includes all real random probabilities, not merely rational policies or a finite grid.

## Sharp legal strategy Y(epsilon)

Choose first action with these probabilities, in order (A0,A1,B0,B1,STOP):

    w=0: (9/16−6epsilon, 0, 1/16+3epsilon, 0, 3/8+3epsilon)
    w=1: (0,1,0,0,0)
    w=2: (1,0,0,0,0).

All entries are nonnegative for 0<=epsilon<=3/32. After each paid (label,u), **always** purchase S; accept precisely when

    d(c,u,z) := sum_w x[w,c] * (P(w,u,z)−k Q(w,u,z)) > 0.

Ties may be accepted or rejected. STOP is rejected. All random choices are local and fresh, with no cross-stage shared seed and no access to hidden w. For Y, the row-total STOP mass is s=3/8+3epsilon; the B mass is b=1/16+3epsilon. Thus

    C1=(3−s+b)/3=43/48
    C2=1−s/3=7/8−epsilon.

Six positive atoms on the first open segment are (A0,0,2),(A0,1,0),(A1,0,1),(A1,1,1),(B0,0,0),(B0,1,0). At epsilon=3/128, (A0,1,2) changes from negative to positive and is added. At epsilon=179/2592, (A0,1,0) changes from positive to negative and is removed. Specifically,

    d_Y(A0,1,2) = −3/860+(32/215)epsilon
    d_Y(A0,1,0) = 179/10320−(54/215)epsilon.

There are no other interior sign roots across the 24 paid-observation atoms on [0,3/32]. Each interval has a fixed optimal acceptance mask and therefore an affine H(Y_epsilon); exact summation of source contributions produces the three stated lines. At the switching points, the affected atom has zero H contribution even though its P and Q masses are separately positive. Thus an optimal alpha/beta realization can jump at the mask tie without violating continuity of the sharp support value.

## Universal proof (not an extrapolation of a finite test)

For arbitrary legal first-stage probabilities x[w,c], let

    q(c,u) = (1/3) sum_w x[w,c] t(w,u)
    Phi(c,u) = sum_z max(0,d(c,u,z)).

The marginal distribution at STOP and at a paid (c,u) without S is the same under P,Q. Since k>1, accepting at either uninformative outcome contributes a nonpositive quantity to H. If r(c,u) is the independent S-buy probability, then

    H <= sum_{c,u} r(c,u) Phi(c,u),
    sum_{c,u} r(c,u) q(c,u) = C2, 0<=r(c,u)<=1.

Therefore for every lambda>=0,

    H <= F_lambda(x,epsilon)
       := lambda C2 + sum_{c,u} max(0,Phi(c,u)−lambda q(c,u)).

We fix **the same lambda=49/860 for ALL three cost intervals**. For any fixed epsilon, F is convex in x, since d and q are linear, positive part is convex, and sums and positive parts preserve convexity.

Now let b denote the unnormalized sum over all three histories of B0/B1 first-action probability; let s denote the corresponding STOP sum. Exact C1 implies s=5/16+b. Since second-stage expenditure cannot exceed the paid probability 1−s/3, exact C2 requires

    0<=b<=B_epsilon:=1/16+3epsilon.

On the entire proposed domain, 5/16+2B_epsilon<=1. This is the key capacity condition. It proves that every lawful x lies in the convex hull of **288 indexed templates**:

* choose b=0 or B_epsilon;
* place all STOP mass s in one of three history rows i;
* place all B mass b in one of three rows j, with one of two B labels;
* choose A0 or A1 independently for each of three rows, assigning all the remaining row probability to that label.

Count: 2 * 3 * 3 * 2 * 2^3 = 288 indexed templates, with repetitions when b=0. There are 168 distinct templates for the first three knot values and 144 at epsilon=3/32. Every template is nonnegative because if STOP and B fall in the same row, s+b<=1. Conversely, any feasible x at fixed b is the average of templates with exactly that b: independently select its STOP row, B row/B label, and conditional A0/A1 labels to reproduce x's marginals. Then each template's x(b) is affine in b; mix the b=0 and b=B_epsilon endpoint versions with weights (1−b/B_epsilon,b/B_epsilon). This decomposition exists for the proof of a convex bound. It does **not** authorize implementing a behavioral strategy by storing a shared random choice.

For any indexed template v(epsilon), its x coordinates are affine in epsilon. Thus F_lambda(v(epsilon),epsilon) is convex as a function of epsilon, being an affine lambda C2 plus positive parts of convex functions of affine parameters. The checker verifies at each of **four exact knot values**:

    epsilon = 0, 3/128, 179/2592, 3/32,

that for all 288 indexed templates, F_lambda(v(epsilon),epsilon)<=H(Y_epsilon). The maximum is equal to the witness at every knot. For a fixed template on an interval between adjacent knots, convexity bounds F by the chord joining its endpoint bounds. H(Y_epsilon) is affine on this interval, so that chord equals the exact target H(Y_epsilon). Then convexity in x carries the upper bound to every feasible first-stage policy, and the sensor dual bounds every real post-observation policy. Since Y_epsilon is a lawful attaining witness, the proposed global support is proved for **all real epsilon and all real behavioral strategies** in the stated domain.

## Actually executed exact evidence

The self-contained Python standard-library Fraction verifier and the independently implemented JavaScript BigInt verifier were both actually run and yielded matching rational endpoint certificates. The checks comprise 288 indexed templates x 4 knots = **1152 exact endpoint inequalities**, with **648 distinct endpoint comparisons**, exact first/second costs, 18+18 positive normalized source leaves, correct P/Q marginal equality, exact global primal values, both sign roots, and correct three affine segments. Reports saved as EXACT_FRACTION_REPORT.json and EXACT_BIGINT_REPORT.json. These are author-run arithmetic checks, not independent mathematical review and not formal proof-assistant certification. The all-real claim is justified by the analytic convex-hull and convexity argument plus the exhaustive exact finite checks.

## Exact stopping boundary and research next step

At epsilon=3/32, Y's w=0 A0 mass 9/16−6epsilon reaches zero, and the capacity relation s+b=5/16+2 B_epsilon reaches 1. Above that point, Y would have a negative action probability and the old 288 templates cease to be a complete feasible convex family: the extension of the third line is UNPROVED. EC49AK should derive the correct capacity-constrained first-stage vertices for epsilon>3/32 and find the next sharp primal/dual segment or an exact counterexample. The present theorem does **not** assert a third global kink at that boundary.

No native signed/phase BRC amplitude, provenance, X6 cell geometry or heartbeat-time theorem is claimed. Native transfer still needs typed observer maps and preservation under the explicitly declared terminal operations; P000 and ACTIVE worldview are not modified.

Status: AUTHOR_PROVED / TWO_EXACT_RATIONAL_CHECKERS_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED.