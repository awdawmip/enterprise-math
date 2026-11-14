# Frozen R5: 15 effective cuts, sextic mean and unique inflection

Date 2026-11-14. Evidence status: author-side exact finite result; NOT_REVIEWED. Frozen input: awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551. Predecessors: Draft PR #2359 at bb93147a53f9d046bd74fd4daa683847ff717a42, pivotality certificate; Draft PR #2353 at ba53c76f26fb03ee1ffc50de2b4bf77e3ab4e0f6, full center-count distribution. Scope: derived one-dimensional integer-event radius-2 observer, not native X6 or the original 2,520-byte/28-coordinate/8,192-query benchmark.

## Theorem 1: exact global 15-cut reduction

There are 954 strictly increasing integer event boundaries and 28 distinguished length-3 gaps. For a subset C of cuts shortened from 3 to 2, D(C) is the minimum number of event-coordinate centers covering all event boundaries within radius 2.

The preceding bridge theorem establishes that for every cut i and all C avoiding i, delta_i(C)=D(C)-D(C union {i}) belongs to {0,1}. Its complete exact integer first-moment transfer provides each pivotal count P_i=sum_C delta_i(C).

**Zero-pivotal lemma.** If P_i=0, then delta_i(C)=0 for every C: the sum of 2^27 nonnegative integer terms can vanish only if every term vanishes. In particular, zero *average* influence here implies global irrelevance due to this proved monotonicity, not by an unsupported average-to-pointwise inference.

The 13 indices with P_i=0 in the pinned PR #2359 certificate are:

    I = [0,1,7,14,15,17,18,19,20,21,22,23,24].

The remaining 15 are:

    A = [2,3,4,5,6,8,9,10,11,12,13,16,25,26,27].

Eliminating the 13 inert bits successively gives, for **every** 28-cut C,

    D(C) = D(C intersect A).

Hence the 28-bit center-count set function factors through a 15-bit one. Each effective configuration has exactly 2^13=8,192 original preimages with equal *optimal center count*. Translated coordinates and actual optimal witness sets need not coincide.

## Theorem 2: direct 32,768-case census and exact sextic Bernoulli mean

The accompanying standard-library Python verifier reconstructs all 15 original frozen atoms via integer Gray-code updates and exact rational activation thresholds. It reproduces 954 boundaries and 28 cuts, then explicitly translates and greedily solves the radius-2 minimum center-cover problem for all 2^15=32,768 active-cut configurations. It does not use the prior 28-cut histogram to generate its observations.

For the seven possible D values, exact direct active-configuration multiplicities are:

| D | Effective configurations | Expanded 28-cut configurations |
|---:|---:|---:|
| 207 | 28 | 229376 |
| 208 | 624 | 5111808 |
| 209 | 4413 | 36151296 |
| 210 | 11462 | 93896704 |
| 211 | 11404 | 93421568 |
| 212 | 4298 | 35209216 |
| 213 | 539 | 4415488 |
| Total | 32768 | 268435456 |

Every expanded count agrees with the earlier complete transfer histogram. The full 28-bit inference relies on the predecessor's exact all-background P_i=0 certificate, while the new 15-bit direct run independently validates the reduced function and its census.

The greedy covering method is optimal: for the leftmost uncovered point x, select the rightmost candidate center not exceeding x+2. Every feasible cover has a center within two units of x. Replacing that center by the rightmost eligible candidate cannot reduce coverage of any point at or to the right of x; by induction the greedy selection uses the minimum number of centers.

Close each original cut independently with probability p in [0,1]. The 13 inert bits may be removed. Write M_q for the sum of D over effective configurations with exactly q cuts closed. The directly enumerated values for q=0,...,15 are:

    M = [213,3190,22296,96470,288970,634752,1056246,1355811,
         1353501,1050834,629296,285456,94940,21856,3114,207].

The exact Bernstein-form expectation is F(p)=sum(q=0..15) M_q p^q (1-p)^(15-q). Expanding with integer binomial coefficients yields the identity, for **every real p in [0,1]**,

    F(p) = 213 - 5p + p^2 - 3p^3 + 3p^4 - 3p^5 + p^6.

All nine coefficients of degrees 7 through 15 cancel exactly. The verifier checks every coefficient. This recovers F(0)=213, F(1/2)=13471/64 and F(1)=207. It also gives the complete aggregate influence polynomial

    sum_i Prob_p(i pivotal)
       = -F'(p) = 5 - 2p + 9p^2 - 12p^3 + 15p^4 - 6p^5.

This is a finite-model polynomial identity, not an empirical fit or an independence claim about individual pivotal events.

## Theorem 3: exactly one curvature transition

Differentiate the sextic:

    F''(p) = 2 Q(p),
    Q(p) = 1 - 9p + 18p^2 - 30p^3 + 15p^4.

The substitution t=p/(1-p) bijects (0,1) and (0,+infinity), with

    (1+t)^4 Q(t/(1+t)) = G(t)
                            = 1 - 5t - 3t^2 - 17t^3 - 5t^4.

For every t>=0,

    G'(t) = -5 - 6t - 51t^2 - 20t^3 < 0.

Since G(0)=1 and G(t) tends to negative infinity, it has exactly one zero for t>0. The denominator (1+t)^4 is strictly positive; therefore F'' has exactly one zero p_* in (0,1). The curve is strictly convex for p<p_* and strictly concave for p>p_*.

Exact rational substitution shows Q(142932/1000000)>0 and Q(142933/1000000)<0, so

    0.142932 < p_* < 0.142933
    p_* approximately 0.142932616061798.

This sharpens the prior existence-only curvature claim to a unique threshold and global sign classification.

## Verification, scope, next research

Executed an equivalent local standalone Python program with exact rational arithmetic and full enumeration of all 32,768 effective-cut configurations: PASS_EXACT_R5_EFFECTIVE15_AND_UNIQUE_INFLECTION. The adjacent VERIFY_R5_EFFECTIVE15_CURVATURE.py and EXACT_OUTPUT.json contain the reproducible algorithm and full numeric certificate. Exact integer algebra verifies the expectation coefficients; the root bound follows from exact rational signs plus the monotonicity proof. Published code readback and an independent rerun remain distinct from this author's local equivalent run.

Next: derive a structural low-order decomposition explaining the degree-six cancellation beyond its exact algebraic verification, and extend the finite interval transfer to fixed-budget-K nearest-center total correction cost with optimal-center witnesses. Original native 2,520-byte seed / 28-coordinate / 8,192-prefix-query benchmark is independently unfinished. No formal Task CLAIM, independent mathematical review, admitted Result or P000 promotion is asserted.
