# EC49AI — Exact second-stage cost facet and immediate loss of fixed-prefix optimality

2026-10-29. Author-side portable research; mathematically proven under the model specified below with two executed exact-rational checkers. Unreviewed and not canonically admitted.

## Theorem (EC49AI-1)

Consider precisely the auxiliary 18-leaf-per-source positive probability observer of EC49AH. Histories w,z∈{0,1,2}, first observation u∈{0,1}; fix η=3/10 and k=177/172. The source laws are

    t(w,u)=1/2+(2u−1)(1−w)η,
    P(w,u,z)=t(w,u)*(1/6 if w=z else 1/12),
    Q(w,u,z)=t(w,u)/9.

First-stage actions STOP, A0, A1, B0, B1 cost respectively 0,1,1,2,2. At every paid (action-label c,u), the observer has forgotten w and its first-stage random seed; with a fresh independent Bernoulli decision it may buy sensor S, costing 1 and revealing z; further fresh terminal acceptance coins may depend only on available information. Both sources have the same paid-observation marginal. Fix exact expected first-stage cost C1=43/48, and exact second-stage cost C2=7/8−ε. Let α and β denote acceptance under P and Q.

**For every real 0≤ε≤3/128 and every lawful real erased-history fresh-coin policy,**

    H=α−(177/172)β ≤ 919/8256 − (49/860) ε.

This bound is sharp simultaneously for all ε. Equivalently, for every real 109/128≤C2≤7/8,

    max H = 919/8256 − (49/860)(7/8−C2).

Moreover the earlier fixed prefix X ceases to be optimal at every strict reduction 0<ε≤3/128:

    Hmax given fixed X = 919/8256 − (179/2236) ε,

so the exact loss from insisting on X is

    Hmax − HX = (3/130) ε > 0.

At ε=0 the prefix X is optimal; for C2>7/8 X cannot satisfy the cost since its total paid mass is only 7/8. This is an exact local optimal-prefix transition at the baseline budget, not a claim about the entire lower-cost parameter axis.

## The optimal lawful prefix Yε

Use the following first-stage policy, with the entries in each history listing the probabilities of A0, A1, B0, B1, STOP:

    w=0: (9/16−6ε, 0, 1/16+3ε, 0, 3/8+3ε)
    w=1: (0, 1, 0, 0, 0)
    w=2: (1, 0, 0, 0, 0).

All entries are nonnegative throughout the claimed range. On every paid (c,u), ALWAYS buy S, and after observing z accept exactly the six atoms

    (A0,0,2), (A0,1,0), (A1,0,1), (A1,1,1),
    (B0,0,0), (B0,1,0).

Reject all remaining terminal atoms and every STOP outcome. All decisions use fresh local coins; this strategy stores no shared random seed and retains no access to w after the first-stage action.

Writing b=Σ_w P(B action|w) for the UNNORMALIZED three-row B mass and s=Σ_w P(STOP|w), the first-stage cost identity is

    C1=(3−s+b)/3 = 43/48, hence s=5/16+b.

For Yε, b=1/16+3ε and s=3/8+3ε. The total paid source mass, equal for P and Q, is

    1−s/3 = 7/8−ε = C2.

Thus buying S on every paid observation is lawful with both costs exact. Each terminal signed support contribution

    d(c,u,z)=Σ_w x_wc (P(w,u,z)−kQ(w,u,z))

is AFFINE in ε. The six listed atoms are nonnegative and every other atom is nonpositive at BOTH endpoints ε=0 and 3/128. Therefore the same acceptance mask is optimal throughout the REAL interval. Their six contributions sum at ε=0 to 919/8256 and have sum slope −49/860. It follows exactly that

    HYε=919/8256−(49/860)ε.

No terminal mixing is required for Yε beyond the explicit first-stage Bernoulli/multinomial choices.

## Universal dual upper bound

For an arbitrary lawful first-stage policy x=(x_wc), let

    q_cu=(1/3) Σ_w x_wc t(w,u)   (source-identical paid marginal),
    d_cuz=Σ_w x_wc(P(w,u,z)−kQ(w,u,z)),
    Φ_cu=Σ_z max(0,d_cuz).

An observation that skips S has identical P and Q probabilities, so because k>1, accepting there cannot improve H. If the S-buy probability on (c,u) is r_cu∈[0,1], then

    H ≤ Σ_cu r_cu Φ_cu,        Σ_cu r_cu q_cu = C2.

For any nonnegative λ,

    H ≤ Fλ(x,ε)
      := λ C2 + Σ_cu max(0,Φ_cu−λ q_cu).

This is a valid bound for every lawfully randomized future policy, not an assertion that an independently optimized future mask itself satisfies the budget. Fix λ=49/860. For fixed ε, Fλ is a convex function of x because every d and q is linear in x and the positive-part and maxima preserve convexity.

Let b=Σ_wc∈{B0,B1} x_wc. The first-stage cost gives s=5/16+b, while capacity to purchase S at exact cost C2 requires

    0≤b≤Bε := 1/16+3ε.

For ε≤3/128 we have 5/16+2Bε≤37/64<1, so no history-row A probability capacity is exhausted by placing all the STOP and B mass in the same row. Every feasible first-stage x is a convex combination of the following 288 INDEXED templates (168 DISTINCT templates at each endpoint):

    b∈{0,Bε};
    put all STOP mass s=5/16+b in one history i∈{0,1,2};
    put all B mass b in one history j and choose B label bl∈{0,1};
    choose one A label independently for each of the three histories;
    fill its A probability with the row's remaining mass.

To justify completeness rather than merely assume it, normalize the actual STOP distribution across histories, the B-label distribution when b>0, and each row's conditional A-label distribution. Their product mixture produces the original action probabilities at fixed b. Since all templates are affine in b, a further mixture of b=0 and b=Bε, with weights 1−b/Bε and b/Bε, preserves those averages. The b=0 B-label choice can be arbitrary. The uniform slack ensures every template is lawful. Thus the convex hull statement and the 288 indexed family are exact.

For each fixed indexed template v(ε), every x coordinate, every q_cu and every d_cuz is affine in ε (η is FIXED at 3/10). Hence Fλ(v(ε),ε) is convex in ε: it is an affine term λ C2 plus a sum of pointwise maxima of affine functions. The proposed target

    h(ε)=919/8256−(49/860) ε

is affine. Accordingly it suffices to verify for EACH indexed template only

    Fλ(v(0),0)≤h(0),
    Fλ(v(3/128),3/128)≤h(3/128).

The fully specified independent exact-rational programs perform the endpoint checks: each has 288 indexed / 168 distinct vertices, 336 distinct endpoint inequalities and 576 indexed checks in total; both endpoint maxima equal the target, namely

    ε=0:       max Fλ = 919/8256,
    ε=3/128:   max Fλ = 36319/330240.

For any real ε between endpoints, convexity puts each template's value below its affine endpoint chord, and that chord is at most h(ε). A second application of convexity in x proves H≤h(ε) for ALL real lawful behavioral strategies. The lawful Yε attains it, completing the theorem.

## Proof that fixed X is strictly suboptimal

The prior prefix X is

    w=0: A0 with probability 1,
    w=1: A1 with probability 1,
    w=2: A0 with 9/16, B0 with 1/16, STOP with 3/8.

It has paid mass 7/8. With fixed X, the positive-support-per-unit-S-cost ratios Φ_cu/q_cu on its six nonzero paid observations are

    (A0,0): 179/2236; (A0,1): 396/3139;
    (A1,0),(A1,1),(B0,0),(B0,1): 27/172.

The uniquely smallest ratio is 179/2236 on (A0,0), which has paid mass 13/60. For any 0≤ε≤3/128<13/60, reduce S purchases only at that observation by using fresh-coin probability 1−ε/(13/60), and buy S everywhere else. The fractional-knapsack exchange argument shows this is the BEST possible support among all lawful continuations of the fixed prefix X: any other skipped observation loses more H per saved unit of C2. Therefore

    HX=919/8256−(179/2236)ε.

Since 179/2236−49/860=3/130, Yε improves X by exactly 3ε/130. At the lower endpoint, the gap is 9/16640.

## Evidence, model boundary and status

The complete code VERIFY.js uses reduced JavaScript BigInt rationals; EXACT_BIGINT_REPORT.json is its actual output. An independent Python 3 standard-library Fraction checker was executed in the same research run, with matching endpoint maxima and primal/ratio checks. No sampling, floating point or hidden external oracle is used. The all-real extension is analytic convexity PLUS finite exhaustive endpoint enumeration; neither finite numerical sampling alone nor a claim of Lean formalization is used.

This is an auxiliary POSITIVE probabilistic BRC observer, with explicit provenance erasure. The theorem is NOT a result about cancellation in signed/phase BRC, the native six-dimensional X6 torsor, its three-dimensional slice, or heartbeat physical time. Such transfer needs a typed observer-preservation/fiber theorem with composition scope. P000 and the ACTIVE worldview remain untouched.

Author-side classification: AUTHOR_PROVED / TWO_EXACT_RATIONAL_CHECKERS_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED. Formal native task authority, independent Driver review and Foundation admission have not been established.
